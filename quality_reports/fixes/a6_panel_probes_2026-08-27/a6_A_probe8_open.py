"""ANALYST A probe 8 -- is the A3 failure (3 crossings) an OPEN set in k2, or a
knife-edge?  Scratch only."""
import sys
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")
import numpy as np
from numerical_v4.params import ParamsV4, HOLD, VOICE
from numerical_v4.menu import atoms, _sigmoid_inv
from numerical_v4.pooled import pooled_pass
from numerical_v4.policy import plan_payoff

base = ParamsV4.baseline()
p = base.replace(kappa=0.5, tau=0.09076405861553302, T=5)
K1 = 1.2405757282617416
E = {}
for m in range(1, p.H + 2):
    g = 1.0 - m / (p.n_scale * (p.H + 1))
    if 0.0 < g < 1.0:
        s = p.mu_v + p.sigma_s * _sigmoid_inv(g)
        if p.s_lo < s < p.s_hi: E[m] = s
GRID = np.linspace(p.s_lo, p.s_hi, 6001)
print("edge(6) = %.8f, edge(5) = %.8f  (type 7's cell top / type 6's cell top)"
      % (E[6], E[5]))
for off in (1e-9, 1e-4, 1e-3, 5e-3, 2e-2, 5e-2, 1e-1):
    k2 = E[6] + off
    res = pooled_pass(atoms((K1, k2), p), p, with_runup=True)
    g = np.array([plan_payoff(VOICE, float(s), res, p)
                  - plan_payoff(HOLD, float(s), res, p) for s in GRID])
    sc = np.nonzero(np.sign(g[:-1]) * np.sign(g[1:]) < 0)[0]
    mono = "MONOTONE-OK" if len(sc) <= 1 else "A3 FAILS (argmax alternates)"
    print("  k2 = edge(6) + %-8.0e = %.7f : %d sign changes  -> %s"
          % (off, k2, len(sc), mono))
