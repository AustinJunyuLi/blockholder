"""Two facts that settle the correspondence-route verdict.

(A) Does the fixed-t blend actually RESTORE k-continuity of T_2?  That is the
    route's positive claim (A6's continuity half).  Sweep k_2 across the
    edge(8) = 1.583333333 hyperplane, where the shipped map jumps 6.33e-3, and
    compare the shipped switch against the blend at eps = 1e-6.
    PREDICTION: the switch jumps between +/-1e-8; the blend resolves the same
    total move into a smooth transition over a window of width ~ eps/phi.

(B) Does the locus-(ii) A3 failure -- the VOICE->HOLD argmax REVERSAL across
    edge 1.659062163 at the (kappa=0.15, tau=0.05, T=5) node's located fixed
    point, where U_H - U_V jumps through zero without crossing -- survive the
    mass-proportional (card Step 9(b)-faithful) off-path family?
    Locus (i) did NOT (t_blend_diagnose.py: 3 sign changes -> 1 under
    massprop).  Locus (ii) is a different mechanism: a single n(s) step in
    U_VOICE at a fixed s-edge, not a multi-dead-type belief average.
    PREDICTION: locus (ii) SURVIVES -- it is s-direction, not belief-family.

Read-only on the repo.  No repo writes, no git.
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np
from scipy.optimize import brentq

ROOT = "/Users/austinli/Projects/blockholder_v4_theory"
sys.path.insert(0, ROOT)

import numerical_v4.pooled as pooled_mod                              # noqa: E402
from numerical_v4.params import ParamsV4, VOICE, HOLD                 # noqa: E402
from numerical_v4.menu import (atoms, type_reference, n_days,         # noqa: E402
                               _sigmoid_inv, _interval_mass_and_mean)
from numerical_v4.pooled import pooled_pass                           # noqa: E402
from numerical_v4.policy import plan_payoff, frozen_tau_grid          # noqa: E402
from numerical_v4.solver import solve_policy                          # noqa: E402

NG = 4001
_ORIG = pooled_mod._alive_weights
NODE15_K = (1.0202217805248246, 1.6590621627461504)      # filed pinned point
NODE15_EDGE = 1.6590621627456204


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


def make(kind, eps, mass):
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
                Wm[t], WVm[t], WAm[t] = fl, fl * float(ref.Ev[t]), fl * float(ref.a[t])
            else:
                Wm[t] = (1.0 - eps) * Wm[t] + fl
                WVm[t] = (1.0 - eps) * WVm[t] + fl * float(ref.Ev[t])
                WAm[t] = (1.0 - eps) * WAm[t] + fl * float(ref.a[t])
        return W, Wm, WVm, WAm
    return f


def card_T2(k1, k2, p):
    """inf{s : VOICE is the argmax} -- the card's T_2, lowest up-crossing."""
    res = pooled_pass(atoms((k1, k2), p), p, with_runup=True)

    def gap(s):
        return float(plan_payoff(VOICE, float(s), res, p)
                     - plan_payoff(HOLD, float(s), res, p))
    grid = np.linspace(p.s_lo, p.s_hi, NG)
    vals = np.array([gap(s) for s in grid])
    for i in range(NG - 1):
        if vals[i] < 0.0 <= vals[i + 1] or vals[i] <= 0.0 < vals[i + 1]:
            return float(brentq(gap, grid[i], grid[i + 1], xtol=1e-13))
    return float(p.s_hi)


def sign_profile(k1, k2, p, probe_s=None):
    res = pooled_pass(atoms((k1, k2), p), p, with_runup=True)
    grid = np.linspace(p.s_lo, p.s_hi, NG)
    vals = np.array([float(plan_payoff(VOICE, float(s), res, p)
                           - plan_payoff(HOLD, float(s), res, p))
                     for s in grid])
    cr = [0.5 * (grid[i] + grid[i + 1]) for i in range(NG - 1)
          if (vals[i] < 0.0 <= vals[i + 1]) or (vals[i] > 0.0 >= vals[i + 1])]
    out = dict(n_sign_changes=len(cr), crossings=[float(c) for c in cr[:6]])
    if probe_s is not None:
        for lbl, s in probe_s.items():
            out[f"UV_minus_UH@{lbl}"] = float(
                plan_payoff(VOICE, float(s), res, p)
                - plan_payoff(HOLD, float(s), res, p))
    return out


def main() -> int:
    out: dict = {"kind": "route-exploration probe (scratchpad, NOT a t2 check)"}
    p_seed = ParamsV4.baseline()
    pol_seed, _ = solve_policy(p_seed)
    tau50 = float(frozen_tau_grid(pol_seed, p_seed, (0.5,))[0])
    p_base = p_seed.replace(tau=tau50)
    pol_base, _ = solve_policy(p_base)
    k1 = float(pol_base.k[0])
    pA = p_base.replace(kappa=0.5, T=5)
    massA = uniform_type_mass(pA)
    edges = {}
    for m in range(1, pA.H + 2):
        g = 1.0 - m / (pA.n_scale * (pA.H + 1))
        if 0.0 < g < 1.0:
            x = pA.mu_v + pA.sigma_s * _sigmoid_inv(g)
            if pA.s_lo < x < pA.s_hi:
                edges[m] = x
    E8 = edges[8]
    print(f"(A) k-continuity across edge(8) = {E8!r}, k1 = {k1!r}")
    offs = (-1e-4, -1e-5, -3e-6, -1e-6, -3e-7, -1e-7, -1e-8, 0.0, 1e-8, 1e-6, 1e-4)
    rowsA = []
    for kind, eps in (("switch_uniform", 1e-14), ("blend_uniform", 1e-6)):
        pooled_mod._alive_weights = make(kind, eps, massA)
        vals = []
        for o in offs:
            v = card_T2(k1, E8 + o, pA)
            vals.append(v)
            print(f"    {kind:15s} off={o:+9.1e}  T_2 = {v:.10f}")
        step = max(abs(vals[i + 1] - vals[i]) for i in range(len(vals) - 1))
        rowsA.append(dict(kind=kind, eps=eps, offsets=list(offs),
                          T2=[float(v) for v in vals],
                          total_move=float(abs(vals[-1] - vals[0])),
                          max_adjacent_step=float(step)))
        print(f"    -> total move {abs(vals[-1]-vals[0]):.3e}, "
              f"max adjacent step {step:.3e}")
    out["A_k_continuity"] = dict(edge=E8, k1=k1, rows=rowsA)

    # ---- (B) locus (ii): the argmax REVERSAL at the node-15 pinned point ----
    pB = p_base.replace(kappa=0.15, tau=0.05, T=5)
    massB = uniform_type_mass(pB)
    probe = {"edge-1e-6": NODE15_EDGE - 1e-6, "edge+1e-6": NODE15_EDGE + 1e-6,
             "edge-1e-3": NODE15_EDGE - 1e-3, "edge+1e-3": NODE15_EDGE + 1e-3}
    print(f"\n(B) locus (ii) at kappa=0.15, tau=0.05, T=5, "
          f"k = {NODE15_K}, edge = {NODE15_EDGE!r}")
    rowsB = []
    for kind in ("switch_uniform", "switch_massprop",
                 "blend_uniform", "blend_massprop"):
        for eps in (1e-14, 1e-6):
            pooled_mod._alive_weights = make(kind, eps, massB)
            pr = sign_profile(NODE15_K[0], NODE15_K[1], pB, probe)
            below = pr["UV_minus_UH@edge-1e-6"]
            above = pr["UV_minus_UH@edge+1e-6"]
            reversal = bool(below > 0.0 > above)   # VOICE below -> HOLD above
            rowsB.append(dict(kind=kind, eps=eps, reversal=reversal, **pr))
            print(f"    {kind:17s} eps={eps:7.0e}  "
                  f"UV-UH below={below:+.6e} above={above:+.6e}  "
                  f"V->H reversal = {reversal}  n_sign_changes={pr['n_sign_changes']}")
    pooled_mod._alive_weights = _ORIG
    out["B_locus_ii"] = dict(node=dict(kappa=0.15, tau=0.05, T=5),
                             k=list(NODE15_K), edge=NODE15_EDGE, rows=rowsB)
    out["verdict_B"] = ("reversal SURVIVES every family"
                        if all(r["reversal"] for r in rowsB)
                        else "reversal is family-dependent: "
                             + str([(r["kind"], r["reversal"]) for r in rowsB]))
    print(f"\n(B) VERDICT: {out['verdict_B']}")
    dst = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "t_blend_settle.json")
    with open(dst, "w") as fh:
        json.dump(out, fh, indent=1, default=float)
    print(f"-> {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
