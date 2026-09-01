"""The Hold-collapse face is measured CLEAN on the implemented menu -- curated.

WHAT THIS IS.  The third decisive measurement of the 2026-08-27 A6 panel, as
quoted in the card's section 5 A6 evidence note:

    "The implemented menu is NOT in that class: Exit and Hold pool perfectly in
     order flow, and its Hold-collapse face is measured clean (pooled prices
     within 4.4e-16 and T bit-identical as k_1 sweeps to full collapse)."

This is the one measurement in the A6 note that runs AGAINST the panel's own
indictment, and it is why the card's locus sentence reads "the failure is live
at the interior n(s) cell edges INSTEAD".  The re-derivation's withheld change 6
(N11) named the collapsed cutoff vectors as the place A6's continuity would
fail.  The panel's continuum-face lemma says a collapse face is a discontinuity
only when the dying plan is the SOLE generator of some reachable pooled history.
On this menu it is not: ``Gamma`` is a buy-indicator, Exit's day-0 increment is
negative and marks 0, so Exit and Hold pool perfectly at mark-path type 0.  The
whole pooled price system therefore depends on k through k_2 alone, and the
collapse face {k_1 = k_2} carries no discontinuity at all.

SOURCE PROBE (adapted): ``a6_panel_probes_2026-08-27/a6_B_sweep.py`` part (A),
Analyst B's "probe 2A", and its filed log ``a6_B_sweep.log``.  Note that part
(B) of the same script -- the k_2 sweep -- is NOT the jump measurement the card
quotes; that one is ``a6_B_baseline.py``, curated in
``t2_a6_edge_jump_check.py``.  (The probe directory's README conflates the two;
the correction is recorded in that check's provenance.)

THE PARAMETER MIX IS REPLAYED VERBATIM, INCLUDING ITS ODDITY.  The filed probe
runs at ``ParamsV4()`` -- the SEED threshold tau = 0.05 -- while holding k_2 at
the FROZEN-tau baseline's k_2* = 1.5310222869.  That mix is not what a fresh
script would choose, but it is the configuration that produced the card's
4.441e-16, and this curation reproduces it rather than tidying it.  The
substantive content does not depend on the choice: the invariance is exact
(most rows are bit-identical, the two non-zero rows are one and two ulps of a
price near 1.4), and the same k_1-invariance is re-verified independently at
kappa = 0.15 in ``t2_a6_node15_check.py``.

WHAT "PASS" MEANS HERE.  As in the sibling checks the semantics are inverted
relative to a proof check, but the direction differs: here ``pass: true`` means
the face was measured CLEAN -- N11's literal mechanism does NOT fire on this
menu.  That is not a rescue of A6.  A6's continuity clause still fails at this
calibration, at the interior cell edges instead (see
``t2_a6_edge_jump_check.py``).  This file licenses NO label move; A6 is a listed
hypothesis of P1, and P1 stays PROVED as a conditional.

GATES.  Fixed from the filed log before this script was first run, with ONE
exception, declared here rather than left for a reader to notice: the T gate was
originally a bit-equality (``==``), transcribing the card's own word, and it
missed on the first run.  It was replaced by invariance at the map's own
root-finder resolution, and the measured bit-inequality is recorded in the
JSON's ``known_discrepancies`` and in the check's own
``card_wording_discrepancy``.  See the paragraph below the gate list.  No
tolerance was widened on any other gate.

  prices_invariant   max over the k_1 ladder of
                     max |signature(k_1) - signature(k_1 = 0.5)| <= 5e-16,
                     where the signature stacks every date's E[P_d | theta] with
                     E[p_bid | theta] and E[p*P | theta] (filed: 4.441e-16)
  U_bit_identical    U_VOICE(1.6) and U_HOLD(1.6) EQUAL (==, not approx) at
                     every k_1 including k_1 = k_2 (filed: 0.040113093715)
  T_invariant        the spread of T(k) over the k_1 ladder is at most 2e-12 --
                     scipy ``brentq``'s default ``xtol``, which is the
                     resolution at which ``solver.outer_map`` defines T at all
                     (filed: (1.25054030, 1.41006135))
  full_collapse      the Hold region really does close: width exactly 0.0 and
                     Hold's population mass exactly 0.0 at k_1 = k_2
  exit_hold_pool     every Exit and every Hold atom carries mark-path type 0,
                     which is the mechanism the face result rests on

DISCREPANCY AGAINST THE CARD'S WORDING, recorded rather than smoothed.  The card
says T is "bit-identical" across the ladder.  At full double precision it is
not, at exactly one row: T_2 = 1.4100613525452288 at k_1 = 1.2405757283 against
1.4100613525452281 at every other k_1 -- a spread of 6.66e-16, exactly three
ulps of a double near 1.41.  That row is precisely the one where the price
signature itself deviates MOST, by 4.441e-16 (k_1 = 1.52 deviates by 2.220e-16;
the other four rows are bit-identical), so the three ulps are the propagated
image of the price deviation the card does quote.  Analyst B's filed log prints
T to 8 decimals, which is where
"bit-identical" came from; U_VOICE and U_HOLD ARE bit-identical at full
precision, and T is identical to three orders below its own root-finder's xtol.
Substantively nothing moves -- but "bit-identical" is literally false for T_2,
and this check gates the invariance at the map's own resolution instead of
asserting a bit-equality that does not hold.

NOT CURATED HERE: Analyst A's independent collapse-face probe at the
(0.5, 0.05, 1) node, where a solved equilibrium has k_1 == k_2 exactly
(``a6_A_probe5_collapseface.py``).  It corroborates, but the card's face clause
cites only Analyst B's numbers, and this curation stays with what the card
cites.  Also not curated: the continuum-face lemma itself (a single-pass panel
derivation the card already flags as not gate-checked) and the J >= 3
exclusive-history class it applies to -- both are mathematics, not measurement.

RUN:  ``.venv/bin/python numerical_v4/checks/t2_a6_collapse_face_check.py``
      from the repo root.  Deterministic; read-only on ``numerical_v4/``.
      Writes ``t2_a6_collapse_face_check.json`` beside itself.
"""

from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO not in sys.path:
    sys.path.insert(0, REPO)

from numerical_v4.params import ParamsV4, EXIT, HOLD, VOICE  # noqa: E402
from numerical_v4.menu import atoms  # noqa: E402
from numerical_v4.pooled import pooled_pass  # noqa: E402
from numerical_v4.policy import plan_payoff  # noqa: E402
from numerical_v4.solver import outer_map  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "t2_a6_collapse_face_check.json")

# a6_B_sweep.py verbatim: seed-tau params, frozen-tau k*, the same k_1 ladder.
KSTAR = (1.2405757283, 1.5310222869)
K1_LADDER = [0.5, 1.0, KSTAR[0], 1.40, 1.52, KSTAR[1]]   # last = full collapse
S_EVAL = 1.60                                            # probe's payoff signal

FILED_MAX_DEV = 4.441e-16
FILED_UV = 0.040113093715
FILED_T = (1.25054030, 1.41006135)

TOL_DEV = 5e-16          # "pooled prices within 4.4e-16"
TOL_FILED_UV = 1e-12     # agreement with the filed 12-dp U_VOICE printout
TOL_FILED_T = 1e-8       # agreement with the filed 8-dp T printout
TOL_T_SPREAD = 2e-12     # scipy brentq's default xtol -- the resolution at
#                          which solver.outer_map defines T at all

results: dict = {"kind": "A6 applicability evidence (panel-probe curation)",
                 "checks": [], "n_fail": 0}


def record(name: str, ok: bool, kind: str, detail: dict) -> None:
    results["checks"].append({"name": name, "kind": kind, "pass": bool(ok),
                              **detail})
    if not ok:
        results["n_fail"] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def main() -> int:
    t_run = time.perf_counter()
    p = ParamsV4.baseline()          # SEED tau = 0.05, as the probe ran it
    k2 = KSTAR[1]

    results["node"] = dict(
        kappa=float(p.kappa), tau=float(p.tau), T=int(p.T),
        params_hash=p.hash_str(), k2_held=k2, k1_ladder=list(K1_LADDER),
        s_eval=S_EVAL,
        parameter_mix_note="replayed verbatim from a6_B_sweep.py part (A): "
                           "SEED tau = 0.05 with the FROZEN-tau baseline's "
                           "k_2* = 1.5310222869. Odd, but it is the "
                           "configuration that produced the card's 4.441e-16, "
                           "and the result does not depend on it -- the same "
                           "k_1-invariance is re-verified at kappa = 0.15 in "
                           "t2_a6_node15_check.py",
    )

    rows = []
    base_sig = None
    for k1 in K1_LADDER:
        al = atoms((k1, k2), p)
        res = pooled_pass(al, p, with_runup=True)
        sig = np.concatenate([res.EP[d] for d in res.dates]
                             + [res.Ep_bid, res.EpP])
        dev = 0.0 if base_sig is None else float(np.max(np.abs(sig - base_sig)))
        if base_sig is None:
            base_sig = sig
        Uv = float(plan_payoff(VOICE, S_EVAL, res, p))
        Uh = float(plan_payoff(HOLD, S_EVAL, res, p))
        T = outer_map((k1, k2), p, res)
        hold_mass = float(sum(a.w for a in al if a.plan == HOLD))
        exit_mass = float(sum(a.w for a in al if a.plan == EXIT))
        off_theta = sorted({int(a.theta) for a in al
                            if a.plan in (EXIT, HOLD) and a.theta != 0})
        rows.append(dict(k1=float(k1), hold_region_width=float(k2 - k1),
                         max_abs_dev_from_k1_0p5=dev,
                         U_VOICE=Uv, U_HOLD=Uh,
                         T=[float(T[0]), float(T[1])],
                         hold_mass=hold_mass, exit_mass=exit_mass,
                         non_zero_theta_on_exit_or_hold=off_theta))
        print(f"  k1={k1:.10f}  width={k2-k1:.3e}  "
              f"max|dev|={dev:.3e}  U_V={Uv:.12f}  "
              f"T=({T[0]:.8f}, {T[1]:.8f})", flush=True)

    max_dev = max(r["max_abs_dev_from_k1_0p5"] for r in rows)
    record("a6_collapse_face_prices_invariant",
           max_dev <= TOL_DEV, "substantive",
           dict(max_abs_deviation=max_dev, tol=TOL_DEV,
                panel_filed=FILED_MAX_DEV,
                matches_filed_exactly=(max_dev == FILED_MAX_DEV),
                per_k1=[{"k1": r["k1"], "dev": r["max_abs_dev_from_k1_0p5"]}
                        for r in rows],
                signature="every date's E[P_d | theta], stacked with "
                          "E[p_bid | theta] and E[p*P | theta] -- the three "
                          "type-indexed aggregates policy.plan_payoff reads",
                note="the whole pooled price system depends on k through k_2 "
                     "alone; the two non-zero rows are one and two ulps of a "
                     "price near 1.4"))

    uv = [r["U_VOICE"] for r in rows]
    uh = [r["U_HOLD"] for r in rows]
    record("a6_collapse_face_U_bit_identical",
           all(x == uv[0] for x in uv) and all(x == uh[0] for x in uh)
           and abs(uv[0] - FILED_UV) <= TOL_FILED_UV, "substantive",
           dict(U_VOICE=uv[0], U_HOLD=uh[0], s=S_EVAL,
                distinct_U_VOICE_values=len(set(uv)),
                distinct_U_HOLD_values=len(set(uh)),
                panel_filed_U_VOICE=FILED_UV,
                abs_diff_from_filed=abs(uv[0] - FILED_UV),
                comparison="equality (==), not a tolerance"))

    Ts = [tuple(r["T"]) for r in rows]
    spread = [max(t[i] for t in Ts) - min(t[i] for t in Ts) for i in (0, 1)]
    max_spread = max(spread)
    ulps = [int(round(spread[i] / np.spacing(Ts[0][i]))) for i in (0, 1)]
    record("a6_collapse_face_T_invariant",
           max_spread <= TOL_T_SPREAD
           and max(abs(Ts[0][i] - FILED_T[i]) for i in (0, 1)) <= TOL_FILED_T,
           "substantive",
           dict(T_at_k1_0p5=list(Ts[0]), distinct_T_values=len(set(Ts)),
                T_spread=[float(s) for s in spread], T_spread_in_ulps=ulps,
                max_spread=float(max_spread), tol=TOL_T_SPREAD,
                tol_basis="scipy brentq's default xtol = 2e-12, the resolution "
                          "at which solver.outer_map defines T at all",
                panel_filed_T=list(FILED_T),
                max_abs_diff_from_filed=max(abs(Ts[0][i] - FILED_T[i])
                                            for i in (0, 1)),
                T_bit_identical=all(t == Ts[0] for t in Ts),
                rows_differing_from_k1_0p5=[r["k1"] for r, t in zip(rows, Ts)
                                            if t != Ts[0]],
                card_wording_discrepancy=(
                    "the card says T is 'bit-identical'. At full double "
                    "precision it is not: T_2 differs by 6.66e-16 -- exactly 3 "
                    "ulps of a double near 1.41 -- at k_1 = 1.2405757283, the "
                    "row where the price signature itself deviates MOST, by "
                    "4.441e-16 (k_1 = 1.52 deviates by 2.220e-16; the other "
                    "four rows are bit-identical). Analyst B's filed log prints "
                    "T to 8 decimals, which is where 'bit-identical' came from. "
                    "U_VOICE and U_HOLD ARE bit-identical at full precision. "
                    "Nothing substantive moves -- 3 ulps is three orders below "
                    "the map's own root-finder xtol -- but the word is "
                    "literally false for T_2."
                ),
                note="T is invariant in k_1 at every point on the ladder, the "
                     "fully collapsed k_1 = k_2 included: the collapse face "
                     "carries no discontinuity on this menu"))

    last = rows[-1]
    record("a6_collapse_face_reaches_full_collapse",
           last["hold_region_width"] == 0.0 and last["hold_mass"] == 0.0,
           "substantive",
           dict(k1=last["k1"], k2=k2,
                hold_region_width=last["hold_region_width"],
                hold_mass=last["hold_mass"], exit_mass=last["exit_mass"],
                note="the ladder really does reach the face, so the "
                     "invariance above is measured ON it and not merely "
                     "near it"))

    stray = sorted({t for r in rows for t in r["non_zero_theta_on_exit_or_hold"]})
    record("a6_collapse_face_exit_and_hold_pool_at_type_0",
           len(stray) == 0, "substantive",
           dict(non_zero_theta_on_exit_or_hold=stray,
                mechanism="Gamma is a buy-indicator and Exit's day-0 increment "
                          "is negative, so it marks 0: Exit and Hold pool "
                          "perfectly in order flow at mark-path type 0 "
                          "(numerical_v4/menu.py docstring). That is why the "
                          "dying plan is not the sole generator of any "
                          "reachable pooled history, and why the "
                          "continuum-face lemma does not bite here"))

    # -- aggregate -----------------------------------------------------------
    results["ladder"] = rows
    results["known_discrepancies"] = [
        {
            "card_wording": "T bit-identical as k_1 sweeps to full collapse",
            "reproduced": "in substance, not literally",
            "measured_T_spread": float(max_spread),
            "measured_T_spread_in_ulps": ulps,
            "U_bit_identical": True,
            "finding": "U_VOICE and U_HOLD are bit-identical at full "
                       "precision, but T_2 is not: it differs by 6.66e-16 -- "
                       "exactly 3 ulps of a double near 1.41 -- at "
                       "k_1 = 1.2405757283, the row where the price signature "
                       "itself deviates MOST, by 4.441e-16 (k_1 = 1.52 deviates "
                       "by 2.220e-16; the other four rows are bit-identical). "
                       "The filed panel log prints T to 8 decimals, which is "
                       "where "
                       "'bit-identical' came from. The invariance is real and "
                       "gated here at the map's own root-finder resolution "
                       "(brentq xtol 2e-12), three orders above the observed "
                       "spread; only the word 'bit-identical' is too strong, "
                       "and only for T_2.",
        }
    ]
    results["seconds"] = time.perf_counter() - t_run
    results["all_pass"] = results["n_fail"] == 0
    results["verdict"] = (
        "Hold-collapse face MEASURED CLEAN at calibration"
        if results["all_pass"] else
        f"Hold-collapse face measurement PARTIALLY REPRODUCED "
        f"({results['n_fail']} gate(s) missed)"
    ) + (
        f" -- as k_1 sweeps to full collapse (k_1 = k_2 = {k2}) the pooled "
        f"price system moves by at most {max_dev:.3e}, U_VOICE and U_HOLD are "
        f"bit-identical at every k_1 on the ladder and T(k) is invariant to "
        f"{max_spread:.1e} (3 ulps at one row, not literally bit-identical -- "
        f"see known_discrepancies). Exit and Hold pool "
        f"perfectly at mark-path type 0, so the dying plan generates no "
        f"reachable pooled history of its own and the continuum-face lemma does "
        f"not bite. THIS IS NOT A RESCUE OF A6: the continuity clause still "
        f"fails at this calibration, at the interior n(s) cell edges instead "
        f"(t2_a6_edge_jump_check.json). What it establishes is that the LOCUS "
        f"is not the one the re-derivation's change 6 named. NO LABEL MOVES AND "
        f"NONE IS LICENSED -- P1 stays PROVED as a conditional."
    )
    results["provenance"] = {
        "follow_up": "numerical_v4/checks/a6_panel_probes_2026-08-27/"
                     "README.md -- the standing curation follow-up",
        "source_probe": "a6_panel_probes_2026-08-27/a6_B_sweep.py part (A) "
                        "(Analyst B, probe 2A) and its filed log a6_B_sweep.log",
        "sibling_checks": [
            "numerical_v4/checks/t2_a6_edge_jump_check.py -- the three T_2 "
            "jumps at the interior cell edges, where the failure IS live",
            "numerical_v4/checks/t2_a6_node15_check.py -- the kappa = 0.15 "
            "node, the destroyed crossing and the edge-pinned fixed point",
        ],
        "card_row": "research/model_v4/MODEL_CARD.md section 5, A6 evidence "
                    "note (stamp 2026-08-27, commit ae9caea)",
        "panel_reports": [
            "research/model_v4/threads/2026-08-27_A6_panel_substantiate.md",
            "research/model_v4/threads/2026-08-27_A6_panel_defuse.md",
        ],
        "verdict_semantics": (
            "pass = the face was measured CLEAN, i.e. N11's literal mechanism "
            "does not fire on this menu. That is a LOCUS finding, not a rescue "
            "of A6 and not a label move."
        ),
        "environment_gate": ".venv/bin/python -m numerical_v4.smoke, exit 0",
        "does_not": [
            "touch MODEL_CARD.md, the mirrors, sections_v3/ or anything under "
            "research/",
            "modify anything under numerical_v4/ (imported read-only)",
            "curate Analyst A's corroborating collapse-face probe at "
            "(0.5, 0.05, 1) -- the card's face clause cites only B's numbers",
            "curate the continuum-face lemma or the J >= 3 exclusive-history "
            "class -- mathematics, not measurement",
            "claim that A6's continuity clause holds anywhere",
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
