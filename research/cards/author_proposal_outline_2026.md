# Li (2026) — "Five Business Days: Disclosure Deadlines, Activist Stakes, and Takeover Gains"

**Venue / status:** Unpublished research proposal (the author's own), dated August 2026 (`proposal/outline.tex:19`). Accompanied by a private "Research Execution Plan" (`proposal/execution_plan.tex:14-17`). Not a paper; a proposal + workplan. No results estimated.
**Full text from:** local LaTeX source under `/Users/austinli/Projects/blockholder_v4/proposal/` — `outline.tex` (37 lines), `execution_plan.tex` (27), `outline.bib` (310), and `sections/{abstract,framing,model,empirics,lit,conclusion,technical_appendix,workplan}.tex` (~9,060 words of source). · **Reader:** opus · **Read:** full text of every file, all lines.
**Page-numbering convention:** the PDFs (`outline.pdf`, `execution_plan.pdf`) were not opened; this card cites **`file:line` in the LaTeX source** instead of printed pages, per the ticket. Quotes are verbatim from the source with soft line-wraps joined by a single space and LaTeX markup (`\parencite{...}`, `\textcite{...}`, `~`, `$...$`) left in place exactly as written.
**Type:** proposal (theory sketch + empirical design + workplan)   **Role for us:** competitor (the author's own side proposal; `CONTEXT.md` lists "the author's own `proposal/` outline" in the competitor set)

---

## 1. Question

Did the SEC's February 2024 acceleration of the initial Schedule 13D filing deadline — ten calendar days to five business days, effective 2024-02-05 — change activist behaviour, and where in event time do activist-related takeover gains show up? Three sub-questions (`sections/framing.tex:15-21`): (i) did campaign entry or target composition change more for targets where the deadline binds harder; (ii) conditional on a campaign, did the stake at filing and the use of cash-settled derivatives respond; (iii) do activist-related takeover gains appear at filing, in the pre-bid run-up, or in the announced bid markup. The stated contribution is "a realised evaluation of the February 2024 Schedule~13D acceleration using predetermined variation in required trading days" (`sections/framing.tex:78-79`).

The proposal is explicitly *not* claiming the activist-as-intermediary mechanism or the capitalisation interpretation of conditional premia — those are imported from Corum–Levit / Burkart–Lee and Celentano–Levine and "motivate the empirical tests" (`sections/framing.tex:86-88`).

## 2. Model / data and method

### Model sketch (`sections/model.tex`, appendix `sections/technical_appendix.tex`)

Partial equilibrium, one privately informed risk-neutral activist, no Kyle-style market-maker inference, no equilibrium partition.

- **Primitives** (`model.tex:25-38`): target *i* with shares outstanding `S_out,i` and liquidity `L_i`; activist privately observes opportunity `θ ≥ 0` at `t_0`; builds an unconstrained pre-trigger toehold and crosses 5% at `t_1`; discount `δ ∈ (0,1)`. The statutory clock starts only at the crossing, so the pre-trigger phase is unconstrained by the deadline.
- **The distinctive margin** is time, not stake size: the activist may add an undisclosed increment `Δx` over at most `d` business days; filing stake `x = 0.05 + Δx`; pre-reform `d ≈ 7` business days, post-reform `d = 5` (`model.tex:46-50`).
- **Accumulation cost** (`model.tex:79-94`, derived at `technical_appendix.tex:5-20`): linear price impact `λ_L(L)`, per-day excess cost `(λ_L/2)r²`, constant rate optimal by convexity, so `C(x;d,L) = (λ_L/2)·x²/d`, with `C_x > 0`, `C_xx > 0`, `C_xd = −λ_L x/d² < 0`, and exact horizon scaling `C(x; κd, L) = κ⁻¹C(x;d,L)`. Moving 7 → 5 business days raises the quadratic cost of a fixed increment by `7/5 = 1.4` (`model.tex:99-101`).
- **Exposure measure** (`framing.tex:23-37`, `model.tex:124-141`): a daily participation cap `φ·ADV` gives `Δx̄_i(d) = φ·ADV_i·d/S_out,i`, and **`RTD_i = 0.05·S_out,i /(φ·ADV_i)`**, so `Δx̄_i(d) = 0.05·d/RTD_i`. `ADV` measured over six months ending 60 trading days before the trigger, Amihud illiquidity as alternative.
- **Bidder entry** (`model.tex:225-278`): ex ante identical acquirers, search cost `s`, free entry, bid hazard `h(s, B^e)`. Certification (13D filing does part of the bidder's screening, lowering `s`) versus deterrence/pre-emption (disclosure capitalised into `P^F`, stronger bloc bargains harder). `d log h/de = ε_cert − ε_det`; **no sign imposed**.
- **A third, offsetting entry channel** *(added by verifier)* (`model.tex:275-278`): the reform does not move disclosure timing alone — by lowering `x*` it also lowers `B^e` and can therefore *raise* entry, so "an empirical entry response cannot be attributed entirely to certification". This is a stated identification limit on the entry margin, not just an unsigned sign.
- **Bargaining** (`model.tex:280-320`): `B = V_a + β(x)(Y − V_a)`, `β(x) = β̄·λ_app`, with `λ_app = 1 − q(1−γ)ψ` **imported wholesale** from the companion (draft_v2's D7 tender game); the tender game is deliberately not reproduced. `λ_app` jumps up when the bloc crosses the blocking threshold `1 − τ_c`.
- **Gain accounting** (`model.tex:322-374`): identity `G_tot = log(B/P⁰) = G_fil + G_run + G_mkp`; with `P^B = δ[ϱB + (1−ϱ)P^fail]` the measured markup is bounded below by `log(1/δ) > 0`, so "a declining markup alone has no structural interpretation" (`model.tex:352-353`). Holding `B` and `P⁰` fixed: `dG_mkp = −(dG_fil + dG_run)` — capitalisation versus value destruction.
- **Welfare** (`model.tex:376-427`): `dW/dd` decomposed into (i) entry margin, (ii) campaign-supply margin (non-negative), (iii) stake–bargaining margin. *(added by verifier)* Welfare is defined **for the shareholder cohort present at trigger-minus-`k`**, because part of `G_fil` is a transfer from selling shareholders to the activist; that transfer component is reported separately (`model.tex:423-427`). The exposure design is defended as delivering the **LATE-style weights the decomposition needs** — high-`RTD` campaigns are the marginal units — rather than an ATE (`model.tex:414-421`).
- **Why only one private type** *(added by verifier)* (`model.tex:61-68`): with a two-dimensional type and the two-dimensional signal `(x, Item 4 purpose)`, "the filing generically separates types and `P^F` collapses to the full-information price, eliminating the signal noise needed elsewhere in the model". This is a **second and distinct** objection to a partition/signalling structure, separate from the pooling-and-refinement objection at `model.tex:435-438` — and it bears directly on v4's flagged-vs-pooled plan.
- **Declared scope restrictions** (`model.tex:429-462`): one private type only; the filing price is a *Bayesian update on an exogenously garbled filing*, the stake is **not** solved as an endogenous signal; `B` held independent of `P^F` to dodge a fixed point; omitted are the operational-vs-sale second type, the tender game, bidder competition, the within-window trading path, and priced cash-settled derivatives.

### Empirical design (`sections/empirics.tex`, `sections/workplan.tex`)

- **Margin used:** the **window margin only** — the Feb-2024 acceleration. The 5% threshold margin is never varied; it enters only as the level at which the clock starts and as the scale (`0.05`) inside `RTD`.
- **Control group: NONE, admitted in the first sentence of the design section.** Identification is a continuous-dose generalised DiD across 13D filers: `Y_{i,q} = α_{a(i),q} + γ_{ℓ(i),q} + β·Post_q × RTD_i + ε` (`empirics.tex:33-38`), with the *primary* estimates non-parametric across RTD bins (`empirics.tex:44-50`). Fixed effects: activist × quarter, liquidity-decile × quarter, size-decile × quarter.
- **Binary dose** `1{RTD_i > d}` is explicitly demoted: "the corresponding binary classification under the doubling calibration, not a general treatment definition" (`model.tex:201-203`), the doubling calibration being `Δx^u = 0.05`.
- **Non-US "control":** a UK DTR5 / EU Transparency Directive activist-block sample, used **only** to absorb the global M&A and interest-rate cycle, explicitly **not** as a legal-threshold comparison (`empirics.tex:179-182`, `workplan.tex:208-211`).
- **Unaffected-price anchor** *(added by verifier)*: `P⁰` is measured a fixed `k` trading days before the **trigger** (not the filing), `k = 60` in both reform periods with robustness at 30 and 120 — chosen so the treatment cannot move the starting point of the decomposition (`model.tex:40-44`, `empirics.tex:190-193`).
- **Inference battery** (`workplan.tex:199-217`): ≥500 placebo reform dates 2015–2023 with full re-estimation; ≥500 permutations of RTD across activists; quarterly exposure-bin event studies from 2019 plus a joint pre-trend test (failure blocks causal interpretation); MDEs pre-registered off SEC Tables 3, 5, 6 before looking at estimates.
- **Confounds handled:** anticipation (proposal 2022-03-10, reopened 2023-04-28, adopted 2023-10-10; Oct 2023–Feb 2024 excluded from the pre-period, `empirics.tex:58-64`); bundled rule changes (13D/A → 2 business days, 13G restructuring, XML from 2024-12-18; the amendment rule mechanically changes post-filing accumulation so that outcome is dropped, `empirics.tex:66-79`); 13G→13D switching near 5% as a diagnostic.
- **Data:** EDGAR 13D/13D-A enumeration (core sample 2022–2026, SEC's published 2011–2021 tables as the pre-period benchmark); Item 5(c) transaction tables; Item 4 purpose codebook (target: 95% blinded agreement on 200 filings); CRSP/WRDS for ADV, Amihud and returns — **status "unconfirmed"**; an M&A outcomes source — **status "none"**, Bloomberg or hand-collection from Forms 8-K and DEFM14A (`workplan.tex:92-123`). Trigger-date parser at parse rate 0.64–0.68. An initial 300-filing sample already exists.
- **Timeline:** March 2027 milestone presentation, full paper summer 2027, "the autumn job market" (`workplan.tex:25-28`); publication targets RFS-or-above on a detectable response, JCF/RF on a precise null (`workplan.tex:287-292`).

### Pre-committed interpretation of results *(section added by verifier — the card omitted `sections/conclusion.tex` entirely)*

`conclusion.tex` (50 lines) commits, before any estimate, to a 2×2 reading of the two primary behavioural margins (entry/composition × Item 6 derivative use), `conclusion.tex:9-28`. Three points matter for v4:

- **The proposal expects a null.** "No response on either margin is the modal ex ante outcome given the SEC's compliance statistics and would provide a policy null bounded by the reported confidence intervals and minimum detectable effects" (`conclusion.tex:36-38`).
- **It reserves a fallback identity.** "An increase in derivative use without a campaign response would identify the decision not to adopt proposed Rule~13d-3(e), rather than the headline deadline change, as the operative policy margin" (`conclusion.tex:33-36`). So the derivative-non-adoption lever is claimed as a *second* paper-saving reading, not only as background.
- **It pre-disclaims the premium object.** "A lower markup is not by itself evidence of a lower total gain" (`conclusion.tex:47-48`) — consistent with the demotion in §5, and it means the proposal will not be caught claiming a premium result.

## 3. Results — with honesty labels

**No empirical result is estimated anywhere in the proposal.** The only numbers from the author's own data are pipeline diagnostics. Analytical content is a single proposition plus algebraic identities.

| # | Result (one line) | Label | Where (`file:line`) |
|---|---|---|---|
| R1 | Quadratic accumulation cost `C(x;d,L)=(λ_L/2)x²/d` with `C_x>0, C_xx>0, C_xd<0` and exact `1/d` homogeneity; constant daily rate optimal | PROVED | `model.tex:79-94`; derivation `technical_appendix.tex:5-20` |
| R2 | Deadline does not constrain reaching the 5% threshold (clock starts at crossing); it caps only the post-threshold increment; maximum filing stake `0.05(1 + d/RTD_i)` | PROVED (one-line algebra inside the proposition; not separately derived) | `model.tex:143-163`, Prop. "Deadline exposure and stake formation" |
| R3 | The constrained set `{i : RTD_i > 0.05d/Δx^u}` expands in the set-inclusion sense as `d` falls; equals `{i : RTD_i > d}` under the doubling calibration `Δx^u = 0.05` | PROVED | `model.tex:165-178` |
| R4 | Shadow value of the window on the constrained set increases with `RTD_i` | ASSERTED (stated inside the proposition without derivation; holds only if `λ_L` is held fixed across `i` — see §5) | `model.tex:170-175` |
| R5 | Interior comparative static `dΔx*/dd = −(b_xd − C_xd)/(b_xx − C_xx) > 0` **iff** `b_xd > C_xd = −λ_LΔx*/d²` (the model's single-crossing restriction) | PROVED, but **conditional** — `b(·,·)` is never given a functional form, so the condition is untested | `model.tex:180-189`, `technical_appendix.tex:22-37` |
| R6 | At the constrained corner `dΔx*_i/dd = φ·ADV_i/S_out,i > 0` with no further restriction | PROVED | `model.tex:191-197`, `technical_appendix.tex:31-37` |
| R7 | Reform dose is a monotone function of `RTD_i/d`; the continuous dose is the primary model object | PROVED (immediate from R2–R3) | `model.tex:199-203` |
| R8 | `G_tot = G_fil + G_run + G_mkp` | PROVED (accounting identity, stated as such) | `model.tex:327-336` |
| R9 | Measured markup bounded below: `G_mkp ≥ log(1/δ) > 0`, so a fully anticipated deal still shows a positive markup | PROVED (under the stated `P^B = δ[ϱB+(1−ϱ)P^fail]` assumption) | `model.tex:338-353` |
| R10 | Invariance restriction `dG_mkp = −(dG_fil + dG_run)` holding `B, P⁰` fixed; distinguishes capitalisation from value destruction | PROVED (algebra), but the paper labels it "a measurement restriction rather than the paper's main theoretical claim" | `model.tex:355-364`, `model.tex:446-448` |
| R11 | Bidder entry: `d log h/de = ε_cert − ε_det`; earlier disclosure raises the bid hazard iff `ε_cert > ε_det` — **no sign imposed** | ASSERTED (definitional; `h`, `s`, `B^e` never derived from primitives) | `model.tex:246-266` |
| R12 | Appropriability `λ_app = 1 − q(1−γ)ψ`, rising discontinuously at the blocking threshold `1−τ_c` | ASSERTED here (explicitly **imported** from the companion's tender-game appendix; "The tender game itself is not reproduced") | `model.tex:296-320` |
| R13 | Welfare decomposition `dW/dd` into entry, campaign-supply and stake-bargaining margins; campaign-supply margin non-negative | ASSERTED (stated; envelope argument only sketched in prose, no derivation) | `model.tex:376-421` |
| E1 | Own pipeline: post-reform median trigger-to-filing delay 5.0 business days (2024Q3–Q4) vs 7.0 (2023Q2–Q3) | ESTIMATED (descriptive, no SE; the proposal itself calls delay compression mechanical and non-behavioural) | `workplan.tex:176-179`, `empirics.tex:195-196` |
| E2 | Own pipeline: 75.6% of post-reform filings within 5 business days vs 35.7% before — **but** that post-reform figure silently trims delays >60 business days; untrimmed it is 68/96 = 70.8% | ESTIMATED (descriptive; the proposal flags its own trimming as undocumented and mandates the untrimmed statistic in production) | `workplan.tex:176-186` |
| E3 | Own initial 300-filing sample: 259 unique filer CIKs, 29 filers with ≥2 filings, 3 with ≥3 — kills the activist-level (leave-one-out) exposure design | ESTIMATED (counts) | `empirics.tex:99-103`, `workplan.tex:37-43` |
| P1 | Expected 2024–2026 post-reform sample ≈ 540–700 non-corporate-action campaigns | PLANNED / projection | `empirics.tex:119-120`, `workplan.tex:224-225` |
| P2 | Implied average accumulation effect "on the order of one tenth of a percentage point of shares outstanding" | ASSERTED (arithmetic on SEC tables, not estimated) | `empirics.tex:108-117` |
| P3 | Sale-intent triple interaction on bid hazard: MDE 17–31 pp on a base rate ≈17 pp, ≈3 bids in the materially exposed post-reform cell — **descriptive, CIs only** | ASSERTED (ex ante power calculation) | `empirics.tex:143-146`, `workplan.tex:225-229` |

## 4. Institutional facts used

- Feb-2024 acceleration: initial Schedule 13D deadline ten calendar days → five business days, effective 2024-02-05; "the first change to the accumulation window since 1968" (`framing.tex:4-7`, `empirics.tex:7-9`).
- The Section 13(d) clock begins only after the 5% beneficial-ownership crossing, so the pre-trigger toehold is unconstrained (`model.tex:36-38`, `model.tex:157-159`).
- The final rule **declined** to adopt proposed Rule 13d-3(e), which would have treated certain cash-settled derivatives as beneficial ownership; it clarified Item 6 derivative disclosure without expanding scope (`framing.tex:9-13`, `empirics.tex:71-72`, `lit.tex:120-122`). This is what makes derivative substitution a live margin.
- Bundled changes in Release 33-11253: 13D/A deadline to two business days; 13G deadlines restructured; structured XML filing required from 2024-12-18 (`empirics.tex:66-71`).
- Rulemaking chronology: proposed 2022-03-10, comment period reopened 2023-04-28, adopted 2023-10-10, effective four months later (`empirics.tex:58-61`).
- Feb 2025 SEC CDI Question 103.12 on when calls for a sale/restructuring, alternative director nominees, or conditional voting support make Schedule 13G unavailable (`lit.tex:121-124`; bib entry `outline.bib:303-310`).
- Pre-reform, "ten calendar days corresponded to approximately seven business days" (`model.tex:48-49`).
- Data sources: EDGAR (13D, Item 4, Item 5(c), Item 6); CRSP/WRDS (unconfirmed); Bloomberg or hand-collected 8-K/DEFM14A; UK DTR5 and EU Transparency Directive notifications (`workplan.tex:92-129`, `empirics.tex:217-227`).

## 5. Referee-facing strengths / weaknesses

**Strengths**

- Honest about the absence of a control group and says so in the first sentence of the design (Q1). It does not dress a single-date rule change as a DiD.
- The exposure measure is genuinely predetermined and price-free in construction: shares outstanding and lagged ADV, no realised stake or outcome, defined for one-time filers (`empirics.tex:13-21`, `model.tex:220-223`).
- It disqualifies its own most tempting result in advance: filing-delay compression is mechanical compliance, not behaviour (Q8), and the amendment-deadline outcome is dropped for the same reason (`empirics.tex:72-75`).
- Anti-truncation care in the gain decomposition is real: a fixed trigger-to-bid horizon, a `[-1,+1]` filing CAR as a share of total gain, a mechanical placebo that recuts pre-reform filings at five business days, and a behavioural placebo restricted to campaigns that already filed within five days (`empirics.tex:194-204`).
- It pre-computes its own power ceiling from the SEC's tables and states it as a binding interpretive constraint (Q7, P2, P3).
- It audits its own pipeline against itself and catches an undocumented trim (E2) — the kind of self-check a referee likes to see already done.

**Weaknesses / open flanks**

- **The dose is nearly collinear with its own fixed effects.** `RTD_i ∝ S_out,i/ADV_i`, and the specification includes liquidity-decile × quarter **and** size-decile × quarter fixed effects (`empirics.tex:33-53`). The identifying variation is whatever survives double-residualising `S_out/ADV` on size and liquidity deciles. The proposal promises covariate balance across exposure bins (`empirics.tex:91-94`) but never discusses this collinearity. *Reader-identified, not conceded in the text.*
- **`φ` is never calibrated.** The participation cap `φ` appears in `RTD` and in the cap `Δx̄`, but no numeric value is given anywhere. The *ranking* of targets by `RTD` is invariant to `φ`, but the binary set `{RTD_i > d}` and the "doubling calibration" are not — they are unidentified without a chosen `φ`. *Reader-identified.*
- **R4's cross-sectional monotonicity is not safe.** On the constrained set `C_x = λ_L·Δx̄_i/d = λ_L·0.05/RTD_i`. If `λ_L ∝ 1/ADV` (as the proposal states, `model.tex:74-76`) and `RTD_i ∝ S_out,i/ADV_i`, then `λ_L/RTD_i ∝ 1/S_out,i` — the marginal cost term varies with firm size, not monotonically with `RTD_i`. The shadow value therefore increases with `RTD_i` only holding `λ_L` fixed, which the cross-section does not do. *Reader-identified.*
- **Power is close to null-by-construction and the proposal admits it** (Q7): SEC tables imply ~3% of non-corporate-action campaigns (≈7/year) were materially constrained, and the implied average accumulation effect is ~0.1 pp of shares outstanding. The gate at `workplan.tex:165-169` explicitly plans for the "reposition around a well-measured policy null" branch.
- **Deliverability is gated on data that does not exist yet.** The *primary* exposure measure's denominator needs CRSP/WRDS, status "unconfirmed"; the gain decomposition needs an M&A source, status "none", 4–8 weeks by the EDGAR route; Item 5(c) extraction is 4–8+ weeks, "High" risk; the trigger parser is at 0.64–0.68 (`workplan.tex:92-123`). Without CRSP the design collapses to an EDGAR-only fallback (`workplan.tex:273-277`).
- **The theory is thin relative to the empirics and is a means, not an end.** Its stated main purpose is "to derive the target-level exposure measure `RTD_i`" (`model.tex:4-6`). One proposition, whose interior half rests on an unrestricted `b(·)`; the welfare decomposition and entry elasticities are definitions, not derivations; `λ_app` is imported rather than proved.
- **The takeover-premium object is demoted to descriptive.** Bid hazard is "Confidence intervals only" (`empirics.tex:143-146`); the capitalisation interpretation "remains a measurement restriction, not a separate contribution" (`empirics.tex:213-215`).
- **The novelty claim is false as printed** *(added by verifier)*. `lit.tex:138-141` says a search on 2 August 2026 "found no study of realised post-February-2024 Schedule~13D outcomes". Trivedi (SSRN 6866499) was posted 3 June 2026 and is exactly that study — a pre-registered DiD on the 2024-02-05 change with **13G filers as a control group** (`research/review_v3/verify_facts.md:35`). This is a referee-visible error, and it also undercuts the proposal's stronger scope claim: a treated-vs-control design on this shock does exist, so "no untreated group" (Q1) is a design *choice*, not a fact about the reform.
- **A one-claim citation caveat is carried in the text**: the Boyson–Gantchev–Shivdasani characterisation "rests on an author-posted summary rather than the primary text" (`lit.tex:111-113`).
- **`\phi` notation collision** with the companion's charter dilution is patched by renaming to `φ_c` (`model.tex:316-320`) — a small tell that the tender game and the deadline model were not built together.

## 6. What they do NOT do (scope boundary)

Declared out of scope, in the proposal's own words and structure:

- **The threshold margin.** The 5% trigger is never varied. `\textcite{ordonezcalafibernhardt2022}`'s "policy instrument is a static stake-size trigger, not the period between threshold crossing and mandatory filing" (Q10) — the proposal positions *against* the threshold margin, and its own Table `tab:position` (`lit.tex:151-173`) lists "Filing window" as the column it claims and never lists a threshold column at all. *(verifier qualifier)* The **disclosure** threshold is never a policy variable, but a **control** threshold is: `λ_app` "rises discontinuously when the bloc crosses the blocking threshold `1−τ_c`. This produces a stake-size threshold prediction linked directly to the deadline through `x`" (`model.tex:311-314`), with an empirical discontinuity check at 5% (`empirics.tex:211-213`).
- **The stake as an endogenous signal / the partition.** "The activist's stake is not solved as an endogenous signal" (Q4); the filing price is a Bayesian update on an *exogenously garbled* filing; "Endogenising the filing price is left for separate work" (Q5). There is no flagged-vs-pooled information structure, no equilibrium refinement, no uniqueness result. *(added by verifier)* Two *separate* arguments are given for why: (a) without a refinement and a uniqueness result `P^F` is not a well-defined empirical object (`model.tex:435-438`); (b) with a two-dimensional type and the two-dimensional signal `(x, purpose)`, the filing **generically separates** and `P^F` collapses to the full-information price, killing the signal noise the rest of the model needs (`model.tex:61-68`). v4 must answer (b) as well as (a).
- **The sign of the bidder-entry effect.** "The model therefore does not impose a sign on bidder entry" (Q6).
- **The tender game.** "The tender game itself is not reproduced" (`model.tex:316`; the card originally mis-pointed this to Q12, which is the novelty-search quote — *fixed by verifier*) — `λ_app` enters as an imported reduced form. **But the empirical proxy map for `λ_app`'s primitives is already claimed** (`model.tex:307-314`: fringe M&A intensity → `q`; strategic/financial acquirer mix and asset redeployability → `γ`; state and charter antitakeover provisions → charter dilution; bloc stake relative to control thresholds → `ψ`), together with "a discontinuity check around the five-per-cent ownership threshold" (`empirics.tex:211-213`). *(added by verifier)*
- **Priced derivatives.** "Cash-settled derivatives are treated in the empirical Item~6 analysis as an outside option but are not priced in the model. This omission is consequential because derivative substitution is a primary empirical margin" (Q11).
- **A second (operational vs sale) private type, bidder competition, repeated fringe entry, the within-window trading path** (`model.tex:450-455`); a deadline version of the Kyle framework is named as the right tool and then set aside (`model.tex:110-119`).
- **Any treated-vs-control identification.** "no untreated group" (Q1); the non-US block sample "will not be used as a legal-threshold comparison" (Q9).
- **Filing delay and post-filing accumulation as evidence.** "mechanical consequences of compliance and cannot establish a behavioural response" (Q8).
- **Liquidity as a comparative-static object.** Liquidity enters only twice: as the cost shifter `λ_L(L)` and as the `ADV` denominator of `RTD`. Nothing in the proposal asks how a control outcome moves *with* liquidity; liquidity deciles are in fact absorbed by fixed effects.
- **Merger-background chronologies:** "out of scope … No tooling, corpus, or design note exists; exclude from the critical path" (`workplan.tex:119-120`).

## 7. Implications for our position — what the proposal already occupies

Read against **ADR-0004** (`docs/adr/0004-identity-and-wording-constraints.md`), which states that the author's `proposal/` "is a demo that dies if v4 lands better — it does not reserve the Feb-2024 anchor." So this section is about *occupied cells*, not about a claim of priority. v4 may use the Feb-2024 acceleration; it must not land in the same cell.

### Occupied cells (do not re-enter without a reason)

| Dimension | What the proposal occupies | `file:line` |
|---|---|---|
| **Object** (primary) | Campaign entry and target composition; stake at filing and trigger-to-filing accumulation; Item 6 cash-settled-derivative language | `empirics.tex:133-138` |
| **Object** (secondary) | Filing return and pre-filing drift (CRSP-dependent) | `empirics.tex:141-142` |
| **Object** (descriptive only) | Filing delay; 6- and 12-month bid hazard; the three-way gain decomposition `G_fil / G_run / G_mkp` | `empirics.tex:139-146`, `empirics.tex:184-204` |
| **Margin** | **Window margin only** — Feb-2024, ten calendar days → five business days, entering the model as `d` in `C(x;d,L)` and as `d` in the cap `Δx̄_i(d) = 0.05d/RTD_i` | `model.tex:46-50`, `model.tex:124-138` |
| **Threshold margin** | **Not occupied as a *disclosure* margin.** 5% is fixed: clock-start and the `0.05` scale factor, never a policy variable. *(verifier)* A **control**-threshold prediction *is* occupied — `λ_app` jumps at the blocking threshold `1−τ_c`, plus a 5% discontinuity check | `model.tex:36-38`, `lit.tex:12-15`; `model.tex:311-314`, `empirics.tex:211-213` |
| **Identification** | Continuous-dose (`RTD_i × Post`) generalised DiD on the 13D filer population, **no control group**; non-parametric RTD bins primary; activist × quarter + liquidity-decile × quarter + size-decile × quarter FE; ≥500 placebo dates, ≥500 RTD permutations, 2019-onward event studies, joint pre-trend test, pre-registered MDEs | `empirics.tex:7-11`, `empirics.tex:33-53`, `workplan.tex:199-217` |
| **Theory tool** | Static deterministic accumulation problem with quadratic price impact + a corner from a participation cap; free-entry bidder cutoff; reduced-form bargaining share | `model.tex:70-320` |
| **Anchor exploitation** | 13D→13G substitution near 5% as a *diagnostic* for bundled 13G changes; UK DTR5 / EU TD as a cycle absorber only | `empirics.tex:76-79`, `empirics.tex:179-182` |
| **Institutional lever it uniquely leans on** | The SEC's *decision not to adopt* proposed Rule 13d-3(e) → derivative substitution as a behavioural margin | `framing.tex:9-13`, `empirics.tex:71-72` |

### Whitespace the proposal leaves open (v4 candidates)

1. **The threshold margin** (5% US vs 3% UK; 13D vs 13G) as a *policy variable* rather than a clock-start. Untouched, and the proposal's own lit review says Ordoñez-Calafi–Bernhardt occupy the static trigger — leaving the threshold-margin *control-outcome* question open.
2. **The partition** — flagged vs pooled as an equilibrium information structure, with the stake chosen as a signal. Explicitly excluded (Q4, Q5) and named as the reason a signalling model would not deliver a well-defined `P^F`. This is precisely the identity `CONTEXT.md` reserves for our paper ("The disclosure rule is the market's partition; this is the paper's identity").
3. **Liquidity κ as the driving comparative static on a control outcome.** The proposal has no `dPremium/dκ`-style object at all; liquidity is a nuisance absorbed by fixed effects. This is our whole driving variable.
4. **The premium wedge as a causal/theoretical object.** The proposal demotes premia to descriptive with CIs only and imports the capitalisation reading from Celentano–Levine as a measurement restriction, not a claim.
5. **The sign of the entry/deterrence trade-off.** Left unsigned (Q6) and handed to the data — a theory result that signs it under stated conditions is open ground.
6. **Disclosure attenuation** (draft_v2's T2 — that a stricter rule flattens the liquidity→control-outcome slope) is nowhere in the proposal, on either margin.
7. **The tender game / `λ_app`.** Imported here, so re-deriving or extending it is not a duplication. *(verifier caveat)* The **empirical** side is partly taken: the proposal already writes down observable proxies for `q`, `γ` and `ψ` and a 5%-threshold discontinuity check (`model.tex:307-314`, `empirics.tex:211-213`). Re-deriving the game is open; re-using that proxy map is not new.

### Costs of standing too close

- Sharing the Feb-2024 *window* margin plus a *dose* identification plus *entry / stake / derivatives* outcomes would put v4 in the same cell. If v4 uses the acceleration at all, it should differ on at least the object (a control outcome, not a stake) **and** the theory tool (a partition, not an accumulation cost).
- **Deliverability warning for the December package**: the proposal's own primary design cannot run without CRSP/WRDS ("unconfirmed"), an M&A source ("none"), and 4–8+ weeks of Item 5(c) extraction. Anything v4 inherits from it inherits that gate. The one leg that is already partly built and needs no external access is the EDGAR first stage (`empirics.tex:151-168`) — which the proposal itself says cannot establish behaviour (Q8).
- **What the proposal says about draft_v2 — the single most decision-relevant omission from the first pass** *(added by verifier)*. `workplan.tex:12-17`: "The earlier 92-page liquidity-hump draft remains a separate working paper. It is frozen after a bounded hygiene pass covering the enumerated cross-country threshold claims, the $\kappa\to1$ narrative, welfare units, and two citation attributions. A one-week Gaussian-noise falsification exercise closes the remaining question about the old model's hump and belongs in that draft's appendix, not in this project." That is the author's own defect list for the base v4 is building on: (i) the cross-country threshold claims, (ii) the `κ→1` narrative, (iii) welfare units, (iv) two citation attributions, (v) the hump's robustness to Gaussian noise. And `workplan.tex:134-139` (Gate 0) records that the advisor memo states "what is being abandoned as the job-market-paper framing" — i.e. the proposal is written as the *replacement* for the liquidity draft, which is exactly the substitution ADR-0004 says v4 must reverse.
- **Competitive clock** *(added by verifier)*: "The first-stage facts and exposure design go to SSRN when the exposure measure is fixed, with month 4--5 as the target" (`workplan.tex:279-280`). If v4 intends to use the Feb-2024 anchor, the proposal's own first-stage facts are planned to be public within roughly four to five months.
- **Wording**: this proposal names the job market and journal targets (`workplan.tex:27-28`, `workplan.tex:287-292`). ADR-0004 forbids both in v4's text, memo and slides. Do not port that prose.

## 8. Literature the proposal cites — competitor-set coverage

Full bibliography: `proposal/outline.bib` (32 entries; *corrected by verifier* — 29 was wrong). Citation counts in the section files: `sec2023modernization` 12, `celentanolevine2025` 8, `polk2024` 5, `bett2014` 5, `corumlevit2019` 4, `collindufresnefos2015` 5, `burkartlee2022` 4.

### Competitor-set members it DOES cite

| Competitor | Cite key | Where cited (`file:line`) | How characterised |
|---|---|---|---|
| **Polk, Buchheit, Riley & Stone (2024)** | `polk2024` | `framing.tex:54`, `empirics.tex:98`, `lit.tex:133-142`, `lit.tex:167` (table), `workplan.tex:37` | "the only prior study focused on the acceleration"; sample ends before the reform; no campaign-resolution, bidder-entry, takeover or premium outcomes |
| **Corum (& Levit) (2019)** | `corumlevit2019` | `model.tex:235`, `empirics.tex:213`, `lit.tex:55-63`, `lit.tex:162` (table) | supplies the bidder-discovery mechanism; disclosure step "instantaneous", governed by neither threshold nor deadline |
| **Back, Collin-Dufresne, Fos, Li & Ljungqvist (2018)** | `back2018` | `model.tex:113`, `lit.tex:32` | "The strategic benchmark"; endogenises activist trading and liquidity but is not a deadline model |
| **Johnson & Swem (2021)** | `johnsonswem2021` | `lit.tex:69`, `lit.tex:163` (table) | dynamic reputation structural model; accumulation subsumed in a lognormal campaign-cost draw; filing coincides with campaign initiation |
| **Albuquerque, Fos & Schroth (2022) [AFS]** | `albuquerquefosschroth2022` | `lit.tex:71`, `lit.tex:164` (table) | decomposes the 6.34% announcement return; "Their activism cost is a fixed scalar, and they do not study takeover premia" |
| **Celentano & Levine (2025)** | `celentanolevine2025` | `framing.tex:63`, `model.tex:16`, `model.tex:367`, `empirics.tex:215`, `lit.tex:77-83`, `lit.tex:141`, `lit.tex:165` (table), `workplan.tex:282` | the closest related work; supplies the capitalisation interpretation; "contains no disclosure timing"; publication status to be re-checked at every revision |
| **Cetemen, Cisternas, Kolb & Viswanathan (2026)** | `cetemen2026` | `lit.tex:65-68`, `lit.tex:168` (table) | leader-follower / wolf-pack in continuous time; "mention the February 2024 acceleration as institutional background, but do not make the window a choice or policy variable" |

### Competitor-set members it does NOT cite

- **Trivedi** — **absent**. No occurrence of "Trivedi" anywhere in `proposal/` (`grep -rniE "trivedi" proposal/` returns nothing), including `outline.bib`. Notable, since `CONTEXT.md` lists Trivedi among the papers already using the Feb-2024 acceleration; the proposal's novelty search (`lit.tex:138-141`, dated 2026-08-02) claims to have found no study of realised post-Feb-2024 outcomes. **Flag for the verifier: this is the proposal's most exposed novelty claim.**
- **Bishop et al.** — **absent**. No occurrence of "Bishop" anywhere in `proposal/`.

### Other papers it leans on (not in the competitor set)

`ordonezcalafibernhardt2022` (the threshold-margin antecedent, `lit.tex:10-15`), `bonettiduroormazabal2020` ("the closest empirical disclosure design", `lit.tex:17-29`), `burkartlee2022` (activist-as-intermediary, `lit.tex:48-53`), `collindufresnefos2015` / `collindufresnefos2016`, `kyle1985`, `grossmanhart1980disclosure`, `grossmanhart1980freerider`, `fishman1988`, `schwert1996`, `bett2014`, `eckbomalenkothorburn2025`, `greenwoodschor2009`, `brav2008`, `boysongantchevshivdasani2017`, `gantchev2013`, `edmansfangzur2013`, `edmansholderness2017`, `maug1998`, `kahnwinton1998`, `seccdi2025`. **Cited in `outline.bib` but never used in any section:** `hirschman1970` (`outline.bib:1-7`), `coffee1991` (`outline.bib:48-56`), `bhide1993` (`outline.bib:58-66`) — the classic liquidity-vs-control trio is in the bibliography but dropped from the text, another sign that liquidity is not this proposal's driving variable.

### Numbers the proposal quotes from other sources — for the verifier to check against the originals

| # | Number as printed in the proposal | `file:line` | Attributed to |
|---|---|---|---|
| N1 | "9{,}685 initial filings by 5{,}863 entities from 2001--2022, or 1.65 filings per entity" | `empirics.tex:98-99`; restated `workplan.tex:37-39`; "9{,}685 initial Schedule~13D filings from 2001--2022" `lit.tex:133-134` | Polk et al. (2024) |
| N2 | Polk et al. "compares investors who filed voluntarily within five days with those who waited the full ten"; outcomes are "returns and trading volume around trigger and filing dates" | `lit.tex:134-136` | Polk et al. (2024) |
| N3 | "approximately \$810 million a year in foregone shareholder value" | `framing.tex:51-53`; restated `lit.tex:130-131`, `abstract.tex:18-19` | SEC Release 33-11253 |
| N4 | "roughly 80 per cent of filers had already completed accumulation by the five-business-day deadline" | `framing.tex:55-57`; restated `model.tex:216-217`, `lit.tex:128` | SEC Release 33-11253 |
| N5 | SEC baseline: "Roughly 29 per cent of 2022 initial filings, or 41 per cent of timely filings, were made within five business days … and 97 per cent had reached 90 per cent of their reported stake" | `lit.tex:126-130` | SEC Release 33-11253 |
| N6 | SEC Table 6, constrained vs unconstrained campaigns: target market cap "\$1.8 billion rather than \$916 million"; Amihud "0.09 rather than 0.13"; prominent-activist share "43.6 rather than 29.8 per cent"; filing-window CAR "17.2 rather than 5.7 per cent"; increase in shareholder value "\$222 million rather than \$36 million" | `empirics.tex:84-91` | SEC Release 33-11253, Table 6 |
| N7 | "only 3 per cent of non-corporate-action campaigns, about seven per year, had accumulated less than 90 per cent … 1 per cent, about one per year, had accumulated less than 75 per cent" | `empirics.tex:108-112`; restated `workplan.tex:221-224` | SEC Release 33-11253 |
| N8 | "Among the 20 per cent that continued to accumulate after the deadline, only 5.9 per cent of the reported stake was acquired within the filing window on average" | `empirics.tex:112-114` | SEC Release 33-11253 |
| N9 | "The 3 per cent of non-corporate-action campaigns that remain below 90 per cent completion at the amended deadline form the deeply constrained tail" | `model.tex:218-220` | SEC Release 33-11253 |
| N10 | Late-filing rates "of 34 and 11 per cent" for corporate-action vs non-corporate-action filings | `workplan.tex:183-184` | SEC Release 33-11253 |
| N11 | Celentano–Levine: SMM "on 2001--2019 data"; "activist presence reduces the conditional bid premium by 13.7 per cent, or 5.2 percentage points" | `lit.tex:77-81` | Celentano & Levine (2025) |
| N12 | AFS: "average Schedule~13D announcement return of 6.34 per cent into treatment, stock-picking, and sample-selection components of 75.2, 12.2, and 12.6 per cent" | `lit.tex:71-75` | Albuquerque, Fos & Schroth (2022) |
| N13 | Collin-Dufresne & Fos (2015): 13D filers "trade on days when measured price impact is almost 30 per cent below its sample average" | `lit.tex:37-39` | Collin-Dufresne & Fos (2015) |
| N14 | Betton et al. (2014): run-up/markup slope "changes from $-0.09$ under the unadjusted method to $-0.39$" | `lit.tex:95-98` | Betton, Eckbo, Thompson & Thorburn (2014) |
| N15 | Schwert (1996): run-up "from day $-42$ to day $-1$"; "at least two-thirds of the run-up added to the total price" | `lit.tex:93-95` | Schwert (1996) |
| N16 | Eckbo, Malenko & Thorburn (2025): "a run-up from day $-41$ to day $-2$ and a separate three-day announcement window" | `lit.tex:98-100` | Eckbo, Malenko & Thorburn (2025) |
| N17 | Greenwood & Schor (2009): activism raises takeover probability "by about eleven percentage points" | `lit.tex:104-107` | Greenwood & Schor (2009) |
| N18 | Brav et al. (2008): "selling the company is an objective in roughly 14--18 per cent of campaigns"; "about 15 per cent of activist targets are acquired" | `lit.tex:107-109` | Brav, Jiang, Partnoy & Thomas (2008) |
| N19 | Gantchev (2013): "an average campaign cost of about \$10.5 million, roughly half in the proxy stage" | `lit.tex:84-86` | Gantchev (2013) — **the proposal's figure is loose**: Gantchev prints **\$10.71m**, and it is the cost of a campaign *ending in a proxy contest*, not an average campaign (`research/cards/gantchev_2013_jfe.md` R4, Q7). "Roughly half in the proxy stage" checks out (\$5.94m of \$10.71m). *(verifier)* |
| N20 | Bonetti, Duro & Ormazabal (2020): "staggered implementation of the E.U.\ Transparency Directive from 2007 to 2009" | `lit.tex:18-19` | Bonetti, Duro & Ormazabal (2020) |
| N21 | Own claim: "Moving from approximately seven to five business days raises the quadratic cost of a fixed post-trigger increment by $7/5=1.4$, or 40 per cent" | `model.tex:99-101` | author's own arithmetic (depends on the "ten calendar days ≈ seven business days" mapping, `model.tex:48-49`) |
| N22 | Own claim: novelty search "conducted on 2 August 2026 … found no study of realised post-February-2024 Schedule~13D outcomes" | `lit.tex:138-141` | author's own search — **REFUTED (verifier).** Trivedi, SSRN 6866499, posted **3 June 2026** (two months before the proposal's search date), runs a pre-registered DiD on the 2024-02-05 deadline change *using 13G filers as the control group*, and reports realised post-reform outcomes (+0.35 on the within-five-business-day compliance share, p = 0.007; nulls on mean lag, bid-ask spread, illiquidity). Verified in `research/review_v3/verify_facts.md:35` (N-1, CONFIRMED verbatim from the SSRN page) and `research/review_v3/novelty_scan.md:11,32`. Bishop/Fos/Jiang/Partnoy (SSRN 6061814, Jan 2026) does **not** refute the sentence — its lever is the HSR premerger threshold, not the 13D window. |

## 9. Quotes we may lean on (verbatim, `file:line`-cited)

Copied character-for-character from the LaTeX source; soft line-wraps in the source are joined here with a single space, and LaTeX markup is preserved as written.

| # | Quote (verbatim) | `file:line` | Used for |
|---|---|---|---|
| Q1 | "The reform has a single adoption date and no untreated group: every initial Schedule~13D filer became subject to the five-business-day deadline on 5 February 2024 \parencite{sec2023modernization}. Identification therefore uses cross-sectional variation in how tightly the common deadline constrains each target, rather than a treated-versus-control comparison." | `proposal/sections/empirics.tex:7-11` | §6, §7 — no control group; the identification cell it occupies |
| Q2 | "The contribution is a realised evaluation of the February 2024 Schedule~13D acceleration using predetermined variation in required trading days." | `proposal/sections/framing.tex:78-79` | §7 — the exact claim v4 must not duplicate |
| Q3 | "First, the deadline does not constrain the activist's ability to reach the disclosure threshold because the statutory clock starts at the crossing. It constrains only ownership acquired beyond the threshold." | `proposal/sections/model.tex:157-159` | §7 — the threshold margin is left free |
| Q4 | "The filing price is a Bayesian update based on an exogenously garbled filing. Nature adds noise to the disclosed $(x,\text{purpose})$ pair, and a false Item~4 statement carries an exogenous securities-liability cost. The activist's stake is not solved as an endogenous signal." | `proposal/sections/model.tex:432-435` | §6, §7 — the partition/signalling whitespace |
| Q5 | "Endogenising the filing price is left for separate work." | `proposal/sections/model.tex:447-448` | §7 — explicit hand-off of the partition question |
| Q6 | "Earlier disclosure raises the bid hazard if and only if $\varepsilon_{\mathrm{cert}}>\varepsilon_{\mathrm{det}}$. The model therefore does not impose a sign on bidder entry." | `proposal/sections/model.tex:264-266` | §3 R11, §7 — unsigned entry effect is open ground |
| Q7 | "Together, these figures imply an average accumulation effect on the order of one tenth of a percentage point of shares outstanding. The interpretation of any estimate will remain bounded by that scale." | `proposal/sections/empirics.tex:114-117` | §5 — the proposal's own power ceiling |
| Q8 | "Filing-delay compression and accumulation after the legal deadline are mechanical consequences of compliance and cannot establish a behavioural response." | `proposal/sections/empirics.tex:166-168` | §5, §7 — the EDGAR-only leg cannot carry a behavioural claim |
| Q9 | "It will not be used as a legal-threshold comparison because the disclosure regimes are not otherwise comparable." | `proposal/sections/empirics.tex:180-182` | §6, §7 — the UK/EU sample is not a control group |
| Q10 | "is a static stake-size trigger, not the period between threshold crossing and mandatory filing. Their discussion of objective-specific thresholds, including sale-seeking campaigns, leaves open the corresponding question for filing deadlines." | `proposal/sections/lit.tex:12-15` | §6 — how it positions against the threshold margin |
| Q11 | "Cash-settled derivatives are treated in the empirical Item~6 analysis as an outside option but are not priced in the model. This omission is consequential because derivative substitution is a primary empirical margin." | `proposal/sections/model.tex:453-455` | §6 — self-declared theory gap on its own primary margin |
| Q12 | "A systematic search conducted on 2 August 2026 across SSRN, NBER, arXiv, SEC and DERA materials, forthcoming journal pages, and author websites found no study of realised post-February-2024 Schedule~13D outcomes." | `proposal/sections/lit.tex:138-141` | §8 N22 — the novelty claim to test against Trivedi / Bishop et al. |

## 10. Verification log

*(Filled by the verifier, 2026-08-19. Method: every `file:line` opened with `sed`/`cat -n` against
`/Users/austinli/Projects/blockholder_v4/proposal/`; every quote matched character-for-character
under the card's line-join rule; competitor coverage by `grep -rniE` over the whole `proposal/`
tree; borrowed numbers by `grep -rn` on each printed figure; cross-checks against
`research/cards/celentano_levine_2025.md`, `research/cards/albuquerque_fos_schroth_2022.md`,
`research/cards/gantchev_2013_jfe.md`, `research/cards/greenwood_schor_2009_jfe.md`,
`research/txt_extracts/collin_dufresne_fos_2015_jf.txt`, `research/review_v3/verify_facts.md`,
`research/review_v3/novelty_scan.md`. Nothing under `proposal/` was edited.)*

**Counts: 73 OK · 3 WRONG · 6 MISCITED · 7 UNCHECKED.**

### Quotes Q1–Q12 (§9)

| # | Verdict | Checked against |
|---|---|---|
| Q1 | **OK** | `empirics.tex:7-11`, verbatim incl. `\parencite{sec2023modernization}` |
| Q2 | **OK** | `framing.tex:78-79` |
| Q3 | **OK** | `model.tex:157-159` (inside Prop. 1) |
| Q4 | **OK** | `model.tex:432-435` |
| Q5 | **OK** | `model.tex:447-448` (begins mid-line 447) |
| Q6 | **OK** | `model.tex:264-266` |
| Q7 | **OK** | `empirics.tex:114-117` (begins mid-line 114) |
| Q8 | **OK** | `empirics.tex:166-168` |
| Q9 | **OK** | `empirics.tex:180-182` (begins mid-line 180) |
| Q10 | **OK** | `lit.tex:12-15` (begins mid-line 12) |
| Q11 | **OK** | `model.tex:453-455` (begins mid-line 453) |
| Q12 | **OK** as a quote (`lit.tex:138-141`) — but the **claim it makes is false**: see N22 below |

All twelve reproduce the source exactly under the declared line-join convention. No paraphrase, no
altered meaning, no dropped negation.

### Results R1–R13, E1–E3, P1–P3 (§3)

- **Labels all sustained.** Re-read `model.tex` and `technical_appendix.tex` in full. The proposal
  contains **exactly one** `\begin{proposition}` (`model.tex:143`) and no theorem/lemma/corollary —
  the card's "a single proposition plus algebraic identities" is confirmed by
  `grep -rn "begin{proposition}\|begin{theorem}\|begin{lemma}\|begin{corollary}" sections/`.
- R1 **OK**: derivation present at `technical_appendix.tex:5-20` (constant-rate argument from
  convexity plus the symmetric constraint); PROVED is right.
- R2 **OK with a nuance**: the *first* half ("the deadline does not constrain reaching the
  threshold") is an institutional premise carried from `model.tex:36-38`, not a derivation; only
  the maximum-stake formula `0.05(1+d/RTD_i)` is algebra. The card's parenthetical already says
  "one-line algebra inside the proposition", which is fair.
- R3–R10, R12–R13, E1–E3, P1–P3 **OK**: statements, ranges and labels all match the print.
- R4 **OK (ASSERTED is correct, not too weak)**: `model.tex:170-175` states the monotonicity inside
  the proposition with no proof, and `technical_appendix.tex` does not derive it.
- R5 **OK**: `model.tex:180-189` + `technical_appendix.tex:22-37`; `b(·,·)` is indeed never given a
  functional form anywhere in `proposal/`.
- R11 **OK**: `h`, `s`, `B^e` are defined but never derived from primitives — ASSERTED is right.
- **§5 reader inferences re-derived and confirmed** (they are the card's, not the proposal's, and
  are labelled as such): on the constrained set `C_x = λ_L·Δx̄_i/d = 0.05·λ_L/RTD_i`, and with
  `λ_L ∝ 1/ADV` (`model.tex:74-76`) and `RTD_i = 0.05·S_out/(φ·ADV)` this is `∝ 1/S_out` — so the
  shadow value is not monotone in `RTD_i` across the cross-section. **The `φ` gap is also
  confirmed**: `grep -rn "phi" sections/` returns only the symbol's definition and its two
  appearances in the `RTD` formula — **no numeric value for `φ` is given anywhere**, so
  `{RTD_i > d}` and the doubling calibration are unidentified as printed.

### Scope claims (§6) — all confirmed

- **Window margin only / threshold never a policy variable** — **OK**, with one qualifier now added
  to §6 and §7: `threshold` occurs 27 times across the sections and never as something the paper
  varies; the *disclosure* threshold is only the clock-start and the `0.05` scale. But a **control**
  threshold prediction does exist (`model.tex:311-314`, `empirics.tex:211-213`) — the card had
  called the threshold margin flatly "not occupied".
- **"The reform has a single adoption date and no untreated group"** — **OK**, `empirics.tex:7-8`,
  first sentence of the design section, exactly as the card says.
- **UK/EU sample is not a threshold comparison** — **OK**, `empirics.tex:180-182` and restated in
  the inference battery at `workplan.tex:209-211` ("used only to absorb the global M&A and
  interest-rate cycle, not as a legal-threshold comparison").
- **"Endogenising the filing price is left for separate work"** — **OK**, `model.tex:447-448`.
- **Liquidity is not a comparative-static object** — **OK**: liquidity appears only as `λ_L(L)`, as
  the `ADV` denominator of `RTD`, and as liquidity-decile-by-quarter fixed effects. There is no
  `d(outcome)/d(liquidity)` object anywhere.

### Citation coverage (§8) — greps over the whole `proposal/` tree

- **Trivedi — ABSENT** (confirmed, zero hits in `.tex` and `.bib`). **Bishop — ABSENT** (confirmed).
- **Cited, and the card's locations are right**: `polk2024` (framing 54, empirics 98, workplan 37,
  lit 133/167), `johnsonswem2021` (lit 69, 163), `celentanolevine2025` (all eight locations exact),
  `cetemen2026` (lit 65-68, 168).
- **MISCITED, now fixed**: `corumlevit2019` is at `model.tex:235`, not 236; `back2018` is at
  `lit.tex:32`, not 33; `albuquerquefosschroth2022` is at `lit.tex:71`, not 72.
- **WRONG, now fixed**: the bibliography has **32** entries, not 29 (`grep -c '^@'`).
- **MISCITED, now fixed**: `collindufresnefos2015` is cited **5** times, not 4.
- **OK and worth keeping**: `hirschman1970`, `coffee1991`, `bhide1993` really are in `outline.bib`
  (lines 1, 48, 58) with **zero** occurrences in any section file — the exit-voice trio is dropped
  from the text, exactly as the card says.
- **WRONG, now fixed**: the card's §6 attributed "The tender game itself is not reproduced" to Q12;
  Q12 is the novelty-search quote. The tender-game sentence is `model.tex:316`.

### Borrowed numbers N1–N22 — each checked against the proposal print

All 22 are stated by the proposal at (or within one line of) the cited location; every distinctive
figure was located by `grep -rn`. Line-range corrections and cross-checks:

- **N1–N19, N21 — OK against the proposal text.** N20 was **MISCITED**: the Bonetti–Duro–Ormazabal
  "2007 to 2009" sentence is at `lit.tex:18-19`, not 20-22 (**fixed**).
- **N1 and N2 — OK against the source.** `research/txt_extracts/polk_et_al_2024_jfrc.txt:264-265`:
  "9,685 initial Schedule 13D filings over the period 2001--2022, representing 5,863 reporting
  entities"; 9,685/5,863 = 1.652, so the proposal's "1.65 filings per entity" is its own correct
  arithmetic. The design characterisation in N2 also checks out: Polk compares filers inside five
  days "with those filing between 6 and 10 days" (line 85), and the outcomes are excess returns and
  abnormal trading volume around the trigger and filing dates (lines 204, 241, 304-311).
- **N11 — OK against the source.** `research/cards/celentano_levine_2025.md` R6/Q4: "13.7 percent
  (5.2 percentage points) lower", SMM on 2001–2019 data. The proposal borrows it correctly. (The CL
  card's own caveat — no SE on that counterfactual — is not something the proposal claims.)
- **N12 — OK against the source.** `research/cards/albuquerque_fos_schroth_2022.md` R1/Q5: 75.2 /
  12.2 / 12.6 per cent of a model-**predicted** 6.34%. The proposal uses 6.34 (predicted), not 6.33
  (observed) — correct.
- **N13 — OK against the source.** `research/txt_extracts/collin_dufresne_fos_2015_jf.txt:119`:
  "impact (λ) is almost 30% lower relative to the sample average".
- **N17 — OK against the source.** `research/cards/greenwood_schor_2009_jfe.md` R7/Q5: ~11
  percentage points.
- **N19 — MISCITED at source (the proposal's own slip, now noted in the §8 table).** Gantchev prints
  **\$10.71m** for a campaign *ending in a proxy contest*, not "an average campaign cost of about
  \$10.5 million" (`research/cards/gantchev_2013_jfe.md` R4, Q7). "Roughly half in the proxy stage"
  is right (\$5.94m of \$10.71m).
- **N22 — WRONG. The proposal's novelty claim is refuted.** Trivedi (SSRN 6866499, posted **3 June
  2026**, i.e. two months *before* the proposal's 2 August 2026 search) runs a pre-registered DiD on
  the 2024-02-05 acceleration with **13G filers as a control group** and reports realised
  post-reform outcomes (+0.35 on the within-five-business-day compliance share, p = 0.007; nulls on
  mean lag, bid–ask spread and the illiquidity proxy). Verified verbatim from the SSRN page in
  `research/review_v3/verify_facts.md:35` (N-1, CONFIRMED) and summarised at
  `research/review_v3/novelty_scan.md:11,32`. Bishop/Fos/Jiang/Partnoy (SSRN 6061814, 13 Jan 2026)
  does **not** refute the sentence — its lever is the HSR premerger-notification threshold, not the
  13D filing window. **Consequence for v4, added to §5:** a treated-vs-control design on this shock
  already exists in public, so the proposal's "no untreated group" is a design *choice*, not a fact
  about the reform.

### UNCHECKED (left in place, marked)

1. ~~**N3–N10 against SEC Release 33-11253 itself.**~~ **CLOSED 2026-08-19 — see §9c.** The release
   was fetched and all eight items checked against it: **5 OK, 2 MISCITED, 1 NOT FOUND (N3, the
   \$810m figure, does not exist in the release), 0 WRONG.** N7's power ceiling is confirmed. The
   original note is kept below for the record.
   All eight are confirmed *as printed in the
   proposal* at the cited lines. They are **not** confirmed against the release: `sec.gov` returns
   **HTTP 403** to a direct `curl` of `https://www.sec.gov/files/rules/final/2023/33-11253.pdf`
   (attempted, 403), no local copy exists in the repo, and the same block is on record in
   `research/review_v3/facts_verification.md:32`. This includes the Table 6 pairs (N6) and the 5.9%
   figure (N8). **Decision-critical for positioning**: N7/P2 (the ~3% / ~7-per-year constrained
   population and the ~0.1 pp implied effect) is the entire power ceiling on which the card's
   "null-by-construction" judgement rests — if those figures are misread from the release, the
   whole deliverability argument in §5 and §7 changes. Someone with SEC access should re-check
   N6, N7 and N8 against the printed tables.
2. **N14 (Betton et al., −0.09 → −0.39), N15 (Schwert, day −42 to −1, two-thirds), N16 (Eckbo–
   Malenko–Thorburn, −41 to −2), N18 (Brav et al., 14–18% sale objective, ~15% acquired), N20
   (Bonetti–Duro–Ormazabal, 2007–2009).** No usable local full text or card for any of these five; the
   Brav extraction in `research/txt_extracts/brav_etal_2008.txt` is column-scrambled and the
   objective table could not be read reliably. Confirmed as printed in the proposal only. None is
   decision-critical for v4's position.
3. **The PDFs (`outline.pdf`, `execution_plan.pdf`) were not opened**, per the card's stated
   convention. Everything here is checked against the LaTeX source, which is the build input.

### Omissions found and added to the card

1. **`sections/conclusion.tex` was missing from the card entirely** — 50 lines, a pre-committed 2×2
   interpretation table. Added as a new subsection in §2. It carries three things that change how
   v4 should read the proposal: the author states that **no response on either margin is the modal
   ex ante outcome** (`conclusion.tex:36-38`); that a derivative-only response would make **the
   non-adoption of Rule 13d-3(e), not the deadline, the operative policy margin**
   (`conclusion.tex:33-36`); and that "a lower markup is not by itself evidence of a lower total
   gain" (`conclusion.tex:47-48`).
2. **The disposition of `draft_v2` — the biggest omission** (`workplan.tex:12-17`, `134-139`).
   The proposal freezes the 92-page liquidity draft after a named hygiene list (cross-country
   threshold claims, the `κ→1` narrative, welfare units, two citation attributions) plus a
   one-week Gaussian-noise falsification of the hump, and Gate 0's memo states "what is being
   abandoned as the job-market-paper framing". That is the author's own defect list for v4's base
   and the substitution ADR-0004 exists to reverse. Added to §7.
3. **A third bidder-entry channel** (`model.tex:275-278`): the reform lowers `x*`, which lowers
   `B^e`, which *raises* entry — so an entry response "cannot be attributed entirely to
   certification". A stated identification limit, not just an unsigned sign. Added to §2.
4. **The empirical proxy map for `λ_app`** (`model.tex:307-314`) plus the 5% discontinuity check
   (`empirics.tex:211-213`). The card said the tender game is "not a duplication"; the *theory* is
   free, but the proxy map (`q`, `γ`, `ψ` → fringe M&A intensity, acquirer mix and redeployability,
   bloc stake vs control thresholds) is already claimed. Added to §6 and §7 item 7.
5. **A control-threshold prediction does exist** — `λ_app` jumps at the blocking threshold `1−τ_c`
   (`model.tex:311-314`). The card's "threshold margin: not occupied" needed the qualifier that it
   is the *disclosure* threshold that is free. Added to §6 and the §7 table.
6. **The second argument against a signalling structure** (`model.tex:61-68`): a two-dimensional
   type with a two-dimensional signal `(x, purpose)` **generically separates**, collapsing `P^F` to
   the full-information price. Distinct from the refinement/uniqueness objection at
   `model.tex:435-438`, and it lands directly on v4's flagged-vs-pooled plan. Added to §6.
7. **Welfare cohort and the LATE-weights defence** (`model.tex:414-427`): welfare is defined for
   shareholders present at trigger-minus-`k`, with the activist's transfer from selling
   shareholders reported separately; and the exposure design is defended as producing the marginal
   weights the decomposition needs rather than an ATE. Added to §2.
8. **The unaffected-price anchor** (`model.tex:40-44`, `empirics.tex:190-193`): `P⁰` at `k = 60`
   trading days before the **trigger**, robustness at 30 and 120. Added to §2.
9. **The SSRN posting clock** (`workplan.tex:279-280`): first-stage facts and the exposure design
   go public at month 4–5. Added to §7 as a competitive-clock line.

### Overall verdict

**Sound and unusually accurate on the source; two substantive corrections.** Every quote is
verbatim, every honesty label survives re-reading, and the three §5 reader-inferences (dose–FE
collinearity, uncalibrated `φ`, non-monotone shadow value) were re-derived from the proposal's own
equations and hold. The two things that change a decision are: (i) **N22 is refuted** — Trivedi
already published a DiD on this shock *with* a control group, two months before the proposal's
novelty search, so the proposal's headline novelty sentence is false and its "no untreated group"
premise is a choice rather than a constraint; and (ii) the card had **no line on what the proposal
does with `draft_v2`**, which is the one passage in `proposal/` that speaks directly to v4's own
base. Smaller fixes: 32 bib entries not 29, three off-by-one cite lines, one wrong line range, one
mis-pointed Q-reference, and one citation count. N3–N10 remain unchecked against SEC Release
33-11253 (sec.gov 403s); N7/N8 are the ones worth re-checking with SEC access, because the whole
power-ceiling argument rests on them.

## 9c. SEC-release check (supplement reader, opus, 2026-08-19)

**Closes UNCHECKED item 1 of §9** ("N3–N10 against SEC Release 33-11253 itself"), which the verifier
flagged as decision-critical because N7 carries the whole power/deliverability argument in §5 and §7.

**Source now in hand:** `research/txt_extracts/sec_release_33_11253.pdf` / `.txt` — Release Nos.
33-11253; 34-98704, File No. S7-06-22, "Modernization of Beneficial Ownership Reporting", October
2023, Conformed to Federal Register version, **295 pages**. Every number below was located by regex
over the full text and then read in its surrounding page. **Page numbers are the release's own printed
pages (1–295), which match the PDF page index.** A companion fact sheet with the release's dates,
tables and caveats is at `research/cards/_institutional_sec_33_11253.md`.

### Verdicts

| # | Number as the proposal prints it | Verdict | Where it actually is in the release |
|---|---|---|---|
| **N3** | "approximately \$810 million a year in foregone shareholder value" | **NOT FOUND** | **No such figure exists in Release 33-11253.** A regex sweep for `810` returns two hits, both footnote numbers (p. 222). A full inventory of every dollar amount in all 295 pages returns nothing between \$128 million and \$1.5 billion. The release's own annualised foregone-value figures are **\$49 million/year** (p. 211: "$23 million from Column 1 plus $26 million from Column 2"), or **\$42M** / **\$36M** under two adaptation assumptions (p. 211 and n. 773). The Commission also disclaims them: "the wealth transfer estimates in Table 5 **do not represent estimates of the benefit** of the final rule amendments" (p. 211). |
| **N4** | "roughly 80 per cent of filers had already completed accumulation by the five-business-day deadline" | **OK** | **Table 3, p. 189**: 1,907 of 2,370 non-corporate-action campaigns = **80%**, avg. **173/year**. Restated in text at p. 234 ("80 percent of campaigns were completed by the amended deadline"). |
| **N5** | "Roughly 29 per cent of 2022 initial filings, or 41 per cent of timely filings, were made within five business days … and 97 per cent had reached 90 per cent of their reported stake" | **OK** | **p. 178**, verbatim: "Approximately **29 percent** of the initial Schedule 13D filings, representing about **41 percent** of all of the initial Schedule 13D filings that were filed by the current filing deadline, were filed within the amended five-business day deadline." (repeated p. 46 n. 166; p. 193). The 97%: **p. 188**, "about **97 percent** of the filers completed acquiring 90 percent of their reported stake by the amended deadline". Note the two statistics come from **different samples** — the 29/41% is *all* initial 13Ds in calendar **2022**; the 97% is *non-corporate-action* filings **2011–2021**. The proposal's sentence runs them together; harmless as written, but do not describe them as one population. |
| **N6** | Table 6 pairs: \$1.8bn vs \$916m; Amihud 0.09 vs 0.13; 43.6 vs 29.8 per cent; CAR 17.2 vs 5.7 per cent; \$222m vs \$36m | **OK on all five number pairs · MISCITED on one label** | **Table 6, pp. 225–226**, columns (3) <90% vs (1) 100%: market cap **\$1.8B vs \$916M** ✓ (Row 2); Amihud **0.09 vs 0.13** ✓ (Row 4); Prominent Activist **43.6% vs 29.8%** ✓ (Row 6); CAR **17.2% vs 5.7%** ✓ (Row 10); increase in shareholder value per campaign **\$222M vs \$36M** ✓ (Row 11). **The label is wrong:** Row 10 is "Average return around filing date (**cumulative abnormal return, day −20 to 20**)" — a 41-*business*-day window centred on the filing date (construction spelled out at p. 224 n. 817, which also notes it differs from the calendar-day Figures 7a/7b). Calling it "filing-window CAR" implies the trigger-to-filing interval and is not what the release measures. **Fix the wording in `empirics.tex:84-91` before draft_v3.** |
| **N7** | "only 3 per cent of non-corporate-action campaigns, about seven per year, had accumulated less than 90 per cent … 1 per cent, about one per year, had accumulated less than 75 per cent" | **OK — the decision-critical one, and it holds exactly** | **Table 3, p. 189**: <90% = **78 campaigns, 3%, 7/year**; <75% = **16 campaigns, 1%, 1/year**. Text at **p. 188** gives the complements ("about 97 percent … the remaining three percent"; "about 99 percent … the remaining one percent"). The same 7 and 1 per year appear in **Table 5 Row 1, p. 210** and **Table 6 Row 1, p. 225**. **The power ceiling in §5/§7 is confirmed against the primary source: the deeply constrained population really is ~78 campaigns over eleven years.** |
| **N8** | "Among the 20 per cent that continued to accumulate after the deadline, only 5.9 per cent of the reported stake was acquired within the filing window on average" | **OK on both numbers · MISCITED on wording** | The 20%: **Table 3, p. 189**, column (2) = 463 campaigns = **20%**, 42/year. The 5.9%: **Table 6 Row 8, p. 225**, column (2). But Row 8 is titled "Average percentage of reported ownership stake accumulated **after amended deadline**" — i.e. between the *five-business-day* deadline and the actual filing date, **not** "within the filing window". If "filing window" is read as the ten-day window, the sentence overstates what the release shows; if it is read as the residual post-deadline stub, it is right but ambiguous. **Rewrite as "after the five-business-day deadline" in `empirics.tex:112-114`.** For context the same row reads 19.2% (<90%) and 35.3% (<75%). |
| **N9** | "The 3 per cent of non-corporate-action campaigns that remain below 90 per cent completion at the amended deadline form the deeply constrained tail" | **OK** | Same source as N7: **Table 3, p. 189**, and **p. 188**. The release's own characterisation of this group matches: they "continued to accumulate shares constituting 10 percent or more of their reported stake after the amended deadline" (p. 188). |
| **N10** | Late-filing rates "of 34 and 11 per cent" for corporate-action vs non-corporate-action filings | **OK** | **Table 2 footnotes, p. 181**: non-corporate-action — "About **11%** of these filings were filed late relative to the current deadline"; corporate-action — "About **34%** of filings in this category were filed late relative to the current deadline". Sample 2011–2021: 3,067 non-corporate-action (20% of all) vs 12,657 corporate-action (80%). |

**Counts: 5 OK · 2 MISCITED · 1 NOT FOUND · 0 WRONG.**

### What this changes

1. **N3 must be removed or re-sourced before draft_v3.** It appears in three places — `framing.tex:51-53`, `lit.tex:130-131`, `abstract.tex:18-19` — and one of them is the **abstract**. A referee who opens the release will not find \$810 million in it. Either drop the number, or replace it with the release's own **\$49 million per year** (Table 5, p. 211) *together with* the Commission's disclaimer that this is not a benefit estimate. If \$810m came from the DERA Memorandum or the 2022 Proposing Release (33-11030), that is a **different document** and must be cited as such.
2. **Two wording fixes, both cheap:** N6's "filing-window CAR" → "cumulative abnormal return, day −20 to +20 around the filing date"; N8's "within the filing window" → "after the five-business-day deadline".
3. **The deliverability judgement in §5/§7 stands.** N7 — the ~3% / ~7-per-year constrained population on which the "null-by-construction" power ceiling rests — is confirmed verbatim against Table 3 and the surrounding text. Nothing in the release makes that tail larger.
4. **Two confounds the release itself documents, now with page cites** (see the fact sheet §3 and §6): the **EDGAR cut-off moved 5:30 p.m. → 10 p.m. ET on the same date** as the deadline change (pp. 9, 11, 39 n. 137), so filing-time outcomes are jointly treated; and the release cites **Gantchev & Jotikasthira (2018)** for activist accumulation tracking institutional selling at the daily frequency (p. 212 n. 775) — the liquidity-timing channel is already in the regulatory record.
5. **Remaining UNCHECKED in §9 after this pass:** item 2 only (N14, N15, N16, N18, N20 — none decision-critical). Item 1 is closed.
