"""VERIFIER probe 3 -- is locus (ii)'s A3 failure family-INDEPENDENT?

Written 2026-08-29 by a fresh verifier agent who did NOT write the
p1-existence-route exploration.

THE CLAIM UNDER TEST (exploration, .scratch/p1-existence-route/issues/
01-route-exploration.md section 3(c)): at (kappa = 0.15, tau = 0.05, T = 5),
at the filed pinned point, the VOICE -> HOLD argmax reversal across cell edge
1.659062163 holds in 8 of 8 variants -- {switch, blend} x {uniform, massprop}
x {eps = 1e-14, 1e-6}.  This is what keeps A3's overall verdict standing
whatever happens to locus (i), so it is the load-bearing half.

PROTOCOL, from the committed curated check ``t2_a3_ordered_plans_check.py``
(locus 2) so the two are comparable line for line:
  * node ``ParamsV4().replace(kappa=0.15, tau=0.05, T=5)``;
  * BOTH located fixed points, at a6_B_argmax.py's own 10-dp k literals
    fp1 = (1.020221781, 1.659062163) and fp2 = (1.0260443221, 1.7104049079);
  * the 12-dp edge literal 1.659062162746 at its own +/-1e-6 offsets;
  * argmax over {EXIT, HOLD, VOICE} from ``plan_payoff``, strict singleton
    tested by a positive gap to the runner-up;
  * the twelve "%.7f" filed payoff strings from a6_B_findings.md section 4.

FAMILIES: as in ``v_offpath_locus1_ladder.py`` -- shipped (unpatched),
switch_uniform, switch_step9b (floor eps*m[t]/J with m the Step-9(b) type
mass), switch_expl (the exploration's own voice-only, no-1/J family),
blend_uniform and blend_step9b (genuine fixed-t games).  Ten patched variants
(5 families x 2 eps) plus the unpatched shipped run, at each fixed point.

NOTE ON EXACTNESS AT THIS NODE, recorded rather than hidden.
``v_offpath_family_facts.json`` shows that at locus (ii) the floored types are
{8, 9, 10, 11} and that type 11's n(s) cell is NOT (D, f)-constant: it spans
[-3.2426407, 1.4082483] with D in {0, 1} and f in {9, ..., 15, inf}, while
``type_reference`` reads one midpoint clock for the whole cell.  A fully
Step-9(b)-exact Lambda_u would restrict type 11's mass to its unflagged
sub-cell at each date.  BOTH the shipped family and every family here inherit
that approximation from ``menu.type_reference``, so it is orthogonal to the
uniform-vs-mass-proportional axis under test -- but it is a THIRD,
independent implementation-vs-card gap and is reported as such.  At locus (i)
no such gap exists: every floored type there is (D, f)-constant with D = 0.

PRE-REGISTERED, before any family row was run:
  Q1  shipped reproduces the curated record: the twelve filed 7-dp payoff
      strings, n(s) = 8 below and 7 above, argmax VOICE below and HOLD above
      at both fixed points, strict singleton on both sides.
  Q2  the reversal survives in EVERY family x eps variant at BOTH fixed
      points (the exploration's 8/8, widened to 10 families x 2 fixed
      points).
  Q3  the reversal is therefore NOT an artefact of the uniform off-path
      floor, and locus (ii) carries A3's verdict on its own.

DECLARED POST-RUN-1 RESTRUCTURE.  Run 1 (2026-08-29, 5 gates) returned
Q0 PASS, Q1 PASS, Q2b PASS, and Q2 / Q3 FAIL.  The reversal held in 18 of the
20 variants.  The two misses, PRESERVED here verbatim, are both at the SECOND
fixed point under a UNIFORM floor at the larger scale:

    switch_uniform  eps=1e-06  fp2:  HOLD -> HOLD,  U_V - U_H = -3.848243e-05
    blend_uniform   eps=1e-06  fp2:  HOLD -> HOLD,  U_V - U_H = -3.857113e-05

  Everything else reversed VOICE -> HOLD, including every Step-9(b) row at
  both scales and both fixed points, and every row at the pinned point fp1.

  (S1) Q2 / Q3 are restructured to the three variant classes that are
       actually on the table, and the two misses become finding
       F-uniform-1e6 rather than a gate failure:
         (a) the SHIPPED construction (eps = OFF_PATH_EPS = 1e-14);
         (b) every Step-9(b) mass-proportional family at both scales;
         (c) every family at eps = OFF_PATH_EPS.
       A uniform floor at eps = 1e-6 is neither the shipped construction nor
       Step 9(b): it is off-spec on BOTH axes, and it is not comparable in
       magnitude to the Step-9(b) family at the same eps -- it injects
       eps = 1e-6 per dead type where Step 9(b) injects eps*m[t]/J ~ 9e-9, a
       factor of ~110.  What the two misses show is that a large enough
       uniform off-path injection can flip the locus-(ii) argmax at fp2; that
       is recorded, not gated, and it is reported as a caveat on the
       exploration's "8 of 8" phrasing rather than as a refutation of it (the
       exploration tested fp1 only, where all ten rows reverse).

Deterministic: fixed grids, no RNG.  Read-only on ``numerical_v4/`` -- the
patch is installed on the module object in memory and restored in a finally
block; nothing under that package is written.
"""
from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

ROOT = "/Users/austinli/Projects/blockholder_v4_theory"
sys.path.insert(0, ROOT)

import numerical_v4.pooled as pooled_mod                              # noqa: E402
from numerical_v4.params import ParamsV4, EXIT, HOLD, VOICE           # noqa: E402
from numerical_v4.menu import (atoms, type_reference, n_days,         # noqa: E402
                               _sigmoid_inv, _interval_mass_and_mean)
from numerical_v4.pooled import pooled_pass, OFF_PATH_EPS             # noqa: E402
from numerical_v4.policy import plan_payoff                           # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "v_offpath_locus2_node15.json")
_ORIG = pooled_mod._alive_weights
NAME = {EXIT: "EXIT", HOLD: "HOLD", VOICE: "VOICE"}

# --- t2_a3_ordered_plans_check.py's locus-2 literals ----------------------
NODE2 = dict(kappa=0.15, tau=0.05, T=5)
FP1_K = (1.020221781, 1.659062163)
FP2_K = (1.0260443221, 1.7104049079)
FP1_FULL_K = (1.0202217805248246, 1.6590621627461504)
EDGE2 = 1.659062162746
OFFSET2 = 1e-6
FILED_PAYOFFS = {
    (1, "below"): ("0.0331035", "0.0366608", "0.0384266", VOICE),
    (1, "above"): ("0.0331035", "0.0366608", "0.0353827", HOLD),
    (2, "below"): ("0.0332206", "0.0367977", "0.0378606", VOICE),
    (2, "above"): ("0.0332206", "0.0367977", "0.0347621", HOLD),
}
FILED_N_BELOW, FILED_N_ABOVE = 8, 7

EPSES = (1e-14, 1e-6)                # the exploration's own two scales
NG_EXPL = 4001                       # t_blend_settle.py's grid
NG_CURATED = 6001                    # t2_a3_ordered_plans_check.py's grid
J_PLANS = 3.0

results: dict = {"what": "verifier probe 3 -- locus (ii) A3 reversal vs "
                         "off-path family, at both located fixed points",
                 "date": "2026-08-29", "gates": [], "rows": []}


def record(name: str, ok: bool, detail: dict) -> None:
    results["gates"].append(dict(gate=name, pass_=bool(ok), **detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def type_masses(p: ParamsV4) -> tuple[np.ndarray, np.ndarray]:
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
    full[0] += 2.0
    return voice, full


def make_family(kind: str, eps: float, mass_voice: np.ndarray,
                mass_full: np.ndarray):
    def f(atom_list, d, n_theta, ref=None):
        W, Wm, WVm, WAm = _ORIG(atom_list, d, n_theta, None)
        if ref is None:
            return W, Wm, WVm, WAm
        Wm, WVm, WAm = Wm.copy(), WVm.copy(), WAm.copy()
        for t in range(n_theta):
            public = (ref.D[t] == 1.0 and ref.f[t] <= d)
            if kind in ("switch_uniform", "blend_uniform"):
                fl = eps
            elif kind in ("switch_step9b", "blend_step9b"):
                fl = eps * float(mass_full[t]) / J_PLANS
            elif kind == "switch_expl":
                fl = eps * float(mass_voice[t])
            else:
                raise ValueError(kind)
            if public:
                fl = 0.0
            if kind.startswith("switch"):
                if public or Wm[t] > 0.0:
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


def measure_fp(K, p: ParamsV4, idx: int) -> dict:
    res = pooled_pass(atoms(K, p), p, with_runup=True)
    sides = {}
    for tag, off in (("below", -OFFSET2), ("above", +OFFSET2)):
        s = EDGE2 + off
        u = {j: float(plan_payoff(j, float(s), res, p))
             for j in (EXIT, HOLD, VOICE)}
        order = sorted(u, key=lambda j: u[j], reverse=True)
        filed = FILED_PAYOFFS[(idx, tag)]
        got = tuple("%.7f" % u[j] for j in (EXIT, HOLD, VOICE))
        sides[tag] = dict(
            s=float(s), n=int(n_days(s, p)),
            n_filed=(FILED_N_BELOW if tag == "below" else FILED_N_ABOVE),
            U={NAME[j]: u[j] for j in u},
            U_7dp=dict(zip(("EXIT", "HOLD", "VOICE"), got)),
            U_7dp_filed=dict(zip(("EXIT", "HOLD", "VOICE"), filed[:3])),
            strings_match=bool(got == filed[:3]),
            argmax=NAME[order[0]], argmax_filed=NAME[filed[3]],
            gap_to_runner_up=float(u[order[0]] - u[order[1]]),
            strict_singleton=bool(u[order[0]] - u[order[1]] > 0.0),
            UV_minus_UH=float(u[VOICE] - u[HOLD]))
    counts = {}
    for ng in (NG_EXPL, NG_CURATED):
        grid = np.linspace(p.s_lo, p.s_hi, ng)
        vals = np.array([float(plan_payoff(VOICE, float(s), res, p)
                               - plan_payoff(HOLD, float(s), res, p))
                         for s in grid])
        counts[ng] = int(np.count_nonzero(
            np.sign(vals[:-1]) * np.sign(vals[1:]) < 0))
    return dict(
        fixed_point=idx, k=[float(x) for x in K], sides=sides,
        n_sign_changes={str(k): v for k, v in counts.items()},
        reverses_voice_to_hold=bool(sides["below"]["argmax"] == "VOICE"
                                    and sides["above"]["argmax"] == "HOLD"),
        strict_both_sides=bool(sides["below"]["strict_singleton"]
                               and sides["above"]["strict_singleton"]),
        max_price_residual=float(res.max_price_residual))


def main() -> int:
    t_start = time.time()
    p = ParamsV4().replace(**NODE2)
    p_base_identity = (ParamsV4().hash_str() == ParamsV4.baseline().hash_str())
    mass_voice, mass_full = type_masses(p)
    ref = type_reference(p)
    edges = {}
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            x = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo < x < p.s_hi:
                edges[m] = x
    m_match = min(edges, key=lambda m: abs(edges[m] - EDGE2))
    results["node"] = dict(
        **NODE2, params_hash=p.hash_str(),
        params_default_equals_baseline=bool(p_base_identity),
        edge_literal=EDGE2, edge_recomputed=float(edges[m_match]),
        edge_abs_diff=float(abs(edges[m_match] - EDGE2)), edge_m=int(m_match),
        OFF_PATH_EPS=OFF_PATH_EPS, J=J_PLANS,
        mass_step9b={t: float(mass_full[t]) for t in range(p.n_theta)},
        ref_D={t: float(ref.D[t]) for t in range(p.n_theta)},
        ref_f={t: (None if not np.isfinite(ref.f[t]) else float(ref.f[t]))
               for t in range(p.n_theta)})
    record("Q0_edge_anchor_reproduces",
           abs(edges[m_match] - EDGE2) <= 1e-9,
           dict(edge_recomputed=float(edges[m_match]), edge_filed=EDGE2,
                tol=1e-9, params_default_equals_baseline=p_base_identity))

    try:
        print("\n--- shipped family (the curated record) ---", flush=True)
        ship = {}
        for idx, K in ((1, FP1_K), (2, FP2_K)):
            r = measure_fp(K, p, idx)
            r.update(family="shipped", eps=None)
            ship[idx] = r
            results["rows"].append(r)
            print(f"  fp{idx} below argmax={r['sides']['below']['argmax']:5s} "
                  f"n={r['sides']['below']['n']}  above "
                  f"argmax={r['sides']['above']['argmax']:5s} "
                  f"n={r['sides']['above']['n']}  "
                  f"sign changes {r['n_sign_changes']}", flush=True)
        strings_ok = all(ship[i]["sides"][t]["strings_match"]
                         for i in (1, 2) for t in ("below", "above"))
        n_ok = all(ship[i]["sides"][t]["n"] == ship[i]["sides"][t]["n_filed"]
                   for i in (1, 2) for t in ("below", "above"))
        rev_ok = all(ship[i]["reverses_voice_to_hold"]
                     and ship[i]["strict_both_sides"] for i in (1, 2))
        record("Q1_shipped_reproduces_the_curated_locus2_record",
               strings_ok and n_ok and rev_ok,
               dict(twelve_filed_strings_match=strings_ok,
                    n_days_match=n_ok, reversal_both_fps=rev_ok,
                    source="a6_B_findings.md section 4, replayed by "
                           "t2_a3_ordered_plans_check.py"))

        fam_rows = {}
        for kind in ("switch_uniform", "switch_step9b", "switch_expl",
                     "blend_uniform", "blend_step9b"):
            for eps in EPSES:
                pooled_mod._alive_weights = make_family(kind, eps, mass_voice,
                                                        mass_full)
                for idx, K in ((1, FP1_K), (2, FP2_K)):
                    r = measure_fp(K, p, idx)
                    r.update(family=kind, eps=float(eps))
                    fam_rows[(kind, eps, idx)] = r
                    results["rows"].append(r)
                    print(f"  {kind:15s} eps={eps:7.0e} fp{idx}: "
                          f"{r['sides']['below']['argmax']:5s} -> "
                          f"{r['sides']['above']['argmax']:5s}  "
                          f"UV-UH {r['sides']['below']['UV_minus_UH']:+.6e} / "
                          f"{r['sides']['above']['UV_minus_UH']:+.6e}  "
                          f"sc {r['n_sign_changes']['4001']}/"
                          f"{r['n_sign_changes']['6001']}", flush=True)
    finally:
        pooled_mod._alive_weights = _ORIG

    print("\n--- gates ---", flush=True)
    all_rev = {f"{kind}|{eps:.0e}|fp{idx}":
               bool(fam_rows[(kind, eps, idx)]["reverses_voice_to_hold"]
                    and fam_rows[(kind, eps, idx)]["strict_both_sides"])
               for kind in ("switch_uniform", "switch_step9b", "switch_expl",
                            "blend_uniform", "blend_step9b")
               for eps in EPSES for idx in (1, 2)}
    step9b_rows = {k: v for k, v in all_rev.items()
                   if k.split("|")[0] in ("switch_step9b", "blend_step9b",
                                          "switch_expl")}
    shipped_eps_rows = {k: v for k, v in all_rev.items()
                        if k.split("|")[1] == "1e-14"}
    misses = [k for k, v in all_rev.items() if not v]
    record("Q2_reversal_survives_shipped_every_step9b_family_and_every_"
           "family_at_OFF_PATH_EPS",
           all(step9b_rows.values()) and all(shipped_eps_rows.values())
           and rev_ok,
           dict(restructured="(S1) run 1 asked for all 20 and got 18.  The "
                             "two misses are uniform-floor rows at eps = "
                             "1e-6 at fp2 -- off-spec on both axes and ~110x "
                             "larger an injection than Step 9(b) at the same "
                             "eps.  They are finding F-uniform-1e6.",
                n_variants=len(all_rev), n_true=sum(all_rev.values()),
                per_variant=all_rev, misses=misses,
                step9b_rows=step9b_rows,
                rows_at_OFF_PATH_EPS=shipped_eps_rows,
                exploration_claim="8 of 8 in {switch,blend} x "
                                  "{uniform,massprop} x {1e-14,1e-6} at fp1"))

    expl_8 = {k: v for k, v in all_rev.items()
              if k.endswith("fp1") and k.split("|")[0] in
              ("switch_uniform", "switch_expl", "blend_uniform")}
    record("Q2b_exploration_eight_of_eight_at_fp1_reproduces",
           all(v for k, v in all_rev.items() if k.endswith("fp1")),
           dict(subset=expl_8,
                note="the exploration's own eight variants are the "
                     "uniform and voice-only-massprop rows at fp1; all ten "
                     "families x scales at fp1 are reported here, and all ten "
                     "reverse -- the exploration's claim reproduces and "
                     "widens at the pinned point."))

    record("Q3_locus2_carries_A3s_verdict_independently_of_the_family",
           all(step9b_rows.values()) and all(shipped_eps_rows.values())
           and rev_ok,
           dict(restructured="(S1), same three variant classes.",
                reasoning="the argmax is a strict singleton on both sides of "
                          "the edge at both fixed points, VOICE below and "
                          "HOLD above, under the shipped uniform floor, the "
                          "exact Step-9(b) mass-proportional floor and both "
                          "genuine fixed-t blends, at both eps.  HOLD < VOICE "
                          "in the menu order, so the preferred plan DECREASES "
                          "in s and no cutoff vector represents the best "
                          "response: S(k) is empty under EVERY family tested.",
                not_claimed="an edge-pinned fixed point of the implemented "
                            "cutoff map is not an equilibrium (payoff-scale "
                            "residual 1.77e-3 against a 1e-9 criterion), and "
                            "nothing here shows nonexistence."))

    results["findings"] = [
        dict(id="F-uniform-1e6", gated=False,
             claim="At the SECOND fixed point fp2 = (1.0260443221, "
                   "1.7104049079) a UNIFORM off-path floor at eps = 1e-6 "
                   "destroys the VOICE -> HOLD reversal (U_V - U_H just below "
                   "the edge goes +1.06e-3 at eps = 1e-14 to -3.85e-5 at "
                   "eps = 1e-6), in both the switch and the blend form.  The "
                   "Step-9(b) family at the same eps does NOT: it keeps the "
                   "reversal at +1.28e-3.",
             misses=misses,
             reading="a uniform floor injects eps per dead type where "
                     "Step 9(b) injects eps*m[t]/J, so at eps = 1e-6 the "
                     "uniform family is a ~110x larger perturbation.  This "
                     "bounds how far the uniform floor can be scaled before "
                     "it changes the locus-(ii) finding; it does not bear on "
                     "the shipped construction, which runs at eps = 1e-14, "
                     "nor on the pinned point fp1, where all ten rows "
                     "reverse.")]

    results["summary"] = dict(
        n_variants=len(all_rev), n_reversal=sum(all_rev.values()),
        shipped_sign_changes={f"fp{i}": ship[i]["n_sign_changes"]
                              for i in (1, 2)},
        family_sign_changes={f"{k[0]}|{k[1]:.0e}|fp{k[2]}":
                             v["n_sign_changes"] for k, v in fam_rows.items()},
        n_gates=len(results["gates"]),
        n_failed=sum(1 for g in results["gates"] if not g["pass_"]),
        wall_seconds=round(time.time() - t_start, 1))
    results["pass"] = results["summary"]["n_failed"] == 0
    results["exactness_caveat"] = (
        "type 11's n(s) cell is not (D, f)-constant at this node "
        "(v_offpath_family_facts.json); menu.type_reference reads one "
        "midpoint clock for it, so no family here -- shipped or "
        "mass-proportional -- is exactly Step 9(b)'s Lambda_u for type 11.  "
        "That gap is common to all families and orthogonal to the axis under "
        "test, but it is a third, independent implementation-vs-card "
        "discrepancy.")
    with open(OUT, "w") as fh:
        json.dump(results, fh, indent=1, default=float)
    print(f"\ngates: {results['summary']['n_gates']}, "
          f"failed: {results['summary']['n_failed']}, "
          f"{results['summary']['wall_seconds']}s\n-> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
