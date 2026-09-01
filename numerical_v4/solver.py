"""Outer cutoff best-response map T(k), damped iteration, seeded multi-start.

Design section 7, build step 8.  ``numerical/solver.py``'s architecture
transfers directly: grid-scan for sign changes, brentq on the bracket *nearest
the current iterate* (that is the branch-continuity device), damped update
alpha = 0.75, warm start, multi-start fallback -- generalised from three named
actions to J - 1 adjacent-plan indifferences.

P1 tolerances (design section 13, ruling 4): both scales are reported plus the
local slope of the payoff gap, and the *binding verdict criterion is the
payoff-scale one* -- no adjacent-plan deviation above 1e-9.  The cutoff-scale
1e-10 is diagnostic only.
"""

from __future__ import annotations

from typing import Callable, NamedTuple, Optional, Sequence

import numpy as np
from scipy.optimize import brentq

from numerical_v4.menu import atoms
from numerical_v4.params import EXIT, HOLD, VOICE, ParamsV4
from numerical_v4.policy import Policy, menu_of, plan_payoff
from numerical_v4.pooled import PooledResult, pooled_pass

TOL_CUTOFF: float = 1e-10       # P1 diagnostic scale
TOL_PAYOFF: float = 1e-9        # P1 binding scale
ALPHA: float = 0.75             # damping
N_GRID: int = 241               # bracket grid.  Finer than v3's 61: U_Voice(s)
#                                 steps down at every n(s) decrement (faster
#                                 accumulation costs more in price impact), and
#                                 a bracket wider than an n-plateau lets brentq
#                                 converge on the jump instead of the root.
DEV_OFFSETS: tuple[float, ...] = (1e-2, 1e-3, 1e-4, 1e-5, 1e-6)


class Residual(NamedTuple):
    """Both P1 scales plus the local slope that relates them."""

    cutoff_scale: float          # |k - T(k)|_inf
    payoff_scale: float          # max profitable adjacent-plan deviation
    slopes: tuple[float, ...]    # d(U_j - U_{j+1})/ds at each cutoff
    binding: str = "payoff"


def _payoffs(res: PooledResult, s: float, p: ParamsV4) -> dict[int, float]:
    return {j: plan_payoff(j, s, res, p) for j in (EXIT, HOLD, VOICE)}


def _bracket_root(func: Callable[[float], float], grid: np.ndarray,
                  low: Optional[float] = None, high: Optional[float] = None,
                  target: Optional[float] = None):
    """Sign-change bracket nearest the current iterate (verbatim from v3)."""
    g = grid
    if low is not None:
        g = g[g >= low]
    if high is not None:
        g = g[g <= high]
    if len(g) < 2:
        return None
    vals = np.array([func(float(s)) for s in g], dtype=float)
    if np.any(np.isnan(vals)):
        return None
    brackets: list[tuple[float, float]] = []
    for i in range(len(g) - 1):
        if vals[i] == 0.0:
            brackets.append((float(g[i]), float(g[i])))
        elif vals[i] * vals[i + 1] < 0.0:
            brackets.append((float(g[i]), float(g[i + 1])))
    if not brackets:
        return None
    if target is None or not np.isfinite(target):
        return brackets[0]
    return min(brackets, key=lambda ab: abs(0.5 * (ab[0] + ab[1]) - float(target)))


def outer_map(k: tuple[float, float], p: ParamsV4,
              res: Optional[PooledResult] = None) -> tuple[float, float]:
    """T(k): the adjacent-plan indifference cutoffs at the prices implied by k."""
    if res is None:
        res = pooled_pass(atoms(k, p), p, with_runup=True)
    grid = np.linspace(p.s_lo, p.s_hi, N_GRID)

    def gap_EH(s: float) -> float:
        u = _payoffs(res, s, p)
        return u[EXIT] - u[HOLD]

    def gap_HV(s: float) -> float:
        u = _payoffs(res, s, p)
        return u[HOLD] - u[VOICE]

    br = _bracket_root(gap_EH, grid, target=k[0])
    if br is None:
        k1 = p.s_hi if gap_EH(p.s_lo) >= 0.0 else p.s_lo
    else:
        k1 = br[0] if br[0] == br[1] else float(brentq(gap_EH, br[0], br[1]))

    br = _bracket_root(gap_HV, grid, low=k1, high=p.s_hi, target=k[1])
    if br is None:
        k2 = k1 if gap_HV(min(k1 + 1e-4, p.s_hi)) <= 0.0 else p.s_hi
    else:
        k2 = br[0] if br[0] == br[1] else float(brentq(gap_HV, br[0], br[1]))

    return (float(k1), float(max(k2, k1)))


def equilibrium_residual(k: tuple[float, float], p: ParamsV4,
                         res: Optional[PooledResult] = None) -> Residual:
    """Cutoff-scale and payoff-scale residuals, plus the local gap slopes."""
    if res is None:
        res = pooled_pass(atoms(k, p), p, with_runup=True)
    Tk = outer_map(k, p, res)
    cutoff = float(max(abs(Tk[0] - k[0]), abs(Tk[1] - k[1])))

    # Payoff scale: no profitable adjacent-plan deviation anywhere on the grid.
    # The grid carries points hugging each cutoff -- that is where a residual
    # cutoff error of order 1e-9 can actually show up as a payoff gain.
    dev_grid = list(np.linspace(p.s_lo, p.s_hi, N_GRID))
    for cut in k:
        for off in DEV_OFFSETS:
            dev_grid += [cut - off, cut + off]
    worst = 0.0
    for s in dev_grid:
        s = float(s)
        if not (p.s_lo <= s <= p.s_hi):
            continue
        u = _payoffs(res, s, p)
        chosen = EXIT if s < k[0] else (HOLD if s < k[1] else VOICE)
        for alt in (chosen - 1, chosen + 1):
            if alt in u:
                worst = max(worst, u[alt] - u[chosen])

    eps = 1e-5
    slopes = []
    for cut, (a, b) in zip(k, ((EXIT, HOLD), (HOLD, VOICE))):
        hi = _payoffs(res, cut + eps, p)
        lo = _payoffs(res, cut - eps, p)
        slopes.append(((hi[a] - hi[b]) - (lo[a] - lo[b])) / (2.0 * eps))
    return Residual(cutoff, float(worst), tuple(slopes))


def solve_policy(p: ParamsV4, seed: int = 0,
                 k_init: Optional[tuple[float, float]] = None,
                 max_iter: int = 60, tol: float = TOL_CUTOFF,
                 verbose: bool = False) -> tuple[Policy, Residual]:
    """Damped fixed-point iteration on the ordered polytope Theta."""
    rng = np.random.default_rng(seed)
    if k_init is None:
        jitter = rng.normal(0.0, 0.15, size=2) if seed else np.zeros(2)
        k = (p.mu_v - 0.5 * p.sigma_s + jitter[0],
             p.mu_v + 0.5 * p.sigma_s + jitter[1])
    else:
        k = k_init
    k = (float(k[0]), float(max(k[1], k[0])))

    res = None
    for it in range(max_iter):
        res = pooled_pass(atoms(k, p), p, with_runup=True)
        Tk = outer_map(k, p, res)
        step = max(abs(Tk[0] - k[0]), abs(Tk[1] - k[1]))
        if verbose:
            print(f"    iter {it:2d}  k = ({k[0]:.8f}, {k[1]:.8f})  "
                  f"|k-T(k)| = {step:.3e}", flush=True)
        if step < tol:
            k = Tk
            break
        k = (ALPHA * Tk[0] + (1 - ALPHA) * k[0],
             ALPHA * Tk[1] + (1 - ALPHA) * k[1])
        k = (k[0], max(k[1], k[0]))

    res = pooled_pass(atoms(k, p), p, with_runup=True)
    return Policy(tuple(k), menu_of(p)), equilibrium_residual(k, p, res)


def solve_valid(p: ParamsV4, seeds: Sequence[int] = (0, 1, 2),
                k_init: Optional[tuple[float, float]] = None,
                tol: float = TOL_PAYOFF) -> tuple[Policy, Residual]:
    """Seeded multi-start; returns the best payoff-scale residual found.

    P1 asks for 30 seeds; that is the check script's grid, not the smoke run's.
    """
    best: Optional[tuple[Policy, Residual]] = None
    for sd in seeds:
        pol, r = solve_policy(p, seed=sd, k_init=k_init if sd == 0 else None)
        if best is None or r.payoff_scale < best[1].payoff_scale:
            best = (pol, r)
        if r.payoff_scale < tol:
            break
    assert best is not None
    return best


def equilibrium_sweep(p: ParamsV4, kappas: Sequence[float],
                      with_runup: bool = False):
    """Policy re-solved at each kappa (the thin wrapper policy.py cannot hold)."""
    from numerical_v4.policy import equilibrium_sweep as _sweep

    return _sweep(p, kappas, lambda pk: solve_policy(pk), with_runup)
