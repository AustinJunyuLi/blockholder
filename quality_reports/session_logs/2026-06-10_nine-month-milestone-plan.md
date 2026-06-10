# Session Log: Nine-Month Milestone Implementation Plan

**Date:** 2026-06-10
**Branch:** jmp-upgrade-2026-05
**Status:** PLAN APPROVED — implementation not yet started

## Goal

Turn the 2026-06-10 two-path feasibility decision (§4, 0–9-month deliverable) into an executable implementation plan for the ~March 2027 milestone: **Theorem A** (microfound wedge m1>m0), **Theorem B** (sign GE cutoff-shift channel via MCS or counterexample), **de-risk leg** (13D/G XML facts + competitor reads + positioning).

## Approach

3 parallel Explore agents (manuscript map / numerical layer / prior plans + lit inventory); Plan-agent pass deliberately skipped (budget-conscious preference — milestone structure already fixed by the decision report). Plan written directly from verified exploration.

## Key findings that shaped the plan

- **Theorem A is not greenfield**: App. B (`app:bg`) already proves the wedge from Nash bargaining conditional on Condition BG (λ>0); draft states λ "can only be pinned by a complete tender-game equilibrium" (l.2440–41). D4 derivation record (906 lines) + verification scripts exist. Theorem A = build the tender game that pins λ.
- **GE-dominance is false globally**: trough in 4/20 sensitivity cells (σ_ξ=0.60, channel B). So Theorem B = sufficient-conditions theorem on a region + formalized counterexample (both halves, both milestone-valid). IFT machinery reusable from `D3_prop8_IFT.tex`; sweep template from `_export_sensitivity()`.
- All gating literature missing from `lit/`/bib (Celentano–Levine, Johnson–Swem, AFS, MCS toolkit papers, tender-game papers); no data code exists anywhere.

## Decisions (user, 2026-06-10)

1. **Theorem A primary route = Grossman–Hart free-rider tender game** (BGP toehold as documented fallback at Gate G1, end-Sep).
2. **Empirics live in this repo** (`empirics/` package, raw data gitignored).

## Plan on disk

`quality_reports/plans/2026-06-10_nine-month-milestone-implementation.md` — workstreams A (Theorem A → D7 record + `numerical/takeover_game.py`), B (Theorem B → D8 record + GE-decomposition export/figure), C (lit/bib, scope tables, `empirics/` parser, Facts 1–2, Bloomberg checklist, positioning memo), D (manuscript/presentation integration, milestone talk); month-by-month timeline with gates G1 (end-Sep), G2 (end-Dec); division of labour; verification per phase; risk register.

## Open questions / blockers

- WRDS/CRSP access unconfirmed (gates Fact 2; degrades gracefully to Fact 1 + design note).
- Bloomberg function inventory (decision-report open item 2d) — author to run checklist at terminal.
- Author full reads of Celentano–Levine + Johnson–Swem scheduled M0–M1; they gate framing and the month-9+ structural commitment (out of this plan's scope).

## Next step

M0 chunk: lit downloads + bib entries → competitor scope-table skeletons → Theorem A game-spec note → `empirics/` scaffold + parser v0.
