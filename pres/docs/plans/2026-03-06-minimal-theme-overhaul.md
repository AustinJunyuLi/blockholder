# Minimal Theme Overhaul — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the heavy UCL institutional Beamer theme with a light, airy, minimalistic design while keeping all content and the color-coded variable system.

**Architecture:** Create a new self-contained `beamerthememinimal.sty` that replaces the UCL banner machinery. A small UCL logo is placed in the top-right corner via TikZ. Frame titles sit on a white background with a thin navy accent line. Footer is just a slide number. Content slides get wider margins and larger base font — dense slides are split where needed.

**Tech Stack:** LaTeX/Beamer, TikZ, XeLaTeX, TeX Gyre Heros (already in use)

---

### Task 1: Create `beamerthememinimal.sty`

**Files:**
- Create: `pres/beamerthememinimal.sty`

This is the core theme file. It replaces the 4 UCL `.sty` files.

**Step 1: Write the theme file**

```latex
% beamerthememinimal.sty
% Light, airy Beamer theme with subtle UCL branding
\ProvidesPackage{beamerthememinimal}

\mode<presentation>

% --- Dependencies ---
\RequirePackage{tikz}
\RequirePackage{iftex}
\RequirePackage{calc}

% --- Fonts ---
\ifPDFTeX
  \RequirePackage[scaled]{helvet}
\else
  \RequirePackage{fontspec}
  \setsansfont{TeX Gyre Heros}
\fi
\renewcommand{\familydefault}{\sfdefault}

% --- Color Palette ---
\definecolor{mnNavy}{HTML}{1B2A4A}
\definecolor{mnBlue}{HTML}{3366A0}
\definecolor{mnBody}{HTML}{2D2D2D}
\definecolor{mnGray}{HTML}{999999}
\definecolor{mnLightGray}{HTML}{E0E0E0}
\definecolor{mnAccent}{HTML}{CC6677}

% --- Beamer color assignments ---
\setbeamercolor{normal text}{fg=mnBody}
\setbeamercolor{structure}{fg=mnNavy}
\setbeamercolor{frametitle}{fg=mnNavy}
\setbeamercolor{alerted text}{fg=mnAccent}
\setbeamercolor{example text}{fg=mnBlue}
\setbeamercolor{title}{fg=mnNavy}
\setbeamercolor{subtitle}{fg=mnBody}
\setbeamercolor{author}{fg=mnBody}
\setbeamercolor{institute}{fg=mnGray}
\setbeamercolor{date}{fg=mnGray}
\setbeamercolor{block title}{fg=mnNavy}
\setbeamercolor{block body}{fg=mnBody}
\setbeamercolor{block title alerted}{fg=mnAccent}
\setbeamercolor{block body alerted}{fg=mnBody}
\setbeamercolor{block title example}{fg=mnBlue}
\setbeamercolor{block body example}{fg=mnBody}
\setbeamercolor{footline}{fg=mnGray}
\setbeamercolor{itemize item}{fg=mnNavy}
\setbeamercolor{itemize subitem}{fg=mnGray}
\setbeamercolor{enumerate item}{fg=mnNavy}

% --- Beamer font assignments ---
\setbeamerfont{title}{series=\bfseries,size=\Large}
\setbeamerfont{subtitle}{size=\normalsize}
\setbeamerfont{frametitle}{series=\bfseries,size=\large}
\setbeamerfont{framesubtitle}{size=\normalsize,series=\mdseries}
\setbeamerfont{block title}{series=\bfseries,size=\normalsize}
\setbeamerfont{footline}{size=\tiny}

% --- Margins ---
\setbeamersize{text margin left=2.5em, text margin right=2.5em}

% --- Remove navigation symbols ---
\setbeamertemplate{navigation symbols}{}

% --- Itemize: small circles ---
\setbeamertemplate{itemize item}{\small\raise0.5pt\hbox{\textbullet}}
\setbeamertemplate{itemize subitem}{\scriptsize\raise0.5pt\hbox{\textbullet}}
\setbeamertemplate{itemize subsubitem}{\scriptsize\raise0.5pt\hbox{--}}

% --- Block templates: no boxes, just bold title + spacing ---
\setbeamertemplate{block begin}{%
  \par\vskip0.6em%
  {\usebeamerfont{block title}\usebeamercolor[fg]{block title}\insertblocktitle\par}%
  \vspace{0.15em}%
  \begingroup\usebeamerfont{block body}\usebeamercolor[fg]{block body}\ignorespaces
}
\setbeamertemplate{block end}{\par\endgroup\vskip0.4em}

\setbeamertemplate{block alerted begin}{%
  \par\vskip0.6em%
  {\usebeamerfont{block title}\usebeamercolor[fg]{block title alerted}\insertblocktitle\par}%
  \vspace{0.15em}%
  \begingroup\usebeamerfont{block body}\usebeamercolor[fg]{block body alerted}\ignorespaces
}
\setbeamertemplate{block alerted end}{\par\endgroup\vskip0.4em}

\setbeamertemplate{block example begin}{%
  \par\vskip0.6em%
  {\usebeamerfont{block title}\usebeamercolor[fg]{block title example}\insertblocktitle\par}%
  \vspace{0.15em}%
  \begingroup\usebeamerfont{block body}\usebeamercolor[fg]{block body example}\ignorespaces
}
\setbeamertemplate{block example end}{\par\endgroup\vskip0.4em}

% --- UCL logo dimension ---
\newlength{\logoheight}
\setlength{\logoheight}{0.65cm}

% --- Frame title with accent line + UCL logo ---
\setbeamertemplate{frametitle}{%
  \vskip0.6em%
  \begin{beamercolorbox}[wd=\textwidth]{frametitle}%
    \usebeamerfont{frametitle}\usebeamercolor[fg]{frametitle}%
    \insertframetitle%
    \ifx\insertframesubtitle\@empty\else%
      \\[0.15em]{\usebeamerfont{framesubtitle}\usebeamercolor[fg]{framesubtitle}\insertframesubtitle}%
    \fi%
  \end{beamercolorbox}%
  \vskip0.2em%
  {\color{mnNavy}\hrule height 1.5pt}%
  \vskip0.5em%
  % UCL logo in top-right corner
  \begin{tikzpicture}[remember picture, overlay]
    \node[anchor=north east, inner sep=0pt]
      at ([xshift=-1em, yshift=-0.5em] current page.north east)
      {\includegraphics[height=\logoheight, trim=315bp 0 0 0, clip]
        {theme/ucl/banners/uclbannerblack}};
  \end{tikzpicture}%
}

% --- Footline: just slide number ---
\setbeamertemplate{footline}{%
  \vskip0.3em%
  {\color{mnLightGray}\hrule height 0.3pt}%
  \vskip0.3em%
  \hfill{\usebeamerfont{footline}\usebeamercolor[fg]{footline}\insertframenumber}\hspace{2em}%
  \vskip0.4em%
}

% --- Title page ---
\defbeamertemplate*{title page}{minimal}{%
  \vfill
  \begin{center}
    % UCL logo above title
    \includegraphics[height=1cm, trim=315bp 0 0 0, clip]
      {theme/ucl/banners/uclbannerblack}\\[1.5em]
    {\usebeamerfont{title}\usebeamercolor[fg]{title}\inserttitle\par}%
    \ifx\insertsubtitle\@empty\else%
      \vskip0.5em%
      {\usebeamerfont{subtitle}\usebeamercolor[fg]{subtitle}\insertsubtitle\par}%
    \fi%
    \vskip1.2em%
    {\usebeamerfont{author}\usebeamercolor[fg]{author}\insertauthor\par}%
    \vskip0.3em%
    {\usebeamerfont{institute}\usebeamercolor[fg]{institute}\insertinstitute\par}%
    \ifx\insertdate\@empty\else%
      \vskip0.3em%
      {\usebeamerfont{date}\usebeamercolor[fg]{date}\insertdate\par}%
    \fi%
  \end{center}
  \vfill
}

% --- Headline: empty (no banner) ---
\setbeamertemplate{headline}{}

% --- Background: plain white ---
\setbeamertemplate{background}{}

\mode<all>
```

**Step 2: Compile a minimal test**

Create a 2-slide test document to verify the theme loads:
```bash
cd pres && xelatex -interaction=nonstopmode -halt-on-error presentation.tex
```

**Step 3: Commit**

```bash
git add pres/beamerthememinimal.sty
git commit -m "feat(pres): add minimal beamer theme"
```

---

### Task 2: Rewrite presentation.tex preamble

**Files:**
- Modify: `pres/presentation.tex:24-120` (preamble section)

**Step 1: Replace the preamble**

Replace lines 24–120 with:

```latex
\documentclass[aspectratio=169,11pt]{beamer}
\usepackage{beamerthememinimal}

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

% --- Serif math ---
\usefonttheme[onlymath]{serif}

% --- Math macros ---
\newcommand{\E}{\mathbb{E}}
\newcommand{\PP}{\mathbb{P}}
\newcommand{\1}{\mathbf{1}}
\newcommand{\Var}{\mathrm{Var}}
\newcommand{\R}{\mathbb{R}}

% --- Color-coded variable system (refined for light bg) ---
\colorlet{txblue}{mnNavy!85!black}
\colorlet{txrose}{mnGray!70!black}
\colorlet{txgreen}{mnBlue!70!mnNavy}
\newcommand{\choice}[1]{{\color{txblue}#1}}
\newcommand{\obs}[1]{{\color{txrose}#1}}
\newcommand{\outcome}[1]{{\color{txgreen}#1}}

% --- Hyperlinks ---
\hypersetup{colorlinks=true, linkcolor=mnBlue, urlcolor=mnBlue, citecolor=mnBlue}

% --- Navigation helpers ---
\newcommand{\backuplink}[2]{%
  \hfill{\scriptsize\hyperlink{#1}{\textcolor{mnBlue}{#2\,$\nearrow$}}}%
}
\newcommand{\returnlink}[2]{%
  \par\vspace{0.2em}\hfill{\scriptsize\hyperlink{#1}{\textcolor{mnBlue}{$\leftarrow$\,#2}}}%
}

% --- Title ---
\title{Liquidity, Activism Disclosure,\\ and Takeover Premia}
\subtitle{Exit, Voice, and Corporate Control}
\author{Austin Li}
\institute{University College London}
\date{}
```

Key changes:
- `\usetheme{ucl}` + `\useoutertheme{ucltitlebanner}` → `\usepackage{beamerthememinimal}`
- All UCL color overrides removed (theme handles it)
- Color-coded variable system uses new palette names
- All block template overrides removed (theme handles it)
- Navigation symbol removal handled by theme
- Footer template handled by theme

**Step 2: Update title frame**

Replace lines 135–139:
```latex
\begin{frame}[plain,noframenumbering]
  \hypertarget{main:title}{}
  \titlepage
\end{frame}
```

The `[plain]` option removes the frametitle/footline for the title slide.

**Step 3: Compile and verify**

```bash
cd pres && xelatex -interaction=nonstopmode presentation.tex
```

**Step 4: Commit**

```bash
git add pres/presentation.tex
git commit -m "feat(pres): switch to minimal theme, rewrite preamble"
```

---

### Task 3: De-cramp content slides — remove font size overrides

**Files:**
- Modify: `pres/presentation.tex` (all `\small`, `\footnotesize`, `\scriptsize` commands)

**Step 1: Remove all font-size overrides from main slides**

Go through each frame in the core slides (slides 2–16) and:
1. Remove `\small`, `\footnotesize`, `\scriptsize` declarations at the start of frames
2. Increase `\itemsep` values from 0.15em/0.2em to 0.6em–0.8em
3. Adjust column widths to give figures more room (aim for 55-60% for figure columns)
4. Remove `\vspace{0.3em}` micro-adjustments — let the theme's natural spacing work

Specific frames to adjust (with approach):

| Frame | Current issue | Fix |
|-------|--------------|-----|
| Slide 2 (Motivation) | `\small`, tight itemsep | Remove `\small`, widen itemsep to 0.6em |
| Slide 3 (Literatures) | `\small`, 3 cramped columns | Remove `\small`, itemsep 0.5em |
| Slide 4 (Disclosure) | `\footnotesize`, dense table + lists | Split into 2 slides (see Task 4) |
| Slide 5 (Notation) | `\scriptsize`, 2 dense notation tables | Split into 2 slides (see Task 4) |
| Slide 6 (Timeline) | `\footnotesize`, table + text | Remove size override, keep layout |
| Slide 7 (Pricing) | `\footnotesize`, dense equations | Split into 2 slides (see Task 4) |
| Slides 8–14 | Various `\footnotesize` | Remove, adjust spacing |
| Slide 15 (Theory) | `\small`, fine as-is | Remove `\small` |
| Slide 16 (Summary) | `\small`, fine | Remove `\small` |

For backup slides: keep `\small` or `\footnotesize` — these are reference slides where density is acceptable.

**Step 2: Compile and check for overflow**

```bash
cd pres && xelatex -interaction=nonstopmode presentation.tex 2>&1 | grep -i "overfull"
```

Fix any overfull hbox warnings by adjusting column ratios or splitting content.

**Step 3: Commit**

```bash
git add pres/presentation.tex
git commit -m "style(pres): remove font-size overrides, increase spacing"
```

---

### Task 4: Split dense slides for breathing room

**Files:**
- Modify: `pres/presentation.tex`

Split these 3 slides into 2 each (adding ~3 slides, total goes from 16 to ~19):

**4a: Disclosure slide → "Institutional Context" + "Model Translation"**

Slide 4a: Institutional Context
- Institutional trigger (US/UK thresholds)
- Quiet Voice vs Public Voice comparison table
- Full width, no columns needed

Slide 4b: Model Translation
- Model variables (q, a, z, X, D)
- Regime split (D=1 vs D=0)
- Full width or gentle two-column

**4b: Notation Guide → "Notation: Choices & Market" + "Notation: Outcomes"**

Slide 5a: Choices & Observables
- Blockholder choices table (left)
- Market observables table (right)
- Comfortable two-column at normal font size

Slide 5b: Outcomes & Mechanism Chain
- Outcomes table
- Mechanism chain figure (full width below)

**4c: Feed-Forward Pricing → "Engagement & Standalone Value" + "Bid Entry & Prices"**

Slide 7a: Engagement & Standalone Value
- Engagement technology equation
- Standalone value V-hat
- Feed-forward logic sentence

Slide 7b: Bid Entry & Prices
- Bid probability formula
- Post-disclosure and execution price
- No-fixed-point emphasis

**Step 1: Implement the splits**

For each split, preserve all `\hypertarget` labels on the first of the two slides so backup links still work. Update `\backuplink` targets if needed.

**Step 2: Compile and verify all hyperlinks work**

```bash
cd pres && xelatex presentation.tex && biber presentation && xelatex presentation.tex && xelatex presentation.tex
```

Check that all backup ↗ and ← links navigate correctly in the PDF.

**Step 3: Commit**

```bash
git add pres/presentation.tex
git commit -m "refactor(pres): split 3 dense slides for breathing room"
```

---

### Task 5: Polish individual slide layouts

**Files:**
- Modify: `pres/presentation.tex`

Go through each remaining slide and apply these layout rules:

1. **Figure slides** (Main Result, Decomposition, Disclosure, Prices): give the figure column 58–60% width
2. **Two-column text slides** (Literatures, Theory Status, Summary): use 48/48 split with 4% gap
3. **Tables**: add `\renewcommand{\arraystretch}{1.25}` for comfortable row spacing
4. **Equations**: add `\vskip0.4em` above and below display math for breathing room
5. **Backup links**: keep at bottom-right but ensure they don't crowd content — add `\vfill` before them

Also adjust the Summary/Thank You slide:
- Center the 4 blocks in a 2×2 grid with generous spacing
- Make "Thank you." more prominent (larger, with vertical space above)

**Step 1: Apply layout polish**

Work through slides sequentially, adjusting column ratios, spacing, and alignment.

**Step 2: Compile and visually inspect**

```bash
cd pres && xelatex presentation.tex && biber presentation && xelatex presentation.tex
```

Open the PDF and check every slide for:
- [ ] No text touching margins
- [ ] No overfull boxes
- [ ] Figures have breathing room
- [ ] Equations are not cramped
- [ ] Consistent spacing across slides

**Step 3: Commit**

```bash
git add pres/presentation.tex
git commit -m "style(pres): polish slide layouts, improve spacing"
```

---

### Task 6: Tune the UCL logo trim and accent colors

**Files:**
- Modify: `pres/beamerthememinimal.sty`

The `trim=315bp 0 0 0` value for extracting the UCL logo from the banner is approximate. After compilation:

**Step 1: Open the PDF and check the logo**

- Is just the UCL tower + text visible?
- Is it the right size (~0.65cm height)?
- Adjust `trim` values if too much or too little of the banner is showing

**Step 2: Check accent line color and weight**

- Does the 1.5pt navy line look good?
- Too heavy → reduce to 1pt
- Too light → increase to 2pt

**Step 3: Check color-coded variables**

- Are `txblue`, `txrose`, `txgreen` visible and distinct on white background?
- Adjust if any color is too faint or too saturated

**Step 4: Commit**

```bash
git add pres/beamerthememinimal.sty pres/presentation.tex
git commit -m "fix(pres): tune logo trim, accent colors, variable palette"
```

---

### Task 7: Final compilation and verification

**Files:**
- All presentation files

**Step 1: Clean build**

```bash
cd pres && rm -f presentation.aux presentation.bbl presentation.bcf presentation.blg presentation.log presentation.nav presentation.out presentation.run.xml presentation.snm presentation.toc
xelatex presentation.tex && biber presentation && xelatex presentation.tex && xelatex presentation.tex
```

**Step 2: Verify**

- [ ] No compilation errors or warnings (except font substitution)
- [ ] All hyperlinks work (backup ↗ and return ←)
- [ ] Title slide: UCL logo centered, clean layout
- [ ] Content slides: UCL logo top-right, accent line under title
- [ ] Footer: just slide number, right-aligned
- [ ] No text overflow on any slide
- [ ] Color-coded variables legible
- [ ] Figures have adequate space
- [ ] Backup slides render correctly

**Step 3: Commit**

```bash
git add pres/
git commit -m "feat(pres): complete minimal theme overhaul"
```
