# Full Read: Celentano & Levine (2025) — "Shareholder Activism, Takeovers, and Managerial Discipline"

**Read date:** 2026-06-11. **Reader coverage:** all 62 PDF pages (title page; manuscript pp. 1–34; Fig. 1 p. 35; Figs. 2–5 pp. 36–39; Tables 1–10 pp. 40–49; References pp. 50–54; Internet Appendix pp. 1–7 = PDF pp. 56–62). Page citations below use the **printed manuscript page numbers** (PDF page = printed page + 1 for the main text; "IA p. N" for the Internet Appendix).

---

## 1. Metadata

| Field | Value |
|---|---|
| Title | Shareholder Activism, Takeovers, and Managerial Discipline |
| Authors | Francesco Celentano (U. Lausanne & Swiss Finance Institute); Oliver Levine (U. Wisconsin–Madison) |
| Version date (in PDF) | **October 1, 2025** (title page). The SSRN listing's "rev. 17 Nov 2025" is not visible inside the document. |
| Status claims (R&R at RFS; FMA 2025 CF semifinalist) | **Not verifiable from the PDF** — nothing in the document states journal status. Keep sourced to the deep-research journal, not to the paper. |
| JEL / Keywords | G34, G32, G39, G23, G14; activism, M&A, governance, agency conflicts (title page) |
| Acknowledgments of note | Discussants Muthyala, Sacchetto; thanks Gantchev, Malenko, Mello, Morellec, Schroth, Schürhoff, Wang; **Alon Brav provided the hedge-fund campaign data** (title page) |
| Length/structure | Intro (pp. 1–7), Model (pp. 8–14), Data (pp. 14–16), Identification (pp. 16–19), Estimation results (pp. 19–21), Implications/counterfactuals (pp. 21–30), Hedge funds/time/severance (pp. 30–33), Conclusion (pp. 33–34), IA: estimation details + elasticities only |

---

## 2. Model Summary

**Players (4):** firm's **manager** (effort choice), **board** (CEO turnover; takeover negotiation), a potential **activist investor** (entry), a potential **acquirer** (Nash bargaining). Shareholders are passive valuation-takers. Discrete time, infinite horizon, risk-neutral agents, common discount factor β (p. 8).

**Timing within a period** (Fig. 1, p. 35; narrative p. 8): (1) firm produces π_t = z_t k_t^α − c_k k_t, pays dividend; (2) activist privately observes two signals s_p,t, s_w,t about the period's i.i.d. **project quality** p_t ~ Exp(λ_p) and **acquirer quality** w_t ~ Exp(λ_w) (signals = truth + normal noise, eq. 3, p. 9) and chooses entry ν_t ∈ {0, ν̄}, ν̄ = 5% (the 13D threshold, p. 16); (3) **entry and the private signals immediately become common knowledge and the share price updates** (p. 10); (4) manager observes true p_t, chooses effort e_t ∈ {0,1} at private cost c_e·π_t (eq. 5, p. 10); (5) board chooses turnover f_t at private cost c_f(ν_t)·π_t (eq. 6, p. 11); (6) z_{t+1} realized; w_t revealed to acquirer and board; takeover price set by **Nash bargaining** (acquirer power θ_a = 0.5): P_t = (1−θ_a)V(w_t) + θ_a·V(z_{t+1})/(1−c_m(ν_t)) (eq. 9, p. 13); deal occurs iff both surpluses positive; (7) activist sells, campaign ends (campaigns last one period); takeover ⇒ firm exits with productivity replaced by w_t (q-theory technology transfer, Jovanovic–Rousseau, p. 12).

**State variables:** public state = productivity z_t (log-AR(1) with effort shifter e_t·p_t, eq. 2, p. 9); within-period shocks (p_t, w_t); activist's private signals (s_p,t, s_w,t); activist presence ν_t. Value functions V(z) (shareholders, eq. 10, p. 13) and M(z) (manager). Type I extreme-value preference shocks on manager and board choices (p. 16); economically negligible (~10⁻⁵ %) EV shocks on entry/takeover purely for computation (IA p. 1).

**Activist entry problem (eq. 4, p. 10):** max over ν_t ∈ {0, ν̄} of βE[V(z_{t+1}) | signals]·ν_t − (1+ξ)(V(z_t) − π_t)·ν_t. The stake is bought at the **public-information ex-dividend price** with proportional cost ξ; "the term ξV(z_t)ν_t reflects the costs arising from **limited liquidity and information leakages** associated with large share purchases as well as expected campaign costs" (p. 10). That sentence is the entire liquidity content of the model.

**Activist's two technologies:** (i) lowers board's turnover cost c_f(ν̄) < c_f(0) → credible replacement threat → manager effort (pp. 11, 20); (ii) lowers board's takeover entrenchment cost c_m(ν̄) < c_m(0) → facilitates deals but also **lowers the price the board demands** (pp. 12–13, 22).

**Equilibrium concept:** recursive dynamic-discrete-choice equilibrium with rational-expectations pricing; estimated by SMM (Lee–Ingram), K=20 simulations, influence-function weight matrix (Erickson–Whited), global genetic algorithm (IA pp. 1–2).

**Headline quantitative results:**
- Campaign raises takeover probability **+7.7%** (12.46 vs 11.57); ~7% of in-campaign deals are marginal to the activist (p. 2, p. 22, Table 4 p. 43).
- **Bid premium 13.7% (5.2 pp) lower** with an activist present in negotiations (32.90 vs 38.12 counterfactual; p. 2, p. 22, Table 4 p. 43).
- Net M&A-channel value per campaign ≈ **6 bp**; conditional on takeover +0.44% (split +1.23% probability gain, −0.78% premium loss); marginal deals gain 15.4–15.7%, the 92.8% non-marginal deals **lose 0.75%** (pp. 2, 22–23).
- Effort channel: +30.8% project take-up, **+1.17% productivity, +0.35% shareholder value** per campaign (pp. 2, 23, Table 4).
- Equilibrium: effort-incentive channel **crowds out 0.79% of M&A volume**; facilitation adds +0.64%; **net effect on takeover volume ≈ 0** (−0.05%) (pp. 3, 24–25, Table 5 p. 44). Total (target+acquirer) M&A surplus −0.16% (p. 25).
- Threat effect: equity value **+0.33%** economy-wide vs no-activist counterfactual, entirely from effort incentives; campaigns occur in only ~4% of firm-years (pp. 4, 25, Table 5).
- Externalities: crowd-out destroys 0.37% of acquirer surplus; facilitation more than offsets → acquirer surplus **+0.22%** net (p. 4).
- Selection vs treatment: **91% of the 4.07% entry announcement return is selection** (information), 76.3 pp of it from the takeover signal; treatment only 9.3% (Table 7 p. 46; pp. 5, 27). Explicitly contrasted with AFS 2022's majority-treatment finding (p. 7).
- No private information ⇒ **activist never enters** (entry −100%, Table 8 col. 3 p. 47; p. 29) — information advantage is what overcomes the entry-stage free-rider problem.
- Policy experiment: ±20% in ξ; higher cost → entry −41%, value −0.15%, takeover-freq-given-activist +11% (selection strengthens) (p. 30, Table 9 p. 48).
- Key estimates (Table 3 p. 42): c_f(0)=2.072 → c_f(ν̄)=1.618 (−22%, p. 20); c_m(0)=0.151 → c_m(ν̄)=0.135 (−11%, i.e., 1.6 pp of firm value, p. 20); **ξ = 0.030** (3.0% of pre-campaign price of the shares acquired, p. 20); signal-to-noise 3.2% (acquirer), 14.6% (project) (p. 19).
- Hedge funds (2001–14, 87% of campaigns): modestly stronger on both technologies and acquirer information (pp. 31, Table 10 p. 49). Late sample (2010–19): takeover-friction reduction appears (15.6%) and signal-to-noise rises (3.2→5.4% takeover; →13.1% project) (p. 32).

---

## 3. Data & Identification

- **Sample:** U.S. public firms **2001–2019**, 52,666 firm-year obs (Table 1 p. 40). CRSP/Compustat merged; drops non-US, utilities, financials, quasi-government (p. 14).
- **M&A:** SDC Platinum via Michael Ewens' SDC–Compustat mapping; 2,194 bids = 4.2% of firm-years (pp. 14–15).
- **Activism:** Audit Analytics **initial Schedule 13D filings** (amendments excluded, following AFS 2022); first filing per target per 12 months (wolf-pack rationale); 2,083 campaigns = 4.0% of firm-years (p. 15). Hedge-fund classification from Brav's data (p. 15).
- **CEO turnover/compensation:** Equilar; 8.5%/yr turnover (p. 15).
- **Event-ordering conventions:** campaigns <1 yr after a bid dropped (risk arb); turnover <1 yr after a bid dropped; turnover/bids within 2 yrs of a 13D attributed to activism (Boyson et al.) (p. 15).
- **Bid premium definition:** bid price / CRSP price 25 days pre-announcement (price 1 day after any intervening campaign/turnover event); premia restricted to (0,1); **mean 36.6%, mean with activist 33.2%** (p. 16, Table 1). Model analog: P_t over the pre-announcement price, which "incorporates information on z_{t+1}, ν_t, and s_{w,t}" (fn. 9 p. 18).
- **Activist entry CAR:** market-adjusted, −30d to +1d around 13D filing; mean 4.4% (p. 16).
- **Estimation:** SMM, **12 estimated parameters, 15 targeted moments** (Table 2 p. 41): asymmetric persistence of good/bad performance (identifies c_e, à la Wang–Wu 2020, eq. 11 p. 17), residual variance, entry frequency, mean entry CAR (**identifies ξ**, p. 18), 3-yr-performance-on-activism coefficient (λ_p), takeover frequency (λ_w), takeover|activist frequency, **mean bid premium → c_m(0); bid premium|activist → c_m(ν̄)** (p. 18), turnover and turnover|activist frequencies (c_f(0), c_f(ν̄)), three lagged-performance correlations. Preset: α=0.7, β=0.952, c_k=0.20, θ_a=0.5, θ_d=1.6%, **ν̄=5% = statutory 13D threshold** (p. 16). Elasticity diagnostics per Andrews–Gentzkow–Shapiro (IA p. 2, Figs. B.1–B.5).

---

## 4. Cell-by-Cell Validation

### 4.1 Section 1 scope table ("Their paper" column)

| Cell | Pre-read claim | Verdict | Evidence |
|---|---|---|---|
| Status | SFI RP 25-81, Oct 2025; R&R RFS; FMA semifinalist | **NUANCED** | Internal date Oct 1, 2025 (title p.). R&R/FMA status nowhere in the document — keep that claim sourced externally, not to the PDF. |
| Type | Structural estimation of equilibrium model: activism + M&A + managerial discipline | **CONFIRMED** | SMM on dynamic model with activist entry, Nash-bargained takeovers, CEO turnover/effort (abstract; pp. 8–13, 16–19; IA p. 1). |
| Core question | Quantify activism's role in the market for corporate control | **CONFIRMED** | "We quantitatively assess the role of activism in the market for corporate control" (abstract; pp. 1–2). |
| Mechanism: complements + crowds out; **CEO incentive effects ◑** | ◑ inferred | **CONFIRMED & STRENGTHENED** | CEO incentives are not a side channel but the **dominant** one: activist cuts board turnover cost 22% (p. 20), effort +30.8%, productivity +1.17%, value +0.35%/campaign (p. 23) vs ~6 bp from M&A facilitation (p. 23); the effort channel is precisely what crowds out M&A (−0.79%, p. 24); threat effect +0.33% economy-wide "comes entirely from improved effort incentives" (p. 4). |
| Trading/liquidity/price impact: **Absent** | claimed absent | **CONFIRMED** | No order flow, no noise traders, no price-impact function, no inference problem anywhere incl. IA. Liquidity = one sentence motivating scalar ξ (p. 10). Nuance: a one-shot "trade on private information" exists (stake bought at uninformed price, full revelation at entry, p. 10) and drives the 91% selection result (Table 7 p. 46) — but with zero microstructure. |
| Disclosure rule: **not a design object ◑** | ◑ inferred | **CONFIRMED** | 13D threshold appears only as calibration of stake size ν̄=5% (p. 16) and as the empirical entry event (p. 15). Revelation at entry is automatic and total (p. 10). Policy experiment varies the **cost** ξ, with "trade block disclosure requirements (Bebchuk et al., 2013; Back et al., 2018)" cited merely as motivation (p. 30). No threshold/timing counterfactual, no planner. |
| Free-rider: **info advantage overcomes free-rider problem in intervention ◑** | ◑ inferred | **CONFIRMED, with sharp nuance** | It is the **Grossman–Hart entry-stage** free-rider problem (campaign costs private, benefits shared, p. 29), overcome by trading gains from buying 5% before revelation: with no information, "the activist never finds it optimal to enter" (p. 29; Table 8 col. 3 p. 47). **Not** a tender-offer dilution mechanism — no appropriability object, nothing like our λ. |
| Estimation target ◑ | "equilibrium model on activism+M&A data" | **CONFIRMED & SPECIFIED** | SMM, 15 moments / 12 parameters, 2001–2019; CRSP/Compustat + SDC + Audit Analytics 13D + Equilar + Brav HF data (pp. 14–19, Tables 1–3). |
| Differentiation one-liner | "discipline role with no market microstructure" | **CONFIRMED** | No liquidity state variable; all regulatory/market variation collapses into scalar ξ (pp. 10, 30); no object indexes where activism pays except z_t and signal draws. |

### 4.2 Overlap matrix, C–L column

| Object | Pre-read | Verdict | Evidence |
|---|---|---|---|
| Structural estimation ✓ | ✓ | **CONFIRMED** | pp. 16–19, IA p. 1. (R&R status not in doc.) |
| Takeovers/M&A in model ✓ | ✓ | **CONFIRMED** | Takeover phase §1.5, Nash bargaining eq. 9 (pp. 12–13). |
| Trading/liquidity/price impact ✗ | ✗ | **CONFIRMED** | Only reduced-form ξ (p. 10). |
| Disclosure rule as object ✗ ◑ | ✗ ◑ | **CONFIRMED ✗** | 5% threshold = calibration only (p. 16); cost experiment ≠ disclosure design (p. 30). |
| Premium wedge microfounded ✗ ◑ | ✗ ◑ | **CONFIRMED ✗, important nuance** | No tender game, no dilution, no λ. **But** the premium is endogenous: Nash bargaining + board entrenchment c_m(ν) (eq. 9 p. 13), estimated off mean premia (p. 18), delivering their headline −13.7% activist effect (p. 22). They occupy "endogenous premium responding to activism," not "microfounded wedge from tender mechanics." |
| Engagement-cost distribution ? ◑ | unknown | **RESOLVED: NO distribution** | Single scalar ξ = 0.030 (Table 3 p. 42; 3.0% of pre-campaign price, p. 20); within-campaign stage costs explicitly out of scope (fn. 5 p. 10, deferring to Gantchev 2013 and J–S 2021). EV shocks are computational only (IA p. 1). **White space intact.** |
| Reputation dynamics ✗ | ✗ | **CONFIRMED** | No reputation; campaigns last one period (p. 8); time-variation handled by sample splits (p. 31–32). |
| 2024 acceleration anchor ? | unknown | **RESOLVED: ABSENT** | No mention of the 2024 13D deadline acceleration, the 10-day/5-business-day window, or filing-delay timing anywhere; sample ends 2019 (p. 14). |

**Tally: 14 CONFIRMED, 2 RESOLVED (both ?-cells), 1 NUANCED (Status). 0 cells refuted.** All six ◑ flags are now validated.

### 4.3 Cross-table correction discovered (affects the AFS section, not the C–L section)

The Section 3 (AFS) row "Activism **LOWERS** takeover bid premia 13.7% (5.2pp) vs no-activist counterfactual (verified)" reproduces **exactly** C–L's numbers: "the bid premium is 13.7 percent (5.2 percentage points) lower than if the activist had not been present" (C–L p. 22, Table 4 p. 43). Identical figures appearing as a "verified" AFS claim strongly indicate the deep-research journal **misattributed C–L's Table 4 result to AFS**. Action: during the AFS full read, pull AFS's actual premium finding (if any) and its construction; do not cite −13.7%/5.2pp to AFS anywhere. Prop d7:afs's mapping must be re-anchored to whatever AFS actually reports — and must now engage C–L's −13.7% as the competing structural estimate of the same sign.

---

## 5. Checklist Answers (one per question)

1. **Exact state space:** public firm state z_t (log-AR(1) + effort shifter, eq. 2 p. 9); i.i.d. per-period shocks p_t ~ Exp(λ_p), w_t ~ Exp(λ_w); activist private signals s_x = x + σ_x η; binary stake ν_t ∈ {0, 0.05}; choices e_t, f_t, a_t ∈ {0,1}; EV preference shocks. Value functions V(z), M(z); one-period campaigns; infinite horizon (pp. 8–13).
2. **Any trading/inference/microstructure?** **No — searched all 62 pages incl. IA.** One-shot stake purchase at the public-information price with proportional cost ξ (p. 10); entry triggers full, immediate revelation of the activist's signals (pp. 10, 27). No noise trading, no order-flow inference, no price impact, no partial pooling, no robustness extension with any of these. The IA contains only SMM mechanics and elasticities.
3. **How premia are determined:** **bilateral Nash bargaining** (θ_a = 0.5 imposed) between board and acquirer; P_t = (1−θ_a)V(w_t) + θ_a V(z_{t+1})/(1−c_m(ν_t)) (eq. 9 p. 13). Entrenchment c_m(ν) inflates the board's demanded price ("the bid premium reflects the private costs of the board, as the acquirer must offer a higher bid to offset those costs," p. 18); the activist lowers c_m, hence lowers the premium. No auction, no tender offer, not exogenous.
4. **Identification + dataset:** SMM (Lee–Ingram 1991; Nikolov–Whited/Bazdresch panel approach; Erickson–Whited influence-function weight matrix; K=20; genetic algorithm — IA pp. 1–2). 2001–2019; CRSP/Compustat (52,666 obs), SDC Platinum (2,194 bids), Audit Analytics 13D (2,083 campaigns), Equilar, Brav HF data. 15 moments listed in §3 above; premium moments pin c_m(0), c_m(ν̄); entry CAR pins ξ (p. 18).
5. **2024 13D acceleration mentioned?** **No.** Nowhere in text, footnotes, policy section, or references; sample ends 2019.
6. **Back/Collin-Dufresne/Fos-type citations; liquidity engagement?** **Back, Collin-Dufresne, Fox, Li, Ljunqvist (2018, Econometrica) — cited twice**: theory footnote 1 (p. 6) and as a "trade block disclosure requirements" reference motivating the cost experiment (p. 30). **Collin-Dufresne & Fos (2015/2016) standalone — not cited.** Mello–Repullo 2004 (activism non-monotonic in liquidity) — cited fn. 1 p. 6. Norli–Ostergaard–Schindele 2015 (liquidity and activism, RFS) — cited fn. 2 p. 6 (ref. p. 54). Substantive engagement with liquidity: **none beyond the single ξ-motivation sentence (p. 10)** — no liquidity proxy, moment, parameter, or comparative static.
7. **Maug / Kahn–Winton / Edmans / AFS / J–S?** Maug 1998 — **yes** (fn. 1 p. 6). Kahn–Winton 1998 — **yes** (fn. 1). Edmans — **only** the Edmans–Holderness 2017 survey (fn. 1); no Edmans 2009, no Edmans–Fang–Zur 2013. **AFS 2022 — engaged substantively**: data conventions follow it (p. 15), cost estimate compared (p. 20), and its treatment-majority finding explicitly contradicted, with reconciliation discussion (selection 91% here vs treatment ~75% there; pp. 5, 7). **Johnson–Swem 2021 — cited repeatedly**: proxy-fight facilitation motivation (p. 1), structural lineage (p. 7), within-campaign costs deferral (fn. 5 p. 10), cost-estimate comparison (p. 20), time-variation motivation (p. 31). No σ²T/13D-window discussion anywhere.

---

## 6. Engagement Points (our 3 conjectures, confirmed/sharpened)

**(i) Their crowding-out vs our deterrence channel ∂p/∂π<0 — CONFIRMED, and sharper than conjectured.** Their crowd-out is a *real-options/surplus* effect: activist threat → effort → higher standalone V(z) → smaller takeover surplus → marginal deals die (−0.79% of M&A volume, Table 5 col. 2, p. 24; net ≈ 0 after facilitation, p. 25). There is **no informational deterrence at all**: the acquirer arrives exogenously each period and observes w_t perfectly (p. 12); bidder entry is not a decision. Our ∂p/∂π<0 channel (bidder behavior responds to the disclosure-induced posterior) is a margin their machinery cannot represent, yet it bears directly on their headline "zero net volume effect" — if disclosure-sensitive bidder entry is active, their net-zero decomposition is mis-specified. Quantities of theirs we can speak to: −0.79% crowd-out, +0.64% facilitation, −0.05% net, and the 12%→14% takeover-probability-given-activist range (p. 25).

**(ii) No κ / disclosure-rule comparative statics — CONFIRMED exactly, and upgraded.** Their only policy lever is the scalar cost ξ (±20%, Table 9 p. 48); they themselves describe disclosure regulation as something that changes "the cost of activism" (p. 30). So: (a) our headline objects (κ comparative statics; threshold k_D as design margin; counterfactual disclosure regimes) are untouched; (b) better, their framework forces all regulation to act **monotonically through a cost**, whereas our model predicts **non-monotone** responses (κ† hump) and distinguishes the *information content* of disclosure from its *cost* — a falsifiable difference we should state explicitly against their Table 9.

**(iii) D7 primitives (q, γ) give cross-sections their model doesn't index — CONFIRMED.** Their premium wedge is governed by two estimated constants c_m(0)=0.151, c_m(ν̄)=0.135 (Table 3 p. 42) and fixed θ_a=0.5; nothing indexes acquirer type (strategic vs financial), pivotality, or fringe competition. Our (q, γ, ψ)-indexed sign-and-size predictions for the activist-premium relation are therefore strictly outside their model — and give the natural cross-sectional test separating our appropriability mechanism from their board-bargaining mechanism for the *same* −13.7%-type fact.

**(Bonus 4th point — recommend adopting.)** Their selection/treatment split (91/9, Table 7 p. 46) versus AFS's (≈25/75) is an open dispute they flag themselves (p. 7). In C–L the split is mechanical because **revelation at entry is total and immediate** (p. 10). In our model, how much private information is capitalized at the 13D event is an equilibrium object of the trading environment — the posterior π(X, D) and κ govern partial capitalization. We can position our framework as endogenizing the very quantity the two structural papers disagree about: the announced-return split depends on the information environment (κ, disclosure regime), not only on signal precision. This is a high-value engagement because it speaks to both competitors at once.

---

## 7. Threats

**Overall: MEDIUM.**

1. **Biggest threat — competing explanation for the negative activism-premium fact.** C–L deliver a structural, estimated, R&R-track result that "an activist campaign decreases the bid price and takeover premium" by 13.7% (p. 22), via board bargaining position. Our D7 (measured premium falls when λ < λ_crit, capitalization in the denominator) now has a named rival mechanism for the same sign. We must (a) stop attributing −13.7%/5.2pp to AFS (see §4.3), (b) cite C–L for it, and (c) differentiate on testability: their wedge moves only with activist presence ν; ours moves with q, γ, ψ, κ — different cross-sections, and theirs implies a real wealth transfer in 92.8% of deals (−0.75%, p. 23) while ours is partly capitalization. Not an overlap with the *microfoundation* claim itself: they have no tender game, no dilution, no λ.
2. **Disclosure-policy adjacency, minor.** A referee could say "C–L already run a regulation experiment" (Table 9, motivated by block-disclosure rules, p. 30). Preempt: a cost shift cannot capture the information content of disclosure; in C–L, disclosure *is* full revelation by assumption (p. 10), so the design margin we study is degenerate in their model. No overlap with "disclosure rule as design object."
3. **Liquidity-as-engine: no overlap.** The word liquidity appears once, motivating ξ (p. 10). They cite Back et al. 2018, Mello–Repullo 2004, Norli et al. 2015 without engaging them. Our engine is untouched — and their footnote-level treatment of this literature is itself useful evidence that the structural activism literature has left the margin open (supports our intro's "missing state variables" line).
4. **Free-rider language collision, cosmetic.** Their abstract says information "is critical to overcoming the free rider problem in activist intervention" (title page; pp. 5, 29). Ours says the free-rider tender game pins the premium wedge. Same phrase, different problems (entry-cost externality vs tender dilution). Define both clearly in our lit review to avoid referee conflation.
5. **Crowding-out vs deterrence, low.** Their crowd-out channel is surplus-based, not information-based; complementary rather than competing (§6.i).

**Nothing in the paper anticipates:** κ comparative statics, stake-triggered disclosure as a threshold choice, planner over k_D, tender-game premium wedge, appropriability primitives, the 2024 acceleration, or an engagement-cost distribution.

---

## 8. Quotable Sentences (≤10, with printed pages)

1. "We find that activism complements M&A, reducing the agency frictions associated with takeovers. However, activism simultaneously crowds out some M&A activity by substituting for disciplinary takeovers." (Abstract)
2. "the term ξV(z_t)ν_t reflects the costs arising from limited liquidity and information leakages associated with large share purchases as well as expected campaign costs." (p. 10)
3. "the presence of activists in the economy has essentially zero net effect on the volume of takeovers in equilibrium." (p. 3)
4. "Through this channel, activism crowds out M&A activity—about 0.8 percent of total volume—acting as a partial substitute for takeovers." (p. 3)
5. "in takeovers with an activist present, the bid premium is 13.7 percent (5.2 percentage points) lower than if the activist had not been present." (p. 22)
6. "The size of the activist stake (ν̄) is set to the statutory disclosure threshold of 5 percent, which corresponds to the ownership threshold to file a Schedule 13D with the SEC." (p. 16)
7. "the bid premium reflects the private costs of the board, as the acquirer must offer a higher bid to offset those costs." (p. 18)
8. "the activist never finds it optimal to enter as it is unable to trade on private information, and the returns to its treatment effects are not sufficiently large to overcome the cost of launching a campaign." (p. 29)
9. "This is analogous to the classic free-rider problem in corporate takeovers (Grossman and Hart, 1980), as the costs of the campaign are borne solely by the activist, but the benefits are shared by all shareholders, leading to inefficiently low activism." (p. 29)
10. "Examples include trade block disclosure requirements (Bebchuk et al., 2013; Back et al., 2018), universal proxy regulations (Hirst, 2018), and anti-activist poison pills (Eldar et al., 2023). These factors have the potential to change the cost of activism." (p. 30)
