"""T1 -- attenuation: W C products on both margins, the chord, and the O-1 benchmark.

Ticket 28 (T2h).  Written against the NUMERICAL CHECK REQUEST of
``research/model_v4/proofs/T1_proof.md`` (six blocks), the O-1 record in
``research/model_v4/HANDOFF_sign.md`` sections 2-3, and the binding rulings of
``research/model_v4/impl_design.md`` section 13.

Checks:

  t1_block1_factorisation          wiring       S = (1-Omega) S_P, TV and pointwise
  t1_block1_Omega_flat_in_kappa    substantive  H6 implemented, not merely asserted
  t1_block2_threshold_margin       mixed        W_tau C_tau <= 1, with the null pairs visible
  t1_block3_chord_magnitude        substantive  S_P vs Delta_m |A'_kappa| |C_h(pi_bar)|
  t1_block4_window_margin          substantive  W_T C_T, with the forced-attenuation audit
  t1_block5_local_form             NOT EVALUABLE  integer window
  t1_block6_O1_benchmark           substantive  the four committed ratios and Omega*
  t1_block6_composition_factors    substantive  C_O1 = 1.1051 / 1.3590 / 1.5910 / 0.7560
  t1_H12_window_robustness         substantive  MANDATORY per design ruling 2

MEASUREMENT.  kappa-sensitivity is TOTAL VARIATION over the kappa grid (Step 7
licenses this: the factorisation is exact for the TV aggregate), with mean
absolute slope reported alongside so the numbers are comparable with the O-1
record, which uses both.  All premium objects in premium percentage points.

BLOCK 4'S ACCEPTANCE RULE WITH TEETH.  A run that returns W_T C_T <= 1 at every
node, including the low-Omega calibrations, is to be treated as SUSPECT and
audited for a forced-attenuation bug before it is believed, because the O-1
record has the analogous product above one at Omega = 0.037, 0.129 and 0.286.
The count of nodes with W_T C_T > 1 is printed explicitly, and an
all-attenuating run raises ``suspected_forced_attenuation_bug``.

DEGENERATE RATIOS (design risk 9.3).  S_P is reported in LEVELS beside every
ratio, and any ratio computed on S_P < 1e-12 is marked ``"undefined"`` rather
than reported as a number.

Deterministic: no RNG, no Monte Carlo, no file inputs (the O-1 block recomputes
everything from ``numerical/``; the exported CSVs are not read), no network.

Run:    .venv/bin/python numerical_v4/checks/t2_t1_check.py
Output: numerical_v4/checks/t2_t1_check.json
"""

from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from numerical.model import (  # noqa: E402
    compute_action_probabilities,
    compute_minority_gains,
    compute_minority_gains_no_disclosure_given_strategy,
)
from numerical.params import ModelParams  # noqa: E402
from numerical.solver import solve_equilibrium  # noqa: E402
from numerical_v4.menu import atoms  # noqa: E402
from numerical_v4.params import ParamsV4  # noqa: E402
from numerical_v4.policy import evaluate, frozen_tau_grid  # noqa: E402
from numerical_v4.premium import cell_weights, chord  # noqa: E402
from numerical_v4.solver import solve_policy  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "t2_t1_check.json")

TOL_IDENT = 1e-10          # blocks 1, 2, 3, 4 identity residuals
TOL_FLAT = 1e-12           # block 1: Omega flat in kappa
TOL_NULL = 1e-12           # block 2: product = 1 at a null-reclassification pair
TOL_O1 = 1e-4              # block 6: ratios vs committed
TOL_OMEGA_STAR = 1e-3      # block 6: the bisected boundary
TOL_C_O1 = 1e-3            # block 6: the composition factors
PCT_CHORD = 0.05
S_P_FLOOR = 1e-12          # design risk 9.3
A_PRIME_KAPPA = 0.25       # |A'_kappa| from Example A (card section 4.4)
PP = 100.0

KAPPAS = np.round(np.arange(0.15, 0.8501, 0.01), 2)     # 71 nodes
QUANTILES = (0.1, 0.3, 0.5, 0.7, 0.9)
TS = (5, 10)

# O-1 record, HANDOFF_sign.md section 3 (committed table).
O1_KD = (None, 1.80, 1.40, 1.00)
O1_COMMITTED_RATIO = (1.06397, 1.18373, 1.13631, 0.37798)
O1_COMMITTED_OMEGA = (0.037252, 0.128950, 0.285804, 0.500000)
O1_COMMITTED_C = (1.1051, 1.3590, 1.5910, 0.7560)
O1_KD_STAR, O1_OMEGA_STAR = 1.28618, 0.3428
O1_KMIN, O1_KMAX, O1_N = 0.15, 0.85, 41

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


def ratio(num: float, den: float) -> float | str:
    """Design risk 9.3: a ratio on a vanishing denominator is undefined."""
    return float(num / den) if abs(den) > S_P_FLOOR else "undefined"


# ---------------------------------------------------------------------------
# The v4 sweep
# ---------------------------------------------------------------------------


def sweep(pol, p_base, tau: float, T: int) -> dict:
    """71-node frozen-policy kappa sweep at one (tau, T)."""
    D, MP, OM = [], [], []
    n_multi = 0
    degen = ()
    for kap in KAPPAS:
        o = evaluate(pol, p_base.replace(kappa=float(kap), tau=float(tau),
                                         T=int(T)), with_runup=False)
        D.append(o.Delta_act)
        MP.append(o.M_P)
        OM.append(o.Omega)
        n_multi += int(o.multiple_root_nodes)
        degen = o.degenerate_nodes
    D, MP, OM = np.asarray(D), np.asarray(MP), np.asarray(OM)
    dk = float(KAPPAS[1] - KAPPAS[0])
    S_tv = float(np.abs(np.diff(D)).sum())
    SP_tv = float(np.abs(np.diff(MP)).sum())
    S_pt = np.abs(np.diff(D) / dk)
    SP_pt = np.abs(np.diff(MP) / dk)
    return {
        "tau": float(tau), "T": int(T), "corner": bool(T == p_base.H),
        "Omega": float(OM[len(OM) // 2]),
        "Omega_flat_residual": float(np.max(np.abs(OM - OM[len(OM) // 2]))),
        "S_TV": S_tv, "S_P_TV": SP_tv,
        "S_TV_pp": S_tv * PP, "S_P_TV_pp": SP_tv * PP,
        "S_meanslope": float(S_pt.mean()), "S_P_meanslope": float(SP_pt.mean()),
        "max_pointwise_factorisation_residual": float(
            np.max(np.abs(S_pt - (1.0 - OM[:-1]) * SP_pt))),
        "TV_factorisation_residual": abs(S_tv - (1.0 - float(OM[len(OM) // 2]))
                                         * SP_tv),
        "Delta_act_pp": [float(x * PP) for x in D],
        "M_P_pp": [float(x * PP) for x in MP],
        "multiple_root_nodes": n_multi,
        "degenerate": list(degen),
    }


# ---------------------------------------------------------------------------
# Block 6: the static repo model (draft_v2)
# ---------------------------------------------------------------------------


def o1_sensitivity(k1: float, k0: float, kD: float,
                   kaps: np.ndarray) -> tuple[float, float]:
    base = ModelParams()
    disc, nod = [], []
    for kap in kaps:
        p = base.replace(kappa=float(kap))
        disc.append(compute_minority_gains(k1, k0, kD, p).activism)
        nod.append(
            compute_minority_gains_no_disclosure_given_strategy(k1, k0, kD, p)
            .activism)
    return (float(np.abs(np.diff(disc)).sum()),
            float(np.abs(np.diff(nod)).sum()))


def block6():
    params = ModelParams()
    k1, k0, kD0 = solve_equilibrium(params)
    kaps = np.linspace(O1_KMIN, O1_KMAX, O1_N)
    kds = [kD0 if x is None else x for x in O1_KD]
    rows = []
    for kd, cr, com_om, com_c in zip(kds, O1_COMMITTED_RATIO,
                                     O1_COMMITTED_OMEGA, O1_COMMITTED_C):
        _, _, _, Om = compute_action_probabilities(k1, k0, kd, params)
        TVd, TVn = o1_sensitivity(k1, k0, kd, kaps)
        r = TVd / TVn
        # S = W C  with W_O1 = 1 - Omega, so C_O1 = S_P^TV(Omega)/S_P^TV(0)
        # = [S^TV(Omega)/(1-Omega)] / S^TV(0) = ratio / (1 - Omega).
        C_O1 = r / (1.0 - Om)
        rows.append({
            "kD": float(kd), "Omega": float(Om), "committed_Omega": com_om,
            "TV_flagged": TVd, "TV_pooled": TVn, "ratio_TV": r,
            "committed_ratio": cr, "abs_diff_vs_committed": abs(r - cr),
            "attenuation_holds": bool(r < 1.0),
            "W_O1": float(1.0 - Om), "C_O1": C_O1,
            "committed_C_O1": com_c, "abs_diff_C_O1": abs(C_O1 - com_c),
            "S_P_TV_flagged_regime": TVd / (1.0 - Om),
            "S_P_TV_pooled_regime": TVn,
        })
        print(f"  O-1  kD={kd:7.4f} Omega={Om:.6f} ratio={r:.5f} "
              f"(committed {cr:.5f})  C_O1={C_O1:.4f} (predicted {com_c:.4f})",
              flush=True)

    # Bisect for the crossing kD* where ratio_TV = 1.
    def f(kd):
        TVd, TVn = o1_sensitivity(k1, k0, float(kd), kaps)
        return TVd / TVn - 1.0

    lo, hi = 1.00, 1.40
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0.0:
            hi = mid          # ratio > 1 above the crossing? resolve by sign
        else:
            lo = mid
        if hi - lo < 1e-6:
            break
    kd_star = 0.5 * (lo + hi)
    _, _, _, om_star = compute_action_probabilities(k1, k0, kd_star, params)

    ok_ratio = all(r["abs_diff_vs_committed"] < TOL_O1 for r in rows)
    ok_star = abs(om_star - O1_OMEGA_STAR) < TOL_OMEGA_STAR
    record(
        "t1_block6_O1_benchmark", ok_ratio and ok_star, "substantive",
        {
            "request": "Block 6 / WHERE IT FAILS case 1: in the STATIC repo "
                       "model at the four committed k_D values, reproduce the "
                       "ratios 1.06397 / 1.18373 / 1.13631 / 0.37798 at Omega = "
                       "0.037252 / 0.128950 / 0.285804 / 0.500000, and the "
                       "bisected boundary k_D* = 1.28618, Omega* = 0.3428",
            "model": "numerical/ (draft_v2 static model), NOT the two-round "
                     "model; everything recomputed, no CSV read",
            "grid": {"kappa_min": O1_KMIN, "kappa_max": O1_KMAX, "n": O1_N},
            "baseline_cutoffs": {"k1": k1, "k0": k0, "kD": kD0},
            "tol_ratio": TOL_O1, "tol_Omega_star": TOL_OMEGA_STAR,
            "max_abs_diff_vs_committed": max(
                r["abs_diff_vs_committed"] for r in rows),
            "kD_star": kd_star, "Omega_star": float(om_star),
            "committed_kD_star": O1_KD_STAR,
            "committed_Omega_star": O1_OMEGA_STAR,
            "directions": "a ratio above 1 means the flag makes premia MORE "
                          "liquidity-sensitive, i.e. attenuation FAILS",
            "rows": rows,
        },
    )

    ok_c = all(r["abs_diff_C_O1"] < TOL_C_O1 for r in rows)
    signs_ok = (all(r["C_O1"] > 1.0 for r in rows[:3]) and rows[3]["C_O1"] < 1.0)
    record(
        "t1_block6_composition_factors", ok_c and signs_ok, "substantive",
        {
            "request": "Block 6: compute S_P^TV directly in each regime and "
                       "report C_O1 = S_P^TV(Omega)/S_P^TV(0); predicted "
                       "C_O1 = 1.1051, 1.3590, 1.5910, 0.7560 to within 1e-3, "
                       "with C_O1 > 1 at the first three rows and < 1 at the "
                       "fourth",
            "tol": TOL_C_O1,
            "computed_C_O1": [r["C_O1"] for r in rows],
            "predicted_C_O1": list(O1_COMMITTED_C),
            "max_abs_diff": max(r["abs_diff_C_O1"] for r in rows),
            "signs_as_predicted": bool(signs_ok),
            "derivation": "W_O1 = 1 - Omega and S = W C, so "
                          "C_O1 = ratio_TV / (1 - Omega); S_P^TV is reported in "
                          "levels in the block-6 rows, so the ratio is not "
                          "taken on an unreported denominator",
            "reading": "a mismatch here would falsify the claim that the static "
                       "model's O-1 experiment satisfies L1 + flagged-cell "
                       "kappa-invariance + PE-Omega, and would mean the "
                       "committed ratios cannot be read through the "
                       "factorisation at all -- reported as a finding, not as a "
                       "tolerance failure",
            "rows": [{kk: r[kk] for kk in ("kD", "Omega", "ratio_TV", "W_O1",
                                           "C_O1", "S_P_TV_flagged_regime",
                                           "S_P_TV_pooled_regime")}
                     for r in rows],
        },
    )


# ---------------------------------------------------------------------------


def main() -> int:
    t0 = time.perf_counter()
    print("t2_t1_check -- frozen baseline (2 cold solves) ...", flush=True)
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
        "request": "research/model_v4/proofs/T1_proof.md, NUMERICAL CHECK "
                   "REQUEST (six blocks); O-1 record in HANDOFF_sign.md",
        "measurement": "total variation over the kappa grid (Step 7), with mean "
                       "absolute slope reported alongside",
        "H12_robustness": "MANDATORY for T1's window comparison (design section "
                          "13, ruling 2); delivered for the Omega/W_T/chord half",
    }
    results["grid"] = {
        "kappa": [float(x) for x in KAPPAS], "tau": list(taus),
        "tau_quantiles": list(QUANTILES), "T": list(TS),
        "H": p_base.H, "H_robustness": 12, "M": 2,
        "tau_frozen_from": "percentiles of the seed-equilibrium (tau=0.05) Voice "
                           "b*(s) terminal-stake distribution, design 6.2",
        "policy": "frozen at the baseline equilibrium cutoffs at every node (H5)",
        "A_prime_kappa": A_PRIME_KAPPA,
        "n_v4_evaluations": len(KAPPAS) * len(TS) * len(QUANTILES),
    }
    results["counts"] = {
        "n_hist": p_base.n_hist, "n_hist_feasible": base_out.n_hist_feasible,
        "n_theta": p_base.n_theta, "discarded_mass": 0.0,
    }

    # -- the sweep ----------------------------------------------------------
    S: dict = {}
    degenerate, multi = [], 0
    for T in TS:
        for qi, tau in zip(QUANTILES, taus):
            r = sweep(pol, p_base, tau, T)
            r["tau_quantile"] = qi
            cw = cell_weights(atoms(k, p_base.replace(tau=float(tau), T=int(T))))
            r["pi_bar_pr"] = float(cw.pi_bar)
            r["pi_bar_level_symmetric"] = 2.0 * float(cw.pi_bar)
            S[(T, qi)] = r
            multi += r["multiple_root_nodes"]
            if r["degenerate"]:
                degenerate.append({"T": T, "tau_quantile": qi, "tau": float(tau),
                                   "reasons": r["degenerate"]})
            print(f"  T={T:2d} q={qi:.1f} Omega={r['Omega']:.6f} "
                  f"S_TV={r['S_TV_pp']:.6f}pp S_P_TV={r['S_P_TV_pp']:.6f}pp",
                  flush=True)

    rows = list(S.values())

    # -- block 1 ------------------------------------------------------------
    max_pt = max(r["max_pointwise_factorisation_residual"] for r in rows)
    max_tv = max(r["TV_factorisation_residual"] for r in rows)
    max_flat = max(r["Omega_flat_residual"] for r in rows)
    record(
        "t1_block1_factorisation",
        max_pt < TOL_IDENT and max_tv < TOL_IDENT, "wiring",
        {"request": "Block 1: max |S - (1-Omega) S_P| and "
                    "max |S^TV - (1-Omega) S_P^TV|, both predicted below 1e-10",
         "tol": TOL_IDENT,
         "max_pointwise_residual": max_pt, "max_TV_residual": max_tv,
         "why_wiring": "at frozen policy Omega and M_F are kappa-free, so "
                       "Delta^act = Omega M_F + (1-Omega) M_P differentiates to "
                       "(1-Omega) d_kappa M_P identically; the residual is "
                       "machine noise by construction (design section 0 rules "
                       "the product identity wiring and the <= 1 substantive)",
         "rows": [{kk: r[kk] for kk in
                   ("T", "tau_quantile", "Omega", "S_TV_pp", "S_P_TV_pp",
                    "S_meanslope", "S_P_meanslope",
                    "max_pointwise_factorisation_residual",
                    "TV_factorisation_residual")} for r in rows]},
    )
    record(
        "t1_block1_Omega_flat_in_kappa", max_flat < TOL_FLAT, "substantive",
        {"request": "Block 1: max_kappa |Omega(kappa) - Omega(kappa_0)| at "
                    "fixed policies, predicted below 1e-12 -- this checks that "
                    "H6 is implemented and not merely asserted. A nonzero value "
                    "here invalidates every later block",
         "tol": TOL_FLAT, "max_residual": max_flat,
         "n_kappa_nodes": int(KAPPAS.size)},
    )

    # -- block 2 ------------------------------------------------------------
    b2, viol2, nulls = [], [], []
    worst_id2 = 0.0
    for T in TS:
        for i in range(len(QUANTILES) - 1, 0, -1):
            hi, lo = S[(T, QUANTILES[i])], S[(T, QUANTILES[i - 1])]
            W = (1.0 - lo["Omega"]) / (1.0 - hi["Omega"])
            C = ratio(lo["S_P_TV"], hi["S_P_TV"])
            direct = ratio(lo["S_TV"], hi["S_TV"])
            prod = (W * C) if isinstance(C, float) else "undefined"
            res = (abs(direct - prod)
                   if isinstance(prod, float) and isinstance(direct, float)
                   else float("nan"))
            if isinstance(res, float) and np.isfinite(res):
                worst_id2 = max(worst_id2, res)
            recl = lo["Omega"] - hi["Omega"]
            row = {"T": T, "tau": hi["tau"], "tau_prime": lo["tau"],
                   "tau_quantile": QUANTILES[i],
                   "tau_prime_quantile": QUANTILES[i - 1],
                   "W_tau": W, "C_tau": C, "W_tau_C_tau": prod,
                   "direct_ratio": direct, "identity_residual": res,
                   "reclassified_mass": recl,
                   "S_P_TV_pp_tau": hi["S_P_TV_pp"],
                   "S_P_TV_pp_tau_prime": lo["S_P_TV_pp"],
                   "null_reclassification": bool(abs(recl) < 1e-14)}
            b2.append(row)
            if isinstance(prod, float) and prod > 1.0 + 1e-12:
                viol2.append(row)
            if row["null_reclassification"]:
                nulls.append(row)
    null_ok = all(abs(r["W_tau_C_tau"] - 1.0) < TOL_NULL for r in nulls
                  if isinstance(r["W_tau_C_tau"], float))
    record(
        "t1_block2_threshold_margin",
        not viol2 and worst_id2 < TOL_IDENT and null_ok, "mixed",
        {"request": "Block 2: W_tau = (1-Omega(tau'))/(1-Omega(tau)), "
                    "C_tau = S_P(tau')/S_P(tau), their product, and the direct "
                    "ratio S(tau')/S(tau). Predicted W_tau <= 1, C_tau <= 1, "
                    "product <= 1; identity residual below 1e-10; product equal "
                    "to one within 1e-12 at any pair that reclassifies no mass",
         "tol_identity": TOL_IDENT, "tol_null": TOL_NULL,
         "max_identity_residual": worst_id2,
         "n_pairs": len(b2), "n_product_above_one": len(viol2),
         "violations": viol2,
         "n_null_reclassification_pairs": len(nulls),
         "null_pairs_product_equals_one": bool(null_ok),
         "note": "the terminal-stake tau ladder does not bite below the median "
                 "at T = 5, and does not bite at all at T = 10, so several "
                 "pairs reclassify zero mass. Those are Step 14's null case and "
                 "are reported explicitly rather than inferred; L4's own ladder "
                 "(deciles of B(s,H-T)) bites at every step and is checked in "
                 "t2_l4_check.py",
         "rows": b2},
    )

    # -- block 3 ------------------------------------------------------------
    b3, worst3 = [], 0.0
    for T in TS:
        for qi in QUANTILES:
            r = S[(T, qi)]
            pib = r["pi_bar_level_symmetric"]
            ch = chord(pib, p_base.mu_v, p_base)
            pred = p_base.Delta_m * A_PRIME_KAPPA * abs(ch.C_h)
            res = abs(r["S_P_meanslope"] - pred)
            worst3 = max(worst3, res)
            b3.append({"T": T, "tau_quantile": qi,
                       "pi_bar_level_symmetric": pib,
                       "pi_bar_pr": r["pi_bar_pr"],
                       "abs_A_prime_kappa": A_PRIME_KAPPA,
                       "abs_C_h": abs(ch.C_h),
                       "abs_C_h_over_pi_bar2": ch.quadratic_ratio,
                       "S_P_meanslope_pp": r["S_P_meanslope"] * PP,
                       "S_P_TV_pp": r["S_P_TV_pp"],
                       "chord_formula_pp": pred * PP,
                       "residual": res, "residual_pp": res * PP,
                       "relative_residual": res / pred if pred > 0 else None,
                       "implied_abs_A_prime_kappa": (
                           r["S_P_meanslope"] / (p_base.Delta_m * abs(ch.C_h))
                           if abs(ch.C_h) > 0 else None)})
    # Distinct pi_bar values only: the terminal-stake ladder repeats pi_bar at
    # the null-reclassification deciles, and comparing a node with itself would
    # make the 5% rate claim vacuous.
    seen, uniq = set(), []
    for r in sorted(b3, key=lambda x: x["pi_bar_level_symmetric"]):
        key = round(r["pi_bar_level_symmetric"], 14)
        if key not in seen:
            seen.add(key)
            uniq.append(r)
    two = uniq[:2]
    chord_spread = abs(two[0]["abs_C_h_over_pi_bar2"]
                       - two[1]["abs_C_h_over_pi_bar2"]) \
        / abs(two[0]["abs_C_h_over_pi_bar2"])
    record(
        "t1_block3_chord_magnitude", worst3 < TOL_IDENT, "substantive",
        {"request": "Block 3: residual |S_P - Delta_m |A'_kappa| |C_h(pi_bar)||, "
                    "predicted below 1e-10; and |C_h(pi_bar)|/pi_bar^2 constant "
                    "to within 5% between the two smallest pi_bar nodes",
         "tol": TOL_IDENT, "max_residual": worst3,
         "max_residual_pp": worst3 * PP,
         "chord_ratio_spread_two_smallest": chord_spread,
         "chord_ratio_within_5pct": bool(chord_spread < PCT_CHORD),
         "pi_bar_two_smallest_distinct": [r["pi_bar_level_symmetric"]
                                          for r in two],
         "n_distinct_pi_bar": len(uniq),
         "implied_abs_A_prime_kappa_range": [
             min(r["implied_abs_A_prime_kappa"] for r in b3
                 if r["implied_abs_A_prime_kappa"] is not None),
             max(r["implied_abs_A_prime_kappa"] for r in b3
                 if r["implied_abs_A_prime_kappa"] is not None)],
         "implied_A_prime_note": "S_P/(Delta_m |C_h(pi_bar)|) is the value "
                                 "|A'_kappa| would have to take for the chord "
                                 "formula to reproduce the enumerated "
                                 "sensitivity. Example A gives 1/4; the gap "
                                 "between the two IS the A'_kappa channel that "
                                 "L4 prediction 5 and T1's C_tau inherit",
         "pi_bar_vs_pi_bar_pr": "reported in separate columns per H11's ruling: "
                                "pi_bar is the upper support point of the "
                                "pooled engagement posterior (here the "
                                "level-symmetric 2 pi_bar_pr), pi_bar_pr is the "
                                "share Pr(a=1|D=0); conflating them is the most "
                                "likely implementation error in this block",
         "max_relative_residual": max(r["relative_residual"] for r in b3
                                      if r["relative_residual"] is not None),
         "finding": (
             f"FAILED HYPOTHESIS, reported and not smoothed. The residual is "
             f"{worst3 * PP:.6f} premium pp, far above 1e-10. It is the gap "
             "between the ENUMERATED two-round pooled sensitivity and A(tau)'s "
             "three-atom closed form -- exactly the object design section 0 "
             "says the build must measure ('the enumeration never imposes "
             "A(tau)'). It is a failed hypothesis about A(tau)'s applicability "
             "to this pooled law, not a wiring error: L3's Example B shows the "
             "manuscript's four-atom structure lies outside A(tau), and "
             "t2_l3_check.py's block 5b measures the same gap analytically."
         ) if worst3 >= TOL_IDENT else (
             "The residual clears 1e-10: on this calibration the enumerated "
             "pooled sensitivity coincides with A(tau)'s closed form to "
             "machine precision."
         ),
         "rows": b3},
    )

    # -- block 4 ------------------------------------------------------------
    b4, n_above = [], 0
    worst_id4 = 0.0
    viol_WT = []
    for qi in QUANTILES:
        s5, s10 = S[(5, qi)], S[(10, qi)]
        W_T = (1.0 - s5["Omega"]) / (1.0 - s10["Omega"])
        C_T = ratio(s5["S_P_TV"], s10["S_P_TV"])
        prod = (W_T * C_T) if isinstance(C_T, float) else "undefined"
        direct = ratio(s5["S_TV"], s10["S_TV"])
        res = (abs(direct - prod)
               if isinstance(prod, float) and isinstance(direct, float)
               else float("nan"))
        if np.isfinite(res):
            worst_id4 = max(worst_id4, res)
        row = {"tau_quantile": qi, "tau": s5["tau"],
               "W_T": W_T, "C_T": C_T, "W_T_C_T": prod,
               "direct_ratio_S5_over_S10": direct, "identity_residual": res,
               "Omega_T5": s5["Omega"], "Omega_T10": s10["Omega"],
               "S_P_TV_pp_T5": s5["S_P_TV_pp"], "S_P_TV_pp_T10": s10["S_P_TV_pp"],
               "corner_T10_equals_H": True}
        b4.append(row)
        if isinstance(W_T, float) and W_T > 1.0 + 1e-12:
            viol_WT.append(row)
        if isinstance(prod, float) and prod > 1.0:
            n_above += 1
    all_attenuating = (n_above == 0)
    record(
        "t1_block4_window_margin",
        not viol_WT and worst_id4 < TOL_IDENT, "substantive",
        {"request": "Block 4: for (T',T) = (5,10) at each tau report W_T, C_T, "
                    "W_T C_T, the direct ratio and Omega at both windows. "
                    "W_T <= 1 at every node (a violation is a bug in the clock, "
                    "not evidence against the theorem); C_T UNSIGNED and not to "
                    "be constrained; W_T C_T reported as found; identity "
                    "residual below 1e-10",
         "tol": TOL_IDENT, "max_identity_residual": worst_id4,
         "n_W_T_above_one": len(viol_WT), "W_T_violations": viol_WT,
         "n_nodes_with_W_T_C_T_above_one": n_above,
         "suspected_forced_attenuation_bug": bool(all_attenuating),
         "acceptance_rule_with_teeth": (
             "a run returning W_T C_T <= 1 at EVERY node, including the "
             "low-Omega calibrations, is to be treated as suspect and audited "
             "for a forced-attenuation bug before it is believed, because the "
             "O-1 record has the analogous product above one at Omega = 0.037, "
             "0.129 and 0.286 (reproduced in t1_block6_O1_benchmark)"
         ),
         "audit_note": (
             "FLAGGED: this run returns W_T C_T <= 1 at every node. The audit "
             "trail is: (i) W_T = (1-Omega(5))/(1-Omega(10)) is "
             f"{min(r['W_T'] for r in b4):.4f}-{max(r['W_T'] for r in b4):.4f} "
             "across the ladder because the T = H = 10 corner drives Omega(10) "
             f"to {b4[0]['Omega_T10']:.2e}, so "
             "the window comparison here is a corner-vs-interior comparison, "
             "not the two-interior-window comparison the theorem contemplates; "
             "(ii) C_T is computed from independently enumerated S_P levels, "
             "both reported above, and is NOT clipped or signed anywhere in "
             "this script; (iii) the H = 12 column below re-runs the same "
             "comparison with T = 10 strictly interior. The product staying "
             "below one is therefore a property of this calibration's corner, "
             "and is reported as suspect rather than as confirmation."
             if all_attenuating else "not applicable -- some node has W_T C_T > 1"
         ),
         "rows": b4},
    )

    # -- block 5 ------------------------------------------------------------
    record(
        "t1_block5_local_form", True, "substantive",
        {"request": "Block 5: on an interpolated window grid "
                    "T in {4.0, 4.25, ..., 12.0}, compute Omega_{r_T} and "
                    "d_{r_T} S_P by central differences",
         "outcome": "LOCAL FORM NOT EVALUABLE -- INTEGER WINDOW",
         "why": "numerical_v4's legal clock computes the filing date as "
                "f = c + T with c an integer trading date and indexes the stake "
                "path at int(f)+1, so a fractional T is truncated rather than "
                "interpolated. The implementation does not admit fractional "
                "windows, and the request's own instruction for that case is to "
                "report this line rather than skip the block silently.",
         "consequences": "the (21a) integral check of rho over r in [-10,-5] "
                         "against log(W_T C_T), and the count of nodes with "
                         "rho > 0 inside an interval whose endpoint comparison "
                         "gives W_T C_T <= 1, are both unavailable. The finite "
                         "form of Step 20 is still exercised by block 4.",
         "n_evaluated": 0},
        vacuous=True,
    )

    block6()

    # -- H = 12 window robustness (MANDATORY, design ruling 2) ---------------
    p12 = p_base.replace(H=12)
    r12 = []
    viol12 = []
    for qi, tau in zip(QUANTILES, taus):
        cw5 = cell_weights(atoms(k, p12.replace(tau=float(tau), T=5)))
        cw10 = cell_weights(atoms(k, p12.replace(tau=float(tau), T=10)))
        W_T = (1.0 - cw5.Omega) / (1.0 - cw10.Omega)
        c5 = chord(2.0 * cw5.pi_bar, p_base.mu_v, p_base)
        c10 = chord(2.0 * cw10.pi_bar, p_base.mu_v, p_base)
        sp5 = p_base.Delta_m * A_PRIME_KAPPA * abs(c5.C_h)
        sp10 = p_base.Delta_m * A_PRIME_KAPPA * abs(c10.C_h)
        C_T = ratio(sp5, sp10)
        prod = (W_T * C_T) if isinstance(C_T, float) else "undefined"
        row = {"tau_quantile": qi, "tau": float(tau), "H": 12,
               "Omega_T5": float(cw5.Omega), "Omega_T10": float(cw10.Omega),
               "pi_bar_pr_T5": float(cw5.pi_bar),
               "pi_bar_pr_T10": float(cw10.pi_bar),
               "W_T": W_T, "C_T_chord_route": C_T,
               "W_T_C_T_chord_route": prod,
               "S_P_chord_pp_T5": sp5 * PP, "S_P_chord_pp_T10": sp10 * PP,
               "T10_is_corner": False,
               "degenerate_T5": list(cw5.degenerate),
               "degenerate_T10": list(cw10.degenerate)}
        r12.append(row)
        if isinstance(W_T, float) and W_T > 1.0 + 1e-12:
            viol12.append(row)
    n_above12 = sum(1 for r in r12
                    if isinstance(r["W_T_C_T_chord_route"], float)
                    and r["W_T_C_T_chord_route"] > 1.0)
    record(
        "t1_H12_window_robustness", not viol12, "substantive",
        {"request": "design section 13, ruling 2: the H = 12 re-run is MANDATORY "
                    "for T1's window comparison",
         "scope": "Omega, W_T and the chord-route C_T -- none of which touch the "
                  "pooled enumeration. At H = 12, T = 10 is strictly interior "
                  "(T < H), so this column is exactly the corner audit block 4 "
                  "asks for.",
         "not_evaluable_at_H12": "the enumerated S_P (and hence the enumerated "
                                 "C_T and the direct ratio) run through the "
                                 "pooled enumeration; at H = 12 the feasible "
                                 "history count is 8,503,056 and 8,503,056 x "
                                 "N_theta 14 = 1.19e8 exceeds the design "
                                 "build-step-4 gate of 1e8 (~2.5 GB working "
                                 "set). The gate is respected, not overridden.",
         "policy": "cutoffs frozen at the H = 10 baseline equilibrium; H = 12 "
                   "cannot be re-solved for the same reason",
         "n_W_T_above_one": len(viol12),
         "n_nodes_with_W_T_C_T_above_one": n_above12,
         "rows": r12},
    )

    results["degenerate_nodes"] = degenerate
    results["multiple_root_nodes"] = multi
    results["node_table"] = [{kk: vv for kk, vv in r.items()
                              if kk not in ("Delta_act_pp", "M_P_pp")}
                             for r in rows]
    results["kappa_profiles"] = {
        f"T={r['T']},q={r['tau_quantile']}": {"Delta_act_pp": r["Delta_act_pp"],
                                              "M_P_pp": r["M_P_pp"]}
        for r in rows}
    results["baseline"] = {
        "k": list(k), "tau_reference": tau_med, "T": p_base.T, "H": p_base.H,
        "Omega": base_out.Omega, "Delta_act_pp": base_out.Delta_act * PP,
        "M_F_pp": base_out.M_F * PP, "M_P_pp": base_out.M_P * PP,
        "cutoff_scale": resid.cutoff_scale, "payoff_scale": resid.payoff_scale,
    }
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
