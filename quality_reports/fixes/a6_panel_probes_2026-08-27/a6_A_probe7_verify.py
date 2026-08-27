"""ANALYST A probe 7 — two verifications.  Scratch only.

(A) At k2 = edge(6) + 1e-9 the gap U_VOICE - U_HOLD has 3 sign changes.  If the
    middle excursion is real (>> solver noise), argmax alternates V,H,V, no
    weakly increasing selection exists, and h.3/A3's second clause FAILS -- a
    definedness failure upstream of A6's continuity.

(B) Re-run the death-surface bracket at +/-1e-6 instead of +/-1e-9, well clear
    of menu.breakpoints' 1e-9 near-duplicate merge tolerance, to close the
    "you resolved a sliver that the atom builder had already merged away" attack.
"""
import sys
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")

import numpy as np
from scipy.optimize import brentq
from numerical_v4.params import ParamsV4, EXIT, HOLD, VOICE
from numerical_v4.menu import atoms, type_reference, _sigmoid_inv
from numerical_v4.pooled import pooled_pass, _alive_weights
from numerical_v4.policy import plan_payoff

base = ParamsV4.baseline()
p = base.replace(kappa=0.5, tau=0.09076405861553302, T=5)
ref = type_reference(p)
K1 = 1.2405757282617416

E = {}
for m in range(1, p.H + 2):
    g = 1.0 - m / (p.n_scale * (p.H + 1))
    if 0.0 < g < 1.0:
        s = p.mu_v + p.sigma_s * _sigmoid_inv(g)
        if p.s_lo < s < p.s_hi:
            E[m] = s

# ---------------------------------------------------------------- (A) --------
print("(A) sign structure of U_VOICE - U_HOLD at k2 = edge(6) + 1e-9 = %.10f"
      % (E[6] + 1e-9))
NG = 6001
GRID = np.linspace(p.s_lo, p.s_hi, NG)
for tag, k2 in (("below  edge(6)-1e-9", E[6] - 1e-9),
                ("above  edge(6)+1e-9", E[6] + 1e-9)):
    res = pooled_pass(atoms((K1, k2), p), p, with_runup=True)
    g = np.array([plan_payoff(VOICE, float(s), res, p)
                  - plan_payoff(HOLD, float(s), res, p) for s in GRID])
    sc = np.nonzero(np.sign(g[:-1]) * np.sign(g[1:]) < 0)[0]
    roots = [float(brentq(lambda s: plan_payoff(VOICE, float(s), res, p)
                          - plan_payoff(HOLD, float(s), res, p),
                          GRID[i], GRID[i + 1], xtol=1e-13)) for i in sc]
    print("  %s : %d sign changes at s = %s"
          % (tag, len(sc), ["%.7f" % r for r in roots]))
    # excursion magnitudes between consecutive roots
    bnds = [p.s_lo] + roots + [p.s_hi]
    for a, b in zip(bnds[:-1], bnds[1:]):
        seg = g[(GRID > a) & (GRID < b)]
        if seg.size:
            k = int(np.argmax(np.abs(seg)))
            print("      s in (%9.5f,%9.5f): sign %+d, max|gap| = %.4e"
                  % (a, b, int(np.sign(seg[k])), abs(seg[k])))
    print("      (solver payoff tolerance TOL_PAYOFF = 1e-9)")

# ---------------------------------------------------------------- (B) --------
print("\n(B) robustness: same death surface at +/-1e-6 (merge tol is 1e-9)")
def side(k2, t):
    al = atoms((K1, k2), p)
    W, Wm, WVm, WAm = _alive_weights(al, 0, p.n_theta, ref)
    res = pooled_pass(al, p, with_runup=True)
    GG = np.linspace(p.s_lo, p.s_hi, 4001)
    def gHV(s): return plan_payoff(VOICE, float(s), res, p) - plan_payoff(HOLD, float(s), res, p)
    v = np.array([gHV(s) for s in GG])
    T2 = p.s_hi
    for i in range(len(GG) - 1):
        if v[i] < 0.0 <= v[i + 1]:
            T2 = float(brentq(gHV, GG[i], GG[i + 1], xtol=1e-13)); break
    vh = WVm[t] / Wm[t] if Wm[t] > 0 else float("nan")
    return W[t], vh, T2, res

for m_die, eps in ((9, 1e-6), (9, 1e-9), (8, 1e-6), (7, 1e-6)):
    top = E[m_die - 1]
    wA, vA, TA, rA = side(top - eps, m_die)
    wB, vB, TB, rB = side(top + eps, m_die)
    print("  type %2d, eps=%.0e : W below %.4e above %.4e | vhat %.8f -> %.8f "
          "(JUMP %+.4e) | card T2 %.8f -> %.8f (|JUMP| %.4e)"
          % (m_die, eps, wA, wB, vA, vB, vB - vA, TA, TB, abs(TB - TA)))
