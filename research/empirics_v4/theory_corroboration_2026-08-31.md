# How the empirics can corroborate the theory, leg by leg (2026-08-31)

Dated note under §0 rule 1. **No SPEC object changes and nothing here is adopted.**
It changes no prediction, test, sample rule, variable, window, filter, standard-error
rule or decision rule, proposes no new leg, and moves no honesty label. It reads the
frozen theory record and the committed estimate artifacts side by side and says which
theory claim each live leg can speak to. Every proposal that would touch a registered
rule is filed in §4b as a decision for Austin.

Sources read this pass: `research/empirics_v4/SPEC.md`; `empirics/output/*.json` and
`fact1_summary.csv`, `reparse_quarterly_parse_rates.csv`, `reparse_funnel.csv`;
`research/empirics_v4/decisions_2026-08-31.md`; `research/empirics_v4/did_matching_2026-08-31.md`;
and, in the theory worktree frozen at `65b8db3`,
`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/HANDOFF_sign.md`,
`MODEL_CARD.md`, `model_v4.md`, and `/Users/austinli/Projects/blockholder_v4_theory/draft_v3.tex`.

**The opinion this note defends.** The theory's headline object for the Feb-2024
acceleration is a window-margin sign, and that sign cannot be corroborated with the data
in hand. It is sign-only, it carries no magnitude that maps to a coefficient, and the
realised resolution on the estimand it maps to is 12.39 pp of abnormal return against a
point estimate of 0.0175 pp. The single theory object that sits inside the package's
reach is L2's zero on the flagged half of the timing split, and even that is a one-sided
non-refutation, because the pooled half came back a statistical zero too. The honest
December package reports three bounded nulls against their pre-fixed MDEs, prints the
bounded-null ladder as the control-outcome answer, and claims corroboration of exactly
one PROVED lemma, weakly.

---

## 1. What the theory actually delivers

### 1.1 The labels, and what each one is worth

The frozen record carries eight result rows and all eight are PROVED. Nothing in the
theory record is ESTIMATED, and the only NUMERICAL content is grid evidence attached to
hypotheses and to C1's node count. Four of the PROVED rows are weaker than their label
sounds, and the empirics lane needs the distinction.

**L2, flagged-cell liquidity invariance. PROVED, general, sign-free.** At fixed cutoff and
execution policies, the flagged tuple makes the pre-filing pooled history conditionally
independent of the value, signal and synergy draws, so the flagged posterior, the flagged
price, the entry probability and the flagged-cell premium are all invariant to liquidity
(`blockholder_v4_theory/research/model_v4/MODEL_CARD.md:656`;
`.../model_v4.md:698`). This is the model's one clean liquidity comparative static and it
is a point at zero. `draft_v3.tex:759-774` calls it the theoretical statement behind the
empirics' identification claim. It needs no handoff, no calibration and no A(tau).

**T1, the weight-times-composition factorisation. PROVED at fixed policies, and it signs
no window margin.** Part A is an exact factorisation of the liquidity sensitivity into the
pooled cell's weight and the pooled cell's own sensitivity. Part B attenuates
unconditionally on the threshold margin because both ratios lie in the unit interval.
Part C is an iff. Window tightening attenuates if and only if the weight ratio times the
composition ratio is at most one, the weight ratio is proved to be at most one, and the
composition ratio is unsigned (`MODEL_CARD.md:664`; `model_v4.md:702`). The record's own
not-claimed list opens with a global window-margin attenuation sign
(`model_v4.md:784-789`), and the draft says the same in the paper's own voice. The
February 2024 acceleration is a window change and it lands on the margin where the theory
signs nothing (`blockholder_v4_theory/draft_v3.tex:866-869`).

**D1, the disclosure partition and the clock equivalence. PROVED.** The flag lands if and
only if the crossing date plus the window is inside the horizon, which is equivalent to
the stake path clearing the threshold by horizon minus window. This is what makes the
timing split a partition of histories rather than a labelling of them, and it is what
gives the exact identity that the price move from crossing to flag decomposes into the
run-up plus the filing-day jump (`draft_v3.tex:728-743`).

**L3, L4 leg 3 and T1 Part B are conditionals whose antecedent is measured false here.**
The chord restriction A(tau) fails at all 180 non-degenerate nodes of a 200-node exact
enumeration at the implemented calibration, and the SPEC already carries that fact and its
consequence, which is that no mechanism sentence may lean on the chord formula
(`SPEC.md §0.1`, verbatim from `HANDOFF_sign.md` §8). Those legs stay PROVED as
conditionals. At this calibration they say nothing about the implemented pooled cell.

### 1.2 The handoff sign, stated exactly

The single dependency the empirics lane has on the theory lane is `HANDOFF_sign.md`, and
the entry the SPEC consumes is §8, the two-round model at flagged weight near 13.8 percent,
not §1 to §6, which is a disclosure-regime margin experiment at flagged weight 0.037 whose
sign points the other way (`HANDOFF_sign.md` §8.1; `SPEC.md §0.1`).

What §8 delivers is a direction and nothing else. Cutting the window from 10 to 5 cuts the
liquidity sensitivity of the activism premium to between 18 and 77 percent of its
long-window value, at every node checked, 0 of 5 nodes above one at horizon 10 and 0 of 5
at horizon 12. In SPEC language that is Branch A, a positive delta on the liquidity by
post interaction given a negative pre-period slope on the five-day run-up
(`HANDOFF_sign.md` §8.1). Its honesty label is NUMERICAL. The file's own status word for
the re-run is VERIFIED, which certifies reproduction, not generality.

Four conditions travel with the sign and the SPEC restates all four
(`SPEC.md §0.1`).

1. Fixed policies. Cutoffs are frozen at the baseline equilibrium at every node. No
   general-equilibrium cutoff-shift term is signed on either entry.
2. The implemented calibration only, at cutoffs (1.240576, 1.531022), flagged weight
   13.8396 percent, disclosed share of engagements 61.1473 percent.
3. A(tau) measured to fail there, so nothing may lean on the chord-formula mechanism.
4. The horizon-12 column's composition ratio travels the chord route, so it is directional
   corroboration of the corner audit, not a second independent magnitude. Inside the same
   caveat sits the horizon-10 corner, where the long window is the corner case and the
   comparison is corner against interior rather than the two-interior comparison the
   theorem contemplates. The check flags itself as suspect for that reason
   (`HANDOFF_sign.md` §8.1, corner-caveat row).

### 1.3 What the sign is not

The sign is not a theorem, and the record says so twice, in `MODEL_CARD.md:664` and in
`model_v4.md:784-789`.

The sign carries no magnitude the empirics can target. The five products for the (5,10)
pair are 0.1818, 0.1818, 0.2055, 0.4299, 0.7724, and the SPEC quotes them as directional
support only (`SPEC.md §0.1`). There is no registered mapping from those ratios to any
coefficient scale, and building one now would be inventing an estimand after the estimates
were seen.

There is a split worth stating plainly, because it constrains prose rather than numbers.
The SPEC's Branch A mechanism row attributes attenuation to the weight effect. The shorter
window moves mass from the pooled cell to the flagged cell, and the flagged cell is
liquidity-invariant, so the composite slope flattens (`SPEC.md §3.5.2`, Branch A mechanism
cell). That sentence is built on the weight ratio and on L2, both PROVED, and it is
A(tau)-free. It is writable. But the numbers do not sit where that sentence puts them. The
weight leg runs 0.8559 to 0.9730, a shave of 3 to 14 percent, while the products run 0.1818
to 0.7724, so composition carries the great bulk of the numerical effect
(`HANDOFF_sign.md` §8.1, magnitude row). The magnitude attribution is exactly the sentence
the A(tau) failure forbids. The paper may write the registered mechanism sentence. It may
not write where the magnitude came from.

---

## 2. What the empirics actually have, leg by leg

Every figure below is read from the committed artifacts. Only §8 is not ESTIMATED.

### H1, the partition test (SPEC §3.4). Label ESTIMATED

`h1_estimate.json` key `h1_main`, n 979 filings and 1,958 stacked rows, 891 firm clusters,
47 month clusters. Partition coefficient 0.58 pp, two-way clustered standard error 1.56 pp,
quoted conservative p 0.741, realised MDE on disk 4.38 pp (`mde_beta2_pp`). Pooled slope
0.67 pp with standard error 2.84 pp. Flagged slope 1.24 pp with standard error 1.93 pp.

Two derived numbers, my arithmetic from the on-disk standard errors, flagged as such. The
flagged slope's 95 percent interval is minus 2.5 pp to plus 5.0 pp. At the SPEC's own
registered MDE convention of 2.802 times the standard error (`SPEC.md §5`), the flagged
slope's MDE is 5.40 pp and the pooled slope's is 7.96 pp.

The registered verdict under `SPEC.md §10` row 1 is uninformative. Supportive needs the partition
coefficient significant and the pooled slope significantly non-zero while the flagged slope
sits inside the MDE. The second condition fails.

One more fact belongs beside it. `SPEC.md:420-424` registers a pre-period prediction both
branches agree on, a negative liquidity slope on the run-up. The realised pooled slope is
positive and insignificant here, and the realised pre-period slope on the five-day run-up
is plus 4.14 pp with standard error 3.95 pp (`h2_estimate.json h2_runup5.beta_liq_pre`).
The shared prediction did not come through point-wise, and it is not distinguishable from
zero either.

### H2, the reform slope change (SPEC §3.5). Label ESTIMATED

`h2_estimate.json`. On the five-day run-up the interaction is 0.0175 pp with standard error
4.42 pp, quoted p 0.997, realised MDE 12.39 pp (`h2_runup5.mde_realised_se_pp`). On the
filing-day jump it is 0.54 pp with standard error 4.15 pp, quoted p 0.928, realised MDE
11.62 pp. The contamination check that runs first records `partition_refuted: false`.

The verdict under `SPEC.md §10` row 2 is uninformative, reported as a bounded null with the
MDE quoted. The point estimate is roughly one seven-hundredth of its own MDE. Reading its
nominal sign as directional support would be indefensible.

The contamination check deserves an honest caption. It would fire only if the jump
interaction were significant, same-signed and comparable in size. With an MDE of 11.62 pp
on a coefficient of 0.54 pp, the test had no power to fire. It is an untaken test, not a
passed one.

### Bindingness dose (SPEC §4). Label ESTIMATED

`dose_estimate.json`. Directly measured dose covers 127 filers, 249 filings, against 1,380
pre-window filings and 1,103 filers with any pre-period filing. The SPEC requires that
coverage be printed next to every dose estimate (`SPEC.md §4`, realised-counts corrigendum
item 5). Every dose estimate is a null. Run-up 3.83 pp against MDE 17.01 pp; jump 3.14 pp
against 8.62 pp; stake 0.14 pp against 7.51 pp; the imputed robustness row 14.74 pp against
62.36 pp. All three within-liquidity-tercile rows run n 83 with MDEs 14.3 to 41.7 pp.

The first stage is sharp and is not a finding. Filers whose pre-period delay ran past five
business days cut their delay by 7.25 business days more than fast filers, standard error
1.44, t minus 5.03, n 249. The artifact carries its own label, "mechanical validity check,
not a finding", and `SPEC.md:672` says the same.

Row 3's discriminating cells cannot fire. Supportive needs the dose coefficient to carry
the same sign as the H2 interaction, and that interaction is 0.0175 pp. Against needs the
dose coefficient near zero while the H2 interaction is large, and it is not large. The row
lands in uninformative by default.

### Stake at filing (SPEC §5). Label ESTIMATED

`stake_estimate.json`, `primary_trend_qoy`, n 962. Level shift minus 0.98 pp, standard
error 2.34, wild p 0.714, realised MDE 6.55 pp (`gamma_mde_pp_stake`). Interaction minus
2.16 pp, standard error 1.27, wild p 0.120, realised MDE 3.57 pp. Liquidity main effect
minus 6.65 pp per standard deviation, standard error 1.37, t minus 4.85, p 1.3e-06, and
minus 6.89 with standard error 1.38 in the year-quarter variant.

The level shift is dead by a wide margin, and the SPEC predicted it in writing. The
historical days-to-stake gradient implies a mechanical change of about 0.12 pp for a
two-business-day cut in the median delay (`stake_estimate.json
bbjj_days_stake_gradient_warning`; `SPEC.md §5`). The realised MDE is 6.55 pp, about 55
times that. The SPEC's own line, written before the estimate, is that if the reform works
only through mechanical accumulation time then we cannot see it. Confirmed.

The liquidity main effect is the strongest outcome coefficient in the package and the model
signs nothing about it. There is no liquidity comparative static anywhere in the record for
the stake at filing, the run-up, the run-up path or the jump, and invariance of the jump is
explicitly disclaimed (`model_v4.md:784-789`).

### Bounded null (SPEC §6). Arithmetic, not an estimate

The ladder is 20 pp at any accumulation cut, 3 pp at a cut of a tenth of the stake, 1 pp at
a quarter (`SPEC.md:846` and the two rows under it). Three restrictions travel with it. It
covers the accumulation channel only, it is not the aggregate footprint of the disclosure
rule, and the reduced-form matched design may legitimately exceed it. `SPEC.md §10` row 5
(`SPEC.md:1339`) says the bound is arithmetic and cannot fail, only be mis-stated. The
figure that is not in the SEC release must never appear.

### Run-up path (SPEC §7). Descriptive by registration, no artifact on disk

No run-up-path artifact exists in `empirics/output`. The leg is registered and unrun. It
carries no MDE and no inference, and `SPEC.md §10` row 6 registers an against condition as
well as a supportive one. No separation by liquidity in either period would say that
liquidity is not the operative cut. On the realised pooled slope of 0.67 pp with standard
error 2.84 pp, that against branch is live. This is not a free illustration.

### Matched DiD on the control outcome (SPEC §8). Label NOT ESTIMATED

`did_estimate.json` carries label NOT ESTIMATED, status `design_failure`,
`quote_as_result: false`, blocked by two independent registered bars. The §8.2 balance gate
fails on past return minus 0.131 and idiosyncratic volatility 0.122 after the predeclared
tighter caliper rerun, and the §8.8 pre-trend joint F is 3.249 with p 0.0214, which blocks
causal language on its own terms (`did_diagnostics.json pretrend`). The §8.7 placebo is
BLOCKED with zero estimable dates of 568 candidates and four recorded blockers.

There is no realised MDE for this leg, because no regression was fitted. What exists is
design arithmetic on the realised matched counts of 325 pre and 140 post, giving standard
error 4.17 pp, MDE 11.70 pp, 15.32 pp clustered, and the artifact labels it not a realised
MDE (`did_estimate.json mde_pp_design_arithmetic`;
`research/empirics_v4/did_matching_2026-08-31.md` §1). The 9.09 pp figure printed in
`SPEC.md §8.6` is computed on the §2.3 estimation sample of 569 and 543, one funnel stage
above the §8 design.

One registered bar is cleared. The blind hand audit passed 0 disagreements of 30.

### Bidder entry by liquidity (SPEC §9). Label ESTIMATED, and the triple inherits a failed gate

`bidder_entry_estimate.json`. Within 13D targets, n 465, interaction minus 0.65 pp with
standard error 3.93, quoted p 0.878, realised MDE 11.01 pp; liquidity main effect minus
1.63 pp with standard error 2.65. The triple difference is minus 5.94 pp with standard
error 6.59, quoted p 0.398, realised MDE 18.45 pp, and its own record carries
`design_status: failed_balance` with the instruction that it is reported as an interval and
a sign, never as a test. S2 and the 2025 extension are NOT ESTIMATED. `SPEC.md §9`
registered uninformative as the expected outcome, so landing there is not a failure.

### A gate that travels with every bid-outcome number

`bid12_gates.json` records the treated base-rate gate as a fail, 0.1261 on 3,418 coded rows
against the 18.1 percent Greenwood-Schor anchor, and `all_passed: false`. Every MDE in
§8.6 and §9 is built on the borrowed 18.1 percent treated rate. Our coder counts failed and
withdrawn bids, so our rate was expected to run higher, and it runs lower. No recompute on
the measured rate exists on disk. The caveat must travel with every bid-outcome MDE the
package prints. `decisions_2026-08-31.md` Decision 2 already has it in front of Austin.

### Fact 1, and why its committed numbers cannot be quoted as they stand

`fact1_summary.csv` is the only executed descriptive on the disclosure rule, showing mean
delay 9.63 to 6.40 business days and the share inside five business days 0.357 to 0.756. It
was written 2026-08-19, before the mandatory re-parse. `SPEC.md §2.2` lists the parser
defects and three of them land on this exact measure. Federal holidays in the business-day
arithmetic, event-date labels split across HTML tags, and the form rename, where an
explicit caller tuple in `facts.py` bypassed the alias map and 2024Q3 and 2024Q4 lost 18 and
114 filings silently. The re-parse ran 2026-08-30 and those two quarters moved from 57 to
76 percent parsed (`empirics/output/reparse_quarterly_parse_rates.csv`, 2024Q3 0.710 and
2024Q4 0.800). Fact 1's post window is 2024Q3 to Q4 and its module is `facts.py`. The
committed numbers are old-parser numbers on the repaired quarters.

The recompute is cheap and local. `empirics/data/fact2_parsed.jsonl` was rewritten
2026-08-30 and no SEC network call is involved. It is a run for a later ticket, not for this
note.

---

## 3. The join

Read the table with one rule in mind. A null corroborates only where the theory's
prediction is itself a zero. Everywhere else a null is a bounded null and nothing more.

| Theory claim | Label | Live leg on disk | Realised resolution | Can it speak to the claim |
|---|---|---|---|---|
| L2, flagged cell invariant in liquidity (`MODEL_CARD.md:656`) | PROVED, general | H1 partition, `h1_estimate.json` | flagged slope 1.24 pp, se 1.93, MDE 5.40 pp (my arithmetic at 2.802 x se) | Partly. The zero is not refuted. It cannot corroborate against the rival reading that nothing moves with liquidity anywhere, because the pooled slope is 0.67 pp with se 2.84 |
| L2's other half, the pooled cell carries the whole liquidity derivative (`draft_v3.tex:759-774`) | PROVED, general | same regression, pooled slope | pooled slope MDE 7.96 pp (my arithmetic) | No. Not established. `SPEC.md §10` row 1 needs it significant and it is not |
| T1 Part C, window margin is an iff with the composition ratio unsigned (`MODEL_CARD.md:664`) | PROVED at fixed policies | none, and none is possible | n/a | No. An iff with an unsigned factor has no estimand. It is the reason the December text can say the acceleration lands where the theory signs nothing |
| HANDOFF §8 window-margin sign, Branch A (`HANDOFF_sign.md` §8.1) | NUMERICAL at one calibration, four conditions | H2 interaction on the five-day run-up | 0.0175 pp against MDE 12.39 pp | No. Sign-only against a design 700 times too coarse. Report as a bounded null with the MDE |
| The same sign, as a mechanism dose (`SPEC.md §4`) | NUMERICAL | dose interaction | 3.83 pp against MDE 17.01 pp, 27.5 percent direct coverage (`SPEC.md:638`) | No. Row 3's discriminating cells cannot fire when the H2 interaction is a zero |
| The same sign, oriented on the stake at filing (`SPEC.md §5`) | NUMERICAL | stake interaction | minus 2.16 pp against MDE 3.57 pp | No. Inside its MDE, and the orientation is itself contested. See §4b item 3 |
| D1, the partition and the run-up plus jump identity (`draft_v3.tex:728-743`) | PROVED | the timing split's construction | n/a | It is used, not tested. The design measures the two halves the identity names |
| Weight ratio at most one, the reclassification direction (`model_v4.md:702`) | PROVED | none | n/a | No. The pooled cell is unobservable by construction, so no 13D sample shows histories moving into the flag. Fact 1 and the dose first stage show the legal clock bound, which is the premise, not the prediction |
| L3, L4 leg 3, T1 Part B, the chord mechanism | PROVED as conditionals, antecedent measured false here | none | n/a | No, and the SPEC forbids mechanism prose that leans on them |
| L4 legs 1 and 2, threshold margin (`model_v4.md:700`) | PROVED | none | n/a | No registered test. The 5 percent trigger is fixed by law and the 2024 change moved the window margin |
| C1, general-equilibrium survival (`MODEL_CARD.md:665`) | PROVED as an implication, region carried as a hypothesis, restricted to the threshold margin | none | n/a | No. It names the term the fixed-policies condition brackets out. It cannot be mapped onto a window change |
| P1, existence | PROVED, two hypotheses measured to fail at the implemented calibration | none | n/a | No empirical counterpart exists or could |
| Bidder entry, flagged leg invariant (L2) | PROVED | §9 within 13D targets, `bidder_entry_estimate.json` | interaction minus 0.65 pp against MDE 11.01 pp; base-rate gate failed | Weakly at best. It is a zero against a zero prediction, but on an outcome whose coder failed the base-rate gate |
| Control outcome, aggregate | no theory claim, there is no bid hazard in the model | §6 ladder plus §8 design arithmetic | 3 pp rung against 15.32 pp clustered | The arithmetic is sound and corroborates no theory claim. Say so in the text |

Three joins are worth naming as false leads before anyone reaches for them, and §5 does
that.

---

## 4. The recommended route

### 4a. What can be done now, ranked, with costs

**1. Report H1 at its registered verdict, framed as a one-sided non-refutation of L2.**
Cost is zero compute. Every number is committed. This is the only place in the package
where a theory prediction is a point at zero, so it is the only place a null does any
corroborative work at all. Print the flagged slope with its interval and its MDE, print the
pooled slope beside it, print the word uninformative, and say in one sentence that the test
was one-sided because the discriminating half also came back a zero. A referee told the
jump is flat in liquidity as the theorem says, and not told the run-up is equally flat, has
been misled. This is the strongest honest claim the package has and it is a modest one.

**2. Print the bounded null in the form the author has already filed.**
`decisions_2026-08-31.md` Decision 1 Option A is the stand-pat sentence, the bounded null
quoted against the design arithmetic of 15.32 pp clustered against the 3 pp headline rung.
Cost is zero. It is arithmetic on a public SEC table. Two repairs are needed against how
the plans wanted to write it. There is no realised DiD MDE, so no coefficient and no
confidence interval can be printed, which means the §8.9 reporting template cannot be
filled and the §6 interpretive rule has no antecedent to fire on. And the base-rate gate
fail travels with the number. On S1 the design is powered only against the loose 20 pp
rung. Say that plainly.

**3. Report H2 as the registered bounded null, both branches live.** Cost is zero compute.
The value is that it is exactly what §0 rule 2 asks for, and it forecloses the temptation
to read a sign off a coefficient 700 times inside its MDE. Report the jump contamination
check as untaken rather than passed.

**4. Report the stake leg in two clearly separated halves.** The reform coefficients are
bounded nulls and the level shift is dead by a factor of about 55 against the mechanical
prediction. The liquidity main effect is the strongest outcome coefficient in the package
and it is a cross-sectional regularity the model does not sign. Print it as descriptive,
with the SPEC's own selection warning attached, and never let its significance carry across
to the reform nulls sitting beside it.

**5. Report the dose with its coverage and with the first stage in its registered role.**
The first stage is the sharpest institutional number in the package and the SPEC and the
artifact both label it a validity check. Keep that label on it.

That is the December empirical package I would write. It contains one clean result in the
CONTEXT.md sense, H1, and its content is that the two halves of the timing split cannot be
told apart at 4.38 pp. It contains three bounded nulls, an arithmetic ceiling on the
control outcome, and one descriptive regularity. It corroborates one PROVED lemma weakly
and no NUMERICAL sign at all. I think that package survives the referee checklist and I do
not think anything more ambitious does.

### 4b. What needs Austin's ruling on a registered rule

None of these is work to do. Each is a decision.

1. **The §3.7 quarterly pre-trend for the timing split.** No artifact exists in
   `empirics/output`, and the only pre-trend on disk is §8.8's on the control outcome. The
   registered text fixes the window and the joint F and says p below 0.10 blocks causal
   language, but it names no dependent variable and no handling of the quarter effects.
   Whoever runs it completes a specification after every estimate is on disk. That is a
   post-registration decision under §0 rule 1, not an estimation ticket.
2. **The pseudo-trigger placebo threshold.** `SPEC.md §3.7` says the pseudo slope must be
   statistically indistinguishable from zero and registers no numeric level. The realised
   pseudo slope on the five-day run-up is minus 2.01 pp with quoted p 0.0811
   (`placebo_h1h2_estimate.json`), which passes at 5 percent and fails at 10. The
   mitigation belongs in the same sentence. That coefficient sits inside its own MDE of
   3.22 pp. The partition placebo is clean at minus 0.19 pp with p 0.754. Which convention
   applies is Austin's call, and a failure demotes the headline to descriptive.
3. **The stake interaction's branch orientation.** Two readings are on disk and I print
   both rather than picking. Reading one holds that §5 contradicts itself. Its opening
   paragraph adopts the positive-interaction orientation of §3.5.2 given a negative
   pre-period run-up slope, while `SPEC.md:731` and the supportive row say the fall is
   larger in liquid names, which given the SPEC's construction of the liquidity variable
   implies a negative interaction. Reading two holds that the §5 supportive row governs
   its own leg, in which case the realised minus 2.16 pp is Branch-A-oriented rather than
   Branch-B-oriented. The verdict is uninformative either way, because the coefficient
   sits inside its 3.57 pp MDE, so nothing about the reported result turns on it. The
   prose does.
4. **Any relabel of Fact 1 or the dose first stage.** Both are registered as validation
   rather than findings (`SPEC.md:672`, `SPEC.md:877`). Calling either one corroboration of
   the theory's premise is a post-registration relabel. Separately, Fact 1's committed
   numbers should not be quoted until they are recomputed on the re-parsed corpus, for the
   reasons in §2 above.
5. **The headline choice.** `draft_v3.tex:1025-1027` names the timing split as the default
   and `draft_v3.tex:1264-1265` reserves the selection among the three candidates to
   Austin. This note recommends the reporting package and does not select the headline. For
   the record, the draft's own Candidate C text says the bounded null can sit alongside
   another candidate rather than standing alone.
6. **The three questions already filed.** `decisions_2026-08-31.md` items 1 to 3 stand as
   written and this note does not re-adjudicate them.

---

## 5. What would be false corroboration

Each of these was proposed and killed, and it stays dead for the reason given.

**Any mechanism sentence built on the chord formula.** A(tau) fails at all 180
non-degenerate nodes at the implemented calibration. The conditionals keep their proofs and
say nothing about the implemented pooled cell there, and the SPEC already bars the prose
(`SPEC.md §0.1`). This includes the true-sounding line that the composition leg carries the
effect while the weight leg is a small shave. That line is the magnitude attribution the
failure forbids.

**Treating the products 0.1818 to 0.7724 as a coefficient target.** Only the sign travels.
There is no registered mapping to a coefficient scale, and no proportional prediction is
available in any case, because the realised pre-period slope on the five-day run-up is
itself a statistical zero at plus 4.14 pp with standard error 3.95 pp.

**Quoting the horizon-12 column as a second independent magnitude.** Its composition ratio
travels the chord route. It is directional corroboration of the corner audit.

**Quoting the disclosure-regime margin ratios as a window result.** They are a regime
comparison at a fixed window and measure no window pair, and the SPEC's 2026-08-23
corrigendum withdraws the earlier mislabel that treated them as a window result
(`SPEC.md §3.5.2`, note on the O-1 history, and the corrigendum at the foot of the
document). The same applies to the regime-margin boundary near 0.343.
It is a disclosure-regime boundary, so anchoring the disclosed share of engagements to one
side of it would decide the §1 entry's sign and would not touch the §8 sign the SPEC
consumes.

**Quoting §8 as evidence of anything about the control outcome.** Two independent
registered bars block it and the placebo is blocked on four grounds. Repairing the balance
gate would buy a design whose own arithmetic is still five times too coarse to see the 3 pp
rung (`research/empirics_v4/did_matching_2026-08-31.md` §1).

**Reading the §9 triple difference as a test.** It is estimated on the failed-balance draw
and its own record says it is reported as an interval and a sign, never as a test
(`bidder_entry_estimate.json triple.match_design_status`).

**Any bid-hazard, duration or bid-timing estimand as a theory counterpart.** There is no
such object in the model. The strings hazard, duration, arrival and Poisson return zero
matches in both `model_v4.md` and `model_v4.tex` (grep run this pass), the blockholder's
engagement moves a single static entry probability evaluated once at the horizon
(`model_v4.md:132`), and the not-claimed list confirms nothing further
(`model_v4.md:784-789`). A hazard-shaped claim would need new theory after the freeze at
`65b8db3`.

**Saying the data show histories being reclassified from the pooled cell into the flagged
cell.** The pooled cell is unobservable by construction, and the model fixes filing at the
deadline and puts endogenous filing before the deadline on its not-claimed list
(`model_v4.md:784-789`), so observed delay dispersion is off-model.
The delay compression and the dose first stage show that the legal clock bound. That is the
premise of the window-margin discussion, not a prediction of it.

**Quoting Fact 1's committed numbers.** Old parser, on the two quarters the re-parse
repaired, from the module the form-rename defect named.

**Reading H1 as support for the partition.** The registered supportive branch cannot be
met. Uninformative is the registered word and it is the honest one.

**Letting the stake liquidity main effect stand next to the reform nulls without a label.**
It is significant, it is cross-sectional, and the model signs nothing about it.

---

## 6. Open questions and what is not on disk

**Not on disk, and decisive for the theory record's internal reconciliation.** The
disclosed share of engagements has no empirical estimate anywhere. The implemented 61.1473
percent is a calibration output. The three available proxies are each disqualified in the
handoff and straddle the regime-margin boundary. The handoff calls this the highest-value
calibration input the project could acquire, and the denominator is the object the
disclosure rule makes unobservable. There is no December path to it, and standing up a leg
for it would be a post-registration addition made after the estimates were seen.

**Not on disk.** No general-equilibrium cutoff-shift term is bounded on either entry, so
nothing constrains the term the fixed-policies condition brackets out. No second
independent magnitude for the window effect exists. No §7 run-up-path artifact exists. No
§3.7 quarterly pre-trend artifact for the timing split exists. The 13G descriptive placebo
is recorded not run. No recompute of the bid-outcome MDEs on the measured base rate exists.
No control-side liquidity variable is committed, so the exact triple-difference MDE is not
computable from anything on disk.

**Open, and I would not try to close them for December.** Whether the two-round pooled cell
satisfies A(tau) on some other menu, horizon or calibration. Whether any parameter vector
satisfies the full C1 antecedent. Whether the amendment-orphan residual in the control pool
is material. Which rung of the ladder is the bound, which is a judgement and is why all
three stay printed.

**The honest summary.** The theory's window-margin claim about the February 2024
acceleration cannot be corroborated with the data in hand, and it is the theory itself,
not the data, that says the strongest version of that claim was never available. What the
empirics can do is report one PROVED zero that survived a test with a stated MDE, three
bounded nulls at their registered MDEs, and an arithmetic ceiling on the control outcome
that no design in the package can see under.
