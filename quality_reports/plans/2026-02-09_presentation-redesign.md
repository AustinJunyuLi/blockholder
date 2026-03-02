# Plan: Fundamental Presentation Redesign + Handout
**Date:** 2026-02-09
**Status:** DRAFT

## Task Description
Fundamentally recreate the slide deck for a 25-30 minute presentation to a panel of financial economists. Create a supplementary handout (both LaTeX article and Beamer handout mode). Deploy a team of agents for parallel execution.

### User Decisions
- **Theme**: Keep UCL Beamer theme (institutional branding)
- **Result reveal**: Save hump-shaped figure for results section (no early preview)
- **Handout**: Both LaTeX article AND Beamer handout mode
- **Trimming**: Aggressive — 16 main slides, move all non-essential formulas to backup/handout

## Files to Create/Modify

### New Files
1. `presentation/slides_v2.tex` — **New main slide deck** (16 main + 8 backup slides)
2. `presentation/handout.tex` — **Standalone LaTeX handout** (article class, ~10-15 pages)
3. `presentation/slides_v2_handout.tex` — **Beamer handout driver** (includes slides_v2 with handout mode)

### Files to Read (not modify)
- `presentation/slides.tex` — Current deck (reference for content)
- `draft_v2.tex` — Paper (source of truth for all model content)
- `numerical_output/*.pdf` — All 8 figures
- `numerical_output/table_*.tex` — Both tables
- `presentation/slides.bib` — Bibliography
- `presentation/beamerthemeucl.sty` + related theme files — UCL theme

## Approach

### Phase 1: Slide Deck (slides_v2.tex)

**Structure: 16 Main Slides**

| # | Title | Content | Time |
|---|-------|---------|------|
| 1 | Title | Title, author, affiliation | 0:30 |
| 2 | Motivation: The Puzzle | Liquidity paradox + activist M&A evidence | 2:00 |
| 3 | This Paper | Three forces unified + contribution statement | 2:00 |
| 4 | Related Literature | Position vs 3 literatures (Exit/Voice, Microstructure, Takeovers) | 1:30 |
| 5 | Model Timeline | TikZ 4-stage visual diagram | 2:00 |
| 6 | Action Space & Disclosure | 2x2 grid + D=1{q=+1} + key: two information regimes | 2:00 |
| 7 | Equilibrium: Cutoff Structure | Cutoff ordering + fig_cutoff_structure.pdf | 2:00 |
| 8 | The Inference Channel | D=1 observed vs D=0 inferred — mechanism heart | 2:00 |
| 9 | Activism Premium in Prices | Two-channel decomposition equation | 1:30 |
| 10 | **Main Result**: Hump-Shaped Gains | fig_nonmonotone.pdf + formula + intuition | 2:00 |
| 11 | Decomposition | fig_decomposition.pdf — base vs activism | 1:30 |
| 12 | Disclosure Attenuates | fig_disclosure.pdf + policy link | 1:30 |
| 13 | Sensitivity Analysis | fig_sensitivity_C0.pdf + fig_sensitivity_wedge.pdf (two panels) | 1:30 |
| 14 | Testable Predictions | 3-4 empirical implications | 1:30 |
| 15 | Policy Implications | Disclosure thresholds + liquidity as governance | 1:30 |
| 16 | Conclusion | Mechanism + prediction + contribution | 1:00 |

**Total: ~25 minutes**

**8 Backup Slides (for Q&A)**

| # | Title | Anticipated Question |
|---|-------|---------------------|
| B1 | Notation Reference | Full notation table (moved from main) |
| B2 | Full Posterior Formulas | Bayes' rule computation details |
| B3 | Pricing Fixed Point | How the price equation is solved |
| B4 | Baseline Calibration | Parameter table + equilibrium values |
| B5 | Cutoffs vs Liquidity | fig_cutoffs_kappa.pdf |
| B6 | Price Function | fig_prices.pdf |
| B7 | Alternative Disclosure Regimes | FI/ND/NR + table |
| B8 | Model Design Choices | "Why discrete orders?" rationale |

**Design Principles:**
- Keep color coding: blue=choices, red=observables, green=outcomes
- TikZ timeline diagram (horizontal, 4 stages with icons)
- TikZ mechanism flow: Order Flow → Inference → Premium → Bid → Gains
- Figures at 0.60-0.65\textheight for readability
- One key idea per slide, minimal text
- Block callouts used sparingly (max 1 per slide)

### Phase 2: Standalone Handout (handout.tex)

**Article-class document, ~10-15 pages:**

1. **Header**: Title, author, "Supplementary Handout" subtitle, date
2. **Model Summary** (2 pages): Full notation table, timeline, assumptions, action space
3. **Equilibrium Characterization** (2 pages): Propositions 1-4 with proof sketches
4. **Posterior Formulas** (1 page): Full Bayesian inference for D=1 and D=0
5. **Pricing Equation** (1 page): Fixed-point equation, regularity conditions
6. **Numerical Calibration** (1 page): Parameter table, baseline equilibrium table
7. **All Figures** (3-4 pages): Full-page versions of all 8 figures with detailed captions
8. **Extensions** (1 page): FI/ND/NR disclosure regimes with comparison table
9. **References** (1-2 pages): Full bibliography

### Phase 3: Beamer Handout Driver (slides_v2_handout.tex)

Small driver file that includes slides_v2.tex with `\documentclass[handout]{beamer}`:
- Suppresses overlays/pauses
- Prints 2 or 4 slides per page
- Can add notes in margins

## Team Deployment

| Agent | Name | Type | Task | Dependencies |
|-------|------|------|------|--------------|
| 1 | slide-architect | general-purpose | Write slides_v2.tex — all 16 main + 8 backup slides | None |
| 2 | handout-writer | general-purpose | Write handout.tex — standalone article handout | None (parallel) |
| 3 | handout-driver | general-purpose | Write slides_v2_handout.tex + compile all 3 | After 1 & 2 |
| 4 | proofreader | general-purpose | Review all 3 documents via proofreading skill | After 3 |
| 5 | compiler | Bash | Final 3-pass compilation of all documents | After 4 |

Agents 1 and 2 run in parallel. Agent 3 depends on both completing. Agent 4 reviews. Agent 5 compiles.

## Dependencies
- UCL Beamer theme files must be in `presentation/` (confirmed present)
- All 8 figures must exist in `numerical_output/` (confirmed present)
- Both tables must exist in `numerical_output/` (confirmed present)
- `slides.bib` must be present (confirmed)
- XeLaTeX + Biber must be installed

## Verification
1. `slides_v2.tex` compiles with 3-pass XeLaTeX + Biber — zero errors
2. `handout.tex` compiles with 3-pass XeLaTeX + Biber — zero errors
3. `slides_v2_handout.tex` compiles — zero errors
4. All figures render correctly in both documents
5. All citations resolve
6. No overfull hbox > 10pt
7. Slide count: exactly 16 main + 8 backup
8. Handout: 10-15 pages, all sections present
9. Proofreading report generated

## Risks
1. **TikZ diagrams**: Complex TikZ may need iteration; keep fallback text-only version
2. **Theme compatibility**: slides_v2.tex must work with existing UCL theme files
3. **Bibliography**: slides.bib must contain all cited keys; cross-check with draft
4. **Time constraint**: 16 slides for 25 min is tight; may need to drop 1-2 slides
5. **Handout length**: Could balloon; cap at 15 pages strictly
