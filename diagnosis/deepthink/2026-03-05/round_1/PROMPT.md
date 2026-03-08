# Theory + Numerical Audit — Liquidity, Activism Disclosure, and Takeover Premia (Round 5)

**Commit:** 4c63de2 (2026-03-05)
**Files uploaded:** 9 consolidated files covering the complete manuscript + numerical codebase + generated outputs + audit trail

## How to Read the Uploaded Files

| File | Contents |
|------|----------|
| 00_PROJECT_OVERVIEW.md | CLAUDE.md, git history, directory tree, Makefile |
| 01_PAPER.md | Complete LaTeX source of draft_v3.tex (the authoritative manuscript) |
| 02_PARAMS_MODEL.md | params.py + model.py (core economics: posteriors, prices, payoffs, welfare) |
| 03_SOLVER.md | solver.py (equilibrium solver: damped fixed-point iteration + Brent root-finding) |
| 04_EXPORT_FIGURES.md | export_data.py + figures.py + theme.py + __init__.py |
| 05_NUMERICAL_OUTPUT.md | All 13 CSVs + 2 LaTeX tables (generated equilibrium data) |
| 06_AUDIT_HISTORY.md | GPT Pro Round 2 theory audit meeting notes (previous round findings) |
| 07_CLAUDE_AUDIT.md | Claude's theory-to-code audit results from this session |
| 08_SUPPORTING.md | bibliography.bib |

Each file contains concatenated source with `## path/to/file` headers.
The manuscript (01) defines all equations; the code (02-04) implements them; the output (05) shows what the code produces.

---

## Previous Rounds Summary

This paper has undergone 4 previous rounds of multi-model theory auditing:

- **Rounds 1-3.5 (Gemini Deep Think, 2026-03-03):** Identified pricing recursion bug, introduced anonymous accumulation, exhaustive theory rewrite producing draft_v3.tex.
- **Round 4 (GPT Pro + Gemini + Claude, 2026-03-04):** GPT Pro identified 6 proof issues. Gemini proposed fixes. Claude found a gap in the Lemma 1 fix. GPT Pro Round 2 provided camera-ready patches. All 5 patches applied. The theory in draft_v3.tex is the corrected version.
- **Claude audit (2026-03-05):** Meticulous theory-to-code verification. 12/13 sections MATCH. One stale numerical claim fixed (line 638). Post-audit: tightened sensitivity ranges (ρ ±2%, s_ξ ±20%, δ ±2% around baseline), refactored solver kD boundary to use max(U_HOLD, U_QUIET) instead of hard switch, reformatted several equations for readability.

See files 06 and 07 for detailed audit trail.

---

## Your Task

**CRITICAL INSTRUCTIONS ON VERBOSITY AND DETAIL:**

This is a rigorous academic research project. Your response must be **exhaustive, meticulous, and complete**. Specifically:

1. **Do NOT abbreviate.** Do not say "the rest is analogous" or "remains unchanged" without providing a complete algebraic proof showing WHY it is unchanged.
2. **Do NOT provide proof sketches.** Provide complete proofs with every algebraic step shown.
3. **Do NOT summarize.** If a proposition needs rewriting, provide the complete camera-ready LaTeX, not a description of what it should say.
4. **Show ALL algebra.** Every derivative, every substitution, every simplification step.
5. **Your response should be VERY LONG.** A short response means you have abbreviated something. We expect and want a long, detailed response.
6. **For code changes:** Provide complete function implementations, not skeletons with "..." or "setup unchanged."
7. **For LaTeX changes:** Provide the exact replacement text with line number boundaries, ready to paste into the manuscript.
8. **Verify your own work.** After providing a fix, trace through it step by step to confirm correctness.

The cost of verbosity is zero. The cost of a gap in a proof is a desk reject. Err on the side of too much detail, never too little.

**CRITICAL INSTRUCTIONS ON INTELLECTUAL HONESTY:**

I am a serious academic researcher. I need your **honest, independent judgment** — not agreement, not flattery, not validation.

1. **Do NOT open with compliments.** Skip "brilliant," "impressive," "well-documented." Go straight to substance.
2. **Do NOT agree with my analysis just because I presented it.** If my root cause diagnosis is wrong, say so. If my proposed fix has a flaw I haven't seen, tell me.
3. **Challenge my assumptions.** If I claim something "must be structural," but you see a parametric fix I missed, say so. If I ruled out an approach prematurely, push back.
4. **Flag where I might be wrong.** Even if you broadly agree, identify the weakest points in my reasoning and stress-test them.
5. **Distinguish your confidence levels.** Say "I am confident that X" vs "I suspect Y but haven't verified" vs "Z is speculative." Do not present uncertain claims with false confidence.
6. **Prioritize correctness over my feelings.** A polite "your proof is flawed at step 3" is infinitely more valuable than an enthusiastic "great work, here's how to extend it."

I would rather receive a harsh, correct assessment that saves me from a referee embarrassment than a warm, agreeable one that lets an error through. Treat me as a colleague submitting to a top-5 journal, not as a student seeking encouragement.

---

## Focus Areas (CRITICAL)

This round has **four specific focus areas** in addition to a general pass on the paper. Address each one explicitly with its own section in your response.

### Focus 1: Solver Convergence Failures at Extreme κ

**Problem:** The equilibrium solver (`solver.py`, file 03) occasionally fails to converge or produces poor-quality equilibria at extreme κ values (κ < 0.15 or κ > 0.80). The `solve_valid` function attempts multi-start search with fallbacks but sometimes returns equilibria with high residuals.

**Specific concern:** The `equilibrium_residual` function (lines 40-81 of solver.py) now uses `U_lower(s) = max(U(HOLD, s), U(QUIET, s))` for the kD boundary (an improvement over the previous hard-switch logic). However, the collapsed-regime branch still has a one-sided check:

```python
elif (kD - k0) < TOL_REGION:
    # quiet region collapsed: only penalize if the lower action dominates PUBLIC above k0
    s_test = min(k0 + TOL_REGION, s_max)
    rD = max(0.0, U_lower(s_test) - U(Action.PUBLIC, s_test))
```

This `max(0.0, ...)` means if PUBLIC dominates HOLD/QUIET at the reported cutoff, the residual is zero — the solver thinks everything is fine when actually the cutoff should be lower. This may cause:
1. A kink/discontinuity in the Δ^min(κ) curve at the QV collapse point
2. Incorrect post-collapse cutoff values
3. Occasional solver failures when warm-starting from a bad collapsed-regime solution

**What I need:**
- Diagnose whether this is a real bug or an acceptable approximation
- If it's a bug, provide the corrected `equilibrium_residual` function
- Provide corrected `solve_equilibrium` function if the iteration logic also needs fixing
- Verify the fix doesn't break convergence at other κ values

### Focus 2: Recalibration of m₁ (0.30 → 0.45)

**Change made:** We increased m₁ from 0.30 to 0.45 to produce a more quantitatively visible hump shape in Δ^min(κ).

**Why:** With m₁=0.30, the activism premium wedge m̃−m₀ = 0.18 was so small that the Quiet Voice region was microscopic (width 0.015 in σ_s units) and the hump had only ~11% peak-to-trough amplitude. With m₁=0.45, the wedge is 0.315 and the QV region is 0.184 wide — an order of magnitude larger.

**What I need:**
- Is m₁=0.45 economically defensible? This means an activist who successfully engages can extract a 45% premium above standalone value (vs 10% baseline). Is this consistent with empirical evidence on activist-driven M&A premia?
- Does this violate any of the paper's assumptions (A1-A7)?
- Does this change the qualitative predictions of the model, or only the quantitative magnitudes?
- Are there alternative calibration strategies that would produce a visible hump without requiring such a large m₁?
- Specifically verify A5 (net deterrence): Δ̃ + m̃ − m₀ = 0.225 + 0.315 = 0.540 > 0.30 = ΔS. Does the large gap (0.540 vs 0.30) create any economic implausibility?

### Focus 3: Full Paper Pass (Proofs, Propositions, Claims)

With the updated calibration (m₁=0.45), do a complete pass on draft_v3.tex checking:

1. **All assumptions (A1-A7):** Are they all still satisfied with m₁=0.45? Are the assumption statements tight enough?
2. **All propositions and lemmas:** Do the proofs still hold? Pay special attention to:
   - Lemma 1 (QA domination) — uses belief-free lower bound
   - Lemma 2 (endpoint behavior) — purely Bayesian, no GE claims
   - Proposition 5 (nonmonotonicity) — decomposition + numerical verification
3. **All in-text numerical claims:** Any values that reference old calibration? I fixed line 638 but there may be others.
4. **Calibration discussion (Section 5):** Does the narrative about parameter choices make sense with m₁=0.45?
5. **Welfare results (Section 7):** Any claims that need updating?
6. **Extensions (Section 8):** Disclosure and noisy rumor results — do qualitative claims still hold?

### Focus 4: Collapsed-Regime (k₀ ≈ k_D) Equilibrium Quality

**Context:** At high κ, the Quiet Voice region collapses (k₀ → k_D). This is a genuine economic prediction: when noise is so high that order flow is nearly uninformative, the benefit of quiet engagement (trading information advantage without disclosure) vanishes.

**What I need:**
- At the collapse point, what is the equilibrium residual? Is U_Hold(k₀) = U_Public(k₀) properly enforced?
- Does the kink in Δ^min(κ) at the collapse point represent a genuine non-smoothness in the equilibrium correspondence, or is it a solver artifact?
- If it's a solver artifact, how should the post-collapse equilibrium be computed? Should the solver switch to a two-cutoff (k₁, k_D) regime with k₀ = k_D by constraint?
- Provide the corrected solver code if changes are needed.

---

## Deliverables

### Part 1: Focus Area Responses
Address each of the four focus areas above with:
- Complete diagnosis
- Complete corrected code (if applicable)
- Complete corrected LaTeX (if applicable)
- Verification that the fix is correct

### Part 2: Full Theory Audit
Beyond the focus areas, conduct a complete independent audit of the manuscript:
- Are there any false claims, overclaims, or unjustified assertions?
- Are there any proof gaps that could trigger a desk reject?
- Are the proofs self-contained (a reader shouldn't need to reconstruct missing steps)?
- Is the notation consistent throughout?
- Are figure descriptions accurate for what the code produces?

### Part 3: Calibration Strategy Discussion
Provide a thoughtful discussion of:
- The trade-offs in the m₁=0.45 calibration
- Alternative calibration strategies (different parameter combinations that achieve a visible hump)
- How to frame the calibration in the paper for maximum credibility with finance referees
- Empirical evidence that could support or challenge the chosen values

---

_Internal: snapshot_sha=4c63de2, round=1, date=2026-03-05_
