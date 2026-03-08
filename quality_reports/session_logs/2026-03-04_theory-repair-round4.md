# Session Log: Theory Repair Round 4

**Date:** 2026-03-04
**Branch:** theory-fixes
**Goal:** Fix 6 mathematical issues in draft_v3.tex identified by GPT Pro audit, using multi-model triangulation (GPT Pro → Gemini Deep Think → Claude verification → GPT Pro Round 2).

## Context

GPT Pro produced a hard-nosed theory audit (`diagnosis/gptpro/pro_v1.md`) identifying 6 issues:
- **P0 (Critical):** Lemma 2 right-endpoint claim — π(1,0) is κ-invariant, contradicts "converges to unconditional prior"
- **P0b (Critical):** Proposition 5 proof relies on broken Lemma 2 + invalid Jensen argument
- **P1:** Premium interpretation inconsistency (b=P+m vs b=V̂+m̄)
- **P2:** λ_B < 1/2 hidden restriction not formalized
- **P3:** Lemma 1 QA domination proof too loose
- **P4:** B.11 "by definition" misnomer, missing P(D=d|X) formulas

All 6 verified valid by numerical computation and Claude audit.

## Progress

1. ✅ Full codebase scan + theory verification (pre-compaction session)
2. ✅ Numerical falsification of Lemma 2: voice doesn't collapse, ω_P grows to 0.362 at κ=0.99
3. ✅ Packaged Deep Think Round 4 prompt → `diagnosis/deepthink/2026-03-04/`
4. ✅ Received Gemini fix → `diagnosis/fix4.md`
5. ✅ Meticulous Claude audit of Gemini fix: 5/6 correct, D5 has new "a fortiori" gap
6. ✅ Packaged GPT Pro Round 2 → `diagnosis/gptpro/2026-03-04/round_2/`
7. ✅ GPT Pro Round 2 received → `diagnosis/gptpro/2026-03-04/round_2_reply.md`
8. ✅ Meeting notes generated → `diagnosis/gptpro/2026-03-04/round_2_meeting_notes.md`
9. ✅ All 5 patches applied to `draft_v3.tex`:
   - Patch 1: Lemma 1 — explicit belief-free proof (Version 1 in main text, Version 2 as appendix remark with A8)
   - Patch 2: Lemma 2 + Prop 5 — numbered items (i)/(ii), explicit decomposition display, honestly labeled numerical monotonicities
   - Patch 3: Premium — already correct in v3
   - Patch 4: A7 — already present, added US M&A data justification sentence
   - Patch 5: P(D=1|X) explicit Bayes formula added after posterior derivation; B.11 "by definition" fixed
10. ✅ LaTeX compiles cleanly (54 pages, zero errors)

## Key Decisions

- D5 gap confirmed real by all 3 models (Claude, GPT Pro, Gemini's step was wrong)
- Lemma 1: Version 1 (no new assumptions, "for sufficiently high s") in main text; Version 2 (with A8) as appendix remark
- D2 monotonicity: cannot be proved analytically from GE primitives. Stated honestly as numerical comparative statics
- A7 (λ_B ≤ 1/2): defensible — annual bid incidences are single-digit percentages
- Hybrid analytic+numerical approach: standard practice, cited Edmans-Goldstein-Jiang as precedent

## Resolved Questions

- D5 gap is real (all 3 models agree). Fixed with belief-free lower bound: pα+(1-p)β ≥ min{α,β}
- Δ_base monotonicity cannot be proved analytically. Hybrid approach is standard for top journals if explicitly labeled
- A7 is economically defensible with one-sentence justification
