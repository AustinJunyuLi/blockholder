# Integration-angle review: the strongest December 2026 paper

**Decision date:** 31 August 2026  
**Departmental-review deadline:** 18 December 2026  
**Literature search date:** 31 August 2026  
**Review boundary:** the live working trees of `/Users/austinli/Projects/blockholder_v4` and `/Users/austinli/Projects/blockholder_v4_theory`. No estimation pipeline was run. No repository object was changed except this report.

This report uses three evidentiary labels. **Verified fact** means a statement is directly supported by a live repository artifact, an independent reproduction record, or a primary online source. **Inference** means the conclusion follows from those facts but is not itself an estimated or proved result. **Recommendation** is the research or editorial decision proposed here.

## 1. Executive verdict

### 1.1 Decision

**Recommendation — winner:** make the December paper a theory-led paper about **the legal disclosure clock as an information partition**, supported by one corrected and independently reproduced empirical result showing that the February 2024 rule changed realised Schedule 13D filing timing. The working title should be:

> **The Disclosure Clock: Market Inference and Corporate Control**

The current integration memo is directionally right when it recommends “a theory paper with one empirical fact” rather than a causal empirical paper (`/Users/austinli/Projects/blockholder_v4/research/empirics_v4/2026-08-31_theory_empirics_december_integration.md:5-7`). That hypothesis survives this review, but only after three material corrections.

1. The filing-delay result must be presented as an **implementation fact**: it establishes that the legal clock moved realised disclosure timing. It does not corroborate the model's liquidity or takeover mechanism.
2. The public-facing theory must be narrowed to the clock, the flagged-versus-pooled information partition, the premium decomposition, and the exact limits of the threshold and window comparative statics. The current proof architecture is too large to be the paper's public face.
3. The current H1/H2 timing split cannot be presented as a test of the model's flagged and pooled states. The frozen authority explicitly says that the filing jump `J` is not claimed to be liquidity-invariant (`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/MODEL_CARD.md:141-144`), while the live draft still says the empirical “flagged half” should not move with liquidity (`/Users/austinli/Projects/blockholder_v4_theory/draft_v3.tex:759-774`). That bridge is false as written.

**Verified fact:** the core theory contains a real contribution. D1, L1, and L2 are labelled `PROVED`. T1 signs the threshold margin under its stated fixed-policy conditions but gives only an if-and-only-if condition for the window margin; it does not provide an unconditional sign for the February 2024 reform (`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/MODEL_CARD.md:654-665`).

**Verified fact:** the existing return and corporate-control evidence cannot carry the paper. H1 and H2 reproduce, but their intervals are too wide and their observables do not recover the corresponding theoretical information states. The matched control-outcome design is labelled `NOT ESTIMATED`; its balance gate fails, and its pre-trend test independently blocks causal language (`/Users/austinli/Projects/blockholder_v4/quality_reports/verification/2026-08-30_estimates_verify.md:44-75`; `/Users/austinli/Projects/blockholder_v4/research/empirics_v4/did_matching_2026-08-31.md:67-84`; `/Users/austinli/Projects/blockholder_v4/research/empirics_v4/did_matching_2026-08-31.md:118-145`).

**Inference:** the strongest coherent December contribution is therefore not “the 2024 rule reduced the liquidity sensitivity of takeover premia.” It is: **a statutory threshold and deadline create economically distinct public-information states; the model identifies what can and cannot be signed across those states; and the data show that the relevant legal clock moved sharply in practice.**

### 1.2 Runner-up and rejected position

**Runner-up:** a timestamp-aware paper on the **reallocation of price discovery around the public filing**. It would replace the current overlapping daily windows with non-overlapping pre-publication and post-publication measures, use exact EDGAR acceptance times, and seek confirmation on untouched 2026 data. It has a higher eventual journal ceiling than the winner because it could align an observable market-learning object with the legal clock. It is not the December winner because it requires new data engineering, verified TAQ access, a prospective holdout, and power that has not yet been demonstrated.

**Rejected:** the strongest honest version of the registered H1/H2 and control-outcome programme. It is rejected, not merely ranked third, because it has two fatal defects: the return variables do not identify the model's pooled and flagged states, and the causal control-outcome leg was never estimated under its registered rules. More controls or more observations cannot repair a wrong model-to-measure mapping.

### 1.3 December go/no-go

| Empirical standard | Verdict | Strongest December headline | Binding condition |
|---|---:|---|---|
| A corrected, independently reproduced descriptive filing-timing result is admissible | **GO, conditional** | The February 2024 Schedule 13D regime compressed realised filing delays in pre-fixed windows | A near-census denominator audit, manual validation, immutable result artifact, and independent reproduction must clear by **25 September 2026** |
| A credible causal estimate is required | **NO-GO** | None | No current causal design survives its registered gates; a new same-sample specification would be post-view, and an independent causal design is not December-feasible |

### 1.4 Live-worktree provenance and caveats

The repositories were opened once as separate DevSpace workspaces, their instructions and `CONTEXT.md` files were read, and their live states were recorded before substantive review.

| Repository | Branch | HEAD | Live working-tree caveat |
|---|---|---|---|
| `/Users/austinli/Projects/blockholder_v4` | `v4` | `8e200ec92b11ba40d45cdc9a7e92307846a945fb` | Ahead of `origin/v4` by 37 commits. Untracked `.grok/` and untracked `research/empirics_v4/2026-08-31_theory_empirics_december_integration.md`. This review therefore uses the live untracked integration memo where cited, not merely HEAD. |
| `/Users/austinli/Projects/blockholder_v4_theory` | `v4-theory` | `adf97c6130c83bcf72b16694f18fd8f9878a776d` | Dirty live manuscript tree: modified `deliverable/draft_v3.pdf`, `deliverable/draft_v3_onlineappendix.pdf`, `draft_v3.tex`, `draft_v3_trace.md`, and a session brief; deleted four older deliverables; untracked browser, legal-portability, extract, PDF, teaching, and archive material. The frozen theory authority remains `MODEL_CARD.md`; the live manuscript is an editable presentation layer. |

The theory repository's own root instructions state that the theory record is frozen and that live work is confined to `draft_v3` and code. This review has not reopened or modified the frozen record.

## 2. End-to-end explanation from zero

### 2.1 Institutional sequence

A Schedule 13D is the public filing normally used when a person crosses five percent beneficial ownership of a covered voting class and holds with an intent or effect related to control. The SEC's 2023 amendments shortened the initial Schedule 13D deadline from ten days to five business days, effective 5 February 2024. The official sources are the [SEC final-rule page](https://www.sec.gov/rules-regulations/2023/10/33-11180) and [SEC press release 2023-219](https://www.sec.gov/newsroom/press-releases/2023-219), searched 31 August 2026.

The economically relevant sequence is:

1. A blockholder acquires shares without a public Schedule 13D flag.
2. Beneficial ownership crosses five percent on a trigger date.
3. A legal filing interval remains. The blockholder may continue trading and may communicate or engage during this interval.
4. The Schedule 13D becomes public when accepted and disseminated by EDGAR.
5. A bidder, target board, management, other investors, and the market may act on the resulting information.

The legal deadline is not necessarily the filing date chosen by every filer. It is the latest permitted disclosure time. Realised delay is therefore a compliance or equilibrium outcome bounded by law, not the law itself. The model simplifies this distinction by setting filing at crossing plus the legal window and by excluding endogenous early filing. The model note defines crossing date `c`, legal filing date `f=c+T`, and flag condition `f<=H` at `/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/model_v4.md:95-118`.

Two institutional details matter for measurement. First, on the same date that the new deadline became effective, EDGAR extended the daily filing cut-off for these forms from 5:30 p.m. to 10:00 p.m. Eastern Time; the [SEC EDGAR 24.0.2 announcement](https://www.sec.gov/filergroup/announcements-old/edgar-release-24-0-2) records that simultaneous change. Second, the [SEC's current 13D/13G interpretations](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/exchange-act-sections-13d-13g-regulation-13d-g-beneficial-ownership-reporting), last updated 9 July 2026, state that the five-business-day clock runs from trade date and clarify how control intent affects 13G eligibility. A historical parser must apply a time-consistent rulebook rather than silently back-casting later guidance.

### 2.2 Actors, information, choices, and payoffs

**The blockholder** observes a private signal `s` about standalone value `v`. At the start she chooses a complete contingent plan from an ordered menu. The plan determines exit, hold, or voice; the stake path; threshold crossing; engagement; filing; and any residual order after the flag. There is no within-window re-optimisation in the core model (`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/model_v4.md:199-220`).

**Noise traders and the competitive market maker** generate and interpret order flow. Noise obscures the blockholder's trades. The parameter `kappa` is noise-trading intensity, not literal Amihud illiquidity, quoted depth, turnover, or volume. Competitive prices equal expected terminal shareholder value conditional on public information.

**The bidder** draws a private synergy shock and pays an entry cost. Entry depends on the bidder's posterior about target value and engagement. A successful control transaction creates a shareholder premium. The model therefore links information in prices and filings to bidder entry instead of treating a takeover premium as a reduced-form announcement return (`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/model_v4.md:81-91`; `/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/model_v4.md:122-149`).

**Dispersed shareholders** receive standalone value plus any control premium. The paper's principal value object is the expected engagement-related component of that premium, not total social welfare.

### 2.3 Why liquidity affects inference

When informed buying is mixed with little unrelated noise, a given order-flow history is more revealing. When more unrelated noise can generate the same history, the market maker's posterior reacts less sharply. In the model, `kappa` changes the signal-to-noise ratio in the pooled state.

The empirical variable is different. `LIQ` is negative standardised log Amihud, calculated within calendar quarter (`/Users/austinli/Projects/blockholder_v4/research/empirics_v4/SPEC.md:364-369`). It is a defensible proxy for the trading environment, but the theory does not establish a one-to-one or monotone mapping from that proxy to `kappa`. Empirical prose may say “liquidity proxy”; it may not say that the regression literally estimates a derivative with respect to the structural noise parameter.

### 2.4 Pooled and flagged are information states, not return windows

The model defines a flagged cell when a Voice history crosses the threshold and the filing arrives before the control decision. Otherwise the control node is pooled. The indicator is `D=1{a=1, c(tau)+T<=H}`. A tighter threshold or shorter window can move histories from the pooled cell to the flagged cell (`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/model_v4.md:224-238`).

The distinction is latent and informational.

* **Pooled state:** no public filing has arrived by the control node. The public market infers from the order-flow history and the absence of a filing.
* **Flagged state:** the filing and flagged-round tuple have arrived. Under L2's identification conditions, that tuple absorbs the value-relevant information carried by the pre-filing path.

A return from the trigger date to the day before filing is not automatically “the pooled cell.” It is a price path eventually observed on a flagged history. A filing-day return is not automatically “the flagged cell.” It is a difference between a post-filing endpoint and a pre-filing price, and the pre-filing price can vary with liquidity. The current integration memo correctly warns that D1 does not label the empirical `RUNUP` and `JUMP` windows as the two cells (`/Users/austinli/Projects/blockholder_v4/research/empirics_v4/2026-08-31_theory_empirics_december_integration.md:29-41`).

### 2.5 Threshold and window are distinct policy margins

A lower disclosure threshold changes **which stake paths cross**. It alters the cross-sectional set of positions that can become publicly flagged.

A shorter filing window changes **whether a crossing becomes public before the control decision**. It alters timing conditional on crossing. The clock equivalence converts `f<=H` into a stake-path condition at `H-T`, which makes the distinction formal.

This is the paper's clearest economic contribution. It also explains why the February 2024 reform does not automatically test the theory's strongest comparative static. The US reform changed the window, while the cleaner signed result concerns the threshold margin. The live draft itself concedes that the reform lands on the margin for which the theory has no unconditional sign (`/Users/austinli/Projects/blockholder_v4_theory/draft_v3.tex:860-869`).

### 2.6 Bidder entry and takeover premia

At the control node, the bidder combines private synergy with the public information set. That public state affects the posterior about target value and the probability that the blockholder is engaged, which changes the entry decision. Conditional on control, engaged and unengaged states carry different premium components, denoted by `m1` and `m0`, with `m1>m0` maintained.

L1 decomposes the expected engagement-related premium into flagged and pooled conditional components weighted by the probability of reaching each cell. The decomposition is exact under its stated conditions. It does not imply that a twelve-month acquisition indicator equals the model bidder's entry decision or that an observed offer premium equals the model's engagement-premium component.

### 2.7 What the theory establishes

The frozen authority gives the following hierarchy.

**D1 — `PROVED`.** The legal clock creates an exhaustive partition. For Voice plans, filing before the control horizon is equivalent to reaching the threshold by `H-T`. On flagged histories, the movement from just before crossing to the flagged price decomposes into cumulative run-up plus filing jump. This is a clock and accounting result, not a causal result about returns (`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/MODEL_CARD.md:654`).

**L1 — `PROVED`.** The expected engagement premium is the probability-weighted sum of flagged and pooled conditional premia, with null-cell averages left undefined at degenerate endpoints rather than imputed (`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/MODEL_CARD.md:655`).

**L2 — `PROVED` under explicit fixed-policy and identification conditions.** Conditional on a sufficiently informative flagged tuple, the pre-filing pooled history is independent of value, signal, and bidder shock on the flagged set. The flagged posterior, flagged price, bidder-entry probability, and flagged premium component are invariant to `kappa` (`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/MODEL_CARD.md:656`). The conclusion concerns endpoint and control-node objects. It does not make the filing return invariant.

**L3 and L4 — conditional.** L3 is proved under support representation `A(tau)`. L4's reclassification legs are proved outright, while its pooled-sensitivity leg requires bridge assumptions. At the implemented calibration, the key support representation fails broadly: the pooled posterior has 23 to 767 support values rather than the compressed representation. The statements remain valid conditionals, but their applicability to that calibration is not established.

**P1 — `PROVED` under a demanding antecedent.** An equilibrium exists within the strategy, regularity, pricing, and identification class stated in the model card. This is not a general existence theorem for every plausible menu or for every implemented numerical node. Four policy nodes remain unresolved numerically, and the implemented calibration does not establish all antecedents. The card separates the analytical label from numerical applicability (`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/MODEL_CARD.md:659-663`).

**T1 — `PROVED` at fixed policies.** The flagged-cell weight gives an exact attenuation factor. Threshold tightening attenuates under the theorem's conditions. Window tightening attenuates if and only if the weight effect dominates an unsigned pooled-composition effect. No unconditional window sign is claimed (`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/MODEL_CARD.md:664`).

**C1 — a conditional implication is `PROVED`, with separate `NUMERICAL` node evidence.** It identifies sufficient conditions under which a fixed-policy attenuation sign survives equilibrium feedback. A named nonempty region has not been verified; 18 of 80 grid nodes satisfy pointwise diagnostics (`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/MODEL_CARD.md:665-670`).

**Ten-to-five window calculation — `NUMERICAL`, not a theorem.** At one fixed-policy calibration, shortening the window from ten to five lowers computed sensitivity to 18.18–77.24 percent of its long-window value. Most movement comes from composition. The same handoff records that the filing jump moves by about 5,090 basis points across liquidity even though the flagged endpoint is invariant, and that the chord antecedent fails (`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/HANDOFF_sign.md:186-228`; `/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/HANDOFF_sign.md:251-263`).

The model card's labels are binding: `PROVED` means a completed proof, `NUMERICAL` means executed grid evidence, and unproved statements remain conditional or conjectural (`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/MODEL_CARD.md:675-682`).

### 2.8 Numerical example: invariant endpoint, non-invariant filing return

Suppose the public filing and flagged order imply a flagged price of 110 in both a high-noise and a low-noise market.

* In the high-noise market, the last pre-filing price is 100. The filing jump is `110-100=10`.
* In the low-noise market, order flow reveals more before filing, so the last pre-filing price is 107. The filing jump is `110-107=3`.

The flagged endpoint is invariant; the filing return is not. The entire difference comes from the liquidity-sensitive pre-filing price. This is why H1's filing-window slope is not a direct test of L2.

### 2.9 What the empirical programme measures

The empirical repository contains several different exercises. They cannot be merged into a generic statement that “the evidence is consistent with the model.”

**Filing-delay fact.** The old committed table used 300 rows but only 282 unique accessions and an older parser. It cannot be quoted as the corrected result. A read-only feasibility audit using the current parsed universe finds, in the pre-fixed 2023Q2–Q3 and 2024Q3–Q4 windows, 399 and 365 retained filings, provisional medians of seven and four business days, and provisional shares filed within five business days of 37.6 and 78.6 percent. These numbers are not yet saved as an adopted result artifact or independently reproduced (`/Users/austinli/Projects/blockholder_v4/research/empirics_v4/2026-08-31_theory_empirics_december_integration.md:154-231`).

**H1 timing split.** The unit is a filing-window row in a stacked regression, two rows per filing. `RUNUP` is `CAR[TD,FD*-1]`; `JUMP` is `CAR[FD*-1,FD*+1]`, so the windows overlap on `FD*-1`. The estimand is the difference between their liquidity slopes. The sample has 979 filings. This is a return-window contrast, not a comparison of latent pooled and flagged control-node states (`/Users/austinli/Projects/blockholder_v4/research/empirics_v4/SPEC.md:330-414`).

**H2 reform interaction.** The unit is an initial 13D filing. The estimand is the post-February-2024 change in the liquidity slope of `RUNUP5` or `JUMP`, with controls and fixed effects. `RUNUP5` is a fixed five-trading-day return from the trigger, but for early filers it can include the public filing. It is a before-after slope comparison, not a causal design with an unaffected control group.

**Bindingness dose.** The unit is a filing with a reconstructed treatment dose. The estimand interacts predicted deadline bite with liquidity and the post indicator. Only 127 filers have a direct dose; imputation and small cells dominate precision. The first stage is a mechanical validation that higher predicted bite is associated with shorter observed delay, not a causal instrument.

**Stake at filing.** The outcome is the percentage of the class reported at filing. The model object is filing stake or terminal target within a selected Voice plan. The empirical percentage is selected on filing, can use a stale denominator, and need not recover either theoretical object.

**Matched control-outcome design.** The intended unit is an activist target matched to never-13D controls. The intended outcome is a twelve-month bid indicator. The intended estimand is a post-reform difference-in-differences. Balance after matching and parallel trends are registered identifying conditions. Both gates fail, so no coefficient was fitted and the result is `NOT ESTIMATED`.

**Within-13D bidder-entry regressions.** The outcome is the same twelve-month bid code among 13D targets. An interaction is estimated, but the outcome base-rate gate fails and the triple difference inherits the failed matching draw. A bid observed within twelve months is not the model bidder's entry at a common control node.

## 3. Current theory and empirical truth ledger

### 3.1 Theory ledger

| Object | Authority label | What is established | What is not established | December use |
|---|---|---|---|---|
| D1 clock and partition | `PROVED` | Measurable flagged/pooled partition; clock equivalence; run-up-plus-jump identity | Observed return windows recover latent cells; causal effect of the law | Main text and opening figure |
| L1 premium mixture | `PROVED` | Exact probability-weighted decomposition of engagement premium | Cell weights and conditional premia are observed | Main text, short proposition |
| L2 flagged endpoint | `PROVED` under stated conditions | Flagged posterior, price, entry probability, and flagged premium component invariant to `kappa` at fixed policies | Filing return `J` invariant; assumptions hold in field data; endogenous-policy invariance | Main text with explicit assumptions and the 110/100/107 example |
| L3 pooled motion | `PROVED` under `A(tau)` | Exact representation conditional on support and regularity | `A(tau)` holds at the implemented calibration | Appendix; not an empirical mechanism sentence |
| L4 threshold reclassification | Legs 1–2 `PROVED`; leg 3 conditional | Lower threshold expands flagged set and lowers pooled engagement share; sensitivity result under bridges | Broad empirical threshold effect | Main-text intuition; details in appendix |
| P1 equilibrium existence | `PROVED` for restricted antecedent | Existence within the explicitly defined strategy and regularity class | General existence, uniqueness, or applicability at all numerical nodes | State once; proof and caveats in appendix |
| T1 attenuation | `PROVED` at fixed policies | Exact mixture attenuation; threshold result; window if-and-only-if condition | Unconditional window attenuation or global general-equilibrium sign | Main theorem in compressed form |
| C1 equilibrium feedback | Conditional implication `PROVED`; nodes `NUMERICAL` | Sufficient dominance/contraction condition and 18 diagnostic nodes | Verified nonempty region or global sign | Appendix only |
| Ten-to-five window calculation | `NUMERICAL` | Attenuation at five threshold nodes in one fixed-policy calibration | General sign, causal estimate, chord mechanism, or empirical magnitude | One illustration with all conditions attached |

### 3.2 Empirical ledger

| Exercise | Artifact status | Realised result | Precision or gate | Claim allowed |
|---|---|---|---|---|
| Corrected filing delay | **No adopted result artifact yet** | Feasibility audit: pre 399, post 365; median 7 to 4 business days; share within five days 37.6% to 78.6% | Missing-trigger denominator and manual audit unresolved; no independent reproduction | “Promising feasibility result,” not yet a manuscript result |
| H1 partition contrast | `ESTIMATED`, independently reproduced | Pooled slope 0.67 pp; flagged-window slope 1.24 pp; difference 0.58 pp | Difference SE 1.56 pp, conservative p 0.741, MDE 4.38 pp | Estimate and interval; no partition validation and no evidence of a structural zero |
| H2 `RUNUP5` | `ESTIMATED`, independently reproduced | Liquidity-by-post 0.0175 pp | SE 4.42 pp, p 0.997, MDE 12.39 pp | Boundedly uninformative; no attenuation claim |
| H2 `JUMP` | `ESTIMATED`, independently reproduced | Liquidity-by-post 0.54 pp | SE 4.15 pp, p 0.928, MDE 11.62 pp | Same; not a test of L2's endpoint |
| Bindingness dose | `ESTIMATED` | Return and stake interactions close to zero | Direct coverage 127 filers; MDEs roughly 7.5–17.0 pp; imputed run-up MDE about 62.4 pp | Weak exploratory or bounded evidence only |
| Stake at filing | `ESTIMATED` | Post level -0.98 pp; liquidity-by-post -2.16 pp | MDE 6.55 pp and 3.57 pp; selection and object mismatch | Descriptive only |
| Pseudo-trigger placebo | `ESTIMATED` | Pseudo-H1 clean; pseudo-H2 run-up p 0.081 | Borderline status ambiguity; 13G placebo not run | Full disclosure; no rescue of H2 |
| BID12 coding | Audit pass, base-rate gate fail | Blind audit 0 disagreements of 30; measured treated rate 12.61% | Registered 18.1% base-rate gate fails; `all_passed=false` | Reliability on audited cases, not complete outcome coverage |
| Matched BID12 DiD | `NOT ESTIMATED` | No coefficient | Balance fails after tighter caliper; pre-trend F 3.249, p 0.0214; causal language barred | Design failure only, never “null effect” |
| Within-13D BID12 | `ESTIMATED` | Liquidity-by-post -0.65 pp | SE 3.93 pp, p 0.878, MDE 11.01 pp; failed base-rate gate | Interval and caveat, not mechanism test |
| Triple difference | `ESTIMATED` on failed draw | -5.94 pp | SE 6.59 pp, p 0.398, MDE 18.45 pp; failed matching status | Sign and interval only |
| Run-up path and 13G placebo | Not run | None | No artifact | No claim |

The independent verification report reproduces H1 and H2 coefficients and clustered standard errors and finds the relevant result files internally consistent (`/Users/austinli/Projects/blockholder_v4/quality_reports/verification/2026-08-30_estimates_verify.md:28-75`; `/Users/austinli/Projects/blockholder_v4/quality_reports/verification/2026-08-30_estimates_verify.md:170-175`). The main problem is therefore not computational reliability. It is interpretation, power, and registered design failure.

### 3.3 Artifact-verified mandatory statuses

**H1 — `ESTIMATED`.** `h1_estimate.json` records `main_n=979`, the partition coefficient 0.005766, two-way SE 0.015634, conservative p 0.740874, and MDE 4.38072 percentage points (`/Users/austinli/Projects/blockholder_v4/empirics/output/h1_estimate.json:3`; `/Users/austinli/Projects/blockholder_v4/empirics/output/h1_estimate.json:28-30`; `/Users/austinli/Projects/blockholder_v4/empirics/output/h1_estimate.json:51-62`).

**H2 — `ESTIMATED`.** `h2_estimate.json` records the `JUMP` interaction 0.005395 with MDE 11.6208 percentage points and the `RUNUP5` interaction 0.000175 with MDE 12.3932 points (`/Users/austinli/Projects/blockholder_v4/empirics/output/h2_estimate.json:3-17`; `/Users/austinli/Projects/blockholder_v4/empirics/output/h2_estimate.json:32-40`; `/Users/austinli/Projects/blockholder_v4/empirics/output/h2_estimate.json:141-149`).

**BID12 — audit reliability does not clear the outcome gate.** `bid12_gates.json` records a treated rate of 0.1261 on 3,418 coded rows against the 18.1 percent gate and `all_passed=false` (`/Users/austinli/Projects/blockholder_v4/empirics/output/bid12_gates.json:40-42`; `/Users/austinli/Projects/blockholder_v4/empirics/output/bid12_gates.json:75`). `did_estimate.json` remains `NOT ESTIMATED`, with `quote_as_result=false` (`/Users/austinli/Projects/blockholder_v4/empirics/output/did_estimate.json:3-7`; `/Users/austinli/Projects/blockholder_v4/empirics/output/did_estimate.json:160-162`). `did_diagnostics.json` separately records `BLOCKED`, no causal language, and pre-trend p=0.021438 (`/Users/austinli/Projects/blockholder_v4/empirics/output/did_diagnostics.json:3-4`; `/Users/austinli/Projects/blockholder_v4/empirics/output/did_diagnostics.json:40-45`).

The realised reparse funnel is 4,639 enumerated filings, 3,710 parsed trigger dates, 3,356 valid 0–90-day delays, 1,465 CRSP-linked observations, and 1,112 deduplicated subject-trigger observations (`/Users/austinli/Projects/blockholder_v4/empirics/output/reparse_counts.json:4`; `/Users/austinli/Projects/blockholder_v4/empirics/output/reparse_counts.json:103-131`).

## 4. Theory-to-evidence bridge

| Theory primitive or result | Mechanism | Predicted object | Closest observable | Current measure | Mismatch | Claim currently allowed | Required fix |
|---|---|---|---|---|---|---|---|
| `kappa`: noise-trading intensity | Noise changes how informative pooled order flow is | Derivative of posterior, price, entry, or premium with respect to structural noise | Pre-event liquidity and order-flow measures | Negative standardised log Amihud | Amihud is not `kappa`; no proved mapping; quarter standardisation changes interpretation | Heterogeneity by a liquidity proxy | Estimate or calibrate a measurement mapping; at minimum report spread, turnover, and price-impact variants without structural language |
| D1 flagged/pooled partition | Threshold plus deadline determine whether filing arrives before control | Indicator `D` and cell-specific public information | Filing accepted before a specified control event | All sample observations are eventual 13D filers; no observed common control node | Empirics condition on eventual filing and do not observe model horizon `H` or latent cell | The law defines a possible public-information partition | Define an observable decision horizon and disclosure status at that horizon, or leave D1 as theory |
| D1 price-path identity | Total movement on a flagged history decomposes around disclosure | `R` and `J` on the same history | Trigger-to-filing and filing-window returns | `RUNUP=CAR[TD,FD*-1]`; `JUMP=CAR[FD*-1,FD*+1]` | One-day overlap; model price levels differ from market-model CARs; no same-order-flow counterfactual | Descriptive price-path components | Use non-overlapping timestamp-aware windows; treat identity as accounting intuition, not an identified theorem test |
| L2 flagged endpoint invariance | Flagged tuple fully reveals the value-relevant plan component | `P^F`, flagged posterior, entry probability, `M_F` | Post-disclosure endpoint or innovation conditional on pre-filing information | Filing-window CAR slope in H1/H2 | Return equals endpoint minus liquidity-sensitive pre-price; L2 does not sign `J` | No L2 claim from H1/H2; only estimate and interval | Test an endpoint or residualised post-publication innovation conditional on the pre-filing information set; maintain explicit separation assumptions |
| L1 premium mixture | Overall engagement premium is a weighted average across cells | `Omega`, `M_F`, `M_P` | Share flagged by a decision date and cell-specific outcomes | No empirical `Omega`; only a calibrated engagement share | Cell weights and conditional premia unobserved | The decomposition organises theory | Build a dated control-event panel or leave mixture unestimated |
| Threshold margin `tau` | Lower threshold reclassifies more histories as flagged | Change in flagged mass and pooled composition | Historical or cross-jurisdiction threshold changes | No threshold reform in current US sample | February 2024 changed the window, not threshold | Threshold and window are conceptually distinct | Obtain a separate threshold change or present threshold result as theory only |
| Window margin `T` | Shorter deadline moves some crossings into flagged state and changes pooled composition | Change in liquidity sensitivity governed by weight and composition | February 2024 deadline change | H2 liquidity-by-post interactions | No unconditional theoretical sign; windows may include filing; no unaffected state | One calibration points toward attenuation; data are uninformative | New public-arrival measure plus untouched confirmation; never select sign after viewing |
| Filing stake `B^F` and residual order `Q^F` | Filing reveals stake and post-flag order, helping identify type | Stake at filing and post-filing accumulation | Reported percentage and transaction table | `pct_of_class` at filing | Derivatives, groups, stale denominator, selection; residual target unobserved | Descriptive stake distributions only | Parse transaction-level holdings, denominator dates, and amendments; define exact theoretical counterpart |
| Bidder entry | Public information changes entry cutoff | Probability bidder enters after observing state | Deal announcement or bid filing | BID12 within twelve months | Multiple bidders, endogenous campaign duration, defensive sales, censoring, coding coverage; model time is not twelve months | No causal or structural entry claim | Build dated SC TO-T, 14D-9, DEFM14A, and 8-K event histories and predefine the control node |
| Engagement premium | Voice changes premium conditional on entry | `m1-m0` or cell-specific expected premium | Offer premium in identified transaction | Binary BID12; no offer premium headline | Incidence is not premium; engagement and counterfactual missing | Theory discusses a premium mechanism | Parse or hand-collect offer and unaffected prices; separately identify engagement effect |
| Realised legal clock | Reform changes latest permissible disclosure and possibly realised timing | Filing-delay distribution | Trigger and accepted filing timestamp | Old Fact 1 plus read-only corrected audit | Old duplicates/parser; residual missing trigger dates; historical outcome already viewed | Feasibility evidence strongly suggests compression | Freeze protocol, resolve denominator, blind-audit, save immutable artifact, reproduce independently, and use an untouched extension for confirmation |

**Inference:** the filing-delay fact is the only December-feasible observable that cleanly corresponds to an institutional primitive. It measures the realised clock. It does not measure the latent partition, structural noise, bidder entry, or engagement premium.

## 5. Refreshed competitor map

### 5.1 Search procedure, scope, and limits

The online refresh was conducted on **31 August 2026**. Searches covered Schedule 13D thresholds and deadlines, the February 2024 rule, blockholder disclosure and activism, liquidity and order-flow inference, block accumulation, activism and takeover incidence or premia, market prices as bidder signals, empirical use of the 2024 reform, and 2025–2026 working papers, forthcoming articles, and conference records. Priority was given to SEC materials, official journal pages, author pages, CEPR and ECGI records, DOI records, and SSRN records.

Access was imperfect. Some SSRN pages returned robot or rendering failures; several journal full texts are paywalled; and a search cannot prove non-existence. The local competitor map also records soft search walls. The defensible conclusion is therefore bounded: **no direct duplicate was found that combines the Schedule 13D legal clock, liquidity-sensitive order-flow inference, and a bidder or control-premium object.** The local map reaches the same bounded conclusion and expressly records its limitations (`/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:74-78`).

### 5.2 Direct institutional competitor

**Avaneendra Trivedi, “The Mandated Revelation Field.”** The [current author research page](https://www.avaneendratrivedi.com/research), checked 31 August 2026, describes a broader disclosure system with 1,132 filings and 2,583 facts and states that a pre-registered flagship return claim failed out of sample. The local full-paper record corresponds to an earlier 333-filing Schedule 13D natural experiment, with a compliance-share first stage of 0.348 and no control-outcome object (`/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:41-51`; `/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:109-111`). This version drift is material; the latest paper must be obtained before circulation.

**Substitution threat:** high for any claim that this is the first empirical paper on the 2024 deadline or the first to treat legally scheduled disclosure as a market state.

**Increment required:** make the **equilibrium corporate-control mechanism of a legal threshold-plus-clock partition** the contribution. Do not compete on compliance measurement or broad “mandated revelation” infrastructure.

### 5.3 Corporate-control and activism competitors

**Burkart, Lee, and Voss, “The Evolution of the Market for Corporate Control.”** The [LSE repository](https://researchonline.lse.ac.uk/129506/), checked 31 August 2026, records the paper as *Journal of Finance*, in press, accepted 14 September 2025. The [ECGI record](https://www.ecgi.global/publications/working-papers/the-evolution-of-the-market-for-corporate-control) records a 29 December 2025 revision. The paper models informed large shareholders choosing between bidding and initiating a sale, with takeover activism and private equity as complementary control mechanisms.

**Substitution threat:** high for a generic “activism and corporate control” theory paper.

**Increment required:** the statutory disclosure clock and market-information partition must be essential, not decorative.

**Celentano and Levine, “Shareholder Activism, Takeovers, and Managerial Discipline.”** The [ECGI presentation record](https://www.ecgi.global/shareholder-activism-takeovers-and-managerial-discipline) describes an estimated activism-and-M&A model. The [author page](https://oliverlevine.com/) lists it as a revise-and-resubmit at the *Review of Financial Studies*, and the July 2026 [ECGI summary](https://www.ecgi.global/publications/blog/activism-and-takeovers-friends-or-competitors) describes both facilitation and crowd-out channels. The local reading record warns that the often-quoted 13.69 percent premium effect is a marginal counterfactual; the general-equilibrium change reported there is 0.60 percent in magnitude (`/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:41-41`; `/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:109-109`).

**Substitution threat:** very high for any quantitative statement about activism changing takeover incidence or premia.

**Increment required:** do not lead with the level effect of activism on takeovers. Lead with how the legal clock changes what the public market and bidder know.

**Payne-Mann, Stice-Lawrence, and Wong, “Potential Activism and the Threat of Public Campaigns.”** The [SSRN DOI record](https://doi.org/10.2139/ssrn.5076900) was checked 31 August 2026. The local map identifies this as the one direct 2024–2026 hit not fully obtained and therefore a live threat for 13D/13G-linked control outcomes (`/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:78-88`; `/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:407-413`).

**Increment required:** distinguish a legal timing partition from the threat of a public campaign and from the 13D/13G purpose split. The paper must be read before final novelty language is frozen.

### 5.4 Trading, liquidity, and information competitors

**Cetemen, Cisternas, Kolb, and Viswanathan.** Their 2026 [Journal of Finance article](https://onlinelibrary.wiley.com/doi/full/10.1111/jofi.70033) places informed activist trading inside a dynamic strategic market.

**Substitution threat:** high for generic claims about activism, private information, and order flow.

**Increment required:** the disclosure deadline must be a primitive that changes the public information set and control decision; citing 13D as background is insufficient.

**Back, Collin-Dufresne, Fos, Li, and Ljungqvist.** Their [Econometrica article](https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA14917) develops dynamic informed activist trading.

**Substitution threat:** high for dynamic liquidity and accumulation, lower for the legal partition and bidder premium.

**Increment required:** show that the threshold and deadline cannot be reduced to a single trading-horizon or noise-variance term.

**Choi, Joenväärä, Rösch, and Tiu, “Market Quality of Informed Trades.”** The [current SSRN record](https://doi.org/10.2139/ssrn.5317851), checked 31 August 2026, describes roughly 500,000 timestamped 13D transactions matched to TAQ and studies execution, price impact, and realised spreads.

**Substitution threat:** severe for the runner-up's generic “what happens around activist trades” language.

**Increment required:** use legal-clock variation and exact public-arrival timing; do not compete on transaction-level execution quality alone.

**Marinovic and Varas, “Strategic Trading and Blockholder Dynamics.”** The 2026 [RAND Journal of Economics article](https://onlinelibrary.wiley.com/doi/10.1111/1756-2171.70040) studies private information, block size, trading speed, and liquidity.

**Substitution threat:** moderate for generic informed-blockholder dynamics.

**Increment required:** retain the statutory trigger, filing clock, and external bidder's information state.

### 5.5 Disclosure, leakage, and structural-form competitors

**Zeng, “Do managers learn about their firm's ownership changes before public disclosure?”** The 2026 [Review of Accounting Studies record](https://ideas.repec.org/a/spr/reaccs/v31y2026i2d10.1007_s11142-026-09958-z.html) documents manager and insider learning before 13D/13G disclosure. The local card shows why this paper's pooled state must be described as pooled **for the price-setting public market**, not unknown to every actor (`/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:65`; `/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:173-189`).

**Substitution threat:** high for claims that no one learns before filing.

**Increment required:** explicitly model public-market inference while allowing target managers or other informed actors to be exceptions or extensions.

**Albuquerque, Fos, and Schroth.** Their [Journal of Financial Economics article](https://www.sciencedirect.com/science/article/pii/S0304405X21003950) structurally analyses value creation and 13D versus 13G announcement effects.

**Substitution threat:** high for broad “structural blockholder disclosure” positioning.

**Increment required:** distinguish purpose-form choice from the legal threshold and deadline and from an external bidder's entry decision.

### 5.6 Dynamic ownership competitor

**Gryglewicz, Mayer, and Morellec, “Ownership Dynamics and Firm Policies with a Large Shareholder.”** The [CEPR record](https://cepr.org/publications/dp21226), checked 31 August 2026, describes a dynamic model of endogenous ownership and firm policy. The local map identifies it as occupying the gradual stake path and lumpy acquisition object, but not the legal clock, private-information partition, external bidder, or takeover-premium mechanism (`/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:66`; `/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:140-153`).

**Increment required:** do not sell the stake path itself as new. Sell the legal clock's effect on information and control.

### 5.7 Whitespace verdict

**Verified fact:** the local map's strongest cells remain unoccupied in the material reviewed: window length as a determinant of a takeover-premium object, a rule-keyed threshold-plus-date partition, and bidder entry linked to a filing window (`/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:140-173`; `/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:210-239`; `/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:272-274`).

**Inference:** the whitespace is narrow but defensible. It is not “activism plus liquidity plus takeovers”; each broad ingredient is crowded. It is **the statutory disclosure clock as an equilibrium public-information partition for a corporate-control decision**.

**Recommendation:** every novelty paragraph should name the nearest owner of each ingredient and state the missing link. Do not use “no paper” without the bounded search qualification.

## 6. Three-position scorecard

Scores run from 1 to 5. December feasibility is counted twice. A fatal defect in identification, theorem validity, data, novelty, or model-to-measure alignment overrides the total.

| Rank | Integrated paper position | Importance | Novelty | Theory validity and value | Model-to-measure alignment | Empirical credibility | December feasibility | Presentation clarity | Journal ceiling | Feasibility counted twice | Weighted total | Fatal flaw? |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **1** | **Legal disclosure clock as an information partition, plus one corrected filing-delay implementation fact** | 4 | 4 | 4 | 3 | 3 | 5 | 5 | 3 | 5 | **36** | No, conditional on empirical gate |
| **2** | **Timestamp-aware reallocation of price discovery around the public filing** | 4 | 4 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | **32** | No current result; material December execution risk |
| **3** | **Registered H1/H2 timing split plus matched control-outcome programme** | 4 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | 2 | **20** | **Yes: wrong observable bridge and causal leg not estimated** |

### Position 1 — winner

**Core:** D1, L1, L2, and the threshold-versus-window distinction explain how law changes public information before a control decision. A corrected EDGAR result documents the reform's realised timing bite.

**Why it wins:** it uses the strongest proved theory, demands the smallest empirical repair, can be completed and explained by December, and survives honest claim limits. It does not require a causal estimate that the project does not have.

**Weakness:** the empirical fact verifies the institutional first stage, not the mechanism. That limits the journal ceiling and creates the principal integration risk.

### Position 2 — runner-up

**Core:** use exact EDGAR acceptance times and non-overlapping market windows to test whether price incorporation shifts from the covert interval to the public-arrival interval when the clock shortens.

**Why it is viable:** it repairs the current observable mismatch and speaks directly to market learning. It uses D1's price-path decomposition without pretending that a filing return is the flagged endpoint.

**Direct reason it loses:** no compliant result exists; TAQ access and linkage are unverified; the Choi et al. paper raises the novelty bar; and prospective confirmation is needed because the historical return outcomes have been viewed. It is a post-December upgrade unless all blind feasibility gates clear unusually early.

### Position 3 — rejected

**Core:** present H1 as the partition test, H2 as the 2024 window test, and BID12 as the control-outcome leg.

**Direct rejection reason:** H1 labels calendar-return windows as latent information cells even though the theory does not. H2 has MDEs of 11.6–12.4 percentage points and cannot discriminate economically relevant signs. BID12's matched design is `NOT ESTIMATED`, and its pre-trend rule forbids causal language. This is not merely a weak paper; the proposed interpretation is incoherent. The registered results should remain in an honesty appendix, not in the headline.

## 7. Winning December paper

### 7.1 One-sentence objects

**Working title:** *The Disclosure Clock: Market Inference and Corporate Control*.

**Economic question:** How do a statutory blockholder-disclosure threshold and filing deadline divide trading histories into public and still-pooled information states before a corporate-control decision?

**Contribution:** The paper makes the legal disclosure clock an equilibrium information-partition primitive, proves what that partition implies for market and bidder inference under explicit conditions, and documents that the February 2024 rule materially compressed realised Schedule 13D filing delays.

**Main theoretical result:** Under the model's fixed-policy and flagged-identification conditions, the legal threshold and deadline create an exhaustive flagged/pooled partition; the flagged endpoint and flagged control-premium component are invariant to noise-trading intensity, while threshold tightening and window tightening have distinct comparative statics, with no unconditional sign for the window.

**One empirical headline result:** Conditional on the acceptance protocol below, a corrected unique-accession analysis will show that realised filing delays compressed sharply under the five-business-day regime. The provisional audit is seven to four business days at the median and 37.6 to 78.6 percent filed within five business days in the pre-fixed windows. These values remain provisional until saved as an immutable result artifact and independently reproduced.

### 7.2 Complete logic chain

1. **Institution.** A holder crosses five percent, but the public market need not receive the Schedule 13D immediately. The threshold and legal filing interval are separate legal margins.
2. **Mechanism.** Before public filing, informative order flow is pooled with noise. After a sufficiently revealing filing and flagged order, the public market and bidder condition on a sharper information set.
3. **Prediction.** The rule changes the probability of reaching each public-information state before control. The flagged endpoint can be insulated from noise under L2, but the observed filing jump need not be. Threshold tightening has a cleaner attenuation result than window tightening; the latter depends on composition.
4. **Estimand.** The December empirical estimand is not a return or takeover coefficient. It is the change in the realised distribution of trigger-to-filing delay under the new legal clock.
5. **Evidence.** A near-census EDGAR reconstruction, with exact trigger and acceptance dates, establishes whether filers actually moved inside the new clock.
6. **Interpretation.** The evidence validates the empirical relevance of the legal timing primitive. It does not identify the effect of the rule on liquidity, prices, activism, bidder entry, or takeover premia.

### 7.3 Why theory and evidence belong together

The empirical fact is not ornamental if the paper asks whether a legal clock is an economically meaningful state variable. A model of `T` would be institutionally weak if filers followed the same schedule regardless of the legal change. A large realised compression establishes that the statutory clock altered the timing environment that the model treats as primitive.

The integration remains deliberately modest. The evidence does not test L2 or T1. The theory explains why a timing change can matter even when a simple average return effect is absent or ambiguous; the evidence establishes that the timing change occurred in practice. That is enough for a coherent departmental paper. It is not enough by itself for a near-top empirical contribution.

### 7.4 Exact permissible and impermissible claims

**Permissible claim:** “After the February 2024 Schedule 13D deadline change, the realised filing-delay distribution in our pre-fixed samples moved sharply toward five business days. The model shows why a legal threshold and filing clock can change the public information available before a control decision, while also showing that the window's effect on liquidity sensitivity has no unconditional sign.”

**Attractive but impermissible claim:** “The shorter deadline caused less pre-filing informed trading, made the filing response liquidity-invariant, reduced takeover premia, or reduced the liquidity sensitivity of control outcomes.” No current result identifies any of those statements.

### 7.5 Closest competitors and precise differences

The closest institutional competitor is Trivedi's current mandated-revelation paper. It owns the empirical idea that legally scheduled disclosure can be represented as a dated market-state object and already uses the February 2024 change. The incremental contribution must therefore be narrower and more economic: **a corporate-control equilibrium in which the legal threshold and filing clock determine the bidder's public information set and separate threshold from window comparative statics.**

The closest corporate-control competitors are Burkart–Lee–Voss and Celentano–Levine. They own important activism/takeover mechanisms and quantitative control effects. This paper differs by making the statutory clock and public-market inference essential. The closest trading competitors are Cetemen et al., Back et al., Marinovic–Varas, and Choi et al. They own dynamic informed trading or transaction-level execution; this paper differs by tying public arrival to a legal clock and an external bidder.

### 7.6 Section-by-section manuscript outline

1. **Introduction: the missing clock.** One motivating timeline, one contribution paragraph, and one honesty paragraph. State immediately that the paper does not estimate a causal takeover effect.
2. **Institution: crossing, clock, public filing, control.** Explain the 13D/13G distinction only to the level needed; show ten calendar days versus five business days; discuss EDGAR public arrival and current trade-date counting. Define “pooled for the price-setting public market.”
3. **Model.** Introduce value, signal, plan, stake path, noise, prices, filing, bidder, and premium. Suppress proof-level regularity from the main exposition.
4. **The disclosure-clock partition.** Present D1, L1, L2, the 110/100/107 example, and the threshold/window distinction.
5. **Policy margins and limits.** State T1 compactly: threshold result, window if-and-only-if, fixed-policy scope. Show one calibration table or figure and immediately state that `A(tau)` fails at the implemented calibration.
6. **Did the clock move?** Present the corrected filing-delay protocol, sample, main table, empirical CDF, missingness audit, and prospective 2026 validation.
7. **Implications and conclusion.** Explain what the model changes about interpretation of disclosure policy, what the evidence establishes, and what remains open.

### 7.7 Theorem, proposition, calibration, table, and figure placement

| Item | Placement | Purpose |
|---|---|---|
| Proposition 1: clock partition and price-path identity, D1 | Main text, Section 4 | Establish the institutional state map |
| Proposition 2: premium mixture, L1 | Main text, directly after Proposition 1 | Link states to the control-value object |
| Proposition 3: flagged endpoint invariance, L2 | Main text, with assumptions in a boxed paragraph | State the sharp inference result without mislabelling filing returns |
| Theorem 1: threshold/window comparative statics, compressed T1 | Main text, Section 5 | Make the policy-margin distinction the headline theorem |
| Existence theorem P1 | Appendix statement; one sentence in main text | Prevent technical existence from dominating the paper |
| L3, L4, and C1 details | Technical appendix | Preserve the complete honesty record |
| Calibration table | Main text, one compact table | Show `W_T*C_T` at five nodes and all fixed-policy/calibration caveats |
| Main empirical table | Main text, Section 6 | Counts, coverage, median, quantiles, share within legal deadline, and exact definitions |
| Anchor figure | End of introduction and presentation | Two-panel clock diagram plus audited pre/post delay CDF |

### 7.8 Main text, appendix, and cuts

**Main text:** institution, actors, clock partition, D1/L1/L2, threshold-versus-window theorem, one numerical illustration, corrected filing-delay fact, and explicit non-claims.

**Appendix:** complete P1 proof; A3/A6 restrictions; L3/L4 chord machinery; C1 dominance/contraction; numerical failures and unresolved nodes; all H1/H2/dose/stake/BID12 estimates with registered statuses; parser and audit protocol; full competitor and search record.

**Cut from the December argument:** the claim that the filing-window return is the flagged state; H1/H2 as headline tests; the matched BID12 design as an estimate; any causal language; the erroneous $810 million SEC motivation identified in the competitor audit (`/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:51`); the disclosure-regime comparison as evidence about the window margin; the chord calculation as independent evidence at a calibration where its support condition fails; proof-condition inventories in the main text; and any suggestion that a numerical sign is a theorem.

### 7.9 Presentation anchor

The presentation should turn on one two-panel graphic.

* **Left panel:** a horizontal timeline showing quiet acquisition, five-percent crossing, legal interval, EDGAR public arrival, and bidder/control decision. Beneath it, show that the threshold changes who crosses while the window changes whether the flag arrives before control.
* **Right panel:** the audited pre- and post-rule empirical CDF of business-day filing delay, with the five-business-day line and coverage counts.

The audience should understand the institution, model partition, empirical fact, and claim limit from this single slide.

### 7.10 150-word supervisor pitch

> The paper asks what a blockholder-disclosure clock does to market inference and corporate control. A blockholder can cross five percent, continue trading before the filing becomes public, and face a bidder whose entry decision depends on what prices and filings reveal. The model's clean result is not that shorter deadlines always improve outcomes. It is that the threshold and filing window create different information margins: the threshold changes which positions enter the public state, while the deadline changes whether disclosure arrives before the control decision. Under explicit conditions, the flagged endpoint is insulated from order-flow noise, whereas the still-pooled state is not; the window's sign remains conditional. The empirical contribution is deliberately narrower: an independently reproduced EDGAR result will document how the February 2024 rule compressed filing delays. That fact verifies that the legal clock moved in practice. It does not claim a causal effect on returns, activism, or takeovers.

### 7.11 Five hard referee or supervisor questions

**1. Is the filing-delay result too obvious to count as evidence?**  
It is not a mechanism test and should not be sold as one. Its value is to establish that the legal primitive moved realised behaviour rather than remaining slack. That is admissible for a December theory paper. It is insufficient for a near-top journal without a model-aligned market or control outcome.

**2. Why include corporate control when no takeover effect is estimated?**  
Because bidder inference and the premium make the information partition economically consequential inside the model. The manuscript must say that corporate control is a theoretical application, not an empirically identified outcome. If the bidder can be removed without changing the core economic results, then “corporate control” should be removed from the title rather than preserved rhetorically.

**3. Why should a filing reveal enough to make the flagged endpoint invariant?**  
Only under the explicit flagged-tuple injectivity and fixed-policy conditions. The result is not generic. Zeng's evidence also means the pre-filing state is not unknown to all actors. The paper should state “pooled for the price-setting public market,” explain the separation condition, and put failure cases in the appendix.

**4. Why not use H1 as a simple test of L2?**  
Because L2 is an endpoint and posterior result, while H1 uses a return from a liquidity-sensitive pre-filing price to the endpoint. An invariant endpoint can coexist with a strongly liquidity-sensitive filing return. The 110/100/107 example establishes the logical point without econometrics.

**5. What is new relative to Trivedi, Burkart–Lee–Voss, Celentano–Levine, and the trading literature?**  
Not the existence of legally scheduled disclosure, activism and takeovers, or informed accumulation separately. The increment is the statutory threshold-plus-deadline as an equilibrium public-information partition that shapes a bidder's inference, with separate threshold and window margins and explicit non-sign results.

## 8. Required theory work

### 8.1 No new theorem is required for December

**Recommendation:** do not reopen the frozen model record for the winning December paper. D1, L1, L2, and T1 are sufficient. The binding theory task is exposition and claim discipline, not another theorem.

A new theorem would become necessary only if the paper insisted on an unconditional sign for the five-business-day reform or a direct mapping from filing-window returns to the flagged state. The current model provides neither. Attempting to prove either now would be a wholesale research reopening rather than a minimum repair.

### 8.2 Minimum manuscript repair

| Economic or presentation defect | Minimum change | Independent validation | Files that would eventually require authorised change | Kill criterion |
|---|---|---|---|---|
| Live draft maps L2 to a liquidity-invariant empirical filing window | Delete that bridge; insert endpoint-versus-return example | Independent theory reader checks every L2 empirical sentence against MODEL_CARD row 656 | `draft_v3.tex`, `draft_v3_trace.md`; no frozen model file | Any surviving sentence says `J` or an observed filing CAR is `kappa`-invariant |
| Public theory is dominated by proof architecture | Move P1 condition inventory, L3/L4 construction, and C1 region machinery to appendix | A finance theorist can state the mechanism after a five-minute read | `draft_v3.tex` and online appendix organisation | Main text remains a proof ledger rather than an economic paper |
| Window attenuation reads stronger than authority permits | State exact if-and-only-if, fixed-policy scope, and calibration status every time | Search audit for “attenuate,” “shorter window,” and “2024” | `draft_v3.tex`, slides | Any unconditional reform sign remains |
| Pooled state reads as unknown to everyone | Change to “pooled for the price-setting public market”; cite Zeng | Literature and assumption audit | `draft_v3.tex`, bibliography | Claim survives that no actor can know before filing |
| Corporate-control title risks overstatement | Show that bidder and premium are load-bearing for L1/L2/T1; state empirical non-identification in abstract and conclusion | Removal test: if bidder can be deleted without changing results, retitle | `draft_v3.tex` | Corporate control remains in title but not in the economic contribution |
| Numerical calibration is mistaken for theorem evidence | Use one compact calibration table with labels and support failures | Reproduce values from frozen handoff; line-by-line label audit | `draft_v3.tex`, authorised generated table | Any `NUMERICAL` result is called proved, general, or causal |

### 8.3 Effort, dependencies, and fallback

Estimated effort is **six to eight concentrated author days** for manuscript surgery plus **two independent reader days** for a claim audit. The critical dependency is the author's willingness to remove technically correct but editorially non-load-bearing material.

The last safe date to reopen theory is **25 September 2026**. After that, only exposition and genuine error correction should be allowed. If a supervisor requires an unconditional window sign by then, narrow the paper to the clock partition and non-sign result rather than starting a new equilibrium model.

## 9. Required empirical work

### 9.1 Required exercise E1: corrected filing-delay implementation result

This is the only new empirical exercise on the winning paper's critical path. The existing historical numbers have been viewed. The historical analysis is therefore a transparent descriptive reconstruction; an untouched 2026 extension supplies prospective confirmation of persistence, not causal identification.

| Design element | Fixed specification |
|---|---|
| Economic question and model object | Did realised disclosure timing move when the legal Schedule 13D clock changed? The corresponding model primitive is the filing window `T`, not `kappa`, a return, bidder entry, or takeover premium. |
| Unit of observation | One unique initial Schedule 13D accession for one subject issuer and reporting group. Amendments are excluded. Duplicate accessions and duplicate group filings are resolved by a predeclared hierarchy. |
| Target population | All initial Schedule 13D filings enumerated by EDGAR in the pre-fixed 2023Q2–Q3 and 2024Q3–Q4 windows. A prospective validation population consists of all eligible initial filings accepted from **1 September through 20 November 2026**, frozen before those outcomes are parsed. |
| Treatment or comparison | Descriptive comparison of the old ten-calendar-day regime and the new five-business-day regime. The 2026 extension tests persistence under the new regime. Neither comparison is labelled causal. |
| Primary outcome | Indicator that the initial 13D was publicly accepted within five business days of the trigger under a contemporaneous legal calendar. |
| Co-primary outcome | Trigger-to-acceptance delay in business days, summarised by the median. |
| Secondary outcomes | Calendar-day delay; legal on-time status under the contemporaneous rule; 25th, 75th, and 90th percentiles; empirical CDF; mass at each delay day; accepted-after-4 p.m. and after-market-close indicators. |
| Exact historical estimand | Difference between post- and pre-regime shares filed within five business days, and the post-minus-pre median delay. These are labelled viewed descriptive estimates. |
| Exact prospective estimand | Difference between the fixed historical pre-regime share and the 2026 post-rule share, using the same frozen parser, calendar, and sample rules. This confirms persistence of clock compression, not the causal effect of the 2024 reform. |
| Core data fields | Form, accession, accepted timestamp, SEC filing date, reporting CIK, subject CIK, subject name, reporting group, Item 5 event or trigger date, percent of class, filing document route, raw text or XML, and amendment status. |
| Data sources | EDGAR quarterly master indexes, submissions metadata, filing documents, and a versioned US-federal-business-day calendar. The legal-rule version is stored with each observation. |
| EDGAR linkage | Accession is the immutable filing key. Subject and reporting CIKs are parsed from the filing and checked against submissions metadata. Reporting groups are deduplicated with an explicit same-subject, same-trigger, same-group rule. |
| CRSP linkage | Not required for sample inclusion or the headline. CUSIP and PERMNO may be retained for audit and descriptive composition tables, using the existing CIK/CUSIP/PERMNO bridge and a documented one-to-many hierarchy. |
| Compustat linkage | Optional for secondary industry and size composition only. It cannot determine headline inclusion or change the denominator. |
| Expected historical sample | The read-only audit enumerates 616 pre and 521 post unique accessions and currently retains 399 and 365 valid 0–60-day delays. Roughly 315 enumerated cases require classification, parser recovery, or explicit unresolved status. |
| Expected prospective sample | Approximately 180–300 initial filings by 20 November, based on recent EDGAR frequency. This is a planning range, not a guaranteed count; blind counts replace it before power lock. |
| Estimator | Counts, shares, empirical CDFs, and quantile differences. Historical confidence intervals use subject-CIK cluster bootstrap and are labelled descriptive. The prospective confirmation uses the pre-registered cluster-bootstrap procedure. |
| Fixed effects and controls | None in the primary result. Secondary composition panels may show filing month, filer type, group status, industry, and market-cap bin. No regression-selected control set becomes the headline. |
| Inference and clustering | Cluster on subject CIK. A two-way subject-CIK and filing-month sensitivity is reported if month-cluster counts support it. Exact or wild-bootstrap inference is used when month clusters are few. |
| Historical power | At provisional counts and shares, the unclustered standard error of the share difference is about 3.24 percentage points and the 80-percent-power MDE is about 9.07 points. The provisional difference is 41.04 points. Budget for a clustered MDE no better than 12 points. |
| Prospective power gate | Before parsing any 2026 delay outcome, compute power from the blind eligible count and historical pre share. Require an MDE no larger than 15 percentage points for the prospective persistence test. If the gate fails, report the extension descriptively without calling it confirmation. |
| Identifying assumptions | Trigger dates are measured consistently; accepted timestamp captures public arrival; manual recovery removes differential parser selection; the reported population and unresolved category are complete. No parallel-trend or stable-composition assumption is used for a causal claim because no causal claim is made. |
| Anticipation threat | The rule was adopted in October 2023, so filers could adjust before February 2024. This is a reason not to call the pre/post difference causal; it is not a reason to suppress the timing comparison. |
| Selection threat | Missing trigger dates, filings more than 60 or 90 days late, group structures, and amendments can differ by regime. Every enumerated accession must receive a resolved, ineligible, or unresolved code. |
| Measurement threat | Calendar versus business days, federal holidays, trade-date counting, same-day timestamps, structured XML, and stale document labels can move delay. The protocol fixes each definition and stores raw source fields. |
| Contemporaneous-rule threat | The EDGAR daily cut-off changed on 5 February 2024. The primary day-level result is less exposed, but exact timestamp analyses must report it. Later SEC interpretations are not silently applied to historical filer intent. |
| Parser gates | Reconcile every master-index accession to one status. Achieve at least **95 percent resolved trigger classification** in each historical window, or carry an unresolved category below five percent. No unexplained pre/post difference in unresolved share above three percentage points. Preserve source-document and parser hashes. |
| Linkage gates | Headline sample cannot depend on CRSP or Compustat linkage. For composition tables, manually audit 50 one-to-many or low-confidence security links; require at least 98 percent correct subject identity. |
| Manual-audit gates | Manually resolve every residual historical case where the filing contains a usable trigger date. Separately blind-audit 100 automated parses, stratified by regime and parser route. Permit at most two material date errors and no systematic direction by regime. A second reader adjudicates all disagreements. |
| Balance and falsification diagnostics | Compare unresolved rates, filer type, group status, filing month, accepted-after-4 p.m., structured versus text route, and market-cap distribution where linked. Recompute with calendar delay, business delay, exact legal on-time status, and the predeclared late-filing cap. These are diagnostics, not a search for a preferred result. |
| Placebos | Report impossible negative-delay cases and duplicate-trigger conflicts as data-quality falsifications. Calendar pseudo-cutoffs may be shown descriptively but do not convert the design into a causal one. |
| Multiple testing | One primary share and one co-primary median. Apply Holm adjustment to the two prospective confirmation tests. CDF bands, additional quantiles, month panels, and composition splits are secondary and all are shown. |
| Exploration and confirmation safeguard | Label all corrected historical outputs as viewed. Before ingesting the 2026 extension, freeze code, legal calendar, sample rules, primary outcomes, audit gates, and power gate. Report every predeclared variant. No result-dependent exclusion or preferred window is allowed. |
| Registration | Store a dated protocol and machine-readable configuration before any adopted rerun. It must identify the exact input hashes, parser version, calendar version, eligible forms, deduplication rule, outcomes, audit sample seed, inference, and acceptance gates. |
| Existing files and code reused | `empirics/data/fact2_parsed.jsonl`, EDGAR master indexes, `empirics/facts.py`, current parser and reparse components, and the read-only feasibility logic. The inventory documents 9,234 parsed filing rows, existing CRSP data, and the earlier parser/reproducibility limitations (`/Users/austinli/Projects/blockholder_v4/research/empirics_v4/data_inventory.md:16-27`; `/Users/austinli/Projects/blockholder_v4/research/empirics_v4/data_inventory.md:49-76`; `/Users/austinli/Projects/blockholder_v4/research/empirics_v4/data_inventory.md:153-175`). |
| New code eventually needed | One immutable result builder; contemporaneous rule/calendar module; robust XML/text parser for 2025–2026; unresolved-case queue; audit export; source and output hash manifest; independent reproduction entry point; environment lock. |
| New paid data | None. EDGAR is sufficient. CRSP and Compustat are optional composition aids under the mandate's access assumption. |
| Calendar time | Five to seven author days of code and data work; 20–30 hours of manual resolution and audit; two independent reproduction days. |
| Acceptance test | A committed result artifact and table built from hashed inputs; at least 95 percent resolved denominator in each historical window; blind-audit gate passed; definitions fixed in protocol; independent clean rerun reproduces counts and estimates; manuscript numbers match the artifact exactly. |
| Kill criterion | Kill the empirical headline on **25 September 2026** if coverage remains below 95 percent, the manual error gate fails, the result is driven by one discretionary sample choice, or independent reproduction disagrees. |
| Fallback | A theory-only paper would remain intellectually coherent but would fail the December mandate's requirement of one reproducible empirical result. The December package is therefore `NO-GO` unless E2 has already cleared every feasibility gate. |

The old fact table must not be patched silently. The integration memo states that its 300 rows contain only 282 unique accessions and that its figures are not publishable until corrected (`/Users/austinli/Projects/blockholder_v4/research/empirics_v4/2026-08-31_theory_empirics_december_integration.md:67-69`). E1 must receive a new artifact, new hash, and explicit viewed-status note.

### 9.2 Contingent exercise E2: timestamp-aware price discovery

E2 is the runner-up's design. It is not authorised as the winner's headline. Give it only a blind, two-day feasibility check in parallel. It becomes an active pivot only if access, linkage, timestamp, power, and holdout gates all pass before 11 September.

| Design element | Fixed specification |
|---|---|
| Economic question and model object | Does a shorter legal clock reallocate price incorporation from the pre-publication interval to the immediate public-arrival interval, while leaving the total trigger-to-post-publication response separately measurable? This uses D1's price-path decomposition, not L2's endpoint invariance as a direct empirical null. |
| Unit of observation | Initial Schedule 13D event by intraday interval, collapsed to one filing-level observation for headline estimates. |
| Target population | Initial 13Ds with reliable trigger date, exact EDGAR acceptance timestamp, CRSP security match, and TAQ coverage. Historical 2022–2025 observations form an exploratory sample. All eligible events with trigger or filing dates from 1 September through 20 November 2026 form an untouched confirmation sample if the power gate clears. |
| Treatment or variation | Old versus new legal deadline. Continuous realised delay and a pre-registered predicted-bindingness measure are secondary. No observation is selected using returns, spreads, or sign. |
| Primary outcomes | Pre-publication cumulative abnormal midpoint return ending before the public-acceptance interval; immediate post-publication innovation over a predeclared 60-minute or next-open window; total trigger-to-next-close abnormal return. |
| Secondary outcomes | Thirty-minute response, close-to-next-open response, effective spread, realised spread, price impact, volume imbalance, volatility, and quoted depth. |
| Exact estimand | A three-element vector: post-rule change in pre-publication incorporation, post-rule change in immediate public-arrival incorporation, and post-rule change in total response. The first two are interpreted jointly; the total prevents mechanical window reallocation from being mistaken for new information. Liquidity interactions are secondary. |
| Data fields | EDGAR accession, trigger date, acceptance timestamp, filing date, CIKs, CUSIP, filer type, purpose; CRSP PERMNO and daily returns; TAQ trades, best bid and offer, midpoint, exchange, condition codes, and timestamps; optional Compustat size, industry, and accounting controls. |
| EDGAR–CRSP–TAQ linkage | Accession to subject CIK and filing CUSIP; CUSIP to CRSP history by event date; PERMNO/CUSIP and ticker/exchange to TAQ symbol history. Freeze tie-breaking and effective-date rules before outcomes. Manually audit all low-confidence links and a random 100 high-confidence links. |
| Expected sample | Planning range of 600–900 historical events after linkage and 150–250 prospective events. Replace these approximations with blind counts before inspecting any outcome or conducting the power calculation. |
| Estimator | Stacked event-time local projections or filing-level regressions with predeclared event intervals. Estimate the three primary outcomes separately and jointly test reallocation. Historical specifications are exploratory and reported in full. |
| Fixed effects | Filing month, industry, exchange, price bin, size bin, filer type, and public-arrival bin. The exact set must be fixed before historical outcome estimation and may not absorb the treatment indicator by construction. |
| Controls | Pre-event volatility, market return, industry return, lagged spread, lagged turnover, and pre-event liquidity. Controls are predetermined and fixed before results. No stepwise selection. |
| Inference and clustering | Two-way cluster by subject firm and calendar date. Use wild-cluster inference when one dimension has few clusters. The joint reallocation test uses a covariance matrix across the pre, public, and total equations. |
| Randomisation or placebo unit | Placebo policy dates shifted by fixed multiples of 63 trading days; placebo filing timestamps within the same day; unaffected form types only as diagnostics after proving their filing rules did not change contemporaneously. Placebos do not establish random treatment. |
| Blind power gate | Use only eligible counts and pre-period outcome variances. Require an MDE no larger than 1.5 percentage points for the immediate public response and 2.0 points for the principal liquidity interaction. Failure ends the pivot before post-rule outcomes are viewed. |
| Identifying assumptions | Conditional on controls and fixed effects, no contemporaneous change differentially reallocates price discovery at the exact public-arrival boundary; trigger and acceptance times are accurate; the total-response window captures the same information episode; security linkage is correct. These are demanding assumptions, so the historical result remains descriptive unless a stronger control design is separately registered. |
| Anticipation threat | The October 2023 adoption date can shift behaviour before February 2024. The main pre-period must end at adoption or report an explicit anticipation band. A narrow regression discontinuity in time is not credible by itself. |
| Simultaneous-rule threat | EDGAR's daily filing cut-off changed on 5 February 2024. After-hours and before-open events must be allocated by a frozen public-arrival rule, and the cut-off change must be discussed as a competing channel. |
| Selection threat | Filing timing is endogenous; late filers and early filers differ. The primary comparison is by legal regime with a fixed total-return horizon, not a cross-sectional regression of returns on realised delay. |
| Measurement threat | Trigger dates can be stale or ambiguous; public acceptance may occur outside regular hours; TAQ condition codes and midpoint construction matter; news can coincide with the filing. Every dimension enters the predeclared multiverse. |
| Balance and pre-trend gates | Compare pre-event returns, spreads, volatility, turnover, size, industry, and filer composition across regimes. Estimate monthly pre-period interaction coefficients through 2023Q3. A joint pre-trend p below 0.10 bars causal language but does not suppress descriptive estimates. |
| News and event-overlap gate | Link 8-K, earnings, merger, bankruptcy, and major corporate-action filings. Primary results include all events with flags; a predeclared clean-event sensitivity excludes overlaps. No discretionary manual news exclusions. |
| Parser and timestamp gates | At least 95 percent of eligible filings must have verified acceptance timestamp and trigger date. Blind audit 100 timestamps and 100 trigger dates; no more than two material errors in each and no regime-specific direction. |
| Linkage gate | At least 70 percent of eligible EDGAR events must link unambiguously to TAQ. If linkage is below 70 percent or differs by more than ten percentage points across regimes after conditioning on listing status, kill the design. |
| Multiverse dimensions | Pre-publication endpoint; 30-minute, 60-minute, close, and next-open public windows; market return versus factor model; trade price versus midpoint; after-hours allocation; liquidity proxy; overlap treatment; trigger-date source; extreme-return handling. All cells are fixed before outcomes and reported. |
| Multiple testing | Historical multiverse findings are exploratory. Report the full specification matrix and adjusted q-values within outcome families. Choose one confirmation specification by economic and measurement criteria before the holdout is opened, not by its historical t-statistic. |
| Confirmation safeguard | Register one primary public-arrival window, one total window, one liquidity proxy, one estimator, and one sign pattern after the exploratory multiverse is complete but before opening the untouched 2026 sample. Historical “best” specifications cannot be relabelled confirmatory. |
| Existing files and code reused | Existing EDGAR parser, CIK/CUSIP links, `crsp_daily.csv`, event-study infrastructure, H1/H2 sample construction, and acceptance-time fields. The existing data inventory records CRSP coverage through 2025 and the absence of reproducible WRDS extraction code (`/Users/austinli/Projects/blockholder_v4/research/empirics_v4/data_inventory.md:16-21`; `/Users/austinli/Projects/blockholder_v4/research/empirics_v4/data_inventory.md:71-76`; `/Users/austinli/Projects/blockholder_v4/research/empirics_v4/data_inventory.md:153-156`). |
| New code and data | TAQ query and cleaning pipeline; time-varying security-symbol crosswalk; public-arrival calendar; intraday event builder; news-overlap flags; multiverse runner; frozen holdout loader; independent reproduction package. Compustat is optional. SDC, Bloomberg, FactSet, SharkRepellent, and Activist Insight are not required. |
| Calendar time | Two blind feasibility days; if activated, at least three weeks of data engineering, one week of auditing, one week of exploratory analysis, a holdout freeze, and two independent reproduction days. |
| Acceptance test | TAQ accessible by 7 September; blind counts and variance power gate passed; linkage above 70 percent; timestamp and trigger audits passed; non-overlapping windows add to the total response within predeclared tolerance; at least 150 holdout events or an MDE that meets the gate. |
| Kill criterion | Kill by **11 September 2026** if TAQ access, linkage, timestamps, or blind-count power fails. Kill by **2 October 2026** if no untouched confirmation sample or no stable total-response accounting exists. |
| Fallback | Return immediately to E1. Do not run additional historical specifications in search of a publishable sign. |

### 9.3 Viewed-result locks

H1, H2, dose, stake, placebo, and BID12 outcomes have been viewed. Their registered specifications and statuses remain fixed. They may be reproduced, tabulated, or diagnosed, but not searched for significance. `SPEC.md` is the authority for estimands, decision rules, viewed-result history, and demotion rules (`/Users/austinli/Projects/blockholder_v4/research/empirics_v4/SPEC.md:55-116`; `/Users/austinli/Projects/blockholder_v4/research/empirics_v4/SPEC.md:1333-1349`; `/Users/austinli/Projects/blockholder_v4/research/empirics_v4/SPEC.md:1459-1518`).

The corroboration audit reaches the same practical conclusion: H1 does not establish the pooled slope; H2's principal coefficient is roughly one seven-hundredth of its MDE; the matched design is not estimated; and the most the existing evidence can honestly provide is labelled estimates, intervals, MDEs, and failures (`/Users/austinli/Projects/blockholder_v4/research/empirics_v4/theory_corroboration_2026-08-31.md:133-179`; `/Users/austinli/Projects/blockholder_v4/research/empirics_v4/theory_corroboration_2026-08-31.md:228-266`; `/Users/austinli/Projects/blockholder_v4/research/empirics_v4/theory_corroboration_2026-08-31.md:285-312`).

## 10. Two empirical-standard verdicts

### 10.1 Standard A: a corrected descriptive filing-timing result is admissible

**Verdict: `GO`, conditional.**

**Strongest permissible headline:** “In pre-fixed initial-13D samples, the realised filing-delay distribution compressed sharply under the five-business-day regime; the result is independently reproducible and remains directionally present in a prospectively frozen 2026 extension if that extension clears its power gate.”

**Weakest link:** unresolved trigger dates and parser selection. The preliminary effect is large, but the present 399/365 retained sample leaves a material unresolved denominator. The historical result has also been viewed, so it must be labelled descriptive rather than retroactively confirmatory.

**Minimum work needed:** freeze the protocol; construct a unique-accession denominator; resolve or classify missing trigger dates; apply a contemporaneous business-day calendar; conduct the blind manual audit; create a new immutable result artifact; reproduce it in a clean environment; and freeze the 2026 extension before its delay outcomes are parsed.

**Fallback date:** **25 September 2026.** If E1 has not passed its denominator, audit, and reproduction gates by then, drop the empirical headline. Under the mandate's requirement of one reproducible empirical result, the December paper becomes `NO-GO` unless E2 has already passed all of its feasibility gates.

### 10.2 Standard B: a credible causal estimate is required

**Verdict: `NO-GO`.**

**Strongest permissible headline now:** none. The current timing comparison is descriptive. The matched control-outcome design is `NOT ESTIMATED`; its pre-trend p-value of 0.0214 independently prohibits causal language under the registered rule (`/Users/austinli/Projects/blockholder_v4/empirics/output/did_diagnostics.json:3-4`; `/Users/austinli/Projects/blockholder_v4/empirics/output/did_diagnostics.json:40-45`).

**Weakest link:** there is no credible untouched counterfactual for a model-aligned outcome. The 13G group differs structurally from 13D filers and its deadlines also changed on a different schedule. A narrow regression discontinuity in calendar time faces October 2023 anticipation and the simultaneous EDGAR cut-off change. The downstream takeover sample is underpowered and fails balance.

**Minimum work that would clear the standard:** a pre-registered independent design with a genuinely unaffected comparison and an untouched outcome sample. The most defensible route would be a second legal-clock change in another jurisdiction or period, with harmonised ownership filings, a common public-arrival measure, matched control outcomes, event-time pre-trends, parser and audit gates, and independent replication. A US-only specification on already viewed 2022–2025 outcomes cannot be transformed into confirmation by adding fixed effects.

**December feasibility:** no. Building a cross-jurisdiction filing and control-outcome panel, validating legal comparability, and obtaining adequate power cannot credibly be completed by 18 December without displacing the paper itself.

**Fallback date:** **11 September 2026.** Unless an already accessible, untouched, adequately powered legal-shock dataset is identified by then, causal work leaves the December critical path and Standard A becomes the binding plan.

## 11. Manuscript and presentation architecture

### 11.1 Manuscript architecture

A disciplined main paper should be approximately 35–45 pages before the online appendix. Exact length is secondary to the allocation of attention.

| Section | Main content | Reader burden limit |
|---|---|---|
| 1. Introduction | Institution, question, result hierarchy, one figure, and explicit limits | No theorem notation beyond threshold and window |
| 2. Institutional environment | Five-percent trigger, 13D/13G purpose, legal clock, EDGAR public arrival, and control timing | Legal detail only where it changes measurement or timing |
| 3. Model | Actors, information, plan, stake path, prices, filing, bidder, and premium | One page of primitives and one timing figure before formal notation |
| 4. Information partition | D1, L1, L2, and the endpoint-versus-return example | Three propositions; no proof-condition inventory in running prose |
| 5. Policy margins | Threshold result, window if-and-only-if, one numerical illustration, and limitations | One theorem and one compact calibration table |
| 6. Filing-delay evidence | Protocol, sample, main result, empirical CDF, denominator and audit | One empirical headline; no return or takeover detour |
| 7. Implications | What law changes, what remains unsigned, and what evidence does not establish | Explicit non-claims |

The appendix should contain the complete existence proof; L3/L4/T1/C1 derivations; assumption satisfiability and failure cases; numerical audit outputs; parser and manual-audit documentation; the H1/H2/dose/stake/BID12 truth ledger; legal-calendar details; and the literature search log.

### 11.2 Abstract architecture

The abstract should contain five moves:

1. State the institutional question.
2. Explain the threshold-plus-clock partition mechanism.
3. State the flagged-endpoint result and the threshold/window distinction.
4. Report the corrected descriptive filing-delay fact.
5. State the limits: no unconditional window sign and no causal takeover estimate.

The current abstract mixes a numerical sign, an old seeded fact, and prospective return/control designs (`/Users/austinli/Projects/blockholder_v4_theory/draft_v3.tex:72-82`). It should be rewritten after E1 clears rather than patched sentence by sentence.

### 11.3 Core presentation

The existing presentation infrastructure is designed for a roughly 20–25 minute audience and already records audience calibration (`/Users/austinli/Projects/blockholder_v4/pres/README.md:3-18`; `/Users/austinli/Projects/blockholder_v4/pres/README.md:37-73`). The December deck should use 12–14 core slides:

1. Question and one-sentence verdict.
2. Schedule 13D clock and February 2024 change.
3. Anchor two-panel figure.
4. Actors and timing.
5. Flagged versus pooled information states.
6. D1 and L1.
7. L2 with the 110/100/107 example.
8. Threshold versus window.
9. T1: what is signed and unsigned.
10. One calibration slide with labels and failure conditions.
11. Filing-delay protocol and audit.
12. Filing-delay result.
13. Contribution relative to closest papers.
14. Limits and the next empirical test.

Back-up slides should contain P1 assumptions, the `A(tau)` failure, C1, H1/H2 intervals, the BID12 design failure, legal details, and robustness. Target-journal names should not appear in the manuscript or presentation.

### 11.4 Presentation quality test

The paper is ready to present only if a listener can answer four questions after the first ten minutes: What legal clock changed? What information is pooled or flagged? Why is an invariant flagged endpoint not an invariant filing return? What does the empirical result establish and not establish? If any answer requires the proof appendix, the main exposition has failed.

## 12. Dated December execution plan

### 12.1 Week-by-week critical path

| Week | Output | Dependency | Acceptance check | Estimated effort | Decision or kill gate | Fallback |
|---|---|---|---|---:|---|---|
| **1–4 Sep** | Author decision memo; immutable evidence manifest; E1 protocol; current-result status ledger | This review and existing artifacts | Protocol fixes sample, outcomes, legal calendar, deduplication, audit, viewed labels, inference, and acceptance tests before a new adopted rerun | 2 author days | Winner and Standard A adopted by 4 Sep | Stop parallel agendas and use Position 1 |
| **7–11 Sep** | Parser and denominator diagnostic; E2 access-only feasibility; causal-data inventory | EDGAR raw files; TAQ access check; no outcome inspection | Unique-accession universe reconciled; blind E2 counts, linkage rates, and pre-period variances only | 4 days | Kill E2 if TAQ, linkage, timestamp, or power input fails; kill causal route absent untouched shock | Put all resources into E1 |
| **14–18 Sep** | Historical E1 near-census build; unresolved-case queue; first 50 blind audits | Parser repair and protocol | At least 90 percent resolved progress; no regime-specific error signal; source hashes preserved | 5 days plus coding | Escalate to full manual recovery if projected final coverage is below 95 percent | Narrow only under a predeclared rule; otherwise no headline |
| **21–25 Sep** | Final E1 artifact; 100-case blind audit; independent clean reproduction | Completed historical resolution | At least 95 percent resolved in each window; no more than two material audit errors; clean rerun exactly matches | 5 author days plus 2 reader days | **Binding E1 GO/NO-GO; last safe theory reopening date** | If fail, December is NO-GO unless E2 has already cleared every gate |
| **28 Sep–2 Oct** | Rewrite introduction, institution, model timing, D1/L1/L2; build anchor figure | E1 numbers frozen | Endpoint-versus-return bridge independently audited; figure tells institution, partition, and result | 5 days | Final E2 kill if no holdout or stable total-return accounting | E1-only winner |
| **5–9 Oct** | Compress T1 section; create calibration table; draft empirical section | Frozen theory authority and E1 artifact | Every result carries authority label and assumptions; no stronger causal or theorem language | 5 days | **Last safe date to change the empirical headline** | Keep E1; later additions go to appendix only |
| **12–16 Oct** | Reorganise technical appendix; build H1/H2/BID12 honesty appendix | Existing proofs and artifacts | All viewed results and design failures disclosed with intervals, MDEs, and gates | 4 days | No new specification search after 16 Oct | Reproduction and wording repair only |
| **19–23 Oct** | Complete integrated manuscript version 1 | Main sections, appendix, figures, tables | Manuscript compiles; core has no placeholders; logic chain is continuous | 5 days | Coherence review removes any section that does not support the chain | Narrow rather than add |
| **26–30 Oct** | Independent theory-claim audit and empirical reproduction package | Complete version 1 | Theory prose matches `MODEL_CARD.md`; E1 table matches artifact; links and hashes validate | 3 author days plus 3 reader days | Any label, theorem, or result mismatch blocks circulation | Repair only; no redesign |
| **2–6 Nov** | Supervisor draft version 2 | Audit fixes | Abstract, introduction, anchor figure, main result, and appendix are complete enough to verify | 5 days | Supervisor comments may narrow claims but do not reopen the headline without a fatal finding | Preserve Position 1 |
| **9–13 Nov** | Revision version 3; seminar narrative; objection memo | Supervisor comments | Paper can be explained in 20 minutes without relying on technical appendix | 5 days | Reject requests requiring a new causal design unless the claim is explicitly demoted | Add limitation, not ad hoc test |
| **16–20 Nov** | Core slide deck; freeze prospective 2026 extension at 20 Nov | Manuscript version 3 and unchanged E1 protocol | Slides compile; 2026 sample is frozen before outcomes are opened | 4 days | Validation is robustness, not a condition for the historical result | Report count and power transparently |
| **23–27 Nov** | Final tables, appendix, references, and 2026 persistence result if powered | Frozen extension and reproduction environment | Independent check; all registered variants shown; underpowered result labelled | 5 days | No suppression or redefinition if validation is weak | Keep historical descriptive headline |
| **30 Nov–4 Dec** | Circulation draft, online appendix, code manifest, and deck | Full package | Files open and compile on a second machine; table, figure, and citation cross-references pass | 4 days | **Circulate on 4 December** | Remove nonessential material rather than delay |
| **7–11 Dec** | Rehearsals, final objection responses, supervisor corrections | Circulated draft | Three timed rehearsals; concise answers to five hard questions | 4 days | No new empirical headline | Wording and slide changes only |
| **14–18 Dec** | Frozen departmental paper and presentation | Final quality assurance | Hashes, compilation, references, authority labels, and numbers pass; final freeze 14 Dec | 3 days | **Departmental review 18 December** | Emergency factual correction only |

### 12.2 First action, dependencies, and hard dates

**First action:** before rerunning or extending the filing-delay calculation, create and commit an immutable evidence manifest containing the current result labels and hashes, then register E1. The existing integration memo independently identifies preservation of hashes and labels as the first operational step (`/Users/austinli/Projects/blockholder_v4/research/empirics_v4/2026-08-31_theory_empirics_december_integration.md:146-151`).

**Single critical path:** E1 protocol -> denominator and parser recovery -> manual audit -> immutable result artifact -> independent reproduction -> main empirical table and CDF -> integrated manuscript -> circulation -> presentation.

**Parallel work:** theory exposition and the anchor-figure design can begin immediately. Literature and bibliography verification and appendix reorganisation can proceed while E1 is audited. E2 receives at most its blind feasibility check through 11 September.

**Last safe date for changing the empirical headline:** **9 October 2026.**  
**Last safe date for reopening theory:** **25 September 2026.**  
**Circulation date:** **4 December 2026.**  
**Final freeze date:** **14 December 2026.**

The plan does not assume that E2 succeeds, that the 2026 extension is powered, or that every missing trigger is recoverable. The only path assumed to succeed is the one with an explicit 25 September kill gate.

## 13. Journal-ceiling verdicts

Journal names in this section are diagnostic benchmarks only. They should not appear as targets in the manuscript or presentation.

### 13.1 December departmental paper

**Verdict: `GO`, conditional.**

**Single strongest feature:** a distinctive legal-clock partition with a rigorously labelled theoretical record and a clear separation between threshold and window policy margins.

**Single weakest link:** the empirical result establishes implementation of the legal clock but does not test the liquidity or corporate-control mechanism.

**Missing ingredient:** a corrected, independently reproduced filing-delay artifact and a substantially cleaner public exposition.

**Feasible before December:** yes, if E1 clears by 25 September and the theory is not reopened after that date.

### 13.2 Strongest plausible journal immediately below JF/JFE/RFS

Use the *Journal of Financial and Quantitative Analysis* as the principal benchmark, with the *Review of Finance* as a close alternative.

**Verdict: `POSSIBLE AFTER SPECIFIED WORK`.**

**Single strongest feature:** the statutory clock is a defensible and economically meaningful addition to the activism, market-microstructure, and corporate-control literatures.

**Single weakest link:** model-to-measure alignment. A descriptive timing fact plus a conditional theory is unlikely to clear a near-top field-journal bar on its own, especially after Trivedi's empirical entry and the dense 2026 blockholder literature.

**Missing contribution or evidence:** either a model-aligned, independently confirmed price-discovery or control-outcome result, or a substantially stronger theoretical window result with disciplined calibration and policy content. The preferable upgrade is the timestamp design because it repairs the observable bridge rather than adding more proof machinery.

**Feasible before December:** no as a submission-quality package. It is feasible after December only if E2 passes access, linkage, power, and holdout gates.

### 13.3 JF/JFE/RFS standard

**Verdict: `NO-GO` at the current stage.**

**Single strongest feature:** an unusual integration of securities law, market microstructure, and corporate control.

**Single weakest link:** the headline policy shock changes exactly the margin for which the theory has no unconditional sign, and no empirical result identifies the model's mechanism or control outcome.

**Missing contribution or evidence:** a broadly robust theorem or structural quantitative result on the legal window, plus compelling model-aligned causal or quasi-experimental evidence that the legal clock changes a first-order corporate-finance outcome rather than only filing compliance.

**Feasible before December:** no. Pursuing that standard now would turn a deliverable departmental paper into a moonshot and reduce the probability of a coherent December result.

## 14. Referee objections, risks, and kill criteria

### 14.1 Risk register

| Risk | Probability | Damage | Mitigation | Kill or fallback |
|---|---:|---:|---|---|
| Filing-delay evidence appears adjacent rather than integrated | High | High | Define the empirical claim as “the clock moved”; use the timeline/CDF anchor; never call it validation of L2 or T1 | If supervisors require a mechanism test, pivot only if E2 already passed all gates; otherwise narrow the title and accept the ceiling |
| Filing-delay denominator is selected by parser success | Medium-high | High | Near-census manual resolution, unresolved-rate table, blind audit, and no CRSP inclusion restriction | Kill headline on 25 Sep if resolution is below 95 percent or differential missingness persists |
| L2 separation assumptions look engineered | High | Medium-high | Put exact assumptions in a box, provide failure cases, use “pooled for the price-setting public market,” and avoid field-universality claims | Reframe L2 as a benchmark result rather than a universal description |
| Window theorem does not sign the reform | Certain | Medium | Make the non-sign economically substantive: weight and composition compete | Do not reopen solely to force a sign; retain labelled numerical illustration |
| P1 applicability problems undermine confidence | Medium | Medium-high | State conditional existence once; report A3/A6 failures and four unresolved nodes in appendix | If a displayed calibration relies on a failed antecedent, remove the calibration claim rather than weaken labels |
| Trivedi occupies legal-schedule framing | High | High | Obtain latest paper; position on bidder/control equilibrium and threshold/window separation | If latest version contains the same control partition, reassess winner before 11 Sep |
| Burkart–Lee–Voss or Celentano–Levine crowd generic activism/control claims | High | High | Make legal clock essential and avoid generic activism-takeover novelty | Remove broad title and abstract language |
| Existing return estimates invite “null effect” language | High | Medium | Print coefficient, interval, MDE, and object mismatch every time | Any “no effect” sentence fails the claim audit |
| BID12 outcome coverage remains questionable | High | High for causal version; low for winner | Appendix only; preserve base-rate failure and `NOT ESTIMATED` label | No new BID12 headline work on December path |
| Structured XML and changing guidance affect parsing | Medium | High | Versioned parser, contemporaneous calendar, manual audit, and prospective extension | Restrict to validated routes with an explicit population; never silently drop failures |
| Corporate control is not load-bearing for the empirical fact | Medium-high | High | Demonstrate that bidder and premium change the theory's economic object | If the control block is removable, retitle to market inference and move control to an extension |
| E2 becomes a specification search | Medium | High | Blind feasibility only; predefine multiverse; report all cells; confirm only on untouched data | Kill immediately if historical t-statistics affect the confirmation design |

### 14.2 Five non-negotiable kill criteria

1. No filing-delay headline if the denominator-resolution or blind-audit gate fails on 25 September.
2. No causal language from a before-after timing comparison.
3. No statement that `JUMP` or an observed filing CAR is L2's invariant flagged object.
4. No promotion of a `NUMERICAL`, conditional, `ESTIMATED`, or `NOT ESTIMATED` result through prose.
5. No post-view specification search on H1, H2, dose, stake, placebo, or BID12.

### 14.3 Fallback

The fallback is not another menu of partially developed tests. It is the same legal-clock paper with a narrower empirical role: a fully audited implementation fact and an appendix of failed or uninformative mechanism tests. If the implementation fact fails its own gate, the December package is `NO-GO` under the mandate because it lacks a reproducible empirical result. Position 2 is a valid pivot only if its access, linkage, power, timestamp, and untouched-holdout gates have already passed; it is not a last-minute rescue.

## 15. Evidence ledger and immediate next decision

### 15.1 Five read-first authorities

1. **Current integration hypothesis:** `/Users/austinli/Projects/blockholder_v4/research/empirics_v4/2026-08-31_theory_empirics_december_integration.md:5-7`, `:29-41`, `:67-77`, `:132-151`, and `:154-231`.
2. **Live December manuscript:** `/Users/austinli/Projects/blockholder_v4_theory/draft_v3.tex:63-82`, `:730-774`, `:860-901`, `:945-1013`, `:1021-1046`, `:1118-1159`, `:1232-1253`, and `:1273-1303`.
3. **Frozen theory authority:** `/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/MODEL_CARD.md:141-158`, `:654-670`, `:675-682`, and `:710-750`.
4. **Registered empirical specification and locks:** `/Users/austinli/Projects/blockholder_v4/research/empirics_v4/SPEC.md:55-116`, `:330-414`, `:566-606`, `:1236-1251`, `:1422-1459`, and `:1517-1518`.
5. **Competitor and whitespace map:** `/Users/austinli/Projects/blockholder_v4/research/competitor_map.md:41-78`, `:109-111`, `:140-173`, `:210-239`, `:255-330`, and `:364-413`.

### 15.2 Supporting repository evidence

* Theory-to-empirics corroboration audit: `/Users/austinli/Projects/blockholder_v4/research/empirics_v4/theory_corroboration_2026-08-31.md:133-179`, `:228-266`, `:285-312`, and `:400-490`.
* Independent numerical reproduction: `/Users/austinli/Projects/blockholder_v4/quality_reports/verification/2026-08-30_estimates_verify.md:28-75` and `:128-175`.
* Matched-design failure: `/Users/austinli/Projects/blockholder_v4/research/empirics_v4/did_matching_2026-08-31.md:12-43`, `:67-91`, and `:118-179`.
* Registered-rule decisions: `/Users/austinli/Projects/blockholder_v4/research/empirics_v4/decisions_2026-08-31.md:6-18`, `:42-55`, and `:68-147`.
* Numerical window handoff: `/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/HANDOFF_sign.md:186-228`, `:251-263`, and `:343`.
* Presentation architecture: `/Users/austinli/Projects/blockholder_v4/pres/README.md:3-18` and `:37-73`.

### 15.3 Immutable artifact hashes recorded in this review

| Artifact | Authority status | SHA-256 |
|---|---|---|
| `empirics/output/h1_estimate.json` | `ESTIMATED` | `c813b6580dd717de4e7e54f0adb48d790222e175f27b5f5b15e99bef6fb469d2` |
| `empirics/output/h2_estimate.json` | `ESTIMATED` | `b639b78233c8074808314c4411a6ae769006f3be185c07199f74ff0b89731deb` |
| `empirics/output/did_estimate.json` | `NOT ESTIMATED` | `1f7e430aa91ac28ca6e40614443269a6a36cc2f7ccc89c717c0ad1aba54af3f3` |
| `empirics/output/did_diagnostics.json` | `BLOCKED` | `90a0efc93256f8f369505c313a5670104ffa70107f7221f8385e79faf209e3c7` |
| `empirics/output/bid12_gates.json` | `all_passed=false` | `d8e73aa5b9bf178f7eb37151203090950c5e54cbe239612fe0a3b50a4c149dad` |
| `empirics/output/reparse_counts.json` | Realised funnel | `49c3c077fd2ee8040404aa6b26f5fcb86a8372681b2ec0b13454387806f3d617` |

### 15.4 Online evidence ledger

All links below were checked or searched on **31 August 2026**:

* [SEC final-rule page](https://www.sec.gov/rules-regulations/2023/10/33-11180)
* [SEC press release 2023-219](https://www.sec.gov/newsroom/press-releases/2023-219)
* [SEC EDGAR 24.0.2 announcement](https://www.sec.gov/filergroup/announcements-old/edgar-release-24-0-2)
* [Current SEC 13D/13G interpretations](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/exchange-act-sections-13d-13g-regulation-13d-g-beneficial-ownership-reporting)
* [Trivedi research page](https://www.avaneendratrivedi.com/research)
* [Burkart–Lee–Voss LSE record](https://researchonline.lse.ac.uk/129506/)
* [Burkart–Lee–Voss ECGI record](https://www.ecgi.global/publications/working-papers/the-evolution-of-the-market-for-corporate-control)
* [Celentano–Levine ECGI record](https://www.ecgi.global/shareholder-activism-takeovers-and-managerial-discipline)
* [Oliver Levine research page](https://oliverlevine.com/)
* [Cetemen et al., Journal of Finance](https://onlinelibrary.wiley.com/doi/full/10.1111/jofi.70033)
* [Back et al., Econometrica](https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA14917)
* [Marinovic–Varas, RAND Journal of Economics](https://onlinelibrary.wiley.com/doi/10.1111/1756-2171.70040)
* [Choi et al., SSRN](https://doi.org/10.2139/ssrn.5317851)
* [Zeng, Review of Accounting Studies](https://ideas.repec.org/a/spr/reaccs/v31y2026i2d10.1007_s11142-026-09958-z.html)
* [Gryglewicz–Mayer–Morellec, CEPR](https://cepr.org/publications/dp21226)
* [Potential Activism, SSRN](https://doi.org/10.2139/ssrn.5076900)
* [Albuquerque–Fos–Schroth, Journal of Financial Economics](https://www.sciencedirect.com/science/article/pii/S0304405X21003950)

### 15.5 Immediate decision

**Recommendation:** approve Position 1 now. Authorise only E1 as the December empirical headline. Preserve H1, H2, dose, stake, placebo, and BID12 exactly as viewed; place them in the appendix with their intervals, MDEs, and gate failures. Allow E2 only a blind two-day feasibility check through 11 September. Do not reopen the frozen theory unless a genuine logical error in D1, L1, L2, or T1 is found.

The first concrete action on 1 September is to write the E1 protocol and immutable evidence manifest **before** rerunning or extending the filing-delay calculation. The binding decision is mechanical: if E1 clears on 25 September, proceed with the integrated legal-clock paper; if it fails, the December deliverable is `NO-GO` unless the runner-up has already passed every feasibility gate.
