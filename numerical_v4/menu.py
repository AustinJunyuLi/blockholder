"""Plan menu, the coarsening Gamma, the legal clock, breakpoints, A7 probe.

Design section 2 (menu), section 1 (breakpoint-first discretisation of s),
section 3 (calendar).  Build step 1.

The menu is J = 3: Exit, Hold, one Voice family (design section 2).

    j            a_j   B_j(s,d)                                mark path
    1 Exit       0     b0 -> 0 in one day-0 block, then flat   all zeros
    2 Hold       0     flat at b0                              all zeros
    3 Voice      1     b0 + (b*(s)-b0)*min(1,(d+1)/n(s))       n(s) ones, zeros

PINNED FUNCTIONAL FORMS (design section 2 asks for "simple explicit forms").

    b*(s) = b0 + (b_bar - b0) * (1 + x/sqrt(1+x^2))/2,   x = (s - mu_v)/sigma_s

The algebraic sigmoid, *not* the Gaussian one: it is strictly increasing on the
whole line with **polynomial** tails, so d b*/ds stays above 1e-8 across the
entire s-span.  Phi((s-mu)/sigma) would decay like exp(-x^2/2) and fail the
a7_certificate min-slope gate at the top of the support.

    n(s) = clip(ceil(n_scale*(H+1)*(1 - g(x))), 1, H+1),  g = the same sigmoid

Weakly decreasing in s -- a stronger signal accumulates faster (design 2).

    Gamma(x) = 1{x >= gamma_bar}, gamma_bar = 1e-6  (M = 2 marks, design 2)

gamma_bar sits below every realised positive increment, so the Voice mark path
is exactly "n(s) ones then zeros" and N_theta = H + 2 as the design counts it.
Exit's day-0 increment is negative and marks 0, so Exit and Hold pool perfectly
in order flow -- the deliberate flattening of design section 2, ruled
acceptable by design section 13 ruling 1.
"""

from __future__ import annotations

import math
from typing import NamedTuple

import numpy as np
from scipy.optimize import brentq
from scipy.stats import norm

from numerical_v4.params import EXIT, HOLD, VOICE, ParamsV4, TOL_PROB

# ---------------------------------------------------------------------------
# b*(s), n(s), Gamma
# ---------------------------------------------------------------------------


def _sigmoid(x: float | np.ndarray) -> float | np.ndarray:
    """Algebraic sigmoid on (0,1): (1 + x/sqrt(1+x^2))/2."""
    return 0.5 * (1.0 + x / np.sqrt(1.0 + x * x))


def _sigmoid_inv(g: float) -> float:
    """Inverse of ``_sigmoid`` on (0,1)."""
    u = 2.0 * g - 1.0
    return float(u / math.sqrt(1.0 - u * u))


def b_star(s: float | np.ndarray, p: ParamsV4) -> float | np.ndarray:
    """Terminal target stake b*(s) = B_Voice(s, H).  Strictly increasing."""
    x = (np.asarray(s, dtype=float) - p.mu_v) / p.sigma_s
    out = p.b0 + (p.b_bar - p.b0) * _sigmoid(x)
    return float(out) if np.isscalar(s) or np.ndim(s) == 0 else out


def b_star_prime(s: float | np.ndarray, p: ParamsV4) -> float | np.ndarray:
    """db*/ds; polynomial tails, so bounded away from 0 on the whole span."""
    x = (np.asarray(s, dtype=float) - p.mu_v) / p.sigma_s
    out = 0.5 * (p.b_bar - p.b0) * (1.0 + x * x) ** -1.5 / p.sigma_s
    return float(out) if np.isscalar(s) or np.ndim(s) == 0 else out


def b_star_inverse(y: float, p: ParamsV4) -> float:
    """Closed-form inverse of b*.  Used only for breakpoint generation;
    the flagged posterior inverts with brentq instead (design risk 9.1)."""
    u = 2.0 * (y - p.b0) / (p.b_bar - p.b0) - 1.0
    if not (-1.0 < u < 1.0):
        return math.nan
    return p.mu_v + p.sigma_s * (u / math.sqrt(1.0 - u * u))


def b_star_inverse_brentq(y: float, p: ParamsV4) -> float:
    """Invert b* by root-finding, never by a grid lookup (design risk 9.1)."""
    return float(brentq(lambda s: b_star(s, p) - y, p.s_lo, p.s_hi, xtol=1e-14,
                        rtol=1e-15))


def n_days(s: float, p: ParamsV4) -> int:
    """Accumulation length n(s) in {1,...,H+1}; weakly decreasing in s."""
    x = (s - p.mu_v) / p.sigma_s
    raw = p.n_scale * (p.H + 1) * (1.0 - _sigmoid(x))
    return int(np.clip(math.ceil(raw), 1, p.H + 1))


def gamma_mark(increment: float, p: ParamsV4) -> int:
    """The coarsening Gamma: binary buy-indicator, M = 2 marks."""
    return 1 if increment >= p.gamma_bar else 0


# ---------------------------------------------------------------------------
# Stake paths and mark paths
# ---------------------------------------------------------------------------


def stake_path(j: int, s: float, p: ParamsV4) -> np.ndarray:
    """B_j(s, d) for d = -1, 0, ..., H (index 0 holds B(s,-1) = b0)."""
    d = np.arange(p.H + 1, dtype=float)
    if j == EXIT:
        body = np.zeros(p.H + 1)
    elif j == HOLD:
        body = np.full(p.H + 1, p.b0)
    elif j == VOICE:
        bs = b_star(s, p)
        n = n_days(s, p)
        body = p.b0 + (bs - p.b0) * np.minimum(1.0, (d + 1.0) / n)
    else:
        raise ValueError(f"unknown plan {j}")
    return np.concatenate(([p.b0], body))


def terminal_stake(j: int, s: float, p: ParamsV4) -> float:
    """b*_j(s) = B_j(s, H)."""
    if j == EXIT:
        return 0.0
    if j == HOLD:
        return p.b0
    return float(b_star(s, p))


def mark_path(j: int, s: float, p: ParamsV4) -> tuple[int, ...]:
    """q_{jd}(s) = Gamma(B(s,d) - B(s,d-1)) for d = 0..H."""
    B = stake_path(j, s, p)
    return tuple(gamma_mark(float(B[d + 1] - B[d]), p) for d in range(p.H + 1))


def theta_index(j: int, s: float, p: ParamsV4) -> int:
    """Mark-path type index n: the path is 1 for d < n and 0 for d >= n.

    n = 0 is the all-zero path shared by Exit and Hold; n in {1,...,H+1} are the
    Voice paths.  N_theta = H + 2 = 12 at H = 10 (design section 4).
    """
    if j != VOICE:
        return 0
    return n_days(s, p)


# ---------------------------------------------------------------------------
# Legal clock (card section 4.2)
# ---------------------------------------------------------------------------


class Clock(NamedTuple):
    """Crossing date, filing date, disclosure flag, and the filing objects."""

    c: float          # crossing date, +inf if the path never reaches tau
    f: float          # filing date c + T
    D: int            # disclosure indicator
    B_F: float        # stake at filing, nan when D = 0
    Q_F: float        # flagged-round order b* - B^F, nan when D = 0


def legal_clock(j: int, s: float, p: ParamsV4) -> Clock:
    """c, f, D, B^F, Q^F for plan j at signal s (card section 4.2)."""
    if j != VOICE:
        return Clock(math.inf, math.inf, 0, math.nan, math.nan)
    bs = b_star(s, p)
    if bs < p.tau:
        return Clock(math.inf, math.inf, 0, math.nan, math.nan)
    n = n_days(s, p)
    ratio = (p.tau - p.b0) / (bs - p.b0)
    c = min(max(math.ceil(ratio * n) - 1, 0), n - 1)
    f = c + p.T
    if f > p.H:
        return Clock(float(c), float(f), 0, math.nan, math.nan)
    B = stake_path(j, s, p)
    B_F = float(B[int(f) + 1])
    return Clock(float(c), float(f), 1, B_F, float(bs - B_F))


def disclosure_by_scan(j: int, s: float, p: ParamsV4) -> int:
    """D via an explicit date-by-date crossing scan (D1, route 1)."""
    if j != VOICE:
        return 0
    B = stake_path(j, s, p)
    for d in range(p.H + 1):
        if B[d + 1] >= p.tau:
            return 1 if d + p.T <= p.H else 0
    return 0


def disclosure_by_h_minus_T(j: int, s: float, p: ParamsV4) -> int:
    """D via the card's one-shot equivalence B(s, H-T) >= tau (D1, route 2)."""
    if j != VOICE:
        return 0
    B = stake_path(j, s, p)
    return int(B[(p.H - p.T) + 1] >= p.tau)


# ---------------------------------------------------------------------------
# Breakpoints and atoms (design section 1)
# ---------------------------------------------------------------------------


def signature(s: float, k: tuple[float, ...], p: ParamsV4) -> tuple:
    """Everything that must be constant on an atom of the s-partition."""
    j = EXIT if s < k[0] else (HOLD if s < k[1] else VOICE)
    cl = legal_clock(j, s, p)
    return (j, theta_index(j, s, p), cl.c, cl.f, cl.D)


def breakpoints(k: tuple[float, ...], p: ParamsV4) -> np.ndarray:
    """Sorted breakpoint set S_break (design section 1, step 1).

    Plan cutoffs, the pull-backs of the Gamma bin edges (equivalently the jump
    points of n(s)), and the pull-backs of every tau-crossing date.
    """
    pts: list[float] = [p.s_lo, p.s_hi]
    pts += [float(x) for x in k if p.s_lo < x < p.s_hi]

    # Jump points of n(s): n_scale*(H+1)*(1 - g(x)) = m, m = 1..H+1
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            pts.append(p.mu_v + p.sigma_s * _sigmoid_inv(g))

    # tau-crossing pull-backs: B(s,d) = tau within an n-plateau means
    # b*(s) = b0 + (tau - b0) * n / min(d+1, n).
    for n in range(1, p.H + 2):
        for d in range(p.H + 1):
            y = p.b0 + (p.tau - p.b0) * n / min(d + 1, n)
            if p.b0 < y < p.b_bar:
                s = b_star_inverse(y, p)
                if not math.isnan(s):
                    pts.append(s)

    arr = np.array([x for x in pts if p.s_lo - 1e-12 <= x <= p.s_hi + 1e-12])
    arr = np.clip(arr, p.s_lo, p.s_hi)
    arr = np.sort(arr)
    # Merge near-duplicates: a cutoff landing on an n-jump would otherwise
    # leave a 1e-12-wide atom whose midpoint signature is unreliable.
    keep = np.concatenate(([True], np.diff(arr) > 1e-9))
    return arr[keep]


class Atom(NamedTuple):
    """An interval of s on which the whole plan/clock signature is constant."""

    lo: float
    hi: float
    plan: int
    a: int
    theta: int
    c: float
    f: float
    D: int
    w: float       # prior mass Pr(s in [lo, hi))
    Ev: float      # E[v | s in [lo, hi))


def _interval_mass_and_mean(lo: float, hi: float, p: ParamsV4) -> tuple[float, float]:
    """Exact Phi-difference mass and truncated-normal E[v|interval]."""
    al = (lo - p.mu_v) / p.sigma_s
    ah = (hi - p.mu_v) / p.sigma_s
    w = float(norm.cdf(ah) - norm.cdf(al))
    if w < TOL_PROB:
        Es = 0.5 * (lo + hi)
    else:
        Es = p.mu_v + p.sigma_s * float(norm.pdf(al) - norm.pdf(ah)) / w
    return w, p.mu_v + p.beta * (Es - p.mu_v)


def atoms(k: tuple[float, ...], p: ParamsV4, verify: bool = True) -> list[Atom]:
    """Partition the s-support into signature-constant atoms."""
    bps = breakpoints(k, p)
    out: list[Atom] = []
    for lo, hi in zip(bps[:-1], bps[1:]):
        if hi - lo < 1e-13:
            continue
        mid = 0.5 * (lo + hi)
        j, th, c, f, D = signature(mid, k, p)
        if verify:
            for frac in (0.15, 0.85):
                s = lo + frac * (hi - lo)
                assert signature(s, k, p) == (j, th, c, f, D), (
                    f"breakpoint set incomplete on [{lo}, {hi}]"
                )
        w, Ev = _interval_mass_and_mean(lo, hi, p)
        out.append(Atom(float(lo), float(hi), j, int(j == VOICE), th,
                        c, f, D, w, Ev))
    # Normalise: the +-s_span truncation leaks ~2e-9 of tail mass, which would
    # otherwise show up as a spurious residual in the L1 decomposition.
    tot = sum(a.w for a in out)
    return [a._replace(w=a.w / tot) for a in out]


# ---------------------------------------------------------------------------
# Off-path reference types (card section 3, clause vi)
# ---------------------------------------------------------------------------


class TypeReference(NamedTuple):
    """Beliefs to attach to a mark path that carries no equilibrium mass.

    Card section 3 clause (vi) fixes off-path beliefs as limits of full-support
    perturbations.  Numerically that is a weight floor: a mark path only a
    zero-mass Voice type could produce is still priced, and it is priced as if
    that Voice type had produced it.  Without this the pricing map has holes,
    and the outer map T(k) jumps by ~0.1 in the cutoff whenever a type's mass
    crosses zero -- which is exactly where the equilibrium sits.

    The reference is computed from the n(s) partition of the whole signal line,
    so it does not move with the cutoffs.
    """

    Ev: np.ndarray      # (H+2,) E[v | n(s) = t]
    a: np.ndarray       # (H+2,) engagement of the reference type
    D: np.ndarray       # (H+2,) disclosure of the reference type
    f: np.ndarray       # (H+2,) filing date of the reference type


def type_reference(p: ParamsV4) -> TypeReference:
    """Reference beliefs per mark-path type, independent of the cutoffs."""
    edges = [p.s_lo, p.s_hi]
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            x = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo < x < p.s_hi:
                edges.append(x)
    edges = sorted(set(edges))

    n_t = p.H + 2
    Ev = np.full(n_t, p.mu_v)
    a = np.zeros(n_t, dtype=float)
    D = np.zeros(n_t, dtype=float)
    f = np.full(n_t, math.inf)
    acc: dict[int, list[tuple[float, float]]] = {}
    for lo, hi in zip(edges[:-1], edges[1:]):
        t = n_days(0.5 * (lo + hi), p)
        acc.setdefault(t, []).append((lo, hi))

    for t, ivs in acc.items():
        wsum = 0.0
        vsum = 0.0
        for lo, hi in ivs:
            w, ev = _interval_mass_and_mean(lo, hi, p)
            wsum += w
            vsum += w * ev
        Ev[t] = vsum / wsum if wsum > TOL_PROB else p.mu_v
        a[t] = 1.0
        mid = 0.5 * (ivs[0][0] + ivs[-1][1])
        cl = legal_clock(VOICE, mid, p)
        D[t] = float(cl.D)
        f[t] = cl.f
    return TypeReference(Ev, a, D, f)


# ---------------------------------------------------------------------------
# A7 certificate (design section 2, risk 9.1)
# ---------------------------------------------------------------------------


class A7Certificate(NamedTuple):
    """Evidence that A7' holds on this menu (design section 13, ruling 7)."""

    min_slope: float          # min |db*/ds| over the flagged set
    n_flat_subintervals: int  # sub-intervals with slope below 1e-12
    n_collisions: int         # (B^F, Q^F) pairs colliding at 1e-12
    n_cross_plan: int         # cross-plan collisions (0: one Voice family)
    passes: bool              # min_slope >= 1e-8
    n_flagged_atoms: int


A7_MIN_SLOPE: float = 1e-8


def a7_certificate(k: tuple[float, ...], p: ParamsV4,
                   atom_list: list[Atom] | None = None) -> A7Certificate:
    """min |db*/ds| on the flagged set, flat-interval and collision counts.

    A7' (ticket 24): the composed terminal target s -> b*_{j(s)}(s) is strictly
    increasing on the flagged signal region.  Because B^F + Q^F = b*(s)
    identically on this menu, injectivity of (B^F, Q^F) reduces to that.
    """
    al = atom_list if atom_list is not None else atoms(k, p)
    flagged = [a for a in al if a.D == 1]
    if not flagged:
        return A7Certificate(math.inf, 0, 0, 0, False, 0)

    nodes, sums = [], []
    min_slope = math.inf
    n_flat = 0
    for a in flagged:
        grid = np.linspace(a.lo, a.hi, 41)
        slopes = np.asarray(b_star_prime(grid, p))
        min_slope = min(min_slope, float(slopes.min()))
        n_flat += int((slopes < 1e-12).sum())
        for s in grid:
            cl = legal_clock(VOICE, float(s), p)
            nodes.append(s)
            sums.append(cl.B_F + cl.Q_F)

    # Distinct signals only: adjacent atoms share an endpoint, and a repeated
    # s is not an injectivity failure.
    s_arr = np.asarray(nodes)
    sum_arr = np.asarray(sums)
    order = np.argsort(s_arr)
    s_arr, sum_arr = s_arr[order], sum_arr[order]
    keep = np.concatenate(([True], np.diff(s_arr) > 1e-12))
    gaps = np.diff(sum_arr[keep])
    n_coll = int((np.abs(gaps) < 1e-12).sum())

    return A7Certificate(float(min_slope), n_flat, n_coll, 0,
                         bool(min_slope >= A7_MIN_SLOPE), len(flagged))
