# 27 — T2g · Verification pipeline: proof-reads, re-derivations, label moves

**Lane:** theory (`v4-theory` worktree at `~/Projects/blockholder_v4_theory`)

**Routing (lane v2, agentic):** fresh Opus agents throughout; finder ≠ verifier
strictly — a proof-reader never reads a proof it wrote; a re-deriver gets
STATEMENTS ONLY (never any proof file). Fable adjudicates writer-vs-re-deriver
disagreements (a named Fable checkpoint). Precedent for the proof-read format:
`threads/thread1_turn2_audit.md` (the D1/L1/L2 proof-read).

**Premise:** proofs on file from tickets 21–24, 26 (plus D1/L1/L2 already
proof-read PASS 2026-08-20). Label rule (unchanged): CONJECTURE → PROVED needs
adversarial Opus proof-read PASS **plus** independent re-derivation PASS by an
agent who never saw the proof. GPT Pro's end review (ticket 30) can demote,
never promote.

**What to build:**

- [ ] Adversarial proof-reads of L3, L4, P1, T1 and the A7 construction
      (batched; audit file per batch under `research/model_v4/threads/` or
      `proofs/`), verdicts WRONG / MISCITED / UNCHECKED per claim; WRONG →
      one retry with the failure injected, fixed by a fresh writer, re-checked
      by a fresh checker; cap three rounds, then escalate (ultimately GPT Pro
      per the failure rule)
- [ ] Independent re-derivations, statements-only, for every result whose
      proof-read passed: D1, L1, L2 (already read) + the new ones
- [ ] Label moves executed in the card ledger with the log line
      `ID | old→new | evidence path | who | date | commit` — the first PROVED
      labels of the stack
- [ ] Card regenerated (new stamp) after the moves
- [ ] Session log lines; commits on `v4-theory`

**Blocked by:** 21, 22, 23, 24, 26 (runs incrementally as each proof lands —
partial execution per landed proof is fine and encouraged).

**Status:** ready-for-agent

## Comments
