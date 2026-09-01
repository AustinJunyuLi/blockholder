"""Control-outcome objects: pi, h, Omega, omega_a, M_F, M_P, Delta^act, S_P.

Design sections 6 and 8, build steps 3 and 6.

Omega and omega_a are deterministic in (j, s) -- D does not depend on the noise
at all -- so they need no enumeration and land before any history is priced
(build step 3).  M_P is the only object that runs through the 4.19M-history
pooled cell.

Units follow the card's calibration card: the functions here return *natural*
units (fractions, premia in value units).  Conversion to percent / premium
percentage points / basis points happens at the print boundary in smoke.py.
"""

from __future__ import annotations

from typing import Callable, NamedTuple

import numpy as np

from numerical_v4.menu import Atom
from numerical_v4.params import ParamsV4, TOL_PROB
from numerical_v4.pooled import PooledResult, inner_price

MIN_CELL_MASS: float = 0.01     # design risk 9.3 / D1's request


# ---------------------------------------------------------------------------
# Cell weights -- no enumeration needed (build step 3)
# ---------------------------------------------------------------------------


class CellWeights(NamedTuple):
    Omega: float        # Pr(D = 1)
    Pr_a: float         # Pr(a = 1)
    omega_a: float      # Pr(D = 1 | a = 1), the calibration target
    pi_bar: float       # Pr(a = 1 | D = 0), the pooled engagement share
    degenerate: tuple[str, ...]


def cell_weights(atom_list: list[Atom]) -> CellWeights:
    """Omega, Pr(a=1), omega_a and pi_bar straight off the s-partition."""
    w = np.array([a.w for a in atom_list])
    D = np.array([a.D for a in atom_list], dtype=float)
    a_ = np.array([a.a for a in atom_list], dtype=float)
    tot = float(w.sum())
    Omega = float((w * D).sum() / tot)
    Pr_a = float((w * a_).sum() / tot)
    omega_a = Omega / Pr_a if Pr_a > TOL_PROB else float("nan")
    nd = float((w * (1.0 - D)).sum() / tot)
    pi_bar = float((w * a_ * (1.0 - D)).sum() / tot / nd) if nd > TOL_PROB \
        else float("nan")

    bad: list[str] = []
    if Omega < MIN_CELL_MASS:
        bad.append(f"flagged cell mass {Omega:.4g} < {MIN_CELL_MASS}")
    if 1.0 - Omega < MIN_CELL_MASS:
        bad.append(f"pooled cell mass {1.0 - Omega:.4g} < {MIN_CELL_MASS}")
    return CellWeights(Omega, Pr_a, omega_a, pi_bar, tuple(bad))


# ---------------------------------------------------------------------------
# Pooled-cell premium
# ---------------------------------------------------------------------------


def pooled_premium(res: PooledResult, Omega: float, p: ParamsV4) -> float:
    """M_P = Delta_m * E[h | D = 0], h = pi*p, over the enumerated cell.

    ``res.mass[H]`` already carries only the atoms alive at H, i.e. exactly the
    D = 0 atoms, so its total is 1 - Omega and no extra conditioning is needed.
    """
    H = max(res.dates)
    mass = res.mass[H]
    live = mass > 0.0
    h = res.pi[H][live] * res.p_bid[H][live]
    denom = float(mass[live].sum())
    if denom <= TOL_PROB:
        return float("nan")
    return float(p.Delta_m * np.dot(mass[live], h) / denom)


def pooled_cell_mass(res: PooledResult) -> float:
    """Total enumerated mass at the control node; must equal 1 - Omega."""
    H = max(res.dates)
    return float(res.mass[H].sum())


def total_premium(res: PooledResult, flagged_w: np.ndarray,
                  flagged_p: np.ndarray, p: ParamsV4) -> float:
    """Delta^act = Delta_m * E[h] over the *whole* population, summed directly.

    Computed independently of L1's decomposition so that
    ``decomposition_residual`` is a real subtraction rather than 0 - 0.  It is
    still a wiring check (design section 0): both sides run through the same
    enumeration.
    """
    H = max(res.dates)
    mass = res.mass[H]
    live = mass > 0.0
    pooled = float(np.dot(mass[live], res.pi[H][live] * res.p_bid[H][live]))
    flag = float(np.dot(flagged_w, flagged_p))     # pi = 1 on the flagged cell
    denom = float(mass[live].sum() + flagged_w.sum())
    if denom <= TOL_PROB:
        return float("nan")
    return float(p.Delta_m * (pooled + flag) / denom)


def decomposition_residual(Delta_act: float, Omega: float, M_F: float,
                           M_P: float) -> float:
    """L1: |Delta^act - (Omega*M_F + (1-Omega)*M_P)|.

    This is a wiring check (design section 0): both sides run through the same
    enumeration, so the residual is machine noise by construction.  It must not
    be quoted as evidence for L1.
    """
    return abs(Delta_act - (Omega * M_F + (1.0 - Omega) * M_P))


# ---------------------------------------------------------------------------
# Liquidity sensitivities (design section 7)
# ---------------------------------------------------------------------------


DERIV_STEP: float = 1e-3


def d_dkappa(fn: Callable[[float], float], kappa: float,
             h: float = DERIV_STEP) -> float:
    """4th-order central difference; truncation O(h^4) ~ 1e-12 at h = 1e-3.

    Roundoff is ~eps/h ~ 2e-13, so both sit two orders inside the 1e-10 targets.
    """
    f1 = fn(kappa + h)
    f2 = fn(kappa - h)
    f3 = fn(kappa + 2.0 * h)
    f4 = fn(kappa - 2.0 * h)
    return float((8.0 * (f1 - f2) - (f3 - f4)) / (12.0 * h))


# ---------------------------------------------------------------------------
# Section 8: the standalone chord
# ---------------------------------------------------------------------------


def h_kernel(pi: float | np.ndarray, v_hat: float, p: ParamsV4) -> np.ndarray:
    """h(I) = pi(I) * p(I) with p at the inner fixed point (card section 4.4)."""
    pi_a = np.atleast_1d(np.asarray(pi, dtype=float))
    sol = inner_price(np.full_like(pi_a, v_hat), pi_a, p)
    return pi_a * sol.p_bid


class Chord(NamedTuple):
    pi_bar: float
    C_h: float
    h0: float
    h_half: float
    h1: float
    cancellation_headroom: float   # eps*max|h| against |C_h|
    quadratic_ratio: float         # |C_h| / pi_bar^2


def chord(pi_bar: float, v_hat: float, p: ParamsV4) -> Chord:
    """C_h(pi_bar) = h(0) - 2h(pi_bar/2) + h(pi_bar), evaluated directly.

    Design section 8 splits L3: for pi_bar >= 1e-2 the enumeration resolves the
    comparison; below that this standalone route is used, with the relative
    criterion |residual|/|C_h| < 1e-6 (design section 13, ruling 5).
    """
    vals = h_kernel(np.array([0.0, pi_bar / 2.0, pi_bar]), v_hat, p)
    C = float(vals[0] - 2.0 * vals[1] + vals[2])
    head = float(np.finfo(float).eps * np.max(np.abs(vals)))
    return Chord(pi_bar, C, float(vals[0]), float(vals[1]), float(vals[2]),
                 head, abs(C) / pi_bar**2 if pi_bar > 0 else float("nan"))
