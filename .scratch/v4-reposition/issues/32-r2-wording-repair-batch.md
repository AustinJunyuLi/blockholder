# 32 — R2 · Wording-repair batch: card, ledger note, HANDOFF, model note

**Lane:** theory (`v4-theory` worktree at `~/Projects/blockholder_v4_theory`)

**Routing (lane v2, agentic):** Opus writer, effort medium (careful prose surgery on
load-bearing records). Then a **fresh Opus verifier**, effort medium, read-only: diff every edit
against the audit's repair list — flag over-correction, under-correction, or any label-content
change beyond reflecting ticket 31's move (three outcomes: WRONG blocks, MISCITED/UNCHECKED
never block). Orchestrator commits.

**Premise:** Audit findings 4, 6, 7, 8 (`threads/2026-08-23_gpt_end_review_audit.md`) + approved
naming package (Q9). Ticket 31's ledger move is on file. No result's label changes here except
the P1 row reflecting the demotion.

**Status:** done (2026-08-25) — post-review wording-repair batch landed and verifier-accepted after one repair round (commit d2ccf62): A7′/A7-J split, "certified" → dominance-and-contraction, O-1 relabelled disclosure-regime, A(τ) left open, ledger supersessions, HANDOFF §7/§8.3 amendments, mirrors and PDF regenerated. The freeze-stamp card (65b8db3, 2026-08-30) carries the repairs forward.

**What to build:**

- [ ] **`research/model_v4/MODEL_CARD.md` — regenerate** with a fresh stamp
      ("2026-08-23 · post-review repairs · commit <hash>") and one consistent history in §6's
      intro: seven results moved 2026-08-21 (627642c), C1 moved 2026-08-22 (403ac8e),
      **P1 demoted 2026-08-23** (review + audit). Delete the contradictory sentences at :7,
      :297, :301-302 ("all seven" / "C1 is untouched and stays CONJECTURE").
- [ ] Card **P1 row** (:314): label → **CONJECTURE**, statement kept, evidence cell rewritten to
      name the three gaps (form mismatch, Step-12 cost, κ=1) + pointer to ticket 35. Do not
      delete the old evidence chain — mark it "did not satisfy the two-pass gate (form mismatch)".
- [ ] **A7 naming split (Q9a):** in §5's A7 note and §4.2's B_j row (:80), name the two forms
      **A7′ (on-path composed target)** and **A7-J (joint tuple injectivity)**. Fix the two false
      consequences: ":80 'each $b_j^*$ strictly increasing'" → strictness for **flag-capable
      composed targets** only, no backtracking across admissible Voice-plan switches;
      ":196-197 'forces $B^F$ continuum-valued'" → "forces the **tuple** $(B^F,Q^F)$
      continuum-valued; the coordinates may trade the burden" (per `A7_attack_verdict.md` S-10).
- [ ] **"Certified" rename (Q9b):** :123, :138, :316 (and anywhere else `grep -n certif` hits) →
      "**dominance-and-contraction node**": pointwise $L_{\mathcal R}<1$ and $\eta_r>0$ plus
      supporting diagnostics; **not** a verification of the full C1 antecedent. Keep the honest
      disclaimers already in the row.
- [ ] **§9 item 3 rewrite (finding 4):** O-1 is a **disclosure-regime** experiment (flag observed
      vs hidden at a fixed window — Q9c's term "disclosure-regime margin"); its ratios are not
      $W_TC_T$ and it refutes no window claim. Keep it as the motivating analogy for T1's iff
      (a composition factor can exceed one in a regime comparison). The genuine window-margin
      record: `t2_t1_check` block 4 — $W_TC_T<1$ at every checked node at this calibration.
- [ ] **`research/model_v4/LABEL_LEDGER.md` standing notes:** amend note 1 (:15-16) with a dated
      supersession marker — C1 moved 2026-08-22, P1 demoted 2026-08-23; keep the original words
      struck-through or bracketed, never silently deleted (house pattern: the "Not moved" line).
- [ ] **`research/model_v4/HANDOFF_sign.md`:** §7's "The O-1 numbers in §3 are the live failure
      case that iff has to accommodate" → relabel per finding 4; **§8.3 rewrite**: title and body
      no longer say A(τ) "fails" — both recorded failures were test-design artifacts (L2 placebo
      demanded a sign A(τ) does not imply — the card's own Example A has $A'_\kappa=-1/4$; block 3
      hard-coded 0.25 where the implied coefficient is ≈[0.997,1.158]). Status: **OPEN, untested;
      decisive check = ticket 33**. Keep every number. Add a visible
      "**Amended 2026-08-23 (post-review)**" marker at each edit site — the empirics lane
      consumes this file.
- [ ] **`research/model_v4/model_v4.md` + `.tex`** — §6 facts 1–2 rewritten to match (O-1
      relabel; A(τ) → open, tests misformulated; P1 → conjecture, gaps named), :438 and the :460
      DROP-row sentence fixed; recompile the PDF (xelatex, clean).

**Do NOT:** touch proofs/ (ticket 35 owns P1_proof.md); touch check scripts or JSONs; change any
statement's mathematical content; edit CONTEXT.md or docs/adr/.

**Stopping condition:** verifier pass returns no WRONG; PDF compiles; committed + pushed. If the
verifier finds a WRONG, one repair round with the finding injected, then stop and report.
