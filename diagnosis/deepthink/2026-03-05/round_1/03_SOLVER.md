# Solver

## evt_codebase/numerical/solver.py

```python
"""Equilibrium solver for the numerical exercise.

We solve for a monotone-cutoff equilibrium (k1, k0, kD) via damped fixed-point
iteration:

1. Start with a cutoff guess.
2. Compute implied equilibrium objects (prices/posteriors) under that guess.
3. Compute best-response cutoffs from indifference conditions using Brent roots.
4. Damp-update and iterate.

This approach matches the constructive existence argument and avoids any
recursive pricing loops because pricing is feed-forward.
"""

from __future__ import annotations

import warnings
from typing import Callable, Optional, Tuple

import numpy as np
from scipy.optimize import brentq

from .params import (
    Action,
    Cutoffs,
    ModelParams,
    SIGMA_GRID,
    TOL_CONVERGE,
    TOL_REGION,
    TOL_RESIDUAL,
)
from .model import (
    compute_equilibrium_objects,
    compute_expected_payoff,
    compute_minority_gains,
    compute_minority_gains_no_disclosure_given_strategy,
)


def equilibrium_residual(k1: float, k0: float, kD: float, params: ModelParams) -> float:
    """Maximum absolute indifference residual across the three cutoff conditions."""
    eq = compute_equilibrium_objects(k1, k0, kD, params)

    def U(act: Action, s: float) -> float:
        return compute_expected_payoff(act, float(s), eq, params)

    s_min = params.mu - SIGMA_GRID * params.sigma_s
    s_max = params.mu + SIGMA_GRID * params.sigma_s

    # k1 condition: EXIT vs best of {HOLD, QUIET}
    diff1 = U(Action.EXIT, k1) - max(U(Action.HOLD, k1), U(Action.QUIET, k1))
    if k1 <= s_min + TOL_REGION or k1 >= s_max - TOL_REGION:
        # boundary: only penalize violations of corner behavior
        r1 = max(0.0, -diff1) if k1 >= s_max - TOL_REGION else max(0.0, diff1)
    else:
        r1 = abs(diff1)

    # k0 condition: HOLD vs QUIET (if region exists)
    if (k0 - k1) > TOL_REGION:
        r0 = abs(U(Action.HOLD, k0) - U(Action.QUIET, k0))
    else:
        # hold region collapsed: require QUIET weakly dominates HOLD just above k1
        s_test = min(k1 + TOL_REGION, s_max)
        r0 = max(0.0, U(Action.HOLD, s_test) - U(Action.QUIET, s_test))

    # kD condition: boundary between PUBLIC and the best nondisclosed action.
    # This formulation is robust to region collapse (e.g., kD=k0 so Quiet Voice is empty).
    def U_lower(s: float) -> float:
        return max(U(Action.HOLD, s), U(Action.QUIET, s))

    if kD >= s_max - TOL_REGION:
        # no public region: require PUBLIC does not dominate at upper bound
        rD = max(0.0, U(Action.PUBLIC, s_max) - U_lower(s_max))
    elif (kD - k0) < TOL_REGION:
        # quiet region collapsed: only penalize if the lower action dominates PUBLIC above k0
        s_test = min(k0 + TOL_REGION, s_max)
        rD = max(0.0, U_lower(s_test) - U(Action.PUBLIC, s_test))
    else:
        rD = abs(U_lower(kD) - U(Action.PUBLIC, kD))

    return float(max(r1, r0, rD))


def _bracket_root(
    func: Callable[[float], float],
    grid: np.ndarray,
    low: Optional[float] = None,
    high: Optional[float] = None,
) -> Optional[Tuple[float, float]]:
    """Find the *first* sign-change bracket on a (possibly truncated) grid.

    We deliberately return the **first** bracket (lowest-s root). This matches
    the legacy implementation and avoids accidentally selecting a higher root
    when the payoff-difference function has multiple crossings.

    Robustness detail: if `low`/`high` are provided, we *include* those
    endpoints in the search grid to avoid missing a root that lies between the
    endpoint and the first interior grid point.
    """

    g = np.array(grid, dtype=float)
    if low is not None:
        g = g[g >= low]
        g = np.concatenate(([float(low)], g))
    if high is not None:
        g = g[g <= high]
        g = np.concatenate((g, [float(high)]))

    g = np.unique(g)
    g = np.sort(g)

    if g.size < 2:
        return None

    vals = np.array([func(float(x)) for x in g], dtype=float)
    if np.any(~np.isfinite(vals)):
        return None

    for i in range(len(g) - 1):
        if vals[i] * vals[i + 1] <= 0.0:
            return float(g[i]), float(g[i + 1])

    return None


def solve_equilibrium(
    params: ModelParams,
    k1_init: Optional[float] = None,
    k0_init: Optional[float] = None,
    kD_init: Optional[float] = None,
    max_iter: int = 80,
    tol: float = TOL_CONVERGE,
) -> Cutoffs:
    """Solve for equilibrium cutoffs (k1,k0,kD) for given parameters."""

    # Initial guesses
    k1 = params.mu - 1.0 * params.sigma_s if k1_init is None else float(k1_init)
    k0 = params.mu - 0.5 * params.sigma_s if k0_init is None else float(k0_init)
    kD = params.mu + 0.5 * params.sigma_s if kD_init is None else float(kD_init)

    s_min = params.mu - SIGMA_GRID * params.sigma_s
    s_max = params.mu + SIGMA_GRID * params.sigma_s
    s_grid = np.linspace(s_min, s_max, 61)

    for _it in range(max_iter):
        # enforce ordering
        k0 = max(k0, k1)
        kD = max(kD, k0)

        eq = compute_equilibrium_objects(k1, k0, kD, params)

        def U(act: Action, s: float) -> float:
            return compute_expected_payoff(act, float(s), eq, params)

        # ------------------------------------------------------------------
        # 1) k1: EXIT vs best of {HOLD, QUIET}
        # ------------------------------------------------------------------
        def diff_exit_best(s: float) -> float:
            return U(Action.EXIT, s) - max(U(Action.HOLD, s), U(Action.QUIET, s))

        br = _bracket_root(diff_exit_best, s_grid)
        if br is None:
            # corner
            k1_new = s_max if diff_exit_best(s_min) >= 0.0 else s_min
        else:
            a, b = br
            k1_new = a if a == b else float(brentq(diff_exit_best, a, b))

        # ------------------------------------------------------------------
        # 2) k0: HOLD vs QUIET above k1
        # ------------------------------------------------------------------
        def diff_hold_quiet(s: float) -> float:
            return U(Action.HOLD, s) - U(Action.QUIET, s)

        # search on [k1_new, s_max]
        s0 = min(k1_new + 1e-4, s_max)
        br = _bracket_root(diff_hold_quiet, s_grid, low=k1_new, high=s_max)
        if br is None:
            # if QUIET dominates immediately, collapse HOLD region
            k0_new = k1_new if diff_hold_quiet(s0) <= 0.0 else s_max
        else:
            a, b = br
            k0_new = a if a == b else float(brentq(diff_hold_quiet, a, b))

        k0_new = max(k0_new, k1_new)

        # ------------------------------------------------------------------
        # 3) kD: boundary between PUBLIC and the best nondisclosed action
        # ------------------------------------------------------------------
        def diff_lower_public(s: float) -> float:
            return max(U(Action.HOLD, s), U(Action.QUIET, s)) - U(Action.PUBLIC, s)

        start = min(k0_new, s_max)
        br = _bracket_root(diff_lower_public, s_grid, low=start, high=s_max)
        if br is None:
            # if PUBLIC dominates immediately, collapse quiet region
            kD_new = start if diff_lower_public(min(start + 1e-4, s_max)) <= 0.0 else s_max
        else:
            a, b = br
            kD_new = a if a == b else float(brentq(diff_lower_public, a, b))

        kD_new = max(kD_new, k0_new)

        # ------------------------------------------------------------------
        # Convergence check
        # ------------------------------------------------------------------
        if (abs(k1_new - k1) < tol) and (abs(k0_new - k0) < tol) and (abs(kD_new - kD) < tol):
            return Cutoffs(float(k1_new), float(k0_new), float(kD_new))

        # Damped update
        alpha = 0.75
        k1 = alpha * k1_new + (1.0 - alpha) * k1
        k0 = alpha * k0_new + (1.0 - alpha) * k0
        kD = alpha * kD_new + (1.0 - alpha) * kD

    return Cutoffs(float(k1), float(k0), float(kD))


def solve_valid(params: ModelParams, prev_cutoffs: Optional[Cutoffs] = None, residual_tol: float = TOL_RESIDUAL) -> Tuple[Optional[Cutoffs], float]:
    """Solve equilibrium with warm start + fallback starts.

    Returns (cutoffs, residual). If residual is too high, caller may treat as
    non-converged.
    """

    def attempt(start: Tuple[float, float, float]) -> Tuple[Cutoffs, float]:
        cut = solve_equilibrium(params, k1_init=start[0], k0_init=start[1], kD_init=start[2], max_iter=120)
        res = equilibrium_residual(cut.k1, cut.k0, cut.kD, params)
        return cut, res

    # Warm start from previous kappa
    if prev_cutoffs is not None:
        cut, res = attempt((prev_cutoffs.k1, prev_cutoffs.k0, prev_cutoffs.kD))
        if np.isfinite(res) and res <= residual_tol:
            return cut, float(res)

        # Fallback: collapsed HOLD
        cut2, res2 = attempt((prev_cutoffs.k1, prev_cutoffs.k1, prev_cutoffs.kD))
        if np.isfinite(res2) and res2 < res:
            cut, res = cut2, res2

        # Additional fallback if kD went extreme
        if prev_cutoffs.kD > params.mu + 2.0 * params.sigma_s or res > residual_tol:
            kD_mod = params.mu + 0.5 * params.sigma_s
            cut3, res3 = attempt((prev_cutoffs.k1, params.mu + 0.4 * params.sigma_s, kD_mod))
            if np.isfinite(res3) and res3 < res:
                cut, res = cut3, res3

        return cut, float(res)

    # Cold starts
    starts = [
        (params.mu - 1.0 * params.sigma_s, params.mu - 1.0 * params.sigma_s, params.mu + 0.5 * params.sigma_s),
        (params.mu - 1.0 * params.sigma_s, params.mu - 0.5 * params.sigma_s, params.mu + 0.5 * params.sigma_s),
    ]

    best_cut: Optional[Cutoffs] = None
    best_res = np.inf
    for st in starts:
        cut, res = attempt(st)
        if np.isfinite(res) and res < best_res:
            best_cut, best_res = cut, res

    return best_cut, float(best_res)


def compute_series_over_kappa(
    base_params: ModelParams,
    kappa_values: np.ndarray,
    include_no_disclosure: bool = False,
) -> dict:
    """Compute equilibrium series over a kappa grid.

    Returns numpy arrays for:
        kappa, k1, k0, kD, delta_min, base, act
    and optionally act_no_disclosure.
    """

    k1_vals: List[float] = []
    k0_vals: List[float] = []
    kD_vals: List[float] = []
    delta_vals: List[float] = []
    base_vals: List[float] = []
    act_vals: List[float] = []
    act_nd_vals: List[float] = []

    prev: Optional[Cutoffs] = None

    for kappa in kappa_values:
        try:
            p = base_params.replace(kappa=float(kappa))
            cut, res = solve_valid(p, prev)
            if cut is None or (not np.isfinite(res)) or (res > TOL_RESIDUAL):
                raise RuntimeError(f"no valid equilibrium (residual={res})")
            prev = cut

            gains = compute_minority_gains(cut.k1, cut.k0, cut.kD, p)

            k1_vals.append(cut.k1)
            k0_vals.append(cut.k0)
            kD_vals.append(cut.kD)
            delta_vals.append(gains.total)
            base_vals.append(gains.base)
            act_vals.append(gains.activism)

            if include_no_disclosure:
                nd = compute_minority_gains_no_disclosure_given_strategy(cut.k1, cut.k0, cut.kD, p)
                act_nd_vals.append(nd.activism)

        except Exception as exc:
            warnings.warn(f"Solver failed at kappa={kappa}: {exc}")
            k1_vals.append(np.nan)
            k0_vals.append(np.nan)
            kD_vals.append(np.nan)
            delta_vals.append(np.nan)
            base_vals.append(np.nan)
            act_vals.append(np.nan)
            if include_no_disclosure:
                act_nd_vals.append(np.nan)
            prev = None

    out = {
        "kappa": np.array(kappa_values, dtype=float),
        "k1": np.array(k1_vals, dtype=float),
        "k0": np.array(k0_vals, dtype=float),
        "kD": np.array(kD_vals, dtype=float),
        "delta_min": np.array(delta_vals, dtype=float),
        "base": np.array(base_vals, dtype=float),
        "act": np.array(act_vals, dtype=float),
    }

    if include_no_disclosure:
        out["act_no_disclosure"] = np.array(act_nd_vals, dtype=float)

    return out
```
