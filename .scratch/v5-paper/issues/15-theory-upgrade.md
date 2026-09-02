# 15 · Theory upgrade: information is monotone in the rule, noise robustness is not

**Lane:** theory and paper. **Routing:** batch 4, on top of the delivered v5 paper (checkpoint 3).
**Blocked by:** 14 (delivered). **Blocks:** nothing. **Triage:** superseded by 16 on 2026-09-02.
The batch runs from 16; the sections of this file that 16 lists as inherited bind as written here.

Revised 2026-09-02 after GPT Pro's review of the first draft
(`.scratch/v5-paper/hunt/pro_response.md`) and an independent Fable review of that review. Both
are input, never authority, never cited. This file is final; the batch runs from it.

Inputs: the four hunt memos and attack records under `.scratch/v5-paper/hunt/` (every candidate
passed writer, then an independent Opus attacker), the committed grid records under
`numerical_v4/checks/`, and the delivered `paper.tex`, `appendix.tex`, `proofs/`.

## Problem statement

The delivered paper says that tightening a disclosure rule lowers the noise sensitivity of the
engagement premium at fixed policies, one leg proved and one leg on the grid, and that
shortening the clock does so when a composition ratio is at most one. A reader takes that as
"more disclosure, cleaner prices", which is the ordinary intuition, and the paper reads as a
refinement of it. The order size of two noise lumps reads as a convenience and the benchmark
policy as arbitrary.

The hunt proved four results that turn the paper's message from a refinement into a contrast,
and the record already contains the instance that makes the contrast bite. None of it is in the
paper.

## Solution

The paper states a contrast between two things a disclosure rule does, proves both halves, and
names the mechanism. The abstract's central sentences, as the batch prints them:

> At fixed policies and a common liquidity, tightening either dial makes the market's
> control-node experiment weakly more informative in Blackwell's order, because the filing tuple
> identifies the blockholder's signal. That order does not settle what liquidity does to prices.
> For either dial, the tighter rule lowers the liquidity sensitivity of the engagement premium
> exactly when the premium mass it removes from the pool, the re-pricing of what stays pooled
> included, lies in a band set by the pool's own sensitivity and the share removed. On the
> calibration the band holds on the whole liquidity interval from 0.15 to 0.85, and for every
> pair of both dials it fails on an open interval below it, around the liquidity at which the
> looser pool's sensitivity changes sign, where the tighter rule is the more noise-sensitive one.

1. **Information is monotone in the rule.** Tightening either dial at a common liquidity and
   fixed policies is a Blackwell improvement of the market's experiment at the control node. It
   holds under the standing conditions together with the noise channel and the flagged-tuple
   decoder, both stated as standing conditions. The market knows the blockholder is engaged and
   the filing tuple identifies her signal. This is the paper's first economic result.
2. **Noise robustness is not implied by it.** At the control node, liquidity enters the
   engagement premium only through the pooled cell. A tighter rule removes histories from the
   pooled cell, and the looser pool's sensitivity is a mass-weighted average of the survivors'
   sensitivity and the net cut leg, the sensitivity per unit mass of what was removed, survivor
   re-pricing included. The same identity holds for both dials. The composition ratio is at most
   one exactly when the net cut leg lies between the pool's sensitivity and (2 minus φ)/φ times
   it; total sensitivity falls exactly when the net cut leg lies between zero and 2/φ times the
   pool's sensitivity, so the weight leg can attenuate even when the removed histories were less
   sensitive than the pool. A one-crossing lemma on the liquidity-free coefficients decides the
   band on any liquidity interval above a computable cutoff; its calibration application is
   NUMERICAL.
3. **The reversal.** Each pool's sensitivity has one sign change in liquidity and the two pools'
   zeros differ, so on an open interval around the looser pool's zero the tighter rule has
   strictly larger total sensitivity. The paper reports that interval for every non-null pair of
   both dials, inward-rounded, with the magnitudes beside it (three to four orders below the
   grid values), and never says that thin-market prices are volatile.
4. **The mechanism is inference from silence.** The net cut leg splits into a caught-only leg
   and a re-pricing term δ scaled by (1 minus φ)/φ: the histories that stay pooled are re-priced
   because the absence of a filing now says more. This is the interpretation the paper gives
   and it carries no label. The split is reported at every node from a record. A sentence that
   one term dominates the other enters only if the record shows it at every node, with the
   record's ratio, never a round number.
5. **The order size and the benchmark are defended.** Among positive integer multiples of one
   noise lump, order size two is the unique size whose binary order-mark channel is an exact,
   non-trivial erasure family over the whole interior liquidity range: at size one the
   higher-liquidity experiment is never a garbling of the lower one on any nondegenerate mark-path
   set, and at sizes three and above each binary order mark is decoded. The benchmark policy's
   interim regret, a certified upper bound on the largest one-step deviation gain at benchmark
   prices and beliefs over the computational signal support, is reported at every node with the
   convention and a normaliser.

The abstract, the introduction and the conclusion are rewritten. The model, the factorisation,
the existing theorems and their proofs are not rewritten; they are reordered, relabelled and
extended as listed below.

## User stories

1. As a reader of the abstract, I want the two central sentences above, so that I know the contrast before the model.
2. As a reader of the introduction, I want the Blackwell result stated first among the results, so that the sensitivity results read as the surprise.
3. As a reader of the introduction, I want an explicit sentence that a Blackwell order at fixed liquidity does not sign the liquidity sensitivity of the premium, so that I do not conflate the two objects.
4. As a referee, I want the Blackwell theorem stated at the control date with every hypothesis numbered in the standing-condition scheme, the noise channel and the flagged-tuple decoder among them, so that I can check what it rests on.
5. As a referee, I want the theorem to name the flagged-tuple decoder as its load-bearing hypothesis and point to the model paragraph that defends the tuple, so that the result is not read as free.
6. As a referee, I want strictness and equivalence stated per comparison: strict on the threshold ladder at the five-round clock where the cut has positive mass, Blackwell-equivalent at the null ten-round threshold cuts, and the clock comparison a separate non-null comparison, so that no sentence overreaches the theorem.
7. As a referee, I want the paper never to claim a strict Blackwell order from a change in the flagged share alone, so that strictness rests on positive cut mass plus the decoder.
8. As a reader of the model section, I want one paragraph on the order-size trichotomy with the proof in the appendix, so that the normalisation reads as a transparency choice.
9. As a referee, I want the erasure proposition stated at the channel level and transferred to the pooled experiment only under a nondegenerate mark-path set, with the one-round decision-problem value scoped to one coordinate, so that no side remark is false over the horizon.
10. As a reader of the results section, I want the who-gets-caught corollary restated at the threshold margin with the same words after the clock-indexed sets and kernels are replaced by their threshold counterparts, so that both dials visibly obey one accounting law.
11. As a reader, I want the removed histories' leg called the net cut leg everywhere, the caught-only leg and the re-pricing term named, and the split reported at every node, so that "who gets caught" is read honestly.
12. As a referee, I want the composition condition on a liquidity interval decided by the gated one-crossing lemma on the coefficients, with the cutoff, the sign lists and their margins reported, so that the grid claim becomes an interval claim.
13. As a reader of the calibration section, I want the total-sensitivity reversal interval for every non-null pair of both dials, inward-rounded, with the composition interval beside it and the magnitudes at the interval and at the grid, so that the contrast is shown on the paper's own numbers and read at its true size.
14. As a referee, I want the reversal proved as a lemma from one crossing at both pools and distinct roots, so that the reversal is a structural fact and not a grid coincidence.
15. As a reader of the calibration section, I want the benchmark's interim regret bound at every node in one sentence and one table row, with the deviation convention and the normaliser stated, so that "why this policy" has a number and a definition.
16. As a referee, I want the ten-round threshold comparisons marked as boundary checks where the cut is null, so that a degenerate cell is not read as a finding.
17. As a referee, I want the standing conditions to state the noise channel and Borel regularity of the policy objects, so that every kernel expectation is well defined.
18. As a referee, I want one sentence reconciling the off-path belief floor in the records with the exact liquidity representation, with the perturbation bound compared to the smallest sign margin, so that the records and the lemma agree.
19. As a referee, I want the standing-condition citation in the corollary's hypothesis corrected (liquidity enters in one place is (S10), fixed policies is (S11)), so that the numbering is consistent.
20. As a reader, I want every new statement to carry the label it holds, every label to come from the attack gate and not from prose, and any post-gate edit to a statement or proof to reopen the gate, so that the honesty rules hold on the upgraded paper.
21. As a reader, I want every new number to render from a result file that the number guard asserts against, so that no number in the paper is typed by hand.
22. As the author, I want the existing theorems, corollary and proofs untouched except for the reorder, the renaming, the corrected citation and the reconciliation sentence, so that no PROVED result reopens its gate.
23. As the author, I want the paper to say nothing about the hunt, the memos, the external reviews, or any earlier version, so that the paper stays the only record.
24. As the author, I want both PDFs recompiled clean, inspected page by page, unslop-gated, and delivered, so that the upgraded paper replaces the delivered one in full.
25. As a reader of the conclusion, I want the fixed-policy scope stated plainly with the regret bound as its quantitative answer and no claim that it establishes existence or robustness to a reacting blockholder, so that the paper owns its limit.

## Implementation decisions

- **Placement.** In the results section the partition lemma stays first, because the theorem's
  statement uses the two cells and the flag. The Blackwell theorem follows it immediately, then
  the non-implication sentence of story 3, then the two-cell decomposition, the flagged cell's
  invariance and the factorisation as a following subsection. The introduction leads with the
  Blackwell result. The trichotomy paragraph goes into the order-size subsection of the model,
  its proposition and proof into the appendix's garbling section, stated before the order-size-two
  lemma with a local auxiliary integer order size. The threshold-margin restatement, the split
  identity, the one-crossing lemma and the reversal lemma go into the who-gets-caught subsection
  and its appendix section, retitled for nested cuts under both dials. The regret sentence and
  table row and the reversal intervals go into the calibration section.
- **Statements.** The Blackwell theorem is stated at the control date, on the flagged region of
  the tighter rule; corollaries (posterior risk, the two-parameter chain with the garbling lemma)
  are separate statements. The strictness corollary (positive newly flagged mass, nonatomic signal
  there, finite pooled range) is a separate gated statement. The trichotomy proposition follows
  the hunt memo's statement, with its nondegeneracy and noise hypotheses named, not the weaker
  order-size-one clause of the external review. The one-crossing lemma is the hunt memo's
  Descartes argument on the reversed coefficient polynomial: one sign change in each pool's
  coefficient list and one in their difference give one positive root each, and above the largest
  root the band holds. The reversal lemma states that one crossing at both pools with distinct
  roots gives a strict reversal of total sensitivity on an open interval around the looser pool's
  root. The regret statement is an upper bound on the essential supremum of the one-step
  deviation gain over the truncated signal support, at benchmark prices and beliefs.
- **The corollary is not restructured.** A generic nested-cut proposition replacing both
  corollaries is not adopted. The threshold-margin restatement carries the content.
- **Standing conditions.** Add the noise channel (independence of the noise marks from value,
  signal noise and bidder draw; independence across dates; the ternary law) and the flagged-tuple
  decoder as two new numbered conditions. Add Borel regularity to the selector, stake-path and
  no-feedback conditions as a clarification, recorded as such in the batch result, with the
  attacker asked to confirm that no existing proof changes. Update every "(S1) to (S11)" citation.
  Correct the corollary's (C-1) citation from (S11) to (S10) and cite (S11) separately.
- **Renaming.** The leg written s_B is the net cut leg everywhere: paper prose, corollary
  statement and proof, the reading paragraphs, the abstract, the Figure 2 legend and caption.
  The leg written with a tilde is the caught-only leg. One glossary entry "Net cut leg" is added
  to CONTEXT.md. The condition the paper prints as Condition 1 keeps that name; "Condition D" does
  not appear in the paper.
- **Labels at write time.** New statements carry no label until the attack gate returns. The
  expected outcome, set at the checkpoint and not by the writer: the Blackwell theorem, the
  trichotomy, the threshold-margin restatement, the split identity, the one-crossing lemma and
  the reversal lemma PROVED; the strictness corollary PROVED if it passes and absent otherwise;
  the sign lists, cutoffs, intervals, magnitudes, the split at the nodes and the regret bound
  NUMERICAL with the grid and the calibration named.
- **Records.** Two new check records under the theory-code checks, each with the provenance block
  of the existing records. The cut record carries, per non-null pair of either dial: the
  coefficient lists and sign lists with their smallest margins, the roots and the cutoff in
  high-precision arithmetic, the total-sensitivity reversal interval with a Lipschitz cover on a
  dense mesh and inward-rounded endpoints, the composition interval beside it, the magnitudes of
  both rules' sensitivities inside the interval and at three grid points, the split (pool
  sensitivity, survivor sensitivity, net cut leg, caught-only leg, re-pricing term, φ) at every
  grid node with the three residuals of the identities, a cancellation measure for the scaled
  re-pricing term, the off-path floor's uniform perturbation bound on the coefficients against the
  smallest sign margin, and the newly flagged masses per comparison. The regret record is the
  hunt's, re-run through a check run with provenance, the deviation convention (benchmark pass
  fixed, reference belief off path, truncated support, tie rule) and a normaliser in the record.
  The number guard grows by one test per record.
- **Compute.** No cold solve. The coefficients exist in the committed revelation record; the
  split needs level-set sums under both rules' kernels for the cell events, a handful of pooled
  passes; the finite-difference route needs about 120 pooled passes. Under an hour on the machine,
  one run at a time under the compute lock. The horizon is not lowered.
- **Certification standard.** No interval arithmetic and no coefficient enclosures. The word
  "certificate" is reserved for the PROVED one-crossing lemma; the calibration section says
  "the lemma applied to the record's coefficients" and labels it NUMERICAL. The reversal
  intervals are covered on a mesh by the polynomial's Lipschitz bound, the same method as the
  regret record.
- **Prose.** The abstract, the introduction and the conclusion are rewritten around the two
  central sentences. Section 2 of the session spec carries them. No ADR is written.
- **Sequence inside the batch.** Records first, then the appendix statements and proofs, then
  the attack gate per statement, then the paper prose, then the label-and-compile check, one
  referee read, one author fix, the gate reopened for any statement the fix touches, compile,
  inspect, deliver.

## Testing decisions

- A good check reads a statement and its proof and tries to break it, or reads a record and
  recomputes it by an independent route. It does not re-read the memo or the worker's reasoning.
- **Attack gate**, one per new statement: writer, then an independent Opus attacker with the
  statement, the model and the proof. Any edit to a statement, a hypothesis, a kernel, a
  polynomial or a proof step after the gate reopens it. Prior art: the `02-attack`, `03-attack`,
  `13-attack` and `13-attack-2` run records.
- **Check runs** for the two records, at every node rather than one: the sign lists, roots and
  cutoffs recomputed in high-precision arithmetic from the record's coefficients; the closed-form
  derivative compared with central finite differences of the pooled premium from pooled passes at
  three liquidities per node, one inside the reversal interval, with the tolerance stated against
  the derivative scale and the sign margin; the three identity residuals with absolute and
  scale-adjusted values; the regret bound recomputed at the attaining piece and every cutoff and
  beaten by a refined search. Prior art: `03-grid-judge`, `01-verify`, the hunt's attack scripts.
- **Number guard**: the existing test module, extended with one test per new record, asserting
  every rendered string appears in the paper verbatim.
- **Label-and-compile check** over the final tree, with a substantive hypothesis audit: every
  statement labelled; no absent result mentioned; no process language; every standing-condition
  citation resolves to the right condition; no "(S1) to (S11)" left; no differentiability claimed
  on a null cell; no ratio where the denominator sensitivity is zero; "prices" never used where
  only the engagement premium is proved; "caught leg" never used for the net quantity; compile
  clean in the order the project file gives; cross-document references regenerated from labels.
  Prior art: `11-check-2`, `13-check-2`.
- **One referee read** at journal standard, then one author fix pass, then the unslop gate.
  Prior art: `12-referee-3`, `14-unslop`.

## Out of scope

- Restructuring the who-gets-caught corollary into a generic nested-cut proposition.
- Equilibrium existence, a reacting blockholder, or any best-response layer. The regret bound
  quantifies the fixed-policy approximation under its stated convention and establishes nothing
  beyond that.
- The robustness neighbourhood around the benchmark policy. Deferred; it enters only if compute
  allows after every gate above has passed.
- Interval arithmetic in the pooled pass or the pricing root; coefficient enclosures; a keyed
  TeX-macro rendering refactor for the number guard.
- Any change to the calibration, the empirics, the registered spec, or the figures beyond
  regenerating the ones whose legend or record changes.
- Removing objects the external review flagged that are not in the paper.
- A new ADR or a CONTEXT.md rewrite beyond the one glossary entry.

## Further notes

- Fail twice, stop, per statement. A statement that fails its attack twice is absent from the
  paper, and the paper does not mention it. The strictness corollary and the reversal lemma are
  the two statements the abstract can survive without; the abstract's reversal clause then becomes
  a NUMERICAL sentence off the record.
- The multiplier (1 minus φ)/φ is near forty on the calibration. That number is not a finding.
  Whether the re-pricing term dominates the caught-only leg is decided by the split record.
- Any future external pack quotes the delivered paper, not the inherited draft, which produced
  three false alarms in the first review.
