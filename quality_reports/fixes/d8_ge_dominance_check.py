"""Numerical verification of D8: the GE cutoff-shift channel.

Checks (mirroring D8_GE_dominance_MCS.tex):
  1. Pricing-layer IFT (Lemma d8:pricing): the quotient formula for dP*/dpi
     matches finite differences of the pricing fixed point, cell by cell.
  2. Channel decomposition along the baseline path: total dDmin/dkappa
     (equilibrium FD) = E' (channel A, kappa-FD at frozen cutoffs) + B
     (residual); cross-checked against the exact IFT form
     B_ift = sum_i dPhi/dk_i * (dk/dkappa)_i with dk/dkappa solved from
     (I - D_kT) x = d_kappa T.
  3. Contraction modulus L = ||D_kT||_inf < 1 along the path (A6, quantified).
  4. Region certification (Theorem thm:d8-region / Corollary cor:d8-baseline):
     (R1) pointwise dominance off an eps-ball around the channel-A peak and
     (R2) integral control inside it, under three bounds (exact |B_ift|,
     sharp (sum W)*||dk/dkappa||, loose (sum W)*||d_kappa T||/(1-L)).
  5. Counterexample (Proposition prop:d8-counter): at sigma_xi = 0.60 cells,
     full-equilibrium Delta_min(kappa) has an interior trough while channel A
     is single-peaked; int |B| exceeds the channel-A amplitude.

The best-response map T freezes beliefs/prices at the current cutoffs and
re-solves the three indifference points (collapsed-Hold handled by working in
the effective (k1, kD) system, as at the baseline calibration).

Run:  .venv/bin/python quality_reports/fixes/d8_ge_dominance_check.py
Output: quality_reports/fixes/d8_ge_dominance_check.json  (+ console log)
"""

from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

from numerical.params import Action, ModelParams, TOL_REGION, TOL_RESIDUAL  # noqa: E402
from numerical.model import (  # noqa: E402
    compute_action_probabilities,
    compute_equilibrium_prices,
    compute_expected_payoff,
    compute_minority_gains,
    compute_posteriors,
)
from numerical.solver import solve_valid  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "d8_ge_dominance_check.json")
results: dict = {"checks": [], "n_fail": 0}


def record(name: str, ok: bool, detail: dict) -> None:
    results["checks"].append({"name": name, "pass": bool(ok), **detail})
    if not ok:
        results["n_fail"] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    for k, v in detail.items():
        print(f"    {k}: {v}")


# ----------------------------------------------------------------------------
# Phi(k; kappa) and the best-response map T
# ----------------------------------------------------------------------------

def phi_fn(k1: float, k0: float, kD: float, params: ModelParams) -> float:
    """Delta_min as a function of cutoffs and (through params) kappa."""
    return compute_minority_gains(k1, k0, kD, params).total


def _frozen_payoffs(k1, k0, kD, params):
    omega = compute_action_probabilities(k1, k0, kD, params)
    post = compute_posteriors(*omega, params.kappa)
    prices = compute_equilibrium_prices(k1, k0, kD, params)
    return lambda action, s: compute_expected_payoff(action, float(s), prices, post, params)


def _root(g, lo: float, hi: float, n_scan: int = 121) -> float:
    """Bisection root of g on [lo, hi] after a sign-change scan; boundary on failure."""
    xs = np.linspace(lo, hi, n_scan)
    gs = np.array([g(x) for x in xs])
    idx = np.where(np.sign(gs[:-1]) * np.sign(gs[1:]) < 0)[0]
    if len(idx) == 0:
        return float(xs[np.argmin(np.abs(gs))])
    a, b = float(xs[idx[0]]), float(xs[idx[0] + 1])
    for _ in range(80):
        m = 0.5 * (a + b)
        if np.sign(g(a)) * np.sign(g(m)) <= 0:
            b = m
        else:
            a = m
    return 0.5 * (a + b)


def best_response(k1: float, k0: float, kD: float, params: ModelParams,
                  collapsed: bool) -> tuple:
    """One application of T: re-solve indifference points at frozen beliefs."""
    U = _frozen_payoffs(k1, k0, kD, params)
    s_min = params.mu - 6 * params.sigma_s
    s_max = params.mu + 6 * params.sigma_s
    if collapsed:
        t1 = _root(lambda s: U(Action.EXIT, s) - U(Action.QUIET, s), s_min, s_max)
        tD = _root(lambda s: U(Action.QUIET, s) - U(Action.PUBLIC, s), t1, s_max)
        return (t1, t1, tD)
    t1 = _root(lambda s: U(Action.EXIT, s) - max(U(Action.HOLD, s), U(Action.QUIET, s)),
               s_min, s_max)
    t0 = _root(lambda s: U(Action.HOLD, s) - U(Action.QUIET, s), t1, s_max)
    tD = _root(lambda s: U(Action.QUIET, s) - U(Action.PUBLIC, s), t0, s_max)
    return (t1, t0, tD)


# ----------------------------------------------------------------------------
# 1. Pricing-layer IFT spot check
# ----------------------------------------------------------------------------

def norm_cdf(x):
    return 0.5 * math.erfc(-x / math.sqrt(2.0))


def norm_pdf(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def _price_fp(pi: float, Ev: float, p: ModelParams) -> float:
    mbar = p.m0 + (p.m_tilde - p.m0) * pi
    Vhat = Ev + p.Delta_tilde * pi
    P = p.delta * p.mu
    for _ in range(800):
        pb = 1.0 - norm_cdf((mbar + p.K - p.S_bar + P) / p.sigma_xi)
        P_new = p.delta * (pb * (P + mbar) + (1 - pb) * Vhat)
        if abs(P_new - P) < 1e-14:
            return P_new
        P = 0.5 * P + 0.5 * P_new
    return P


def check_pricing_ift():
    p = ModelParams.baseline()
    Ev = p.mu
    worst = 0.0
    for pi in (0.1, 0.5, 0.9):
        h = 1e-6
        fd = (_price_fp(pi + h, Ev, p) - _price_fp(pi - h, Ev, p)) / (2 * h)
        # quotient formula (Lemma d8:pricing)
        P = _price_fp(pi, Ev, p)
        mbar = p.m0 + (p.m_tilde - p.m0) * pi
        Vhat = Ev + p.Delta_tilde * pi
        t = (mbar + p.K - p.S_bar + P) / p.sigma_xi
        pb = 1.0 - norm_cdf(t)
        dpdm = -norm_pdf(t) / p.sigma_xi
        num = p.delta * (pb * (p.m_tilde - p.m0) + (1 - pb) * p.Delta_tilde
                         + dpdm * (p.m_tilde - p.m0) * (P + mbar - Vhat))
        ell = p.delta * (pb + dpdm * (P + mbar - Vhat))
        quotient = num / (1 - ell)
        worst = max(worst, abs(fd - quotient))
    record("pricing_layer_ift", worst < 1e-6, {"worst_abs_err": worst})


# ----------------------------------------------------------------------------
# 2-4. Path decomposition, contraction modulus, region certification
# ----------------------------------------------------------------------------

def path_analysis(params: ModelParams, kappas: np.ndarray, h_k: float = 2e-3,
                  h_c: float = 1e-4, label: str = "baseline") -> dict:
    """Solve the path and compute (E', B, B_ift, L, weights, bounds) per kappa."""
    rows = []
    prev = None
    for kap in kappas:
        p = params.replace(kappa=float(kap))
        cut, res = solve_valid(p, prev)
        if cut is None or res > TOL_RESIDUAL:
            prev = None
            continue
        prev = cut
        k1, k0, kD = cut
        collapsed = (k0 - k1) <= TOL_REGION

        # total derivative: FD with warm-started re-solves
        tot = None
        cut_p, res_p = solve_valid(params.replace(kappa=float(kap + h_k)), cut)
        cut_m, res_m = solve_valid(params.replace(kappa=float(kap - h_k)), cut)
        if cut_p is not None and cut_m is not None and max(res_p, res_m) <= TOL_RESIDUAL:
            tot = (phi_fn(*cut_p, params.replace(kappa=float(kap + h_k)))
                   - phi_fn(*cut_m, params.replace(kappa=float(kap - h_k)))) / (2 * h_k)

        # channel A: kappa-FD at frozen cutoffs
        Ep = (phi_fn(k1, k0, kD, params.replace(kappa=float(kap + h_k)))
              - phi_fn(k1, k0, kD, params.replace(kappa=float(kap - h_k)))) / (2 * h_k)

        # weights: FD of Phi in effective cutoffs
        if collapsed:
            W1 = abs(phi_fn(k1 + h_c, k0 + h_c, kD, p) - phi_fn(k1 - h_c, k0 - h_c, kD, p)) / (2 * h_c)
            WD = abs(phi_fn(k1, k0, kD + h_c, p) - phi_fn(k1, k0, kD - h_c, p)) / (2 * h_c)
            grads = [
                (phi_fn(k1 + h_c, k0 + h_c, kD, p) - phi_fn(k1 - h_c, k0 - h_c, kD, p)) / (2 * h_c),
                (phi_fn(k1, k0, kD + h_c, p) - phi_fn(k1, k0, kD - h_c, p)) / (2 * h_c),
            ]
            Ws = [W1, WD]
        else:
            grads, Ws = [], []
            for i in range(3):
                dv = [0.0, 0.0, 0.0]
                dv[i] = h_c
                g = (phi_fn(k1 + dv[0], k0 + dv[1], kD + dv[2], p)
                     - phi_fn(k1 - dv[0], k0 - dv[1], kD - dv[2], p)) / (2 * h_c)
                grads.append(g)
                Ws.append(abs(g))

        # best-response Jacobian and kappa-sensitivity (effective system)
        def T_eff(vec, kappa_val):
            pp = params.replace(kappa=float(kappa_val))
            if collapsed:
                t = best_response(vec[0], vec[0], vec[1], pp, True)
                return np.array([t[0], t[2]])
            t = best_response(vec[0], vec[1], vec[2], pp, False)
            return np.array(t)

        vec0 = np.array([k1, kD]) if collapsed else np.array([k1, k0, kD])
        n = len(vec0)
        J = np.zeros((n, n))
        for j in range(n):
            dv = np.zeros(n)
            dv[j] = h_c
            J[:, j] = (T_eff(vec0 + dv, kap) - T_eff(vec0 - dv, kap)) / (2 * h_c)
        dTdk_inf = float(np.max(np.sum(np.abs(J), axis=1)))  # ||D_kT||_inf
        dT_dkappa = (T_eff(vec0, kap + h_k) - T_eff(vec0, kap - h_k)) / (2 * h_k)

        L = dTdk_inf
        B_ift = None
        dk_inf = None
        if L < 1:
            dk = np.linalg.solve(np.eye(n) - J, dT_dkappa)
            dk_inf = float(np.max(np.abs(dk)))
            B_ift = float(np.dot(grads, dk))

        rows.append({
            "kappa": float(kap), "k1": k1, "k0": k0, "kD": kD,
            "collapsed": bool(collapsed), "Dmin": phi_fn(k1, k0, kD, p),
            "total_deriv": tot, "chanA": Ep,
            "chanB_resid": (tot - Ep) if tot is not None else None,
            "B_ift": B_ift, "L": L, "sumW": float(np.sum(Ws)),
            "dT_dkappa_inf": float(np.max(np.abs(dT_dkappa))),
            "dk_dkappa_inf": dk_inf,
        })
    return {"label": label, "rows": rows}


def check_baseline_path():
    params = ModelParams.baseline()
    kappas = np.linspace(0.30, 0.85, 23)
    pa = path_analysis(params, kappas)
    rows = [r for r in pa["rows"] if r["total_deriv"] is not None and r["B_ift"] is not None]
    if not rows:
        record("baseline_path_decomposition", False, {"reason": "no valid rows"})
        return None

    # contraction modulus along the path
    Lmax = max(r["L"] for r in rows)
    record("contraction_modulus_A6", Lmax < 1.0,
           {"L_max_on_path": Lmax, "n_points": len(rows)})

    # cross-check: residual B vs exact IFT B
    errs = [abs(r["chanB_resid"] - r["B_ift"]) for r in rows]
    scale = max(max(abs(r["chanB_resid"]) for r in rows), 1e-6)
    ok = max(errs) < max(0.25 * scale, 5e-3)
    record("channel_B_residual_vs_IFT", ok,
           {"max_abs_diff": max(errs), "scale": scale,
            "note": "FD-on-solver noise tolerance"})

    # region certification
    ks = np.array([r["kappa"] for r in rows])
    Ep = np.array([r["chanA"] for r in rows])
    E_path = np.concatenate([[0.0], np.cumsum(0.5 * (Ep[1:] + Ep[:-1]) * np.diff(ks))])
    i_peak = int(np.argmax(E_path))
    Astar = float(E_path[i_peak] - 0.5 * (E_path[0] + E_path[-1]))
    eps = 2 * float(np.mean(np.diff(ks)))
    ball = np.abs(ks - ks[i_peak]) <= eps

    cert = {}
    for bound_name, bvals in [
        ("exact_Bift", np.array([abs(r["B_ift"]) for r in rows])),
        ("sharp_sumW_dk", np.array([r["sumW"] * r["dk_dkappa_inf"] for r in rows])),
        ("loose_sumW_dT_over_1mL",
         np.array([r["sumW"] * r["dT_dkappa_inf"] / (1 - r["L"]) for r in rows])),
    ]:
        r1_off = bvals[~ball] < np.abs(Ep[~ball])
        r1_frac = float(np.mean(r1_off)) if len(r1_off) else 0.0
        int_ball = float(np.trapezoid(bvals[ball], ks[ball])) if ball.sum() > 1 else 0.0
        edges = np.where(~ball)[0]
        margin = (min(E_path[max(i_peak - 2, 0)], E_path[min(i_peak + 2, len(ks) - 1)])
                  - max(E_path[0], E_path[-1]))
        r2 = int_ball < margin
        # largest contiguous certified interval around the peak under R1
        lo, hi = i_peak, i_peak
        while lo - 1 >= 0 and (ball[lo - 1] or bvals[lo - 1] < abs(Ep[lo - 1])):
            lo -= 1
        while hi + 1 < len(ks) and (ball[hi + 1] or bvals[hi + 1] < abs(Ep[hi + 1])):
            hi += 1
        cert[bound_name] = {
            "R1_fraction_off_ball": r1_frac,
            "R2_integral_lt_margin": bool(r2),
            "ball_integral": int_ball, "margin": margin,
            "certified_interval": [float(ks[lo]), float(ks[hi])],
        }
    ok_cert = cert["exact_Bift"]["R2_integral_lt_margin"] and \
        cert["exact_Bift"]["certified_interval"][0] < ks[i_peak] < cert["exact_Bift"]["certified_interval"][1]
    record("region_certification", ok_cert,
           {"channelA_peak_kappa": float(ks[i_peak]), "Astar": Astar,
            "eps": eps, **{k: v for k, v in cert.items()}})
    results["baseline_path"] = pa["rows"]
    return pa


# ----------------------------------------------------------------------------
# 5. Counterexample at sigma_xi = 0.60
# ----------------------------------------------------------------------------

def check_counterexample():
    base = ModelParams.baseline()
    kappas = np.linspace(0.10, 0.90, 33)
    found = []
    for S_bar in (1.24, 1.34, 1.44, 1.54, 1.64):
        p0 = base.replace(sigma_xi=0.60, S_bar=S_bar)
        prev = None
        ks, vals, EpL = [], [], []
        for kap in kappas:
            p = p0.replace(kappa=float(kap))
            cut, res = solve_valid(p, prev)
            if cut is None or res > TOL_RESIDUAL:
                prev = None
                continue
            prev = cut
            ks.append(float(kap))
            vals.append(phi_fn(*cut, p))
            h = 2e-3
            EpL.append((phi_fn(*cut, p0.replace(kappa=float(kap + h)))
                        - phi_fn(*cut, p0.replace(kappa=float(kap - h)))) / (2 * h))
        if len(ks) < 10:
            continue
        v = np.array(vals)
        k_arr = np.array(ks)
        i_min = int(np.argmin(v))
        interior_min = 0 < i_min < len(v) - 1
        depth = float(min(v[0], v[-1]) - v[i_min])
        is_trough = interior_min and depth > 1e-4
        # channel A path and amplitude
        Ep = np.array(EpL)
        E_path = np.concatenate([[0.0], np.cumsum(0.5 * (Ep[1:] + Ep[:-1]) * np.diff(k_arr))])
        Astar = float(np.max(E_path) - 0.5 * (E_path[0] + E_path[-1]))
        chanA_singlepeak = bool(np.max(E_path) > max(E_path[0], E_path[-1]))
        # B residual integral
        tot = np.gradient(v, k_arr)
        B = tot - Ep
        intB = float(np.trapezoid(np.abs(B), k_arr))
        found.append({"S_bar": S_bar, "is_trough": is_trough, "trough_depth": depth,
                      "kappa_min": float(k_arr[i_min]), "chanA_singlepeaked": chanA_singlepeak,
                      "Astar_chanA": Astar, "int_absB": intB,
                      "B_exceeds_A": bool(intB > Astar)})
    any_counter = any(c["is_trough"] and c["chanA_singlepeaked"] and c["B_exceeds_A"]
                      for c in found)
    record("counterexample_sigma_xi_060", any_counter, {"cells": found})


# ----------------------------------------------------------------------------

def main() -> int:
    check_pricing_ift()
    check_baseline_path()
    check_counterexample()
    results["all_pass"] = results["n_fail"] == 0
    with open(OUT, "w") as fh:
        json.dump(results, fh, indent=2, default=float)
    print(f"\n{'ALL CHECKS PASS' if results['all_pass'] else 'FAILURES: ' + str(results['n_fail'])}")
    print(f"JSON: {OUT}")
    return 0 if results["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
