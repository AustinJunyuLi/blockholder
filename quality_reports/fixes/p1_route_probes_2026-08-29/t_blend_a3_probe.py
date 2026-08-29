"""ROUTE-EXPLORATION PROBE (scratchpad, analysis-grade, NOT a curated t2 check).

QUESTION.  Does the A3 failure at the implemented calibration survive in the
GENUINE fixed-t constrained game -- i.e. is the correspondence route's
nonemptiness hypothesis still false once the off-path belief switch is replaced
by a continuous full-support blend?

WHY IT MATTERS.  Step 18's Kakutani correspondence is "nonempty by A3".  If the
fixed-t game repairs A3, the route buys both A3 and A6.  If not, it buys only
A6's continuity half.

WHAT THE IMPLEMENTATION DOES NOW (numerical_v4/pooled.py:225-235):

    if Wm[t] > 0.0: continue        # <- HARD SWITCH at exactly zero mass
    Wm[t]  = OFF_PATH_EPS
    WVm[t] = OFF_PATH_EPS * ref.Ev[t]

At a type-EXCLUSIVE pooled history the belief is WVm[t]/Wm[t] = ref.Ev[t],
independent of the floor's size -- so this is the t = 0 card construction with
a discontinuous switch, NOT a fixed-t game.

WHAT THE BLEND DOES (the genuine fixed-t constrained game):

    Wm[t]  = (1-e)*W[t]  + e*m[t]
    WVm[t] = (1-e)*WV[t] + e*m[t]*ref.Ev[t]
    WAm[t] = (1-e)*WA[t] + e*m[t]*ref.a[t]

with m[t] the whole-line (cutoff-free) mass of {n(s) = t}: every type carries a
full-support floor proportional to its plan-uniform mass, and the belief slides
CONTINUOUSLY from the truncated-cell mean to ref.Ev[t] as W[t] falls to 0.
That is Step 9(b)'s stage-n object at t_n = e.

PRE-REGISTERED PREDICTION (written before the first run).
  (P1) The dying type's alive mass is EXACTLY zero above the edge (its cell
       lies entirely below k_2), so the blend returns ref.Ev[t] exactly at
       every e: the two levels the switch interpolates between do not move
       with e.  Only the WIDTH of the transition window is t-sensitive.
  (P2) Hence the three strict sign changes of U_VOICE - U_HOLD persist at
       every e <= 1e-6, with excursions within a few percent of baseline.
  (P3) Therefore S(k) = {} at those k in the fixed-t game too, and Step 18's
       correspondence is EMPTY there -- Kakutani fails at nonemptiness, not at
       convexity or at upper hemicontinuity.

  FALSIFIER: if the sign-change count drops to 1 at some e <= 1e-6, the blend
  repairs A3 and the verdict flips toward GO.

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
from numerical_v4.params import ParamsV4, HOLD, VOICE                 # noqa: E402
from numerical_v4.menu import (atoms, type_reference, n_days,         # noqa: E402
                               _sigmoid_inv, _interval_mass_and_mean)
from numerical_v4.pooled import pooled_pass                           # noqa: E402
from numerical_v4.policy import plan_payoff, frozen_tau_grid          # noqa: E402
from numerical_v4.solver import solve_policy                          # noqa: E402

NG = 4001
DELTAS = (1e-9, 1e-4, 2e-2)
EPSILONS = (1e-14, 1e-9, 1e-6, 1e-3)
FILED_SIGN_CHANGES = (1.5754434, 1.5833333, 1.5902426)   # Analyst A, filed

_ORIG_ALIVE = pooled_mod._alive_weights


def uniform_type_mass(p: ParamsV4) -> np.ndarray:
    """m[t] = Pr(n(s) = t) on the whole signal line -- the plan-uniform mass.

    Built from the same edge list menu.type_reference uses, so the partition is
    identical to the one the reference beliefs are computed on.
    """
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


def make_blend(eps: float, mass: np.ndarray):
    """The continuous fixed-t replacement for _alive_weights."""
    def blended(atom_list, d, n_theta, ref=None):
        W, Wm, WVm, WAm = _ORIG_ALIVE(atom_list, d, n_theta, None)
        if ref is None:
            return W, Wm, WVm, WAm
        Wm, WVm, WAm = W.copy(), WVm.copy(), WAm.copy()
        for t in range(n_theta):
            if ref.D[t] == 1.0 and ref.f[t] <= d:
                continue            # this type's flag would already be public
            m = float(mass[t]) if t < len(mass) else 0.0
            Wm[t] = (1.0 - eps) * Wm[t] + eps * m
            WVm[t] = (1.0 - eps) * WVm[t] + eps * m * float(ref.Ev[t])
            WAm[t] = (1.0 - eps) * WAm[t] + eps * m * float(ref.a[t])
        return W, Wm, WVm, WAm
    return blended


def gap_profile(k1: float, k2: float, p: ParamsV4) -> dict:
    """Sign changes and argmax pattern of U_VOICE - U_HOLD over the bracket."""
    al = atoms((k1, k2), p)
    res = pooled_pass(al, p, with_runup=True)
    grid = np.linspace(p.s_lo, p.s_hi, NG)
    vals = np.array([float(plan_payoff(VOICE, float(s), res, p)
                           - plan_payoff(HOLD, float(s), res, p))
                     for s in grid])
    crossings, excursions = [], []
    for i in range(NG - 1):
        a, b = vals[i], vals[i + 1]
        if (a < 0.0 <= b) or (a <= 0.0 < b) or (a > 0.0 >= b) or (a >= 0.0 > b):
            crossings.append(0.5 * (grid[i] + grid[i + 1]))
    # the middle excursion: max |gap| strictly between the first and last crossing
    if len(crossings) >= 2:
        sel = (grid > crossings[0]) & (grid < crossings[-1])
        if sel.any():
            excursions = [float(np.max(np.abs(vals[sel])))]
    return dict(n_sign_changes=len(crossings),
                crossings=[float(c) for c in crossings[:8]],
                middle_excursion_max_abs=excursions[0] if excursions else None,
                argmax_pattern="".join(
                    ("V" if v > 0 else "H") for v in vals[::200]))


def main() -> int:
    print("solving seed / frozen-tau baseline ...", flush=True)
    p_seed = ParamsV4.baseline()
    pol_seed, _ = solve_policy(p_seed)
    tau50 = float(frozen_tau_grid(pol_seed, p_seed, (0.5,))[0])
    p_base = p_seed.replace(tau=tau50)
    pol_base, _ = solve_policy(p_base)
    k1 = float(pol_base.k[0])
    p = p_base.replace(kappa=0.5, T=5)
    print(f"  tau_50 = {tau50!r}   k1 = {k1!r}", flush=True)

    # the edge whose crossing kills mark-type 7 (Analyst A's "edge(6)")
    edges = {}
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            x = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo < x < p.s_hi:
                edges[m] = x
    edge6 = edges[6]
    mass = uniform_type_mass(p)
    ref = type_reference(p)
    print(f"  edge(6) = {edge6!r}   dying type = 7   "
          f"ref.Ev[7] = {float(ref.Ev[7])!r}   m[7] = {float(mass[7]):.6e}",
          flush=True)

    out: dict = {"kind": "route-exploration probe (scratchpad, NOT a t2 check)",
                 "node": dict(kappa=0.5, tau=tau50, T=5, k1=k1,
                              edge6=edge6, dying_type=7),
                 "prediction": "3 sign changes persist at every eps <= 1e-6",
                 "rows": []}

    # (P1) is the dying type's alive mass exactly zero above the edge?
    for delta in DELTAS:
        al = atoms((k1, edge6 + delta), p)
        W, _, _, _ = _ORIG_ALIVE(al, 0, p.n_theta, ref)
        out.setdefault("alive_mass_of_dying_type", {})[f"delta={delta:g}"] = \
            float(W[7])
    print(f"  alive mass of type 7 above the edge: "
          f"{out['alive_mass_of_dying_type']}", flush=True)

    for eps in (None,) + EPSILONS:
        label = "baseline (hard switch)" if eps is None else f"blend eps={eps:g}"
        pooled_mod._alive_weights = (_ORIG_ALIVE if eps is None
                                     else make_blend(eps, mass))
        for delta in DELTAS:
            prof = gap_profile(k1, edge6 + delta, p)
            row = dict(variant=label, eps=eps, delta=delta, **prof)
            out["rows"].append(row)
            print(f"  {label:24s} delta={delta:8.1e}  "
                  f"sign changes = {prof['n_sign_changes']}  "
                  f"excursion = {prof['middle_excursion_max_abs']}",
                  flush=True)
    pooled_mod._alive_weights = _ORIG_ALIVE

    base = {r["delta"]: r["n_sign_changes"]
            for r in out["rows"] if r["eps"] is None}
    survives = all(r["n_sign_changes"] == base[r["delta"]]
                   for r in out["rows"] if r["eps"] is not None
                   and r["eps"] <= 1e-6)
    out["prediction_upheld"] = bool(survives)
    out["verdict"] = ("A3 failure SURVIVES the fixed-t blend at every eps <= 1e-6"
                      if survives else
                      "A3 failure DOES NOT survive -- blend repairs it")
    dst = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "t_blend_a3_probe.json")
    with open(dst, "w") as fh:
        json.dump(out, fh, indent=1, default=float)
    print(f"\nVERDICT: {out['verdict']}\n  -> {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
