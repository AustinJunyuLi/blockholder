"""ANALYST B probe 2 -- the decisive sweep.

(A) k1-invariance across the Hold-collapse face (k2 fixed).
(B) k2 swept across the top edge of the marginal on-path type's cell:
    price at a diagnostic history, U_VOICE(s), and T(k).
"""
import sys, json, math, time
import numpy as np
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")

from numerical_v4.params import ParamsV4, EXIT, HOLD, VOICE
from numerical_v4.menu import (atoms, breakpoints, n_days, type_reference,
                               theta_index, _sigmoid_inv)
from numerical_v4.pooled import pooled_pass, mark_stats
from numerical_v4.policy import plan_payoff
from numerical_v4.solver import outer_map

SCR = ("/private/tmp/claude-501/-Users-austinli-Projects-blockholder-v4-theory/"
       "ab9c0696-e7f9-466e-8d38-08f559ee1613/scratchpad/")
p = ParamsV4()
KSTAR = (1.2405757283, 1.5310222869)
out = {}

# exact n(s) jump points -----------------------------------------------------
njump = {}
for m in range(1, p.H + 2):
    g = 1.0 - m / (p.n_scale * (p.H + 1))
    if 0.0 < g < 1.0:
        njump[m] = p.mu_v + p.sigma_s * _sigmoid_inv(g)
print("== exact n(s) jump points (top edge of cell m+1 == njump[m]) ==")
for m, s in sorted(njump.items()):
    print(f"   m={m:2d}  s={s:.12f}   n(s-)={n_days(s-1e-9,p)}  n(s+)={n_days(s+1e-9,p)}")
S9 = njump[8]                       # top edge of cell n=9
print(f"\n  top edge of cell n=9:  s9bar = {S9:.12f}")
print(f"  n just below/above: {n_days(S9-1e-9,p)} / {n_days(S9+1e-9,p)}")
out["njump"] = {int(m): float(s) for m, s in njump.items()}
out["S9"] = float(S9)

# --------------------------------------------------------------------------
# (A) k1-invariance: vary k1 at fixed k2, including the Hold-collapse face
# --------------------------------------------------------------------------
print("\n" + "=" * 74)
print("(A) k1-INVARIANCE (k2 fixed at k2*); Hold collapses at k1 = k2")
print("=" * 74)
k2 = KSTAR[1]
k1_list = [0.5, 1.0, KSTAR[0], 1.40, 1.52, k2]      # last = Hold collapsed
base = None
recA = []
for k1 in k1_list:
    res = pooled_pass(atoms((k1, k2), p), p, with_runup=True)
    sig = np.concatenate([res.EP[d] for d in res.dates] + [res.Ep_bid, res.EpP])
    if base is None:
        base = sig
        dmax = 0.0
    else:
        dmax = float(np.max(np.abs(sig - base)))
    Uv = plan_payoff(VOICE, 1.60, res, p)
    Uh = plan_payoff(HOLD, 1.60, res, p)
    T = outer_map((k1, k2), p, res)
    print(f"  k1={k1:.10f}  Hold width={k2-k1:.3e}  "
          f"max|EP - EP(k1=0.5)|={dmax:.3e}  U_V(1.6)={Uv:.12f}  "
          f"T=({T[0]:.8f},{T[1]:.8f})")
    recA.append(dict(k1=float(k1), dmax=dmax, Uv=float(Uv), Uh=float(Uh),
                     T=[float(T[0]), float(T[1])]))
out["A_k1_invariance"] = recA

# --------------------------------------------------------------------------
# (B) k2 swept across s9bar
# --------------------------------------------------------------------------
print("\n" + "=" * 74)
print("(B) k2 SWEPT ACROSS s9bar = top edge of the marginal type's cell")
print("=" * 74)

# diagnostic history: a date-7 prefix carrying an X=2 mark -> infeasible for
# type 0, feasible only for the tall-mark types {9,10,11} (identical marks on
# d<=7).  digit x = X+1, index = sum x_d * 4^(7-d).
D_DIAG = 7
Xpath = [1, 1, 2, 1, 0, 1, 1, 0]          # X in {-1,0,1,2}; X_2 = 2
hidx = 0
for X in Xpath:
    hidx = 4 * hidx + (X + 1)
ms = mark_stats(p.H)
print(f"  diagnostic history X_0..X_7 = {Xpath}  index={hidx}")
print(f"  feasible types: {list(np.where(ms.feas[D_DIAG][hidx])[0])}")

k1 = KSTAR[0]
deltas = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-8, 1e-10, 1e-12, 1e-13,
          3e-14, 1e-14, 0.0, -1e-6, -1e-2]
recB = []
print(f"\n  {'k2 - s9bar':>12} {'W[9]':>11} {'vhat(h)':>11} {'P_7(h)':>11} "
      f"{'U_V(1.55)':>13} {'U_H(1.55)':>13} {'T_2(k)':>13}")
for d in deltas:
    k2v = S9 - d if d != 0.0 else S9
    al = atoms((k1, k2v), p)
    W9 = sum(a.w for a in al if a.theta == 9)
    res = pooled_pass(al, p, with_runup=True)
    P7 = float(res.price[D_DIAG][hidx])
    pi7 = float(res.pi[D_DIAG][hidx])
    s_ev = 1.55
    Uv = plan_payoff(VOICE, s_ev, res, p)
    Uh = plan_payoff(HOLD, s_ev, res, p)
    T = outer_map((k1, k2v), p, res)
    print(f"  {k2v-S9:12.3e} {W9:11.3e} {pi7:11.6f} {P7:11.6f} "
          f"{Uv:13.9f} {Uh:13.9f} {T[1]:13.9f}")
    recB.append(dict(delta=float(k2v - S9), k2=float(k2v), W9=float(W9),
                     pi7=pi7, P7=P7, Uv=float(Uv), Uh=float(Uh),
                     T1=float(T[0]), T2=float(T[1])))
out["B_k2_sweep"] = recB
out["diag"] = dict(Xpath=Xpath, hidx=int(hidx), date=D_DIAG,
                   feas=[int(t) for t in np.where(ms.feas[D_DIAG][hidx])[0]])

json.dump(out, open(SCR + "a6_B_sweep.json", "w"), indent=1)
print("\nwrote a6_B_sweep.json")
