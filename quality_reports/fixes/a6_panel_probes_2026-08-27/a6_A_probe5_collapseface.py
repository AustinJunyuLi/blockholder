"""ANALYST A probe 5 — (a) is the PLAN-collapse face (k1 = k2, Hold collapsed)
belief-inert on this menu?  (b) how close does each solved equilibrium sit to a
type-death discontinuity surface?   Scratch only.
"""
import sys, math
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")

import numpy as np
from scipy.optimize import brentq
from numerical_v4.params import ParamsV4, EXIT, HOLD, VOICE
from numerical_v4.menu import atoms, type_reference, _sigmoid_inv, theta_index
from numerical_v4.pooled import _alive_weights, pooled_pass
from numerical_v4.policy import plan_payoff
from numerical_v4.solver import outer_map

base = ParamsV4.baseline()

def edges_of(p):
    out = {}
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            s = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo < s < p.s_hi:
                out[m] = s
    return out

# ---------------------------------------------------------------- (a) --------
print("(a) PLAN-COLLAPSE FACE at the node whose solved k has k1 == k2 exactly")
p = base.replace(kappa=0.5, tau=0.05, T=1)
KC = 1.35358624390523
ref = type_reference(p)
NG = 2001
GRID = np.linspace(p.s_lo, p.s_hi, NG)

def snap(k):
    al = atoms(k, p)
    W, Wm, WVm, WAm = _alive_weights(al, 0, p.n_theta, ref)
    res = pooled_pass(al, p, with_runup=True)
    def gEH(s): return plan_payoff(EXIT, float(s), res, p) - plan_payoff(HOLD, float(s), res, p)
    def gHV(s): return plan_payoff(VOICE, float(s), res, p) - plan_payoff(HOLD, float(s), res, p)
    hold_mass = sum(a.w for a in al if a.plan == HOLD)
    vals = np.array([gHV(s) for s in GRID])
    T2 = p.s_hi
    for i in range(NG - 1):
        if vals[i] < 0.0 <= vals[i + 1]:
            T2 = float(brentq(gHV, GRID[i], GRID[i + 1], xtol=1e-13)); break
    return dict(W=W.copy(), hold_mass=hold_mass, T=outer_map(k, p, res),
                cardT2=T2,
                EP0=res.EP[0].copy(), Epb=res.Ep_bid.copy())

for lab, k in (("ON the face  k1=k2", (KC, KC)),
               ("k1 = k2 - 1e-9  ", (KC - 1e-9, KC)),
               ("k1 = k2 - 1e-4  ", (KC - 1e-4, KC)),
               ("k1 = k2 - 1e-2  ", (KC - 1e-2, KC))):
    r = snap(k)
    live = [t for t in range(p.n_theta) if r["W"][t] > 0]
    print("  %-18s Hold mass %.4e | live types %s | E[P0|th=0] %.10f | "
          "impl T=(%.8f,%.8f) | card T2 %.8f"
          % (lab, r["hold_mass"], live, r["EP0"][0], r["T"][0], r["T"][1],
             r["cardT2"]))
print("  => if E[P0|theta=0] and T are the same on and off the face, the Hold")
print("     collapse is belief-INERT: Exit and Hold share the theta=0 mark path.")

# ---------------------------------------------------------------- (b) --------
print("\n(b) distance from each solved equilibrium k2* to the nearest")
print("    type-death surface (an n(s) cell edge), in units of sigma_s")
import json
d = json.load(open("/Users/austinli/Projects/blockholder_v4_theory/"
                   "quality_reports/fixes/t2_p1_check.json"))
rows = [c for c in d["checks"] if c["name"] == "p1_multistart_existence_sweep"][0]["rows"]
E = edges_of(base)
ev = sorted(E.values())
print("  %-5s %-9s %-3s %-12s %-12s %-11s %-9s %s"
      % ("kap", "tau", "T", "k2*", "nearest edge", "dist", "dist/sig", "conv"))
for r in rows:
    k2 = r["k"][1]
    near = min(ev, key=lambda s: abs(s - k2))
    dist = abs(near - k2)
    print("  %-5.2f %-9.5f %-3d %-12.7f %-12.7f %-11.3e %-9.4f %s"
          % (r["kappa"], r["tau"], r["T"], k2, near, dist,
             dist / base.sigma_s, r["converged_payoff"]))
