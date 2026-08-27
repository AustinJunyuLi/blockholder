"""ANALYST B probe 5 -- one of ticket 34's four sweep-UNRESOLVED nodes.

kappa = 0.15, tau = 0.05, T = 5.  T(k) depends on k only through k2 on this
menu (probe 2A), so the whole fixed-point problem is one-dimensional: sweep k2
and look at where T_2(k2) - k2 changes sign relative to the discontinuity
hyperplanes (the n(s) cell edges).
"""
import sys, json
import numpy as np
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")

from numerical_v4.params import ParamsV4
from numerical_v4.menu import atoms, breakpoints, _sigmoid_inv, n_days
from numerical_v4.pooled import pooled_pass
from numerical_v4.solver import outer_map

SCR = ("/private/tmp/claude-501/-Users-austinli-Projects-blockholder-v4-theory/"
       "ab9c0696-e7f9-466e-8d38-08f559ee1613/scratchpad/")
p = ParamsV4().replace(kappa=0.15, tau=0.05, T=5)
K1 = 1.20

nj = {}
for m in range(1, p.H + 2):
    g = 1.0 - m / (p.n_scale * (p.H + 1))
    if 0.0 < g < 1.0:
        nj[m] = p.mu_v + p.sigma_s * _sigmoid_inv(g)
edges = sorted(nj.values())
print("  n(s) cell edges (discontinuity candidates):")
print("   " + "  ".join(f"{e:.6f}" for e in edges))

grid = sorted(set([round(x, 12) for x in np.linspace(1.30, 2.10, 33)]
                  + [e - 1e-7 for e in edges if 1.29 < e < 2.11]
                  + [e for e in edges if 1.29 < e < 2.11]
                  + [e + 1e-7 for e in edges if 1.29 < e < 2.11]))
rec = []
print(f"\n  {'k2':>16} {'T_1':>13} {'T_2':>13} {'T_2 - k2':>13}  edge?")
prev = None
for k2 in grid:
    res = pooled_pass(atoms((K1, k2), p), p, with_runup=True)
    T = outer_map((K1, k2), p, res)
    tag = ""
    for e in edges:
        if abs(k2 - e) <= 1.5e-7:
            tag = f"  <-- edge {e:.6f} ({k2-e:+.0e})"
    print(f"  {k2:16.9f} {T[0]:13.9f} {T[1]:13.9f} {T[1]-k2:13.3e}{tag}")
    rec.append(dict(k2=float(k2), T1=float(T[0]), T2=float(T[1]),
                    gap=float(T[1] - k2)))

g = np.array([r["gap"] for r in rec]); ks = np.array([r["k2"] for r in rec])
sgn = np.sign(g)
print("\n  sign changes of T_2(k2) - k2:")
for i in range(len(g) - 1):
    if sgn[i] * sgn[i + 1] < 0:
        onedge = any(abs(ks[i] - e) < 1e-6 or abs(ks[i + 1] - e) < 1e-6
                     for e in edges)
        print(f"    between k2={ks[i]:.9f} (gap {g[i]:+.3e}) and "
              f"k2={ks[i+1]:.9f} (gap {g[i+1]:+.3e})"
              f"{'   *** ACROSS AN EDGE ***' if onedge else ''}")
json.dump(rec, open(SCR + "a6_B_node15.json", "w"), indent=1)
print("wrote a6_B_node15.json")
