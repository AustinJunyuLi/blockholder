"""ANALYST A probe 6 — WHICH channel carries the belief jump into U_j?
Scratch only.

plan_payoff reads the pooled price family only through three type-indexed
aggregates: res.EP[d][theta] (execution-cost channel) and res.Ep_bid[theta],
res.EpP[theta] (terminal-value channel).  All three are integrals against the
type's OWN noise law -- full weight, no equilibrium-probability factor.
Measure each across the death surface of the type they index.
"""
import sys
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")

import numpy as np
from numerical_v4.params import ParamsV4, VOICE, HOLD
from numerical_v4.menu import atoms, type_reference, _sigmoid_inv, legal_clock, n_days
from numerical_v4.pooled import pooled_pass, _alive_weights

base = ParamsV4.baseline()
p = base.replace(kappa=0.5, tau=0.09076405861553302, T=5)
ref = type_reference(p)
K1 = 1.2405757282617416
EPS = 1e-9

E = {}
for m in range(1, p.H + 2):
    g = 1.0 - m / (p.n_scale * (p.H + 1))
    if 0.0 < g < 1.0:
        s = p.mu_v + p.sigma_s * _sigmoid_inv(g)
        if p.s_lo < s < p.s_hi:
            E[m] = s

for m_die in (10, 9, 8, 7):
    top = E[m_die - 1]
    bot = E[m_die]
    s_mid = 0.5 * (bot + top)
    cl = legal_clock(VOICE, s_mid, p)
    A = pooled_pass(atoms((K1, top - EPS), p), p, with_runup=True)
    B = pooled_pass(atoms((K1, top + EPS), p), p, with_runup=True)
    t = m_die
    print("=" * 72)
    print("TYPE %d (cell [%.5f,%.5f], n(s_mid)=%d, D=%s, f=%s) dies at k2=%.8f"
          % (t, bot, top, n_days(s_mid, p), cl.D, cl.f, top))
    print("  channel                below            above            JUMP")
    print("  Ep_bid[%2d]        %14.10f %14.10f  %+.4e"
          % (t, A.Ep_bid[t], B.Ep_bid[t], B.Ep_bid[t] - A.Ep_bid[t]))
    print("  EpP[%2d]           %14.10f %14.10f  %+.4e"
          % (t, A.EpP[t], B.EpP[t], B.EpP[t] - A.EpP[t]))
    tot = 0.0
    for d in range(p.H + 1):
        j = B.EP[d][t] - A.EP[d][t]
        tot += abs(j)
        if abs(j) > 1e-9:
            print("  EP[d=%2d][%2d]       %14.10f %14.10f  %+.4e"
                  % (d, t, A.EP[d][t], B.EP[d][t], j))
    print("  sum_d |EP[d] jump| = %.4e" % tot)
    # neighbouring (surviving) type, as a control
    tc = m_die - 1
    print("  CONTROL surviving type %d: Ep_bid jump %+.3e, sum_d|EP jump| %.3e"
          % (tc, B.Ep_bid[tc] - A.Ep_bid[tc],
             sum(abs(B.EP[d][tc] - A.EP[d][tc]) for d in range(p.H + 1))))
    print()
