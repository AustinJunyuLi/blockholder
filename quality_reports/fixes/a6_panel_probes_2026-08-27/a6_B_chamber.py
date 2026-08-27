"""ANALYST B probe 4 -- the chamber containing k2* = 1.5310222869.

Chamber = (1.517932397378, 1.583333333333): consecutive breakpoints, no
interior breakpoint.  Question: is T continuous on it, and does some compact
sub-box map into itself (i.e. is A6 satisfiable with a chamber-restricted Theta)?
"""
import sys, json
import numpy as np
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")

from numerical_v4.params import ParamsV4, VOICE, HOLD
from numerical_v4.menu import atoms
from numerical_v4.pooled import pooled_pass
from numerical_v4.solver import outer_map

SCR = ("/private/tmp/claude-501/-Users-austinli-Projects-blockholder-v4-theory/"
       "ab9c0696-e7f9-466e-8d38-08f559ee1613/scratchpad/")
p = ParamsV4().replace(tau=0.090764058616)
K1 = 1.2405757283
LO, HI = 1.517932397378, 1.583333333333       # chamber edges

grid = ([LO, LO + 1e-8, LO + 1e-6, LO + 1e-4]
        + list(np.linspace(LO + 1e-3, HI - 1e-3, 21))
        + [HI - 1e-4, HI - 1e-6, HI - 1e-8, HI])
rec = []
print(f"  chamber ({LO:.12f}, {HI:.12f})   k2* = 1.5310222869")
print(f"  {'k2':>16} {'T_1':>14} {'T_2':>14} {'T_2 - k2':>13}")
for k2 in grid:
    k2 = float(k2)
    res = pooled_pass(atoms((K1, k2), p), p, with_runup=True)
    T = outer_map((K1, k2), p, res)
    print(f"  {k2:16.12f} {T[0]:14.9f} {T[1]:14.9f} {T[1]-k2:13.3e}")
    rec.append(dict(k2=k2, T1=float(T[0]), T2=float(T[1])))

T2 = np.array([r["T2"] for r in rec])
T1 = np.array([r["T1"] for r in rec])
ks = np.array([r["k2"] for r in rec])
inner = (ks > LO + 5e-9) & (ks < HI - 5e-9)
print(f"\n  interior of chamber: T_2 range [{T2[inner].min():.9f}, "
      f"{T2[inner].max():.9f}]   T_1 range [{T1[inner].min():.9f}, "
      f"{T1[inner].max():.9f}]")
print(f"  max |dT_2| between adjacent interior grid points: "
      f"{np.max(np.abs(np.diff(T2[inner]))):.3e}")
print(f"  edge jumps:  at LO  T_2({LO:.6f})={T2[0]:.9f} vs "
      f"T_2(LO+1e-8)={T2[1]:.9f}  -> {T2[1]-T2[0]:+.3e}")
print(f"               at HI  T_2(HI-1e-8)={T2[-2]:.9f} vs "
      f"T_2(HI)={T2[-1]:.9f}  -> {T2[-1]-T2[-2]:+.3e}")
sub_ok = (T2[inner].min() > LO) and (T2[inner].max() < HI)
print(f"\n  T_2(interior) contained strictly inside the chamber? {sub_ok}")
json.dump(rec, open(SCR + "a6_B_chamber.json", "w"), indent=1)
print("wrote a6_B_chamber.json")
