# Lit Brief — Strand: theory-to-empirics-templates
**Researcher:** LitResearcher_TheoryToEmpiricsTemplates
**Question:** What template do recent JF/RFS/JFE(/Econometrica/RAPS) papers use when they are PRIMARILY THEORY but anchor the model institutionally or empirically — and what should our blockholder paper (Exit/Voice/disclosure/takeover premia) borrow?

## Access log (honesty)
| Paper | Access | Read |
|---|---|---|
| Back, Collin-Dufresne, Fos, Li, Ljungqvist (2018, *Econometrica* 86(4):1431–1463) | local `lit/Back-ACTIVISMSTRATEGICTRADING-2018.pdf` | **full text** |
| Corum & Levit (2019, *JFE*) "Corporate Control Activism" | local `lit/corum-levit-2019.pdf` | **full text** |
| Johnson & Swem (2021, *JFE* 139:29–56) | local `lit/johnson-swem-2021-jfe.pdf` | **full text** |
| Burkart & Lee (2022, *RFS* 35:1868–1896) "Activism and Takeovers" | local `lit/hhab039.pdf` — **NB: this file is Burkart–Lee, NOT Edmans–Goldstein–Jiang as the assignment stated** | **full text** |
| Albuquerque, Fos & Schroth (2022, *JFE* 145:153–178) | local `lit/albuquerque-fos-schroth-2022-wp.pdf` (ECGI WP 685/2020 = published JFE version's twin) | **full text** |
| Celentano & Levine (2025 WP, Oct 2025) "Shareholder Activism, Takeovers, and Managerial Discipline" | local `lit/celentano-levine-2025-ssrn.pdf` | **full text** |
| Gantchev (2013, *JFE* 107:610–631 — **not JF** as assignment stated) | paywalled (ScienceDirect/Wiley/SSRN all bot-blocked in shared browser; SMU/SSRN PDF curls blocked) | **verified, NOT full text**; characterization from abstract + detailed in-text descriptions in Johnson–Swem §2/§5.1 and AFS §1 |
| Edmans, Goldstein & Jiang (2012, *JF* 67:933–971 — **not RFS** as assignment stated; pre-window) | paywalled (Wiley Cloudflare) | **verified, NOT full text**; from abstract + Bond–Edmans–Goldstein (2012, *Annu. Rev. Financ. Econ.*) design summary |

No bluffing: the two pre-2015 ancestors were confirmed bibliographically but could not be opened; everything else was read cover to cover.

---

## 1. Back, Collin-Dufresne, Fos, Li & Ljungqvist (2018, *Econometrica*) — "Activism, Strategic Trading, and Liquidity"

**Question / summary.** How does market liquidity interact with activism and firm value when an activist's private information is her *own stake* (hence her own intentions)? Continuous-time Kyle model with a strategic trader who expends costly effort to move the terminal value.

**Model architecture.** One strategic trader (potential activist), noise traders (Brownian cumulative demand Z_t, vol σ), competitive risk-neutral market makers. Trader's initial stake X₀ ~ N(μ_x, σ_x²) known only to her. At fixed horizon T the activist chooses value v at cost C(v) (general, lower-semicontinuous, superlinear at extremes); G(x)=sup_v{xv−C(v)} is convex; V(x)=G′(x) is the post-action share value. Trading continuous on [0,T]; equilibrium = price rule P(t,Y_t)=E[V(X_T)|order history] + trading strategy θ. **Closed form**: trader's strategy is independent of C (linear in X and Y); X_T = μ_x + ΛY_T with Λ from a generalized Brownian-bridge construction. Equilibrium concept: Kyle-style (inconspicuous insider trading + price = marginal value at T).

**Key results (all proven analytically).** Thm 1: closed-form equilibrium, λ(t,y) martingale. Thm 2: comparative statics depend on convexity of V — noise trading ↑ efficiency iff V convex; expected initial stake ↑ efficiency but ↓ liquidity if V convex; etc. Five examples (quadratic, asymmetric quadratic, exponential, binary à la Maug 1998, probabilistic binary) with full comparative-static tables; increase in noise trading can *reduce* market liquidity (activist trades against noise ⇒ more uncertainty about her block). Numerical content: only illustrative simulated paths (Figs 1–2) and one parameter-region plot (Fig 3). **Zero original empirics.**

**Institutional anchoring (the template payload).** (i) 13D 5% threshold and the pre-disclosure window as the model's T, with explicit mapping: "reducing the trading horizon T is isomorphic to reducing noise trading volatility" — the Bebchuk–Brav–Jackson–Jiang (2013) 10-day debate becomes a comparative static in σ²T; (ii) 13(f) quarterly disclosure as noisy signals of toehold; (iii) calibration anchors from data: Collin-Dufresne–Fos (2015a) average 13D-filer stake 7.51% (8.70% with derivatives), used to argue costs-per-share are small; (iv) Brav et al. (2008) campaign-goal taxonomy used to motivate the "general activism technology." The conclusion explicitly lists as future work: **"we assume the horizon at which the activist's stake is disclosed is fixed… it might be interesting to endogenize the horizon… activists have to disclose their stake when it reaches a regulatory threshold of 5%"** — a direct opening for our paper.

**Referee-facing strengths/weaknesses.** Strength: maximal generality with closed form; every comparative static proven; honesty about what depends on functional form. Weakness (for a finance-5 journal): no data section at all; results' signs flip with unobservable technology curvature (V′′), which referees could call untestable — they convert this into a *feature* (pooling across campaign types can yield null results).

**Implications for us.** Borrow: (a) the "one friction, one private state variable" discipline — their ONLY asymmetry is the stake; (b) the parameter→policy mapping table (T ↔ window, σ ↔ anonymous trading volume); (c) prove comparative statics by convexity cases rather than full characterization. Differentiate: we endogenize the disclosure event (threshold crossing) and add bidder entry — precisely their stated gaps.

---

## 2. Corum & Levit (2019, *JFE*) — "Corporate Control Activism"

**Question / summary.** Why do activists, not bidders, launch proxy fights to unseat resisting boards? Because a bidder who wins board seats faces a commitment problem (shareholders expect him to low-ball the deal once in control), while a sell-side activist is credible. Activism and takeovers are complements: activists put firms "into play," bidders free-ride on that.

**Model architecture.** Baseline: bidder negotiates with entrenched incumbent board (private benefits B, per-share b); two bargaining rounds (random proposer, prob s = board) separated by a proxy-fight stage (cost χ to challenge; majority vote elects rival slate); elected rival cannot commit to act for shareholders (can divert ε). SPE in pure strategies, backward induction. Extension (§4): activist builds toehold α via a **static Kyle (1985) trading block** (noise demand L or 0, market maker sets price = standalone value + expected takeover premium), activist has private signal y about synergy Δ~F; bidder observes activist presence (e.g., via 13D filings) and decides whether to pay due-diligence cost c before negotiating. PBE with two refinements stated explicitly.

**Key results (all proven).** Prop 1–2: only activists can credibly challenge incumbents; bidder's commitment problem. Prop 3: existence/uniqueness conditions for equilibria with α*(1)>0 — keyed on h(2L)/h(L), the marginal effect of stake on expected premium; **if the activist's stake fully prices its effect, she earns nothing and abstains** (cut-and-run logic very close to our exit branch). Corollary 2: partitions equilibrium into selection vs treatment regions. **Prop 4 (the identification gem): if only selection, takeover probability strictly decreases in agency severity b; if treatment, it is NON-MONOTONE in b** — a sign-flip comparative static offered explicitly as an empirical identification strategy. Extensions: deal-jumping, MBOs, tender-offer substitution, cross-jurisdiction prediction (weaker board-blocking power ⇒ smaller activist role — UK vs US).

**Institutional anchoring.** Fos (2016) proxy-fight census (632 fights 2003–2012: 5% corporations, 70% hedge funds); KKR–Gardner Denver–ValueAct case with the George Roberts quote; Sotheby's two-tier anti-activist pill (Third Point LLC v. Ruprecht, Del. 2014); classified-board decline (57%→11% of S&P 500, 2003→2013); Delaware board-veto/poison-pill mechanics; Boyson et al. (2016): 70% of bids within 2 years of campaign start.

**Referee-facing strengths/weaknesses.** Strength: answers a puzzle the data literally poses (why activists run fights); every extension answers a likely referee objection. Weakness: reduced-form proxy-fight success; no empirics of its own; the Kyle block is separate from the bargaining block (prices in one, agency in other) — a referee could ask for integration (our paper does integrate disclosure into trading).

**Implications for us.** This is the closest architectural cousin: Kyle toehold + post-disclosure control contest. Borrow the *identification-by-non-monotonicity* device (Prop 4) — it is exactly how to present our hump-shaped-premia result (R1): a sign-flip is more falsifiable than a level. Note they explicitly abstract from GH free-riding and from information asymmetry about q and Δ to keep ONE friction (commitment) — license for us to collapse our action menu.

---

## 3. Johnson & Swem (2021, *JFE*) — "Reputation and Investor Activism: A Structural Approach"

**Question / summary.** Why do targets settle so often, and why do activists fight despite free-rider costs? Answer: reputation for proxy fighting. Estimate a dynamic Kreps–Wilson-style reputation model by MLE on 2,434 hedge-fund campaigns (1999–2016).

**Architecture (model).** Stage game: activist gets Poisson(λ_c) campaign opportunity → 13D/Ignore (cost L̃) → manager Settle/Refuse → Fight/Fold (costs F̃_A, F̃_M). Two activist types (aggressive/cautious, differ in μ_A); reputation r_t = P(aggressive | track record) evolves via Bayes + type resets (Poisson λ_r). Log-normal cost shocks make all outcomes interior. Dynamic: activist internalizes effect of current actions on future r_t through value functions V^i(r). Static (no-reputation) benchmark solved in closed form for comparison.

**Estimation / identification (the template payload).** §3.6 "Identification in the model" is THE exemplar: parameter-by-parameter, each is tied to a *distinct* comparative static of an observable relation (level vs slope of r_t→13D/year, r_t→P(Settle), r_t→P(Fight), reputation-updating moments, decay moments), illustrated with comparative-static figures; Table 3 reports elasticities of each moment to each parameter — "no single moment identifies a parameter; the full joint distribution does" (informal overidentification). MLE with closed-form likelihood (4-step: solve equilibrium → compute daily r_t → per-campaign likelihood from gap/13D/CAR/outcome components → sum). Δ identified ONLY through announcement CARs (E[payoff|13D]=Δ·P(project occurs)) — market data pins the value scale. Hypothesis tests: LR rejection of no-reputation (χ²=340) and full-information (χ²=21) nested alternatives. Validation: reduced-form regressions of outcomes on model-generated r_t with simulated null distributions; honesty about misfit (proxy-fight slope too weak, CAR slope weaker than model).

**Results (estimated).** High-reputation activists: 3.5 campaigns/yr vs 0.6; settle 44% vs 29%; 20% of campaigns and 19% of fights are reputation investments (loss-making standalone); removing reputation halves target shareholder gains. Costs: campaign mean 5.44% of stake, fights 8.68%/19.44% by type — compared head-to-head with Gantchev (2013).

**Institutional facts.** 13D filing = campaign initiation marker (10-day rule); proxy fights identified from DFAN14A/DEFC14A etc.; settlements unobservable ⇒ inferred from 5 target actions (reorg, payout, CEO, board, M&A) from Capital IQ/SharkWatch/Compustat, with â_i from predictive regressions on the whole Compustat universe to handle selection; wolf-pack campaigns collapsed to lead activist.

**Strengths/weaknesses.** Strength: the model's data limitations are built INTO the model (targets see what econometricians see) — estimation is internally consistent. Weakness: heavy parametric assumptions (log-normal costs, δ=0.9 and λ_c=10 fixed because unidentified); settlements are model-imputed; hedge-fund-only external validity.

**Implications for us.** If we ever structurally estimate, §3.6 is the format: an identification section organized parameter-by-parameter around observable-relation slopes, plus nested-alternative LR tests, plus validation on untargeted dimensions. For a theory-first repositioning, cite them for escalation costs and settlement frequency (27% baseline) — useful calibration anchors for voice-branch payoffs.

---

## 4. Burkart & Lee (2022, *RFS*) — "Activism and Takeovers"  *(this is the paper in `lit/hhab039.pdf`)*

**Question / summary.** Compare activism vs takeovers as governance interventions by the same blockholder under the SAME technology. Dual free-riding (Jensen–Meckling on effort benefits; Grossman–Hart on tendered shares) makes activism more profitable than takeovers precisely when takeovers are more efficient; "takeover activism" (campaign to force a merger) combines the best of both.

**Model architecture.** Single toehold owner t < 1/2; continuum of atomistic shareholders. Continuous effort e, value improvement V(e,θ), cost C(e), SAME for both modes ("level playing field"); only control acquisition differs: buy (tender offer, BGP-1998-style restricted offer, free-rider condition p ≥ V*(s_b,θ), majority requirement 1/2) vs work (reduced-form campaign: success prob q(a,ψ,s), cost K(a) — microfoundations from Brav et al., Maug–Rydqvist, Gantchev 2013 relegated to Internet Appendix). Takeover activism: successful activist negotiates merger with third-party bidder (full bargaining power), bidder buys 1−t_b, legal risk ε (Müller–Panunzi) restores partial free-riding. All proofs by concavity + envelope/IFT — no fixed points, no numerics beyond one illustrative figure.

**Key results (all proven).** Lemma 2 (BGP analog): bidder buys exactly to 1/2, pays full post-takeover value — "unrecompensed effort." Props 1–3: bidder profits DECREASE in θ for small toeholds while activist profits INCREASE — opposite-sign comparative statics from the two free-rider forms; activism more profitable though less efficient when θ high, toeholds/campaign costs low. Lemma 4/Prop 4: takeover activism dominates both modes for low legal risk. Prop 5 + Corollaries 1–2: free-riding on tender offers doesn't kill takeover activism but creates a selection effect ⇒ takeover activism should earn *excess* returns; higher campaigning efficacy ψ raises total M&A but reduces hostile bids.

**Mapping predictions to data (template payload).** No original empirics, but: intro lists **four numbered testable predictions**; each proposition is immediately confronted with existing evidence (Greenwood–Schor 2009 and Becht et al. 2017 on takeover-activism returns; Brav et al. 2008 / Boyson–Mooradian 2011 on M&A as campaign objective; Betton–Eckbo–Thorburn 2008 Fig 9 trends for Corollary 2); institutional facts as calibration anchors (Gantchev 2013: $10.5M avg campaign cost ≈ 1/3 of gross return; Brav–Jiang–Kim 2010: 52.4% success; Cain–Solomon 2014: litigation on 97.5% of >$100M deals motivates ε>0; Holderness 2009 blockholder prevalence); practitioner quotes (Icahn manifesto, Orol 2008 on "Trojan horse" toehold deals). Robustness (multiple blockholders, discrete shareholders, timing of effort, bargaining power) all in Internet Appendix with one-paragraph summaries in text.

**Strengths/weaknesses.** Strength: maximal conceptual clarity per page; the "same V,C, only control differs" device kills all confounds; every claim proven. Weakness: reduced-form q(·); no stake-building stage (explicitly disclaimed: **"we do not endogenize the acquisition of the toehold in anonymous, predisclosure markets… We leave an analysis of how predisclosure and post-disclosure decisions interact to future work"** — again, our paper's exact gap); efficiency statements are partial-equilibrium.

**Implications for us.** This is the best pure-theory template for our target journals. Borrow: (i) level-playing-field comparisons across our Exit/Quiet/Public branches (same information, same primitives, differ only in the disclosure/inference regime); (ii) one driving parameter with opposite-sign effects (their θ; ours: κ or the disclosure threshold τ); (iii) a numbered "Testable predictions" list + per-proposition mapping to published evidence; (iv) robustness exiled to appendix with in-text summaries. And cite their gap statement as motivation.

---

## 5. Albuquerque, Fos & Schroth (2022, *JFE* 145:153–178) — "Value Creation in Shareholder Activism: A Structural Approach"

**Question / summary.** Decompose 13D announcement returns into treatment (activism value), stock picking, and sample selection, by modeling the investor's 13D-vs-13G filing choice.

**Architecture.** Static: investor with a stake chooses filing type. Returns Δ_D = μ_D + ε, Δ_G = μ_G + ε (normal); due-diligence signals s_j = Δ_j + noise; private cost C; file 13D iff E[U_D] > E[U_G]. Econometrician observes filing choice + announcement return (CAR −30/+10, wide window because Collin-Dufresne–Fos 2015 show pre-filing run-up from activist trading). Closed-form truncated-normal selection: E(Δ_D|z>0) = μ_D + ρσλ(α) (inverse Mills) ⇒ three-way decomposition.

**Estimation/identification.** ML on joint distribution of {choice, return} with μ_D = x′β_D, μ_G = x′β_G linear in firm + investor-experience characteristics. Identification: cross-equation restriction — the SAME loadings drive choices and returns; C identified by trading off selection amounts across the two subsamples (FOC equates weighted inverse Mills ratios); FOCs shown to be OLS-orthogonality + selection correction. Sample: ALL EDGAR 13D/13G 1996–2017 (69,937 filings; 8,703 13D) merged to CRSP/Compustat; Feb-14 13G filings dropped (exempt, uninformative — a nice data-cleaning-as-identification detail). Results: treatment 75.2% / picking 12.2% / selection 12.6% of the 6.34% mean 13D CAR; C ≈ 4.6% of stake (≈$2.43M); net activist return 1.73%. Validation: estimated Treatment predicts future ΔROA and Δsales-turnover beyond CAR, and predicts LOWER proxy-contest probability; hedge-fund subsample re-estimation (treatment 92.4%); comparison vs probit/OLS/Heckman two-step (structural wins on choice distribution). Counterfactual: cost-sharing ⇒ 60% of 13Gs would be 13Ds, $60B/yr upper-bound gains.

**Strengths/weaknesses.** Strength: the institutional choice (13D vs 13G) IS the model — maximal institutional leverage per equation; parsimony defended explicitly (C constant "to keep the model parsimonious… performance of the model is the test"). Weaknesses a referee attacks: static, no equilibrium price formation; announcement return ≡ value creation assumption; normality; C net of everything unobserved.

**Implications for us.** (i) Proof that a 2-decision institutional discrete choice (theirs: D vs G; ours: disclosed vs non-disclosed branch / public vs quiet voice) can carry a JFE paper when the choice maps to observables. (ii) The validation-via-future-outcomes device (Treatment → future ROA) is how to validate our model-implied "inferred vs disclosed" premia split. (iii) Their estimate that illiquidity loads POSITIVELY on expected returns for BOTH filing types (illiquidity premium, contra Edmans–Fang–Zur) is a fact our liquidity-premia relation must confront. (iv) Our empirics/ EDGAR pipeline can replicate their sample construction at low cost.

---

## 6. Celentano & Levine (2025 WP) — "Shareholder Activism, Takeovers, and Managerial Discipline"

**Question / summary.** Quantitative dynamic equilibrium model with BOTH activism and M&A: does activism complement or crowd out takeovers, and how much value comes from threat vs actual campaigns? SMM estimation, 2001–2019.

**Architecture.** Infinite-horizon discrete time. Firm: π = zk^α − c_k·k; log-AR(1) productivity + effort·project-quality increment (p ~ Exp(λ_p)). Activist gets private signals on project quality and acquirer quality (w ~ Exp(λ_w)), chooses entry ν∈{0, ν̄} at cost ξ; **ν̄ set to the statutory 5% 13D threshold** — institutional parameter used as a model primitive. Manager effort vs private cost; board turnover decision with entrenchment cost c_f(ν) ↓ when activist present; takeover by Nash bargaining with board entrenchment c_m(ν) ↓ with activist; Type-I-extreme-value preference shocks for interior discrete choices. Post-entry, signals become public.

**Estimation/identification.** SMM: 12 parameters, 15 moments. Identification section walks moment-by-moment (asymmetric sales-persistence regression coefficients ρ⁺/ρ⁻ identify effort cost; turnover frequency → c_f(0); turnover-in-campaign → c_f(ν̄); bid premium mean (conditional and unconditional) → c_m(0), c_m(ν̄); entry CAR → ξ; takeover-in-campaign frequency → signal noise σ_w; etc.); Internet Appendix reports full elasticity matrices. Calibrated upfront: α=0.7, β=0.952, bargaining θ_a=0.5, CEO pay share from Equilar, **stake = 5%**. Validation on UNTARGETED dimensions: kernel densities of target performance (data vs simulated), bid-premium histogram. Event-attribution rules (turnover/bid within 2 years of 13D = campaign consequence, Boyson et al. 2017) stated as data construction.

**Results.** Campaign ↑ takeover prob 7.7pp but ↓ bid premium 13.7% (5.2pp) — facilitation benefits accrue to acquirers; effort-incentive channel worth 0.35% shareholder value/campaign; equilibrium threat of activism worth 0.33% to ALL firms; crowding-out of M&A ≈ 0.8% of volume; 76% of the 4.1% entry CAR is private information about takeovers (selection), 14% about projects — direct tension with AFS's 75% treatment, discussed honestly.

**Strengths/weaknesses.** Strength: equilibrium threat effects computable only structurally — a clear raison d'être for structure; confronts AFS head-on. Weakness: heavily parameterized (12 params, distributional assumptions everywhere); reduced-form "technologies" (activism = cost shifters c_f(ν), c_m(ν)); no microstructure at all — prices are just present values; year-level timing.

**Implications for us.** (i) This is the state of the art in the *quantitative* activism–M&A niche we must cite and differentiate: they have no trading, no disclosure event, no liquidity — our margin (how the market LEARNS, and how disclosure rules shape inference and premia) is orthogonal and complementary. (ii) Their bid-premium definition (bid / price 25 days pre-bid, adjusted if intervening events) and activist-entry CAR window (−30/+1) are reusable measurement conventions. (iii) The "two countervailing channels → near-zero net effect" finding style is a cautionary template for presenting our hump: be explicit about which forces dominate where.

---

## 7. Verified but NOT fully read (paywalled/bot-blocked)

**Gantchev (2013, *JFE* 107:610–631)** — "The Costs of Shareholder Activism: Evidence from a Sequential Decision Model." The ancestor of all structural activism papers. Model: activism as a sequential decision tree (demand negotiations → board representation → proxy contest) with stage-specific costs; estimated on ~1,164 campaigns by 171 hedge funds. Headline estimates: average cost $10.71M for campaigns ending in proxy fights ($10.5M cited in Burkart–Lee as ~1/3 of gross campaign return); monitoring costs reduce activist returns by >2/3; mean net activist return ≈ 0 (annualized market-adjusted ≈ 4%); top quartile earns more on activist than non-activist holdings. Template note: a *statistical* sequential model (no strategic counterparty equilibrium — Johnson–Swem §2 contrasts precisely this) whose staged structure delivers identification of unobservable stage costs from observed stage transitions and outcomes. Lesson: even the canonical "model + estimation" activism paper keeps the model to a decision tree with three stages.

**Edmans, Goldstein & Jiang (2012, *JF* 67:933–971)** — "The Real Effects of Financial Markets: The Impact of Prices on Takeovers." Structure: a short model generating two opposing forces — the *trigger effect* (low price attracts bids; negative price→takeover relation) and the *anticipation effect* (prices rise in anticipation of bids, biasing OLS toward zero/positive) — then empirics: mutual-fund-redemption-induced price pressure (Coval–Stafford style instrument) identifies a strong negative causal effect: interquartile valuation decrease ⇒ +7pp takeover likelihood vs 6% unconditional; overturns the prior non-instrumented literature. Template note: this is the canonical **"small model that organizes the empirics"** design — the theory's job is (a) to produce the anticipation-effect bias story explaining why OLS fails, and (b) to deliver one signed prediction for the IV. Our bidder-entry block is exactly the microfoundation of their trigger effect; cite as such.

---

## Cross-paper template synthesis

**Fractions (main text, excluding appendices).**
- Pure theory + institutional anchoring + evidence mapping: Back et al. (~100/0), Corum–Levit (~100/0), Burkart–Lee (~100/0, plus 4 numbered predictions).
- Structural/quantitative: Johnson–Swem ~35% model / 65% estimation+validation; AFS ~40/60; Celentano–Levine ~25/75; Gantchev ~40/60.
- EGJ: ~15% model / 85% empirics.
- **The missing middle is real**: in-window top-5 activism papers do NOT staple a casual event study onto a theory model. The viable hybrid is either (a) pure theory with dense institutional anchoring + explicit prediction-mapping, or (b) full structural commitment. A 70/30 theory + "some suggestive empirics" paper is the weakest position at these journals.

**How predictions are mapped to data (devices, in order of increasing commitment).**
1. *Calibration anchors in footnotes/text*: Gantchev's $10.5M, CDF's 7.51% average stake, Brav et al. success rates (Back et al., Burkart–Lee).
2. *Parameter→policy isomorphism*: 13D window shortening ≡ ↓σ²T (Back et al. Discussion); proxy-access easing ≡ ↓χ (Corum–Levit).
3. *Numbered testable predictions* matched to published findings (Burkart–Lee intro; Corum–Levit Prop 4 as identification strategy).
4. *Institutional choice as empirical lever*: 13D-vs-13G filing choice (AFS); 13D filing as campaign-initiation marker (Johnson–Swem); stake = 5% statutory threshold as a *calibrated primitive* (Celentano–Levine).
5. *One clean quasi-experiment for the one signed prediction* (EGJ's mutual-fund-redemption IV).

**How the theory was kept simple (recurring devices).**
- ONE friction, stated and defended: own-stake asymmetry only (Back); commitment problem only, GH free-riding and asymmetric information explicitly switched off (Corum–Levit); dual free-riding with identical V,C across modes (Burkart–Lee).
- Reduced-form subgames with microfoundations in appendix: Burkart–Lee's q(a,ψ,s); Corum–Levit's h(α).
- Continuous effort replacing binary action (Burkart–Lee §1 shows binary effort makes activism/takeover profits *equal* — the richness IS the result; generalizing the binary action space is what creates the economics).
- Comparative statics in ONE parameter with sign flips (θ; b; σ) rather than full characterization.
- Existence/uniqueness: closed form (Back), concavity+IFT (Burkart–Lee), constructive PBE with explicit selection (Corum–Levit). **None of the successful theory papers makes uniqueness a headline** — Brouwer-level existence + numerical uniqueness is socially acceptable IF the headline comparative statics are proven.

**Referee attack patterns to preempt.** (i) "Your central result is only numerical" (fatal if the hump is the headline; survivable as a secondary, clearly-labeled numerical result — cf. our honesty-label convention). (ii) "Too many moving parts" — four action branches is more than ANY template above. (iii) "Empirics without exogenous variation" — only acceptable as stylized-fact anchoring, never as "tests," unless a real shock is used.

---

## Recommended template for our paper

**Recommended architecture: the Burkart–Lee / Corum–Levit pure-theory-plus-anchoring template (≈85–90% theory), with (a) a numbered testable-predictions section, (b) one compact "institutional facts + feasibility" empirical section built on the project's existing EDGAR 13D/G pipeline, and (c) ONE clean empirical leverage point reserved for the disclosure-attenuation theorem. Do NOT attempt Johnson–Swem/AFS-style structural estimation — our fixed-point microstructure model has no closed-form likelihood, and a weakly-identified SMM would invite the worst referee fight.**

**What to cut (theory).**
1. Collapse the four-branch action space (Exit / Hold / Quiet Voice / Public Voice) to at most three: every template above has ONE decision margin plus at most one mode choice. Exit vs Hold can be a single trading decision (sell down vs keep stake); the voice margin should be binary (public/disclosed vs quiet). Corum–Levit show a Kyle toehold block + one post-disclosure contest is publishable scope; Back et al. show one informed trader + one action is *Econometrica* scope.
2. Keep the bidder-entry block as a reduced-form price-trigger rule (EGJ's trigger effect), relegating the Appendix-D7 tender-game microfoundation to an appendix with honesty labels intact.
3. Brouwer existence stays (appendix); numerical uniqueness is fine if labeled and the headline comparative statics are proven.

**What the minimal elegant model must still PROVE (non-negotiable).**
1. **R2 (disclosure attenuation) must become a theorem**: stricter disclosure (threshold/window) ⇒ premia less sensitive to liquidity κ. This is the paper's most theorem-shaped and most policy-relevant result; it is also the one with a live empirical counterpart (below). Prove under stated primitive conditions; this replaces the current numerically-verified R1 as the headline.
2. **R1 (hump-shaped minority premia in κ)**: prove the endpoint structure (Δ(0)=Δ(1) symmetry and signs of Δ′ at the endpoints), which establishes the hump's existence from continuity + sign flips; present the interior location/shape as a clearly-labeled numerical proposition and immediately convert it into a falsifiable prediction (Corum–Levit Prop 4 precedent: non-monotonicity as identification). Do not present a purely numerical hump as a "result."
3. One clean existence/uniqueness statement for the disclosure-split equilibrium (Brouwer + uniqueness under a stated restriction, e.g., small noise or linear inference), with everything else labeled numerical.

**Which results become empirical tests, and with what identification.**
1. **R2 → the paper's flagship test**: the SEC's *Modernization of Beneficial Ownership Reporting* (Rel. 33-11253, adopted Oct 10, 2023) shortened the initial Schedule 13D deadline from 10 days to 5 business days and amendments to 2 business days, effective/compliance **Feb 5, 2024** (13G deadlines Sept 30, 2024). This is a direct, plausibly exogenous tightening of the disclosure regime — the exact policy margin Back et al. map to σ²T. Test: diff-in-diff / interaction of pre-filing target liquidity (Amihud) × post-Feb-2024 on (i) 13D announcement CARs and (ii) takeover premia in deals with prior 13D presence. Prediction: liquidity-sensitivity of premia FALLS post-reform. The project's `empirics/` EDGAR pipeline already produces the filing sample.
2. **R1 → cross-sectional falsification**: takeover premia (and 13D CARs) hump-shaped in pre-event liquidity; the sign-flip between low-κ and high-κ halves is the testable content — more credible than a monotone claim precisely because it can fail.
3. **Institutional-facts section (Burkart–Lee style, 3–5 pages)**: from the EDGAR pipeline — distribution of stake at first 13D (benchmark: 7.51%), time-to-file vs the 10-day/5-day window, share of campaigns ending in takeover (Greenwood–Schor benchmark), premia by liquidity tercile. Framed as "facts the model must match," not as tests.

**Cite and differentiate (line up the six).**
- Back et al. 2018: fixed disclosure horizon; they explicitly call endogenizing the 5%-threshold disclosure timing future work — **that is our paper**. Also their binary-example non-monotonicity in liquidity is a cousin of R1.
- Burkart–Lee 2022: post-disclosure mode choice; they explicitly leave pre-disclosure trading + its interaction with post-disclosure decisions to future work — **our paper sits exactly in that gap**; our minority premia connect to their GH free-rider pricing.
- Corum–Levit 2019: activist presence → takeover probability (solicitation); we add the *information/disclosure* channel through which the market and bidder learn.
- AFS 2022: 13D-vs-13G filing choice as the value-relevant institutional margin; their both-types illiquidity premium is a fact our premia-liquidity relation must confront.
- Johnson–Swem 2021: escalation/settlement calibration anchors (settle 27–44%, fight costs 8.7–19.4% of stake) for voice-branch payoffs.
- Celentano–Levine 2025: quantitative activism–M&A complementarity and the treatment/selection debate; our channel (disclosure → inference → premia) is orthogonal — cite as the structural benchmark and for bid-premium measurement conventions.
- EGJ 2012 + Gantchev 2013 as the canonical price→takeover evidence and campaign-cost anchors.

**Framing recommendation (one sentence).** Reposition from "a static microstructure model with numerically verified comparative statics" to **"the first model in which the 13D disclosure event itself is the equilibrium object that splits market inference — with a proven disclosure-attenuation theorem for takeover premia, a falsifiable hump in liquidity, and a live 2024 policy shock to test it."**
