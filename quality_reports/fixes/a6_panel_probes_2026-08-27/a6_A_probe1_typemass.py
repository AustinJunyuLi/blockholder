"""ANALYST A probe 1 — type-mass census and floor firing at the implemented nodes.

Scratch only. Writes nothing outside the scratchpad.

Question: at the implemented equilibria, does any mark-path type theta carry zero
equilibrium mass (so that numerical_v4.pooled._alive_weights fires the
OFF_PATH_EPS floor and prices theta-exclusive histories off the k-free
type_reference belief)?  And does the Hold region collapse?
"""
import sys
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")

import numpy as np
from numerical_v4.params import ParamsV4, EXIT, HOLD, VOICE
from numerical_v4.menu import atoms, type_reference, n_days
from numerical_v4.pooled import _alive_weights, OFF_PATH_EPS

NODES = [
    # (kappa, tau, T, k1, k2, label)
    (0.5, 0.05, 1, 1.35358624390523, 1.35358624390523, "COLLAPSED Hold"),
    (0.5, 0.075, 1, 1.3329053753496902, 1.3856452728203859, "near-collapse"),
    (0.5, 0.09076405861553302, 5, 1.2405757282617416, 1.5310222869296415, "BASELINE"),
    (0.15, 0.05, 5, 1.0074676693103841, 1.5613050961812023, "unresolved node"),
    (0.85, 0.075, 1, 1.0888619, 1.5387850, "unresolved node"),
]

base = ParamsV4.baseline()
ref = type_reference(base)
print("s_lo=%.5f s_hi=%.5f sigma_s=%.5f beta=%.5f mu_v=%.3f"
      % (base.s_lo, base.s_hi, base.sigma_s, base.beta, base.mu_v))
print("reference E[v | n(s)=t] (k-FREE, menu.type_reference):")
print("  t : ", " ".join("%2d" % t for t in range(base.n_theta)))
print("  Ev: ", " ".join("%.3f" % v for v in ref.Ev))
print()

for (kap, tau, T, k1, k2, label) in NODES:
    p = base.replace(kappa=kap, tau=tau, T=T)
    k = (k1, k2)
    al = atoms(k, p)
    W, Wm, WVm, WAm = _alive_weights(al, p.H, p.n_theta, ref)
    dead = [t for t in range(p.n_theta) if W[t] <= 0.0 and Wm[t] > 0.0]
    hold_atoms = [a for a in al if a.plan == HOLD]
    hold_mass = sum(a.w for a in hold_atoms)
    print("== kappa=%.2f tau=%.5f T=%d  k=(%.7f, %.7f)  [%s]"
          % (kap, tau, T, k1, k2, label))
    print("   k2-k1 = %.3e   Hold prior mass = %.6e   n_atoms=%d"
          % (k2 - k1, hold_mass, len(al)))
    print("   type mass W[t] (date H, alive):")
    print("     ", " ".join("%d:%.3e" % (t, W[t]) for t in range(p.n_theta)))
    print("   DEAD types (floor fires, priced off k-free reference): %s" % dead)
    for t in dead:
        # what would the on-path belief have converged to as this type died?
        print("        t=%d  reference Ev=%.6f" % (t, ref.Ev[t]))
    print()
