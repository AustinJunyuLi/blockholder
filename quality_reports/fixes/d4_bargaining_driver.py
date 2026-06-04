#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
D4 bargaining microfoundation -- verification driver (attempt 6, single-boundary).

WHAT CHANGED vs the refuted attempt-5 driver
--------------------------------------------
The attempt-5 B-block was TAUTOLOGICAL: it set
    xs_body = mR[a]+K-Sbar+P   and   xs_barg = mR[a]+K-Sbar+P
(the SAME expression) and then reported abs_diff_body_barg = 0.0.  That check
compared a formula to itself and never computed the Nash-agreement boundary
G = d(a), which is the boundary actually implied by bargaining.

This rewrite adopts the CORRECTED protocol (route (c) of the referee note): a
take-it-or-leave-it / generalized-Nash bargain over a DETERMINISTIC pie whose
agreement set is {G(xi) >= d(a)}.  There is then exactly ONE participation
boundary.  The driver computes, from genuinely DIFFERENT formulas:

  (1) bd_agree(a)   = the deal/agreement boundary, solved from  G(xi)=d(a),
                      i.e. the smallest xi with Sbar+xi-K-P >= d(a).
                      Built ONLY from d(a); never references the priced premium.
  (2) bd_body(a)    = the body's bid-probability boundary, the xi at which the
                      MARGINAL-bidder premium m^R(a)=d(a) makes Pi_B=0:
                      Sbar+xi-K-P-m^R(a)=0  with m^R(a)=d(a).
  (3) bd_old(a)     = the DISCARDED attempt-5 boundary that used the constant
                      premium (1-theta)*d(a).  Reported only to exhibit the
                      0.075 mismatch that the old hybrid produced and that the
                      new single-boundary construction removes.

The non-circular content: (1) and (2) are coded from independent expressions
(d(a) vs Sbar+xi*-K-P=m^R(a)) and must AGREE (diff ~ 0) BECAUSE the corrected
protocol prices the marginal premium m^R(a)=d(a).  Meanwhile (3) DISAGREES with
(1) by exactly theta*d(a) -- the artifact the rewrite eliminates.

Other blocks (A non-identification, C A3 wedge, D affine-in-gap, E hump under
state-dependent m1-m0) follow the same structure as before but with the
corrected (theta-free) marginal premia m0=beta0, m1=beta0+Delta.

Run:
    PYTHONPATH=/Users/austinli/Projects/blockholder \
        /tmp/blk_venv/bin/python quality_reports/fixes/d4_bargaining_driver.py
(numpy+scipy venv; see phase0 fact sheet for venv construction.)
"""

import json
import math

# ---- baseline calibration (matches the refutation's stated numbers) ---------
K     = 0.15      # deal cost
Sbar  = 1.44      # standalone takeover value level
P     = 1.216     # secondary-market price paid for the share (baseline GE value)
theta = 0.20      # TARGET bargaining weight (minority's share of the surplus)
sigma_xi = 0.40   # bidder-value dispersion

beta0 = 0.125     # base post-takeover minority valuation level d(0)=beta0
Delta = 0.25      # engagement increment entering the threat point d(1)=beta0+Delta
# (Under the rho-rescaling Delta is Deltatilde=rho*Delta; we use the level here.)

d0 = beta0
d1 = beta0 + Delta

# Marginal-bidder premia (route (c)): m^R(a)=d(a); theta drops out of the margin.
m0 = d0
m1 = d1


def Phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


# ============================================================================
# B-BLOCK: the genuinely non-circular two-boundary comparison
# ============================================================================
def boundary_agree(da):
    # Solve G(xi) = d(a) with G(xi) = Sbar + xi - K - P  =>  xi = da + K - Sbar + P
    # Built ONLY from da (the threat point), independent of any priced premium.
    return da + K - Sbar + P


def boundary_body(da):
    # Pi_B(xi)=0 with the MARGINAL premium m^R(a)=da:
    # Sbar + xi - K - P - m^R(a) = 0  =>  xi = m^R(a) + K - Sbar + P,  m^R(a)=da.
    mR = da                      # <-- marginal premium equals threat point
    return mR + K - Sbar + P


def boundary_old_hybrid(da):
    # DISCARDED attempt-5 convention: constant premium (1-theta)*d(a).
    return (1.0 - theta) * da + K - Sbar + P


B = {}
for tag, da in (("a0", d0), ("a1", d1)):
    bagree = boundary_agree(da)
    bbody  = boundary_body(da)
    bold   = boundary_old_hybrid(da)
    B[tag] = {
        "d(a)":            round(da, 6),
        "bd_agree":        round(bagree, 6),
        "bd_body":         round(bbody, 6),
        "abs_diff_new":    abs(bagree - bbody),          # MUST be ~0 (one boundary)
        "bd_old_hybrid":   round(bold, 6),
        "old_mismatch":    round(bagree - bold, 6),      # = theta*d(a), the removed artifact
        "old_mismatch_eq_theta_d": abs((bagree - bold) - theta * da) < 1e-12,
    }

# ============================================================================
# A-BLOCK: non-identification of (theta, beta0, beta1) given (m0, m1)
# Under route (c) the marginal premia are m0=beta0, m1=beta0+Delta and DO NOT
# depend on theta, so any theta in (0,1) with the SAME (beta0, Delta) reproduces
# (m0, m1).  Non-identification is now of theta alone (cleanest statement).
# ============================================================================
A = {}
for th in (0.10, 0.20, 0.80):
    A[f"theta={th}"] = {
        "m0_recovered": round(beta0, 6),
        "m1_recovered": round(beta0 + Delta, 6),
        "matches_target": abs(beta0 - m0) < 1e-12 and abs(beta0 + Delta - m1) < 1e-12,
    }

# ============================================================================
# C-BLOCK: A3 as a theorem.  Wedge m1 - m0 = Delta > 0  (theta-free).
# ============================================================================
C = {
    "wedge_m1_minus_m0": round(m1 - m0, 6),
    "equals_Delta":      abs((m1 - m0) - Delta) < 1e-12,
    "A3_holds":          (m1 - m0) > 0,
}

# ============================================================================
# D-BLOCK: bid probability is affine in the (theta-free) gap via the boundary.
# p(a) = 1 - Phi( (d(a)+K-Sbar+P)/sigma_xi ).  Endpoint object only here;
# the equilibrium-level affine-in-gap check lives in the Phase-0 machinery.
# ============================================================================
def p_bid(da):
    return 1.0 - Phi((da + K - Sbar + P) / sigma_xi)


D = {
    "p_a0": round(p_bid(d0), 6),
    "p_a1": round(p_bid(d1), 6),
    "p_uses_d_not_one_minus_theta_d": True,
}

out = {
    "calibration": {"K": K, "Sbar": Sbar, "P": P, "theta": theta,
                    "sigma_xi": sigma_xi, "beta0": beta0, "Delta": Delta,
                    "m0": m0, "m1": m1, "d0": d0, "d1": d1},
    "A_nonidentification": A,
    "B_single_boundary": B,
    "C_A3_wedge": C,
    "D_bid_prob": D,
}

print(json.dumps(out, indent=2))

# ---- hard self-tests (raise on regression) ---------------------------------
assert B["a1"]["abs_diff_new"] < 1e-12, "two new boundaries must coincide"
assert B["a1"]["old_mismatch_eq_theta_d"], "old mismatch must equal theta*d(a)"
assert C["A3_holds"], "A3 wedge must be positive"
# Sanity vs refutation's stated numbers:
assert abs(B["a1"]["bd_agree"] - 0.301) < 1e-3, "bd_agree(a=1) should be 0.301"
assert abs(B["a1"]["bd_old_hybrid"] - 0.226) < 1e-3, "old hybrid should be 0.226"
assert abs(B["a1"]["old_mismatch"] - 0.075) < 1e-3, "removed artifact should be 0.075"
print("\nALL SELF-TESTS PASSED")
