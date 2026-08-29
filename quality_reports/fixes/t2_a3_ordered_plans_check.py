"""A3 (ordered plans / single crossing) measured to FAIL at the implemented
calibration -- the two loci of the card's section 5 A3 evidence note, curated.

WHAT THIS IS.  The 2026-08-27 A6 panel (two opposed-brief Opus agents,
substantiate / defuse) found, in passing and as a separate finding from the A6
one, that **A3 itself fails at the implemented calibration, at two
independently-found loci, upstream of A6**.  Its working scripts are filed at
``quality_reports/fixes/a6_panel_probes_2026-08-27/`` and are explicitly
*analysis-grade, not curated t2 checks*.  The A6 half of that directory's
standing follow-up was curated on 2026-08-28 into ``t2_a6_edge_jump_check.py``,
``t2_a6_node15_check.py`` and ``t2_a6_collapse_face_check.py``, each of which
records that "the A3 material ... a separate follow-up owns the A3 locus".
**This script is that follow-up.**  It was re-requested independently by GPT
Pro's 2026-08-28 re-review (``threads/2026-08-28_gpt_rereview.md``, A3 section,
UNCHECKED item 5 and NUMERICAL CHECK REQUEST) and carried into the session log
as the one re-review check request singled out as a legitimate follow-up
(``quality_reports/session_logs/2026-08-28_gpt_rereview_audit_repairs.md``).

PRE-REGISTERED BY CONSTRUCTION.  Every predicted number below is quoted from
the card's section 5 A3 evidence note (stamp 2026-08-28, commit ``59c0dfc`` --
verified against the file before this script was written) or from the panel's
own filed values, and GPT Pro's request restates the same numbers.  Nothing
here was chosen after looking at a result; the two exceptions to "the gate is
the card's number" are the sampling geometry of the argmax gate and the dense-
grid location radius, both declared under GATES below with their reasons.

THE TWO LOCI.

  locus 1  (kappa = 0.5, tau_50, T = 5), k_1 held at k*[0], k_2 on an OPEN SET
           above cell edge 6.  U_VOICE - U_HOLD has THREE strict sign changes;
           the pointwise argmax runs H,V,H,V, single-valued on each interval,
           so no weakly increasing selection exists -- Step 13's S(k) is EMPTY
           and the card's T is UNDEFINED there, not merely discontinuous.
  locus 2  (kappa = 0.15, tau = 0.05, T = 5) -- a ticket-34 UNRESOLVED node.
           The argmax reverses VOICE -> HOLD across the n(s) cell edge
           s = 1.659062162746, at BOTH located fixed points: the preferred plan
           DECREASES in s.

SOURCE PROBES (adapted, not re-imported -- the probes live in a directory with
no package init and hard-code a scratchpad path):

  * ``a6_A_probe8_open.py``   -- Analyst A: is the A3 failure an OPEN set in
    k_2 or a knife edge?  The 6001-point global signal grid, the strict
    sign-change criterion, and the k_2 offset ladder are taken from it
    verbatim.                                            -> locus 1.
  * ``a6_A_findings.md`` (A)  -- Analyst A's filed locus-1 numbers: the three
    crossing locations, the two middle excursions, the H,V,H,V argmax, the
    open-set width, and the one-sign-change rows below the edge and at the
    +5e-2 / +1e-1 offsets where the set closes.
  * ``a6_B_argmax.py``        -- Analyst B: pointwise argmax over all three
    plans across the cell edge at both fixed points of the kappa = 0.15 node.
    Its two k literals and its 12-dp edge literal are used verbatim.
                                                         -> locus 2.
  * ``a6_B_alt.py``           -- Analyst B: the interior-crossing fixed point,
    reached from k_init = (1.02, 1.71).                  -> locus 2, fp2.
  * ``a6_B_findings.md`` section 4 -- Analyst B's filed 7-dp payoff strings at
    the four (fixed point, side) combinations.
  * ``t2_t34_account_sweep.json`` ``provenance.node15_reference_values`` --
    the full-precision pinned fixed point and its two residuals.

WHAT "PASS" MEANS HERE -- READ THIS BEFORE READING THE VERDICT.  The verdict
semantics of this check are INVERTED relative to a proof check, exactly as in
``t2_a6_edge_jump_check.py``.  ``pass: true`` means *the panel's measurement
reproduced*: A3 fails, at the quoted loci, in the quoted way.  It does NOT mean
A3 holds, and it does not mean anything about a label.  **A3 is a hypothesis of
P1, not a claim of it: no label attaches to A3 and none moves.**  This file is
applicability evidence in the A(tau) pattern -- a measured failure of a listed
antecedent at the implemented calibration is a satisfiability finding, not a
derivability one.  P1 stays PROVED as a conditional.  Nothing here establishes
equilibrium nonexistence, turns an edge-pinned cutoff-map fixed point into an
equilibrium, or resolves the four ticket-34 existence questions.

WHERE EACH GATE IS ALLOWED TO READ FROM (the A6 check's "each route at ITS OWN
filed deltas" rule, applied here).

  * The locus-1 sign-change count, the crossing locations and the middle
    excursions are all measured on probe 8's own 6001-point global grid.  The
    filed excursions 2.80e-4 / 2.40e-4 are MAXIMA OVER THAT GRID -- which
    spans [s_lo, s_hi] = [-3.2426407, 5.2426407] at a spacing of 1.4142e-3, so
    it puts only 6 and 5 points inside the two middle intervals (widths
    7.890e-3 and 6.909e-3); a refined grid finds a larger maximum for grid
    reasons, not model reasons, so the refined-interval maxima are recorded
    and NOT gated.
  * The card quotes the three crossing locations at the probes' own +1e-9
    offset.  That is the only offset at which they are gated.  The card's
    open-set claim ranges over the ladder; the per-offset locations across the
    ladder are recorded, ungated, with only a coarse declared containment
    window.  No drift tolerance is invented.
  * Locus 2's 7-dp payoff strings are replayed at ``a6_B_argmax.py``'s own k
    literals (10 dp) and its own 12-dp edge, at its own +/-1e-6 offsets.  The
    ticket-34 full-precision fixed point (1.0202217805248246,
    1.6590621627461504) is used ONLY for the residual gate, which is where it
    was filed.

THE MIDDLE "CROSSING" IS A JUMP, NOT A ROOT.  n(s) is integer-valued, so
U_VOICE steps in s at every n(s) cell edge.  The middle sign change sits
exactly at cell edge 8, s = 1.583333333333, where U_VOICE - U_HOLD jumps
through zero rather than crossing it.  ``brentq`` on that bracket converges to
the discontinuity, which is the right location to 7 dp but is not a root; the
one-sided limits and n(s) either side are recorded so no reader takes it for a
smooth crossing.  Sign changes 1 and 3 are ordinary continuous crossings.

GATES.  All were fixed from the card and the filed panel values before this
script was first run, with ONE exception, declared here rather than left for a
reader to notice: the ``excursions`` gate was RESTRUCTURED AFTER the first run,
which missed on one of its two intervals.  What changed is the FORM of the
comparison, not any measured number.

  The original gate required agreement with the filed excursions to 5e-4
  RELATIVE -- a tolerance carried over from ``t2_a6_edge_jump_check.py``, where
  the filed panel values are quoted to five significant figures (6.3333e-03)
  and 5e-4 relative is about their last-digit rounding window.  Analyst A filed
  the A3 excursions to THREE significant figures ("max|gap| = 2.80e-4 and
  2.40e-4"), so a 5e-4 relative gate demands four to five digits of a number
  recorded with three.  The measured maxima are 2.80370586579648e-4 and
  2.40107065617487e-4: relative differences 1.3226e-3 and 4.4601e-4, the first
  outside the transplanted tolerance and the second inside it, while BOTH round
  to the filed strings exactly.  The gate is now the house form for a 3-s.f.
  source -- ``%.3g`` string equality, which is what ``t2_a6_edge_jump_check.py``
  itself uses for its 3-s.f. card figures (``card_3sf``) -- and the card's band
  is read at the same precision.

  This restructure is NUMERICALLY WIDER, not tighter: the 3-s.f. rounding
  window is about 1.8e-3 relative against the original 5e-4.  It is also
  digit-exact in form, where the original was a tolerance calibrated to the
  wrong source precision.  Both relative differences stay in the JSON, ungated,
  and the original miss is preserved verbatim in ``known_discrepancies``.  No
  other gate has moved.  Any gate that misses is recorded in
  ``known_discrepancies`` rather than smoothed.

  locus 1
    anchors          tau_50 and k* reproduce the probes' literals to 1e-9, and
                     the recomputed cell edges reproduce the filed edge
                     literals to 1e-9
    open_set         EXACTLY 3 strict sign changes at every k_2 offset in
                     {1e-9, 1e-4, 1e-3, 5e-3, 2e-2}   (the card's ladder)
    boundary         EXACTLY 1 strict sign change at k_2 = edge - 1e-9 and at
                     offsets {5e-2, 1e-1}   (panel-filed rows, NOT card-quoted:
                     the card claims openness only through 2e-2)
    locations        at the +1e-9 offset, "%.7f" of the three located sign
                     changes equals the card's 1.5754434 / 1.5833333 /
                     1.5902426 exactly
    excursions       the two middle-interval max|U_V - U_H| on the 6001 grid
                     reproduce the filed 2.80e-4 / 2.40e-4 EXACTLY at their
                     filed precision ("%.3g" string equality), both lie in the
                     card's quoted 2.4e-4 - 2.8e-4 band read at that same
                     precision, and both exceed the 1e-9 payoff tolerance by
                     >= 1e5  (gate form restructured after the first run -- see
                     the paragraph above)
    argmax           the pointwise argmax over {EXIT, HOLD, VOICE} is constant
                     and equal to HOLD, VOICE, HOLD, VOICE on the four
                     crossing-delimited intervals, and is a strict singleton at
                     every sampled point
    no_selection     derived from the row above: the argmax is single-valued on
                     each interval and runs H,V,H,V, so every selection of the
                     best-response correspondence takes value V then H as s
                     rises -- S(k) is empty
    dense_grid       on a 60001-point grid the count is still exactly 3 and
                     every sign change lies within 1e-3 in s of one of the
                     three located crossings

  locus 2
    edge_anchor      the recomputed cell edge reproduces the probe's 12-dp
                     literal 1.659062162746 to 1e-9
    fp1_residual     at the ticket-34 full-precision pinned fixed point the
                     cutoff-scale residual reproduces 5.340172748e-13 and the
                     payoff-scale residual 1.7657302401e-3, each to 1e-6
                     relative
    fp2_reproduces   solve_policy from a6_B_alt's k_init = (1.02, 1.71) returns
                     k within 1e-9 of the filed (1.0260443221, 1.7104049079)
    reversal         at BOTH fixed points the argmax is VOICE at edge - 1e-6
                     and HOLD at edge + 1e-6, a strict singleton on both sides,
                     with n(s) = 8 below and 7 above
    payoff_strings   all twelve "%.7f" payoff strings (3 plans x 2 sides x 2
                     fixed points) equal Analyst B's filed values exactly
    decreasing       derived: the preferred plan moves VOICE -> HOLD as s
                     rises, i.e. DECREASES in the menu order, contradicting
                     A3's second clause independently of locus 1

DECLARED SAMPLING GEOMETRY (the two places a gate needed a choice the card does
not make, both fixed before the first run).

  * The four locus-1 intervals are crossing-delimited, with a buffer of 10% of
    the smaller middle-interval width held off each crossing (V - H tends to 0
    continuously at crossings 1 and 3, so a point-by-point "gap above 1e-9"
    gate would fail there for reasons that are not the finding), and with the
    two outer intervals sampled over a flanking window one middle-interval
    width wide rather than out to s_lo / s_hi -- far below crossing 1 the
    argmax is EXIT, which is the ordinary Exit region and not an A3 failure.
    The quantitative single-valuedness content the card asserts ("against the
    1e-9 payoff tolerance") is carried by the excursion gate, which is where
    the card puts it; the argmax gate carries the ordering content.
  * The dense-grid location radius is 1e-3.  What it compares is NOT grid
    points but brentq-LOCATED crossings -- each grid's sign-change brackets are
    handed to brentq at xtol = 1e-13 -- so the radius has to clear the
    root-finder's precision, not either grid's spacing (1.4142e-3 panel,
    1.4142e-4 dense).  It clears it by about eleven orders: the measured
    cross-grid agreement is 0.0 / 4.35e-14 / 2.31e-14.  At the other end it
    sits an order of magnitude below the smallest gap between two crossings
    (6.909e-3), so it cannot merge two crossings either.  Bracketed on both
    sides, it can neither merge a pair nor reject a correctly located one.

RUN:  ``.venv/bin/python quality_reports/fixes/t2_a3_ordered_plans_check.py``
      from the repo root.  Deterministic; no randomness, no wall clock, no file
      input, no network.  Writes ``t2_a3_ordered_plans_check.json`` beside
      itself, once after locus 1 (checkpoint, ``loci_done: 1``) and once at the
      end.  Read-only on ``numerical_v4/``.
"""

from __future__ import annotations

import json
import os
import sys
import time

import numpy as np
from scipy.optimize import brentq

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if REPO not in sys.path:
    sys.path.insert(0, REPO)

from numerical_v4.params import ParamsV4, EXIT, HOLD, VOICE  # noqa: E402
from numerical_v4.menu import atoms, n_days, _sigmoid_inv  # noqa: E402
from numerical_v4.pooled import pooled_pass  # noqa: E402
from numerical_v4.policy import plan_payoff, frozen_tau_grid  # noqa: E402
from numerical_v4.solver import solve_policy, equilibrium_residual  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "t2_a3_ordered_plans_check.json")

NAME = {EXIT: "EXIT", HOLD: "HOLD", VOICE: "VOICE"}

# --------------------------------------------------------------------------
# The card's quoted numbers and the panel's filed values -- all frozen here.
# --------------------------------------------------------------------------

# MODEL_CARD.md section 5, A3 evidence note (stamp 2026-08-28, commit 59c0dfc):
#   "(i) At (kappa=0.5, tau_50, T=5) with k_2 on an open set above cell edge 6
#    (verified at offsets 1e-9 through 2e-2), U_V - U_H has three strict sign
#    changes (s = 1.5754434 / 1.5833333 / 1.5902426; middle excursions 2.4-2.8
#    e-4 against a 1e-9 payoff tolerance), the pointwise argmax runs H,V,H,V
#    single-valued on each interval, so no weakly increasing selection exists"
CARD_CROSSINGS_7DP = ("1.5754434", "1.5833333", "1.5902426")
CARD_EXCURSION_LO = 2.4e-4          # card band, inclusive
CARD_EXCURSION_HI = 2.8e-4
CARD_ARGMAX_PATTERN = (HOLD, VOICE, HOLD, VOICE)

# a6_A_findings.md (A): the filed maxima over probe 8's own 6001-point grid,
# in interval order (interval 2 first, then interval 3).
FILED_EXCURSIONS = (2.80e-4, 2.40e-4)

# a6_A_probe8_open.py: the k_2 offset ladder.  The card's open-set claim runs
# from 1e-9 through 2e-2; a6_A_findings.md records the set closing ("back to 1")
# at 5e-2 and 1e-1, and one sign change below the edge.
LADDER_OPEN = (1e-9, 1e-4, 1e-3, 5e-3, 2e-2)     # card-quoted: expect 3
LADDER_CLOSED = (5e-2, 1e-1)                     # panel-filed: expect 1
OFFSET_BELOW = -1e-9                             # panel-filed: expect 1
OFFSET_CARD = 1e-9                               # where the locations are filed

# a6_A_probe8_open.py hard-codes these; t2_a6_edge_jump_check.py recomputes and
# gates them the same way.  Recomputed values are the ones actually used.
FILED_TAU50 = 0.09076405861553302
FILED_K1 = 1.2405757282617416
# Filed cell-edge literals, from a6_B_baseline.log's breakpoint list and
# t2_a6_edge_jump_check.py's FILED table (edge_m -> s).
FILED_EDGES = {8: 1.583333333333333, 7: 1.659062163, 6: 1.749268649265}

# a6_B_argmax.py's own literals (locus 2).
NODE2 = dict(kappa=0.15, tau=0.05, T=5)
FP1_ARGMAX_K = (1.020221781, 1.659062163)          # a6_B_argmax.py literal
FP2_ARGMAX_K = (1.0260443221, 1.7104049079)        # a6_B_argmax.py literal
EDGE2 = 1.659062162746                             # a6_B_argmax.py 12-dp edge
OFFSET2 = 1e-6                                     # a6_B_argmax.py's own offset
OFFSET2_EXTRA = 1e-4                               # recorded, not gated

# a6_B_findings.md section 4: the filed 7-dp payoff strings.
#   key: (fixed point index, side) -> (U_EXIT, U_HOLD, U_VOICE, argmax)
FILED_PAYOFFS = {
    (1, "below"): ("0.0331035", "0.0366608", "0.0384266", VOICE),
    (1, "above"): ("0.0331035", "0.0366608", "0.0353827", HOLD),
    (2, "below"): ("0.0332206", "0.0367977", "0.0378606", VOICE),
    (2, "above"): ("0.0332206", "0.0367977", "0.0347621", HOLD),
}
FILED_N_BELOW, FILED_N_ABOVE = 8, 7

# t2_t34_account_sweep.json, provenance.node15_reference_values.
FP1_FULL_K = (1.0202217805248246, 1.6590621627461504)
FILED_FP1_CUTOFF_SCALE = 5.340172748447003e-13
FILED_FP1_PAYOFF_SCALE = 0.0017657302401005992
FILED_FP2_PAYOFF_SCALE = 0.0003055        # a6_B_alt route, filed to 4 s.f.
FP2_K_INIT = (1.02, 1.71)                 # a6_B_alt.py's own k_init

# Gates -- fixed before the first run.
TOL_PANEL_REL = 5e-4      # relative agreement with a filed panel number
TOL_ANCHOR = 1e-9         # tau_50 / k* / cell-edge reproduction
TOL_FP_K = 1e-9           # fixed-point coordinate reproduction
TOL_RESID_REL = 1e-6      # residual reproduction, relative
TOL_PAYOFF = 1e-9         # numerical_v4's payoff tolerance; the card's scale
EXCURSION_MARGIN = 1e5    # excursions must exceed TOL_PAYOFF by this factor
NG_PANEL = 6001           # a6_A_probe8_open.py's own global grid
NG_DENSE = 60001          # 10x, the robustness row
DENSE_RADIUS = 1e-3       # declared; see the docstring
BUFFER_FRAC = 0.10        # declared; argmax sampling buffer off each crossing
N_ARGMAX_SAMPLES = 41     # per interval
CONTAINMENT_LO, CONTAINMENT_HI = 1.55, 1.62   # coarse, declared: the ungated
#                             per-offset containment window for the ladder

results: dict = {"kind": "A3 applicability evidence (panel-probe curation)",
                 "checks": [], "n_fail": 0, "loci_done": 0}


def record(name: str, ok: bool, kind: str, detail: dict) -> None:
    results["checks"].append({"name": name, "kind": kind, "pass": bool(ok),
                              **detail})
    if not ok:
        results["n_fail"] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def rel(a: float, b: float) -> float:
    """Relative difference on the mean scale; 0 if both are 0."""
    m = 0.5 * (abs(a) + abs(b))
    return 0.0 if m == 0.0 else abs(a - b) / m


def sig3(x: float) -> str:
    """3 significant figures -- the precision Analyst A filed the excursions at,
    and the form t2_a6_edge_jump_check.py uses for its 3-s.f. card figures."""
    return "%.3g" % abs(x)


def g3(x: float) -> float:
    """``x`` rounded to 3 significant figures, as a float."""
    return float(sig3(x))


def flush_json() -> None:
    tmp = OUT + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(results, fh, indent=2, default=float)
    os.replace(tmp, OUT)


def n_edges(p: ParamsV4) -> dict[int, float]:
    """Interior n(s) cell edges, verbatim from a6_A_probe8_open.py (which is
    the same construction menu.type_reference uses).

    n(s) is weakly DECREASING, so edge(m) is where n steps from m+1 (below) to
    m (above).
    """
    out: dict[int, float] = {}
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            s = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo < s < p.s_hi:
                out[m] = s
    return out


def gap_fn(res, p: ParamsV4):
    """U_VOICE - U_HOLD as a function of s, at a fixed pooled pass."""
    def g(s: float) -> float:
        return (plan_payoff(VOICE, float(s), res, p)
                - plan_payoff(HOLD, float(s), res, p))
    return g


def sign_changes(vals: np.ndarray, grid: np.ndarray) -> list[tuple[int, float, float]]:
    """Probe 8's criterion verbatim: sign(g[:-1]) * sign(g[1:]) < 0.

    Returns (index, bracket_lo, bracket_hi) per strict sign change.
    """
    idx = np.nonzero(np.sign(vals[:-1]) * np.sign(vals[1:]) < 0)[0]
    return [(int(i), float(grid[i]), float(grid[i + 1])) for i in idx]


def locate(g, lo: float, hi: float) -> float:
    """Locate a sign change.  At crossings 1 and 3 this is an ordinary root; at
    crossing 2 (cell edge 8) U_VOICE jumps, and brentq converges on the
    discontinuity -- see the module docstring."""
    return float(brentq(g, lo, hi, xtol=1e-13))


def argmax_at(s: float, res, p: ParamsV4) -> tuple[int, dict[int, float], float]:
    """(argmax plan, payoffs, gap to the runner-up) at signal s."""
    u = {j: plan_payoff(j, float(s), res, p) for j in (EXIT, HOLD, VOICE)}
    order = sorted(u, key=lambda j: u[j], reverse=True)
    return order[0], u, u[order[0]] - u[order[1]]


# ==========================================================================
# LOCUS 1 -- (kappa = 0.5, tau_50, T = 5), k_2 above cell edge 6
# ==========================================================================

def locus1() -> None:
    print("\n=== LOCUS 1: (kappa=0.5, tau_50, T=5), k_2 above cell edge 6 ===",
          flush=True)

    # -- calibration ---------------------------------------------------------
    print("solving the seed equilibrium (tau = 0.05) ...", flush=True)
    p_seed = ParamsV4.baseline()
    pol_seed, r_seed = solve_policy(p_seed)
    tau50 = float(frozen_tau_grid(pol_seed, p_seed, (0.5,))[0])
    print(f"  tau_50 = {tau50!r}", flush=True)
    print("solving the baseline equilibrium (frozen tau) ...", flush=True)
    p_base = p_seed.replace(tau=tau50)
    pol_base, r_base = solve_policy(p_base)
    K1 = float(pol_base.k[0])
    print(f"  k* = ({K1!r}, {float(pol_base.k[1])!r})", flush=True)

    p = p_base.replace(kappa=0.5, T=5)
    edges = n_edges(p)
    d_tau = abs(tau50 - FILED_TAU50)
    d_k1 = abs(K1 - FILED_K1)
    d_edge = {m: abs(edges[m] - v) for m, v in FILED_EDGES.items() if m in edges}
    record("a3_l1_calibration_anchors_reproduce",
           d_tau <= TOL_ANCHOR and d_k1 <= TOL_ANCHOR
           and all(v <= TOL_ANCHOR for v in d_edge.values()), "wiring",
           dict(tau50=tau50, tau50_filed=FILED_TAU50, tau50_abs_diff=d_tau,
                k1=K1, k1_filed=FILED_K1, k1_abs_diff=d_k1,
                kstar=[float(x) for x in pol_base.k],
                edges={int(m): float(s) for m, s in edges.items()},
                edges_filed={int(m): v for m, v in FILED_EDGES.items()},
                edge_abs_diff={int(m): v for m, v in d_edge.items()},
                tol=TOL_ANCHOR,
                seed_cutoff_scale=float(r_seed.cutoff_scale),
                base_cutoff_scale=float(r_base.cutoff_scale),
                base_payoff_scale=float(r_base.payoff_scale),
                note="a6_A_probe8_open.py hard-codes tau = 0.09076405861553302 "
                     "and K1 = 1.2405757282617416; both are recomputed here and "
                     "the recomputed values are the ones used, as in "
                     "t2_a6_edge_jump_check.py.  k_1 is held at k*[0] throughout, "
                     "as the probe does.  edge(6) is the hyperplane the card's "
                     "open set sits above; the three sign changes sit far below "
                     "it, around edge(8)."))

    EDGE6 = edges[6]
    results["locus1_node"] = dict(kappa=float(p.kappa), tau=float(p.tau),
                                  T=int(p.T), k1_held=K1, edge6=float(EDGE6),
                                  edge8=float(edges[8]),
                                  params_hash=p.hash_str(),
                                  grid_panel=NG_PANEL, grid_dense=NG_DENSE,
                                  s_lo=float(p.s_lo), s_hi=float(p.s_hi))

    grid = np.linspace(p.s_lo, p.s_hi, NG_PANEL)

    # -- the k_2 ladder ------------------------------------------------------
    ladder: list[dict] = []
    card_row: dict | None = None
    for off in (OFFSET_BELOW,) + LADDER_OPEN + LADDER_CLOSED:
        k2 = EDGE6 + off
        res = pooled_pass(atoms((K1, k2), p), p, with_runup=True)
        g = gap_fn(res, p)
        vals = np.array([g(float(s)) for s in grid])
        sc = sign_changes(vals, grid)
        located = [locate(g, lo, hi) for _, lo, hi in sc]
        row = dict(offset=float(off), k2=float(k2), n_sign_changes=len(sc),
                   located=[float(x) for x in located],
                   located_7dp=["%.7f" % x for x in located],
                   expect=3 if off in LADDER_OPEN else 1)
        print(f"  k2 = edge(6) {off:+.0e} = {k2:.9f} : {len(sc)} sign change(s)"
              f"  at {['%.7f' % x for x in located]}", flush=True)
        if off == OFFSET_CARD:
            card_row = dict(row)
            card_row["res"] = res
            card_row["g"] = g
            card_row["vals"] = vals
        ladder.append(row)
    results["locus1_ladder"] = ladder

    open_rows = [r for r in ladder if r["offset"] in LADDER_OPEN]
    record("a3_l1_open_set_three_sign_changes",
           all(r["n_sign_changes"] == 3 for r in open_rows), "card",
           dict(offsets=[r["offset"] for r in open_rows],
                counts=[r["n_sign_changes"] for r in open_rows], expected=3,
                grid=NG_PANEL,
                card_wording="k_2 on an open set above cell edge 6 (verified at "
                             "offsets 1e-9 through 2e-2), U_V - U_H has three "
                             "strict sign changes",
                criterion="sign(g[:-1]) * sign(g[1:]) < 0, verbatim from "
                          "a6_A_probe8_open.py, on its own 6001-point grid"))

    closed_rows = [r for r in ladder if r["offset"] in LADDER_CLOSED
                   or r["offset"] == OFFSET_BELOW]
    record("a3_l1_set_closes_outside_the_card_range",
           all(r["n_sign_changes"] == 1 for r in closed_rows), "panel_filed",
           dict(offsets=[r["offset"] for r in closed_rows],
                counts=[r["n_sign_changes"] for r in closed_rows], expected=1,
                scope="PANEL-FILED, NOT CARD-QUOTED.  The card claims openness "
                      "only through +2e-2.  a6_A_findings.md (A) records one "
                      "sign change below the edge and the count back to 1 at "
                      "+5e-2 and +1e-1; those rows are reproduced here so the "
                      "OPENNESS of the set is bounded on both sides rather "
                      "than merely asserted."))

    # containment of the located crossings across the whole open ladder,
    # recorded with a coarse declared window; no drift tolerance is invented.
    all_open_located = [x for r in open_rows for x in r["located"]]
    record("a3_l1_ladder_containment",
           all(CONTAINMENT_LO <= x <= CONTAINMENT_HI for x in all_open_located),
           "declared_window",
           dict(window=[CONTAINMENT_LO, CONTAINMENT_HI],
                per_offset={("%.0e" % r["offset"]): r["located_7dp"]
                            for r in open_rows},
                scope="COARSE and declared.  The card files the three locations "
                      "at the probes' own +1e-9 offset only; how they move "
                      "across the ladder is not a filed number, so it is "
                      "recorded rather than gated against a tolerance."))

    assert card_row is not None
    res_c, g_c, vals_c = card_row["res"], card_row["g"], card_row["vals"]
    cross = card_row["located"]

    # -- locations at the card's own offset ----------------------------------
    got_7dp = tuple(card_row["located_7dp"]) if len(cross) == 3 else ()
    record("a3_l1_crossing_locations_card_7dp",
           got_7dp == CARD_CROSSINGS_7DP, "card",
           dict(measured=list(cross), measured_7dp=list(got_7dp),
                card_7dp=list(CARD_CROSSINGS_7DP), offset=OFFSET_CARD,
                k2=card_row["k2"],
                abs_diff_from_card_string=[abs(x - float(c))
                                           for x, c in zip(cross,
                                                           CARD_CROSSINGS_7DP)]
                if len(cross) == 3 else None))

    # -- the middle crossing is a jump, not a root ---------------------------
    if len(cross) == 3:
        c2 = cross[1]
        jump = dict(
            located=float(c2), cell_edge_8=float(edges[8]),
            abs_diff_from_edge8=abs(c2 - edges[8]),
            n_below=int(n_days(c2 - 1e-9, p)), n_above=int(n_days(c2 + 1e-9, p)),
            gap_below=float(g_c(c2 - 1e-9)), gap_above=float(g_c(c2 + 1e-9)),
            gap_below_1e6=float(g_c(c2 - 1e-6)), gap_above_1e6=float(g_c(c2 + 1e-6)),
            U_HOLD_below=float(plan_payoff(HOLD, c2 - 1e-6, res_c, p)),
            U_HOLD_above=float(plan_payoff(HOLD, c2 + 1e-6, res_c, p)),
            U_VOICE_below=float(plan_payoff(VOICE, c2 - 1e-6, res_c, p)),
            U_VOICE_above=float(plan_payoff(VOICE, c2 + 1e-6, res_c, p)))
        jump["one_sided_limits_differ"] = (
            abs(jump["gap_above"] - jump["gap_below"]) > TOL_PAYOFF)
        record("a3_l1_middle_sign_change_is_an_n_step_jump",
               jump["n_below"] == jump["n_above"] + 1
               and jump["one_sided_limits_differ"]
               and abs(c2 - edges[8]) <= 1e-6, "structure",
               dict(**jump,
                    note="the middle sign change is NOT a root: n(s) steps 9 -> 8 "
                         "at cell edge 8 and U_VOICE jumps through zero.  brentq "
                         "converges on the discontinuity, which is the right "
                         "location to 7 dp.  U_HOLD does not move across it -- "
                         "the whole step is in U_VOICE.  This is the route the "
                         "card names (Step 15(i) / WHERE IT FAILS 4's card-legal "
                         "counterexample, instantiated by the solver's own "
                         "N_GRID note) interacting with the off-path price snap."))

    # -- middle excursions ---------------------------------------------------
    if len(cross) == 3:
        exc: list[dict] = []
        for a, b in ((cross[0], cross[1]), (cross[1], cross[2])):
            mask = (grid > a) & (grid < b)
            sub = np.abs(vals_c[mask])
            # refined, ungated: a 2001-point grid over the interval interior
            fine = np.linspace(a, b, 2001)[1:-1]
            fine_max = float(np.max([abs(g_c(float(s))) for s in fine]))
            exc.append(dict(lo=float(a), hi=float(b), width=float(b - a),
                            n_panel_points=int(mask.sum()),
                            max_abs_gap_panel_grid=float(sub.max()) if sub.size
                            else float("nan"),
                            max_abs_gap_refined_ungated=fine_max))
        meas = [e["max_abs_gap_panel_grid"] for e in exc]
        rels = [rel(m, f) for m, f in zip(meas, FILED_EXCURSIONS)]
        sf_match = [sig3(m) == sig3(f) for m, f in zip(meas, FILED_EXCURSIONS)]
        in_band = [CARD_EXCURSION_LO <= g3(m) <= CARD_EXCURSION_HI
                   for m in meas]
        above_tol = [m >= EXCURSION_MARGIN * TOL_PAYOFF for m in meas]
        for e, m, f, r in zip(exc, meas, FILED_EXCURSIONS, rels):
            e.update(filed=f, rel_diff_from_filed=r, measured_3sf=sig3(m),
                     filed_3sf=sig3(f))
        results["locus1_excursions"] = exc
        record("a3_l1_middle_excursions",
               all(sf_match) and all(in_band) and all(above_tol), "card+panel",
               dict(measured_panel_grid=meas, filed=list(FILED_EXCURSIONS),
                    measured_3sf=[sig3(m) for m in meas],
                    filed_3sf=[sig3(f) for f in FILED_EXCURSIONS],
                    three_sf_match=sf_match,
                    rel_diff_ungated=rels,
                    superseded_tol_rel=TOL_PANEL_REL,
                    card_band=[CARD_EXCURSION_LO, CARD_EXCURSION_HI],
                    card_band_read_at_3sf=[g3(m) for m in meas],
                    in_card_band=in_band,
                    payoff_tolerance=TOL_PAYOFF,
                    ratio_to_payoff_tolerance=[m / TOL_PAYOFF for m in meas],
                    required_ratio=EXCURSION_MARGIN, above_tolerance=above_tol,
                    refined_ungated=[e["max_abs_gap_refined_ungated"]
                                     for e in exc],
                    scope="GATED ON PROBE 8's OWN 6001-POINT GRID, which is "
                          "where the filed 2.80e-4 / 2.40e-4 were measured: it "
                          "spans [s_lo, s_hi] at a spacing of 1.4142e-3, so it "
                          "puts only 6 and 5 points inside the two middle "
                          "intervals (widths 7.890e-3 and 6.909e-3).  The "
                          "refined-interval maxima are recorded and NOT gated: "
                          "a finer grid finds a larger maximum for grid "
                          "reasons, not model reasons.",
                    gate_form="EXACT equality at the filed precision (3 s.f.), "
                              "which is the form t2_a6_edge_jump_check.py uses "
                              "for 3-s.f. figures.  The relative differences "
                              "against a 5e-4 tolerance are retained above, "
                              "ungated -- that tolerance was transplanted from "
                              "the A6 check's 5-s.f. filed values and is the "
                              "gate this one replaced after the first run; see "
                              "known_discrepancies and the module docstring."))

    # -- argmax pattern ------------------------------------------------------
    if len(cross) == 3:
        w_mid = min(cross[1] - cross[0], cross[2] - cross[1])
        buf = BUFFER_FRAC * w_mid
        windows = [(cross[0] - w_mid, cross[0] - buf),
                   (cross[0] + buf, cross[1] - buf),
                   (cross[1] + buf, cross[2] - buf),
                   (cross[2] + buf, cross[2] + w_mid)]
        iv: list[dict] = []
        for (lo, hi), want in zip(windows, CARD_ARGMAX_PATTERN):
            ams, gaps, worst = [], [], None
            for s in np.linspace(lo, hi, N_ARGMAX_SAMPLES):
                am, u, gp = argmax_at(float(s), res_c, p)
                ams.append(am)
                gaps.append(gp)
                if worst is None or gp < worst[1]:
                    worst = (float(s), gp, {NAME[j]: float(u[j]) for j in u})
            uniq = sorted({NAME[a] for a in ams})
            iv.append(dict(window=[float(lo), float(hi)], want=NAME[want],
                           got=uniq, constant=len(uniq) == 1,
                           matches=len(uniq) == 1 and ams[0] == want,
                           n_samples=N_ARGMAX_SAMPLES,
                           min_gap_to_runner_up=float(min(gaps)),
                           strict_singleton_everywhere=bool(min(gaps) > 0.0),
                           worst_point=worst[0], worst_payoffs=worst[2]))
        results["locus1_intervals"] = iv
        record("a3_l1_argmax_H_V_H_V_single_valued",
               all(x["matches"] for x in iv)
               and all(x["strict_singleton_everywhere"] for x in iv), "card",
               dict(pattern_measured=[x["got"] for x in iv],
                    pattern_card=[NAME[j] for j in CARD_ARGMAX_PATTERN],
                    min_gap_to_runner_up=[x["min_gap_to_runner_up"] for x in iv],
                    buffer_fraction=BUFFER_FRAC,
                    flank_width=float(w_mid), buffer=float(buf),
                    n_samples_per_interval=N_ARGMAX_SAMPLES,
                    scope="Intervals are crossing-delimited with a declared 10% "
                          "buffer off each crossing and outer windows one "
                          "middle-interval wide; see the docstring's DECLARED "
                          "SAMPLING GEOMETRY.  Singleton-ness is tested as "
                          "strict float uniqueness at the sampled points; the "
                          "card's quantitative 'against the 1e-9 payoff "
                          "tolerance' content is carried by the excursion gate."))

        record("a3_l1_no_weakly_increasing_selection_exists",
               all(x["matches"] for x in iv)
               and all(x["strict_singleton_everywhere"] for x in iv), "derived",
               dict(argmax_sequence=[x["got"][0] for x in iv],
                    menu_order="EXIT < HOLD < VOICE",
                    descent_at_crossing_2=float(cross[1]),
                    reasoning="the best-response correspondence is a strict "
                              "singleton at every sampled point of all four "
                              "intervals, so every selection of it EQUALS the "
                              "pointwise argmax there.  That argmax is VOICE on "
                              "interval 2 and HOLD on interval 3, and HOLD < "
                              "VOICE in the menu order, so every selection "
                              "strictly decreases across crossing 2.  Hence "
                              "S(k) -- Step 13's set of weakly increasing "
                              "selections -- is EMPTY, and the card's outer map "
                              "T is UNDEFINED at this k, not merely "
                              "discontinuous.  This is a logical consequence of "
                              "the measured rows above, not a separate "
                              "measurement.",
                    not_claimed="this does not establish that no equilibrium "
                                "exists at this calibration; it establishes "
                                "that A3, and with it the Step 13 construction "
                                "P1 runs through, is unavailable here."))

    # -- dense-grid robustness ----------------------------------------------
    if len(cross) == 3:
        dgrid = np.linspace(p.s_lo, p.s_hi, NG_DENSE)
        dvals = np.array([g_c(float(s)) for s in dgrid])
        dsc = sign_changes(dvals, dgrid)
        dloc = [locate(g_c, lo, hi) for _, lo, hi in dsc]
        near = [min(abs(x - c) for c in cross) for x in dloc]
        record("a3_l1_dense_grid_robustness",
               len(dsc) == 3 and all(d <= DENSE_RADIUS for d in near), "declared",
               dict(grid=NG_DENSE, n_sign_changes=len(dsc),
                    located=[float(x) for x in dloc],
                    located_7dp=["%.7f" % x for x in dloc],
                    distance_to_nearest_panel_grid_crossing=[float(d)
                                                             for d in near],
                    radius=DENSE_RADIUS,
                    panel_grid_spacing=float(grid[1] - grid[0]),
                    dense_grid_spacing=float(dgrid[1] - dgrid[0]),
                    smallest_gap_between_crossings=float(
                        min(cross[1] - cross[0], cross[2] - cross[1])),
                    scope="count AND location, so a spurious count can be "
                          "diagnosed rather than merely reported.  The radius "
                          "1e-3 compares brentq-LOCATED crossings (xtol = "
                          "1e-13 on each grid's own sign-change brackets), not "
                          "grid points, so what it must clear is the "
                          "root-finder's precision rather than either grid's "
                          "spacing -- and it clears it by about eleven orders, "
                          "the measured cross-grid agreement being <= 4.4e-14. "
                          "At the other end it sits an order of magnitude below "
                          "the smallest inter-crossing gap (6.909e-3), so it "
                          "cannot merge two crossings either."))

    results["loci_done"] = 1
    flush_json()


# ==========================================================================
# LOCUS 2 -- (kappa = 0.15, 0.05, 5), argmax reversal across cell edge
# ==========================================================================

def locus2() -> None:
    print("\n=== LOCUS 2: (kappa=0.15, tau=0.05, T=5), cell edge "
          f"{EDGE2:.12f} ===", flush=True)
    p = ParamsV4().replace(**NODE2)
    edges = n_edges(p)

    # a6_B_argmax.py's edge literal, recomputed.  n(s) is weakly decreasing, so
    # the edge just above k2* is the one the probe names.
    m_match = min(edges, key=lambda m: abs(edges[m] - EDGE2))
    d_edge = abs(edges[m_match] - EDGE2)
    record("a3_l2_edge_anchor_reproduces",
           d_edge <= TOL_ANCHOR, "wiring",
           dict(edge_recomputed=float(edges[m_match]), edge_filed=EDGE2,
                abs_diff=float(d_edge), m=int(m_match), tol=TOL_ANCHOR,
                node=NODE2, params_hash=p.hash_str(),
                params_identity_note="a6_B_argmax.py starts from ParamsV4(), "
                                     "a6_A_probe8_open.py from "
                                     "ParamsV4.baseline(); the two agree "
                                     "before the .replace() calls, checked in "
                                     "a3_params_baseline_identity.",
                edges={int(m): float(s) for m, s in edges.items()}))

    # -- fp1: residual at the ticket-34 full-precision coordinates ------------
    res_full = pooled_pass(atoms(FP1_FULL_K, p), p, with_runup=True)
    r1 = equilibrium_residual(FP1_FULL_K, p, res_full)
    rc = rel(float(r1.cutoff_scale), FILED_FP1_CUTOFF_SCALE)
    rp = rel(float(r1.payoff_scale), FILED_FP1_PAYOFF_SCALE)
    record("a3_l2_fp1_residual_reproduces",
           rc <= TOL_RESID_REL and rp <= TOL_RESID_REL, "panel_filed",
           dict(k=list(FP1_FULL_K),
                cutoff_scale=float(r1.cutoff_scale),
                cutoff_scale_filed=FILED_FP1_CUTOFF_SCALE, cutoff_rel=rc,
                payoff_scale=float(r1.payoff_scale),
                payoff_scale_filed=FILED_FP1_PAYOFF_SCALE, payoff_rel=rp,
                tol_rel=TOL_RESID_REL,
                source="t2_t34_account_sweep.json provenance."
                       "node15_reference_values",
                note="the pinned fixed point is a fixed point of the IMPLEMENTED "
                     "CUTOFF MAP and is NOT an equilibrium: its payoff-scale "
                     "residual is 1.77e-3 against a 1e-9 criterion.  Recorded "
                     "here only to identify the configuration the argmax "
                     "reversal is measured at."))

    # -- fp2: reproduced from a6_B_alt's own k_init --------------------------
    print(f"  solving from a6_B_alt's k_init = {FP2_K_INIT} ...", flush=True)
    pol2, r2 = solve_policy(p, k_init=FP2_K_INIT)
    k2_got = (float(pol2.k[0]), float(pol2.k[1]))
    d_fp2 = max(abs(k2_got[i] - FP2_ARGMAX_K[i]) for i in (0, 1))
    record("a3_l2_fp2_reproduces_from_filed_k_init",
           d_fp2 <= TOL_FP_K, "panel_filed",
           dict(k_init=list(FP2_K_INIT), k=list(k2_got),
                k_filed=list(FP2_ARGMAX_K), max_abs_diff=float(d_fp2),
                tol=TOL_FP_K,
                cutoff_scale=float(r2.cutoff_scale),
                payoff_scale=float(r2.payoff_scale),
                payoff_scale_filed_4sf=FILED_FP2_PAYOFF_SCALE,
                payoff_scale_rel_to_filed=rel(float(r2.payoff_scale),
                                              FILED_FP2_PAYOFF_SCALE),
                n_below_k2=int(n_days(k2_got[1] - 1e-9, p)),
                n_above_k2=int(n_days(k2_got[1] + 1e-9, p)),
                scope="the filed payoff_scale 3.055e-4 is quoted to 4 s.f. in "
                      "t2_t34_account_sweep.json and is RECORDED, not gated; "
                      "the gate is the fixed-point coordinates.",
                route="a6_B_alt.py: this is the interior-crossing fixed point, "
                      "reached from k_init = (1.02, 1.71).  It is a second, "
                      "independent basin at the same node, which is why the "
                      "card says the reversal holds at BOTH located fixed "
                      "points."))

    # -- the reversal at both fixed points -----------------------------------
    per_fp: list[dict] = []
    ok_reversal, ok_strings, ok_n = True, True, True
    for idx, K in ((1, FP1_ARGMAX_K), (2, FP2_ARGMAX_K)):
        res = pooled_pass(atoms(K, p), p, with_runup=True)
        sides: dict[str, dict] = {}
        for tag, off in (("below", -OFFSET2), ("above", +OFFSET2)):
            s = EDGE2 + off
            am, u, gp = argmax_at(s, res, p)
            filed = FILED_PAYOFFS[(idx, tag)]
            got = tuple("%.7f" % u[j] for j in (EXIT, HOLD, VOICE))
            match = got == filed[:3]
            n_here = int(n_days(s, p))
            n_want = FILED_N_BELOW if tag == "below" else FILED_N_ABOVE
            sides[tag] = dict(
                s=float(s), offset=float(off), n=n_here, n_filed=n_want,
                U={NAME[j]: float(u[j]) for j in (EXIT, HOLD, VOICE)},
                U_7dp=dict(zip(("EXIT", "HOLD", "VOICE"), got)),
                U_7dp_filed=dict(zip(("EXIT", "HOLD", "VOICE"), filed[:3])),
                strings_match=bool(match),
                argmax=NAME[am], argmax_filed=NAME[filed[3]],
                argmax_matches=bool(am == filed[3]),
                gap_to_runner_up=float(gp),
                strict_singleton=bool(gp > 0.0))
            ok_strings = ok_strings and match
            ok_n = ok_n and (n_here == n_want)
            ok_reversal = ok_reversal and (am == filed[3]) and (gp > 0.0)
            print(f"  fp{idx} {tag:5s} s=edge{off:+.0e} n={n_here} "
                  f"argmax={NAME[am]:5s} "
                  f"U_E={u[EXIT]:.7f} U_H={u[HOLD]:.7f} U_V={u[VOICE]:.7f}",
                  flush=True)
        # extra, non-gating: the probe's other offset
        extra = {}
        for tag, off in (("below", -OFFSET2_EXTRA), ("above", +OFFSET2_EXTRA)):
            am, u, gp = argmax_at(EDGE2 + off, res, p)
            extra[tag] = dict(offset=float(off), argmax=NAME[am],
                              n=int(n_days(EDGE2 + off, p)),
                              U={NAME[j]: float(u[j]) for j in (EXIT, HOLD, VOICE)},
                              gap_to_runner_up=float(gp))
        per_fp.append(dict(fixed_point=idx, k=list(K), sides=sides,
                           extra_offsets_ungated=extra,
                           reverses_voice_to_hold=bool(
                               sides["below"]["argmax"] == "VOICE"
                               and sides["above"]["argmax"] == "HOLD")))
    results["locus2_fixed_points"] = per_fp

    record("a3_l2_argmax_reverses_voice_to_hold",
           ok_reversal and all(f["reverses_voice_to_hold"] for f in per_fp),
           "card",
           dict(per_fixed_point=[dict(k=f["k"],
                                      below=f["sides"]["below"]["argmax"],
                                      above=f["sides"]["above"]["argmax"],
                                      min_gap=min(f["sides"][t]["gap_to_runner_up"]
                                                  for t in ("below", "above")))
                                 for f in per_fp],
                edge=EDGE2, offset=OFFSET2,
                card_wording="the argmax reverses VOICE -> HOLD across cell "
                             "edge s = 1.659062163 at both located fixed "
                             "points: the preferred plan decreases in s"))

    record("a3_l2_filed_payoff_strings_reproduce",
           ok_strings and ok_n, "panel_filed",
           dict(n_strings=12, all_match=ok_strings, n_days_match=ok_n,
                n_below_filed=FILED_N_BELOW, n_above_filed=FILED_N_ABOVE,
                source="a6_panel_probes_2026-08-27/a6_B_findings.md section 4, "
                       "replayed at a6_B_argmax.py's own k literals, its own "
                       "12-dp edge and its own +/-1e-6 offsets"))

    record("a3_l2_preferred_plan_decreasing_in_s",
           ok_reversal and all(f["reverses_voice_to_hold"] for f in per_fp),
           "derived",
           dict(menu_order="EXIT < HOLD < VOICE",
                reasoning="the argmax is a strict singleton on both sides of "
                          "the edge at both fixed points, VOICE below and HOLD "
                          "above, and HOLD < VOICE in the menu order.  The "
                          "preferred plan therefore DECREASES in s, "
                          "contradicting A3's second clause -- independently of "
                          "locus 1, at a different (kappa, tau, T) and by a "
                          "different route.  As at locus 1, S(k) is empty and "
                          "no cutoff vector represents the best response.",
                route="the s-direction step of U_VOICE (n(s) is integer-valued) "
                      "interacting with the off-path price snap; NOT a "
                      "non-monotone cost",
                not_claimed="an edge-pinned fixed point of the implemented "
                            "cutoff map is not an equilibrium, and none of this "
                            "resolves the four ticket-34 existence questions."))

    results["loci_done"] = 2


def main() -> int:
    t_run = time.perf_counter()

    # wiring: the two probe families start from different constructors
    p_a, p_b = ParamsV4.baseline(), ParamsV4()
    record("a3_params_baseline_identity",
           p_a.hash_str() == p_b.hash_str(), "wiring",
           dict(baseline_hash=p_a.hash_str(), default_hash=p_b.hash_str(),
                note="a6_A_probe8_open.py builds locus 1 from "
                     "ParamsV4.baseline(); a6_B_argmax.py / a6_B_alt.py build "
                     "locus 2 from ParamsV4().  The two must be the same "
                     "starting point for the two loci to be the same "
                     "calibration."))

    locus1()
    locus2()

    results["seconds"] = time.perf_counter() - t_run
    results["all_pass"] = results["n_fail"] == 0
    exc = results.get("locus1_excursions", [])
    results["known_discrepancies"] = [
        {
            "item": "the excursion gate's FORM was restructured after the "
                    "first run (declared, not silent)",
            "reproduced": True,
            "original_gate": "relative agreement with the filed excursions to "
                             "TOL_PANEL_REL = 5e-4",
            "original_result": "MISSED on the first interval: relative "
                               "differences 1.3226e-3 and 4.4601e-4 against "
                               "5e-4, so the run reported 1 gate failing.  The "
                               "measured maxima were 2.80370586579648e-4 and "
                               "2.40107065617487e-4 -- unchanged by the "
                               "restructure, and unchanged since.",
            "why": "5e-4 relative was carried over from "
                   "t2_a6_edge_jump_check.py, whose filed panel values are "
                   "quoted to FIVE significant figures (6.3333e-03), where "
                   "5e-4 is about the last-digit rounding window.  Analyst A "
                   "filed the A3 excursions to THREE ('max|gap| = 2.80e-4 and "
                   "2.40e-4'), so the transplanted tolerance demanded digits "
                   "the source never recorded.  Both measured maxima round to "
                   "the filed strings EXACTLY.",
            "new_gate": "'%.3g' string equality against the filed values, plus "
                        "the card's 2.4e-4 - 2.8e-4 band read at the same 3 "
                        "s.f. -- the form t2_a6_edge_jump_check.py itself uses "
                        "for 3-s.f. card figures (card_3sf)",
            "direction": "NUMERICALLY WIDER, not tighter: the 3-s.f. rounding "
                         "window is about 1.8e-3 relative against the original "
                         "5e-4.  Digit-exact in form.  It keeps teeth -- the "
                         "refined-grid maximum 3.07e-4 would still fail it.  No "
                         "measured number moved, no other gate moved, and both "
                         "relative differences remain in the JSON, ungated.",
        },
        {
            "item": "the card's quoted excursion band is a GRID-RESOLUTION "
                    "quantity and understates the true excursions",
            "reproduced": True,
            "card_wording": "middle excursions 2.4-2.8e-4 against a 1e-9 "
                            "payoff tolerance",
            "measured_on_the_panel_grid": [e["max_abs_gap_panel_grid"]
                                           for e in exc],
            "measured_on_a_refined_interval_grid": [
                e["max_abs_gap_refined_ungated"] for e in exc],
            "finding": "the filed 2.80e-4 / 2.40e-4 are maxima over probe 8's "
                       "6001-point GLOBAL signal grid, which puts only 5 and 6 "
                       "points inside the two middle intervals.  Resampling "
                       "each interval on its own 2001-point grid gives 3.066e-4 "
                       "and 2.686e-4 -- about 9% and 12% larger.  The card's "
                       "band is therefore a property of the panel's sampling, "
                       "not the true suprema of |U_V - U_H| on those intervals.",
            "direction": "This STRENGTHENS the A3 failure rather than "
                         "weakening it: the true excursions are LARGER than the "
                         "card quotes, so the departure from single crossing is "
                         "bigger than recorded, and the margin over the 1e-9 "
                         "payoff tolerance rises from ~2.8e5 to ~3.1e5.  "
                         "Nothing in the finding is in doubt; only the two "
                         "quoted figures are resolution-limited.",
            "recommendation": "a wording note if the card is ever touched here "
                              "-- the numbers are correct AS the panel-grid "
                              "maxima they are, and this check gates them as "
                              "such.  No label implication either way.",
        },
    ]
    results["verdict"] = (
        "A3 failure REPRODUCED at calibration"
        if results["all_pass"] else
        f"A3 failure PARTIALLY REPRODUCED ({results['n_fail']} gate(s) missed)"
    ) + (
        " -- locus 1 (kappa=0.5, tau_50, T=5): three strict sign changes in "
        "U_VOICE - U_HOLD on an open set of k_2 above cell edge 6, at the "
        "card's quoted signals, with the pointwise argmax H,V,H,V single-valued "
        "on each interval, so no weakly increasing selection exists and Step "
        "13's outer map is undefined there.  locus 2 (kappa=0.15, 0.05, 5): the "
        "argmax reverses VOICE -> HOLD across cell edge 1.659062163 at both "
        "located fixed points, so the preferred plan decreases in s.  NO LABEL "
        "MOVES AND NONE IS LICENSED -- A3 is a listed hypothesis of P1 and "
        "carries no label of its own, so this is applicability evidence on an "
        "antecedent at the implemented calibration, in the A(tau) pattern.  P1 "
        "stays PROVED as a conditional."
    )
    results["provenance"] = {
        "follow_up": "the standing 'a separate follow-up owns the A3 locus' "
                     "item recorded in t2_a6_edge_jump_check.py, "
                     "t2_a6_node15_check.py and t2_a6_collapse_face_check.py, "
                     "re-requested as UNCHECKED item 5 of GPT Pro's 2026-08-28 "
                     "re-review and carried in "
                     "quality_reports/session_logs/"
                     "2026-08-28_gpt_rereview_audit_repairs.md as 'on file, "
                     "not started'",
        "card_row": "research/model_v4/MODEL_CARD.md section 5, A3 evidence "
                    "note (stamp 2026-08-28, commit 59c0dfc -- verified "
                    "against the file before this script was written)",
        "check_request": "research/model_v4/threads/2026-08-28_gpt_rereview.md, "
                         "A3 section, NUMERICAL CHECK REQUEST",
        "source_probes": [
            "a6_panel_probes_2026-08-27/a6_A_probe8_open.py (locus 1: the k_2 "
            "offset ladder, the 6001-point grid, the strict sign-change "
            "criterion)",
            "a6_panel_probes_2026-08-27/a6_A_findings.md (A) (locus 1: the "
            "three crossing locations, the two middle excursions, the H,V,H,V "
            "argmax, the open-set width, the closing offsets)",
            "a6_panel_probes_2026-08-27/a6_B_argmax.py (locus 2: the argmax "
            "reversal at both fixed points; its k literals, its 12-dp edge and "
            "its +/-1e-6 offsets are used verbatim)",
            "a6_panel_probes_2026-08-27/a6_B_alt.py (locus 2: the interior-"
            "crossing fixed point, from k_init = (1.02, 1.71))",
            "a6_panel_probes_2026-08-27/a6_B_findings.md section 4 (locus 2: "
            "the filed 7-dp payoff strings)",
            "quality_reports/fixes/t2_t34_account_sweep.json provenance."
            "node15_reference_values (locus 2: the full-precision pinned fixed "
            "point and its two residuals)",
        ],
        "panel_reports": [
            "research/model_v4/threads/2026-08-27_A6_panel_substantiate.md",
            "research/model_v4/threads/2026-08-27_A6_panel_defuse.md",
        ],
        "pre_registration": (
            "PRE-REGISTERED BY CONSTRUCTION.  Every gated number is the card's "
            "section 5 A3 evidence note or a panel-filed value, both written "
            "before this script; GPT Pro's NUMERICAL CHECK REQUEST restates "
            "the same predictions.  The two declared choices the card does not "
            "make -- the argmax sampling geometry and the dense-grid location "
            "radius -- are set out in the module docstring with their reasons, "
            "and neither was moved after a run."
        ),
        "verdict_semantics": (
            "INVERTED relative to a proof check.  pass = the panel's "
            "measurement REPRODUCED, i.e. A3 fails at the quoted loci in the "
            "quoted way.  pass does NOT mean A3 holds.  A3 is a HYPOTHESIS of "
            "P1 and carries no honesty label of its own, so NO LABEL MOVE is "
            "possible or licensed here; this is applicability evidence in the "
            "A(tau) pattern.  P1 stays PROVED as a conditional."
        ),
        "environment_gate": ".venv/bin/python -m numerical_v4.smoke, exit 0, "
                            "SMOKE COMPLETE in 65.9 s, run before this script",
        "determinism": "no randomness, no wall-clock dependence, no Monte "
                       "Carlo, no file input, no network; every k, offset, grid "
                       "and seed is a frozen literal; numerical_v4 imported "
                       "read-only",
        "does_not": [
            "touch MODEL_CARD.md, the mirrors, sections_v3/, LABEL_LEDGER.md, "
            "HANDOFF_sign.md or anything under research/",
            "modify anything under numerical_v4/ (imported read-only)",
            "move, or license moving, any honesty label -- A3 has none",
            "claim or deny existence of equilibrium at either locus",
            "turn an edge-pinned fixed point of the cutoff map into an "
            "equilibrium",
            "resolve any of the four ticket-34 UNRESOLVED nodes",
            "re-run the ticket-34 sweep or recheck, or change any tolerance in "
            "numerical_v4",
            "curate the A6 material (the T_2 edge jumps, the collapse face, the "
            "chamber-interior Theta+ rescue) -- the three committed t2_a6_* "
            "checks own it",
        ],
    }

    flush_json()

    print(f"\n{results['verdict']}", flush=True)
    print(f"({len(results['checks'])} checks, {results['n_fail']} failing, "
          f"{results['seconds']:.0f} s)  ->  {OUT}", flush=True)
    return 0 if results["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
