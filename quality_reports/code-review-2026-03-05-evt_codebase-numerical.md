# Code Review
Target: `evt_codebase/numerical/*.py`
Date: 2026-03-05

## Summary

- Critical: 0
- Major: 0
- Minor: 3
- Suggestions: 4

The core theory implementation in `model.py` is internally consistent (feed-forward pricing, δ-discounted prices, closed-form posteriors matching Proposition 2, and exact minority-gains decomposition in the exported baseline series). The main correctness risk I found was solver behavior under region collapse; that has been fixed by making the `k_D` step compare PUBLIC against `max(HOLD, QUIET)`.

## Findings

### Minor

1. `evt_codebase/numerical/solver.py`: region-collapse robustness (fixed)
   - Location: `solve_equilibrium` step “3) kD …” and `equilibrium_residual` kD residual.
   - Issue: previously hard-coded `lower_action=QUIET` in practice, which is not correct when the Quiet Voice region collapses (kD≈k0). This could select the wrong boundary condition.
   - Fix: now uses `max(U(HOLD), U(QUIET))` vs `U(PUBLIC)` for the kD condition.

2. `evt_codebase/numerical/figures.py`: price figure legend clarity
   - Location: `fig_prices`.
   - Issue: earlier plots had no bar legend and no posterior annotations while the paper caption claimed otherwise.
   - Fix: added bar legend + π annotations; still worth checking for crowding if you later add more states.

3. `evt_codebase/numerical/export_data.py`: sensitivity grids are hard-coded
   - Location: `export_sensitivity_*` helpers.
   - Issue: hard-coded grids make it easy for calibration edits (e.g., baseline `m1`) to silently desync from sensitivity panels.
   - Mitigation: wedge grid was recentered to include baseline; consider centralizing all sweep values in one config block.

### Suggestions

1. Add a lightweight `numerical/tests_smoke.py` (or pytest) that asserts:
   - `max|delta_min-(base+act)| < 1e-8` on `baseline_series.csv`.
   - `P_trade(X)=sum_d P(D=d|X)P_post(X,d)` for all X on-path.
   - κ-invariance of disclosed objects (`E[v|X,1]`, `π(X,1)`, etc.) under fixed cutoffs.

2. Expose sensitivity sweep values in a single place (e.g., `params.py` constants or an `export_config.py`) so paper-calibration changes cannot drift.

3. In `fig_prices`, consider nudging π labels slightly above bar tops (e.g., `y=p_post+0.01`) to avoid overlap when bars and markers are close.

4. Consider logging a one-line residual summary in `export_data.py` when a sensitivity point is marked `NA` to ease diagnosing pathological parameter sets.
