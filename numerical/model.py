"""
Core economic model functions for the Exit-Voice-Takeover model.

This module implements the equilibrium objects described in Sections 2--5
of "Liquidity, Activism Disclosure, and Takeover Premia":

    Section 2 -- Information structure (signal, engagement cost, posterior mean)
    Section 3 -- Market microstructure (action probabilities, posteriors, prices)
    Section 4 -- Welfare and minority gains
    Section 5 -- Counterfactual information regimes

All mathematical computations are identical to those in the monolithic
``numerical.py``; only the interface has been modernised (Action enum,
MinorityGains namedtuple, named tolerance constants).
"""

from __future__ import annotations

from typing import Dict, Tuple

import numpy as np

# --- numpy>=2.0 compatibility: np.trapz was removed in favor of np.trapezoid ---
if not hasattr(np, 'trapezoid') and hasattr(np, 'trapz'):
    np.trapezoid = np.trapz  # older numpy
if not hasattr(np, 'trapz') and hasattr(np, 'trapezoid'):
    np.trapz = np.trapezoid  # numpy>=2.0
from scipy.stats import norm

from numerical.params import (
    Action,
    MinorityGains,
    ModelParams,
    TOL_CONVERGE,
    TOL_PROB,
    TOL_REGION,
)

# ── Section 2: Information Structure ────────────────────────────────────────


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


# ── Section 3: Market Microstructure ────────────────────────────────────────


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
    p0 = 1 - kappa   # P(z=0)
    p1 = kappa / 2    # P(z=+1) = P(z=-1)

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
    p0 = 1 - kappa
    p1 = kappa / 2

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


def bid_probability(P: float, m_XD: float, params: ModelParams) -> float:
    """Bid probability p(X, D) -- Equation (8).

    The bidder submits a takeover offer when synergy shock xi exceeds
    the threshold T = (m + K - S_bar + P) / sigma_xi.
    """
    T = (m_XD + params.K - params.S_bar + P) / params.sigma_xi
    return 1 - norm.cdf(T)


def solve_price_fixed_point(
    E_v_XD: float, pi_XD: float, params: ModelParams,
    max_iter: int = 100, tol: float = 1e-8
) -> float:
    """Solve for equilibrium price P(X, D) via fixed-point iteration -- Equation (9).

    Price equation:
        P = delta * [(1 - p) * V_hat + p * (P + m)]

    where V_hat = E[v|X,D] + Delta_tilde * pi(X,D)
    and   m     = m0 + (m_tilde - m0) * pi(X,D).
    """
    V_hat = E_v_XD + params.Delta_tilde * pi_XD
    m_XD = params.m0 + (params.m_tilde - params.m0) * pi_XD

    # Initial guess
    P = params.delta * V_hat

    for _ in range(max_iter):
        p = bid_probability(P, m_XD, params)
        P_new = params.delta * ((1 - p) * V_hat + p * (P + m_XD))

        if abs(P_new - P) < tol:
            return P_new
        P = P_new

    return P


def compute_equilibrium_prices(
    k1: float, k0: float, kD: float, params: ModelParams
) -> Dict[Tuple[int, int], float]:
    """Equilibrium prices P(X, D) for all feasible (X, D) pairs.

    Combines action probabilities, conditional means, posteriors, and the
    price fixed point (Eq. 9) for each information state.
    """
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(
        k1, k0, kD, params
    )
    mu_E, mu_H, mu_Q, mu_P = compute_conditional_means(k1, k0, kD, params)
    posteriors = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)

    prices: Dict[Tuple[int, int], float] = {}

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

            prices[(X, D)] = solve_price_fixed_point(E_v_XD, pi_XD, params)

    return prices


def compute_expected_payoff(
    action: Action, s: float,
    prices: Dict[Tuple[int, int], float],
    posteriors: Dict[Tuple[int, int], float],
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
    params : ModelParams
        Model calibration.

    Returns
    -------
    float
        Expected payoff of the blockholder under the chosen action.
    """
    p0 = 1 - params.kappa
    p1 = params.kappa / 2

    v_post = v_hat(s, params)

    def get_price_safe(X: int, D: int) -> float:
        return prices.get((X, D), params.mu)

    def get_m_XD(X: int, D: int) -> float:
        pi = posteriors.get((X, D), 0)
        return params.m0 + (params.m_tilde - params.m0) * pi

    if action == Action.EXIT:  # Exit: q=-1, a=0, h=0
        # Payoff: +P(X, 0) (selling 1 share)
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
            P = get_price_safe(X, 0)
            m_XD = get_m_XD(X, 0)
            p_bid = bid_probability(P, m_XD, params)
            # Holding h=1 share, no trading cash flow
            # Terminal: if bid, get P + m(a=0); if no bid, get v
            expected_terminal = p_bid * (P + params.m0) + (1 - p_bid) * v_post
            payoff += pz * params.delta * expected_terminal
        return payoff

    elif action == Action.QUIET:  # Quiet Voice: q=0, a=1, h=1
        # X = 0 + z, so X in {-1, 0, 1}
        C = engagement_cost(s, params)
        payoff = -C  # Pay engagement cost
        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = z
            P = get_price_safe(X, 0)
            m_XD = get_m_XD(X, 0)
            p_bid = bid_probability(P, m_XD, params)
            # Terminal with engagement: if bid, get P + m_tilde; if no bid, get v + Delta_tilde
            expected_terminal = p_bid * (P + params.m_tilde) + (1 - p_bid) * (v_post + params.Delta_tilde)
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
            p_bid = bid_probability(P, m_XD, params)
            # Trading cash flow: -P (buying 1 share)
            # Terminal with h=2: if bid, get 2*(P + m_tilde); if no bid, get 2*(v + Delta_tilde)
            trading_cf = -P
            expected_terminal = p_bid * 2 * (P + params.m_tilde) + (1 - p_bid) * 2 * (v_post + params.Delta_tilde)
            payoff += pz * (trading_cf + params.delta * expected_terminal)
        return payoff

    else:
        raise ValueError(f"Unknown action: {action}")


# ── Section 4: Welfare and Minority Gains ───────────────────────────────────


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
    mu_E, mu_H, mu_Q, mu_P = compute_conditional_means(k1, k0, kD, params)
    posteriors = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    prices = compute_equilibrium_prices(k1, k0, kD, params)

    p0 = 1 - params.kappa
    p1 = params.kappa / 2

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

            P = prices.get((X, D), params.mu)
            pi_XD = posteriors.get((X, D), 0)
            m_XD = params.m0 + (params.m_tilde - params.m0) * pi_XD

            p_bid = bid_probability(P, m_XD, params)

            # Realized premium
            m_realized = params.m_tilde if a == 1 else params.m0

            # Weight
            weight = omega_a * pz

            # Contributions
            total_gains += weight * p_bid * m_realized
            base_gains += weight * p_bid * params.m0
            activism_gains += weight * p_bid * (m_realized - params.m0)

    return MinorityGains(total=total_gains, base=base_gains, activism=activism_gains)


# ── Section 4b: Bidder Surplus and Total Welfare ─────────────────────────────


def compute_bidder_surplus_state(
    P: float, m_XD: float, params: ModelParams
) -> float:
    """Bidder expected surplus E[max(Pi_B, 0)] in a specific (X, D) state.

    The bidder's surplus from entry is xi - T where T = m_XD + K - S_bar + P,
    and she enters when xi > T.  The expectation of max(xi - T, 0) for
    xi ~ N(0, sigma_xi^2) is the standard truncated-normal formula.
    """
    T = m_XD + params.K - params.S_bar + P
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
    prices = compute_equilibrium_prices(k1, k0, kD, params)

    p0 = 1 - params.kappa
    p1 = params.kappa / 2

    # ── Bidder welfare W_bid ──────────────────────────────────────────────
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
            P = prices[(X, D)]
            pi_XD = posteriors.get((X, D), 0.0)
            m_XD = params.m0 + (params.m_tilde - params.m0) * pi_XD
            surplus = compute_bidder_surplus_state(P, m_XD, params)
            W_bid += omega_a * pz * surplus

    # ── Blockholder welfare W_B ───────────────────────────────────────────
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
            act, float(s), prices, posteriors, params
        )

    W_B = float(np.trapezoid(u_vals * pdf, s_grid))

    # ── Minority gains W_min ──────────────────────────────────────────────
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
        prices_X[X] = solve_price_fixed_point(E_v_X, pi_X, params)

    p0 = 1 - params.kappa
    p1 = params.kappa / 2

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
            P = prices_X.get(X, params.mu)
            pi_X = post_X.get(X, 0.0)
            m_X = params.m0 + (params.m_tilde - params.m0) * pi_X
            p_bid = bid_probability(P, m_X, params)

            weight = omega_a * pz
            total_gains += weight * p_bid * m_realized
            base_gains += weight * p_bid * params.m0
            activism_gains += weight * p_bid * (m_realized - params.m0)

    return MinorityGains(total=total_gains, base=base_gains, activism=activism_gains)


# ── Section 5: Counterfactual Information Regimes ───────────────────────────


def compute_posteriors_no_disclosure(
    omega_E: float, omega_H: float, omega_Q: float, omega_P: float,
    kappa: float
) -> Dict[int, float]:
    """Posterior pi(X) when disclosure is not observed -- Section 5.1.

    In this counterfactual the market conditions only on order flow X
    (no D signal), so (q,a)=(+1,1) states are pooled with other D=0 states.
    """
    p0 = 1 - kappa   # P(z=0)
    p1 = kappa / 2    # P(z=+1) = P(z=-1)

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
    p0 = 1 - kappa
    p1 = kappa / 2

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
    p0 = 1 - params.kappa
    p1 = params.kappa / 2

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

                prices_R[(X, D, R)] = solve_price_fixed_point(
                    E_v, pi_XDR, params
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
                P = prices_R.get((X, D, R), params.mu)
                pi_XDR = post_R.get((X, D, R), 0.0)
                m_XDR = params.m0 + (params.m_tilde - params.m0) * pi_XDR
                p_bid = bid_probability(P, m_XDR, params)

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
    p0 = 1 - kappa
    p1 = kappa / 2

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
