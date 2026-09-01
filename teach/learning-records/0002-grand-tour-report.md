# 0002: the grand-tour report

Status: artifact record. This file records a course deliverable, not learner
evidence. Do not use it to set Austin's demonstrated knowledge.

Austin asked for one polished interactive HTML report that teaches the project
from zero footing: the legal, institutional and financial background, the
research idea, then the math eased in.

## What was built

`teach/report.html`, linking the shared `assets/lesson.css` and
`assets/quiz.js`. Three parts: the world the model lives in, seven sections
from the agency problem to 13D versus 13G; the research idea, partition through
refusals; the math, symbols through the ledger walk and the verification
culture. Five widgets: the model disclosure clock, kappa camouflage (exact ternary
arithmetic), the one-way door, attenuation arithmetic, and the cutoff rule.
Three quiz checkpoints with six questions.

## Decisions

- The report is a companion to the lesson sequence, not a numbered lesson. It
  reuses course chrome and vocabulary but stands alone.
- Widget arithmetic is exact where the theory is exact: the camouflage toy is
  the one-round ternary market with informed mark twice the noise size; the
  clock widget enforces the D1 equivalence; the door widget enforces one-way
  pooled-to-flagged classification. The pooled-share direction is a threshold
  result under L4. Window composition is schematic and has no general sign.
  Magnitudes in the widget are labelled as schematic.
- The 13G section stays within what legal_regime_portability.md and the
  empirics README support. No deadline detail beyond the sources.
- Honesty labels and the three caveat blocks (A(tau) failing, A6 jumps, four
  unresolved nodes) are stated in the report at statement level, matching the
  model note. Nothing was strengthened.

## Verification

This was the initial build check. Playwright against a local server was console
clean apart from a favicon 404. Each widget, quiz, and the desktop and 800px
layouts was exercised. Rerun current checks after any report or asset edit.

## Next measurement point

The report's whiteboard test is a practice prompt, not evidence by itself. Use
the current live gate in `teach/NOTES.md` to decide what Austin has demonstrated.
