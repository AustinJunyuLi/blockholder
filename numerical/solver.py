"""
Equilibrium solver for the Exit-Voice-Takeover model.

This module implements the fixed-point iteration described in Proposition 1
of the paper.  It provides:

- ``equilibrium_residual`` -- residual metric for verifying equilibrium quality
- ``solve_equilibrium``    -- damped fixed-point solver for cutoffs (k1, k0, kD)
- ``solve_valid``          -- multi-start wrapper with collapsed-hold fallback
- ``solve_equilibrium_for_kappa`` -- convenience wrapper for kappa sweeps
- ``compute_series_over_kappa``   -- full series computation over a liquidity grid
"""

from __future__ import annotations

import warnings
from typing import Dict, List, Optional, Tuple

import numpy as np
from scipy.optimize import brentq

from numerical.params import (
    Action,
    Cutoffs,
    MinorityGains,
    ModelParams,
    TOL_CONVERGE,
    TOL_PROB,
    TOL_REGION,
    TOL_RESIDUAL,
)
from numerical.model import (
    compute_action_probabilities,
    compute_equilibrium_prices,
    compute_expected_payoff,
    compute_minority_gains,
    compute_minority_gains_no_disclosure_given_strategy,
    compute_posteriors,
)

try:
    from numerical.accel import solve_equilibrium_fast as _solve_fast
    from numerical.accel import compute_series_over_kappa_fast as _series_fast
    HAS_NUMBA = True
except ImportError:
    HAS_NUMBA = False

# -- Equilibrium Solver --------------------


def equilibrium_residual(
    k1: float, k0: float, kD: float, params: ModelParams
) -> float:
    """Compute maximum indifference residual across the three cutoff conditions.

    The model allows region collapse (e.g., k0 = k1).  In such cases the
    corresponding condition is treated as an inequality and contributes only
    its positive-part violation.

    Parameters
    ----------
    k1, k0, kD : float
        Candidate equilibrium cutoffs.
    params : ModelParams
        Model parameters.

    Returns
    -------
    float
        Maximum absolute indifference residual.
    """
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(
        k1, k0, kD, params
    )
    post = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    prices = compute_equilibrium_prices(k1, k0, kD, params)

    def U(action: Action, s: float) -> float:
        return compute_expected_payoff(action, float(s), prices, post, params)

    s_min = params.mu - 6 * params.sigma_s
    s_max = params.mu + 6 * params.sigma_s

    # -- k1: Exit vs best q=0 option ------------------------------------
    diff1 = U(Action.EXIT, k1) - max(U(Action.HOLD, k1), U(Action.QUIET, k1))
    if k1 <= s_min + TOL_REGION or k1 >= s_max - TOL_REGION:
        r1 = max(0.0, -diff1) if k1 >= s_max - TOL_REGION else max(0.0, diff1)
    else:
        r1 = abs(diff1)

    # -- k0: Hold vs Quiet Voice (only if Hold region is interior) ------
    if (k0 - k1) > TOL_REGION:
        r0 = abs(U(Action.HOLD, k0) - U(Action.QUIET, k0))
    else:
        # Hold region collapsed: require Hold not strictly dominate Quiet
        # Voice just above k1.
        s_test = min(k1 + TOL_REGION, s_max)
        r0 = max(0.0, U(Action.HOLD, s_test) - U(Action.QUIET, s_test))

    # -- kD: (Quiet or Hold) vs Public Voice ----------------------------
    lower = Action.QUIET if k0 < s_max - TOL_REGION else Action.HOLD
    if kD >= s_max - TOL_REGION:
        # Public voice never used: require it not dominate the lower action
        # at the top end.
        rD = max(0.0, U(Action.PUBLIC, s_max) - U(lower, s_max))
    else:
        rD = abs(U(lower, kD) - U(Action.PUBLIC, kD))

    return float(max(r1, r0, rD))


def solve_equilibrium(
    params: ModelParams,
    k1_init: Optional[float] = None,
    k0_init: Optional[float] = None,
    kD_init: Optional[float] = None,
    max_iter: int = 60,
    tol: float = TOL_CONVERGE,
) -> Cutoffs:
    """Solve for equilibrium cutoffs via damped fixed-point iteration -- Proposition 1.

    Parameters
    ----------
    params : ModelParams
        Model parameters.
    k1_init, k0_init, kD_init : float, optional
        Initial guesses.  When *None*, heuristic defaults based on mu and
        sigma_s are used.
    max_iter : int
        Maximum number of fixed-point iterations.
    tol : float
        Convergence tolerance for cutoff updates.

    Returns
    -------
    Cutoffs
        Named tuple ``(k1, k0, kD)``.
    """
    if HAS_NUMBA:
        return _solve_fast(params, k1_init, k0_init, kD_init, max_iter, tol)

    # Initial guesses
    k1 = params.mu - 1.0 * params.sigma_s if k1_init is None else float(k1_init)
    k0 = params.mu - 0.5 * params.sigma_s if k0_init is None else float(k0_init)
    kD = params.mu + 0.5 * params.sigma_s if kD_init is None else float(kD_init)

    s_min = params.mu - 6 * params.sigma_s
    s_max = params.mu + 6 * params.sigma_s
    s_grid = np.linspace(s_min, s_max, 61)

    def bracket_root(
        func,
        low: Optional[float] = None,
        high: Optional[float] = None,
        target: Optional[float] = None,
    ):
        grid = s_grid
        if low is not None:
            grid = grid[grid >= low]
        if high is not None:
            grid = grid[grid <= high]
        if len(grid) < 2:
            return None
        vals = np.array([func(s) for s in grid], dtype=float)
        if np.any(np.isnan(vals)):
            return None
        brackets: List[Tuple[float, float]] = []
        for i in range(len(grid) - 1):
            if vals[i] == 0:
                brackets.append((float(grid[i]), float(grid[i])))
            elif vals[i] * vals[i + 1] < 0:
                brackets.append((float(grid[i]), float(grid[i + 1])))

        if not brackets:
            return None
        if target is None or (not np.isfinite(target)):
            return brackets[0]
        # Prefer the bracket closest to the current iterate to keep the
        # solution branch continuous.
        return min(
            brackets, key=lambda ab: abs(((ab[0] + ab[1]) / 2) - float(target))
        )

    for _iteration in range(max_iter):
        # Ensure weak ordering (allow region collapse)
        k0 = max(k0, k1)
        kD = max(kD, k0)

        # Compute prices and posteriors
        omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(
            k1, k0, kD, params
        )
        posteriors = compute_posteriors(
            omega_E, omega_H, omega_Q, omega_P, params.kappa
        )
        prices = compute_equilibrium_prices(k1, k0, kD, params)

        def U(action: Action, s: float) -> float:
            return compute_expected_payoff(
                action, float(s), prices, posteriors, params
            )

        # k1: Exit vs best q=0 option (Hold or Quiet Voice)
        def diff_E_best0(s: float) -> float:
            return U(Action.EXIT, s) - max(U(Action.HOLD, s), U(Action.QUIET, s))

        bracket = bracket_root(diff_E_best0, target=k1)
        if bracket is None:
            # If exit always dominates on grid, push k1 to upper end;
            # if never, to lower end.
            k1_new = s_max if diff_E_best0(s_min) >= 0 else s_min
        else:
            a, b = bracket
            if a == b:
                k1_new = a
            else:
                k1_new = brentq(diff_E_best0, a, b)

        # k0: Passive Hold vs Quiet Voice (only relevant above k1)
        def diff_H_Q(s: float) -> float:
            return U(Action.HOLD, s) - U(Action.QUIET, s)

        eps = 1e-4
        s0 = min(k1_new + eps, s_max)
        bracket = bracket_root(diff_H_Q, low=k1_new, high=s_max, target=k0)
        if bracket is None:
            # No crossing above the exit boundary: one action dominates.
            k0_new = k1_new if diff_H_Q(s0) <= 0 else s_max
        else:
            a, b = bracket
            if a == b:
                k0_new = a
            else:
                k0_new = brentq(diff_H_Q, a, b)

        # kD: Quiet Voice (or Hold if Quiet Voice absent) vs Public Voice
        # If k0_new is pushed to s_max, Quiet Voice is absent; compare
        # Hold vs Public Voice.
        lower_action = (
            Action.QUIET if k0_new < s_max - 1e-6 else Action.HOLD
        )

        def diff_lower_P(s: float) -> float:
            return U(lower_action, s) - U(Action.PUBLIC, s)

        start = min(k0_new, s_max)
        bracket = bracket_root(diff_lower_P, low=start, high=s_max, target=kD)
        if bracket is None:
            # No crossing: either Public Voice dominates immediately
            # (collapse) or is never optimal.
            kD_new = start if diff_lower_P(start + eps) <= 0 else s_max
        else:
            a, b = bracket
            if a == b:
                kD_new = a
            else:
                kD_new = brentq(diff_lower_P, a, b)

        # Enforce ordering
        k0_new = max(k0_new, k1_new)
        kD_new = max(kD_new, k0_new)

        # Check convergence
        if (
            abs(k1_new - k1) < tol
            and abs(k0_new - k0) < tol
            and abs(kD_new - kD) < tol
        ):
            return Cutoffs(float(k1_new), float(k0_new), float(kD_new))

        # Damped update
        alpha = 0.75
        k1 = alpha * float(k1_new) + (1 - alpha) * k1
        k0 = alpha * float(k0_new) + (1 - alpha) * k0
        kD = alpha * float(kD_new) + (1 - alpha) * kD

    return Cutoffs(float(k1), float(k0), float(kD))


def solve_valid(
    params: ModelParams,
    prev_cutoffs: Optional[Cutoffs] = None,
    residual_tol: float = TOL_RESIDUAL,
) -> Tuple[Optional[Cutoffs], float]:
    """Multi-start equilibrium solver with collapsed-hold fallback.

    Tries a warm start from *prev_cutoffs* (when available), then falls
    back to a collapsed-hold initialization.  When no previous cutoffs are
    supplied, two generic starting points are evaluated.

    Parameters
    ----------
    params : ModelParams
        Model parameters.
    prev_cutoffs : Cutoffs, optional
        Cutoffs from a nearby parameter point (warm start).
    residual_tol : float
        Residual threshold below which a solution is accepted immediately.

    Returns
    -------
    (cutoffs, residual) : Tuple[Optional[Cutoffs], float]
        Best cutoffs found (or *None* if all starts failed) and the
        corresponding residual.
    """

    def attempt(
        start: Tuple[float, float, float],
    ) -> Tuple[Cutoffs, float]:
        k1i, k0i, kDi = start
        cut = solve_equilibrium(
            params,
            k1_init=float(k1i),
            k0_init=float(k0i),
            kD_init=float(kDi),
            max_iter=90,
            tol=TOL_CONVERGE,
        )
        return cut, equilibrium_residual(*cut, params)

    # 1) Warm start from previous kappa (if available).
    if prev_cutoffs is not None:
        cut, res = attempt(prev_cutoffs)
        if np.isfinite(res) and res <= residual_tol:
            return cut, res

        # 2) Alternative branch: no Passive Hold.
        k1p, _, kDp = prev_cutoffs
        alt_start = (k1p, k1p, kDp)
        cut2, res2 = attempt(alt_start)
        if res2 < res:
            cut, res = cut2, res2
        return cut, res

    # No previous cutoffs: try a couple of generic starts.
    starts = [
        (
            params.mu - 1.0 * params.sigma_s,
            params.mu - 1.0 * params.sigma_s,
            params.mu + 0.5 * params.sigma_s,
        ),
        (
            params.mu - 1.0 * params.sigma_s,
            params.mu - 0.5 * params.sigma_s,
            params.mu + 0.5 * params.sigma_s,
        ),
    ]
    best_cut: Optional[Cutoffs] = None
    best_res = np.inf
    for st in starts:
        cut, res = attempt(st)
        if res < best_res:
            best_cut, best_res = cut, res
    return best_cut, float(best_res)


def solve_equilibrium_for_kappa(
    kappa: float,
    base_params: ModelParams,
    prev_cutoffs: Optional[Cutoffs] = None,
) -> Cutoffs:
    """Convenience wrapper: solve equilibrium at a specific kappa value.

    Parameters
    ----------
    kappa : float
        Noise trading intensity to evaluate.
    base_params : ModelParams
        Template parameters (all fields except *kappa* are preserved).
    prev_cutoffs : Cutoffs, optional
        Warm-start cutoffs from an adjacent grid point.

    Returns
    -------
    Cutoffs
        Equilibrium cutoffs at the given kappa.
    """
    params = base_params.replace(kappa=kappa)

    if prev_cutoffs is not None:
        return solve_equilibrium(
            params,
            k1_init=prev_cutoffs[0],
            k0_init=prev_cutoffs[1],
            kD_init=prev_cutoffs[2],
        )
    return solve_equilibrium(params)


def compute_series_over_kappa(
    base_params: ModelParams,
    kappa_values: np.ndarray,
    include_no_disclosure: bool = False,
) -> Dict[str, np.ndarray]:
    """Compute equilibrium cutoffs and welfare series over a liquidity grid.

    Parameters
    ----------
    base_params : ModelParams
        Template parameters (kappa will be overridden for each grid point).
    kappa_values : np.ndarray
        1-D array of kappa values to sweep.
    include_no_disclosure : bool
        If True, also compute the no-disclosure counterfactual activism
        component at each grid point.

    Returns
    -------
    Dict[str, np.ndarray]
        Keys: ``kappa``, ``k1``, ``k0``, ``kD``, ``Delta_min``, ``base``,
        ``act``, and optionally ``act_no_disclosure``.
    """
    if HAS_NUMBA:
        return _series_fast(base_params, kappa_values, include_no_disclosure)

    k1_vals: List[float] = []
    k0_vals: List[float] = []
    kD_vals: List[float] = []
    Delta_min_vals: List[float] = []
    base_vals: List[float] = []
    act_vals: List[float] = []
    act_nd_vals: List[float] = []

    prev_cutoffs: Optional[Cutoffs] = None
    for kappa in kappa_values:
        try:
            cutoffs = solve_equilibrium_for_kappa(
                float(kappa), base_params, prev_cutoffs
            )
            prev_cutoffs = cutoffs

            params = base_params.replace(kappa=float(kappa))

            total, base_c, act_c = compute_minority_gains(
                cutoffs.k1, cutoffs.k0, cutoffs.kD, params
            )
            if include_no_disclosure:
                _, _, act_nd = compute_minority_gains_no_disclosure_given_strategy(
                    cutoffs.k1, cutoffs.k0, cutoffs.kD, params
                )
                act_nd_vals.append(act_nd)

            k1_vals.append(cutoffs.k1)
            k0_vals.append(cutoffs.k0)
            kD_vals.append(cutoffs.kD)
            Delta_min_vals.append(total)
            base_vals.append(base_c)
            act_vals.append(act_c)
        except (RuntimeError, ValueError) as exc:
            warnings.warn(f"Solver failed at kappa={kappa}: {exc}")
            k1_vals.append(np.nan)
            k0_vals.append(np.nan)
            kD_vals.append(np.nan)
            Delta_min_vals.append(np.nan)
            base_vals.append(np.nan)
            act_vals.append(np.nan)
            if include_no_disclosure:
                act_nd_vals.append(np.nan)

    series: Dict[str, np.ndarray] = {
        "kappa": np.array(kappa_values, dtype=float),
        "k1": np.array(k1_vals, dtype=float),
        "k0": np.array(k0_vals, dtype=float),
        "kD": np.array(kD_vals, dtype=float),
        "Delta_min": np.array(Delta_min_vals, dtype=float),
        "base": np.array(base_vals, dtype=float),
        "act": np.array(act_vals, dtype=float),
    }
    if include_no_disclosure:
        series["act_no_disclosure"] = np.array(act_nd_vals, dtype=float)

    return series
