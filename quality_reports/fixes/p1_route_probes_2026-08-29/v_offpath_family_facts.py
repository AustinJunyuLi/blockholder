"""VERIFIER probe 1 -- the structural facts behind findings F1 and F2.

Written 2026-08-29 by a fresh verifier agent who did NOT write the
p1-existence-route exploration.  Read-only on ``numerical_v4/``: nothing under
that package is modified on disk and no monkeypatch is installed here.

WHAT THIS ESTABLISHES (facts only; no verdict is computed here).

  A.  ``type_reference`` per type: Ev[t], a[t], D[t], f[t], and the
      plan-uniform type mass m[t] = Pr(n(s) = t) that a Step-9(b)-faithful
      off-path family would attach.  The EXACTNESS PRE-CHECK for F2 lives
      here: Step 9(b)'s Lambda_u weights type t by
      sum_j int_{theta(j,s)=t} L_j(h|s) phi_s(s) ds, and L_j carries the FLAG
      indicator.  If every DEAD type at the probed k has D[t] = 0 (or
      f[t] > H) then the flag indicator is vacuous on the pooled cell for
      those types and m[t] = Pr(n(s)=t) is EXACTLY Step 9(b)'s weight for
      them (the 1/J factor cancels in the ratio).  Type 0's weight is the one
      the exploration's ``uniform_type_mass`` gets wrong (it returns 0.0; the
      Step-9(b) value is 2 = Exit + Hold, each contributing all of phi_s) --
      that error is inert iff type 0 is ALIVE at the probed k, which is
      recorded here at both loci.

  B.  The alive weight vector W[t] at locus (i)'s whole k_2 ladder and at
      locus (ii)'s pinned fixed point: which types are dead, and with what
      plan-uniform mass.

  C.  ``menu.breakpoints`` merges near-duplicate breakpoints at 1e-9
      (``menu.py:244``, ``np.diff(arr) > 1e-9``).  So as k_2 rises to an n(s)
      cell edge from BELOW, the sliver atom [k_2, edge) is merged away and the
      type that owns it dies at an offset of order 1e-9 rather than at the
      edge itself.  This sweep measures exactly where W[t] hits 0.0.  It is
      the empirical content of the card's A6-note hedge "with the switch
      relocated by ~1e-9 rather than removed" (MODEL_CARD.md:309-310).

Deterministic: fixed grids, no RNG.  Run with ``.venv/bin/python`` from the
repo root.
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

ROOT = "/Users/austinli/Projects/blockholder_v4_theory"
sys.path.insert(0, ROOT)

from numerical_v4.params import ParamsV4                          # noqa: E402
from numerical_v4.menu import (atoms, type_reference, n_days,      # noqa: E402
                               _sigmoid_inv, _interval_mass_and_mean,
                               breakpoints)
from numerical_v4.pooled import _alive_weights, OFF_PATH_EPS       # noqa: E402
from numerical_v4.policy import frozen_tau_grid                    # noqa: E402
from numerical_v4.solver import solve_policy                       # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "v_offpath_family_facts.json")

# The card's locus-1 k_2 ladder (MODEL_CARD.md:190-191, and
# t2_a3_ordered_plans_check.py LADDER_OPEN / LADDER_CLOSED / OFFSET_BELOW).
LADDER = (-1e-9, 1e-9, 1e-4, 1e-3, 5e-3, 2e-2, 5e-2, 1e-1)

# Locus (ii): a6_B_argmax.py's own k literals, replayed by
# t2_a3_ordered_plans_check.py; and the ticket-34 full-precision pinned point.
NODE15_FP1 = (1.0202217805, 1.6590621627)
NODE15_FP1_FULL = (1.0202217805248246, 1.6590621627461504)
NODE15_FP2 = (1.0260443221, 1.7104049079)
NODE15_EDGE = 1.659062162746


def n_edges(p: ParamsV4) -> dict[int, float]:
    """Interior n(s) cell edges -- the construction menu.type_reference uses."""
    out: dict[int, float] = {}
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            s = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo < s < p.s_hi:
                out[m] = s
    return out


def plan_uniform_type_mass(p: ParamsV4) -> np.ndarray:
    """m[t] = sum_j Pr(theta(j, s) = t) under the plan-uniform perturbation.

    Step 9(b)'s Lambda_u = sum_{j'} int L_{j'}(h|s') phi_s(s') ds'.  Grouping
    (j', s') by mark-path type: Lambda_u = sum_t L_t(h) * m[t] with
    m[t] = sum_{j'} Pr(theta(j', s) = t).  On this menu (menu.py:6-11):
      * Exit and Hold both give the all-zero path for EVERY s  -> m[0] = 2;
      * Voice gives theta = n(s)                               -> m[t] = Pr(n(s)=t).
    The exploration's ``uniform_type_mass`` returns the Voice half only, so it
    reports m[0] = 0.  Both variants are recorded here.
    """
    edges = [p.s_lo, p.s_hi]
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            x = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo < x < p.s_hi:
                edges.append(x)
    edges = sorted(set(edges))
    voice = np.zeros(p.n_theta)
    for lo, hi in zip(edges[:-1], edges[1:]):
        t = n_days(0.5 * (lo + hi), p)
        w, _ = _interval_mass_and_mean(lo, hi, p)
        voice[t] += w
    full = voice.copy()
    full[0] += 2.0            # Exit + Hold, each carrying all of phi_s
    return voice, full


def type_table(p: ParamsV4, ref, voice_mass, full_mass) -> list[dict]:
    return [dict(t=t, Ev=float(ref.Ev[t]), a=float(ref.a[t]),
                 D=float(ref.D[t]), f=(None if not np.isfinite(ref.f[t])
                                       else float(ref.f[t])),
                 m_voice_only=float(voice_mass[t]),
                 m_step9b=float(full_mass[t]))
            for t in range(p.n_theta)]


def alive_row(k: tuple[float, float], p: ParamsV4, ref) -> dict:
    al = atoms(k, p)
    W, Wm, _, _ = _alive_weights(al, 0, p.n_theta, ref)
    W_H, Wm_H, _, _ = _alive_weights(al, p.H, p.n_theta, ref)
    return dict(
        k=[float(x) for x in k],
        W={t: float(W[t]) for t in range(p.n_theta)},
        dead_at_d0=[t for t in range(p.n_theta) if W[t] == 0.0],
        floored_at_d0=[t for t in range(p.n_theta)
                       if W[t] == 0.0 and Wm[t] == OFF_PATH_EPS],
        dead_at_dH=[t for t in range(p.n_theta) if W_H[t] == 0.0],
        floored_at_dH=[t for t in range(p.n_theta)
                       if W_H[t] == 0.0 and Wm_H[t] == OFF_PATH_EPS],
        n_atoms=len(al), n_breakpoints=int(len(breakpoints(k, p))))


def main() -> int:
    out: dict = {"what": "verifier probe 1 -- off-path family structural facts",
                 "date": "2026-08-29",
                 "OFF_PATH_EPS": OFF_PATH_EPS,
                 "breakpoint_merge_tol": 1e-9}

    # ---- calibration (locus 1's node) -------------------------------------
    print("solving seed equilibrium ...", flush=True)
    p_seed = ParamsV4.baseline()
    pol_seed, _ = solve_policy(p_seed)
    tau50 = float(frozen_tau_grid(pol_seed, p_seed, (0.5,))[0])
    print(f"  tau_50 = {tau50!r}", flush=True)
    p_base = p_seed.replace(tau=tau50)
    pol_base, _ = solve_policy(p_base)
    K1 = float(pol_base.k[0])
    print(f"  k* = ({K1!r}, {float(pol_base.k[1])!r})", flush=True)

    p1 = p_base.replace(kappa=0.5, T=5)
    edges1 = n_edges(p1)
    ref1 = type_reference(p1)
    vm1, fm1 = plan_uniform_type_mass(p1)

    out["locus1"] = dict(
        node=dict(kappa=0.5, tau=tau50, T=5, k1_held=K1,
                  kstar=[float(x) for x in pol_base.k],
                  edges={int(m): float(s) for m, s in edges1.items()},
                  n_theta=int(p1.n_theta), H=int(p1.H),
                  params_hash=p1.hash_str()),
        types=type_table(p1, ref1, vm1, fm1))

    print("\nLOCUS 1 type table (kappa=0.5, tau_50, T=5)")
    print(f"{'t':>3} {'Ev':>12} {'D':>4} {'f':>6} {'m_voice':>12} {'m_step9b':>12}")
    for row in out["locus1"]["types"]:
        print(f"{row['t']:3d} {row['Ev']:12.6f} {row['D']:4.0f} "
              f"{('inf' if row['f'] is None else '%.0f' % row['f']):>6} "
              f"{row['m_voice_only']:12.6f} {row['m_step9b']:12.6f}")

    # ---- B: alive weights over the card's ladder --------------------------
    e6 = edges1[6]
    ladder_rows = []
    print("\nLOCUS 1 alive/dead types over the card's k_2 ladder "
          f"(edge(6) = {e6!r})")
    for off in LADDER:
        r = alive_row((K1, e6 + off), p1, ref1)
        r["offset"] = float(off)
        ladder_rows.append(r)
        print(f"  offset {off:+.0e}: dead(d=0) = {r['dead_at_d0']}, "
              f"dead(d=H) = {r['dead_at_dH']}, W[0] = {r['W'][0]:.6f}")
    out["locus1"]["ladder_alive"] = ladder_rows

    # ---- C: where the switch actually fires -------------------------------
    e8 = edges1[8]
    print(f"\nSWITCH LOCATION SWEEP: k_2 -> edge(8) = {e8!r} from below")
    print(f"{'offset below':>14} {'n_bps':>7} {'dying t':>8} {'W[t]':>14} "
          f"{'dead?':>6}")
    sweep = []
    for off in (1e-5, 1e-6, 1e-7, 1e-8, 5e-9, 2e-9, 1.5e-9, 1.1e-9, 1.0e-9,
                9.9e-10, 9e-10, 5e-10, 1e-10, 1e-11, 1e-12):
        k2 = e8 - off
        al = atoms((K1, k2), p1)
        W, Wm, _, _ = _alive_weights(al, 0, p1.n_theta, ref1)
        t = n_days(e8 - 0.5 * off, p1)
        row = dict(offset_below=float(off), k2=float(k2), dying_type=int(t),
                   W_dying=float(W[t]), Wm_dying=float(Wm[t]),
                   dead=bool(W[t] == 0.0),
                   n_breakpoints=int(len(breakpoints((K1, k2), p1))))
        sweep.append(row)
        print(f"{off:14.3e} {row['n_breakpoints']:7d} {t:8d} "
              f"{W[t]:14.6e} {str(row['dead']):>6}")
    out["locus1"]["switch_location_sweep"] = dict(
        edge8=float(e8), rows=sweep,
        note="menu.breakpoints merges at np.diff > 1e-9 (menu.py:244); a "
             "sliver [k_2, edge(8)) narrower than that is merged away and the "
             "type owning it dies BEFORE k_2 reaches the edge.")
    first_dead = next((r for r in sweep if r["dead"]), None)
    last_alive = None
    for r in sweep:
        if not r["dead"]:
            last_alive = r
    out["locus1"]["switch_relocation"] = dict(
        largest_offset_below_edge_at_which_type_is_already_dead=(
            None if first_dead is None else first_dead["offset_below"]),
        smallest_offset_below_edge_at_which_type_is_still_alive=(
            None if last_alive is None else last_alive["offset_below"]),
        card_hedge="MODEL_CARD.md:309-310 'with the switch relocated by "
                   "~1e-9 rather than removed'")

    # ---- locus 2 ----------------------------------------------------------
    p2 = p_base.replace(kappa=0.15, tau=0.05, T=5)
    ref2 = type_reference(p2)
    vm2, fm2 = plan_uniform_type_mass(p2)
    edges2 = n_edges(p2)
    out["locus2"] = dict(
        node=dict(kappa=0.15, tau=0.05, T=5,
                  edges={int(m): float(s) for m, s in edges2.items()},
                  edge_literal=NODE15_EDGE, params_hash=p2.hash_str()),
        types=type_table(p2, ref2, vm2, fm2),
        alive=dict(fp1=alive_row(NODE15_FP1, p2, ref2),
                   fp1_full=alive_row(NODE15_FP1_FULL, p2, ref2),
                   fp2=alive_row(NODE15_FP2, p2, ref2)))
    print("\nLOCUS 2 (kappa=0.15, tau=0.05, T=5) at the pinned fixed points")
    for nm in ("fp1", "fp1_full", "fp2"):
        r = out["locus2"]["alive"][nm]
        print(f"  {nm:9s} k = {r['k']}  dead(d=0) = {r['dead_at_d0']}  "
              f"W[0] = {r['W'][0]:.6f}")

    # ---- the exactness pre-check verdict, as recorded facts ---------------
    dead_i = set()
    for r in ladder_rows:
        dead_i |= set(r["dead_at_d0"]) | set(r["dead_at_dH"])
    dead_ii = set(out["locus2"]["alive"]["fp1"]["dead_at_d0"]) \
        | set(out["locus2"]["alive"]["fp1"]["dead_at_dH"]) \
        | set(out["locus2"]["alive"]["fp2"]["dead_at_d0"]) \
        | set(out["locus2"]["alive"]["fp2"]["dead_at_dH"])
    out["exactness_precheck"] = dict(
        locus1_dead_types=sorted(dead_i),
        locus1_dead_types_D=[float(ref1.D[t]) for t in sorted(dead_i)],
        locus1_dead_types_f=[(None if not np.isfinite(ref1.f[t])
                              else float(ref1.f[t])) for t in sorted(dead_i)],
        locus1_type0_alive_at_every_ladder_point=all(
            r["W"][0] > 0.0 for r in ladder_rows),
        locus2_dead_types=sorted(dead_ii),
        locus2_dead_types_D=[float(ref2.D[t]) for t in sorted(dead_ii)],
        locus2_dead_types_f=[(None if not np.isfinite(ref2.f[t])
                              else float(ref2.f[t])) for t in sorted(dead_ii)],
        locus2_type0_alive=bool(
            out["locus2"]["alive"]["fp1"]["W"][0] > 0.0),
        rule="If every dead type has D = 0 then the flag indicator in "
             "L_j(h|s) is vacuous for it on the pooled cell and "
             "m[t] = Pr(n(s)=t) is EXACTLY Step 9(b)'s Lambda_u weight for "
             "that type (the 1/J cancels).  If type 0 is alive everywhere on "
             "the ladder, the exploration's m[0] = 0 error never enters a "
             "switch-form floor.")
    print("\nEXACTNESS PRE-CHECK")
    print(f"  locus 1 dead types {sorted(dead_i)} have D = "
          f"{out['exactness_precheck']['locus1_dead_types_D']}")
    print(f"  locus 2 dead types {sorted(dead_ii)} have D = "
          f"{out['exactness_precheck']['locus2_dead_types_D']}")
    print(f"  type 0 alive on the whole locus-1 ladder: "
          f"{out['exactness_precheck']['locus1_type0_alive_at_every_ladder_point']}")

    with open(OUT, "w") as fh:
        json.dump(out, fh, indent=1, default=float)
    print(f"\n-> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
