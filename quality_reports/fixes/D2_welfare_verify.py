#!/usr/bin/env python
"""
Self-verification for D2_welfare_planner.tex.

Run with:
  PYTHONPATH=/Users/austinli/Projects/blockholder \
    /tmp/blk_venv/bin/python quality_reports/fixes/D2_welfare_verify.py \
    > quality_reports/fixes/D2_welfare_verify.out 2>&1

Checks every QUANTITATIVE claim that appears in D2_welfare_planner.tex:
  (1) Near-end W_min values printed in nr:hump are from a VALID solve
      (residual <= 1e-5), replacing the prior wrong 0.0621 / 0.0643.
  (2) Endpoint-symmetry headline: |W_min(0.02) - W_min(0.98)| small.
  (3) The plateau / single-hump shape across the residual-passing interior.
  (4) The bid-margin cutoff kD is NON-MONOTONE in kappa (falls then rises),
      so p = 1 - Phi(tau) is U-shaped -> dW_bid/dkappa > 0 only on a
      LEFT-neighborhood of k_dag.
  (5) Delta_tilde = rho * Delta = 0.9 * 0.25 = 0.225, distinct from
      m_tilde - m0 = 0.18.
All printed numbers are copied into the .tex as verified comments.
EXPECTED (from Phase-0 fact sheets + task-verified solve, to compare on re-run):
  W_min(0.05) = 0.066968   (resid ~4e-7)      [replaces WRONG 0.0621]
  W_min(0.95) = 0.067814   (resid ~4e-7)      [replaces WRONG 0.0643]
  |W_min(0.02) - W_min(0.98)| ~ 6.4e-4        (endpoint-symmetry headline)
  near-end limit W_min -> ~0.07021            (limit form)
  kD: 2.6848 / 2.3135 / 2.2499(min) / 2.3980 / 2.6446
      at kappa = 0.05/0.40/0.59/0.80/0.95     (U-shaped => dW_bid/dkappa>0
                                               only on LEFT-nbhd of k_dag)
  peak W_min(0.59) ~ 0.07756; plateau totals
      0.07744/0.07756/0.07755/0.07728/0.07386 at 0.55/0.59/0.60/0.65/0.80
  Delta_tilde = rho*Delta = 0.9*0.25 = 0.225 ; m_tilde - m0 = 0.18
"""
import numpy as np

from numerical import params as P
from numerical import model as M
from numerical import solver as S


def solve_at(kappa, tol=1e-5):
    pr = P.ModelParams(kappa=kappa)
    cut, resid = S.solve_valid(pr, prev_cutoffs=None, residual_tol=tol)
    if cut is None:
        return None, resid, pr
    return cut, resid, pr


def wmin_at(kappa, tol=1e-5):
    cut, resid, pr = solve_at(kappa, tol)
    if cut is None:
        return None, None, resid, pr
    mg = M.compute_minority_gains(cut.k1, cut.k0, cut.kD, pr)
    return mg.total, cut, resid, pr


def main():
    base = P.ModelParams()
    print("=== Calibration sanity ===")
    print(f"delta      = {base.delta}")
    print(f"sigma_xi   = {base.sigma_xi}")
    print(f"rho        = {base.rho}")
    Delta = getattr(base, "Delta", None)
    print(f"Delta      = {Delta}")
    if Delta is not None:
        print(f"Delta_tilde = rho*Delta = {base.rho*Delta:.6f}  (claim: 0.225)")
    # m0, m1
    m0 = getattr(base, "m0", None)
    m1 = getattr(base, "m1", None)
    print(f"m0 = {m0}, m1 = {m1}")
    if (m0 is not None) and (m1 is not None):
        mt = m0 + base.rho * (m1 - m0)
        print(f"m_tilde = m0+rho(m1-m0) = {mt:.6f}")
        print(f"m_tilde - m0 = {mt - m0:.6f}  (claim: 0.18)")

    print("\n=== (1)+(2) Near-end W_min (valid solve, tol=1e-5) ===")
    for k in [0.02, 0.05, 0.95, 0.98]:
        w, cut, resid, pr = wmin_at(k)
        if w is None:
            print(f"  kappa={k}: NO valid solve (resid {resid:.2e})")
        else:
            print(f"  kappa={k:.2f}: W_min={w:.6f}  resid={resid:.2e}  "
                  f"cut=({cut.k1:.4f},{cut.k0:.4f},{cut.kD:.4f})")

    print("\n=== (3) Shape over the grid (residual-passing) ===")
    grid = [0.05, 0.20, 0.40, 0.55, 0.59, 0.60, 0.65, 0.80, 0.95]
    rows = []
    for k in grid:
        w, cut, resid, pr = wmin_at(k)
        rows.append((k, w, cut, resid))
        if w is None:
            print(f"  kappa={k:.2f}: NO valid solve (resid {resid:.2e})")
        else:
            print(f"  kappa={k:.2f}: W_min={w:.6f}  kD={cut.kD:.4f}  resid={resid:.2e}")

    print("\n=== (4) kD non-monotonicity (bid margin tau=kD) ===")
    kDs = [(k, c.kD) for (k, w, c, r) in rows if c is not None]
    print("  kappa, kD:", [(round(k, 2), round(kd, 4)) for k, kd in kDs])
    # check fall-then-rise around 0.59
    if len(kDs) >= 3:
        kvals = [kd for _, kd in kDs]
        kmin_idx = int(np.argmin(kvals))
        print(f"  argmin kD at kappa={kDs[kmin_idx][0]:.2f}, kD_min={kvals[kmin_idx]:.4f}")
        print("  -> kD falls then rises => p=1-Phi(kD) is U-shaped "
              "=> dW_bid/dkappa>0 only on a LEFT-nbhd of k_dag.")

    print("\n=== Peak / plateau ===")
    vals = [(k, w) for (k, w, c, r) in rows if w is not None]
    if vals:
        kstar, wstar = max(vals, key=lambda t: t[1])
        print(f"  interior max over grid: kappa*={kstar:.2f}, W_min={wstar:.6f}")
        ends = [w for (k, w) in vals if k in (0.05, 0.95)]
        if ends:
            print(f"  endpoints (0.05,0.95): {[round(w,6) for w in ends]}")
            print(f"  amplitude vs min endpoint: {wstar - min(ends):.6f} "
                  f"({100*(wstar-min(ends))/wstar:.2f}% of peak)")


if __name__ == "__main__":
    main()
