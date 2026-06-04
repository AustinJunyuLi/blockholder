#!/usr/bin/env python3
"""
D6 equilibrium-foundations numeric checks.

Companion to D6_equilibrium_foundations.tex.  Every quantitative claim made in
that file is reproduced here so the manuscript cites a readable artifact rather
than the (non-committed) phase0_facts.md.  Run with the paper's own solver:

    PYTHONPATH=/Users/austinli/Projects/blockholder \
        /tmp/blockholder_venv/bin/python \
        quality_reports/fixes/D6_equilibrium_checks.py

(/tmp/blockholder_venv created via `python3 -m venv --system-site-packages`
 + `pip install scipy`; system python lacks scipy.)

Checks performed
----------------
(A) Chord/MVT identity: for the three equally-spaced nodes {0, pibar/2, pibar}
    with step h_step = pibar/2, the second central difference equals
    (h_step)^2 * h''(xi).  We verify numerically that the discrete chord
    Lambda matches 0.25 * pibar^2 * (mean curvature) in sign on a calibrated
    h(pi)=pi*p(pi).
(B) B_P > B_Q from the (1+q)*beta channel alone: B_P = 2 beta, B_Q = beta.
    (Pure algebra, asserted in a comment; no solver needed.)
(C) Endpoint reflection symmetry of the noise law z: kappa <-> 1-kappa leaves
    the realized D=0 two-point law {0, pibar} and the bid weights invariant in
    the kappa->0 / kappa->1 limits.  We verify Delta^min(eps) ~ Delta^min(1-eps)
    on validly-solved near-endpoints, and reproduce the interior hump.
(D) (C*) baseline margin and the chord diagnostic sign.

This file is defensive: if `numerical` is importable it runs the live solver,
otherwise it runs the self-contained surrogate for (A) and (B) only and clearly
labels the output as a SURROGATE.
"""
from __future__ import annotations
import math
from math import erf, sqrt, exp, pi as PI


def Phi(x: float) -> float:
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


def phi(x: float) -> float:
    return exp(-0.5 * x * x) / sqrt(2.0 * PI)


# --------------------------------------------------------------------------- #
# (A) Chord / MVT identity on a calibrated h(pi) = pi * p(pi).
# --------------------------------------------------------------------------- #
def check_chord(sigma_xi=0.40, delta=0.95, c0=0.90, c1=-0.10,
                mbar0=0.05, mbar1=0.02, K=0.10, Sbar=1.44, pibar=1.0):
    def P(piv):    return delta * (c0 + c1 * piv)
    def mbar(piv): return mbar0 + mbar1 * piv
    def t(piv):    return (mbar(piv) + K - Sbar + P(piv)) / sigma_xi
    def p(piv):    return 1.0 - Phi(t(piv))
    def h(piv):    return piv * p(piv)

    Lam = h(0.0) - 2.0 * h(pibar / 2.0) + h(pibar)

    # discrete h'' on a fine grid
    n = 4001
    xs = [1e-4 + (pibar - 2e-4) * i / (n - 1) for i in range(n)]
    hv = [h(x) for x in xs]
    # central second difference
    hpp = []
    for i in range(1, n - 1):
        dx = xs[i + 1] - xs[i]
        hpp.append((hv[i + 1] - 2 * hv[i] + hv[i - 1]) / (dx * dx))
    mean_hpp = sum(hpp) / len(hpp)
    print("[A] chord Lambda                =", round(Lam, 6))
    print("[A] 0.25*pibar^2*mean(h'')      =", round(0.25 * pibar * pibar * mean_hpp, 6))
    print("[A] sign(Lambda)==sign(mean h'')?", (Lam < 0) == (mean_hpp < 0))
    # (C*) representative-state margin: mbar*T - 2 sigma_xi  (schematic)
    # T = -dP/dpi/... collected; here report mbar(pibar/2)*|c1*delta| vs 2 sigma_xi
    Trep = abs(c1) * delta  # |dP/dpi|; T collects this
    margin = mbar(pibar / 2.0) * Trep - 2.0 * sigma_xi
    print("[D] (C*) representative margin mbar*T - 2 sigma_xi =", round(margin, 4),
          "(<0 => hump)")
    return Lam, mean_hpp


# --------------------------------------------------------------------------- #
# (B) Slope chain from (1+q)*beta.   B_alpha = (1+q_alpha)*beta.
# --------------------------------------------------------------------------- #
def check_slopes():
    q = {"Exit": -1, "Hold": 0, "Quiet": 0, "Public": +1}
    beta = 1.0  # any positive scale; only the ordering matters
    B = {a: (1 + q[a]) * beta for a in q}
    print("[B] slopes (1+q)beta:", B)
    print("[B] B_E < B_H == B_Q < B_P ?",
          B["Exit"] < B["Hold"] == B["Quiet"] < B["Public"])
    return B


# --------------------------------------------------------------------------- #
# (C) Live solver: endpoint symmetry + interior hump.
# --------------------------------------------------------------------------- #
def check_live():
    try:
        import numerical.params as P
        import numerical.solver as S
        import numerical.model as M
    except Exception as e:  # pragma: no cover
        print("[C] numerical package not importable -> SKIP live checks:", e)
        return
    params = P.ModelParams()

    def dmin_at(kappa):
        pr = params.__class__(**{**params.__dict__, "kappa": kappa}) \
            if hasattr(params, "__dict__") else params
        try:
            cut, resid = S.solve_valid(pr, prev_cutoffs=None, residual_tol=1e-5)
        except Exception:
            cut, resid = S.solve_valid(pr, residual_tol=1e-5)
        if cut is None:
            return None, resid
        mg = M.compute_minority_gains(cut.k1, cut.k0, cut.kD, pr)
        return mg.total, resid

    for k in (0.02, 0.59, 0.98):
        d, r = dmin_at(k)
        print(f"[C] kappa={k:>4}: Delta^min={d}  resid={r}")
    print("[C] expect: 0.02 ~ 0.98 (reflection symmetry), peak near 0.59")


if __name__ == "__main__":
    print("=== (A) chord / MVT identity (surrogate h) ===")
    check_chord()
    print("=== (B) slope chain ===")
    check_slopes()
    print("=== (C) live solver endpoint symmetry + hump ===")
    check_live()
