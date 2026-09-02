"""Pooled-history enumeration, the inner pricing fixed point, run-up and jump.

Design sections 4 (enumeration), 5 (inner fixed points), build steps 4 and 5.

A pooled public history is the order-flow path X_{0:H}, X_d = q_{jd}(s) + z_d
with z_d in {-z_bar, 0, +z_bar} at probabilities (kappa/2, 1-kappa, kappa/2).
The blockholder's order while building is ``mark`` noise lumps (ADR 0003), so
q_{jd}(s) is ``mark`` on a buying date and 0 otherwise, z_bar is one lump,
supp X = {-1, 0, ..., mark + 1} and n_hist = (mark + 3)^(H+1).  A buying date
cannot produce flow below mark - 1 and an idle date cannot produce flow above
1, so the two sets overlap in {mark - 1, ..., 1}: at mark = 1 that is the two
values {0, 1} and at mark = 2 it is the single value {1}.

FACTORISED LIKELIHOOD (design section 4).  Marks are deterministic given the
type and noise is i.i.d. across dates, so

    L[h, theta] = (1-kappa)^n0 * (kappa/2)^(H+1-n0) * feasible(h, theta)

with n0 the count of zero-noise dates.  Both n0 (int8) and ``feasible`` (bool)
are independent of kappa and of the cutoffs, so they are computed once per H
and memoised.  Regenerating L at a new kappa is a table lookup.

Type index convention: the mark path of type n is 1 for d < n and 0 for d >= n.
n = 0 is the all-zero path (Exit and Hold); n in {1,...,H+1} are the Voice
accumulation lengths.  N_theta = H + 2.

DEVIATION FROM THE DESIGN (named, section 4 bullet 3).  The design chunks over
histories in blocks of 1e6 to cap the float64 working set.  This build never
materialises L as an (n_hist x N_theta) array at all: it accumulates the three
weighted sums one type at a time, so the peak temporary is a single
(n_hist,) float64 vector (33 MB at H = 10, mark = 1; 391 MB at H = 10,
mark = 2).  Same goal, less code.
"""

from __future__ import annotations

import time
from functools import lru_cache
from typing import NamedTuple

import numpy as np
from scipy.special import ndtr

from numerical_v4.menu import Atom, TypeReference, atoms, type_reference
from numerical_v4.params import ParamsV4, TOL_PROB

# ---------------------------------------------------------------------------
# Section 5: the inner pricing fixed point
# ---------------------------------------------------------------------------

_N_BISECT: int = 30
_N_NEWTON: int = 3
_INV_SQRT_2PI: float = 0.3989422804014327


def _phi(u: np.ndarray) -> np.ndarray:
    """Standard normal density; scipy.stats.norm.pdf is far too slow here."""
    return _INV_SQRT_2PI * np.exp(-0.5 * u * u)


def bid_probability(P: np.ndarray, m_tilde: np.ndarray,
                    p: ParamsV4) -> np.ndarray:
    """p(I) = 1 - Phi((P + K + m0 + pi*Delta_m - S_bar)/sigma_xi)."""
    return 1.0 - ndtr((P + p.K + m_tilde - p.S_bar) / p.sigma_xi)


def _price_residual(P: np.ndarray, V_hat: np.ndarray, m_tilde: np.ndarray,
                    p: ParamsV4) -> tuple[np.ndarray, np.ndarray]:
    """g(P) = (1-p)(P - V_hat) - p*m_tilde, and the entry probability."""
    pb = bid_probability(P, m_tilde, p)
    return (1.0 - pb) * (P - V_hat) - pb * m_tilde, pb


class PriceSolution(NamedTuple):
    P: np.ndarray
    p_bid: np.ndarray
    max_residual: float
    n_bad_bracket: int


def inner_price(v_hat: np.ndarray, pi: np.ndarray,
                p: ParamsV4) -> PriceSolution:
    """Solve P = E[Y | I] by vectorised bisection on a certified bracket.

    Do not iterate the map: the v4 card carries no discount factor (design
    section 13, ruling 3), so the naive iteration is not a contraction.

    The bracket is certified analytically.  Writing the fixed point as
    P = V_hat + m_tilde * p(P)/(1 - p(P)) shows the right-hand side is
    *decreasing* in P, so g(P) = P - RHS is strictly increasing and the root is
    unique.  lo = V_hat gives g < 0; hi = V_hat + m_tilde*p(lo)/(1-p(lo)) gives
    g >= 0.  ``n_bad_bracket`` counts nodes where that certificate fails --
    those are the ``multiple_root_nodes`` of design section 5, the direct
    numerical evidence about A5.
    """
    v_hat = np.atleast_1d(np.asarray(v_hat, dtype=float))
    pi = np.atleast_1d(np.asarray(pi, dtype=float))
    V_hat = v_hat + pi * p.Delta_V
    m_tilde = p.m0 + pi * p.Delta_m

    lo = V_hat.copy()
    g_lo, p_lo = _price_residual(lo, V_hat, m_tilde, p)
    p_lo_c = np.clip(p_lo, 0.0, 1.0 - 1e-12)
    # Pad by a few ulp of the quantities entering g.  Where p(V_hat) ~ 1e-9 the
    # analytic bracket is only ~3e-9 wide and the true g(hi) ~ m*p^2 ~ 3e-19,
    # which is below the rounding noise of the subtraction -- the certificate
    # would then report a sign failure that is arithmetic, not multiplicity.
    pad = 16.0 * np.finfo(float).eps * (np.abs(V_hat) + m_tilde)
    hi = V_hat + m_tilde * p_lo_c / (1.0 - p_lo_c) + pad
    g_hi, _ = _price_residual(hi, V_hat, m_tilde, p)

    n_bad = int(np.count_nonzero(~((g_lo <= 0.0) & (g_hi >= 0.0))))

    for _ in range(_N_BISECT):
        mid = 0.5 * (lo + hi)
        g_mid, _ = _price_residual(mid, V_hat, m_tilde, p)
        neg = g_mid < 0.0
        lo = np.where(neg, mid, lo)
        hi = np.where(neg, hi, mid)

    P = 0.5 * (lo + hi)
    for _ in range(_N_NEWTON):
        g, pb = _price_residual(P, V_hat, m_tilde, p)
        u = (P + p.K + m_tilde - p.S_bar) / p.sigma_xi
        dg = (1.0 - pb) + _phi(u) / p.sigma_xi * (P - V_hat + m_tilde)
        P = P - g / np.where(np.abs(dg) < 1e-300, 1e-300, dg)

    g, pb = _price_residual(P, V_hat, m_tilde, p)
    return PriceSolution(P, pb, float(np.max(np.abs(g))) if g.size else 0.0,
                         n_bad)


def prior_price(atom_list: list[Atom], p: ParamsV4) -> float:
    """P_{-1}^P := E[Y], the pre-trading pooled price (card section 4.3)."""
    w = np.array([a.w for a in atom_list])
    pi0 = float(np.sum(w * np.array([a.a for a in atom_list])) / np.sum(w))
    v0 = float(np.sum(w * np.array([a.Ev for a in atom_list])) / np.sum(w))
    return float(inner_price(np.array([v0]), np.array([pi0]), p).P[0])


# ---------------------------------------------------------------------------
# Section 4: the kappa-free exponent and feasibility arrays
# ---------------------------------------------------------------------------


class MarkStats(NamedTuple):
    """Per date d: n0 and feasibility over (prefixes of length d+1) x types."""

    n0: tuple[np.ndarray, ...]     # int8, shape ((mark+3)**(d+1), H+2)
    feas: tuple[np.ndarray, ...]   # bool, same shape


@lru_cache(maxsize=2)
def mark_stats(H: int, mark: int) -> MarkStats:
    """Build n0 and feasibility incrementally over dates (design section 4).

    ``base = mark + 3`` is the size of supp X = {-1, 0, ..., mark + 1}.  Child
    index of prefix i with appended digit x is base*i + x, which is exactly
    ``np.repeat(parent, base)`` aligned against ``np.tile(digit_table,
    n_parent)``.

    A buying date (mark path 1) executes ``mark`` lumps, so its zero-noise
    outcome is X = mark and its support is {mark - 1, mark, mark + 1}; an idle
    date's zero-noise outcome is X = 0 and its support is {-1, 0, 1}.
    """
    if mark < 1:
        raise ValueError(f"order size must be at least one lump, got {mark}")
    base = mark + 3
    n_theta = H + 2
    n_arr = np.arange(n_theta)
    digits = np.arange(base, dtype=np.int8) - 1   # X in {-1, 0, ..., mark+1}

    n0 = np.zeros((1, n_theta), dtype=np.int8)
    feas = np.ones((1, n_theta), dtype=bool)
    n0_list, feas_list = [], []
    for d in range(H + 1):
        mark1 = (d < n_arr)[None, :]                      # (1, n_theta)
        inc = np.where(mark1, digits[:, None] == mark,
                       digits[:, None] == 0).astype(np.int8)
        ok = np.where(mark1, digits[:, None] >= mark - 1, digits[:, None] <= 1)
        n0 = np.repeat(n0, base, axis=0) + np.tile(inc, (n0.shape[0], 1))
        feas = np.repeat(feas, base, axis=0) & np.tile(ok, (feas.shape[0], 1))
        n0_list.append(n0)
        feas_list.append(feas)
    return MarkStats(tuple(n0_list), tuple(feas_list))


def _likelihood_lut(d: int, kappa: float) -> np.ndarray:
    """lut[e] = (1-kappa)^e * (kappa/2)^(d+1-e) for e = 0..d+1."""
    e = np.arange(d + 2, dtype=float)
    return (1.0 - kappa) ** e * (kappa / 2.0) ** (d + 1.0 - e)


# ---------------------------------------------------------------------------
# The pooled pass
# ---------------------------------------------------------------------------


class PooledResult(NamedTuple):
    """Everything the pooled cell contributes, per date and per type."""

    dates: tuple[int, ...]
    price: dict[int, np.ndarray]       # d -> P_d^P, nan on dead prefixes
    pi: dict[int, np.ndarray]          # d -> engagement posterior
    p_bid: dict[int, np.ndarray]       # d -> bidder entry probability
    mass: dict[int, np.ndarray]        # d -> sum_a w_a L_d[h, theta(a)]
    EP: dict[int, np.ndarray]          # d -> (n_theta,) E[P_d^P | theta]
    Ep_bid: np.ndarray                 # (n_theta,) E[p_H | theta]
    EpP: np.ndarray                    # (n_theta,) E[p_H*(P_H) | theta]
    n_hist_feasible: int
    n_alive_terminal: int
    multiple_root_nodes: int
    max_price_residual: float
    P_prior: float


OFF_PATH_EPS: float = 1e-14


def _alive_weights(atom_list: list[Atom], d: int, n_theta: int,
                   ref: "TypeReference | None" = None
                   ) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Type weights, w*E[v] and w*a over atoms whose flag has not landed by d.

    Returns the *measure* weights and, separately, *market* weights carrying a
    full-support floor on types that no equilibrium signal selects (card
    section 3 clause vi).  The measure integrates M_P and Omega; the market
    weights only set beliefs, so the floor never leaks into a reported mass.
    """
    W = np.zeros(n_theta)
    WV = np.zeros(n_theta)
    WA = np.zeros(n_theta)
    for a in atom_list:
        if a.D == 1 and a.f <= d:
            continue                        # flag already public at date d
        W[a.theta] += a.w
        WV[a.theta] += a.w * a.Ev
        WA[a.theta] += a.w * a.a

    Wm, WVm, WAm = W.copy(), WV.copy(), WA.copy()
    if ref is not None:
        for t in range(n_theta):
            if Wm[t] > 0.0:
                continue
            if ref.D[t] == 1.0 and ref.f[t] <= d:
                continue                    # this type's flag would be public
            Wm[t] = OFF_PATH_EPS
            WVm[t] = OFF_PATH_EPS * ref.Ev[t]
            WAm[t] = OFF_PATH_EPS * ref.a[t]
    return W, Wm, WVm, WAm


def pooled_pass(atom_list: list[Atom], p: ParamsV4,
                with_runup: bool = True) -> PooledResult:
    """Enumerate pooled histories and price every live public history.

    ``with_runup=False`` computes only the control-node date d = H, which is
    all that M_P, Delta^act and S_P need; the run-up path R_d and the jump J
    need the earlier dates and cost roughly three times as much.
    """
    ms = mark_stats(p.H, p.mark)
    ref = type_reference(p)
    n_theta = p.n_theta
    dates = tuple(range(p.H + 1)) if with_runup else (p.H,)

    price: dict[int, np.ndarray] = {}
    pi_d: dict[int, np.ndarray] = {}
    pbid_d: dict[int, np.ndarray] = {}
    mass_d: dict[int, np.ndarray] = {}
    EP: dict[int, np.ndarray] = {}
    n_bad = 0
    max_res = 0.0

    Ep_bid = np.zeros(n_theta)
    EpP = np.zeros(n_theta)

    for d in dates:
        n0, feas = ms.n0[d], ms.feas[d]
        lut = _likelihood_lut(d, p.kappa)
        W, Wm, WVm, WAm = _alive_weights(atom_list, d, n_theta, ref)

        n = n0.shape[0]
        mass = np.zeros(n)       # measure: on-path weights only
        market = np.zeros(n)     # beliefs: with the full-support floor
        num_v = np.zeros(n)
        num_a = np.zeros(n)
        for t in range(n_theta):
            if Wm[t] <= 0.0:
                continue
            Lt = lut[n0[:, t]]
            Lt *= feas[:, t]
            if W[t] > 0.0:
                mass += W[t] * Lt
            market += Wm[t] * Lt
            num_v += WVm[t] * Lt
            num_a += WAm[t] * Lt

        live = market > 0.0
        vhat = np.full(n, np.nan)
        pi = np.full(n, np.nan)
        vhat[live] = num_v[live] / market[live]
        pi[live] = num_a[live] / market[live]

        sol = inner_price(vhat[live], pi[live], p)
        P = np.full(n, np.nan)
        pb = np.full(n, np.nan)
        P[live] = sol.P
        pb[live] = sol.p_bid
        n_bad += sol.n_bad_bracket
        max_res = max(max_res, sol.max_residual)

        price[d] = P
        pi_d[d] = pi
        pbid_d[d] = pb
        mass_d[d] = mass

        # E[P_d^P | theta]: the blockholder's expected execution price.
        ep = np.zeros(n_theta)
        Pz = np.where(live, P, 0.0)
        for t in range(n_theta):
            Lt = lut[n0[:, t]]
            Lt *= feas[:, t]
            ep[t] = float(np.dot(Lt, Pz))
        EP[d] = ep

        if d == p.H:
            pbz = np.where(live, pb, 0.0)
            for t in range(n_theta):
                Lt = lut[n0[:, t]]
                Lt *= feas[:, t]
                Ep_bid[t] = float(np.dot(Lt, pbz))
                EpP[t] = float(np.dot(Lt, pbz * Pz))

    feas_H = ms.feas[p.H]
    n_feasible = int(np.count_nonzero(feas_H.any(axis=1)))

    return PooledResult(
        dates=dates, price=price, pi=pi_d, p_bid=pbid_d, mass=mass_d, EP=EP,
        Ep_bid=Ep_bid, EpP=EpP, n_hist_feasible=n_feasible,
        n_alive_terminal=int(np.count_nonzero(mass_d[p.H] > TOL_PROB)),
        multiple_root_nodes=n_bad, max_price_residual=max_res,
        P_prior=prior_price(atom_list, p),
    )


# ---------------------------------------------------------------------------
# Run-up path, cumulative run-up, filing-day jump (card section 4.3)
# ---------------------------------------------------------------------------


class RunUp(NamedTuple):
    """Per flagged atom: the run-up and jump objects over pooled prefixes."""

    c: int
    f: int
    P_c_minus: np.ndarray   # P_{c-1}^P per prefix of length f
    P_f_minus: np.ndarray   # P_{f-1}^P per prefix of length f
    R: np.ndarray           # cumulative run-up
    J: np.ndarray           # filing-day jump P^F - P_ND
    identity: np.ndarray    # |P^F - P_{c-}^P - R - J|
    weight: np.ndarray      # prefix probability under the atom's own type


def run_up(res: PooledResult, atom: Atom, P_F: float,
           p: ParamsV4) -> RunUp:
    """R_d, R, J and the D1 identity for one flagged atom.

    ``P_ND`` is the pooled price at the same realised order flow with no flag,
    which the card fixes as ``P_{f-}^P`` by construction.  Prefix indices at
    date f-1 map to their ancestors at date c-1 by integer division by
    (mark+3)**T.
    """
    assert atom.D == 1, "run_up is defined on flagged atoms only"
    c, f = int(atom.c), int(atom.f)
    ms = mark_stats(p.H, p.mark)

    P_fm = res.price[f - 1] if f >= 1 else None
    if P_fm is None:
        raise ValueError("f = 0 has no pre-filing pooled date")
    if c == 0:
        P_cm = np.full(P_fm.shape, res.P_prior)
    else:
        anc = np.arange(P_fm.size) // (p.n_flow ** (f - c))
        P_cm = res.price[c - 1][anc]

    lut = _likelihood_lut(f - 1, p.kappa)
    n0, feas = ms.n0[f - 1], ms.feas[f - 1]
    weight = lut[n0[:, atom.theta]] * feas[:, atom.theta]

    R = P_fm - P_cm
    J = P_F - P_fm
    identity = np.abs((P_F - P_cm) - R - J)
    return RunUp(c, f, P_cm, P_fm, R, J, identity, weight)


# ---------------------------------------------------------------------------
# Build step 4: the enumeration probe -- the go/no-go gate
# ---------------------------------------------------------------------------


class Probe(NamedTuple):
    H: int
    M: int
    n_hist: int
    n_hist_feasible: int
    n_theta: int
    n_theta_populated: int
    product: float          # feasible n_hist * N_theta -- the gate quantity
    int8_bytes: int
    eval_seconds: float
    gate_limit: float
    gate_pass: bool


GATE_LIMIT: float = 1e8


def probe(p: ParamsV4, k: tuple[float, ...]) -> Probe:
    """Feasible history count, N_theta, array size, one evaluation's wall time.

    GATE (design build step 4, section 13): if feasible n_hist * N_theta
    exceeds 1e8, stop and re-open design open questions 1 and 2 before writing
    any pricing code.
    """
    al = atoms(k, p)
    ms = mark_stats(p.H, p.mark)
    feas_H = ms.feas[p.H]
    n_feasible = int(np.count_nonzero(feas_H.any(axis=1)))
    W, _, _, _ = _alive_weights(al, p.H, p.n_theta)
    populated = int(np.count_nonzero(W > 0.0))

    t0 = time.perf_counter()
    pooled_pass(al, p, with_runup=False)
    dt = time.perf_counter() - t0

    product = float(n_feasible) * p.n_theta
    return Probe(
        H=p.H, M=2, n_hist=p.n_hist, n_hist_feasible=n_feasible,
        n_theta=p.n_theta, n_theta_populated=populated, product=product,
        int8_bytes=int(ms.n0[p.H].nbytes + ms.feas[p.H].nbytes),
        eval_seconds=dt, gate_limit=GATE_LIMIT, gate_pass=product <= GATE_LIMIT,
    )
