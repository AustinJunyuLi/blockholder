import sys
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")
from numerical_v4.params import ParamsV4, VOICE, HOLD
from numerical_v4.menu import atoms, n_days
from numerical_v4.pooled import pooled_pass
from numerical_v4.policy import plan_payoff
from numerical_v4.solver import solve_policy, equilibrium_residual

p = ParamsV4().replace(kappa=0.15, tau=0.05, T=5)
for init in [(1.02, 1.71), (1.02, 1.70), (1.02, 1.72)]:
    pol, r = solve_policy(p, k_init=init)
    k = tuple(round(float(x), 10) for x in pol.k)
    print(f"  init={init}  ->  k={k}  cutoff={r.cutoff_scale:.3e}  "
          f"payoff={r.payoff_scale:.3e}  slopes={tuple(round(s,4) for s in r.slopes)}")
    print(f"       n(k2-)={n_days(k[1]-1e-9,p)} n(k2+)={n_days(k[1]+1e-9,p)}")
