"""Disentangle WHY the blend changed the A3 pattern.

The blend differs from the implementation's floor in THREE ways at once:
  (a) continuous vs hard switch at exactly-zero mass;
  (b) mass-PROPORTIONAL floor (eps*m[t]) vs UNIFORM floor (eps for every dead
      type) -- these give different beliefs at a history reachable only by a
      SET of dead types;
  (c) types with m[t] = 0 (no interval in the n(s) partition maps to them) lose
      their floor entirely under a mass-proportional rule, so a history only
      such a type can produce has ZERO market weight.

Four variants, to isolate which one moves the A3 pattern.
Read-only on the repo.  No repo writes, no git.
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

ROOT = "/Users/austinli/Projects/blockholder_v4_theory"
sys.path.insert(0, ROOT)

import numerical_v4.pooled as pooled_mod                              # noqa: E402
from numerical_v4.params import ParamsV4, VOICE, HOLD                 # noqa: E402
from numerical_v4.menu import (atoms, type_reference, n_days,         # noqa: E402
                               _sigmoid_inv, _interval_mass_and_mean)
from numerical_v4.pooled import pooled_pass, OFF_PATH_EPS             # noqa: E402
from numerical_v4.policy import plan_payoff, frozen_tau_grid          # noqa: E402
from numerical_v4.solver import solve_policy                          # noqa: E402

NG = 4001
_ORIG = pooled_mod._alive_weights


def uniform_type_mass(p):
    edges = [p.s_lo, p.s_hi]
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            x = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo < x < p.s_hi:
                edges.append(x)
    edges = sorted(set(edges))
    out = np.zeros(p.n_theta)
    for lo, hi in zip(edges[:-1], edges[1:]):
        t = n_days(0.5 * (lo + hi), p)
        w, _ = _interval_mass_and_mean(lo, hi, p)
        out[t] += w
    return out


def make(kind: str, eps: float, mass: np.ndarray):
    """kind in {switch_uniform (= shipped), switch_massprop,
                blend_uniform, blend_massprop}."""
    def f(atom_list, d, n_theta, ref=None):
        W, Wm, WVm, WAm = _ORIG(atom_list, d, n_theta, None)
        if ref is None:
            return W, Wm, WVm, WAm
        Wm, WVm, WAm = W.copy(), WVm.copy(), WAm.copy()
        for t in range(n_theta):
            if ref.D[t] == 1.0 and ref.f[t] <= d:
                continue
            m = float(mass[t]) if t < len(mass) else 0.0
            fl = eps * (m if "massprop" in kind else 1.0)
            if kind.startswith("switch"):
                if Wm[t] > 0.0:
                    continue
                Wm[t] = fl
                WVm[t] = fl * float(ref.Ev[t])
                WAm[t] = fl * float(ref.a[t])
            else:
                Wm[t] = (1.0 - eps) * Wm[t] + fl
                WVm[t] = (1.0 - eps) * WVm[t] + fl * float(ref.Ev[t])
                WAm[t] = (1.0 - eps) * WAm[t] + fl * float(ref.a[t])
        return W, Wm, WVm, WAm
    return f


def profile(k1, k2, p):
    al = atoms((k1, k2), p)
    res = pooled_pass(al, p, with_runup=True)
    grid = np.linspace(p.s_lo, p.s_hi, NG)
    vals = np.array([float(plan_payoff(VOICE, float(s), res, p)
                           - plan_payoff(HOLD, float(s), res, p))
                     for s in grid])
    cr = [0.5 * (grid[i] + grid[i + 1]) for i in range(NG - 1)
          if (vals[i] < 0.0 <= vals[i + 1]) or (vals[i] > 0.0 >= vals[i + 1])]
    exc = None
    if len(cr) >= 2:
        sel = (grid > cr[0]) & (grid < cr[-1])
        if sel.any():
            exc = float(np.max(np.abs(vals[sel])))
    return dict(n=len(cr), crossings=[float(c) for c in cr[:6]],
                excursion=exc, nan=bool(np.isnan(vals).any()),
                max_resid=float(res.max_price_residual),
                n_hist=int(res.n_hist_feasible))


def main() -> int:
    p_seed = ParamsV4.baseline()
    pol_seed, _ = solve_policy(p_seed)
    tau50 = float(frozen_tau_grid(pol_seed, p_seed, (0.5,))[0])
    p_base = p_seed.replace(tau=tau50)
    pol_base, _ = solve_policy(p_base)
    k1 = float(pol_base.k[0])
    p = p_base.replace(kappa=0.5, T=5)
    edges = {}
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            x = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo < x < p.s_hi:
                edges[m] = x
    edge6, mass, ref = edges[6], uniform_type_mass(p), type_reference(p)
    k2 = edge6 + 1e-4

    al = atoms((k1, k2), p)
    W, Wm0, _, _ = _ORIG(al, 0, p.n_theta, ref)
    zero_m = [t for t in range(p.n_theta) if float(mass[t]) == 0.0]
    dead = [t for t in range(p.n_theta) if float(W[t]) == 0.0]
    out = {"node": dict(kappa=0.5, tau=tau50, T=5, k1=k1, k2=k2, edge6=edge6),
           "OFF_PATH_EPS": OFF_PATH_EPS,
           "types_with_zero_uniform_mass": zero_m,
           "types_dead_at_this_k": dead,
           "mass": {t: float(mass[t]) for t in range(p.n_theta)},
           "alive_W": {t: float(W[t]) for t in range(p.n_theta)},
           "rows": []}
    print(f"dead types at k2={k2:.9f}: {dead}")
    print(f"types with ZERO uniform mass m[t]: {zero_m}")
    print(f"m[t] = {[round(float(x), 5) for x in mass]}")

    for kind in ("switch_uniform", "switch_massprop",
                 "blend_uniform", "blend_massprop"):
        for eps in (1e-14, 1e-9, 1e-6):
            pooled_mod._alive_weights = make(kind, eps, mass)
            pr = profile(k1, k2, p)
            out["rows"].append(dict(kind=kind, eps=eps, **pr))
            print(f"  {kind:17s} eps={eps:7.0e}  n={pr['n']}  "
                  f"exc={pr['excursion']}  nan={pr['nan']}  "
                  f"resid={pr['max_resid']:.2e}  nhist={pr['n_hist']}")
    pooled_mod._alive_weights = _ORIG
    dst = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "t_blend_diagnose.json")
    with open(dst, "w") as fh:
        json.dump(out, fh, indent=1, default=float)
    print(f"\n-> {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
