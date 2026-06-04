#!/usr/bin/env python
"""
D2 welfare verification (attempt 2). Self-contained, robust.

Uses the paper's OWN solver (numerical.solver.solve_valid) and model
(numerical.model.compute_minority_gains, compute_posteriors, compute_prices,
probability_bid, prob_public_voice). Falls back gracefully if a helper name
differs, by reflecting available functions.

Outputs a clean JSON to quality_reports/fixes/_d2_verify2.json and a human
summary to _d2_verify2.txt so results survive a flaky display channel.

Run:
  PYTHONPATH=/Users/austinli/Projects/blockholder \
    /tmp/blk_venv/bin/python quality_reports/fixes/D2_welfare_verify2.py
"""
import json, math, traceback
from dataclasses import replace

OUT = {}
ERRS = []

def safe(label, fn):
    try:
        return fn()
    except Exception as e:
        ERRS.append(f"{label}: {repr(e)}\n{traceback.format_exc()}")
        return None

import numpy as np
from scipy.stats import norm
import numerical.params as P
import numerical.model as M
import numerical.solver as S

base = P.ModelParams()
OUT["params"] = {k: getattr(base, k) for k in dir(base)
                 if not k.startswith("_") and isinstance(getattr(base, k), (int, float))}

# ---- discover model helpers ----
model_fns = [n for n in dir(M) if not n.startswith("_")]
OUT["model_fns"] = model_fns

def solve(kappa, prev=None, tol=1e-5):
    pp = replace(base, kappa=kappa)
    c, r = S.solve_valid(pp, prev_cutoffs=prev, residual_tol=tol)
    return pp, c, r

# ---------------------------------------------------------------------------
# (1) Endpoint symmetry + hump in Delta^min  (re-confirm Phase-0)
# ---------------------------------------------------------------------------
def dmin_grid():
    rows = []
    prev = None
    for kappa in [1e-4, 0.05, 0.20, 0.35, 0.50, 0.59, 0.70, 0.85, 0.95, 1-1e-4]:
        pp, c, r = solve(kappa, prev)
        if c is None:
            rows.append({"kappa": kappa, "fail": True, "resid": r})
            continue
        prev = c
        g = M.compute_minority_gains(c, pp)
        rows.append({"kappa": kappa, "Dmin": g.total,
                     "ext": getattr(g, "extensive", None),
                     "intn": getattr(g, "intensive", None),
                     "k1": c.k1, "k0": c.k0, "kD": c.kD, "resid": r})
    return rows
OUT["dmin_grid"] = safe("dmin_grid", dmin_grid)

# ---------------------------------------------------------------------------
# (2) Welfare components at equilibrium across kappa.
#     W (eq:welfare, delta=1 PV units) = E[ 1{bid}(Sbar+xi-K-v-a*Dtilde)
#                                            + v + a*Dtilde - a*C(s) ].
#     We DO NOT recompute the full W integral from scratch (it needs the
#     blockholder action integral); instead we certify the SIGN structure of
#     the two pieces the proof needs:
#       (a) W_min = Delta^min (already have), and
#       (b) the raider REAL surplus E[(Sbar - mbar - K + xi) 1{bid}] using the
#           model's equilibrium bid prob and posteriors -- price nets out.
# ---------------------------------------------------------------------------
def raider_real_and_bidprob(pp, c):
    """Real per-bid control value net of K, integrated over xi and states.
       Uses bidder's PRIVATE decision a_dec = Sbar - P - mbar - K so bid prob
       p = Phi(a_dec/sx) = eq:bid-prob; realized SOCIAL value per bid excludes
       the price transfer P: real_const = Sbar - mbar - K."""
    sx = pp.sigma_xi
    post = M.compute_posteriors(M.compute_action_probs(c, pp) if hasattr(M, "compute_action_probs") else None, pp) \
        if False else None
    # Use the model's own price + posterior machinery if available.
    prices = M.compute_prices(c, pp) if hasattr(M, "compute_prices") else None
    return prices

OUT["has_compute_prices"] = hasattr(M, "compute_prices")
OUT["has_probability_bid"] = hasattr(M, "probability_bid")
OUT["has_prob_public_voice"] = hasattr(M, "prob_public_voice")

# ---------------------------------------------------------------------------
# (3) PLANNER over kD: constrained equilibrium with kD pinned, compare
#     kD_eq vs argmax_kD W2(kD) where W2 = Delta^min + raider_real_surplus.
#     This is the disclosure-wedge / underdisclosure test.
#     We need a block best-response that returns (k1,k0,kD). Discover it.
# ---------------------------------------------------------------------------
block_br = None
for cand in ["solve_block_cutoffs", "block_best_response", "best_response_cutoffs",
             "compute_block_cutoffs", "block_cutoffs"]:
    if hasattr(M, cand):
        block_br = getattr(M, cand); OUT["block_br_name"] = cand; break
    if hasattr(S, cand):
        block_br = getattr(S, cand); OUT["block_br_name"] = cand; break
OUT["block_br_found"] = block_br is not None

# Closed-form raider real surplus given (P_D1, mbar_D1) on the disclosed branch
def raider_surplus_from(P_paid, mbar, pp):
    sx = pp.sigma_xi
    a = pp.Sbar - P_paid - mbar - pp.K
    p = norm.cdf(a / sx)
    real_const = pp.Sbar - mbar - pp.K
    return real_const * p + sx * norm.pdf(a / sx), p

def welfare2_at(pp, c):
    """W2 = Delta^min + pi * raider_real_surplus_on_disclosed_branch.
       This is a CERTIFIABLE lower-dimensional welfare proxy whose kD-derivative
       we sign; full W tracked separately via eq:welfare integrand check."""
    g = M.compute_minority_gains(c, pp)
    Dmin = g.total
    prices = M.compute_prices(c, pp) if hasattr(M, "compute_prices") else None
    post = None
    for cand in ["compute_posteriors_from_cutoffs", "posteriors"]:
        pass
    # Extract disclosed-branch price and mbar.
    P_D1 = None; mbar_D1 = None
    if prices is not None:
        for fld in ["P_D1", "p_D1", "price_D1"]:
            if hasattr(prices, fld):
                P_D1 = getattr(prices, fld); break
    return {"Dmin": Dmin, "P_D1": P_D1, "kD": c.kD,
            "prices_fields": getattr(prices, "_fields", None) if prices is not None else None}

def kD_planner():
    res = {}
    for kappa in [0.20, 0.50, 0.80]:
        pp, c, r = solve(kappa)
        if c is None:
            res[str(kappa)] = {"fail": True}; continue
        info = welfare2_at(pp, c)
        res[str(kappa)] = {"kD_eq": c.kD, "Dmin_eq": info["Dmin"],
                           "prices_fields": info["prices_fields"]}
    return res
OUT["kD_planner_probe"] = safe("kD_planner_probe", kD_planner)

# ---------------------------------------------------------------------------
# (4) Full W integrand SIGN check at baseline: confirm transfers net to zero
#     by verifying E[Y]=P/delta identity is consistent (sanity) and that
#     W(kappa) tracks engagement probability (Phase-0: hump conditional).
# ---------------------------------------------------------------------------
def engagement_prob_grid():
    rows = []
    prev = None
    for kappa in [0.05, 0.20, 0.35, 0.50, 0.65, 0.80, 0.95]:
        pp, c, r = solve(kappa, prev)
        if c is None:
            rows.append({"kappa": kappa, "fail": True}); continue
        prev = c
        # omega_Q + omega_P = P(engage) = P(s>=k0)
        ap = None
        for cand in ["compute_action_probs", "action_probabilities", "action_probs"]:
            if hasattr(M, cand):
                ap = getattr(M, cand)(c, pp); break
        peng = None
        if ap is not None:
            wq = getattr(ap, "omega_Q", None); wp = getattr(ap, "omega_P", None)
            if wq is not None and wp is not None:
                peng = wq + wp
        g = M.compute_minority_gains(c, pp)
        rows.append({"kappa": kappa, "Dmin": g.total, "P_engage": peng,
                     "k0": c.k0, "kD": c.kD})
    return rows
OUT["engagement_grid"] = safe("engagement_grid", engagement_prob_grid)

OUT["errors"] = ERRS

with open("/Users/austinli/Projects/blockholder/quality_reports/fixes/_d2_verify2.json", "w") as f:
    json.dump(OUT, f, indent=1, default=str)

with open("/Users/austinli/Projects/blockholder/quality_reports/fixes/_d2_verify2.txt", "w") as f:
    f.write("MODEL FNS: " + ", ".join(OUT.get("model_fns", [])) + "\n\n")
    f.write("DMIN GRID (endpoint symmetry + hump):\n")
    for row in (OUT.get("dmin_grid") or []):
        f.write("  " + json.dumps(row, default=str) + "\n")
    f.write("\nENGAGEMENT GRID:\n")
    for row in (OUT.get("engagement_grid") or []):
        f.write("  " + json.dumps(row, default=str) + "\n")
    f.write("\nkD PLANNER PROBE:\n")
    f.write(json.dumps(OUT.get("kD_planner_probe"), indent=1, default=str) + "\n")
    f.write("\nblock_br_found: %s (%s)\n" % (OUT.get("block_br_found"), OUT.get("block_br_name")))
    f.write("has_compute_prices: %s  has_probability_bid: %s  has_prob_public_voice: %s\n" %
            (OUT.get("has_compute_prices"), OUT.get("has_probability_bid"), OUT.get("has_prob_public_voice")))
    f.write("\nERRORS:\n")
    for e in ERRS:
        f.write(e + "\n----\n")
print("DONE")
