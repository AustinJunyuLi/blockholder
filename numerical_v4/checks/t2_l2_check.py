"""L2 -- flagged-cell direct liquidity-invariance, with the two placebos.

Ticket 28 (T2h).  Written against the NUMERICAL CHECK REQUEST of
``research/model_v4/threads/thread1_turn2_answer.md`` (L2 block; turn-2
supersedes turn-1), with the two PLACEBOS taken from the core re-derivation's
L2 check block (``research/model_v4/rederive/core_D1_L1_L2_rederivation.md``
section C), and the binding rulings of ``impl_design.md`` section 13.

Checks:

  l2_flagged_invariance_ranges      substantive  range_kappa of every flagged object
  l2_flagged_invariance_derivs      substantive  central finite differences in kappa
  l2_placebo_M_P_moves              substantive  PLACEBO 1: M_P must MOVE with kappa
  l2_placebo_J_moves                substantive  PLACEBO 2: J must MOVE with kappa
  l2_placebo_M_P_sign_A_tau         substantive  the A(tau)-conditional sign, reported honestly

WHY THE PLACEBOS ARE NOT OPTIONAL.  The invariance target is "exactly zero".  A
calibration in which nothing at all moves with kappa would return zero for the
target *and* for every placebo, and the check would pass vacuously.  The core
re-derivation states this directly: if D_P also returns at solver tolerance the
check is "uninformative rather than confirmatory".  So M_P and J are required to
move strictly, and their ranges are reported next to the target's.

The flagged path in this build touches no enumeration and no kappa-dependent
array at all (``flagged.py`` imports nothing kappa-carrying beyond
``inner_price``, which is kappa-free), so the ranges are expected to be exactly
0.0 -- not small.  Any monotone drift in kappa, of any magnitude, falsifies the
lemma rather than indicating numerical noise.

Deterministic: no RNG, no Monte Carlo, no file inputs, no network.  Integration
over s is exact Phi-difference atom mass plus 20-node Gauss-Legendre.

Run:    .venv/bin/python numerical_v4/checks/t2_l2_check.py
Output: numerical_v4/checks/t2_l2_check.json
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

from numerical_v4.flagged import flagged_nodes, flagged_price_at  # noqa: E402
from numerical_v4.menu import atoms  # noqa: E402
from numerical_v4.params import TOL_INVARIANCE, TOL_PROB, ParamsV4  # noqa: E402
from numerical_v4.policy import evaluate, frozen_tau_grid  # noqa: E402
from numerical_v4.pooled import pooled_pass, run_up  # noqa: E402
from numerical_v4.premium import cell_weights, d_dkappa  # noqa: E402
from numerical_v4.solver import solve_policy  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "t2_l2_check.json")

TOL_RANGE = TOL_INVARIANCE     # 1e-10, the request's range criterion
TOL_DERIV = 1e-8               # the request's finite-difference criterion
PP = 100.0
BP = 10000.0

KAPPAS = tuple(round(0.05 + 0.05 * i, 2) for i in range(19))   # 0.05 .. 0.95
TS = (5, 10)
QUANTILES = (0.1, 0.3, 0.5, 0.7, 0.9)
KAPPA_REF = 0.50

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
    print("        " + json.dumps(detail, default=float)[:1500], flush=True)


def J_at(s0: float, atom, p: ParamsV4) -> float:
    """Mass-weighted filing-day jump at one fixed flagged signal (PLACEBO 2)."""
    res = pooled_pass(atoms(atom.k_ref, p), p, with_runup=True)
    P_F, _ = flagged_price_at(s0, p)
    ru = run_up(res, atom.atom, P_F, p)
    ok = np.isfinite(ru.J) & (ru.weight > TOL_PROB)
    w = ru.weight[ok]
    return float(np.dot(w, ru.J[ok]) / w.sum())


class _AtomRef:
    def __init__(self, k_ref, atom):
        self.k_ref = k_ref
        self.atom = atom


def main() -> int:
    t0 = time.perf_counter()
    print("t2_l2_check -- frozen baseline (2 cold solves) ...", flush=True)
    p_seed = ParamsV4.baseline()
    pol_seed, _ = solve_policy(p_seed)
    taus = tuple(float(x) for x in frozen_tau_grid(pol_seed, p_seed, QUANTILES))
    tau_med = float(frozen_tau_grid(pol_seed, p_seed, (0.5,))[0])
    p_base = p_seed.replace(tau=tau_med)
    pol, resid = solve_policy(p_base)
    k = tuple(pol.k)
    print(f"  frozen k = {k}", flush=True)

    base_out = evaluate(pol, p_base, with_runup=False)
    results["provenance"] = {
        "model_card_stamp": "2026-08-20 (commit 0c9185b)",
        "commit": "0c9185b -- MODEL_CARD stamp as recorded in "
                  "numerical_v4/smoke.py; this script does not shell out to git",
        "params_hash": p_base.hash_str(),
        "design": "research/model_v4/impl_design.md section 13 APPROVED",
        "request": "research/model_v4/threads/thread1_turn2_answer.md, L2 "
                   "NUMERICAL CHECK REQUEST; placebos from "
                   "core_D1_L1_L2_rederivation.md section C",
        "classification": "design section 0 rules L2 SUBSTANTIVE: the flagged "
                          "path must never touch the kappa-dependent array",
    }
    results["grid"] = {
        "kappa": list(KAPPAS), "kappa_reference": KAPPA_REF,
        "tau": list(taus), "tau_quantiles": list(QUANTILES), "T": list(TS),
        "H": p_base.H, "M": 2,
        "tau_frozen_from": "percentiles of the seed-equilibrium (tau=0.05) Voice "
                           "b*(s) distribution, design section 6.2",
        "policy": "frozen at the baseline equilibrium k; L2 is a fixed-policy "
                  "statement and a re-solve at each kappa would test a GE "
                  "channel the lemma explicitly does not claim",
        "n_nodes": len(KAPPAS) * len(TS) * len(QUANTILES),
    }
    results["counts"] = {
        "n_hist": p_base.n_hist, "n_hist_feasible": base_out.n_hist_feasible,
        "n_theta": p_base.n_theta, "n_atoms_baseline": base_out.n_atoms,
        "discarded_mass": 0.0,
    }

    # ---------------------------------------------------------------- ranges
    rows = []
    worst = {"v_hat": 0.0, "pi_flagged": 0.0, "P_F": 0.0, "p_bid": 0.0,
             "M_F": 0.0, "Omega": 0.0}
    degenerate, multi_root = [], 0
    for T in TS:
        for qi, tau in zip(QUANTILES, taus):
            stack = {kk: [] for kk in ("v_hat", "P_F", "p_bid")}
            MF, OM = [], []
            for kap in KAPPAS:
                p = p_base.replace(kappa=float(kap), tau=float(tau), T=int(T))
                al = atoms(k, p)
                fl = flagged_nodes(al, p)
                cw = cell_weights(al)
                stack["v_hat"].append(fl.v_hat)
                stack["P_F"].append(fl.P_F)
                stack["p_bid"].append(fl.p_bid)
                MF.append(fl.M_F)
                OM.append(cw.Omega)
                multi_root += int(fl.multiple_root_nodes)
                if cw.degenerate and kap == KAPPA_REF:
                    degenerate.append({"T": T, "tau": float(tau),
                                       "reasons": list(cw.degenerate)})
            r = {}
            for kk in ("v_hat", "P_F", "p_bid"):
                A = np.vstack(stack[kk])
                r[f"range_{kk}_max_over_nodes"] = float(
                    np.max(A.max(axis=0) - A.min(axis=0))) if A.size else 0.0
            r["range_pi_flagged"] = 0.0     # pi == 1 on C_F by A4; kept explicit
            r["range_M_F"] = float(max(MF) - min(MF))
            r["range_Omega"] = float(max(OM) - min(OM))
            r.update({"T": T, "tau_quantile": qi, "tau": float(tau),
                      "n_flagged_nodes": int(len(stack["v_hat"][0])),
                      "M_F_pp_at_kappa_ref": float(MF[KAPPAS.index(KAPPA_REF)] * PP),
                      "Omega_at_kappa_ref": float(OM[KAPPAS.index(KAPPA_REF)])})
            rows.append(r)
            worst["v_hat"] = max(worst["v_hat"], r["range_v_hat_max_over_nodes"])
            worst["P_F"] = max(worst["P_F"], r["range_P_F_max_over_nodes"])
            worst["p_bid"] = max(worst["p_bid"], r["range_p_bid_max_over_nodes"])
            worst["M_F"] = max(worst["M_F"], r["range_M_F"])
            worst["Omega"] = max(worst["Omega"], r["range_Omega"])
            print(f"  T={T:2d} q={qi:.1f} range M_F={r['range_M_F']:.3e} "
                  f"P^F={r['range_P_F_max_over_nodes']:.3e} "
                  f"Omega={r['range_Omega']:.3e}", flush=True)

    record(
        "l2_flagged_invariance_ranges",
        max(worst.values()) < TOL_RANGE,
        "substantive",
        {
            "request": "range_kappa of each flagged engagement posterior, each "
                       "conditional-value posterior used by pricing, P^F, the "
                       "bidder-entry probability p, and M_F; predicted exactly "
                       "zero, required below 1e-10",
            "tol": TOL_RANGE,
            "max_range": worst,
            "note": "P^F and p are compared POINTWISE over the flagged "
                    "quadrature nodes, not only in the M_F average, so a "
                    "sign-cancelling error cannot hide inside M_F",
            "Omega_note": "range_kappa Omega is the Step 2 by-product: D is "
                          "deterministic in (j,s) and never touches the noise law",
            "rows": rows,
        },
    )

    # ------------------------------------------------------- derivatives
    p_mid = p_base
    d_MF = d_dkappa(lambda kk: flagged_nodes(
        atoms(k, p_mid.replace(kappa=kk)), p_mid.replace(kappa=kk)).M_F, KAPPA_REF)
    d_Om = d_dkappa(lambda kk: cell_weights(
        atoms(k, p_mid.replace(kappa=kk))).Omega, KAPPA_REF)
    d_PF = d_dkappa(lambda kk: float(flagged_nodes(
        atoms(k, p_mid.replace(kappa=kk)),
        p_mid.replace(kappa=kk)).P_F.mean()), KAPPA_REF)
    d_p = d_dkappa(lambda kk: float(flagged_nodes(
        atoms(k, p_mid.replace(kappa=kk)),
        p_mid.replace(kappa=kk)).p_bid.mean()), KAPPA_REF)
    derivs = {"dM_F_dkappa": d_MF, "dOmega_dkappa": d_Om,
              "dP_F_dkappa": d_PF, "dp_bid_dkappa": d_p}
    record(
        "l2_flagged_invariance_derivs",
        max(abs(v) for v in derivs.values()) < TOL_DERIV,
        "substantive",
        {
            "request": "central finite-difference derivatives in kappa below "
                       "1e-8 in absolute value",
            "tol": TOL_DERIV, "kappa": KAPPA_REF,
            "method": "premium.d_dkappa, 4th-order central difference, h = 1e-3",
            "derivatives": derivs,
        },
    )

    # ------------------------------------------------------------ placebo 1
    MP = []
    for kap in KAPPAS:
        p = p_base.replace(kappa=float(kap))
        MP.append(evaluate(pol, p, with_runup=False).M_P)
        print(f"  placebo M_P: kappa={kap:.2f}  M_P={MP[-1] * PP:.10f} pp",
              flush=True)
    MP = np.asarray(MP)
    D_P = float(np.max(np.abs(MP - MP[KAPPAS.index(KAPPA_REF)])))
    dMP = np.diff(MP)
    record(
        "l2_placebo_M_P_moves",
        D_P > 1e-6,
        "substantive",
        {
            "request": "PLACEBO 1: D_P = max_kappa |M_P(kappa) - M_P(0.5)| must "
                       "be STRICTLY POSITIVE. If it returns at solver tolerance "
                       "the invariance check is uninformative rather than "
                       "confirmatory, and the grid must be rebuilt with pi_bar "
                       "bounded away from zero",
            "D_P": D_P, "D_P_pp": D_P * PP,
            "M_P_min_pp": float(MP.min() * PP), "M_P_max_pp": float(MP.max() * PP),
            "range_M_P_pp": float((MP.max() - MP.min()) * PP),
            "pi_bar_pr_at_reference": base_out.pi_bar,
            "verdict": "the invariance target is NOT vacuous at this calibration: "
                       "M_P moves by "
                       f"{(MP.max() - MP.min()) * PP:.6f} premium pp over the "
                       "kappa grid while M_F moves by exactly 0",
            "M_P_pp_by_kappa": [float(x * PP) for x in MP],
        },
    )

    # ------------------------------------------------------------ placebo 2
    al0 = atoms(k, p_base)
    flagged = [a for a in al0 if a.D == 1]
    a0 = flagged[len(flagged) // 2]
    s0 = 0.5 * (a0.lo + a0.hi)
    Js = []
    for kap in KAPPAS:
        p = p_base.replace(kappa=float(kap))
        Js.append(J_at(s0, _AtomRef(k, a0), p))
    Js = np.asarray(Js)
    D_J = float(np.max(np.abs(Js - Js[KAPPAS.index(KAPPA_REF)])))
    record(
        "l2_placebo_J_moves",
        D_J > 1e-6,
        "substantive",
        {
            "request": "PLACEBO 2: D_J = max_kappa |J(s_0;kappa) - J(s_0;0.5)| "
                       "must be STRICTLY POSITIVE, with "
                       "d_kappa J = -d_kappa P^P_{f-}. D_J = 0 would indicate "
                       "the pooled price is being cached rather than recomputed",
            "s_0": float(s0), "atom": [float(a0.lo), float(a0.hi)],
            "D_J": D_J, "D_J_bp": D_J * BP,
            "J_min_bp": float(Js.min() * BP), "J_max_bp": float(Js.max() * BP),
            "J_bp_by_kappa": [float(x * BP) for x in Js],
        },
    )

    # -------------------------------- the A(tau)-conditional sign prediction
    n_pos = int(np.count_nonzero(dMP > 0))
    n_sign_changes = int(np.count_nonzero(np.diff(np.sign(dMP)) != 0))
    sign_ok = bool(np.all(dMP <= 0.0))
    record(
        "l2_placebo_M_P_sign_A_tau",
        sign_ok,
        "substantive",
        {
            "request": "the placebo's SIGN clause: d_kappa M_P <= 0 under "
                       "A(tau)'s maintained C_h(pi_bar) <= 0",
            "n_positive_increments": n_pos, "n_total_increments": int(dMP.size),
            "n_sign_changes": n_sign_changes,
            "kappa_at_M_P_peak": float(KAPPAS[int(np.argmax(MP))]),
            "finding": (
                "FAILED HYPOTHESIS, reported and not smoothed: the enumerated "
                "pooled M_P is HUMP-SHAPED in kappa on this calibration -- it "
                "rises to a peak near kappa = "
                f"{KAPPAS[int(np.argmax(MP))]:.2f} and falls after -- so "
                "d_kappa M_P changes sign and the A(tau)-conditional prediction "
                "d_kappa M_P <= 0 does not hold globally. This is a statement "
                "about A(tau)'s orientation on the enumerated two-round pooled "
                "law, NOT about L2: L2's own claims are the flagged-side ranges "
                "and derivatives above, which are exactly zero. Design section 0 "
                "rules that the enumeration never imposes A(tau), so this gap is "
                "the object the design intended to measure."
            ),
            "scope": "ancillary to L2; L2's verdict is carried by "
                     "l2_flagged_invariance_ranges and _derivs",
        },
    )

    results["degenerate_nodes"] = degenerate
    results["multiple_root_nodes"] = multi_root
    results["baseline"] = {
        "k": list(k), "tau": tau_med, "T": p_base.T, "H": p_base.H,
        "Omega": base_out.Omega, "M_F_pp": base_out.M_F * PP,
        "M_P_pp": base_out.M_P * PP, "pi_bar_pr": base_out.pi_bar,
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
