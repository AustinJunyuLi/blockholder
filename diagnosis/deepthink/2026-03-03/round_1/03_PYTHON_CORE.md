# Python Core: numerical package

This file contains the four core modules of the `numerical/` package, which implement
the Exit-Voice-Takeover economic model. The dependency flow is:

```
params.py -> model.py -> solver.py
```

`__init__.py` re-exports the public API.

---

## File: `numerical/__init__.py`

```python
"""
Exit-Voice-Takeover Model: Numerical Analysis Package.

Modules
-------
params       -- Model parameters, Action enum, Cutoffs/MinorityGains types
model        -- Core economic functions (posteriors, prices, payoffs)
solver       -- Equilibrium solver and comparative statics
export_data  -- CSV data export and LaTeX table generation
"""

from numerical.params import Action, Cutoffs, MinorityGains, ModelParams
from numerical.solver import solve_equilibrium, solve_valid, compute_series_over_kappa
from numerical.export_data import export_all

__all__ = [
    "Action",
    "Cutoffs",
    "MinorityGains",
    "ModelParams",
    "solve_equilibrium",
    "solve_valid",
    "compute_series_over_kappa",
    "export_all",
]
```

---

## File: `numerical/params.py`

```python
"""
Model parameters and type definitions for the Exit-Voice-Takeover model.

This is the foundational module -- all other modules in the numerical package
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
from scipy.stats import norm

# ---------------------------------------------------------------------------
# Tolerance constants
# ---------------------------------------------------------------------------

TOL_PROB: float = 1e-10        # Near-zero probability threshold
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
    """Expected minority takeover gains decomposition (Section 5).

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

        mu, sigma_v     -- Prior: v ~ N(mu, sigma_v^2)              [Section 2.1]
        sigma_eps       -- Signal noise: s = v + eps                 [Eq. 1]
        kappa           -- Noise trading intensity                   [Definition 1]
        C0, chi         -- Engagement cost: C(s) = C0*exp(-chi*z)   [Eq. 3]
        rho, Delta      -- Success probability and value improvement [Eq. 4]
        m0, m1          -- Takeover premia without/with engagement   [Eq. 5]
        S_bar, K        -- Baseline synergy and bidding cost         [Eq. 8]
        sigma_xi        -- Synergy shock volatility                  [Eq. 8]
        lambda_B        -- Bidder arrival rate (scales bid prob.)    [Eq. 8']
        delta           -- Discount factor                           [Eq. 6]

    Default values correspond to the baseline calibration used throughout
    the paper.
    """

    # Fundamentals
    mu: float = 1.0                # Prior mean of v
    sigma_v: float = 0.5           # Std dev of v
    sigma_eps: float = 0.5         # Std dev of signal noise

    # Liquidity
    kappa: float = 0.5             # Noise trading intensity

    # Engagement
    C0: float = 0.12              # Base engagement cost
    chi: float = 0.5              # Cost sensitivity to signal
    rho: float = 0.9              # Engagement success probability
    Delta: float = 0.25           # Value improvement from engagement

    # Takeover
    m0: float = 0.10              # Base takeover premium
    m1: float = 0.30              # Premium with successful engagement
    S_bar: float = 0.60           # Baseline synergy
    K: float = 0.15               # Bidding cost
    sigma_xi: float = 0.30        # Synergy shock volatility
    lambda_B: float = 0.05        # Bidder arrival rate

    # Discounting
    delta: float = 0.95           # Discount factor

    # -- Derived quantities ------------------------------------------------

    @property
    def sigma_s(self) -> float:
        """Signal standard deviation: sqrt(sigma_v^2 + sigma_eps^2)."""
        return np.sqrt(self.sigma_v**2 + self.sigma_eps**2)

    @property
    def beta(self) -> float:
        """Posterior weight on the signal in v_hat(s).

        beta = sigma_v^2 / (sigma_v^2 + sigma_eps^2)
        """
        return self.sigma_v**2 / (self.sigma_v**2 + self.sigma_eps**2)

    @property
    def m_tilde(self) -> float:
        """Expected takeover premium under engagement.

        m_tilde = m0 + rho * (m1 - m0)
        """
        return self.m0 + self.rho * (self.m1 - self.m0)

    @property
    def Delta_tilde(self) -> float:
        """Expected value improvement under engagement.

        Delta_tilde = rho * Delta
        """
        return self.rho * self.Delta

    # -- Convenience methods -----------------------------------------------

    def replace(self, **kwargs) -> ModelParams:
        """Return a copy with specified fields overridden."""
        return dataclasses.replace(self, **kwargs)

    @classmethod
    def baseline(cls) -> ModelParams:
        """Baseline calibration used in the paper."""
        return cls()
```

---

## File: `numerical/model.py`

```python
"""
Core economic model functions for the Exit-Voice-Takeover model.

This module implements the equilibrium objects described in Sections 2--5
of "Liquidity, Activism Disclosure, and Takeover Premia":

    Section 2 -- Information structure (signal, engagement cost, posterior mean)
    Section 3 -- Market microstructure (action probabilities, posteriors, prices)
    Section 4 -- Welfare and minority gains
    Section 5 -- Counterfactual information regimes

Revision notes (2026-03-03, "theory fixes" atomic bundle):
    - Noise distribution: p0 = 1 - 2*kappa/3, p1 = kappa/3  (Fix 1)
    - Bid probability decoupled from price P  (Fix 2)
    - Direct pricing formula replaces fixed-point iteration  (Fix 2)
    - Bidder arrival rate lambda_B scales all bid probabilities  (Fix 3)
"""

from __future__ import annotations

from typing import Dict, Tuple

import numpy as np
from scipy.stats import norm

from numerical.params import (
    Action,
    MinorityGains,
    ModelParams,
    TOL_CONVERGE,
    TOL_PROB,
    TOL_REGION,
)

# -- Noise Distribution ----------------------------------------------------


def noise_probs(kappa: float) -> Tuple[float, float]:
    """Noise-trader order flow probabilities -- Definition 1.

    Returns
    -------
    (p0, p1) : Tuple[float, float]
        p0 = P(z=0),  p1 = P(z=+1) = P(z=-1).
        Satisfies p0 + 2*p1 = 1 for all kappa in [0, 1].

    The parametrisation p0 = 1 - 2*kappa/3, p1 = kappa/3 ensures
    that z=0 retains positive mass (1/3) at kappa=1, preventing
    the disjoint-support pathology where order flow becomes perfectly
    separating at high noise-trading intensity.

    Raises
    ------
    ValueError
        If kappa is outside [0, 1].
    """
    if not (0.0 <= kappa <= 1.0):
        raise ValueError(f"kappa must be in [0, 1], got {kappa}")
    p0 = 1.0 - (2.0 / 3.0) * kappa
    p1 = (1.0 / 3.0) * kappa
    return p0, p1


# -- Section 2: Information Structure --------------------------------------


def engagement_cost(s: float, params: ModelParams) -> float:
    """Signal-dependent engagement cost C(s) -- Equation (3).

    C(s) = C0 * exp(-chi * z),  where z = (s - mu) / sigma_s.
    """
    z = (s - params.mu) / params.sigma_s
    return params.C0 * np.exp(-params.chi * z)


def v_hat(s: float, params: ModelParams) -> float:
    """Posterior mean of v given signal s -- Equation (2).

    v_hat(s) = mu + beta * (s - mu).
    """
    return params.mu + params.beta * (s - params.mu)


# -- Section 3: Market Microstructure --------------------------------------


def compute_action_probabilities(
    k1: float, k0: float, kD: float, params: ModelParams
) -> Tuple[float, float, float, float]:
    """Unconditional action probabilities -- Proposition 1.

    Returns
    -------
    (omega_E, omega_H, omega_Q, omega_P):
        Exit, Passive Hold, Quiet Voice, Public Voice probabilities.
    """
    alpha1 = (k1 - params.mu) / params.sigma_s
    alpha0 = (k0 - params.mu) / params.sigma_s
    alphaD = (kD - params.mu) / params.sigma_s

    omega_E = norm.cdf(alpha1)
    omega_H = norm.cdf(alpha0) - norm.cdf(alpha1)
    omega_Q = norm.cdf(alphaD) - norm.cdf(alpha0)
    omega_P = 1 - norm.cdf(alphaD)

    # Ensure non-negative (numerical stability)
    omega_E = max(0, omega_E)
    omega_H = max(0, omega_H)
    omega_Q = max(0, omega_Q)
    omega_P = max(0, omega_P)

    return omega_E, omega_H, omega_Q, omega_P


def compute_conditional_means(
    k1: float, k0: float, kD: float, params: ModelParams
) -> Tuple[float, float, float, float]:
    """Conditional means E[v | action region] -- derived from Proposition 1.

    Returns
    -------
    (mu_E, mu_H, mu_Q, mu_P):
        Conditional mean of v in each signal region.
    """
    alpha1 = (k1 - params.mu) / params.sigma_s
    alpha0 = (k0 - params.mu) / params.sigma_s
    alphaD = (kD - params.mu) / params.sigma_s

    # Inverse Mills ratios
    def lambda_L(alpha: float) -> float:
        """Lower inverse Mills ratio."""
        cdf = norm.cdf(alpha)
        if cdf < TOL_PROB:
            return -alpha  # Approximation for extreme values
        return norm.pdf(alpha) / cdf

    def lambda_U(alpha: float) -> float:
        """Upper inverse Mills ratio."""
        ccdf = 1 - norm.cdf(alpha)
        if ccdf < TOL_PROB:
            return alpha  # Approximation for extreme values
        return norm.pdf(alpha) / ccdf

    # Exit: s < k1
    mu_E = params.mu - params.beta * params.sigma_s * lambda_L(alpha1)

    # Passive Hold: k1 <= s < k0
    denom_H = norm.cdf(alpha0) - norm.cdf(alpha1)
    if denom_H > TOL_PROB:
        mu_H = params.mu + params.beta * params.sigma_s * (
            norm.pdf(alpha1) - norm.pdf(alpha0)
        ) / denom_H
    else:
        mu_H = params.mu + params.beta * (k0 + k1) / 2 - params.beta * params.mu

    # Quiet Voice: k0 <= s < kD
    denom_Q = norm.cdf(alphaD) - norm.cdf(alpha0)
    if denom_Q > TOL_PROB:
        mu_Q = params.mu + params.beta * params.sigma_s * (
            norm.pdf(alpha0) - norm.pdf(alphaD)
        ) / denom_Q
    else:
        mu_Q = params.mu + params.beta * (kD + k0) / 2 - params.beta * params.mu

    # Public Voice: s >= kD
    mu_P = params.mu + params.beta * params.sigma_s * lambda_U(alphaD)

    return mu_E, mu_H, mu_Q, mu_P


def compute_posteriors(
    omega_E: float, omega_H: float, omega_Q: float, omega_P: float,
    kappa: float
) -> Dict[Tuple[int, int], float]:
    """Bayesian posterior pi(X, D) -- Proposition 2, Eqs. (12)--(15).

    Returns
    -------
    dict mapping (X, D) -> pi(X, D):
        Posterior probability of engagement given market observables.
    """
    p0, p1 = noise_probs(kappa)

    posteriors: Dict[Tuple[int, int], float] = {}

    # Disclosed states: D=1 => a=1 always
    for X in [0, 1, 2]:
        posteriors[(X, 1)] = 1.0

    # Non-disclosed states: D=0
    # X = -2: only Exit possible
    posteriors[(-2, 0)] = 0.0

    # X = 1: q=0 with z=+1 (only Hold/Quiet Voice)
    denom_1 = omega_H + omega_Q
    if denom_1 > TOL_PROB:
        posteriors[(1, 0)] = omega_Q / denom_1
    else:
        posteriors[(1, 0)] = 0.0

    # X = -1: Hold/QuietVoice with z=-1, or Exit with z=0
    denom_m1 = (omega_H + omega_Q) * p1 + omega_E * p0
    if denom_m1 > TOL_PROB:
        posteriors[(-1, 0)] = omega_Q * p1 / denom_m1
    else:
        posteriors[(-1, 0)] = 0.0

    # X = 0: Hold/QuietVoice with z=0, or Exit with z=+1
    denom_0 = (omega_H + omega_Q) * p0 + omega_E * p1
    if denom_0 > TOL_PROB:
        posteriors[(0, 0)] = omega_Q * p0 / denom_0
    else:
        posteriors[(0, 0)] = 0.0

    return posteriors


def compute_E_v_given_XD(
    X: int, D: int,
    omega_E: float, omega_H: float, omega_Q: float, omega_P: float,
    mu_E: float, mu_H: float, mu_Q: float, mu_P: float,
    kappa: float
) -> float:
    """Conditional expectation E[v | X, D] -- Eqs. (10)--(11).

    Mixes over unobserved blockholder actions weighted by their likelihood
    of producing the observed order flow and disclosure state.
    """
    p0, p1 = noise_probs(kappa)

    if D == 1:
        # Only Public Voice possible
        return mu_P

    # D = 0
    if X == -2:
        return mu_E
    elif X == 1:
        # Hold/QuietVoice with z=+1 only
        denom = omega_H + omega_Q
        if denom < TOL_PROB:
            return (mu_H + mu_Q) / 2
        return (omega_H * mu_H + omega_Q * mu_Q) / denom
    elif X == -1:
        # Hold/QuietVoice with z=-1, or Exit with z=0
        denom = (omega_H + omega_Q) * p1 + omega_E * p0
        if denom < TOL_PROB:
            return (mu_H + mu_Q + mu_E) / 3
        return ((omega_H * mu_H + omega_Q * mu_Q) * p1 + omega_E * mu_E * p0) / denom
    else:  # X == 0
        # Hold/QuietVoice with z=0, or Exit with z=+1
        denom = (omega_H + omega_Q) * p0 + omega_E * p1
        if denom < TOL_PROB:
            return (mu_H + mu_Q + mu_E) / 3
        return ((omega_H * mu_H + omega_Q * mu_Q) * p0 +
                omega_E * mu_E * p1) / denom


def bid_probability(m_XD: float, params: ModelParams) -> float:
    """Bid probability p(X, D) -- Equation (8), decoupled from price.

    The bidder submits a takeover offer when synergy shock xi exceeds
    the threshold T = (m + K - S_bar) / sigma_xi.

    Note: this returns the *conditional* bid probability (given a bidder
    arrives).  Multiply by params.lambda_B to get the effective bid rate.
    """
    T = (m_XD + params.K - params.S_bar) / params.sigma_xi
    return float(norm.sf(T))


def compute_price_direct(
    E_v_XD: float, pi_XD: float, p_bid: float, m_XD: float,
    params: ModelParams
) -> float:
    """Equilibrium price P(X, D) -- direct formula (no fixed-point).

    After decoupling bid probability from price, the price equation
    becomes a direct computation:

        P = delta * [V_hat + p_bid * m_XD]

    where V_hat = E[v|X,D] + Delta_tilde * pi(X,D)
    and   p_bid already incorporates lambda_B.
    """
    V_hat = E_v_XD + params.Delta_tilde * pi_XD
    return params.delta * (V_hat + p_bid * m_XD)


def compute_equilibrium_prices(
    k1: float, k0: float, kD: float, params: ModelParams
) -> Tuple[Dict[Tuple[int, int], float], Dict[Tuple[int, int], float]]:
    """Equilibrium prices P(X, D) for all feasible (X, D) pairs.

    Returns
    -------
    (prices, E_v_dict) : Tuple[Dict, Dict]
        prices: mapping (X, D) -> P(X, D)
        E_v_dict: mapping (X, D) -> E[v | X, D]
    """
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(
        k1, k0, kD, params
    )
    mu_E, mu_H, mu_Q, mu_P = compute_conditional_means(k1, k0, kD, params)
    posteriors = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)

    prices: Dict[Tuple[int, int], float] = {}
    E_v_dict: Dict[Tuple[int, int], float] = {}

    # All possible (X, D) pairs
    for X in [-2, -1, 0, 1, 2]:
        for D in [0, 1]:
            # Check feasibility
            if D == 1 and X < 0:
                continue  # D=1 requires q=+1, so X >= 0

            if (X, D) not in posteriors:
                continue

            pi_XD = posteriors[(X, D)]
            E_v_XD = compute_E_v_given_XD(
                X, D, omega_E, omega_H, omega_Q, omega_P,
                mu_E, mu_H, mu_Q, mu_P, params.kappa
            )
            E_v_dict[(X, D)] = E_v_XD

            m_XD = params.m0 + (params.m_tilde - params.m0) * pi_XD
            p_bid = params.lambda_B * bid_probability(m_XD, params)

            prices[(X, D)] = compute_price_direct(
                E_v_XD, pi_XD, p_bid, m_XD, params
            )

    return prices, E_v_dict


def compute_expected_payoff(
    action: Action, s: float,
    prices: Dict[Tuple[int, int], float],
    posteriors: Dict[Tuple[int, int], float],
    E_v_dict: Dict[Tuple[int, int], float],
    params: ModelParams
) -> float:
    """Expected payoff for a given action and signal -- Equation (7).

    Parameters
    ----------
    action : Action
        One of Action.EXIT, Action.HOLD, Action.QUIET, Action.PUBLIC.
    s : float
        Private signal realisation.
    prices : dict
        Equilibrium prices P(X, D).
    posteriors : dict
        Posterior engagement probabilities pi(X, D).
    E_v_dict : dict
        Conditional expectations E[v | X, D].
    params : ModelParams
        Model calibration.

    Returns
    -------
    float
        Expected payoff of the blockholder under the chosen action.
    """
    p0, p1 = noise_probs(params.kappa)

    v_post = v_hat(s, params)

    def get_price_safe(X: int, D: int) -> float:
        return prices.get((X, D), params.mu)

    def get_m_XD(X: int, D: int) -> float:
        pi = posteriors.get((X, D), 0)
        return params.m0 + (params.m_tilde - params.m0) * pi

    def get_V_hat(X: int, D: int) -> float:
        """V_hat = E[v|X,D] + Delta_tilde * pi(X,D)."""
        E_v = E_v_dict.get((X, D), params.mu)
        pi = posteriors.get((X, D), 0)
        return E_v + params.Delta_tilde * pi

    if action == Action.EXIT:  # Exit: q=-1, a=0, h=0
        # Payoff: +P(X, 0) (selling 1 share at market price)
        # X = -1 + z, so X in {-2, -1, 0}
        payoff = 0.0
        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = -1 + z
            P = get_price_safe(X, 0)
            payoff += pz * P
        return payoff

    elif action == Action.HOLD:  # Passive Hold: q=0, a=0, h=1
        # X = 0 + z, so X in {-1, 0, 1}
        payoff = 0.0
        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = z
            m_XD = get_m_XD(X, 0)
            p_bid = params.lambda_B * bid_probability(m_XD, params)
            V_hat_XD = get_V_hat(X, 0)
            # Holding h=1 share, no trading cash flow
            # Terminal: if bid, get V_hat + m0; if no bid, get v
            expected_terminal = p_bid * (V_hat_XD + params.m0) + (1 - p_bid) * v_post
            payoff += pz * params.delta * expected_terminal
        return payoff

    elif action == Action.QUIET:  # Quiet Voice: q=0, a=1, h=1
        # X = 0 + z, so X in {-1, 0, 1}
        C = engagement_cost(s, params)
        payoff = -C  # Pay engagement cost
        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = z
            m_XD = get_m_XD(X, 0)
            p_bid = params.lambda_B * bid_probability(m_XD, params)
            V_hat_XD = get_V_hat(X, 0)
            # Terminal with engagement: if bid, get V_hat + m_tilde; if no bid, get v + Delta_tilde
            expected_terminal = p_bid * (V_hat_XD + params.m_tilde) + (1 - p_bid) * (v_post + params.Delta_tilde)
            payoff += pz * params.delta * expected_terminal
        return payoff

    elif action == Action.PUBLIC:  # Public Voice: q=+1, a=1, h=2, D=1
        # X = 1 + z, so X in {0, 1, 2}
        C = engagement_cost(s, params)
        payoff = -C  # Pay engagement cost
        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = 1 + z
            P = get_price_safe(X, 1)
            m_XD = params.m_tilde  # D=1 means a=1 is known
            p_bid = params.lambda_B * bid_probability(m_XD, params)
            V_hat_XD = get_V_hat(X, 1)
            # Trading cash flow: -P (buying 1 share at market price)
            # Terminal with h=2: if bid, get 2*(V_hat + m_tilde); if no bid, get 2*(v + Delta_tilde)
            trading_cf = -P
            expected_terminal = p_bid * 2 * (V_hat_XD + params.m_tilde) + (1 - p_bid) * 2 * (v_post + params.Delta_tilde)
            payoff += pz * (trading_cf + params.delta * expected_terminal)
        return payoff

    else:
        raise ValueError(f"Unknown action: {action}")


# -- Section 4: Welfare and Minority Gains ---------------------------------


def compute_minority_gains(
    k1: float, k0: float, kD: float, params: ModelParams
) -> MinorityGains:
    """Expected minority takeover gains by exact enumeration -- Section 4.

    Iterates over all (action, noise-trader) state pairs, weighting by
    unconditional probabilities and bid incidence.

    Returns
    -------
    MinorityGains
        Named tuple (total, base, activism).
    """
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(
        k1, k0, kD, params
    )
    posteriors = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    prices, _ = compute_equilibrium_prices(k1, k0, kD, params)

    p0, p1 = noise_probs(params.kappa)

    total_gains = 0.0
    base_gains = 0.0
    activism_gains = 0.0

    # Iterate over all (action, z) combinations
    actions = [
        (Action.EXIT, -1, omega_E),
        (Action.HOLD, 0, omega_H),
        (Action.QUIET, 0, omega_Q),
        (Action.PUBLIC, 1, omega_P),
    ]

    for action, q, omega_a in actions:
        if omega_a < TOL_PROB:
            continue

        a = 1 if action in (Action.QUIET, Action.PUBLIC) else 0
        D = 1 if action == Action.PUBLIC else 0

        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = q + z

            # Skip infeasible combinations
            if D == 1 and (X, D) not in prices:
                continue
            if D == 0 and (X, D) not in prices:
                continue

            pi_XD = posteriors.get((X, D), 0)
            m_XD = params.m0 + (params.m_tilde - params.m0) * pi_XD

            p_bid = params.lambda_B * bid_probability(m_XD, params)

            # Realized premium
            m_realized = params.m_tilde if a == 1 else params.m0

            # Weight
            weight = omega_a * pz

            # Contributions
            total_gains += weight * p_bid * m_realized
            base_gains += weight * p_bid * params.m0
            activism_gains += weight * p_bid * (m_realized - params.m0)

    return MinorityGains(total=total_gains, base=base_gains, activism=activism_gains)


# -- Section 4b: Bidder Surplus and Total Welfare --------------------------


def compute_bidder_surplus_state(
    m_XD: float, params: ModelParams
) -> float:
    """Bidder expected surplus E[max(Pi_B, 0)] in a specific (X, D) state.

    The bidder's surplus from entry is xi - T where T = m_XD + K - S_bar,
    and she enters when xi > T.  The expectation of max(xi - T, 0) for
    xi ~ N(0, sigma_xi^2) is the standard truncated-normal formula.

    Note: this is the surplus conditional on a bidder arriving.
    Multiply by lambda_B for the unconditional expected surplus.
    """
    T = m_XD + params.K - params.S_bar
    z = T / params.sigma_xi
    return params.sigma_xi * norm.pdf(z) - T * (1 - norm.cdf(z))


def compute_welfare(
    k1: float, k0: float, kD: float, params: ModelParams
) -> Tuple[float, float, float, float]:
    """Compute total expected welfare and its components.

    Returns
    -------
    (W_min, W_bid, W_B, W_total):
        Minority gains, bidder surplus, blockholder utility, total surplus.
    """
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(
        k1, k0, kD, params
    )
    posteriors = compute_posteriors(
        omega_E, omega_H, omega_Q, omega_P, params.kappa
    )
    prices, E_v_dict = compute_equilibrium_prices(k1, k0, kD, params)

    p0, p1 = noise_probs(params.kappa)

    # -- Bidder welfare W_bid ----------------------------------------------
    W_bid = 0.0
    actions = [
        (Action.EXIT, -1, omega_E),
        (Action.HOLD, 0, omega_H),
        (Action.QUIET, 0, omega_Q),
        (Action.PUBLIC, 1, omega_P),
    ]
    for action, q, omega_a in actions:
        if omega_a < TOL_PROB:
            continue
        D = 1 if action == Action.PUBLIC else 0
        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = q + z
            if (X, D) not in prices:
                continue
            pi_XD = posteriors.get((X, D), 0.0)
            m_XD = params.m0 + (params.m_tilde - params.m0) * pi_XD
            surplus = params.lambda_B * compute_bidder_surplus_state(m_XD, params)
            W_bid += omega_a * pz * surplus

    # -- Blockholder welfare W_B -------------------------------------------
    s_grid = np.linspace(
        params.mu - 6 * params.sigma_s,
        params.mu + 6 * params.sigma_s,
        501,
    )
    pdf = norm.pdf(s_grid, loc=params.mu, scale=params.sigma_s)
    u_vals = np.zeros_like(s_grid)
    for i, s in enumerate(s_grid):
        if s < k1:
            act = Action.EXIT
        elif s < k0:
            act = Action.HOLD
        elif s < kD:
            act = Action.QUIET
        else:
            act = Action.PUBLIC
        u_vals[i] = compute_expected_payoff(
            act, float(s), prices, posteriors, E_v_dict, params
        )

    W_B = float(np.trapz(u_vals * pdf, s_grid))

    # -- Minority gains W_min ----------------------------------------------
    gains = compute_minority_gains(k1, k0, kD, params)
    W_min = gains.total

    W_total = W_min + W_bid + W_B
    return float(W_min), float(W_bid), float(W_B), float(W_total)


def compute_minority_gains_no_disclosure_given_strategy(
    k1: float, k0: float, kD: float, params: ModelParams
) -> MinorityGains:
    """Counterfactual minority gains when disclosure is not observed -- Section 4.

    Holds fixed the blockholder strategy (cutoffs) and recomputes inference,
    prices, and bid incidence when the market conditions only on order flow X.

    Returns
    -------
    MinorityGains
        Named tuple (total, base, activism).
    """
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(
        k1, k0, kD, params
    )
    mu_E, mu_H, mu_Q, mu_P = compute_conditional_means(k1, k0, kD, params)

    post_X = compute_posteriors_no_disclosure(
        omega_E, omega_H, omega_Q, omega_P, params.kappa
    )

    # Compute pooled prices P(X) for all X
    prices_X: Dict[int, float] = {}
    for X in [-2, -1, 0, 1, 2]:
        pi_X = post_X.get(X, 0.0)
        E_v_X = compute_E_v_given_X_no_disclosure(
            X,
            omega_E, omega_H, omega_Q, omega_P,
            mu_E, mu_H, mu_Q, mu_P,
            params.kappa
        )
        m_X = params.m0 + (params.m_tilde - params.m0) * pi_X
        p_bid_X = params.lambda_B * bid_probability(m_X, params)
        prices_X[X] = compute_price_direct(E_v_X, pi_X, p_bid_X, m_X, params)

    p0, p1 = noise_probs(params.kappa)

    total_gains = 0.0
    base_gains = 0.0
    activism_gains = 0.0

    actions = [
        (Action.EXIT, -1, omega_E),
        (Action.HOLD, 0, omega_H),
        (Action.QUIET, 0, omega_Q),
        (Action.PUBLIC, 1, omega_P),
    ]

    for action, q, omega_a in actions:
        if omega_a < TOL_PROB:
            continue

        a = 1 if action in (Action.QUIET, Action.PUBLIC) else 0
        m_realized = params.m_tilde if a == 1 else params.m0

        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = q + z
            pi_X = post_X.get(X, 0.0)
            m_X = params.m0 + (params.m_tilde - params.m0) * pi_X
            p_bid = params.lambda_B * bid_probability(m_X, params)

            weight = omega_a * pz
            total_gains += weight * p_bid * m_realized
            base_gains += weight * p_bid * params.m0
            activism_gains += weight * p_bid * (m_realized - params.m0)

    return MinorityGains(total=total_gains, base=base_gains, activism=activism_gains)


# -- Section 5: Counterfactual Information Regimes -------------------------


def compute_posteriors_no_disclosure(
    omega_E: float, omega_H: float, omega_Q: float, omega_P: float,
    kappa: float
) -> Dict[int, float]:
    """Posterior pi(X) when disclosure is not observed -- Section 5.1.

    In this counterfactual the market conditions only on order flow X
    (no D signal), so (q,a)=(+1,1) states are pooled with other D=0 states.
    """
    p0, p1 = noise_probs(kappa)

    def prob_z(z: int) -> float:
        if z == 0:
            return p0
        if z in (-1, 1):
            return p1
        return 0.0

    # (action, q, a, omega)
    actions = [
        (Action.EXIT, -1, 0, omega_E),
        (Action.HOLD, 0, 0, omega_H),
        (Action.QUIET, 0, 1, omega_Q),
        (Action.PUBLIC, 1, 1, omega_P),
    ]

    posteriors: Dict[int, float] = {}
    for X in [-2, -1, 0, 1, 2]:
        denom = 0.0
        numer = 0.0
        for _, q, a, omega in actions:
            pz = prob_z(X - q)
            if pz == 0.0 or omega < TOL_PROB:
                continue
            w = omega * pz
            denom += w
            if a == 1:
                numer += w
        posteriors[X] = (numer / denom) if denom > TOL_PROB else 0.0

    return posteriors


def compute_posteriors_full_information() -> Dict[Tuple[int, int], float]:
    """Posterior pi under full information S_FI = (q, a) -- Section 5.2.

    Returns
    -------
    dict mapping (q, a) -> pi = a.
    """
    return {(-1, 0): 0.0, (0, 0): 0.0, (0, 1): 1.0, (1, 1): 1.0}


def compute_posteriors_noisy_rumor(
    omega_E: float, omega_H: float, omega_Q: float, omega_P: float,
    kappa: float, rho1: float, rho0: float
) -> Dict[Tuple[int, int, int], float]:
    """Posterior pi under the noisy-rumor regime -- Section 5.3.

    Signal S_NR = (D, R), where D = 1{q=+1} and R is informative about
    engagement only when D=0.  Uses P(R=1|Exit) = rho0.
    """
    p0, p1 = noise_probs(kappa)

    posteriors: Dict[Tuple[int, int, int], float] = {}

    # Disclosed branch: D=1 => engagement known
    for X in [0, 1, 2]:
        for R in [0, 1]:
            posteriors[(X, 1, R)] = 1.0

    # Non-disclosed branch: D=0
    for R in [0, 1]:
        posteriors[(-2, 0, R)] = 0.0

    # X = 1, D = 0: q=0 pinned down
    denom_r1 = omega_Q * rho1 + omega_H * rho0
    denom_r0 = omega_Q * (1 - rho1) + omega_H * (1 - rho0)
    posteriors[(1, 0, 1)] = (omega_Q * rho1 / denom_r1) if denom_r1 > TOL_PROB else 0.0
    posteriors[(1, 0, 0)] = (omega_Q * (1 - rho1) / denom_r0) if denom_r0 > TOL_PROB else 0.0

    # X = -1, D = 0: q in {-1,0}
    denom_m1_r1 = (omega_H * p1 + omega_E * p0) * rho0 + omega_Q * p1 * rho1
    denom_m1_r0 = (omega_H * p1 + omega_E * p0) * (1 - rho0) + omega_Q * p1 * (1 - rho1)
    posteriors[(-1, 0, 1)] = (omega_Q * p1 * rho1 / denom_m1_r1) if denom_m1_r1 > TOL_PROB else 0.0
    posteriors[(-1, 0, 0)] = (omega_Q * p1 * (1 - rho1) / denom_m1_r0) if denom_m1_r0 > TOL_PROB else 0.0

    # X = 0, D = 0: q in {-1,0}
    denom_0_r1 = (omega_H * p0 + omega_E * p1) * rho0 + omega_Q * p0 * rho1
    denom_0_r0 = (omega_H * p0 + omega_E * p1) * (1 - rho0) + omega_Q * p0 * (1 - rho1)
    posteriors[(0, 0, 1)] = (omega_Q * p0 * rho1 / denom_0_r1) if denom_0_r1 > TOL_PROB else 0.0
    posteriors[(0, 0, 0)] = (omega_Q * p0 * (1 - rho1) / denom_0_r0) if denom_0_r0 > TOL_PROB else 0.0

    return posteriors


def compute_premium_wedges_full_information(
    params: ModelParams
) -> Dict[Tuple[int, int], float]:
    """Takeover premium m under full information S_FI = (q, a) -- Section 5.2."""
    posteriors = compute_posteriors_full_information()
    return {k: params.m0 + (params.m_tilde - params.m0) * v for k, v in posteriors.items()}


def compute_premium_wedges_no_disclosure(
    omega_E: float, omega_H: float, omega_Q: float, omega_P: float,
    kappa: float, params: ModelParams
) -> Dict[int, float]:
    """Takeover premium m under the no-disclosure regime -- Section 5.1."""
    posteriors = compute_posteriors_no_disclosure(omega_E, omega_H, omega_Q, omega_P, kappa)
    return {k: params.m0 + (params.m_tilde - params.m0) * v for k, v in posteriors.items()}


def compute_premium_wedges_noisy_rumor(
    omega_E: float, omega_H: float, omega_Q: float, omega_P: float,
    kappa: float, rho1: float, rho0: float, params: ModelParams
) -> Dict[Tuple[int, int, int], float]:
    """Takeover premium m under the noisy-rumor regime -- Section 5.3."""
    posteriors = compute_posteriors_noisy_rumor(omega_E, omega_H, omega_Q, omega_P, kappa, rho1, rho0)
    return {k: params.m0 + (params.m_tilde - params.m0) * v for k, v in posteriors.items()}


def compute_minority_gains_noisy_rumor(
    k1: float, k0: float, kD: float, params: ModelParams,
    eta_1: float, eta_0: float,
) -> MinorityGains:
    """Expected minority gains under the noisy-rumor regime (partial equilibrium).

    Holds fixed the blockholder's strategy (cutoffs) and augments the
    market's information set with a binary rumor signal R.  The rumor fires
    with probability eta_1 when the blockholder engages and eta_0 otherwise.

    Parameters
    ----------
    k1, k0, kD : float
        Equilibrium cutoffs (held fixed from the baseline).
    params : ModelParams
        Model calibration.
    eta_1 : float
        True-positive rumor probability (P(R=1 | a=1)).
    eta_0 : float
        False-positive rumor probability (P(R=1 | a=0)).

    Returns
    -------
    MinorityGains
        Named tuple (total, base, activism).
    """
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(
        k1, k0, kD, params
    )
    mu_E, mu_H, mu_Q, mu_P = compute_conditional_means(k1, k0, kD, params)
    post_R = compute_posteriors_noisy_rumor(
        omega_E, omega_H, omega_Q, omega_P, params.kappa, eta_1, eta_0
    )

    # Compute prices P(X, D, R) for the augmented state space
    prices_R: Dict[Tuple[int, int, int], float] = {}
    p0, p1 = noise_probs(params.kappa)

    for X in [-2, -1, 0, 1, 2]:
        for D in [0, 1]:
            if D == 1 and X < 0:
                continue
            for R in [0, 1]:
                if (X, D, R) not in post_R:
                    continue
                pi_XDR = post_R[(X, D, R)]

                # E[v | X, D, R]
                if D == 1:
                    E_v = mu_P
                elif X == -2:
                    E_v = mu_E
                elif X == 1:
                    wH = omega_H * (eta_0 if R == 1 else 1 - eta_0)
                    wQ = omega_Q * (eta_1 if R == 1 else 1 - eta_1)
                    denom = wH + wQ
                    E_v = (
                        (wH * mu_H + wQ * mu_Q) / denom
                        if denom > TOL_PROB
                        else (mu_H + mu_Q) / 2
                    )
                elif X == -1:
                    wE = omega_E * p0 * (eta_0 if R == 1 else 1 - eta_0)
                    wH = omega_H * p1 * (eta_0 if R == 1 else 1 - eta_0)
                    wQ = omega_Q * p1 * (eta_1 if R == 1 else 1 - eta_1)
                    denom = wE + wH + wQ
                    E_v = (
                        (wE * mu_E + wH * mu_H + wQ * mu_Q) / denom
                        if denom > TOL_PROB
                        else (mu_E + mu_H + mu_Q) / 3
                    )
                else:  # X == 0
                    wE = omega_E * p1 * (eta_0 if R == 1 else 1 - eta_0)
                    wH = omega_H * p0 * (eta_0 if R == 1 else 1 - eta_0)
                    wQ = omega_Q * p0 * (eta_1 if R == 1 else 1 - eta_1)
                    denom = wE + wH + wQ
                    E_v = (
                        (wE * mu_E + wH * mu_H + wQ * mu_Q) / denom
                        if denom > TOL_PROB
                        else (mu_E + mu_H + mu_Q) / 3
                    )

                m_XDR = params.m0 + (params.m_tilde - params.m0) * pi_XDR
                p_bid_XDR = params.lambda_B * bid_probability(m_XDR, params)
                prices_R[(X, D, R)] = compute_price_direct(
                    E_v, pi_XDR, p_bid_XDR, m_XDR, params
                )

    # Enumerate (action, noise, rumor) states to compute gains
    total_gains = 0.0
    base_gains = 0.0
    activism_gains = 0.0

    actions = [
        (Action.EXIT, -1, omega_E),
        (Action.HOLD, 0, omega_H),
        (Action.QUIET, 0, omega_Q),
        (Action.PUBLIC, 1, omega_P),
    ]

    for action, q, omega_a in actions:
        if omega_a < TOL_PROB:
            continue
        a = 1 if action in (Action.QUIET, Action.PUBLIC) else 0
        D = 1 if action == Action.PUBLIC else 0
        m_realized = params.m_tilde if a == 1 else params.m0

        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = q + z
            for R in [0, 1]:
                # Rumor probability conditional on action
                if D == 1:
                    pR = 1.0 if R == 1 else 0.0
                else:
                    pR = (
                        (eta_1 if R == 1 else 1 - eta_1)
                        if a == 1
                        else (eta_0 if R == 1 else 1 - eta_0)
                    )

                if pR < TOL_PROB:
                    continue

                weight = omega_a * pz * pR
                pi_XDR = post_R.get((X, D, R), 0.0)
                m_XDR = params.m0 + (params.m_tilde - params.m0) * pi_XDR
                p_bid = params.lambda_B * bid_probability(m_XDR, params)

                total_gains += weight * p_bid * m_realized
                base_gains += weight * p_bid * params.m0
                activism_gains += weight * p_bid * (m_realized - params.m0)

    return MinorityGains(
        total=total_gains, base=base_gains, activism=activism_gains
    )


def compute_E_v_given_X_no_disclosure(
    X: int,
    omega_E: float, omega_H: float, omega_Q: float, omega_P: float,
    mu_E: float, mu_H: float, mu_Q: float, mu_P: float,
    kappa: float
) -> float:
    """E[v | X] when disclosure is not observed -- Section 5.1.

    Pools over all actions (including Public Voice) since the market
    does not observe the disclosure signal D.
    """
    p0, p1 = noise_probs(kappa)

    def prob_z(z: int) -> float:
        if z == 0:
            return p0
        if z in (-1, 1):
            return p1
        return 0.0

    # (q, mu, omega)
    actions = [
        (-1, mu_E, omega_E),
        (0, mu_H, omega_H),
        (0, mu_Q, omega_Q),
        (1, mu_P, omega_P),
    ]

    denom = 0.0
    numer = 0.0
    for q, mu_a, omega in actions:
        pz = prob_z(X - q)
        if pz == 0.0 or omega < TOL_PROB:
            continue
        w = omega * pz
        denom += w
        numer += w * mu_a

    if denom < TOL_PROB:
        return float(np.mean([mu_E, mu_H, mu_Q, mu_P]))
    return numer / denom
```

---

## File: `numerical/solver.py`

```python
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

# Numba accel module has not yet been updated for the new pricing structure
# (bid_probability signature change, compute_price_direct, lambda_B).
# Disable until accel.py is brought in sync.
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
    prices, E_v_dict = compute_equilibrium_prices(k1, k0, kD, params)

    def U(action: Action, s: float) -> float:
        return compute_expected_payoff(action, float(s), prices, post, E_v_dict, params)

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
        prices, E_v_dict = compute_equilibrium_prices(k1, k0, kD, params)

        def U(action: Action, s: float) -> float:
            return compute_expected_payoff(
                action, float(s), prices, posteriors, E_v_dict, params
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
```
