# Spec — v4 repositioning of the blockholder paper

Status: ready-for-agent · Written 2026-08-19 from the grilling session (no new interview). **Revised 2026-08-19 after the ticket-03 discussion** (position and theory-ambition checkpoints settled; work split into two lanes). Vocabulary: `CONTEXT.md`. Decisions: `docs/adr/0001–0007`. Plan: `quality_reports/plans/2026-08-19_v4-two-lane-plan.md`.

## Problem Statement

The author has a pure-theory paper (draft_v2) whose headline results were found, on referee review (2026-08-19), to be overclaimed on originality, margin-dependent in sign, small at baseline, and anchored on a natural experiment already used by three other papers and by the author's own side proposal. The modelling is judged messy. The supervisor has read draft_v2 and expects a recognizable descendant, but has asked for out-of-the-box thinking. A department review is due around December 2026 and needs a full draft.

## Solution

Find the best defensible position for the paper by reading the literature in full, then rebuild the paper around it. Both author decision points are now settled (ADR-0006, ADR-0007): the position is the disclosure rule as the market's partition, carrying a bounded null and a matched DiD; the theory ambition is one new theorem proved on a two-round model. What remains is built in two parallel lanes — a theory lane (two-round core model, the partition theorem with an independent re-derivation, a scoping note, and the draft-ready model section) and an empirics lane (parser fixes, a pre-specified design, the headline timing split, stake at filing, outcome coding, the matched DiD with bidder entry by liquidity, a run-up path figure, and the draft-ready empirics section) — then converged into a v4 memo, a compiled draft_v3, a supervisor-note sketch and a final review. Ticket by ticket, with separate verifiers throughout.

## User Stories

1. As the author, I want ~30 papers read in full (not abstracts) and summarized as structured cards, so that positioning rests on what the papers actually prove and estimate.
2. As the author, I want a competitor scope table showing exactly which object, margin and identification each competitor occupies, so that whitespace is visible, not asserted.
3. As the author, I want several independent position proposals judged and adversarially checked, so that the choice is not one agent's taste.
4. As the author, I want to see the winning position and the runner-up with their trade-offs before anything is edited, so that I make the call.
5. As the author, I want the core model restated from minimal primitives, so that the paper reads clean and the proofs are re-derivable.
6. As the author, I want the main result stated with a proof route and an honesty label, so that I never claim more than is proved.
7. As the author, I want to be asked how much new theory to take on once the winner is known, so that I don't commit to what I cannot robustly deliver.
8. As the author, I want an empirical spec (design, sample, variables, identification, confounds, power, placebos, parser validation) written before any regression, so that results are pre-specified.
9. As the author, I want the one headline empirical test — the timing split, run-up versus filing-day jump by liquidity, before and after Feb-2024 — actually run on data on disk, so that December has a number.
10. As the author, I want the stake at filing measured off the 13D itself, so that the model's stake object has a matching number in the data.
11. As the author, I want the bounded null computed from the SEC's own tables, so that the aggregate claim has a stated ceiling even where the estimate is underpowered.
12. As the author, I want the matched DiD on the twelve-month bid hazard against never-13D controls, and bidder entry by liquidity on the same outcome coding, actually run, so that the control-outcome leg is a result and not a promise.
13. As the author, I want any needed WRDS/SSRN login to be requested from me explicitly and only when needed, so that nothing depends on a fresh pull.
14. As the author, I want a `framework_v4` memo (position, model, empirics, edit map, slide outline), so that the plan is one document.
15. As the author, I want a compiling `draft_v3.tex` with the repositioned intro, the new model section and the empirical-design section, so that the December draft is real, not promised.
16. As the author, I want a two-page supervisor-note sketch (what stayed, what changed, why), so that another agent can polish it.
17. As the author, I want theory and empirics to run as two lanes in two sessions on two machines, so that the model rebuild and the data work progress at the same time instead of queueing.
18. As the author, I want each stage committed on its lane's branch and logged, so that any checkpoint is recoverable after a context reset.
19. As the author, I want the paper never to say "job-market paper" or name a journal, so that the draft is simply a good draft.

## Implementation Decisions

- Process: mattpocock main flow with a local `.scratch/` tracker; one ticket per fresh session; each ticket run by a bounded parallel Agent team (≤12), finder ≠ verifier, verifiers prompted to refute; no dynamic Workflow tool; Fable head, Sonnet/Opus hands — the session model orchestrates only, fresh subagents do all reading/drafting/coding/checking (ADR-0005).
- Literature access: ego-browser through the author's browser; Wiley (JF, Econometrica), OUP (RFS), NBER open with UCL; JFE via SSRN/NBER/author working-paper versions (ScienceDirect and JSTOR bot-blocked, not bypassed); SSRN and WRDS require the author to log in on request.
- Reading list: the 16 PDFs in `lit/`, the competitor set, and the papers the positioning judges name as decisive, ~30 total; extracted texts stored under `research/txt_extracts/`; cards under `research/cards/`.
- Positioning: tournament of independent proposals judged on whitespace, fact anchoring, deliverability by December, supervisor continuity; adversarial verification of the winner against the cards; checkpoint with the author (ADR-0003, 0004).
- Model: rebuilt from minimal primitives for the winning position (ADR-0002); **two-round form** — one pooled trading round, the flag lands or not, one flagged round plus the bidder's decision — so the window margin is a primitive and the stake at filing is an object (ADR-0007); one new theorem, not a sharpening, because the referee's O-1 check shows window-margin attenuation is false at baseline in the repo model; tools in reach: monotone comparative statics, information design, tender-offer game theory; calibration re-anchored so the flagged share is an empirically meaningful number, with magnitudes reported and not only signs; continuous-time methods named as an extension, not December work; honesty labels preserved.
- Lanes: **theory lane** on the author's other machine, worktree on branch `v4-theory` pushed to GitHub, writing under `research/model_v4/`, `quality_reports/fixes/`, `sections_v3/` (model, theorem, proofs) and `research/cards/`; **empirics lane** in this session on branch `v4`, writing under `empirics/`, `research/empirics_v4/`, `sections_v3/empirics.tex` and `numerical_output/empirics/`. Shared files (`CONTEXT.md`, `docs/adr/`, `.scratch/`, `bibliography.bib`) are edited only by the empirics-lane session, which also owns the convergence tickets; the theory lane proposes glossary terms through its session log. Each lane keeps its own session log (filename suffix `_theory` / `_empirics`). `v4-theory` merges into `v4` at the draft_v3 ticket.
- Coupling: exactly one hard dependency between the lanes — the slope sign for the post-2024 prediction comes from the theory lane's `research/model_v4/HANDOFF_sign.md` (sign, magnitude, condition, date). The empirics lane writes its spec with a placeholder and does not wait.
- Routing: per ADR-0005 (Opus for the model writer, the re-deriver, judges and the final referee; Sonnet for mechanical stages). The theory lane may additionally use **GPT Pro as its theorist** — a chatbot the author pastes into, with Claude Code agents as hands; every claim it returns is re-derived by an Opus checker before it enters a file.
- Honesty labels: PROVED, NUMERICAL, **ESTIMATED** (an empirical estimate with a standard error and a stated design), CONJECTURE. Region-certified means PROVED with the region in the hypothesis, not a separate label.
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
- **Hand-collection of takeover premia** for December — the causal premium leg is specified only (ADR-0006).
- **Continuous-time re-modelling** — decided against at the theory-ambition checkpoint; it appears in the scoping note as an extension, not as December work (ADR-0007).
- **Cross-country disclosure-rule panels** — US only; named as an extension in the memo, no sweep and no data.
- Editing `draft_v2.tex` or anything on branch `proposal`.
- Polishing the supervisor note (sketch only).
- Submitting anywhere.

## Further Notes

- The Feb-2024 acceleration is available as an anchor but earns no bonus for existing (ADR-0003); `proposal/` does not reserve it (ADR-0004).
- Deliverability is a first-class ranking criterion: the author will not commit to what cannot be robustly delivered by December.
- Plain-language reporting to the author at every checkpoint.
