> **SUPERSEDED.** This card reads the August-2016 working paper. The paper the field cites is the published version; see `research/cards/corum_levit_2019_jfe_published.md` (JFE 133(1), 1–17, 2019), whose §10 lists what changed. Use this card only as a record of the WP.

# Corum & Levit (2016/2019) — "Corporate Control Activism"

**Venue / status:** Published as *Journal of Financial Economics* 133(1), 1–17 (2019). **The version read here is a WORKING PAPER dated August 11, 2016** (title page: "Adrian A. Corum, Wharton / Doron Levit, Wharton / August 11, 2016"), 45 pages. It is not the published JFE article: it has no JFE masthead, no volume/issue/DOI, no "Received/Accepted" block, its references cite Back et al. and Boyson et al. as 2016 working papers, and it points to an Online Appendix (Appendices B and C) that is **not included in the file**. Numbering, proposition labels and figures may differ from the published version.
**Full text from:** `lit/corum-levit-2019.pdf` (45 pages) · re-extracted with `pdftotext -layout`; `research/txt/corum_levit_jfe2019.txt` is the same 2016 WP · **Reader:** opus · **Read:** full text, 45 pages (body pp. 1–31, references pp. 32–35, Appendix A proofs pp. 36–45)
**Page-numbering convention:** printed page number of the WP, which equals the PDF page index throughout.
**Extraction caveat:** this PDF's font encoding breaks the fi/fl/ff/ffi ligatures (they extract as …, ‡, ¤, ¢) and drops **every Greek symbol and every math glyph**. Quotes in §8 have the ligatures restored (so "bene…ts" is quoted as "benefits"). **CORRECTED BY VERIFIER — the first reader reconstructed the dropped Greek letters by guesswork and got most of them wrong.** The verifier re-read pp. 9, 12, 19–24, 26, 30–31, 44–45 as rendered images (`pdftoppm -r 150 -png`) and read the symbols off the page. The corrected dictionary is:

| Object | Paper's symbol | What the first draft of this card wrongly used |
|---|---|---|
| proxy-fight cost | **κ** | γ |
| ex-ante probability of a takeover | **θ\*** | Π |
| activist's expected trading profit | **Π(α)** (Eq. 8, p. 21) | — (the card gave Π the wrong referent entirely) |
| binary state "firm is a viable target" | **ζ ∈ {0,1}**, prior μ | θ |
| precision of the activist's signal y | **φ** | π |
| probability the activist buys 2L (mixing prob.) | **σ\*** | θ |
| probability the board can still block (§5.3) | **λ ∈ [0,1]** | φ |
| minority-share value under bidder control, q + φΔ (§5.3) | **φ ∈ [0,1]** | — (absent) |

**Notation collision to flag in any lit table:** their **κ is the proxy-fight cost**; our κ is noise-trading intensity. Never carry κ across the two papers unlabelled.
**Type:** theory   **Role for us:** competitor

> ## ⚠ READ FIRST — the PUBLISHED version breaks this card's central claim
>
> *(added by verifier, 2026-08-19, from `research/txt_extracts/corum_levit_2019_jfe_published.txt` — JFE 133 (2019) 1–17, received 24 Aug 2017, revised 29 May 2018, fetched by another agent while this verification was running.)*
>
> **The published article replaced the Kyle noise-trader block with an explicit disclosure threshold, and says so.** Published §4, p. 10:
>
> > "we assume that the market maker can condition the price on the order flow if and only if the order is strictly larger than **ᾱ** ∈ (0, 1). That is, **the stock is perfectly liquid (illiquid) for small (large) orders.** Parameter **ᾱ can also be interpreted as a disclosure threshold (e.g., regulation 13D).** Moreover, buying up to ᾱ shares does not trigger a poison pill if such exists. **Empirically, ᾱ ∈ [5%, 10%].**"
>
> and footnote 23: *"A previous version of the paper assumed the existence of liquidity traders à la Kyle (1985) and showed that similar results hold under this alternative formulation."* — i.e. **the 2016 WP this card reads is the superseded formulation.**
>
> **Consequences for §6 and §7, which the rest of this card has not yet absorbed:**
> 1. **"There is no 5% threshold in the model" is FALSE of the published article.** There is a threshold ᾱ, it is explicitly labelled a 13D disclosure threshold, and it is calibrated to 5–10%. §7 pt 1 ("they have no threshold … and no 13G") must be rewritten: only *no window, no delay, no 13G* survives. **The threshold margin is occupied.**
> 2. **Liquidity is no longer only a concealment device.** ᾱ is simultaneously a liquidity parameter ("perfectly liquid (illiquid) for small (large) orders") and the disclosure threshold — the two are the *same* parameter. Our separation of κ (liquidity) from the partition is therefore a genuine modelling difference, but it must be argued, not asserted, and §7 pt 4 ("their liquidity is degenerate") overstates the whitespace.
> 3. **The published version has seven numbered Predictions** (1–7), including *Prediction 5* (policies undermining activism hurt takeovers), *Prediction 6* (takeover probability is **U-shaped** in b — the published form of WP Prop. 4), and *Prediction 7* (takeover probability weakly decreasing in the proxy-fight cost). §6's "no empirical implications section, 'testable' never appears" is true of the 2016 WP **only**.
> 4. **Structure differs throughout:** the published article has Lemma 1, Propositions 1–7, Corollaries 1–2, and Appendices **A (proofs), B (limited veto power), C (the role of a majority stake) all printed in the article** — no Online Appendix. Every proposition number in §3 below is a WP number and does not map to the published one.
> 5. **What survives unchanged:** κ is still the proxy-fight campaigning cost (published p. 4); the bidder still never starts a proxy fight (published Prop. 1); the commitment problem, the complementarity, and the selection-vs-treatment identification logic are all intact.
>
> **Action:** this card must be re-read against the published article before any positioning paragraph is written. Treat §§3, 5, 6, 7 below as a record of the 2016 WP, not of the paper the field cites.


## 1. Question

Why do activist hedge funds, not bidders, run the proxy fights that unseat entrenched target boards? Boards with a de facto veto (poison pills) can block value-increasing takeovers to protect private benefits, and the only way through is a contested election — yet Fos (2016) finds only 5% of 632 proxy fights 2003–2012 were sponsored by corporations and 70% by activist hedge funds (p. 2, fn. 3). Corum and Levit identify a **commitment problem**: a bidder who wins board control sits on both sides of the table and will low-ball, so rational shareholders will not elect him. An activist, being on the sell-side, is trusted. From this they derive a complementarity between activism and takeovers, and an identification strategy for separating the activist's treatment effect from selection.

## 2. Model / data and method

**Primitives (Section 2, pp. 7–10).** Players: incumbent board, bidder, one activist, passive investors, all risk-neutral. Total shares normalised to 1; one share one vote; takeover needs ≥50% of votes. Initial holdings: board n ≥ 0, activist α > 0, bidder m ≥ 0, with n + α + m < 0.5 so passive investors hold the majority. Board's private benefits of control B > 0, lost if the firm is acquired or if it loses the board; per share b ≡ B/n. Target standalone value q > 0; bidder creates net value Δ > 0 only by acquiring. **The bidder cannot bypass the board with a tender offer** (poison pill) in the baseline.

**Timing (Figure 1, p. 9).** Round I bargaining, bidder vs incumbent board: with probability s the board proposes, with 1 − s the bidder proposes, take-it-or-leave-it; any agreement needs a shareholder vote. If Round I fails or is voted down → **proxy fight stage**: bidder and activist simultaneously decide whether to run one, each paying a non-reimbursable private cost **κ > 0** (*corrected by verifier*; p. 9 also says κ "decreases with the fraction of the firm that is held by institutional investors or the governance expertise of the challenger" — a mapping from ownership structure to the proxy cost we can use); shareholders elect one team. → Round II bargaining with whoever now controls the board. If Round II fails, the target stays independent at q.

**Equilibrium notion:** Subgame Perfect Equilibrium in pure strategies for the baseline (p. 10); Perfect Bayesian Equilibrium for the extended trading model (p. 20), with two stated refinements (positive expected activist profit on the equilibrium path; a bound on the market maker's off-equilibrium beliefs — fn. 25, p. 22).

**Functional forms that buy tractability:**
- **No commitment for anyone.** Whoever wins the board maximises the value of the party they are affiliated with (p. 10). This single assumption is the whole engine.
- **Diversion is "limited and arbitrarily small"** so that an indifferent shareholder retains the incumbent (p. 10) — a tie-breaking device, relaxed only in the (absent) Online Appendix C.4.
- **Random proposer with a single parameter s**, interpreted as target bargaining power; microfounded by reference to Rubinstein (1982) (fn. 10, p. 8).
- **Δ and q commonly known** in the baseline (p. 8); asymmetric information relegated to Online Appendix C.3.
- **Binary signal, two-point noise trade.** *(symbols corrected by verifier against pp. 19–20 of the PDF.)* In the extension (Section 4.1, pp. 19–20): a binary state **ζ ∈ {0,1}** with prior Pr[ζ=1] = μ ∈ (0,1); if ζ = 0 the firm is not a viable target and Δ ≤ 0 with certainty. The activist gets a binary signal y ∈ {0,1} with **precision φ**: Pr[y=1|ζ=1] = 1 and Pr[y=1|ζ=0] = 1 − φ, so y = 0 reveals ζ = 0 with certainty and y = 1 raises the posterior to μ̂ ≡ μ/(1 − φ(1−μ)). **Liquidity traders buy L ∈ (0, ½) shares with probability ½ and nothing with probability ½**; the activist cannot buy more than 2L. Bidder's due-diligence cost c ~ G with full support on [0, ∞); Δ | ζ=1 ~ F, differentiable, full support on the real line, with **E[Δ | ζ = 1] ≤ 0** ("finding a corporate asset with which the bidder can create synergies is hard", p. 19) — this is what forces due diligence to be necessary.
- **m = 0 in the whole extension** (p. 20) — the toehold is switched off exactly where trading is introduced.

**No data, no estimation.** Numerical figures (Figures 2 and 3) are illustrations at **L = 0.1, s = 0.75, κ = 0.225, μ = 0.6, φ = 0.5, Δ ~ N(0,5), c ~ LogN(−1.62, 0.13)** (captions pp. 26 and 27 — *symbols corrected by verifier*). Note L is fixed at 0.1 in both figures: there is no figure that varies L.

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where (page / prop / table) |
|---|---|---|---|
| R1 | **Lemma 1** — Round II outcome and expected shareholder value under each of the three board identities: q + 1{Δ/(1−m) ≥ b}[sΔ/(1−m) + (1−s)b] if the incumbent retains control; q + sΔ/(1−m) if the activist controls; **q if the bidder controls** | PROVED | Lemma 1, p. 11; proof pp. 36–37 |
| R2 | **Proposition 1(i)** — the bidder **never** runs a proxy fight, in any equilibrium of the subgame, regardless of Δ, **κ**, m, b, or what the activist does | PROVED | Prop. 1(i), p. 12; proof pp. 36–39 |
| R3 | **Proposition 1(ii)** — the activist runs a proxy fight iff **(κ/s)/α ≤ Δ/(1−m) < b**, and whenever she runs it she wins *(verifier: symbol γ→κ, and the first inequality is **weak**, not strict — Eq. (2) reads ≤)* | PROVED | Prop. 1(ii), Eq. (2), p. 12 |
| R4 | **Proposition 2** — unique equilibrium: if min{b, **(κ/s)/α**} ≤ Δ/(1−m) the deal closes in Round I at π = q + sΔ/(1−m) + (1−s)b·1{Δ/(1−m) ≥ b}; if Δ/(1−m) < min{b, **(κ/s)/α**} the target stays independent | PROVED | Prop. 2, Eq. (3), p. 13 |
| R5 | **Corollary 1** — conditional on due diligence and on ζ: expected shareholder value q + ζv(α), **bidder's expected profit ζ(w(α) − v(α))** (*verifier: ζ, not μ*), value created ζw(α); "all three terms strictly increase in α when **(κ/s)/α < b** and are invariant to α otherwise". The **unconditional** expected takeover premium is a separate object, **h(α) ≡ G(w(α) − v(α))·v(α)** (Eq. 7, p. 21) | PROVED | Cor. 1, Eqs. (5)–(7), pp. 20–21 |
| R6 | **Proposition 3** — α\*(0) = 0 always; an equilibrium with α\*(1) = 0 exists iff Eq. (9); a **unique** equilibrium with α\*(1) > 0 exists iff h(2L)/h(L) < 2, in which **α\*(1) = 2L with probability σ\* ∈ [0,1) and L with probability 1 − σ\*** (*verifier: σ\*, not θ*), σ\* in closed form (Eq. 10) and prices in Eq. (11). The **interior** case σ\* ∈ (0,1) requires the sharper two-sided condition **1 + ½(μ̂−μ)/μ̂ < h(2L)/h(L) < 2** (p. 23) — the card previously reported only the upper bound | PROVED | Prop. 3, pp. 22–23; proof pp. 40–44 |
| R7 | **Corollary 2** (given h(2L)/h(L) < 2, in the unique equilibrium with α\*(1) > 0) — exact partition: *treatment only* iff **(κ/s)/L < b**; *both selection and treatment* iff (κ/s)/(2L) < b ≤ (κ/s)/L **and** 1 + ½(μ̂−μ)/μ̂ < h(2L)/h(L); *selection only* otherwise | PROVED | Cor. 2, Eqs. (12)–(14), p. 24 |
| R8 | **Proposition 4 (the non-monotonicity)** — "If the equilibrium exhibits only selection then **θ\*** is strictly decreasing in b. If the equilibrium exhibits treatment then **θ\*** is non-monotonic in b." (**θ\*** = ex-ante takeover probability, Eq. 15, p. 25; b = incumbent's private benefits per share). *(Verifier: the symbol is θ\*, read off the rendered page. It is **not** Π — in this paper Π(α) is the activist's expected trading profit, Eq. 8, p. 21.)* | PROVED, **with two caveats, both confirmed by the verifier**: (a) the proof of the second half establishes the *increasing* branch only inside a worked case — p. 44 reads "Next, suppose the equilibrium exhibits treatment. **For example, suppose σ\* = 0 and (κ/s)/L < b**" — and derives ∂θ\*/∂b > 0 ⟺ b > (1 − F(b))/f(b) (p. 45). The full non-monotone shape is NUMERICAL (Figure 2, one parameter vector). (b) fn. 28, p. 26 restricts the whole statement to **local** comparative statics of the α\*(1) > 0 equilibrium, "where the equilibrium continues to exist upon a small change in the parameter" | Prop. 4, p. 26; proof pp. 44–45; Figure 2 p. 26 |
| R9 | Solicitation effect: activist presence signals the board is sellable, raising the bidder's incentive to do due diligence — so the activist moves control outcomes *even when her ex-post proxy threat is not credible* | PROVED (within Prop. 3 / Cor. 2) but stated in the text as intuition | pp. 5, 21, 24 |
| R10 | If h(2L)/h(L) ≥ 2 there is **no** equilibrium with activist entry: "the marginal effect of increasing the activist's position on the expected takeover premium is very large … the market maker realizes this temptation and prices the shares accordingly, leaving the activist with no profit in equilibrium" (p. 23) | PROVED | *(verifier: cite **Prop. 3(ii)**, p. 22 — the "if and only if h(2L)/h(L) < 2" — plus the discussion on p. 23. Prop. 3(i) is the α\*(1)=0 existence condition Eq. (9), a different statement)* |
| R11 | Motivated-seller extension: with a board too eager to sell, the activist raises the premium without raising deal probability, so activism and takeovers become **substitutes** | ASSERTED in the WP text — "The formal results and their proofs are given in the Online Appendix", which is absent from this file | §5.1, pp. 28–29 |
| R12 | Non-control activism (a standalone-value proposal of size ε) complements corporate-control activism if ε is small, substitutes if ε is large | ASSERTED (same reason: Online Appendix) | §5.2, pp. 29–30 |
| R13 | Limited veto power: with probability **λ ∈ [0,1]** the deal is blocked and with 1 − λ the bidder can tender directly (the baseline model is the special case λ = 1); the post-takeover value of minority shares under the bidder's control is q + **φ**Δ, φ ∈ [0,1]. "the activist runs a proxy fight if and only if **(κ/s)/(αλ) ≤ Δ < b**", so the activist matters *more* when λ is larger — activists play a smaller role where boards are weaker (U.S. in the 1980s, the U.K.). *(All four symbols corrected by verifier from the rendered pp. 30–31; the card previously conflated λ and φ.)* | ASSERTED (same reason) | §5.3, pp. 30–31 |
| R15 | *(added by verifier)* **§4.2.1 "Arbitrage activism — activist moves last" (p. 28)**: a variant in which the bidder's due-diligence decision precedes the activist's trade (h(·) is replaced by v(·), and not investing is no longer a bad signal). "It can be shown that the activist can still profit…" — the complementarity survives. This sits in the **main text**, not §5, but is equally unproved in this file | ASSERTED | §4.2.1, p. 28 |
| R16 | *(added by verifier)* **The activist's intervention can LOWER the premium.** fn. 29, p. 27: if b is small the bidder reaches agreement with the incumbent and pays sΔ + (1−s)b; if b is large he can only close with the activist's help and "pays a **lower** premium of sΔ". So more entrenchment ⇒ higher deal probability but a *smaller* premium conditional on a deal | PROVED (implied by Lemma 1 / Prop. 2) | fn. 29, p. 27 |
| R17 | *(added by verifier)* **The trading result does not depend on their own microfoundation of the premium.** fn. 24, p. 21: "the results in this section continue to hold even if h(α) stems from a different microfoundation, as long as h(α) is an increasing function. See Back et al. (2016) for a dynamic model … where the mapping from activist's ownership to firm value is exogenous." Our model can therefore be *plugged into* their §4 rather than competing with it | ASSERTED (a generality claim, no proof given) | fn. 24, p. 21 |
| R14 | Legal/economic "solutions" to the bidder's commitment problem (fiduciary duties, competition, independent nominees, reputation, standalone value creation, proxy-fight-plus-tender-offer) are each imperfect or costly | ASSERTED (discursive, §3.2, no formal result in this file; B.1–B.3 are in the absent Online Appendix) | pp. 13–16 |

## 4. Institutional facts used

- Fos (2016): 632 proxy fights 2003–2012, of which **only 5% sponsored by corporations (potential bidders), 70% by activist hedge funds** (p. 2, fn. 3). This is the motivating fact the whole paper is built to explain.
- Greenwood and Schor (2009), Boyson et al. (2016): probability of a takeover is several times higher when an activist hedge fund is a shareholder (p. 2). Boyson et al.: a bid is announced within 2 years in **70%** of activist events, and in **30%** the activist enters after an acquisition agreement is announced but before closing (p. 28); the activist is also the bidder in **15%** of events (fn. 17, p. 16).
- Delaware / US law: merger proposals reach a vote only via the board; tender offers need no vote but are vulnerable to pills (fn. 2, p. 2); non-redeemable pills are illegal in most states including NY and Delaware (fn. 12, p. 10); Entire Fairness vs Business Judgment review (p. 14); the Revlon Rule (p. 14); **SEC Rule 14a-9** requires the activist to disclose net economic exposure in a proxy solicitation (p. 19).
- Two-tier "anti-activism" poison pill upheld for Sotheby's against Third Point, Del. Ch. 2014 (fn. 6, p. 5).
- Declassification: only 11% of S&P 500 had a classified board in 2013, down from 57% in 2003 (fn. 11, p. 9).
- Cases: KKR/Gardner Denver after ValueAct's 5% stake, $3.7bn, 2013, with the Roberts quote (p. 2); Valeant/Allergan/Pershing Square 2014 as the failed-collaboration case (p. 18).
- Collin-Dufresne et al. (2016): activists rarely trade derivatives, limiting empty voting (p. 19).
- *(added by verifier — this is the paper's third "13D" mention and the card missed it)* **p. 8, the fact that licenses the whole design:** "consistent with Greenwood and Schor (2009) and Becht et al. (2015), who show that the positive abnormal returns around 13D filings by activist investors stem mostly from events in which the target is eventually acquired, we assume that the activist cannot affect the standalone value of the target." This is why their model is a pure control-outcome model, and it is the empirical bridge from announcement returns to control outcomes. (Relaxed in §5.2.)
- *(added by verifier)* **Sotheby's / Third Point detail:** the 2014 Delaware two-tier pill was aimed at blocking Third Point from going **above 10%** (fn. 6, p. 5) — a stake ceiling, worth noting next to the 5% flag.

## 5. Referee-facing strengths / weaknesses

**Strengths:**
- The core mechanism is one sentence long, is not a knife-edge, and explains a first-order stylised fact (who runs proxy fights) that no prior model addressed. Prop. 1(i) holds for *all* parameter values — an unusually clean result.
- The credibility argument is **relative, not absolute** (p. 17): the activist may divert, may be short-termist, may have private benefits; all that is needed is that the bidder's conflict is worse. That makes the result robust to the obvious referee attack.
- §3.2's six candidate "solutions" is a genuine pre-emption of referee objections rather than a literature dump.
- Prop. 4 turns a comparative static into an identification strategy — a theory paper that hands empiricists a falsifiable sign test is rare and is the paper's main claim on empirical relevance.
- Prop. 3 is a *unique* equilibrium with a closed-form mixing probability, not a "there exists" result.

**Weaknesses / open flanks:**
- **This file's Sections 5.1–5.3 and Appendices B and C are unproved here** — the formal statements live in an Online Appendix that is not in the PDF. R11–R14 must be labelled ASSERTED until the published JFE version or the Online Appendix is obtained.
- The trading block is Kyle stripped to a two-point noise distribution (L or 0) with a hard cap of 2L on the activist's order. There is no continuous liquidity parameter, no price-impact schedule, and **no comparative static in L anywhere in the paper**. Liquidity is a device for concealment, not an object of study.
- The bargaining protocol is a single random-proposer parameter s. Everything about premium determination rides on it.
- Δ | θ = 1 has full support on the real line with E[Δ | θ=1] ≤ 0 — a modelling convenience with no empirical counterpart, and it is what forces due diligence to be necessary.
- The board's private benefits b ≡ B/n depend on the incumbent's own shareholding n, but n plays no other role and is set aside; comparative statics "in b" are therefore not cleanly interpretable as "in entrenchment".
- Prop. 4's treatment branch is proved by a worked case rather than in general (see R8), and the non-monotone shape the paper advertises is carried by Figure 2 at one parameter vector. *(Verifier confirms: the worked case is "suppose σ\* = 0 and (κ/s)/L < b", p. 44.)*
- *(added by verifier)* **Two equilibrium-selection assumptions carry the headline results and are stated only in footnotes.** fn. 27, p. 25: "When multiple equilibria exist, we assume that the equilibrium with higher ex-ante probability of takeover (or, equivalently the equilibrium with α\*(1) > 0) is in play." fn. 28, p. 26: Prop. 4 is a *local* comparative static of that same equilibrium. A referee who does not accept the selection gets neither Eq. (15) nor Prop. 4.
- The paper's own identification proposal — sign of the (agency problem × takeover probability) relation — requires measuring b in the cross-section, which is exactly the hard part and is not discussed.

## 6. What they do NOT do (scope boundary)

**Object.** Their objects are the **ex-ante probability of a takeover θ\*** (Eq. 15, p. 25 — *verifier: θ\*, not Π*), the **expected takeover premium** (v(α) conditional on a deal, Eq. 5; h(α) ≡ G(w−v)·v unconditional, Eq. 7), the identity of the proxy-fight challenger, and the activist's stake choice. They do *not* study announcement returns, campaign success rates, or post-campaign firm performance. Our "control outcome" (bidder entry, takeover premium, campaign success) is **squarely their object** — this is the closest competitor of the two papers on this card.

**Free-riding — explicitly out of scope in the baseline.** pp. 6–7: *"different from Burkart et al. (2000), Cornelli and Li (2002), Gomes (2012), and Burkart and Lee (2015), who study the interaction between bidders and target blockholders, we abstract away from the free-rider problem in tender offers of Grossman and Hart (1980). Instead, we focus on agency problems in the target firm and the ability of the target board to veto the takeover."* Grossman–Hart free-riding re-enters only in §5.3 (p. 30) once tender offers are allowed, and in §3.2.6 as a cost of the tender-offer-plus-proxy-fight route (p. 16).

**Information asymmetry about value — out of scope in the baseline.** p. 8: *"To focus the analysis on agency problems as the key friction, we abstract from information asymmetries about q or [Δ] and assume that they are both commonly known."* (relaxed in the absent Online Appendix C.3).

**Toehold — switched off where it would matter.** m ≥ 0 in the baseline and appears in Lemma 1 and Props. 1–2, but p. 20: *"For simplicity, we abstract from the bidder's decision to build a toehold and assume m = 0"* — i.e. in the entire trading/entry extension the bidder has no toehold, and the activist's α is the only stake being chosen.

**Liquidity — present as machinery, absent as a subject.** There is a Kyle (1985) market maker and there are liquidity traders (pp. 4, 19–20), but liquidity is a two-point random variable (L or 0) whose only job is to conceal the activist's order. The word "liquidity" never appears in a result, a comparative static, an implication, or the conclusion. **There is no comparative static in L in the paper.**

**Disclosure rule — mentioned, never modelled.** Disclosure is a timing device, not a margin: p. 20, *"After trading, the activist's ownership in the target becomes public (e.g., by filing schedule 13D)"*, and p. 4, the bidder *"observes the arrival of the activist (e.g., by tracking 13D filings)"*. There is no 5% threshold in the model (the only threshold is 2L, and it is a wealth/poison-pill constraint, not a legal one), no filing window, no delay between crossing and revelation, and no Schedule 13G. The rule appears exactly once as a *conjecture about policy*, p. 5: *"Third, small regulatory changes, such as easing the access of shareholders to the ballot or modifying the rules that govern the filing of 13D schedules, can have an amplified effect on the aggregate volume of M&A."* — an unformalised claim, since the disclosure rule is not a parameter of the model. The formalised amplification result is about **κ**, the proxy-fight cost, not about disclosure — p. 24: "a small decrease in κ (e.g., a change in regulation that eases the proxy access) can have an amplified positive effect". *(Verifier: independent grep confirms **"13G" never appears**; "5%" appears only in the ValueAct anecdote and the Fos statistic, both p. 2; the strings "threshold", "business day", "filing window" and "disclosure" appear nowhere except the Rule 14a-9 net-exposure sentence on p. 19.)* **The string "13D" occurs four times, not once** (added by verifier): p. 4 (bidder tracks 13D filings), **p. 8** (Greenwood–Schor / Becht et al. on 13D announcement returns — see §4), p. 5 (the policy conjecture below), p. 20 (Q2).

**The 13D conjecture is one of five listed implications (p. 5), and the fourth is also a regulatory one** *(added by verifier)*: "Fourth, policies and regulations that exclusively undermine shareholder activism, such as the legalization of two-tier 'anti-activism' poison pills, might adversely affect M&A even if 'standard pills' that prevent takeovers are already prevalent." The fifth is that the complementarity also holds when the activist arrives *after* a deal is announced but before closing. So the 13D sentence is not a stray aside — it sits inside a deliberate policy block, which makes it a better, not a weaker, hook for our introduction.

**Empirical implications.** This version has **no section headed "empirical implications" or "testable predictions"** — the word "testable" does not appear. What is testable, in their words:
- p. 5: *"We provide necessary and sufficient conditions under which the treatment effect exists in equilibrium. We show that the model's comparative statics is sensitive to the existence of the treatment effect. This feature can be used to create identification strategies for empirical research."*
- p. 6: *"Based on this logic, the treatment effect can be identified by a positive relationship between the severity of agency problems in the cross section of target firms and the likelihood of a takeover."*
- p. 25, a warning about reading the existing evidence: *"This observation suggests that one should not conclude from the empirical evidence that targets are more likely to be acquired when they have activist as a shareholder (e.g., Greenwood and Schor (2009) and Boyson et al. (2016)) that activists are necessarily affecting the takeover process."*
- p. 31 / §5.3: activists should matter less where boards are weaker (UK today, US 1980s) — a cross-jurisdiction prediction.

## 7. Implications for our position

**What Corum–Levit occupies:** object = **takeover probability and takeover premium** (both, jointly determined); margin = **none of the disclosure rule** — their comparative statics are in b (entrenchment), **κ** (proxy cost), **λ** (board veto power) and ε (standalone proposal value); identification = **theory only**, no data, no estimation, one illustrative parameter vector.

This is the hardest constraint in the competitor set on the *object* dimension and simultaneously the clearest confirmation that the *margin* dimension is open.

**1. We cannot claim the control outcome as whitespace. We can claim the margin.** Corum–Levit already have a blockholder who trades against noise, buys a stake, and thereby changes the takeover premium and the probability of a bid. If our position is stated as "a blockholder's engagement affects control outcomes", it is scooped. If it is stated as "**the disclosure rule's partition** — which stake sizes are flagged, and how long the flag can wait — is what determines how liquidity maps into control outcomes", it is not: they have no threshold, no window, no delay, and no 13G. The position must lead with the partition, exactly as CONTEXT.md defines the paper's identity.

**2. Their disclosure sentence (p. 5) is our opening, not our obstacle.** They conjecture that "modifying the rules that govern the filing of 13D schedules, can have an amplified effect on the aggregate volume of M&A" and never formalise it, because the rule is not in their model. That is a named, citable, unformalised conjecture by a JFE-published competitor about precisely our object × margin. It is the single best sentence in the competitor set for our introduction: we formalise the conjecture and take it to the Feb-2024 acceleration.

**3. Their amplification logic is a gift and a warning.** The feedback between the solicitation effect and the activist's entry incentive means "small changes to the environment can have a large effect on the equilibrium" (p. 24). If a disclosure-rule change shifts the concealment available to the blockholder, our model should inherit that amplification — good for power in the empirical leg. The warning: amplification also means our comparative statics may be regime-dependent, so a claim like draft_v2's **disclosure attenuation (T2)** needs its regime stated (which of their selection / treatment regions it lives in), not asserted globally.

**4. Their liquidity is our κ, but degenerate — and that is our machinery whitespace.** Noise demand is L or 0, capped at 2L, and never varied. We can say truthfully that in the closest control-outcome competitor liquidity is a concealment device with no comparative static, whereas κ is our driving variable. But we must be careful: because their h(2L)/h(L) < 2 condition *is* a statement about how much price impact concealment can bear, a referee may read it as a liquidity result in disguise. Our core model should be able to nest or at least speak to their h(2L)/h(L) ≥ 2 no-entry region.

**5. Prop. 4 constrains our hump claim.** Draft_v2's R1 ("minority gains from control are non-monotone in liquidity", certified only on a grid) is a non-monotonicity claim in the same family as their Prop. 4 non-monotonicity in b. Theirs is a proposition with a proof; ours is a grid. Two consequences: (a) do not present the hump as the headline — CONTEXT.md already calls it disposable, and Prop. 4 is the reason; (b) if the hump survives, its honesty label must stay NUMERICAL, and it must be shown to be a *different* non-monotonicity (in liquidity, holding entrenchment fixed) or it will read as a re-derivation.

**6. Their identification proposal is the empirical design we are competing with.** "Positive relationship between the severity of agency problems in the cross section of target firms and the likelihood of a takeover" (p. 6) is a cross-sectional sign test that will not pass our own referee checklist (no control group, no bounded null, no design-based variation). A dated rule change with a control group is strictly better on the checklist. That is a deliverability argument for the Feb-2024 anchor, and it should be made explicitly rather than left implicit.

**7. *(added by verifier)* Their §4 is modular in the premium function — that is a bridge, not a wall.** fn. 24, p. 21 says the trading results hold for *any* increasing h(α), and points at Back et al. (2016) for an exogenous ownership→value mapping. So the honest framing is not "we compete with Corum–Levit on control outcomes" but "Corum–Levit take h(α) as a primitive; we derive which stake sizes are *observable* and therefore what h can be, from the disclosure partition." That is a stronger and more defensible relationship to a JFE competitor than a whitespace claim.

**8. *(added by verifier)* Watch the sign on the premium.** fn. 29, p. 27: when the activist has to intervene, the bidder pays sΔ; when the incumbent can be bought off directly he pays sΔ + (1−s)b — i.e. **activist involvement raises the takeover *probability* but can lower the *premium* conditional on a deal**. Any claim we make of the form "the disclosure rule raises takeover premia" must say which of these two margins it moves, or a referee holding this footnote will read our result as inconsistent with the closest theory paper.

**Vocabulary caution:** they use "treatment effect" and "selection effect" for the activist's real effect vs her stock-picking, which is the *same word pair* AFS use for the announcement-return decomposition, with a different referent. Any lit table that puts both papers in one row must disambiguate, or a referee will think one is a test of the other.

## 8. Quotes we may lean on (verbatim, page-cited)

*(fi/fl/ff/ffi ligatures restored from the PDF's broken encoding; dropped Greek symbols shown in square brackets — see the header caveat)*

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "Third, small regulatory changes, such as easing the access of shareholders to the ballot or modifying the rules that govern the filing of 13D schedules, can have an amplified effect on the aggregate volume of M&A." | p. 5 | **The disclosure margin as an unformalised conjecture** — our opening |
| Q2 | "After trading, the activist's ownership in the target becomes public (e.g., by filing schedule 13D)." | p. 20 | Disclosure is a timing device, not a modelled rule: no threshold, no window |
| Q3 | "We assume that initially the activist builds a position by trading with a market maker à la Kyle (1985)." | p. 4 | Their trading block — Kyle in name, two-point noise in substance |
| Q4 | "not trigger a poison pill if such exists, and the activist cannot buy more than 2L shares of the target, because of either wealth constraints or the concern of triggering a poison pill." | p. 20 | The only stake cap is a pill/wealth constraint, not a legal disclosure threshold |
| Q5 | "bidders and target blockholders, we abstract away from the free-rider problem in tender offers of Grossman and Hart (1980)." | p. 7 | Free-riding declared out of scope in the baseline |
| Q6 | "To focus the analysis on agency problems as the key friction, we abstract from information asymmetries about q or [Δ] and assume that they are both commonly known." | p. 8 | Asymmetric information out of scope in the baseline |
| Q7 | "(i) The bidder never runs a proxy fight." | p. 12 | Proposition 1(i), the paper's headline PROVED result |
| Q8 | "If the equilibrium exhibits only selection then θ* is strictly decreasing in b. If the equilibrium exhibits treatment then θ* is non-monotonic in b." | p. 26 | **Proposition 4, stated exactly** — *verifier restored the symbol as θ\* from the rendered page; the earlier "[Π]" was wrong* |
| Q14 | *(added by verifier)* "consistent with Greenwood and Schor (2009) and Becht et al. (2015), who show that the positive abnormal returns around 13D filings by activist investors stem mostly from events in which the target is eventually acquired, we assume that the activist cannot affect the standalone value of the target." | p. 8 | Their empirical warrant for making activism a pure control-outcome story |
| Q15 | *(added by verifier)* "the results in this section continue to hold even if h(α) stems from a different microfoundation, as long as h(α) is an increasing function." | p. 21, fn. 24 | Their §4 is modular in the premium function — our model can supply h(·) instead of competing with it |
| Q16 | *(added by verifier)* "Fourth, policies and regulations that exclusively undermine shareholder activism, such as the legalization of two-tier \"anti-activism\" poison pills, might adversely affect M&A even if \"standard pills\" that prevent takeovers are already prevalent." | p. 5 | The second regulatory conjecture in the same block as Q1 |
| Q9 | "Therefore, contrary to the common wisdom, the probability of a takeover and the likelihood of an activist campaign can increase with the resistance of the incumbents, as such resistance creates more investment opportunities for the activist." | p. 27 | The economics behind Prop. 4 |
| Q10 | "This feature can be used to create identification strategies for empirical research." | p. 5 | Their claim to empirical relevance |
| Q11 | "Based on this logic, the treatment effect can be identified by a positive relationship between the severity of agency problems in the cross section of target firms and the likelihood of a takeover." | p. 6 | Their proposed test — the design we improve on |
| Q12 | "For simplicity, we abstract from the bidder's decision to build a toehold and assume m = 0." | p. 20 | Toehold switched off exactly where trading enters |
| Q13 | "there is substitution between the bidder's ability to bypass the target board through tender offers and the activist's ability or need to unseat it through proxy fights." | p. 31 | Cross-jurisdiction prediction (§5.3, unproved in this file) |

## 9. Verification log

**Verifier:** adversarial second reader (Opus), 2026-08-19. **Method:** independent re-extraction of `lit/corum-levit-2019.pdf` with `pdftotext -layout` (46 form-feeds → 45 printed pages + trailer; printed folio = PDF page throughout, confirmed on pp. 9, 12, 26, 31, 45). Because the font encoding drops every Greek letter, **pp. 9, 12, 19, 20, 21, 22, 23, 24, 26, 30, 31, 44, 45 were re-read as 150-dpi rendered images** and the symbols read off the page. Quote matching used a ligature-aware normaliser (… → fi, ‡ → fl, ¤ → ff, ¢ → ffi) over the page-marked extract. `research/txt/corum_levit_jfe2019.txt` was NOT used. **Counts: OK 24 · WRONG 8 · MISCITED 2 · UNCHECKED 1.**

### Version / venue (§ header) — OK

Confirmed from PDF p. 1: title "Corporate Control Activism", "Adrian A. Corum / Wharton", "Doron Levit / Wharton", "August 11, 2016". No JFE masthead, no volume/issue, no DOI, no Received/Accepted block. Acknowledgements list 2015–2016 conferences (IDC Herzliya 7th Summer Finance Conference, 2016 FIRS, 2016 WFA). p. 28 confirms "The formal results and their proofs are given in the Online Appendix", and no Appendix B or C is in the file. **This is the August 2016 working paper, not the published article.**

*One correction to the card's own verifier note:* the file does **not** end mid-proof. p. 45 completes the proof of Proposition 4 — "∂θ*/∂b > 0 ⟺ b > (1 − F(b))/f(b), as required. ∎". Appendix A (pp. 36–45) is complete; only Appendices B and C are missing.

### Quotes (§8)

| Q | Verdict | Checked against |
|---|---|---|
| Q1 | OK | p. 5 — verbatim |
| Q2 | OK | p. 20 — verbatim (also read on the rendered page) |
| Q3 | OK | p. 4 — verbatim; the source has "à la Kyle (1985)" with a grave accent |
| Q4 | OK | p. 20 — verbatim on the rendered page |
| Q5 | OK | p. 7 — verbatim (the full sentence begins "Moreover, different from Burkart et al. (2000)…" on p. 6) |
| Q6 | OK | p. 8 — verbatim; the bracketed symbol is Δ, correct |
| Q7 | OK | p. 12 — verbatim |
| Q8 | **WRONG (symbol), corrected** | p. 26 — the wording is exact, but the symbol is **θ\*, not Π**. Fixed in §8, R8 and §6 |
| Q9 | OK | p. 27 — verbatim |
| Q10 | OK | p. 5 — verbatim |
| Q11 | OK | p. 6 — verbatim |
| Q12 | OK | p. 20 — verbatim on the rendered page |
| Q13 | OK | p. 31 — verbatim |
| Q14–Q16 | OK | pp. 8, 21, 5 — added by verifier from the source |

### Results (§3)

| # | Verdict | Executed check |
|---|---|---|
| R1 | OK | Lemma 1 statement, p. 11 |
| R2 | **MISCITED (symbol)** | Prop. 1(i), p. 12 verbatim. The parameter list should read "Δ, **κ**, m, b" — the paper's proxy cost is κ (p. 9), never γ. Fixed |
| R3 | **WRONG** | Eq. (2), p. 12, read off the rendered page: **(κ/s)/α ≤ Δ/(1−m) < b**. Two errors: γ→κ, and the first inequality is **weak**. Fixed |
| R4 | **WRONG (symbol)** | Prop. 2, p. 13 — γ→κ. Fixed |
| R5 | **WRONG** | Cor. 1, pp. 20–21, rendered: the bidder's profit is **ζ**(w(α) − v(α)), conditional on the state ζ — not μ(w−v). Also the increase condition is (κ/s)/α < b, and h(α) ≡ G(w−v)·v (Eq. 7) is a *third* object the card had merged with v. Fixed |
| R6 | **WRONG** | Prop. 3, p. 22, rendered: the mixing probability is **σ\* ∈ [0,1)**, not θ. The interior case additionally needs 1 + ½(μ̂−μ)/μ̂ < h(2L)/h(L) (p. 23), which the card omitted. Fixed |
| R7 | OK on substance, symbol fixed | Cor. 2, p. 24, rendered: Eqs. (12)–(14) with κ/s. The "both" and "selection only" branches also carry the h(2L)/h(L) condition. Fixed |
| R8 | **WRONG on the symbol; the honesty caveat is CONFIRMED** | Prop. 4, p. 26 uses **θ\***. The proof, p. 44: "Next, suppose the equilibrium exhibits treatment. **For example, suppose σ\* = 0 and (κ/s)/L < b.**" — the card said "suppose μ = 0 and γ/(sL) < b", wrong on both. **The treatment branch is indeed established only inside that worked case**, and p. 45 ends at ∂θ*/∂b > 0 ⟺ b > (1−F(b))/f(b). The PROVED-with-caveat label stands, and a third caveat was added: fn. 28, p. 26 makes it a *local* comparative static of the α\*(1) > 0 equilibrium |
| R9 | OK | pp. 5, 21, 24 — "activists can affect corporate control outcomes even if ex-post their threat of running a proxy fight is not credible" (p. 5); solicitation effect named on p. 24 |
| R10 | **MISCITED** | The statement is right (p. 23) but it is **Prop. 3(ii)**'s "if and only if h(2L)/h(L) < 2", not Prop. 3(i). Prop. 3(i) is the α\*(1)=0 existence condition, Eq. (9). Fixed |
| R11–R12 | OK | §5.1 p. 28–29, §5.2 pp. 29–30; ASSERTED label confirmed by p. 28: "The formal results and their proofs are given in the Online Appendix" |
| R13 | **WRONG** | §5.3, pp. 30–31, rendered: veto probability is **λ ∈ [0,1]** (baseline λ = 1), and **φ ∈ [0,1]** is a *different* parameter — the post-takeover value of minority shares is q + φΔ. The condition is **(κ/s)/(αλ) ≤ Δ < b**. The card had conflated λ and φ and used γ. Fixed |
| R14 | OK | §3.2, pp. 13–16, discursive; B.1–B.3 in the absent Online Appendix |
| R15–R17 | OK (added by verifier) | §4.2.1 p. 28; fn. 29 p. 27; fn. 24 p. 21 |

**Π is not the takeover probability.** Eq. (8), p. 21 defines **Π(α) = α(q + μ̂h(α) − [p(α) + p(α+L)]/2)** — the *activist's expected trading profit*. It is used with that meaning again throughout the Prop. 3 proof (p. 44). The takeover probability is θ\* (Eq. 15, p. 25). The card had Π standing for the takeover probability in R8, §6 and Q8; all three corrected.

### Scope claims (§6) — all independently grepped, all CONFIRMED

| Claim | Verdict | Check |
|---|---|---|
| No comparative static in L anywhere | **OK** | Every hit of `liquid` inspected: p. 20 (two-point noise setup), p. 22 (concealment), p. 23 ("the liquidity demand is either L or zero"), p. 25 ("the liquidity demand is smaller than L"), reference titles (Back et al. 2016; Maug 1998), appendix probability bookkeeping pp. 42–43. **No result, no comparative static, nothing in the conclusion (§6, p. 31 — read in full).** L is fixed at 0.1 in both figures |
| "13G" never appears | **OK** | Zero hits |
| No "testable", no "empirical implications" section | **OK** | Zero hits for `testable`, `empirical implication`, `predictions` |
| No 5% threshold in the model | **OK** | `5%` occurs twice, both p. 2 (ValueAct's stake; Fos's 5%-of-proxy-fights statistic). `threshold`, `business day`, `filing window` — zero hits. `disclos` — one hit, the Rule 14a-9 net-exposure sentence, p. 19 |
| Free-riding out of scope in the baseline | **OK** | pp. 6–7 verbatim; re-enters §3.2.6 (p. 16) and §5.3 (p. 30) |
| Toehold m = 0 in the extension | **OK** | p. 20 verbatim |
| The 13D policy conjecture is unformalised | **OK** | p. 5; nothing downstream turns it into a parameter |
| "13D" appears once | **WRONG as stated** | It appears **four** times: pp. 4, 5, 8, 20. The p. 8 occurrence is substantive and was missing — added to §4 and §8 (Q14). The *policy conjecture* does appear only once, and that narrower claim stands |

### Institutional facts (§4) — all OK

Fos (2016) 632 proxy fights 2003–2012, 5% corporations / 70% activist hedge funds (fn. 3, p. 2) · KKR–Gardner Denver $3.7bn 2013 after ValueAct's 5% stake, Roberts quote via WSJ 1/5/2013 (fn. 4, p. 2) · Delaware merger-vote / tender-offer / pill note (fn. 2, p. 2) · Sotheby's–Third Point two-tier pill 2014, aimed at a **10%** ceiling (fn. 6, p. 5) · classified boards 11% in 2013 vs 57% in 2003 (fn. 11, p. 9) · non-redeemable pills illegal in most states incl. NY and Delaware (p. 10) · Rubinstein (1982) microfoundation (fn. 10, p. 8) — note the paper calls it the **Nash bargaining protocol** · Rule 14a-9 net-exposure disclosure (p. 19) · Collin-Dufresne et al. (2016) on derivatives / empty voting (p. 19) · Boyson et al. 70% within 2 years, 30% post-announcement (p. 28), activist is the bidder in 15% (fn. 17, p. 16) · Valeant–Allergan–Pershing Square (p. 18) · n + α + m < 0.5 (p. 7) · diversion "arbitrarily small", relaxed in Appendix C.4 (p. 10).

### Omissions added

- **p. 8** — the assumption that the activist cannot affect standalone value is justified by Greenwood–Schor (2009) and Becht et al. (2015): 13D abnormal returns "stem mostly from events in which the target is eventually acquired". This is the paper's empirical bridge from announcement returns to control outcomes and the card had no trace of it. → §4, Q14.
- **fn. 29, p. 27** — activist involvement raises deal probability but the bidder then pays sΔ rather than sΔ + (1−s)b, i.e. **a lower premium**. → R16, §7 pt 8.
- **fn. 24, p. 21** — the §4 results hold for any increasing h(α), citing Back et al. (2016). Their trading block is modular in the premium function. → R17, §7 pt 7.
- **fn. 27, p. 25 and fn. 28, p. 26** — two equilibrium-selection assumptions carry Eq. (15) and Prop. 4, and both live only in footnotes. → §5.
- **§4.2.1, p. 28** — "Arbitrage activism — activist moves last", a main-text extension asserted without proof in this file. → R15.
- **p. 5, implications four and five** — the anti-activism-pill conjecture and the post-announcement-arrival case; the 13D sentence is the third of five, inside a deliberate policy block. → §6, Q16.
- **p. 9** — κ "decreases with the fraction of the firm that is held by institutional investors or the governance expertise of the challenger". → §2.
- **p. 23** — the economics of the h(2L)/h(L) ≥ 2 no-entry region, in their own words. → R10.
- **Notation collision** — their κ is the proxy-fight cost; our κ is noise-trading intensity. → header.

### UNCHECKED

**R11–R14's substance.** The formal statements for §§5.1–5.3 and the six commitment-problem "solutions" (B.1–B.3) are in an Online Appendix that is not in this WP file, so the ASSERTED labels are correct for this file but the *content* of those results cannot be verified from it.

**RESOLVED, mid-verification, and it went badly.** The published article (`research/txt_extracts/corum_levit_2019_jfe_published.txt`, fetched by another agent during this run) was checked. It does not merely fill the gap — **it supersedes the formulation this card describes.** The published §4 replaces the Kyle noise-trader block with an explicit disclosure threshold ᾱ, calls it "a disclosure threshold (e.g., regulation 13D)", calibrates it to 5–10%, and demotes the Kyle version to footnote 23. It also carries seven numbered Predictions and prints Appendices A–C in the article. **This falsifies the card's "no 5% threshold" scope claim and weakens §7 pt 1 and pt 4.** See the ⚠ block at the top of this card. The correct next step is a fresh read of the published article, not a patch of this one — flagged to the orchestrator.

### Overall verdict

**The card's strategic conclusions all survive; its formal apparatus did not.** The four decision-critical negative claims — no comparative static in L, no 13G, no "testable"/"empirical implications" section, no 5% threshold or filing window in the model — are independently confirmed, as is the exact wording of Proposition 4 and the honesty caveat that its treatment branch rests on a worked case. But **eight of the card's symbol/statement transcriptions were wrong**, because the first reader reconstructed the PDF's dropped Greek letters by guesswork rather than by rendering the pages. Every one is now corrected against the rendered PDF and a symbol dictionary added to the header. The one genuinely open item is the missing Online Appendix.
