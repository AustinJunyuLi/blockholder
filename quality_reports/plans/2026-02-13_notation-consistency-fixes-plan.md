# Notation Consistency Fixes — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Achieve full notation and terminology consistency across `draft_v2.tex`, `slides_v2.tex`, `handout.tex`, and `numerical/figures.py`.

**Architecture:** Four independent file-level tasks (one per file), then a verification pass. Each task is a batch of targeted text edits. No structural changes — all fixes are in-place replacements or small insertions.

**Tech Stack:** LaTeX (XeLaTeX + biber), Python (matplotlib labels), Edit tool for precise replacements.

---

### Task 1: Fix `slides_v2.tex` (6 edits)

**File:** `presentation/slides_v2.tex`

**Step 1: C1 — Swap B6 captions (lines 811, 814)**

The left figure panel shows D=0 (non-disclosed, varying prices); the right shows D=1 (disclosed, flat prices). Current captions are reversed.

Replace:
```latex
\column{0.48\textwidth}
\textbf{$D=1$ (disclosed):} Prices are high and nearly flat across $X$; $\pi = 1$ ensures full activism premium.

\column{0.48\textwidth}
\textbf{$D=0$ (non-disclosed):} Prices vary with $X$ as the market infers engagement probability from order flow.
```

With:
```latex
\column{0.48\textwidth}
\textbf{$D=0$ (non-disclosed):} Prices vary with $X$ as the market infers engagement probability from order flow.

\column{0.48\textwidth}
\textbf{$D=1$ (disclosed):} Prices are high and nearly flat across $X$; $\pi = 1$ ensures full activism premium.
```

**Step 2: m10 — Unify exp notation (line 265)**

Replace:
```latex
$C(s) = C_0\, e^{-\chi(s - \mu)/\sigma_s}$
```

With:
```latex
$C(s) = C_0 \exp\!\bigl(-\chi(s - \mu)/\sigma_s\bigr)$
```

**Step 3: m9 — Add color scheme footnote (after line 376)**

After the `\end{align*}` for the cutoff equations, insert a brief note. Replace:
```latex
\end{align*}

\vspace{0.2em}

\textbf{Note:} Hold and Quiet Voice produce the same order flow distribution --- the market cannot distinguish them.
```

With:
```latex
\end{align*}

\vspace{0.2em}

\textbf{Note:} Hold and Quiet Voice produce the same order flow distribution --- the market cannot distinguish them.
{\scriptsize (Region colors above are for visual distinction; they differ from the notation color scheme.)}
```

**Step 4: m7 — Regularity condition precision (line 785)**

Replace:
```latex
Specifically, $\delta\,\phi(\cdot)/\sigma_\xi < 1$.
```

With:
```latex
Specifically, $\delta\,\phi(0)/\sigma_\xi < 1$.
```

**Step 5: M4-slides — Invertibility note (after line 779)**

Replace:
```latex
  where $p(P, D) = 1 - \Phi\left(\frac{m(X, D) + K - \bar{S} + P}{\sigma_\xi}\right)$
```

With:
```latex
  where $p(P, D) = 1 - \Phi\left(\frac{m(X, D) + K - \bar{S} + P}{\sigma_\xi}\right)$

  {\scriptsize (We write $m(X,D)$ since $P(\cdot,D)$ is injective, so the bidder infers $X$ from $P$.)}
```

**Step 6: Verify — no other changes needed in slides**

Run: `grep -c "Passive Hold" presentation/slides_v2.tex` — expected: 0 (already uses "Hold")

---

### Task 2: Fix `handout.tex` (3 edits)

**File:** `presentation/handout.tex`

**Step 1: m8 — Reorder posterior denominators (lines 230–233)**

Replace the $\pi(-1,0)$ denominator (line 231):
```latex
  \pi(-1, 0) &= \frac{\omega_Q \cdot p_1}
    {\omega_E \cdot p_0 + (\omega_H + \omega_Q) \cdot p_1}, \\[4pt]
```

With:
```latex
  \pi(-1, 0) &= \frac{\omega_Q \cdot p_1}
    {(\omega_H + \omega_Q) \cdot p_1 + \omega_E \cdot p_0}, \\[4pt]
```

Replace the $\pi(0,0)$ denominator (line 233):
```latex
  \pi(0, 0) &= \frac{\omega_Q \cdot p_0}
    {\omega_E \cdot p_1 + \omega_H \cdot p_0 + \omega_Q \cdot p_0}, \\[4pt]
```

With:
```latex
  \pi(0, 0) &= \frac{\omega_Q \cdot p_0}
    {(\omega_H + \omega_Q) \cdot p_0 + \omega_E \cdot p_1}, \\[4pt]
```

**Step 2: M4-handout — Invertibility note (after line 342)**

Replace:
```latex
  \end{equation}
  A higher price raises the effective acquisition cost,
```

With:
```latex
  \end{equation}
  Since $P(\cdot,D)$ is injective (Assumption A7), the bidder infers $X$ from $P$;
  we write $m(X,D)$ as shorthand.
  A higher price raises the effective acquisition cost,
```

**Step 3: m5 — Fix m₁ label in calibration table (line 388)**

Replace:
```latex
Activist premium        & $m_1$           & 0.30  & Premium with engagement \\
```

With:
```latex
Success premium         & $m_1$           & 0.30  & Premium with successful engagement \\
```

---

### Task 3: Fix `draft_v2.tex` (~18 replacements)

**File:** `draft_v2.tex`

**Step 1: Global replace "Passive Hold" → "Hold"**

Use `replace_all: true` to change every occurrence of "Passive Hold" to "Hold" in `draft_v2.tex`.

This affects approximately 18 locations across:
- Body text (lines 60, 89, 227, 363, 376, 414, 429, 502, 509, 593)
- Equation labels (line 346)
- Proof appendix (lines 789, 815, 821, 842, 853, 938, 945, 952)
- Indifference conditions (lines 1064, 1065)
- Figure caption (line 1208)
- Notation table (lines 1317, 1319)

**Step 2: Spot-check critical contexts**

After replacement, read lines 502, 815, 842 to verify "Hold" reads naturally in these technical contexts:
- Line 502: should read "Exit, Hold, Quiet Voice, and Public Voice"
- Line 815: should read "separates Exit from Hold"
- Line 842: should read "Hold $H\equiv(0,0)$"

**Step 3: Verify**

Run: `grep -c "Passive Hold" draft_v2.tex` — expected: 0

---

### Task 4: Fix `numerical/figures.py` (1 edit)

**File:** `numerical/figures.py`

**Step 1: m6 — Fix probability operator in legend (line 331)**

Replace:
```python
        label="Base: $m_0 \\cdot \\Pr(\\mathrm{bid})$",
```

With:
```python
        label="Base: $m_0 \\cdot \\mathbb{P}(\\mathrm{bid})$",
```

**Step 2: Regenerate the decomposition figure**

Run: `cd /mnt/d/Dropbox/Blockholder/directory && python run_numerical.py`

This regenerates all figures including `fig_decomposition.pdf` with the corrected label. Verify the output PDF exists and is non-empty.

---

### Task 5: Verification Pass

**Step 1: Compile draft_v2.tex**

```bash
cd /mnt/d/Dropbox/Blockholder/directory
xelatex -interaction=nonstopmode draft_v2.tex
biber draft_v2
xelatex -interaction=nonstopmode draft_v2.tex
xelatex -interaction=nonstopmode draft_v2.tex
```

Check: zero new warnings, PDF exists and is non-empty.

**Step 2: Compile slides_v2.tex**

```bash
cd /mnt/d/Dropbox/Blockholder/directory/presentation
xelatex -interaction=nonstopmode slides_v2.tex
biber slides_v2
xelatex -interaction=nonstopmode slides_v2.tex
xelatex -interaction=nonstopmode slides_v2.tex
```

Check: zero new warnings, PDF exists.

**Step 3: Compile handout.tex**

```bash
cd /mnt/d/Dropbox/Blockholder/directory/presentation
xelatex -interaction=nonstopmode handout.tex
biber handout
xelatex -interaction=nonstopmode handout.tex
xelatex -interaction=nonstopmode handout.tex
```

Check: zero new warnings (pre-existing overfull hbox at line 123 is acceptable), PDF exists.

**Step 4: Final grep checks**

```bash
grep -c "Passive Hold" draft_v2.tex           # expect: 0
grep -c "Activist premium" presentation/handout.tex  # expect: 0
grep "\\\\Pr(" numerical/figures.py            # expect: no matches
```

**Step 5: Visual spot-check**

Open `slides_v2.pdf` backup slide B6 — confirm left caption says D=0, right says D=1, matching the figure panels.
