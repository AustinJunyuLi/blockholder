"""ANALYST A probe 4 — precise jump in the CARD's outer map at type-death
surfaces.  Scratch only.

Corrected indexing: n(s) is weakly DECREASING, edge(m) is where n steps from
m+1 (below) to m (above).  So mark-type m occupies [edge(m), edge(m-1)] and it
DIES when the Voice cutoff k2 crosses edge(m-1), the TOP of its cell.

For each death surface we report
  (1) W[m] and vhat(m) just below / just above           -- the belief snap
  (2) the jump in U_VOICE(s;k) at the cell midpoint      -- the payoff channel
  (3) the CARD's T_2(k) = inf{s : j*(s;k) = VOICE}, located by brentq on the
      LOWEST sign change of U_VOICE - U_HOLD, on each side  -- the map jump
  (4) the implementation's outer_map T_2 for comparison (nearest-bracket).
"""
import sys, math
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")

import numpy as np
from scipy.optimize import brentq
from numerical_v4.params import ParamsV4, EXIT, HOLD, VOICE
from numerical_v4.menu import atoms, type_reference, n_days, _sigmoid_inv
from numerical_v4.pooled import _alive_weights, pooled_pass
from numerical_v4.policy import plan_payoff
from numerical_v4.solver import outer_map

base = ParamsV4.baseline()
p = base.replace(kappa=0.5, tau=0.09076405861553302, T=5)
ref = type_reference(p)
K1 = 1.2405757282617416
EPS = 1e-9

EDGES = {}
for m in range(1, p.H + 2):
    g = 1.0 - m / (p.n_scale * (p.H + 1))
    if 0.0 < g < 1.0:
        s = p.mu_v + p.sigma_s * _sigmoid_inv(g)
        if p.s_lo < s < p.s_hi:
            EDGES[m] = s

NG = 4001
GRID = np.linspace(p.s_lo, p.s_hi, NG)


def side(k2, m_dying):
    k = (K1, k2)
    al = atoms(k, p)
    W, Wm, WVm, WAm = _alive_weights(al, 0, p.n_theta, ref)
    res = pooled_pass(al, p, with_runup=True)

    def gapHV(s):
        return plan_payoff(VOICE, float(s), res, p) - plan_payoff(HOLD, float(s), res, p)

    vals = np.array([gapHV(s) for s in GRID])
    # CARD convention: T_2 = inf{s : VOICE is the argmax} -> LOWEST sign change
    T2 = p.s_hi
    for i in range(NG - 1):
        if vals[i] < 0.0 <= vals[i + 1] or (vals[i] <= 0.0 < vals[i + 1]):
            T2 = float(brentq(gapHV, GRID[i], GRID[i + 1], xtol=1e-13))
            break
    n_cross = int(np.count_nonzero(np.sign(vals[:-1]) * np.sign(vals[1:]) < 0))
    vh = WVm[m_dying] / Wm[m_dying] if Wm[m_dying] > 0 else float("nan")
    return dict(W=W[m_dying], vhat=vh, T2=T2, n_cross=n_cross,
                impl=outer_map(k, p, res)[1], res=res)


print("EDGES:", {m: round(s, 7) for m, s in EDGES.items()})
print("\ntype m cell = [edge(m), edge(m-1)];  m dies when k2 crosses edge(m-1)\n")

for m_die in (11, 10, 9, 8, 7, 6):
    top = EDGES.get(m_die - 1)
    bot = EDGES.get(m_die)
    if top is None:
        continue
    conc = p.mu_v + p.beta * (top - p.mu_v)
    A = side(top - EPS, m_die)     # type m_die still alive (sliver)
    B = side(top + EPS, m_die)     # type m_die dead -> k-free reference
    s_mid = 0.5 * ((bot if bot else p.s_lo) + top)
    uvA = plan_payoff(VOICE, s_mid, A["res"], p)
    uvB = plan_payoff(VOICE, s_mid, B["res"], p)
    print("=" * 76)
    print("TYPE %d  cell=[%.6f, %.6f]  dies at k2 = edge(%d) = %.10f"
          % (m_die, bot if bot else p.s_lo, top, m_die - 1, top))
    print("  W[%d]           below %.6e   above %.6e" % (m_die, A["W"], B["W"]))
    print("  vhat(%d)        below %.8f   above %.8f   JUMP %+.4e"
          % (m_die, A["vhat"], B["vhat"], B["vhat"] - A["vhat"]))
    print("     (k-free reference Ev[%d]=%.8f ; concentration limit %.8f ; "
          "predicted jump %+.4e)"
          % (m_die, ref.Ev[m_die], conc, ref.Ev[m_die] - conc))
    print("  U_VOICE(s=%.6f) below %.9f   above %.9f   JUMP %+.4e"
          % (s_mid, uvA, uvB, uvB - uvA))
    print("  CARD  T2 (lowest crossing)  below %.9f  above %.9f  |JUMP| %.4e"
          % (A["T2"], B["T2"], abs(B["T2"] - A["T2"])))
    print("  n sign changes of U_V-U_H   below %d  above %d"
          % (A["n_cross"], B["n_cross"]))
    print("  IMPL  T2 (nearest bracket)  below %.9f  above %.9f  |JUMP| %.4e"
          % (A["impl"], B["impl"], abs(B["impl"] - A["impl"])))
    print()
