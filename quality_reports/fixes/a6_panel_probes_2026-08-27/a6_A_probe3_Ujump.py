"""ANALYST A probe 3 — the payoff-level jump at a type-death surface, and the
CARD's own outer map (inf of the argmax up-set, Step 13) rather than the
implementation's nearest-bracket device.

Scratch only.

At k2 crossing the top edge of mark-type t's cell, W[t] goes 0+ -> 0 and the
belief at t-exclusive pooled histories snaps from the concentration value to the
k-free type_reference value.  Measure:
  (1) the jump in vhat(t)
  (2) the jump in U_VOICE(s;k) at signals inside type t's cell
  (3) the jump in the card's T_i(k) = inf{s : j*(s;k) >= i+1}
"""
import sys, math, time
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")

import numpy as np
from numerical_v4.params import ParamsV4, EXIT, HOLD, VOICE
from numerical_v4.menu import atoms, type_reference, n_days, _sigmoid_inv
from numerical_v4.pooled import _alive_weights, pooled_pass
from numerical_v4.policy import plan_payoff

base = ParamsV4.baseline()
p = base.replace(kappa=0.5, tau=0.09076405861553302, T=5)
ref = type_reference(p)
K1 = 1.2405757282617416

def cell_edges():
    out = {}
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            s = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo < s < p.s_hi:
                out[m] = s
    return out

EDGES = cell_edges()

NG = 1201
GRID = np.linspace(p.s_lo, p.s_hi, NG)

def card_T(k, res):
    """T_i(k) = inf{s : j*(s;k) >= i+1}, j* the largest weakly increasing
    selection from argmax_j U_j(s;k).  With J = 3 the two components are the
    infima of the up-sets {j* >= HOLD} and {j* >= VOICE}."""
    U = np.array([[plan_payoff(j, float(s), res, p) for j in (EXIT, HOLD, VOICE)]
                  for s in GRID])
    arg = U.argmax(axis=1) + 1              # 1=EXIT 2=HOLD 3=VOICE
    # largest weakly increasing selection from a single-valued argmax is the
    # argmax itself where it is monotone; report the raw up-set infima.
    i_h = np.nonzero(arg >= HOLD)[0]
    i_v = np.nonzero(arg >= VOICE)[0]
    T1 = float(GRID[i_h[0]]) if i_h.size else p.s_hi
    T2 = float(GRID[i_v[0]]) if i_v.size else p.s_hi
    return T1, T2, U, arg

def snapshot(k2, tag, s_probe):
    k = (K1, k2)
    al = atoms(k, p)
    W, Wm, WVm, WAm = _alive_weights(al, 0, p.n_theta, ref)
    res = pooled_pass(al, p, with_runup=True)
    T1, T2, U, arg = card_T(k, res)
    uv = [plan_payoff(VOICE, s, res, p) for s in s_probe]
    uh = [plan_payoff(HOLD, s, res, p) for s in s_probe]
    return dict(k2=k2, tag=tag, W=W.copy(), Wm=Wm.copy(),
                vhat=np.where(Wm > 0, WVm / np.where(Wm > 0, Wm, 1), np.nan),
                T1=T1, T2=T2, uv=np.array(uv), uh=np.array(uh),
                EP0=res.EP[0].copy(), Epb=res.Ep_bid.copy())

print("cell edges:", {m: round(s, 6) for m, s in EDGES.items()})
print()

# Type t dies as k2 crosses the TOP of its cell.  n(s) is weakly decreasing, so
# type m's cell is [edge(m+1), edge(m)] -- crossing edge(m) upward kills type m.
for m_die in (10, 9, 8):
    s_e = EDGES[m_die]
    lo_e = EDGES.get(m_die + 1, p.s_lo)
    s_probe = np.array([lo_e + f * (s_e - lo_e) for f in (0.2, 0.5, 0.8, 0.98)])
    print("=" * 78)
    print("TYPE %d dies as k2 crosses s=%.10f  (its cell = [%.6f, %.6f])"
          % (m_die, s_e, lo_e, s_e))
    print("   k-free reference Ev[%d] = %.8f ; concentration limit mu+beta(edge-mu) = %.8f"
          % (m_die, ref.Ev[m_die], p.mu_v + p.beta * (s_e - p.mu_v)))
    A = snapshot(s_e - 1e-9, "below (type alive)", s_probe)
    B = snapshot(s_e + 1e-9, "above (type dead)", s_probe)
    print("   W[%d]: below=%.4e   above=%.4e" % (m_die, A["W"][m_die], B["W"][m_die]))
    print("   vhat(t=%d):  below=%.8f  above=%.8f   JUMP=%+.6e"
          % (m_die, A["vhat"][m_die], B["vhat"][m_die],
             B["vhat"][m_die] - A["vhat"][m_die]))
    print("   E[P_0^P | theta=%d]: below=%.8f above=%.8f  JUMP=%+.6e"
          % (m_die, A["EP0"][m_die], B["EP0"][m_die],
             B["EP0"][m_die] - A["EP0"][m_die]))
    print("   E[p_bid | theta=%d]: below=%.8f above=%.8f  JUMP=%+.6e"
          % (m_die, A["Epb"][m_die], B["Epb"][m_die],
             B["Epb"][m_die] - A["Epb"][m_die]))
    print("   U_VOICE(s) inside the dying cell:")
    for i, s in enumerate(s_probe):
        print("      s=%.6f  below=%.9f  above=%.9f   JUMP=%+.6e   (U_HOLD jump %+.3e)"
              % (s, A["uv"][i], B["uv"][i], B["uv"][i] - A["uv"][i],
                 B["uh"][i] - A["uh"][i]))
    print("   CARD T(k) (inf of argmax up-sets, grid %d):" % NG)
    print("      below: T1=%.8f T2=%.8f" % (A["T1"], A["T2"]))
    print("      above: T1=%.8f T2=%.8f" % (B["T1"], B["T2"]))
    print("      |T1 jump| = %.4e   |T2 jump| = %.4e"
          % (abs(B["T1"] - A["T1"]), abs(B["T2"] - A["T2"])))
    print()
