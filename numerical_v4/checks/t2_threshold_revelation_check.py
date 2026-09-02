"""Revelation dominance: the kappa-free coefficients c_k and Condition D.

Grid verification for the threshold dial at order size two.  The pooled
order-flow experiment at mark = 2 is a product erasure channel: a round's flow
equals one lump under both marks and only under both, with probability
kappa/2 whatever the type, and every other flow value pins the mark down.  The
pooled premium is therefore a polynomial in eps = kappa/2 with kappa-free
coefficients,

    M_P(tau, T; kappa) = Delta_m * sum_S (1-eps)^|S| eps^(H+1-|S|) G_{tau,T}(S),

    G_{tau,T}(S) = E[ h(nu_S) ],  nu_S the pooled posterior after the marks on S,

and its kappa-derivative is

    d_kappa M_P = -(Delta_m/2) * sum_k (1-eps)^k eps^(H-k) c_k(tau, T),

    c_k = sum_d sum_{|S| = k, d not in S} [ G(S + d) - G(S) ].

This script computes the c_k at every calibration node at mark = 2 and reports:

  rev_representation_matches_pooled_pass   wiring       M_P from the c_k / G(S)
                                                        representation against
                                                        pooled_premium
  rev_coefficients                         substantive  the c_k per node, their
                                                        sign pattern, and S_P
  rev_condition_D                          substantive  |W(tau')| <= |W(tau)| at
                                                        every kappa node on every
                                                        adjacent threshold pair
  rev_condition_D_kappa_free               substantive  the kappa-free sufficient
                                                        form: one sign across k
                                                        and |c_k(tau')| <= |c_k(tau)|
  rev_threshold_dial                       substantive  W_tau * C_tau <= 1 per node

MEASUREMENT.  Sensitivity here is the POINT derivative d_kappa M_P, which the
representation gives in closed form; no finite differencing is used.  The
threshold ladder, the two windows and the 71 node kappa grid are the same ones
the T1 check sweeps, so the verdicts are read at the same nodes.

CELLS.  The S-record partitions the pooled type set into the level sets of the
restricted mark path.  Type n has mark 2 on d < n and 0 on d >= n, so two types
share a level set exactly when no cut point d+1, d in S, separates them: the
cells are intervals of the type index.  G(S) is therefore a sum over at most
|S|+1 intervals, and the 78 possible intervals are priced once per node.

WEIGHTS.  Cell masses use the MEASURE weights and cell beliefs use the MARKET
weights, exactly as the pooled pass does.

Deterministic: no RNG, no Monte Carlo, no file inputs, no network.

Run:    .venv/bin/python numerical_v4/checks/t2_threshold_revelation_check.py
Output: numerical_v4/checks/t2_threshold_revelation_check.json
"""

from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from numerical_v4.menu import atoms, type_reference          # noqa: E402
from numerical_v4.params import ParamsV4                      # noqa: E402
from numerical_v4.policy import evaluate, frozen_tau_grid      # noqa: E402
from numerical_v4.pooled import (                              # noqa: E402
    _alive_weights,
    inner_price,
    pooled_pass,
)
from numerical_v4.premium import pooled_premium                # noqa: E402
from numerical_v4.solver import solve_policy                   # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "t2_threshold_revelation_check.json")

TOL_REP = 1e-12            # representation vs pooled_premium, absolute
TOL_SLACK = 1e-15          # slack allowed in an inequality verdict
S_P_FLOOR = 1e-14          # a ratio on a vanishing denominator is undefined

KAPPAS = np.round(np.arange(0.15, 0.8501, 0.01), 2)     # 71 nodes
QUANTILES = (0.1, 0.3, 0.5, 0.7, 0.9)
TS = (5, 10)
KAPPAS_REP = (0.15, 0.50, 0.85)     # representation wiring check

results: dict = {"checks": [], "n_fail": 0}


def record(name: str, ok: bool, kind: str, detail: dict) -> None:
    results["checks"].append(
        {"name": name, "kind": kind, "pass": bool(ok), **detail}
    )
    if not ok:
        results["n_fail"] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} ({kind})", flush=True)
    print("        " + json.dumps(detail, default=float)[:1200], flush=True)


# ---------------------------------------------------------------------------
# The kappa-free revelation coefficients
# ---------------------------------------------------------------------------


def pooled_weights(k: tuple[float, ...], p: ParamsV4):
    """Measure and market type weights on the pooled cell at the control node."""
    al = atoms(k, p)
    ref = type_reference(p)
    return _alive_weights(al, p.H, p.n_theta, ref)


def interval_kernel(W, Wm, WVm, WAm, p: ParamsV4):
    """h at the posterior of every type interval [lo, hi), priced in one call."""
    n = p.n_theta
    cW = np.concatenate([[0.0], np.cumsum(W)])
    cM = np.concatenate([[0.0], np.cumsum(Wm)])
    cV = np.concatenate([[0.0], np.cumsum(WVm)])
    cA = np.concatenate([[0.0], np.cumsum(WAm)])

    los, his = [], []
    for lo in range(n):
        for hi in range(lo + 1, n + 1):
            los.append(lo)
            his.append(hi)
    los_a, his_a = np.array(los), np.array(his)
    mass_meas = cW[his_a] - cW[los_a]
    mass_mkt = cM[his_a] - cM[los_a]
    live = mass_mkt > 0.0
    pi = np.zeros(los_a.size)
    vhat = np.zeros(los_a.size)
    pi[live] = (cA[his_a] - cA[los_a])[live] / mass_mkt[live]
    vhat[live] = (cV[his_a] - cV[los_a])[live] / mass_mkt[live]
    sol = inner_price(vhat[live], pi[live], p)
    h = np.zeros(los_a.size)
    h[live] = pi[live] * sol.p_bid

    hmap = {(int(a), int(b)): float(x) for a, b, x in zip(los_a, his_a, h)}
    mmap = {(int(a), int(b)): float(x) for a, b, x in zip(los_a, his_a, mass_meas)}
    return hmap, mmap, float(W.sum())


def all_G(W, Wm, WVm, WAm, p: ParamsV4) -> np.ndarray:
    """G(S) for every S in the 2^(H+1) subsets of rounds, indexed by bitmask."""
    hmap, mmap, tot = interval_kernel(W, Wm, WVm, WAm, p)
    n_rounds = p.H + 1
    G = np.zeros(1 << n_rounds)
    for mask in range(1 << n_rounds):
        cuts = [d + 1 for d in range(n_rounds) if mask >> d & 1]
        edges = [0] + cuts + [p.n_theta]
        g = 0.0
        for lo, hi in zip(edges[:-1], edges[1:]):
            if hi <= lo:
                continue
            g += (mmap[(lo, hi)] / tot) * hmap[(lo, hi)]
        G[mask] = g
    return G


def c_levels(G: np.ndarray, H: int) -> np.ndarray:
    """c_k = sum_d sum_{|S| = k, d not in S} [G(S + d) - G(S)]."""
    n_rounds = H + 1
    c = np.zeros(n_rounds)
    pc = np.array([bin(m).count("1") for m in range(1 << n_rounds)])
    for d in range(n_rounds):
        bit = 1 << d
        idx = np.flatnonzero((np.arange(1 << n_rounds) & bit) == 0)
        inc = G[idx | bit] - G[idx]
        np.add.at(c, pc[idx], inc)
    return c


def M_P_from_G(G: np.ndarray, p: ParamsV4, kappa: float) -> float:
    n_rounds = p.H + 1
    eps = kappa / 2.0
    pc = np.array([bin(m).count("1") for m in range(1 << n_rounds)])
    w = (1.0 - eps) ** pc * eps ** (n_rounds - pc)
    return float(p.Delta_m * np.dot(w, G))


def W_of_kappa(c: np.ndarray, p: ParamsV4, kappa: float) -> float:
    """The pooled revelation value W(kappa) = sum_k (1-eps)^k eps^(H-k) c_k."""
    eps = kappa / 2.0
    ks = np.arange(p.H + 1)
    return float(np.dot((1.0 - eps) ** ks * eps ** (p.H - ks), c))


def S_P_of_kappa(c: np.ndarray, p: ParamsV4, kappa: float) -> float:
    return abs(0.5 * p.Delta_m * W_of_kappa(c, p, kappa))


# ---------------------------------------------------------------------------


def main() -> int:
    t0 = time.perf_counter()
    p_seed = ParamsV4.baseline()
    assert p_seed.mark == 2, "this check is stated at order size two"
    print(f"t2_threshold_revelation_check -- mark={p_seed.mark} H={p_seed.H} "
          f"n_hist={p_seed.n_hist}; frozen baseline (2 cold solves) ...",
          flush=True)
    pol_seed, _ = solve_policy(p_seed)
    taus = tuple(float(x) for x in frozen_tau_grid(pol_seed, p_seed, QUANTILES))
    tau_med = float(frozen_tau_grid(pol_seed, p_seed, (0.5,))[0])
    p_base = p_seed.replace(tau=tau_med)
    pol, resid = solve_policy(p_base)
    k = tuple(pol.k)
    print(f"  frozen k = {k}   tau ladder {['%.8f' % t for t in taus]}",
          flush=True)

    results["provenance"] = {
        "script": "numerical_v4/checks/t2_threshold_revelation_check.py",
        "params_hash": p_base.hash_str(),
        "mark": int(p_base.mark), "H": int(p_base.H),
        "frozen_k": [float(x) for x in k],
        "cutoff_scale": float(resid.cutoff_scale),
        "payoff_scale": float(resid.payoff_scale),
        "tau_ladder": list(taus), "tau_quantiles": list(QUANTILES),
        "T_grid": list(TS),
        "kappa_grid": {"lo": float(KAPPAS[0]), "hi": float(KAPPAS[-1]),
                       "n": int(KAPPAS.size), "step": 0.01},
        "measurement": "point derivative d_kappa M_P in closed form from the "
                       "kappa-free coefficients c_k; no finite differencing",
        "weights": "cell mass from the measure weights, cell belief from the "
                   "market weights, as in the pooled pass",
    }

    # -- the coefficients, node by node -------------------------------------
    node: dict = {}
    for T in TS:
        for qi, tau in zip(QUANTILES, taus):
            p = p_base.replace(tau=float(tau), T=int(T))
            W, Wm, WVm, WAm = pooled_weights(k, p)
            G = all_G(W, Wm, WVm, WAm, p)
            c = c_levels(G, p.H)
            Omega = 1.0 - float(W.sum())
            node[(T, qi)] = {
                "T": int(T), "tau_quantile": float(qi), "tau": float(tau),
                "Omega": float(Omega),
                "pooled_type_weights": [float(x) for x in W],
                "c_k": [float(x) for x in c],
                "c_k_signs": [int(np.sign(x)) for x in c],
                "c_k_one_sign": bool(len({int(np.sign(x)) for x in c
                                          if x != 0.0}) <= 1),
                "S_P_at_kappa": {f"{kap:.2f}": S_P_of_kappa(c, p, float(kap))
                                 for kap in KAPPAS_REP},
                "_G": G, "_c": c, "_p": p,
            }
            print(f"  T={T:2d} q={qi:.1f} tau={tau:.8f} Omega={Omega:.6f} "
                  f"c_k={np.array2string(c, precision=5)}", flush=True)

    # -- representation wiring ----------------------------------------------
    probe = node[(TS[0], QUANTILES[-1])]
    rows_rep = []
    for kap in KAPPAS_REP:
        pk = probe["_p"].replace(kappa=float(kap))
        res = pooled_pass(atoms(k, pk), pk, with_runup=False)
        M_code = pooled_premium(res, 0.0, pk)
        M_rep = M_P_from_G(probe["_G"], pk, float(kap))
        rows_rep.append({"kappa": float(kap), "M_P_pooled_pass": float(M_code),
                         "M_P_representation": float(M_rep),
                         "abs_diff": abs(M_code - M_rep)})
        print(f"  representation kappa={kap:.2f} "
              f"M_P={M_code:.15f} vs {M_rep:.15f}", flush=True)
    max_rep = max(r["abs_diff"] for r in rows_rep)
    record(
        "rev_representation_matches_pooled_pass", max_rep < TOL_REP, "wiring",
        {"request": "M_P from the erasure representation against the enumerated "
                    "pooled pass at one node and three kappa values",
         "node": {"T": probe["T"], "tau_quantile": probe["tau_quantile"]},
         "tol": TOL_REP, "max_abs_diff": max_rep, "rows": rows_rep,
         "why_wiring": "the representation is an exact regrouping of the same "
                       "enumeration, so a mismatch is an implementation error "
                       "and not a finding about the model"},
    )

    record(
        "rev_coefficients", True, "substantive",
        {"request": "the kappa-free coefficients c_k at every node, their sign "
                    "pattern, and the implied S_P at three kappa values",
         "reading": "c_k < 0 is the concave direction: revealing one more round "
                    "lowers the pooled expectation of the kernel, so M_P rises "
                    "in kappa; c_k > 0 is the convex direction",
         "rows": [{kk: v[kk] for kk in
                   ("T", "tau_quantile", "tau", "Omega", "c_k", "c_k_signs",
                    "c_k_one_sign", "S_P_at_kappa")}
                  for v in node.values()]},
    )

    # -- Condition D and the dial, pair by pair ------------------------------
    pairs, viol_D, viol_dial = [], [], []
    kappa_free_rows = []
    for T in TS:
        for i in range(len(QUANTILES) - 1, 0, -1):
            hi_n = node[(T, QUANTILES[i])]        # tau
            lo_n = node[(T, QUANTILES[i - 1])]    # tau' < tau
            p = hi_n["_p"]
            W_tau = (1.0 - lo_n["Omega"]) / (1.0 - hi_n["Omega"])
            c_hi, c_lo = hi_n["_c"], lo_n["_c"]

            level_ok = bool(np.all(np.abs(c_lo) <= np.abs(c_hi) + TOL_SLACK))
            kf_ok = bool(level_ok and hi_n["c_k_one_sign"])
            kappa_free_rows.append(
                {"T": int(T), "tau_quantile": float(QUANTILES[i]),
                 "tau_prime_quantile": float(QUANTILES[i - 1]),
                 "level_wise_magnitude_holds": level_ok,
                 "c_k_one_sign_at_tau": bool(hi_n["c_k_one_sign"]),
                 "kappa_free_sufficient_form_holds": kf_ok,
                 "max_level_excess": float(np.max(np.abs(c_lo) - np.abs(c_hi))),
                 "c_k_tau": [float(x) for x in c_hi],
                 "c_k_tau_prime": [float(x) for x in c_lo]})

            per_kappa = []
            for kap in KAPPAS:
                Wv_hi = W_of_kappa(c_hi, p, float(kap))
                Wv_lo = W_of_kappa(c_lo, p, float(kap))
                SP_hi = 0.5 * p.Delta_m * abs(Wv_hi)
                SP_lo = 0.5 * p.Delta_m * abs(Wv_lo)
                D_ok = abs(Wv_lo) <= abs(Wv_hi) + TOL_SLACK
                if SP_hi > S_P_FLOOR:
                    C_tau = SP_lo / SP_hi
                    prod = W_tau * C_tau
                    dial_ok = bool(prod <= 1.0 + TOL_SLACK)
                else:
                    C_tau, prod, dial_ok = "undefined", "undefined", True
                per_kappa.append({"kappa": float(kap), "W_rev_tau": float(Wv_hi),
                                  "W_rev_tau_prime": float(Wv_lo),
                                  "S_P_tau": float(SP_hi),
                                  "S_P_tau_prime": float(SP_lo),
                                  "C_tau": C_tau, "W_tau_C_tau": prod,
                                  "condition_D": bool(D_ok),
                                  "dial_holds": bool(dial_ok)})
                if not D_ok:
                    viol_D.append({"T": int(T), "q": float(QUANTILES[i]),
                                   "q_prime": float(QUANTILES[i - 1]),
                                   "kappa": float(kap)})
                if not dial_ok:
                    viol_dial.append({"T": int(T), "q": float(QUANTILES[i]),
                                      "q_prime": float(QUANTILES[i - 1]),
                                      "kappa": float(kap), "W_C": prod})

            Cs = [r["C_tau"] for r in per_kappa if isinstance(r["C_tau"], float)]
            prods = [r["W_tau_C_tau"] for r in per_kappa
                     if isinstance(r["W_tau_C_tau"], float)]
            pairs.append({
                "T": int(T), "tau": float(hi_n["tau"]),
                "tau_prime": float(lo_n["tau"]),
                "tau_quantile": float(QUANTILES[i]),
                "tau_prime_quantile": float(QUANTILES[i - 1]),
                "Omega_tau": float(hi_n["Omega"]),
                "Omega_tau_prime": float(lo_n["Omega"]),
                "W_tau": float(W_tau),
                "reclassified_mass": float(lo_n["Omega"] - hi_n["Omega"]),
                "condition_D_all_kappa": bool(
                    all(r["condition_D"] for r in per_kappa)),
                "dial_all_kappa": bool(all(r["dial_holds"] for r in per_kappa)),
                "C_tau_min": min(Cs) if Cs else None,
                "C_tau_max": max(Cs) if Cs else None,
                "W_C_max": max(prods) if prods else None,
                "per_kappa": per_kappa,
            })
            print(f"  pair T={T:2d} q{QUANTILES[i]}->q{QUANTILES[i-1]} "
                  f"W_tau={W_tau:.6f} D_all={pairs[-1]['condition_D_all_kappa']} "
                  f"C_max={pairs[-1]['C_tau_max']} "
                  f"WC_max={pairs[-1]['W_C_max']}", flush=True)

    record(
        "rev_condition_D", len(viol_D) == 0, "substantive",
        {"request": "Condition D, |W_rev(tau')| <= |W_rev(tau)|, at every "
                    "adjacent threshold pair, both windows, all 71 kappa nodes",
         "n_pairs": len(pairs), "n_kappa_nodes": int(KAPPAS.size),
         "n_violations": len(viol_D), "violations": viol_D[:40],
         "reading": "Condition D is the composition leg of the threshold dial. "
                    "The coefficients c_k it is built from do not depend on "
                    "kappa, so the whole kappa dependence of the comparison is "
                    "the positive weight vector (1-eps)^k eps^(H-k)",
         "rows": [{kk: r[kk] for kk in
                   ("T", "tau_quantile", "tau_prime_quantile", "W_tau",
                    "Omega_tau", "Omega_tau_prime", "reclassified_mass",
                    "condition_D_all_kappa", "C_tau_min", "C_tau_max")}
                  for r in pairs]},
    )

    n_kf = sum(1 for r in kappa_free_rows
               if r["kappa_free_sufficient_form_holds"])
    record(
        "rev_condition_D_kappa_free", True, "substantive",
        {"request": "the kappa-free sufficient form: the c_k(tau) share one "
                    "sign and |c_k(tau')| <= |c_k(tau)| level by level, which "
                    "delivers Condition D at every kappa at once",
         "n_pairs": len(kappa_free_rows), "n_pairs_holding": int(n_kf),
         "reading": "this is a sufficient condition reported for information. "
                    "Where it fails, Condition D is still read directly at each "
                    "kappa node, which is what the theorem consumes",
         "rows": kappa_free_rows},
    )

    record(
        "rev_threshold_dial", len(viol_dial) == 0, "substantive",
        {"request": "W_tau * C_tau <= 1 at every adjacent threshold pair, both "
                    "windows, all 71 kappa nodes, with W_tau from the flagged "
                    "weights and C_tau from the revelation values",
         "n_violations": len(viol_dial), "violations": viol_dial[:40],
         "rows": [{kk: r[kk] for kk in
                   ("T", "tau_quantile", "tau_prime_quantile", "W_tau",
                    "dial_all_kappa", "W_C_max")} for r in pairs]},
    )

    results["pairs"] = pairs
    results["nodes"] = [{kk: v[kk] for kk in
                         ("T", "tau_quantile", "tau", "Omega",
                          "pooled_type_weights", "c_k", "c_k_signs",
                          "c_k_one_sign", "S_P_at_kappa")}
                        for v in node.values()]
    results["seconds"] = time.perf_counter() - t0

    with open(OUT, "w") as fh:
        json.dump(results, fh, indent=2, default=float)
    print(f"\nwrote {OUT}  ({results['seconds']:.1f}s, "
          f"{results['n_fail']} failing checks)", flush=True)
    return 1 if results["n_fail"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
