# Spec — v4 repositioning of the blockholder paper

Status: ready-for-agent · Written 2026-08-19 from the grilling session (no new interview). Vocabulary: `CONTEXT.md`. Decisions: `docs/adr/0001–0005`.

## Problem Statement

The author has a pure-theory paper (draft_v2) whose headline results were found, on referee review (2026-08-19), to be overclaimed on originality, margin-dependent in sign, small at baseline, and anchored on a natural experiment already used by three other papers and by the author's own side proposal. The modelling is judged messy. The supervisor has read draft_v2 and expects a recognizable descendant, but has asked for out-of-the-box thinking. A department review is due around December 2026 and needs a full draft.

## Solution

Find the best defensible position for the paper by reading the literature in full, then rebuild the paper around it: a clean core model with one honestly-labelled main result, an empirical specification that passes the referee checklist, one clean empirical result on data already in hand, a v4 memo, a compiled draft_v3, and a sketch of a supervisor note. Everything is done in the v4 worktree, ticket by ticket, with separate verifiers, and the author is consulted at the two decision points (position; theory ambition).

## User Stories

1. As the author, I want ~30 papers read in full (not abstracts) and summarized as structured cards, so that positioning rests on what the papers actually prove and estimate.
2. As the author, I want a competitor scope table showing exactly which object, margin and identification each competitor occupies, so that whitespace is visible, not asserted.
3. As the author, I want several independent position proposals judged and adversarially checked, so that the choice is not one agent's taste.
4. As the author, I want to see the winning position and the runner-up with their trade-offs before anything is edited, so that I make the call.
5. As the author, I want the core model restated from minimal primitives, so that the paper reads clean and the proofs are re-derivable.
6. As the author, I want the main result stated with a proof route and an honesty label, so that I never claim more than is proved.
7. As the author, I want to be asked how much new theory to take on once the winner is known, so that I don't commit to what I cannot robustly deliver.
8. As the author, I want an empirical spec (design, sample, variables, identification, confounds, power, placebos, parser validation) written before any regression, so that results are pre-specified.
9. As the author, I want the one headline empirical test actually run on data on disk, so that December has a number.
10. As the author, I want any needed WRDS/SSRN login to be requested from me explicitly and only when needed, so that nothing depends on a fresh pull.
11. As the author, I want a `framework_v4` memo (position, model, empirics, edit map, slide outline), so that the plan is one document.
12. As the author, I want a compiling `draft_v3.tex` with the repositioned intro, the new model section and the empirical-design section, so that the December draft is real, not promised.
13. As the author, I want a two-page supervisor-note sketch (what stayed, what changed, why), so that another agent can polish it.
14. As the author, I want each stage committed on branch `v4` and logged, so that any checkpoint is recoverable after a context reset.
15. As the author, I want the paper never to say "job-market paper" or name a journal, so that the draft is simply a good draft.

## Implementation Decisions

- Process: mattpocock main flow with a local `.scratch/` tracker; one ticket per fresh session; each ticket run by a bounded parallel Agent team (≤12), finder ≠ verifier, verifiers prompted to refute; no dynamic Workflow tool (ADR-0005).
- Literature access: ego-browser through the author's browser; Wiley (JF, Econometrica), OUP (RFS), NBER open with UCL; JFE via SSRN/NBER/author working-paper versions (ScienceDirect and JSTOR bot-blocked, not bypassed); SSRN and WRDS require the author to log in on request.
- Reading list: the 16 PDFs in `lit/`, the competitor set, and the papers the positioning judges name as decisive, ~30 total; extracted texts stored under `research/txt_extracts/`; cards under `research/cards/`.
- Positioning: tournament of independent proposals judged on whitespace, fact anchoring, deliverability by December, supervisor continuity; adversarial verification of the winner against the cards; checkpoint with the author (ADR-0003, 0004).
- Model: rebuilt from minimal primitives for the winning position (ADR-0002); tools in reach: monotone comparative statics, information design, tender-offer game theory; continuous-time methods reserved as an extension unless the author opts in; honesty labels preserved.
- Empirics: US only; data caps — WRDS pulls limited to CRSP, Compustat, Thomson 13F and SDC/Refinitiv M&A if present, each < ~2 GB; EDGAR via the existing pipeline; hand-collection by agents capped at ~300 offer prices; the on-disk CRSP 2021–25 snapshot and parsed 13D universe are the default data; sample = full parsed EDGAR era for power, XML era as validation.
- Outputs: `framework_v4.qmd/.pdf/.md`, `draft_v3.tex` (XeLaTeX, from draft_v2 as a copy), `research/`, `quality_reports/`; presentation deferred to a later session; slide outline only.
- Version control: branch `v4` in the worktree; commit at the end of every ticket; `proposal` and `draft_v2.tex` untouched.

## Testing Decisions

A good check tests the claim against a source or an executed run, never against the claimant's reasoning.
- Literature cards: a separate verifier opens the cited page/PDF and confirms each quoted result and page number (WRONG / MISCITED / UNCHECKED).
- Competitor table and positions: verified against the cards; a claim of whitespace must name the card that would refute it and show it does not.
- Model: an independent theory checker re-derives the main statement; every numerical claim re-run with `.venv/bin/python` against the `numerical` package or a new minimal script committed alongside.
- Empirics: the spec is written before estimation; the estimate is re-run by a verifier from the committed script and data manifest; parser fixes come with a small assert-based check.
- Draft: compiles with `xelatex`+`biber`; a final referee-style read for gaps and contradictions.
- Prior art: `quality_reports/fixes/dN_*_check.py` (paired check scripts), `research/review_v3/verify_*.md` (verifier reports).

## Out of Scope

- The Beamer/PowerPoint presentation (later session; outline only).
- Any pull from Bloomberg, Activist Insight, LSEG Workspace, or non-US premia sources.
- Continuous-time re-modelling unless the author opts in at the theory-ambition checkpoint.
- Editing `draft_v2.tex` or anything on branch `proposal`.
- Polishing the supervisor note (sketch only).
- Submitting anywhere.

## Further Notes

- The Feb-2024 acceleration is available as an anchor but earns no bonus for existing (ADR-0003); `proposal/` does not reserve it (ADR-0004).
- Deliverability is a first-class ranking criterion: the author will not commit to what cannot be robustly delivered by December.
- Plain-language reporting to the author at every checkpoint.
