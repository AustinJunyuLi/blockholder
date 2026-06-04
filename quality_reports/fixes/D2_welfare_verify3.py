#!/usr/bin/env python
"""
D2 welfare verification (attempt 3 -- CORRECT API).

API (verified by reading numerical/model.py, numerical/solver.py):
  solver.solve_valid(params, prev_cutoffs=None, residual_tol=1e-5) -> (Cutoffs|None, residual)
  model.compute_minority_gains(k1, k0, kD, params) -> MinorityGains(total, base, activism)
  model.compute_welfare(k1, k0, kD, params) -> (W_min, W_bid, W_B, W_total)
  model.compute_action_probabilities(k1, k0, kD, params) -> (wE, wH, wQ, wP)
  model.compute_equilibrium_prices(k1, k0, kD, params) -> dict {(X,D): P}
  model.compute_posteriors(wE, wH, wQ, wP, kappa) -> dict {(X,D): pi}
  model.bid_probability(P, m_XD, params) -> p

Outputs JSON + TXT so results survive a flaky display channel.
Run:
  PYTHONPATH=/Users/austinli/Projects/blockholder \
    /tmp/blk_venv/bin/python quality_reports/fixes/D2_welfare_verify3.py
"""
import json, traceback
import numpy as np
from scipy.stats import norm
from numerical import params as P
from numerical import model as M
from numerical import solver as S

OUT = {}
ERRS = []

base = P.ModelParams()
OUT["calib"] = dict(delta=base.delta, sigma_xi=base.sigma_xi, S_bar=base.S_bar,
                    rho=base.rho, m0=base.m0, m1=base.m1, K=base.K,
                    m_tilde=base.m_tilde, Delta_tilde=base.Delta_tilde,
                    mu=base.mu, sigma_s=base.sigma_s)

def solve(kappa, prev=None, tol=1e-5):
    pp = P.ModelParams(kappa=kappa)
    c, r = S.solve_valid(pp, prev_cutoffs=prev, residual_tol=tol)
    return pp, c, r

# ---------------------------------------------------------------------------
# (1) Re-confirm Phase-0: endpoint symmetry + Delta^min hump, AND get the
#     FULL welfare decomposition (W_min, W_bid, W_B, W) at every kappa.
# ---------------------------------------------------------------------------
def full_grid():
    rows = []
    prev = None
    for kappa in [1e-4, 0.05, 0.20, 0.35, 0.50, 0.55, 0.59, 0.60, 0.65,
                  0.70, 0.80, 0.85, 0.95, 1-1e-4]:
        pp, c, r = solve(kappa, prev)
        if c is None:
            rows.append({"kappa": kappa, "fail": True, "resid": r}); continue
        prev = c
        wmin, wbid, wB, wtot = M.compute_welfare(c.k1, c.k0, c.kD, pp)
        wE, wH, wQ, wP = M.compute_action_probabilities(c.k1, c.k0, c.kD, pp)
        rows.append({"kappa": round(kappa, 5), "Dmin": wmin, "W_bid": wbid,
                     "W_B": wB, "W_total": wtot,
                     "P_engage": wQ + wP, "omega_P": wP, "omega_Q": wQ,
                     "k1": c.k1, "k0": c.k0, "kD": c.kD, "resid": r})
    return rows
try:
    OUT["full_grid"] = full_grid()
except Exception as e:
    ERRS.append("full_grid: " + repr(e) + "\n" + traceback.format_exc())

# ---------------------------------------------------------------------------
# (2) Locate kappa-dagger (argmax Dmin) and kappa-star (argmax W_total) on a
#     fine residual-filtered grid. Tests the planner-wedge SIGN claim that
#     W' at kappa-dagger has a definite sign (so kappa* != kappa-dagger).
# ---------------------------------------------------------------------------
def planner_kappa():
    fine = np.linspace(0.05, 0.95, 31)
    prev = None
    pts = []
    for kappa in fine:
        pp, c, r = solve(float(kappa), prev)
        if c is None or r > 1e-5:
            continue
        prev = c
        wmin, wbid, wB, wtot = M.compute_welfare(c.k1, c.k0, c.kD, pp)
        pts.append((float(kappa), wmin, wbid, wB, wtot))
    if not pts:
        return {"empty": True}
    arr = np.array(pts)
    kdag = arr[np.argmax(arr[:, 1]), 0]      # argmax W_min
    kstar = arr[np.argmax(arr[:, 4]), 0]     # argmax W_total
    # finite-diff W' and W_min' near kdag
    return {"n": len(pts),
            "kappa_dagger_argmaxWmin": kdag,
            "Dmin_peak": float(np.max(arr[:, 1])),
            "kappa_star_argmaxW": kstar,
            "W_peak": float(np.max(arr[:, 4])),
            "wedge_sign(kstar-kdag)": float(np.sign(kstar - kdag)),
            "grid_head": pts[:3], "grid_tail": pts[-3:]}
try:
    OUT["planner_kappa"] = planner_kappa()
except Exception as e:
    ERRS.append("planner_kappa: " + repr(e) + "\n" + traceback.format_exc())

# ---------------------------------------------------------------------------
# (3) Disclosure-threshold planner. Pin kD, recompute a constrained
#     equilibrium for (k1,k0) holding kD fixed, evaluate W_total(kD) and
#     Dmin(kD); locate kD_star = argmax W_total(kD) and compare to kD_eq.
#     Constrained eq: damped best-response in (k1,k0) with kD pinned. We do
#     NOT have a packaged block best-response, so we re-solve the FULL system
#     and then OVERRIDE kD, recomputing welfare at the perturbed threshold --
#     this is a comparative-welfare probe (partial), clearly labeled.
# ---------------------------------------------------------------------------
def kD_welfare_probe():
    res = {}
    for kappa in [0.20, 0.50, 0.80]:
        pp, ceq, r = solve(kappa)
        if ceq is None:
            res[str(kappa)] = {"fail": True}; continue
        wmin0, wbid0, wB0, wtot0 = M.compute_welfare(ceq.k1, ceq.k0, ceq.kD, pp)
        scan = []
        for kD in np.linspace(max(ceq.k0 + 0.05, ceq.kD - 1.0), ceq.kD + 1.0, 21):
            # hold k1,k0 at equilibrium; vary only the disclosure threshold kD
            wmin, wbid, wB, wtot = M.compute_welfare(ceq.k1, ceq.k0, float(kD), pp)
            scan.append((float(kD), wmin, wbid, wB, wtot))
        arr = np.array(scan)
        kD_star_W = arr[np.argmax(arr[:, 4]), 0]
        kD_star_Wmin = arr[np.argmax(arr[:, 1]), 0]
        res[str(kappa)] = {
            "kD_eq": ceq.kD, "W_eq": wtot0, "Dmin_eq": wmin0,
            "kD_star_argmaxW": float(kD_star_W),
            "kD_star_argmaxWmin": float(kD_star_Wmin),
            "underdisclosure_W(kD_eq>kD_star)": bool(ceq.kD > kD_star_W),
            "scan_head": scan[:2], "scan_tail": scan[-2:],
        }
    return res
try:
    OUT["kD_welfare_probe"] = kD_welfare_probe()
except Exception as e:
    ERRS.append("kD_welfare_probe: " + repr(e) + "\n" + traceback.format_exc())

# ---------------------------------------------------------------------------
# (4) Transfer-netting sanity: confirm the model's compute_welfare uses the
#     same net surplus identity (price-free) we claim in Lemma transfer-netting,
#     by checking that W_total is INVARIANT to a uniform shift in the price
#     level is NOT directly testable here; instead verify the closed-form
#     raider real surplus matches compute_bidder_surplus_state up to the
#     price-transfer convention.
# ---------------------------------------------------------------------------
def raider_closed_form_check():
    pp = P.ModelParams(kappa=0.5)
    # pick a representative disclosed-branch state
    _, c, _ = solve(0.5)
    if c is None:
        return {"fail": True}
    prices = M.compute_equilibrium_prices(c.k1, c.k0, c.kD, pp)
    wE, wH, wQ, wP = M.compute_action_probabilities(c.k1, c.k0, c.kD, pp)
    post = M.compute_posteriors(wE, wH, wQ, wP, pp.kappa)
    checks = []
    for (X, D), Pval in prices.items():
        pi = post.get((X, D), 0.0)
        m_XD = pp.m0 + (pp.m_tilde - pp.m0) * pi
        # model's bidder surplus E[max(Pi_B,0)]
        bs_model = M.compute_bidder_surplus_state(Pval, m_XD, pp)
        # closed form: T=(m+K-S+P)/sx ; E[max(xi-T*sx? )]... model uses
        # surplus = sx*phi(z) - T*(1-Phi(z)) with T=m+K-Sbar+P, z=T/sx
        T = m_XD + pp.K - pp.S_bar + Pval
        z = T / pp.sigma_xi
        bs_cf = pp.sigma_xi * norm.pdf(z) - T * (1 - norm.cdf(z))
        checks.append({"X": X, "D": D, "P": Pval, "pi": pi,
                       "bs_model": bs_model, "bs_cf": bs_cf,
                       "match": abs(bs_model - bs_cf) < 1e-9})
    return {"all_match": all(ch["match"] for ch in checks), "states": checks}
try:
    OUT["raider_check"] = raider_closed_form_check()
except Exception as e:
    ERRS.append("raider_check: " + repr(e) + "\n" + traceback.format_exc())

OUT["errors"] = ERRS

base_out = "/Users/austinli/Projects/blockholder/quality_reports/fixes/"
with open(base_out + "_d2_verify3.json", "w") as f:
    json.dump(OUT, f, indent=1, default=str)

with open(base_out + "_d2_verify3.txt", "w") as f:
    f.write("CALIB: " + json.dumps(OUT["calib"], default=str) + "\n\n")
    f.write("FULL GRID (kappa, Dmin=W_min, W_bid, W_B, W_total, P_engage, kD, resid):\n")
    for row in OUT.get("full_grid", []):
        f.write("  " + json.dumps(row, default=str) + "\n")
    f.write("\nPLANNER (kappa): " + json.dumps(OUT.get("planner_kappa"), indent=1, default=str) + "\n")
    f.write("\nkD WELFARE PROBE: " + json.dumps(OUT.get("kD_welfare_probe"), indent=1, default=str) + "\n")
    f.write("\nRAIDER CLOSED-FORM CHECK all_match: %s\n" %
            (OUT.get("raider_check", {}).get("all_match")))
    f.write("\nERRORS:\n")
    for e in ERRS:
        f.write(e + "\n----\n")
print("DONE verify3")
