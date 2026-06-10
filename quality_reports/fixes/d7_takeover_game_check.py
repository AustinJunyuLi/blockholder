"""Numerical verification of D7: the disagreement-node tender game.

Checks (mirroring D7_takeover_game_microfound.tex):
  1. Monte-Carlo of the *game itself* vs closed forms for d(a), both regimes.
  2. Bounds and monotonicity: psi, lambda in [0,1]; lambda decreasing in q,
     increasing in gamma; pivotal lambda >= non-pivotal lambda; pivotality jump.
  3. Theorem d7:A3 iff boundary: lambda == 0 exactly on (F1) q=1, (F2) gamma=0,
     (F3) non-pivotal OR P(S_F >= phi + delta_e) = 1.
  4. Calibration consistency: primitives reproducing the body's wedge
     m1 - m0 = 0.20 (and hence mtil - m0 = 0.18 at rho = 0.9).
  5. Proposition d7:afs: measured premium M(pi) = mbar(pi)/P(pi) on the body's
     pricing fixed point is strictly decreasing in pi for small lambda;
     numerical lambda_crit reported.

Run:  .venv/bin/python quality_reports/fixes/d7_takeover_game_check.py
Output: quality_reports/fixes/d7_takeover_game_check.json
"""

from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

RNG = np.random.default_rng(20260610)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "d7_takeover_game_check.json")

TOL_MC = 4e-3      # Monte-Carlo tolerance (N = 2e6, CRN differencing)
TOL_EXACT = 1e-12  # closed-form identity tolerance

results: dict = {"checks": [], "n_fail": 0}


def record(name: str, ok: bool, detail: dict) -> None:
    results["checks"].append({"name": name, "pass": bool(ok), **detail})
    if not ok:
        results["n_fail"] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# ----------------------------------------------------------------------------
# Closed forms (exponential fringe synergy S_F ~ Exp(mean=mu_S), c_F ~ U[0,c_max])
# ----------------------------------------------------------------------------

def q_of(phi: float, c_max: float) -> float:
    return min(phi / c_max, 1.0) if c_max > 0 else 1.0


def Gbar_exp(x: float, mu_S: float, s_min: float = 0.0) -> float:
    """Survival of S_F = s_min + Exp(mu_S)."""
    return 1.0 if x <= s_min else math.exp(-(x - s_min) / mu_S)


def Emax_exp(x: float, mu_S: float, s_min: float = 0.0) -> float:
    """E[(S_F - x)^+] for S_F = s_min + Exp(mu_S)."""
    if x <= s_min:
        return (s_min - x) + mu_S
    return mu_S * math.exp(-(x - s_min) / mu_S)


def psi_pivotal(gamma: float, delta_e: float, phi: float, mu_S: float, s_min: float = 0.0) -> float:
    """psi = (1/c) int_0^c Gbar(phi + t) dt, c = (1-gamma) delta_e."""
    c = (1.0 - gamma) * delta_e
    if c <= 0:
        return 1.0  # multiplied by zero anyway; convention
    # integral of survival of shifted exponential
    a, b = phi, phi + c
    lo = max(a, s_min)
    integral = max(0.0, min(b, s_min) - a)  # region where Gbar = 1
    if b > lo:
        integral += mu_S * (math.exp(-(lo - s_min) / mu_S) - math.exp(-(b - s_min) / mu_S))
    return integral / c


def lam_closed(q: float, gamma: float, pivotal: bool, delta_e: float, phi: float,
               mu_S: float, s_min: float = 0.0) -> float:
    psi = psi_pivotal(gamma, delta_e, phi, mu_S, s_min) if pivotal else 1.0
    return 1.0 - q * (1.0 - gamma) * psi


def d_closed(a: int, q: float, gamma: float, pivotal: bool, w: float, delta_e: float,
             phi: float, mu_S: float, s_min: float = 0.0) -> float:
    base = w + a * delta_e
    if pivotal:
        return base + q * Emax_exp(phi + (1.0 - gamma) * a * delta_e, mu_S, s_min)
    mean_S = s_min + mu_S
    return base + q * (mean_S - phi - (1.0 - gamma) * a * delta_e)


# ----------------------------------------------------------------------------
# 1. Monte-Carlo of the game vs closed forms
# ----------------------------------------------------------------------------

def mc_game(a: int, q: float, gamma: float, pivotal: bool, w: float, delta_e: float,
            phi: float, mu_S: float, n: int, cF: np.ndarray, SF: np.ndarray) -> float:
    """Simulate the solved equilibrium path of the tender game."""
    c_max = phi / q if q > 0 else float("inf")  # uniform c_F on [0, c_max]
    enter = (cF * c_max) <= phi if np.isfinite(c_max) else np.ones(n, bool)
    if pivotal:
        acquiesce = SF >= phi + (1.0 - gamma) * a * delta_e
        raid = enter & acquiesce
    else:
        raid = enter
    payoff = np.where(raid, w + gamma * a * delta_e + SF - phi, w + a * delta_e)
    return float(payoff.mean())


def check_mc():
    n = 2_000_000
    w, delta_e, phi, mu_S = 1.0, 0.5, 0.12, 0.6
    cF = RNG.random(n)                       # common random numbers across cells
    SF = RNG.exponential(mu_S, n)
    worst = 0.0
    for pivotal in (False, True):
        for q in (0.35, 0.8):
            for gamma in (0.0, 0.55, 1.0):
                for a in (0, 1):
                    mc = mc_game(a, q, gamma, pivotal, w, delta_e, phi, mu_S, n, cF, SF)
                    cf = d_closed(a, q, gamma, pivotal, w, delta_e, phi, mu_S)
                    worst = max(worst, abs(mc - cf))
                # lambda via CRN differencing
                lam_mc = (mc_game(1, q, gamma, pivotal, w, delta_e, phi, mu_S, n, cF, SF)
                          - mc_game(0, q, gamma, pivotal, w, delta_e, phi, mu_S, n, cF, SF)) / delta_e
                lam_cf = lam_closed(q, gamma, pivotal, delta_e, phi, mu_S)
                worst = max(worst, abs(lam_mc - lam_cf))
    record("mc_game_vs_closed_forms", worst < TOL_MC, {"worst_abs_err": worst, "tol": TOL_MC, "n": n})


# ----------------------------------------------------------------------------
# 2. Bounds, monotonicity, pivotality jump
# ----------------------------------------------------------------------------

def check_bounds_monotonicity():
    delta_e, phi, mu_S = 0.5, 0.12, 0.6
    qs = np.linspace(0, 1, 21)
    gs = np.linspace(0, 1, 21)
    ok_bounds, ok_q, ok_g, ok_regime = True, True, True, True
    for pivotal in (False, True):
        for g in gs:
            lams = [lam_closed(q, g, pivotal, delta_e, phi, mu_S) for q in qs]
            ok_bounds &= all(-1e-15 <= l <= 1 + 1e-15 for l in lams)
            ok_q &= all(lams[i + 1] <= lams[i] + 1e-12 for i in range(len(lams) - 1))
        for q in qs:
            lams = [lam_closed(q, g, pivotal, delta_e, phi, mu_S) for g in gs]
            ok_g &= all(lams[i + 1] >= lams[i] - 1e-12 for i in range(len(lams) - 1))
    for q in qs:
        for g in gs:
            ok_regime &= (lam_closed(q, g, True, delta_e, phi, mu_S)
                          >= lam_closed(q, g, False, delta_e, phi, mu_S) - 1e-12)
    psis = [psi_pivotal(g, delta_e, phi, mu_S) for g in gs[:-1]]
    ok_psi = all(0 <= p <= 1 for p in psis)
    jump = (lam_closed(0.8, 0.3, True, delta_e, phi, mu_S)
            - lam_closed(0.8, 0.3, False, delta_e, phi, mu_S))
    record("bounds_and_monotonicity",
           ok_bounds and ok_q and ok_g and ok_regime and ok_psi and jump >= 0,
           {"lambda_in_01": ok_bounds, "decreasing_in_q": ok_q, "increasing_in_gamma": ok_g,
            "pivotal_ge_nonpivotal": ok_regime, "psi_in_01": ok_psi,
            "pivotality_jump_at_q08_g03": jump})


# ----------------------------------------------------------------------------
# 3. Theorem d7:A3 iff boundary
# ----------------------------------------------------------------------------

def check_iff_boundary():
    delta_e, phi, mu_S = 0.5, 0.12, 0.6
    ok = True
    cells = []
    for q in (0.0, 0.3, 0.7, 1.0):
        for gamma in (0.0, 0.4, 1.0):
            for pivotal in (False, True):
                for s_min in (0.0, phi + delta_e + 0.05):  # second: P(S_F >= phi+delta_e)=1
                    lam = lam_closed(q, gamma, pivotal, delta_e, phi, mu_S, s_min)
                    F1 = (q == 1.0)
                    F2 = (gamma == 0.0)
                    F3 = (not pivotal) or (Gbar_exp(phi + delta_e, mu_S, s_min) >= 1.0)
                    predicted_zero = F1 and F2 and F3
                    actual_zero = abs(lam) < TOL_EXACT
                    ok &= (predicted_zero == actual_zero)
                    cells.append({"q": q, "gamma": gamma, "pivotal": pivotal,
                                  "s_min": s_min, "lambda": lam,
                                  "F1F2F3": [F1, F2, F3]})
    record("thm_A3_iff_boundary", ok, {"n_cells": len(cells)})
    results["iff_cells"] = cells


# ----------------------------------------------------------------------------
# 4. Calibration consistency with the body's (m0, m1) = (0.10, 0.30)
# ----------------------------------------------------------------------------

def check_calibration():
    theta, rho = 0.5, 0.9
    q, gamma, pivotal = 0.5, 0.6, True
    phi, mu_S = 0.12, 0.6
    target_wedge = 0.20
    # solve for Delta_eng: (1-theta) * lambda(Delta_eng) * rho * Delta_eng = 0.20
    lo, hi = 1e-6, 10.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lam = lam_closed(q, gamma, pivotal, mid, phi, mu_S)
        val = (1 - theta) * lam * rho * mid
        if val < target_wedge:
            lo = mid
        else:
            hi = mid
    delta_eng = 0.5 * (lo + hi)
    lam = lam_closed(q, gamma, pivotal, delta_eng, phi, mu_S)
    wedge = (1 - theta) * lam * rho * delta_eng
    mtil_minus_m0 = rho * wedge
    ok = (abs(wedge - 0.20) < 1e-9 and abs(mtil_minus_m0 - 0.18) < 1e-9
          and 0 < lam <= 1 and 0 < delta_eng < 2.0)
    record("calibration_consistency", ok,
           {"theta": theta, "rho": rho, "q": q, "gamma": gamma, "pivotal": pivotal,
            "phi": phi, "mu_S": mu_S, "Delta_eng": delta_eng, "lambda": lam,
            "wedge_m1_minus_m0": wedge, "mtil_minus_m0": mtil_minus_m0})


# ----------------------------------------------------------------------------
# 5. Proposition d7:afs — measured-premium reversal on the pricing fixed point
# ----------------------------------------------------------------------------

def norm_cdf(x: float) -> float:
    return 0.5 * math.erfc(-x / math.sqrt(2.0))


def solve_price(pi: float, wedge_expected: float, *, m0=0.10, rho=0.9, Delta=0.25,
                delta_disc=0.95, S_bar=1.44, K=0.15, sigma_xi=0.40, Ev=1.0) -> tuple[float, float]:
    """Fixed point P = delta * [ p(P)*(P + mbar) + (1-p(P))*(Ev + Dtil*pi) ].

    wedge_expected = mtil - m0 (the lambda-scaled object). Returns (P, p).
    """
    Dtil = rho * Delta
    mbar = m0 + wedge_expected * pi
    P = delta_disc * Ev
    for _ in range(500):
        p = 1.0 - norm_cdf((mbar + K - S_bar + P) / sigma_xi)
        P_new = delta_disc * (p * (P + mbar) + (1 - p) * (Ev + Dtil * pi))
        if abs(P_new - P) < 1e-14:
            P = P_new
            break
        P = 0.5 * P + 0.5 * P_new
    p = 1.0 - norm_cdf((mbar + K - S_bar + P) / sigma_xi)
    return P, p


def check_afs_reversal():
    theta, rho = 0.5, 0.9
    # Use the calibration cell from check 4: wedge(lambda) = (1-theta)*lambda*rho*Delta_eng
    cal = next(c for c in results["checks"] if c["name"] == "calibration_consistency")
    Delta_eng = cal["Delta_eng"]
    pis = np.linspace(0.05, 0.95, 19)
    lam_grid = np.linspace(0.0, 1.0, 101)
    lambda_crit = None
    monotone_at_zero = None
    for lam in lam_grid:
        wedge_exp = rho * (1 - theta) * lam * rho * Delta_eng  # mtil - m0
        M = []
        for pi in pis:
            P, _ = solve_price(pi, wedge_exp)
            mbar = 0.10 + wedge_exp * pi
            M.append(mbar / P)
        dM = np.diff(M)
        decreasing = bool(np.all(dM < 0))
        if lam == 0.0:
            monotone_at_zero = decreasing
        if decreasing:
            lambda_crit = float(lam)  # last lambda with full reversal
        elif lambda_crit is not None:
            break
    ok = bool(monotone_at_zero) and lambda_crit is not None and lambda_crit > 0
    record("afs_measured_premium_reversal", ok,
           {"M_decreasing_at_lambda0": monotone_at_zero,
            "lambda_crit_numeric": lambda_crit,
            "note": "M' < 0 for all interior pi at every lambda <= lambda_crit"})


# ----------------------------------------------------------------------------

def main() -> int:
    check_mc()
    check_bounds_monotonicity()
    check_iff_boundary()
    check_calibration()
    check_afs_reversal()
    results["all_pass"] = results["n_fail"] == 0
    with open(OUT, "w") as fh:
        json.dump(results, fh, indent=2, default=float)
    print(f"\n{'ALL CHECKS PASS' if results['all_pass'] else 'FAILURES: ' + str(results['n_fail'])}")
    print(f"JSON: {OUT}")
    return 0 if results["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
