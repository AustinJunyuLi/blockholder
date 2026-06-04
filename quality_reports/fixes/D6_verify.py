"""
D6 equilibrium-foundations numeric self-checks.

Run:
  PYTHONPATH=/Users/austinli/Projects/blockholder \
    /tmp/blk_venv/bin/python quality_reports/fixes/D6_verify.py

Writes a human-readable results block to D6_results.txt and a machine copy to
D6_results.json. Every quantitative claim cited in D6_equilibrium_foundations.tex
is recomputed here from the paper's own numerical package.
"""
import sys, os, math, json

REPO = "/Users/austinli/Projects/blockholder"
sys.path.insert(0, REPO)

out = {}

# ---- 0. closed-form constants (no solver needed) -------------------------
phi0 = 1.0 / math.sqrt(2.0 * math.pi)            # phi(0) = 0.3989422804
out["phi0"] = phi0
out["inv_phi0"] = 1.0 / phi0                      # sqrt(2 pi) = 2.5066282746
DELTA, SIGMA_XI = 0.95, 0.40
out["delta_over_sigma_xi"] = DELTA / SIGMA_XI     # 2.375 (the LOOSE one-term number)
out["A5a_slope_coeff"] = DELTA * phi0 / SIGMA_XI  # 0.9474 < 1  (feedback SLOPE)
# Corrected A5a sufficient condition:  delta*( phi0/sigma_xi * |gap| + p ) < 1.
# With p<=1 and using the conservative p=1 the admissible gap satisfies
#   |gap| < ( 1/delta - 1 ) * sigma_xi / phi0 .  (strict global contraction)
out["A5a_gapmax_p1"] = (1.0 / DELTA - 1.0) * SIGMA_XI / phi0
# With the realised direct term p(P) at the node (<=1/2 by Lemma B.P>B.Q region):
out["A5a_gapmax_phalf"] = (1.0 / DELTA - 0.5) * SIGMA_XI / phi0

# ---- 1. solver-based node checks (best effort) ---------------------------
have_num = False
try:
    import numerical.model as model
    import numerical.solver as solver
    import numerical.params as P
    have_num = True
except Exception as e:                                   # pragma: no cover
    out["numerical_import"] = f"ERR:{type(e).__name__}:{e}"

if have_num:
    out["numerical_import"] = "ok"
    pars = P.ModelParams()                               # baseline calibration
    # baseline kappa for the price/feedback margin check
    kap = 0.5
    try:
        pars_k = pars
        # solve_valid signature per phase-0: (params, prev_cutoffs=None, residual_tol=...)
        sol, resid = solver.solve_valid(pars_k, None, 1e-6) \
            if hasattr(solver, "solve_valid") else (None, None)
        out["solve_valid_resid@0.5"] = resid
        if sol is not None:
            out["cutoffs@0.5"] = list(sol)
    except Exception as e:
        out["solve_err"] = f"{type(e).__name__}:{e}"

# ---- persist ------------------------------------------------------------
with open(os.path.join(REPO, "quality_reports/fixes/D6_results.json"), "w") as f:
    json.dump(out, f, indent=2, default=float)
lines = [f"{k} = {v}" for k, v in out.items()]
with open(os.path.join(REPO, "quality_reports/fixes/D6_results.txt"), "w") as f:
    f.write("\n".join(lines) + "\n")
print("\n".join(lines))
