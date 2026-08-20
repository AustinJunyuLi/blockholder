---
status: accepted
date: 2026-08-20
---
# The theory lane goes agentic: GPT Pro moves from theorist to end-reviewer, and Fable may reason on the hardest bits

The courier loop of ADR-0007 — GPT Pro as theorist, the author hand-carrying
every message — produced two good turns (the model card and the D1/L1/L2
proofs, both surviving adversarial proof-reads) but each round trip needs the
author at the keyboard, and the author judged it too slow to finish on. The
theory work therefore moves in-house: Opus agents write the proofs, fresh Opus
agents proof-read adversarially and re-derive independently (statements-only),
and Sonnet does the plumbing. The label discipline is unchanged — CONJECTURE →
PROVED still requires proof-read PASS plus an independent re-derivation by an
agent that never saw the proof; executed committed checks still gate NUMERICAL;
finder ≠ verifier throughout. GPT Pro is reduced to exactly one planned courier
moment — an adversarial end-review of the complete bundle (card + proofs + raw
check output), which can demote labels but never promote — plus escalation
when a claim fails twice in-house. Thread 1 is retired with turns 1–2 as its
record; the drafted msg3 was never pasted and is re-purposed as the spec for
the local L3/L4 writers.

One amendment to ADR-0005's routing: by the author's explicit grant
(2026-08-20), **Fable may reason through the most challenging theory bits
directly** rather than only orchestrating — currently the A7 satisfiability
construction, adjudication of writer-vs-re-deriver disagreements, the
implementation design review, and the final coherence read before the GPT
bundle. Everything bulky stays delegated, and Fable is still never spawned as a
subagent. The work is captured as tickets 21–30 in
`.scratch/v4-reposition/issues/` (protocol and wave structure in
`quality_reports/plans/2026-08-20_theory-lane-agentic.md`); the two-lane
ownership split of ADR-0007 (branches, disjoint writes, `HANDOFF_sign.md` as
the only hard coupling) is unchanged.
