"""ANALYST B probe 6 -- residual at the kappa=0.15 node's fixed point.

Does the ticket-34 signature (cutoff residual ~1e-12, payoff residual ~1e-3)
reproduce at k2 = 1.659062163, an n(s) cell edge?
"""
import sys
import numpy as np
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")
from numerical_v4.params import ParamsV4, VOICE, HOLD
from numerical_v4.menu import atoms, n_days
from numerical_v4.pooled import pooled_pass
from numerical_v4.policy import plan_payoff
from numerical_v4.solver import equilibrium_residual, outer_map, solve_policy

p = ParamsV4().replace(kappa=0.15, tau=0.05, T=5)
K = (1.020221781, 1.659062163)
res = pooled_pass(atoms(K, p), p, with_runup=True)
T = outer_map(K, p, res)
r = equilibrium_residual(K, p, res)
print(f"  k        = ({K[0]:.9f}, {K[1]:.9f})   [k2 = n(s) cell edge 1.659062163]")
print(f"  T(k)     = ({T[0]:.9f}, {T[1]:.9f})")
print(f"  cutoff-scale residual |k-T(k)|_inf = {r.cutoff_scale:.3e}")
print(f"  payoff-scale residual              = {r.payoff_scale:.3e}   "
      f"(criterion 1e-9)")
print(f"  local gap slopes = {r.slopes}")
print(f"  card ticket-34 record: cutoff 1e-14..1e-11, payoff 3.1e-4..1.5e-3")

print("\n  U_HOLD - U_VOICE just either side of the cell edge s = 1.659062163:")
for off in (1e-3, 1e-5, 1e-7, 1e-9, -1e-9, -1e-7, -1e-5, -1e-3):
    s = 1.659062163 - off
    uv = plan_payoff(VOICE, s, res, p); uh = plan_payoff(HOLD, s, res, p)
    print(f"    s = edge {-off:+.0e}  n(s)={n_days(s,p):2d}  U_H-U_V = {uh-uv:+.6e}")

print("\n  solver from its own default seed at this node:")
pol, rr = solve_policy(p)
print(f"    k = {tuple(round(float(x),9) for x in pol.k)}  "
      f"cutoff={rr.cutoff_scale:.3e}  payoff={rr.payoff_scale:.3e}")
