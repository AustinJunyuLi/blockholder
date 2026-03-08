# Visual Overhaul Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Migrate the Beamer presentation from UCL theme to metropolis with Paul Tol color-coded variables, two new matplotlib figures, and fleshed-out backup slides.

**Architecture:** Three-phase approach: (1) add 2 new figures to Python pipeline, (2) rewrite presentation.tex with metropolis theme + color-coded variables throughout, (3) compile + verify. The presentation content (theory) is already correct — this is purely visual/layout.

**Tech Stack:** Python/matplotlib (figures), LaTeX/Beamer/metropolis (slides), XeLaTeX + biber (compilation)

---

### Task 1: Add timeline and mechanism chain figures to figures.py

**Files:**
- Modify: `numerical/figures.py` (add 2 new functions + update `make_all()`)
- Modify: `Makefile` (add 2 new PDFs to PDFS list)

**Step 1: Add `fig_timeline()` function to `numerical/figures.py`**

Insert after the `fig_welfare()` function (line 400), before `make_all()`:

```python
def fig_timeline(output_dir: str, data_dir: str) -> None:
    """4-stage model timeline with color-coded annotations."""
    fig, ax = plt.subplots()

    # Stage positions and labels
    stages = [0, 1, 1.5, 2]
    stage_labels = [r"$t=0$", r"$t=1$", r"$t=1.5$", r"$t=2$"]

    # Draw timeline arrow
    ax.annotate("", xy=(2.3, 0), xytext=(-0.3, 0),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.5))

    # Stage markers
    for x, lab in zip(stages, stage_labels):
        ax.plot(x, 0, "o", color="black", markersize=8, zorder=5)
        ax.text(x, 0.12, lab, ha="center", va="bottom", fontsize=12, fontweight="bold")

    # Color-coded annotations (blue=choices, rose=observables, green=outcomes)
    blue = "#4477aa"    # choices
    rose = "#cc6677"    # observables
    green = "#228833"   # outcomes

    # t=0: Nature draws v, blockholder sees s
    ax.text(0, -0.15, "Nature draws $v$", ha="center", va="top", fontsize=9, color="black")
    ax.text(0, -0.28, "Blockholder sees $s$", ha="center", va="top", fontsize=9, color=blue)

    # t=1: Choose (q,a), noise z, X=q+z
    ax.text(1, -0.15, "Choose $(q, a)$", ha="center", va="top", fontsize=9, color=blue)
    ax.text(1, -0.28, "Noise $z$ realized", ha="center", va="top", fontsize=9, color=rose)
    ax.text(1, -0.41, "$X = q + z$,  $D = \\mathbf{1}\\{q=+1\\}$",
            ha="center", va="top", fontsize=9, color=rose)

    # t=1.5: Bidder arrives, observes (X,D), draws xi
    ax.text(1.5, -0.15, "Bidder arrives w.p. $\\lambda_B$", ha="center", va="top", fontsize=9, color="black")
    ax.text(1.5, -0.28, "Observes $(X, D)$, draws $\\xi$", ha="center", va="top", fontsize=9, color=rose)

    # t=2: Payoffs
    ax.text(2, -0.15, "Takeover or not", ha="center", va="top", fontsize=9, color="black")
    ax.text(2, -0.28, "Payoffs realized", ha="center", va="top", fontsize=9, color=green)

    ax.set_xlim(-0.4, 2.5)
    ax.set_ylim(-0.55, 0.3)
    ax.axis("off")

    save_figure(fig, os.path.join(output_dir, "fig_timeline.pdf"), width=8.0, height=2.8)


def fig_mechanism_chain(output_dir: str, data_dir: str) -> None:
    """Feed-forward mechanism chain: s -> (q,a) -> (X,D) -> pi -> p -> Delta^min."""
    fig, ax = plt.subplots()

    blue = "#4477aa"    # choices
    rose = "#cc6677"    # observables
    green = "#228833"   # outcomes

    nodes = [
        (0.0, r"$s$", blue),
        (1.0, r"$(q, a)$", blue),
        (2.0, r"$(X, D)$", rose),
        (3.0, r"$\pi$", green),
        (4.0, r"$p$", green),
        (5.0, r"$\Delta^{\min}$", green),
    ]

    for x, label, color in nodes:
        circle = plt.Circle((x, 0), 0.3, facecolor=color, edgecolor="black",
                            alpha=0.2, linewidth=1.2, zorder=2)
        ax.add_patch(circle)
        ax.text(x, 0, label, ha="center", va="center", fontsize=13,
                fontweight="bold", color=color, zorder=3)

    # Arrows between nodes
    for i in range(len(nodes) - 1):
        x_start = nodes[i][0] + 0.32
        x_end = nodes[i + 1][0] - 0.32
        ax.annotate("", xy=(x_end, 0), xytext=(x_start, 0),
                    arrowprops=dict(arrowstyle="-|>", color="#333333", lw=1.5))

    # Category labels below
    ax.text(0.5, -0.55, "Choices", ha="center", va="top", fontsize=10, color=blue, fontstyle="italic")
    ax.text(2.0, -0.55, "Observables", ha="center", va="top", fontsize=10, color=rose, fontstyle="italic")
    ax.text(4.0, -0.55, "Outcomes", ha="center", va="top", fontsize=10, color=green, fontstyle="italic")

    ax.set_xlim(-0.6, 5.6)
    ax.set_ylim(-0.75, 0.55)
    ax.set_aspect("equal")
    ax.axis("off")

    save_figure(fig, os.path.join(output_dir, "fig_mechanism_chain.pdf"), width=8.0, height=2.5)
```

**Step 2: Update `make_all()` in `numerical/figures.py`**

Add these two calls inside `make_all()`, after `fig_welfare(output_dir, data_dir)`:

```python
    fig_timeline(output_dir, data_dir)
    fig_mechanism_chain(output_dir, data_dir)
```

**Step 3: Update `Makefile` PDFS list**

Add these two lines to the PDFS variable (after `fig_welfare.pdf`):

```makefile
        $(OUTPUT_DIR)/fig_timeline.pdf \
        $(OUTPUT_DIR)/fig_mechanism_chain.pdf
```

**Step 4: Run pipeline to generate new figures**

Run: `make figures`
Expected: 18 PDFs generated (16 existing + 2 new)

**Step 5: Visual inspection of new figures**

Read: `numerical_output/fig_timeline.pdf` and `numerical_output/fig_mechanism_chain.pdf`
Verify: Color coding matches (blue=choices, rose=observables, green=outcomes), text is legible, no overlap

**Step 6: Commit**

```bash
git add numerical/figures.py Makefile numerical_output/fig_timeline.pdf numerical_output/fig_mechanism_chain.pdf
git commit -m "feat(figures): add timeline and mechanism chain figures for presentation"
```

---

### Task 2: Rewrite presentation.tex with metropolis theme

**Files:**
- Modify: `pres/presentation.tex` (complete rewrite of preamble + all slides)

This is the main creative task. The full rewrite preserves ALL existing theoretical content (which was verified correct) but changes:

1. Theme: UCL → metropolis
2. Typography: consistent `\small` body, normal-size equations
3. Color coding: `\choice{}`, `\obs{}`, `\outcome{}` macros applied everywhere
4. Timeline: TikZ → `fig_timeline.pdf`
5. Section dividers: plain white → metropolis `\section{}`
6. Sparse slides: fleshed out with paper content
7. Block styling: metropolis default (cleaner than UCL custom blocks)

**Step 1: Write the new preamble**

Replace lines 1-94 of `pres/presentation.tex` with:

```latex
% ============================================================================
% presentation.tex
% Beamer deck for: Liquidity, Activism Disclosure, and Takeover Premia
%
% Source of truth: ../draft_v3.tex
% Figures: ../numerical_output/*.pdf
% Theme: metropolis (Fira Sans + progress bar)
% ============================================================================
%
% -- AUDIENCE CALIBRATION --------------------------------------------------
%
% Primary audience: Finance seminar (theory or corporate finance field)
%   Frame as: liquidity -> inference -> prices -> takeover premia
%   Emphasize: disclosure policy as governance tool + testable predictions
%   Duration: 30 min talk + 15 min Q&A
%
% Key hooks for different audiences:
%   Corporate finance: SEC 13D filing window, activism returns, M&A premia
%   Microstructure: order-flow inference, Kyle-type noise trading, price feedback
%   Theory: existence + single-crossing + (numerical) uniqueness
%   Empirical: four predictions incl. hump test + 13D CAR interaction
% ============================================================================

\documentclass[aspectratio=169,11pt]{beamer}
\usetheme[progressbar=frametitle]{metropolis}

% --- Packages ---
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{booktabs}
\usepackage{graphicx}
\graphicspath{{../numerical_output/}}
\usepackage{array,tabularx,multirow}
\usepackage{csquotes}
\usepackage{appendixnumberbeamer}

\usepackage[backend=biber,style=authoryear,natbib=true,maxcitenames=2,maxbibnames=99]{biblatex}
\addbibresource{slides.bib}

% --- Paul Tol palette (colourblind-safe) ---
\usepackage{xcolor}
\definecolor{ptblue}{HTML}{4477aa}
\definecolor{ptrose}{HTML}{cc6677}
\definecolor{ptgreen}{HTML}{228833}
\definecolor{ptsand}{HTML}{ddcc77}
\definecolor{ptcyan}{HTML}{88ccee}
\definecolor{ptteal}{HTML}{44aa99}

% --- Metropolis color overrides ---
\setbeamercolor{progress bar}{fg=ptblue}
\setbeamercolor{title separator}{fg=ptblue}
\setbeamercolor{alerted text}{fg=ptblue}
\setbeamercolor{example text}{fg=ptgreen}

% --- Serif math (matches matplotlib figures) ---
\usefonttheme[onlymath]{serif}

% --- Notation macros ---
\newcommand{\E}{\mathbb{E}}
\newcommand{\PP}{\mathbb{P}}
\newcommand{\1}{\mathbf{1}}
\newcommand{\Var}{\mathrm{Var}}
\newcommand{\R}{\mathbb{R}}

% --- Color-coded variable system (used throughout) ---
% Choices: decisions made by agents (blue)
\newcommand{\choice}[1]{{\color{ptblue}#1}}
% Observables: market signals, noise, data (rose)
\newcommand{\obs}[1]{{\color{ptrose}#1}}
% Outcomes: equilibrium objects computed from model (green)
\newcommand{\outcome}[1]{{\color{ptgreen}#1}}

% --- Hyperlink styling ---
\hypersetup{colorlinks=true, linkcolor=ptblue, urlcolor=ptblue}

% --- Navigation helpers (bidirectional links for Q&A) ---
\newcommand{\backuplink}[2]{%
  \hfill{\scriptsize\hyperlink{#1}{\textcolor{ptblue}{#2\,$\nearrow$}}}%
}
\newcommand{\returnlink}[2]{%
  \par\vspace{0.2em}\hfill{\scriptsize\hyperlink{#1}{\textcolor{ptblue}{$\leftarrow$\,#2}}}%
}

% --- Title ---
\title{Liquidity, Activism Disclosure, and Takeover Premia}
\subtitle{A Theory of Exit, Voice, and Corporate Control}
\author{Austin Li}
\institute{University College London}
\date{}
```

**Step 2: Write core slides 1-16**

Replace ALL core slide content (lines 95-559) with the color-coded metropolis version. Each slide keeps the same theoretical content but applies `\choice{}`, `\obs{}`, `\outcome{}` macros and uses consistent `\small` body text. Key changes per slide:

- **Slide 1 (Title)**: Standard `\maketitle` (metropolis handles it)
- **Slide 5 (Notation Guide)**: Use colored boxes/columns with Paul Tol colors matching the macro system
- **Slide 6 (Timeline)**: Replace TikZ with `\includegraphics{fig_timeline.pdf}` + action table
- **Slide 7 (Engagement)**: Add `\includegraphics{fig_mechanism_chain.pdf}` showing feed-forward chain
- **Slide 10 (Price Decomposition)**: Flesh out with two-channel description and color-coded equation
- **ALL equations**: Apply `\choice{}`, `\obs{}`, `\outcome{}` to every variable

**Step 3: Write section dividers and backup slides**

Replace ALL backup content (lines 560-994) using metropolis `\section{}` for dividers (which render with dark accent background) and flesh out sparse slides:

- **B7**: Add limit expressions: at $\kappa\downarrow 0$, $P_{\text{trade}} \to P_{\text{post}}$ (full inference); at $\kappa\uparrow 1$, extreme flows still reveal $D$
- **B8**: Add two-force argument: Weierstrass on compact $[0,1]$ + endpoint separation → interior peak. Note it doesn't rule out multiple peaks (but baseline is single-peaked)
- **B15**: Add both terms with signs: transparency $(+)$ removes inference discount; deterrence $(-)$ shrinks $\omega_Q + \omega_P$
- **B16**: Add comparison table: PE holds $(k_1,k_0,k_D)$ fixed; GE lets cutoffs respond; both preserve $\omega_P \gg 0$
- **B17**: Full chain with color: $\obs{D}=1 \Rightarrow \choice{a}=1$ a.s., $\obs{X}=1+\obs{z}$ reveals only noise, $\outcome{\pi}(\obs{X},1)=1$, $\outcome{P_{\text{post}}}(\obs{X},1)$ constant
- **B19**: Add Grossman-Hart argument: with dispersed ownership, minority gain from control changes = takeover premia. Alternative: total surplus (but premia are transfers, so different object)

**Step 4: Compile the presentation**

Run:
```bash
cd /home/austinli/Dropbox/Projects/Blockholder/directory/pres && \
  xelatex presentation.tex && biber presentation && xelatex presentation.tex && xelatex presentation.tex
```
Expected: Clean compile, ~44 pages, no missing figures, no broken citations

**Step 5: Visual inspection**

Read `pres/presentation.pdf` — all pages. Check:
- Metropolis theme renders correctly (progress bar, clean titles)
- Color coding visible and consistent
- No title overflow
- Section dividers have dark background
- Figures integrate cleanly
- All hyperlinks work (forward/back)
- No overfull hbox warnings (check log)

**Step 6: Commit**

```bash
git add pres/presentation.tex pres/presentation.pdf
git commit -m "feat(pres): visual overhaul — metropolis theme, color-coded variables, new figures"
```

---

### Task 3: Verification and cleanup

**Step 1: Full pipeline rebuild**

Run: `make clean && make all`
Expected: 13 CSVs + 18 PDFs generated cleanly

**Step 2: Recompile presentation from clean state**

Run:
```bash
cd /home/austinli/Dropbox/Projects/Blockholder/directory/pres && \
  rm -f *.aux *.bbl *.bcf *.blg *.log *.nav *.out *.run.xml *.snm *.toc && \
  xelatex presentation.tex && biber presentation && xelatex presentation.tex && xelatex presentation.tex
```
Expected: Clean compile

**Step 3: Verify paper still compiles**

Run:
```bash
cd /home/austinli/Dropbox/Projects/Blockholder/directory && \
  xelatex draft_v3.tex && biber draft_v3 && xelatex draft_v3.tex
```
Expected: 54 pages, no errors

**Step 4: Clean build artifacts**

Run:
```bash
cd /home/austinli/Dropbox/Projects/Blockholder/directory && \
  rm -f *.aux *.log *.bbl *.bcf *.blg *.run.xml *.synctex.gz *.out *.toc *.fls *.fdb_latexmk && \
  cd pres && rm -f *.aux *.log *.bbl *.bcf *.blg *.run.xml *.nav *.out *.snm *.toc
```

**Step 5: Final commit**

```bash
git add -A
git commit -m "chore: clean build artifacts after visual overhaul verification"
```
