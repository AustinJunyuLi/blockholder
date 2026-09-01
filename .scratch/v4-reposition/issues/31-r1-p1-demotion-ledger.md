# 31 — R1 · P1 demotion: the ledger move

**Lane:** theory (`v4-theory` worktree at `~/Projects/blockholder_v4_theory`)

**Routing (lane v2, agentic):** Sonnet, effort low — the move line is given verbatim below;
this is a mechanical append. Orchestrator commits.

**Premise:** GPT Pro end review finding 1 (`research/model_v4/threads/2026-08-22_gpt_end_review.md`),
upheld by the audit (`threads/2026-08-23_gpt_end_review_audit.md` §Finding 1). Ledger standing
note 2 sanctions demotion on review findings without new passes. Austin approved 2026-08-23 (Q1).

**Status:** done (2026-08-23) — the move is on file in `research/model_v4/LABEL_LEDGER.md` (commits 43a45f8, 133ea83). Superseded in turn by ticket 35's restore (2026-08-25, 0cbdb37), recorded in the same ledger.

**What to build:**

- [ ] Append to `research/model_v4/LABEL_LEDGER.md`, after the 2026-08-22 C1 move section, a new
      section exactly:

```
## Move — GPT end review + audit, 2026-08-23

P1 | PROVED→CONJECTURE | GPT Pro end review `threads/2026-08-22_gpt_end_review.md` finding 1, upheld by `threads/2026-08-23_gpt_end_review_audit.md`: the proof's h.7 consumes the joint injective form of A7 while the card row and the re-derivation carry the on-path form — the two-pass gate never covered a single statement; independently, Step 12 lacks a continuation-cost clause (sunk-cost gap, live for multi-Voice menus) and Step 9's positivity claim fails at κ=1 under card §4.1's noise law. The pinned single-Voice menu instance is untouched by all three gaps. Demotion per standing note 2 (the review may demote, never promote); approved by Austin 2026-08-23. Repair: ticket 35. | theory lane (Fable orchestrating) | 2026-08-23 | commit: recorded at commit time
```

- [ ] Replace "commit: recorded at commit time" with the actual short hash immediately after the
      orchestrator commits (same pattern as the 627642c / 403ac8e lines: amend in the following
      commit or use `git rev-parse --short HEAD` post-commit and amend — either is fine, the
      ledger's existing moves name their landing commit).

**Do NOT:** touch the card in this ticket (ticket 32 regenerates it); touch any other ledger line
except this append; edit the standing notes (32 owns that).

**Stopping condition:** the move line is on file and pushed. One file, one append.
