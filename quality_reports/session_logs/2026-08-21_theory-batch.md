# 2026-08-21 — Theory batch run (waves A–D)

**Goal:** execute tickets 04, 05, 21–30 per the batch-run section of
`quality_reports/plans/2026-08-20_theory-lane-agentic.md`. Fable orchestrates;
Opus writes/verifies; Sonnet plumbs. Fable personally does: ticket-24 A7
reasoning, ticket-25 design review, adjudications, final coherence read.
Stop at ticket 30's GPT paste (bundle handed to Austin, not pasted).

**Orchestration note:** subagents write files but do NOT run git — the
orchestrator commits/pushes centrally after each landed unit, to avoid
concurrent index.lock races in the shared worktree. Same per-unit commit
cadence the tickets ask for.

## Wave A dispatch (start)

- L3 writer (opus), L4 writer (opus), P1 writer (opus) — proofs to
  `research/model_v4/proofs/`. Writers independent: L4 must not read L3's
  proof file; all cite card-ledger statements only.
- impl-design (opus) — ticket 25 design doc only; STOP before build for
  Fable review.
- O-1 re-run (opus) — ticket 05 repo-model check + provisional
  HANDOFF_sign.md.
- lit-fetch (sonnet) — ticket 04 full texts (Chabakauri 2022 priority;
  Burkart–Lee–Van Schepdechen Dec-2025 rev; Zeng internet appendix) to
  scratchpad; Opus readers follow.
- Fable: ticket-24 A7 satisfiability construction, inline.

## Incremental notes

- **Ticket 05 (T1, O-1 re-run) DONE.** Committed claim located in
  `quality_reports/reports/2026-08-19_framework_v3_referee_report.md:113-120`
  (referee's [O] finding), independently re-executed in
  `research/review_v3/verify_theory.md:32,42-53`. Reproduced in the current
  repo model by `quality_reports/fixes/t1_o1_rerun_check.py` (5 checks, all
  pass, JSON on disk, byte-identical across runs and cwds). **Every committed
  number matches to the last printed digit** — ratios 1.06397 / 1.18373 /
  1.13631 / 0.37798 vs committed 1.0640 / 1.1837 / 1.1363 / 0.3780; baseline
  masses, pointwise-slope claim and figure-magnitude claim all reproduce too.
- **New beyond the committed claim:** ADR-0007's "Ω ≲ 0.29" is a grid point,
  not the crossing. Bisection puts the sign flip at **k_D* = 1.28618,
  Ω* = 0.3428**. Failure region is wider than recorded; the decision is
  unaffected, but anything quoting 0.29 as the boundary should quote 0.343.
- **Sign published (PROVISIONAL, PE, fixed cutoffs):** flagging the public buy
  RAISES κ-sensitivity — the empirics spec's **Branch B, δ < 0** — magnitude
  +6.4% at baseline (curves 0.9% apart in range), so a bounded null is the
  realistic empirical outcome. `research/model_v4/HANDOFF_sign.md`, with a
  "Two-round model" placeholder for tickets 25/30.
- **ω_a data anchor: ABSENT, stated plainly.** No repo card measures the
  disclosed share of engagements; Becht et al. 2017 fn.2/fn.15, Norli et al.
  2015 n.10 and Edmans 2014 p.35 each say the denominator is unobservable.
  Three bounded proxies recorded with sources and labelled for what they are
  (BJPT 97.5% upper bound; Gantchev 98.2% upper bound, self-declared
  non-random; SEC 2022 13D/13G split 12.1%, wrong unit). They straddle Ω*,
  so the sign is not yet anchored on data — flagged as the highest-value
  calibration input the project can acquire.
- Note for the orchestrator: the `blockholder_v4_theory` venv was empty;
  `requirements.txt` installed into it so the check script runs.
- **Ticket 22 (L4 proof) LANDED** (`proofs/L4_proof.md`, 545 lines). Legs 1-2
  (nestedness, Ω↑) proved outright from D1's clock equivalence; leg 3 (𝒮_P↓)
  needs a named bridging hypothesis **A(br)** (chord–sensitivity bridge, 4
  clauses; br-iii is the genuinely unjustified one). Step 9/11/13 = the
  newly-flagged-is-Voice arithmetic. Extra hypothesis b_0 < τ' < τ. Two
  adjudication items for Fable at card-regeneration time: (1) intended label
  should read "PROVED under A(br)", not "under nested reclassification";
  (2) π̄ definitional tension — §4.4 gloss ("pre-order pooled engagement
  share") vs A(τ)'s chord upper support point; factor two under A_0=A_1
  martingale reading. Fable to rule before the card is regenerated.
- **Ticket 24 (A7 construction) DRAFTED by Fable** (`proofs/A7_construction.md`):
  A7′ = composed terminal target strictly increasing on the flagged region;
  sum B^F+Q^F reveals b*; pro-rata Exit/Hold/Voice menu satisfies A7′ and
  VIOLATES the card's strict-pair patch (B^F jumps down at crossing-date
  boundaries — numeric witness 1.68→1.56). A7′ necessary within pro-rata
  family. Opus adversarial attack dispatched; card edits wait on it.
- Wave A agent fates so far: lit-fetch (sonnet) PASS — all 3 texts obtained
  (CFJ via LSE eprint; BLV Dec-2025 via ECGI long-timeout; Zeng IA via
  Springer supplement). Ticket's "Van Schepdechen" author name corrected to
  Voss by repo evidence. o1-rerun (opus) PASS. L4-writer (opus) PASS.
