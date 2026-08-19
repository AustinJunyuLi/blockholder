# Plan — v4 two-lane restructure (theory lane + empirics lane)

Status: APPROVED (author, 2026-08-19, grilling rounds 1–3 after ticket 03)
Vocabulary: `CONTEXT.md`. Prior decisions: `docs/adr/0001–0005`. New: ADR-0006 (position), ADR-0007 (theory ambition, model form, two lanes).

## Decisions (all author-confirmed)

| # | Decision |
|---|---|
| D1 | **Position = P2** (the disclosure rule as the market's partition; W3), **plus** P4's bounded null, **plus** P4's matched DiD on bid hazard — now *run*, not just specified. P4's premium hand-collection cut for December. |
| D2 | **Theory ambition = one new theorem** (the partition theorem, correctly signed on both margins) on a **two-round model**: one pooled trading round → the flag lands or not → one flagged round + the bidder's decision. Makes the window margin a genuine primitive; gives stake-at-filing as an object. Not continuous time before December. |
| D3 | **Ticket 4's first milestone** = re-run the referee's O-1 experiment (window margin: Public buy flagged vs pooled at fixed cutoffs) in the rebuilt model; publish the sign + magnitude to `research/model_v4/HANDOFF_sign.md`. The empirics spec waits only for that file. |
| D4 | **Calibration re-anchored** so the flagged share is an empirically meaningful number (share of engagements that get disclosed); magnitudes reported, not just signs. |
| D5 | **December empirics (E-lane):** headline = timing split (run-up vs filing jump by liquidity, pre/post Feb-2024); add-ons: bindingness dose, stake at filing, bounded null, run-up path figure; then P4's matched DiD on 12-month bid hazard with never-13D controls **and** bidder entry by liquidity (same outcome coding). Headline secured before the long pole starts. |
| D6 | Parallel scoping note (theory lane, one Opus agent): filing-timing game (endogenous filing date within the window; Acharya–DeMarzo–Kremer / Guttman–Kremer–Skrzypacz tools), continuous-time endogenous-trigger tractability, occupancy check. Research note only. |
| D7 | US only. Cross-country rule panel named as extension in the memo; no sweep, no data. |
| D8 | Honesty labels: add **ESTIMATED**. "Region-certified" = PROVED with the region in the hypothesis; no new theory label. |
| D9 | Routing per ADR-0005: Opus for model-writer, re-deriver, judges, final referee; Sonnet for mechanical. Theory lane may use GPT Pro (chatbot only) as the theorist — see the handoff. |
| D10 | **Two lanes, two sessions, two machines.** Theory lane: other laptop, worktree on branch `v4-theory` (pushed to GitHub). Empirics lane: this session, branch `v4`. Convergence tickets (memo, draft_v3, supervisor note, final review) and `CONTEXT.md`/`docs/adr/` owned by the empirics-lane session (this one). Theory lane proposes glossary terms in its session log; convergence owner merges. |

## Lane structure

### Theory lane (T) — branch `v4-theory`, other laptop

- **T0 — Lit housekeeping.** Card Chabakauri et al. (2022) (named live W3 refuter); fetch/attempt Burkart–Lee–Van Schepdechen Dec-2025 revision; check Zeng IA Table 2 if obtainable. Outputs: cards + INDEX update. (Sonnet fetch, Opus read.)
- **T1 — O-1 re-run + calibration facts.** Reproduce O-1 in the current repo model from the committed claim; then re-run in the two-round model as soon as it exists; find a data anchor for the flagged share. Output: `research/model_v4/HANDOFF_sign.md` (sign, magnitude, condition, date). **This is the E-lane's only dependency on T.**
- **T2 — Two-round core model + partition theorem.** `research/model_v4/model_v4.tex` (+ `.md` mirror): primitives, timing, partition, equilibrium notion, theorem with proof route and labels (decomposition identity; flagged-cell κ-invariance; threshold-margin attenuation with the second lemma; window-margin sign with the weight/composition condition; GE region certificate). Independent re-derivation by a fresh checker (WRONG/MISCITED/UNCHECKED). Numerical checks from committed scripts under `quality_reports/fixes/` (D-series pattern), run with `.venv/bin/python`.
- **T3 — Scoping note** (D6). `research/model_v4/SCOPING_timing_game.md`.
- **T4 — Draft-ready model section.** `sections_v3/model.tex`, `sections_v3/theorem.tex`, `sections_v3/proofs_appendix.tex` for `\input` into draft_v3; bibliography entries.
- Map of draft_v2 machinery reused / simplified / dropped (inside T2).

### Empirics lane (E) — branch `v4`, this session

- **E1 — Parser fixes with checks.** `pct_of_class` regex (3-digit, correct reporting person), event-date fix for 2025, federal-holiday business-day arithmetic; assert-based checks; re-parse the universe.
- **E2 — Pre-specified empirical design.** Full spec: timing split (headline), bindingness dose, stake at filing, bounded null, run-up path, P4 matched DiD on bid hazard (sample, 3:1 matching on size/Amihud/SIC2/quarter, outcome coding, confounds, power/MDE, placebos ≥500 dates, pre-trends), bidder entry by liquidity. Data manifest. Slope sign for the post-2024 prediction = placeholder until `HANDOFF_sign.md`. Verifier against cards and disk.
- **E3 — Headline: timing split + dose + bounded null.** Committed script, verifier re-run, plain-language result note. Secured early.
- **E4 — Stake at filing.** Blocked by E1 (and reads T1's prediction).
- **E5 — Outcome coding.** Bids within 12 months of each initial 13D (SC TO-T / DEFM14A / 8-K), EDGAR via existing pipeline + EDGAR MCP tools; 30-filing hand audit.
- **E6 — Matched DiD + bidder entry by liquidity.** Blocked by E5.
- **E7 — Run-up path figure.** Cheap; any time after E1.
- **E8 — Empirical section `.tex`** + tables + figures for draft_v3.

### Convergence (C) — this session, after T and E deliver

- **C1 (= old 07)** framework_v4 memo; **C2 (= old 08)** draft_v3.tex (inputs T4 + E8); **C3 (= old 09)** supervisor-note sketch; **C4 (= old 10)** final referee-style review + fix round + HANDOFF for the presentation session.
- Merge `v4-theory` into `v4` at C2.

## Coupling and protocol

- Single hard dependency: E2's slope sign ← T1's `HANDOFF_sign.md`. E-lane proceeds with a placeholder.
- Disjoint paths: T writes under `research/model_v4/`, `quality_reports/fixes/`, `sections_v3/` (model/theorem/proofs), `research/cards/`; E writes under `empirics/`, `research/empirics_v4/`, `sections_v3/empirics.tex`, `numerical_output/empirics/`. Shared files (`CONTEXT.md`, `docs/adr/`, `.scratch/`, `bibliography.bib`) edited by the convergence owner; T proposes via its session log + a `PROPOSED_TERMS.md`.
- Each lane keeps its own session log under `quality_reports/session_logs/` (filename suffix `_theory` / `_empirics`).
- Commit at the end of every ticket; push `v4-theory` so the convergence owner can pull.

## Verification (unchanged from the spec)

Finder ≠ verifier; verifiers prompted to refute; executed checks wherever one exists; honesty labels never weakened.
