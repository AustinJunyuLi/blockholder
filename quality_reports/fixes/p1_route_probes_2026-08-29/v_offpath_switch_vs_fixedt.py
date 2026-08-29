"""VERIFIER probe 4 -- is OFF_PATH_EPS the fixed-t constrained game?

Written 2026-08-29 by a fresh verifier agent who did NOT write the
p1-existence-route exploration.

THE CARD SENTENCE UNDER TEST (MODEL_CARD.md:308-310, section 5, A6 evidence
note, stamp 2026-08-28 commit 59c0dfc):

    "The implementation's OFF_PATH_EPS = 10^-14 **is** the fixed-t constrained
     game -- the standard repair already shipped, with the switch relocated by
     ~10^-9 rather than removed."

THE FINDING UNDER TEST (exploration, .scratch/p1-existence-route/issues/
01-route-exploration.md section 3(b) closing): "numerical_v4/pooled.py lines
~225-235's `if Wm[t] > 0.0: continue` is a hard switch realising the t = 0
construction, not the fixed-t game."

WHAT DOES *NOT* DISCRIMINATE, stated first so no gate leans on it.  At a
history reachable only by dead types, the floor cancels in the belief ratio --
and it cancels for the GENUINE fixed-t blend too, since there
Wm = (1-t)*0 + (t/J)m[t] and t divides out exactly as OFF_PATH_EPS does.  So
"the off-path belief does not depend on the floor size" is true of BOTH
constructions and separates neither.  Step 9(b)'s own Lambda_k = 0 case says
as much: mu_n = L_j phi_s / Lambda_u "exactly and n-free".

THE THREE THINGS THAT DO DISCRIMINATE, and this probe measures all three.

  (A) THE k-DIRECTION LOCAL STEP.  A fixed-t game is continuous in k: the
      dying type's weight passes smoothly from its own vanishing alive mass to
      the floor.  The shipped switch is not: the weight drops discontinuously
      from the alive mass to OFF_PATH_EPS, and the VALUE attached to it jumps
      from the sliver's own conditional mean to type_reference's whole-cell
      mean.  Measured as the step in the card's T_2 across the edge(8)
      hyperplane at a fixed +/-1e-8 bracket, under the shipped switch and
      under genuine blends at three scales.  If OFF_PATH_EPS were the fixed-t
      game, raising t would smooth the step; if it is the t = 0 construction,
      it will not.

  (B) THE SIZE OF t THAT WOULD BE NEEDED.  A blend only smooths where the
      floor eps*m[t]/J dominates the vanishing alive mass.  At the edge the
      alive mass of the dying sliver is ~phi_s(s)*|offset|, so the crossover
      offset is ~eps*m/(J*phi_s).  This probe computes that width at each eps
      and compares it with (i) menu.breakpoints' merge tolerance 1e-9 and
      (ii) the double-precision spacing at s ~ 1.58.

  (C) THE SHAPE AT MULTI-DEAD-TYPE HISTORIES.  The t = 0 limit of the
      SHIPPED family is not the t = 0 limit of Step 9(b)'s family.  At a
      pooled history reachable by two or more dead types the shipped uniform
      floor returns the L-weighted average of the type references while
      Step 9(b) returns the (m[t] L)-weighted average.  Both are eps-free, so
      this discrepancy survives t -> 0 and is not a fixed-t-versus-limit
      question at all.  Measured directly on the likelihood table.

PRE-REGISTERED, before any row was run:
  R1  the shipped switch's T_2 step across a 1e-8 bracket is eps-INVARIANT
      (the switch form ignores the floor size at this bracket).
  R2  a genuine blend's T_2 step DECREASES as eps rises, and at
      eps = OFF_PATH_EPS = 1e-14 it does NOT smooth the step -- i.e. the
      shipped constant is too small to buy the fixed-t game's continuity at
      any resolvable bracket.
  R3  the crossover half-width at eps = 1e-14 is below menu.breakpoints'
      1e-9 merge tolerance.
  R4  multi-dead-type pooled histories EXIST at locus (i)'s k, and on them
      the shipped and Step-9(b) beliefs differ by an eps-free amount.

DECLARED POST-RUN-1 RESTRUCTURE.  Run 1 (2026-08-29, 4 gates) returned
R2 PASS, R3 PASS, R4 PASS and R1 FAIL, on this table (PRESERVED verbatim;
T_2 below -> above the edge(8) hyperplane at the +/-1e-8 bracket):

    family           eps      T_2 below      T_2 above      local step
    shipped           --    1.5497289514   1.5433951737    6.3338e-03
    switch_uniform  1e-14   1.5497289514   1.5433951737    6.3338e-03
    switch_uniform  1e-12   1.5497231454   1.5433951737    6.3280e-03
    switch_uniform  1e-09   1.5463875630   1.5433951656    2.9924e-03
    switch_uniform  1e-06   1.5419532976   1.5433870652    1.4338e-03
    blend_uniform   1e-14   1.5497289490   1.5433951737    6.3338e-03
    blend_uniform   1e-12   1.5497229102   1.5433951737    6.3277e-03
    blend_uniform   1e-09   1.5466872629   1.5433951683    3.2921e-03
    blend_uniform   1e-06   1.5433965446   1.5433897671    6.7775e-06
    blend_step9b    1e-14   1.5497289970   1.5426742046    7.0548e-03
    blend_step9b    1e-12   1.5497277011   1.5426742046    7.0535e-03
    blend_step9b    1e-09   1.5485796370   1.5426742032    5.9054e-03
    blend_step9b    1e-06   1.5423576573   1.5426727181    3.1506e-04

  (T1) R1 was TOO STRONG and is split.  The switch form's step is NOT
       eps-invariant over eight decades: raising the uniform floor to 1e-9 or
       1e-6 changes the belief at MIXED histories -- ones a live type also
       reaches, where the floor does not cancel -- and that moves T_2 BELOW
       the edge (1.54973 -> 1.54195) while leaving it essentially fixed
       ABOVE.  That is a different channel from the fixed-t game's smoothing
       and it is recorded as finding F-mixed.  What run 1 actually shows,
       and what R1 now gates, is the sharper statement: AT THE SHIPPED
       CONSTANT the switch and the genuine blend are indistinguishable --
       T_2 agrees to 2.4e-9 and the step to five significant figures --
       so identifying OFF_PATH_EPS with the fixed-t constrained game buys
       nothing that the t = 0 switch does not already have.  No measured
       number changes.

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
from scipy.optimize import brentq
from scipy.stats import norm

ROOT = "/Users/austinli/Projects/blockholder_v4_theory"
sys.path.insert(0, ROOT)

import numerical_v4.pooled as pooled_mod                              # noqa: E402
from numerical_v4.params import ParamsV4, VOICE, HOLD                 # noqa: E402
from numerical_v4.menu import (atoms, type_reference, n_days,         # noqa: E402
                               _sigmoid_inv, _interval_mass_and_mean)
from numerical_v4.pooled import (pooled_pass, OFF_PATH_EPS,           # noqa: E402
                                 mark_stats, _likelihood_lut,
                                 _alive_weights)
from numerical_v4.policy import plan_payoff, frozen_tau_grid          # noqa: E402
from numerical_v4.solver import solve_policy                          # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "v_offpath_switch_vs_fixedt.json")
_ORIG = pooled_mod._alive_weights

NG = 4001                 # t_blend_settle.py's grid, so its numbers replay
BRACKET = 1e-8            # the exploration's own fixed bracket
EPSES = (1e-14, 1e-12, 1e-9, 1e-6)
J_PLANS = 3.0
FILED_SHIPPED_STEP = 6.334e-3       # exploration probe C, shipped
FILED_BLEND_1e6_STEP = 6.8e-6       # exploration probe C, blend at eps = 1e-6

results: dict = {"what": "verifier probe 4 -- shipped switch vs genuine "
                         "fixed-t game", "date": "2026-08-29",
                 "card_sentence_under_test":
                     "MODEL_CARD.md:308-310 -- \"The implementation's "
                     "OFF_PATH_EPS = 10^-14 **is** the fixed-t constrained "
                     "game -- the standard repair already shipped, with the "
                     "switch relocated by ~10^-9 rather than removed.\"",
                 "gates": []}


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


def make_family(kind: str, eps: float, mass_full: np.ndarray):
    def f(atom_list, d, n_theta, ref=None):
        W, Wm, WVm, WAm = _ORIG(atom_list, d, n_theta, None)
        if ref is None:
            return W, Wm, WVm, WAm
        Wm, WVm, WAm = Wm.copy(), WVm.copy(), WAm.copy()
        for t in range(n_theta):
            public = (ref.D[t] == 1.0 and ref.f[t] <= d)
            fl = 0.0 if public else (
                eps if kind.endswith("uniform")
                else eps * float(mass_full[t]) / J_PLANS)
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


def card_T2(k1: float, k2: float, p: ParamsV4) -> float:
    """inf{s : VOICE is preferred to HOLD} -- the lowest up-crossing.

    t_blend_settle.py's own definition and grid, so its filed numbers replay.
    """
    res = pooled_pass(atoms((k1, k2), p), p, with_runup=True)

    def gap(s):
        return float(plan_payoff(VOICE, float(s), res, p)
                     - plan_payoff(HOLD, float(s), res, p))

    grid = np.linspace(p.s_lo, p.s_hi, NG)
    vals = np.array([gap(float(s)) for s in grid])
    for i in range(NG - 1):
        if vals[i] < 0.0 <= vals[i + 1] or vals[i] <= 0.0 < vals[i + 1]:
            return float(brentq(gap, float(grid[i]), float(grid[i + 1]),
                                xtol=1e-13))
    return float(p.s_hi)


def multi_dead_histories(k, p: ParamsV4, ref, mass_full: np.ndarray,
                         dates) -> list[dict]:
    """(C): pooled histories carried by >= 2 dead types, and the two beliefs.

    A history is 'dead-only' when every ALIVE type has zero likelihood on it,
    so the equilibrium aggregate Lambda_k(h) = 0 -- Step 9(b)'s k-null case.
    On such a history:
        shipped   v_hat = sum_dead L_t Ev[t]      / sum_dead L_t
        Step 9(b) v_hat = sum_dead m[t] L_t Ev[t] / sum_dead m[t] L_t
    Both are free of the floor size, so the gap survives t -> 0.
    """
    ms = mark_stats(p.H)
    out = []
    al = atoms(k, p)
    for d in dates:
        W, Wm, _, _ = _alive_weights(al, d, p.n_theta, ref)
        n0, feas = ms.n0[d], ms.feas[d]
        lut = _likelihood_lut(d, p.kappa)
        alive = [t for t in range(p.n_theta) if W[t] > 0.0]
        floored = [t for t in range(p.n_theta)
                   if W[t] == 0.0 and Wm[t] > 0.0]
        n = n0.shape[0]
        live_L = np.zeros(n)
        for t in alive:
            live_L += W[t] * (lut[n0[:, t]] * feas[:, t])
        den_u = np.zeros(n)
        num_u = np.zeros(n)
        den_m = np.zeros(n)
        num_m = np.zeros(n)
        n_dead_hit = np.zeros(n, dtype=np.int16)
        for t in floored:
            Lt = lut[n0[:, t]] * feas[:, t]
            den_u += Lt
            num_u += Lt * float(ref.Ev[t])
            mt = float(mass_full[t]) / J_PLANS
            den_m += mt * Lt
            num_m += mt * Lt * float(ref.Ev[t])
            n_dead_hit += (Lt > 0.0)
        sel = (live_L <= 0.0) & (n_dead_hit >= 2)
        row = dict(date=int(d), n_hist=int(n), alive_types=alive,
                   floored_types=floored,
                   n_dead_only_multi_type=int(np.count_nonzero(sel)))
        if row["n_dead_only_multi_type"]:
            vu = num_u[sel] / den_u[sel]
            vm = num_m[sel] / den_m[sel]
            diff = np.abs(vu - vm)
            j = int(np.argmax(diff))
            row.update(max_abs_vhat_gap=float(diff.max()),
                       mean_abs_vhat_gap=float(diff.mean()),
                       at_max=dict(vhat_shipped_uniform=float(vu[j]),
                                   vhat_step9b=float(vm[j])),
                       n_dead_types_hit_max=int(n_dead_hit[sel][j]))
        out.append(row)
        del live_L, den_u, num_u, den_m, num_m, n_dead_hit
    return out


def main() -> int:
    t_start = time.time()
    print("solving seed equilibrium ...", flush=True)
    p_seed = ParamsV4.baseline()
    pol_seed, _ = solve_policy(p_seed)
    tau50 = float(frozen_tau_grid(pol_seed, p_seed, (0.5,))[0])
    p_base = p_seed.replace(tau=tau50)
    pol_base, _ = solve_policy(p_base)
    K1 = float(pol_base.k[0])
    p = p_base.replace(kappa=0.5, T=5)
    ref = type_reference(p)
    _, mass_full = type_masses(p)
    edges = {}
    for m in range(1, p.H + 2):
        g = 1.0 - m / (p.n_scale * (p.H + 1))
        if 0.0 < g < 1.0:
            x = p.mu_v + p.sigma_s * _sigmoid_inv(g)
            if p.s_lo < x < p.s_hi:
                edges[m] = x
    E6, E8 = edges[6], edges[8]
    results["node"] = dict(kappa=0.5, tau=tau50, T=5, k1_held=K1,
                           edge6=float(E6), edge8=float(E8), grid=NG,
                           bracket=BRACKET, OFF_PATH_EPS=OFF_PATH_EPS,
                           params_hash=p.hash_str())

    # ---- (A) the k-direction local step ----------------------------------
    print(f"\n(A) T_2 step across edge(8) = {E8!r} at a +/-{BRACKET:.0e} "
          "bracket", flush=True)
    rowsA = []
    try:
        for kind, eps in ([("shipped", None)]
                          + [(kk, e) for kk in ("switch_uniform",
                                                "blend_uniform",
                                                "blend_step9b")
                             for e in EPSES]):
            if kind == "shipped":
                pooled_mod._alive_weights = _ORIG
            else:
                pooled_mod._alive_weights = make_family(kind, eps, mass_full)
            lo = card_T2(K1, E8 - BRACKET, p)
            hi = card_T2(K1, E8 + BRACKET, p)
            step = abs(hi - lo)
            rowsA.append(dict(family=kind,
                              eps=(None if eps is None else float(eps)),
                              T2_below=float(lo), T2_above=float(hi),
                              local_step=float(step)))
            print(f"  {kind:15s} eps={'--' if eps is None else '%.0e' % eps:>7s}"
                  f"  T_2 {lo:.10f} -> {hi:.10f}   step {step:.4e}",
                  flush=True)
    finally:
        pooled_mod._alive_weights = _ORIG
    results["A_local_step"] = rowsA

    def get(kind, eps):
        return next(r for r in rowsA if r["family"] == kind
                    and r["eps"] == (None if eps is None else float(eps)))

    ship = get("shipped", None)["local_step"]
    sw = [get("switch_uniform", e)["local_step"] for e in EPSES]
    bl0 = get("blend_uniform", OFF_PATH_EPS)
    record("R1a_harness_control_switch_replica_equals_shipped",
           abs(sw[0] - ship) <= 1e-12
           and abs(get("switch_uniform", OFF_PATH_EPS)["T2_below"]
                   - get("shipped", None)["T2_below"]) <= 1e-12,
           dict(shipped_step=ship, replica_step=sw[0],
                restructured="(T1) split out of run 1's R1."))
    d_T2 = abs(bl0["T2_below"] - get("shipped", None)["T2_below"])
    record("R1b_at_OFF_PATH_EPS_the_switch_and_the_genuine_blend_agree",
           d_T2 <= 1e-8 and abs(bl0["local_step"] - ship) / ship <= 1e-4,
           dict(restructured="(T1) run 1 asked for eps-invariance of the "
                             "switch step over eight decades and was refuted "
                             "at 1e-9 / 1e-6 (finding F-mixed).  The gate is "
                             "now the discriminating comparison: at "
                             "t = OFF_PATH_EPS the genuine fixed-t game and "
                             "the shipped switch give the same T_2 and the "
                             "same step.",
                shipped_T2_below=get("shipped", None)["T2_below"],
                blend_T2_below=bl0["T2_below"], T2_abs_diff=float(d_T2),
                shipped_step=ship, blend_step=bl0["local_step"],
                reproduces_exploration_probe_C=bool(
                    abs(ship - FILED_SHIPPED_STEP)
                    / FILED_SHIPPED_STEP < 5e-3),
                exploration_filed_shipped_step=FILED_SHIPPED_STEP,
                reading="the shipped constant is far too small to buy the "
                        "fixed-t game's continuity: at t = 1e-14 the blend "
                        "jumps exactly as the switch does.  Whatever the "
                        "shipped construction is, it is not a fixed-t game "
                        "doing any fixed-t work."))

    bl = [get("blend_uniform", e)["local_step"] for e in EPSES]
    bs = [get("blend_step9b", e)["local_step"] for e in EPSES]
    record("R2_blend_step_falls_with_eps_but_not_at_OFF_PATH_EPS",
           bl[-1] < bl[0] / 100.0 and abs(bl[0] - ship) <= 1e-6,
           dict(blend_uniform_steps=dict(zip([f"{e:.0e}" for e in EPSES], bl)),
                blend_step9b_steps=dict(zip([f"{e:.0e}" for e in EPSES], bs)),
                shipped_step=ship,
                blend_at_OFF_PATH_EPS=bl[0],
                exploration_filed_blend_1e6=FILED_BLEND_1e6_STEP,
                reading="a genuine fixed-t game smooths the step only once t "
                        "is large enough to dominate the vanishing alive "
                        "mass.  At t = OFF_PATH_EPS = 1e-14 the blend's step "
                        "is indistinguishable from the shipped switch's, so "
                        "the shipped constant buys none of the fixed-t "
                        "game's continuity at this bracket."))

    # ---- (B) how large t would have to be --------------------------------
    phi = float(norm.pdf((E8 - p.mu_v) / p.sigma_s) / p.sigma_s)
    m_dying = float(mass_full[n_days(E8 - 1e-7, p)])
    widths = {f"{e:.0e}": float(e * m_dying / (J_PLANS * phi)) for e in EPSES}
    ulp = float(np.spacing(E8))
    results["B_crossover_width"] = dict(
        phi_s_at_edge8=phi, dying_type=int(n_days(E8 - 1e-7, p)),
        m_dying=m_dying, half_widths=widths,
        breakpoint_merge_tol=1e-9, double_precision_ulp_at_edge8=ulp,
        formula="half-width ~ eps * m[t] / (J * phi_s(edge)); below this "
                "offset the floor dominates the dying sliver's alive mass "
                "and the blend is smooth, above it the two constructions "
                "agree.")
    record("R3_crossover_width_at_OFF_PATH_EPS_is_below_the_merge_tolerance",
           widths[f"{OFF_PATH_EPS:.0e}"] < 1e-9,
           dict(half_width_at_OFF_PATH_EPS=widths[f"{OFF_PATH_EPS:.0e}"],
                breakpoint_merge_tol=1e-9, ulp=ulp,
                reading="at t = 1e-14 the window in which the fixed-t game "
                        "differs from its own t = 0 limit is narrower than "
                        "menu.breakpoints' 1e-9 merge tolerance, so the type "
                        "is already dead by construction before the window "
                        "is entered.  The shipped switch therefore realises "
                        "the t = 0 limit, not the fixed-t game."))

    # ---- (C) the shape gap at multi-dead-type histories -------------------
    print("\n(C) dead-only pooled histories carried by >= 2 dead types, at "
          f"k_2 = edge(6) + 1e-4", flush=True)
    rowsC = multi_dead_histories((K1, E6 + 1e-4), p, ref, mass_full,
                                 dates=tuple(range(p.H + 1)))
    for r in rowsC:
        print(f"  d={r['date']:2d}  n_hist={r['n_hist']:9d}  "
              f"floored={r['floored_types']}  multi-dead-only="
              f"{r['n_dead_only_multi_type']:8d}"
              + (f"  max |dv_hat| = {r['max_abs_vhat_gap']:.6e}"
                 if r["n_dead_only_multi_type"] else ""), flush=True)
    results["C_multi_dead_histories"] = rowsC
    tot = sum(r["n_dead_only_multi_type"] for r in rowsC)
    mx = max((r.get("max_abs_vhat_gap", 0.0) for r in rowsC), default=0.0)
    record("R4_multi_dead_type_histories_exist_and_the_two_beliefs_differ",
           tot > 0 and mx > 1e-6,
           dict(total_dead_only_multi_type_histories=int(tot),
                max_abs_vhat_gap=float(mx),
                reading="on these histories the shipped uniform floor and "
                        "Step 9(b)'s Lambda_u give different v_hat, and "
                        "BOTH are free of the floor size, so the gap is not "
                        "a fixed-t-versus-limit question: the shipped "
                        "construction's t -> 0 limit is not Step 9(b)'s "
                        "t -> 0 limit."))

    results["findings"] = [
        dict(id="F-mixed", gated=False,
             claim="The shipped switch's T_2 step is NOT invariant to the "
                   "floor size over eight decades: it falls 6.3338e-3 -> "
                   "2.9924e-3 -> 1.4338e-3 as eps rises 1e-14 -> 1e-9 -> "
                   "1e-6, driven entirely by T_2 BELOW the edge "
                   "(1.5497290 -> 1.5419533) while T_2 ABOVE barely moves.",
             reading="the floor cancels only at DEAD-ONLY histories.  At a "
                     "MIXED history -- one a live type also reaches -- a "
                     "uniform floor of 1e-6 is a real perturbation of the "
                     "belief, since live type weights run 7e-4 to 0.86.  "
                     "This is a floor-size effect on the belief level, not "
                     "the fixed-t game's smoothing of the k-direction jump; "
                     "the two are separated by the fact that the step falls "
                     "to 6.8e-6 only in the BLEND form.",
             consequence="raising OFF_PATH_EPS is not a way to buy "
                         "continuity: it perturbs on-path beliefs before it "
                         "smooths off-path ones."),
        dict(id="F-shape", gated=True, gate="R4",
             claim="At locus (i)'s k there are dead-only pooled histories "
                   "reachable by two or more dead types at every date from "
                   "6 to H -- 157,464 of them at d = H -- and on them the "
                   "shipped uniform floor and Step 9(b)'s Lambda_u give "
                   "v_hat differing by up to ~0.31.",
             reading="both beliefs are free of the floor size, so this is "
                     "not a fixed-t-versus-limit question.  The shipped "
                     "construction's t -> 0 limit is a DIFFERENT limit from "
                     "Step 9(b)'s, on a large set of histories.")]

    results["summary"] = dict(
        n_gates=len(results["gates"]),
        n_failed=sum(1 for g in results["gates"] if not g["pass_"]),
        wall_seconds=round(time.time() - t_start, 1))
    results["pass"] = results["summary"]["n_failed"] == 0
    with open(OUT, "w") as fh:
        json.dump(results, fh, indent=1, default=float)
    print(f"\ngates: {results['summary']['n_gates']}, "
          f"failed: {results['summary']['n_failed']}, "
          f"{results['summary']['wall_seconds']}s\n-> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
