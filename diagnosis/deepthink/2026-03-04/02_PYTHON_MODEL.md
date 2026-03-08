# Python Core Model

## numerical/model.py
Core economic functions: posteriors, prices, payoffs, welfare, information regimes.
This is the computational implementation of the theory. Cross-reference with draft_v3.tex.

```python
"""
Core economic model functions for the Exit-Voice-Takeover model.

This module implements the equilibrium objects described in Sections 3--5
of "Liquidity, Activism Disclosure, and Takeover Premia".

Revision notes:
    - Noise distribution: p0 = 1 - 2*kappa/3, p1 = kappa/3
    - Bid probability decoupled from recursive price P and shifted to Logistic CDF
    - Synergy facilitation parameter Delta_S embedded into bidder surplus
    - Direct feed-forward pricing formula replaces fixed-point iteration
"""

from __future__ import annotations

from typing import Dict, Tuple

import numpy as np
from scipy.stats import norm
from scipy.special import expit

from numerical.params import (
    Action,
    MinorityGains,
    ModelParams,
    TOL_PROB,
)

# ── Noise Distribution ──────────────────────────────────────────────────────

def noise_probs(kappa: float) -> Tuple[float, float]:
    """Noise-trader order flow probabilities -- Definition 1."""
    if not (0.0 <= kappa <= 1.0):
        raise ValueError(f"kappa must be in [0, 1], got {kappa}")
    p0 = 1.0 - (2.0 / 3.0) * kappa
    p1 = (1.0 / 3.0) * kappa
    return p0, p1


# ── Information Structure ────────────────────────────────────────

def engagement_cost(s: float, params: ModelParams) -> float:
    """Signal-dependent engagement cost C(s)."""
    z = (s - params.mu) / params.sigma_s
    return params.C0 * np.exp(-params.chi * z)


def v_hat(s: float, params: ModelParams) -> float:
    """Posterior mean of v given signal s."""
    return params.mu + params.beta * (s - params.mu)


# ── Market Microstructure ────────────────────────────────────────

def compute_action_probabilities(
    k1: float, k0: float, kD: float, params: ModelParams
) -> Tuple[float, float, float, float]:
    """Unconditional action probabilities."""
    alpha1 = (k1 - params.mu) / params.sigma_s
    alpha0 = (k0 - params.mu) / params.sigma_s
    alphaD = (kD - params.mu) / params.sigma_s

    omega_E = norm.cdf(alpha1)
    omega_H = norm.cdf(alpha0) - norm.cdf(alpha1)
    omega_Q = norm.cdf(alphaD) - norm.cdf(alpha0)
    omega_P = 1.0 - norm.cdf(alphaD)

    # Ensure non-negative (numerical stability)
    return max(0.0, omega_E), max(0.0, omega_H), max(0.0, omega_Q), max(0.0, omega_P)


def compute_conditional_means(
    k1: float, k0: float, kD: float, params: ModelParams
) -> Tuple[float, float, float, float]:
    """Conditional means E[v | action region]."""
    alpha1 = (k1 - params.mu) / params.sigma_s
    alpha0 = (k0 - params.mu) / params.sigma_s
    alphaD = (kD - params.mu) / params.sigma_s

    def lambda_L(alpha: float) -> float:
        cdf = norm.cdf(alpha)
        if cdf < TOL_PROB:
            return -alpha 
        return norm.pdf(alpha) / cdf

    def lambda_U(alpha: float) -> float:
        ccdf = 1.0 - norm.cdf(alpha)
        if ccdf < TOL_PROB:
            return alpha  
        return norm.pdf(alpha) / ccdf

    mu_E = params.mu - params.beta * params.sigma_s * lambda_L(alpha1)

    denom_H = norm.cdf(alpha0) - norm.cdf(alpha1)
    if denom_H > TOL_PROB:
        mu_H = params.mu + params.beta * params.sigma_s * (norm.pdf(alpha1) - norm.pdf(alpha0)) / denom_H
    else:
        mu_H = params.mu + params.beta * (k0 + k1) / 2.0 - params.beta * params.mu

    denom_Q = norm.cdf(alphaD) - norm.cdf(alpha0)
    if denom_Q > TOL_PROB:
        mu_Q = params.mu + params.beta * params.sigma_s * (norm.pdf(alpha0) - norm.pdf(alphaD)) / denom_Q
    else:
        mu_Q = params.mu + params.beta * (kD + k0) / 2.0 - params.beta * params.mu

    mu_P = params.mu + params.beta * params.sigma_s * lambda_U(alphaD)

    return mu_E, mu_H, mu_Q, mu_P


def compute_posteriors(
    omega_E: float, omega_H: float, omega_Q: float, omega_P: float,
    kappa: float
) -> Dict[Tuple[int, int], float]:
    """Bayesian posterior pi(X, D) -- Proposition 2."""
    p0, p1 = noise_probs(kappa)
    posteriors: Dict[Tuple[int, int], float] = {}

    for X in [0, 1, 2]:
        posteriors[(X, 1)] = 1.0

    posteriors[(-2, 0)] = 0.0

    denom_1 = omega_H + omega_Q
    posteriors[(1, 0)] = (omega_Q / denom_1) if denom_1 > TOL_PROB else 0.0

    denom_m1 = (omega_H + omega_Q) * p1 + omega_E * p0
    posteriors[(-1, 0)] = (omega_Q * p1 / denom_m1) if denom_m1 > TOL_PROB else 0.0

    denom_0 = (omega_H + omega_Q) * p0 + omega_E * p1
    posteriors[(0, 0)] = (omega_Q * p0 / denom_0) if denom_0 > TOL_PROB else 0.0

    return posteriors


def compute_E_v_given_XD(
    X: int, D: int,
    omega_E: float, omega_H: float, omega_Q: float, omega_P: float,
    mu_E: float, mu_H: float, mu_Q: float, mu_P: float,
    kappa: float
) -> float:
    """Conditional expectation E[v | X, D]."""
    p0, p1 = noise_probs(kappa)

    if D == 1:
        return mu_P

    if X == -2:
        return mu_E
    elif X == 1:
        denom = omega_H + omega_Q
        if denom < TOL_PROB:
            return (mu_H + mu_Q) / 2.0
        return (omega_H * mu_H + omega_Q * mu_Q) / denom
    elif X == -1:
        denom = (omega_H + omega_Q) * p1 + omega_E * p0
        if denom < TOL_PROB:
            return (mu_H + mu_Q + mu_E) / 3.0
        return ((omega_H * mu_H + omega_Q * mu_Q) * p1 + omega_E * mu_E * p0) / denom
    else:  
        denom = (omega_H + omega_Q) * p0 + omega_E * p1
        if denom < TOL_PROB:
            return (mu_H + mu_Q + mu_E) / 3.0
        return ((omega_H * mu_H + omega_Q * mu_Q) * p0 + omega_E * mu_E * p1) / denom


def bid_probability(V_hat_XD: float, m_XD: float, pi_XD: float, params: ModelParams) -> float:
    """Conditional bid probability p_tilde(X, D) -- Equation (1).

    The bidder submits a takeover offer when synergy shock xi (Logistic) exceeds
    the threshold T_raw = V_hat_XD + m_XD + K - (S_bar + pi_XD * Delta_S).
    Returns 1 - Lambda(T_raw / s_xi)
    """
    T_raw = V_hat_XD + m_XD + params.K - (params.S_bar + pi_XD * params.Delta_S)
    T_scaled = T_raw / params.s_xi
    
    # 1 - Lambda(T_scaled) = expit(-T_scaled)
    return float(expit(-T_scaled))


def compute_price_direct(
    V_hat_XD: float, p_bid: float, m_XD: float, params: ModelParams
) -> float:
    """Equilibrium feed-forward price P(X, D)."""
    return params.delta * (V_hat_XD + p_bid * m_XD)


def compute_equilibrium_prices(
    k1: float, k0: float, kD: float, params: ModelParams
) -> Tuple[Dict[Tuple[int, int], float], Dict[int, float], Dict[Tuple[int, int], float]]:
    """Equilibrium prices P_post(X,D), P_trade(X), and E[v|X,D].

    Returns a 3-tuple:
        prices      -- P_post(X,D): post-disclosure prices for terminal valuation
        prices_trade -- P_trade(X): anonymous execution prices (Proposition 3)
        E_v_dict    -- E[v|X,D] conditional expectations
    """
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(
        k1, k0, kD, params
    )
    mu_E, mu_H, mu_Q, mu_P = compute_conditional_means(k1, k0, kD, params)
    posteriors = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    p0, p1 = noise_probs(params.kappa)

    prices: Dict[Tuple[int, int], float] = {}
    E_v_dict: Dict[Tuple[int, int], float] = {}

    for X in [-2, -1, 0, 1, 2]:
        for D in [0, 1]:
            if D == 1 and X < 0:
                continue

            if (X, D) not in posteriors:
                continue

            pi_XD = posteriors[(X, D)]
            E_v_XD = compute_E_v_given_XD(
                X, D, omega_E, omega_H, omega_Q, omega_P,
                mu_E, mu_H, mu_Q, mu_P, params.kappa
            )
            E_v_dict[(X, D)] = E_v_XD

            V_hat_XD = E_v_XD + params.Delta_tilde * pi_XD
            m_XD = params.m0 + (params.m_tilde - params.m0) * pi_XD

            p_bid_cond = bid_probability(V_hat_XD, m_XD, pi_XD, params)
            p_bid_uncond = params.lambda_B * p_bid_cond

            prices[(X, D)] = compute_price_direct(
                V_hat_XD, p_bid_uncond, m_XD, params
            )

    # ── Anonymous execution prices P_trade(X) ── Proposition 3
    # P_trade(X) = Σ_D Pr(D=d|X) · P_post(X,d)
    # Market maker observes order flow X but not disclosure D at trade time.
    # Joint Pr(X, D) from action probabilities and noise distribution.
    prob_XD: Dict[Tuple[int, int], float] = {}
    actions_list = [(-1, 0, omega_E), (0, 0, omega_H), (0, 0, omega_Q), (1, 1, omega_P)]
    for q, D, omega in actions_list:
        if omega < TOL_PROB:
            continue
        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            key = (q + z, D)
            prob_XD[key] = prob_XD.get(key, 0.0) + omega * pz

    prices_trade: Dict[int, float] = {}
    for X in [-2, -1, 0, 1, 2]:
        prob_X = sum(prob_XD.get((X, d), 0.0) for d in [0, 1])
        if prob_X < TOL_PROB:
            continue
        ptrade = 0.0
        for d in [0, 1]:
            pr = prob_XD.get((X, d), 0.0)
            if pr < TOL_PROB or (X, d) not in prices:
                continue
            ptrade += (pr / prob_X) * prices[(X, d)]
        prices_trade[X] = ptrade

    return prices, prices_trade, E_v_dict


def compute_expected_payoff(
    action: Action, s: float,
    prices: Dict[Tuple[int, int], float],
    prices_trade: Dict[int, float],
    posteriors: Dict[Tuple[int, int], float],
    E_v_dict: Dict[Tuple[int, int], float],
    params: ModelParams
) -> float:
    """Expected payoff for a given action and signal.

    Under anonymous accumulation, the blockholder trades at P_trade(X)
    (EXIT sells, PUBLIC buys). Terminal values use post-disclosure P_post(X,D).
    HOLD and QUIET have q=0, so no trading cash flow.
    """
    p0, p1 = noise_probs(params.kappa)
    v_post = v_hat(s, params)

    def get_pi(X: int, D: int) -> float:
        return posteriors.get((X, D), 0.0)

    def get_V_hat(X: int, D: int, pi: float) -> float:
        E_v = E_v_dict.get((X, D), params.mu)
        return E_v + params.Delta_tilde * pi

    if action == Action.EXIT:
        # EXIT: sell q=-1 at anonymous price P_trade(X), X = -1 + z
        payoff = 0.0
        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = -1 + z
            P = prices_trade.get(X, params.mu)
            payoff += pz * P
        return payoff

    elif action == Action.HOLD:
        payoff = 0.0
        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = z
            pi_XD = get_pi(X, 0)
            m_XD = params.m0 + (params.m_tilde - params.m0) * pi_XD
            V_hat_XD = get_V_hat(X, 0, pi_XD)
            
            p_bid_cond = bid_probability(V_hat_XD, m_XD, pi_XD, params)
            p_bid_uncond = params.lambda_B * p_bid_cond
            
            expected_terminal = p_bid_uncond * (V_hat_XD + params.m0) + (1.0 - p_bid_uncond) * v_post
            payoff += pz * params.delta * expected_terminal
        return payoff

    elif action == Action.QUIET:
        C = engagement_cost(s, params)
        payoff = -C
        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = z
            pi_XD = get_pi(X, 0)
            m_XD = params.m0 + (params.m_tilde - params.m0) * pi_XD
            V_hat_XD = get_V_hat(X, 0, pi_XD)
            
            p_bid_cond = bid_probability(V_hat_XD, m_XD, pi_XD, params)
            p_bid_uncond = params.lambda_B * p_bid_cond
            
            expected_terminal = p_bid_uncond * (V_hat_XD + params.m_tilde) + (1.0 - p_bid_uncond) * (v_post + params.Delta_tilde)
            payoff += pz * params.delta * expected_terminal
        return payoff

    elif action == Action.PUBLIC:
        # PUBLIC: buy q=+1 at anonymous price P_trade(X), X = 1 + z
        C = engagement_cost(s, params)
        payoff = -C
        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = 1 + z
            P = prices_trade.get(X, params.mu)
            pi_XD = 1.0
            m_XD = params.m_tilde
            V_hat_XD = get_V_hat(X, 1, pi_XD)
            
            p_bid_cond = bid_probability(V_hat_XD, m_XD, pi_XD, params)
            p_bid_uncond = params.lambda_B * p_bid_cond
            
            trading_cf = -P
            expected_terminal = p_bid_uncond * 2.0 * (V_hat_XD + params.m_tilde) + (1.0 - p_bid_uncond) * 2.0 * (v_post + params.Delta_tilde)
            payoff += pz * (trading_cf + params.delta * expected_terminal)
        return payoff

    else:
        raise ValueError(f"Unknown action: {action}")


# ── Section 5: Welfare and Minority Gains ───────────────────────────────────

def compute_minority_gains(
    k1: float, k0: float, kD: float, params: ModelParams
) -> MinorityGains:
    """Expected minority takeover gains by exact enumeration."""
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    posteriors = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    prices, _prices_trade, E_v_dict = compute_equilibrium_prices(k1, k0, kD, params)

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
        D = 1 if action == Action.PUBLIC else 0

        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = q + z

            if (X, D) not in prices:
                continue

            pi_XD = posteriors.get((X, D), 0.0)
            E_v_XD = E_v_dict.get((X, D), params.mu)
            V_hat_XD = E_v_XD + params.Delta_tilde * pi_XD
            m_XD = params.m0 + (params.m_tilde - params.m0) * pi_XD
            
            p_bid_cond = bid_probability(V_hat_XD, m_XD, pi_XD, params)
            p_bid_uncond = params.lambda_B * p_bid_cond

            m_realized = params.m_tilde if a == 1 else params.m0
            weight = omega_a * pz

            total_gains += weight * p_bid_uncond * m_realized
            base_gains += weight * p_bid_uncond * params.m0
            activism_gains += weight * p_bid_uncond * (m_realized - params.m0)

    return MinorityGains(total=total_gains, base=base_gains, activism=activism_gains)


def compute_bidder_surplus_state(
    V_hat_XD: float, m_XD: float, pi_XD: float, params: ModelParams
) -> float:
    """Bidder expected surplus E[max(Pi_B, 0)] in a specific (X, D) state.
    
    E[max(xi - T, 0)] for Logistic(0, s_xi) is exactly the softplus integral:
    s_xi * ln(1 + exp(-T/s_xi))
    """
    T_raw = V_hat_XD + m_XD + params.K - (params.S_bar + pi_XD * params.Delta_S)
    return params.s_xi * float(np.logaddexp(0.0, -T_raw / params.s_xi))


def compute_welfare(
    k1: float, k0: float, kD: float, params: ModelParams
) -> Tuple[float, float, float, float]:
    """Compute total expected welfare and its components."""
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    posteriors = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    prices, prices_trade, E_v_dict = compute_equilibrium_prices(k1, k0, kD, params)

    p0, p1 = noise_probs(params.kappa)

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
            E_v_XD = E_v_dict.get((X, D), params.mu)
            V_hat_XD = E_v_XD + params.Delta_tilde * pi_XD
            
            surplus = params.lambda_B * compute_bidder_surplus_state(V_hat_XD, m_XD, pi_XD, params)
            W_bid += omega_a * pz * surplus

    s_grid = np.linspace(params.mu - 6 * params.sigma_s, params.mu + 6 * params.sigma_s, 501)
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
        u_vals[i] = compute_expected_payoff(act, float(s), prices, prices_trade, posteriors, E_v_dict, params)

    W_B = float(np.trapz(u_vals * pdf, s_grid))

    gains = compute_minority_gains(k1, k0, kD, params)
    W_min = gains.total

    W_total = W_min + W_bid + W_B
    return float(W_min), float(W_bid), float(W_B), float(W_total)


# ── Section 6: Counterfactual Information Regimes ───────────────────────────

def compute_posteriors_no_disclosure(
    omega_E: float, omega_H: float, omega_Q: float, omega_P: float, kappa: float
) -> Dict[int, float]:
    """Posterior pi(X) when disclosure is not observed."""
    p0, p1 = noise_probs(kappa)

    def prob_z(z: int) -> float:
        if z == 0: return p0
        if z in (-1, 1): return p1
        return 0.0

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
    return {(-1, 0): 0.0, (0, 0): 0.0, (0, 1): 1.0, (1, 1): 1.0}

def compute_posteriors_noisy_rumor(
    omega_E: float, omega_H: float, omega_Q: float, omega_P: float,
    kappa: float, rho1: float, rho0: float
) -> Dict[Tuple[int, int, int], float]:
    p0, p1 = noise_probs(kappa)
    posteriors: Dict[Tuple[int, int, int], float] = {}

    for X in [0, 1, 2]:
        for R in [0, 1]:
            posteriors[(X, 1, R)] = 1.0

    for R in [0, 1]:
        posteriors[(-2, 0, R)] = 0.0

    denom_r1 = omega_Q * rho1 + omega_H * rho0
    denom_r0 = omega_Q * (1 - rho1) + omega_H * (1 - rho0)
    posteriors[(1, 0, 1)] = (omega_Q * rho1 / denom_r1) if denom_r1 > TOL_PROB else 0.0
    posteriors[(1, 0, 0)] = (omega_Q * (1 - rho1) / denom_r0) if denom_r0 > TOL_PROB else 0.0

    denom_m1_r1 = (omega_H * p1 + omega_E * p0) * rho0 + omega_Q * p1 * rho1
    denom_m1_r0 = (omega_H * p1 + omega_E * p0) * (1 - rho0) + omega_Q * p1 * (1 - rho1)
    posteriors[(-1, 0, 1)] = (omega_Q * p1 * rho1 / denom_m1_r1) if denom_m1_r1 > TOL_PROB else 0.0
    posteriors[(-1, 0, 0)] = (omega_Q * p1 * (1 - rho1) / denom_m1_r0) if denom_m1_r0 > TOL_PROB else 0.0

    denom_0_r1 = (omega_H * p0 + omega_E * p1) * rho0 + omega_Q * p0 * rho1
    denom_0_r0 = (omega_H * p0 + omega_E * p1) * (1 - rho0) + omega_Q * p0 * (1 - rho1)
    posteriors[(0, 0, 1)] = (omega_Q * p0 * rho1 / denom_0_r1) if denom_0_r1 > TOL_PROB else 0.0
    posteriors[(0, 0, 0)] = (omega_Q * p0 * (1 - rho1) / denom_0_r0) if denom_0_r0 > TOL_PROB else 0.0

    return posteriors

def compute_E_v_given_X_no_disclosure(
    X: int, omega_E: float, omega_H: float, omega_Q: float, omega_P: float,
    mu_E: float, mu_H: float, mu_Q: float, mu_P: float, kappa: float
) -> float:
    p0, p1 = noise_probs(kappa)
    def prob_z(z: int) -> float: return p0 if z == 0 else (p1 if z in (-1, 1) else 0.0)

    actions = [(-1, mu_E, omega_E), (0, mu_H, omega_H), (0, mu_Q, omega_Q), (1, mu_P, omega_P)]
    denom = 0.0
    numer = 0.0
    for q, mu_a, omega in actions:
        pz = prob_z(X - q)
        if pz == 0.0 or omega < TOL_PROB: continue
        w = omega * pz
        denom += w
        numer += w * mu_a

    return numer / denom if denom >= TOL_PROB else float(np.mean([mu_E, mu_H, mu_Q, mu_P]))

def compute_minority_gains_no_disclosure_given_strategy(
    k1: float, k0: float, kD: float, params: ModelParams
) -> MinorityGains:
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    mu_E, mu_H, mu_Q, mu_P = compute_conditional_means(k1, k0, kD, params)
    post_X = compute_posteriors_no_disclosure(omega_E, omega_H, omega_Q, omega_P, params.kappa)

    p_bid_X_dict: Dict[int, float] = {}
    for X in [-2, -1, 0, 1, 2]:
        pi_X = post_X.get(X, 0.0)
        E_v_X = compute_E_v_given_X_no_disclosure(
            X, omega_E, omega_H, omega_Q, omega_P, mu_E, mu_H, mu_Q, mu_P, params.kappa
        )
        V_hat_X = E_v_X + params.Delta_tilde * pi_X
        m_X = params.m0 + (params.m_tilde - params.m0) * pi_X
        p_bid_X_dict[X] = params.lambda_B * bid_probability(V_hat_X, m_X, pi_X, params)

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
        if omega_a < TOL_PROB: continue
        a = 1 if action in (Action.QUIET, Action.PUBLIC) else 0
        m_realized = params.m_tilde if a == 1 else params.m0

        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = q + z
            p_bid = p_bid_X_dict.get(X, 0.0)
            weight = omega_a * pz
            
            total_gains += weight * p_bid * m_realized
            base_gains += weight * p_bid * params.m0
            activism_gains += weight * p_bid * (m_realized - params.m0)

    return MinorityGains(total=total_gains, base=base_gains, activism=activism_gains)


def compute_minority_gains_noisy_rumor(
    k1: float, k0: float, kD: float, params: ModelParams,
    eta_1: float, eta_0: float,
) -> MinorityGains:
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    mu_E, mu_H, mu_Q, mu_P = compute_conditional_means(k1, k0, kD, params)
    post_R = compute_posteriors_noisy_rumor(omega_E, omega_H, omega_Q, omega_P, params.kappa, eta_1, eta_0)

    p_bid_R: Dict[Tuple[int, int, int], float] = {}
    p0, p1 = noise_probs(params.kappa)

    for X in [-2, -1, 0, 1, 2]:
        for D in [0, 1]:
            if D == 1 and X < 0: continue
            for R in [0, 1]:
                if (X, D, R) not in post_R: continue
                pi_XDR = post_R[(X, D, R)]

                if D == 1:
                    E_v = mu_P
                elif X == -2:
                    E_v = mu_E
                elif X == 1:
                    wH = omega_H * (eta_0 if R == 1 else 1 - eta_0)
                    wQ = omega_Q * (eta_1 if R == 1 else 1 - eta_1)
                    denom = wH + wQ
                    E_v = (wH * mu_H + wQ * mu_Q) / denom if denom > TOL_PROB else (mu_H + mu_Q) / 2.0
                elif X == -1:
                    wE = omega_E * p0 * (eta_0 if R == 1 else 1 - eta_0)
                    wH = omega_H * p1 * (eta_0 if R == 1 else 1 - eta_0)
                    wQ = omega_Q * p1 * (eta_1 if R == 1 else 1 - eta_1)
                    denom = wE + wH + wQ
                    E_v = (wE * mu_E + wH * mu_H + wQ * mu_Q) / denom if denom > TOL_PROB else (mu_E + mu_H + mu_Q) / 3.0
                else:  
                    wE = omega_E * p1 * (eta_0 if R == 1 else 1 - eta_0)
                    wH = omega_H * p0 * (eta_0 if R == 1 else 1 - eta_0)
                    wQ = omega_Q * p0 * (eta_1 if R == 1 else 1 - eta_1)
                    denom = wE + wH + wQ
                    E_v = (wE * mu_E + wH * mu_H + wQ * mu_Q) / denom if denom > TOL_PROB else (mu_E + mu_H + mu_Q) / 3.0

                m_XDR = params.m0 + (params.m_tilde - params.m0) * pi_XDR
                V_hat_XDR = E_v + params.Delta_tilde * pi_XDR
                p_bid_R[(X, D, R)] = params.lambda_B * bid_probability(V_hat_XDR, m_XDR, pi_XDR, params)

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
        if omega_a < TOL_PROB: continue
        a = 1 if action in (Action.QUIET, Action.PUBLIC) else 0
        D = 1 if action == Action.PUBLIC else 0
        m_realized = params.m_tilde if a == 1 else params.m0

        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            X = q + z
            for R in [0, 1]:
                if D == 1:
                    pR = 1.0 if R == 1 else 0.0
                else:
                    pR = (eta_1 if R == 1 else 1 - eta_1) if a == 1 else (eta_0 if R == 1 else 1 - eta_0)

                if pR < TOL_PROB: continue

                weight = omega_a * pz * pR
                p_bid = p_bid_R.get((X, D, R), 0.0)

                total_gains += weight * p_bid * m_realized
                base_gains += weight * p_bid * params.m0
                activism_gains += weight * p_bid * (m_realized - params.m0)

    return MinorityGains(total=total_gains, base=base_gains, activism=activism_gains)
```
