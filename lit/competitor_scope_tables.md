# Competitor Scope Tables — Three Gating Papers

**Status:** VALIDATED against full reads, 2026-06-11 (page-anchored reports: `lit/reads/celentano-levine_full_read.md`, `lit/reads/johnson-swem_full_read.md`, `lit/reads/afs_full_read.md`). Originally a pre-read skeleton from the 2026-06-10 deep-research verified-claim journal (63 claims, 3-vote adversarial verification, "0 refuted").

**⚠ Two load-bearing corrections from the full reads — the verified-claim journal was wrong twice:**
1. **The −13.7% (5.2pp) takeover-premium effect is NOT in AFS.** It is **Celentano–Levine (2025), p. 22 / Table 4** (structural counterfactual via board bargaining; verbatim number match). AFS contains *no* takeover, premium, or deal analysis of any kind. All citations of the negative premium estimate must point to C–L; AFS is instead the evidence that prices *capitalize* activism at disclosure (6.34% announcement return, ≈3/4 treatment).
2. **The "13D-window ↔ σ²T isomorphism" is NOT in Johnson–Swem.** No such mapping, no noise-trading object, no window-as-policy discussion exists in the paper (their only window mention is descriptive fn. 13, p. 39). Nobody in the trio owns the 2024-acceleration framing — it is open, and our deliberate "data fact only" posture stands. Do not cite J–S for it.

Cells below marked ◑ were inferences; the per-cell verdicts (CONFIRMED/CORRECTED/NUANCED, with page anchors) live in the three read reports. The tables below have been corrected in place where the reads refuted a cell; all other cells were confirmed.

PDFs: `lit/albuquerque-fos-schroth-2022-wp.pdf` (ECGI WP version), `lit/johnson-swem-2021-jfe.pdf` (author-posted JFE version), `lit/celentano-levine-2025-ssrn.pdf` (SSRN 5506659, SFI RP 25-81 rev. 17 Nov 2025, 62 pp. — downloaded 2026-06-10).

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
| 13D window / σ²T | ~~σ²T isomorphism~~ **REFUTED by full read:** no window↔noise mapping exists in the paper; the 10-day window appears once, descriptively (fn. 13, p. 39); no policy discussion of window length | We do NOT hang the paper on the acceleration; it appears only as a de-risk *data fact* (filing-delay compression) and a testable implication — and the framing turns out to be unowned |
| Trading/liquidity/price impact | **Not estimated** — accumulation collapsed to reduced-form lognormal cost draw (verified) | Modeled explicitly (κ, order flow X, pricing P(X,D)) |
| Disclosure timing | Act/disclosure date T **fixed**; endogenous T declared open (verified) | Disclosure is action-triggered, not time-triggered; the threshold is a policy object |
| **Differentiation one-liner** | They estimate *who* activists are (reputation dynamics); we solve *where* activism pays (liquidity, disclosure regime) — orthogonal state variables. | |

**Engagement points (post-read):** (i) ~~cite them for σ²T~~ **dead** — the mapping is not in the paper; the window↔noise lineage belongs to Back/Collin-Dufresne/Fos-type Kyle models, and nobody owns the 2024-acceleration framing; (ii) their reduced-form accumulation is exactly the object our microstructure fills — cost draw L̃ "encompassing the price impact associated with buying shares" (p. 30), mean 5.44% of position (p. 42); their CAR equation prices the 13-D only through success probability, no order-flow inference (eqs. 18/23); (iii) stronger than "fixed-T": the disclosure margin is *absent* (the 13-D is an instantaneous initiation flag; "disclosure" never appears) — their single state r_t is orthogonal to our (κ, D) by construction. Quote levels as "3.5 vs 0.6 campaigns/yr" (abstract's "3.5×" is loose; body says 6×, p. 46).

**Full-read checklist (author):** the precise σ²T statement and whether the 2024 5-day rule is discussed; their cost-draw distribution (scalar vs distribution — bears on the AFS white space); any liquidity proxies in estimation; whether endogenous-T extension has since appeared.

---

## 3. Albuquerque, Fos & Schroth (JFE 2022) — "Value Creation in Shareholder Activism"

| Dimension | Their paper | This paper |
|---|---|---|
| Type | Structural MLE on the **static binary 13D-vs-13G choice**, joint with announcement returns | Theory + calibration; AFS's headline estimate becomes an *explained quantity* |
| Headline decomposition | 6.34% avg 13D announcement return ≈ 74.8% treatment + 13.4% stock-picking + 11.8% selection (verified) | — |
| **The premium finding** | ~~−13.7% (5.2pp)~~ **CORRECTED: not in AFS — the number is Celentano–Levine (2025) p. 22/Table 4.** AFS has no takeover/premium/deal analysis (0 hits across all 84 pp.); their object is the filing CAR [t−30,t+10]. What AFS *does* deliver: prices capitalize activism at disclosure (6.34%, ≈3/4 treatment) — the **denominator** input to our Prop d7:afs | **Rationalized, not contradicted** (D7 Prop d7:afs, re-anchored to C–L): measured premium M = m̄/P falls in activism evidence whenever appropriability λ < λ_crit — price capitalizes activism (denominator, magnitude per AFS) faster than the wedge (numerator); deterrence composition reinforces. m1 ≥ m0 throughout. C–L's rival mechanism (board bargaining, c_m(ν)) moves only with activist presence; ours is indexed by (q, γ, ψ, κ) — different cross-sections. |
| Engagement cost | **Single constant scalar** — no distribution estimated (verified) | White space reserved for the 9–24mo structural leg (engagement-cost *distribution* on 13D XML) |
| Trading/price impact/stake | Not modeled; stake exogenous (verified) | Modeled |
| First-mover claim | Structural estimation of activism value creation (vs Gantchev 2013 cost-stages) | — |
| **Differentiation one-liner** | (Re-targeted at C–L, the true source of the negative premium estimate:) the estimated negative activism–premium effect is our low-λ region: superseding acquirers + hot fringe markets (γ≈0, q≈1). Our model predicts *where* the estimate should flip sign (portable improvements, pivotal stakes, cold fringe markets). vs AFS proper: they hold the value-creation-decomposition high ground; our engagement-cost-distribution leg and κ-engine are literally their declared future research (p. 41). | |

**Full-read checklist (author):** exact counterfactual construction behind the −13.7% (which price is the denominator — this is load-bearing for Prop d7:afs's mapping); their sample's strategic-vs-financial acquirer mix (proxies γ); cost-scalar identification (what moment pins it); whether premia are offer-over-price or offer-over-preannouncement.

---

## Overlap matrix (what each paper does / doesn't)

| Object | C–L 2025 | J–S 2021 | AFS 2022 | **This paper** |
|---|---|---|---|---|
| Structural estimation | ✓ (R&R RFS) | ✓ | ✓ | ✗ (calibration; estimation = later leg) |
| Takeovers/M&A in model | ✓ | ✗ | ✗ (filing CARs only; no deals) | ✓ (bidder entry + tender microfoundation) |
| Trading/liquidity/price impact | ✗ | ✗ | ✗ | **✓ (engine)** |
| Disclosure rule as object | ✗ ◑ | fixed T | 13D-vs-13G choice | **✓ (design margin + planner)** |
| Premium wedge microfounded | ✗ ◑ | ✗ | ✗ | **✓ (D7 tender game)** |
| Engagement-cost distribution | scalar ξ=0.030 only (resolved) | lognormal draws (3 families, τ estimated — but from campaign frequencies, not cost microdata) | scalar only | white space (9–24mo): a cost *distribution from filing microdata, linked to liquidity primitives* — wording matters since J–S do estimate distribution parameters |
| Reputation dynamics | ✗ | ✓ | ✗ | ✗ |
| 2024 acceleration anchor | ✗ (absent; sample ends 2019) | ✗ (refuted — no σ²T mapping exists; framing unowned) | ✗ | data fact only (deliberately) — and the framing is open |

**Bottom line for the intro:** the three competitors hold the *estimation* high ground on discipline (C–L), reputation (J–S), and value-creation decomposition (AFS) — none models the trading-and-disclosure margin. This paper's claim: liquidity and disclosure law are the *missing state variables* of the structural activism literature, and the premium wedge those papers assume or estimate as a constant is an equilibrium object of tender mechanics with sign and size that vary in observable primitives.

---

## Positioning memo (validated, 2026-06-11)

All cells above are now full-read-validated (reports in `lit/reads/`). The five sentences that survive adversarial reading:

1. **The lane is empty.** None of the trio models trading, order-flow inference, or the disclosure rule as a design object — C–L collapse all regulation into a scalar cost ξ (their p. 30); J–S collapse accumulation into a lognormal draw (their p. 32); AFS defer the trading margin to Back et al. (2018) and name our agenda as future research (their p. 41, fn. 6).
2. **The negative premium fact belongs to C–L** (−13.7%/5.2pp, p. 22, Table 4, board-bargaining channel). Our Prop d7:afs offers a complementary mechanism — capitalized denominator + deterrence — indexed by (q, γ, ψ, κ) where theirs moves only with activist presence: different cross-sections, jointly testable.
3. **AFS is our denominator evidence, not our premium anchor**: 13D announcement returns ≈ 3/4 anticipated treatment — the price capitalization Prop d7:afs's mechanism requires.
4. **The 2024-acceleration framing is unowned** — J–S contains no σ²T mapping (refuted on full read); our deliberate "data fact, not identification" posture stands, and Facts 1–2 now exist (delay compression 7→5 days, 36%→76% within-5bd; CAR doubling post-rule with a strong liquidity cross-section, t≈−3.7).
5. **The selection-vs-treatment dispute (C–L 91/9 vs AFS ~25/75) is endogenous to our model**: how much information is capitalized at the 13D event is governed by (κ, D) through π(X,D) — we endogenize the very quantity the two structural papers disagree about. (High-value engagement point; both papers at once.)

Residual watch-items: C–L's "free-rider" language collision (entry-stage vs our tender-stage — define both); quote J–S levels as "3.5 vs 0.6 campaigns/yr" (not "3.5×"); engagement-cost white space wording: "no one estimates the cost distribution *from filing microdata or links it to liquidity*" (J–S do estimate lognormal parameters from campaign frequencies).
