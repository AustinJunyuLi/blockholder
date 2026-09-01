"""A6 continuity failure at the kappa = 0.15 node -- the destroyed crossing and
the fixed point pinned on a cell edge, curated.

WHAT THIS IS.  The second decisive measurement of the 2026-08-27 A6 panel, as
quoted in the card's section 5 A6 evidence note:

    "at (kappa = 0.15, 0.05, 5) jumps reach 0.16 and a diagonal crossing of
     T_2 is destroyed"
    "no such chamber exists at the kappa = 0.15 node, where a fixed point sits
     exactly on the edge k_2 = 1.659062163"

(0.15, 0.05, 5) is one of ticket 34's four sweep-UNRESOLVED nodes
(``t2_p1_fournode_recheck.json``).

SOURCE PROBE (adapted): ``a6_panel_probes_2026-08-27/a6_B_node15.py``, Analyst
B's "probe 5" -- a 60-point k_2 sweep over [1.30, 2.10] with every n(s) cell
edge bracketed at -/+1e-7.  This curation replays the three decisive BRACKETS
rather than the whole sweep: the sweep's other 50 points establish nothing the
card cites, and re-running them would only make the check slower and the JSON
harder to read.  The filed sweep log is
``a6_panel_probes_2026-08-27/a6_B_node15.log``.

Two supporting evaluations are added, both licensing the panel's own reading:

  * k_1-INVARIANCE.  B's sweep holds k_1 = 1.20 fixed and reads a fixed point
    off T_2 alone.  That one-dimensional reduction is licensed by the
    collapse-face measurement (``t2_a6_collapse_face_check.py``): the whole
    pooled price system depends on k through k_2 only.  It is re-verified here
    at this node, at the fixed point's own k_1.
  * THE FULL 2-D FIXED POINT.  T is evaluated at (1.020221781, 1.659062163) to
    confirm that the edge-pinned k_2 really is a fixed point of the full map,
    not an artifact of the sweep's held k_1.

WHAT "PASS" MEANS HERE.  Inverted, as in ``t2_a6_edge_jump_check.py``:
``pass: true`` means the panel's measurement REPRODUCED -- the jump is there at
the quoted size, the crossing really is destroyed, the fixed point really does
sit on the edge.  It does NOT mean A6 holds, and it licenses NO label move.
A6 is a listed hypothesis of P1; this is applicability evidence on its
antecedent at the implemented calibration, in the A(tau) pattern.  P1 stays
PROVED as a conditional.  Nonexistence is neither claimed nor shown anywhere in
this file: two fixed points survive at this node.

WHAT A "DESTROYED CROSSING" IS, precisely.  Write gap(k_2) = T_2(k_2) - k_2, so
a fixed point of the reduced map is a zero of gap.  Approaching the edge
S = 1.583333333333 from below, gap stays strictly POSITIVE and falls to +1.0e-07
at S - 1e-7; at k_2 = S the map jumps, T_2 falls to 1.5163, and gap lands at
-6.7e-2.  The sign change therefore happens ACROSS the discontinuity, with no
k_2 at which gap = 0.  That is the destroyed crossing, and it is what the gate
below asserts: gap > 0 at every approach point, gap < 0 at S, and a gap jump
five orders of magnitude larger than the 1e-7 step in k_2 that produced it.

A MECHANISM NOTE, RECORDED BUT NOT GATED.  Immediately below the edge T_2 is
*pinned* at S itself -- it is the infimum of a signal set whose boundary sits at
a jump point of U_HOLD - U_VOICE in s -- so there gap(k_2) = S - k_2 exactly.
This holds within ~1e-5 of the edge (residual ~1e-12) but NOT uniformly over the
approach: at S - 1e-3 the map is on a different branch, T_2 = 1.6464, and gap is
+6.4e-2.  The pinning ladder is recorded in the JSON as measured; it is not
gated, because neither the panel nor the card claims pinning over the whole
approach, and the destroyed-crossing reading does not need it -- gap is positive
at every approach point either way, so there is no zero on [S - 1e-2, S).

GATES.  Fixed from the filed sweep log before this script was first run, with
ONE exception, declared here rather than left for a reader to notice: the
``destroyed_crossing`` gate originally also required T_2 to be pinned at S over
the whole approach, which missed on the first run (at S - 1e-3 the map sits on a
different branch).  That sub-gate was an invention of this curation -- neither
the panel nor the card claims pinning over the approach -- so it was dropped and
replaced by the stronger and more directly relevant requirement that gap be
positive at EVERY approach point, which is what "no zero in between" actually
needs.  The pinning measurement is retained ungated, including the row that
misses.  No tolerance was widened.

  jump_reaches_0p16    |T_2 jump| at edge 1.749268649 is >= 0.16, and matches
                       the filed 0.1647 to a relative 5e-4
  destroyed_crossing   gap > 0 at every approach point, gap(S) < 0, the two
                       filed values (+1.000e-07 / -6.703e-02) matched to a
                       relative 5e-4, and |gap jump| / step >= 1e5
  fixed_point_on_edge  |T_2(1.659062163) - 1.659062163| <= 1e-9, and T_2 flat
                       across the edge bracket to 1e-9
  k1_invariance        T at k_1 = 1.20 equals T at k_1 = 1.020221781 to 1e-12
  full_2d_fixed_point  |T(k) - k|_inf <= 1e-8 at (1.020221781, 1.659062163)

NOT CURATED HERE: the argmax reversal across the edge and the empty
weakly-increasing selection at this node (``a6_B_argmax.py``,
``a6_B_findings.md`` section 4f), and the payoff-residual reconciliation with
ticket 34 (``a6_B_resid.py``, ``a6_B_alt.py``).  Both belong to the A3 locus,
which the card files as a SEPARATE evidence note with its own follow-up.

COROLLARY, argued not measured (so recorded, not gated): a fixed point sitting
ON a cell edge cannot lie in the interior of any chamber, since the chambers are
by construction the open intervals between consecutive edges.  That is the
card's "no such chamber exists at the kappa = 0.15 node".

RUN:  ``.venv/bin/python numerical_v4/checks/t2_a6_node15_check.py`` from the
      repo root.  Deterministic; read-only on ``numerical_v4/``.  Writes
      ``t2_a6_node15_check.json`` beside itself.
"""

from __future__ import annotations

import json
import os
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO not in sys.path:
    sys.path.insert(0, REPO)

from numerical_v4.params import ParamsV4  # noqa: E402
from numerical_v4.menu import atoms, _sigmoid_inv  # noqa: E402
from numerical_v4.pooled import pooled_pass  # noqa: E402
from numerical_v4.solver import outer_map  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "t2_a6_node15_check.json")

NODE = dict(kappa=0.15, tau=0.05, T=5)
K1_SWEEP = 1.20                 # a6_B_node15.py's held k_1
BRACKET = 1e-7                  # a6_B_node15.py's edge bracket

# The three decisive edges, named by the LITERALS the card and the sweep log
# print (which are rounded displays).  The script locates each one in the exact
# n(s) edge set and works with the exact value -- the card's "the edge
# k_2 = 1.659062163" is a 9-dp display of 1.6590621627456204, and testing a
# fixed point that sits ON an edge against the rounded literal would report a
# spurious 2.5e-10 residual.
EDGE_JUMP_LIT = 1.749268649265      # "jumps reach 0.16"
EDGE_CROSS_LIT = 1.583333333333     # "a diagonal crossing of T_2 is destroyed"
EDGE_FP_LIT = 1.659062163           # "a fixed point sits exactly on the edge"

FILED = {
    "jump_T2_below": 1.675112972,
    "jump_T2_at": 1.510436155,
    "jump": abs(1.510436155 - 1.675112972),        # 0.164676817
    "cross_gap_below": 1.000e-07,
    "cross_gap_at": -6.703e-02,
    "cross_T2_at": 1.516301532,
    "fp_gap_at_edge": 1.064e-12,
    "fp_T1_at_edge": 1.020221781,
}

TOL_REL = 5e-4                  # relative agreement with the filed sweep value
TOL_JUMP_FLOOR = 0.16           # the card's "jumps reach 0.16"
TOL_FP = 1e-9                   # fixed point sits ON the edge
TOL_FLAT = 1e-9                 # T_2 flat across the edge bracket
TOL_K1_INV = 1e-12              # k_1-invariance of T at this node
TOL_2D = 1e-8                   # full 2-D fixed-point residual

results: dict = {"kind": "A6 applicability evidence (panel-probe curation)",
                 "checks": [], "n_fail": 0}


def record(name: str, ok: bool, kind: str, detail: dict) -> None:
    results["checks"].append({"name": name, "kind": kind, "pass": bool(ok),
                              **detail})
    if not ok:
        results["n_fail"] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def rel(a: float, b: float) -> float:
    m = 0.5 * (abs(a) + abs(b))
    return 0.0 if m == 0.0 else abs(a - b) / m


def T_at(k1: float, k2: float, p: ParamsV4) -> tuple[float, float]:
    res = pooled_pass(atoms((k1, k2), p), p, with_runup=True)
    T = outer_map((k1, k2), p, res)
    return float(T[0]), float(T[1])


def main() -> int:
    t_run = time.perf_counter()
    p = ParamsV4.baseline().replace(**NODE)

    # the n(s) cell edges, built exactly as menu.type_reference builds them
    edges = {}
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            s = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo < s < p.s_hi:
                edges[m] = s

    def exact(lit: float) -> float:
        """The exact n(s) edge the card's rounded literal names."""
        e = min(edges.values(), key=lambda s: abs(s - lit))
        assert abs(e - lit) < 1e-8, (lit, e)
        return float(e)

    EDGE_JUMP, EDGE_CROSS, EDGE_FP = (exact(EDGE_JUMP_LIT),
                                      exact(EDGE_CROSS_LIT),
                                      exact(EDGE_FP_LIT))
    results["node"] = dict(**{k: float(v) if k != "T" else int(v)
                              for k, v in NODE.items()},
                           k1_swept_at=K1_SWEEP, params_hash=p.hash_str(),
                           n_edges={int(m): float(s) for m, s in edges.items()},
                           edges_used={"jump": EDGE_JUMP, "crossing": EDGE_CROSS,
                                       "fixed_point": EDGE_FP},
                           card_literals={"jump": EDGE_JUMP_LIT,
                                          "crossing": EDGE_CROSS_LIT,
                                          "fixed_point": EDGE_FP_LIT},
                           literal_offsets={"jump": EDGE_JUMP - EDGE_JUMP_LIT,
                                            "crossing": EDGE_CROSS - EDGE_CROSS_LIT,
                                            "fixed_point": EDGE_FP - EDGE_FP_LIT},
                           ticket_34_status="one of the four sweep-UNRESOLVED "
                                            "nodes (t2_p1_fournode_recheck.json)")

    # -- (1) the jump reaches 0.16 -------------------------------------------
    T1_lo, T2_lo = T_at(K1_SWEEP, EDGE_JUMP - BRACKET, p)
    T1_at, T2_at = T_at(K1_SWEEP, EDGE_JUMP, p)
    T1_hi, T2_hi = T_at(K1_SWEEP, EDGE_JUMP + BRACKET, p)
    jump = abs(T2_at - T2_lo)
    record("a6_node15_jump_reaches_0p16",
           jump >= TOL_JUMP_FLOOR and rel(jump, FILED["jump"]) <= TOL_REL,
           "substantive",
           dict(edge=EDGE_JUMP, bracket=BRACKET,
                T2_below=T2_lo, T2_at_edge=T2_at, T2_above=T2_hi,
                jump=jump, jump_floor=TOL_JUMP_FLOOR,
                panel_filed=FILED["jump"],
                panel_filed_T2_below=FILED["jump_T2_below"],
                panel_filed_T2_at=FILED["jump_T2_at"],
                panel_rel_diff=rel(jump, FILED["jump"]), tol_rel=TOL_REL,
                T1_below=T1_lo, T1_at_edge=T1_at,
                T1_move=abs(T1_at - T1_lo),
                right_continuity=abs(T2_hi - T2_at),
                note="T_2 falls by 0.165 across a 1e-7 step in k_2; the value "
                     "at the edge and just above it agree, so the map is "
                     "right-continuous there and the jump is the left limit "
                     "failing to meet it"))

    # -- (2) the destroyed diagonal crossing ---------------------------------
    approach = []
    for d in (1e-2, 1e-3, 1e-5, BRACKET):
        _, T2 = T_at(K1_SWEEP, EDGE_CROSS - d, p)
        approach.append(dict(k2=EDGE_CROSS - d, T2=T2,
                             gap=T2 - (EDGE_CROSS - d),
                             T2_pinned_at_edge=abs(T2 - EDGE_CROSS)))
    T1_c, T2_c = T_at(K1_SWEEP, EDGE_CROSS, p)
    gap_below = approach[-1]["gap"]
    gap_at = T2_c - EDGE_CROSS
    all_positive = all(r["gap"] > 0.0 for r in approach)
    pinned_near = max(r["T2_pinned_at_edge"] for r in approach if r["gap"] < 1e-4)
    record("a6_node15_destroyed_diagonal_crossing",
           all_positive and gap_at < 0.0
           and rel(gap_below, FILED["cross_gap_below"]) <= TOL_REL
           and rel(gap_at, FILED["cross_gap_at"]) <= TOL_REL
           and abs(gap_at - gap_below) / BRACKET >= 1e5,
           "substantive",
           dict(edge=EDGE_CROSS, bracket=BRACKET,
                gap_below=gap_below, gap_at_edge=gap_at,
                gap_jump=abs(gap_at - gap_below),
                step_in_k2=BRACKET,
                jump_over_step=abs(gap_at - gap_below) / BRACKET,
                T2_at_edge=T2_c, T1_at_edge=T1_c,
                panel_filed_gap_below=FILED["cross_gap_below"],
                panel_filed_gap_at=FILED["cross_gap_at"],
                panel_filed_T2_at=FILED["cross_T2_at"],
                rel_gap_below=rel(gap_below, FILED["cross_gap_below"]),
                rel_gap_at=rel(gap_at, FILED["cross_gap_at"]),
                tol_rel=TOL_REL,
                gap_positive_at_every_approach_point=all_positive,
                approach=approach,
                pinning_residual_within_1e5_of_edge=pinned_near,
                pinning_note="NOT GATED. T_2 is pinned at the edge value S "
                             "within ~1e-5 of it (residual ~1e-12), but not "
                             "uniformly over the approach: at S - 1e-3 the map "
                             "sits on a different branch, T_2 = 1.6464, gap "
                             "+6.4e-2. Neither the panel nor the card claims "
                             "pinning over the whole approach, and the "
                             "destroyed-crossing reading does not need it.",
                reading="gap is strictly POSITIVE at every approach point and "
                        "falls to +1.0e-07 at S - 1e-7; at k_2 = S the map "
                        "jumps and gap lands at -6.7e-2. The sign change "
                        "happens ACROSS the discontinuity: there is no k_2 in "
                        "[S - 1e-2, S] at which gap = 0. That is the destroyed "
                        "crossing."))

    # -- (3) the fixed point pinned on the edge ------------------------------
    T1_f_lo, T2_f_lo = T_at(K1_SWEEP, EDGE_FP - BRACKET, p)
    T1_f, T2_f = T_at(K1_SWEEP, EDGE_FP, p)
    T1_f_hi, T2_f_hi = T_at(K1_SWEEP, EDGE_FP + BRACKET, p)
    fp_gap = T2_f - EDGE_FP
    flat = max(abs(T2_f_lo - T2_f), abs(T2_f_hi - T2_f))
    record("a6_node15_fixed_point_on_edge",
           abs(fp_gap) <= TOL_FP and flat <= TOL_FLAT, "substantive",
           dict(edge=EDGE_FP, bracket=BRACKET,
                T2_at_edge=T2_f, fixed_point_residual=fp_gap, tol=TOL_FP,
                panel_filed_gap=FILED["fp_gap_at_edge"],
                T2_below=T2_f_lo, T2_above=T2_f_hi,
                local_flatness=flat, tol_flat=TOL_FLAT,
                T1_at_edge=T1_f, panel_filed_T1=FILED["fp_T1_at_edge"],
                T1_abs_diff=abs(T1_f - FILED["fp_T1_at_edge"]),
                note="T_2 is locally CONSTANT at the edge value across the "
                     "whole bracket -- it is pinned at a jump point of "
                     "U_HOLD - U_VOICE in s -- so the diagonal is met exactly "
                     "on the discontinuity hyperplane",
                chamber_corollary="argued, not measured: a fixed point ON a "
                                  "cell edge cannot be interior to any "
                                  "chamber, the chambers being by construction "
                                  "the open intervals between consecutive "
                                  "edges. This is the card's 'no such chamber "
                                  "exists at the kappa = 0.15 node'."))

    # -- (4) k_1-invariance, which licenses the 1-D reading ------------------
    T1_a, T2_a = T_at(K1_SWEEP, EDGE_FP, p)
    T1_b, T2_b = T_at(FILED["fp_T1_at_edge"], EDGE_FP, p)
    dT = max(abs(T1_a - T1_b), abs(T2_a - T2_b))
    record("a6_node15_k1_invariance_licenses_1d_reduction",
           dT <= TOL_K1_INV, "substantive",
           dict(k2=EDGE_FP, k1_a=K1_SWEEP, k1_b=FILED["fp_T1_at_edge"],
                T_at_k1_a=[T1_a, T2_a], T_at_k1_b=[T1_b, T2_b],
                max_abs_diff=dT, tol=TOL_K1_INV,
                note="B's sweep holds k_1 = 1.20 and reads a fixed point off "
                     "T_2 alone; T is invariant in k_1 at this node too, so "
                     "the 1-D reading is licensed (the general statement is "
                     "t2_a6_collapse_face_check.py)"))

    # -- (5) the full 2-D fixed point ----------------------------------------
    kfp = (FILED["fp_T1_at_edge"], EDGE_FP)
    T1_2d, T2_2d = T_at(kfp[0], kfp[1], p)
    resid = max(abs(T1_2d - kfp[0]), abs(T2_2d - kfp[1]))
    record("a6_node15_full_2d_fixed_point", resid <= TOL_2D, "substantive",
           dict(k=list(kfp), T=[T1_2d, T2_2d], cutoff_residual_inf=resid,
                tol=TOL_2D,
                note="the edge-pinned k_2 is a fixed point of the FULL map, "
                     "not an artifact of the sweep's held k_1"))

    # -- aggregate -----------------------------------------------------------
    results["seconds"] = time.perf_counter() - t_run
    results["all_pass"] = results["n_fail"] == 0
    results["summary"] = dict(
        jump_at_1p749268649=jump,
        destroyed_crossing_gap_below=gap_below,
        destroyed_crossing_gap_at_edge=gap_at,
        fixed_point_residual_on_edge=fp_gap,
        full_2d_cutoff_residual=resid,
    )
    results["verdict"] = (
        "A6 continuity failure REPRODUCED at calibration"
        if results["all_pass"] else
        f"A6 kappa=0.15 measurement PARTIALLY REPRODUCED "
        f"({results['n_fail']} gate(s) missed)"
    ) + (
        f" -- at (kappa=0.15, tau=0.05, T=5) the outer map's T_2 jumps by "
        f"{jump:.4f} across a {BRACKET:g} step in k_2 at the cell edge "
        f"{EDGE_JUMP:.9f}; the diagonal crossing at {EDGE_CROSS:.9f} is "
        f"DESTROYED (gap {gap_below:+.3e} just below the edge, {gap_at:+.3e} at "
        f"it, with no zero in between); and a fixed point sits exactly ON the "
        f"edge k_2 = {EDGE_FP:.9f} (residual {fp_gap:.3e}), which no "
        f"chamber-interior Theta can contain. NONEXISTENCE IS NEITHER CLAIMED "
        f"NOR SHOWN -- a discontinuous self-map may still have fixed points, "
        f"and two survive at this node. NO LABEL MOVES AND NONE IS LICENSED: "
        f"A6 is a listed hypothesis of P1, so this is applicability evidence "
        f"on its antecedent, in the A(tau) pattern -- P1 stays PROVED as a "
        f"conditional."
    )
    results["provenance"] = {
        "follow_up": "numerical_v4/checks/a6_panel_probes_2026-08-27/"
                     "README.md -- the standing curation follow-up",
        "source_probe": "a6_panel_probes_2026-08-27/a6_B_node15.py "
                        "(Analyst B, probe 5) and its filed log "
                        "a6_B_node15.log",
        "scope_note": "the three decisive BRACKETS are replayed, not the "
                      "60-point sweep: the remaining sweep points establish "
                      "nothing the card cites",
        "card_row": "research/model_v4/MODEL_CARD.md section 5, A6 evidence "
                    "note (stamp 2026-08-27, commit ae9caea)",
        "panel_reports": [
            "research/model_v4/threads/2026-08-27_A6_panel_substantiate.md",
            "research/model_v4/threads/2026-08-27_A6_panel_defuse.md",
        ],
        "verdict_semantics": (
            "INVERTED relative to a proof check. pass = the panel's "
            "measurement REPRODUCED. pass does NOT mean A6 holds; this file "
            "is applicability evidence and licenses no label move."
        ),
        "environment_gate": ".venv/bin/python -m numerical_v4.smoke, exit 0",
        "does_not": [
            "touch MODEL_CARD.md, the mirrors, sections_v3/ or anything under "
            "research/",
            "modify anything under numerical_v4/ (imported read-only)",
            "curate the A3 material at this node (argmax reversal, empty "
            "weakly-increasing selection, ticket-34 residual reconciliation) "
            "-- a separate follow-up owns the A3 locus",
            "claim or deny nonexistence of equilibrium at this node",
        ],
    }

    tmp = OUT + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(results, fh, indent=2, default=float)
    os.replace(tmp, OUT)

    print(f"\n{results['verdict']}", flush=True)
    print(f"({len(results['checks'])} checks, {results['n_fail']} failing, "
          f"{results['seconds']:.0f} s)  ->  {OUT}", flush=True)
    return 0 if results["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
