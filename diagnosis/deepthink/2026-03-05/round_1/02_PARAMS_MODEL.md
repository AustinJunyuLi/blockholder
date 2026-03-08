# Core Economics: Parameters and Model

## evt_codebase/numerical/params.py

```python
"""Parameter and type definitions for the numerical exercise.

Notation matches `draft_v3.tex`.

Key objects:
- Action set: Exit, Hold, Quiet Voice, Public Voice
- Cutoffs: (k1, k0, kD)
- ModelParams: baseline calibration + derived quantities
"""

from __future__ import annotations

import dataclasses
import enum
from dataclasses import dataclass
from typing import NamedTuple

import numpy as np

# -----------------------------------------------------------------------------
# Numerical tolerances
# -----------------------------------------------------------------------------

TOL_PROB: float = 1e-12        # treat probabilities below as 0
TOL_CONVERGE: float = 1e-7     # fixed-point cutoff convergence
TOL_RESIDUAL: float = 5e-3     # acceptable max cutoff indifference residual
TOL_REGION: float = 1e-5       # treat regions narrower than this as collapsed

# Integration / grids
SIGMA_GRID: float = 6.0        # integrate over s in [mu-6*sigma_s, mu+6*sigma_s]


# -----------------------------------------------------------------------------
# Actions
# -----------------------------------------------------------------------------

class Action(enum.Enum):
    """Blockholder action.

    EXIT   : (q=-1, a=0)
    HOLD   : (q=0,  a=0)
    QUIET  : (q=0,  a=1)
    PUBLIC : (q=+1, a=1)  (stake-triggered disclosure)
    """

    EXIT = "E"
    HOLD = "H"
    QUIET = "Q"
    PUBLIC = "P"


class Cutoffs(NamedTuple):
    """Equilibrium cutoffs (k1, k0, kD) with weak ordering k1 <= k0 <= kD."""

    k1: float
    k0: float
    kD: float


class MinorityGains(NamedTuple):
    """Minority takeover gains decomposition (Eq. (decomp) in the paper)."""

    total: float
    base: float
    activism: float


@dataclass(frozen=True)
class ModelParams:
    """Model parameters.

    Fundamentals:
        v ~ N(mu, sigma_v^2)
        s = v + eps, eps ~ N(0, sigma_eps^2)

    Liquidity:
        z ∈ {-1,0,1} with P(0)=1-2kappa/3, P(±1)=kappa/3

    Engagement:
        C(s) = C0 * exp(-chi * (s-mu)/sigma_s)
        success prob rho; improvement Delta; premium wedge m0→m1

    Takeover:
        bidder arrives with prob lambda_B
        synergy shock xi ~ Logistic(0, s_xi)
        entry depends on inferred engagement π(X,D)

    Discounting:
        delta

    Baseline calibration defaults match the paper.
    """

    # Fundamentals
    mu: float = 1.0
    sigma_v: float = 0.50
    sigma_eps: float = 0.50

    # Liquidity
    kappa: float = 0.50

    # Engagement
    C0: float = 0.25
    chi: float = 0.50
    rho: float = 0.90
    Delta: float = 0.25

    # Takeover terms
    m0: float = 0.10
    # Chosen to deliver a clean single-peaked Δ^{min}(κ) in the baseline sweep.
    m1: float = 0.45
    S_bar: float = 1.10
    Delta_S: float = 0.30
    K: float = 0.15
    s_xi: float = 0.15
    lambda_B: float = 0.20

    # Discount factor
    delta: float = 0.95

    # ------------------------------------------------------------------
    # Derived quantities
    # ------------------------------------------------------------------

    @property
    def sigma_s(self) -> float:
        return float(np.sqrt(self.sigma_v**2 + self.sigma_eps**2))

    @property
    def beta(self) -> float:
        # Posterior weight on signal (E[v|s] = mu + beta(s-mu))
        return float(self.sigma_v**2 / (self.sigma_v**2 + self.sigma_eps**2))

    @property
    def Delta_tilde(self) -> float:
        # Expected fundamental improvement under engagement
        return float(self.rho * self.Delta)

    @property
    def m_tilde(self) -> float:
        # Expected premium wedge under engagement
        return float(self.m0 + self.rho * (self.m1 - self.m0))

    @property
    def net_deterrence(self) -> bool:
        # Assumption (A5): Delta_tilde + m_tilde - m0 > Delta_S
        return (self.Delta_tilde + self.m_tilde - self.m0) > self.Delta_S

    def replace(self, **kwargs) -> "ModelParams":
        return dataclasses.replace(self, **kwargs)
```

## evt_codebase/numerical/model.py

```python
"""Core economic functions for the numerical exercise.

This module is the *source of truth* for implementing the model primitives in
`draft_v3.tex`. It is intentionally explicit rather than clever.

Objects implemented:

- Noise distribution z and order flow X = q + z
- Signal posterior v_hat(s) and engagement cost C(s)
- Action probabilities ω_a and conditional means μ_a
- Posteriors π(X,D) (baseline disclosure) and counterfactual posteriors
- Conditional means E[v|X,D] and pricing objects V_hat, m_bar, p(X,D), P_post, P_trade
- Payoffs U(q,a|s)
- Minority gains Δ^min and decomposition
- Welfare components (minority, bidder, blockholder, total)

All formulas are coded to match the paper's equations and propositions.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Mapping, Tuple

import numpy as np
from scipy.special import expit
from scipy.stats import norm

from .params import (
    Action,
    MinorityGains,
    ModelParams,
    SIGMA_GRID,
    TOL_PROB,
)

# States
XD = Tuple[int, int]          # (X, D)
XDR = Tuple[int, int, int]    # (X, D, R)


# -----------------------------------------------------------------------------
# Noise distribution
# -----------------------------------------------------------------------------

def noise_probs(kappa: float) -> Tuple[float, float]:
    """Return (p0, p1) where

    - p0 = P(z=0) = 1 - 2*kappa/3
    - p1 = P(z=+1) = P(z=-1) = kappa/3

    Requires kappa in [0,1].
    """
    if not (0.0 <= kappa <= 1.0):
        raise ValueError(f"kappa must be in [0,1], got {kappa}")
    p0 = 1.0 - (2.0 / 3.0) * kappa
    p1 = (1.0 / 3.0) * kappa
    return float(p0), float(p1)


# -----------------------------------------------------------------------------
# Information structure
# -----------------------------------------------------------------------------

def engagement_cost(s: float, params: ModelParams) -> float:
    """Engagement cost C(s) = C0 * exp(-chi*(s-mu)/sigma_s)."""
    z = (s - params.mu) / params.sigma_s
    return float(params.C0 * np.exp(-params.chi * z))


def v_hat(s: float, params: ModelParams) -> float:
    """Posterior mean E[v|s] for Gaussian signal structure."""
    return float(params.mu + params.beta * (s - params.mu))


# -----------------------------------------------------------------------------
# Action probabilities and conditional means
# -----------------------------------------------------------------------------

def compute_action_probabilities(k1: float, k0: float, kD: float, params: ModelParams) -> Tuple[float, float, float, float]:
    """Unconditional action probabilities (ω_E, ω_H, ω_Q, ω_P)."""
    alpha1 = (k1 - params.mu) / params.sigma_s
    alpha0 = (k0 - params.mu) / params.sigma_s
    alphaD = (kD - params.mu) / params.sigma_s

    omega_E = float(norm.cdf(alpha1))
    omega_H = float(norm.cdf(alpha0) - norm.cdf(alpha1))
    omega_Q = float(norm.cdf(alphaD) - norm.cdf(alpha0))
    omega_P = float(1.0 - norm.cdf(alphaD))

    # numerical guard
    omega_E = max(0.0, omega_E)
    omega_H = max(0.0, omega_H)
    omega_Q = max(0.0, omega_Q)
    omega_P = max(0.0, omega_P)

    # normalize (rarely needed; just protects against tiny rounding drift)
    tot = omega_E + omega_H + omega_Q + omega_P
    if tot <= TOL_PROB:
        return 0.0, 0.0, 0.0, 0.0
    return omega_E / tot, omega_H / tot, omega_Q / tot, omega_P / tot


def _inv_mills_left(alpha: float) -> float:
    """λ_L(α) = φ(α)/Φ(α) with a stable tail fallback."""
    cdf = float(norm.cdf(alpha))
    if cdf < TOL_PROB:
        # As α→-∞, φ/Φ ~ -α (Mills ratio asymptotic)
        return float(-alpha)
    return float(norm.pdf(alpha) / cdf)


def _inv_mills_right(alpha: float) -> float:
    """λ_U(α) = φ(α)/(1-Φ(α)) with a stable tail fallback."""
    ccdf = float(1.0 - norm.cdf(alpha))
    if ccdf < TOL_PROB:
        # As α→+∞, φ/(1-Φ) ~ α
        return float(alpha)
    return float(norm.pdf(alpha) / ccdf)


def compute_conditional_means(k1: float, k0: float, kD: float, params: ModelParams) -> Tuple[float, float, float, float]:
    """Conditional means (μ_E, μ_H, μ_Q, μ_P) as in Proposition 2 proof.

    These are E[v | s in region] where regions correspond to the cutoff strategy.
    """
    alpha1 = (k1 - params.mu) / params.sigma_s
    alpha0 = (k0 - params.mu) / params.sigma_s
    alphaD = (kD - params.mu) / params.sigma_s

    # Exit region: s < k1
    mu_E = params.mu - params.beta * params.sigma_s * _inv_mills_left(alpha1)

    # Hold region: k1 <= s < k0
    denom_H = float(norm.cdf(alpha0) - norm.cdf(alpha1))
    if denom_H > TOL_PROB:
        mu_H = params.mu + params.beta * params.sigma_s * (norm.pdf(alpha1) - norm.pdf(alpha0)) / denom_H
    else:
        # collapsed region fallback: mean at midpoint (should not matter on-path)
        mu_H = v_hat(0.5 * (k1 + k0), params)

    # Quiet region: k0 <= s < kD
    denom_Q = float(norm.cdf(alphaD) - norm.cdf(alpha0))
    if denom_Q > TOL_PROB:
        mu_Q = params.mu + params.beta * params.sigma_s * (norm.pdf(alpha0) - norm.pdf(alphaD)) / denom_Q
    else:
        mu_Q = v_hat(0.5 * (k0 + kD), params)

    # Public region: s >= kD
    mu_P = params.mu + params.beta * params.sigma_s * _inv_mills_right(alphaD)

    return float(mu_E), float(mu_H), float(mu_Q), float(mu_P)


# -----------------------------------------------------------------------------
# Baseline disclosure posteriors π(X,D)
# -----------------------------------------------------------------------------

def compute_posteriors(omega_E: float, omega_H: float, omega_Q: float, omega_P: float, kappa: float) -> Dict[XD, float]:
    """Posterior π(X,D)=P(a=1|X,D) in the baseline disclosure regime.

    Implements Proposition 2.

    Returns dict keyed by (X,D) for the 7 on-/near-path states.
    """
    p0, p1 = noise_probs(kappa)

    post: Dict[XD, float] = {}

    # disclosed states (D=1): engagement known
    for X in (0, 1, 2):
        post[(X, 1)] = 1.0

    # nondisclosed states (D=0)
    post[(-2, 0)] = 0.0

    denom_10 = omega_H + omega_Q
    post[(1, 0)] = float(omega_Q / denom_10) if denom_10 > TOL_PROB else 0.0

    denom_m10 = (omega_H + omega_Q) * p1 + omega_E * p0
    post[(-1, 0)] = float(omega_Q * p1 / denom_m10) if denom_m10 > TOL_PROB else 0.0

    denom_00 = (omega_H + omega_Q) * p0 + omega_E * p1
    post[(0, 0)] = float(omega_Q * p0 / denom_00) if denom_00 > TOL_PROB else 0.0

    return post


# -----------------------------------------------------------------------------
# Conditional mean E[v | X,D]
# -----------------------------------------------------------------------------

def compute_E_v_given_XD(
    X: int,
    D: int,
    omega_E: float,
    omega_H: float,
    omega_Q: float,
    omega_P: float,
    mu_E: float,
    mu_H: float,
    mu_Q: float,
    mu_P: float,
    kappa: float,
) -> float:
    """Compute E[v | X,D] for reached states.

    Matches the formulas in the equilibrium characterization.
    """
    p0, p1 = noise_probs(kappa)

    if D == 1:
        # only Public Voice possible
        return float(mu_P)

    # D == 0
    if X == -2:
        return float(mu_E)

    if X == 1:
        denom = omega_H + omega_Q
        if denom <= TOL_PROB:
            return float(0.5 * (mu_H + mu_Q))
        return float((omega_H * mu_H + omega_Q * mu_Q) / denom)

    if X == -1:
        denom = (omega_H + omega_Q) * p1 + omega_E * p0
        if denom <= TOL_PROB:
            return float((mu_E + mu_H + mu_Q) / 3.0)
        return float(((omega_H * mu_H + omega_Q * mu_Q) * p1 + omega_E * mu_E * p0) / denom)

    if X == 0:
        denom = (omega_H + omega_Q) * p0 + omega_E * p1
        if denom <= TOL_PROB:
            return float((mu_E + mu_H + mu_Q) / 3.0)
        return float(((omega_H * mu_H + omega_Q * mu_Q) * p0 + omega_E * mu_E * p1) / denom)

    raise ValueError(f"E[v|X,D] requested for infeasible state X={X}, D={D}")


# -----------------------------------------------------------------------------
# Bid probability and pricing
# -----------------------------------------------------------------------------

def bid_probability_tilde(V_hat_XD: float, m_bar_XD: float, pi_XD: float, params: ModelParams) -> float:
    r"""Conditional bid probability \tilde{p}(X,D) given bidder arrival.

    Eq. (bid-prob):

        \tilde{p}(X,D) = 1 - \Lambda( (V_hat + m_bar + K - (S_bar + pi*Delta_S)) / s_xi )

    with \Lambda the standard logistic CDF.

    For Logistic(0,s), 1-\Lambda(t/s) = expit(-t/s).
    """
    T_raw = V_hat_XD + m_bar_XD + params.K - (params.S_bar + pi_XD * params.Delta_S)
    return float(expit(-T_raw / params.s_xi))


def bid_probability(V_hat_XD: float, m_bar_XD: float, pi_XD: float, params: ModelParams) -> float:
    r"""Unconditional bid probability p(X,D) = lambda_B * \tilde{p}(X,D)."""
    return float(params.lambda_B * bid_probability_tilde(V_hat_XD, m_bar_XD, pi_XD, params))


def price_post(V_hat_XD: float, p_bid: float, m_bar_XD: float, params: ModelParams) -> float:
    """Post-disclosure price P_post(X,D) = δ [ V_hat + p * m_bar ]."""
    return float(params.delta * (V_hat_XD + p_bid * m_bar_XD))


# -----------------------------------------------------------------------------
# Equilibrium objects for a given cutoff triple
# -----------------------------------------------------------------------------

@dataclass(frozen=True)
class EquilibriumObjects:
    """Container for equilibrium objects computed from cutoffs and params."""

    omega_E: float
    omega_H: float
    omega_Q: float
    omega_P: float
    mu_E: float
    mu_H: float
    mu_Q: float
    mu_P: float
    posteriors: Dict[XD, float]
    E_v: Dict[XD, float]
    P_post: Dict[XD, float]
    P_trade: Dict[int, float]
    prob_XD: Dict[XD, float]   # unconditional probability of (X,D)


def compute_equilibrium_objects(k1: float, k0: float, kD: float, params: ModelParams) -> EquilibriumObjects:
    """Compute all equilibrium objects implied by cutoffs (k1,k0,kD).

    This is the workhorse used by the solver and exporters.
    """
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    mu_E, mu_H, mu_Q, mu_P = compute_conditional_means(k1, k0, kD, params)
    post = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)

    # Conditional means E[v|X,D]
    E_v: Dict[XD, float] = {}
    # Prices P_post
    P_post: Dict[XD, float] = {}

    # Compute for the 7 feasible states
    feasible_states: List[XD] = [(-2, 0), (-1, 0), (0, 0), (1, 0), (0, 1), (1, 1), (2, 1)]

    for X, D in feasible_states:
        pi = post.get((X, D), 0.0)
        # E[v|X,D]
        if D == 1:
            E_v_XD = mu_P
        else:
            E_v_XD = compute_E_v_given_XD(
                X, D,
                omega_E, omega_H, omega_Q, omega_P,
                mu_E, mu_H, mu_Q, mu_P,
                params.kappa,
            )
        E_v[(X, D)] = float(E_v_XD)

        V_hat_XD = float(E_v_XD + params.Delta_tilde * pi)
        m_bar_XD = float(params.m0 + (params.m_tilde - params.m0) * pi)
        p_bid = bid_probability(V_hat_XD, m_bar_XD, pi, params)
        P_post[(X, D)] = price_post(V_hat_XD, p_bid, m_bar_XD, params)

    # Joint distribution of (X,D) given action probabilities and noise
    p0, p1 = noise_probs(params.kappa)
    prob_XD: Dict[XD, float] = {}

    # action list: (q, D, omega)
    actions: List[Tuple[int, int, float]] = [
        (-1, 0, omega_E),
        (0, 0, omega_H),
        (0, 0, omega_Q),
        (1, 1, omega_P),
    ]

    for q, D, omega in actions:
        if omega < TOL_PROB:
            continue
        for z, pz in ((-1, p1), (0, p0), (1, p1)):
            key = (q + z, D)
            prob_XD[key] = prob_XD.get(key, 0.0) + omega * pz

    # Anonymous execution prices P_trade(X) = E[P_post(X,D) | X]
    P_trade: Dict[int, float] = {}
    for X in (-2, -1, 0, 1, 2):
        pr_X = prob_XD.get((X, 0), 0.0) + prob_XD.get((X, 1), 0.0)
        if pr_X < TOL_PROB:
            continue
        val = 0.0
        for D in (0, 1):
            pr = prob_XD.get((X, D), 0.0)
            if pr < TOL_PROB:
                continue
            if (X, D) not in P_post:
                continue
            val += (pr / pr_X) * P_post[(X, D)]
        P_trade[X] = float(val)

    return EquilibriumObjects(
        omega_E=omega_E,
        omega_H=omega_H,
        omega_Q=omega_Q,
        omega_P=omega_P,
        mu_E=mu_E,
        mu_H=mu_H,
        mu_Q=mu_Q,
        mu_P=mu_P,
        posteriors=post,
        E_v=E_v,
        P_post=P_post,
        P_trade=P_trade,
        prob_XD=prob_XD,
    )


# -----------------------------------------------------------------------------
# Payoffs
# -----------------------------------------------------------------------------

def _p_z(z: int, p0: float, p1: float) -> float:
    if z == 0:
        return p0
    if z in (-1, 1):
        return p1
    return 0.0


def compute_expected_payoff(action: Action, s: float, eq: EquilibriumObjects, params: ModelParams) -> float:
    r"""Compute the blockholder's expected utility U(action | s).

    Utility definition (Eq. U-def in paper):

        U(q,a|s) = E[ -q P_trade(X) + δ h Y - a C(s) | s, q, a ]

    where h is the terminal shareholdings (1 for Exit/Hold/Quiet, 2 for Public).

    Terminal per-share payoff Y:

    - if bid occurs: \hat{V}(X,D) + m^R(a)
    - if no bid:     v + a \tilde{\Delta}

    Bid probability is p(X,D) determined by market inference.
    """

    p0, p1 = noise_probs(params.kappa)
    v_post = v_hat(s, params)
    C = engagement_cost(s, params)

    if action == Action.EXIT:
        q, a, h, D = -1, 0, 0, 0
    elif action == Action.HOLD:
        q, a, h, D = 0, 0, 1, 0
    elif action == Action.QUIET:
        q, a, h, D = 0, 1, 1, 0
    elif action == Action.PUBLIC:
        q, a, h, D = 1, 1, 2, 1
    else:
        raise ValueError(f"Unknown action {action}")

    m_realized = params.m_tilde if a == 1 else params.m0

    # Upfront cost
    util = -a * C

    # Expectation over z
    for z in (-1, 0, 1):
        pz = _p_z(z, p0, p1)
        if pz < TOL_PROB:
            continue

        X = q + z

        # Trading cash flow at t=1
        if q != 0:
            P_exec = eq.P_trade.get(X, params.mu)
            util += pz * (-q * P_exec)

        # Terminal expected payoff per share
        if h == 0:
            continue

        # Determine relevant posterior state
        if D == 1:
            # public voice always implies D=1
            pi = 1.0
            E_v_XD = eq.E_v[(X, 1)]
        else:
            pi = eq.posteriors.get((X, 0), 0.0)
            E_v_XD = eq.E_v[(X, 0)]

        V_hat_XD = float(E_v_XD + params.Delta_tilde * pi)
        m_bar_XD = float(params.m0 + (params.m_tilde - params.m0) * pi)
        p_bid = bid_probability(V_hat_XD, m_bar_XD, pi, params)

        per_share_terminal = p_bid * (V_hat_XD + m_realized) + (1.0 - p_bid) * (v_post + a * params.Delta_tilde)

        util += pz * params.delta * h * per_share_terminal

    return float(util)


# -----------------------------------------------------------------------------
# Minority gains and welfare
# -----------------------------------------------------------------------------

def compute_minority_gains(k1: float, k0: float, kD: float, params: ModelParams) -> MinorityGains:
    """Compute Δ^min, its base component, and activism component.

    Definition (Eq. (minority)):
        Δ^min = E[m^R(a) * 1{bid}]

    Decomposition (Eq. (decomp)):
        Δ^min = m0 * P(bid) + (m_tilde - m0) * E[ π(X,D) * 1{bid} ]

    Numerically, we enumerate actions, noise, and use p(X,D) from equilibrium objects.
    """

    eq = compute_equilibrium_objects(k1, k0, kD, params)
    p0, p1 = noise_probs(params.kappa)

    actions: List[Tuple[Action, int, int, float]] = [
        (Action.EXIT, -1, 0, eq.omega_E),
        (Action.HOLD, 0, 0, eq.omega_H),
        (Action.QUIET, 0, 0, eq.omega_Q),
        (Action.PUBLIC, 1, 1, eq.omega_P),
    ]

    total = 0.0
    base = 0.0
    act = 0.0

    for act_name, q, D, omega in actions:
        if omega < TOL_PROB:
            continue
        a = 1 if act_name in (Action.QUIET, Action.PUBLIC) else 0
        m_realized = params.m_tilde if a == 1 else params.m0

        for z, pz in ((-1, p1), (0, p0), (1, p1)):
            if pz < TOL_PROB:
                continue
            X = q + z
            # posterior state uses market inference (depends on X,D)
            if (X, D) not in eq.E_v:
                continue
            pi = 1.0 if D == 1 else eq.posteriors.get((X, 0), 0.0)
            E_v_XD = eq.E_v[(X, D)]
            V_hat_XD = float(E_v_XD + params.Delta_tilde * pi)
            m_bar_XD = float(params.m0 + (params.m_tilde - params.m0) * pi)
            p_bid = bid_probability(V_hat_XD, m_bar_XD, pi, params)

            w = omega * pz
            total += w * p_bid * m_realized
            base += w * p_bid * params.m0
            act += w * p_bid * (m_realized - params.m0)

    return MinorityGains(total=float(total), base=float(base), activism=float(act))


def compute_bidder_surplus_state(V_hat_XD: float, m_bar_XD: float, pi_XD: float, params: ModelParams) -> float:
    """Expected bidder surplus E[max(ξ - T, 0)] in a given state.

    With ξ ~ Logistic(0, s_xi) and threshold
        T = V_hat + m_bar + K - (S_bar + pi*Delta_S),

    we need E[max(ξ - T, 0)]. For the logistic distribution this has the
    closed form:

        s_xi * ln(1 + exp(-T/s_xi)).

    (This is the integral of the logistic survival function.)
    """
    T_raw = V_hat_XD + m_bar_XD + params.K - (params.S_bar + pi_XD * params.Delta_S)
    return float(params.s_xi * np.logaddexp(0.0, -T_raw / params.s_xi))


def compute_welfare(k1: float, k0: float, kD: float, params: ModelParams) -> Tuple[float, float, float, float]:
    """Compute welfare components (W_min, W_bid, W_B, W_tot).

    Paper definition (Section 7):

        W_min = Δ^min
        W_bid = E[max(Π_B,0)] (bidder surplus)
        W_B   = E[ U(q*,a*|s) ] (blockholder welfare)
        W_tot = W_min + W_bid + W_B

    Implementation:
    - W_min from compute_minority_gains
    - W_bid by enumerating (action, z) states and using closed-form logistic surplus
    - W_B by integrating U(s) over the signal distribution

    Note: W_min is an *expected premium* (not discounted) by paper definition.
    """

    eq = compute_equilibrium_objects(k1, k0, kD, params)
    p0, p1 = noise_probs(params.kappa)

    # Bidder surplus
    W_bid = 0.0
    actions: List[Tuple[Action, int, int, float]] = [
        (Action.EXIT, -1, 0, eq.omega_E),
        (Action.HOLD, 0, 0, eq.omega_H),
        (Action.QUIET, 0, 0, eq.omega_Q),
        (Action.PUBLIC, 1, 1, eq.omega_P),
    ]

    for act_name, q, D, omega in actions:
        if omega < TOL_PROB:
            continue
        for z, pz in ((-1, p1), (0, p0), (1, p1)):
            if pz < TOL_PROB:
                continue
            X = q + z
            if (X, D) not in eq.E_v:
                continue
            pi = 1.0 if D == 1 else eq.posteriors.get((X, 0), 0.0)
            E_v_XD = eq.E_v[(X, D)]
            V_hat_XD = float(E_v_XD + params.Delta_tilde * pi)
            m_bar_XD = float(params.m0 + (params.m_tilde - params.m0) * pi)

            surplus = params.lambda_B * compute_bidder_surplus_state(V_hat_XD, m_bar_XD, pi, params)
            W_bid += omega * pz * surplus

    # Blockholder welfare: integrate expected utility over s
    s_min = params.mu - SIGMA_GRID * params.sigma_s
    s_max = params.mu + SIGMA_GRID * params.sigma_s
    s_grid = np.linspace(s_min, s_max, 801)
    pdf = norm.pdf(s_grid, loc=params.mu, scale=params.sigma_s)

    U_vals = np.zeros_like(s_grid)
    for i, s in enumerate(s_grid):
        if s < k1:
            act = Action.EXIT
        elif s < k0:
            act = Action.HOLD
        elif s < kD:
            act = Action.QUIET
        else:
            act = Action.PUBLIC
        U_vals[i] = compute_expected_payoff(act, float(s), eq, params)

    W_B = float(np.trapezoid(U_vals * pdf, s_grid))

    gains = compute_minority_gains(k1, k0, kD, params)
    W_min = float(gains.total)

    W_tot = float(W_min + W_bid + W_B)

    return float(W_min), float(W_bid), float(W_B), float(W_tot)


# -----------------------------------------------------------------------------
# Counterfactual information regimes
# -----------------------------------------------------------------------------

def compute_posteriors_no_disclosure(
    omega_E: float, omega_H: float, omega_Q: float, omega_P: float, kappa: float
) -> Dict[int, float]:
    """Posterior π(X) when the market observes only X (no disclosure signal D)."""
    p0, p1 = noise_probs(kappa)

    def pr_z(z: int) -> float:
        if z == 0:
            return p0
        if z in (-1, 1):
            return p1
        return 0.0

    # actions: (q, a, omega)
    acts = [
        (-1, 0, omega_E),
        (0, 0, omega_H),
        (0, 1, omega_Q),
        (1, 1, omega_P),
    ]

    post: Dict[int, float] = {}
    for X in (-2, -1, 0, 1, 2):
        denom = 0.0
        numer = 0.0
        for q, a, omega in acts:
            if omega < TOL_PROB:
                continue
            pz = pr_z(X - q)
            if pz < TOL_PROB:
                continue
            w = omega * pz
            denom += w
            if a == 1:
                numer += w
        post[X] = float(numer / denom) if denom > TOL_PROB else 0.0

    return post


def compute_E_v_given_X_no_disclosure(
    X: int,
    omega_E: float,
    omega_H: float,
    omega_Q: float,
    omega_P: float,
    mu_E: float,
    mu_H: float,
    mu_Q: float,
    mu_P: float,
    kappa: float,
) -> float:
    """Conditional mean E[v|X] when the market observes only X."""
    p0, p1 = noise_probs(kappa)

    def pr_z(z: int) -> float:
        if z == 0:
            return p0
        if z in (-1, 1):
            return p1
        return 0.0

    # actions (q, mu_action, omega)
    acts = [
        (-1, mu_E, omega_E),
        (0, mu_H, omega_H),
        (0, mu_Q, omega_Q),
        (1, mu_P, omega_P),
    ]

    denom = 0.0
    numer = 0.0
    for q, mu_a, omega in acts:
        if omega < TOL_PROB:
            continue
        pz = pr_z(X - q)
        if pz < TOL_PROB:
            continue
        w = omega * pz
        denom += w
        numer += w * mu_a

    if denom <= TOL_PROB:
        return float(np.mean([mu_E, mu_H, mu_Q, mu_P]))

    return float(numer / denom)


def compute_minority_gains_no_disclosure_given_strategy(k1: float, k0: float, kD: float, params: ModelParams) -> MinorityGains:
    """Compute minority gains under *no disclosure*, holding cutoffs fixed.

    This is the partial-equilibrium counterfactual used in Section 8.

    Implementation: we keep ω and μ implied by (k1,k0,kD), compute π(X) and
    E[v|X], and then compute p(X) and expected premia.
    """

    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    mu_E, mu_H, mu_Q, mu_P = compute_conditional_means(k1, k0, kD, params)
    post_X = compute_posteriors_no_disclosure(omega_E, omega_H, omega_Q, omega_P, params.kappa)

    # Bid probability depends only on X under this regime
    p_bid_X: Dict[int, float] = {}
    for X in (-2, -1, 0, 1, 2):
        pi_X = post_X.get(X, 0.0)
        E_v_X = compute_E_v_given_X_no_disclosure(X, omega_E, omega_H, omega_Q, omega_P, mu_E, mu_H, mu_Q, mu_P, params.kappa)
        V_hat_X = float(E_v_X + params.Delta_tilde * pi_X)
        m_bar_X = float(params.m0 + (params.m_tilde - params.m0) * pi_X)
        p_bid_X[X] = bid_probability(V_hat_X, m_bar_X, pi_X, params)

    p0, p1 = noise_probs(params.kappa)
    actions: List[Tuple[Action, int, float]] = [
        (Action.EXIT, -1, omega_E),
        (Action.HOLD, 0, omega_H),
        (Action.QUIET, 0, omega_Q),
        (Action.PUBLIC, 1, omega_P),
    ]

    total = base = act = 0.0

    for act_name, q, omega in actions:
        if omega < TOL_PROB:
            continue
        a = 1 if act_name in (Action.QUIET, Action.PUBLIC) else 0
        m_realized = params.m_tilde if a == 1 else params.m0

        for z, pz in ((-1, p1), (0, p0), (1, p1)):
            if pz < TOL_PROB:
                continue
            X = q + z
            p_bid = p_bid_X.get(X, 0.0)
            w = omega * pz
            total += w * p_bid * m_realized
            base += w * p_bid * params.m0
            act += w * p_bid * (m_realized - params.m0)

    return MinorityGains(total=float(total), base=float(base), activism=float(act))


def compute_posteriors_noisy_rumor(
    omega_E: float,
    omega_H: float,
    omega_Q: float,
    omega_P: float,
    kappa: float,
    eta_1: float,
    eta_0: float,
) -> Dict[XDR, float]:
    """Posterior π(X,D,R) for the noisy-rumor regime (Section 8).

    R is only informative in nondisclosed states D=0.

    eta_1 = P(R=1 | a=1)
    eta_0 = P(R=1 | a=0)
    """
    p0, p1 = noise_probs(kappa)
    post: Dict[XDR, float] = {}

    # Disclosed states: D=1 => engagement certain regardless of R
    for X in (0, 1, 2):
        for R in (0, 1):
            post[(X, 1, R)] = 1.0

    # D=0, X=-2: Exit only => no engagement
    for R in (0, 1):
        post[(-2, 0, R)] = 0.0

    # Helper: rumor likelihoods
    def pr_R_given_a(R: int, a: int) -> float:
        if a == 1:
            return eta_1 if R == 1 else (1.0 - eta_1)
        return eta_0 if R == 1 else (1.0 - eta_0)

    # X=1,D=0 can only come from q=0 (Hold or Quiet) with z=+1.
    # Hence π depends only on ω_H, ω_Q and rumor.
    for R in (0, 1):
        wQ = omega_Q * pr_R_given_a(R, 1)
        wH = omega_H * pr_R_given_a(R, 0)
        denom = wQ + wH
        post[(1, 0, R)] = float(wQ / denom) if denom > TOL_PROB else 0.0

    # X=-1,D=0 can come from Exit with z=0, or q=0 with z=-1.
    for R in (0, 1):
        # weights proportional to prior * likelihood
        wQ = omega_Q * p1 * pr_R_given_a(R, 1)
        wH = omega_H * p1 * pr_R_given_a(R, 0)
        wE = omega_E * p0 * pr_R_given_a(R, 0)
        denom = wQ + wH + wE
        post[(-1, 0, R)] = float(wQ / denom) if denom > TOL_PROB else 0.0

    # X=0,D=0 can come from Exit with z=+1, or q=0 with z=0.
    for R in (0, 1):
        wQ = omega_Q * p0 * pr_R_given_a(R, 1)
        wH = omega_H * p0 * pr_R_given_a(R, 0)
        wE = omega_E * p1 * pr_R_given_a(R, 0)
        denom = wQ + wH + wE
        post[(0, 0, R)] = float(wQ / denom) if denom > TOL_PROB else 0.0

    return post


def compute_minority_gains_noisy_rumor_given_strategy(
    k1: float,
    k0: float,
    kD: float,
    params: ModelParams,
    eta_1: float,
    eta_0: float,
) -> MinorityGains:
    """Minority gains under the noisy-rumor regime, holding cutoffs fixed."""

    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    mu_E, mu_H, mu_Q, mu_P = compute_conditional_means(k1, k0, kD, params)
    post = compute_posteriors_noisy_rumor(omega_E, omega_H, omega_Q, omega_P, params.kappa, eta_1, eta_0)

    p0, p1 = noise_probs(params.kappa)

    # Precompute bid probabilities p(X,D,R)
    p_bid: Dict[XDR, float] = {}
    E_v: Dict[XDR, float] = {}

    for X in (-2, -1, 0, 1, 2):
        for D in (0, 1):
            if D == 1 and X < 0:
                continue
            for R in (0, 1):
                key = (X, D, R)
                if key not in post:
                    continue
                pi = post[key]

                # E[v|X,D,R] must incorporate rumor because it shifts weights across H vs Q.
                if D == 1:
                    E_v_XDR = mu_P
                else:
                    # D=0 cases
                    if X == -2:
                        E_v_XDR = mu_E
                    elif X == 1:
                        # only H or Q; rumor reweights
                        wH = omega_H * (eta_0 if R == 1 else 1.0 - eta_0)
                        wQ = omega_Q * (eta_1 if R == 1 else 1.0 - eta_1)
                        denom = wH + wQ
                        E_v_XDR = (wH * mu_H + wQ * mu_Q) / denom if denom > TOL_PROB else 0.5 * (mu_H + mu_Q)
                    elif X == -1:
                        # Exit with z=0 plus H/Q with z=-1
                        wE = omega_E * p0 * (eta_0 if R == 1 else 1.0 - eta_0)
                        wH = omega_H * p1 * (eta_0 if R == 1 else 1.0 - eta_0)
                        wQ = omega_Q * p1 * (eta_1 if R == 1 else 1.0 - eta_1)
                        denom = wE + wH + wQ
                        E_v_XDR = (wE * mu_E + wH * mu_H + wQ * mu_Q) / denom if denom > TOL_PROB else (mu_E + mu_H + mu_Q) / 3.0
                    elif X == 0:
                        # Exit with z=+1 plus H/Q with z=0
                        wE = omega_E * p1 * (eta_0 if R == 1 else 1.0 - eta_0)
                        wH = omega_H * p0 * (eta_0 if R == 1 else 1.0 - eta_0)
                        wQ = omega_Q * p0 * (eta_1 if R == 1 else 1.0 - eta_1)
                        denom = wE + wH + wQ
                        E_v_XDR = (wE * mu_E + wH * mu_H + wQ * mu_Q) / denom if denom > TOL_PROB else (mu_E + mu_H + mu_Q) / 3.0
                    else:
                        # X=2 with D=0 is infeasible
                        continue

                E_v[key] = float(E_v_XDR)

                V_hat = float(E_v_XDR + params.Delta_tilde * pi)
                m_bar = float(params.m0 + (params.m_tilde - params.m0) * pi)
                p_bid[key] = bid_probability(V_hat, m_bar, pi, params)

    # Expected minority gains: enumerate action, noise, and rumor likelihood
    total = base = act = 0.0

    # rumor likelihood conditional on a in D=0 states
    def pr_R_given_a(R: int, a: int) -> float:
        if a == 1:
            return eta_1 if R == 1 else 1.0 - eta_1
        return eta_0 if R == 1 else 1.0 - eta_0

    actions: List[Tuple[Action, int, int, float]] = [
        (Action.EXIT, -1, 0, omega_E),
        (Action.HOLD, 0, 0, omega_H),
        (Action.QUIET, 0, 0, omega_Q),
        (Action.PUBLIC, 1, 1, omega_P),
    ]

    for act_name, q, D, omega in actions:
        if omega < TOL_PROB:
            continue
        a = 1 if act_name in (Action.QUIET, Action.PUBLIC) else 0
        m_realized = params.m_tilde if a == 1 else params.m0

        for z, pz in ((-1, p1), (0, p0), (1, p1)):
            if pz < TOL_PROB:
                continue
            X = q + z

            for R in (0, 1):
                if D == 1:
                    # rumor irrelevant; treat as degenerate (say R=1 always)
                    prR = 1.0 if R == 1 else 0.0
                else:
                    prR = pr_R_given_a(R, a)

                if prR < TOL_PROB:
                    continue
                key = (X, D, R)
                if key not in p_bid:
                    continue
                w = omega * pz * prR
                pb = p_bid[key]
                total += w * pb * m_realized
                base += w * pb * params.m0
                act += w * pb * (m_realized - params.m0)

    return MinorityGains(total=float(total), base=float(base), activism=float(act))
```
