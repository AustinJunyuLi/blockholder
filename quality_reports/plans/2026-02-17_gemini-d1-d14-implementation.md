# Plan: Implement Gemini D1-D14 Surgical Revisions
**Date:** 2026-02-17
**Status:** COMPLETED (prose); PENDING (figures)

## Task Description
Implement 14 deliverables from Gemini Deep Think review into draft_v2.tex.

## Citation Key Mapping (Gemini to Actual Bib)
| Gemini Key | Actual Bib Key |
|---|---|
| `Bond2012` | `BondEdmansGoldstein2012` |
| `Edmans2012` | `EdmansGoldsteinJiang2012` |
| `Brav2008` | `BravJiangPartnoyThomas2008` |
| `Greenwood2009` | `GreenwoodSchor2009` |
| `Grossman1980` | `GrossmanHart1980` |
| `Edmans2011` | `EdmansManso2011` |
| `Edmans2013` | `EdmansFangZur2013` |
| `Glosten1985` | `GlostenMilgrom1985` |
| `Edmans2015` | `EdmansGoldsteinJiang2015` |
| `Dow2017` | `DowGoldsteinGuembel2017` |
| `Back2018` | `BackEtAl2018` |
| `Fang2009` | `FangPeress2009` (ADDED to bib) |

Keys already correct: Hirschman1970, Coffee1991, Bhide1993, Maug1998, Edmans2009, Kyle1985

## Deliverable Status

| # | Deliverable | Status |
|---|---|---|
| Foundation | TikZ preamble + FangPeress2009 bib entry | DONE |
| D1 | Abstract rewrite | DONE |
| D2 | Introduction restructure | DONE (citation keys corrected) |
| D3 | Literature review trim | DONE (citation keys corrected) |
| D4 | TikZ timeline figure | DONE |
| D5 | Engagement cost micro-foundation | DONE |
| D6 | Nonmonotonicity: Lemma (endpoints) + revised Prop 4 + shape remark | DONE |
| D7 | Existence via Brouwer + numerical uniqueness | DONE |
| D8 | Testable implications (5 predictions) | DONE |
| D9 | GE disclosure subsection (transparency/deterrence) | DONE |
| D10 | Expanded sensitivity analysis (rho, sigma_xi, delta) | DONE (prose) |
| D11 | Expanded noisy rumors (Bayesian posterior, wolf pack) | DONE |
| D12 | Welfare analysis subsection | DONE |
| D13 | Notation streamlining (m(a) to m^R(a), m(X,D) to bar-m) | DONE |
| D14 | Conclusion rewrite | DONE |
| Appendix | Brouwer proof, endpoint lemma, revised nonmonotonicity proof | DONE |

## D13 Notation Mapping (Applied)
| Old | New | Count |
|---|---|---|
| `m(a)` | `m^{R}(a)` | 21 instances (global replace) |
| `m(X,D)` | `\bar{m}(X,D)` | All instances (global replace, done in prior session) |
| `m(X,0)` | `\bar{m}(X,0)` | All instances (global replace) |
| `m(X,1)` | `\bar{m}(X,1)` | All instances (global replace) |
| `m(P,D)` | `\bar{m}(P,D)` | All instances (global replace, done in prior session) |
| `m(P(X,0),0)` | `\bar{m}(P(X,0),0)` | 1 instance (manual) |
| `m(X(P,D),D)` | `\bar{m}(X(P,D),D)` | 1 instance (manual) |
| `m(\cdot)` | `m^{R}(\cdot)` | 1 instance (manual) |
| `\tilde{m}` | `\tilde{m}` | No change |

## Compilation Verification
- XeLaTeX 3-pass + biber: PASSES (45 pages)
- No undefined citations
- No em-dashes
- Overfull hbox: 1 remaining at 7.74pt (below 10pt threshold)
- 21pt overfull at line 712-713: FIXED (split sentence)

## Figures Report
Written to: `quality_reports/plans/2026-02-17_figures-report.md`
- 5 new figures needed (3 sensitivity, 1 rumor precision, 1 welfare)
- 5 new functions in figures.py
- 1 new welfare computation in model.py
- Figure references to add in draft_v2.tex prose + appendix figure floats

## Risks (Resolved)
- Line numbers shift with each edit: mitigated by front-to-back order
- Citation key typos: verified all 12 corrections
- D13 mass substitution errors: verified with grep sweeps, no residuals
