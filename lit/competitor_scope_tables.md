# Competitor Scope Tables — Three Gating Papers

**Status:** pre-read skeleton, populated from the 2026-06-10 deep-research verified-claim journal (63 claims, 3-vote adversarial verification, 0 refuted) + abstracts + D7/D8 engagement points. **Author validates each cell during the full reads (M0–M1)**; cells marked ◑ are inferred from abstracts/secondary sources rather than the verified journal.

PDFs: `lit/albuquerque-fos-schroth-2022-wp.pdf` (ECGI WP version), `lit/johnson-swem-2021-jfe.pdf` (author-posted JFE version). Celentano–Levine: **author download needed** (SSRN 5506659 anti-bot-blocked; one browser click).

---

## 1. Celentano & Levine (2025) — "Shareholder Activism, Takeovers, and Managerial Discipline"

| Dimension | Their paper | This paper |
|---|---|---|
| Status | SFI RP 25-81, Oct 2025; **R&R at RFS**; FMA 2025 CF semifinalist | Working paper, milestone Mar 2027 |
| Type | **Structural estimation** of equilibrium model: activism + M&A + managerial discipline | Theory-led hybrid: tender-game microfoundation + GE-channel theorem + calibration |
| Core question | Quantify activism's role in the market for corporate control | How market **liquidity** and **disclosure rules** shape activism and takeover premia |
| Mechanism | Activism complements M&A (cuts agency frictions) AND crowds out disciplinary takeovers; CEO incentive effects ◑ | Trading-and-inference: noise trading κ, stake-triggered disclosure D, Bayesian pricing, premium wedge from disagreement-node tender game |
| Trading/liquidity/price impact | **Absent** (no microstructure) | The paper's engine (κ comparative statics, posterior π(X,D)) |
| Disclosure rule | Not modeled as a design object ◑ | First-class: stake-triggered D=1{q=+1}, counterfactual regimes, planner over k_D |
| Free-rider problem | Activist info advantage overcomes free-rider problem in intervention ◑ | Free-rider tender game **pins the premium wedge** (D7: λ = 1 − q(1−γ)ψ) |
| Estimation target | Equilibrium model on activism+M&A data ◑ | Calibration only (this milestone); engagement-cost distribution = white space for 9–24mo leg |
| **Differentiation one-liner** | They price activism's *discipline* role with no market microstructure; we derive *when liquidity and disclosure law* make activism pay, with premia microfounded from tender mechanics. | |

**Threats:** same three nouns (activism, takeovers, governance), structural, top-3 track. **Engagement points:** (i) their crowding-out result is a quantity our deterrence channel (∂p/∂π<0) speaks to; (ii) they have no κ or disclosure-rule comparative statics — exactly our headline objects; (iii) our D7 primitives (q, γ) give testable cross-sections their model doesn't index.

**Full-read checklist (author):** exact state space; does ANY trading/inference appear; how premia are determined (bargaining? auction?); identification strategy + data; whether 2024 13D acceleration is mentioned; whether they cite BCDFLL or engage liquidity at all.

---

## 2. Johnson & Swem (JFE 2021) — "Reputation and Investor Activism: A Structural Approach"

| Dimension | Their paper | This paper |
|---|---|---|
| Type | **Structural dynamic reputation** model (Kreps–Wilson / chain-store lineage), estimated | Static disclosure-and-liquidity equilibrium, calibrated |
| Core object | Activist **reputation** for proxy fighting; campaign frequency, settlements | Liquidity κ and disclosure rule; minority takeover gains Δmin(κ) |
| Key numbers | High-reputation activists: 3.5× campaigns, +85% settlements; reputation ≈ doubles activism's value | κ†≈0.59 hump; disclosure attenuation; wedge from primitives |
| 13D window / σ²T | **Maps the 13D filing window to noise trading via σ²T isomorphism** — owns the 2024-acceleration framing (verified claim) | We do NOT hang the paper on the acceleration; it appears only as a de-risk *data fact* (filing-delay compression) and a testable implication |
| Trading/liquidity/price impact | **Not estimated** — accumulation collapsed to reduced-form lognormal cost draw (verified) | Modeled explicitly (κ, order flow X, pricing P(X,D)) |
| Disclosure timing | Act/disclosure date T **fixed**; endogenous T declared open (verified) | Disclosure is action-triggered, not time-triggered; the threshold is a policy object |
| **Differentiation one-liner** | They estimate *who* activists are (reputation dynamics); we solve *where* activism pays (liquidity, disclosure regime) — orthogonal state variables. | |

**Engagement points:** (i) cite them for the σ²T/13D-window mapping and *defer* the acceleration anchor to them — our Fact 1 is descriptive de-risking, not the paper's identification; (ii) their reduced-form accumulation is exactly the object our microstructure fills; (iii) their fixed-T limitation motivates our action-triggered disclosure as the complementary margin.

**Full-read checklist (author):** the precise σ²T statement and whether the 2024 5-day rule is discussed; their cost-draw distribution (scalar vs distribution — bears on the AFS white space); any liquidity proxies in estimation; whether endogenous-T extension has since appeared.

---

## 3. Albuquerque, Fos & Schroth (JFE 2022) — "Value Creation in Shareholder Activism"

| Dimension | Their paper | This paper |
|---|---|---|
| Type | Structural MLE on the **static binary 13D-vs-13G choice**, joint with announcement returns | Theory + calibration; AFS's headline estimate becomes an *explained quantity* |
| Headline decomposition | 6.34% avg 13D announcement return ≈ 74.8% treatment + 13.4% stock-picking + 11.8% selection (verified) | — |
| **The premium finding** | Activism **LOWERS** takeover bid premia 13.7% (5.2pp) vs no-activist counterfactual (verified) | **Rationalized, not contradicted** (D7 Prop d7:afs): measured premium M = m̄/P falls in activism evidence whenever appropriability λ < λ_crit — price capitalizes activism (denominator) faster than the wedge (numerator); deterrence composition reinforces. m1 ≥ m0 throughout. |
| Engagement cost | **Single constant scalar** — no distribution estimated (verified) | White space reserved for the 9–24mo structural leg (engagement-cost *distribution* on 13D XML) |
| Trading/price impact/stake | Not modeled; stake exogenous (verified) | Modeled |
| First-mover claim | Structural estimation of activism value creation (vs Gantchev 2013 cost-stages) | — |
| **Differentiation one-liner** | Their negative premium effect is our low-λ region: superseding acquirers + hot fringe markets (γ≈0, q≈1). Our model predicts *where* their estimate should flip sign (portable improvements, pivotal stakes, cold fringe markets). | |

**Full-read checklist (author):** exact counterfactual construction behind the −13.7% (which price is the denominator — this is load-bearing for Prop d7:afs's mapping); their sample's strategic-vs-financial acquirer mix (proxies γ); cost-scalar identification (what moment pins it); whether premia are offer-over-price or offer-over-preannouncement.

---

## Overlap matrix (what each paper does / doesn't)

| Object | C–L 2025 | J–S 2021 | AFS 2022 | **This paper** |
|---|---|---|---|---|
| Structural estimation | ✓ (R&R RFS) | ✓ | ✓ | ✗ (calibration; estimation = later leg) |
| Takeovers/M&A in model | ✓ | ✗ | premia as outcome | ✓ (bidder entry + tender microfoundation) |
| Trading/liquidity/price impact | ✗ | ✗ | ✗ | **✓ (engine)** |
| Disclosure rule as object | ✗ ◑ | fixed T | 13D-vs-13G choice | **✓ (design margin + planner)** |
| Premium wedge microfounded | ✗ ◑ | ✗ | ✗ | **✓ (D7 tender game)** |
| Engagement-cost distribution | ? ◑ | lognormal draw (reduced-form) | scalar only | white space (9–24mo) |
| Reputation dynamics | ✗ | ✓ | ✗ | ✗ |
| 2024 acceleration anchor | ? | σ²T mapping (framing taken) | ✗ | data fact only (deliberately) |

**Bottom line for the intro:** the three competitors hold the *estimation* high ground on discipline (C–L), reputation (J–S), and value-creation decomposition (AFS) — none models the trading-and-disclosure margin. This paper's claim: liquidity and disclosure law are the *missing state variables* of the structural activism literature, and the premium wedge those papers assume or estimate as a constant is an equilibrium object of tender mechanics with sign and size that vary in observable primitives.
