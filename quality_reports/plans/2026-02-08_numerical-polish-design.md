# Plan: Polish Numerical Code
**Date:** 2026-02-08
**Status:** APPROVED

## Task Description
Comprehensive polish of `numerical.py` across three dimensions:
1. **Figure aesthetics** — grayscale-friendly, PDF output, publication-quality styling
2. **Theory-code mapping** — docstrings linking to paper equations/propositions, section headers matching paper structure
3. **Code quality / DRY** — eliminate duplication, split into modules, add type safety

## Files to Create/Modify

### New module structure: `numerical/`
- `numerical/__init__.py` — Package exports
- `numerical/params.py` — `ModelParams` dataclass + `replace()`, calibration presets, named tolerances
- `numerical/model.py` — Core economic model (posteriors, prices, payoffs, minority gains)
- `numerical/solver.py` — Equilibrium solver, `solve_valid`, `compute_series_over_kappa`
- `numerical/figures.py` — All plotting + LaTeX table generation, shared style config
- `run_numerical.py` — Entry point replacing `python numerical.py`

### Files to remove after migration
- `numerical.py` — replaced by the package

## Approach

### 1. Module Split
- Extract `ModelParams` + tolerances → `params.py`
  - Add `replace(**overrides)` via `dataclasses.replace()`
  - Add calibration presets as class methods: `ModelParams.baseline()`, etc.
  - Define named tolerance constants: `TOL_PROB`, `TOL_CONVERGE`, `TOL_RESIDUAL`, `TOL_REGION`
- Extract economic functions → `model.py`
  - `engagement_cost`, `v_hat`, `compute_action_probabilities`, `compute_conditional_means`
  - `compute_posteriors`, `compute_E_v_given_XD`, `bid_probability`, `solve_price_fixed_point`
  - `compute_equilibrium_prices`, `compute_expected_payoff`
  - `compute_minority_gains`, `compute_minority_gains_no_disclosure_given_strategy`
  - All counterfactual posterior functions (no-disclosure, full-info, noisy-rumor)
  - All premium-wedge functions
- Extract solver → `solver.py`
  - `equilibrium_residual`, `solve_equilibrium`, `solve_valid` (defined ONCE)
  - `solve_equilibrium_for_kappa`, `compute_series_over_kappa`
- Extract plotting → `figures.py`
  - All `plot_*` functions + `write_*_table` functions
  - Shared style config at top: `STYLES`, `configure_matplotlib()`
  - `generate_all_figures()` orchestrator function

### 2. Theory-Code Mapping
- `ModelParams` docstring: mini notation table linking each param to paper equation
- Every function docstring: "Implements Equation (N)" or "Implements Proposition N"
- Section headers in each module: `# -- Section 3: Market Microstructure --`
- `Action` enum: `EXIT`, `HOLD`, `QUIET`, `PUBLIC` replacing string dispatch
- `Cutoffs` and `MinorityGains` NamedTuples replacing bare tuples

### 3. Figure Aesthetics (Grayscale-Friendly)
- Line differentiation: line style + marker shape + color (three channels)
- Style dict: `STYLES` mapping action/series to `(color, ls, marker)`
- Font: Computer Modern serif, `text.usetex: True`
- Axes: no top/right spines, light grid alpha=0.15
- Figure size: `(5.5, 3.8)` single-column journal width
- Output: PDF vector, `bbox_inches='tight'`
- Fig 1: hatching patterns for regions instead of colored fills
- Fig 3: hatched stacked areas (`///` vs `\\\\`)
- Fig 4: fill patterns for D=0 vs D=1 bars
- Figs 7-8: distinct line style + marker per parameter value

### 4. Code Quality
- `solve_valid` defined once in `solver.py`
- `params.replace(kappa=0.3)` replaces 10+ manual reconstructions
- Named tolerance constants replace magic numbers
- `except Exception` narrowed to `except (RuntimeError, ValueError)` with warnings
- Type hints on all functions (already mostly present, verify completeness)

## Dependencies
- Python 3.8+ (dataclasses, typing)
- numpy, scipy, matplotlib (already used)
- No new external dependencies

## Verification
- [ ] `python run_numerical.py --output_dir numerical_output` produces all 8 figures + 2 tables
- [ ] Output figures are PDF format
- [ ] Figures are grayscale-distinguishable (print test)
- [ ] All functions have docstrings with equation references
- [ ] No duplicated `solve_valid` or `ModelParams(...)` reconstruction
- [ ] `Action` enum used throughout, no string literals for actions
- [ ] Named tolerances used, no magic numbers
- [ ] Existing `numerical_output/` results are reproducible (same equilibrium cutoffs)

## Risks
- **LaTeX rendering (`text.usetex`)**: requires a TeX installation on the system. Mitigate with a fallback flag.
- **Import path changes**: anything that imports `numerical` as a module will need updating. Mitigate by providing `run_numerical.py` as the entry point.
- **Numerical reproducibility**: refactoring must not change any computation. Mitigate by comparing cutoff values before/after.
