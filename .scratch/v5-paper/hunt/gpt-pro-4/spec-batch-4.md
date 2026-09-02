# 15 · Theory upgrade: information is monotone in the rule, noise robustness is not

**Lane:** theory and paper. **Routing:** batch 4, on top of the delivered v5 paper (checkpoint 3).
**Blocked by:** 14 (delivered). **Blocks:** nothing. **Triage:** ready-for-agent.

Inputs: the four hunt memos and their attack records under `.scratch/v5-paper/hunt/` (every
candidate passed writer, then an independent Opus attacker), GPT Pro's review at
`.scratch/v5-paper/hunt/pro_response.md` (input, never authority, never cited), and the delivered
`paper.tex`, `appendix.tex`, `proofs/`.

## Problem statement

The delivered paper says that tightening a disclosure rule lowers the noise sensitivity of
prices at fixed policies, with one leg proved and one leg on the grid, and that shortening the
clock does so when its composition ratio is at most one. A reader takes that as "more disclosure,
cleaner prices", which is the ordinary intuition, and the paper reads as a refinement of it. The
paper also carries an order size of two noise lumps that a referee reads as a convenience, and a
benchmark policy that a referee reads as arbitrary.

The hunt proved four results that turn the paper's message from a refinement into a contrast,
but none of them is in the paper.

## Solution

The paper states a contrast between two things a disclosure rule does, proves both halves, and
names the mechanism.

1. **Information is monotone in the rule.** Tightening either dial, at a common liquidity and
   fixed policies, is a Blackwell improvement of the market's experiment at the control node.
   This is the paper's first result. It holds always.
2. **Noise robustness is not.** Liquidity enters prices only through the pooled cell. A tighter
   rule removes histories from the pooled cell, and the looser pool's sensitivity is a
   mass-weighted average of the survivors' sensitivity and the net sensitivity of what was
   removed. The same identity holds for both dials. Prices become less noise-driven if and only if
   the removed histories carried more than their share of the noise. A polynomial certificate
   decides this exactly on any liquidity interval, and the paper reports the interval at low
   liquidity where a tighter threshold makes prices more noise-driven.
3. **The mechanism is inference from silence.** At the threshold margin, the direct contribution
   of the caught histories is small next to the re-pricing of the histories that stay pooled. The
   rule disciplines prices through what the absence of a filing tells the market. The paper reports
   both legs at every node and words the who-gets-caught reading accordingly.
4. **The order size and the benchmark are defended by results.** Order size two is the unique
   integral order size at which more liquidity is an exact, non-trivial erasure of the pooled
   experiment. The benchmark policy's maximal regret is reported at every calibration node.

The abstract and the introduction are rewritten around the contrast. The model, the factorisation,
the existing theorems and their proofs are not rewritten.

## User stories

1. As a reader of the abstract, I want one sentence that says information is monotone in the rule and noise robustness is not, so that I know what the paper claims before the model.
2. As a reader of the introduction, I want the Blackwell result stated before the sensitivity results, so that the sensitivity results read as the surprise.
3. As a reader of the introduction, I want an explicit sentence that a Blackwell order at fixed liquidity does not sign the liquidity sensitivity of the premium, so that I do not conflate the two objects.
4. As a referee, I want the Blackwell theorem stated at the control date with every hypothesis numbered in the standing-condition scheme, so that I can check what it rests on.
5. As a referee, I want the Blackwell theorem to name the flagged-tuple identification condition as its load-bearing hypothesis and point to the model paragraph that defends the tuple, so that the result is not read as free.
6. As a referee, I want the strictness of the Blackwell order at the five-round clock argued from the tighter tuple identifying a continuous signal, and the ten-round corner reported as an equality, so that the theorem's bite on the calibration is stated and not implied.
7. As a referee, I want the paper never to claim a strict Blackwell order from a change in the flagged share alone, so that no sentence overreaches the theorem.
8. As a reader of the model section, I want one paragraph that says order size two is the unique integral order size with exact non-trivial erasure, with the proof in the appendix, so that the normalisation reads as a transparency choice.
9. As a referee, I want the erasure proposition trimmed to its two-round-safe content, with the one-round facts and the incomparability language absent, so that no side remark is false over the horizon.
10. As a reader of the results section, I want one remark that the who-gets-caught corollary holds verbatim at the threshold margin under a nested cut, so that both dials visibly obey one accounting law.
11. As a reader of the results section, I want the removed histories' leg named the net cut leg, with the caught-only leg and the survivor re-pricing term reported at every node, so that "who gets caught" is read honestly.
12. As a referee, I want the composition condition certified by a polynomial inequality on the image of a liquidity interval, with the endpoints and the critical points listed, so that the grid claim becomes an interval claim with an exact certificate.
13. As a reader of the calibration section, I want the exact low-liquidity interval on which a tighter threshold raises noise sensitivity reported as a result, so that the contrast is shown on the paper's own numbers.
14. As a reader of the calibration section, I want the benchmark policy's maximal regret at every node in one sentence and one table row, so that "why this policy" has a number.
15. As a referee, I want the ten-round clock threshold comparisons marked as a boundary check where the cut is null, so that a degenerate cell is not read as a finding.
16. As a referee, I want the standing measurability condition to say that the stake path and the plan are Borel functions of the type, so that every kernel expectation is well defined.
17. As a referee, I want one sentence reconciling the off-path belief floor in the records with the exact liquidity representation, with the perturbation bound stated, so that the records and the lemma agree.
18. As a reader, I want every new statement to carry the label it holds, and every label to come from the attack gate and not from prose, so that the honesty rules hold on the upgraded paper.
19. As a reader, I want every new number to render from a result file that the number guard asserts against, so that no number in the paper is typed by hand.
20. As the author, I want the existing theorems, corollary, proofs and figures untouched except for the remark and the reconciliation sentence, so that no PROVED result reopens its gate.
21. As the author, I want the paper to say nothing about the hunt, the memos, the external review, or any earlier version, so that the paper stays the only record.
22. As the author, I want both PDFs recompiled clean, inspected page by page, unslop-gated, and delivered, so that the upgraded paper replaces the delivered one in full.
23. As a reader of the conclusion, I want the fixed-policy scope stated plainly with the regret number as its quantitative answer, so that the paper owns its limit.

## Implementation decisions

- **Placement.** The Blackwell theorem opens the results section, before the partition and the
  factorisation, followed by the sentence of story 3. The erasure paragraph goes into the
  order-size subsection of the model, its proposition and proof into the appendix's garbling
  section. The threshold-margin remark and the certificate lemma sit in the who-gets-caught
  subsection and its appendix section. The regret sentence and table row go into the calibration
  section. The exact failure interval joins the calibration section's Condition D remark.
- **Statements.** The Blackwell theorem is stated at the control date only; corollaries (posterior
  risk, the two-parameter chain with the garbling lemma) are separate statements. The decoder
  condition is named as a hypothesis. The erasure proposition is the trichotomy at a fixed depth:
  order size one is not monotone, two is exact non-trivial erasure, three and above decodes. The
  certificate lemma states that the composition condition on a compact liquidity interval is
  equivalent to a fixed polynomial being non-positive on the image interval, and that this holds
  if and only if it holds at the endpoints and the real critical points.
- **The corollary is not restructured.** The generic nested-cut proposition GPT Pro proposed as a
  replacement for both corollaries is not adopted in this batch. The remark of story 10 carries the
  content. The replacement is a later version's question.
- **Nits.** Every attacker nit recorded in the hunt attack files is applied unless the attack file
  or the hunt log marks it as bookkeeping. GPT Pro's dispositions are input.
- **Labels at write time.** New statements carry no label until the attack gate returns. The
  expected outcome, set at the checkpoint and not by the writer: the Blackwell theorem, the
  erasure proposition, the threshold-margin remark and the certificate implication PROVED; the
  certificate's application to the calibration's coefficients, the failure interval, and the
  regret NUMERICAL with the grid named.
- **Records.** Two new check records under the theory-code checks: the certificate record (per
  threshold pair and per clock pair: the polynomial coefficients, the critical points, the
  endpoint values, the certified verdict, the failure interval, the net cut leg, the caught-only
  leg and the re-pricing term at every node, the residual of the cut identity) and the regret
  record (per node: the regret, the payoff level at the cutoff, the ratio). Both carry the
  provenance block of the existing records. The number guard grows by one test per record
  asserting that every rendered string appears in the paper.
- **Compute.** The certificate needs the cut coefficients per rule, which the existing pooled
  passes produce; no cold solve. The regret record exists in the hunt directory and is
  re-run through a check run so that it carries provenance. Runs go one at a time under the
  compute lock. The horizon is not lowered.
- **Prose.** The abstract, the introduction and the conclusion are rewritten. Section 2 of the
  session spec carries the new headline. No ADR is written for this batch; the session spec is the
  record of the change.
- **Sequence inside the batch.** Records first, then the appendix statements and proofs, then the
  attack gate, then the paper prose, then the label-and-compile check, one referee read, one
  author fix, compile, inspect, deliver. Labels enter the paper only after the gate.

## Testing decisions

- A good check reads a statement and its proof and tries to break it, or reads a record and
  recomputes one node independently. It does not re-read the memo or the worker's reasoning.
- **Attack gate**, one per new statement: writer, then an independent Opus attacker with the
  statement, the model and the proof, exactly as tickets 02, 03 and 13 ran it. Prior art: the
  `02-attack`, `03-attack`, `13-attack` and `13-attack-2` run records.
- **Check runs** for the two records: recorded provenance, a one-node independent recompute to
  the record's tolerance, and the certificate's verdict recomputed from the coefficients with
  independent code. Prior art: `03-grid-judge`, `01-verify`, and the hunt's attack scripts.
- **Number guard**: the existing test module, extended with one test per new record, asserting
  every rendered string appears in the paper verbatim.
- **Label-and-compile check** over the final tree: every statement labelled, no absent result
  mentioned, no process language, compile clean in the order the project file gives, cross-document
  references resolved. Prior art: `11-check-2`, `13-check-2`.
- **One referee read** of the upgraded paper at journal standard, then one author fix pass, then
  the unslop gate. Prior art: `12-referee-3`, `14-unslop`.
- **External review.** The delivered PDFs and this spec go to GPT Pro for one review before the
  batch starts. Its answer is input. It does not replace any gate above.

## Out of scope

- Restructuring the who-gets-caught corollary into a generic nested-cut proposition.
- Equilibrium existence, a reacting blockholder, or any best-response layer. The regret record
  is the paper's whole answer on this.
- The robustness neighbourhood around the benchmark policy (nearby cutoff policies). Deferred;
  it enters only if compute allows after every gate above has passed.
- Any change to the calibration, the empirics, the registered spec, or the figures beyond
  regenerating them if a record they draw from changes.
- Removing objects GPT Pro flagged that are not in the paper (inherited equilibrium machinery,
  the word "equilibrium" for the benchmark).
- A new ADR or a CONTEXT.md rewrite. The session spec's headline is updated instead.

## Further notes

- Fail twice, stop, per statement. A statement that fails its attack twice is absent from the
  paper, and the paper does not mention it.
- The pack sent to GPT Pro quoted the inherited draft's model section verbatim, which produced
  three false alarms. Any future pack quotes the delivered paper, not the inherited draft.
- The survivor re-pricing factor at the threshold margin (near forty at the calibration) is the
  sentence people will repeat. It is a NUMERICAL fact off the certificate record and is worded
  as one.
