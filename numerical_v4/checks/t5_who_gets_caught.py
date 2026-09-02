"""Who gets caught: the clock's composition ratio, split by caught type.

Grid verification for the corollary of the clock theorem (ticket 03).  Let A be
the pooled cell at the longer clock T = 10 and B the histories the shorter
clock T' = 5 newly flags.  At fixed policies the cell masses do not depend on
kappa.  With s_A the kappa-sensitivity of E[h^{(T)} | A] and s_B the corollary's
caught leg

    s_B = d_kappa(Lambda_T - Lambda_T') / P(B),

Lambda_T = E[h^{(T)} 1_A], Lambda_T' = E[h^{(T')} 1_{A \\ B}], the cut identity
is s_{A \\ B} = (P(A) s_A - P(B) s_B) / (P(A) - P(B)).  s_B carries the
survivors' re-pricing; it is not tilde s_B = d_kappa E[h^{(T)} | B].  C_T is at
most one iff s_B lies weakly between s_A and ((2 - phi)/phi) s_A,
phi = P(B)/P(A).

METHOD.  The pooled pass keeps only the sum of the per-type masses over the
pooled cell.  This check reconstructs the per-history, per-type mass matrix at
mark = 2 from the likelihood table and the alive MEASURE weights (not the
market weights), prices each clock's pooled cell once per kappa stencil point,
and splits the T = 10 pooled cell by which types the T = 5 clock newly flags:

    A = {types alive at T = 10},   B = {t in A: newly flagged at T = 5},

so P(A) = 1 - Omega(10), P(B) = Omega(5) - Omega(10) and A \\ B is exactly the
T = 5 pooled cell.  s_A is the 4th-order point derivative of E[h | A] under the
T = 10 pricing map.  s_B is the point derivative of (Lambda_T - Lambda_T') /
P(B), with Lambda_T' read at the T = 5 kernel.  C_T is S_P(5)/S_P(10) from each
clock's own pooled pass, the point-derivative convention for S_P (same stencil
as numerical_v4.premium.d_dkappa).

Checks:

  t5_mass_bookkeeping        wiring       P(A), P(B) and E[h|A], E[h|A\\B]
                                          against the independently computed
                                          cell weights and pooled_premium
  t5_identity                wiring       the cut identity and the split
                                          s_B = tilde s_B - ((1-phi)/phi) delta
  t5_biconditional           substantive  C_T <= 1 iff s_B between s_A and
                                          ((2-phi)/phi) s_A
  t5_CT_point_convention     reported     S_P(5)/S_P(10) per node and its <= 1
                                          verdict; the T1 comparison is read
                                          from t2_t1_check.json block 4 by the
                                          orchestrator

Deterministic: no RNG, no Monte Carlo, no file inputs, no network.

Run:    .venv/bin/python numerical_v4/checks/t5_who_gets_caught.py [--nodes n]
Output: numerical_v4/checks/t5_who_gets_caught.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

import numpy as np

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from numerical_v4.menu import atoms                             # noqa: E402
from numerical_v4.params import ParamsV4                        # noqa: E402
from numerical_v4.policy import frozen_tau_grid                 # noqa: E402
from numerical_v4.pooled import (                                # noqa: E402
    _alive_weights,
    _likelihood_lut,
    mark_stats,
    pooled_pass,
)
from numerical_v4.premium import (                               # noqa: E402
    DERIV_STEP,
    cell_weights,
    pooled_premium,
)
from numerical_v4.solver import solve_policy                    # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "t5_who_gets_caught.json")

TOL_MASS = 1e-12            # bookkeeping: cell masses and E[h] vs M_P
TOL_IDENT = 1e-12           # the cut identity, exact by linearity
TOL_SLACK = 1e-12           # slack allowed in an inequality verdict
BOUNDARY = 1e-9             # |C_T - 1| below this is a boundary node
S_P_FLOOR = 1e-14           # a ratio on a vanishing denominator is undefined

QUANTILES = (0.1, 0.3, 0.5, 0.7, 0.9)
T_LONG, T_SHORT = 10, 5

results: dict = {"checks": [], "n_fail": 0}


def record(name: str, ok: bool, kind: str, detail: dict) -> None:
    results["checks"].append(
        {"name": name, "kind": kind, "pass": bool(ok), **detail}
    )
    if not ok:
        results["n_fail"] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} ({kind})", flush=True)
    print("        " + json.dumps(detail, default=float)[:1200], flush=True)


def d_point(vals: np.ndarray, h: float = DERIV_STEP) -> float:
    """4th-order central difference over the 5-point stencil of premium.d_dkappa.

    ``vals`` is ordered [k-2h, k-h, k, k+h, k+2h]; only the four outer points
    enter.
    """
    return float((8.0 * (vals[3] - vals[1]) - (vals[4] - vals[0])) / (12.0 * h))


def kernel_h(res) -> np.ndarray:
    """h = pi p at the control node, 0 on histories the pass left unpriced."""
    d = res.dates[-1]
    piH, pbH = res.pi[d], res.p_bid[d]
    return np.where(np.isfinite(piH), piH * pbH, 0.0)


def integrate_subsets(weights: tuple[np.ndarray, ...], hz: np.ndarray,
                      lut: np.ndarray, n0: np.ndarray,
                      feas: np.ndarray) -> list[float]:
    """Measure integrals of h against each type-weight vector.

    For each type t, E[h | t] is the likelihood-weighted sum of ``hz``.  The
    per-history, per-type mass is W[t] * L[h, t]; the pooled pass keeps only
    the sum over t, so this loop rebuilds that matrix type by type from the
    likelihood table and the alive measure weights.
    """
    n_theta = weights[0].size
    out = [0.0] * len(weights)
    active = np.zeros(n_theta, dtype=bool)
    for W in weights:
        active |= W > 0.0
    for t in np.flatnonzero(active):
        Lt = lut[n0[:, t]] * feas[:, t]
        eh = float(np.dot(Lt, hz))
        for i, W in enumerate(weights):
            wt = float(W[t])
            if wt > 0.0:
                out[i] += wt * eh
        del Lt
    return out


def subset_weights(al10, al5, n_theta: int, H: int):
    """Measure weights on A, on B, and on A \\ B, from the alive type masses.

    ``_alive_weights`` at the control node returns the on-path (measure)
    weights of types whose flag has not landed.  A is alive at T = 10; A \\ B
    is alive at T = 5; B is the difference.
    """
    W_A, _, _, _ = _alive_weights(al10, H, n_theta)
    W_surv, _, _, _ = _alive_weights(al5, H, n_theta)
    W_B = np.maximum(W_A - W_surv, 0.0)
    return W_A, W_B, W_surv


def lies_weakly_between(x: float, a: float, b: float, slack: float) -> bool:
    """True iff x lies weakly between a and b, with relative slack."""
    lo, hi = (a, b) if a <= b else (b, a)
    pad = slack * (abs(a) + abs(b) + abs(x) + 1e-18)
    return bool(lo - pad <= x <= hi + pad)


def node_row(k, p_base, tau: float, qi: float) -> dict:
    """One calibration node: the subsets, the sensitivities, the booleans."""
    p10 = p_base.replace(tau=float(tau), T=T_LONG)
    p5 = p_base.replace(tau=float(tau), T=T_SHORT)
    al10 = atoms(k, p10)
    al5 = atoms(k, p5)
    n_theta = p10.n_theta
    H = p10.H
    ms = mark_stats(H, p10.mark)
    Delta_m = float(p_base.Delta_m)

    W_A, W_B, W_surv = subset_weights(al10, al5, n_theta, H)
    P_A = float(W_A.sum())
    P_B = float(W_B.sum())
    P_surv = float(W_surv.sum())
    # Independent route: the flagged weights read the atoms' own D flags, not
    # the subset weights, so the bookkeeping check below is a real comparison.
    Omega10 = float(cell_weights(al10).Omega)
    Omega5 = float(cell_weights(al5).Omega)
    A_types = [int(t) for t in range(n_theta) if W_A[t] > 0.0]
    B_types = [int(t) for t in range(n_theta) if W_B[t] > 0.0]

    kap0 = p_base.kappa
    h = DERIV_STEP
    stencil = kap0 + h * np.array([-2.0, -1.0, 0.0, 1.0, 2.0])

    Lambda_T_v, Lambda_Tp_v = [], []
    Lambda_B_T_v, Lambda_surv_T_v = [], []
    M_P10_v, M_P5_v = [], []
    res10_M_P = 0.0
    n0_H, feas_H = ms.n0[H], ms.feas[H]
    for kap in stencil:
        lut = _likelihood_lut(H, float(kap))

        p10k = p10.replace(kappa=float(kap))
        res10 = pooled_pass(al10, p10k, with_runup=False)
        hz10 = kernel_h(res10)
        num_A, num_B, num_surv_T = integrate_subsets(
            (W_A, W_B, W_surv), hz10, lut, n0_H, feas_H
        )
        del hz10
        Lambda_T_v.append(num_A)
        Lambda_B_T_v.append(num_B)
        Lambda_surv_T_v.append(num_surv_T)
        M_P10 = float(pooled_premium(res10, Omega10, p10k))
        M_P10_v.append(M_P10)
        if float(kap) == float(kap0):
            res10_M_P = M_P10
        del res10

        p5k = p5.replace(kappa=float(kap))
        res5 = pooled_pass(al5, p5k, with_runup=False)
        hz5 = kernel_h(res5)
        num_surv_Tp, = integrate_subsets(
            (W_surv,), hz5, lut, n0_H, feas_H
        )
        del hz5
        Lambda_Tp_v.append(num_surv_Tp)
        M_P5_v.append(float(pooled_premium(res5, Omega5, p5k)))
        del res5, lut

    Lambda_T_v = np.array(Lambda_T_v)
    Lambda_Tp_v = np.array(Lambda_Tp_v)
    Lambda_B_T_v = np.array(Lambda_B_T_v)
    Lambda_surv_T_v = np.array(Lambda_surv_T_v)
    M_P10_v, M_P5_v = np.array(M_P10_v), np.array(M_P5_v)

    E_A_v = Lambda_T_v / P_A
    E_B_v = Lambda_B_T_v / P_B if P_B > TOL_MASS else np.full(5, np.nan)
    E_surv_T_v = Lambda_surv_T_v / P_surv if P_surv > TOL_MASS else np.full(5, np.nan)
    E_surv_Tp_v = Lambda_Tp_v / P_surv if P_surv > TOL_MASS else np.full(5, np.nan)

    s_A = d_point(E_A_v, h)
    s_B_tilde = d_point(E_B_v, h) if P_B > TOL_MASS else float("nan")
    s_AB_fixed = d_point(E_surv_T_v, h) if P_surv > TOL_MASS else float("nan")
    s_AB_own = d_point(E_surv_Tp_v, h) if P_surv > TOL_MASS else float("nan")
    # Corollary s_B: d_kappa(Lambda_T - Lambda_T') / P(B), survivors re-priced.
    s_B = (d_point(Lambda_T_v - Lambda_Tp_v, h) / P_B
           if P_B > TOL_MASS else float("nan"))
    s_AB_formula = ((P_A * s_A - P_B * s_B) / (P_A - P_B)
                    if P_A > P_B else float("nan"))
    delta = s_AB_own - s_AB_fixed
    phi = P_B / P_A if P_A > 0.0 else float("nan")
    s_B_split = (s_B_tilde - ((1.0 - phi) / phi) * delta
                 if phi > 0.0 else float("nan"))

    s_A_from_MP = d_point(M_P10_v, h) / Delta_m
    s_AB_from_MP = d_point(M_P5_v, h) / Delta_m
    SP10 = abs(d_point(M_P10_v, h))
    SP5_own = abs(d_point(M_P5_v, h))
    C_T_model = (SP5_own / SP10 if SP10 > S_P_FLOOR else "undefined")
    C_T_from_s = (abs(s_AB_own) / abs(s_A)
                  if abs(s_A) > S_P_FLOOR else "undefined")

    defined = isinstance(C_T_model, float) and P_B > TOL_MASS
    upper_b = (2.0 - phi) / phi if phi > 0.0 else float("inf")
    shares_sign = bool(s_A * s_B > 0.0)
    # Corollary part (iv): C_T <= 1 iff s_B lies weakly between s_A and
    # ((2-phi)/phi) s_A.  Mixed signs sit outside that interval.
    condition_holds = bool(
        np.isfinite(s_A) and np.isfinite(s_B) and phi > 0.0
        and lies_weakly_between(s_B, s_A, upper_b * s_A, TOL_SLACK)
    )
    CT_le_1 = (bool(C_T_model <= 1.0 + TOL_SLACK)
               if isinstance(C_T_model, float) else None)
    CT_from_s_le_1 = (bool(C_T_from_s <= 1.0 + TOL_SLACK)
                      if isinstance(C_T_from_s, float) else None)
    boundary = (isinstance(C_T_model, float) and abs(C_T_model - 1.0) < BOUNDARY)

    return {
        "tau_quantile": float(qi), "tau": float(tau),
        "T_long": T_LONG, "T_short": T_SHORT,
        "Omega_T10": Omega10, "Omega_T5": Omega5,
        "P_A": P_A, "P_B": P_B, "P_surv": P_surv, "phi": float(phi),
        "upper_limit_b": float(upper_b),
        "B_types": B_types, "A_types": A_types,
        "A_type_weights": [float(x) for x in W_A],
        "B_type_weights": [float(x) for x in W_B],
        "surv_type_weights": [float(x) for x in W_surv],
        "kappa_point": float(kap0), "deriv_step": float(h),
        "E_A_at_kappa": float(E_A_v[2]),
        "E_B_at_kappa": float(E_B_v[2]),
        "E_AB_T_at_kappa": float(E_surv_T_v[2]),
        "E_AB_Tp_at_kappa": float(E_surv_Tp_v[2]),
        "M_P10_at_kappa": res10_M_P, "M_P5_at_kappa": float(M_P5_v[2]),
        "s_A": float(s_A), "s_B": float(s_B),
        "s_B_tilde": float(s_B_tilde),
        "s_AB_own": float(s_AB_own),
        "s_AB_fixed_map": float(s_AB_fixed),
        "s_AB_formula": float(s_AB_formula),
        "identity_residual": abs(s_AB_own - s_AB_formula),
        "split_residual": abs(s_B - s_B_split),
        "repricing_remainder_delta": float(delta),
        "s_A_vs_MP_residual": abs(s_A - s_A_from_MP),
        "s_AB_vs_MP_residual": abs(s_AB_own - s_AB_from_MP),
        "S_P10_point": float(SP10), "S_P5_point_own": float(SP5_own),
        "C_T": C_T_model, "C_T_from_sensitivities": C_T_from_s,
        "shares_sign": shares_sign,
        "corollary_condition_holds": condition_holds,
        "C_T_le_1": CT_le_1,
        "C_T_from_sensitivities_le_1": CT_from_s_le_1,
        "predicted_C_T_le_1": condition_holds,
        "biconditional_boundary_node": bool(boundary),
        "mass_residual_PA": abs(P_A - (1.0 - Omega10)),
        "mass_residual_PB": abs((P_A - P_B) - (1.0 - Omega5)),
        "mass_residual_PB_omega_gap": abs(P_B - (Omega5 - Omega10)),
        "mass_residual_Psurv": abs(P_surv - (P_A - P_B)),
        "kernel_residual_T10": abs(Delta_m * float(E_A_v[2]) - res10_M_P),
        "kernel_residual_T5": abs(Delta_m * float(E_surv_Tp_v[2])
                                  - float(M_P5_v[2])),
        "_defined": bool(defined),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--nodes", type=int, default=None,
                    help="limit the run to the first n calibration nodes")
    args = ap.parse_args()

    t0 = time.perf_counter()
    p_seed = ParamsV4.baseline()
    assert p_seed.mark == 2, "this check is stated at order size two"
    print(f"t5_who_gets_caught -- mark={p_seed.mark} H={p_seed.H} "
          f"n_hist={p_seed.n_hist:,}; frozen baseline (2 cold solves) ...",
          flush=True)
    pol_seed, _ = solve_policy(p_seed)
    taus = tuple(float(x) for x in frozen_tau_grid(pol_seed, p_seed, QUANTILES))
    tau_med = float(frozen_tau_grid(pol_seed, p_seed, (0.5,))[0])
    p_base = p_seed.replace(tau=tau_med)
    pol, resid = solve_policy(p_base)
    k = tuple(pol.k)
    print(f"  frozen k = {k}   tau ladder {['%.8f' % t for t in taus]}",
          flush=True)

    nodes = list(zip(QUANTILES, taus))
    if args.nodes is not None:
        nodes = nodes[:args.nodes]

    results["provenance"] = {
        "script": "numerical_v4/checks/t5_who_gets_caught.py",
        "params_hash": p_base.hash_str(),
        "mark": int(p_base.mark), "H": int(p_base.H),
        "frozen_k": [float(x) for x in k],
        "cutoff_scale": float(resid.cutoff_scale),
        "payoff_scale": float(resid.payoff_scale),
        "tau_ladder": list(taus), "tau_quantiles": list(QUANTILES),
        "windows": {"T_long": T_LONG, "T_short": T_SHORT},
        "kappa_point": float(p_base.kappa),
        "deriv_step": float(DERIV_STEP),
        "measurement": "s_A is the 4th-order point derivative of E[h | A] "
                       "under the T = 10 pricing map; s_B is "
                       "d_kappa(Lambda_T - Lambda_T') / P(B), which carries "
                       "survivors' re-pricing (not tilde s_B); C_T is "
                       "S_P(5)/S_P(10) from each clock's own pooled pass "
                       "(the point-derivative convention for S_P, stencil "
                       "as numerical_v4.premium.d_dkappa)",
        "weights": "subset masses from the alive MEASURE weights and the "
                   "likelihood table (the pooled pass keeps only their sum "
                   "over types); beliefs from the pooled pass's own market "
                   "weights",
        "nodes_run": (len(nodes) if args.nodes is not None else "all"),
        "t1_comparison": "read by the orchestrator from "
                         "numerical_v4/checks/t2_t1_check.json, check "
                         "t1_block4_window_margin, at the same tau nodes",
    }

    rows = []
    for qi, tau in nodes:
        t1 = time.perf_counter()
        r = node_row(k, p_base, tau, qi)
        rows.append(r)
        print(f"  q={qi:.1f} tau={tau:.8f} P(A)={r['P_A']:.6f} "
              f"P(B)={r['P_B']:.6f} s_A={r['s_A']:+.6e} s_B={r['s_B']:+.6e} "
              f"C_T={r['C_T'] if isinstance(r['C_T'], float) else 'undef'} "
              f"cond={r['corollary_condition_holds']} "
              f"C_T_le_1={r['C_T_le_1']}"
              f"  ({time.perf_counter() - t1:.0f}s)", flush=True)

    defined_rows = [r for r in rows if r["_defined"]]
    max_mass = max(max(r["mass_residual_PA"], r["mass_residual_PB"],
                       r["mass_residual_PB_omega_gap"], r["mass_residual_Psurv"],
                       r["kernel_residual_T10"], r["kernel_residual_T5"],
                       r["s_A_vs_MP_residual"], r["s_AB_vs_MP_residual"])
                   for r in rows)
    record(
        "t5_mass_bookkeeping", max_mass < TOL_MASS, "wiring",
        {"request": "P(A) = 1 - Omega(T=10), P(A) - P(B) = 1 - Omega(T=5), "
                    "P(B) = Omega(T=5) - Omega(T=10), all against the "
                    "independently computed cell weights, and "
                    "Delta_m E[h|A] = M_P of the T = 10 pooled pass, "
                    "Delta_m E[h^{(T')}|A\\\\B] = M_P of the T = 5 pooled "
                    "pass, at every node, predicted below 1e-12",
         "tol": TOL_MASS, "max_residual": max_mass,
         "why_wiring": "the subsets are a regrouping of the same enumeration "
                       "the pooled pass performs, and Omega here comes from the "
                       "atoms' own D flags rather than from the subset weights, "
                       "so a mismatch is an implementation error and not a "
                       "finding about the model",
         "rows": [{"tau_quantile": r["tau_quantile"], "P_A": r["P_A"],
                   "P_B": r["P_B"], "mass_residual_PA": r["mass_residual_PA"],
                   "mass_residual_PB": r["mass_residual_PB"],
                   "mass_residual_PB_omega_gap": r["mass_residual_PB_omega_gap"],
                   "kernel_residual_T10": r["kernel_residual_T10"],
                   "kernel_residual_T5": r["kernel_residual_T5"]}
                  for r in rows]},
    )

    max_ident = max(max(r["identity_residual"], r["split_residual"])
                    for r in rows)
    record(
        "t5_identity", max_ident < TOL_IDENT, "wiring",
        {"request": "the cut identity: d_kappa E[h^{(T')} | A\\\\B] against "
                    "(P(A) s_A - P(B) s_B) / (P(A) - P(B)), with s_B = "
                    "d_kappa(Lambda_T - Lambda_T') / P(B), and the split "
                    "s_B = tilde s_B - ((1-phi)/phi) delta, at every node, "
                    "predicted below 1e-12",
         "tol": TOL_IDENT, "max_residual": max_ident,
         "why_wiring": "the cell masses do not depend on kappa, so the "
                       "identity is exact by linearity once s_B is the "
                       "corollary's caught leg; the residual is round-off",
         "rows": [{"tau_quantile": r["tau_quantile"], "s_A": r["s_A"],
                   "s_B": r["s_B"], "s_B_tilde": r["s_B_tilde"],
                   "s_AB_formula": r["s_AB_formula"],
                   "s_AB_own": r["s_AB_own"],
                   "identity_residual": r["identity_residual"],
                   "split_residual": r["split_residual"],
                   "repricing_remainder_delta": r["repricing_remainder_delta"]}
                  for r in rows]},
    )

    # Biconditional: C_T <= 1 iff s_B lies weakly between s_A and
    # ((2-phi)/phi) s_A.  A node whose C_T sits within BOUNDARY of one is
    # counted as agreeing.
    agree, disagree = [], []
    for r in rows:
        if r["biconditional_boundary_node"]:
            agree.append({kk: r[kk] for kk in ("tau_quantile", "C_T")})
            continue
        ok = (r["C_T_le_1"] == r["corollary_condition_holds"])
        (agree if ok else disagree).append(
            {kk: r[kk] for kk in ("tau_quantile", "s_A", "s_B", "shares_sign",
                                  "C_T", "C_T_le_1",
                                  "corollary_condition_holds")})
    record(
        "t5_biconditional", len(disagree) == 0, "substantive",
        {"request": "at every calibration node, C_T <= 1 if and only if "
                    "s_B lies weakly between s_A and ((2-phi)/phi) s_A "
                    "(corollary part iv)",
         "n_nodes": len(rows), "n_agree": len(agree), "n_disagree": len(disagree),
         "mixed_sign_nodes": [r["tau_quantile"] for r in rows
                              if not r["shares_sign"]],
         "boundary_tolerance": BOUNDARY,
         "disagreements": disagree,
         "rows": [{kk: r[kk] for kk in
                   ("tau_quantile", "tau", "s_A", "s_B", "phi", "upper_limit_b",
                    "shares_sign", "corollary_condition_holds", "C_T",
                    "C_T_le_1", "predicted_C_T_le_1")}
                  for r in rows]},
    )

    record(
        "t5_CT_point_convention", len(defined_rows) == len(rows), "reported",
        {"request": "S_P(5)/S_P(10) per node under the point-derivative "
                    "convention, with its <= 1 verdict, the two sensitivities "
                    "behind the corollary, and both booleans",
         "reading": "this is the record the orchestrator compares against "
                    "t2_t1_check.json check t1_block4_window_margin at the "
                    "same tau nodes; the verdicts, not the values, are the "
                    "comparison, because T1 measures S_P by total variation "
                    "over the kappa grid and this record by the point "
                    "derivative at the baseline kappa",
         "n_nodes": len(rows),
         "verdicts": [{kk: r[kk] for kk in
                       ("tau_quantile", "s_A", "s_B", "S_P10_point",
                        "S_P5_point_own", "C_T", "C_T_le_1",
                        "corollary_condition_holds", "shares_sign")}
                      for r in rows]},
    )

    results["nodes"] = [{kk: v for kk, v in r.items() if not kk.startswith("_")}
                        for r in rows]
    results["seconds"] = time.perf_counter() - t0
    results["all_pass"] = results["n_fail"] == 0
    results["n_nodes_run"] = len(rows)

    with open(OUT, "w") as fh:
        json.dump(results, fh, indent=2, default=float)
    print(f"\n{'ALL PASS' if results['all_pass'] else str(results['n_fail']) + ' FAIL'}"
          f"  in {results['seconds']:.0f} s  ({len(rows)} node(s))  ->  {OUT}",
          flush=True)
    return 0 if results["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
