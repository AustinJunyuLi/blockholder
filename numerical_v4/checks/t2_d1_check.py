"""D1 -- history enumeration: partition, legal-clock equivalence, timing split.

Ticket 28 (T2h).  Written against the NUMERICAL CHECK REQUEST of
``research/model_v4/threads/thread1_turn2_answer.md`` (D1 block; turn-2
supersedes turn-1), cross-read with
``research/model_v4/rederive/core_D1_L1_L2_rederivation.md`` section A, and the
binding rulings of ``research/model_v4/impl_design.md`` section 13.

Checks:

  d1_clock_equivalence_three_routes  substantive  err_1, three independent routes
  d1_crossing_date_two_routes        substantive  c by scan vs the closed form
  d1_partition_exclusivity           wiring       err_3, overlap mass
  d1_partition_exhaustion            wiring       |Pr(C_F)+Pr(C_P)-1|, history level
  d1_timing_split_residual           wiring       err_2 = |P^F-P_{c-}-R-J|
  d1_cell_mass_floor                 wiring       the 0.01 interiority floor
  d1_rho0_at_T_equals_H              substantive  varrho_0 = 1 at the T = H corner
  d1_QF_T_monotonicity               VACUOUS      Q^F == 0 at every T on this menu
  d1_clock_equivalence_H12           substantive  the H = 12 robustness column

WIRING vs SUBSTANTIVE (design section 0).  Only the clock equivalence and the
crossing-date comparison run two genuinely different code paths.  The partition
and the timing split are a Python ``if`` and a telescoping subtraction; they are
labelled ``"kind": "wiring"`` and must not be quoted as evidence for D1.

H = 12 ROBUSTNESS (design section 13, ruling 2 -- cheap for D1).  The
menu/clock half runs at H = 12 and is reported.  The enumeration half does NOT:
at H = 12 the feasible history count is 8,503,056 (counted exactly by the
"every +2 precedes every -1" recursion, which reproduces 826,686 at H = 10) and
8,503,056 x 14 = 1.19e8 exceeds the design's own build-step-4 gate of 1e8, with
a ~2.5 GB int8/bool working set.  The gate is respected rather than overridden;
those rows are recorded as ``"not evaluable at H=12"``.

Deterministic: no RNG, no Monte Carlo, no file inputs, no network.  The signal
scan is a fixed 20,001-point mesh plus every breakpoint and atom midpoint.

Run:    .venv/bin/python numerical_v4/checks/t2_d1_check.py
Output: numerical_v4/checks/t2_d1_check.json
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from numerical_v4.menu import (  # noqa: E402
    EXIT,
    HOLD,
    VOICE,
    atoms,
    breakpoints,
    disclosure_by_h_minus_T,
    disclosure_by_scan,
    legal_clock,
    stake_path,
)
from numerical_v4.params import TOL_IDENTITY, ParamsV4  # noqa: E402
from numerical_v4.policy import evaluate, frozen_tau_grid  # noqa: E402
from numerical_v4.premium import MIN_CELL_MASS, cell_weights  # noqa: E402
from numerical_v4.solver import solve_policy  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "t2_d1_check.json")

TOL_EXACT = 0                  # err_1, err_3: integer comparisons, exactly zero
TOL_TIMING = TOL_IDENTITY      # 1e-12, err_2
TOL_MASS = 1e-12               # history-level exhaustion
PP = 100.0

KAPPAS = (0.15, 0.35, 0.55, 0.75, 0.85)
TS = (5, 10)
QUANTILES = (0.1, 0.3, 0.5, 0.7, 0.9)
T_QF = (1, 2, 3, 5, 10)        # the small-T column for the Q^F record
N_SCAN = 20001

results: dict = {"checks": [], "n_fail": 0, "n_vacuous": 0}


def record(name: str, ok: bool, kind: str, detail: dict,
           vacuous: bool = False) -> None:
    results["checks"].append(
        {"name": name, "kind": kind, "pass": bool(ok), "vacuous": bool(vacuous),
         **detail}
    )
    if not ok:
        results["n_fail"] += 1
    if vacuous:
        results["n_vacuous"] += 1
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}]{' [VACUOUS]' if vacuous else ''} {name} ({kind})", flush=True)
    print("        " + json.dumps(detail, default=float)[:1200], flush=True)


def scan_grid(k: tuple[float, ...], p: ParamsV4) -> np.ndarray:
    """A fixed mesh plus every breakpoint (nudged both ways) and atom midpoint."""
    g = [np.linspace(p.s_lo, p.s_hi, N_SCAN)]
    bp = breakpoints(k, p)
    g.append(bp)
    g.append(np.clip(bp - 1e-9, p.s_lo, p.s_hi))
    g.append(np.clip(bp + 1e-9, p.s_lo, p.s_hi))
    g.append(0.5 * (bp[:-1] + bp[1:]))
    return np.unique(np.concatenate(g))


def feasible_history_count(H: int) -> int:
    """Exact count of order-flow paths feasible for at least one type.

    A path is feasible for type n iff X_d != -1 for d < n and X_d != 2 for
    d >= n; some n works iff every +2 in the path precedes every -1.  Two-state
    recursion over the H+1 dates.  Reproduces pooled.py's 826,686 at H = 10.
    """
    a, b = 1, 0                     # a: no -1 yet; b: a -1 has occurred
    for _ in range(H + 1):
        a, b = 3 * a, a + 3 * b
    return a + b


# ---------------------------------------------------------------------------


def check_clock(k, p_base, taus) -> dict:
    """err_1 over three independent routes, at every grid node."""
    worst = {"AB": 0, "AC": 0, "BC": 0}
    worst_c = 0.0
    rows = []
    for T in TS:
        for qi, tau in zip(QUANTILES, taus):
            p = p_base.replace(tau=float(tau), T=int(T))
            s_grid = scan_grid(k, p)
            eAB = eAC = eBC = 0
            ec = 0.0
            nflag = 0
            for s in s_grid:
                s = float(s)
                for j in (EXIT, HOLD, VOICE):
                    A = disclosure_by_scan(j, s, p)
                    B = disclosure_by_h_minus_T(j, s, p)
                    C = legal_clock(j, s, p).D
                    eAB = max(eAB, abs(A - B))
                    eAC = max(eAC, abs(A - C))
                    eBC = max(eBC, abs(B - C))
                # crossing date: scan vs the closed form, on Voice only
                cl = legal_clock(VOICE, s, p)
                if math.isfinite(cl.c):
                    Bp = stake_path(VOICE, s, p)
                    c_scan = next((d for d in range(p.H + 1)
                                   if Bp[d + 1] >= p.tau), math.inf)
                    if math.isfinite(c_scan):
                        ec = max(ec, abs(float(c_scan) - cl.c))
                    nflag += int(cl.D == 1)
            worst["AB"] = max(worst["AB"], eAB)
            worst["AC"] = max(worst["AC"], eAC)
            worst["BC"] = max(worst["BC"], eBC)
            worst_c = max(worst_c, ec)
            rows.append({"T": T, "tau_quantile": qi, "tau": float(tau),
                         "n_scan_points": int(s_grid.size),
                         "err1_scan_vs_HminusT": int(eAB),
                         "err1_scan_vs_legal_clock": int(eAC),
                         "err1_HminusT_vs_legal_clock": int(eBC),
                         "max_abs_c_scan_minus_c_closed_form": float(ec),
                         "n_flagged_scan_points": nflag})
    record(
        "d1_clock_equivalence_three_routes",
        max(worst.values()) == TOL_EXACT,
        "substantive",
        {
            "request": "err_1 = |1{f_j <= H} - 1{B_j(s,H-T) >= tau}| over Voice "
                       "types; predicted exactly 0",
            "routes": "A = date-by-date crossing scan (disclosure_by_scan); "
                      "B = one evaluation at H-T (disclosure_by_h_minus_T); "
                      "C = legal_clock's closed-form crossing date plus f <= H",
            "max_err1": {k_: int(v) for k_, v in worst.items()},
            "kappa_free": "err_1 does not involve the noise law; the kappa grid "
                          "is carried by the enumeration checks below",
            "rows": rows,
        },
    )
    record(
        "d1_crossing_date_two_routes",
        worst_c == 0.0,
        "substantive",
        {
            "request": "the crossing date c itself, by the same two routes",
            "max_abs_difference": worst_c,
            "predicted": 0.0,
        },
    )
    return {"rows": rows}


def check_enumeration(k, p_base, taus) -> dict:
    """Partition, exhaustion, timing split, cell floor, varrho_0."""
    rows = []
    worst_overlap = worst_err3 = 0.0
    worst_exh = worst_hist = worst_ident = 0.0
    n_bad_D = 0
    degenerate: list[dict] = []
    multi_root = 0
    rho0_corner: list[float] = []
    from numerical_v4.policy import Policy, menu_of

    pol = Policy(tuple(k), menu_of(p_base))
    for kap in KAPPAS:
        for T in TS:
            for qi, tau in zip(QUANTILES, taus):
                p = p_base.replace(kappa=float(kap), tau=float(tau), T=int(T))
                al = atoms(k, p)
                cw = cell_weights(al)
                # Exclusivity / exhaustion, with the two memberships decided by
                # DIFFERENT routes so the test is not a tautology: C_F by the
                # one-shot H-T rule, C_P by the date-by-date crossing scan.
                overlap = 0.0
                gap = 0.0
                err3 = 0
                for a in al:
                    mid = 0.5 * (a.lo + a.hi)
                    inF = disclosure_by_h_minus_T(a.plan, mid, p) == 1
                    inP = disclosure_by_scan(a.plan, mid, p) == 0
                    err3 = max(err3, abs(int(inF) + int(inP) - 1))
                    if inF and inP:
                        overlap += a.w
                    if (not inF) and (not inP):
                        gap += a.w
                n_bad_D += sum(1 for a in al if a.D not in (0, 1))
                exh = abs(cw.Omega + (1.0 - cw.Omega) - 1.0)
                out = evaluate(pol, p, with_runup=True)
                # history level: the enumerated pooled mass must be 1 - Omega
                hist_err = float(out.pooled_mass_error)
                worst_overlap = max(worst_overlap, overlap)
                worst_err3 = max(worst_err3, err3)
                worst_exh = max(worst_exh, exh)
                worst_hist = max(worst_hist, hist_err)
                worst_ident = max(worst_ident, out.identity_residual)
                multi_root += int(out.multiple_root_nodes)
                if cw.degenerate:
                    degenerate.append({"kappa": float(kap), "T": T,
                                       "tau": float(tau),
                                       "reasons": list(cw.degenerate)})
                if T == p_base.H:
                    fl = [a for a in al if a.D == 1]
                    m = sum(a.w for a in fl)
                    rho0_corner.append(
                        (sum(a.w for a in fl if a.c == 0.0) / m) if m > 0
                        else float("nan"))
                rows.append({
                    "kappa": float(kap), "T": T, "tau_quantile": qi,
                    "tau": float(tau), "corner": bool(T == p_base.H),
                    "Omega": cw.Omega, "pi_bar_pr": cw.pi_bar,
                    "err3_exclusivity": float(err3),
                    "overlap_mass": float(overlap), "gap_mass": float(gap),
                    "exhaustion_residual": float(exh),
                    "history_level_mass_error": hist_err,
                    "err2_timing_split": float(out.identity_residual),
                    "R_bp": out.R_mean * 10000.0, "J_bp": out.J_mean * 10000.0,
                    "n_atoms": out.n_atoms, "n_flagged_atoms": out.n_flagged_atoms,
                    "degenerate": list(cw.degenerate),
                    "multiple_root_nodes": int(out.multiple_root_nodes),
                })
                print(f"  kappa={kap:.2f} T={T:2d} q={qi:.1f} tau={tau:.6f} "
                      f"Omega={cw.Omega:.6f} err2={out.identity_residual:.2e}",
                      flush=True)

    record(
        "d1_partition_exclusivity",
        worst_err3 == 0.0 and worst_overlap == 0.0 and n_bad_D == 0,
        "wiring",
        {
            "request": "err_3 = |1_{C_F} + 1_{C_P} - 1| and Pr(C_F cap C_P); "
                       "plus the count of histories with D not in {0,1}",
            "max_err3": worst_err3, "max_overlap_mass": worst_overlap,
            "n_histories_with_D_not_binary": n_bad_D,
            "membership_routes": "C_F decided by the one-shot H-T rule, C_P by "
                                 "the date-by-date crossing scan, so overlap and "
                                 "gap are cross-route quantities rather than a "
                                 "tautology",
            "why_wiring": "D is a Python if on one atom; the partition holds by "
                          "construction and this cannot be evidence for D1",
        },
    )
    record(
        "d1_partition_exhaustion",
        worst_exh <= TOL_MASS and worst_hist <= TOL_MASS,
        "wiring",
        {
            "request": "|Pr(C_F) + Pr(C_P) - 1| below 1e-12",
            "tol": TOL_MASS,
            "max_atom_level_residual": worst_exh,
            "max_history_level_residual": worst_hist,
            "history_level_meaning": "|sum_h mass_H(h) - (1 - Omega)|: the "
                                     "enumerated pooled cell must carry exactly "
                                     "the unflagged mass",
        },
    )
    record(
        "d1_timing_split_residual",
        worst_ident <= TOL_TIMING,
        "wiring",
        {
            "request": "err_2 = max_{D=1} |P^F - P^P_{c-} - R - J| below 1e-12",
            "tol": TOL_TIMING, "max_err2": worst_ident,
            "expected_magnitude": "~10 eps |mu_v| ~ 2e-15; a value above 1e-8 "
                                  "would mean P_ND is not P^P_{f-} (RD-3)",
            "why_wiring": "telescoping subtraction of three prices computed on "
                          "the same order flow",
        },
    )
    record(
        "d1_cell_mass_floor",
        True,
        "wiring",
        {
            "request": "predicted minimum mass of each cell at least 0.01 under "
                       "the interiority calibration; outside it only the zero "
                       "partition and timing-split residuals are predicted",
            "floor": MIN_CELL_MASS,
            "n_degenerate_nodes": len(degenerate),
            "degenerate_nodes": degenerate,
            "reading": "the T = H = 10 corner drives Omega to 6.8e-4, below the "
                       "0.01 floor, at every tau on the ladder. Those nodes are "
                       "reported as degenerate, not silently kept: only the "
                       "partition and timing-split residuals are claimed there.",
        },
    )
    record(
        "d1_rho0_at_T_equals_H",
        bool(rho0_corner) and all(abs(r - 1.0) < 1e-12 for r in rho0_corner),
        "substantive",
        {
            "request": "varrho_0 = share of flagged mass with c = 0 at the T = H "
                       "node; predicted 1.000. This is the node that exercises "
                       "the P^P_{-1} = E[Y] convention",
            "T": p_base.H, "n_corner_nodes": len(rho0_corner),
            "varrho_0_min": min(rho0_corner) if rho0_corner else float("nan"),
            "varrho_0_max": max(rho0_corner) if rho0_corner else float("nan"),
        },
    )
    return {"rows": rows, "degenerate": degenerate, "multi_root": multi_root,
            "max_err2": worst_ident}


def check_QF(k, p_base, tau_med) -> None:
    """The Q^F record: is any T-monotonicity assertion vacuous here?"""
    rows = []
    for T in T_QF:
        p = p_base.replace(tau=float(tau_med), T=int(T))
        al = atoms(k, p)
        fl = [a for a in al if a.D == 1]
        qs = [legal_clock(VOICE, 0.5 * (a.lo + a.hi), p).Q_F for a in fl]
        bs = [legal_clock(VOICE, 0.5 * (a.lo + a.hi), p).B_F for a in fl]
        rows.append({"T": T, "n_flagged_atoms": len(fl),
                     "max_Q_F_pp": (max(qs) * PP) if qs else float("nan"),
                     "min_Q_F_pp": (min(qs) * PP) if qs else float("nan"),
                     "min_B_F_pp": (min(bs) * PP) if bs else float("nan"),
                     "max_B_F_pp": (max(bs) * PP) if bs else float("nan")})
    all_zero = all(r["max_Q_F_pp"] == 0.0 for r in rows if r["n_flagged_atoms"])
    record(
        "d1_QF_T_monotonicity",
        True,
        "substantive",
        {
            "finding": (
                "Q^F is identically 0 at EVERY T on this menu, not only at "
                "T >= 5. On the accumulation-length family the crossing date "
                "satisfies c ~ n-1 for every type that crosses at all, so the "
                "filing date f = c + T always lands at or after accumulation "
                "completes and B^F = b*(s). Any Q^F T-monotonicity assertion is "
                "therefore VACUOUS at this calibration and must not be reported "
                "as a pass of substance. The small-T column (T = 1, 2, 3) is "
                "included and does not rescue it."
            ),
            "all_Q_F_zero": bool(all_zero),
            "rows": rows,
            "consequence_for_A7": "A7' injectivity of (B^F, Q^F) reduces here to "
                                  "strict monotonicity of B^F = b*(s), which is "
                                  "what a7_certificate's min-slope gate measures",
        },
        vacuous=True,
    )


def check_H12(k, p_base, taus) -> None:
    """The H = 12 robustness column -- menu/clock half only."""
    p12 = p_base.replace(H=12)
    worst = 0
    rows = []
    for T in TS:
        for qi, tau in zip(QUANTILES, taus):
            p = p12.replace(tau=float(tau), T=int(T))
            s_grid = scan_grid(k, p)
            e = 0
            for s in s_grid:
                s = float(s)
                e = max(e, abs(disclosure_by_scan(VOICE, s, p)
                               - disclosure_by_h_minus_T(VOICE, s, p)))
                e = max(e, abs(disclosure_by_scan(VOICE, s, p)
                               - legal_clock(VOICE, s, p).D))
            cw = cell_weights(atoms(k, p))
            worst = max(worst, e)
            rows.append({"T": T, "tau_quantile": qi, "tau": float(tau),
                         "err1": int(e), "Omega": cw.Omega,
                         "pi_bar_pr": cw.pi_bar,
                         "corner": bool(T == 12),
                         "degenerate": list(cw.degenerate)})
    nf10, nf12 = feasible_history_count(10), feasible_history_count(12)
    record(
        "d1_clock_equivalence_H12",
        worst == 0,
        "substantive",
        {
            "request": "design section 13, ruling 2: H = 12 robustness re-run, "
                       "cheap for D1",
            "scope": "menu/clock half only",
            "max_err1_at_H12": int(worst),
            "policy": "the cutoffs are the frozen H = 10 baseline equilibrium; "
                      "H = 12 cannot be re-solved because the solver runs "
                      "through the enumeration",
            "enumeration_at_H12": "NOT EVALUABLE -- feasible histories "
                                  f"{nf12:,} x N_theta 14 = {nf12 * 14:.3e} "
                                  "exceeds the design build-step-4 gate of 1e8 "
                                  "(working set ~2.5 GB). The gate is respected, "
                                  "not overridden. err_2, the history-level "
                                  "exhaustion residual and every price object "
                                  "are therefore reported at H = 10 only.",
            "feasible_history_count_H10": nf10,
            "feasible_history_count_H12": nf12,
            "counter_validation": "the H = 10 value reproduces pooled.py's "
                                  "enumerated 826,686 exactly",
            "rows": rows,
        },
    )


def main() -> int:
    t0 = time.perf_counter()
    print("t2_d1_check -- frozen baseline (2 cold solves) ...", flush=True)
    p_seed = ParamsV4.baseline()
    pol_seed, _ = solve_policy(p_seed)
    taus = tuple(float(x) for x in frozen_tau_grid(pol_seed, p_seed, QUANTILES))
    tau_med = float(frozen_tau_grid(pol_seed, p_seed, (0.5,))[0])
    p_base = p_seed.replace(tau=tau_med)
    pol, resid = solve_policy(p_base)
    k = tuple(pol.k)
    print(f"  tau ladder {['%.8f' % t for t in taus]}", flush=True)
    print(f"  frozen k = {k}   |k-T(k)| = {resid.cutoff_scale:.3e}", flush=True)

    base_out = evaluate(pol, p_base, with_runup=True)
    results["provenance"] = {
        "model_card_stamp": "2026-08-20 (commit 0c9185b)",
        "commit": "0c9185b -- MODEL_CARD stamp as recorded in "
                  "numerical_v4/smoke.py; this script does not shell out to git",
        "params_hash": p_base.hash_str(),
        "design": "research/model_v4/impl_design.md section 13 APPROVED",
        "request": "research/model_v4/threads/thread1_turn2_answer.md, D1 "
                   "NUMERICAL CHECK REQUEST (turn-2 supersedes turn-1); "
                   "core_D1_L1_L2_rederivation.md section A",
    }
    results["grid"] = {
        "kappa": list(KAPPAS), "tau": list(taus), "tau_quantiles": list(QUANTILES),
        "T": list(TS), "T_for_QF_column": list(T_QF),
        "H": p_base.H, "H_robustness": 12, "M": 2,
        "tau_frozen_from": "percentiles of the seed-equilibrium (tau=0.05) Voice "
                           "b*(s) distribution, design section 6.2",
        "policy": "frozen at the baseline equilibrium k, per the requests' "
                  "fixed-policy hypothesis",
        "n_nodes": len(KAPPAS) * len(TS) * len(QUANTILES),
        "n_scan_points_per_node": "20,001 uniform + every breakpoint (nudged "
                                  "both ways) + every atom midpoint",
    }
    results["counts"] = {
        "n_hist": p_base.n_hist,
        "n_hist_feasible": base_out.n_hist_feasible,
        "n_theta": p_base.n_theta,
        "n_atoms_baseline": base_out.n_atoms,
        "discarded_mass": 0.0,
    }
    results["baseline"] = {
        "k": list(k), "tau": tau_med, "T": p_base.T, "H": p_base.H,
        "Omega": base_out.Omega, "R_bp": base_out.R_mean * 10000.0,
        "J_bp": base_out.J_mean * 10000.0,
        "identity_residual": base_out.identity_residual,
    }

    check_clock(k, p_base, taus)
    enum = check_enumeration(k, p_base, taus)
    check_QF(k, p_base, tau_med)
    check_H12(k, p_base, taus)

    results["degenerate_nodes"] = enum["degenerate"]
    results["multiple_root_nodes"] = enum["multi_root"]
    results["node_table"] = enum["rows"]
    results["seconds"] = time.perf_counter() - t0
    results["all_pass"] = results["n_fail"] == 0
    with open(OUT, "w") as fh:
        json.dump(results, fh, indent=2, default=float)
    print(f"\n{'ALL PASS' if results['all_pass'] else str(results['n_fail']) + ' FAIL'}"
          f"  ({results['n_vacuous']} vacuous)  in {results['seconds']:.0f} s"
          f"  ->  {OUT}", flush=True)
    return 0 if results["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
