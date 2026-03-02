# Plan: Full Prose Polish for Top Finance Journals
**Date:** 2026-02-09
**Status:** APPROVED

## Task Description
Fundamentally polish the paper "Liquidity, Activism Disclosure, and Takeover Premia" so it reads appropriate for top finance journals (JF, JFE, RFS) instead of a math journal. Full overhaul of all sections, with assumptions integrated into narrative, full restructuring permitted, and all mathematical content preserved.

## Guiding Principles
1. **Lead with economics, follow with math** — every proposition gets a 1-2 sentence intuition preview
2. **Active voice** — "I show" or "The model predicts" instead of passive
3. **Shorter paragraphs** — one idea per paragraph (3-5 lines max)
4. **Stronger hooks** — the intro reads like a pitch, not a summary
5. **Assumptions integrated** — each assumption introduced where first needed, not in a separate block
6. **Preserve all math** — equations, propositions, proofs unchanged; only surrounding prose changes

## Section-by-Section Plan

### Introduction (rewrite)
- 8 shorter paragraphs (~1,000-1,100 words)
- Structure: Hook → Tension → Gap → This paper → Key result #1 → Key result #2 → Empirical relevance → Roadmap
- Open with concrete, vivid question
- State contribution assertively

### Literature Review (polish)
- Tighten paragraphs
- Active voice throughout
- Stronger "Relation to This Paper" subsection

### Model Section (restructure)
- Remove standalone "Model Assumptions" subsection
- Integrate A1-A8 into model description where each is first needed
- A6, A7 become footnotes/parentheticals
- A8 moves to non-monotonicity result
- Add bridge sentences between subsections
- Merge Blockholder Payoff + Equilibrium Concept

### Equilibrium Characterization (polish)
- Add intuition previews before each proposition
- Shorter economic interpretation paragraphs after propositions
- One insight per paragraph

### Numerical Illustration (polish)
- Frame calibration as grounding the theory
- Tighten figure descriptions
- Remove duplication between captions and body text

### Comparative Statics (polish)
- Lead with economic prediction, then formal statement
- Forward-looking language instead of apologetic

### Extensions (tighten)
- Stronger opening with policy framing
- Each extension ~250 words
- Tighter prose throughout

### Conclusion (restructure)
- Structure: What we learned → Policy implications → Future directions
- Frame limitations as exciting future work, not apologies
- 3 paragraphs max

## Team Structure
- **intro-agent**: Introduction + Literature Review
- **model-agent**: Model section + assumptions integration
- **equilibrium-agent**: Equilibrium Characterization + Prices/Premia
- **numerical-agent**: Numerical Illustration + Sensitivity
- **policy-agent**: Comparative Statics + Extensions + Conclusion
- **abstract-agent**: Abstract rewrite (after all sections done)
- **proofreader-agent**: Final meticulous pass on full draft

## Verification
- LaTeX compilation (3-pass XeLaTeX + biber)
- All cross-references resolve
- All equations preserved exactly
- No overfull hbox > 10pt
- Consistent terminology throughout
- Finance-journal tone in every section

## Risks
- Cross-reference breaks when restructuring assumptions
- Terminology inconsistencies between agents
- Over-editing that loses the author's voice
- Mitigation: proofreader agent does final consistency pass; user reviews before commit
