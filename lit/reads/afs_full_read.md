# Full Read — Albuquerque, Fos & Schroth, "Value Creation in Shareholder Activism: A Structural Approach"

**Read:** 2026-06-11, all 84 PDF pages including internal appendix, tables, figures, and ECGI back matter, plus a decompressed-text keyword sweep of the entire PDF.
**File:** `lit/albuquerque-fos-schroth-2022-wp.pdf`
**Page convention:** "p.N" = printed paper page (paper p.N = PDF p.N+5 for the main text; internal-appendix p.N = PDF p.N+61).

---

## 1. Metadata

- **Version read:** ECGI Finance Working Paper N° 685/2020, dated **July 8, 2020** (title page, PDF p.4); SSRN 3639636. This is *not* the published JFE text. Published version: JFE 145(2), 2022, 153–178.
- **Authors:** Rui Albuquerque (Boston College, CEPR, ECGI), Vyacheslav Fos (Boston College, CEPR, ECGI), Enrique Schroth (EDHEC, CEPR).
- **Length:** main text pp.1–41; references pp.42–43; Tables 1–7 pp.44–52; Figures 1–4 pp.53–56; Internal Appendix pp.1–20 (Appendices A–E, Tables A1–A6, Figures A1–A2); 3 pp. ECGI covers/back matter.
- **JEL:** C34, G14, G34. Keywords: shareholder activism, value creation, passive investors, stock picking, structural estimation (PDF p.3, p.5).
- **Version-number caveat:** this WP's decomposition is **75.2% / 12.2% / 12.6%** (treatment / stock picking / selection). The scope table's 74.8 / 13.4 / 11.8 tracks the published JFE version. All page-anchored numbers below are WP numbers.

## 2. Model Summary

Static, one-shot binary filing choice; no dynamics, no takeovers, no trading.

- **Choice (§2, pp.8–11):** an investor who has *already* acquired a stake chooses Schedule 13D (activist) vs 13G (passive). Valuation gains are normal r.v.s Δ_D = μ_D + ε_{Δ_D}, Δ_G = μ_G + ε_{Δ_G}. Before filing she observes noisy due-diligence signals s_D = Δ_D + ε_{s_D}, s_G = Δ_G + ε_{s_G}. Risk-neutral; files 13D iff EU_D = E(Δ_D|s_D) − C > EU_G = E(Δ_G|s_G) (eq. 1, p.11). Risk aversion is shown isomorphic to a relabeled C (Appendix A, app. pp.2–3, eq. A.6).
- **Cost (§2.3, §2.6, pp.10, 14–15):** C is the private cost of activism, borne only by the filer, **constant across all filings** ("We assume that C is constant across all filings in the data... The main reason... is to keep the model parsimonious," p.15). It bundles pecuniary cost, risk disutility, reputational penalty, private benefits (netted), and any accumulation-cost differential (p.15).
- **Econometrician's problem (§2.4–2.5, pp.11–14):** filing event {z > 0} with z = EU_D − EU_G censors each return distribution; Arnold et al. (1983) conditional density (eq. 6, p.12); E(Δ_D|z>0) = μ_D + ρ_{zD}σ_{Δ_D}λ_D(α) (eq. 7, p.13).
- **The decomposition (eq. 9, p.14):** E(Δ_D|z>0) = (μ_D − μ_G) [treatment] + μ_G [stock picking] + ρ_{zD}σ_{Δ_D}λ_D(α) [sample selection]. Estimating stock picking and treatment "requires knowledge of the counterfactual valuation, μ_G" (p.14).
- **Expected returns (§3.1, p.16):** μ_{D,i} = x_i′β_D, μ_{G,i} = x_i′β_G; x = firm characteristics (leverage, B/M, ROA, Amihud illiquidity, analyst coverage, inst. ownership, idio. vol., past return, size, age, sales growth, HHI), investor 13D/13G filing experience, activist-HF dummy, FF3 factors (pp.16–17).
- **Estimation (§3.2–3.3, pp.17–22):** MLE on the joint likelihood of filing choices and announcement returns; β_D FOC = selection-corrected OLS orthogonality (eq. 11–12, p.19); C's FOC (eq. 13, p.20) equates average inverse-Mills selection across 13D and 13G samples.

## 3. Data & Identification

- **Sample (§4, pp.23–25; Tables 1–2, pp.44–45):** EDGAR 1996–2017 universe (50,708 13D; 171,051 13G) → CRSP/Compustat merge → drop 28,663 Feb-14 exempt 13G filings → final **69,937 filings = 8,703 13D + 61,234 13G**. Activist hedge funds: 7,551 filings (5,012 13D per p.24; estimation subsample 2,523 13D + 4,219 13G, Table A2/A3).
- **Return variable (Table 1, p.44; §3.2, p.17):** CAR, Fama-French 3-factor, **window [t−30, t+10] around the filing date** — starts at t−30 "because Collin-Dufresne and Fos (2015) show that price appreciation prior to Schedule 13D filings likely reflects the price impact of activist's trades" (p.17). Winsorized 1%/99%.
- **Headline moments:** mean CAR 6.33% (13D) vs 0.59% (13G) raw (Table 2, p.45); 6.34% model/decomposition base (Table 5, p.50; p.1 intro).
- **Key estimates (spec. (4), Table 3, pp.47–48):** C = 0.046*** (4.6pp of stake value ≈ **$2.43m**; net activist return 6.33 − 4.6 = 1.73%, p.28); σ_{Δ_D} = 0.219, σ_{Δ_G} = 0.169, σ_{s_D} = 5.581, σ_{s_G} = 5.180 (low signal-to-noise: filing choices driven by expected returns, p.29).
- **Decomposition estimates (pp.32–33; Table 6, p.51):** for actual 13D filings μ̂_D = 5.53%, μ̂_G = 0.77% → treatment 4.77% (**75.2%** of 6.34%), stock picking 0.77% (**12.2%**), selection 0.80% (**12.6%**). For 13G filings: μ̂_G = 0.64%, selection 0.04%. Hedge-fund subsample: treatment 92.4%, stock picking −4%, selection 11.6% (pp.6, 40).
- **Validation (§6.2, pp.34–37; Table 7, p.52):** Treatment and Stockpicking predict ΔROA and Δsales-turnover (subsuming CAR's information); Treatment negatively predicts proxy contests (Panel C).
- **Efficiency counterfactual (§6.3, pp.37–38):** the paper's only counterfactual policy exercise — **cost sharing**: "A striking 60% of Schedule 13G filings in the data satisfy μ_D − μ_G > 0" (p.38); shared cost → $35.6m per 13G filing, ≈ **$60bn/year** (p.38).

## 4. Cell-by-Cell Validation (Section 3 scope table + AFS column of overlap matrix)

### Section 3 table

| Cell | Verdict | Evidence |
|---|---|---|
| Type: "Structural MLE on the static binary 13D-vs-13G choice, joint with announcement returns" | **CONFIRMED** | §2 pp.8–15 (static binary choice), §3.2 p.18 (joint likelihood, MLE) |
| Headline decomposition: "6.34% ≈ 74.8% treatment + 13.4% stock-picking + 11.8% selection" | **NUANCED (version)** | This WP: **75.2 / 12.2 / 12.6** of 6.34% (abstract PDF p.5; p.3: 4.77% and 0.77% of 6.34%; pp.32–33; Table 6 p.51; Fig. 4 p.56). The 74.8/13.4/11.8 split is the published-JFE vintage. Substance (≈3/4 treatment, small stock-picking, ≈1/8 selection) confirmed; cite version-consistent numbers. |
| **The premium finding: "Activism LOWERS takeover bid premia 13.7% (5.2pp) vs no-activist counterfactual (verified)"** | **REFUTED — NOT IN THIS PAPER** | See §5 below. Zero occurrences of "takeover", "premia", "bid premium", "tender", "13.7", "5.2pp" in all 84 pages (visual read + decompressed-text sweep). No deal data, no premium variable, no takeover counterfactual. |
| Engagement cost: "Single constant scalar — no distribution estimated" | **CONFIRMED** | p.15 ("constant across all filings"); FOC eq. 13 p.20; C = 0.046 (Table 3 Panel B p.48); HF subsample 0.028–0.046 (Table A3) |
| Trading/price impact/stake: "Not modeled; stake exogenous" | **CONFIRMED** | fn.6 p.8 ("We take the stake size as given..."); price impact only as measurement contamination (event window choice, p.17); conclusion p.41 defers price-impact-aware accumulation to future research |
| First-mover claim: "Structural estimation of activism value creation (vs Gantchev 2013 cost-stages)" | **CONFIRMED** | p.7: "first to use structural estimation to quantify value creation in shareholder activism"; identification contrast with Gantchev (2013) spelled out p.7 |
| Differentiation one-liner ("their negative premium effect is our low-λ region...") | **BROKEN AS WRITTEN** | Premise (their negative premium effect) has no source in this paper; reword once the true source of −13.7%/5.2pp is located (see §5.4) |

### Overlap-matrix AFS column

| Object | Matrix says | Verdict |
|---|---|---|
| Structural estimation | ✓ | **CONFIRMED** (MLE, §3) |
| Takeovers/M&A in model | "premia as outcome" | **CORRECTED → ✗**. No takeovers anywhere in model or empirics. M&A appears only in cited literature (Greenwood-Schor 2009, Boyson et al. 2017, Jiang et al. 2018 in fn.4 p.7; Li-Taylor-Wang 2018 fn.5 p.7 and fn.18 p.38) |
| Trading/liquidity/price impact | ✗ | **CONFIRMED**, one nuance: Amihud illiquidity is a *covariate* loading positively on both μ_D and μ_G (0.021***/0.019***, Table 3 p.47), read as an Amihud illiquidity premium (p.27), with a nod that "stock market liquidity facilitates Schedule 13D or Schedule 13G filings (Collin-Dufresne and Fos, 2015, 2016)" (p.27). Liquidity is never a mechanism. |
| Disclosure rule as object | "13D-vs-13G choice" | **CONFIRMED**. The choice margin is the rule; window length/timing never a design object. The 10-day deadline appears once, descriptively, re exempt investors (p.24). |
| Premium wedge microfounded | ✗ | **CONFIRMED** (trivially — no premium object) |
| Engagement-cost distribution | "scalar only" | **CONFIRMED** (p.15, p.20) |
| Reputation dynamics | ✗ | **CONFIRMED**, with hook: past-filing experience variables are static reputation proxies and almost exclusively drive the treatment effect (pp.4, 26–27, Table 3); "past 13D filings serve as a signal of commitment that the activist will stick around after the price jump at announcement" (p.4) |
| 2024 acceleration anchor | ✗ | **CONFIRMED** (sample ends 2017; paper dated July 2020; no rule-change discussion) |

## 5. THE PREMIUM COUNTERFACTUAL — the load-bearing question

### 5.1 Finding: the claim is absent from this paper

The Section-3 scope-table cell and Prop d7:afs's anchor — *"AFS estimate that activism lowers takeover bid premia by 13.7% (5.2pp) relative to a no-activist counterfactual"* — **does not appear anywhere in this 84-page document.**

Forensic detail:

- Visual read of every page: no takeover, merger, acquisition, bid, offer-price, or deal-premium analysis; no SDC or deal-level data; no acquirer appears anywhere in the model or the data section. The outcome variable is exclusively the filing-event CAR over [t−30, t+10] (Table 1, p.44).
- Decompressed-PDF text sweep (all content streams): `takeover` 0 hits; `premia` 0; `tender` 0; `bid premi` 0; `13.7` 0; `5.2p`/`5.2 percentage` 0. The 7 hits on `premium` are: one "illiquidity premium as in Amihud (2002)" (p.27) and six "Market premium" rows (the FF3 market-factor regressor) in Tables 3/4/A1/A2/A6. `acquir` hits are incidental ("has acquired a stake," p.8; "acquiring a position," p.15) plus two reference titles; `merger` hits only the Boyson–Gantchev–Shivdasani reference (p.42).
- The paper's only counterfactuals are: (i) the per-filing counterfactual return μ_G for actual 13D filers (the stock-picking term, eq. 9 p.14, Table 6 p.51); (ii) the cost-sharing exercise (60% of 13G filings would flip to 13D; $60bn/yr, p.38). Neither involves takeovers or premia.

Consequently the four sub-questions posed for the counterfactual construction — (i) premium variable and baseline price, (ii) structural simulation vs regression coefficient, (iii) whether the baseline price capitalizes activism, (iv) deal sample and years — are **unanswerable from AFS: there is no premium variable, no premium counterfactual, no deal sample.** Nothing can be quoted because nothing exists.

### 5.2 What this means for Prop d7:afs

- The proposition's *mathematics* is untouched: M(π) = m̄(π)/P(π) decreasing in π for λ < λ_crit is an internal result of our model and needs nothing from AFS.
- The proposition's *framing and citation* are broken: §"Measured premia: rationalizing the Albuquerque–Fos–Schroth sign" (`D7_takeover_game_microfound.tex`, app:d7-afs) opens with "\citet{AlbuquerqueFosSchroth2022} estimate that activism *lowers* takeover bid premia by 13.7% (5.2pp) relative to a no-activist counterfactual." That sentence misattributes a finding to a paper that contains no such estimate (in this WP version, definitively). The same sentence pattern presumably appears wherever the draft motivates the proposition.
- The *denominator premise* of the proposition (bid premia measured against a market price that already capitalizes activism beliefs) is a statement about whoever actually measures activism-conditional premia — it cannot be checked against AFS because AFS measures no premium. Note, however, §7 below: AFS's announcement-return evidence directly supports the *capitalization* half of the premise.

### 5.3 Residual possibility: the published JFE version

The scope table's decomposition numbers (74.8/13.4/11.8) match the published JFE vintage, not this WP — so the deep-research journal was drawing on the published version. I cannot rule out from this PDF alone that the JFE 2022 text added a takeover-premium analysis, but it is highly implausible: it would require a new deal-level dataset and a different outcome variable in a published version of the same announcement-return decomposition paper, and the published abstract's counterfactual remains the cost-sharing exercise. **Action before any rewording: pull the published JFE PDF and run the same `takeover|premia|13.7` sweep.**

### 5.4 Where the −13.7%/5.2pp likely lives

Candidates to check, in order of plausibility (the number has the shape "5.2pp on a ≈38% mean premium ⇒ −13.7%"):

1. **Boyson, Gantchev & Shivdasani (JFE 2017), "Activism mergers"** — the canonical activism-target takeover-premium comparison; cited by AFS themselves (fn.4 p.7; refs p.42). Most likely true home of a "premia are lower in activism deals than matched non-activism deals" estimate.
2. **Greenwood & Schor (JFE 2009)** — activism targets and takeover outcomes (also cited fn.4).
3. **Celentano & Levine (2025)** — their structural model has a takeover margin and crowding-out counterfactuals; a model-based "premium absent activism" number could have been conflated with AFS in the verified-claim journal.
4. **Jiang, Li & Mei (JF 2018)** — jawboning in risk arbitrage (premium *increases*; unlikely source but adjacent).

Until the number is re-sourced, Prop d7:afs should cite "the empirical literature on activism-conditional takeover premia" generically or the verified true source — not AFS.

## 6. Checklist Answers

1. **Strategic-vs-financial acquirer mix (γ proxy):** **Not available.** No acquirers exist in the paper; no table splits acquirer types. γ cannot be indexed from AFS. (BGS 2017, which AFS cite, is where acquirer-type splits for activism targets live.)
2. **Cost-scalar identification:** single constant C (p.15). Pinned by the ML FOC (eq. 13, p.20): Ĉ "equates the average selection effect, i.e., the inverse Mills ratios, across all Schedule 13D and Schedule 13G filings weighted by their conditional variances"; intuition: higher Ĉ inferred from a lower proportion of 13D filings or a larger 13D−13G mean-return gap (pp.20–21; Figure 1, p.53). Estimate 4.6pp of stake value ≈ $2.43m (p.28).
3. **Premia offer-over-price or offer-over-preannouncement:** **N/A — no premia.** Their only price-based object is the filing CAR over [t−30, t+10], FF3-adjusted (p.17, Table 1 p.44), deliberately starting pre-filing to absorb the activist's own price impact.
4. **Model structure:** confirmed — static binary 13D-vs-13G choice with normal valuation gains, due-diligence signals, constant cost; joint MLE of filing choices and announcement returns (§§2–3). No dynamics (one-shot), no reputation state variable (experience enters x_i as a static covariate).
5. **Trading/price impact/stake choice:** none modeled. Stake exogenous (fn.6 p.8). Price impact acknowledged only in event-window design (p.17) and in the C-discussion of accumulation costs (p.15). Conclusion p.41 explicitly lists pre-5% price-impact-aware trading as future research.
6. **Citations to our lineage:** **Back, Collin-Dufresne, Fos, Li & Ljungqvist (Econometrica 2018) — cited** (fn.6 p.8, refs p.42) precisely as the model of activist trading vs liquidity they abstract from. **Collin-Dufresne & Fos 2015 (JF), 2016 (Econometrica) — cited** (pp.17, 27). **Edmans, Fang & Zur 2013 — cited** (fn.2 p.2, p.27: liquidity-and-13D/13G evidence; they note their illiquidity result *contrasts* with EFZ for 13G hedge-fund filings). **Maug (1998): NOT cited. Kahn–Winton (1998): NOT cited. Grossman–Hart (1980): NOT cited.** Full reference list pp.42–43.
7. **Disclosure rules / 13D window as policy:** not modeled, never discussed as a design margin. The 10-day deadline appears once descriptively (exempt 13G investors, p.24); Giglia (2016) on 13D/13G misuse cited fn.2 p.2. No mention of any window-length change (sample ends 2017).

## 7. Engagement Points (3 sharpest)

1. **AFS quantify our denominator channel — cite them FOR Prop d7:afs's mechanism, not for the premium fact.** Their entire measurement object is the price's capitalization of activism news at disclosure: 6.34% on 13D filings, 75.2% of it treatment (anticipated value creation), validated as informative about future fundamentals (Table 7). That is direct evidence that P(π) jumps with activism evidence — exactly the P′(π) > 0 input our measured-premium reversal needs. The corrected engagement line: *any* takeover premium measured against a post-13D market price has an activism-inflated denominator of the magnitude AFS estimate.
2. **The white space survives verbatim, in their own words.** Cost is a single constant pinned by one aggregate moment (p.15, eq. 13 p.20), and their conclusion names our agenda: "The costs of activism or the precision of due diligence may vary across investors or target firms. Investors may take into account the price impact of their trading before crossing the 5% ownership threshold. We leave these extensions for future research" (p.41). Our engagement-cost-distribution leg and κ-microstructure engine are literally their declared open margins; fn.6 (p.8) defers the trading margin to Back et al. (2018) — the lineage we extend with disclosure design.
3. **Their liquidity covariate is a hook, not a threat.** Illiquidity raises expected returns to *both* filing types equally (Table 3: 0.021/0.019) — in their static frame liquidity is compensation, not a mechanism; they flag the unresolved contrast with Edmans-Fang-Zur (p.27, §5.4). Our model supplies the missing mechanism (κ moves the exit/voice composition and the information content of prices), predicting *when* liquidity helps vs hurts activism — a comparative static their estimates can neither generate nor index.

**Plus the correction (must-do before M1):** the planned differentiation one-liner ("their negative premium effect is our low-λ region; we predict where their estimate should flip sign") cannot ship against AFS. Re-target it at the true source of the −13.7%/5.2pp estimate once located (lead candidate: Boyson–Gantchev–Shivdasani 2017), and verify that source's premium baseline (offer over pre-*campaign* vs pre-*offer* price) actually has the activism-capitalized denominator our Prop d7:afs requires. If the true source's denominator is a pre-campaign (pre-13D) price, the denominator channel is muted there and the rationalization must lean on the deterrence/composition channels (Remark d7:afs-comp) instead.

## 8. Threats

- **Competitive threat from AFS to our paper: LOW.** No trading, no liquidity mechanism, no disclosure design, no takeovers, no premium object, scalar cost. They hold the value-creation-decomposition high ground (first structural estimation, p.7) and nothing else we claim.
- **Internal threat: HIGH severity, contained scope.** The 2026-06-10 verified-claim journal (3-vote adversarial verification, "0 refuted") passed a fabricated/misattributed load-bearing claim: the AFS takeover-premium counterfactual. Infected artifacts: scope table §3 (premium row + differentiation one-liner + overlap-matrix "premia as outcome" cell), `quality_reports/fixes/D7_takeover_game_microfound.tex` §app:d7-afs opening sentence and Remark d7:afs-comp's "testable against AFS" framing, and any draft_v2.tex text spliced from D7 that names AFS for the −13.7% figure. The verification pipeline should be re-audited for the other 62 claims, starting with any that anchor propositions.
- **Risk to Prop d7:afs itself: the theory stands; the empirical anchor is currently dangling.** Worst case after re-sourcing: if the true premium study measures offers against pre-campaign prices (denominator not capitalizing activism), the price-channel rationalization loses its bite for that study and the proposition's motivation must be rewritten around composition/deterrence — flagged loudly per the task brief.

## 9. Quotable Sentences (page-anchored, WP pagination)

1. "We take the stake size as given and focus on the activist's choice to be an active or a passive investor." — fn.6, p.8
2. "We assume that C is constant across all filings in the data." — p.15
3. "The cost Ĉ equates the average selection effect, i.e., the inverse Mills ratios, across all Schedule 13D and Schedule 13G filings weighted by their conditional variances." — p.20
4. "We find that the average treatment effect of activism... represents 75.2% of the observed Schedule 13D announcement return, that is, 4.77% of 6.34%." — p.3
5. "We begin the event window 30 days before the filing because Collin-Dufresne and Fos (2015) show that price appreciation prior to Schedule 13D filings likely reflects the price impact of activist's trades." — p.17
6. "Finally, our paper is the first to use structural estimation to quantify value creation in shareholder activism." — p.7
7. "A striking 60% of Schedule 13G filings in the data satisfy μ_D − μ_G > 0." — p.38
8. "past 13D filings serve as a signal of commitment that the activist will stick around after the price jump at announcement." — p.4
9. "investments in less liquid securities appear to be compensated by higher expected returns regardless of the filing schedule, consistent with an illiquidity premium as in Amihud (2002)." — p.27
10. "Investors may take into account the price impact of their trading before crossing the 5% ownership threshold. We leave these extensions for future research." — p.41
