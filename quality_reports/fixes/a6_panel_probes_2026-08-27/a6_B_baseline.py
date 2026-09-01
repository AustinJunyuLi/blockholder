"""ANALYST B probe 3 -- the TRUE implemented baseline (tau frozen, smoke SMOKE 1).

Reproduces the frozen tau, verifies the fixed point, locates it among the
discontinuity hyperplanes, and sweeps k2 across the nearest ones.
"""
import sys, json
import numpy as np
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")

from numerical_v4.params import ParamsV4, EXIT, HOLD, VOICE
from numerical_v4.menu import (atoms, breakpoints, n_days, type_reference,
                               _sigmoid_inv)
from numerical_v4.pooled import pooled_pass, mark_stats
from numerical_v4.policy import plan_payoff, frozen_tau_grid
from numerical_v4.solver import solve_policy, outer_map

SCR = ("/private/tmp/claude-501/-Users-austinli-Projects-blockholder-v4-theory/"
       "ab9c0696-e7f9-466e-8d38-08f559ee1613/scratchpad/")
out = {}

p_seed = ParamsV4()
print("solving seed equilibrium (tau = 0.05) ...", flush=True)
pol_seed, r_seed = solve_policy(p_seed)
print(f"  seed k = {pol_seed.k}   |k-T(k)| = {r_seed.cutoff_scale:.3e}")
tau_frozen = frozen_tau_grid(pol_seed, p_seed, (0.5,))[0]
print(f"  tau frozen at {tau_frozen:.12f}")
p = p_seed.replace(tau=tau_frozen)

print("solving baseline equilibrium (frozen tau) ...", flush=True)
pol, r = solve_policy(p)
KS = tuple(float(x) for x in pol.k)
print(f"  BASELINE k* = ({KS[0]:.10f}, {KS[1]:.10f})   "
      f"|k-T(k)| = {r.cutoff_scale:.3e}  payoff={r.payoff_scale:.3e}")
print(f"  Hold region width = {KS[1]-KS[0]:.6f}  (collapsed iff 0)")
out["tau_frozen"] = float(tau_frozen)
out["kstar"] = list(KS)

# --- n(s) jump points (tau-independent) ------------------------------------
njump = {}
for m in range(1, p.H + 2):
    g = 1.0 - m / (p.n_scale * (p.H + 1))
    if 0.0 < g < 1.0:
        njump[m] = p.mu_v + p.sigma_s * _sigmoid_inv(g)

bps = breakpoints(KS, p)
print(f"\n  breakpoints at k* ({len(bps)}):")
print("   " + "  ".join(f"{b:.6f}" for b in bps))
print(f"\n  n(k2*) = {n_days(KS[1], p)}")
above = sorted(b for b in bps if b > KS[1] + 1e-9)
print(f"  nearest breakpoints above k2*: {[round(float(b),8) for b in above[:4]]}")
out["bps"] = [float(b) for b in bps]

al = atoms(KS, p)
W = np.zeros(p.n_theta)
for a in al:
    W[a.theta] += a.w
print("\n  type masses at k*:")
for t in range(p.n_theta):
    mark = "  <== ZERO (off path, floored)" if W[t] == 0.0 else ""
    print(f"    t={t:2d}  W={W[t]:.6e}{mark}")
out["W"] = W.tolist()
marginal = max(t for t in range(p.n_theta) if W[t] > 0)
print(f"  marginal (largest-n) on-path Voice type: t = {marginal}")
S_edge = njump[marginal - 1] if (marginal - 1) in njump else None
print(f"  top edge of its cell: s_bar = {S_edge}")
out["marginal_type"] = int(marginal)
out["S_edge"] = float(S_edge) if S_edge else None

# --- sweep k2 across each candidate hyperplane above k2* --------------------
cands = []
if S_edge is not None and S_edge > KS[1]:
    cands.append(("n-jump top edge of cell %d" % marginal, float(S_edge)))
for b in above[:3]:
    if all(abs(b - c[1]) > 1e-9 for c in cands):
        cands.append(("breakpoint", float(b)))

recs = []
for label, S in cands:
    print("\n" + "=" * 74)
    print(f"  sweep k2 across {label}  S = {S:.12f}   (k2* = {KS[1]:.10f})")
    print("=" * 74)
    print(f"  {'k2 - S':>12} {'W[marg]':>11} {'U_V(s0)':>14} {'U_H(s0)':>14} "
          f"{'T_1(k)':>13} {'T_2(k)':>13}")
    s0 = 0.5 * (KS[1] + S)
    for d in (1e-2, 1e-3, 1e-5, 1e-7, 1e-8, 0.0, -1e-5, -1e-2):
        k2v = S - d
        alx = atoms((KS[0], k2v), p)
        Wm = sum(a.w for a in alx if a.theta == marginal)
        res = pooled_pass(alx, p, with_runup=True)
        Uv = plan_payoff(VOICE, s0, res, p)
        Uh = plan_payoff(HOLD, s0, res, p)
        T = outer_map((KS[0], k2v), p, res)
        print(f"  {k2v-S:12.3e} {Wm:11.3e} {Uv:14.10f} {Uh:14.10f} "
              f"{T[0]:13.9f} {T[1]:13.9f}")
        recs.append(dict(label=label, S=S, delta=float(k2v - S), k2=float(k2v),
                         Wmarg=float(Wm), s0=float(s0), Uv=float(Uv),
                         Uh=float(Uh), T1=float(T[0]), T2=float(T[1])))
out["sweeps"] = recs
json.dump(out, open(SCR + "a6_B_baseline.json", "w"), indent=1)
print("\nwrote a6_B_baseline.json")
