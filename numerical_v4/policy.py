"""Policy, ``evaluate()``, and the two sweep modes.

Design section 6.2, build step 7.

THE PURITY INVARIANT.  ``evaluate()`` is pure in the policy: it never calls the
solver.  Both sweep modes share ``evaluate`` verbatim, which is the entire
mechanism that makes a frozen-policy sweep and an equilibrium sweep comparable
at all.  A module-level guard parses this file's own imports and fails at import
time if ``solver`` appears anywhere among them, so the invariant cannot rot.

``equilibrium_sweep`` therefore takes the solver as an argument rather than
importing it (named deviation from the design's section 11 sketch, which shows
it importing ``solve_policy`` directly -- that would break the guard the same
section demands).
"""

from __future__ import annotations

import ast
import math
from pathlib import Path
from typing import Callable, NamedTuple, Sequence

import numpy as np

from numerical_v4.flagged import flagged_nodes, flagged_price_at
from numerical_v4.menu import (
    A7Certificate,
    VOICE,
    Atom,
    a7_certificate,
    atoms,
    b_star,
    legal_clock,
    stake_path,
    terminal_stake,
    theta_index,
)
from numerical_v4.params import ParamsV4, TOL_PROB
from numerical_v4.pooled import PooledResult, pooled_pass, run_up
from numerical_v4.premium import (
    cell_weights,
    decomposition_residual,
    pooled_cell_mass,
    pooled_premium,
    total_premium,
)


# ---------------------------------------------------------------------------
# Purity guard (design section 6.2)
# ---------------------------------------------------------------------------


def _assert_solver_not_imported() -> None:
    tree = ast.parse(Path(__file__).read_text())
    for node in ast.walk(tree):
        names: list[str] = []
        if isinstance(node, ast.Import):
            names = [al.name for al in node.names]
        elif isinstance(node, ast.ImportFrom):
            names = [node.module or ""] + [al.name for al in node.names]
        for nm in names:
            assert "solver" not in nm, (
                f"policy.py must stay pure in the policy; found import {nm!r}"
            )


_assert_solver_not_imported()


# ---------------------------------------------------------------------------
# Policy
# ---------------------------------------------------------------------------


class Menu(NamedTuple):
    """The blockholder's execution policy: everything that fixes B_j(s, .).

    tau and T are deliberately absent: they are the regulator's rule, not the
    blockholder's plan, and L4/T1 move them at *fixed* execution policies.
    """

    b0: float
    b_bar: float
    n_scale: float
    gamma_bar: float
    H: int
    label: str = "voice1"


def menu_of(p: ParamsV4) -> Menu:
    return Menu(p.b0, p.b_bar, p.n_scale, p.gamma_bar, p.H)


class Policy(NamedTuple):
    """Frozen cutoffs plus the frozen execution menu."""

    k: tuple[float, ...]
    menu: Menu


# ---------------------------------------------------------------------------
# Outcomes
# ---------------------------------------------------------------------------


class Outcomes(NamedTuple):
    """Everything ``evaluate`` reports, in natural units."""

    k: tuple[float, ...]
    kappa: float
    tau: float
    T: int
    H: int
    corner: bool                     # T == H (design risk 9.5)
    Omega: float
    Pr_a: float
    omega_a: float
    pi_bar: float
    M_F: float
    M_P: float
    Delta_act: float
    decomposition_residual: float    # L1 -- wiring
    identity_residual: float         # D1 -- wiring
    R_mean: float
    J_mean: float
    a7: A7Certificate
    multiple_root_nodes: int
    degenerate_nodes: tuple[str, ...]
    n_hist_feasible: int
    n_atoms: int
    n_flagged_atoms: int
    pooled_mass_error: float         # |sum mass_H - (1 - Omega)|
    max_price_residual: float
    max_inversion_error: float
    max_Q_F: float


def frozen_tau_grid(policy: Policy, p: ParamsV4,
                    quantiles: Sequence[float] = (0.5,)) -> tuple[float, ...]:
    """tau percentiles of the equilibrium Voice b*(s) distribution.

    Design section 6.2: the requests set tau at percentiles "of equilibrium
    Voice stake paths", which depends on the equilibrium, which depends on tau.
    Circular.  The values are computed *once* from a baseline equilibrium,
    frozen, and reused at every node; the frozen values go into the JSON
    provenance.  b* is strictly increasing, so the quantile of b* is b* at the
    quantile of the truncated signal distribution.
    """
    from scipy.stats import norm as _norm       # local: quantile only

    a2 = (policy.k[1] - p.mu_v) / p.sigma_s
    lower = float(_norm.cdf(a2))
    out = []
    for q in quantiles:
        alpha = float(_norm.ppf(lower + q * (1.0 - lower)))
        s_q = p.mu_v + p.sigma_s * alpha
        out.append(float(b_star(min(s_q, p.s_hi), p)))
    return tuple(out)


def engagement_cost(s: float, p: ParamsV4) -> float:
    """C_j(s) = C0 * exp(-chi * (s - mu_v)/sigma_s); zero for non-Voice plans."""
    return p.C0 * math.exp(-p.chi * (s - p.mu_v) / p.sigma_s)


def evaluate(policy: Policy, p: ParamsV4, with_runup: bool = True) -> Outcomes:
    """Every control-outcome object at a *given* policy.  Never calls a solver."""
    assert policy.menu == menu_of(p), (
        "frozen policy evaluated against a different execution menu"
    )
    al = atoms(policy.k, p)
    cw = cell_weights(al)
    fl = flagged_nodes(al, p)
    res = pooled_pass(al, p, with_runup=with_runup)

    M_P = pooled_premium(res, cw.Omega, p)
    M_F = fl.M_F
    Delta_act = total_premium(res, fl.w, fl.p_bid, p)
    dec = decomposition_residual(Delta_act, cw.Omega, M_F, M_P)

    ident, R_mean, J_mean = _runup_objects(res, al, p) if with_runup \
        else (float("nan"), float("nan"), float("nan"))

    a7 = a7_certificate(policy.k, p, al)
    flagged_atoms = [a for a in al if a.D == 1]
    max_QF = max((legal_clock(VOICE, 0.5 * (a.lo + a.hi), p).Q_F
                  for a in flagged_atoms), default=float("nan"))

    return Outcomes(
        k=tuple(policy.k), kappa=p.kappa, tau=p.tau, T=p.T, H=p.H,
        corner=(p.T == p.H),
        Omega=cw.Omega, Pr_a=cw.Pr_a, omega_a=cw.omega_a, pi_bar=cw.pi_bar,
        M_F=M_F, M_P=M_P, Delta_act=Delta_act,
        decomposition_residual=dec, identity_residual=ident,
        R_mean=R_mean, J_mean=J_mean, a7=a7,
        multiple_root_nodes=res.multiple_root_nodes + fl.multiple_root_nodes,
        degenerate_nodes=cw.degenerate,
        n_hist_feasible=res.n_hist_feasible,
        n_atoms=len(al), n_flagged_atoms=len(flagged_atoms),
        pooled_mass_error=abs(pooled_cell_mass(res) - (1.0 - cw.Omega)),
        max_price_residual=res.max_price_residual,
        max_inversion_error=fl.max_inversion_error,
        max_Q_F=max_QF,
    )


def _runup_objects(res: PooledResult, al: list[Atom], p: ParamsV4
                   ) -> tuple[float, float, float]:
    """Max D1 identity residual and mass-weighted mean R and J."""
    worst = 0.0
    num_R = num_J = den = 0.0
    for a in al:
        if a.D != 1 or a.f < 1:
            continue
        for frac in (0.25, 0.5, 0.75):
            s = a.lo + frac * (a.hi - a.lo)
            P_F, _ = flagged_price_at(s, p)
            ru = run_up(res, a, P_F, p)
            ok = np.isfinite(ru.identity) & (ru.weight > TOL_PROB)
            if ok.any():
                worst = max(worst, float(np.max(ru.identity[ok])))
                wt = ru.weight[ok] * a.w / 3.0
                num_R += float(np.dot(wt, ru.R[ok]))
                num_J += float(np.dot(wt, ru.J[ok]))
                den += float(wt.sum())
    if den <= TOL_PROB:
        return worst, float("nan"), float("nan")
    return worst, num_R / den, num_J / den


# ---------------------------------------------------------------------------
# The blockholder's payoff (card section 2.10) -- also pure in the policy
# ---------------------------------------------------------------------------


def plan_payoff(j: int, s: float, res: PooledResult, p: ParamsV4) -> float:
    """U_j(s) = E[b*_j(s) Y - C^trade_j - C_j(s) | s, j].

    Needs a pooled pass with ``with_runup=True``: the trade cost prices every
    pooled execution date at that date's own public history.
    """
    th = theta_index(j, s, p)
    cl = legal_clock(j, s, p)
    v_h = p.mu_v + p.beta * (s - p.mu_v)
    B = stake_path(j, s, p)
    b_term = terminal_stake(j, s, p)
    a = 1 if j == VOICE else 0

    if cl.D == 1:
        P_F, pF = flagged_price_at(s, p)
        EY = (1.0 - pF) * (v_h + p.Delta_V) + pF * (P_F + p.m0 + p.Delta_m)
        last = int(cl.f)
        trade = sum((B[d + 1] - B[d]) * res.EP[d][th] for d in range(last + 1))
        trade += cl.Q_F * P_F
    else:
        Ep = float(res.Ep_bid[th])
        EpP = float(res.EpP[th])
        EY = (1.0 - Ep) * (v_h + a * p.Delta_V) + EpP + Ep * (p.m0 + a * p.Delta_m)
        trade = sum((B[d + 1] - B[d]) * res.EP[d][th] for d in range(p.H + 1))

    cost = engagement_cost(s, p) if j == VOICE else 0.0
    return float(b_term * EY - trade - cost)


# ---------------------------------------------------------------------------
# The two modes (design section 6.2)
# ---------------------------------------------------------------------------


def frozen_policy_sweep(policy: Policy, p: ParamsV4,
                        kappas: Sequence[float],
                        with_runup: bool = False) -> list[Outcomes]:
    """Policy held fixed, kappa moves.  This is L2's and L4's mode."""
    return [evaluate(policy, p.replace(kappa=float(k)), with_runup)
            for k in kappas]


def equilibrium_sweep(p: ParamsV4, kappas: Sequence[float],
                      solve_fn: Callable[[ParamsV4], tuple[Policy, float]],
                      with_runup: bool = False) -> list[Outcomes]:
    """Policy re-solved at each kappa.  ``solve_fn`` is injected, not imported."""
    out = []
    for k in kappas:
        pk = p.replace(kappa=float(k))
        policy, _ = solve_fn(pk)
        out.append(evaluate(policy, pk, with_runup))
    return out
