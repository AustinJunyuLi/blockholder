# Levit, Malenko & Maug (2026) — "The Voting Premium"

**Venue / status:** *The Journal of Finance* Vol. LXXXI (81), No. 3, June 2026, pp. 1321–1375. DOI 10.1111/jofi.70037. Open access (CC-BY). Initial submission: November 15, 2023; accepted: January 12, 2025. Editors listed: Antoinette Schoar, Urban Jermann, Leonid Kogan, Jonathan Lewellen, Thomas Philippon (handling Editor named in the acknowledgement footnote: Thomas Philippon). An **Internet Appendix** (Appendix S1, "Supporting Information") is a separate online file. It was **not** available to the original reader or verifier; it has since been fetched (`research/txt_extracts/lmm_2026_internet_appendix.pdf`, 100 pp.) and read in full — see **§9b**.
**Full text from:** `lit/levit-malenko-maug-voting-premium-jf2026.pdf` (56 PDF pages) and `research/txt/voting_premium_jf2026.txt` · **Reader:** opus · **Read:** full text, pp. 1321–1375 (all body text, Table I, Appendix: Proofs, references). Internet Appendix not read (not in repo).
**Page numbering used:** printed *Journal of Finance* page numbers (1321–1375) of the published June 2026 version.
**Type:** theory **Role for us:** competitor (adjacent object) / template (how a top-journal blockholder-trading theory closes with a measurement section)

## 1. Question

Why does a voting premium — a price wedge attached to the voting rights embedded in a share — exist, and what do standard empirical proxies for it actually measure? The classic answer (Grossman–Hart 1988, Harris–Raviv 1988) attributes the premium to takeovers and control contests, but the empirical record contradicts that: the dual-class premium is largest where majority-control contests are rare, survives coattail rules mandating equal treatment in takeovers, is largest around shareholder meetings, and is negative for many firms. LMM build a theory of the voting premium **with no takeovers, no bidders and no controlling shareholder**, in which a minority blockholder influences outcomes by moving the *median voter* through trade, and use it to reinterpret six families of empirical estimates.

## 2. Model / data and method

**Primitives.** One firm, one unit of shares outstanding. A continuum (measure one) of atomistic price-taking small shareholders, endowed with 1 − α shares in aggregate, plus one strategic blockholder endowed with α ∈ (0, 1). Baseline: one share, one vote.

**Preferences.** A binary proposal d ∈ {0, 1}. Common-value state θ ∈ {−1, 1} plus a private-value "bias" b. Share value to a small shareholder: v(d, θ, b) = v₀ + (θ + b)d (eq. 1, p. 1330). Biases are drawn from a twice-differentiable cdf G with positive density on [−b̄, b̄], b̄ ∈ (0,1). The blockholder's bias is β ∈ [−b̄, b̄]. "More activist" = higher b.

**Trading frictions = liquidity.** Small shareholder utility from buying x shares is (1 − α + x)v(·) − (γ/2)x² (eq. 2, p. 1331); γ > 0 is a quadratic trading cost. The market-clearing price is p*(y, q*ₑ) = γy + v(E[b], q*ₑ) (eq. 10, p. 1334), so **γ is the model's illiquidity parameter and 1/γ its depth** (p. 1334, Q3). The blockholder has trading cost η ≥ 0 (all results hold at η = 0). A maintained assumption γ > γ̄ (eq. 3, p. 1331) — γ̄ "formally defined at the beginning of the Appendix" as the max of the cutoffs used in each proof (p. 1359) — buys uniqueness and the other regularity properties. A *separate* assumption α < min{τ, 1 − τ} is stated on p. 1332; together with γ > γ̄ it rules out a unilateral blockholder veto and short-selling, but only *via Lemma IA.2 of the Internet Appendix* (p. 1332), which this reader could not see. (Page split and IA dependence added by verifier.)

**Timing.** (1) Blockholder submits order y; (2) small shareholders observe y and submit orders (limit-order interpretation); market clears at p; (3) record date passes; (4) all shareholders observe a public signal q = E[θ | signal], distributed F with mean zero and density f on [−Δ, Δ], Δ ∈ (b̄, 1); (5) shareholders vote the shares they hold; the proposal passes if at least fraction τ ∈ (0,1) of all shares are cast in favor.

**Equilibrium notion.** Subgame-perfect Nash equilibrium in undominated strategies of the voting game (p. 1332) — i.e. everyone votes as if pivotal, so shareholder b votes yes iff b + q ≥ 0 (eq. 4).

**Mechanism.** Trading reallocates cash-flow *and* voting rights jointly. The post-trade small-shareholder distribution R first-order stochastically dominates the pre-trade G (p. 1335): the blockholder buys disproportionately from those who disagree most, so influence has a *direct* (more votes) and an *indirect* (shareholder-base composition) channel. The identity of the median voter −q*(y) summarizes the expected voting outcome. The blockholder's marginal payoff splits into MPC (cash-flow rights) + MPV (voting rights) (eq. 19, p. 1338).

**The object.** The **voting premium** is VP(y*) ≡ p* − p_CF(q*(y*)) (eq. 26, p. 1340): actual price minus the price in the hypothetical world where the same decision rule q*(y*) is set exogenously so trades cannot move it (that hypothetical price is the price of a share without voting rights, eq. 25). In equilibrium VP = [γσ(β)/(2γ+η)]·MPV(y*) (eq. 27, p. 1341), and decomposes as (ability to move the median voter) × (marginal benefit of a vote − price impact of a vote) (eq. 28, p. 1341).

**What buys tractability:** quadratic trading costs (linear demands, closed-form market clearing); atomistic price-taking small shareholders; the γ > γ̄ restriction (kills multiple voting-stage equilibria driven by self-fulfilling expectations, kills short sales, and makes σ(β) = 1 outside a vanishing interval); binary state and binary proposal; blockholder-moves-first (Stackelberg) trading; symmetric support of q; no private information at the trading stage (heterogeneity is preferences/beliefs, not signals). Everything beyond the baseline — dual class, record-date dynamics, vote trading, multiple blockholders, proxy advisors, passive investors, uncertainty about biases, management decision-making, selective participation — lives in the Internet Appendix.

**Not a model of takeovers, and not of a disclosure rule.** No bidder, no tender offer, no control contest, no 5%/13D-type filing rule, no stake-disclosure threshold or window anywhere in the paper.

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where (page / prop / table) |
|---|---|---|---|
| R1 | For any trading outcome, approval at the voting stage takes a cutoff form: the proposal passes iff q > q*. | PROVED | p. 1333, Lemma 1 (proof p. 1359) |
| R2 | Given blockholder trade y, the voting-stage equilibrium is unique when γ > γ̄; there exists ȳ such that for y ≥ ȳ the blockholder *is* the median voter, and for y < ȳ the median voter is a small shareholder whose distance from β falls as y rises. | PROVED | pp. 1336–1337, Proposition 1 (proof pp. 1359–1361) |
| R3 | The full equilibrium exists and is unique; blockholder trade y* splits into a cash-flow term and a voting term proportional to MPV(y*); the price is p* = v(b*, q*(y*)) + [γσ(β)/(2γ+η)]MPV(y*). | PROVED | pp. 1338–1339, Proposition 2 (proof pp. 1361 ff.) |
| R4 | With the decision rule set exogenously, the price equals v(b*, q*(y*)) — the price of a share without voting rights; hence VP ≡ p* − p_CF is proportional to MPV. | PROVED | p. 1340, Corollary 1 + eq. (27) (proof p. 1368) |
| R5 | A **positive voting premium arises with no takeover, no bidder and no majority control**, purely from the blockholder's ability to shift the median voter. | PROVED | pp. 1341–1343, Prop. 3(ii); restated p. 1358 |
| R6 | If the blockholder's bias β is moderate (β ∈ [β^L_mv, β^H_mv]) he *becomes* the median voter and **the voting premium is exactly zero** — voting power large, premium zero. | PROVED | p. 1342, Proposition 3(i) |
| R7 | If β is extreme (β > β^H_non-mv or β < β^L_non-mv) the premium is strictly positive and increases as β becomes more extreme. | PROVED | p. 1342, Proposition 3(ii) |
| R8 | The voting premium **underestimates the total value of voting rights**, because it prices only the marginal vote at y*, not the inframarginal accumulation. | ASSERTED (argued from R4/R6, no separate proposition) | pp. 1343–1344, §IV.D.1 |
| R9 | A *higher* voting premium can go with a *higher* payoff to small shareholders: if G⁻¹((1−τ)/(1−α)) < E[b] < β (right-skewed preferences or a supermajority τ > 0.5), both W* and VP strictly increase in β. So VP is not a good proxy for blockholder–minority conflict. | PROVED — **confirmed: IA §III.I, IA pp. 34–36** | p. 1345, Proposition 4 (corrected by verifier; card had 1344) |
| R10 | If all small shareholders share one bias b ≠ β, the voting premium is **zero** — heterogeneity *among small shareholders* is necessary. Conflict that is common to all small shareholders (monitoring, private control benefits) does not generate a voting premium. | PROVED — **confirmed: IA §III.J, IA p. 36** (a five-line proof: with `b = E[b]` for all small shareholders, `∂(−q*)/∂y = 0`, so VP = 0 by eq. 28) | pp. 1346–1347, Corollary 2 |
| R11 | **Liquidity measured as price impact is endogenous** and differs between voting and nonvoting shares: dp*/dy = γ + (price impact of a vote)·∂(−q*)/∂y. If blockholder and average small shareholder are aligned, small shareholders free-ride, price impact rises, and voting shares are *less* liquid; if they conflict, price impact falls and voting shares are *more* liquid. | PROVED (equation 35 derived from Prop. 2 / Prop. 3) | pp. 1347–1348, §IV.D.4, eq. (35) |
| R12 | The voting premium can be **strictly negative**: if E[b] < G⁻¹((1−τ)/(1−α)) and β ∈ (β_neg, β̄_neg), the blockholder buys (y* > 0) yet p* < p_CF — free-riding by small shareholders makes the supply curve too steep. | PROVED — **confirmed: IA §III.K, IA pp. 37–38**; reaches both halves ("the voting premium is also strictly negative" and `y* > 0`) | pp. 1348–1349, Proposition 5 |
| R13 | The dual-class premium in the extension equals [γσ(β)/(2γ+η)]MPV(y*, ŷ*), the same structure as VP; it **exists only if trading frictions exist (γ > 0)** — limits to arbitrage are necessary for any voting premium. | **Split verdict (supplement reader).** The *formula* is **PROVED** — Prop. IA.4, IA §IV.A, IA p. 44, proof IA pp. 72 ff. The "**exists only if γ > 0 / limits to arbitrage are necessary**" reading is **ASSERTED**: it is a prose sentence immediately after Prop. IA.4 (IA p. 44), not part of any proposition, and every existence/uniqueness result in the paper and the IA holds only for `γ` **above** a cutoff (`∃ γ̲ < ∞ such that if γ > γ̲ …`), so the `γ → 0` limit sits outside the proved region. Safe to cite the proportionality; do **not** cite "no premium without frictions" as proved. | p. 1350 |
| R14 | The ex-record-date price drop equals the voting premium plus a new term: concerns about post-record-date trading profits change the blockholder's incentive to accumulate votes. | PROVED (as a derivation, not a numbered proposition) — **IA §IV.B.1, IA pp. 45–48**: "Proposition 2 continues to hold, with the exception that MPV(·) is replaced everywhere by M̂PV(·) and σ(β) … by σ̂(β)", giving `p*₁ − p*₂ = γσ̂(β)/(2γ+η) · M̂PV(y*₁)` (IA p. 48) | pp. 1350–1351 |
| R15 | With a separate market for votes (share lending), the **price of a separately traded vote is zero** while the voting premium on the bundled share stays positive — the two objects are conceptually different. | PROVED — **Prop. IA.5, IA §IV.C, IA p. 52, proof IA p. 84**. Refinement the card lacked: the zero vote price is an *immediate consequence* of small shareholders never being pivotal (IA p. 51); what Prop. IA.5 proves is that the *share* voting premium stays strictly positive, and only when the vote market itself is frictional (`λ_max < λ̄`, "transaction costs or search costs") and `β` is extreme | pp. 1351–1352 |
| R16 | Multiple blockholders: heterogeneous blockholders raise VP as they diverge; homogeneous blockholders compete Cournot-style and VP vanishes as their number grows. | PROVED — **Props. IA.6 (homogeneous, IA p. 54) and IA.7 (heterogeneous, IA p. 55), IA §IV.D, proofs IA pp. 93 and 95**. Qualifier: the `N → ∞` vanishing result is stated for `β > E[b]` | p. 1352 |
| R17 | Proxy advisor: if a fraction of shareholders blindly follow the advisor, the voting premium can be zero even when the blockholder is not the median voter (the advisor becomes the median voter). Net effect on VP ambiguous. | PROVED (as a derivation, no numbered proposition) — **IA §IV.E, IA pp. 56–61**; the "advisor becomes the median voter, jump in the support function, marginal ability to move the median voter is zero" argument is at IA p. 59 | p. 1353 |
| R18 | Passive shareholders (vote but do not trade) reduce liquidity and create more configurations in which VP = 0; the indirect composition effect can now oppose the direct effect but "can never overturn it." | PROVED (as a derivation, no numbered proposition) — **IA §IV.F, IA pp. 61–66**. Mechanism made explicit at IA p. 63: with a passive fraction `1 − φ`, "the parameter for trading costs, γ, is replaced by γ/φ" | pp. 1353–1354 |
| R19 | If management (not a vote) decides, weighting post-trade shareholders, a share-price premium with the same decomposition arises — the mechanism generalizes beyond voting. | PROVED — **Prop. IA.8, IA §IV.H, IA p. 70, proof IA p. 87**; the "influence premium" IP has the identical three-factor decomposition (eq. IA.109) | p. 1354 |
| R19b | **(added by verifier)** The voting premium is **not a measure of voting power** either: greater voting power moves the blockholder closer to the median voter and so *lowers* his valuation of a marginal vote — "the magnitude of the voting premium is unrelated to the blockholder's voting power, with this relationship even turning negative when the blockholder becomes the median voter himself." | ASSERTED (intro statement of the Prop. 3 logic) | p. 1325 |
| R20 | Survey of 40 empirical studies (data from a broad range of countries, 1940–2018), six methodologies. Averages, in % of stock price: dual-class shares 22.68 (median 13.58, min 4.07, max 81.50; 23 studies, 18 with negatives); block trades 20.27 (16.81 / 6.79 / 46.96; 6 studies, 4 with negatives); dual-class tender offers 42.16 (26.59 / 12.27 / 130.7; 5 studies, 0 with negatives); option replication 0.20 (0.16 / 0.09 / 0.37; 5 studies, 5 with negatives); equity lending 0.02 (0.02 / 0.01 / 0.02; 3 studies, 0); record-day trading 0.75 (0.75 / 0.09 / 1.40; 2 studies, 0). | ESTIMATED (they report others' estimates; no SEs given here) | p. 1355, Table I |
| R21 | 27 of the 40 studies reviewed report a negative voting premium for at least some firms ("no less than 27"). | ESTIMATED (literature count) | p. 1357 |
| R22 | The ex-ante (frequency-weighted) dual-class tender-offer premium is 6.08% against a dual-class premium of 22.49% — takeovers explain "only about one-quarter" (sentence is on p. 1358). Maynes (1996): a dual-class premium of 8.22% falls by roughly two percentage points after coattail provisions — **from which LMM draw a second, independent one-quarter estimate: "about one-quarter of the voting premium could arguably be attributed to preferential treatment in takeovers" (fn. 40, p. 1357)** (added by verifier). | ESTIMATED (back-of-envelope, explicitly flagged as such by the authors) | p. 1358 + fn. 40–41, p. 1357 |

## 4. Institutional facts used

- **No stake-disclosure rule is used anywhere.** The single mention of holdings disclosure is a motivation for an extension: small institutions and individuals "do not need to disclose their holdings, so their preferences may be unknown" (p. 1354) — this motivates uncertainty about G, not a filing regime.
- **Record date.** The rule that eligibility to vote is fixed on a record date is the timing anchor: the model assumes the record date follows the trading stage (p. 1331), and the ex-record-date price drop is one of the two empirical counterparts of VP (pp. 1350–1351).
- **Coattail provisions** — since the 1990s many countries mandate equal treatment of share classes in control changes; the voting premium survives them (p. 1357, citing Maynes 1996 and Nenova 2003).
- **Proxy-advisor institutions**: 80% of Glass Lewis' fund clients receive customized advice (Hu, Malenko & Zytnick 2025, p. 1353); proxy recommendations arrive on average about one month after the record date (fn. 19, p. 1331).
- **SEC Release No. IA-5325** cited only as regulatory pressure that makes small institutions rarely abstain (p. 1354).
- **Ownership scale**: Lewellen & Lewellen (2022) — US institutional ownership averages 73.7% over 2015–2017, of which 45.3 pp in blocks under 3% and 31.5 pp in blocks under 1% (fn. 15, p. 1330).
- **(added by verifier)** Limits to arbitrage on voting shares: fn. 5, p. 1326 cites Porras Prado, Saffi & Sturgess (2016) that "voting shares have higher limits to arbitrage than nonvoting shares" — the empirical fact their endogenous-liquidity result is aimed at.
- **(added by verifier)** They place themselves against their own 2024 JF paper explicitly: LMM (2024) "analyze trading and voting by atomistic shareholders, that is, a setting in which the voting premium does not arise" (p. 1329). That is their own statement of how the two papers divide.
- **Data**: no new data. Table I aggregates 40 published studies covering 1940–2018 across many countries; the study-level detail sits in Internet Appendix Tables IA.I and IA.II.

## 5. Referee-facing strengths / weaknesses

**Strengths:**
- Clean single mechanism (trade moves the median voter, directly and by recomposing the base) that delivers positive, zero and negative voting premia from one model — the sign flip is a genuine test, not a knob.
- Sharp separation of *marginal* from *average* value of a vote, which maps one-for-one onto which empirical proxy a study uses; this is what makes the survey section bite.
- Explicit institutional anchoring of the empirical counterparts (dual-class pairs, record date, equity lending) with a quantitative survey table that the theory then sorts.
- Endogenous liquidity: price impact is derived, not assumed, and differs across share classes — a direct answer to the "voting shares are just less liquid" story that the empirical literature used as a residual explanation.
- Textbook top-journal architecture: institutional puzzle → one mechanism → propositions → measurement/implications section → conclusion listing five implications for future work.

**Weaknesses / open flanks:**
- The whole model runs on γ > γ̄, a cutoff defined only as "the maximum of the cutoffs used in each proof" (p. 1359). Everything qualitative — uniqueness, no short sales, σ(β) = 1 — is bought by "γ large enough," i.e. by the market being *illiquid enough*. Comparative statics in liquidity are therefore restricted to a region the paper never bounds numerically, and there is no calibration or numerical exercise anywhere.
- Proposition 3 does not characterize behaviour on β ∈ [β^L_non-mv, β^L_mv) or (β^H_mv, β^H_non-mv], where "the median voter can switch back and forth" (p. 1343) — a hole in the middle of the parameter space, patched only partially by Proposition 5.
- Three of the **eight** numbered results (Props. 4 and 5, Corollary 2) have their proofs in the Internet Appendix, as do all nine extensions. The published article proves Lemma 1, Propositions 1–3 and Corollary 1 only. (Corrected by verifier: the paper carries eight numbered results — Lemma 1, Props. 1–5, Cors. 1–2 — not six.)
- **(added by verifier)** Even two *baseline* properties are IA-dependent: Lemma IA.2 of the Internet Appendix is what guarantees that the blockholder cannot unilaterally veto or pass the proposal and that nobody short-sells (p. 1332). Neither is verifiable from the printed article.
- No private information at the trading stage: heterogeneity is preferences, not signals, so there is no adverse selection, no informed-trading motive, and no camouflage. That is exactly the machinery the Kyle/Maug tradition uses, and its absence means "liquidity" here is a trading-cost parameter, not noise-trader intensity.
- The blockholder moves first and small shareholders condition on y — the blockholder's trade is *observed*. There is no stealth accumulation and therefore no place for a disclosure rule to bind.
- Table I mixes samples, countries and decades; the authors concede the comparison "is only suggestive, since the samples differ across studies" (p. 1355) and that the ex-ante premium calculation "is obviously a back-of-the-envelope calculation" (fn. 41, p. 1357).
- No welfare statement about the level of γ (the planner's liquidity), and no policy margin at all.
- **(added by verifier)** They concede the upward-sloping supply curve that drives everything is not new to them: fn. 8, p. 1328 notes it "is also present in the takeover models with majority control of Stulz (1988) and Burkart, Gromb, and Panunzi (1998, 2006)". If our model has a takeover with an upward-sloping supply of shares, that is the lineage a referee will place us in, not LMM's.

## 6. What they do NOT do (scope boundary)

- **Object.** They price the *voting right embedded in a share* (dual-class premium, ex-record-date price drop, block premium, vote-lending fee). They do **not** study takeover premia, bidder entry, or activism campaign success. **(added by verifier — one qualification)** fn. 2, p. 1322 states that the framework "also captures cases in which the firm has a controlling shareholder but the corporate governance policy requires the majority of minority shareholders to approve the proposal" (Atanasov, Black & Ciccotello 2011; Gözlügöl 2021); so "no controlling shareholder" means no controlling shareholder *voting on this proposal*, not no controlling shareholder in the firm. This is stated as the paper's defining choice, twice: "a setting without takeovers or controlling shareholders" (abstract, p. 1321) and "We study how and why a voting premium emerges in the absence of takeovers or controlling shareholders, which is the most relevant setting in most major economies" (p. 1322). In the conclusion: "a positive voting premium arises even in the absence of takeovers and acquisitions of controlling stakes, so future studies should pay more attention to voting at shareholder meetings" (p. 1358).
- **Margin.** **No disclosure rule at all** — no 5% threshold, no filing window, no 13D, no Williams Act, no toehold rule. Stake disclosure appears exactly once, and only as motivation for an extension in which the *blockholder* is uncertain about small shareholders' biases because "small institutional investors and individual shareholders do not need to disclose their holdings" (p. 1354). The market's partition in our sense (flagged vs pooled) does not exist here: the blockholder's order y is observed by small shareholders by construction (p. 1331).
- **Identification.** Theory only. No estimation of their own; Table I is a survey of others' point estimates with no standard errors, no design, no causal claim. They explicitly do not attempt a systematic survey ("we do not attempt a systematic survey here", p. 1355) and note "We know of no study that provides rigorous estimates of the ex ante voting premium" (fn. 41, p. 1357).
- **Liquidity as a policy or exogenous variable.** γ is a primitive trading cost; the paper's liquidity result (R11) is about *endogenous* price impact differing across share classes, not about how a change in market liquidity changes governance. There is no comparative static of a control outcome in exogenous liquidity.
- **Private information / adverse selection / stealth accumulation.** Absent by construction; heterogeneity is preference-based (p. 1333 explains the finite-voter, private-information case is only a limiting justification via Feddersen–Pesendorfer 1997).
- **Coordination among blockholders**, empty voting via derivatives, and the endogenous emergence of the blockholder are all outside the frame (only multiple exogenous blockholders in the Internet Appendix).

**(added from IA by supplement reader — 100-page Internet Appendix, read in full.)**
- **The scope boundary holds at IA level, and harder.** Zero hits across all 100 IA pages for `noise trad`, `Kyle`, `market maker`, `13D`, `disclos`, `toehold`, `limits to arbitrage`. `takeover` appears five times: once in a footnote example (IA p. 11, antitakeover defences and the merger trade-off, copied from the body) and four times in the reference list. So **there is no disclosure rule and no microstructure anywhere in the 155 pages of body plus appendix.**
- **But `price impact` appears 18 times and `record date` 19 times in the IA** — the two concepts closest to our machinery are worked out at length there, not in the printed article. §IV.B (IA pp. 45–51) is a three-part dynamic-trading extension organised entirely around the record date: trade before the signal (B.1), after the signal (B.2), after the vote (B.3).
- **Exit is in the IA, and it is not what our draft assumes.** §III.A, IA p. 15–16, "Exit and a Positive Voting Premium": **Cor. IA.1** proves the blockholder may *sell* shares — giving up influence — while the voting premium stays strictly positive, because "selling diminishes the blockholder's ability to influence the vote outcome, he demands a premium from the small shareholders." Their words: "the tension between exit and voice (e.g., Hirschman (1970)) also exists in our model" and "a positive voting premium does not necessarily indicate a more concentrated ownership structure." **Exit and voice are already jointly modelled here.** Our exit/voice framing is therefore not whitespace on its own.
- **The bias β is microfounded four ways in IA §II (IA pp. 9–15)** — heterogeneous beliefs (A), heterogeneous time horizons (B), **private benefits of control (C, IA p. 14, an explicit Grossman–Hart (1980) asset-dilution setup: the blockholder diverts ψ after approval, giving β = ψ/(α+y) − ψ and small-shareholder bias b = −ψ)**, and monitoring / managerial agency costs (D, IA p. 14, β = π − k/(α+y)). This is the closest LMM come to our object: a control benefit, microfounded off the same paper (Grossman–Hart 1980) that our free-rider argument runs on. It is a *mapping*, not a control-outcome model — no bidder, no tender, no premium.
- **A liquidity result the card did not carry.** IA §IV.F, IA p. 63: with a passive (non-trading) fraction `1 − φ`, "the parameter for trading costs, γ, is replaced by γ/φ." Investor composition maps directly into the liquidity primitive, and eq. (35)'s price-impact discussion has to be restated because "price impact results only from the actively trading investors."
- **Three IA-only results with no counterpart in the body, all bearing on how we may talk about their premium:**
  - **Prop. IA.2 (§III.L, IA p. 38): the voting premium can be strictly positive *while the blockholder is the median voter*** — in the kink region `β ∈ (β_mv^H, β_non-mv^H]`, where he buys just enough to become the median voter and no more. This **qualifies R6** ("median voter ⇒ premium exactly zero"), which is stated without that caveat in the printed article. Lemma IA.4 (IA p. 38) softens it: as `γ → ∞` the kink interval shrinks to measure zero.
  - **Prop. IA.3 (§III.M, IA p. 40): a strictly negative voting premium even when the blockholder's stake is zero (`α = 0`)** — so the negative-premium result does not need an endowment.
  - **Prop. IA.1 (§III.B, IA p. 16): the voting premium increases in the heterogeneity of small shareholders** (a mean-preserving spread of `G`), for uniform `G`, `F` and `τ = ½`. The complement of Cor. 2, and the sharper form of the constraint in §7.5 below.
- **Two extensions the card's R-list omitted entirely:** §IV.G "Uncertainty about Biases" (IA pp. 66–68 — the blockholder does not know `G`; the equilibrium is fully revealing to small shareholders through the price, and the voting premium is a probability-weighted average of the state-by-state premia) and §IV.I "Vote Participation" (IA pp. 71–72 — turnout `ρ(b)` rising in `|b|`; the eq.-(28) decomposition survives, but the relative magnitudes of the three components change). Both are derivations, not propositions. **So the extension count is eleven, not nine.**

## 7. Implications for our position

**What it occupies, precisely:** object = *price of voting rights* (a valuation object, not a control outcome); margin = *none of the disclosure rule* — the closest institutional dial they touch is the **record date**, not a threshold and not a filing window; identification = *theory only*, with a literature-survey measurement section.

**Why this is friendly to a liquidity × disclosure-rule × control-outcome position:**

1. **It vacates our object and our margin.** LMM own the voting premium; we own the takeover premium / bidder entry / campaign success. They explicitly build the no-takeover case and tell the field to look at shareholder meetings instead (p. 1358). Our whitespace — how the *threshold margin* and the *window margin* of the disclosure rule change control outcomes as liquidity varies — is untouched by the three authors most likely to be our referees.
2. **It removes an easy referee objection.** A referee asking "isn't the takeover-premium story already the standard one?" now has LMM on record that the takeover channel accounts for only about a quarter of measured voting premia (pp. 1357–1358) — which is an argument that the takeover-and-control-outcome channel is *under*-modelled relative to its importance, not over-modelled.
3. **It sets the bar for what "liquidity" must mean in a v4 core model.** LMM's γ is a quadratic trading cost, and they show price impact is endogenous once voting rights are bundled (R11, eq. 35, p. 1347). If our κ is noise-trader intensity in a Kyle-type market, we should say in one sentence why our liquidity concept is the informational one (camouflage for accumulation, which is exactly what a disclosure rule destroys) and theirs is the cost one. Their result also warns us: any statement of the form "voting/flagged shares are less liquid" needs to be derived, not assumed.
4. **It is a usable template for the December package.** Structure to copy: institutional puzzle stated as three conflicting empirical facts → one mechanism → six numbered results → a *measurement* section that maps each empirical proxy to an object in the model → a conclusion that lists implications as instructions to empiricists. Their measurement section (§IV.E, pp. 1349–1352) and empirical-implications section (§VI, pp. 1355–1358) are the "closing implications" feature the positioning stage is looking for. Note also the taste signal: heavy machinery is *relegated* — nine extensions and three proofs live in an Internet Appendix so the printed article carries one mechanism.
5. **A constraint on our T2 / disclosure-attenuation claim.** LMM's Corollary 2 (p. 1346) says any preference component common to *all* small shareholders — explicitly including "monitoring, private control benefits" — produces **no** voting premium. If a v4 model wants to price disclosure through a valuation wedge, that wedge cannot come from a uniform blockholder-vs-minority conflict; it must come from heterogeneity or from an outside bidder. Our premium wedge (m₁ − m₀) is fine because it comes from an outside bidder, but this is the sentence to have ready.
6. **Citation duty.** Maug is a coauthor here and Maug (1998) is the classic our draft descends from; both papers must be cited, and our positioning should say out loud that LMM (2026) is the modern statement of the blockholder-trading-and-influence problem *without* control contests, and that we take the complementary case. **(added by verifier)** Two facts to use: Maug (1998) appears here only in fn. 11, p. 1329, as one of four "voice" antecedents they are departing from — so citing it is cheap for them and load-bearing for us; and LMM themselves draw the line between their two papers at p. 1329 ("Levit, Malenko, and Maug (2024), who analyze trading and voting by atomistic shareholders, that is, a setting in which the voting premium does not arise"). Use their own sentence when we place the pair.
7. **(added by verifier) The hardest constraint in the paper for a premium-wedge story is on p. 1325, not p. 1346.** LMM state flatly that the size of a price wedge is "unrelated to the blockholder's voting power" and can move *against* it. Any v4 claim of the form "the disclosure rule raises/lowers the premium, therefore it raises/lowers blockholder influence" is exactly the inference LMM spend their paper destroying. Our premium must be tied to a control *outcome* (bid succeeds / campaign wins), not used as a proxy for influence.

8. **(added from IA by supplement reader) Do not cite "no voting premium without trading frictions" as a proved result.** It is a prose sentence on IA p. 44, immediately after Prop. IA.4, and every existence/uniqueness result in the paper and the appendix is conditioned on `γ` being **above** a cutoff. The `γ → 0` limit is outside the region where their equilibrium is proved to exist. What *is* proved is the proportionality `VP = γσ(β)/(2γ+η) · MPV`. If our draft leans on "liquidity destroys the premium", cite the formula, not the sentence — and note that we would be extending their claim into a region they did not solve.
9. **(added from IA) Exit-and-voice is occupied; the disclosure partition is not.** IA §III.A (Cor. IA.1, IA p. 16) already has a blockholder who exits *and* commands a premium, with Hirschman cited by name. Our separation cannot be "we model exit as well as voice." It has to be that in LMM the blockholder's trade `y` is **observed by construction** (p. 1331) — there is no pooled state at all — whereas the entire content of a disclosure rule is that `y` is *hidden until a legal threshold is crossed*. That is the one primitive they never vary, in 155 pages.
10. **(added from IA) Their own control microfoundation is Grossman–Hart (1980) dilution (IA §II.C, IA p. 14).** When we place our free-rider/premium-wedge argument, we are in the same ancestry, one step further out: they map private benefits of control into a *bias parameter* and stop; we take the control outcome itself as the object. Saying this explicitly pre-empts "isn't this just their β relabelled?"

**Where they could push back on us:** they would ask (a) whether our liquidity concept is a trading cost or noise-trader intensity and whether the results survive both; (b) whether the disclosure rule is doing anything the record date does not already do; (c) whether our premium wedge is a reduced form where they microfounded theirs; (d) — the hardest — whether we need multiple actions (exit/hold/quiet/public) at all, given that they get positive, zero *and* negative premia out of a single continuous trade y. The v4 instinct to collapse the four actions is well supported by this paper.

## 8. Quotes we may lean on (verbatim, page-cited)

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "We develop a unified theory of blockholder governance and the voting premium in a setting without takeovers or controlling shareholders." | p. 1321 | Scope boundary: their object excludes takeovers |
| Q2 | "We study how and why a voting premium emerges in the absence of takeovers or controlling shareholders, which is the most relevant setting in most major economies." | p. 1322 | Their declared setting; our complement |
| Q3 | "We can therefore interpret γ as measuring the illiquidity of the market, that is, the inverse of γ reflects market depth." | p. 1334 | Their liquidity concept is a trading cost, not noise trading |
| Q4 | "where γ > 0 captures trading frictions, such as illiquidity, transaction costs, or wealth constraints, which limit shareholders' ability to build large positions in the firm" | p. 1331 | Same — exact primitive |
| Q5 | "Overall, this argument implies that liquidity, if measured by price impact, is endogenous in our setting and generally differs between voting and nonvoting shares." | p. 1325 | Endogenous-liquidity result; constrains our liquidity language |
| Q6 | "Moreover, (37) shows that the dual-class premium exists only if there are trading frictions (γ > 0). Such limits to arbitrage are necessary for a voting premium to emerge." | p. 1350 | No frictions, no premium — a modelling requirement we inherit |
| Q7 | "In practice, small institutional investors and individual shareholders do not need to disclose their holdings, so their preferences may be unknown." | p. 1354 | The paper's *only* engagement with holdings disclosure — a motivation, not a rule |
| Q8 | "The average ex ante voting premium accounts for only about one-quarter of the dual-class premium (6.08% compared to 22.49%). Hence, the takeover explanation probably explains only part of market premiums on voting shares." | p. 1358 | Quantifies how much the takeover channel leaves unexplained |
| Q9 | "First, a positive voting premium arises even in the absence of takeovers and acquisitions of controlling stakes, so future studies should pay more attention to voting at shareholder meetings." | p. 1358 | Their instruction to the field — and their handover of the takeover object |
| Q10 | "Any aspect of shareholder preferences that is common to all small shareholders and only creates a conflict between them and the blockholder (e.g., monitoring, private control benefits) is unlikely to lead to a voting premium." | pp. 1346–1347 | Constrains where a disclosure-driven price wedge can come from |
| Q11 | "By contrast, in our setting the blockholder exercises influence by affecting the identity of the median voter." | p. 1329 | Their mechanism in one line, contrasted with exit/voice |
| Q12 | "We analyze subgame perfect Nash equilibria in undominated strategies of the voting game." | p. 1332 | Equilibrium notion, for the competitor-set table |

## 9. Verification log

**Verifier:** opus, 2026-08-19. **Checked against:** a fresh `pdftotext -layout` extraction of
`lit/levit-malenko-maug-voting-premium-jf2026.pdf` (56 PDF pages; `pdfinfo` Subject = "The Journal
of Finance 2026.81:1321-1375"), page-tagged with printed page = PDF page + 1320 (running heads
confirm the map). Quote matching was done on a normalised copy (ligatures expanded, end-of-line
hyphens joined, whitespace collapsed), so a hit means the words are verbatim in the printed text.

**Counts: OK 30 · WRONG 1 · MISCITED 2 · UNCHECKED 8.**

### Quotes (§8)
| Q | Verdict | Checked against |
|---|---|---|
| Q1 | OK | Abstract, p. 1321 — exact |
| Q2 | OK | p. 1322 — exact |
| Q3 | OK | p. 1334 — exact |
| Q4 | OK | p. 1331, text after eq. (2) — exact |
| Q5 | OK | p. 1325 — exact |
| Q6 | OK | p. 1350 — exact, both sentences |
| Q7 | OK | p. 1354 — exact |
| Q8 | OK | p. 1358 — exact, both sentences |
| Q9 | OK | p. 1358, §VII Conclusion — exact |
| Q10 | OK | straddles pp. 1346–1347 with fn. 30 interleaved, exactly as the reader flagged; both halves verbatim |
| Q11 | OK | p. 1329 — exact |
| Q12 | OK | p. 1332 — exact |

### Results (§3) and model claims (§2)
- R1 (Lemma 1, p. 1333; proof p. 1359) — **OK**.
- R2 (Prop. 1, p. 1337 statement; proof pp. 1359–1361) — **OK** (card's "pp. 1336–1337" covers the run-up).
- R3 (Prop. 2, p. 1339 statement; proof from p. 1361) — **OK**.
- R4 (Cor. 1, p. 1340) — **MISCITED**: the proof is on p. **1368**, not p. 1370. Fixed in the table.
- R5/R6/R7 (Prop. 3, p. 1342; restated p. 1358) — **OK**; the un-characterised middle intervals are indeed acknowledged on p. 1343.
- R8 (§IV.D.1, pp. 1343–1344; ASSERTED) — **OK**, label right: no proposition, argued from Cor. 1 / Prop. 3.
- R9 (Prop. 4) — **MISCITED**: the proposition is printed on p. **1345**, not p. 1344 (p. 1344 carries §IV.D.3 and eqs. 31–32). Condition and content verified. Fixed.
- R10 (Cor. 2, p. 1346, discussion to 1347) — **OK**.
- R11 (eq. 35, §IV.D.4, pp. 1347–1348) — **OK**, and the alignment/conflict signs in the card match the print exactly.
- R12 (Prop. 5, p. 1348) — **OK**.
- R13–R19 (extensions, pp. 1350–1354) — statements **OK** where the body states them; the "can never overturn it" phrase for R18 is verbatim on p. 1354.
- R20 (Table I, p. 1355) — **OK**: every one of the 24 numbers and both study counts match the print exactly.
- R21 (p. 1357) — **OK** ("no less than 27" of 40).
- R22 — **OK** on numbers; the 6.08%/22.49% sentence is on p. 1358 (not 1357). Card range narrowed and fn. 40's *second* one-quarter estimate added.
- §2 model claims spot-checked against the print: eq. (1) p. 1330, eq. (2) p. 1331, eq. (4) p. 1332, FOSD of R over G p. 1335, eq. (19) MPC+MPV p. 1338, eqs. (25)–(26) p. 1340, eqs. (27)–(28) p. 1341 — all **OK**. One correction applied: α < min{τ, 1 − τ} is a separate assumption on p. **1332**, and the no-veto / no-short-sale guarantees come from **Lemma IA.2 of the Internet Appendix**, not from the printed article.
- **WRONG (1)**: §5 said "three of the **six** numbered results". The paper carries **eight** numbered results (Lemma 1, Props. 1–5, Cors. 1–2). Corrected.

### Scope claims (§6) — all confirmed by full-text search
Zero hits, anywhere in 56 pages, for: `13D`, `Williams`, `Schedule`, `toehold`, `business day`,
`filing`, `window`, `noise trad`, `market maker`, `adverse selection`. `5%` matches only inside
"45.3%"/"31.5%" (fn. 15). `threshold` occurs **once** (p. 1341) and refers to the *trade* cutoff ȳ,
not a disclosure threshold. `Kyle` occurs twice and both are Kyle (1989) on imperfect competition
among informed speculators — no Kyle (1985) microstructure. `disclos` occurs five times: twice in
the JF conflict-of-interest footnote (p. 1321), once at p. 1331 (management/proxy-advisor/analyst
*disclosures* as a source of the public signal — informational, not a holdings rule), once at
p. 1354 (Q7, the only holdings-disclosure mention), and once in a reference title (p. 1374). The
card's headline claim — **no disclosure rule, no threshold, no window, holdings disclosure once at
p. 1354 as extension motivation** — is confirmed. `numerical`, `calibrat`, `simulat`: zero hits;
Figures 1–4 are schematic, so §5's "no calibration or numerical exercise anywhere" is confirmed.
Venue/DOI/date claims confirmed from the front matter: DOI 10.1111/jofi.70037 (p. 1321), "Initial
submission: November 15, 2023; Accepted: January 12, 2025", editors as listed (p. 1359), and the
Internet Appendix is "Appendix S1" under Supporting Information (p. 1375).

### Proof location (decision-critical) — confirmed
p. **1371**, last line before REFERENCES: "We relegate the proofs of Proposition 4, Corollary 2, and
Proposition 5 to Sections III.I, III.J, and III.K of the Internet Appendix, respectively." The
printed Appendix (pp. 1359–1371) proves Lemma 1 (p. 1359), Prop. 1 (p. 1359), Prop. 2 (p. 1361),
Cor. 1 (p. 1368), Prop. 3 (p. 1368). Nothing else.

### Omissions found and added
1. **p. 1325 — the voting premium is not a measure of voting power**, and the relation can turn
   negative. Added as R19b. This is the sharpest constraint in the paper on any premium-wedge
   argument and the card did not carry it; also added as §7 point 7.
2. **p. 1329 — LMM's own line dividing this paper from LMM (2024)** ("a setting in which the voting
   premium does not arise"). Added to §4 and §7.6. Their sentence, not ours, is the one to cite.
3. **fn. 2, p. 1322** — the framework also covers a firm *with* a controlling shareholder when a
   majority-of-minority rule applies. Added to §6 as a qualification on "no controlling shareholder".
4. **fn. 40, p. 1357** — a *second, independent* one-quarter estimate ("about one-quarter of the
   voting premium could arguably be attributed to preferential treatment in takeovers"), derived
   from Maynes (1996), separate from the 6.08%/22.49% calculation. Added to R22.
5. **fn. 5, p. 1326** — Porras Prado, Saffi & Sturgess (2016): voting shares have higher limits to
   arbitrage than nonvoting shares. Added to §4.
6. **fn. 8, p. 1328** — the upward-sloping supply curve "is also present in the takeover models with
   majority control of Stulz (1988) and Burkart, Gromb, and Panunzi (1998, 2006)". Added to §5:
   this is the lineage a referee will place *our* takeover model in.
7. **Lemma IA.2 (p. 1332)** — two baseline properties (no unilateral veto, no short sales) rest on
   an Internet-Appendix lemma. Added to §5.

### UNCHECKED — the Internet Appendix is not in the repo
The following stand on the paper's own statements and could not be independently verified:
the PROVED labels on **R9 (Prop. 4), R10 (Cor. 2), R12 (Prop. 5)** and on **all nine extensions
R13–R19**; **Lemma IA.2** (no veto / no short sales); and the study-level detail behind Table I
(Tables IA.I and IA.II). Fetching Appendix S1 from the article's Wiley page is the only way to
close these. **Decision-critical among them: R12 (a strictly negative voting premium) and R13
(no premium without trading frictions, γ > 0)** — both are load-bearing for how we talk about
liquidity, and both rest on IA proofs.

**→ SUPERSEDED 2026-08-19: the Internet Appendix has been fetched and read in full. See §9b.
All items above are closed. R12 is PROVED (IA §III.K); R13 splits — the formula is PROVED, the
"no premium without frictions" reading is ASSERTED and sits outside the region where the model is
solved.**

**Overall verdict: the card is sound.** One wrong count, two page slips, no fabricated quote, no
overstated honesty label, and the three decision-critical scope claims (no disclosure rule; γ as a
quadratic trading cost with endogenous price impact at eq. 35; takeovers ≈ one quarter of measured
voting premia) are all confirmed verbatim against the print.

Reader's own notes for the verifier:
- Quotes were taken from a `pdftotext -layout` extraction of `lit/levit-malenko-maug-voting-premium-jf2026.pdf`, which is cleaner than `research/txt/voting_premium_jf2026.txt` (the latter has spacing artefacts such as a space before commas). Verify against the PDF, or against a fresh `-layout` extraction, not against the repo txt.
- Page assignment was computed from the running heads (`NNNN The Journal of Finance` on even pages, `The Voting Premium NNNN` on odd pages). Several quotes straddle a hyphenated line break in the printed text (Q7 "in-vestors", Q10 "share-holders"/"pre-mium", Q11 "exer-cises"); they are verbatim once end-of-line hyphenation is removed. Q10 also straddles the 1346/1347 page break, with footnote 30 interleaved.
- R9, R10, R12 and all extensions (R13–R19) are labelled PROVED on the strength of the paper's statement that the proofs sit in the Internet Appendix ("We relegate the proofs of Proposition 4, Corollary 2, and Proposition 5 to Sections III.I, III.J, and III.K of the Internet Appendix, respectively.", p. 1371). **The Internet Appendix is not in this repo and was not read.** If the verifier wants those labels independently confirmed, the IA must be fetched.

---

## §9b. Internet Appendix supplement — 2026-08-19 (opus supplement reader)

Source read in full: `research/txt_extracts/lmm_2026_internet_appendix.pdf` / `.txt`, 100 pages.
**Page convention: IA printed page = IA PDF page for pp. 1–6, and PDF + 2 thereafter** (verified against the page footers; the Table IA.I/IA.II section is separately numbered). IA pages below are printed IA pages and are *not* comparable to the article's 1321–1375.

**IA map as read** — §I empirical studies, Tables IA.I–IA.II (IA pp. 1–6) · §II microfoundations: beliefs / horizons / private benefits of control / monitoring (9–15) · §III supplementary analysis: A exit (15–16), B heterogeneity of small shareholders (16–19), C Lemma IA.1 median voter (19–23), D visual illustration (23), E Lemma IA.2 (24–25), F Lemma IA.3 concavity (26–27), G supplementary analysis for Prop. 2 (27–31), H supplementary analysis for Prop. 3 (31–34), **I proof of Prop. 4 (34–36)**, **J proof of Cor. 2 (36)**, **K proof of Prop. 5 (37–38)**, L positive premium with blockholder as median voter (38–39), M negative premium with zero stake (40) · §IV extensions: A dual-class (42–44), B dynamic trading B.1–B.3 (45–51), C vote trading (51–52), D multiple blockholders (52–56), E proxy advisors (56–61), F passive shareholders (61–66), G uncertainty about biases (66–68), H influencing management (68–71), I vote participation (71–72), J proofs for §IV (72–98) · references (99–100).

| Item that was UNCHECKED | Verdict | Where in the IA |
|---|---|---|
| **R9 — Proposition 4** (higher VP with higher small-shareholder payoff) | **PROVED**; the proof derives `W*`, then gives sufficient conditions for `∂W*/∂β > 0` and `∂VP/∂β > 0` on the same range | §III.I, IA pp. 34–36 |
| **R10 — Corollary 2** (homogeneous small shareholders ⇒ VP = 0) | **PROVED**; five lines — `x = −y`, the median voter is a small shareholder regardless of the blockholder's vote, `∂(−q*)/∂y = 0`, so VP = 0 by eq. (28) | §III.J, IA p. 36 |
| **R12 — Proposition 5** (strictly negative VP) | **PROVED**; reaches `MPV^L(y*, β) < 0` hence "the voting premium is also strictly negative", *and* `y* > 0` (the blockholder buys) | §III.K, IA pp. 37–38 |
| **R13 — dual-class premium** | **SPLIT.** The formula (eq. IA.65, `p*_voting − p*_nonvoting = γσ(β)/(2γ+η)·MPV(y*, ŷ*)`) is **PROVED** (Prop. IA.4, proof IA pp. 72 ff.). "**Exists only if γ > 0 / limits to arbitrage are necessary**" is **ASSERTED** — prose on IA p. 44, no proposition, and the whole model is solved only for `γ` above a cutoff, so `γ → 0` is unproved territory. **Label changed in §3.** | §IV.A, IA pp. 42–44 |
| **Lemma IA.2** (no unilateral veto, no short sales) | **PROVED**; (i) `|y*| < ε` for `γ` large, hence `y + α < min{τ, 1−τ}` and `y > −α`; (ii) `x*(b) + 1 − α > 0` for all `b` | §III.E, IA pp. 24–25 |
| **R14** ex-record price drop (§IV.B.1) | **PROVED as a derivation**, no numbered proposition: "Proposition 2 continues to hold" with `MPV → M̂PV`, `σ → σ̂`; yields `p*₁ − p*₂ = γσ̂(β)/(2γ+η)·M̂PV(y*₁)` | IA pp. 45–48 |
| **R15** vote trading (§IV.C) | **PROVED** — Prop. IA.5 (IA p. 52), proof IA p. 84. Refinement: the zero vote price is immediate (small shareholders never pivotal, IA p. 51); the proposition proves the *share* premium stays strictly positive when `λ_max < λ̄` and `β` is extreme | IA pp. 51–52, 84 |
| **R16** multiple blockholders (§IV.D) | **PROVED** — Props. IA.6 (IA p. 54) and IA.7 (IA p. 55), proofs IA pp. 93, 95. The `N → ∞` vanishing is stated for `β > E[b]` | IA pp. 52–56 |
| **R17** proxy advisors (§IV.E) | **PROVED as a derivation**, no numbered proposition; the "advisor becomes the median voter ⇒ jump in support ⇒ zero marginal ability ⇒ VP = 0" argument is at IA p. 59, and the ambiguity of the net effect is spelled out at IA pp. 59–61 | IA pp. 56–61 |
| **R18** passive shareholders (§IV.F) | **PROVED as a derivation**, no numbered proposition; mechanism explicit — `γ` becomes `γ/φ` (IA p. 63), and the direct/indirect effects can now have opposite signs (IA p. 64) | IA pp. 61–66 |
| **R19** influencing management (§IV.H) | **PROVED** — Prop. IA.8 (IA p. 70), proof IA p. 87; the influence premium has the same three-factor form (eq. IA.109) | IA pp. 68–71, 87 |
| Table I study-level detail (Tables IA.I, IA.II) | **Present**, IA pp. 1–6 (not re-tabulated here; the article's Table I aggregates them) | §I |

**Everything the article attributes to the Internet Appendix is there and reaches the stated claim. One label change (R13) and three "derivation, not proposition" downgrades (R14, R17, R18) — none of which weakens the substance.**

**Material additions made from the IA** (all marked in place in §6 and §7):
- **§III.A Cor. IA.1 (IA p. 16) — exit *and* a positive voting premium**, Hirschman cited. Exit/voice is occupied; our separation must be the disclosure partition (their `y` is observed by construction, p. 1331).
- **§II.C (IA p. 14) — private benefits of control microfounded as Grossman–Hart (1980) asset dilution.** Same ancestry as our free-rider argument, one step short of a control outcome.
- **§IV.F (IA p. 63) — `γ → γ/φ` with passive shareholders**: investor composition maps straight into the liquidity primitive.
- **§III.L Prop. IA.2 (IA p. 38)** — a strictly positive premium *with* the blockholder as median voter (kink region); **qualifies R6**. **§III.M Prop. IA.3 (IA p. 40)** — negative premium with a zero stake. **§III.B Prop. IA.1 (IA p. 16)** — the premium rises in small-shareholder heterogeneity.
- **Two omitted extensions restored**: §IV.G uncertainty about biases (IA pp. 66–68) and §IV.I vote participation (IA pp. 71–72). The count is **eleven** extensions, not nine.
- **§7.8** — a warning not to cite "no premium without trading frictions" as proved.
- Negative-search evidence at IA level (zero `noise trad`, `Kyle`, `market maker`, `13D`, `disclos`, `toehold`), plus the counterweight that `price impact` (18) and `record date` (19) are heavily worked *in the IA*.
