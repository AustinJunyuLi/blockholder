"""ANALYST B probe 1 -- structure: breakpoints, type masses, k1-invariance.

Read-only on the repo; writes nothing outside the scratchpad.
"""
import sys, json
import numpy as np
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")

from numerical_v4.params import ParamsV4, EXIT, HOLD, VOICE
from numerical_v4.menu import atoms, breakpoints, n_days, type_reference, theta_index
from numerical_v4.pooled import pooled_pass, mark_stats

p = ParamsV4()
KSTAR = (1.2405757283, 1.5310222869)   # smoke_output.txt SMOKE 1 baseline

print("== params ==")
print(f"  H={p.H} T={p.T} kappa={p.kappa} n_scale={p.n_scale} tau={p.tau}")
print(f"  s_lo={p.s_lo:.6f} s_hi={p.s_hi:.6f} mu_v={p.mu_v} sigma_s={p.sigma_s:.6f}"
      f" beta={p.beta:.6f}")
print(f"  n_theta={p.n_theta}")

# --- n(s) jump points -------------------------------------------------------
print("\n== n(s) cells over [s_lo, s_hi] ==")
ss = np.linspace(p.s_lo, p.s_hi, 200001)
nn = np.array([n_days(float(s), p) for s in ss])
cells = {}
for n in sorted(set(nn.tolist())):
    idx = np.where(nn == n)[0]
    cells[int(n)] = (float(ss[idx[0]]), float(ss[idx[-1]]))
    print(f"  n={n:3d}  cell approx [{ss[idx[0]]:.6f}, {ss[idx[-1]]:.6f}]")

print(f"\n  n(k2*)={n_days(KSTAR[1], p)}   n(k1*)={n_days(KSTAR[0], p)}")

# --- breakpoints at k* ------------------------------------------------------
bps = breakpoints(KSTAR, p)
print(f"\n== breakpoints at k* ({len(bps)}) ==")
print("  " + "  ".join(f"{b:.6f}" for b in bps))

# --- atoms and type masses at k* -------------------------------------------
al = atoms(KSTAR, p)
print(f"\n== atoms at k* ({len(al)}) ==")
W = np.zeros(p.n_theta)
for a in al:
    W[a.theta] += a.w
    print(f"  [{a.lo:9.6f},{a.hi:9.6f})  plan={a.plan} th={a.theta:2d} "
          f"D={a.D} c={a.c} f={a.f}  w={a.w:.6e}  Ev={a.Ev:.6f}")
print("\n  type masses W[t] at k*:")
for t in range(p.n_theta):
    print(f"    t={t:2d}  W={W[t]:.6e}")
n_pop = int(np.count_nonzero(W > 0))
print(f"  populated types: {n_pop} of {p.n_theta}")

ref = type_reference(p)
print("\n  type_reference Ev[t] (the plan-uniform / off-path value):")
for t in range(p.n_theta):
    print(f"    t={t:2d}  refEv={ref.Ev[t]:.6f}  a={ref.a[t]}  D={ref.D[t]} f={ref.f[t]}")

json.dump({"cells": cells, "bps": [float(b) for b in bps],
           "W": W.tolist(), "refEv": ref.Ev.tolist()},
          open("/private/tmp/claude-501/-Users-austinli-Projects-blockholder-v4-theory/"
               "ab9c0696-e7f9-466e-8d38-08f559ee1613/scratchpad/a6_B_struct.json", "w"),
          indent=1)
print("\nwrote a6_B_struct.json")
