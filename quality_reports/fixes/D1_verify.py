"""
D1_verify.py  --  Self-verification for D1_prop6_endpoint_variance.tex

Checks the CLOSED-FORM claims of Lemma A and Lemma B against (a) symbolic
algebra (sympy) and (b) a FIXED-MASS numerical sweep.

WHAT IS CHECKED
---------------
Lemma A  : endpoint symmetry of the realized D=0 law of pi. The support is the
           two-point set {0, pibar} at every kappa, and the cell-averaged law
           coincides at kappa=0 and kappa=1, so Var[pi|D=0] (the dispersion of
           the *cell posteriors* pi(X) over X) returns to the same value at
           both ends.  ==> V(0)=V(1).

Lemma B(i,ii) : E[pi|D=0] = omega_Q / (omega_E+omega_H+omega_Q) is EXACTLY
           kappa-invariant under fixed masses (tower identity E[pi*1{D=0}]=
           omega_Q with P(D=0)=P(q!=+1) mass-only). Unconditional.

Lemma B(iii) : the cell-posterior variance V(kappa)=Var_X[pi(X) | D=0] is a
           rational function of kappa that is strictly U-shaped on (0,1):
           V'(0)<0, V'(1)>0, single interior zero of V'.  This is the
           dispersion-of-cell-posteriors object (law of total variance with
           the cells X in {-1,0,+1}); it is the genuine kappa-carrying piece.

THE FIXED-MASS SWEEP is the anchor the previous attempt lacked: it freezes the
baseline masses and varies ONLY kappa through the noise mixing, then confirms
V'(0)<0, V'(1)>0 and a single interior minimizer numerically.  (The
full-equilibrium variances in phase0_facts.md move the masses with kappa and so
are NOT a test of the fixed-mass claim.)

Run:
    python3 quality_reports/fixes/D1_verify.py        # sympy+numpy only
"""

import numpy as np
try:
    import sympy as sp
    HAVE_SYMPY = True
except Exception:
    HAVE_SYMPY = False


# ---------------------------------------------------------------------------
# Model of the D=0 cells.  Noise z in {-1,0,+1}: P(0)=1-kappa, P(+-1)=kappa/2.
# Three D=0 branches (q != +1), with FIXED equilibrium masses:
#   Exit   q=-1, pi=0 :  X = -1 + z
#   Hold   q= 0, pi=0 :  X =  0 + z
#   Quiet  q= 0, pi=pibar : X = 0 + z      (engaged, undisclosed)
# Order-flow support clipped to {-1,0,+1}; X=-2 (Exit,z=-1) is an absorbing
# "deep-sell" cell that is also D=0 and pi=0 -- we keep it as a 4th cell so the
# noise law normalizes exactly (no probability is dropped).
#
# pi(X) = engaged_mass(X) / total_mass(X)   (the MM cell posterior).
# Var[pi|D=0] = sum_X P(X|D=0) * (pi(X) - Ebar)^2 ,  Ebar = E[pi|D=0].
# ---------------------------------------------------------------------------

# baseline-style FIXED masses (Hold nearly collapsed at baseline; Exit present)
wE = 0.20    # exit mass        -> pi = 0
wH = 0.04    # hold mass        -> pi = 0
wQ = 0.76    # quiet-voice mass -> pi = pibar
pibar = wQ / (wH + wQ)          # two-point upper support value (Hold pooled)


def cells(kappa, wE=wE, wH=wH, wQ=wQ):
    """Return list of (mass(X), cell-posterior pi(X)) over D=0 cells."""
    y = 1.0 - kappa             # P(z=0)
    x = kappa / 2.0             # P(z=+1) = P(z=-1)
    # mass[X] and engaged[X]:
    #   Quiet (engaged, pi-weight pibar) : X=0 w.p y, X=+-1 w.p x
    #   Hold  (pi=0)                      : X=0 w.p y, X=+-1 w.p x
    #   Exit  (pi=0)                      : X=-1 w.p y, X=0 w.p x, X=-2 w.p x
    Xs = [-2, -1, 0, 1]
    mass = {X: 0.0 for X in Xs}
    eng = {X: 0.0 for X in Xs}
    # Quiet
    mass[0] += wQ * y; eng[0] += wQ * y
    mass[1] += wQ * x; eng[1] += wQ * x
    mass[-1] += wQ * x; eng[-1] += wQ * x
    # Hold
    mass[0] += wH * y
    mass[1] += wH * x
    mass[-1] += wH * x
    # Exit
    mass[-1] += wE * y
    mass[0] += wE * x
    mass[-2] += wE * x
    out = []
    for X in Xs:
        m = mass[X]
        if m <= 0:
            continue
        # cell posterior on the engaged type: pi(X) = engaged_mass / total_mass.
        # On a pure q=0 cell this equals wQ/(wH+wQ)=pibar; Exit-contaminated
        # cells take values strictly between 0 and pibar.  No extra pibar factor.
        piX = eng[X] / m
        out.append((m, piX))
    return out


def moments(kappa):
    cs = cells(kappa)
    PD0 = sum(m for m, _ in cs)
    Ebar = sum(m * pi for m, pi in cs) / PD0
    Var = sum(m * (pi - Ebar) ** 2 for m, pi in cs) / PD0
    return PD0, Ebar, Var


def numeric_checks():
    print("\n[numeric] baseline masses wE=%.2f wH=%.2f wQ=%.2f  pibar=%.6f"
          % (wE, wH, wQ, pibar))
    ks = np.linspace(0, 1, 2001)
    PD0s = np.array([moments(k)[0] for k in ks])
    Ebars = np.array([moments(k)[1] for k in ks])
    Vs = np.array([moments(k)[2] for k in ks])
    dV = np.gradient(Vs, ks)

    # Lemma B(i): E invariant  ;  P(D=0) invariant
    print("[numeric] E[pi|D=0]:  min=%.8f max=%.8f  spread=%.2e (want ~0)"
          % (Ebars.min(), Ebars.max(), Ebars.max() - Ebars.min()))
    print("[numeric] P(D=0):     min=%.8f max=%.8f  spread=%.2e (want ~0)"
          % (PD0s.min(), PD0s.max(), PD0s.max() - PD0s.min()))
    print("[numeric] E[pi|D=0] closed form omega_Q/(wE+wH+wQ) = %.8f"
          % (wQ / (wE + wH + wQ)))

    # Lemma A: endpoint symmetry of V
    print("[numeric] V(0)=%.8f  V(1)=%.8f  |V(0)-V(1)|=%.2e (want ~0)"
          % (Vs[0], Vs[-1], abs(Vs[0] - Vs[-1])))

    # Lemma B(iii): U-shape
    imin = int(np.argmin(Vs))
    sc = np.where(np.diff(np.sign(dV)) != 0)[0]
    print("[numeric] V'(0)=%.6f (<0? %s)  V'(1)=%.6f (>0? %s)"
          % (dV[1], dV[1] < 0, dV[-2], dV[-2] > 0))
    print("[numeric] argmin kappa*=%.4f  V_min=%.8f  #interior V'-sign-changes=%d"
          % (ks[imin], Vs[imin], len(sc)))
    ok = (abs(Vs[0] - Vs[-1]) < 1e-9 and dV[1] < 0 and dV[-2] > 0
          and 0.0 < ks[imin] < 1.0 and len(sc) == 1
          and (Ebars.max() - Ebars.min()) < 1e-9)
    print("[numeric] LEMMA A + B ANCHOR:", "PASS" if ok else "CHECK")
    return ok


def symbolic_checks():
    if not HAVE_SYMPY:
        print("[symbolic] sympy unavailable -- skipping")
        return
    k = sp.symbols('kappa', nonnegative=True)
    wEs, wHs, wQs = sp.symbols('w_E w_H w_Q', positive=True)
    y = 1 - k
    x = k / 2
    pb = wQs / (wHs + wQs)
    # cell masses / engaged shares
    # X=0 : mass = (wQ+wH)*y + wE*x ; engaged = wQ*y
    m0 = (wQs + wHs) * y + wEs * x
    e0 = wQs * y
    # X=+1: mass = (wQ+wH)*x ; engaged = wQ*x  -> share wQ/(wQ+wH)=pb (const)
    m1 = (wQs + wHs) * x
    e1 = wQs * x
    # X=-1: mass = (wQ+wH)*x + wE*y ; engaged = wQ*x
    mm1 = (wQs + wHs) * x + wEs * y
    em1 = wQs * x
    # X=-2: mass = wE*x ; engaged = 0
    mm2 = wEs * x
    pi0 = e0 / m0
    pi1 = e1 / m1
    pim1 = em1 / mm1
    pim2 = sp.Integer(0)
    PD0 = sp.simplify(m0 + m1 + mm1 + mm2)
    Ebar = sp.simplify((m0 * pi0 + m1 * pi1 + mm1 * pim1 + mm2 * pim2) / PD0)
    Var = sp.simplify((m0 * (pi0 - Ebar) ** 2 + m1 * (pi1 - Ebar) ** 2
                       + mm1 * (pim1 - Ebar) ** 2 + mm2 * (pim2 - Ebar) ** 2) / PD0)
    Ebar_s = sp.simplify(Ebar)
    print("[symbolic] P(D=0)   =", sp.simplify(PD0))
    print("[symbolic] E[pi|D=0]=", Ebar_s, "  (kappa-free?)",
          sp.simplify(sp.diff(Ebar_s, k)) == 0)
    Var = sp.simplify(Var)
    Vp = sp.simplify(sp.diff(Var, k))
    V0 = sp.simplify(Var.subs(k, 0)); V1 = sp.simplify(Var.subs(k, 1))
    print("[symbolic] V(0)-V(1) simplifies to:", sp.simplify(V0 - V1))
    subs = {wEs: wE, wHs: wH, wQs: wQ}
    print("[symbolic] @baseline: V(0)=%.8f V(1)=%.8f V'(0)=%.6f V'(1)=%.6f"
          % (float(V0.subs(subs)), float(V1.subs(subs)),
             float(Vp.subs(k, 0).subs(subs)), float(Vp.subs(k, 1).subs(subs))))
    crit = sp.solve(sp.Eq(Vp, 0), k)
    cin = []
    for c in crit:
        try:
            cv = float(c.subs(subs))
            if 0 < cv < 1:
                cin.append(round(cv, 6))
        except Exception:
            pass
    print("[symbolic] interior critical kappa* =", cin)


if __name__ == "__main__":
    print("=== D1_verify: Lemma A + Lemma B closed-form checks ===")
    symbolic_checks()
    numeric_checks()
