# Upload Instructions for Gemini Deep Think Round 2

**Date:** 2026-03-03

## Files to Upload (in order of importance)

### Required (upload all 4)

1. **`PROMPT.md`** (this directory)
   - The main prompt. Paste this as your message to Gemini, or upload as a file.
   - ~6,000 words. Covers 7 theoretical issues + full calibration diagnosis + 5 deliverables.

2. **`draft_v3.tex`** (root directory)
   - The complete manuscript (~1,438 lines). Gemini needs the full paper to fix proofs.
   - Contains all propositions, lemmas, proofs, assumptions table, calibration table.

3. **`numerical/model.py`**
   - The Python implementation (~650 lines). Every equation matches draft_v3.tex.
   - Gemini can verify proposed parameter changes against actual code formulas.

4. **`numerical/params.py`**
   - The parameter definitions (~180 lines). Contains the ModelParams dataclass.
   - Gemini needs this to see all current defaults and derived quantities.

### Strongly Recommended (upload if within file limit)

5. **`numerical/solver.py`** (~238 lines)
   - The equilibrium solver. Shows the fixed-point iteration structure.
   - Relevant for Issue T6 (Assumption A6 / contraction) and understanding convergence.

6. **`numerical_output/data/baseline_series.csv`**
   - The current (broken) numerical output showing Δ^min across κ values.
   - Gemini can see the actual numbers confirming the calibration failure.

### Optional Context (upload only if Gemini allows many files)

7. **`fix.md`** (root directory, ~950 lines)
   - The implementation plan that created draft_v3.tex. Provides history and rationale.
   - Helps Gemini understand WHY the current model architecture was chosen.

8. **`quality_reports/session_logs/2026-03-03_fixmd_review.md`**
   - Claude's detailed review of fix.md vs draft_v2.tex vs code.
   - Contains the Option A vs Option B analysis that led to current architecture.

## How to Use

1. **Go to:** Gemini 2.5 Pro with Deep Think mode enabled
2. **Upload files:** Start with #1-#4 (required). Add #5-#6 if within limits.
3. **Paste or reference PROMPT.md** as your input message
4. **Expected output:** ~3,000-5,000 words covering all 5 deliverables (D1-D5)
5. **Expected time:** 5-15 minutes in Deep Think mode

## What to Look For in Gemini's Response

- [ ] Does it address all 7 theoretical issues (T1-T7)?
- [ ] Are the proof fixes actual LaTeX-ready text, not just descriptions?
- [ ] Does the recalibration table include ALL parameters?
- [ ] Does it verify A5 holds with the new parameters?
- [ ] Does it provide the D3 verification calculations?
- [ ] Are the sufficient conditions for Prop 4 stated in terms of primitives?
- [ ] Is the economic narrative grounded in empirical citations?

## After Getting Results

Save Gemini's response to `diagnosis/deepthink/2026-03-03/round_2/RESPONSE.md` for Claude to review and implement.
