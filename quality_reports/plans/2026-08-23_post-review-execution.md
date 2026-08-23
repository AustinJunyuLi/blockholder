# EXECUTION PROMPT — post-review repair run (tickets 31–37)

You are the theory-lane orchestrator for the v4 blockholder paper (Fable head, subagent hands —
ADR-0005/ADR-0008). Execute tickets 31–37 end to end and report. Austin approved the whole
package on 2026-08-23; do not re-ask the settled decisions (they are in the spec).

## Read first, in this order

1. This file.
2. The spec: `~/Projects/blockholder_v4/quality_reports/specs/2026-08-23_post-review-repairs.md`
   (the decisions, the MUST/SHOULD/MAY list, the DAG).
3. The audit — the defect list every ticket implements:
   `~/Projects/blockholder_v4_theory/research/model_v4/threads/2026-08-23_gpt_end_review_audit.md`.
4. The verbatim review it verifies: `…_theory/research/model_v4/threads/2026-08-22_gpt_end_review.md`.
5. The tickets: `~/Projects/blockholder_v4/.scratch/v4-reposition/issues/31-…37-*.md`.
   **A ticket wins over anything else if they conflict.**
6. Skim for context as needed: `research/model_v4/MODEL_CARD.md` (§5, §6), `LABEL_LEDGER.md`,
   `proofs/P1_proof.md`, `HANDOFF_sign.md` — all in the theory worktree.

## Worktrees

- Work in `~/Projects/blockholder_v4_theory` (branch `v4-theory`). `git pull` there first.
- **Exception — ticket 36 only:** the edit + commit happen in `~/Projects/blockholder_v4` on
  branch `v4`. Pull there before that ticket.

## Order (DAG)

```
31 → 32 → { 33 ∥ 34 ∥ 36 ∥ 37 } and 35 (35 starts as soon as 32 lands; 33/34/36/37 run alongside)
→ close-out
```

## Standing rules (same as the batch; verbatim constraints)

- **Parallel Agent dispatches; never the Workflow tool.** Every agent call sets `model` and
  `effort` explicitly, per the routing line in each ticket (Opus writers/verifiers, Sonnet
  mechanical/plumbing). Fable does not execute tickets; Fable adjudicates writer-vs-verifier
  disputes (ticket 35) and nothing else.
- **Labels:** ticket 31's demotion is already sanctioned (review + audit + Austin's approval) —
  append the given ledger line, no new passes. Ticket 35's re-promotion needs the FULL two-pass
  rule: adversarial proof-read PASS by a fresh agent AND statements-only re-derivation PASS by
  another fresh agent working from the amended card row alone (`proofs/` and `threads/`
  unopened). Every move is logged in the ledger. Nothing else's label moves in this run.
- **Verification vocabulary:** WRONG blocks (one retry with the failure output injected);
  MISCITED never blocks (swap/drop the citation); UNCHECKED never blocks (return the unchecked
  claims themselves and log them). Finder ≠ verifier, always. Executed checks are the verdict
  where one exists.
- **Git is central:** only the orchestrator commits; agents never run git (index.lock races).
  Commit + push after each landed unit (`v4-theory`, except ticket 36 on `v4`). End commit
  messages with the Claude co-author line.
- **Do not edit:** `CONTEXT.md`, `docs/adr/`, `bibliography.bib`, or the ticket files. Progress
  notes and parked items go in a session log
  (`quality_reports/session_logs/2026-08-2X_post-review-repairs.md`, theory worktree).
- **Failure handling:** a claim or ticket failing twice is parked and reported, never silently
  dropped, never escalated to GPT. Abort the run after 3 consecutive agent nulls/API errors.
- **Out of scope:** ticket 08, any GPT submission, any new theory beyond ticket 35's repair,
  any empirics change beyond ticket 36's addendum. If a subagent's findings suggest more work,
  log it for Austin; do not do it.

## Stop and report

Stop when 31–34, 36, 37 are landed and 35 is either landed (P1 PROVED with two fresh passes) or
parked (P1 stays CONJECTURE; say exactly what failed). Push everything first. Then give Austin a
plain-language report: what landed, every label move, the two check verdicts (33's three-way
A(τ) verdict; 34's per-node outcomes), what's parked, and his two personal to-dos (paste the
ADR-0007 corrigendum from `quality_reports/handoffs/2026-08-23_adr0007_corrigendum.md`; the
CONTEXT.md glossary items listed in the spec). Note that ticket 08 is now unblocked (or what
blocks it, if 35 parked).
