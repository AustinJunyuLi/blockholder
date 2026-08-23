# 35 — R5 · P1 repair (route A) + fresh two-pass

**Lane:** theory (`v4-theory` worktree at `~/Projects/blockholder_v4_theory`)

**Routing (lane v2, agentic):** Opus writer, effort medium, for the statement + proof repair
(gap list is fully specified). **Fresh Opus proof-reader, effort high** (adversarial;
FAIL/REPAIR/OBSERVATION; never saw the writer's thread). **Fresh Opus re-deriver, effort high**
(statements-only: works from the amended card row alone, `proofs/` and `threads/` unopened).
Writer-vs-verifier disputes → Fable adjudicates. Orchestrator commits.

**Premise:** Audit finding 1 (three gaps + one citation nit); Austin chose route A (Q4): keep the
general finite-menu theorem and state the hypotheses the proof actually needs. Runs **after
ticket 32** (needs the A7-J name on the card). The pinned pro-rata single-Voice menu satisfies
every strengthened clause, so the paper's instance is covered by the repaired theorem.

**What to build:**

- [ ] **Amend the card P1 row's statement** (label stays CONJECTURE until both passes land):
      1. hypothesis "A7′ (on-path injective)" → **A7-J (joint tuple injectivity)** — the form
         the proof's h.7 already carries;
      2. new clause **h.16, continuation-cost equivalence**: menu elements sharing a pooled path
         and engagement status share the engagement cost, $C_{j'}(s)=C_j(s)$ on each h.11
         deviation set (trivially true on any single-Voice menu). Spec MAY-11: the writer may
         instead restate round-2 optimality against the sunk-cost continuation and prove Step 12
         from that — either discharge is acceptable;
      3. the κ boundary: either restrict to $\kappa\in[0,1)$ **or** extend Step 9's reachability
         argument to κ=1 (mirror of its κ=0 sentence: at κ=1 histories requiring a zero noise
         mark are outside the reachable alphabet; say it and handle the alphabet honestly);
      4. fix the objective citation nit: card :107 says h.14 is "displayed there in full" while
         h.14 shows $-C_j(s)$ vs the card's $-a_jC_j(s)$ — align the two displays (state
         $C_j\equiv 0$ for $a_j=0$ plans, or write $-a_jC_j$ in h.14).
- [ ] **Patch `proofs/P1_proof.md`:** h.7 renamed to A7-J with the corrected continuum sentence
      (tuple, not $B^F$ — :57); h.16 added with its "Why" note; Step 9's κ=1 sentence; Step 12
      rewritten so the deviation's continuation is compared cost-honestly (via h.16 or the
      sunk-cost route); NOTATION DELTA and NOT CLAIMED updated; keep the P1-R1…R8 repair table
      and append this round's entries.
- [ ] **Pass 1 — adversarial proof-read** (fresh agent): whole proof, not only the patched steps
      (a patch can break a neighbour). FAIL blocks; one retry with the failure output injected;
      a second FAIL parks the ticket.
- [ ] **Pass 2 — statements-only re-derivation** (fresh agent): from the amended card row alone.
      PASS / PASS-WITH-CHANGES (changes folded back into the row, traceably) / FAIL.
- [ ] **Both PASS →** ledger move: `P1 | CONJECTURE→PROVED | <evidence paths incl. both fresh
      passes> | theory lane | <date> | <commit>`; card row label + evidence cell updated; fold in
      ticket 34's node outcomes (spec SHOULD-9); session log outcome line.

**Do NOT:** weaken the conclusion silently; reuse the 2026-08-21 passes as evidence (they covered
mismatched statements — that is the point); let the writer self-verify; exceed one retry per pass.

**Stopping condition:** either P1 is PROVED with two fresh passes on file, or the ticket is
**parked with P1 at CONJECTURE** and a plain report of what failed. Cap: one retry per pass,
three fix rounds total, then park. Ticket 08 unblocks only when this ticket closes (either way —
Austin decides on a parked outcome).
