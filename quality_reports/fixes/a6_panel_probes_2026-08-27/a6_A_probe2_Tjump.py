"""ANALYST A probe 2 — is the implemented outer map T(k) discontinuous where a
mark-path type's equilibrium mass crosses zero?

Scratch only.

Mechanism under test (the P1 re-derivation's N11, in its type-channel form):
a pooled history producible only by mark-type t is ON path while W[t] > 0 (its
belief is the Bayes posterior, which concentrates as W[t] -> 0) and OFF path at
W[t] = 0 (its belief snaps to the k-FREE `type_reference` value).  The two
disagree, so the price at that history jumps, and it enters U_VOICE(s;k) with
full noise weight through res.EP[d][t] / res.Ep_bid[t] / res.EpP[t].
"""
import sys, math, time
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")

import numpy as np
from numerical_v4.params import ParamsV4, EXIT, HOLD, VOICE
from numerical_v4.menu import atoms, type_reference, n_days, _sigmoid_inv
from numerical_v4.pooled import _alive_weights, pooled_pass
from numerical_v4.policy import plan_payoff
from numerical_v4.solver import outer_map

base = ParamsV4.baseline()
p = base.replace(kappa=0.5, tau=0.09076405861553302, T=5)   # BASELINE node
ref = type_reference(p)

# --- the n(s) cell edges: n(s) = ceil(n_scale*(H+1)*(1-g(x))) ---------------
print("n(s) cell edges (s at which n(s) steps):")
edges = {}
for m in range(1, p.H + 2):
    g = 1.0 - m / (p.n_scale * (p.H + 1))
    if 0.0 < g < 1.0:
        s = p.mu_v + p.sigma_s * _sigmoid_inv(g)
        if p.s_lo < s < p.s_hi:
            edges[m] = s
            print("   m=%2d  s=%.8f   n(s-)=%d n(s+)=%d"
                  % (m, s, n_days(s - 1e-9, p), n_days(s + 1e-9, p)))
print()

# Pick the edge nearest the baseline k2 = 1.5310 so the scan stays in a region
# where the equilibrium actually lives.
K2_STAR = 1.5310222869296415
K1 = 1.2405757282617416
cand = sorted(edges.items(), key=lambda kv: abs(kv[1] - K2_STAR))
print("edges nearest baseline k2=%.6f :" % K2_STAR,
      [(m, round(s, 6)) for m, s in cand[:4]])
m_edge, s_edge = cand[0]
print("scanning k2 across edge m=%d at s=%.10f\n" % (m_edge, s_edge))

def census(k):
    al = atoms(k, p)
    out = {}
    for d in range(p.H + 1):
        W, Wm, WVm, WAm = _alive_weights(al, d, p.n_theta, ref)
        out[d] = W.copy()
    return out, al

def vhat_of_type(k, t, d):
    """The market's belief at a date-d history that only type t can produce."""
    al = atoms(k, p)
    W, Wm, WVm, WAm = _alive_weights(al, d, p.n_theta, ref)
    if Wm[t] <= 0.0:
        return math.nan, 0.0
    return WVm[t] / Wm[t], W[t]

DELTAS = [3e-2, 1e-2, 1e-3, 1e-5, 1e-8, 0.0, -1e-8, -1e-5, -1e-3, -1e-2, -3e-2]
print("%-10s %-14s %-14s %-13s %-13s %-11s" %
      ("k2-s_edge", "T1(k)", "T2(k)", "vhat(t=%d,d=0)" % m_edge, "W[t]@d=0", "sec"))
rows = []
for dd in DELTAS:
    k = (K1, s_edge + dd)
    t0 = time.perf_counter()
    vh, w = vhat_of_type(k, m_edge, 0)
    Tk = outer_map(k, p)
    dt = time.perf_counter() - t0
    rows.append((dd, Tk[0], Tk[1], vh, w))
    print("%-10.1e %-14.9f %-14.9f %-13.8f %-13.3e %-11.2f"
          % (dd, Tk[0], Tk[1], vh, w, dt))

print()
print("reference (k-free) Ev[t=%d] = %.8f" % (m_edge, ref.Ev[m_edge]))
print("reference (k-free) Ev[t=%d] = %.8f" % (m_edge - 1, ref.Ev[m_edge - 1]))

# Jump measure: largest |T(k+) - T(k-)| across the smallest bracketing pair
pos = [r for r in rows if r[0] > 0]
neg = [r for r in rows if r[0] < 0]
if pos and neg:
    a = min(pos, key=lambda r: r[0])
    b = max(neg, key=lambda r: r[0])
    print("\nSMALLEST BRACKET  delta=+%.1e vs %.1e" % (a[0], b[0]))
    print("  |T1 jump| = %.6e     |T2 jump| = %.6e"
          % (abs(a[1] - b[1]), abs(a[2] - b[2])))
    print("  vhat: %.8f -> %.8f  (jump %.6e)" % (b[3], a[3], a[3] - b[3]))
