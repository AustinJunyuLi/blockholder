import sys
sys.path.insert(0, "/Users/austinli/Projects/blockholder_v4_theory")
from numerical_v4.params import ParamsV4, EXIT, HOLD, VOICE
from numerical_v4.menu import atoms, n_days
from numerical_v4.pooled import pooled_pass
from numerical_v4.policy import plan_payoff

NAME = {EXIT: "EXIT", HOLD: "HOLD", VOICE: "VOICE"}
p = ParamsV4().replace(kappa=0.15, tau=0.05, T=5)
for K in [(1.020221781, 1.659062163), (1.0260443221, 1.7104049079)]:
    res = pooled_pass(atoms(K, p), p, with_runup=True)
    print(f"\n  k = {K}")
    for e in (1.659062162746, 1.749268649265):
        print(f"   around n(s) cell edge {e:.9f}:")
        for off in (-1e-4, -1e-6, 1e-6, 1e-4):
            s = e + off
            u = {j: plan_payoff(j, s, res, p) for j in (EXIT, HOLD, VOICE)}
            am = max(u, key=u.get)
            print(f"     s=edge{off:+.0e} n={n_days(s,p):2d}  "
                  f"U_E={u[EXIT]:.9f} U_H={u[HOLD]:.9f} U_V={u[VOICE]:.9f}"
                  f"   argmax={NAME[am]}")
