#!/usr/bin/env python3
"""
D3_prop8_IFT_check.py  --  LIVE self-check for D3_prop8_IFT.tex (attempt 3).

This RE-SOLVES the model with the paper's own solver and recomputes the
reduced Jacobian by central differences -- it does NOT hard-code (a,b,c,d).

Run:
  PYTHONPATH=/Users/austinli/Projects/blockholder \
    /tmp/blk_venv/bin/python quality_reports/fixes/D3_prop8_IFT_check.py

Writes _D3_check_result.json next to this file and prints PASS/FAIL lines.

Verifies, against the paper's OWN solver:
  (1) Hold collapses; baseline equilibrium (k,k,kD).
  (2) Reduced 2x2 Jacobian J=[[a,b],[c,d]] of reduced_T, with c<0 (NEGATIVE)
      and det J = ad - bc ~ 0.0752 (NOT the refuted 0.071022).
  (3) IFT cofactor routing: dk/dtheta uses +b/det, dkD/dtheta uses -a/det,
      both > 0 since a<0,b>0,det>0.
  (4) MinorityGains component k_D-derivatives:
      d(total)/dkD<0, d(base)/dkD<0, d(activism)/dkD>0  (so the +6.26e-4
      activism slope must NOT be labelled 'deterrence <=0').
  (5) ModelParams has NO theta field and K is scalar (theta is analytic-only).
"""
import json, os
import numpy as np

from numerical.params import ModelParams, Action
from numerical import solver, model

OUT = {}
base = ModelParams()

# ---- (5) theta is not in the codebase ----------------------------------
OUT["modelparams_fields"] = list(base.__dataclass_fields__.keys())
OUT["has_theta"] = hasattr(base, "theta")
OUT["K_is_scalar"] = isinstance(base.K, (int, float))

# ---- (1) baseline equilibrium ------------------------------------------
cuts0, r0 = solver.solve_valid(base, prev_cutoffs=None, residual_tol=1e-5)
k1b, k0b, kDb = cuts0
kb = 0.5 * (k1b + k0b)
OUT["equilibrium"] = dict(k1=float(k1b), k0=float(k0b), kD=float(kDb),
                          resid=float(r0))
OUT["hold_collapses"] = bool(abs(k1b - k0b) < 1e-3)

# ---- reduced residual T=(T1,TD), Hold collapsed -------------------------
def reduced_T(k, kD):
    oE, oH, oQ, oP = model.compute_action_probabilities(k, k, kD, base)
    post = model.compute_posteriors(oE, oH, oQ, oP, base.kappa)
    prices = model.compute_equilibrium_prices(k, k, kD, base)
    U = lambda a, s: model.compute_expected_payoff(a, float(s), prices, post, base)
    T1 = U(Action.EXIT, k) - U(Action.QUIET, k)   # EXIT=QUIET binds at k
    TD = U(Action.QUIET, kD) - U(Action.PUBLIC, kD)
    return np.array([T1, TD])

# ---- (2) reduced Jacobian via central differences -----------------------
def jac(h):
    dTdk  = (reduced_T(kb + h, kDb) - reduced_T(kb - h, kDb)) / (2 * h)
    dTdkD = (reduced_T(kb, kDb + h) - reduced_T(kb, kDb - h)) / (2 * h)
    J = np.column_stack([dTdk, dTdkD])
    a, b, c, d = J[0, 0], J[0, 1], J[1, 0], J[1, 1]
    return dict(a=float(a), b=float(b), c=float(c), d=float(d),
                det=float(a * d - b * c))

OUT["jacobian_by_h"] = {f"{h:.0e}": jac(h) for h in (1e-3, 1e-4, 1e-5, 1e-6)}
J = OUT["jacobian_by_h"]["1e-04"]
a, b, c, d, det = J["a"], J["b"], J["c"], J["d"], J["det"]

OUT["checks"] = {}
OUT["checks"]["c_negative"] = bool(c < 0)
OUT["checks"]["det_pos"] = bool(det > 0)
OUT["checks"]["det_near_0752"] = bool(abs(det - 0.0752) < 5e-3)
OUT["checks"]["det_not_071022"] = bool(abs(det - 0.071022) > 1e-3)
OUT["checks"]["a_neg"] = bool(a < 0)
OUT["checks"]["b_pos"] = bool(b > 0)
OUT["checks"]["d_neg"] = bool(d < 0)
OUT["checks"]["diag_dom_a"] = bool(abs(a) > abs(b))
OUT["checks"]["diag_dom_d"] = bool(abs(d) > abs(c))

# ---- (3) cofactor routing (theta enters only TD, dTD>0) -----------------
OUT["routing"] = dict(coef_dk_dtheta=float(b / det),
                      coef_dkD_dtheta=float(-a / det))
OUT["checks"]["dk_dtheta_pos"] = bool((b / det) > 0)
OUT["checks"]["dkD_dtheta_pos"] = bool((-a / det) > 0)

# ---- (4) MinorityGains component k_D-derivatives ------------------------
def minority_components(k, kD):
    mg = model.compute_minority_gains(k, k, kD, base)
    return dict(total=float(mg.total), base=float(mg.base),
                activism=float(mg.activism))

h = 1e-4
mp = minority_components(kb, kDb + h)
mm = minority_components(kb, kDb - h)
dmg = {key: (mp[key] - mm[key]) / (2 * h)
       for key in ("total", "base", "activism")}
OUT["minority_dkD"] = {k: float(v) for k, v in dmg.items()}
OUT["checks"]["dtotal_dkD_neg"] = bool(dmg["total"] < 0)
OUT["checks"]["dbase_dkD_neg"] = bool(dmg["base"] < 0)
OUT["checks"]["dactivism_dkD_pos"] = bool(dmg["activism"] > 0)

allpass = all(OUT["checks"].values())
OUT["ALL_PASS"] = bool(allpass)

resdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(resdir, "_D3_check_result.json"), "w") as fh:
    json.dump(OUT, fh, indent=2)

print("=== D3 LIVE self-check (re-solves model) ===")
print("theta in codebase:", OUT["has_theta"], " K scalar:", OUT["K_is_scalar"])
print(f"equilibrium k={kb:.6f} kD={kDb:.6f} resid={r0:.2e} "
      f"holdcollapse={OUT['hold_collapses']}")
print(f"Jacobian(h=1e-4): a={a:.5f} b={b:.5f} c={c:.5f} d={d:.5f} det={det:.6f}")
print(f"  c across h: " + ", ".join(
    f"{hh}={OUT['jacobian_by_h'][hh]['c']:.5f}"
    for hh in OUT['jacobian_by_h']))
print(f"  det across h: " + ", ".join(
    f"{hh}={OUT['jacobian_by_h'][hh]['det']:.6f}"
    for hh in OUT['jacobian_by_h']))
print(f"routing: dk/dtheta coef=+b/det={b/det:.4f}  "
      f"dkD/dtheta coef=-a/det={-a/det:.4f}")
for kk, v in OUT["checks"].items():
    print(f"  [{'PASS' if v else 'FAIL'}] {kk}")
print("minority d/dkD:", {k: round(v, 6) for k, v in dmg.items()})
print("ALL_PASS =", allpass)
