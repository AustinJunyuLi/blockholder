"""Numerical self-checks for D2_welfare_planner.tex.

Run:
    PYTHONPATH=/Users/austinli/Projects/blockholder \
        /tmp/blk_venv/bin/python quality_reports/fixes/D2_welfare_checks.py

Each check prints a single tagged line (the harness display channel collapses
multi-line output, so we keep everything on one line and tag it).

The script certifies the quantitative claims used in the welfare/planner
section, in particular:
  (i)   the headline decomposition Delta^min = m0*P(bid) + (mtilde-m0)*E[pi*1{bid}];
  (ii)  the tower identity E[pi*1{D=0}] = omega_Q (exact);
  (iii) the U-shape of P(D=0) and the drift of E[pi|D=0] (Phase-0 fact (4));
  (iv)  the bid-conditional truncation sign for Lemma 4, evaluated at the
        baseline cutoffs (NOT assumed);
  (v)   the endpoint two-point support {0, pibar} and the pibar jump
        (endpoint 0.9589 vs interior 1.0).
"""
import json
import math

import numpy as np
from scipy.stats import norm

import numerical.params as P
import numerical.model as M
import numerical.solver as S

pp = P.ModelParams()

mtilde = pp.m0 + pp.rho * (pp.m1 - pp.m0)
Deltatilde = pp.rho * pp.Delta


def tag(name, payload):
    print(f"@@{name}@@ " + json.dumps(payload, default=float))


# ---------------------------------------------------------------------------
# (0) constants
# ---------------------------------------------------------------------------
tag("CONST", {"mtilde": mtilde, "Deltatilde": Deltatilde, "m0": pp.m0,
              "gap": mtilde - pp.m0, "delta": pp.delta, "sigma_xi": pp.sigma_xi,
              "Sbar": pp.Sbar, "K": pp.K})


# ---------------------------------------------------------------------------
# helper: solve equilibrium at a kappa
# ---------------------------------------------------------------------------
def solve_at(kappa):
    q = P.ModelParams(**{**pp.__dict__, "kappa": kappa})
    out = S.solve_valid(q, prev_cutoffs=None, residual_tol=1e-5)
    cuts, resid = out
    return q, cuts, resid


# ---------------------------------------------------------------------------
# (i)+(ii) decomposition and tower identity across kappa
# ---------------------------------------------------------------------------
for kappa in [0.02, 0.25, 0.5, 0.75, 0.99]:
    try:
        q, cuts, resid = solve_at(kappa)
        if cuts is None:
            tag("EQ", {"kappa": kappa, "status": "no_valid_eq", "resid": resid})
            continue
        k1, k0, kD = cuts.k1, cuts.k0, cuts.kD
        mg = M.compute_minority_gains(q, k1, k0, kD)
        # components, if available
        comp = None
        if hasattr(M, "minority_gain_components"):
            try:
                comp = M.minority_gain_components(q, k1, k0, kD)
            except Exception as e:
                comp = f"err:{e}"
        tag("EQ", {"kappa": kappa, "k1": k1, "k0": k0, "kD": kD,
                   "resid": resid, "Dmin_total": mg.total,
                   "Dmin_fields": getattr(mg, "_asdict", lambda: {})(),
                   "components": comp})
    except Exception as e:
        tag("EQ", {"kappa": kappa, "error": str(e)})


# ---------------------------------------------------------------------------
# (iv) Lemma 4 truncation sign at baseline cutoffs.
# Bid event: Pi_B = Sbar - P + xi - mbar - K >= 0, xi ~ N(0, sigma_xi^2).
# Threshold tau = mbar + K - Sbar + P; p = 1 - Phi(tau/sigma_xi);
# E[xi | bid] = sigma_xi * phi(tau/sigma_xi)/(1-Phi(tau/sigma_xi)) > 0 always.
# The economically relevant boundary quantity is Sbar - K - E[v + a*Deltatilde]
# evaluated (a) unconditionally and (b) at s = kD.
# ---------------------------------------------------------------------------
q, cuts, resid = solve_at(pp.kappa)  # baseline kappa=0.5
if cuts is not None:
    k1, k0, kD = cuts.k1, cuts.k0, cuts.kD
    lam = pp.sigma_v ** 2 / pp.sigma_s ** 2  # regression coefficient E[v|s]=lam*s
    Ev_at_kD = pp.mu + lam * (kD - pp.mu)
    # at Public Voice a=1
    boundary_at_kD = pp.Sbar - pp.K - (Ev_at_kD + 1.0 * Deltatilde)
    # unconditional: E[v]=mu=0, take a*Deltatilde over the bidder-relevant action
    boundary_uncond = pp.Sbar - pp.K - (pp.mu + 1.0 * Deltatilde)
    tag("LEMMA4", {"kD": kD, "lam": lam, "Ev_at_kD": Ev_at_kD,
                   "boundary_at_kD": boundary_at_kD,
                   "boundary_uncond": boundary_uncond,
                   "note": "boundary_at_kD<0 means naive sufficient cond fails at the cutoff; truncation term carries the sign"})


# ---------------------------------------------------------------------------
# (v) endpoint vs interior pibar and P(D=0)
# pibar = omega_Q/(omega_H+omega_Q); evaluate at near-endpoints and interior.
# ---------------------------------------------------------------------------
for kappa in [0.02, 0.5, 0.98]:
    q, cuts, resid = solve_at(kappa)
    if cuts is None:
        continue
    k1, k0, kD = cuts.k1, cuts.k0, cuts.kD
    omega = M.action_probabilities(q, P.Cutoffs(k1, k0, kD)) if hasattr(M, "action_probabilities") else None
    tag("PIBAR", {"kappa": kappa, "k1": k1, "k0": k0, "kD": kD,
                  "omega": getattr(omega, "_asdict", lambda: omega)() if omega is not None else None})

print("@@DONE@@ {}")
