# Presentation Notes Overhaul Design

## Goal
Bring `pres/lecture_notes.tex` and `pres/presenter_companion.tex` into full alignment with the revised slide deck and manuscript posture.

## Scope
- `pres/lecture_notes.tex` becomes an appendix-style technical note meant for hand derivation and pre-seminar preparation.
- `pres/presenter_companion.tex` becomes a dual-use document with a podium layer and a hardball-defense layer.
- Both outputs must reflect the current narrowed claims:
  - baseline disclosed branch as a maintained baseline action-set feature,
  - hump as a baseline numerical result,
  - existence under maintained regularity,
  - uniqueness as numerical fixed-point selection,
  - welfare and GE disclosure effects as preliminary / heuristic.

## Design

### 1. Technical Note
`pres/lecture_notes.tex` should stop being a loose hybrid of old theory and repair notes. It should become a coherent technical note with a clean logic:
- model primitives and timing,
- action payoffs and information structure,
- cutoff logic,
- belief derivations,
- pricing derivations,
- bidder problem,
- minority-gains decomposition,
- numerical and heuristic sections clearly marked,
- a final “what to derive by hand” checklist.

The note should be useful as a derivation workbook. Every important object should be written in a way that can be reconstructed from scratch at a whiteboard.

### 2. Presenter Companion
`pres/presenter_companion.tex` should become operational rather than encyclopedic. It should open with a compressed talk path and then branch into defense material:
- main-deck speaking script,
- slide objectives and transitions,
- interruption recovery lines,
- standard objections with short and long answers,
- explicit vulnerable points and how to answer them honestly,
- backup-slide map.

### 3. Alignment Rules
Both files must use the same theory-status language:
- `analytic`
- `numerical`
- `heuristic`
- `maintained modeling choice`

Both files must avoid stale overclaims and obsolete references to stronger theorem status.

## Verification
- Compile both LaTeX files successfully.
- Confirm the generated PDFs exist.
- Remove LaTeX intermediate files after compilation.
