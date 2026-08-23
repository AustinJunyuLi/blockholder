# SPEC — post-review repairs (theory lane) — 2026-08-23

**Status:** APPROVED (Austin, 2026-08-23, this session — nine-question round, all answered).
**Source of truth for the defects:** `research/model_v4/threads/2026-08-23_gpt_end_review_audit.md`
(theory worktree, commit 2292798) — Fable's verification of the GPT Pro end review
(`threads/2026-08-22_gpt_end_review.md`, commit e46a071). All eight review findings UPHELD.
**Tickets:** 31–37 in `.scratch/v4-reposition/issues/` (series R). Execution prompt:
`quality_reports/plans/2026-08-23_post-review-execution.md`.

## Decisions on record (Austin, 2026-08-23)

| Q | Decision |
|---|---|
| 1 | P1 demotion recorded now (ledger first) — **ticket 31** |
| 2 | All wording/consistency repairs in one batch — **ticket 32** |
| 3 | Both executed checks run — **tickets 33, 34** |
| 4 | P1 repair route **A**: keep the general theorem, state the three conditions the proof needs — **ticket 35** |
| 5 | P1 repair completes **before** ticket 08 (draft_v3 theory sections). Ticket 08 is NOT part of this run |
| 6 | E2 SPEC gets a dated corrigendum addendum — **ticket 36** |
| 7 | ADR-0007 corrigendum drafted for Austin to paste (agents never edit `docs/adr/`) — **ticket 37** |
| 8 | GPT re-review deferred; bundled later with ticket 08's output. No ticket |
| 9 | Naming fixes adopted (A7′ vs A7-J; "dominance-and-contraction node"; "disclosure-regime margin") — folded into **ticket 32**; CONTEXT.md half is Austin's own item |

## Requirements

**MUST**
1. Ledger move P1 PROVED→CONJECTURE lands before any card edit (31 before 32). Demotion is
   sanctioned by the review + audit under ledger standing note 2 — no new passes needed to demote.
2. Ticket 35's re-promotion of P1 obeys the full two-pass rule: adversarial proof-read PASS by a
   fresh agent AND statements-only re-derivation PASS by another fresh agent working from the
   amended card row alone. No shortcut because the gaps are "known".
3. Every wording repair in 32 traces to a numbered audit finding; no label content changes in 32
   beyond reflecting 31's move.
4. Checks 33/34 report honestly either way — a negative outcome is a result, never smoothed.
   (Precedent: the batch's own FAIL-reporting discipline.)
5. Ticket 36 commits on branch `v4` in `~/Projects/blockholder_v4` (the empirics worktree), as a
   dated ADDENDUM only — the pre-registered text above it is never edited.
6. Agents do not touch git (orchestrator commits centrally); commit + push after each landed unit.
7. No agent edits `CONTEXT.md`, `docs/adr/`, `bibliography.bib`, or the ticket files themselves;
   progress notes go in the theory session log.

**SHOULD**
8. 33's outcome is appended to the card's §5 A(τ) block as a dated evidence note (status becomes
   "verified at calibration" / "refuted at calibration" / mixed, with node counts). Not a label.
9. 34's outcome, if all four nodes resolve, is folded into the P1 row's numerical sentence during
   35's close-out (single card touch).
10. HANDOFF edits in 32 carry a visible "Amended 2026-08-23 (post-review)" marker — the empirics
    lane consumes that file.

**MAY**
11. 35's writer may restructure Step 12 around the sunk-cost objective instead of adding the
    cost-equality clause h.16, if the proof-read prefers it — either discharge is acceptable.

## Clarity declarations

- **CLEAR:** the defect list and exact file:line targets (audit file); the two-pass protocol; the
  demote-only rule; worktree/branch layout; ticket DAG.
- **ASSUMED (Austin may override):** ticket 08's GPT bundle will include the repaired P1 (Q8);
  "dominance-and-contraction node" as the replacement term (any equivalent honest name is fine);
  the corrigendum texts drafted verbatim in tickets 36/37.
- **BLOCKED:** nothing. Ticket 08 itself stays blocked until 35 closes (Q5).

## Sequencing (DAG)

```
31 (ledger demotion)
 └─→ 32 (card/ledger-note/HANDOFF/model-note batch, incl. Q9 renames)
      ├─→ 33 (A(τ) support check)      ─┐
      ├─→ 34 (P1 four-node 30-seed)    ─┼─ parallel
      ├─→ 36 (E2 SPEC corrigendum)     ─┤
      └─→ 37 (ADR-0007 draft)          ─┘
           └─→ 35 (P1 repair + fresh two-pass; needs 32's A7-J name on the card)
                └─→ close-out (session log, memory note, final report) → ticket 08 unblocks
```
33/34/36/37 are independent of each other and of 35's start except that 35 needs 32.
35 is the long pole; start it as soon as 32 lands, with 33/34/36/37 running alongside.

## Austin's own items (not agent work)

- CONTEXT.md glossary: add "A7′ (on-path)" vs "A7-J (joint)"; "dominance-and-contraction node";
  "disclosure-regime margin" (vs the existing "window margin" entry); update line 83's
  weight/composition "Provisional — to be confirmed by the theory lane" (T1 confirmed it).
- Paste ticket 37's corrigendum paragraph into `docs/adr/0007-…md`.

## Out of scope for this run

Ticket 08 (draft_v3 theory sections); any GPT re-submission; any new theory beyond the P1 repair;
any change to E1/E2 empirics beyond ticket 36's addendum.
