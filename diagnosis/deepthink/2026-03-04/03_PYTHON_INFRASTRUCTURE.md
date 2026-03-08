# Python Infrastructure

## numerical/params.py
ModelParams dataclass (baseline calibration), Action enum, Cutoffs and MinorityGains NamedTuples, tolerance constants.

```python
"""
Model parameters and type definitions for the Exit-Voice-Takeover model.

This is the foundational module — all other modules in the numerical package
import from here. It defines:

- Named tolerance constants used across the solver and equilibrium routines
- The ``Action`` enum encoding the blockholder's four action choices
- ``Cutoffs`` and ``MinorityGains`` named tuples for structured return values
- The ``ModelParams`` dataclass with baseline calibration and derived quantities
"""

from __future__ import annotations

import dataclasses
import enum
from dataclasses import dataclass
from typing import NamedTuple

import numpy as np

# ---------------------------------------------------------------------------
# Tolerance constants
# ---------------------------------------------------------------------------

TOL_PROB: float = 1e-10       # Near-zero probability threshold
TOL_CONVERGE: float = 1e-6    # Fixed-point convergence criterion
TOL_RESIDUAL: float = 5e-3    # Equilibrium quality gate
TOL_REGION: float = 1e-4      # Cutoff region collapse detection


# ---------------------------------------------------------------------------
# Action enum
# ---------------------------------------------------------------------------

class Action(enum.Enum):
    """Blockholder action choice (Definition 2 in the paper).

    EXIT   -- Sell stake  (q = -1, a = 0)
    HOLD   -- Passive hold (q = 0,  a = 0)
    QUIET  -- Quiet Voice: engage below disclosure threshold (q = 0,  a = 1)
    PUBLIC -- Public Voice: buy, engage, trigger disclosure  (q = +1, a = 1)
    """

    EXIT = "E"
    HOLD = "H"
    QUIET = "Q"
    PUBLIC = "P"


# ---------------------------------------------------------------------------
# Named tuples
# ---------------------------------------------------------------------------

class Cutoffs(NamedTuple):
    """Equilibrium signal cutoffs (Proposition 1).

    k1: Exit/Hold boundary -- signals below k1 trigger exit
    k0: Hold/Quiet Voice boundary -- signals above k0 trigger engagement
    kD: Quiet/Public Voice boundary -- signals above kD trigger disclosure

    Satisfies k1 <= k0 <= kD (weak ordering allows region collapse).
    """

    k1: float
    k0: float
    kD: float


class MinorityGains(NamedTuple):
    """Expected minority takeover gains decomposition.

    total: Total expected minority gains Delta^min
    base:  Base component m0 * Pr(bid)
    activism: Activism-driven component Delta^act
    """

    total: float
    base: float
    activism: float


# ---------------------------------------------------------------------------
# Model parameters
# ---------------------------------------------------------------------------

@dataclass
class ModelParams:
    """Parameters for the Exit-Voice-Takeover model.

    Notation follows the paper:

        mu, sigma_v     -- Prior: v ~ N(mu, sigma_v^2)              
        sigma_eps       -- Signal noise: s = v + eps                 
        kappa           -- Noise trading intensity                   
        C0, chi         -- Engagement cost: C(s) = C0*exp(-chi*z)   
        rho, Delta      -- Success probability and value improvement 
        m0, m1          -- Takeover premia without/with engagement   
        S_bar, K        -- Baseline synergy and bidding cost         
        Delta_S         -- Synergy improvement from activism         
        s_xi            -- Logistic synergy shock scale              
        lambda_B        -- Bidder arrival rate (scales bid prob.)    
        delta           -- Discount factor                           

    Default values correspond to the baseline calibration used throughout
    the paper (Table C.3).
    """

    # Fundamentals
    mu: float = 1.0                # Prior mean of v
    sigma_v: float = 0.50          # Std dev of v
    sigma_eps: float = 0.50        # Std dev of signal noise

    # Liquidity
    kappa: float = 0.50            # Noise trading intensity

    # Engagement
    C0: float = 0.25               # Base engagement cost
    chi: float = 0.50              # Cost sensitivity to signal
    rho: float = 0.90              # Engagement success probability
    Delta: float = 0.25            # Value improvement from engagement

    # Takeover
    m0: float = 0.10               # Base takeover premium
    m1: float = 0.30               # Premium with successful engagement
    S_bar: float = 1.10            # Baseline synergy
    Delta_S: float = 0.30          # Expected fundamental synergy improvement from activism
    K: float = 0.15                # Bidding cost
    s_xi: float = 0.15             # Logistic synergy shock scale
    lambda_B: float = 0.20         # Poisson bidder arrival rate

    # Discounting
    delta: float = 0.95            # Discount factor

    # -- Derived quantities ------------------------------------------------

    @property
    def sigma_s(self) -> float:
        """Signal standard deviation: sqrt(sigma_v^2 + sigma_eps^2)."""
        return float(np.sqrt(self.sigma_v**2 + self.sigma_eps**2))

    @property
    def beta(self) -> float:
        """Posterior weight on the signal in v_hat(s)."""
        return self.sigma_v**2 / (self.sigma_v**2 + self.sigma_eps**2)

    @property
    def m_tilde(self) -> float:
        """Expected takeover premium under engagement."""
        return self.m0 + self.rho * (self.m1 - self.m0)

    @property
    def Delta_tilde(self) -> float:
        """Expected value improvement under engagement."""
        return self.rho * self.Delta

    @property
    def net_deterrence_active(self) -> bool:
        """Verify Assumption (A5): Net Deterrence Condition.
        
        Requires: Delta_tilde + m_tilde - m0 > Delta_S
        """
        return (self.Delta_tilde + self.m_tilde - self.m0) > self.Delta_S

    # -- Convenience methods -----------------------------------------------

    def replace(self, **kwargs) -> ModelParams:
        """Return a copy with specified fields overridden."""
        return dataclasses.replace(self, **kwargs)

    @classmethod
    def baseline(cls) -> ModelParams:
        """Baseline calibration used in the paper."""
        return cls()
```

## numerical/solver.py
Equilibrium solver using damped fixed-point iteration with scipy.optimize.brentq.
Multi-start search with collapsed-hold fallback.

```python
"""
Equilibrium solver for the Exit-Voice-Takeover model.

This module implements the direct feed-forward fixed-point iteration.
It provides:

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
    ModelParams,
    TOL_CONVERGE,
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

def equilibrium_residual(
    k1: float, k0: float, kD: float, params: ModelParams
) -> float:
    """Compute maximum indifference residual across the three cutoff conditions."""
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    post = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    prices, prices_trade, E_v_dict = compute_equilibrium_prices(k1, k0, kD, params)

    def U(action: Action, s: float) -> float:
        return compute_expected_payoff(action, float(s), prices, prices_trade, post, E_v_dict, params)

    s_min = params.mu - 6 * params.sigma_s
    s_max = params.mu + 6 * params.sigma_s

    diff1 = U(Action.EXIT, k1) - max(U(Action.HOLD, k1), U(Action.QUIET, k1))
    if k1 <= s_min + TOL_REGION or k1 >= s_max - TOL_REGION:
        r1 = max(0.0, -diff1) if k1 >= s_max - TOL_REGION else max(0.0, diff1)
    else:
        r1 = abs(diff1)

    if (k0 - k1) > TOL_REGION:
        r0 = abs(U(Action.HOLD, k0) - U(Action.QUIET, k0))
    else:
        s_test = min(k1 + TOL_REGION, s_max)
        r0 = max(0.0, U(Action.HOLD, s_test) - U(Action.QUIET, s_test))

    lower = Action.QUIET if k0 < s_max - TOL_REGION else Action.HOLD
    if kD >= s_max - TOL_REGION:
        rD = max(0.0, U(Action.PUBLIC, s_max) - U(lower, s_max))
    elif (kD - k0) < TOL_REGION:
        # Quiet voice region collapsed — only penalize if QUIET dominates PUBLIC
        # (which would mean the collapse is incorrect). When PUBLIC dominates,
        # the collapse is correct behavior (stealth advantage at high kappa).
        s_test = min(k0 + TOL_REGION, s_max)
        rD = max(0.0, U(lower, s_test) - U(Action.PUBLIC, s_test))
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
    """Solve for equilibrium cutoffs via damped fixed-point iteration."""
    k1 = params.mu - 1.0 * params.sigma_s if k1_init is None else float(k1_init)
    k0 = params.mu - 0.5 * params.sigma_s if k0_init is None else float(k0_init)
    kD = params.mu + 0.5 * params.sigma_s if kD_init is None else float(kD_init)

    s_min = params.mu - 6 * params.sigma_s
    s_max = params.mu + 6 * params.sigma_s
    s_grid = np.linspace(s_min, s_max, 61)

    def bracket_root(func, low=None, high=None, target=None):
        grid = s_grid
        if low is not None: grid = grid[grid >= low]
        if high is not None: grid = grid[grid <= high]
        if len(grid) < 2: return None
        vals = np.array([func(s) for s in grid], dtype=float)
        if np.any(np.isnan(vals)): return None
        brackets = [(float(grid[i]), float(grid[i + 1])) for i in range(len(grid) - 1) if vals[i] * vals[i + 1] <= 0]
        if not brackets: return None
        if target is None or not np.isfinite(target): return brackets[0]
        return min(brackets, key=lambda ab: abs(((ab[0] + ab[1]) / 2) - float(target)))

    for _iteration in range(max_iter):
        k0 = max(k0, k1)
        kD = max(kD, k0)

        omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
        posteriors = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)
        prices, prices_trade, E_v_dict = compute_equilibrium_prices(k1, k0, kD, params)

        def U(action: Action, s: float) -> float:
            return compute_expected_payoff(action, float(s), prices, prices_trade, posteriors, E_v_dict, params)

        def diff_E_best0(s: float) -> float:
            return U(Action.EXIT, s) - max(U(Action.HOLD, s), U(Action.QUIET, s))

        bracket = bracket_root(diff_E_best0, target=k1)
        if bracket is None:
            k1_new = s_max if diff_E_best0(s_min) >= 0 else s_min
        else:
            a, b = bracket
            k1_new = a if a == b else brentq(diff_E_best0, a, b)

        def diff_H_Q(s: float) -> float:
            return U(Action.HOLD, s) - U(Action.QUIET, s)

        s0 = min(k1_new + 1e-4, s_max)
        bracket = bracket_root(diff_H_Q, low=k1_new, high=s_max, target=k0)
        if bracket is None:
            k0_new = k1_new if diff_H_Q(s0) <= 0 else s_max
        else:
            a, b = bracket
            k0_new = a if a == b else brentq(diff_H_Q, a, b)

        lower_action = Action.QUIET if k0_new < s_max - 1e-6 else Action.HOLD

        def diff_lower_P(s: float) -> float:
            return U(lower_action, s) - U(Action.PUBLIC, s)

        start = min(k0_new, s_max)
        bracket = bracket_root(diff_lower_P, low=start, high=s_max, target=kD)
        if bracket is None:
            kD_new = start if diff_lower_P(start + 1e-4) <= 0 else s_max
        else:
            a, b = bracket
            kD_new = a if a == b else brentq(diff_lower_P, a, b)

        k0_new = max(k0_new, k1_new)
        kD_new = max(kD_new, k0_new)

        if abs(k1_new - k1) < tol and abs(k0_new - k0) < tol and abs(kD_new - kD) < tol:
            return Cutoffs(float(k1_new), float(k0_new), float(kD_new))

        alpha = 0.75
        k1 = alpha * float(k1_new) + (1 - alpha) * k1
        k0 = alpha * float(k0_new) + (1 - alpha) * k0
        kD = alpha * float(kD_new) + (1 - alpha) * kD

    return Cutoffs(float(k1), float(k0), float(kD))


def solve_valid(
    params: ModelParams, prev_cutoffs: Optional[Cutoffs] = None, residual_tol: float = TOL_RESIDUAL
) -> Tuple[Optional[Cutoffs], float]:
    """Multi-start equilibrium solver with collapsed-hold fallback."""
    def attempt(start: Tuple[float, float, float]) -> Tuple[Cutoffs, float]:
        cut = solve_equilibrium(params, k1_init=start[0], k0_init=start[1], kD_init=start[2], max_iter=90, tol=TOL_CONVERGE)
        return cut, equilibrium_residual(*cut, params)

    if prev_cutoffs is not None:
        cut, res = attempt(prev_cutoffs)
        if np.isfinite(res) and res <= residual_tol: return cut, res

        k1p = prev_cutoffs.k1
        kDp = prev_cutoffs.kD
        cut2, res2 = attempt((k1p, k1p, kDp))
        if res2 < res:
            cut, res = cut2, res2

        # Moderate-kD fallback: when continuation has kD far from mu,
        # try a start with kD near mu + 0.5*sigma_s to escape the off-path basin.
        if kDp > params.mu + 2.0 * params.sigma_s or res > residual_tol:
            kD_mod = params.mu + 0.5 * params.sigma_s
            cut3, res3 = attempt((k1p, params.mu + 0.4 * params.sigma_s, kD_mod))
            if res3 < res:
                cut, res = cut3, res3

        return cut, res

    starts = [
        (params.mu - 1.0 * params.sigma_s, params.mu - 1.0 * params.sigma_s, params.mu + 0.5 * params.sigma_s),
        (params.mu - 1.0 * params.sigma_s, params.mu - 0.5 * params.sigma_s, params.mu + 0.5 * params.sigma_s),
    ]
    best_cut, best_res = None, np.inf
    for st in starts:
        cut, res = attempt(st)
        if res < best_res:
            best_cut, best_res = cut, res
    return best_cut, float(best_res)


def solve_equilibrium_for_kappa(kappa: float, base_params: ModelParams, prev_cutoffs: Optional[Cutoffs] = None) -> Cutoffs:
    params = base_params.replace(kappa=kappa)
    if prev_cutoffs is not None:
        return solve_equilibrium(params, k1_init=prev_cutoffs[0], k0_init=prev_cutoffs[1], kD_init=prev_cutoffs[2])
    return solve_equilibrium(params)


def compute_series_over_kappa(
    base_params: ModelParams, kappa_values: np.ndarray, include_no_disclosure: bool = False
) -> Dict[str, np.ndarray]:
    """Compute equilibrium cutoffs and welfare series over a liquidity grid."""
    k1_vals, k0_vals, kD_vals = [], [], []
    Delta_min_vals, base_vals, act_vals, act_nd_vals = [], [], [], []
    prev_cutoffs = None

    for kappa in kappa_values:
        try:
            params = base_params.replace(kappa=float(kappa))
            cutoffs, _res = solve_valid(params, prev_cutoffs)
            if cutoffs is None:
                raise RuntimeError("solve_valid returned None")
            prev_cutoffs = cutoffs

            total, base_c, act_c = compute_minority_gains(cutoffs.k1, cutoffs.k0, cutoffs.kD, params)
            if include_no_disclosure:
                _, _, act_nd = compute_minority_gains_no_disclosure_given_strategy(cutoffs.k1, cutoffs.k0, cutoffs.kD, params)
                act_nd_vals.append(act_nd)

            k1_vals.append(cutoffs.k1)
            k0_vals.append(cutoffs.k0)
            kD_vals.append(cutoffs.kD)
            Delta_min_vals.append(total)
            base_vals.append(base_c)
            act_vals.append(act_c)
        except Exception as exc:
            warnings.warn(f"Solver failed at kappa={kappa}: {exc}")
            for lst in (k1_vals, k0_vals, kD_vals, Delta_min_vals, base_vals, act_vals):
                lst.append(np.nan)
            if include_no_disclosure: act_nd_vals.append(np.nan)

    series = {
        "kappa": np.array(kappa_values, dtype=float),
        "k1": np.array(k1_vals, dtype=float), "k0": np.array(k0_vals, dtype=float), "kD": np.array(kD_vals, dtype=float),
        "Delta_min": np.array(Delta_min_vals, dtype=float), "base": np.array(base_vals, dtype=float), "act": np.array(act_vals, dtype=float),
    }
    if include_no_disclosure: series["act_no_disclosure"] = np.array(act_nd_vals, dtype=float)
    return series
```
