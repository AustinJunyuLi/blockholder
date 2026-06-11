# Full Read: Johnson & Swem (JFE 2021) — "Reputation and Investor Activism: A Structural Approach"

**Read date:** 2026-06-11. **Reader coverage:** every page of `lit/johnson-swem-2021-jfe.pdf` (28 PDF pages = JFE 139 (2021) pp. 29–56, published Elsevier version, including printed Appendices A–D and references), plus full-text keyword sweep (pdftotext + regex) for: `noise`, `isomorph`, `sigma/σ`, `Kyle`, `microstructure`, `accumulat`, `toehold`, `window`, `liquidity`, `disclos*`, `endogen*`, `takeover`, `premium/premia`, `Amihud`, `spread`, `turnover`, `Williams Act`, `Schedule 13`, `2024`, `business day`, `deadline`.

**Page convention:** all page numbers below are **JFE journal pages** (29–56). PDF page = journal page − 28.

**Coverage caveat:** the pre-read brief said "~42 pages, author-posted version"; the actual file is the **28-page published version**. Online Appendices A–G (referenced at pp. 32–33, 39, 42, 44, 46, 49, 52) are **not bundled** in this PDF. Their referenced contents are: OA B (activist-specific data quality / varying Δ), OA C (standard errors), OA D (plots for r₀, λ_r, Δ), OA E (robustness: δ, λ_c, 20-day CAR window, fixed â, random Δ, fight success fraction φ), OA F (longer return windows), OA G (non-hedge-fund activists). None of these titles or in-text descriptions concerns trading, noise, windows-as-policy, or disclosure timing, so the negative findings below are robust to the missing online appendix with high confidence.

---

## 1. Metadata

| Field | Value |
|---|---|
| Title | Reputation and Investor Activism: A Structural Approach |
| Authors | Travis L. Johnson (UT Austin McCombs), Nathan Swem (Federal Reserve Board) |
| Journal | Journal of Financial Economics 139 (2021) 29–56 |
| Timeline | Received 6 Mar 2019; revised 19 Aug 2019; accepted 12 Sep 2019; online 5 Jul 2020 (p. 29) — **all content predates the SEC's 2023 adoption / 2024-02-05 effectiveness of the five-business-day 13D rule** |
| JEL / Keywords | G23, G34, G35; investor activism, reputation, governance, hedge funds, structural estimation (p. 29) |
| Public artifact | Estimated reputation measure per campaign posted on Johnson's website (fn. 2, p. 30) |

## 2. Model Summary

**Class:** dynamic reputation game in the Kreps–Wilson (1982) / Milgrom–Roberts (1982) chain-store lineage, generalized via Fudenberg–Levine (1989, 1992); "to our knowledge, we are the first to apply it to investor activism" (p. 32). One long-lived activist *A* of unknown type vs. a sequence of short-lived target managers *M* (each targeted once, p. 33).

**Stage game** (Model Fig. 1, p. 32): three stages, played **instantly** upon opportunity arrival:
1. *A* chooses **13-D** (initiate campaign, paying cost L̃ > 0) or **Ignore**. The 13-D is the campaign-initiation action itself — there is no accumulation phase, no trading, and no disclosure-timing choice in the model.
2. *M* chooses **Settle** (take the Δ-project, pay private cost B > Δ net) or **Refuse**.
3. If refused, *A* chooses **Fight** (proxy fight, always succeeds; costs F̃_A to *A*, F̃_M to *M*) or **Fold**.

**Cost structure — the reduced form** (eqs. 4–6, p. 32): per-campaign i.i.d. lognormal draws,
log(L̃) ~ N(μ_L, τ_L⁻²), log(F̃_M/(B−Δ)) ~ N(μ_M, τ_M⁻²), log(F̃_A) ~ N(μ_A, τ_A⁻²).
Campaign cost L̃ explicitly stands in for accumulation/trading frictions: "Campaign costs include the round trip liquidity costs of buying and selling shares, as well as the effort and expense related to regulatory document submissions, communications with target managers, and fundamental research analysis" (p. 32); intro version: "a private cost encompassing the price impact associated with buying shares in the target…" (p. 30, citing Gantchev 2013; Brav et al. 2008; **Back et al. 2018** — their only contact with the strategic-trading literature is this cost citation plus a one-line lit-review mention, p. 31).

**Types and state:** activists differ **only** in mean log fight cost μ_A ∈ {μ_agr < μ_caut} (p. 33). "The only state variable in the model is A's reputation r_t, defined as the probability that A is the aggressive type conditional on their observed track record" (p. 33). Bayesian updating after campaigns (eq. 8, p. 33; App. A.1 eqs. A.7–A.10, p. 53); r_t decays toward r₀ between campaigns; Poisson type resets at rate λ_r (p. 34).

**Dynamics:** campaign opportunities arrive via Poisson at annualized rate λ_c (fixed at 10), discount factor δ (fixed at 0.9), type resets λ_r (estimated 0.19/yr). Equilibrium = five functions of r_t: d_caut(r_t), d_agr(r_t) (initiation), y(r_t) (settle), f_caut(r_t), f_agr(r_t) (fight), eqs. (10)–(15), p. 34; solved by value-function iteration on a 106-point grid of r_t (App. A.2, p. 53).

**Pricing:** there is no market. The only price object is the measurement equation CAR ~ N(Δ·P(project occurs | r_t, 13-D), σ²_car) (eq. 18 p. 39; eq. 23 p. 42) — prices react to campaign initiation solely through success probability; no order flow, no inference from trades.

**Mechanisms** (summary list, p. 35): high-reputation activists initiate more campaigns; targets settle more with them; they fight more when refused; all activists sometimes initiate/fight at a single-campaign loss as reputation investment.

## 3. Data & Identification

- **Sample:** 13-D filings from EDGAR (35,768 raw) + SharkWatch (5,910) → 4,235 nonoverlapping campaigns 1999–2016 after CRSP-Compustat matching and filters (drop funds/SPACs; wolf-pack campaigns attributed to a lead activist, p. 40); **main sample: 2,434 campaigns by 420 unique hedge funds targeting 1,889 firms**; 737,004 activist-days for the 13-D frequency variable (pp. 39–41); 603 non-hedge-fund activists relegated to OA G (p. 40).
- **Observables:** 13-D indicator; Proxy (from DFAN14A/DEFR14A/DEFC14A/DEFN14A filings or SharkWatch, fn. 15 p. 40); action vector **a** = (Reorg, Payout, CEO, Board, Acq) measured in the year after initiation from Capital IQ/SharkWatch/Compustat (pp. 40–41, App. B.3 p. 54); CAR = [−1,+1] market-adjusted return around initiation (p. 40). Settlements are **not directly observed**; P(a_i=1) = â_i + 1(Settle or Fight)·β_i (eq. 7, p. 33), with â from propensity regressions on firm characteristics (App. C, p. 54).
- **Method:** **maximum likelihood**, not SMM — "we use a maximum likelihood estimation (MLE), which is similar to the simulated maximum likelihood approach in Morellec et al. (2012)… We use MLE because we have a closed-form solution and a rich enough model to fit the distribution of observed data" (p. 32). Likelihood per campaign = gap × opportunity × CAR × outcome components (eq. 22 p. 42; App. D.1, p. 55). Wilks LR tests (Table 2 Panel C, p. 43).
- **Estimates** (Table 2 Panel A, p. 43): Δ = 6.62% (SE 0.66); d_caut,0 = 4.16%; τ_L = 1.65; y₀ = 21.82%; τ_M = 0.33; f_caut,0 = 11.10%; f_agr,0 = 48.03%; τ_A = 1.45; r₀ = 2.05%; λ_r = 0.19. Fixed (Panel B): δ = 0.9, σ_car = 8.99%, β_reorg = 32.25, β_payout = 6.16, β_ceo = 17.53, β_board = 67.63, β_acq = 30.76, λ_c = 10.
- **Implied costs** (p. 42): mean campaign cost L̃ = **5.44% of the activist's position**; mean proxy-fight cost F̃_A = 8.68% (aggressive) / 19.44% (cautious); cf. Gantchev (2013): 5.05% non-proxy + 8.27% proxy.
- **Key moments** (Table 3, p. 45): means of 13-D/yr, AbActions|Proxy=0, CAR, Proxy in full sample and four subsample differences (high-vs-low r_t; recently-updated r_t; new activists; decaying r_t); identification narrative per parameter in §3.6 (pp. 35–39) and §5.2 (pp. 44–46).
- **Hypothesis tests:** no-reputation null rejected (χ² = 340.1) and full-information null rejected (χ² = 21.0), both p ≈ 0 (Table 2 Panel C, p. 43).
- **Liquidity proxies: none.** No Amihud, no bid-ask spreads, no target-stock turnover anywhere in estimation, moments, or controls. The only liquidity-adjacent variable is **Portfolio Turnover** — the *activist's* trailing one-year average quarterly portfolio turnover (Gaspar et al. 2005), used solely as a Table 6 Panel C robustness control (pp. 50, 54). App. C propensity regressions use Log Size, EBIT/Assets, Net Leverage, Payout/Assets, Capex/Assets, Book-to-Market, Inst Ownership, One-Year Return — no liquidity variable (p. 54).

## 4. Cell-by-Cell Validation (Section 2 scope table + J–S column of overlap matrix)

| Cell | Pre-read claim | Verdict | Evidence |
|---|---|---|---|
| Type | Structural dynamic reputation model (Kreps–Wilson / chain-store lineage), estimated | **CONFIRMED** | p. 32: framework "originated in Kreps and Wilson (1982) and Milgrom and Roberts (1982), which study the chain-store game"; estimated by MLE (pp. 32, 42) |
| Core object | Activist reputation for proxy fighting; campaign frequency, settlements | **CONFIRMED** | Abstract p. 29; r_t = P(aggressive type \| track record) is the **only** state variable (p. 33) |
| Key number: 3.5× campaigns | High-reputation activists: 3.5× campaigns | **CONFIRMED (abstract wording) / NUANCED (body)** | Abstract p. 29: "initiate 3.5 times as many campaigns." Body: high-rep initiate **3.5 campaigns/yr vs 0.6** (p. 30); precisely "3.50 per year, **six times as frequently** as the 0.58 per year rate" (p. 46; Table 5 p. 49: model 3.50 vs data 3.48 for r_t>50%). The "3.5" is the *level* per year; the frequency *ratio* is ≈6×. Cite as "3.5 vs 0.6 campaigns/yr," not "3.5×" |
| Key number: +85% settlements | High-reputation: +85% settlements | **CONFIRMED** | Abstract p. 29 "extract 85% more settlements"; mechanism: settle rate 44.11% (r_t>50%) vs 23.86% (r_t<0.5%), 44.11/23.86 = 1.85 (p. 46; Table 5 p. 49). Minor internal wrinkle: intro states "44%… compared to 29%" (p. 30) — the 85% matches the §5.4/Table 5 figures, not the intro's 29% |
| Key number: reputation ≈ doubles activism's value | Reputation ≈ doubles value added | **CONFIRMED** | Abstract p. 29 "nearly double"; "target shareholders' average payoff would be 48% lower without reputation" (p. 31); "would decline by at least 48% in all three counterfactuals" (p. 52); Table 7 p. 51: 24.53 bp baseline vs 12.67 bp no-reputation (ratio 1.94). Robustness band: 35–60% less value (p. 52). Bonus: reputation-building explains 20% of initiations (19.92%, p. 46) and 19% of fights (18.83%, p. 48) |
| **13D window / σ²T (LOAD-BEARING)** | "Maps the 13D filing window to noise trading via σ²T isomorphism — owns the 2024-acceleration framing (verified claim)" | **REFUTED — no such content anywhere** | Full-text sweep: 0 hits for "isomorph", "Kyle", "microstructure", "noise trad*", "Williams Act", "Schedule 13", "variance". σ appears only as σ_car (std. dev. of CAR, pp. 41–43, 55) and the normal CDF Φ. All four "noise" hits are estimation noise in cost draws / M's observation of outcomes (pp. 33, 36, 39). The 13-D window appears **once**, descriptively: fn. 13, p. 39. No model object T exists. Likely mis-attribution from the Back–Collin-Dufresne–Fos–Li–Ljungqvist (Econometrica 2018) strategic-trading lineage, which J–S cite only as a campaign-cost reference (p. 32) and in a one-line lit list (p. 31) |
| Trading/liquidity/price impact | "Not estimated — accumulation collapsed to reduced-form lognormal cost draw (verified)" | **CONFIRMED** | Cost encompasses "the price impact associated with buying shares in the target" (p. 30) and "the round trip liquidity costs of buying and selling shares" (p. 32); lognormal draws eqs. (4)–(6), p. 32; estimated τ_L = 1.65, implied mean cost 5.44% of position (pp. 42–43). No trading, no order flow, no market-maker inference anywhere |
| Disclosure timing | "Act/disclosure date T fixed; endogenous T declared open (verified)" | **CORRECTED — overstates what exists** | There is **no disclosure date T in the model at all** — fixed or otherwise. "disclos*" : 0 hits in the entire paper; "endogen*": 0 hits. The 13-D is an instantaneous initiation flag; opportunity timing is exogenous Poisson and "the stage game is played instantly" (p. 33). The conclusion's open questions concern *other reputation dimensions* (target selection, negotiation skills…), not disclosure timing (p. 52). So the true statement is stronger for us: the disclosure margin is *absent*, not "fixed" |
| Differentiation one-liner | They estimate *who* activists are (reputation); we solve *where* activism pays (liquidity, disclosure) — orthogonal state variables | **CONFIRMED, strengthened** | "The only state variable in the model is A's reputation r_t" (p. 33) — literally orthogonal to our (κ, D) |
| Matrix: Structural estimation ✓ | ✓ | **CONFIRMED** (method: MLE, not SMM) | pp. 32, 42 |
| Matrix: Takeovers/M&A in model ✗ | ✗ | **CONFIRMED (with footnote)** | No takeover modeling, no bidders, no premia. "takeover" appears once, describing Corum & Levit (2019) (p. 31). M&A enters only as the **Acq outcome indicator** (target announces merger/acquisition/divestiture within a year; β_acq = 30.76% added probability in successful campaigns) — descriptive outcome, not a model object (pp. 40, 43, 54) |
| Matrix: Trading/liquidity/price impact ✗ | ✗ | **CONFIRMED** | See above; also zero liquidity proxies in estimation (§3 above) |
| Matrix: Disclosure rule as object — "fixed T" | fixed T | **CORRECTED** to "absent" | See disclosure-timing row |
| Matrix: Premium wedge microfounded ✗ | ✗ | **CONFIRMED** | "premium/premia": 0 substantive hits (only the Dimopoulos–Sacchetto reference title, p. 56) |
| Matrix: Engagement-cost distribution — "lognormal draw (reduced-form)" | lognormal | **CONFIRMED** | Eqs. (4)–(6) p. 32; three lognormal families (campaign cost + both parties' fight costs); type heterogeneity = two-point mixture over μ_A (p. 33). They *do* estimate distributional parameters (τ_L, τ_M, τ_A) — but identified off campaign frequencies/outcomes, not cost microdata |
| Matrix: Reputation dynamics ✓ | ✓ | **CONFIRMED** | Entire paper |
| Matrix: 2024 acceleration anchor — "σ²T mapping (framing taken)" | framing taken by J–S | **REFUTED** | No σ²T, no window-as-policy discussion, no acceleration analysis (paper predates the rule; "2024", "five", "business day": 0 hits). **The acceleration framing is NOT taken by J–S** |

## 5. Checklist Answers

1. **Precise σ²T statement:** **does not exist in this paper.** Closest passages: (i) fn. 13, p. 39 (the only mention of the window): "The SEC requires that investors file a beneficial ownership report on Form 13-D within ten days of initiating an activist campaign." — purely institutional, attached to the sample-construction discussion; (ii) the cost-encompassing-price-impact sentences (pp. 30, 32). Nothing maps the window length to noise trading, variance, or any policy counterfactual.
2. **2024 five-business-day rule / window as policy margin:** never discussed (paper predates the rule). The 10-day window is **never** treated as a policy margin; no "shortening the window would…" statement exists. The only "window" discussions are CAR *measurement* windows: [−1,+1] baseline, a "wider 20-day window for measuring the market's reaction" as OA E robustness (p. 52), and longer return windows in OA F (p. 49) — do not confuse these with the filing window.
3. **Cost draw — scalar vs distribution:** a **distribution** (three, in fact): per-campaign i.i.d. lognormal draws for L̃ (campaign cost), F̃_M/(B−Δ), F̃_A (eqs. 4–6, p. 32), with precisions τ_L = 1.65, τ_M = 0.33, τ_A = 1.45 estimated (Table 2, p. 43). It stands in for: round-trip liquidity costs of buying/selling shares + price impact + regulatory document submissions + communications + research (pp. 30, 32). Bearing on our white space: J–S occupy "estimated cost *distribution* identified from campaign frequency/outcomes"; AFS occupy "scalar." The white space we reserve — engagement-cost distribution estimated from 13D-filing microdata and linked to *liquidity primitives* — remains open, but our claim should say "no one estimates the cost distribution from filing microdata or links it to liquidity," not "no one estimates a distribution."
4. **Liquidity proxies in estimation:** none (no Amihud, no spreads, no target turnover). Only the activist-level Portfolio Turnover control in robustness regressions (Table 6 Panel C, p. 50; def. App. B.2, p. 54) and Stake Size from 13-F (mean ≈7% where unmatched, p. 54).
5. **Model timing & state space:** continuous-time arrival (Poisson λ_c = 10/yr) of instantaneous three-stage games (13-D/Ignore → Settle/Refuse → Fight/Fold); single state variable r_t ∈ [0,1]; r_t decays between campaigns (eq. A.1, p. 52), jumps via Bayes after campaigns (eqs. 7–8, p. 33; A.7–A.8, p. 53); type resets λ_r = 0.19/yr; δ = 0.9 annualized.
6. **Estimation method, data, key moments:** MLE (closed-form likelihood; explicitly preferred over SMM, p. 32); 2,434 hedge-fund campaigns 1999–2016, 737,004 activist-days (EDGAR 13-D + SharkWatch + CRSP/Compustat/Capital IQ); moments: 13-D/yr, AbActions|Proxy=0 (settlement proxy), Proxy frequency, CAR — levels and high-vs-low/recently-updated/new-activist/decaying-r_t differences (Table 3, p. 45); identification elasticities in Table 3, narrative §3.6.
7. **Endogenous-T extension since:** n/a from this read (no T exists to endogenize; nothing in the paper flags it as future work — the stated future-research agenda is other reputation skills, p. 52).

## 6. Headline Quantitative Results (with pages)

- High-reputation activists: 3.5 campaigns/yr vs 0.6 (p. 30); 3.50 vs 0.58, "six times as frequently" (p. 46); model vs data 3.50 vs 3.48 (Table 5, p. 49).
- Settlement rates: 44.11% (high r_t) vs 23.86% (low r_t) → the abstract's "+85% settlements" (pp. 29, 46; Table 5 p. 49). Fight-when-refused: 26% vs 14% (p. 30).
- Reputation-building motives: 19.92% of 13-D initiations (p. 46); 18.83% of proxy fights (p. 48); robustness 15–30% of aggressive behavior (p. 52).
- Counterfactual value: target shareholders' payoff −48% without reputation (pp. 31, 52); 24.53 bp → 12.67 bp per opportunity (Table 7, p. 51); robustness 35–60% (p. 52).
- Estimated primitives: Δ = 6.62% project value; mean campaign cost 5.44% of position; fight costs 8.68%/19.44% (agr/caut); r₀ = 2.05% (pp. 42–43).
- Distribution of reputation: median r_t = 0.55%, mean 10.81%, 75% below 10% (pp. 36, 46; Table 4 p. 48). Top activists: Starboard 79.15%, Icahn 61.70% (Table 4, p. 48).
- Mean CAR = 2.82%; 14.3% of campaigns have proxy fights (Table 1, p. 41).
- Both nulls rejected: no-reputation χ² = 340.1, full-information χ² = 21.0 (Table 2 Panel C, p. 43).

## 7. Engagement Points (conjectures confirmed/sharpened/revised)

1. **REVISED — do NOT cite J–S for the σ²T/13D-window mapping.** The mapping is not in the paper; citing them for it would be a checkable citation error (and Johnson is a plausible referee). Action: the conjectured "defer the acceleration framing to them" is dead as stated. Re-attribute: the natural home of window-length ↔ noise-trading-variance logic is the Kyle-lineage activism papers — Back, Collin-Dufresne, Fos, Li & Ljungqvist (Econometrica 2018) and Collin-Dufresne & Fos (2015/2016), which J–S cite only in passing (pp. 31–32, 55–56). **Verify BCDFLL (`lit/Back-ACTIVISMSTRATEGICTRADING-2018.pdf`) before asserting anyone owns the framing; if no one does, we can own it** (with our deliberate "data fact only" posture intact). Also fix `competitor_scope_tables.md` row 36 and overlap-matrix row "2024 acceleration anchor" before drafting the intro.
2. **CONFIRMED and sharpened — their reduced-form accumulation is exactly the object our microstructure fills.** Quote pair: cost "encompassing the price impact associated with buying shares in the target" (p. 30) and "round trip liquidity costs of buying and selling shares" (p. 32) — i.e., everything our κ, order flow X, and pricing P(X,D) generate is compressed into one lognormal draw L̃ with estimated mean 5.44% of position (p. 42). Even sharper hook: their market-reaction equation CAR ~ N(Δ·P(project occurs|r_t,13-D), σ²_car) (eqs. 18, 23; pp. 39, 42) prices the 13-D only through success probability — no inference from order flow. Our posterior-pricing machinery microfounds both their cost draw *and* their CAR equation. Bonus calibration anchor: their (Δ, L̃, F̃) magnitudes are usable discipline for our engagement-cost calibration.
3. **REVISED (stronger for us) — not "fixed-T limitation" but total absence of the disclosure margin.** The word "disclosure" never appears; the 13-D is an instantaneous initiation flag triggered by exogenous Poisson opportunities (p. 33). Correct positioning sentence: J–S model *who* files (reputation selects activists into campaigns) while treating the filing itself as a costless-information, exogenously-timed event; we model *when/whether the filing threshold is crossed* and what the rule's design (stake-triggered D, threshold k_D) does to prices, engagement, and premia. Their single state r_t is orthogonal to our (κ, D) — complementary by construction, zero collision.

## 8. Threat Assessment

**Verdict: LOW.**

- **Liquidity as engine:** no overlap. No trading, no noise traders, no price impact beyond a cost label; zero liquidity proxies in estimation. The "engine" cell of the overlap matrix stands.
- **Disclosure rule as design object:** no overlap — stronger than pre-read believed: the disclosure margin is entirely absent (not "fixed"). No policy counterfactual on the window exists.
- **Microfounded premium wedge / takeover analysis:** none. No bidders, no tender, no premia. M&A appears only as the Acq *outcome indicator* (β_acq = 30.76, Table 2 Panel B, p. 43) — worth one footnote-level acknowledgment that activism raises M&A likelihood descriptively (they cite Boyson et al. 2017, p. 31), but nothing prices a takeover.
- **Residual risks (process, not overlap):** (i) the **mis-attributed σ²T claim in our own scope table** is the real hazard — if it migrated into draft text, it must be excised/re-attributed (check BCDFLL next); (ii) when quoting their headline, use "3.5 vs 0.6 campaigns per year" rather than "3.5×" — the abstract's ratio wording is internally loose (body says 6×, p. 46), and precision here signals we actually read the paper; (iii) their estimated cost *distribution* slightly narrows how we word the engagement-cost white space (see Checklist #3).

## 9. Quotable Sentences (verbatim, with JFE pages)

1. p. 29 (abstract): "We find that high reputation activists initiate 3.5 times as many campaigns and extract 85% more settlements from targets, and that reputation-building incentives explain 20% of campaign initiations and 19% of proxy fights."
2. p. 29 (abstract): "Our estimates indicate these reputation effects combine to nearly double the value that activism adds for target shareholders."
3. p. 30: "the activist decides whether to initiate a campaign, which entails a private cost encompassing the price impact associated with buying shares in the target, the effort and expense related to communications with targets and regulators, and any other expenses prior to a proxy fight"
4. p. 32: "Campaign costs include the round trip liquidity costs of buying and selling shares, as well as the effort and expense related to regulatory document submissions, communications with target managers, and fundamental research analysis"
5. p. 32: "This reputation concept has been applied to many settings in finance…, but, to our knowledge, we are the first to apply it to investor activism."
6. p. 33: "The only state variable in the model is A's reputation r_t, defined as the probability that A is the aggressive type conditional on their observed track record of campaigns occurring prior to t."
7. p. 33: "Campaign opportunities arrive exogenously according to a Poisson process with an annualized arrival rate λ_c… Upon receiving a campaign opportunity, the above stage game is played instantly."
8. p. 39 (fn. 13 — the paper's ONLY mention of the filing window): "The SEC requires that investors file a beneficial ownership report on Form 13-D within ten days of initiating an activist campaign."
9. p. 31: "Combining these effects, we estimate target shareholders' average payoff would be 48% lower without reputation."
10. p. 46: "high r_t activist-days (those with r_t > 50%) result in campaign initiations at a rate of 3.50 per year, six times as frequently as the 0.58 per year rate for low r_t activist-days (those with r_t < 0.50%)."
