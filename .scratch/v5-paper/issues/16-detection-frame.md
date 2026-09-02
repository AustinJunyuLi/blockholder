# 16 · Theory upgrade: who gets caught, literally. The rule catches the fast, the tape catches the slow

**Lane:** theory and paper. **Routing:** batch 4, on top of the delivered v5 paper (checkpoint 3).
**Blocked by:** 14 (delivered). **Blocks:** nothing. **Triage:** ready-for-agent.
**Supersedes:** 15. Every decision of 15 that this file lists as inherited binds as written there.
Where the two differ, this file governs.

Written 2026-09-02 after GPT Pro's review of the framing pack
(`.scratch/v5-paper/hunt/gpt-pro-5/response.md`) and an independent Fable consult on the same pack
(`.scratch/v5-paper/hunt/gpt-pro-5/fable-consult.md`). Both are input, never authority, never
cited. The record facts below were re-verified by the orchestrator from the committed check files.

Inputs: the four hunt memos and attack records under `.scratch/v5-paper/hunt/`, the committed
grid records under `numerical_v4/checks/`, the delivered `paper.tex`, `appendix.tex`, `proofs/`.

## Problem statement

The delivered paper measures liquidity through the absolute sensitivity of the engagement premium
and never states the sign. The committed record states it: the pooled premium rises monotonically
in liquidity at all 71 grid points at every one of the ten nodes (`t2_t1_check.json`,
`kappa_profiles`, factor 1.15 at the tightest threshold to 2.24 at the long clock), and the
one-crossing lemma of the hunt certifies the rise above a root below 0.15 from the record's own
coefficients. The clock's effect on the premium level grows from under one percent at κ = 0.15 to
between 18 and 54 percent at κ = 0.85 across the threshold ladder. None of this is in the paper.

Three facts on the existing model explain the sign, and none is stated. First, by the tower
property, the engagement premium equals the premium wedge times the probability that a bidder
enters against a blockholder who is in fact engaged, and the Voice mass is free of liquidity and
of the rule at fixed policies. Second, only Voice plans carry marks, so one revealed building mark
sets the engagement posterior to one: on the tape an engaged blockholder is either fully detected
or silent, and a type with n building rounds is silent with probability exactly (κ/2)^n. Third,
the flagged set at any date is an upper set in the signal: the rule catches the fast builders,
who place the fewest orders and are exactly the types the tape misses most. The filing and the
tape are the market's two detection technologies, and they catch opposite blockholders.

Ticket 15's contrast (information is monotone in the rule, noise robustness is not) is true and
survives in full, but its reversal lives three to four orders below the grid and reads as
bookkeeping. This ticket puts the sign first and keeps 15's results as the second half.

## Solution

The paper's title becomes *Who Gets Caught: Disclosure Rules, Liquidity and the Undetected
Blockholder*. The abstract's central sentences, as the batch prints them, with the bracketed words
chosen by the orchestrator at the checkpoint from the detection record and never by the writer:

> At fixed trading policies the engagement premium equals the premium wedge times the probability
> that a bidder enters against an engaged blockholder, and that probability is [higher / several
> times higher] when the market has not yet detected her. The filing and the trading tape are the
> market's two ways of detecting her, and they catch opposite blockholders: the rule catches the
> fast builders who place the fewest orders, the tape catches the slow builders who place many, so
> a disclosure rule's effect on the premium grows with liquidity, from under one percent in thin
> markets to [the record's share] in liquid ones on the calibration.

Supporting sentences of the abstract: tightening either dial is a Blackwell improvement of the
market's experiment (PROVED); the tape at the paper's order size is an exact erasure channel and
more liquidity is a garbling of it (PROVED); a shorter clock lowers the pool's liquidity
sensitivity almost entirely through what silence tells the market about the histories it does not
catch (NUMERICAL, the record's share at every node); the descriptive empirics as now.

Results, in the order the paper carries them:

1. The partition and the two-cell decomposition (existing, PROVED).
2. **Entry identity (new).** The engagement premium equals Δm times the Voice mass times bidder
   entry conditional on engagement; the same identity per cell; the Voice mass is free of κ and of
   the rule at fixed policies. One line from the tower property, because the price and the entry
   probability are functions of the public information set.
3. **Information is monotone in the rule** (batch 4, PROVED): the Blackwell theorem for both
   dials at the control date, then the flagged cell's κ-invariance (existing): the rule's reach
   does not depend on liquidity.
4. **The tape (existing plus new corollary).** The erasure form at order size two, the trichotomy
   proposition in the model section (batch 4), the garbling lemma in κ (existing), and the new
   **detection lemma**: a revealed building mark sets the engagement posterior to one; an engaged
   type with n building rounds before the date is silent with probability (κ/2)^n. Hypotheses
   named: the noise channel; the menu form under which only Voice plans carry positive marks.
5. **Who gets caught (new).** The flagged set at any date is an upper set in the signal and
   consists of the types with the fewest building rounds, so the silent probability is highest
   exactly on the types the rule catches. Hypotheses named: the target stake increasing and the
   accumulation length weakly decreasing in the signal, as the menu states them. **The silence
   lemma (new):** on every history that stays pooled, the tighter rule lowers the engagement
   posterior and the posterior mean of the fundamental, because it removes an upper set of engaged
   types from the conditioning set. Hypotheses on the signal and fundamental ordering named by the
   writer and tested by the attacker.
6. **Entry against the undetected.** The lemma with real risk: at the pinned pricing root the
   price is increasing in the engagement posterior and the fundamental posterior, so bidder entry
   is decreasing in both; on a silent history entry is therefore higher than on a detected one at
   the same fundamental posterior. If it passes, the abstract's first sentence is signed by proof.
   If it fails its gate, the entry gap stays NUMERICAL from the record and the abstract says
   "on the calibration".
7. **The exact liquidity representation** (existing lemma, new reading): the derivative of the
   pooled premium in κ is minus half the wedge times the total marginal value of one more revealed
   round. **Monotone premium (NUMERICAL):** the one-crossing lemma (batch 4) applied to the
   record's coefficients certifies that the pooled premium is strictly increasing in liquidity
   above a root below 0.15 at every node.
8. **Levels on the calibration (NUMERICAL, from the detection record):** the premium's rise across
   the grid at every node; entry by detection state (flagged, tape-detected, silent) and the
   decomposition of the premium across the three states; the silent mass per node; the clock's
   and the threshold's effect on the level at every κ, with the threshold's effect stated as mixed
   and below 0.3 percent in magnitude beneath κ = 0.45 rather than hidden; the level version of
   the cut split for both dials (the caught histories' contribution against the survivors').
9. **The two dials on liquidity sensitivity** (existing plus batch 4): the factorisation, the
   threshold dial, the clock equivalence, the cut identity at both margins with the bands, the
   net cut leg's split into a caught-only leg and a re-pricing term with the record's share at
   every node (already on record for the clock cut: 93 to 98 percent, common signs, at all five
   nodes), the one-crossing lemma deciding the band on an interval.
10. **Calibration remarks:** the reversal intervals with their magnitudes as a remark, not a
    result; the benchmark regret bound with its convention; the fixed-policy scope stated once:
    the regret bound covers plan choice at benchmark prices and beliefs, not order size or speed,
    and the paper claims nothing about a reacting blockholder.
11. Empirics: E1 and the clock paragraph, unchanged. E2 is absent and unmentioned.

## User stories

Stories 4 to 9, 11, 12, 15 to 25 of ticket 15 are inherited verbatim. Stories 1 to 3, 10, 13
and 14 of ticket 15 are replaced by the following.

1. As a reader of the abstract, I want the two central sentences above, so that I know what the
   rule does to the premium and why before the model.
2. As a reader of the introduction, I want the entry identity stated first among the results and
   the two detection technologies named in the first paragraph, so that "who gets caught" has a
   literal answer on page one.
3. As a reader of the introduction, I want the sign of liquidity on the premium stated in words
   with its calibrated size, so that the paper's main comparative static is a level and not an
   absolute derivative.
4. As a referee, I want the entry identity stated with the exact measurability hypothesis (price
   and entry are functions of the public information set) and the Voice mass shown κ-free and
   rule-free under (S11), so that a one-line result is not read as free.
5. As a referee, I want the detection lemma to name the menu form under which only Voice plans
   carry positive marks as a hypothesis, so that the binary detection does not rest on the
   calibration silently.
6. As a referee, I want the upper-set statement to name the monotone target stake and the weakly
   decreasing accumulation length as hypotheses, so that "the rule catches the fast" is a theorem
   under the menu's stated form and not an observation about the code.
7. As a referee, I want the silence lemma's hypotheses on the ordering of signal and fundamental
   stated and its conclusion restricted to histories with positive probability under both rules,
   so that no sentence is claimed on a null history.
8. As a referee, I want the entry-against-the-undetected lemma either PROVED with its monotonicity
   argument at the pricing root or absent, with the entry gap then reported as NUMERICAL, so that
   the abstract's strongest word carries the label it holds.
9. As a reader of the calibration section, I want one table of entry by detection state at the
   median node and three liquidities, with the silent mass beside it, so that "higher when
   undetected" has a number and a denominator.
10. As a reader of the calibration section, I want the clock's and the threshold's level effects
    at every κ in one figure and one sentence each, with the threshold's mixed region stated, so
    that the paper shows the sign it claims and the region where it does not hold.
11. As a reader of the calibration section, I want the reversal of ticket 15 kept as a one-sentence
    remark with its magnitudes, so that the record is complete without the remark reading as a
    result.
12. As a reader, I want the batch-4 Blackwell theorem, trichotomy, cut identity, one-crossing
    lemma and regret bound carried with the roles listed above, so that nothing that passed its
    gate is dropped.

## Implementation decisions

Inherited from ticket 15 unchanged: standing conditions (noise channel and flagged-tuple decoder
added; Borel regularity; citation fixes), renaming (net cut leg, caught-only leg, re-pricing
term), labels at write time, the cut record and the regret record with their contents, the
certification standard, the compute rule (no cold solve, one run at a time under the compute
lock, the horizon is not lowered), the sequence inside the batch, and "the corollary is not
restructured". The following are new or changed.

- **Placement.** Results section: partition lemma, entry identity, Blackwell theorem, the
  non-implication sentence, flagged invariance, the tape subsection (detection lemma), the
  who-gets-caught subsection (upper set, silence lemma, entry against the undetected), the
  liquidity representation with the monotone-premium corollary, then the sensitivity results of
  ticket 15 as one subsection. Calibration section: levels first, then the detection table, then
  the split and the bands, then the remarks. The model section gains the trichotomy paragraph as
  in 15. The introduction leads with the entry identity and the two detection technologies.
- **New statements.** Entry identity (lemma), detection lemma, upper-set lemma, silence lemma,
  entry-against-the-undetected lemma, monotone-premium corollary (NUMERICAL, the one-crossing
  lemma on the record's coefficients). Each PROVED candidate goes through the attack gate; the
  expected outcome set at the checkpoint: entry identity, detection lemma and upper-set lemma
  PROVED; silence lemma PROVED if its ordering hypotheses hold as stated and absent otherwise;
  entry-against-the-undetected PROVED if it passes and absent otherwise, with the abstract's
  wording falling back as in story 8.
- **The detection record.** One new check record under `numerical_v4/checks/`, provenance block
  as the existing ones, built from the erasure representation's level-set sums with the entry
  probability and the engagement posterior kept separately per level set. Per node and per grid
  κ: the silent mass Σ_n w_n (κ/2)^n; entry conditional on Voice in the flagged cell, on
  tape-detected pooled histories, on silent pooled histories; the premium decomposed across the
  three states; the level profile of the pooled and total premium (regrouped from the existing
  profiles and checked against them to 1e-12); the clock's and the threshold's level effect per κ
  for each adjacent pair; the level cut split for both dials. The number guard grows by one test.
  Editorial rule, fixed now: if entry on silent histories divided by entry on tape-detected
  histories at the median node and κ = 0.5 is below two, the abstract says "higher" and never
  "several times higher".
- **Clock ladder extension.** Orchestrator's ruling: the long clock T = 10 equals the horizon and
  its flagged mass (6.8e-4) sits below the code's degeneracy floor, so every ten-round threshold
  node is one pool. The detection record and the level effects are therefore also computed at
  T = 3, added to the clock ladder as a stated grid extension, giving one interior clock pair
  (3 against 5) beside the existing pair (5 against 10). The existing proved comparisons, their
  records and their statements are untouched; the paper marks the ten-round nodes as boundary
  checks as story 16 of ticket 15 already requires. Cost: pooled passes at five threshold nodes,
  seconds each.
- **Records the abstract's words render from.** "[higher / several times higher]" and "[the
  record's share]" are chosen by the orchestrator at the checkpoint from the detection record and
  written into the number guard as rendered strings. The writer leaves the brackets.
- **Title.** `paper.tex` title and the deliverable name change as above. Running heads and the
  session note follow.
- **Glossary.** CONTEXT.md gains "Detection", "Silent history" and "Net cut leg", and the "Two
  dials" entry is rewritten to the new headline. The orchestrator makes these edits before the
  batch starts.
- **Prose.** Abstract, introduction, conclusion rewritten around the central sentences; section 2
  of the session spec carries them. No ADR. The paper never says "hump", never mentions order size
  one, never mentions an execution response, and never describes what the sensitivity results
  used to be.

## Testing decisions

Inherited from ticket 15: the attack gate per statement with reopening on any post-gate edit,
the check runs for the cut and regret records, the number guard extension, the label-and-compile
check with its hypothesis audit, one referee read, one author fix, the unslop gate. Added:

- **Detection record check run.** At every node: the silent mass recomputed from the mark-path
  weights by an independent enumeration; the three conditional entries recomputed from a pooled
  pass with the cells and detection states classified directly on histories, agreeing with the
  level-set route to the stated tolerance; the three-state decomposition summing to the premium
  to 1e-12; the level profiles matching `t2_t1_check.json` to 1e-12; the T = 3 passes with the
  same provenance checks as the T = 5 ones.
- **Hypothesis audit additions.** "Detected" and "silent" used only for pooled histories;
  "caught" used only for flagged histories; "entry" never used where the record carries the
  premium; the upper-set lemma cited only with its menu hypotheses; no sentence says liquidity
  raises the takeover premium, only the engagement premium.

## Out of scope

Everything in ticket 15's list, and in addition: any execution-mode or order-size choice by the
blockholder; any self-consistent repricing; any change to H; the E2 exercise or any run-up
versus jump statement; a v6 branch. The execution question is a separate paper and is not
mentioned.

## Further notes

- Fail twice, stop, per statement. The abstract survives without the silence lemma and without
  entry-against-the-undetected; it does not survive without the entry identity, the detection
  lemma and the upper-set lemma, which are one-line results on the model and whose failure stops
  the batch for a judgment.
- The multiplier (1 minus φ)/φ is not a finding. The split's share at every node is.
- Any future external pack quotes the record's `kappa_profiles` for the premium's shape. The
  fifth pack described a plateau that the record contradicts, and GPT Pro's pivot reasoned from
  that description.
