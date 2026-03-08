# Claude's Theory-to-Code Audit (2026-03-05)

## Summary
Complete audit of evt_codebase/numerical/ against draft_v3.tex. 12/13 sections MATCH, 1 text error found and fixed.

## Results

| Section | Status |
|---------|--------|
| A. Noise Distribution (P(z=0)=1−2κ/3) | MATCH |
| B. Posteriors (Proposition 2) | MATCH |
| C. Pricing (feed-forward) | MATCH |
| D. Bid Probability | MATCH |
| E. Payoffs (affine structure) | MATCH |
| F. Minority Gains Decomposition | MATCH |
| G. Calibration Parameters | MATCH |
| H. Solver | MATCH |
| I. Paper's Numerical Claims | MISMATCH (fixed) |
| J. Disclosure Comparison | MATCH |
| K. LaTeX Tables | MATCH |
| L. Welfare | MATCH |
| M. Sensitivity Sweep Parameters | MATCH |

## The One Fix Applied
Line 638 of draft_v3.tex had stale values from old m1=0.30 calibration:
- OLD: m̃−m₀ = 0.18, sum = 0.405
- NEW: m̃−m₀ = 0.315, sum = 0.540 (with current m1=0.45)
This was a text-only error — no computation affected. Fixed.

## Calibration Change
m1 was changed from 0.30 to 0.45, which:
- Increased m̃ from 0.28 to 0.415
- Widened the Quiet Voice region from 0.015 to 0.184 σ_s units
- Made the hump shape significantly more visible
- A5 condition still satisfied: 0.540 > 0.30

## Baseline Equilibrium (current calibration)
- k1 = 0.4345, k0 = 1.1783, kD = 1.3622
- σ_s = 0.7071
- QV region width = 0.184
- Equilibrium residual = 2.31e-8
- Hump peak at κ ≈ 0.356

## Known Issue: Solver Collapsed-Regime Handling
When k0 ≈ kD (Quiet Voice collapses at high κ), the equilibrium_residual function (solver.py lines 72-75) uses a one-sided check:
```python
rD = max(0.0, U(lower_action, s_test) - U(Action.PUBLIC, s_test))
```
This only penalizes if HOLD/QUIET dominates PUBLIC, but does NOT catch cases where PUBLIC dominates (the cutoff should be lower). This may cause a kink in the nonmonotone figure at the QV collapse point and occasional solver failures at extreme κ.
