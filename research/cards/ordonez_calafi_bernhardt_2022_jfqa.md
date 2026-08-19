# Ordóñez-Calafi & Bernhardt (2022) — "Blockholder Disclosure Thresholds and Hedge Fund Activism"

**Venue / status:** *Journal of Financial and Quantitative Analysis*, Vol. 57, No. 7 (Nov. 2022), pp. 2834–2859. doi:10.1017/S0022109022000059. Open Access (CC-BY). Published version, © The Author(s) 2022, Cambridge University Press.
**Full text from:** `research/txt_extracts/ordonez_calafi_bernhardt_2022_jfqa.pdf` (26 pp) · **Reader:** opus · **Read:** full text, 26 pages (2834–2859), including Appendix proofs and references
**Page numbering:** printed journal pages 2834–2859. Quotes are transcribed from the printed page; end-of-line hyphenation ("character-/izing") and the PDF's fi/fl ligatures are normalised, nothing else.
**Type:** theory   **Role for us:** antecedent (closest theory antecedent; mandatory citation)

> **Scope flag — RESOLVED 2026-08-19.** The Supplementary Material ("Internet Appendix", 11 printed pages, fetched to `research/txt_extracts/ordonez_calafi_bernhardt_2022_supplement.pdf`) has now been read in full by a supplement reader. It contains exactly two sections: **§A Proof of Proposition 4** (SM pp. 1–9) and **§B Proof of Proposition 7: Stock-Picking** (SM pp. 9–11). All five Supplement-dependent UNCHECKED items are closed — see **§9b** for the item-by-item verdicts and for the two caveats the Supplement itself carries (the ε*I_m < ε*R_m leg is only a *necessary-condition* argument, and the SOC/uniqueness check covers investors and the activist but **not** the regulator).

## 1. Question

Should the legal blockholder disclosure threshold — the stake size at which a large shareholder must reveal itself — be raised or lowered, once you account for the fact that the activist's trading profits are what pay for its monitoring? They ask how the threshold jointly determines (i) an activist fund's incentive to intervene, (ii) managers' choice to misbehave, and (iii) how much capital dispersed uninformed investors put in at date 0. They then derive the optimal threshold separately for uninformed investors, for the activist, and for a welfare-maximising regulator, and rank the three. The motivation is the live US policy fight: the 2011 Wachtell Lipton petition to tighten 13D rules versus the Bebchuk–Jackson academic reply (p. 2835).

## 2. Model / data and method

Pure theory. No data, no calibration, no simulation, no empirical section.

**Timing** (4 dates, no discounting, all agents risk-neutral; Figure 1, p. 2841):
- **t = 0** — a continuum of dispersed uninformed investors chooses capital *k*. Project value `V = f(k)[1 − δ·1{m=0}]`, with `f' > 0`, `f'' < 0`, `f'(0) → ∞`; marginal cost of capital `r > 0`; shares outstanding normalised to measure 1 (pp. 2839–2840).
- **t = 1** — the manager picks business plan `m ∈ {0,1}`. Bad plan (`m = 0`) destroys fraction δ of value and pays the manager private benefit φ; if disciplined she instead bears a privately observed reputation cost ρ ~ H on [0, R̄], density h > 0, with φ < R̄ (p. 2840).
- **t = 2** — initial investors hit by liquidity shocks sell fraction *l*, **exponentially distributed**, `y(l) = μe^{−μl}` for l ≥ 0. **μ > 1 is the (il)liquidity parameter**: larger μ = more illiquid. The activist, an outsider, observes malfeasance with probability λ < 1 and can discipline at cost c ~ G on [0, C̄] (strictly positive, weakly decreasing density g), privately observed. He buys fraction α ("his position"). A competitive market maker sees only net order flow `ω = α − l` and prices at `E[V | ω]`, breaking even (Kyle 1985 dealership) (p. 2840).
- **t = 3** — payoffs realise.

**Equilibrium notion:** perfect Bayesian Nash equilibrium, solved recursively (p. 2842).

**Tractability devices (what buys the closed form):**
1. **Exponential liquidity trading.** This is the whole engine — it delivers the informed position and its price impact in closed form, explicitly following Edmans (2009). The headline consequence is `α* = 1/μ` and `Y(α*) = 1 − e^{−1}` (pp. 2836, 2843, fn. 5 p. 2844).
2. **Static, single-shot trade.** One trading round; explicitly abstracting from the dynamic trading of Collin-Dufresne–Fos (2015) and Back et al. (2018) (pp. 2838, 2841).
3. **Fixed (one-shot) intervention cost c**, orthogonal to k, "in a reduced form that keeps our model tractable" (p. 2842).
4. **No cut-and-run** — if the activist takes a position after m = 0, he intervenes (p. 2840).
5. **Baseline: the activist only trades after observing malfeasance.** Section IV relaxes this with stock-picking probability θ < 1 on good plans (p. 2852).

**How the disclosure threshold enters — the point that matters most for us.** A legal threshold ᾱ forces public announcement *the instant* the position crosses it, and crossing raises the price to `P_h = f(k)`, wiping out all information rents. So in equilibrium the activist **never crosses**: the threshold is an *upper bound on the secret stake*, `α = min{ᾱ, α*}` (pp. 2836, 2846). There is **no filing window, no delay, no timing margin, and no post-crossing trading** anywhere in the model.

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where (page / prop / table) |
|---|---|---|---|
| R1 | Unconstrained optimal secret position is `α* = 1/μ`; market maker prices `P_h = f(k)` on net buys and `P_l < f(k)` on net sells; activist intervenes iff `c ≤ c*_t` | PROVED | Prop. 1, p. 2842; proof Appendix A, pp. 2856–2857 |
| R2 | Conditional trading transfers `c*_t` rise with real investment *k* and with market liquidity `1/μ` | PROVED | p. 2844 + fn. 5 (Implicit Function Theorem on eq. (4)) |
| R3 | Ex ante value decomposition `E[V] = π_V f(k)`, `E[Π_A] = π_A f(k)`, `E[Π_I] = (π_V − π_A) f(k)`; investment solves `π_I f'(k) − r = 0` | PROVED | Prop. 2, p. 2845; proof Appendix B, p. 2857 |
| R4 | A threshold ᾱ binds iff `ᾱ < α*`; when binding the activist sets `α = ᾱ` exactly | PROVED | Corollary 3, p. 2846 |
| R5 | Cutoffs on the activism elasticity of management order as `ε*A_m < ε*I_m < ε*R_m`, generating four regions: only the activist wants a binding threshold / nobody does / only investors do / investors and society do but the activist does not (`0 < ᾱ_I < ᾱ_R < α* ≤ ᾱ_A`) | PROVED for the `ε*A_m < ε*I_m` leg; the `ε*I_m < ε*R_m` leg is only a **necessary-condition** argument. Quasiconcavity remains a *hypothesis of the proposition*, verified nowhere in general. *(label refined by supplement reader)* | Prop. 4, pp. 2847–2848; Figure 2, p. 2848. Proof: **SM §A, pp. 1–9**; explicit cutoffs SM eq. (30) p. 3 (`ε*I_m`), eq. (36) p. 4 (`ε*A_m`), eq. (42) p. 6 (`ε*R_m`); cutoff relation SM §A.3, pp. 6–7 |
| R6 | The activist and uninformed investors can **never** simultaneously benefit from a binding threshold (`ε*A_m < ε*I_m`) | PROVED *(proof located by supplement reader)* — SM eq. (43) reduces it to a sign comparison, and SM eq. (44) supplies the two facts that settle it: `−(∂π_A/∂H)/(∂π_I/∂H) ∈ (0,1)` and `c_t/(c_t − E[c\|c ≤ c_t]) > 1` | p. 2850; proof **SM §A.3, p. 6**, eqs. (43)–(44) |
| R7 | Necessary condition for investors to want a binding threshold: `g(c*_t)[δf(k) − c*_t] < G(c*_t)`, i.e. `ε*_a < c*_t /(δf(k) − c*_t)` | PROVED (in-text: read straight off the investors' FOC, eq. (15) → (16); **no proof in the printed Appendix**). The SOC/uniqueness backing is **SM §A.4, pp. 7–9**, and holds only in the uniform–uniform case, and only for investors and the activist. *(label corrected by verifier; location closed by supplement reader)* | Corollary 5, p. 2849; SM §A.4, pp. 7–9 |
| R8 | Investors always want *some* opacity: `ᾱ_I > 0` | **PROVED** *(closed by supplement reader)* — at α = 0 trading profits are zero so `c_t = 0`, which makes SM eqs. (27) and (26) strictly positive | p. 2848; proof **SM p. 2**, eqs. (26)–(27) |
| R9 | `dc_t/dα > 0` for `α < α*` — the investment-feedback effect never overturns the direct trading-transfer effect; hence the activist **never** gains from a threshold merely because it boosts real investment | **PROVED** *(closed by supplement reader)* — an explicit **proof by contradiction** inside the Activist part of the Prop. 4 proof: if `dc_t/dα < 0` then `∂π_I/∂c_t < 0`, so investors' profits rise in α, so `∂k/∂α > 0` — contradicting the `∂k/∂α < 0` the supposition requires | Corollary 6, p. 2850; proof **SM p. 4** (paragraph following eq. (33)) |
| R10 | The socially optimal threshold lies weakly between the investors' and the activist's (`ᾱ_I < ᾱ_R` whenever `ᾱ_I < α*`); society gains from a threshold only if investors do, not conversely | PROVED | Prop. 4 + §III.B.3, p. 2851 |
| R11 | Better stock-picking (higher θ) *reduces* managerial malfeasance and *raises* the conditional probability of activism — a positive spillover the authors call novel | **PROVED** *(closed by supplement reader)* — SM §B rebuilds the trading equilibrium with θ (prices SM eq. (55), cutoff SM eq. (56), activist gross profits SM eq. (58)) and then signs the **partial** `∂c_t/∂θ > 0` by the implicit function theorem on SM eqs. (59)–(60). The *total* `dc_t/dθ` is left to the main text: SM p. 10 says "the main text argues that investment feedback `∂c_t/∂k · ∂k/∂θ` cannot determine the sign of `dc_t/dθ`" | Prop. 7, p. 2852; proof **SM §B, pp. 9–11** |
| R12 | Stock-picking widens the distance between the investors' and society's optimal thresholds | ASSERTED | p. 2853 (verbal argument closing "Hence, stock-picking contributes to misaligning the interests of uninformed investors and society, increasing the distance between their optimal disclosure thresholds whenever they bind.") *(quote corrected by verifier)* |
| R13 | **High liquidity lowers the optimal threshold; low liquidity raises it** | ASSERTED | p. 2854 (Discussion §V; no proposition, no proof, no numerical grid). *(added by verifier)* The same claim is repeated in the Concluding Remarks, p. 2856: "Our model links the desirability of disclosure thresholds to market fundamentals (e.g., liquidity)…" — so they do promote it to a headline, still with nothing formal behind it |
| R13b | Coupled with the empirical liquidity–activism literature, this "suggests the potential desirability of **industry-specific thresholds based on liquidity measures**" | ASSERTED *(added by verifier)* | p. 2854 (same Discussion paragraph as R13) |
| R16 | The effect of stock-picking θ on the **investors'** optimal threshold is **ambiguous in sign**: `ᾱ_I` rises with θ when `ε*_a` is high and `|ε*_m|` is high, and falls with θ otherwise | ASSERTED *(added by verifier)* | p. 2853 |
| R14 | Optimal thresholds should differ by firm size / market cap; large firms' thresholds may be "too high" | ASSERTED | p. 2855 (Discussion) |
| R15 | Takeover-seeking campaigns, being costlier under permissive US takeover-defence law, should carry a *higher* optimal threshold than other campaign types | ASSERTED | p. 2854 (one paragraph in Discussion; no model of takeovers) |

No NUMERICAL results at all: the paper contains no simulation, no grid, no figure of a solved equilibrium. Figures 1 and 2 are a timeline and a schematic ordering of cutoffs.

## 4. Institutional facts used

- **Williams Act (1968)** introduced blockholder disclosure thresholds, designed to "alert investors in securities markets to potential changes in corporate control and to provide them with an opportunity to evaluate the effect of these potential changes" (p. 2837, fn. 2, quoting *Wellman v. Dickinson*, 682 F.2d 355, 365–66 (2d Cir. 1982)).
- **2011 WLRK petition to the SEC** to tighten blockholder disclosure rules; academic reply by Bebchuk & Jackson (2012) and Bebchuk, Brav, Jackson & Jiang (2013) (p. 2835).
- **2017**: SEC nominee R. Jackson called for expanded disclosure rules for activists (p. 2854, fn. 6).
- **SEC proposal to raise the reporting threshold for institutional investment managers** (13F), on which the authors filed a comment letter, Bernhardt & Ordóñez-Calafi (2020) (p. 2854).
- **Cross-country threshold levels** (fn. 8, p. 2855): US 13D at **5%** of voting rights; **Canada 10%**; **Germany recently cut to the 3% UK cutoff**; **France 5%**.
- **(added by verifier)** They claim existing empirical support for the cap mechanism itself: among predictions with support they list "that disclosure thresholds constrain funds' positions (Bebchuk et al. (2013))" (p. 2839). That is the *threshold-level* version of our identification question, already claimed as settled.
- **(added by verifier)** A competing, non-rents reason blockholders stay below the threshold: "Some activist funds take positions that do not cross disclosure thresholds; recent studies identify capital costs and financial constraints as key reasons (Becht et al. (2017), Brav et al. (2022))" (p. 2855). Relevant to us: not every sub-threshold stake is evidence of a rent motive.
- **(added by verifier)** Scale invariance, fn. 4 p. 2840: results are "qualitatively unchanged if initial investors sell fraction γl of shares, where γ ∈ (0,1)" — i.e. the liquidity primitive can be rescaled, which matters when mapping μ to our κ.
- Empirical facts borrowed to motivate assumptions (p. 2839): liquidity–activism positive relation (Collin-Dufresne & Fos 2015; Gantchev & Jotikasthira 2017), value creation (Brav et al. 2008; Klein & Zur 2009; Bebchuk et al. 2015), intervention costs (Gantchev 2013), managerial costs (Fos & Tsoutsoura 2014: **$1.3–$2.9m** foregone income for the median incumbent director facing removal, p. 2841), managerial response to activism threat (Gantchev, Gredil & Jotikasthira 2019), median 266 days from disclosure to divestment (Brav, Jiang & Kim 2010, fn. 1 p. 2834).

**Not used anywhere:** the 13D filing deadline. The words "window", "business day", "10-day", "10 day", "ten day", "delay", "deadline", "file", "five" and "grace" do not appear in the paper — **0 hits each, re-verified independently by the verifier** on a fresh per-page `pdftotext -layout` extraction. "days" occurs exactly once, in fn. 1 p. 2834 (Brav, Jiang & Kim's median 266 days from disclosure to divestment); "filing" occurs exactly once, in the conclusion (p. 2856, "e.g., 13D filings in the United States"). The Feb-2024 acceleration is not mentioned — the paper predates it.

## 5. Referee-facing strengths / weaknesses

**Strengths:**
- The three-way welfare ranking (investors / activist / regulator) is clean, complete, and stated as a single ordering of one sufficient statistic — the *activism elasticity of management* `ε*_m` — with four exhaustive regions. That is a genuinely well-packaged theory result and the reason this paper is the canonical citation for "the threshold as a design object".
- Corollary 6 is the sharpest result: it kills a plausible-sounding mechanism (activist wants a threshold as a commitment device to protect real investment) by proving the investment-feedback channel is always second-order. Referees like a proof that rules out an intuition.
- The GE structure (trading transfers → activism → managerial behaviour → real investment → back into activism) is a real closed loop, not a partial-equilibrium comparative static.
- Every assumption is tied to a cited empirical regularity (p. 2839), and the mechanisms map onto measurable objects the authors name (Gantchev et al. 2019 for `ε*_m`).

**Weaknesses / open flanks:**
- **The central welfare proposition (Prop. 4) is proved only in the Supplementary Material**, under **two** unproved regularity assumptions that the card previously ran together *(corrected by verifier)*: (i) net expected profits of investors and activists are **assumed quasiconcave** in α for α ≤ α* — this is a hypothesis of Prop. 4 itself and is **never verified anywhere**, not even for uniforms; (ii) second-order conditions are **assumed** well behaved, and the Supplementary Material verifies *these* only when c and ρ are uniform (p. 2847). The printed Appendix contains proofs of Props. 1 and 2 only (pp. 2856–2857). The headline result rests on an unverified regularity condition off the uniform case.
- **The liquidity result (R13) — the one closest to us — is asserted in the Discussion, not proved.** The model gives `α* = 1/μ` and `dc*_t/d(1/μ) > 0`, but the claim that "high liquidity ⇒ lower optimal threshold" is a verbal extension with no proposition attached.
- **Crossing the threshold is assumed to be instantaneous and fully revealing.** This is what makes the threshold a pure cap. It is not derived; it is the modelling of the rule. Any filing window at all breaks it.
- Static one-shot trading: no accumulation path, no dynamic price impact, no strategic timing. They concede this (p. 2841).
- Zero-sum trading between the activist and uninformed investors means the *only* social role of the threshold is via real investment — a strong structural restriction. A referee could ask what happens with a bidder, or with a wealth transfer to a third party.
- No empirics of their own; §V ends by admitting the key elasticities need "indirect proxies" (p. 2855).
- **(added by verifier)** They cite Burkart and Lee (2022), "Activism and Takeovers" (*RFS* 35, 1868–1896), in the literature paragraph on p. 2838 as part of the activist-fund theory lineage, and then never engage it. The one theory paper in their own bibliography that joins activism to takeovers is name-checked and dropped — which is both a flank for them and a paper we must read before claiming the activism × control-outcome space is empty.

## 6. What they do NOT do (scope boundary)

**Object.** Managerial discipline (probability the bad plan is stopped), real investment *k*, and the trading transfer from uninformed investors to the activist. **No control outcome in our sense**: no bidder, no tender offer, no takeover premium, no campaign success/failure — `bidder`, `premium` and `tender` return **0 hits** in the full text (verifier grep). "Takeover" appears **three times in the body** *(count corrected by verifier: the card previously said once)*, but all three sit inside **one** Discussion paragraph on p. 2854, and only as a determinant of *intervention cost*; the remaining three hits are titles in the reference list (Armour & Skeel; Burkart & Lee):

> "U.S. takeover regulation is relatively permissive with regard to takeover defenses (Armour and Skeel (2007)), raising the cost of interventions that advocate the sale of a target company. The optimal threshold for takeover-seeking campaigns may therefore exceed those involving interventions on aspects for which management is legally more exposed." (p. 2854)

**Margin.** The **threshold level only**, and specifically as a *cap on the secret stake* — the activist's position is `min{ᾱ, α*}` and he never crosses (p. 2846). There is **no window margin at all**: no filing deadline, no delay, no pre-disclosure accumulation window, no 10-day or 5-day rule. Crossing ⇒ instant revelation ⇒ zero rents. Their partition has no "flagged but still trading" state.

**Identification.** Theory only. No data, no estimation, no simulation, no calibrated grid. §V explicitly hands the testing to others:

> "Alternatively, one may be able to exploit changes in disclosure thresholds or the heterogeneity of thresholds across financial jurisdictions to test the responsiveness of activism to trading profits." (p. 2855)

and

> "However, regulators and academics may want to investigate the more nuanced mechanisms in our model, involving the activism elasticity of management and the profit elasticity of activism, to better understand the effects of policy changes." (p. 2855)

**Also out of scope:** dynamic trading (p. 2841), uncertain intervention outcomes, activist portfolio choice across firms (raised only in fn. 7, p. 2855, credited to the referee), and any post-2022 rule change.

## 7. Implications for our position

**What they occupy:** object = managerial discipline + real investment + trading transfers; margin = **threshold level** (as a cap on the secret stake); identification = **pure theory**. That triple is closed and we should not re-enter it.

**What this leaves open for us — three separable pieces of whitespace:**

1. **The window margin is untouched.** Their model *requires* that crossing the threshold reveals instantly, because that is exactly what makes the threshold a cap and makes `α = min{ᾱ, α*}` the equilibrium. A filing window is not a small perturbation of their setup — it destroys the mechanism, because it creates a state in which the blockholder has crossed and is still trading unflagged. In our vocabulary: **their partition never has a "crossed but not yet flagged" cell.** Our Public Voice branch (buy past the threshold, be flagged) exists only because a window exists. This is the cleanest statement of our whitespace against the closest antecedent, and it is stronger than "they did not study 2024" — it is structural.

2. **Control outcomes are untouched.** Their control outcome is a binary business plan chosen by an incumbent manager. No bidder ever enters, no premium is ever paid, no third party competes for control. Our premium wedge and bidder-entry object are outside their model entirely. Their one takeover sentence (p. 2854) is ASSERTED and runs the *opposite* way to a premium mechanism — it says takeover campaigns are costlier, so their threshold should be higher.

3. **Liquidity is a comparative static they assert but never prove.** They have the same tractability engine we do — exponential noise trading in the Edmans (2009) lineage, giving `α* = 1/μ` — and they state at p. 2854 that high liquidity should lower the optimal threshold. But R13 carries no proposition. If our κ result on the *window* margin is PROVED, we simultaneously (a) cite them as the antecedent that set up the question and (b) supply the proof they asserted, on a different margin. That is a strong, honest positioning move.

**(added by verifier) Two things to state carefully when we cite them:**

- **The "never aligned" headline has a caveat we must not drop.** Q7 says preferences are "never aligned"; the same page adds "We find scope for agreement only when all market participants gain from **nonbinding** disclosure thresholds" (p. 2856). So the three parties *can* agree — precisely in the region where the rule does not bite (Prop. 4 region 2, `ε*A_m ≤ ε*_m ≤ ε*I_m`). Quoting Q7 alone overstates their result and a referee who knows the paper will catch it.
- **They convert a window complaint into a level instrument, without saying so.** Their own account of the 2011 WLRK petition (p. 2835) is that WLRK "argued that the current disclosure threshold allows activist investors to **secretly accumulate** enough stock to create fundamental changes" — secret *accumulation* is a window/timing complaint, and WLRK's petition is best known for attacking the 10-day lag. OCB model it purely as a cap on the level. That silent translation is where our margin enters the historical record, and it is a fair, sourced sentence for our introduction. *(This reading is the verifier's inference from p. 2835; OCB never discuss the window, so it cannot be sourced to them — do not put it in their mouth.)*

**Constraints they impose on us:**
- We must cite them as *the* paper that made the threshold a design object with a full welfare ranking, and we must not restate that ranking as if it were ours.
- Their `α* = 1/μ` and the exponential-noise closed form are the direct antecedent of our κ machinery; the lineage runs Edmans (2009) → OCB (2022) → us. Say so.
- Their welfare architecture (investors vs blockholder vs regulator, ordered by one elasticity) is the **template** we should mirror on the window margin. If we can produce an analogous ordering for the window, the paper writes its own contribution sentence: *OCB rank the three parties over the threshold level; we rank them over the window, and the ordering differs because the window, unlike the level, lets the blockholder keep buying after crossing.*
- Their disclosure-attenuation intuition (a tighter rule cuts trading rents, cuts intervention, worsens governance) is the *threshold-margin* version of our T2. Because the window margin does not cap the stake, our T2's sign is not inherited from them — it has to be re-derived. Good: that is the paper.

## 8. Quotes we may lean on (verbatim, page-cited)

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "A disclosure threshold limits the equity position that can be secretly acquired. Crossing the threshold reveals the activist's position to the market maker, which then updates prices, eliminating any trading rents for the activist. As a result, in equilibrium, the activist's position does not cross the disclosure threshold, and the policy becomes an upper bound on its position and hence trading profits." | p. 2836 | The threshold is a *level* margin — a cap on the secret stake, with instantaneous revelation and no window. Our single most important quote from this paper. |
| Q2 | "Ownership disclosure rules limit the number of undervalued shares that an activist can acquire, potentially reducing his incentives to participate." | p. 2846 | Same point, stated as the definition of the policy instrument. |
| Q3 | "Liquidity trading is drawn from an exponential distribution. This structure allows us to solve for informed trading and its price impacts in closed form (Edmans (2009))" | p. 2836 | The tractability device; the shared lineage with our κ machinery. |
| Q4 | "Parameter μ > 1 captures market liquidity, with larger values of μ representing more illiquid markets." | p. 2840 | Their liquidity primitive, for the mapping to our κ. |
| Q5 | "Greater liquidity (i.e., a smaller μ), makes it easier for the activist to camouflage his trade, encouraging him to acquire a larger position." | p. 2843 | The liquidity → position channel, PROVED in their setting. |
| Q6 | "Proposition 4 derives the consequences of disclosure thresholds by characterizing the ordering of the optimal threshold policies for investors, the activist, and a welfare-maximizing regulator representing society." | p. 2847 | The welfare-ranking template we mirror on the window margin. |
| Q7 | "We show that the preferences for binding disclosure thresholds of investors, activist funds, and society are never aligned." | p. 2856 | Headline welfare finding, exactly as stated. |
| Q8 | "We prove that activists can gain from such a commitment when it encourages managerial malfeasance but not because it fosters real investment." | p. 2856 | Corollary 6, in their own words, with the word "prove" — a genuine PROVED label. |
| Q9 | "We show that high liquidity can lead the costs of adverse selection in financial markets to outweigh the benefits of managerial disciplining, thereby reducing the optimal threshold, whereas the opposite is the case when liquidity is low." | p. 2854 | The liquidity × threshold claim — note this sits in the Discussion with no proposition behind it (ASSERTED). |
| Q10 | "The optimal threshold for takeover-seeking campaigns may therefore exceed those involving interventions on aspects for which management is legally more exposed." | p. 2854 | Their entire treatment of takeovers: one asserted sentence, no bidder, no premium. Scope boundary evidence. |
| Q11 | "In practice, these processes are dynamic (Collin-Dufresne and Fos (2015), Back et al. (2018)), with uncertain costs (Gantchev (2013)) and outcomes (Becht et al. (2017)). We abstract from these mechanics to study the incentives provided by financial markets." | p. 2841 | Their explicit statement of what they leave out (dynamics, uncertain outcomes). |
| Q12 | "Alternatively, one may be able to exploit changes in disclosure thresholds or the heterogeneity of thresholds across financial jurisdictions to test the responsiveness of activism to trading profits." | p. 2855 | Future work, in their words: they hand the empirics to someone else, and they name *threshold* variation, not window variation. |
| Q13 | "investors that intend to introduce corporate changes in U.S. publicly listed companies must fill a form 13(d) when their holdings reach 5% of voting rights. In Canada, disclosure is not required until a 10% stake is acquired." | p. 2855 (fn. 8) | Institutional anchor; the only place the actual rule appears, and it is threshold levels only — no deadline. ("fill" is theirs, not a transcription slip.) |
| Q14 *(added by verifier)* | "We find scope for agreement only when all market participants gain from nonbinding disclosure thresholds." | p. 2856 | The **caveat to Q7**. Never quote Q7's "never aligned" without this; the parties do agree, in the region where the threshold does not bind. |
| Q15 *(added by verifier)* | "Empirical studies that find a positive relation between liquidity and hedge fund activism generally include industry controls (Edmans, Fang, and Zur (2013), Norli, Ostergaard, and Schindele (2015), and Gantchev et al. (2019)), which, coupled with our results, suggests the potential desirability of industry-specific thresholds based on liquidity measures." | p. 2854 | Their liquidity claim taken all the way to a **policy contingency** — a liquidity-indexed rule. This is the closest anyone has come to our object, and it is asserted, not proved. |
| Q16 *(added by verifier)* | "Our model links the desirability of disclosure thresholds to market fundamentals (e.g., liquidity), firm characteristics (e.g., market capitalization and managerial entrenchment), and the regulatory framework (e.g., cost of activism)." | p. 2856 (Concluding Remarks) | Proof that the liquidity contingency is not a throwaway line in §V — they put it in the conclusion. Still ASSERTED. |
| Q17 *(added by verifier)* | "The Appendix contains the proofs for the analysis of our baseline model; the Supplementary Material contains the remaining proofs." | p. 2839 | The sentence that fixes which results we can say we have *seen* proved. Printed Appendix = Props. 1 and 2 only. |

## 9. Verification log

**Verifier:** adversarial second reader, 2026-08-19. **Method:** the PDF was re-extracted page by page
(`pdftotext -f N -l N -layout`, 26 pages) into a stream carrying a printed-page index, so every quote and
every citation resolves to a printed page mechanically rather than by eye. PDF p. 1 = printed p. 2834 was
confirmed from the front matter and the folio; the mapping printed = 2833 + PDF page then holds throughout.
Ligatures (fi/fl/ff) and end-of-line hyphenation normalised; nothing else. **Supplementary Material was not
obtainable and was not read** — see the UNCHECKED block below.

**Counts: OK 21 · WRONG 1 · MISCITED 0 · UNCHECKED 5.**

### Quotes (§8)

| Quote | Verdict | Checked against |
|---|---|---|
| Q1 | **OK** | Exact string, printed p. 2836. |
| Q2 | **OK** | Exact string, printed p. 2846. |
| Q3 | **OK** | Exact string, printed p. 2836. |
| Q4 | **OK** | Exact string, printed p. 2840 (μ verified as the literal glyph). |
| Q5 | **OK** | Exact string, printed p. 2843. |
| Q6 | **OK** | Exact string, printed p. 2847. |
| Q7 | **OK** | Exact string, printed p. 2856. **But see Q14** — used alone it overstates the result. |
| Q8 | **OK** | Exact string, printed p. 2856. |
| Q9 | **OK** | Exact string, printed p. 2854, inside §V Discussion. No proposition within ±2 pages. |
| Q10 | **OK** | Exact string, printed p. 2854. |
| Q11 | **OK** | Exact string, printed p. 2841. |
| Q12 | **OK** | Exact string, printed p. 2855. |
| Q13 | **OK** | Exact string, printed p. 2855 fn. 8. |
| Q14–Q17 | **OK** | Added by the verifier; each string-matched at the page given. |
| §6 block quote (takeover, p. 2854) | **OK** | Exact string, printed p. 2854. |
| §6 block quotes (both, p. 2855) | **OK** | Exact strings, printed p. 2855. |
| §4 *Wellman v. Dickinson* quote | **OK** | Exact string, printed p. 2837 (fn. 2 carries the full citation). |

### Results (§3)

| Result | Verdict | Checked against |
|---|---|---|
| R1 α* = 1/μ, pricing, c ≤ c*_t | **OK** | Prop. 1 read at p. 2842; "A proof is in the Appendix" p. 2843; Appendix A begins p. 2856 and runs into p. 2857. Card's citation correct. |
| R2 c*_t rises in k and in 1/μ | **OK** | p. 2844 text + fn. 5 (IFT on eq. (4); Y(α*) = 1 − e^{−1}). Card correct. |
| R3 decomposition + π_I f'(k) = r | **OK** | Prop. 2 p. 2845; "A proof of Proposition 2 is in the Appendix"; Appendix B begins p. 2857. |
| R4 binding iff ᾱ < α*, α = ᾱ | **OK** | Corollary 3, p. 2846, stated verbatim as the card has it. |
| R5 ordering + four regions | **OK on substance** | Prop. 4 read at pp. 2847–2848; the ordering ε*A_m < ε*I_m < ε*R_m and all four regions, including `0 < ᾱ_I < ᾱ_R < α* ≤ ᾱ_A`, match the print exactly. Label refined: **two** assumptions, not one (see §5). |
| R6 activist and investors never both gain | **OK** | Closing sentence of p. 2850, verbatim. |
| R7 Corollary 5 necessary condition | **label too strong → corrected** | Corollary 5 at p. 2849 is real, and eq. (16) matches. But there is **no printed proof**: it is read off the investors' FOC (eq. (15)) in the running text, and only the SOCs are pushed to the Supplement. Label amended in §3. |
| R8 ᾱ_I > 0 | **UNCHECKED** | p. 2848 says "In the Supplementary Material, we show that ᾱ_I > 0". Supplement not obtainable. Left in place, marked. |
| R9 Corollary 6 | **location refined** | Corollary 6 stated p. 2850 with an intuition paragraph only; no proof printed. Falls under "the Supplementary Material contains the remaining proofs" (p. 2839). Amended in §3. |
| R10 ᾱ_I < ᾱ_R; society gains only if investors do | **OK** | p. 2851: "Society only benefits from a disclosure threshold if investors gain, but the converse is not true" and "(ᾱ_I < ᾱ_R when ᾱ_I < α*)". |
| R11 Prop. 7 stock-picking | **OK statement / UNCHECKED proof** | Prop. 7 verbatim at p. 2852, followed by "A proof is in the Supplementary Material". |
| R12 stock-picking widens the investor/society gap | **OK, quote fixed** | p. 2853. The card attributed it to a sentence beginning "It follows that…"; the operative sentence begins "Hence, stock-picking contributes to misaligning…". Corrected. |
| R13 liquidity ⇒ lower threshold | **OK, and stronger than the card said** | p. 2854, Discussion, no proposition — confirmed. Also repeated in the Concluding Remarks p. 2856. Added. |
| R14 firm size / market cap | **OK** | p. 2855, Discussion; "Relatively high returns of activism on large companies may make their thresholds too high." |
| R15 takeover campaigns ⇒ higher threshold | **OK** | p. 2854, verbatim, one paragraph, no model. |
| "No NUMERICAL results at all" | **OK** | `FIGURE`/`TABLE` occur only as Figures 1 and 2; `simulat`, `numerical`, `calibrat` return **0 hits** in the full text. |

### Scope claims (§6) — independently re-run

- `window` **0**, `business day` **0**, `10-day` **0**, `10 day` **0**, `ten day` **0**, `deadline` **0**,
  `delay` **0**, `file` **0**, `five` **0**, `grace` **0**. **Confirmed.** `days` **1** (fn. 1, p. 2834),
  `filing` **1** (p. 2856). The load-bearing "no window margin" claim survives.
- `bidder` **0**, `premium` **0**, `tender` **0**. **Confirmed.**
- `takeover` **6** — this is the one **WRONG** item. Body hits are **three**, not one, but all three fall in the
  single Discussion paragraph on p. 2854 ("U.S. takeover regulation…", "takeover defenses", "takeover-seeking
  campaigns"); the other three are reference-list titles. Substance of the card's claim stands; the count did
  not. Corrected in §6.
- `corporate control` 3, `acquisition` 2, `merger` 1 — all incidental (the *Wellman* quote, a reference title,
  and "empire-building mergers and acquisitions" as an example of private benefits, p. 2841). No control object.
- Instantaneous, fully-revealing crossing: **confirmed** at p. 2846 in the model's own words — "an activist must
  publicly announce his position when it crosses the threshold. Then, the activist has no incentive to establish
  a larger position because doing so would reveal his presence, causing the stock price to rise to P_h = f(k)" —
  and the equilibrium position is `min{ᾱ, α*}` (p. 2846). There is no state in which the blockholder has crossed
  and is still trading.

### Venue / header (§ header)

**OK.** Front matter p. 2834 reads "JOURNAL OF FINANCIAL AND QUANTITATIVE ANALYSIS Vol. 57, No. 7, Nov. 2022,
pp. 2834–2859", doi:10.1017/S0022109022000059, "© The Author(s), 2022 … Creative Commons Attribution licence".
26 PDF pages, printed 2834–2859. All as the card states.

### Which proofs are actually printed — the check the card most needed

The printed **Appendix. Proofs** (p. 2856) contains exactly two sections: **A. Proof of Proposition 1**
(pp. 2856–2857) and **B. Proof of Proposition 2** (p. 2857). Nothing else. Everything else the card labels
PROVED rests either on an in-text derivation (Cor. 3, Cor. 5) or on the Supplement (Prop. 4 with explicit
cutoffs, Prop. 7, ᾱ_I > 0, the characterisation of ε*A_m, the SOCs). We may write "they prove" for Props. 1–2;
for the rest we should write "they establish" or "they show (proof in the paper's Supplementary Material)".

### UNCHECKED — decision-critical, not triaged away

1. **Prop. 4's proof and the three explicit cutoffs** (Supplementary Material). This is the paper's headline and
   the template we intend to mirror. We have not seen it.
2. **Prop. 7's proof** (Supplementary Material).
3. **ᾱ_I > 0** — "investors always want some opacity" (Supplementary Material).
4. **The SOC verification under uniform c and ρ** (Supplementary Material).
5. **The characterisation of ε*A_m** and its comparative static in ε*_a (Supplementary Material).

None of these can be closed from the PDF read. **Action for the author:** the Supplement is free at
doi.org/10.1017/S0022109022000059; one download closes all five. Until then, no sentence of ours should assert
that we have verified OCB's welfare ordering — only that they state it.

### Omissions added by the verifier

1. **§3 R13b — liquidity-indexed thresholds** (p. 2854): they recommend "industry-specific thresholds based on
   liquidity measures". This is the single closest thing in the literature to our object, and it is asserted.
   The card had the liquidity claim but not the policy contingency it is taken to.
2. **§3 R13, §8 Q16 — the liquidity claim is repeated in the Concluding Remarks** (p. 2856), not only in §V.
   It is a headline of theirs, not an aside; our "they assert, we prove" line has to be phrased accordingly.
3. **§3 R16 — the sign of dᾱ_I/dθ is ambiguous** (p. 2853): investors' optimal threshold *rises* with
   stock-picking when ε*_a and |ε*_m| are both large, and *falls* otherwise. The card's R12 reported only the
   investor/society divergence and missed the ambiguity underneath it.
4. **§4 — "disclosure thresholds constrain funds' positions (Bebchuk et al. (2013))"** (p. 2839), listed by OCB
   as an already-supported prediction. Relevant because it is the level-margin analogue of the empirical claim
   we would be making on the window margin.
5. **§4 — sub-threshold stakes need not be about rents** (p. 2855): "capital costs and financial constraints"
   (Becht et al. 2017; Brav et al. 2022). A confound for any test that reads a sub-threshold stake as evidence
   of a rent motive.
6. **§4 — fn. 4, p. 2840, scale invariance** of the liquidity shock (γl, γ ∈ (0,1)): matters for mapping μ to κ.
7. **§5 — Burkart and Lee (2022), "Activism and Takeovers" (RFS 35, 1868–1896)** is in their literature
   paragraph (p. 2838) and never engaged. Before we claim activism × control outcomes is open, we must read it.
8. **§7 — the "never aligned" caveat** (p. 2856, new Q14): agreement *is* possible, in the non-binding region.
9. **§7 — the WLRK translation** (p. 2835): OCB describe the 2011 petition as a complaint about *secret
   accumulation* and then model it as a cap on the level. Flagged in §7 as the verifier's inference, not theirs.

### Overall verdict

**The card is substantively sound and its two load-bearing claims survive adversarial checking.** All 13 original
quotes are verbatim and correctly paged — an unusually clean rate. The "no window margin anywhere in this paper"
claim is confirmed by independent grep (0 hits on ten terms) and, more importantly, by the model text at p. 2846,
which makes instantaneous revelation constitutive of the threshold rather than an assumption bolted on. One item
was **WRONG**: "takeover" appears three times in the body, not once — the correction does not touch the argument,
since all three are in one paragraph. Two PROVED labels were too strong about *where* the proof lives and have
been amended. Five Supplementary-Material results remain **UNCHECKED** and are named above; four of them, Prop. 4
above all, are exactly the results we intend to mirror, so the Supplement should be fetched before drafting.


## 9b. Supplement supplement-reader log — 2026-08-19

**Source read:** `research/txt_extracts/ordonez_calafi_bernhardt_2022_supplement.pdf` — "Internet Appendix to: 'Blockholder
Disclosure Thresholds and Hedge Fund Activism'", 12 PDF pages, 11 printed pages (footer folios 1–11; p. 12 blank).
Fetched from Cambridge Core's Supplementary-materials tab (see `research/txt_extracts/FETCH_LOG_C.md`, row
`ordonez_calafi_bernhardt_2022_supplement`). **Reader:** opus, full text. Extraction: `pdftotext -layout` and `pdftotext -raw`
cross-read, because the `-layout` pass scrambles superscripts on `ε^I_m` / `ε^R_m` — the §A.3 paragraph was re-read in `-raw`
before being quoted. **Page cites below are the Supplement's own printed pages ("SM p. N"), not journal pages.**

**Structure of the Supplement.** Its opening line: "This Internet Appendix constitutes an additional section of the printed
manuscript. Equation numbering follows accordingly." Equations run (23)–(60), continuing the article's (1)–(22). Two sections
only:
- **§A — Proof of Proposition 4: Optimal Blockholder Disclosure Thresholds** (SM pp. 1–9), in four numbered parts:
  A.1 Partial Effects on Trading Transfers (pp. 1–2), A.2 Critical Cutoffs (pp. 2–6), A.3 Cutoff Relation (pp. 6–7),
  A.4 The Uniform-Uniform Case (pp. 7–9).
- **§B — Proof of Proposition 7: Stock-Picking** (SM pp. 9–11), in four parts: B.1 Trading, B.2 Management,
  B.3 Investment, B.4 Comparative Statics.

There is **no** Supplement proof of Corollary 5 as such, and **no** regulator/society second-order condition anywhere.

### The five UNCHECKED items → verdicts

| # | UNCHECKED item (from §9) | Verdict | Where in the Supplement |
|---|---|---|---|
| 1 | Prop. 4's proof and the three explicit cutoffs | **CLOSED — proof exists and reaches the claim, with one qualification** (see caveat (a)) | SM §A, pp. 1–9. Explicit cutoffs: `ε*I_m` eq. (30), SM p. 3; `ε*A_m` eq. (36), SM p. 4; `ε*R_m` eq. (42), SM p. 6 |
| 2 | Prop. 7's proof | **CLOSED** | SM §B, pp. 9–11; the signing step is eqs. (59)–(60), SM p. 11 |
| 3 | `ᾱ_I > 0` — investors always want some opacity | **CLOSED** | SM p. 2, one sentence after eq. (27): "At α = 0, activist trading profits are zero, so c_t = 0, and hence (27) > 0 and (26) > 0: investors always value some market opacity, i.e., α_I > 0." |
| 4 | SOC verification under uniform c and ρ | **CLOSED for investors and the activist; NOT DONE for the regulator** (caveat (b)) | SM §A.4, pp. 7–9 |
| 5 | Characterisation of `ε*A_m` and its comparative static in `ε*_a` | **CLOSED for the characterisation; the comparative static is never run** (caveat (c)) | SM eq. (36), p. 4 |

**Bonus item closed (not on the UNCHECKED list):** the card's **R9 / Corollary 6** (`dc_t/dα > 0` for `α < α*`) — the verifier could
only say "no proof printed". It is proved, by contradiction, in the Activist part of §A.2, **SM p. 4**. Likewise **R6**
(`ε*A_m < ε*I_m`) now has a located proof at **SM §A.3, p. 6**, eqs. (43)–(44), rather than a bare main-text assertion.

### The three caveats — material, and they change how we may cite Prop. 4

**(a) The `ε*I_m < ε*R_m` leg of Prop. 4 is not proved as an inequality.** §A.3 proves `ε*A_m < ε*I_m` properly (eqs. (43)–(44),
SM p. 6). But the whole of the second leg is one paragraph, SM p. 7, verbatim (from the `-raw` extraction, superscripts intact):

> "To see ε^I_m < ε^R_m, note that a necessary condition for ε^R_m < 0 is that ∂k/∂α < 0, which implies that investors' marginal
> profits decrease, and thus ε^I_m < ε_m. Hence, if ε^R_m = 0, then ε^I_m < ε_m < 0. Thus, for ε^R_m < ε_m, it is necessary, but
> not sufficient, that ε^I_m < ε_m."

What this establishes is the *implication* "society wants a binding threshold ⇒ investors do" — i.e. the card's **R10**, which is
exactly how the main text states it at p. 2851. It does **not** compare the closed forms (30) and (42) and derive `ε*I_m < ε*R_m`.
So R10 is solid; the strict three-way ordering in Prop. 4's own statement rests on this weaker argument.
**(added by supplement reader)**

**(b) Quasiconcavity is a hypothesis, never verified in general — and the regulator is never covered at all.** Prop. 4 opens
"Suppose that the net expected profits of investors and activists are quasiconcave in α for α ≤ α*" (p. 2847), and the paragraph
above it says "We assume that second-order conditions are well behaved for investors and the activist; the Supplementary Material
shows that they are well behaved when the activist's costs of intervention and the management's reputation costs have uniform
distributions." The Supplement delivers exactly that and no more. §A.4 opens "We show that when both c and ρ are uniformly
distributed, second-order conditions hold" and has two headed parts, **Investors** and **Activist**. There is no **Society** part.
Moreover what §A.4 actually shows is **uniqueness of the FOC solution via monotonicity of the FOC's right-hand side**, not
quasiconcavity of the objective:
- *Investors* (SM pp. 7–8): with `G(c_t) = c_t/C̄`, `g = 1/C̄`, the FOC collapses to eq. (47); `d/dc_t RHS(47) < 0` is shown for
  all admissible `c_t` under the sufficient condition **μ > R̄/φ**, which "is satisfied by assumptions μ > 1 and φ < R̄" (SM p. 8).
  The bound on `c_t` used to get there is eq. (49)–(50), obtained by setting `Y(α) = 0` and then `H(ρ_t) = 0`.
- *Activist* (SM pp. 8–9): the FOC collapses to eq. (52), then with the uniform `c` and `c_t − E[c|c ≤ c_t] = c_t/2`, to
  eq. (53) `0 = 1 − (1/2)[C̄/(C̄ − λc_t)]`, whose RHS decreases in `c_t`, "implying a unique solution".

So: **the answer to "is Prop. 4's quasiconcavity verified anywhere?" is no.** Uniqueness of a stationary point is verified, for two
of the three agents, under one distributional specialisation. **(added by supplement reader)**

**(c) `ε*A_m`'s comparative static in `ε*_a` is not run.** The characterisation exists — SM eq. (36), p. 4:
`ε*A_m ≡ −(1/ε*_a)·[c*_t/(c*_t − E[c|c ≤ c*_t])]`, reached from the activist's FOC (34) → (35) after substituting the two
elasticities. The `1/ε*_a` factor is on the face of it, so the sign of `∂ε*A_m/∂ε*_a` is immediate for fixed `c*_t`; but the
Supplement never states it, and `c*_t` is itself endogenous. Treat any comparative static of `ε*A_m` in `ε*_a` as **ours**, not
theirs. **(added by supplement reader)**

### Two derivations in the Supplement worth having on file (added by supplement reader)

1. **Why an interior `ᾱ_I` satisfies `∂π_I/∂c_t · ∂c_t/∂α · f(k) = 0`** (SM p. 2, around eq. (26)). Two simplifications do all the
   work: the equilibrium condition `π_I f'(k) − r = 0` from Prop. 2 kills the last term, and "the activist position that maximizes
   investor profits also maximizes investment, so any interior maximum of `π_I f(k) − rk` satisfies `∂k/∂α = 0`". That second step
   is an economic argument, not an envelope theorem, and it is the hinge of the whole investors' cutoff.
2. **The stock-picking price is uniformly lower.** SM eq. (55), p. 9, gives `P_l(α)` under stock-picking, and SM p. 9 states in
   words: "the price in equation (55) is smaller than the price in our benchmark setting characterized by equation (6) in the main
   text." Relevant to us because it is the closest thing OCB have to a statement about how the *pooled* price moves when the
   informed trader's motive set widens.

### What may now be written

- "Ordóñez-Calafi and Bernhardt (2022) **prove**" is now safe for Props. 1, 2, 4 (with the caveat in (a) if the three-way
  ordering is the load-bearing claim), 7, and Corollaries 3, 5, 6.
- Their liquidity claims (**R13**, **R13b**, and the industry-specific-threshold recommendation) are still **ASSERTED** — nothing in
  the Supplement touches them. The Supplement contains no simulation, no grid, no figure. The "they assert, we prove" line that
  our position rests on is **unchanged and now fully checked**: liquidity appears in their model only as the parameter μ inside
  `α* = 1/μ`, and no proposition anywhere — printed or supplementary — signs `dᾱ*/dμ`.
- Still **zero** window-margin content: `window`, `business day`, `deadline`, `delay`, `filing`, `takeover`, `premium`, `bidder`,
  `tender` all return **0 hits** across the Supplement's 11 pages — as do `liquidity`, `simulat`, `numerical` and `calibrat`. The scope boundary in §6 holds against the full paper + supplement.

**Counts after this pass: UNCHECKED 5 → 0.** No item was refuted. Two labels were *refined downward in scope* (R5's second leg;
R7's SOC coverage) and three were *upgraded from "PROVED (Supp.)" to PROVED with a located proof* (R8, R9, R11), plus R6 gained a
located proof.
