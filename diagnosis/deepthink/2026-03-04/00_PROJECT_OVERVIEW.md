# Project Overview — EVT Model (Round 4)

## Project Identity
Academic research paper: **"Liquidity, Activism Disclosure, and Takeover Premia"**
An economic theory model studying blockholder behavior (exit, voice, corporate control).

Three layers: numerical computation (Python), visualization (R/ggplot2), manuscript/presentation (LaTeX/Beamer).

Pipeline: Python → CSV → R → PDF figures → LaTeX manuscript.

## Git State
```
Branch: theory-fixes
HEAD: 4c63de2

4c63de2 refactor: move presentation from presentation/ to pres/, delete legacy
4742d6c feat(pres): add 7 theory backup slides and restructure presentation
42c61f9 Initial commit: Exit-Voice-Takeover model codebase

Uncommitted changes:
 M R/plot_fig04_prices.R
 M R/plot_fig06_disclosure.R
 M R/theme_evtmodel.R
 M bibliography.bib
 D draft_v2.pdf
 D draft_v2.tex
 D numerical/accel.py
 M numerical/export_data.py
 M numerical/figures_matplotlib.py
 M numerical/model.py
 M numerical/params.py
 M numerical/solver.py
 M numerical_output/fig_cutoff_structure.pdf
 M numerical_output/fig_cutoffs_kappa.pdf
 M numerical_output/fig_decomposition.pdf
 M numerical_output/fig_disclosure.pdf
 M numerical_output/fig_noisy_rumor_precision.pdf
 M numerical_output/fig_nonmonotone.pdf
 M numerical_output/fig_prices.pdf
 M numerical_output/fig_sensitivity_C0.pdf
```

## Architecture

### Python numerical package (`numerical/`)
```
params.py → model.py → solver.py → export_data.py
```
- **params.py**: ModelParams dataclass, Action enum, Cutoffs/MinorityGains NamedTuples, tolerance constants
- **model.py**: Core economic functions — posteriors, prices, payoffs, welfare, information regimes
- **solver.py**: Equilibrium solver using damped fixed-point iteration with scipy.optimize.brentq
- **export_data.py**: Parameter sweeps → 13 CSV files (Python↔R interface contract)

### R visualization (`R/`)
- 13 figure scripts (`plot_fig01_*.R` through `plot_fig13_*.R`)
- `theme_evtmodel.R`: Shared theme with Paul Tol colourblind-friendly palette
- `render_all.R`: Master orchestrator

### LaTeX
- `draft_v3.tex`: Main manuscript (1462 lines, XeLaTeX + biblatex/biber)
- `pres/presentation.tex`: Beamer slides (45 frames)

## Key Model Concepts
The blockholder chooses among four actions based on a private signal s:
- **Exit** (sell stake) when s < k₁
- **Hold** (passive) when k₁ ≤ s < k₀
- **Quiet Voice** (engage below disclosure threshold) when k₀ ≤ s < k_D
- **Public Voice** (buy, engage, trigger disclosure) when s ≥ k_D

Equilibrium cutoffs (k₁, k₀, k_D) are solved via fixed-point iteration.
κ (noise trading intensity, 0 to 1) is the primary comparative statics variable.

## Numerical Tolerances (do not change)
- TOL_CONVERGE = 1e-6: fixed-point convergence
- TOL_RESIDUAL = 5e-3: equilibrium quality gate
- TOL_REGION = 1e-4: cutoff collapse detection
- TOL_PROB = 1e-10: near-zero probability threshold
