"""Ticket 34's candidate mechanical account, swept over the OTHER THREE nodes.

WHAT THIS IS.  ``quality_reports/fixes/t2_p1_fournode_recheck.py`` left four
sweep nodes STILL UNRESOLVED after 30 seeds each --

    (kappa, tau, T) in {(0.15, 0.05, 5), (0.15, 0.075, 1),
                        (0.85, 0.05, 5), (0.85, 0.075, 1)}

-- with best cutoff-scale residuals of 1e-14..1e-11 (passing the diagnostic
scale) but best payoff-scale residuals of 3.1e-4..1.5e-3 against a 1e-9
criterion: five to six orders of magnitude out, and stubbornly so.

The 2026-08-27 A6 panel produced a CANDIDATE MECHANICAL ACCOUNT of that stall,
probed at ONE node only, (kappa=0.15, tau=0.05, T=5) --
``a6_panel_probes_2026-08-27/a6_B_node15.py`` / ``.json``, ``a6_B_resid.py``,
``a6_B_argmax.py``, ``a6_B_alt.py``, written up in ``a6_B_findings.md`` 4d/4e/4f
and ``a6_A_findings.md`` probe 5(b).  In one sentence:

    the outer map's k_2 coordinate can be pinned exactly on an n(s) CELL EDGE,
    because U_HOLD - U_VOICE JUMPS THROUGH ZERO THERE WITHOUT CROSSING IT
    (n(s) is integer-valued, so U_VOICE steps in s); brentq inside
    ``outer_map`` then converges on the jump rather than on a root, which
    makes the cutoff-scale residual vanish while the payoff-scale residual
    stays at the size of the jump's one-sided value.

MODEL_CARD.md's Section 5 A3 evidence note (stamp 2026-08-27, commit
``ae9caea`` -- verified against the file before this script was written)
records that account as "on file and UNCHECKED beyond the one node probed",
and records alongside it the panel's separate NEGATIVE: the k-direction
(price-discontinuity) jump mechanism does *not* explain these nodes -- the
solved cutoffs are not systematically close to the discontinuity surfaces
("NO CORRELATION -- do not claim one", ``a6_A_findings.md`` probe 5(b), which
records the four nodes' distances as 0.031 / 0.026 / 0.044 / 0.030 sigma_s).

THIS SCRIPT SWEEPS THAT ACCOUNT OVER THE THREE UNPROBED NODES, running the
node-15 diagnostic battery at each and returning a THREE-WAY per-node call.
It adds no model objects: everything comes from ``numerical_v4`` read-only
(``ParamsV4``, ``atoms``, ``n_days``, ``_sigmoid_inv``, ``b_star_inverse``,
``pooled_pass``, ``plan_payoff``, ``outer_map``, ``equilibrium_residual``,
``solve_policy``).

FRAMING -- FIXED IN ADVANCE, INDEPENDENT OF THE OUTCOME.  This is diagnostic
evidence about WHY the ticket-34 recheck stalls at these nodes.  No label
moves and none is licensed: A3 and A6 are listed hypotheses and P1 stays
PROVED as a conditional.  Existence of equilibrium at these nodes is neither
claimed nor denied here -- an edge-pinned "fixed point" is a fixed point of
the implemented cutoff map, NOT an equilibrium (its payoff-scale residual is
1e-3-grade), and a stalled search is not a nonexistence proof.  The account
graduates from "candidate, UNCHECKED beyond one node" to exactly whatever the
per-node record below says, and no further.

--------------------------------------------------------------------------
PRE-REGISTERED VERDICT RULE  (fixed before any of the three nodes was run;
the node-15 numbers below are the only ones that informed the thresholds)
--------------------------------------------------------------------------
Per node, three signatures are measured.

(i) EDGE-PINNED JUMP-THROUGH-ZERO.  Satisfied in one of two manifestations.

    A -- PINNED FIXED POINT.  Some located fixed point k* (confirmed:
        cutoff_scale(k*) < FP_TOL) has |k*_2 - e| < PIN_TOL for a candidate
        edge e, and at e the relevant adjacent-plan gap U_HOLD - U_VOICE has
        one-sided limits of strictly OPPOSITE sign with both magnitudes above
        JUMP_MIN -- i.e. it jumps through zero without crossing -- and n(s)
        differs across e.

    B -- AT-EDGE DEVIATION (fallback, for nodes with no pinned fixed point).
        At the node's achieving fixed point the WORST payoff-scale deviation
        (``equilibrium_residual``'s own dev-grid maximand, re-walked here with
        its argmax location recorded) sits in a cell whose boundary e* lying
        between it and the relevant cutoff carries the same jump-through-zero;
        and the one-sided gap value on the deviation's side matches the
        deviation magnitude within a factor of DEV_FACTOR.

    Neither manifestation => signature (i) FAILS, and the observed locus of
    the worst deviation is recorded instead.

(ii) RESIDUAL REPRODUCTION AND BRACKETING.  Every located configuration that
    matches a recheck basin reproduces that basin's payoff and cutoff scales
    to REPRO_RTOL; and, when two or more INDEPENDENTLY located configurations
    exist (the achieving basin itself excluded, so the test cannot be won by
    construction), their payoff residuals bracket the node's recorded 30-seed
    best payoff residual.  When fewer than two independent configurations
    exist the bracket is recorded N/A and (ii) rests on reproduction alone --
    a missing bracket is not evidence against the account.

(iii) PROXIMITY NEGATIVE REPLICATES.  The achieving fixed point's k_2
    distance to the nearest n(s) cell edge reproduces ``a6_A_findings.md``
    probe 5(b)'s recorded sigma_s figure for this node to SIGMA_TOL, and the
    achieving fixed point is itself NOT edge-pinned.  Per-basin
    (distance, payoff) pairs are recorded; with one to three basins per node
    no within-node correlation is computed and none should be read in -- the
    recorded negative is a cross-node statement and only its per-node inputs
    are replicated here.

CALL:
    HOLDS               -- (i) satisfied (manifestation recorded), (ii) and
                           (iii) both satisfied.
    DIFFERENT MECHANISM -- (i) fails while the diagnostic itself ran clean
                           (gates passed, reproductions agreed): the account's
                           signature is absent at this node and the observed
                           locus is recorded.
    INCONCLUSIVE        -- any other combination: a mixed result ((i) present
                           but (ii) or (iii) not), or an obstructed diagnostic
                           (k_1-invariance gate unrecoverable, a located fixed
                           point that will not confirm, a reproduction
                           disagreement).  Never forced into a call.

NODE-15 REFERENCE VALUES the thresholds were set against (a6_B_resid.py, and
the recheck's own two basins at that node):
    pinned fixed point k* = (1.0202217805, 1.6590621627), edge 1.659062163,
    offset ~1e-10;  U_H - U_V = -1.765771e-03 at edge-1e-5 (n=8) and
    +1.278166e-03 at edge+1e-5 (n=7);  payoff_scale 1.7657e-03 (= the
    below-edge one-sided value to 3 significant figures), cutoff_scale
    5.34e-13;  interior crossing fixed point at k_2 = 1.7104049 with payoff
    3.055e-04;  those two bracket the node's recorded best, 1.4882e-03.

--------------------------------------------------------------------------
METHOD TRANSFER FROM a6_B_node15.py, AND THE THREE ADAPTATIONS
--------------------------------------------------------------------------
The node-15 probe fixed k_1 = 1.20, swept k_2 over np.linspace(1.30, 2.10, 33)
with every n(s) cell edge in range bracketed at +-1e-7, and read off where
T_2(k_2) - k_2 changes sign relative to the edges.  That is reproduced here
verbatim, per node, with three additions -- each recorded in the JSON, none of
which changes what the diagnostic means:

  1. The 1-D reduction is GATED rather than assumed.  Node 15 inherited
     "T depends on k only through k_2" from a6_B probe 2A, which was measured
     at the BASELINE calibration.  Here it is re-measured at each node (k_1
     varied over five values at fixed k_2, T compared) before the sweep runs.
     If it were to fail at a node the sweep would still be run, with k_1 fixed
     at that node's achieving k_1 instead of 1.20, and the adaptation flagged;
     the sweep is a fixed-point locator either way, and every candidate it
     produces is independently confirmed by a full two-coordinate
     ``equilibrium_residual`` call, which does not rely on the reduction.

  2. The tau-crossing pullback family is swept ALONGSIDE the n(s) family.
     ``a6_B_findings.md`` Section 7 lists this as UNCHECKED ("I swept the n(s)
     edges only"), and it matters here because two of the three nodes carry
     tau = 0.075, where ``menu.py::breakpoints``' tau-crossing pullbacks are
     13 in range rather than 4.  Both families are computed exactly as
     ``menu.py`` computes them, k-independently, and every pin is classified
     by family.  Sweeping a superset of node 15's candidate edges can only add
     pins, never remove one, so comparability with node 15 is preserved; the
     n(s)-only result is reported separately as well.

  3. Fixed points are taken from the ticket-34 recheck's OWN 30 seeds, not
     re-solved 30 times.  The recheck's landed basins are embedded below as
     literals (following the parent script's own PRIOR_5SEED precedent),
     and ONE seed per basin is re-solved here as the reproduction check.
     Re-running all 90 solves would reproduce them exactly -- ``solve_policy``
     is deterministic in its seed -- at roughly 40 minutes of extra compute
     and no extra information.

Deterministic and self-contained: no wall-clock dependence, no Monte Carlo, no
file inputs, no network.  The only randomness is ``solve_policy``'s own seeded
jitter (``np.random.default_rng(seed)``), and every seed used is a fixed
literal.  Reads ``numerical_v4`` only; writes only its own JSON.  Does not
rerun the ticket-34 sweep, does not change any tolerance, and does not write
to MODEL_CARD.md, the mirrors, LABEL_LEDGER.md or the session log.

Run:    .venv/bin/python quality_reports/fixes/t2_t34_account_sweep.py
Output: quality_reports/fixes/t2_t34_account_sweep.json
        (checkpointed atomically after every node; safe to interrupt)
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from numerical_v4.menu import (  # noqa: E402
    _sigmoid_inv,
    atoms,
    b_star_inverse,
    n_days,
)
from numerical_v4.params import EXIT, HOLD, VOICE, ParamsV4  # noqa: E402
from numerical_v4.policy import plan_payoff  # noqa: E402
from numerical_v4.pooled import pooled_pass  # noqa: E402
from numerical_v4.solver import (  # noqa: E402
    DEV_OFFSETS,
    N_GRID,
    TOL_CUTOFF,
    TOL_PAYOFF,
    equilibrium_residual,
    outer_map,
    solve_policy,
)

OUT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "t2_t34_account_sweep.json"
)

PLAN_NAME = {EXIT: "EXIT", HOLD: "HOLD", VOICE: "VOICE"}

# -- tolerances (imported verbatim where they exist; DO NOT change) -----------
TOL_EXIST_PAYOFF = TOL_PAYOFF     # 1e-9  -- the binding existence criterion
TOL_EXIST_CUTOFF = TOL_CUTOFF     # 1e-10 -- diagnostic scale

# -- pre-registered diagnostic thresholds (set against the node-15 reference
#    values quoted in the docstring, before any of the three nodes was run) ---
PIN_TOL = 1e-8        # |k2* - edge| for "pinned on the edge".  Node 15's pin
#                       sits at ~1e-10; the recheck's own cutoff residuals at
#                       these nodes are 1e-14..1e-11, so 1e-8 is two-plus
#                       orders looser than the solver's own settling scale and
#                       three orders tighter than the nearest inter-edge gap.
FP_TOL = 1e-9         # cutoff_scale for "this really is a located fixed point"
JUMP_MIN = 1e-6       # both one-sided |U_H - U_V| must exceed this for the gap
#                       to have JUMPED through zero rather than wobbled at the
#                       floating-point floor.  Node 15's are 1.3e-3 and 1.8e-3.
JUMP_DELTAS = (1e-3, 1e-5, 1e-7, 1e-9)   # one-sided offsets, node-15's set
JUMP_REF_DELTA = 1e-5                     # the offset quoted as "the" limit
DEV_FACTOR = 3.0      # manifestation B: |worst deviation| within this factor
#                       of the matching one-sided jump value.  Node 15's
#                       pinned case matches to 3 significant figures; a factor
#                       of 3 allows the dev grid to miss the edge's immediate
#                       neighbourhood without breaking the identification.
REPRO_RTOL = 1e-6     # reproduction of a recheck basin (parent's own rel_tol)
SIGMA_TOL = 1e-3      # replication of a6_A probe 5(b)'s 3-dp sigma_s figures
BRACKET_MIN_CONFIGS = 2   # independent configurations needed for a bracket
# One further tolerance is written inline rather than named here, because it
# gates NOTHING and naming it beside the gating thresholds would imply it does:
# the rel_tol = 5e-3 inside signature (i)'s
# ``payoff_scale_equals_one_sided_jump``.  That field RECORDS whether a pinned
# configuration's payoff residual coincides with the larger one-sided jump
# value; the manifestation-A verdict turns on
# ``jumps_through_zero_without_crossing`` alone, and the field does not exist
# at a manifestation-B node.  It is reported evidence, never a gate.

SWEEP_LO, SWEEP_HI, SWEEP_N = 1.30, 2.10, 33   # a6_B_node15.py's own grid
EDGE_BRACKET = 1e-7                             # a6_B_node15.py's own offset
K1_SWEEP = 1.20                                 # a6_B_node15.py's own fixed k1
K1_GATE_VALUES = (0.90, 1.05, 1.20, 1.40, 1.52)  # probe-2A analogue
K1_GATE_TOL = 1e-6      # T bit-identity in probe 2A was <= 4.4e-16; 1e-6 is a
#                         deliberately loose gate -- it asks whether the 1-D
#                         reduction is USABLE, not whether it is exact.
MAX_CROSSING_SOLVES = 3   # bound on solve_policy calls spent locating interior
#                           (non-edge) crossing fixed points per node
MAX_FP_ITERS = 6          # T-iterations allowed to confirm a candidate pin

# ---------------------------------------------------------------------------
# THE THREE NODES.  (kappa=0.15, tau=0.05, T=5) is deliberately EXCLUDED: it is
# the node the panel already probed, and its numbers are the reference the
# thresholds above were set against.
# ---------------------------------------------------------------------------

NODES = [
    {"kappa": 0.15, "tau": 0.075, "T": 1},
    {"kappa": 0.85, "tau": 0.05, "T": 5},
    {"kappa": 0.85, "tau": 0.075, "T": 1},
]

# ---------------------------------------------------------------------------
# TICKET-34 RECHECK BASINS -- literals transcribed from
# quality_reports/fixes/t2_p1_fournode_recheck.json ("checks" -> "seeds",
# grouped by landed k to 9 dp; the representative row of each group is the one
# with the smallest cutoff_scale).  Following the parent script's own
# PRIOR_5SEED precedent.  "achieving" marks the basin the parent script's
# achieving seed lands in (smallest payoff_scale), i.e. the node's recorded
# best.  ``repro_seed`` is the seed re-solved here as the reproduction check.
# ---------------------------------------------------------------------------

RECHECK = {
    (0.15, 0.075, 1): {
        "recorded_best_payoff_scale": 0.0010592282016552504,
        "recorded_best_cutoff_scale": 1.1213252548714081e-14,
        "recorded_verdict": "STILL UNRESOLVED after 30 seeds",
        "basins": [
            {"k": [1.0039258750649935, 1.5361669836567857],
             "payoff_scale": 0.0010592282019120242,
             "cutoff_scale": 2.0159207636538667e-11,
             "slopes": [-0.0053576803046156965, -0.03869488216963479],
             "seeds": [0, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 17, 19, 20, 21,
                       24, 25],
             "n_seeds": 17, "repro_seed": 7, "achieving": True},
            {"k": [0.9928783153285407, 1.4601789933082776],
             "payoff_scale": 0.0013980610500300764,
             "cutoff_scale": 1.1213252548714081e-14,
             "slopes": [-0.0052193590539817425, 93.1652201244356],
             "seeds": [1, 6, 13, 14, 15, 18, 23, 26, 27, 28],
             "n_seeds": 10, "repro_seed": 14, "achieving": False},
            {"k": [1.001407217606027, 1.4494929696092664],
             "payoff_scale": 0.001936536613003921,
             "cutoff_scale": 0.10524616762963457,
             "slopes": [-0.0051994845214065055, -0.037101851608004055],
             "seeds": [16, 22, 29],
             "n_seeds": 3, "repro_seed": 16, "achieving": False,
             "not_a_fixed_point": "cutoff_scale 0.105 -- these three seeds did "
                                  "not converge; recorded for completeness and "
                                  "excluded from every signature"},
        ],
    },
    (0.85, 0.05, 5): {
        "recorded_best_payoff_scale": 0.00039841768805815025,
        "recorded_best_cutoff_scale": 1.98498995018781e-11,
        "recorded_verdict": "STILL UNRESOLVED after 30 seeds",
        "basins": [
            {"k": [1.0871354370855315, 1.548848450753438],
             "payoff_scale": 0.00039841768845651215,
             "cutoff_scale": 2.027711332175386e-11,
             "slopes": [-0.005380210067740253, -0.03880492667404645],
             "seeds": [s for s in range(30) if s != 6],
             "n_seeds": 29, "repro_seed": 27, "achieving": True},
            {"k": [1.0775987377716223, 1.6077221844186775],
             "payoff_scale": 0.0007586733373637772,
             "cutoff_scale": 1.98498995018781e-11,
             "slopes": [-0.00548250886321655, -0.039321563469196796],
             "seeds": [6],
             "n_seeds": 1, "repro_seed": 6, "achieving": False},
        ],
    },
    (0.85, 0.075, 1): {
        "recorded_best_payoff_scale": 0.0003061479139972942,
        "recorded_best_cutoff_scale": 1.866240495473903e-11,
        "recorded_verdict": "STILL UNRESOLVED after 30 seeds",
        "basins": [
            {"k": [1.0888618834359949, 1.5387849788310486],
             "payoff_scale": 0.0003061479142480797,
             "cutoff_scale": 1.866240495473903e-11,
             "slopes": [-0.005362345141882162, -0.03871753668956146],
             "seeds": list(range(30)),
             "n_seeds": 30, "repro_seed": 16, "achieving": True},
        ],
    },
}

# a6_A_findings.md probe 5(b), verbatim: distance from each solved k2* to the
# nearest death surface, in sigma_s, for the four payoff-unresolved nodes, in
# the ticket-34 node order.  "NO CORRELATION -- do not claim one."
RECORDED_SIGMA_DISTANCE = {
    (0.15, 0.05, 5): 0.031,      # node 15, the already-probed one (reference)
    (0.15, 0.075, 1): 0.026,
    (0.85, 0.05, 5): 0.044,
    (0.85, 0.075, 1): 0.030,
}

NODE15_REFERENCE = {
    "node": {"kappa": 0.15, "tau": 0.05, "T": 5},
    "source": "quality_reports/fixes/a6_panel_probes_2026-08-27/"
              "a6_B_node15.py|.json, a6_B_resid.py, a6_B_argmax.py, "
              "a6_B_alt.py; a6_B_findings.md 4d/4e/4f; a6_A_findings.md "
              "probe 5(b)",
    "pinned_fixed_point_k": [1.0202217805248246, 1.6590621627461504],
    "pinned_edge": 1.659062163,
    "pinned_payoff_scale": 0.0017657302401005992,
    "pinned_cutoff_scale": 5.340172748447003e-13,
    "gap_below_edge": -1.765771e-03,
    "gap_above_edge": +1.278166e-03,
    "n_below_edge": 8,
    "n_above_edge": 7,
    "interior_crossing_fixed_point_k2": 1.7104049079,
    "interior_crossing_payoff_scale": 3.055e-04,
    "recorded_best_payoff_scale": 0.001488170939392311,
    "bracket": "3.055e-04 <= 1.4882e-03 <= 1.7657e-03",
}

results: dict = {"checks": [], "n_fail": 0}


# ---------------------------------------------------------------------------
# Plumbing
# ---------------------------------------------------------------------------


def _checkpoint() -> None:
    """Atomic write: temp file + os.replace (the parent script's pattern)."""
    tmp = OUT + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(results, fh, indent=2, default=float)
    os.replace(tmp, OUT)


def record(name: str, ok: bool, kind: str, detail: dict) -> None:
    results["checks"].append({"name": name, "kind": kind, "pass": bool(ok), **detail})
    if not ok:
        results["n_fail"] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} ({kind})", flush=True)


def node_params(kappa: float, tau: float, T: int) -> ParamsV4:
    """Identical construction to t2_p1_fournode_recheck.node_params -- see that
    script's docstring for why replaying baseline_frozen() is unnecessary."""
    return ParamsV4.baseline().replace(kappa=float(kappa), tau=float(tau), T=int(T))


# ---------------------------------------------------------------------------
# The two candidate-edge families, computed exactly as menu.py computes them
# and, like menu.py's, independent of k.
# ---------------------------------------------------------------------------


def n_edges(p: ParamsV4) -> list[float]:
    """Jump points of n(s): n_scale*(H+1)*(1 - g(x)) = m, m = 1..H+1.

    Verbatim from menu.py::breakpoints, and identical to a6_B_node15.py's own
    edge construction.  Independent of kappa, tau and T, hence the same list at
    all four nodes.
    """
    out = []
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            out.append(p.mu_v + p.sigma_s * _sigmoid_inv(g))
    return sorted(out)


def tau_edges(p: ParamsV4) -> list[float]:
    """tau-crossing pullbacks, verbatim from menu.py::breakpoints.

    a6_B_findings.md Section 7 lists these as UNCHECKED; they move with tau,
    so the tau = 0.075 nodes carry a different (and much denser) list than the
    tau = 0.05 ones.
    """
    out = []
    for n in range(1, p.H + 2):
        for d in range(p.H + 1):
            y = p.b0 + (p.tau - p.b0) * n / min(d + 1, n)
            if p.b0 < y < p.b_bar:
                s = b_star_inverse(y, p)
                if not math.isnan(s):
                    out.append(float(s))
    # menu.py merges near-duplicates at 1e-9 after sorting; do the same.
    out = sorted(out)
    keep = [x for i, x in enumerate(out) if i == 0 or x - out[i - 1] > 1e-9]
    return keep


def nearest(x: float, pts: list[float]) -> tuple[float, float]:
    """(nearest point, signed distance x - point)."""
    if not pts:
        return (float("nan"), float("inf"))
    e = min(pts, key=lambda q: abs(x - q))
    return (float(e), float(x - e))


# ---------------------------------------------------------------------------
# Payoff-gap machinery (read-only reimplementation of what solver.py does, so
# the argmax LOCATION can be recorded -- equilibrium_residual returns only the
# maximum, not where it is attained)
# ---------------------------------------------------------------------------


def payoffs(res, s: float, p: ParamsV4) -> dict:
    return {j: plan_payoff(j, float(s), res, p) for j in (EXIT, HOLD, VOICE)}


def one_sided_gap(e: float, res, p: ParamsV4, relevant: str = "HV") -> dict:
    """U_HOLD - U_VOICE (and U_EXIT - U_HOLD) either side of a candidate edge.

    Mirrors a6_B_resid.py's own offsets.  Returns the two one-sided limits at
    JUMP_REF_DELTA plus the full offset ladder, so a reader can see the limits
    converge rather than take the reference offset on trust.  ``relevant``
    selects which adjacent-plan difference the jump verdict is read off:
    "HV" (Hold vs Voice, the k_2 cutoff -- node 15's case and every pin found
    so far) or "EH" (Exit vs Hold, the k_1 cutoff).
    """
    ladder = []
    for d in JUMP_DELTAS:
        for sgn in (-1.0, +1.0):
            s = e + sgn * d
            if not (p.s_lo <= s <= p.s_hi):
                continue
            u = payoffs(res, s, p)
            ladder.append({
                "offset": sgn * d,
                "n_days": int(n_days(s, p)),
                "U_EXIT": u[EXIT], "U_HOLD": u[HOLD], "U_VOICE": u[VOICE],
                "gap_HV": u[HOLD] - u[VOICE],
                "gap_EH": u[EXIT] - u[HOLD],
                "argmax": PLAN_NAME[max(u, key=u.get)],
            })
    below = [r for r in ladder if r["offset"] == -JUMP_REF_DELTA]
    above = [r for r in ladder if r["offset"] == +JUMP_REF_DELTA]
    b = below[0] if below else None
    a = above[0] if above else None
    fld = "gap_HV" if relevant == "HV" else "gap_EH"
    jumps = False
    if b is not None and a is not None:
        jumps = (
            b[fld] * a[fld] < 0.0
            and abs(b[fld]) > JUMP_MIN
            and abs(a[fld]) > JUMP_MIN
        )
    return {
        "edge": float(e),
        "relevant_adjacent_pair": ("U_HOLD - U_VOICE" if relevant == "HV"
                                   else "U_EXIT - U_HOLD"),
        "reference_offset": JUMP_REF_DELTA,
        "gap_below": b[fld] if b else None,
        "gap_above": a[fld] if a else None,
        "gap_HV_below": b["gap_HV"] if b else None,
        "gap_HV_above": a["gap_HV"] if a else None,
        "gap_EH_below": b["gap_EH"] if b else None,
        "gap_EH_above": a["gap_EH"] if a else None,
        "n_days_below": b["n_days"] if b else None,
        "n_days_above": a["n_days"] if a else None,
        "argmax_below": b["argmax"] if b else None,
        "argmax_above": a["argmax"] if a else None,
        "n_days_changes": (b["n_days"] != a["n_days"]) if (b and a) else None,
        "jumps_through_zero_without_crossing": bool(jumps),
        "criterion": (f"opposite strict signs of "
                      f"{'U_HOLD - U_VOICE' if relevant == 'HV' else 'U_EXIT - U_HOLD'}"
                      f" at edge -+ {JUMP_REF_DELTA:g}, both magnitudes above "
                      f"{JUMP_MIN:g}"),
        "offset_ladder": ladder,
    }


def worst_deviation(k: tuple, p: ParamsV4, res) -> dict:
    """Re-walk equilibrium_residual's dev grid, recording WHERE the maximum is.

    The loop below is solver.equilibrium_residual's own, line for line (same
    grid, same DEV_OFFSETS, same 'chosen' rule, same adjacent-alternative set);
    the only addition is that it remembers the argmax location and the chosen
    and alternative plan.  Its returned maximum matches
    equilibrium_residual's payoff_scale at all located entries in this run;
    that agreement is observed, NOT asserted -- there is no assert here or in
    any caller, so a reader checking the two numbers is checking a fact about
    the run, not a guarantee the code enforces.
    """
    dev_grid = list(np.linspace(p.s_lo, p.s_hi, N_GRID))
    for cut in k:
        for off in DEV_OFFSETS:
            dev_grid += [cut - off, cut + off]
    worst, at_s, chosen_j, alt_j = 0.0, None, None, None
    for s in dev_grid:
        s = float(s)
        if not (p.s_lo <= s <= p.s_hi):
            continue
        u = payoffs(res, s, p)
        chosen = EXIT if s < k[0] else (HOLD if s < k[1] else VOICE)
        for alt in (chosen - 1, chosen + 1):
            if alt in u and u[alt] - u[chosen] > worst:
                worst, at_s, chosen_j, alt_j = u[alt] - u[chosen], s, chosen, alt
    return {
        "worst_payoff_deviation": float(worst),
        "at_s": at_s,
        "chosen_plan": PLAN_NAME.get(chosen_j),
        "alternative_plan": PLAN_NAME.get(alt_j),
        "n_days_at_s": int(n_days(at_s, p)) if at_s is not None else None,
        "note": "re-walk of solver.equilibrium_residual's own dev grid "
                "(linspace(s_lo, s_hi, N_GRID) plus each cutoff -+ "
                "DEV_OFFSETS); identical maximand, argmax location added",
    }


def evaluate_at(k: tuple, p: ParamsV4) -> dict:
    """One pooled pass + equilibrium_residual AT the given k -- no iteration.

    This is what the ticket-34 recheck itself recorded for each landed basin,
    so it is the only faithful reproduction of a recheck basin's numbers.
    Iterating first would move a basin that did NOT converge (one of node
    (0.15, 0.075, 1)'s three basins has cutoff_scale 0.105) and would then
    report a spurious reproduction mismatch against a number that was never
    claimed to be a fixed point.
    """
    k = (float(k[0]), float(k[1]))
    res = pooled_pass(atoms(k, p), p, with_runup=True)
    r = equilibrium_residual(k, p, res)
    return {
        "k": [k[0], k[1]],
        "cutoff_scale": float(r.cutoff_scale),
        "payoff_scale": float(r.payoff_scale),
        "slopes": [float(x) for x in r.slopes],
        "meets_cutoff_criterion": bool(r.cutoff_scale < TOL_EXIST_CUTOFF),
        "meets_payoff_criterion": bool(r.payoff_scale <= TOL_EXIST_PAYOFF),
        "is_located_fixed_point": bool(r.cutoff_scale < FP_TOL),
        "iterations": None,
        "_res": res,
    }


def confirm_fixed_point(k0: tuple, p: ParamsV4) -> dict:
    """Iterate T from k0 (undamped) until the cutoff residual settles.

    A candidate produced by the k_2 sweep has its k_1 coordinate taken from a
    single T evaluation; one or two further T applications settle both
    coordinates.  Undamped rather than damped on purpose: damping is what makes
    the solver's own iteration skate past a pinned point, and the question here
    is whether the point IS fixed, not whether the shipped iteration finds it.
    """
    k = (float(k0[0]), float(max(k0[1], k0[0])))
    trace = []
    res = None
    for it in range(MAX_FP_ITERS):
        res = pooled_pass(atoms(k, p), p, with_runup=True)
        Tk = outer_map(k, p, res)
        step = max(abs(Tk[0] - k[0]), abs(Tk[1] - k[1]))
        trace.append({"iter": it, "k": [k[0], k[1]], "T": [Tk[0], Tk[1]],
                      "step": float(step)})
        if step < FP_TOL:
            break
        k = (float(Tk[0]), float(max(Tk[1], Tk[0])))
    res = pooled_pass(atoms(k, p), p, with_runup=True)
    r = equilibrium_residual(k, p, res)
    return {
        "k": [float(k[0]), float(k[1])],
        "cutoff_scale": float(r.cutoff_scale),
        "payoff_scale": float(r.payoff_scale),
        "slopes": [float(x) for x in r.slopes],
        "meets_cutoff_criterion": bool(r.cutoff_scale < TOL_EXIST_CUTOFF),
        "meets_payoff_criterion": bool(r.payoff_scale <= TOL_EXIST_PAYOFF),
        "is_located_fixed_point": bool(r.cutoff_scale < FP_TOL),
        "iterations": trace,
        "_res": res,
    }


# ---------------------------------------------------------------------------
# Per-node stages
# ---------------------------------------------------------------------------


def stage_k1_gate(p: ParamsV4, k2_probe: float) -> dict:
    """probe-2A analogue: does T depend on k only through k_2 at this node?"""
    rows = []
    for k1 in K1_GATE_VALUES:
        if k1 >= k2_probe:
            continue
        res = pooled_pass(atoms((k1, k2_probe), p), p, with_runup=True)
        T = outer_map((k1, k2_probe), p, res)
        rows.append({"k1": float(k1), "T": [float(T[0]), float(T[1])]})
    spread1 = max(r["T"][0] for r in rows) - min(r["T"][0] for r in rows)
    spread2 = max(r["T"][1] for r in rows) - min(r["T"][1] for r in rows)
    return {
        "hypothesis": "a6_B probe 2A: Exit and Hold share mark-path type 0, so "
                      "the pooled price system -- hence T -- moves with k_2 "
                      "alone.  Measured at the baseline there; re-measured "
                      "here at this node before the 1-D sweep is trusted.",
        "k2_probe": float(k2_probe),
        "rows": rows,
        "T1_spread": float(spread1),
        "T2_spread": float(spread2),
        "tolerance": K1_GATE_TOL,
        "pass": bool(max(spread1, spread2) < K1_GATE_TOL),
    }


def stage_sweep(p: ParamsV4, k1_fixed: float, edges_n: list, edges_tau: list,
                extra_k2: list) -> dict:
    """a6_B_node15.py's 1-D k_2 sweep, with both edge families bracketed."""
    cand = sorted(set(
        [e for e in edges_n if SWEEP_LO - 0.01 < e < SWEEP_HI + 0.01]
        + [e for e in edges_tau if SWEEP_LO - 0.01 < e < SWEEP_HI + 0.01]
    ))
    grid = sorted(set(
        [round(float(x), 12) for x in np.linspace(SWEEP_LO, SWEEP_HI, SWEEP_N)]
        + [round(e - EDGE_BRACKET, 12) for e in cand]
        + [round(e, 12) for e in cand]
        + [round(e + EDGE_BRACKET, 12) for e in cand]
        + [round(float(x), 12) for x in extra_k2]
    ))
    rows = []
    for k2 in grid:
        if k2 <= k1_fixed:
            continue
        res = pooled_pass(atoms((k1_fixed, k2), p), p, with_runup=True)
        T = outer_map((k1_fixed, k2), p, res)
        en, dn = nearest(k2, edges_n)
        et, dt = nearest(k2, edges_tau)
        rows.append({
            "k2": float(k2), "T1": float(T[0]), "T2": float(T[1]),
            "gap": float(T[1] - k2),
            "d_to_n_edge": float(dn), "d_to_tau_edge": float(dt),
            "n_days": int(n_days(k2, p)),
        })
    sign_changes = []
    for i in range(len(rows) - 1):
        g0, g1 = rows[i]["gap"], rows[i + 1]["gap"]
        if g0 * g1 < 0.0:
            a, b = rows[i]["k2"], rows[i + 1]["k2"]
            across = any(a - 1e-12 <= e <= b + 1e-12 for e in cand)
            sign_changes.append({
                "k2_lo": a, "k2_hi": b, "gap_lo": g0, "gap_hi": g1,
                "across_a_candidate_edge": bool(across),
                "same_cell": bool(not across),
            })
    return {
        "method": "a6_B_node15.py's grid: np.linspace(1.30, 2.10, 33) plus "
                  "every candidate edge in range at {-1e-7, 0, +1e-7}, plus "
                  "the ticket-34 recheck's own landed k_2 values",
        "k1_fixed": float(k1_fixed),
        "n_grid_points": len(rows),
        "n_candidate_edges_in_range": len(cand),
        "candidate_edges_in_range": [float(e) for e in cand],
        "sign_changes_of_T2_minus_k2": sign_changes,
        "rows": rows,
    }


def stage_edge_pins(p: ParamsV4, k1_fixed: float, edges_n: list,
                    edges_tau: list) -> list:
    """Direct pin test: is T_2(e) == e at a candidate edge e?

    This is the sharp form of the account's claim.  a6_B_node15.py found its
    pin because its grid happened to contain the edge exactly; testing each
    edge directly is the same measurement made deliberate rather than
    incidental.
    """
    cand = sorted(set(
        [(float(e), "n(s)") for e in edges_n
         if SWEEP_LO - 0.01 < e < SWEEP_HI + 0.01]
        + [(float(e), "tau-crossing") for e in edges_tau
           if SWEEP_LO - 0.01 < e < SWEEP_HI + 0.01]
    ))
    # An s that is in both families is reported once, as "n(s)+tau-crossing".
    merged: dict = {}
    for e, fam in cand:
        merged.setdefault(round(e, 12), []).append(fam)
    out = []
    for e_r, fams in sorted(merged.items()):
        e = float(e_r)
        if e <= k1_fixed:
            continue
        res = pooled_pass(atoms((k1_fixed, e), p), p, with_runup=True)
        T = outer_map((k1_fixed, e), p, res)
        out.append({
            "edge": e,
            "family": "+".join(sorted(set(fams))),
            "T_at_edge": [float(T[0]), float(T[1])],
            "T2_minus_edge": float(T[1] - e),
            "pinned": bool(abs(T[1] - e) < PIN_TOL),
        })
    return out


def stage_proximity(p: ParamsV4, key: tuple, edges_n: list,
                    edges_tau: list, basins: list) -> dict:
    """a6_A probe 5(b) replication, plus the per-basin (distance, payoff) pairs."""
    per_basin = []
    for b in basins:
        k2 = b["k"][1]
        en, dn = nearest(k2, edges_n)
        et, dt = nearest(k2, edges_tau)
        per_basin.append({
            "k2": k2, "payoff_scale": b["payoff_scale"],
            "cutoff_scale": b["cutoff_scale"], "n_seeds": b["n_seeds"],
            "achieving": b["achieving"],
            "nearest_n_edge": en, "distance_to_n_edge": abs(dn),
            "distance_in_sigma_s": abs(dn) / p.sigma_s,
            "nearest_tau_edge": et, "distance_to_tau_edge": abs(dt),
            "edge_pinned": bool(min(abs(dn), abs(dt)) < PIN_TOL),
        })
    ach = next(r for r in per_basin if r["achieving"])
    recorded = RECORDED_SIGMA_DISTANCE[key]
    replicates = abs(ach["distance_in_sigma_s"] - recorded) < SIGMA_TOL
    return {
        "recorded_by_a6_A_probe_5b_sigma_s": recorded,
        "measured_at_achieving_basin_sigma_s": ach["distance_in_sigma_s"],
        "abs_difference": abs(ach["distance_in_sigma_s"] - recorded),
        "tolerance": SIGMA_TOL,
        "recorded_distance_replicates": bool(replicates),
        "achieving_basin_edge_pinned": bool(ach["edge_pinned"]),
        "pass": bool(replicates and not ach["edge_pinned"]),
        "per_basin": per_basin,
        "correlation_note": (
            "a6_A probe 5(b)'s negative ('NO CORRELATION -- do not claim one') "
            "is a CROSS-node statement: the four unresolved nodes' solved "
            "cutoffs sit no closer to the discontinuity surfaces than the "
            "converged nodes' do.  Only its per-node inputs are replicated "
            f"here.  This node has {len(per_basin)} distinct basin(s); no "
            "within-node correlation is computed and none should be read in, "
            "in either direction."
        ),
    }


def analyse_node(node: dict) -> dict:
    """Run the whole battery at one node and return its three-way call."""
    t0 = time.perf_counter()
    key = (node["kappa"], node["tau"], node["T"])
    p = node_params(*key)
    rc = RECHECK[key]
    basins = rc["basins"]
    achieving = next(b for b in basins if b["achieving"])
    edges_n, edges_tau = n_edges(p), tau_edges(p)
    print(f"\n=== node kappa={key[0]} tau={key[1]} T={key[2]} "
          f"(H={p.H}, sigma_s={p.sigma_s:.9f}) ===", flush=True)
    print(f"    n(s) edges in [1.29,2.11]: "
          f"{[round(e,9) for e in edges_n if 1.29 < e < 2.11]}", flush=True)
    print(f"    tau-crossing pullbacks in [1.29,2.11]: "
          f"{[round(e,9) for e in edges_tau if 1.29 < e < 2.11]}", flush=True)

    # -- stage 1: the 1-D reduction gate ------------------------------------
    gate = stage_k1_gate(p, achieving["k"][1])
    k1_fixed = K1_SWEEP
    adaptation = None
    if not gate["pass"]:
        k1_fixed = float(achieving["k"][0])
        adaptation = (
            "k_1-invariance gate did not pass at this node "
            f"(T1 spread {gate['T1_spread']:.3e}, T2 spread "
            f"{gate['T2_spread']:.3e} over k_1 in {list(K1_GATE_VALUES)}); the "
            f"sweep was run at k_1 = {k1_fixed!r}, this node's achieving k_1, "
            "instead of node 15's 1.20.  The sweep is only a locator -- every "
            "candidate it yields is confirmed by a full two-coordinate "
            "equilibrium_residual call, which does not use the reduction."
        )
    print(f"    [gate] k1-invariance {'PASS' if gate['pass'] else 'FAIL'} "
          f"(T1 spread {gate['T1_spread']:.2e}, T2 spread "
          f"{gate['T2_spread']:.2e}); sweep k1 = {k1_fixed}", flush=True)

    # -- stage 2: the k_2 sweep ---------------------------------------------
    sweep = stage_sweep(p, k1_fixed, edges_n, edges_tau,
                        [b["k"][1] for b in basins])
    print(f"    [sweep] {sweep['n_grid_points']} points, "
          f"{len(sweep['sign_changes_of_T2_minus_k2'])} sign change(s) of "
          f"T_2(k_2) - k_2 "
          f"({sum(1 for s in sweep['sign_changes_of_T2_minus_k2'] if s['same_cell'])}"
          " within a single cell)", flush=True)

    # -- stage 3: direct edge-pin tests -------------------------------------
    pins = stage_edge_pins(p, k1_fixed, edges_n, edges_tau)
    pinned = [q for q in pins if q["pinned"]]
    print(f"    [pins] {len(pinned)} of {len(pins)} candidate edges satisfy "
          f"|T_2(e) - e| < {PIN_TOL:g}: "
          f"{[round(q['edge'], 9) for q in pinned]}", flush=True)

    # -- stage 4: locate and confirm fixed points ---------------------------
    located = []

    #    4a. the recheck's own basins, re-evaluated AT their landed k
    for b in basins:
        conf = evaluate_at(tuple(b["k"]), p)
        res = conf.pop("_res")
        dev = worst_deviation(tuple(conf["k"]), p, res)
        en, dn = nearest(conf["k"][1], edges_n)
        et, dt = nearest(conf["k"][1], edges_tau)
        located.append({
            "origin": "ticket-34 recheck basin",
            "recheck_basin_k": b["k"],
            "recheck_basin_payoff_scale": b["payoff_scale"],
            "recheck_basin_cutoff_scale": b["cutoff_scale"],
            "recheck_basin_n_seeds": b["n_seeds"],
            "recheck_basin_seeds": b["seeds"],
            "recheck_basin_seeds_note": f"{b['n_seeds']} of the 30 seeds "
                                        "(0..29) landed here "
                                        "(t2_p1_fournode_recheck.json)",
            "achieving": b["achieving"],
            "independent_of_achieving_basin": not b["achieving"],
            "nearest_n_edge": en, "offset_from_n_edge": dn,
            "nearest_tau_edge": et, "offset_from_tau_edge": dt,
            "edge_pinned": bool(min(abs(dn), abs(dt)) < PIN_TOL),
            "worst_deviation": dev,
            **conf,
        })

    #    4b. every pinned edge the direct test found
    for q in pinned:
        conf = confirm_fixed_point((k1_fixed, q["edge"]), p)
        res = conf.pop("_res")
        dev = worst_deviation(tuple(conf["k"]), p, res)
        en, dn = nearest(conf["k"][1], edges_n)
        et, dt = nearest(conf["k"][1], edges_tau)
        already = any(abs(L["k"][1] - conf["k"][1]) < 1e-9 for L in located)
        located.append({
            "origin": f"direct edge-pin test at {q['family']} edge "
                      f"{q['edge']!r}",
            "duplicate_of_a_recheck_basin": bool(already),
            "achieving": False,
            "independent_of_achieving_basin": True,
            "nearest_n_edge": en, "offset_from_n_edge": dn,
            "nearest_tau_edge": et, "offset_from_tau_edge": dt,
            "edge_pinned": bool(min(abs(dn), abs(dt)) < PIN_TOL),
            "worst_deviation": dev,
            **conf,
        })

    #    4c. interior (non-edge) crossings the sweep flagged -- node 15's
    #        k_init = (1.02, 1.71) route, generalised
    same_cell = [s for s in sweep["sign_changes_of_T2_minus_k2"] if s["same_cell"]]
    for sc in same_cell[:MAX_CROSSING_SOLVES]:
        mid = 0.5 * (sc["k2_lo"] + sc["k2_hi"])
        k_init = (float(achieving["k"][0]), float(mid))
        pol, r = solve_policy(p, k_init=k_init)
        k = [float(pol.k[0]), float(pol.k[1])]
        res = pooled_pass(atoms(tuple(k), p), p, with_runup=True)
        dev = worst_deviation(tuple(k), p, res)
        en, dn = nearest(k[1], edges_n)
        et, dt = nearest(k[1], edges_tau)
        already = any(abs(L["k"][1] - k[1]) < 1e-9 for L in located)
        located.append({
            "origin": f"solve_policy from k_init = {list(k_init)!r} (interior "
                      f"sign change of T_2 - k_2 in [{sc['k2_lo']!r}, "
                      f"{sc['k2_hi']!r}], no candidate edge between)",
            "duplicate_of_a_recheck_basin": bool(already),
            "achieving": False,
            "independent_of_achieving_basin": True,
            "k": k,
            "cutoff_scale": float(r.cutoff_scale),
            "payoff_scale": float(r.payoff_scale),
            "slopes": [float(x) for x in r.slopes],
            "meets_cutoff_criterion": bool(r.cutoff_scale < TOL_EXIST_CUTOFF),
            "meets_payoff_criterion": bool(r.payoff_scale <= TOL_EXIST_PAYOFF),
            "is_located_fixed_point": bool(r.cutoff_scale < FP_TOL),
            "nearest_n_edge": en, "offset_from_n_edge": dn,
            "nearest_tau_edge": et, "offset_from_tau_edge": dt,
            "edge_pinned": bool(min(abs(dn), abs(dt)) < PIN_TOL),
            "worst_deviation": dev,
        })
    for L in located:
        print(f"    [fp] k2={L['k'][1]:.10f}  cutoff={L['cutoff_scale']:.3e}  "
              f"payoff={L['payoff_scale']:.4e}  pinned={L['edge_pinned']}  "
              f"({L['origin'][:48]})", flush=True)

    # -- stage 5: reproduction spot-checks (one seed per recheck basin) ------
    repro = []
    for b in basins:
        pol, r = solve_policy(p, seed=int(b["repro_seed"]))
        k = [float(pol.k[0]), float(pol.k[1])]
        ok_k = all(math.isclose(k[i], b["k"][i], rel_tol=REPRO_RTOL,
                                abs_tol=1e-12) for i in (0, 1))
        ok_pay = math.isclose(float(r.payoff_scale), b["payoff_scale"],
                              rel_tol=REPRO_RTOL, abs_tol=1e-12)
        ok_cut = math.isclose(float(r.cutoff_scale), b["cutoff_scale"],
                              rel_tol=REPRO_RTOL, abs_tol=1e-12)
        repro.append({
            "seed": int(b["repro_seed"]),
            "recorded_k": b["k"], "this_run_k": k,
            "recorded_payoff_scale": b["payoff_scale"],
            "this_run_payoff_scale": float(r.payoff_scale),
            "recorded_cutoff_scale": b["cutoff_scale"],
            "this_run_cutoff_scale": float(r.cutoff_scale),
            "k_reproduces": bool(ok_k),
            "payoff_reproduces": bool(ok_pay),
            "cutoff_reproduces": bool(ok_cut),
            "pass": bool(ok_k and ok_pay and ok_cut),
        })
        print(f"    [repro] seed {b['repro_seed']:2d}  k2 {k[1]:.10f} vs "
              f"{b['k'][1]:.10f}  payoff {float(r.payoff_scale):.6e} vs "
              f"{b['payoff_scale']:.6e}  -> "
              f"{'OK' if repro[-1]['pass'] else 'MISMATCH'}", flush=True)
    repro_pass = all(x["pass"] for x in repro)

    # -- signature (i): edge-pinned jump through zero ------------------------
    pinned_fps = [L for L in located
                  if L["edge_pinned"] and L["is_located_fixed_point"]]
    manifestation, sig_i_detail = None, {}
    for L in sorted(pinned_fps, key=lambda x: x["payoff_scale"], reverse=True):
        e = (L["nearest_n_edge"] if abs(L["offset_from_n_edge"])
             <= abs(L["offset_from_tau_edge"]) else L["nearest_tau_edge"])
        res = pooled_pass(atoms(tuple(L["k"]), p), p, with_runup=True)
        js = one_sided_gap(e, res, p, relevant="HV")
        below, above = js["gap_below"], js["gap_above"]
        payoff_matches_jump = (
            below is not None and above is not None
            and math.isclose(L["payoff_scale"], max(abs(below), abs(above)),
                             rel_tol=5e-3)
        )
        cand = {
            "manifestation": "A -- pinned fixed point",
            "fixed_point_k": L["k"],
            "edge": float(e),
            "edge_family": ("n(s)" if abs(L["offset_from_n_edge"])
                            <= abs(L["offset_from_tau_edge"])
                            else "tau-crossing"),
            "offset_from_edge": float(L["k"][1] - e),
            "pin_tolerance": PIN_TOL,
            "cutoff_scale": L["cutoff_scale"],
            "payoff_scale": L["payoff_scale"],
            "slope_at_k2": L["slopes"][1],
            "jump": js,
            "payoff_scale_equals_one_sided_jump": bool(payoff_matches_jump),
            "payoff_vs_larger_one_sided_jump_ratio": (
                L["payoff_scale"] / max(abs(below), abs(above))
                if (below is not None and above is not None
                    and max(abs(below), abs(above)) > 0) else None),
            "origin": L["origin"],
        }
        if js["jumps_through_zero_without_crossing"]:
            manifestation, sig_i_detail = "A", cand
            break
        sig_i_detail = sig_i_detail or cand

    if manifestation is None:
        # -- manifestation B: at-edge worst deviation at the achieving FP ----
        L = next(x for x in located if x.get("achieving"))
        dev = L["worst_deviation"]
        s_w = dev["at_s"]
        # The cutoff separating the chosen plan from the alternative it loses
        # to: k_1 for the Exit/Hold pair, k_2 for the Hold/Voice pair.
        pair = {dev["chosen_plan"], dev["alternative_plan"]}
        rel = "EH" if pair == {"EXIT", "HOLD"} else "HV"
        cutoff = L["k"][0] if rel == "EH" else L["k"][1]
        all_edges = sorted(set([float(e) for e in edges_n]
                               + [float(e) for e in edges_tau]))
        # the cell boundary lying between s_worst and the relevant cutoff
        between = [e for e in all_edges
                   if min(s_w, cutoff) < e < max(s_w, cutoff)]
        e_star = (min(between, key=lambda e: abs(e - s_w)) if between else None)
        b_detail = {
            "manifestation": "B -- at-edge deviation (no pinned fixed point)",
            "fixed_point_k": L["k"],
            "worst_deviation": dev,
            "relevant_adjacent_pair": ("U_EXIT - U_HOLD" if rel == "EH"
                                       else "U_HOLD - U_VOICE"),
            "relevant_cutoff": float(cutoff),
            "edges_between_deviation_and_cutoff": between,
            "edge": e_star,
        }
        if e_star is not None:
            res = pooled_pass(atoms(tuple(L["k"]), p), p, with_runup=True)
            js = one_sided_gap(e_star, res, p, relevant=rel)
            side = "above" if s_w > e_star else "below"
            one_sided = js[f"gap_{side}"]
            magnitude_ok = (
                one_sided is not None and one_sided != 0.0
                and 1.0 / DEV_FACTOR
                <= abs(dev["worst_payoff_deviation"] / one_sided) <= DEV_FACTOR
            )
            b_detail.update({
                "edge_family": ("n(s)" if any(abs(e_star - e) < 1e-12
                                              for e in edges_n)
                                else "tau-crossing"),
                "deviation_side_of_edge": side,
                "one_sided_gap_on_that_side": one_sided,
                "deviation_over_one_sided_gap": (
                    abs(dev["worst_payoff_deviation"] / one_sided)
                    if one_sided else None),
                "factor_tolerance": DEV_FACTOR,
                "magnitude_matches": bool(magnitude_ok),
                "jump": js,
            })
            if js["jumps_through_zero_without_crossing"] and magnitude_ok:
                manifestation = "B"
        sig_i_detail = b_detail if manifestation == "B" else (
            sig_i_detail or b_detail)
        if manifestation is None:
            sig_i_detail = {"observed_locus_instead": b_detail,
                            "pinned_fixed_point_candidates": [
                                {"k": L2["k"], "cutoff_scale": L2["cutoff_scale"],
                                 "payoff_scale": L2["payoff_scale"]}
                                for L2 in pinned_fps],
                            "note": "neither manifestation A nor B satisfied"}

    sig_i = manifestation is not None

    # -- signature (ii): reproduction and bracketing -------------------------
    # A configuration counts as INDEPENDENT only if it is a confirmed fixed
    # point, is not the achieving basin, is not a duplicate of a basin already
    # listed, and did not simply land BACK in the achieving basin by another
    # route -- otherwise the bracket could be won by re-finding the very number
    # it is supposed to bracket.
    ach_k2 = achieving["k"][1]
    indep = [L for L in located
             if L.get("independent_of_achieving_basin")
             and L["is_located_fixed_point"]
             and not L.get("duplicate_of_a_recheck_basin")
             and abs(L["k"][1] - ach_k2) > 1e-9]
    # de-duplicate by landed k_2
    seen, indep_u = set(), []
    for L in sorted(indep, key=lambda x: x["payoff_scale"]):
        key2 = round(L["k"][1], 9)
        if key2 not in seen:
            seen.add(key2)
            indep_u.append(L)
    recorded_best = rc["recorded_best_payoff_scale"]
    if len(indep_u) >= BRACKET_MIN_CONFIGS:
        lo = min(L["payoff_scale"] for L in indep_u)
        hi = max(L["payoff_scale"] for L in indep_u)
        bracket_ok = bool(lo <= recorded_best <= hi)
        bracket_state = "BRACKETS" if bracket_ok else "DOES NOT BRACKET"
    else:
        lo = hi = None
        bracket_ok, bracket_state = None, "N/A -- fewer than two independent " \
                                          "located configurations"
    # basin-level reproduction of the recheck's recorded residuals
    basin_repro = []
    for L in located:
        if L["origin"] != "ticket-34 recheck basin":
            continue
        basin_repro.append({
            "k2": L["k"][1],
            "recorded_payoff_scale": L["recheck_basin_payoff_scale"],
            "recomputed_payoff_scale": L["payoff_scale"],
            "reproduces": bool(math.isclose(L["payoff_scale"],
                                            L["recheck_basin_payoff_scale"],
                                            rel_tol=REPRO_RTOL, abs_tol=1e-12)),
        })
    sig_ii = bool(repro_pass and all(x["reproduces"] for x in basin_repro)
                  and (bracket_ok is not False))
    sig_ii_detail = {
        "recorded_best_payoff_scale": recorded_best,
        "independent_located_configurations": [
            {"k2": L["k"][1], "payoff_scale": L["payoff_scale"],
             "cutoff_scale": L["cutoff_scale"], "edge_pinned": L["edge_pinned"],
             "origin": L["origin"]} for L in indep_u],
        "bracket_low": lo, "bracket_high": hi,
        "brackets_recorded_best": bracket_ok,
        "bracket_state": bracket_state,
        "achieving_basin_excluded_from_bracket": True,
        "seed_reproduction_spot_checks": repro,
        "basin_residual_reproduction": basin_repro,
        "pass": bool(sig_ii),
    }

    # -- signature (iii): the proximity negative -----------------------------
    prox = stage_proximity(p, key, edges_n, edges_tau, basins)
    sig_iii = bool(prox["pass"])

    # -- the pre-registered call --------------------------------------------
    # "Clean" is about the integrity of THIS diagnostic: the 1-D reduction gate
    # resolved, the recheck's own numbers reproduced, and the configuration the
    # call actually rests on confirmed as a located fixed point.  An auxiliary
    # pin candidate that lands in limbo (|T_2(e) - e| below PIN_TOL but above
    # FP_TOL) is recorded and excluded, not allowed to poison the node: it
    # bears no weight in the call either way.
    call_bearing = (
        sig_i_detail.get("fixed_point_k") if manifestation
        else next(x for x in located if x.get("achieving"))["k"]
    )
    call_bearing_confirmed = any(
        L["is_located_fixed_point"]
        and abs(L["k"][1] - call_bearing[1]) < 1e-9
        for L in located
    ) if call_bearing is not None else False
    unconfirmed_pins = [
        {"k": L["k"], "cutoff_scale": L["cutoff_scale"], "origin": L["origin"]}
        for L in located
        if L["edge_pinned"] and not L["is_located_fixed_point"]
    ]
    diagnostic_clean = bool(
        repro_pass
        and all(x["reproduces"] for x in basin_repro)
        and (gate["pass"] or adaptation is not None)
        and call_bearing_confirmed
    )
    if sig_i and sig_ii and sig_iii:
        account = "HOLDS"
        why = (f"signature (i) satisfied in manifestation {manifestation}, "
               "and (ii) and (iii) both satisfied")
    elif (not sig_i) and diagnostic_clean:
        # The account's own mechanism is absent.  Signatures (ii) and (iii) are
        # reported but do NOT gate this branch: (ii)'s bracketing is part of
        # the account, so its failing alongside (i) is further evidence for
        # this call, not against it.  What does gate it is diagnostic
        # integrity, which is what diagnostic_clean carries.
        account = "DIFFERENT MECHANISM"
        why = ("no edge-pinned fixed point and no at-edge worst deviation at "
               "this node, with the diagnostic itself clean (k_1 gate "
               "resolved, seed reproductions and basin residuals agreed, "
               "call-bearing configuration confirmed); the observed locus is "
               "recorded.  Signatures (ii) and (iii) are reported alongside "
               f"((ii) {'satisfied' if sig_ii else 'not satisfied'}, "
               f"(iii) {'satisfied' if sig_iii else 'not satisfied'}) and do "
               "not gate this call")
    else:
        account = "INCONCLUSIVE"
        parts = []
        if sig_i and not sig_ii:
            parts.append("signature (i) present but (ii) not satisfied")
        if sig_i and not sig_iii:
            parts.append("signature (i) present but (iii) not satisfied")
        if not diagnostic_clean:
            parts.append("diagnostic obstructed (see diagnostic_integrity)")
        why = "mixed result: " + "; ".join(parts)

    seconds = time.perf_counter() - t0
    print(f"=== node kappa={key[0]} tau={key[1]} T={key[2]}: "
          f"account = {account}  ({seconds:.0f}s) ===", flush=True)

    for L in located:
        L.pop("_res", None)

    return {
        "node": {"kappa": key[0], "tau": key[1], "T": key[2],
                 "H": p.H, "sigma_s": p.sigma_s},
        "params_hash": p.hash_str(),
        "account": account,
        "account_reason": why,
        "seconds": seconds,
        "ticket34_record": {
            "verdict": rc["recorded_verdict"],
            "best_payoff_scale": rc["recorded_best_payoff_scale"],
            "best_cutoff_scale": rc["recorded_best_cutoff_scale"],
            "n_distinct_basins_over_30_seeds": len(basins),
            "seeds_used": {
                "recheck_seeds": list(range(30)),
                "grouping": {f"k2={b['k'][1]!r}": b["seeds"] for b in basins},
                "re_solved_here": [b["repro_seed"] for b in basins],
                "note": "all 30 of t2_p1_fournode_recheck.py's seeds (0..29), "
                        "grouped by the k they landed at; one seed per basin "
                        "is re-solved here as the reproduction check",
            },
        },
        "recheck_basins": basins,
        "edges": {
            "n_s_family": [float(e) for e in edges_n],
            "tau_crossing_family": [float(e) for e in edges_tau],
            "n_s_in_sweep_range": [float(e) for e in edges_n
                                   if SWEEP_LO < e < SWEEP_HI],
            "tau_crossing_in_sweep_range": [float(e) for e in edges_tau
                                            if SWEEP_LO < e < SWEEP_HI],
            "note": "both families computed exactly as menu.py::breakpoints "
                    "computes them, and like it independent of k; the n(s) "
                    "family is also independent of kappa, tau and T, so it is "
                    "the same list at all four ticket-34 nodes",
        },
        "signature_i_edge_pinned_jump": {
            "satisfied": bool(sig_i),
            "manifestation": manifestation,
            **sig_i_detail,
        },
        "signature_ii_residuals": sig_ii_detail,
        "signature_iii_proximity_negative": prox,
        "k1_invariance_gate": gate,
        "method_adaptation": adaptation,
        "sweep": sweep,
        "edge_pin_tests": pins,
        "located_fixed_points": located,
        "diagnostic_clean": diagnostic_clean,
        "diagnostic_integrity": {
            "k1_gate_resolved": bool(gate["pass"] or adaptation is not None),
            "seed_reproductions_agree": bool(repro_pass),
            "basin_residuals_reproduce": bool(
                all(x["reproduces"] for x in basin_repro)),
            "call_bearing_configuration_k": call_bearing,
            "call_bearing_configuration_confirmed": bool(call_bearing_confirmed),
            "unconfirmed_pin_candidates": unconfirmed_pins,
            "note": "an edge-pin candidate with |T_2(e) - e| below PIN_TOL but "
                    "cutoff_scale above FP_TOL is recorded here and excluded "
                    "from every signature; it bears no weight in the call",
        },
    }


# ---------------------------------------------------------------------------


def main() -> int:
    t0 = time.perf_counter()
    print("t2_t34_account_sweep -- ticket 34's candidate mechanical account, "
          "swept over the three unprobed nodes.", flush=True)
    print(f"Nodes: {NODES}", flush=True)

    results["provenance"] = {
        "ticket": "34 (R4) follow-up -- the standing 'sweep the account over "
                  "the other three nodes' item",
        "account_under_test": (
            "a located fixed point of the implemented cutoff map sits ON an "
            "n(s) cell edge, where U_HOLD - U_VOICE jumps through zero "
            "without crossing it (n(s) is integer-valued, so U_VOICE steps in "
            "s); brentq inside solver.outer_map then converges on the jump "
            "rather than on a root, so the cutoff-scale residual vanishes "
            "while the payoff-scale residual stays at the size of the jump's "
            "one-sided value"
        ),
        "sources": {
            "one_node_probe": "quality_reports/fixes/a6_panel_probes_2026-08-27/"
                              "a6_B_node15.py|.json (the k_2 sweep and the "
                              "pin), with a6_B_resid.py (the residual and the "
                              "one-sided gap), a6_B_argmax.py (the argmax "
                              "reversal) and a6_B_alt.py (the interior "
                              "crossing fixed point)",
            "findings": "a6_panel_probes_2026-08-27/a6_B_findings.md 4d/4e/4f "
                        "and Section 7; a6_A_findings.md probe 5(b) (the "
                        "proximity negative)",
            "stalled_nodes": "quality_reports/fixes/t2_p1_fournode_recheck.py "
                             "| .json (30 seeds per node, no early stopping; "
                             "all four STILL UNRESOLVED)",
            "card": "research/model_v4/MODEL_CARD.md Section 5, A3 evidence "
                    "note (stamp 2026-08-27, commit ae9caea -- verified "
                    "against the file before this script was written), which "
                    "records the account as 'on file and UNCHECKED beyond the "
                    "one node probed' and records the k-direction negative "
                    "alongside it",
        },
        "node15_reference_values": NODE15_REFERENCE,
        "framing": (
            "DIAGNOSTIC EVIDENCE about why the ticket-34 recheck stalls at "
            "these nodes.  No label moves and none is licensed: A3 and A6 are "
            "listed hypotheses and P1 stays PROVED as a conditional.  "
            "Existence of equilibrium at these nodes is neither claimed nor "
            "denied -- an edge-pinned fixed point of the implemented cutoff "
            "map is NOT an equilibrium (its payoff-scale residual is "
            "1e-3-grade against a 1e-9 criterion), and a stalled search is "
            "not a nonexistence proof.  The account graduates from "
            "'candidate, UNCHECKED beyond one node' to exactly what the "
            "per-node record says and no further."
        ),
        "verdict_rule": (
            "PRE-REGISTERED, see the module docstring.  HOLDS = signature (i) "
            "(edge-pinned jump through zero, manifestation A pinned fixed "
            "point or B at-edge worst deviation) AND (ii) (residual "
            "reproduction, plus bracketing where two or more independent "
            "configurations exist) AND (iii) (the a6_A proximity negative's "
            "per-node input replicates and the achieving fixed point is not "
            "itself pinned).  DIFFERENT MECHANISM = (i) absent with the "
            "diagnostic clean.  INCONCLUSIVE = anything mixed or obstructed."
        ),
        "thresholds": {
            "PIN_TOL": PIN_TOL, "FP_TOL": FP_TOL, "JUMP_MIN": JUMP_MIN,
            "JUMP_REF_DELTA": JUMP_REF_DELTA, "DEV_FACTOR": DEV_FACTOR,
            "REPRO_RTOL": REPRO_RTOL, "SIGMA_TOL": SIGMA_TOL,
            "K1_GATE_TOL": K1_GATE_TOL,
            "TOL_PAYOFF": TOL_EXIST_PAYOFF, "TOL_CUTOFF": TOL_EXIST_CUTOFF,
        },
        "method_transfer": (
            "a6_B_node15.py's battery, run per node: the 1-D k_2 sweep on its "
            "own grid at fixed k_1, the edge bracketing at +-1e-7, the "
            "one-sided U_HOLD - U_VOICE limits, the residual at the located "
            "configuration, and the interior-crossing k_init route.  Three "
            "additions, each recorded: the 1-D reduction is GATED rather than "
            "inherited from the baseline; the tau-crossing pullback family is "
            "swept alongside the n(s) family (a6_B_findings Section 7 lists it "
            "UNCHECKED, and it is 13 edges rather than 4 at tau = 0.075); and "
            "fixed points come from the ticket-34 recheck's own 30 seeds as "
            "embedded literals with one seed per basin re-solved as the "
            "reproduction check, rather than 90 re-solves that would return "
            "the same numbers."
        ),
        "does_not": "rerun the ticket-34 sweep or recheck; change any "
                    "tolerance; modify numerical_v4/; write to MODEL_CARD.md, "
                    "the mirrors, sections_v3/, research/, LABEL_LEDGER.md or "
                    "the session log",
        "determinism": "fixed seed list, no wall-clock dependence, no Monte "
                       "Carlo, no file inputs, no network; numerical_v4 "
                       "imported read-only",
        "smoke_gate": ".venv/bin/python -m numerical_v4.smoke run before this "
                      "script: exit 0, SMOKE COMPLETE in 66.9 s",
    }
    _checkpoint()

    node_results = []
    for node in NODES:
        detail = analyse_node(node)
        node_results.append(detail)
        record(
            f"t34_account_k{node['kappa']}_tau{node['tau']}_T{node['T']}",
            detail["diagnostic_clean"], "diagnostic", detail,
        )
        results["nodes_so_far"] = len(node_results)
        _checkpoint()

    results["seconds"] = time.perf_counter() - t0
    results["all_pass"] = results["n_fail"] == 0
    results["summary_table"] = [
        {
            "kappa": d["node"]["kappa"], "tau": d["node"]["tau"],
            "T": d["node"]["T"],
            "account": d["account"],
            "manifestation": d["signature_i_edge_pinned_jump"]["manifestation"],
            "signature_i": d["signature_i_edge_pinned_jump"]["satisfied"],
            "signature_ii": d["signature_ii_residuals"]["pass"],
            "signature_iii": d["signature_iii_proximity_negative"]["pass"],
            "edge": d["signature_i_edge_pinned_jump"].get("edge"),
            "offset_from_edge":
                d["signature_i_edge_pinned_jump"].get("offset_from_edge"),
            "gap_below": (d["signature_i_edge_pinned_jump"].get("jump") or {}
                          ).get("gap_below"),
            "gap_above": (d["signature_i_edge_pinned_jump"].get("jump") or {}
                          ).get("gap_above"),
            "jumps_through_zero_without_crossing":
                (d["signature_i_edge_pinned_jump"].get("jump") or {}
                 ).get("jumps_through_zero_without_crossing"),
            "payoff_scale_at_configuration":
                d["signature_i_edge_pinned_jump"].get("payoff_scale"),
            "recorded_best_payoff_scale":
                d["ticket34_record"]["best_payoff_scale"],
            "bracket_state": d["signature_ii_residuals"]["bracket_state"],
            "sigma_s_distance_measured":
                d["signature_iii_proximity_negative"][
                    "measured_at_achieving_basin_sigma_s"],
            "sigma_s_distance_recorded":
                d["signature_iii_proximity_negative"][
                    "recorded_by_a6_A_probe_5b_sigma_s"],
            "diagnostic_clean": d["diagnostic_clean"],
            "seconds": d["seconds"],
        }
        for d in node_results
    ]
    calls = "; ".join(
        f"(kappa={d['node']['kappa']}, tau={d['node']['tau']}, "
        f"T={d['node']['T']}): {d['account']}" for d in node_results
    )
    n_holds = sum(1 for d in node_results if d["account"] == "HOLDS")
    results["verdict"] = (
        f"Ticket 34's candidate mechanical account, swept over the three "
        f"nodes it had not been probed at: {n_holds}/3 HOLDS.  {calls}.  "
        "This is diagnostic evidence about WHY the ticket-34 recheck stalls "
        "at these nodes; no label moves and none is licensed (A3 and A6 are "
        "listed hypotheses, P1 stays PROVED as a conditional), and existence "
        "at these nodes is neither claimed nor denied -- an edge-pinned fixed "
        "point of the implemented cutoff map is not an equilibrium, and a "
        "stalled search is not a nonexistence proof.  The account graduates "
        "from 'candidate, UNCHECKED beyond one node' to exactly this per-node "
        "record.  The fourth node, (kappa=0.15, tau=0.05, T=5), is the one "
        "the A6 panel already probed and is not re-adjudicated here; its "
        "values are carried as the reference the thresholds were set against."
    )
    _checkpoint()
    print(f"\n{results['verdict']}\n", flush=True)
    print(f"cumulative {results['seconds']:.0f} s  ->  {OUT}", flush=True)
    return 0 if results["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
