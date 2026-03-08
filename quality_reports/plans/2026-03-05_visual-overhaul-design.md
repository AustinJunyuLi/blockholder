# Design: Presentation Visual Overhaul (Metropolis + Color-Coded Variables)

**Status:** APPROVED
**Date:** 2026-03-05
**Approach:** A — Pure metropolis, no UCL branding
**Scope:** Complete visual redesign + material presentation improvements + new figures
**Prerequisite:** Current slidepack (presentation.tex) already has correct theory content

---

## Context

The current slidepack (`pres/presentation.tex`, 44 slides) has correct theoretical content
verified against `draft_v3.tex`, but the visual design has serious problems:

1. **Density imbalance**: Some slides overpacked (footnotesize/scriptsize), others nearly empty
2. **Ugly section dividers**: Plain white, no visual identity
3. **Figure-slide mismatch**: Matplotlib serif figures on sans-serif beamer theme
4. **No consistent variable color coding**: Notation guide (slide 5) introduces colors but they're never used again
5. **TikZ timeline is cramped**: Resized to fit, text too small
6. **Title overflow**: Long titles collide with UCL banner

## Architecture Decisions

1. **Theme**: Metropolis (`\usetheme[progressbar=frametitle]{metropolis}`)
   - No UCL branding anywhere (user chose pure metropolis)
   - UCL mentioned only in `\institute{}` text
   - Paul Tol blue (`#4477aa`) as accent color
2. **Typography**: Fira Sans (metropolis default) + serif math (`\usefonttheme[onlymath]{serif}`)
3. **Body text**: Consistent `\small` throughout — no more mixed sizes
4. **Equations**: Normal size (stand out from body)
5. **Color coding**: Three-category system used throughout ALL slides
6. **New figures**: Timeline + mechanism chain drawn in matplotlib (not TikZ)
7. **Figures**: Continue sourcing from `../numerical_output/` via `\graphicspath`

## Section 1: Color-Coded Variable System

Three categories using Paul Tol muted palette:

| Category | Color | Hex | Variables |
|----------|-------|-----|-----------|
| **Choices** | Blue | `#4477aa` | s, q, a, k₁, k₀, k_D, ω_E, ω_H, ω_Q, ω_P, C(s) |
| **Observables** | Rose | `#cc6677` | X, D, z, ξ |
| **Outcomes** | Green | `#228833` | π, p, P_post, P_trade, Δ^min, m̄, V̂ |

**κ (liquidity)**: Left black — it's the primary parameter, not a choice/observable/outcome.

LaTeX macros:
```latex
\newcommand{\choice}[1]{\textcolor{ptblue}{#1}}
\newcommand{\obs}[1]{\textcolor{ptrose}{#1}}
\newcommand{\outcome}[1]{\textcolor{ptgreen}{#1}}
```

Applied in EVERY equation across all 44 slides.

## Section 2: New Figures (matplotlib)

### fig_timeline.pdf
- Horizontal 4-stage timeline: t=0, t=1, t=1.5, t=2
- Color-coded annotations: blue for choices, rose for observables, green for outcomes
- Clean arrow, serif fonts matching publication theme
- Dimensions: FIG_WIDTH × FIG_HEIGHT (5.5 × 3.8)
- Replaces TikZ timeline on slide 6

### fig_mechanism_chain.pdf
- Flow diagram: s → (q,a) → (X,D) → π → p → Δ^min
- Color-coded nodes/arrows matching three-category system
- Shows feed-forward structure visually
- Dimensions: 8.0 × 2.5 (wide, short)
- Used on slide 7 or as recurring reference

Both added to `numerical/figures.py` and Makefile.

## Section 3: Theme Configuration

```latex
\documentclass[aspectratio=169,11pt]{beamer}
\usetheme[progressbar=frametitle]{metropolis}

% Paul Tol accent
\definecolor{ptblue}{HTML}{4477aa}
\definecolor{ptrose}{HTML}{cc6677}
\definecolor{ptgreen}{HTML}{228833}
\setbeamercolor{progress bar}{fg=ptblue}
\setbeamercolor{alerted text}{fg=ptblue}
\setbeamercolor{block title}{fg=ptblue}
\setbeamercolor{frametitle}{bg=}  % no background on frame titles

% Serif math (matches matplotlib figures)
\usefonttheme[onlymath]{serif}

% Hyperlinks in accent color
\hypersetup{colorlinks=true, linkcolor=ptblue, urlcolor=ptblue}
```

## Section 4: Slide Content Fixes

### Core slides needing content reflow:
- **Slide 6 (Timeline)**: Replace TikZ with `fig_timeline.pdf`, add action table alongside
- **Slide 7 (Engagement)**: Add mechanism chain figure, reflow equations with color coding
- **Slide 10 (Price Decomposition)**: Currently 3 lines — add two-channel intuition, visual
- **Slide 11 (Prices at Baseline)**: Rebalance table/figure layout

### Sparse backup slides to flesh out:
- **B7 (Endpoints)**: Add actual limit expressions for Δ^min at κ→0 and κ→1
- **B8 (Interior peak)**: Add two-force argument with intuition
- **B15 (GE disclosure)**: Explain both terms of heuristic decomposition with signs
- **B16 (PE vs GE)**: Add comparison table (what's held fixed vs what moves)
- **B17 (Disclosed invariance)**: Full reasoning chain with color-coded variables
- **B19 (Why Δ^min)**: Grossman-Hart connection, alternative metrics

### Section dividers:
- Use metropolis built-in `\section{}` (dark accent background)
- Replaces current plain white dividers

## Section 5: Figure Integration

- All matplotlib figures use serif fonts + Paul Tol palette → natural match with metropolis
- `\graphicspath{{../numerical_output/}}` unchanged
- Sensitivity panels (B9, B10) may need slight resizing for new margins

## Verification Plan

1. Add 2 new figure functions to `figures.py`, update Makefile, regenerate
2. Rewrite `pres/presentation.tex` with metropolis theme + color coding
3. Compile: `cd pres && xelatex presentation.tex && biber presentation && xelatex presentation.tex`
4. Visual inspection of all ~44 pages
5. Verify all hyperlinks (forward/back)
6. Clean build artifacts
