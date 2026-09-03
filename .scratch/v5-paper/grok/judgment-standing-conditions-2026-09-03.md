# Judgment: the standing-conditions gate failed twice

Date: 2026-09-03. Run `v5-detection-frame`, ticket 16. Written under the fail-twice rule.

## What failed

The attack gate on the standing conditions block in `proofs/04_inherited.tex`, (S1) to (S14).

- Attempt 1 (Opus attacker `att-standing-conditions`): FAIL. Two defects. The
  two-cell lemma's statement misdescribed what (S4) supplies, and the second clause of (S6)
  ("the control-node information set contains the pooled history") held on every history and
  so contradicted the new (S13), which makes the flagged information set exactly the flagged
  signal.
- Fix applied by the orchestrator: reworded the two-cell sentence, and confined the second
  clause of (S6) to the pooled cell. This changed an assumption, so it counts as the second
  attempt.
- Attempt 2 (re-gate `att-standing-conditions-2`): FAIL. Step 6 of the disclosure partition
  lemma (`04_inherited.tex` lines 371 to 384) derives the measurability of the disclosure
  indicator at the control node from (S6) alone: "I_H contains that coordinate at d = H". After
  the fix, (S6) grants that only on the pooled cell, and measurability of D is a joint statement
  about both cells. The lemma is stated under (S1) to (S6) (line 320), so it can no longer cite
  (S13) for the flagged cell.

## What it is and is not

It is not a theorem-level defect. Every statement gate passed: 14 of 14 attacks in round 2
returned PASS, including the entry identity, the detection lemma, the upper-set lemma, the
silence lemma, entry against the undetected, the Blackwell theorem and its corollaries, the
trichotomy, the cut identity, the one-crossing and reversal lemmas, and the regret bound. The
detection record ran on the full grid with all nine checks passing and every sign as ticket 16
states. The cut and regret grids are still running.

It is a hypothesis-bookkeeping defect that the first fix introduced: narrowing (S6) removed
the flag coordinate from the flagged cell's information set at the level of the partition lemma,
which is proved before (S13) is in force.

## The fix the attacker named

Two edits, both in `proofs/04_inherited.tex`.

1. (S6), lines 278 to 280. Keep the flag coordinate public on every history and say so: "Every
   control-node history carries the public coordinate 'the filing has landed by date d', so the
   control-node information set contains that coordinate at d = H on both cells. On the pooled
   cell the information set contains the pooled history up to the control node." This is
   consistent with (S13): on the flagged cell D equals one identically, so the coordinate is
   trivially measurable with respect to the flagged signal.
2. Step 6, line 372. Cite the coordinate as holding on every history, which the reworded (S6)
   gives directly. No change to the range at line 320 is then needed. The attacker's
   alternative, citing (S13) in Step 6 and widening the range to "(S1) to (S6) and (S13)", also
   works but reorders the dependency chain, since (S13) is stated after the partition lemma.

Either edit is one clause. The gate would then be re-run once by a fresh Opus attacker on the
whole block, with both verdicts attached to its spec.

## Six further nits from the second verdict, all wording

The hook pair around (S12) to (S14) is dead code; (S12) uses notation foreign to this file;
(S13) should say "cells at depth d"; (S12) never states the mark support; line 547 of
`03_caught.tex` should cite the two-cell lemma beside (S9); `paper.tex` still says (S11) at
lines 385, 386 and 444. None affects a proof. They go into the round-4 hypothesis audit.

## Decision requested

The rule allows no third attempt without Austin. Options:

- A. Authorise one more gate on the block with edit 1 applied. Recommended. Cost: one Opus
  attack, about ten minutes, then rounds 3 and 4 proceed as planned.
- B. Revert (S6) to its pre-fix wording and instead qualify (S13) so it does not contradict
  (S6). Also one gate, but it touches the Blackwell block that already passed.
- C. Stop the operation here. Records and proof fragments stay uncommitted in the worktree.

Nothing has been committed. The worktree holds the five proof fragments, the three record
scripts, one full-grid record, and the appendix edits.
