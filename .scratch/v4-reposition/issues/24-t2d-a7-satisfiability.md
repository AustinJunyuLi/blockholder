# 24 — T2d · The A7 satisfiability construction (the stack's biggest open risk)

**Lane:** theory (`v4-theory` worktree at `~/Projects/blockholder_v4_theory`)

**Routing (lane v2, agentic):** **Fable reasons this one directly** (Austin's
2026-08-20 grant: the hardest bits go to Fable), then ONE Opus agent attacks
the construction adversarially. This is the only ticket where Fable writes
theory.

**Premise:** `threads/thread1_turn2_audit.md` finding L2-R1: injective A7
(the flagged tuple (B^F, Q^F, a=1) recovers (j,s)) conflicts with weak
monotonicity — flat signal intervals break injectivity generically. The card
was patched to require strict monotonicity of s ↦ (B_j^F, b_j^*) for Voice on
the flagged set. L2's economic substance now lives in A7; whether it is
satisfiable on an actual plan menu is open.

**What to build:** `research/model_v4/proofs/A7_construction.md`:

- [ ] The observation that Q^F = b_j^*(s) − B^F makes the tuple informationally
      equivalent to (B^F, b_j^*(s), a) — so the SUM B^F + Q^F reveals the
      terminal target, and strict monotonicity of the *composed* terminal
      target s ↦ b_{j(s)}^*(s) on the flagged signal region alone already
      recovers s (and on-path the cutoff policy then recovers j). Check
      whether this strictly weakens the card's §4.2 patch (strictness of the
      pair → strictness of the sum); if it does, propose the card edit
- [ ] An explicit plan-menu construction satisfying it (candidate: Exit / Hold /
      one Voice family, pro-rata daily accumulation, strictly increasing
      terminal target b*(s)) with the injectivity argument written out
- [ ] The weakest menu condition stated as a named hypothesis (A7′), and the
      failure boundary (what menus break it) stated
- [ ] Consistency with D1-repair-2 (continuum-valued B^F) confirmed
- [ ] Opus adversarial attack on the construction, reported WRONG/MISCITED/
      UNCHECKED; survives → card A7 note updated
- [ ] Session log line; commit on `v4-theory`

**Blocked by:** none. **Unblocks the credibility of L2 → feeds ticket 27.**

**Status:** ready-for-agent (Fable-led)

## Comments
