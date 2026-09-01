# Plan: the grand-tour report (2026-08-29)

Status: historical design note for `teach/report.html`. This is not learner
evidence. Current session state lives in `teach/NOTES.md`.

## Request

Austin asked for one polished interactive HTML report that: teaches every legal,
institutional and financial concept the project leans on, from zero university
footing; hammers home the research idea; then eases into the math for a holistic
view.

## Deliverable

`teach/report.html`. One file, links the shared `assets/lesson.css` and
`assets/quiz.js`, adds report-only CSS in a style block (sidebar contents,
widgets, progress). Course chrome kept: nav, glossary links, ask footer.

## Structure

Part 0. How to read this; the 30-second version.
Part I. The world the model lives in:
firms and agency; blockholders, exit and voice; what activists do;
takeovers, tender offers, premia, free riders, the wedge; how trading works,
order flow, price impact, liquidity = kappa; the law: 13D vs 13G, threshold
and window margins, other jurisdictions; the standoff.
Part II. The research idea:
the rule is the partition; clock equivalence and the one-way door; why
liquidity only bites in the pool; the object and the mechanism; two margins two
answers; the empirical anchor; what the paper refuses to claim.
Part III. The math, gently:
cast in symbols; prices as conditional expectations and the pricing loop;
plans, cutoffs, equilibrium; the ledger walked D1 to C1 with labels and
caveats; how the project knows what it knows.

## Interactive widgets (vanilla JS, exact where stated)

1. Timeline with tau and T sliders; cell label flips by the clock equivalence.
2. Kappa camouflage: exact one-round ternary toy; posterior at chosen order
   flow as kappa moves.
3. Partition mass mover: 40-type schematic. Both sliders move histories only
   from pooled to flagged. The L4 pooled-share direction applies to threshold
   tightening; window composition remains schematic and unsigned.
4. Attenuation calculator: S = (1 - Omega) S_P, and W times C with margin
   toggle (threshold clamps C, window does not).
5. Cutoff selector: k1, k2 sliders, ordered, three-plan regions.

## Facts discipline

Numbers only from: model_v4.md (smoke facts, check inventory, evidence notes),
CONTEXT.md, empirics README, legal_regime_portability.md, draft_v2 abstract and
introduction (literature anchors). 13G detail kept to what the sources support.

## Style

Unslop rules active: no em dashes, sentence-case headings, straight quotes,
plain words, no bold-label-colon list tells. Quiz answers equal word count.

## Verification

Initial build check: Playwright loaded the file, exercised each widget and quiz,
and checked full-page screenshots. Rerun current checks after any report or asset
edit. Record the result in `teach/NOTES.md`; do not treat record 0002 as learner
evidence.
