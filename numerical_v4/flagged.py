"""The flagged side: b* inversion, flagged posterior, P^F, p, M_F.

Design section 6.1, build step 2.

Under injective A7 the flagged posterior conditions on (B^F, Q^F, a = 1) and
nothing else -- in particular not on the pooled history.  So the whole flagged
path touches no enumeration and no kappa, which is the entire content of L2 and
makes its check cheap and genuinely falsifying: if any kappa leaks in, the
range over the kappa grid is nonzero.

Guard against the design's largest named risk (9.1): the signal is recovered by
inverting b* = B^F + Q^F with brentq, never by a grid-index lookup.  The
closed-form inverse is used only as a cross-check.
"""

from __future__ import annotations

from typing import NamedTuple

import numpy as np
from scipy.stats import norm

from numerical_v4.menu import (
    Atom,
    VOICE,
    b_star,
    b_star_inverse_brentq,
    legal_clock,
)
from numerical_v4.params import ParamsV4, TOL_PROB
from numerical_v4.pooled import inner_price

INVERSION_TOL: float = 1e-9


class FlaggedResult(NamedTuple):
    """Flagged-cell objects.  Every field is invariant to kappa (L2)."""

    s: np.ndarray          # Gauss-Legendre nodes over the flagged atoms
    w: np.ndarray          # prior s-weights (unnormalised, sum = Omega)
    B_F: np.ndarray
    Q_F: np.ndarray
    v_hat: np.ndarray
    P_F: np.ndarray
    p_bid: np.ndarray
    M_F: float             # Delta_m * E[h | D = 1], h = pi*p with pi = 1
    Omega: float           # Pr(D = 1)
    max_inversion_error: float
    multiple_root_nodes: int


def flagged_nodes(atom_list: list[Atom], p: ParamsV4) -> FlaggedResult:
    """Gauss-Legendre quadrature over the flagged atoms (design section 1.4)."""
    flagged = [a for a in atom_list if a.D == 1]
    Omega = float(sum(a.w for a in flagged))
    if not flagged:
        z = np.zeros(0)
        return FlaggedResult(z, z, z, z, z, z, z, float("nan"), 0.0, 0.0, 0)

    x_gl, w_gl = np.polynomial.legendre.leggauss(p.n_gl)
    s_all, w_all, BF, QF = [], [], [], []
    for a in flagged:
        half = 0.5 * (a.hi - a.lo)
        mid = 0.5 * (a.hi + a.lo)
        s_nodes = mid + half * x_gl                       # strictly interior
        # Design risk 9.4: a node on a Gamma bin edge has an ambiguous mark
        # path.  Gauss-Legendre nodes are open, but assert the clearance rather
        # than trust it -- a node within 1e-12 of a breakpoint is a failure,
        # not a rounding decision.
        assert float(np.min(np.minimum(s_nodes - a.lo, a.hi - s_nodes))) > 1e-12, (
            f"quadrature node within 1e-12 of a breakpoint on [{a.lo}, {a.hi}]"
        )
        dens = norm.pdf((s_nodes - p.mu_v) / p.sigma_s) / p.sigma_s
        wq = w_gl * half * dens
        # Rescale to the atom's exact Phi-difference mass, so quadrature is
        # left to do only the averaging of p(s), never the mass accounting.
        wq = wq * (a.w / wq.sum()) if wq.sum() > TOL_PROB else wq
        s_all.append(s_nodes)
        w_all.append(wq)
        for s in s_nodes:
            cl = legal_clock(VOICE, float(s), p)
            BF.append(cl.B_F)
            QF.append(cl.Q_F)

    s = np.concatenate(s_all)
    w = np.concatenate(w_all)
    B_F = np.asarray(BF)
    Q_F = np.asarray(QF)

    # A7 in action: recover the signal from the filing alone, by root-finding.
    s_rec = np.array([b_star_inverse_brentq(float(b + q), p)
                      for b, q in zip(B_F, Q_F)])
    max_inv = float(np.max(np.abs(s_rec - s))) if s.size else 0.0

    v_hat = p.mu_v + p.beta * (s_rec - p.mu_v)
    sol = inner_price(v_hat, np.ones_like(v_hat), p)

    # pi = 1 on the flagged cell, so h = p and M_F = Delta_m * E[p | D = 1].
    M_F = (float(p.Delta_m * np.sum(w * sol.p_bid) / np.sum(w))
           if np.sum(w) > TOL_PROB else float("nan"))

    return FlaggedResult(s, w, B_F, Q_F, v_hat, sol.P, sol.p_bid, M_F, Omega,
                         max_inv, sol.n_bad_bracket)


def flagged_price_at(s: float, p: ParamsV4) -> tuple[float, float]:
    """(P^F, p) at a single flagged signal -- used by the payoff and by run_up."""
    cl = legal_clock(VOICE, s, p)
    assert cl.D == 1, (
        f"flagged_price_at called at s = {s!r}, where D = 0: there is no "
        f"flagged round and (B^F, Q^F) are undefined"
    )
    s_rec = b_star_inverse_brentq(float(cl.B_F + cl.Q_F), p)
    v_hat = p.mu_v + p.beta * (s_rec - p.mu_v)
    sol = inner_price(np.array([v_hat]), np.array([1.0]), p)
    return float(sol.P[0]), float(sol.p_bid[0])


def b_star_check(s: float, p: ParamsV4) -> float:
    """|closed-form inverse - brentq inverse| at b*(s); a cross-check only."""
    y = float(b_star(s, p))
    return abs(b_star_inverse_brentq(y, p) - s)
