# Design: Presentation Preparation Documents

**Status:** APPROVED
**Date:** 2026-03-05
**Context:** 20-25 min finance/econ faculty seminar, Monday. Interruptions expected, 5 min Q&A.

---

## Document 1: Comprehensive Lecture Notes (~30-40 pages)

**Purpose:** Private technical bible — every derivation, every step, every "why."

### Sections

1. **Model Primitives** — full setup, all assumptions A1-A7 spelled out with economic motivation
2. **Timeline & Actions** — complete action space with payoff expressions for each action
3. **Equilibrium Theory** — Props 1-4 with full proofs/proof sketches
4. **Bayesian Inference** — complete posterior derivations (Prop 2), conditional means (Lemma 3), inverse Mills ratios
5. **Pricing** — feed-forward chain fully derived (Prop 3), bid probability, P_trade, P_post
6. **Main Results** — Prop 5 (hump shape) with decomposition math, endpoint behavior (Lemma 2)
7. **Disclosure & Policy** — Props 6-7, PE vs GE distinction, transparency vs deterrence
8. **Welfare** — Delta^min definition, total surplus comparison, distributional trade-off
9. **Calibration** — all 16 parameters with economic justification
10. **Numerical Facts** — key numbers from solver (kappa-dagger location, collapse points, etc.)

**Output:** `pres/lecture_notes.md`

---

## Document 2: Presenter's Companion (~4 pages)

**Purpose:** Podium document. Glanceable, interrupt-resilient.

### Sections

1. **Talk Map** — one-line-per-slide roadmap with timing targets and transition phrases
2. **Key Objects Cheat Sheet** — 8-10 most important equations at fingertips
3. **Interrupt Recovery Guide** — per-section "if derailed, say X to get back"
4. **Anticipated Q&A** — 15-20 likely questions with 2-3 sentence answers, organized by inline vs end
5. **Literature Synopses** — all 10 cited papers + important uncited (Hirschman, Coffee, Bhide, wolf packs, etc.), 3-4 sentences each
6. **Danger Zones** — things NOT to say, known weaknesses (numerical uniqueness, Lemma 1 gap), graceful deflections

**Output:** `pres/presenter_companion.md`

---

## Source Material

- Presentation: `pres/presentation.tex` (16 main + 23 backup slides)
- Manuscript: `draft_v3.tex` (1462 lines, full proofs)
- Bibliography: `pres/slides.bib` (25 entries, 10 cited)
- Numerical code: `numerical/` (model.py, solver.py, params.py)
- Theory repair notes: `diagnosis/` (GPT Pro patches, Gemini fixes, known gaps)
- Numerical verification: `diagnosis/gptpro/2026-03-04/round_2/codebase/NUMERICAL_VERIFICATION.md`

## Known Weak Spots to Address

- **Lemma 1 (D5):** "a fortiori" gap — all 3 audit models agree it's real. GPT Pro Patch 1 provides belief-free lower-bound fix.
- **Numerical uniqueness (A6):** Not proven analytically — only verified by multi-start solver.
- **Prop 5 hump shape:** Weierstrass guarantees peak exists, but single-peakedness is numerical not analytic.
- **omega_Q -> 0 claim (D1):** Unproved GE result in Lemma 2.
