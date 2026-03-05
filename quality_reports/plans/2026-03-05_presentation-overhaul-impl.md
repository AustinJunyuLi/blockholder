# Presentation Overhaul Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Clean rewrite of `pres/presentation.tex` — 16 core + 28 backup pages = 44 total, with polished figures from the pipeline, fixed bibliography, and all theory text matching `draft_v3.tex`.

**Architecture:** Single-file Beamer presentation using UCL theme. Figures sourced from `../numerical_output/` via `\graphicspath`. Three new composite figures generated in `numerical/figures.py`. Bidirectional hyperlink system for Q&A navigation.

**Tech Stack:** LaTeX/Beamer (XeLaTeX), Python (matplotlib), biblatex/biber.

---

## Task 1: Fix Bibliography

**Files:**
- Delete: `pres/slides.bib` (broken symlink)
- Create: `pres/slides.bib` (copy of `bibliography.bib`)

**Step 1: Remove broken symlink and copy bibliography**

```bash
rm -f pres/slides.bib
cp bibliography.bib pres/slides.bib
```

**Step 2: Verify the file is valid**

```bash
head -5 pres/slides.bib
# Should show @article or @book entries, not "No such file"
wc -l pres/slides.bib
# Should be same line count as bibliography.bib
```

**Step 3: Commit**

```bash
git add pres/slides.bib
git commit -m "fix(pres): replace broken slides.bib symlink with copy of bibliography.bib"
```

---

## Task 2: Add 3 Composite Figures to figures.py

**Files:**
- Modify: `numerical/figures.py` (add 3 functions + update make_all)
- Modify: `Makefile` (add 3 new PDFs to PDFS list)

**Step 1: Add `fig_sensitivity_panel_a()` to figures.py**

After `fig_sensitivity_delta()`, add:

```python
def fig_sensitivity_panel_a(output_dir: str, data_dir: str) -> None:
    """2-panel: sigma_xi (left) + delta (right). Presentation composite."""
    df_xi = _read_csv(os.path.join(data_dir, "sensitivity_sigma_xi.csv"))
    df_xi = df_xi.dropna(subset=["kappa", "s_xi", "delta_min"])
    df_d = _read_csv(os.path.join(data_dir, "sensitivity_delta.csv"))
    df_d = df_d.dropna(subset=["kappa", "delta", "delta_min"])

    fig, (ax1, ax2) = plt.subplots(1, 2)

    for i, val in enumerate(sorted(df_xi["s_xi"].unique())):
        sub = df_xi[df_xi["s_xi"] == val]
        ax1.plot(sub["kappa"], sub["delta_min"], color=SENSITIVITY_COLORS[i % 4], label=f"$\\sigma_\\xi$={val:g}")
    ax1.set_xlabel(r"Liquidity $\kappa$")
    ax1.set_ylabel(r"$\Delta^{\min}(\kappa)$")
    ax1.set_title(r"Bidder shock $\sigma_\xi$")
    ax1.legend(frameon=False, fontsize=8)

    for i, val in enumerate(sorted(df_d["delta"].unique())):
        sub = df_d[df_d["delta"] == val]
        ax2.plot(sub["kappa"], sub["delta_min"], color=SENSITIVITY_COLORS[i % 4], label=f"$\\delta$={val:g}")
    ax2.set_xlabel(r"Liquidity $\kappa$")
    ax2.set_ylabel(r"$\Delta^{\min}(\kappa)$")
    ax2.set_title(r"Discount factor $\delta$")
    ax2.legend(frameon=False, fontsize=8)

    save_figure(fig, os.path.join(output_dir, "fig_sensitivity_panel1.pdf"), width=2 * FIG_WIDTH, height=FIG_HEIGHT)
```

**Step 2: Add `fig_sensitivity_panel_b()` to figures.py**

```python
def fig_sensitivity_panel_b(output_dir: str, data_dir: str) -> None:
    """3-panel: C0 (left) + wedge (center) + rho (right). Presentation composite."""
    configs = [
        ("sensitivity_C0.csv", "C0", r"Engagement cost $C_0$"),
        ("sensitivity_wedge.csv", "wedge", r"Premium wedge $(m_1{-}m_0)$"),
        ("sensitivity_rho.csv", "rho", r"Success prob.\ $\rho$"),
    ]

    fig, axes = plt.subplots(1, 3)

    for ax, (csv, hue, title) in zip(axes, configs):
        df = _read_csv(os.path.join(data_dir, csv))
        df = df.dropna(subset=["kappa", hue, "delta_min"])
        for i, val in enumerate(sorted(df[hue].unique())):
            sub = df[df[hue] == val]
            ax.plot(sub["kappa"], sub["delta_min"], color=SENSITIVITY_COLORS[i % 4], label=f"{hue}={val:g}")
        ax.set_xlabel(r"Liquidity $\kappa$")
        ax.set_ylabel(r"$\Delta^{\min}$")
        ax.set_title(title, fontsize=10)
        ax.legend(frameon=False, fontsize=7)

    save_figure(fig, os.path.join(output_dir, "fig_sensitivity_panel2.pdf"), width=2.5 * FIG_WIDTH, height=FIG_HEIGHT)
```

**Step 3: Add `fig_disclosure_slopes()` to figures.py**

```python
def fig_disclosure_slopes(output_dir: str, data_dir: str) -> None:
    """Slope figure: d(Delta^act)/d(kappa) for disclosure vs no-disclosure."""
    df = _read_csv(os.path.join(data_dir, "disclosure_attenuation.csv"))
    df = df.dropna(subset=["kappa", "act_disclosure", "act_no_disclosure"])

    kappa = df["kappa"].values
    slope_disc = np.gradient(df["act_disclosure"].values, kappa)
    slope_nodisc = np.gradient(df["act_no_disclosure"].values, kappa)

    fig, ax = plt.subplots()
    ax.plot(kappa, slope_disc, color=SENSITIVITY_COLORS[0], label="Baseline (disclosure)")
    ax.plot(kappa, slope_nodisc, linestyle="--", color=SENSITIVITY_COLORS[1], label="No disclosure")
    ax.fill_between(kappa, slope_disc, slope_nodisc, alpha=0.15, color=SENSITIVITY_COLORS[1], label="Attenuation gap")
    ax.axhline(0, linewidth=0.5, color="#333333")

    ax.set_xlabel(r"Liquidity $\kappa$")
    ax.set_ylabel(r"Slope $\partial\Delta^{\mathrm{act}}/\partial\kappa$")
    ax.set_title("Disclosure attenuates liquidity sensitivity")
    ax.legend(frameon=False)

    save_figure(fig, os.path.join(output_dir, "fig_disclosure_slopes.pdf"), width=FIG_WIDTH, height=FIG_HEIGHT)
```

**Step 4: Update `make_all()` in figures.py**

Add three calls before the closing of `make_all()`:

```python
    fig_sensitivity_panel_a(output_dir, data_dir)
    fig_sensitivity_panel_b(output_dir, data_dir)
    fig_disclosure_slopes(output_dir, data_dir)
```

**Step 5: Update Makefile**

Add to PDFS list:

```makefile
        $(OUTPUT_DIR)/fig_sensitivity_panel1.pdf \
        $(OUTPUT_DIR)/fig_sensitivity_panel2.pdf \
        $(OUTPUT_DIR)/fig_disclosure_slopes.pdf
```

**Step 6: Test the pipeline**

```bash
make clean && make all
# Verify: should produce 16 PDFs now (13 original + 3 new)
ls -la numerical_output/fig_sensitivity_panel1.pdf numerical_output/fig_sensitivity_panel2.pdf numerical_output/fig_disclosure_slopes.pdf
```

**Step 7: Visual inspection of 3 new figures**

Read each PDF to verify colors and layout are correct.

**Step 8: Commit**

```bash
git add numerical/figures.py Makefile
git commit -m "feat(figures): add 3 presentation composite figures (sensitivity panels + disclosure slopes)"
```

---

## Task 3: Write New presentation.tex

**Files:**
- Overwrite: `pres/presentation.tex`

This is the main creative task. The new file must contain ALL of the following, derived from `draft_v3.tex` as single source of truth.

### Critical references for the writing agent

**Proposition numbering (from draft_v3.tex):**
- Lemma 1: Domination of Passive Accumulation (L333)
- Proposition 1: Monotone Cutoff Structure (L345)
- Proposition 2: Posterior Engagement Probabilities (L404)
- Proposition 3: Post-Disclosure Price Decomposition (L479)
- Proposition 4: Existence of Monotone Equilibrium (L531)
- Lemma 2: Endpoint Behavior (L563)
- Proposition 5: Hump-Shaped Minority Takeover Gains (L576)
- Proposition 6: Disclosure Attenuation, Partial Equilibrium (L610)
- Proposition 7: GE Disclosure Trade-off (L810)
- Lemma 3: Truncated Normal Expectations (appendix, L1116)

**Figure filenames (all in `../numerical_output/`):**
- `fig_cutoff_structure.pdf` (7x2.5, special layout)
- `fig_nonmonotone.pdf` (5.5x3.8)
- `fig_decomposition.pdf` (5.5x3.8)
- `fig_prices.pdf` (10x4, dual panel)
- `fig_cutoffs_kappa.pdf` (5.5x3.8)
- `fig_disclosure.pdf` (5.5x3.8)
- `fig_disclosure_slopes.pdf` (5.5x3.8, NEW)
- `fig_sensitivity_panel1.pdf` (11x3.8, 2-panel, NEW)
- `fig_sensitivity_panel2.pdf` (13.75x3.8, 3-panel, NEW)
- `fig_noisy_rumor_precision.pdf` (5.5x3.8)
- `fig_welfare.pdf` (5.5x3.8)

**Hyperlink system:**
- Core slides: `\hypertarget{main:NAME}{}` where NAME = title, motivation, lit, disclosure, notation, timeline, engagement, prop1, prop2, pricedecomp, prices, mainresult, decomp, attenuation, policy, summary
- Backup slides: `\hypertarget{backup:NAME}{}` where NAME matches the backup identifier
- Forward links from core: `\backuplink{backup:NAME}{Link text}`
- Return links from backup: `\returnlink{main:NAME}{Slide N: Title}`

**UCL theme assets (already in pres/):**
- `beamerthemeucl.sty`, `beamercolorthemeucl.sty`, `beamerouterthemeucltitlebanner.sty`
- `beamerinnerthemeblockborder.sty`, `uclcolors.sty`
- `banners/` directory with institutional PDFs

### Preamble specification

```latex
\documentclass[aspectratio=169,11pt]{beamer}
\usetheme{ucl}
\useoutertheme[small]{ucltitlebanner}
\setbeamercolor{title}{fg=black,bg=}
\setbeamerfont{frametitle}{series=\bfseries}

% Packages
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{booktabs}
\usepackage{graphicx}
\graphicspath{{../numerical_output/}}
\usepackage{array,tabularx,multirow}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,shapes.geometric,calc,decorations.pathreplacing}
\usepackage{csquotes}
\usepackage{hyperref}
\usepackage[backend=biber,style=authoryear,natbib=true,maxcitenames=2,maxbibnames=99]{biblatex}
\addbibresource{slides.bib}

% Notation macros
\newcommand{\E}{\mathbb{E}}
\newcommand{\PP}{\mathbb{P}}
\newcommand{\1}{\mathbf{1}}
\newcommand{\Var}{\mathrm{Var}}
\newcommand{\R}{\mathbb{R}}

% Color coding for notation categories
\usepackage{xcolor}
\newcommand{\choice}[1]{\textcolor{blue}{#1}}
\newcommand{\obs}[1]{\textcolor{red!70!black}{#1}}
\newcommand{\outcome}[1]{\textcolor{green!50!black}{#1}}

% Hyperlink styling
\hypersetup{colorlinks=true, linkcolor=brightblue, urlcolor=brightblue}

% Navigation helpers
\newcommand{\backuplink}[2]{%
  \hfill{\scriptsize\hyperlink{#1}{\textcolor{brightblue}{#2\,$\nearrow$}}}%
}
\newcommand{\returnlink}[2]{%
  \par\vspace{0.2em}\hfill{\scriptsize\hyperlink{#1}{\textcolor{brightblue}{$\leftarrow$\,#2}}}%
}

% Beamer cosmetics
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}[author title date]
\setbeamercolor{block title}{fg=brightblue,bg=}
\setbeamercolor{block body}{fg=black,bg=}
\setbeamerfont{block title}{series=\bfseries}
% Block style with rule separator (same as original)
\setbeamertemplate{block begin}{%
  \par\vskip\smallskipamount%
  {\usebeamerfont*{block title}\usebeamercolor[fg]{block title}\insertblocktitle\par}%
  \vskip-0.2em{\color{brightblue}\hrule height 0.8pt}\vskip0.4em%
  \usebeamerfont{block body}%
}
\setbeamertemplate{block end}{\vskip\smallskipamount}
```

### Slide-by-slide specification

The writing agent MUST read `draft_v3.tex` to get exact formulas. Below is the content specification for each slide.

#### CORE SLIDES (16)

**Slide 1 (Title):** Title, subtitle "A Theory of Exit, Voice, and Corporate Control", author "Austin Li", institution "University College London". No date.

**Slide 2 (Motivation):** 3 empirical bullet points citing Brav et al. (2008), Greenwood & Schor (2009), Collin-Dufresne & Fos (2015). Central Question block: "How does market liquidity shape the takeover premia that minority shareholders receive when a blockholder can exit, hold, or engage?"

**Slide 3 (Three Literatures):** Two-column. Left: Exit/Voice (Edmans 2009, Maug 1998, Admati & Pfleiderer 2009), Microstructure (Kyle 1985, Back et al. 2018), Takeover (Edmans, Goldstein & Jiang 2012). Right: The Gap + Contribution (i)-(iii).

**Slide 4 (Disclosure):** Two-column. Left: Institutional facts (US 5%/UK 3%), Quiet vs Public Voice table. Right: Model translation D = 1{q=+1}, two regimes.

**Slide 5 (Notation Guide):** Three-column layout. Choices/Actions (blue), Observables (red), Outcomes (green). Color-coded. Include Equilibrium Objects, Parameters, Cutoffs, Region probs.

**Slide 6 (Timeline):** TikZ timeline: t=0 (Nature), t=1 (Trading), t=1.5 (Entry), t=2 (Payoffs). Action-order matrix. Noise specification. Bidder feedback note. Backuplink to Standing Assumptions.

**Slide 7 (Engagement & Bidder Entry):** Two-column. Left: C(s) = C0 exp(-chi*(s-mu)/sigma_s), success probability rho, value improvement. Right: p(P,D) = 1 - Phi(...), pricing fixed point, regularity. Backuplinks to derivation, bid deterrence, takeover comp statics.

**Slide 8 (Prop 1: Cutoffs):** Block with Prop 1 statement. Cutoff ordering with signal regions. Inline `fig_cutoff_structure`. Key insight: Hold and Quiet Voice produce identical order-flow distributions. Backuplink to proof sketch.

**Slide 9 (Prop 2: Posteriors):** Block with Prop 2 statement. Disclosed: pi(X,1) = 1. Nondisclosed formulas. Mechanism chain: X -> pi -> m_bar -> p -> Delta^min. Kappa enters at inference, only on D=0. Backuplinks to full posteriors, disclosed-branch invariance.

**Slide 10 (Prop 3: Price Decomposition):** Block with Prop 3 statement. Four-term decomposition: E[v|X,D] + Delta_tilde*pi + p*(P+m0) + p*(m_tilde-m0)*pi. Standalone vs takeover channel explanation. Backuplink to pricing derivation.

**Slide 11 (Prices at Baseline):** Left: equilibrium table (D, X, P(X,D), pi, p, m_bar) from `numerical_output/data/prices.csv`. Right: `fig_prices` figure. Key observations about flat D=1 prices, inference gradient on D=0, lower bid probability for D=1.

**Slide 12 (Main Result: Prop 5):** Left half: `fig_nonmonotone`. Right half: Block with Prop 5 statement (hump-shaped). Decomposition formula. Two forces: (i) kappa up -> noise cover -> more bids, (ii) kappa up -> weaker inference -> lower pi. Kappa-dagger annotation. Backuplinks to sensitivity, endpoints, proof.

**Slide 13 (Decomposition):** Left half: `fig_decomposition`. Right half: Two components formula. Base (dashed): monotone increasing. Activism (dotted): hump-shaped, inference degrades. Backuplinks to sensitivity, proof.

**Slide 14 (Disclosure Attenuation: Prop 6):** Left half: `fig_disclosure_slopes`. Right half: Block with Prop 6 statement. Shaded region = attenuation gap. D=1 states contribute zero sensitivity. Implication: disclosure and liquidity are substitutes. UK 3% vs US 5%. Backuplinks to alternative regimes, noisy rumors, PE vs GE.

**Slide 15 (Policy & Testable Predictions):** Left column: Four testable predictions (numbered). Right column: Prop 7 (GE Disclosure Trade-off) with formula d(Delta^act)/d(tau) approx transparency + deterrence. When transparency vs deterrence dominates. Key: liquidity regulation = governance policy. Backuplinks to GE analysis, welfare.

**Slide 16 (Summary):** Four blocks: Mechanism (1 sentence), Main Prediction (1 sentence), Contribution (1 sentence), Extensions (dynamic, multiple blockholders, endogenous info). Thank you + email.

#### BACKUP SLIDES (23 content + 5 dividers)

**Section divider: "Backup: Mathematical Foundations & Equilibrium Robustness"**

**B1: "How do you establish that the cutoff ordering holds?"**
- Proof sketch of Prop 1: single-crossing in 3 steps (Exit vs Hold, Hold vs QV, QV vs PV)
- Return to Slide 8

**B2: "How do you know the equilibrium is unique?"**
- Prop 4 (Existence): Brouwer's fixed-point
- Uniqueness: numerical verification, multi-start
- Return to Slide 8

**B3: "How does the market update its expectation of fundamentals?"**
- Conditional means mu_E, mu_H, mu_Q, mu_P with inverse Mills ratios
- Bayesian mixing formula
- Return to Slide 9

**B4: "What are the full posterior formulas?"**
- D=1 branch (trivial), D=0 branch (four posteriors with kappa)
- Partial derivatives: d(pi(1,0))/dk = 0, d(pi(-1,0))/dk >= 0, d(pi(0,0))/dk <= 0
- Return to Slide 9

**B5: "Walk me through the pricing fixed-point solution."**
- 4-step procedure: compute pi, compute V_hat, define m_bar, solve scalar FP
- Closed form: P* = delta[(1-p*)V_hat + p*m_bar] / (1-delta*p*)
- Regularity check: delta*phi(0)/sigma_xi < 1
- Return to Slide 7

**B6: "How do you derive the Delta^min decomposition?"**
- Goal -> Step 1 (definition) -> Step 2 (conditional independence) -> Step 3 (iterated expectations)
- Key: xi perp (v,a) given public info
- Return to Slide 13

**B7: "What are the endpoint limits of minority gains?"**
- Lemma 2 (Endpoint Behavior): kappa -> 1 and kappa -> 0
- Right endpoint: order flow uninformative, omega_Q + omega_P -> 0
- Left endpoint: X -> q a.s., full informativeness, bid deterrence
- Return to Slide 12

**B8: "How do you know the hump is strict?"**
- Proof of Prop 5: Continuity -> Weierstrass -> interior maximizer via Lemma 2
- Shape note: Weierstrass guarantees >= 1 peak, calibration confirms single peak
- Return to Slide 12

**Section divider: "Backup: Sensitivity & Comparative Statics"**

**B9: "How robust is the hump to bidder and discount parameters?"**
- `fig_sensitivity_panel1.pdf` (sigma_xi left, delta right)
- Commentary on each panel
- Return to Slide 12

**B10: "How do activism frictions affect the hump?"**
- `fig_sensitivity_panel2.pdf` (C0, wedge, rho)
- Commentary on each panel
- Return to Slide 12

**B11: "How do equilibrium cutoffs move with liquidity?"**
- `fig_cutoffs_kappa.pdf`
- k1 = k0 throughout baseline (Hold collapsed), kD tracks QV/PV boundary
- Return to Slide 8

**B12: "Does engagement deter bids?"**
- Bid deterrence: dp/dP < 0, dp/dpi < 0
- Synergies vs entry costs comparative statics
- Return to Slide 7

**Section divider: "Backup: Disclosure Extensions & Information Regimes"**

**B13: "Full disclosure vs. no disclosure benchmarks"**
- FI: pi_FI = a, deterministic, upper bound on disclosure informativeness
- ND: pi_ND(X) pools all states, lower bound
- Ordering: Var_kappa[Delta^act_FI] = 0 < Var baseline < Var ND
- Return to Slide 14

**B14: "How do noisy rumors affect the mechanism?"**
- Extension (Section 8.3): binary rumor R in {0,1}
- Updated posterior formula with eta_1 (true positive) and eta_0 (false positive)
- `fig_noisy_rumor_precision.pdf`
- Return to Slide 14

**B15: "GE effect of stricter disclosure?"**
- Prop 7 formula: d(Delta^act)/d(tau) = partial + (partial w.r.t. kD) * dkD/dtau
- Transparency (+) vs deterrence (-)
- When each dominates
- Return to Slide 15

**B16: "PE vs GE: Two disclosure effects"**
- Prop 6 (PE): fix cutoffs, vary kappa only
- Prop 7 (GE): allow kD = kD(tau) to adjust
- Key distinction and policy implication
- Return to Slide 15

**B17: "Why are prices flat on the disclosed branch?"**
- Claim: P*(x,1) = P*(x',1) for all x,x'
- Proof: D=1 => a=1 a.s., z perp (v,s,xi), pi(x,1)=1
- Consequence: foundation of Prop 6
- Return to Slide 9

**Section divider: "Backup: Welfare"**

**B18: "Distributional or total surplus?"**
- `fig_welfare.pdf`
- W(kappa) = W_min + W_B + W_bid
- Tension: kappa-dagger maximizes extraction, kappa-star maximizes total
- Return to Slide 15

**B19: "Why use Delta^min as the welfare metric?"**
- Grossman & Hart (1980): dispersed minorities benefit only through premium
- Delta^min captures probability, premium, and kappa interaction
- Empirical: activist returns approx takeover premia
- Return to Slide 12

**Section divider: "Backup: Calibration & Numerical Details"**

**B20: "What are your baseline parameter values and why?"**
- Full parameter table from draft_v3.tex Table 1 (see L632-638)
- Derived quantities: sigma_s, beta, m_tilde, Delta_tilde
- Regularity check: delta*phi(0)/sigma_xi < 1
- Return to Slide 7

**B21: "Show me the full equilibrium outcomes at baseline."**
- Full (D, X, P, pi, p, m_bar) table from prices.csv
- Key observations: flat D=1, inference gradient D=0, lower p for D=1
- Return to Slide 11

**B22: "What are the standing assumptions?"**
- A1-A7 table with "Where Used" column
- Note: A5 verifiable ex ante, A6 verified numerically
- Return to Slide 6

**B23: "What are the within-regime kappa effects on posteriors?"**
- Three partial derivatives: d(pi(1,0))/dk, d(pi(0,0))/dk, d(pi(-1,0))/dk
- Net effect on Delta^act: probability-weighted sum yields the hump
- Return to Slide 9

### Audience calibration note (replace current)

```latex
% ── AUDIENCE CALIBRATION ──────────────────────────────────────────────
%
% Primary audience: Finance seminar (theory or corporate finance field)
%   Frame as: liquidity -> information -> prices -> takeover premia
%   Emphasize: disclosure policy as governance tool, testable predictions
%   Duration: 30 min talk + 15 min Q&A
%
% Key hooks for different audiences:
%   Corporate finance: SEC 13D filing window, activism returns, M&A premia
%   Microstructure: order-flow inference, Kyle-type noise trading, price feedback
%   Theory: fixed-point existence, single-crossing, contraction mapping
%   Empirical: four testable predictions, calibration details
% =====================================================================
```

**Step 1: Write the complete `presentation.tex`**

The writing agent must read `draft_v3.tex` (especially lines 330-640 for all proposition statements) and the existing `pres/presentation.tex` (for UCL theme configuration) to produce the new file. The file should be approximately 1200-1500 lines.

**Step 2: Compile**

```bash
cd pres && xelatex -interaction=nonstopmode presentation.tex 2>&1 | tail -10
biber presentation 2>&1 | tail -5
xelatex -interaction=nonstopmode presentation.tex 2>&1 | tail -10
```

Expected: Clean compile, ~44 pages, no undefined references.

**Step 3: Visual inspection**

Read the output PDF page by page. Verify:
- All 16 core slides render correctly
- All figures appear (not missing-file errors)
- All hyperlinks are defined (no "undefined" warnings for hypertargets)
- Bibliography renders properly (no raw citation keys)
- Proposition/Lemma numbers match draft_v3.tex

**Step 4: Commit**

```bash
git add pres/presentation.tex
git commit -m "feat(pres): clean rewrite of presentation for finance seminar circuit

16 core slides + 23 backup slides + 5 section dividers.
Figures sourced from numerical_output/ via graphicspath.
All proposition/lemma numbering matches draft_v3.tex.
Bidirectional hyperlinks for Q&A navigation."
```

---

## Task 4: Final Verification

**Step 1: Full clean rebuild**

```bash
make clean && make all
```

Verify: 16 PDFs in `numerical_output/` (13 original + 3 composites).

**Step 2: Compile presentation**

```bash
cd pres && xelatex presentation.tex && biber presentation && xelatex presentation.tex
```

**Step 3: Compile paper**

```bash
xelatex draft_v3.tex && biber draft_v3 && xelatex draft_v3.tex
```

Both must compile cleanly.

**Step 4: Visual inspection of all ~44 slide pages**

Read the complete PDF. Check every slide for:
- Content correctness (propositions match paper)
- Figure quality (Paul Tol palette, serif fonts, thin lines)
- Hyperlink integrity (forward links from core, return links from backup)
- No overfull hboxes or layout issues

**Step 5: Clean build artifacts**

```bash
rm -f pres/presentation.aux pres/presentation.log pres/presentation.bbl pres/presentation.bcf pres/presentation.blg pres/presentation.run.xml pres/presentation.synctex.gz pres/presentation.out pres/presentation.toc pres/presentation.nav pres/presentation.snm
rm -f draft_v3.aux draft_v3.log draft_v3.bbl draft_v3.bcf draft_v3.blg draft_v3.run.xml draft_v3.synctex.gz draft_v3.out draft_v3.toc
```

**Step 6: Final commit**

If any fixes were needed during verification, commit them.

---

## Key Files Reference

| File | Role |
|------|------|
| `pres/presentation.tex` | Main deliverable (rewritten) |
| `pres/slides.bib` | Bibliography (copied from root) |
| `numerical/figures.py` | 3 new composite figure functions |
| `numerical/theme.py` | Unchanged (already polished) |
| `Makefile` | 3 new PDFs added to targets |
| `draft_v3.tex` | Single source of truth for all theory content |
| `pres/beamerthemeucl.sty` | UCL theme (unchanged) |
| `pres/banners/` | Institutional assets (unchanged) |
