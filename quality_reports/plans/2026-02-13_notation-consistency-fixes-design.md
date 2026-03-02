# Design: Systematic Notation & Consistency Fixes
**Date:** 2026-02-13
**Status:** APPROVED

## Task Description
Fix all notation and consistency issues identified in the devil's advocate report
(`quality_reports/devils-advocate-2026-02-13-presentation.md`) and notation consistency
audit (`quality_reports/notation-consistency-2026-02-13.md`). The goal is full cross-document
alignment between `draft_v2.tex`, `slides_v2.tex`, `handout.tex`, and `numerical/figures.py`.

**Constraint:** The talk is 25–30 minutes, so no new slides or lengthy additions.

## User Decisions
- **Terminology:** Use "Hold" everywhere (not "Passive Hold")
- **Bid formula:** Add brief invertibility note (not change formula)
- **Minor issues:** Fix all of them

## Files to Modify
- `draft_v2.tex` — ~18 "Passive Hold" → "Hold" replacements
- `presentation/slides_v2.tex` — B6 caption swap, invertibility note, φ(0), exp(·), color note, m₁ label
- `presentation/handout.tex` — invertibility note, posterior reordering, m₁ calibration label
- `numerical/figures.py` — `\Pr` → `\mathbb{P}` in legend (line 331)

## Fix Inventory

### Critical (1)
| ID | Issue | File | Lines | Fix |
|----|-------|------|-------|-----|
| C1 | Swapped B6 captions | slides_v2.tex | 811, 814 | Swap left/right: left→D=0, right→D=1 |

### Major (2)
| ID | Issue | File | Lines | Fix |
|----|-------|------|-------|-----|
| M1 | "Passive Hold" → "Hold" | draft_v2.tex | ~18 locations | Global replace |
| M4 | m(X,D) in p(P,D) without invertibility note | slides_v2.tex ~779, handout.tex ~339 | Add parenthetical: "Since P(·,D) is injective (A7), bidder recovers X; we write m(X,D) for brevity." |

### Minor (6)
| ID | Issue | File | Lines | Fix |
|----|-------|------|-------|-----|
| m5 | m₁ description mismatch | handout.tex L388 | "Activist premium" → "Success premium" |
| m6 | Pr(bid) vs P(bid) in figures | figures.py L331 | `\Pr` → `\mathbb{P}` |
| m7 | Regularity condition φ(·) vs φ(0) | slides_v2.tex L785 | φ(·) → φ(0) |
| m8 | Posterior denominator ordering | handout.tex L231, 233 | Reorder to match draft/slides |
| m9 | Action-region color scheme note | slides_v2.tex ~375 | Add footnote about colors |
| m10 | exp(·) vs e^(·) | slides_v2.tex ~265 | e^{…} → \exp(…) |

## Verification
1. Recompile `draft_v2.tex` (3-pass XeLaTeX + biber) — zero new warnings
2. Recompile `slides_v2.tex` (3-pass XeLaTeX + biber) — zero new warnings
3. Recompile `handout.tex` (3-pass XeLaTeX + biber) — zero new warnings
4. Regenerate decomposition figure: `python run_numerical.py` (or targeted figure regen)
5. Visual check: B6 captions match figure panels
6. Grep confirm: zero remaining "Passive Hold" in draft

## Risks
- **Draft "Passive Hold" may appear in non-obvious contexts** (e.g., mid-sentence where "Hold" reads ambiguously). Mitigation: review each replacement in context.
- **Figure regeneration may shift layout** if other code changed. Mitigation: diff the output PDF.
- **exp(·) change on slides may cause overfull hbox** if the expression is wider. Mitigation: check log after compile.
