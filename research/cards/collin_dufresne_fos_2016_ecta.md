# Collin-Dufresne & Fos (2016) — "Insider Trading, Stochastic Liquidity, and Equilibrium Prices"

**Venue / status:** Econometrica 84(4), 1441–1475, July 2016 (published; manuscript received May 2012, final revision February 2016; Co-editor Lars Peter Hansen)
**Full text from:** `research/txt_extracts/collin_dufresne_fos_2016_ecta.pdf` (Wiley/Econometric Society published version, 35 printed pages, pp. 1441–1475) · **Reader:** opus · **Read:** full text, 35 pages (body §§1–5 + Appendix A.1–A.7 proofs + references)
**Page numbering:** printed *Econometrica* pages (1441–1475), verified against the running heads. PDF page 1 = printed p. 1441. (Supplemental Material — Collin-Dufresne & Fos 2016b, Appendices S1 and S2, both cited at p. 1454, fns. 8 and 9 — is a separate file and was **not** available; see §9.)
**Type:** theory (continuous-time market microstructure; no data, no estimation)   **Role for us:** antecedent — the equilibrium mechanism behind "λ falls while activists accumulate"

## 1. Question

Kyle (1985) and its continuous-time version (Back 1992) hold noise-trading volatility constant, so Kyle's lambda (price impact) and price volatility are constant and price volatility is independent of noise trading. CDF ask what changes when noise-trading volatility σ_t is itself a general stochastic process. Three questions, stated on p. 1442: how does the informed investor adapt his trading strategy; how are equilibrium price and volatility dynamics affected by shocks to uninformed-volume volatility; and how are the adverse-selection costs paid by uninformed traders affected? The economic motivation is that an insider with long-lived information can **time liquidity** — wait for thick markets — and that this option changes what measured price impact means.

## 2. Model / data and method

**Primitives.** One risk-neutral insider knows the terminal value v exactly and maximises `E[∫₀ᵀ (v − P_t)θ_t dt | F_t^Y, v]` over absolutely continuous strategies θ ∈ A = {θ : E[∫₀ᵀ θ_s² ds] < ∞} (eq. 1, p. 1444). Risk-neutral competitive market makers hold prior v ~ N(P₀, Σ₀), observe aggregate order flow `dY_t = θ_t dt + σ_t dZ_t` (eq. 2, p. 1445), and set `P_t = E[v | F_t^Y]` (eq. 3, p. 1445).

**The extension.** Noise-trading volatility follows `dσ_t/σ_t = m(t, σ^t) dt + ν(t, σ^t) dW_t` for a possibly discontinuous martingale W (eq. 4, p. 1445). The **binding economic restrictions**: σ is independent of the insider’s private information, and σ may **not be Granger-caused by order flow** (m and ν cannot depend on v or on Y^t). Both the insider and the market maker **observe the whole history of σ perfectly** (p. 1445); in continuous time, observing order flow reveals its quadratic variation, so F^Y contains both Y^t and σ^t (p. 1446).

**Solution device.** Conjecture θ_t = β_t(v − P_t), so dP_t = λ_t dY_t (eq. 5) and dΣ_t = −λ_t²σ_t² dt (eq. 6), p. 1446. (The standard filtering relation λ_t = β_tΣ_t/σ_t² is *not* printed in the article; only (5)–(6) are.) Optimality requires market depth 1/λ to be a martingale, orthogonal to price changes, with Σ_T = 0. Setting λ_t = √Σ_t/G_t decouples the forward–backward system into a **single backward recursion** `G_t = E[∫_t^T (σ_s²/2√G_s) ds | F_t^σ]` (eq. 11, p. 1447). G_t is the sufficient statistic for expected future noise trading relevant to the insider — the "equilibrium noise component" (p. 1448).

**Two worked specifications (§3).** (i) Deterministic growth rate m_t, arbitrary volatility-of-volatility ν: closed form G_t = σ_t²B_t with B_t = ∫_t^T e^{∫_t^u 2m_s ds} du (Theorem 2, pp. 1451–1452). (ii) Two-state continuous-time Markov chain σ ∈ {σ^L, σ^H} with Poisson switching intensities η_L, η_H (eq. 28, p. 1454): G solves a coupled ODE system (Theorem 3 stated p. 1454; eqs. 29–30 printed p. 1455), solved **numerically**. **One calibration throughout, not two:** Σ₀ = 0.04 in the Fig. 1 caption (p. 1455) and Σ₀ = 0.2² in the Fig. 2 caption (p. 1457) and Table I are the same number written two ways, alongside T = 1, η_L = η_H = 2, σ^L = 0.2, σ^H = 0.4.

**No data.** There is no sample, no period, no estimation anywhere in the paper. Empirical content is entirely by reference to Collin-Dufresne & Fos (2015, *JF*) — see §4.

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where (page / result) |
|---|---|---|---|
| R1 | A bounded solution G_t to the backward recursion (11) exists when W is Brownian and σ ∈ [σ̲, σ̄], and satisfies σ̲²(T−t) ≤ G_t ≤ σ̄²(T−t); if a bounded solution exists it is unique | PROVED | Lemma 1, p. 1448; proof A.1–A.2, pp. 1464–1465 |
| R2 | **Main equilibrium.** With bounded G and σ ∈ [σ̲, σ̄] an equilibrium exists with dP_t = κ_t(v−P_t)dt + √Σ₀e^{−∫₀ᵗ½κ_s ds}√κ_t dZ_t, mean-reversion κ_t = σ_t²/G_t, optimal strategy θ*_t = (κ_t/λ_t)(v−P_t), Σ_t = Σ₀e^{−∫₀ᵗκ_u du}, λ_t = √Σ_t/G_t, insider value J_t = ((v−P_t)²+Σ_t)/2λ_t, unconditional profit √Σ₀G₀ | PROVED | Theorem 1, pp. 1448–1449; proof A.3, pp. 1465–1472 |
| R3 | **The liquidity-timing result.** The insider trades proportionally to undervaluation (v−P_t), at a rate **inversely related to price impact λ_t** and **increasing in the liquidity state** κ_t = σ_t²/G_t. Only when σ is constant or a martingale does this collapse to Kyle's 1/(T−t) | PROVED | Theorem 1 eq. (16), p. 1448; discussion p. 1449 |
| R4 | **Price impact is a submartingale** (market depth 1/λ is a martingale), i.e. λ is *expected to increase over time* — the opposite of Baruch (2002) / Back–Baruch (2004), where λ is a supermartingale, and of Kyle/Back, where it is constant or a martingale. Reason: the insider must be paid to give up his option to wait for better liquidity | PROVED | Theorem 1, p. 1449; Lemma 5, p. 1469; discussion p. 1450 |
| R5 | **λ is stochastic and negatively correlated (in changes) with noise-trading volatility.** In the m=0 martingale case, λ_t is literally inversely proportional to σ_t; in the deterministic-growth case λ_t = e^{∫₀ᵗ m_s ds}σ_v/σ_t | PROVED | eq. (25), p. 1452; §3.1 pp. 1453–1454 |
| R6 | The equilibrium price is a **bridge process** converging a.s. and in L² to v at T (generalising Back's Brownian Bridge), and is a martingale in the market maker's filtration | PROVED | Theorem 1, p. 1449; Lemmas 3–4, pp. 1467–1468 |
| R7 | Price volatility is stochastic **only if** the *growth rate* m_t of noise-trading volatility is stochastic. With deterministic m, price volatility and Σ_t are deterministic even though λ is stochastic | PROVED | Theorem 2, p. 1452; §3.1 p. 1453–1454 |
| R8 | Stochastic noise-trading volatility **reduces** the insider's unconditional expected profit relative to an economy with the same average but constant noise variance (because G₀ < E∫σ²) | PROVED | p. 1451; Lemma 6, p. 1469 |
| R9 | The rate of price discovery rises when noise-trading volatility rises and λ falls — unlike Kyle, where information is revealed at a rate independent of σ | PROVED | p. 1450 (from Theorem 1 with dΣ_t = −dP_t²) |
| R10 | Aggregate execution/slippage costs ∫₀ᵀ λ_tσ_t² dt are **stochastic and path-dependent**, unlike Kyle and Back–Pedersen where unconditional expected costs equal realised costs path-wise | PROVED | eq. (20), p. 1451; derivation A.4, p. 1472 |
| R11 | **Average price impact is a bad proxy for adverse-selection costs.** In the two-state calibration, high/low and low/high paths have identical noise-trader "numbers" (0.085) yet aggregate execution costs 0.054 vs 0.057 while average λ is 1.023 vs 0.853 — costs higher where average λ is lower. Volume-weighted ("normalized") λ tracks actual costs | NUMERICAL | Table I, p. 1459; §4.2, p. 1461 |
| R12 | Price volatility is stochastic and "excessive" and its *path* can far exceed the Kyle benchmark: time-averaged price volatility runs 0.174–0.195 across the four paths against a constant Kyle value of **0.2**. Careful with the low/low path: it has the **lowest** time-average (0.174) but the **highest second-half average in the table** (0.242) and the highest terminal spike in Fig. 2(a) — the insider dumps his information into a thin market just before T after waiting unsuccessfully for liquidity | NUMERICAL | Table I Panel E, p. 1459 (totals 0.195 / 0.174 / 0.190 / 0.182; low/low split 0.106 / 0.242; Kyle = 0.2 per table note a); Fig. 2(a) and text, p. 1457 |
| R13 | Mean-reversion (price-discovery rate) is always higher in the high-volatility state, and both κ^L, κ^H → ∞ as t → T | NUMERICAL (shown via Fig. 1 for the stated parameters) | pp. 1455–1456 |
| R14 | With correlated order flow d Ŷ = θdt + σdZ + η dW, a regression of price changes on **total** order flow (the standard empirical Kyle-lambda estimator) recovers λ̂_t = λ_tσ_t²/(σ_t²+η(t)²) ≠ λ_t whenever η ≠ 0 | **ASSERTED** (corrected by verifier: no theorem, no appendix proof — the article says "it can be shown that all our results above … are unchanged", and the λ̂ expression is a one-line in-text derivation) | §4.1, eqs. (35)–(36) p. 1460, λ̂ expression p. 1461 |
| R15 | The equilibrium price is a time-changed Brownian Bridge (insider's filtration) / Brownian motion (market maker's), with an **endogenous** directing process τ_t = T(1 − e^{−∫₀ᵗ σ_u²/G_u du}) — a microfoundation for Clark (1973) subordination without a latent information process | PROVED | Corollary 1, p. 1463; proof A.7, p. 1474 |

## 4. Institutional facts used

Essentially none — this is a pure theory paper. The **single** institutional reference in the entire text is footnote 11, p. 1462, describing the *data of the companion empirical paper* (Collin-Dufresne & Fos 2015, *JF* 70(4), 1555–1582):

> "Exploiting an SEC disclosure requirement that requires activist shareholders to file a 13D schedule in which they report past trades in target stocks when they hit the 5% ownership threshold, CF built a sample of trades by activist investors."

That is the **only** occurrence of "13D", "disclosure" or "5%" in the paper. Verified by grep: `takeover` — 0 hits; `control` — 0 hits; `blockholder` — 0 hits; `learn` — 0 hits; `announce` — 0 hits; `threshold` — 0 hits outside that footnote's "ownership threshold".

Other empirical facts are cited, not used: the volume–volatility relation (Gallant–Rossi–Tauchen 1992), ARCH disappearing when volume is included (Lamoureux–Lastrapes 1990), execution costs rising over the day (Madhavan–Richardson–Roomans 1997), and the survey characterisation of adverse selection quoted at p. 1461 (Biais–Glosten–Spatt 2005, p. 232).

**(added by verifier)** One more empirical fact is imported from CDF (2015) at p. 1462 and matters for how we define κ: those informed investors "are more likely to trade when abnormal volume on the stock itself **as well as other measures of market-wide liquidity, such as the abnormal volume on the S&P 500 stock index**, are high". The liquidity-timing evidence is partly *market-wide*, not purely firm-level — relevant to whether our κ is a firm characteristic or a common factor, and to whether a market-wide liquidity control belongs in the empirical leg.

## 5. Referee-facing strengths / weaknesses

**Strengths:**
- Every headline result is a theorem with a proof in the appendix. The honesty labelling is clean: analytic results are proved for general σ dynamics, and only the *magnitudes* in §3.2 (Figures 1–2, Table I) rest on a numerical calibration.
- The G_t recursion is the paper's real contribution: one scalar backward equation absorbs arbitrary noise-trading-volatility dynamics, and it nests Kyle (G = σ²(T−t)) and Back–Pedersen as special cases.
- The submartingale-λ result is a genuine sign reversal against the prior literature, with an intuition (the option to wait must be priced away) that is stated, not just asserted.
- §4.2 turns the theory into a methodological warning that is directly checkable — average λ is not average adverse selection — with a numerical counter-example.
- §4.1 shows the correlated-order-flow assumption is not load-bearing; what *is* load-bearing (no Granger causation from Y to σ) is stated explicitly.

**Weaknesses / open flanks:**
- **σ is common knowledge and exogenous.** Everyone observes the whole path of noise-trading volatility, and order flow cannot feed back into it. In a setting where an activist's own accumulation changes market conditions, this is exactly what one wants to break.
- **The insider's presence is common knowledge** (own admission, p. 1464). There is no inference problem about *whether* an informed trader is there — precisely the object a disclosure rule creates.
- **T is fixed and known.** The horizon is a modelling primitive, not a decision or a legal deadline. (Their own follow-up, CDF 2016a "Insider Trading With a Random Horizon", relaxes this to a stopping time — cited at p. 1458 fn. 10 as a working paper only.)
- **(added by verifier) But the random-horizon case is not virgin ground, and it flips their headline sign.** fn. 6, p. 1450: in Baruch (2002) and Back–Baruch (2004) "Kyle's lambda is a supermartingale because the insider has an incentive to trade earlier (**because the horizon is random** or because he is risk-averse)", and the main text at p. 1450 lists **Caldentey and Stacchetti (2010), "Insider Trading With a Random Deadline," *Econometrica* 78(1), 245–283** among the models where λ is a martingale or supermartingale. So a deadline effect on the drift of λ is *already published*; what is unoccupied is a deadline that is a **legal filing window** attached to a **disclosure event**, not the randomness of T as such. Our §7 claim must be stated at that precision or a referee will hand us Caldentey–Stacchetti.
- **(added by verifier) fn. 10, p. 1458 gives the comparative static a deadline produces.** "In a model where T is modeled as an unpredictable stopping time with constant arrival intensity, Σ_t always follows a decreasing convex path, with a faster decay rate in the high volatility state" — i.e. the convex→concave switch that the low/low path shows here disappears once the horizon is random. Directly usable if our window margin is modelled as an arrival intensity.
- **(added by verifier) Competition among informed traders also raises λ near the horizon** (Foster–Viswanathan 1996; Back, Cao, and Willard 2000, both at fn. 6, p. 1450). If our model has more than one blockholder, the submartingale result is no longer the distinguishing feature.
- **(added by verifier) The martingale case is observationally silent in prices.** p. 1453: when m_t = 0 the equilibrium is formally identical to Kyle after substituting σ_t — price volatility, the rate of information flow, and the insider's unconditional trading rate are all *unchanged*; only λ and the realised trading rate move, and "both effects exactly offset to leave equilibrium prices unchanged". A liquidity-timing story can therefore be invisible in price paths, so any test of it must look at **trade timing**, not at price volatility.
- **The amount of private information is fixed**; the insider never chooses to acquire, act on, or change v. There is no real action, no engagement, no value creation.
- Risk neutrality throughout, on both sides.
- The quantitative claims (Table I, Figures 1–2) rest on one parameter set (T = 1, η_L = η_H = 2, σ^L = 0.2, σ^H = 0.4) with **no sensitivity analysis in the article**; the diffusion case with stochastic growth rate is in unavailable Supplemental Material (Appendix S2, cited p. 1454).
- The empirical support for the mechanism is entirely by reference to CDF (2015); nothing is estimated here.

## 6. What they do NOT do (scope boundary)

**OBJECT:** equilibrium price dynamics, price volatility, price impact λ, and execution/adverse-selection costs paid by noise traders. **No control outcome of any kind.** The words *takeover*, *control*, *bidder*, *premium*, *campaign* do not appear in the paper.

**MARGIN:** **none.** No disclosure rule is modelled. Schedule 13D and the 5% threshold appear once, in a footnote describing the *sample construction of a different paper*. There is no filing window, no threshold choice, no flagged/pooled partition — indeed the model's key informational assumption is the **opposite** of a partition: the insider's presence is common knowledge from the start, and price impact λ_t is the market maker's *continuous* response to order flow rather than a discrete revision at a disclosure date.

**IDENTIFICATION:** theory only — closed-form equilibrium (Theorems 1–2), plus one numerical Markov-chain calibration (Theorem 3, Figures 1–2, Table I). No data, no design.

**Declared out of scope, verbatim — the conclusion's future-work list (p. 1464):**

> "The model makes many simplifying assumptions that could be relaxed to further our understanding of how information flows into prices and how price volatility, price impact, and trading volume comove. First, we assume that the amount of private information is fixed and only noise trading volatility is time varying. Second, we assume that the horizon is fixed. Third, we assume throughout that the noise trading volatility process is observable to all. Fourth, we assume that the presence of the insider is common knowledge. And last, we assume that the insider and market makers are risk-neutral. We leave these extensions for future research."

Two of those five are **directly ours**: the fixed horizon (our **window margin**) and the common-knowledge presence (our **partition**). Neither is qualified or partially addressed elsewhere in the paper.

A further scope note appears in footnote 3, p. 1445: the absolutely-continuous-strategy result "requires that volatility be common knowledge. Else there could be multiple equilibria where the strategy of the insider is not absolutely continuous." — i.e. relaxing observability of σ is not a small perturbation; it threatens the equilibrium concept.

**(added by verifier) One place they come within touching distance of a partition — and stop.** p. 1461, §4.1: with correlated order flow, uninformed trades "come in two groups … the group who can be used by the informed investor to hide his trades (σ_t dZ_t) and who therefore generate a per-trade slippage cost of λ_t, and the group (η(t) dW_t) who **is known to be pure noise** and whose demand does not generate any slippage. Indeed, **if the market maker could distinguish between the two types of uninformed order flow, then they would each pay different trading costs.**" That is a *flagged vs. pooled* split of order flow, priced differently — but it is exogenous, it is about noise traders rather than about the informed trader's presence, and it is disposed of in one paragraph. The device our disclosure rule needs is the same one, applied to the blockholder and switched on by a legal event.

**(added by verifier) Prices alone need not reveal the liquidity state (p. 1446).** "when uninformed order flow has stochastic volatility, observing only prices may not be sufficient to recover noise trading volatility" — CDF's assumption that everyone sees σ is defended by the availability of volume and order-book data, not derived. A model in which the market must *infer* the liquidity state is left open.

## 7. Implications for our position

**What they occupy.** OBJECT = price impact / price volatility / execution costs. MARGIN = none. IDENTIFICATION = theory (closed form + one numerical calibration). This is the microstructure cell, and they hold it decisively for the exogenous-liquidity, known-presence, known-horizon case.

**What this buys us — the mechanism, ready to cite:**
- CDF 2016 is the **theoretical backing for CDF 2015's empirical "λ falls while activists accumulate"** (their own §4.2, p. 1462, makes the link explicit). If our paper claims that a blockholder accumulates faster when κ is high, R3 is the published proposition that says so, and R5 is the published proposition that measured λ moves the other way. Neither needs to be re-derived by us.
- **R4 (λ is a submartingale) is the sharpest thing we can borrow.** It says the *shadow price of waiting* is what makes price impact drift upward. Our window margin does the same job by fiat: a filing deadline is a legal cap on how long the blockholder may wait. Under a shorter window the option to wait is worth less. That is a clean, previously-unexploited link between an institutional margin and a microstructure object.
- **R14 is a measurement warning we must obey.** If we estimate a Kyle lambda from total order flow around 13D accumulations, R14 says we recover λσ²/(σ²+η²), not λ. And R11 says a *time-averaged* λ is not the average adverse-selection cost. Any empirical liquidity measure we use should be volume-weighted, or we should say why the bias does not matter. This belongs on the referee checklist under "parser/measure validation".
- **R8 gives us a comparative static on informed profits**: stochastic (as against merely high) liquidity *reduces* insider profits. If a disclosure rule changes the predictability of the trading window rather than its level, R8 says the profit effect need not have the sign one expects from level effects alone.

**What is left open for us — three certified pieces of whitespace:**
1. **Learning about presence.** CDF assume the insider's presence is common knowledge (p. 1464), and grep confirms the paper never uses the word "learn". The disclosure rule's whole economic content is that it converts a *pooled* state (the market does not know a blockholder is there) into a *flagged* one. CDF's own list of future work names this gap in one sentence. Our **partition** is unoccupied.
2. **The horizon as a policy instrument.** T is fixed and exogenous here. **(qualified by verifier)** The *random*-horizon case is already occupied — Baruch (2002), Back–Baruch (2004) and Caldentey–Stacchetti (2010, "Insider Trading With a Random Deadline", *Econometrica* 78(1)), all cited at p. 1450, and CDF's own 2016a working paper at p. 1458 fn. 10 — and in those models λ is a *super*martingale, the opposite drift to CDF 2016. So the whitespace is narrower than "T is a primitive": what is unoccupied is T as a **filing window fixed by a disclosure rule**, known in length, triggered by the blockholder's own crossing of a stake threshold, and **moved on a dated day** (10 → 5 business days, 2024-02-05). State it that way; "nobody has made the horizon non-fixed" is refutable in one citation.
3. **No control outcome, full stop.** The insider's information is never acted on; v is exogenous and the insider is a pure trader. There is no engagement, no value creation, no bidder, no premium. Our **control outcome** object is unoccupied by this paper and by the microstructure tradition it summarises.

**What constrains us.**
- **The exogeneity restriction is a real modelling discipline.** CDF need σ not to be Granger-caused by order flow for G_t to be independent of the insider's strategy (p. 1445, p. 1460). If our model lets a disclosure event change subsequent noise trading — which is exactly what a 13D filing plausibly does — we cannot borrow their solution method wholesale; we would need either a discrete-time formulation or an explicit argument for why the feedback is second-order. Flag this before the core model is written.
- **λ is not our κ.** CDF's λ is an *outcome* (price impact), our κ is a *primitive* (noise-trading intensity). Their σ_t is our κ. Keeping this straight matters: a referee who reads "liquidity" in both papers will otherwise see a contradiction where there is none.
- **Their calibration numbers are illustrative, not estimates.** Table I's values (σ^L = 0.2, σ^H = 0.4, T = 1, η = 2) carry the NUMERICAL label and should never be cited as magnitudes.
- **(added by verifier) A liquidity-timing model can leave no trace in prices.** p. 1453: in the pure-martingale case price volatility, the information-flow rate and unconditional profits are *identical to Kyle's*; only λ and the trading rate move, and they offset exactly. If our empirical leg tries to detect the mechanism in price volatility or price paths, the model itself says it may find nothing. Test **trade timing** (accumulation speed against κ), which is also what CDF (2015) actually did.
- **(added by verifier) R14 is asserted, not proved.** §4.1 carries no theorem and no appendix proof; the article says "it can be shown that all our results above … are unchanged". We may cite the estimator-bias formula, but not as a theorem.

## 8. Quotes we may lean on (verbatim, page-cited)

*Line-break hyphens introduced by the PDF layout have been closed up; every other character (including the paper's single quotation marks around ‘liquidity timing’ and the like) is as printed.*

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "The volatility of price volatility appears ‘excessive’ because insiders choose to trade more aggressively (and thus more information is revealed) when uninformed volume is higher and price impact is lower." | p. 1441 | The one-sentence statement of the mechanism |
| Q2 | "Second, we find that the optimal trading strategy for the insider is to trade proportionally to the undervaluation of the asset at a rate that is inversely related to price impact but increasing in a measure of the current ‘state of liquidity’ that we identify below. We thus show that it is optimal for the insider to ‘time liquidity.’" | p. 1442 | R3, the liquidity-timing proposition — the theory behind "the blockholder accumulates when κ is high" |
| Q3 | "This is consistent with the empirical evidence in Collin-Dufresne and Fos (2015), who documented, using data from SEC filings, that informed activist-shareholder investors trade more aggressively when abnormal volume is higher and measured price impact is lower." | p. 1442 | The explicit theory ↔ CDF-2015 link |
| Q4 | "The intuition why price impact is a submartingale in our model is that, with stochastic noise trading volatility, the insider has an option to wait for better liquidity (i.e., higher noise trading volatility) to trade. In equilibrium, price impact must increase on average to entice the insider to trade early and give up his option to wait for better liquidity states." | p. 1450 | R4 and the option-to-wait logic our window margin caps |
| Q5 | "The main (economic) restriction we require throughout is that the noise trading volatility process is independent of the insider’s private information and that it may not be Granger-caused by order flow (i.e., m and ν cannot depend on v or on Y t)." | p. 1445 | The exogeneity discipline our own model must confront |
| Q6 | "We assume that both the market maker and the insider observe the history of σ perfectly." | p. 1445 | Liquidity is common knowledge — no learning about the market state |
| Q7 | "Note that this requires that volatility be common knowledge. Else there could be multiple equilibria where the strategy of the insider is not absolutely continuous." | p. 1445, fn. 3 | Relaxing observability is not a small perturbation — a caution for our partition |
| Q8 | "Fourth, we assume that the presence of the insider is common knowledge." | p. 1464 | **The scope quote.** Blockholder detection / the flagged-vs-pooled partition left to future work |
| Q9 | "Second, we assume that the horizon is fixed." | p. 1464 | **The scope quote for the window margin.** T is a primitive, not a rule |
| Q10 | "Exploiting an SEC disclosure requirement that requires activist shareholders to file a 13D schedule in which they report past trades in target stocks when they hit the 5% ownership threshold, CF built a sample of trades by activist investors." | p. 1462, fn. 11 | The **only** appearance of the disclosure rule in the paper — proof it is a data source, never a modelled margin |
| Q11 | "One implication of our model is that, while at an individual trade level price impact does represent the transaction cost paid by a noise trader, over any finite period average price impact may not be a valid measure of aggregate (or average) adverse selection costs when both σt and λt change over time." | p. 1461 | R11 — the measurement warning our empirical leg must respect |
| Q12 | "So, for example, in this more general model, a regression of price changes on total order flow (which is typically used to estimate Kyle’s lambda in empirical papers) delivers an estimate of price impact ‘regression coefficient’" | p. 1461 | R14 — the estimator bias in the standard Kyle-lambda regression |

## 9. Verification log

**Verifier:** independent agent, 2026-08-19. **Checked against:** `research/txt_extracts/collin_dufresne_fos_2016_ecta.pdf` re-extracted page by page with `pdftotext -f N -l N -layout`, plus a page-mapped flattening of the `.txt` (PDF p. 1 = printed p. 1441; 35 pages, map confirmed by the running heads and the front matter). Not against the card author's reasoning, which the verifier never saw.

**Counts:** OK 31 · WRONG 2 · MISCITED 3 · UNCHECKED 3.

### Header / venue
| Item | Verdict | Checked against |
|---|---|---|
| *Econometrica* 84(4), 1441–1475, July 2016 | OK | p. 1441 masthead "Econometrica, Vol. 84, No. 4 (July, 2016), 1441–1475" |
| Received May 2012, final revision February 2016, Co-editor Lars Peter Hansen | OK | p. 1475 colophon, verbatim |
| Supplemental Material "cited at pp. 1454 and 1458" | **MISCITED → fixed** | Collin-Dufresne & Fos (2016b) — **both** Appendix S1 (fn. 8) and Appendix S2 (fn. 9) are cited at **p. 1454**; the reference list back-links it to [1454] only. p. 1458 cites CDF **2016a**, the *Random Horizon* working paper, not the supplement. |

### Quotes (§8) — all twelve, plus the §4 and §6 block quotes, re-grepped against the printed page named
| # | Verdict | Note |
|---|---|---|
| Q1 p. 1441 | OK | abstract; the single quotes around ‘excessive’ are as printed |
| Q2 p. 1442 | OK | |
| Q3 p. 1442 | OK | exact; the source hyphenates "Collin-Dufresne" across a line break, and the card restores it correctly |
| Q4 p. 1450 | OK | |
| Q5 p. 1445 | OK | exact up to the source's spacing inside "(… on Y t )" |
| Q6 p. 1445 | OK | |
| Q7 p. 1445, fn. 3 | OK | confirmed to be in footnote 3 |
| Q8 p. 1464 | OK | |
| Q9 p. 1464 | OK | |
| Q10 p. 1462, fn. 11 | OK | confirmed to be footnote 11 on p. 1462 |
| Q11 p. 1461 | OK | |
| Q12 p. 1461 | OK | truncation before the inline formula is faithful |
| §6 block quote (full conclusion future-work list, p. 1464) | OK | five items, word for word, including "And last, we assume that the insider and market makers are risk-neutral." |
| §4 block quote (fn. 11, p. 1462) | OK | identical to Q10 |

### Results (§3) and method claims (§2)
| Claim | Verdict | Checked against |
|---|---|---|
| R1 Lemma 1 + bounds σ̲²(T−t) ≤ G_t ≤ σ̄²(T−t); uniqueness | OK | Lemma 1 (i)–(ii) and eq. (12), p. 1448; proofs A.1 p. 1464 and A.2 p. 1465 |
| R2 Theorem 1: eqs. (13)–(19), κ_t = σ_t²/G_t, θ* = (κ/λ)(v−P), Σ_t = Σ₀e^{−∫κ}, λ = √Σ/G, J = ((v−P)²+Σ)/2λ, unconditional profit √(Σ₀G₀), martingale/bridge/submartingale | **OK, every component** | pp. 1448–1449, eqs. 13, 14, 16, 17, 18, 19 and the three closing paragraphs; proof A.3 pp. 1465–1472 (Lemmas 2–8) |
| R2's conditional form ("*If* there exists a bounded solution … *and if* σ is uniformly bounded") | OK | The card states the hypotheses rather than the conclusion alone — correct, and the PROVED label is earned |
| R3 liquidity timing, eq. (16) | OK | p. 1448 eq. (16); p. 1449 discussion; p. 1450 "the idea that the insider trades at a deterministic rate inversely related to the remaining time horizon T − t does not hold outside these specific cases" |
| R4 λ submartingale; contrast with Baruch (2002) / Back–Baruch (2004) | OK | Theorem 1 closing line p. 1449; Lemma 5 p. 1469; p. 1450 and fn. 6 |
| R5 eq. (25) λ_t = e^{∫m}σ_v/σ_t; m=0 ⇒ λ ∝ 1/σ_t | OK | eq. (25) p. 1452; p. 1453 "Price impact is inversely related to noise trading volatility" |
| R6 bridge process / martingale in MM filtration | OK | p. 1449; Lemmas 3–4, pp. 1467–1468 |
| R7 stochastic price volatility requires stochastic m_t | OK | Theorem 2, pp. 1451–1452 (statement starts p. 1451); §3.1 pp. 1453–1454; §3.2 opening p. 1454 |
| R8 stochastic σ *reduces* unconditional insider profit | OK | p. 1451; Lemma 6 p. 1469 |
| R9 price-discovery rate rises with σ | OK | p. 1450, "Fifth, since in equilibrium dΣ_t = −dP_t², …" |
| R10 eq. (20) slippage costs path-dependent | OK | eq. (20) p. 1451; derivation A.4 p. 1472 |
| R11 high/low vs low/high: costs 0.054 vs 0.057, 'number' 0.085 both, avg λ 1.023 vs 0.853; normalized λ tracks costs | **OK, exact** | Table I p. 1459, Panels A–D (normalized costs 0.636 vs 0.671, same ordering as the raw costs); §4.2 p. 1461 |
| R12 "average price volatility 0.174–0.195 vs Kyle 0.2 — volatility *highest* on the low/low path" | **WRONG → fixed** | Table I Panel E, p. 1459: totals are 0.195 (high/high), **0.174 (low/low — the lowest, not the highest)**, 0.190, 0.182. The low/low path's *split* is 0.106 / **0.242**, the largest half-period figure in the panel, and Fig. 2(a) p. 1457 shows the terminal spike the card had in mind. The claim was right about the mechanism and wrong about the statistic; rewritten to say time-average vs late-period. Kyle = 0.2 confirmed in Table I note a. |
| R13 mean-reversion higher in the high state; κ^L, κ^H → ∞ as t → T | OK | p. 1456; NUMERICAL label is appropriately conservative (the first half reads off Fig. 1, the second is the finite-maturity argument) |
| R14 label **PROVED** | **WRONG → fixed** | §4.1 (pp. 1460–1461) contains **no theorem and no appendix proof**. The article says only "it can be shown that all our results above (and in particular Theorem 1) are unchanged", and λ̂ = λσ²/(σ²+η²) is a one-line in-text derivation. Label downgraded to ASSERTED. The *content* of the claim is correct and is on p. 1461. |
| The §4.1 estimator-bias statement itself (λ̂ = λ_tσ_t²/(σ_t²+η(t)²), equals λ only if η = 0) | OK | p. 1461, verbatim formula |
| R15 Corollary 1, τ_t = T(1 − e^{−∫σ²/G}) | OK | eq. (37) p. 1463; proof A.7 p. 1474 |
| §2 primitives: eq. (1) p. 1444, A = {θ : E∫θ² < ∞}, eq. (2)–(3) p. 1445, eq. (4) p. 1445, σ observed perfectly p. 1445, F^Y ⊇ σ^t p. 1446 | OK | all confirmed |
| §2 "λ_t = β_tΣ_t/σ_t²" | **MISCITED → fixed** | Not printed anywhere in the article. p. 1446 prints θ_t = β_t(v−P_t), dP_t = λ_t dY_t (5) and dΣ_t = −λ_t²σ_t² dt (6). Card now cites (5)–(6) and flags the filtering relation as unprinted. |
| §2 "Theorem 3, eqs. 29–30, p. 1455" | **MISCITED → fixed** | Theorem 3 is *stated* on p. 1454; eqs. (29)–(30) are printed on p. 1455. |
| §2 "Σ₀ = 0.04 (Fig. 1) **or** Σ₀ = 0.2² … (Fig. 2, Table I)" | **corrected** | 0.2² = 0.04. Fig. 1 (p. 1455) and Fig. 2 (p. 1457) use the *same* calibration written two ways; the card implied two. |
| §2 "eq. 11, p. 1447"; G_t as "equilibrium noise component", p. 1448 | OK | both exact |
| Nesting: Kyle recovered as G = σ²(T−t) | OK | p. 1452, "Bt = T − t … price impact constant equal to λ = σ_v/σ" |

### Scope claims (§4, §6) — every "zero hits" claim grepped on the dehyphenated full text
| Claim | Verdict | Count |
|---|---|---|
| `takeover` | OK | **0** |
| `control` | OK | **0** |
| `blockholder` | OK | **0** |
| `learn` | OK | **0** |
| `announce` | OK | **0** |
| `bidder`, `premium`, `campaign` | OK | 0 / 0 / 0 |
| `13D`, `5%`, `disclos*`, `threshold` — footnote 11, p. 1462 only | OK | 1 each, all inside fn. 11 (the `threshold` hit is the footnote's "ownership threshold", hyphenated across the line in the raw extract) |
| `window` — 0 hits | OK | 0 |
| `activist` outside fn. 11 | **noted, not a card error** | 3 hits total: p. 1442 (Q3, "activist-shareholder investors") and 2 in fn. 11. The card claims only that the *rule* appears once, which is correct. |
| "no data, no estimation anywhere" | OK | no sample, period, table of estimates, or standard error anywhere in the article |

### Omissions found and added (marked "(added by verifier)" in place)
1. **p. 1450 + fn. 6 — the random-horizon case is already occupied, and it flips the sign.** Baruch (2002) and Back–Baruch (2004) get a *super*martingale λ "because the horizon is random", and **Caldentey and Stacchetti (2010), "Insider Trading With a Random Deadline," *Econometrica* 78(1), 245–283** is listed at p. 1450 among those extensions. **Added to §5 and used to narrow §7's whitespace claim #2** — this was the card's most exposed sentence, and it is the one a referee would break first.
2. **fn. 10, p. 1458 — the deadline comparative static.** With T an unpredictable stopping time of constant arrival intensity, Σ_t is *always* decreasing convex, with faster decay in the high-volatility state; the convex→concave switch disappears. Directly usable if our window margin is an arrival intensity. **Added to §5.**
3. **p. 1461 §4.1 — CDF's own two-group split of uninformed order flow**: trades the insider can hide behind (pay λ) versus trades "known to be pure noise" (pay nothing), with the explicit line that if the market maker could tell them apart "they would each pay different trading costs". A priced flagged/pooled split — exogenous, about noise traders, disposed of in a paragraph. The closest thing to our partition in the paper. **Added to §6.**
4. **p. 1453 — the martingale case is observationally silent in prices.** With m = 0, price volatility, the information-flow rate, the unconditional trading rate and expected profit all match Kyle; only λ and the realised trading rate move, and "both effects exactly offset to leave equilibrium prices unchanged". Our test must look at trade timing, not price paths. **Added to §5 and §7.**
5. **p. 1446 — prices alone may not reveal σ.** "when uninformed order flow has stochastic volatility, observing only prices may not be sufficient to recover noise trading volatility"; common observability of σ is defended by data availability, not derived. **Added to §6.**
6. **p. 1462 — CDF (2015)'s liquidity timing is partly market-wide**, keyed to abnormal S&P 500 volume as well as stock-level volume. Bears on whether our κ is firm-level or a common factor. **Added to §4.**
7. **fn. 6, p. 1450 — competition among informed traders** (Foster–Viswanathan 1996; Back, Cao, and Willard 2000) also raises price impact near the horizon. If our model has two blockholders, the submartingale result stops being distinctive. **Added to §5.**

### UNCHECKED (left in place, marked here — not triaged away)
1. **Supplemental Material (CDF 2016b, Appendices S1 and S2), cited at p. 1454.** Not in the repo; a separate Econometrica file. S1 discusses the insider's optimal strategy in more detail, S2 the mean-reverting-diffusion case with a stochastic growth rate. No claim on this card depends on either — confirmed by reading the two footnotes that cite them. **Not decision-critical**, but it is where any sensitivity analysis would live, and the card's "no sensitivity analysis in the article" weakness should be read as "none in the article", not "none anywhere".
2. **CDF 2016a, "Insider Trading With a Random Horizon" (working paper, SFI/EPFL), cited p. 1458 fn. 10 and listed p. 1474.** The card's §7 says it "makes T random but still not chosen and still not legal". The verifier cannot confirm the content of a paper not in the repo — the *title* and fn. 10's one-sentence summary are all the evidence there is. **Decision-critical for positioning:** whitespace claim #2 rests partly on what that paper does *not* do. Read it, or state the whitespace only in terms of the published Caldentey–Stacchetti (2010) and Back–Baruch (2004) results, which are checkable.
3. **CDF (2015, *JF* 70(4), 1555–1582).** The card's §7 leans on it for "λ falls while activists accumulate". The 2016 article's characterisation of it (pp. 1442, 1462) is what was verified, not the 2015 paper itself. A separate card should carry that weight. (A PDF is in the repo at `research/txt_extracts/collin_dufresne_fos_2015_jf.pdf` but is outside this verifier's assignment.)

### Overall verdict
**The card is accurate and its scope greps hold exactly** — takeover, control, blockholder, learn and announce are all genuinely zero, and the disclosure rule genuinely appears once, in footnote 11 on p. 1462, describing a different paper's sample. All twelve quotes plus both block quotes are verbatim on the pages named. Two things were wrong: **R14 carried a PROVED label that §4.1 does not earn** (no theorem, no proof — "it can be shown"), and **R12 asserted the low/low path has the highest price volatility when Table I Panel E shows it has the lowest time-average** (0.174) and only the highest late-period value (0.242). Three citations were off by a page or a footnote. The material gap was §5/§7 not knowing that **a random horizon already appears in this literature and reverses the drift of λ** (Baruch 2002; Back–Baruch 2004; Caldentey–Stacchetti 2010, all cited on p. 1450) — the window-margin whitespace has been narrowed accordingly, from "T is not random anywhere" to "T is nowhere a legal filing window triggered by the blockholder's own threshold crossing".
