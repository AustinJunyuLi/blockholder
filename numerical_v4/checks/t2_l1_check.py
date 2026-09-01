"""L1 -- premium cell decomposition: direct summation vs Omega M_F + (1-Omega) M_P.

Ticket 28 (T2h).  Written against the NUMERICAL CHECK REQUEST of
``research/model_v4/threads/thread1_turn2_answer.md`` (L1 block; turn-2
supersedes turn-1), cross-read with
``research/model_v4/rederive/core_D1_L1_L2_rederivation.md`` section B, and the
binding rulings of ``research/model_v4/impl_design.md`` section 13.

Checks:

  l1_decomposition_residual   WIRING  err_4 at every interior node of the D1 grid
  l1_degenerate_Omega_1       WIRING  err_5 and the isnan(M_P) clause
  l1_degenerate_Omega_0       WIRING  the mirror corner and the isnan(M_F) clause
  l1_H12_not_evaluable        record  why the H = 12 column is absent

EVERY CHECK IN THIS FILE IS A WIRING CHECK (design section 0, table row L1:
"no -- same enumeration on both sides; the residual is machine noise by
construction").  A pass here is NOT evidence for L1 and must not be quoted as
such when the ledger label moves.  The one clause with real content is the
degenerate-corner requirement that the zero-mass cell average be returned as
*undefined* rather than imputed as zero: an implementation returning M_P = 0
passes err_4 while violating exactly the clause the lemma adds.  That clause is
asserted with ``isnan``, not with a tolerance.

Both sides are computed from the same solved equilibrium object, as the
rederivation demands: ``total_premium`` sums Delta^act directly over the whole
population and ``decomposition_residual`` subtracts the two-term form.

Integration over s is deterministic (exact Phi-difference atom masses plus
20-node Gauss-Legendre inside each atom for the flagged price), never Monte
Carlo -- the rederivation asks for quadrature because O(N^-1/2) sampling noise
at N = 1e4 is three orders above the effect being tested.

Deterministic: no RNG, no file inputs, no network.

Run:    .venv/bin/python numerical_v4/checks/t2_l1_check.py
Output: numerical_v4/checks/t2_l1_check.json
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

from numerical_v4.menu import VOICE, atoms, stake_path  # noqa: E402
from numerical_v4.params import ParamsV4  # noqa: E402
from numerical_v4.policy import (  # noqa: E402
    Policy,
    evaluate,
    frozen_tau_grid,
    menu_of,
)
from numerical_v4.premium import cell_weights  # noqa: E402
from numerical_v4.solver import solve_policy  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "t2_l1_check.json")

TOL_ERR4 = 1e-12          # request: absolute residual below 1e-12
TOL_ERR5 = 1e-10          # rederivation: corner residual below 1e-10
OMEGA_LO, OMEGA_HI = 0.01, 0.99
PP = 100.0                # premium percentage points

KAPPAS = (0.15, 0.35, 0.55, 0.75, 0.85)
TS = (5, 10)
QUANTILES = (0.1, 0.3, 0.5, 0.7, 0.9)

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
    print(f"[{'PASS' if ok else 'FAIL'}] {name} ({kind})", flush=True)
    print("        " + json.dumps(detail, default=float)[:1400], flush=True)


def main() -> int:
    t0 = time.perf_counter()
    print("t2_l1_check -- frozen baseline (2 cold solves) ...", flush=True)
    p_seed = ParamsV4.baseline()
    pol_seed, _ = solve_policy(p_seed)
    taus = tuple(float(x) for x in frozen_tau_grid(pol_seed, p_seed, QUANTILES))
    tau_med = float(frozen_tau_grid(pol_seed, p_seed, (0.5,))[0])
    p_base = p_seed.replace(tau=tau_med)
    pol, resid = solve_policy(p_base)
    k = tuple(pol.k)
    print(f"  frozen k = {k}   tau ladder {['%.8f' % t for t in taus]}",
          flush=True)

    base_out = evaluate(pol, p_base, with_runup=False)
    results["provenance"] = {
        "model_card_stamp": "2026-08-20 (commit 0c9185b)",
        "commit": "0c9185b -- MODEL_CARD stamp as recorded in "
                  "numerical_v4/smoke.py; this script does not shell out to git",
        "params_hash": p_base.hash_str(),
        "design": "research/model_v4/impl_design.md section 13 APPROVED",
        "request": "research/model_v4/threads/thread1_turn2_answer.md, L1 "
                   "NUMERICAL CHECK REQUEST; core_D1_L1_L2_rederivation.md "
                   "section B",
        "classification": "design section 0 rules L1 a WIRING check: both sides "
                          "run through the same enumeration, so the residual is "
                          "machine noise by construction and is not evidence "
                          "for the lemma",
    }
    results["grid"] = {
        "kappa": list(KAPPAS), "tau": list(taus),
        "tau_quantiles": list(QUANTILES), "T": list(TS),
        "H": p_base.H, "M": 2,
        "tau_frozen_from": "percentiles of the seed-equilibrium (tau=0.05) Voice "
                           "b*(s) distribution, design section 6.2",
        "policy": "frozen at the baseline equilibrium k",
        "interior_filter": f"{OMEGA_LO} <= Omega <= {OMEGA_HI}",
        "units": "Delta^act, M_F, M_P in premium percentage points, never "
                 "normalised indices",
    }
    results["counts"] = {
        "n_hist": p_base.n_hist, "n_hist_feasible": base_out.n_hist_feasible,
        "n_theta": p_base.n_theta, "n_atoms_baseline": base_out.n_atoms,
        "discarded_mass": 0.0,
    }

    # -- err_4 over the interior grid ---------------------------------------
    rows, skipped, degenerate = [], [], []
    worst = 0.0
    multi_root = 0
    for kap in KAPPAS:
        for T in TS:
            for qi, tau in zip(QUANTILES, taus):
                p = p_base.replace(kappa=float(kap), tau=float(tau), T=int(T))
                cw = cell_weights(atoms(k, p))
                if cw.degenerate:
                    degenerate.append({"kappa": float(kap), "T": T,
                                       "tau": float(tau),
                                       "reasons": list(cw.degenerate)})
                if not (OMEGA_LO <= cw.Omega <= OMEGA_HI):
                    skipped.append({"kappa": float(kap), "T": T,
                                    "tau": float(tau), "Omega": cw.Omega,
                                    "why": "outside the request's interior "
                                           "filter 0.01 <= Omega <= 0.99"})
                    continue
                o = evaluate(pol, p, with_runup=False)
                worst = max(worst, o.decomposition_residual)
                multi_root += int(o.multiple_root_nodes)
                rows.append({
                    "kappa": float(kap), "T": T, "tau_quantile": qi,
                    "tau": float(tau), "corner": bool(T == p_base.H),
                    "Omega": o.Omega,
                    "Delta_act_pp": o.Delta_act * PP,
                    "M_F_pp": o.M_F * PP, "M_P_pp": o.M_P * PP,
                    "two_term_pp": (o.Omega * o.M_F
                                    + (1.0 - o.Omega) * o.M_P) * PP,
                    "err4": o.decomposition_residual,
                })
                print(f"  kappa={kap:.2f} T={T:2d} q={qi:.1f} Omega={o.Omega:.6f} "
                      f"D_act={o.Delta_act * PP:.10f}pp err4={o.decomposition_residual:.2e}",
                      flush=True)

    record(
        "l1_decomposition_residual",
        worst <= TOL_ERR4 and len(rows) > 0,
        "wiring",
        {
            "request": "err_4 = |Delta^act - (Omega M_F + (1-Omega) M_P)|, both "
                       "sides from the same solved equilibrium object; "
                       "predicted 0, required below 1e-12",
            "tol": TOL_ERR4, "max_err4": worst, "n_nodes": len(rows),
            "n_skipped_non_interior": len(skipped),
            "skipped": skipped[:12],
            "integration": "deterministic: exact Phi-difference atom masses plus "
                           "20-node Gauss-Legendre per atom; no Monte Carlo",
            "why_wiring": "total_premium sums Delta^act over the same "
                          "enumeration the two-term form reads; the residual "
                          "cannot falsify L1",
            "rows": rows,
        },
    )

    # -- Omega = 1 corner ---------------------------------------------------
    # All-Voice menu (cutoffs pushed to the bottom of the support) with tau low
    # enough that every type in the support crosses by H-T -- by D1 Step 8 that
    # is tau <= inf_s B_j(s, H-T), and the infimum is attained at s_lo because
    # both b*(s) and 6/n(s) increase in s.
    k_all_voice = (p_base.s_lo, p_base.s_lo)
    B_inf = float(stake_path(VOICE, p_base.s_lo, p_base)[(p_base.H - p_base.T) + 1])
    tau_1 = p_base.b0 + 0.9 * (B_inf - p_base.b0)
    p1 = p_base.replace(tau=tau_1)
    pol1 = Policy(k_all_voice, menu_of(p1))
    o1 = evaluate(pol1, p1, with_runup=False)
    err5 = abs(o1.Delta_act - o1.M_F)
    record(
        "l1_degenerate_Omega_1",
        (abs(o1.Omega - 1.0) < 1e-12 and err5 <= TOL_ERR5
         and math.isnan(o1.M_P)),
        "wiring",
        {
            "request": "one all-flagged policy with Omega = 1: verify "
                       "Delta^act = M_F and record the zero-mass cell average "
                       "as UNDEFINED rather than imputing it",
            "construction": "all-Voice menu (k = (s_lo, s_lo)) with "
                            f"tau = {tau_1:.10f} <= inf_s B(s, H-T) = {B_inf:.10f}",
            "tol_err5": TOL_ERR5,
            "Omega": o1.Omega, "err5": err5,
            "Delta_act_pp": o1.Delta_act * PP, "M_F_pp": o1.M_F * PP,
            "M_P": None if math.isnan(o1.M_P) else o1.M_P,
            "M_P_is_nan": bool(math.isnan(o1.M_P)),
            "clause_with_content": "isnan(M_P) is asserted, not a tolerance: an "
                                   "implementation returning M_P = 0 would pass "
                                   "err_4 while violating the clause the lemma "
                                   "actually adds",
            "degenerate": list(o1.degenerate_nodes),
        },
    )

    # -- Omega = 0 corner ---------------------------------------------------
    p0 = p_base.replace(tau=float(p_base.b_bar) + 0.02)
    o0 = evaluate(pol, p0, with_runup=False)
    err5b = abs(o0.Delta_act - o0.M_P)
    record(
        "l1_degenerate_Omega_0",
        (o0.Omega == 0.0 and err5b <= TOL_ERR5 and math.isnan(o0.M_F)),
        "wiring",
        {
            "request": "one all-pooled policy with Omega = 0: verify "
                       "Delta^act = M_P and record M_F as UNDEFINED",
            "construction": f"tau = {p0.tau:.4f} > b_bar = {p_base.b_bar}, so no "
                            "type ever crosses",
            "tol_err5": TOL_ERR5,
            "Omega": o0.Omega, "residual_Delta_act_minus_M_P": err5b,
            "Delta_act_pp": o0.Delta_act * PP, "M_P_pp": o0.M_P * PP,
            "M_F": None if math.isnan(o0.M_F) else o0.M_F,
            "M_F_is_nan": bool(math.isnan(o0.M_F)),
            "degenerate": list(o0.degenerate_nodes),
        },
    )

    record(
        "l1_H12_not_evaluable",
        True,
        "wiring",
        {
            "request": "design section 13, ruling 2: H = 12 robustness is cheap "
                       "for L1",
            "outcome": "NOT EVALUABLE. Every object in L1's identity -- "
                       "Delta^act and M_P -- runs through the pooled "
                       "enumeration, and at H = 12 the feasible history count "
                       "is 8,503,056, so 8,503,056 x N_theta 14 = 1.19e8 "
                       "exceeds the design's own build-step-4 gate of 1e8 "
                       "(working set ~2.5 GB). The gate is respected rather "
                       "than overridden; L1 is reported at H = 10 only.",
            "feasible_history_count_H12": 8503056,
            "gate_limit": 1e8,
        },
    )

    results["degenerate_nodes"] = degenerate
    results["multiple_root_nodes"] = multi_root
    results["baseline"] = {
        "k": list(k), "tau": tau_med, "T": p_base.T, "H": p_base.H,
        "Omega": base_out.Omega, "Delta_act_pp": base_out.Delta_act * PP,
        "M_F_pp": base_out.M_F * PP, "M_P_pp": base_out.M_P * PP,
        "cutoff_scale": resid.cutoff_scale, "payoff_scale": resid.payoff_scale,
    }
    results["seconds"] = time.perf_counter() - t0
    results["all_pass"] = results["n_fail"] == 0
    with open(OUT, "w") as fh:
        json.dump(results, fh, indent=2, default=float)
    print(f"\n{'ALL PASS' if results['all_pass'] else str(results['n_fail']) + ' FAIL'}"
          f"  in {results['seconds']:.0f} s  ->  {OUT}", flush=True)
    return 0 if results["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
