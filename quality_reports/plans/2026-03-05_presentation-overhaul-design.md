# Design: Presentation Slide Deck Overhaul

**Status:** APPROVED
**Date:** 2026-03-05
**Approach:** Clean rewrite (Approach C)
**Scope:** Full overhaul — figures, bibliography, text, structure, audience notes

---

## Context

The paper (`draft_v3.tex`) has undergone significant polish:
- All 13 figures regenerated with Paul Tol palette, serif fonts, thin lines (5.5x3.8 standard)
- Theory fixes D1-D7 applied (multi-model triangulation: GPT Pro + Gemini + Claude)
- Proposition/Lemma numbering finalized

The slide deck (`pres/presentation.tex`) has 6 concrete problems:
1. Broken bibliography (dead symlink)
2. Stale figures (old pre-overhaul versions in `pres/figures/`)
3. 4 presentation-specific figures not in pipeline
4. Theory text not reflecting D1-D7 patches
5. Lemma numbering drift (slides say Lemma 1 for endpoints; paper says Lemma 2)
6. Missing fig_prices slide

## Architecture Decisions

1. **Single source of truth**: All content derived from `draft_v3.tex`
2. **Figures from pipeline**: `\graphicspath{{../numerical_output/}}`
3. **Bibliography**: Copy `bibliography.bib` -> `pres/slides.bib` (no symlinks)
4. **Bidirectional hyperlinks**: Preserved (essential for Q&A navigation)
5. **Proposition numbering**: Matches `draft_v3.tex` exactly
6. **Audience notes**: Generalized for finance seminar circuit (not supervisor-specific)

## Core Slides (16)

| # | Slide Title | Key Content | Figure |
|---|-------------|-------------|--------|
| 1 | Title | Title, author, UCL | -- |
| 2 | Motivation | Activist returns, takeover channel, central question | -- |
| 3 | Three Literatures, One Gap | Exit/Voice + Microstructure + Takeover. Contribution (i)-(iii) | -- |
| 4 | Disclosure Creates Two Regimes | Institutional facts (US 5%/UK 3%), model translation | -- |
| 5 | Notation Guide | Choices (blue), Observables (red), Outcomes (green) | -- |
| 6 | Model Timeline & Actions | 4-stage timeline, action-order matrix | -- |
| 7 | Engagement & Bidder Entry | C(s), p(P,D), pricing fixed point | -- |
| 8 | Equilibrium: Cutoff Strategy | Prop 1, signal regions | fig_cutoff_structure |
| 9 | Bayesian Inference | Prop 2, how kappa enters posteriors | -- |
| 10 | Price Decomposition | Prop 3, four-channel decomposition | -- |
| 11 | Prices at Baseline | Equilibrium prices + fig_prices | fig_prices |
| 12 | Main Result: Hump-Shaped | Prop 5, nonmonotone liquidity | fig_nonmonotone |
| 13 | Decomposition: Two Forces | Base vs activism components | fig_decomposition |
| 14 | Disclosure Attenuates | Prop 6, PE attenuation | fig_disclosure |
| 15 | Policy & Testable Predictions | Prop 7 (GE), four testable predictions | -- |
| 16 | Summary | Mechanism, prediction, contribution, extensions | -- |

## Backup Slides (23 + 5 section dividers = 28)

### Section A: Mathematical Foundations (8 slides)
- B1: Proof of cutoff ordering (Prop 1) <- Core 8
- B2: Existence & uniqueness (Prop 4) <- Core 8
- B3: Conditional means & posteriors (Lemma 3) <- Core 9
- B4: Full posterior formulas <- Core 9
- B5: Pricing fixed-point derivation <- Core 7
- B6: Delta^min decomposition proof <- Core 13
- B7: Endpoint behavior (Lemma 2) <- Core 12
- B8: Nonmonotonicity proof (Prop 5) <- Core 12

### Section B: Sensitivity & Comparative Statics (4 slides)
- B9: Sensitivity panel A (delta, sigma_xi) <- Core 12
- B10: Sensitivity panel B (C0, wedge, rho) <- Core 12
- B11: Cutoffs across kappa <- Core 8
- B12: Takeover comparative statics <- Core 7

### Section C: Disclosure Extensions (5 slides)
- B13: FI vs ND benchmarks <- Core 14
- B14: Noisy rumors <- Core 14
- B15: GE disclosure trade-off derivation <- Core 15
- B16: PE vs GE distinction <- Core 15
- B17: Disclosed-branch invariance <- Core 9

### Section D: Welfare (2 slides)
- B18: Welfare decomposition figure <- Core 15
- B19: Why Delta^min as welfare metric? <- Core 12

### Section E: Calibration & Numerics (4 slides)
- B20: Baseline parameters <- Core 7
- B21: Baseline equilibrium outcomes table <- Core 11
- B22: Standing assumptions (A1-A7) <- Core 6
- B23: Within-regime kappa effects on posteriors <- Core 9

## New Code: 3 Composite Figures in figures.py

### fig_sensitivity_panel_a()
- 2-panel subplot: sigma_xi (left) + delta (right)
- Reads: sensitivity_sigma_xi.csv, sensitivity_delta.csv
- Uses: SENSITIVITY_COLORS, width=2*FIG_WIDTH, height=FIG_HEIGHT
- Output: fig_sensitivity_panel1.pdf

### fig_sensitivity_panel_b()
- 3-panel subplot: C0 (left) + wedge (center) + rho (right)
- Reads: sensitivity_C0.csv, sensitivity_wedge.csv, sensitivity_rho.csv
- Uses: SENSITIVITY_COLORS, width=2.5*FIG_WIDTH, height=FIG_HEIGHT
- Output: fig_sensitivity_panel2.pdf

### fig_disclosure_slopes()
- 2-line plot: d(Delta^act)/d(kappa) for disclosure vs no-disclosure
- Reads: disclosure_attenuation.csv, uses np.gradient()
- Uses: SENSITIVITY_COLORS[0] solid, SENSITIVITY_COLORS[1] dashed
- Shaded region between curves (alpha=0.15)
- Output: fig_disclosure_slopes.pdf

## Bibliography Fix

- Remove broken symlink: `pres/slides.bib`
- Copy `bibliography.bib` -> `pres/slides.bib`
- Both use biblatex with authoryear, natbib=true, biber backend

## Verification Plan

1. `make clean && make all` -- regenerate all CSVs + 16 PDFs
2. `cd pres && xelatex presentation.tex && biber presentation && xelatex presentation.tex`
3. Visual inspection of all ~44 pages
4. Verify every hyperlink (forward and back)
5. Compile draft_v3.tex to confirm paper still builds
6. Clean all build artifacts
