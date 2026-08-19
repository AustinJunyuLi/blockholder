# Becht, Franks, Grant & Wagner (2017) — "Returns to Hedge Fund Activism: An International Study"

**Venue / status:** *Review of Financial Studies* 30(9), 2933–2971, 2017, doi:10.1093/rfs/hhx048, Advance Access 20 June 2017; received 3 March 2015, editorial decision 21 December 2016 by Editor Andrew Karolyi; **Open Access (CC BY-NC)** — **PRIMARY for all page cites**. Working-paper version also read: ECGI Finance WP N° 402/2014, dated May 2017 (accepted manuscript; title page reads "Review of Financial Studies, forthcoming / 27 May 2014 / Revised 15 September 2016"), 59 PDF pages. §§1–8 below were written from the WP; §9b records the re-basing onto the published article. **Cite the RFS pages (2933–2971) in draft_v3.**
**Full text from:** published — `research/txt_extracts/becht_2017_rfs_published.pdf` (39 PDF pp.) / `.txt`; **Internet Appendix — `research/txt_extracts/becht_2017_internet_appendix.pdf` (17 pp.) / `.txt`, now IN HAND**; WP — `research/txt_extracts/becht_etal_2017_full.pdf` (59 pp.) · **Reader:** opus, opus (published-version + Internet Appendix supplement) · **Read:** published article end to end (body, Figures 1–3, Tables 1–9) and the full Internet Appendix (Appendices A1–A10, its Tables 1–8 + "Table 18", Figure 4, country case studies)
**Page numbering used below:** §§1–8 cite the **WP's PDF page index** (manuscript printed page = PDF page − 5). §9b gives the **published** RFS page for every one of them. Published RFS page = published PDF page + 2932 (PDF p. 1 = RFS p. 2933). Internet-Appendix cites are given as "IA p. N" (its own PDF page).
**Type:** empirical (event study + panel/probit, cross-country)   **Role for us:** competitor (nearest to a *cross-country disclosure-threshold* fact) + measurement (takeover-outcome CARs)

## 1. Question

How do patterns of ownership and national institutional arrangements shape the *incidence* and *performance* of hedge fund activism? The paper is billed as "the first comparative study of publicly observable activism across 23 countries in Asia, Europe, and North America" (PDF p. 6). Two questions carry the paper: (i) what makes a firm a target, across countries; (ii) what makes an engagement pay — and the answer to (ii) is that returns exist **if and only if the activist achieves an observable outcome**, with takeovers the most valuable outcome of all.

## 2. Model / data and method

**Sample.** **1,740 publicly disclosed hedge fund activist engagements** in publicly traded firms, **23 countries**, initiated **1 January 2000 – 31 December 2010**, covering **1,534 unique target companies** and **330 activist funds**. Hand-collected for Asia, Europe and Canada; for the United States they rely on **13D Monitor**, a commercial provider (PDF p. 10). Distribution: US 1,125, Japan 184, UK 165 (85% in three countries); by region Asia 214, Europe 381, North America 1,145.

**Other data.** FactSet Ownership (Lionshares) for institutional holdings, split domestic / foreign-US / foreign-non-US following Ferreira–Matos (2008); FactSet Fundamentals for financials; **CRSP for US and Datastream for non-US** daily prices and volume; SDC Platinum for unsolicited bids and for third-party takeover verification; World Bank for listed-firm counts and Rule of Law; Djankov et al. (2008) for Common Law and revised anti-director rights; Aggarwal et al. (2009) for the G44 governance index. **Country-level minimum regulatory disclosure thresholds for blockholders, as of the year 2000, are hand-assembled and enter as a right-hand-side variable** (Tables 1 and 9).

**Designs.**
1. *Targeting probit* (Table 4): dependent = firm engaged by an activist in year t (1/0), across 45 countries / 25,018 firms / 114,978 firm-years per the table note — the Observations row of Table 4 col. 1 prints **114,987**, an internal inconsistency [flagged by verifier] — (90,470 with Illiquidity non-missing); "Only activist markets" subsample = 13 countries / 13,479 firms / 68,157 firm-years. Marginal effects reported; year FE always, country FE in column 4; White heteroscedasticity-robust SEs.
2. *Event study on block disclosure* (Table 5): market-model CARs, **country-specific** market models, loadings over 250 trading days pre-window with ≥150 observations; windows (−10,10) and (−20,20); **1,617 of 1,740** disclosures have sufficient data; winsorised at 1/99.
3. *Event study on engagement outcomes* (Table 7): CARs around the earliest outcome announcement; outcomes coded as **Board / Payout / Restructuring / Takeover**, plus **Multiple+Takeover** and **Multiple+NoTakeover**; 850 of 1,740 engagements have ≥1 outcome and sufficient data.
4. *Calendar-time portfolios, disclosure to exit* (Table 8): monthly, n=132 months; equal- and value-weighted; alphas from a market model and from Fama–French–Carhart four factors **built on US stocks**; portfolios of engagements-with-outcomes, engagements-without-outcomes, and a long/short; plus a decomposition into "only month t=0", "only months with outcome announcements", and "all other months".
5. *Country-characteristics regressions* (Table 9): OLS on disclosure CAR and on outcome CAR, probit on firm-engaged, GLM (Papke–Wooldridge fractional) on the country-year fraction of firms engaged.

**Identification.** Cross-sectional and cross-country **association only**. There is no shock, no DiD, no instrument, no policy change. Disclosure thresholds are *levels as of 2000*, not changes.

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where (page / prop / table) |
|---|---|---|---|
| R1 | Block-disclosure CAR (−20,20): full **6.40%*** (SE 0.486)**, N=1,617; North America **7.00%*** (0.641)**, N=1,027; Asia **6.43%*** (1.238)**, N=213; Europe **4.75%*** (0.898)**, N=377 | ESTIMATED (SE) | PDF p. 49, Table 5 Panel A |
| R2 | Outcome-announcement CAR (−20,20), all outcomes **6.42%*** (0.78)**, N=850 | ESTIMATED (SE) | PDF p. 52, Table 7 Panel A |
| R3 | **CAR by outcome type (−20,20):** Takeover **9.73%*** (1.33)**, N=187; **Multiple+Takeover 18.1%*** (4.20)**, N=58; Multiple+NoTakeover **9.04%*** (2.95)**, N=81; Restructuring **5.60%*** (1.92)**, N=118; Board **4.48%*** (1.45)**, N=272; **Payout −0.16% (1.54), N=134 — indistinguishable from zero** | ESTIMATED (SE) | PDF p. 52, Table 7 Panel A |
| R4 | **CAR by outcome × region (−20,20).** Europe: all **8.77%*** (1.74)**, takeover **10.8%*** (2.25)**, Multiple+Takeover **25.1%** (9.45)**. North America: all **5.97%*** (0.90)**, takeover **9.54%*** (1.64)**, Multiple+Takeover **16.2%*** (4.76)**. **Asia: all outcomes 2.72 (3.48) — insignificant, and every Asian category insignificant at (−20,20)** | ESTIMATED (SE) | PDF p. 52, Table 7 Panel B |
| R5 | **Share of the return story carried by takeovers:** of the 850 outcome engagements, **187 are pure takeovers and 58 are multiple-with-takeover (245, ≈29%)**, and those two categories carry the two largest CARs in every region where they are estimable. Takeover-linked outcomes are the *only* category above 9% | ESTIMATED (counts + CARs) | PDF p. 52, Table 7 Panels A–B |
| R6 | Outcome incidence: unconditional P(≥1 outcome) = **53%**; North America **61%**, Europe **50%**, Asia **18%** | ESTIMATED (rates) | PDF p. 7 |
| R7 | Disclosure CAR is higher for engagements that later succeed: **7.9%** with outcomes vs **4.7%** without, (−20,20), difference significant at 1% | ESTIMATED (difference test) | PDF p. 25 |
| R8 | **Total engagement alpha depends entirely on outcomes.** EW annualised Carhart alpha: with outcomes **1.104 (3.407)**, without outcomes **−9.750*** (3.608)**, long/short **10.854*** (4.078)**. VW Carhart: with outcomes **7.987** (3.340)**, without **2.325 (5.379)**, L/S **5.662 (6.140)**. EW MktModel with outcomes **8.399** (4.119)**; VW MktModel with outcomes **11.254*** (3.473)** | ESTIMATED (SE) | PDF p. 54, Table 8 Panel A |
| R9 | Decomposition of the engagement window: annualised alpha in the **disclosure month** 14.2%–18.9%, in **outcome-announcement months** 26.4%–28.2%; in **all other months** the equal-weighted alphas are zero-to-negative (EW Carhart **−6.670\*\*** with outcomes, **−11.677\*\*\*** without) **but the value-weighted market-model alpha for engagements with outcomes is +5.842\*\* [2.917], significantly positive** [corrected by verifier — the card, and the paper's own p. 33 text, asserted "no significant abnormal returns … positive or negative" in these months; Table 8 Panel B contradicts that in both directions] | ESTIMATED (SE) | PDF p. 55, Table 8 Panel B (text PDF p. 33) |
| R10 | **Country disclosure threshold is negatively related to activism incidence:** firm-level probit marginal effect **−0.007*** (0.001)**, N=89,515; country-year GLM **−0.279*** (0.060)**, N=402. Lower threshold ⇒ more activism | ESTIMATED (SE) | PDF p. 56, Table 9, cols. 8 and 11 |
| R11 | **Disclosure threshold is NOT related to returns:** on engagement-disclosure CAR the coefficient is **1.797* (0.972)** (only 10%, adj. R² = −0.012, N=721); on outcome-disclosure CAR **−0.684 (0.878)**, insignificant | ESTIMATED (SE) | PDF p. 56, Table 9, cols. 2 and 5 |
| R12 | **Illiquidity lowers the probability of being engaged:** probit marginal effects **−0.038*** (0.006)** (all countries), **−0.031*** (0.007)** (activist markets), and **−0.013 (0.008), insignificant, once country fixed effects are added.** Illiquidity = share of zero-return days per year | ESTIMATED (SE) | PDF pp. 48, Table 4, cols. 2–4 |
| R13 | Around disclosure, abnormal share turnover "increases by more than 80% over normal turnover prior to the event period" | ASSERTED (figure-based, no SE) | PDF p. 22, Figure 2 (PDF p. 43) |
| R14 | Wolf packs: **378 engagements (21.7%)**, 172 target firms (11.8%); aggregate stake **13.4%** vs **8.0%** stand-alone; disclosure CAR (−20,20) **13.82% (2.33)** vs **6.32% (0.63)**, difference **−7.50\*\*\* (1.93)**; effect survives controlling for stake size (wolf-pack dummy **6.39\*\*\* (2.04)**) | ESTIMATED (SE) | PDF p. 47 Table 3A (counts); PDF p. 23 text (the 13.4/8.0 stakes are "unreported in the table"); PDF pp. 49–50, Table 5 Panels C–D. **Note:** PDF p. 15 gives the same comparison as "13.4% versus 8.3%" — the paper prints two different stand-alone figures [added by verifier] |
| R15 | Wolf packs raise the *probability* of outcomes, not the CAR per outcome: P(any outcome) **78%** vs **46%** (t = −8.11); P(takeover) 15% vs 11% (t = −1.59, insignificant); outcome CARs statistically indistinguishable | ESTIMATED (t) | PDF p. 53, Table 7 Panel D |
| R16 | Domestic beats foreign: disclosure CAR (−20,20) domestic non-US **7.34*** (1.44)**, domestic US **6.94*** (0.65)**, foreign non-US **4.27*** (1.12)**, foreign US **4.87*** (1.10)**; difference t = **2.21**** | ESTIMATED (SE, t) | PDF p. 50, Table 5 Panel E |
| R17 | Institutional ownership drives targeting, with **foreign-US** ownership the strongest: marginal effects **0.063***/0.110***/0.180***/0.209*** (US foreign) vs **0.037***–0.049*** (domestic) across the four columns | ESTIMATED (SE) | PDF p. 48, Table 4 |
| R18 | Average activist stake **11%** across countries (US 11%, Japan 13%, UK 13%) — activists cannot act alone | ESTIMATED (means) | PDF pp. 16, 45, Table 1 |
| R19 | Governance changes *precede* takeovers in multi-outcome engagements: mean engagement length 806 days; board changes announced at 36% of the way, payout 48%, restructuring 44%, takeover **76%**; t-tests vs takeover −8.25***, −4.32***, −4.71*** | ESTIMATED (t) | PDF p. 52, Table 7 Panel C |
| R20 | Activism vs unsolicited bids per 1,000 listed firms: Asia 3.2 vs 0.5, Europe 3.4 vs 2.1, North America 11.7 vs 4.6 — activism exceeds unsolicited bids **in every region, but not in every country**: Canada 0.6 vs 3.3, Norway 3.6 vs 4.8 and Spain 0.2 vs 0.6 run the other way [qualified by verifier] | ESTIMATED (counts/rates) | PDF p. 46, Table 2 |
| R21 | Country characteristics: activism more likely where **rule of law is strong** (probit 0.022\*\*\*), **thresholds are low** (R10), the system is **not Common Law** (−0.020\*\*\*). "Governance is weak" is the paper's wording (PDF p. 35) but holds **only in the country-year GLM** (Quality of governance −5.488\*\*\*, col. 12); in the firm-level probit the same coefficient is **−0.031, insignificant** (col. 9) [qualified by verifier] | ESTIMATED (SE) | PDF p. 56, Table 9 |

## 4. Institutional facts used

- **Cross-country threshold margin — the central institutional fact of the paper.** "all jurisdictions in our sample require shareholders to disclose when stakes reach a minimum threshold. We report disclosure thresholds as of the year 2000, and in the vast majority of countries, this threshold is 5% of capital and/or voting rights, depending on the type of security. Germany, Italy, Switzerland and the United Kingdom have lower thresholds of 2% or 3%, while Canada is the only country with a higher threshold of 10%." (PDF p. 13). Table 1 (PDF p. 45) prints the threshold country by country: **Italy 0.02; Germany, Switzerland, UK 0.03; Canada 0.10; all others 0.05.**
- **Threshold heterogeneity is treated as a *nuisance* to be neutralised, not a source of identification.** Footnote 5: "we exclude engagements where the initial activist stake is below 5% from our analysis. This excludes 273 out of 1,740 engagements in our sample. All of our performance results in later tables obtain for this smaller sample." (PDF p. 13).
- **No US filing window is ever discussed.** The ten-business-day 13D deadline is not mentioned; Schedule 13D appears only twice, once as the source of stated purpose in the US ("while activists engaging U.S.-listed firms need to provide information on the stated purpose of their investment in Schedule 13D filings, no exact equivalent exists elsewhere", PDF p. 7) and once as the data vendor 13D Monitor (PDF p. 10).
- **Group/concert-party rules** (Section 13(d)(3) of the 1934 Act) are used to define wolf packs, quoting Coffee–Palia (2016): a wolf pack is "a loose network of activist investors that act in a parallel fashion, but deliberately avoid forming a "group" under Section 13(d)(3) of the Securities Exchange Act of 1934." (PDF p. 14). Footnote 7 (PDF p. 15) compares UK / US / Germany market-abuse and insider constraints on pack formation.
- **Stake ceilings other than the disclosure threshold** are what actually cap the activist's stake: US poison-pill triggers and Section 16(b) short-swing rules cap at ~10%; the **EU Takeover Directive (2004/25/EC) mandatory bid** typically triggers at 30–33% of voting rights; Japanese poison-pill-style triggers (PDF p. 16, fn. 8). Aderans example: a 24.6% stake was "just below Aderans' 30% poison pill threshold" (PDF p. 18, fn. 9).
- **Special-meeting / board-nomination rights** vary from 5% to 20% of capital across countries, with Delaware an exception where shareholders generally cannot call an EGM but can launch a proxy fight (PDF p. 19).
- **(added by verifier) Where activism happens is where the takeover market is not.** "After the United States, among large economies activism is relatively most frequent in Italy, the Netherlands, Germany and Switzerland (in declining order), none of which are typically labeled as having active markets for corporate control" (PDF p. 13). Italy, Germany and Switzerland are exactly the 2–3% threshold countries in Table 1. The mirror image sits in Table 2: **Canada, the only 10%-threshold country in the sample, has the lowest activism rate of any activist market (0.6 per 1,000 listed firms) and *more* unsolicited bids than activist engagements (3.3 vs 0.6)** — the only North American country where the hostile-bid channel out-runs the activism channel, and by five to one.
- **(added by verifier) The disclosure threshold literally partitions a wolf pack, and they show it.** In the 2005 Deutsche Börse case, of the funds in the pack **three had "publicly observable stakes above the disclosure threshold" (TCI, Atticus, Och-Ziff) and eight "at the time did not disclose their holdings"** (Harris, Seneca, Jana, Lone Pine, Third Point, RIT, Alta, Parvus), alongside Capital Group, Fidelity, Generali and Merrill Lynch; "Combined, these investors owned 59% of the voting rights" (PDF p. 14). Bafin investigated and did not find a group. This is the cleanest institutional illustration in the competitor set that the threshold determines *who is visible*, not who is present.
- **(added by verifier) A three-step disclosure event study, buried in footnote 6 (PDF pp. 14–15).** At Atos Origin (France, 2006–07): "Centaurus disclosed a 5.5% stake in October 2006, followed by Pardus with a 7.3% stake in August 2007. In October 2006, the two funds notified a concert party with a joint stake of 19.4%. The market reaction to the disclosures was 7.8% for Centaurus, 1.7% for Pardus, and a further 5.5% for the joint stake." Three separate disclosure events on one firm, each priced — the price impact of *crossing the flag* measured three times in a footnote.
- **(added by verifier) Target float composition (Table 1, PDF p. 45).** For the FactSet subsample, US targets have a **median 0.77 of shares held by institutions against a 0.43 median for the FactSet US firm population**; Japanese targets 0.07 vs 0.04. Targets are drawn from the institutionally-held end of the distribution everywhere, which is the ownership-structure counterpart of the liquidity margin.
- **Illiquidity measure:** "number of zero daily returns per year divided by the number of available daily returns per year, minimum of 200 available daily returns per year" (PDF p. 48, Table 4 notes) — a zero-return (Lesmond-type) measure, **not** Amihud.
- Third-party takeover check: SDC used to verify all 1,740 engagements; 21 takeover outcomes (15 US) may be attributable to a third party rather than the activist; dropping them leaves conclusions "materially unaltered" (PDF p. 24, fn. 13).

## 5. Referee-facing strengths / weaknesses

**Strengths.**
- The only large-sample dataset that puts **statutory disclosure thresholds of 2%, 3%, 5% and 10% side by side** with activism incidence and returns, and actually estimates the relationship (R10, R11).
- The outcome taxonomy is disciplined — it comes from the internal classification used by one of the largest funds in the sample (Becht et al. 2009) — and is applied identically across 23 jurisdictions, which is what makes the cross-country CAR comparison legitimate.
- The engagement-window decomposition (R9) is the closest thing in the literature to evidence that activist alpha is concentrated in the disclosure month and the outcome months. **[Verifier qualification: it is not as clean as either the card or the paper claimed.** Their own summary — "in months after the block disclosure and excluding the outcome disclosure month(s), there are no significant abnormal returns generated by the activist, positive or negative" (PDF p. 33) — is contradicted by their own Table 8 Panel B in *both* directions: the EW Carhart alpha in "all other months" is −6.670\*\* (and −11.677\*\*\* for no-outcome engagements), and the VW market-model alpha for engagements with outcomes is +5.842\*\*. The honest version is: the disclosure month and outcome months are large and robust; the in-between months are specification-dependent and not zero.**]
- Country-specific market models and country-specific factor discussions; results shown under both a market model and Carhart, EW and VW, by region — hard to accuse them of cherry-picking a specification.
- They test and reject a mechanical explanation of the wolf-pack effect (larger aggregate stake) by residualising the pack dummy on the stake.
- Honest about their own null: country characteristics predict *whether* activism happens but not *how well it does* (R11, and Q10 below). **[Verifier qualification: the null is stated more strongly in the text than Table 9 supports.** PDF p. 34 says of the disclosure-CAR columns "none of the country-level measures are statistically significant" — but col. 1 carries Market cap/GDP 0.039\* and col. 2 carries Disclosure threshold 1.797\*. Of the outcome-CAR columns it says "neither institutional ownership nor country-level characteristics have meaningful explanatory power" — but col. 4 carries Rule of law 7.186\*\*, col. 5 Common law 4.242\* and IO_Foreign_U.S. 45.681\*, col. 6 Board structure 10.649\*\*, IO_Foreign_U.S. 48.629\* and IO_Foreign Non-U.S. 26.282\*. Several 5%- and 10%-level results are described as nothing. If we cite Q10 as "their own null", we must cite the table alongside it, or a referee who opens Table 9 will catch us.**]
- **(added by verifier) Their own explanation for the disclosure-CAR null is a selection argument we can borrow — and must answer.** "The lack of significance is not too surprising, since disclosure abnormal returns are conditional on the activist choosing to go ahead with an engagement. For example, since activists will have considered institutional ownership in picking targets, targets should have conditionally optimal institutional ownership; ownership would then appear unrelated to announcement returns" (PDF p. 34). The same argument applies word-for-word to *liquidity*: if activists select targets on κ, κ will look unrelated to announcement returns in a sample of realised engagements. That is simultaneously a defence of a null we might otherwise fear and a warning that a cross-sectional liquidity–CAR regression cannot test our mechanism.

**Weaknesses / open flanks.**
- **No identification.** Every relationship is a cross-sectional or cross-country partial correlation. Disclosure thresholds are country fixtures as of 2000, perfectly collinear with everything else about a country's legal system; the threshold coefficient in the probit (R10) is not separable from Common Law, governance quality, or anything else on the country level. They say so themselves about the return regressions but not about the incidence regressions.
- **The threshold result is fragile in the direction that matters to us.** In the returns regressions the threshold coefficient is significant only at 10% and the **adjusted R² is negative (−0.012)**; in the incidence regressions it is highly significant but the design is a country-level cross-section with 402–440 observations.
- **The liquidity result does not survive country fixed effects** (R12: −0.013, SE 0.008). Whether liquidity attracts activists *within* a country is therefore left open by this paper.
- **US data are vendor-supplied (13D Monitor) while non-US data are hand-collected** from news searches. The two arms of the comparison have different measurement error, and the paper's central contrast is US-vs-rest.
- **Outcomes are read from "non-standardized news reports"** outside the US. Asia's 18% outcome rate could be a detection failure as easily as an economic fact — and Asia is exactly where the paper's most striking claim (high disclosure returns, no outcomes) sits.
- **Selection on observable disclosure.** Engagements enter only if a stake was publicly disclosed; sub-threshold and private activism are structurally absent (their footnote 2, quoted below).
- Factor portfolios in *all* alpha regressions are **US-based**, applied to Japanese and European portfolios; the regional-market-model alternative is mentioned but "omitted for brevity".
- Several key robustness results live only in an **Internet Appendix not present in this file** (Tables 11, 15, 17, 18, Figure A4).
- Sample ends in **2010**; the modern activism wave, and every 21st-century disclosure-rule change including 2024-02-05, are out of period.

## 6. What they do NOT do (scope boundary)

- **Object.** The objects are (i) the *probability of being engaged*, (ii) *announcement CARs* at block disclosure and at outcome disclosure, and (iii) *calendar-time alpha over the engagement*. **The takeover premium is never measured.** The word "premium"/"premia" does not appear in the paper. Takeover enters as a **binary outcome category** whose announcement CAR is estimated (9.73% at (−20,20)) — that CAR is a target-shareholder announcement return over a 41-day window, *not* a bid premium over an unaffected price, and it must not be reported as one. **Bidder entry is never modelled**; they observe realised takeover announcements only.
- **Margin.** They use the **threshold margin only, and only as a cross-sectional level**, never as a change. They use **no filing-window margin at all** — the window is not mentioned, in any country. And they deliberately *neutralise* the threshold variation rather than exploit it (footnote 5, Q2 below): the below-5% engagements are dropped to make countries comparable. That is precisely the opposite of using the margin for identification, and it is the clearest statement in the competitor set that this margin is open ground.
- **Identification.** Event study + probit/OLS/GLM association. **No structural model, no DiD, no instrument, no natural experiment, no rule change.** They stop short of causal language: country characteristics "correlate", outcomes "contribute to" returns.
- **Liquidity is a control, not an object.** Illiquidity appears in Tables 4 and 9 as one of a dozen firm covariates, is never interacted with anything, is never used to explain returns, and loses significance under country FE. There is no liquidity–activism mechanism in the paper and no reference to Maug/Kyle–Vila/Back.
- **Private activism is explicitly out of scope** (footnote 2, Q7 below) and they say the data to study it are "currently not available to us" (PDF p. 27, fn. 15).
- **Causality of the wolf-pack effect is explicitly disclaimed**: "we cannot distinguish whether the superior performance is due to active coordination amongst the hedge funds or simply the congregation of like-minded investors" (PDF p. 10).

## 7. Implications for our position

1. **This is the competitor closest to our threshold margin, and it hands us the margin without taking it.** They assemble the country-by-country statutory threshold (2% Italy, 3% Germany/Switzerland/UK, 5% most, 10% Canada), estimate that **lower thresholds go with more activism** (R10), find **no relationship between thresholds and returns** (R11) — and then, in footnote 5, *drop* the 273 sub-5% engagements to make the countries comparable. That footnote is the single most useful sentence in the paper for us: the leading international study treats threshold variation as contamination to be removed. Occupying it deliberately is whitespace.
2. **They give us the empirical shape our "control outcome" variable should take, and its ceiling.** Their outcome taxonomy (Board / Payout / Restructuring / Takeover) is broader than "takeover premium" and matches CONTEXT.md's broadened *control outcome*. R3 says the ordering is Takeover (9.7%) > Restructuring (5.6%) > Board (4.5%) > Payout (≈0), and that **takeover preceded by governance change is worth double a bare takeover (18.1% vs 9.7%)**. If our premium wedge m₁ − m₀ is meant to be an engaged-vs-unengaged gap in expected takeover value, R3/R4 is the closest published magnitude — but as an announcement CAR, not a premium. Any calibration must say so.
3. **They pin down what a disclosure return *is* in the data: the market pricing the probability of a control outcome.** R7 (7.9% with outcomes vs 4.7% without) plus R9 (alpha exists only in the disclosure month and the outcome months) is exactly a partition story: the flag arrives, the market re-prices the odds of control changing hands, and nothing happens in between. This is direct support for building the model around the *flagged/pooled partition* rather than around continuous information revelation.
4. **Their liquidity result is a warning, not an ally.** R12: illiquidity predicts fewer engagements, but the effect dies under country fixed effects. If our empirical leg claims a liquidity–control-outcome link, we cannot lean on Becht et al. — the honest reading is that they found a cross-country correlation that does not survive within-country. This raises the bar on our own liquidity measurement (and points at Fos 2017, whose within-US Amihud result does hold).
5. **They constrain our takeover claim through Greenwood–Schor.** R19 (board change at 36% of the engagement, takeover at 76%) plus the "qualifies Greenwood and Schor" passage (Q5) says: activists do not merely pick firms that were going to be bought; the governance action comes first and plausibly *makes* the firm buyable. That is a bidder-entry mechanism stated in the data, and it is friendly to a model where engagement shifts the takeover distribution rather than just selecting on it. But it is association, not identification — they are careful, and we should be too.
6. **(added by verifier) The raw threshold-vs-control-channel pattern is already in their Tables 1 and 2 — they print it and do not read it.** Rank their activist markets by statutory threshold and look at Table 2: Italy (2%) 13.3 activist engagements per 1,000 listed firms against 1.6 unsolicited bids; Germany (3%) 7.3 vs 1.1; Switzerland (3%) 6.6 vs 4.9; UK (3%) 6.0 vs 4.1; US (5%) 19.6 vs 5.8; **Canada (10%) 0.6 vs 3.3 — the one country in the sample where the hostile-bid channel dominates the activism channel**. Their own p. 13 sentence supplies the interpretation: the high-activism countries are the ones "none of which are typically labeled as having active markets for corporate control". This is *exactly* our object (control outcomes), our margin (threshold level) and their data — presented as descriptive colour and never regressed. It is not identification (five threshold values, twenty-odd countries, everything collinear with the legal system), so it cannot be our evidence; but it is the strongest available motivating fact, and it is a live referee question we should answer before it is asked.
7. **Position summary of the cell they occupy:** object = announcement CARs and engagement alpha (not premium, not bidder entry); margin = **threshold level, cross-sectional, and explicitly neutralised**; identification = **cross-country association, no shock**; liquidity = control variable only, insignificant with country FE. The cell "liquidity × *window* margin × takeover premium, with a dated rule change" is untouched by them on all three axes.

## 8. Quotes we may lean on (verbatim, page-cited)

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "Third, all jurisdictions in our sample require shareholders to disclose when stakes reach a minimum threshold. We report disclosure thresholds as of the year 2000, and in the vast majority of countries, this threshold is 5% of capital and/or voting rights, depending on the type of security. Germany, Italy, Switzerland and the United Kingdom have lower thresholds of 2% or 3%, while Canada is the only country with a higher threshold of 10%." | PDF p. 13 (printed 8) | **Threshold margin by country — the institutional fact** |
| Q2 | "To address the potential concern that cross-country differences in disclosure thresholds might create some type of bias in our results, we exclude engagements where the initial activist stake is below 5% from our analysis. This excludes 273 out of 1,740 engagements in our sample. All of our performance results in later tables obtain for this smaller sample." | PDF p. 13 (printed 8), fn. 5 | **They neutralise the threshold margin rather than identify off it — our whitespace, in their words** |
| Q3 | "Further, activism is more frequent in those developed countries (e.g., France, Germany, and Italy) in which minimum regulatory disclosure thresholds for blockholders are low, the legal system is different from Common Law, and governance is relatively weak." | PDF p. 35 (printed 30) | Threshold level ↔ activism incidence |
| Q4 | "The differences are striking, particularly engagements with multiple outcomes that involve a takeover have abnormal returns of 18.1%, whereas those engagements with only the outcome of a takeover have abnormal returns of roughly half that size (9.7%)." | PDF pp. 7–8 (printed 2–3) — the sentence straddles the page break [page corrected by verifier] | **Takeover CAR, and the governance-then-takeover premium on it** |
| Q5 | "This evidence qualifies the results by Greenwood and Schor (2009) who provide evidence that a large proportion of activist returns are the result of "putting companies into play"; our evidence suggests that while activists might be good at picking likely takeover candidates, their other actions might also influence the probability of takeover, in particular since the other actions usually precedes the takeover bid." | PDF p. 26 (printed 21) | Engagement shifts takeover probability, not just selects on it |
| Q6 | "For the entire sample, the unconditional probability of an activist being successful in achieving at least one engagement outcome is 53%. However, the incidence of outcomes varies considerably across countries. In North America activists achieve outcomes in 61% of all engagements and 50% in Europe, but only 18% in Asia." | PDF p. 7 (printed 2) | Country/regime differences in control outcomes |
| Q7 | "What we cannot capture is private activism, that is, activism that is disclosed to the target firm, but not to the wider public and because of smaller stakes is not subject to regulatory disclosure." | PDF p. 10 (printed 5), fn. 2 | **The pooled state is unobserved — scope boundary and our whitespace** |
| Q8 | "Also shown is high abnormal share turnover (calculated relative to average turnover prior to the event window) around the activist engagement disclosure event; it increases by more than 80% over normal turnover prior to the event period, which in part reflects the stake purchases of the activist and, in some cases more than one activist." | PDF p. 22 (printed 17) | Trading around the flag — the only liquidity-adjacent fact |
| Q9 | "Abnormal returns around the announcement of outcomes average 6.4% across all countries during a (-20, 20) window, with the highest returns of 8.8% in Europe, 6.0% in North America and 2.7% in Asia." | PDF p. 7 (printed 2) | CAR by outcome, by region |
| Q10 | "However, conditional on observing an engagement, country characteristics do not correlate with measures of financial performance, such as initial disclosure returns and outcome disclosure returns." | PDF p. 36 (printed 31) | **Their own null: regime does not move returns conditional on engagement** |
| Q11 | "The most profitable outcomes are takeovers that are often preceded by governance changes, such as board restructurings. They signal that the outcome is a consequence of action taken by the activist and may not occur without engagement." | PDF p. 36 (printed 31) | Takeover as the dominant control outcome |
| Q12 | "Illiquidity (number of zero daily returns per year divided by the number of available daily returns per year, minimum of 200 available daily returns per year)." | PDF p. 48 (printed 43), Table 4 notes | Their liquidity proxy is a zero-return measure, not Amihud |

## 9. Verification log

**Verifier:** adversarial re-read of the full 59-page PDF, 2026-08-19.
**Method:** `pdftotext -layout research/txt_extracts/becht_etal_2017_full.pdf` re-extracted with per-page markers; every quote matched as an exact substring after whitespace/curly-quote normalisation. Printed page = PDF page − 5 confirmed from the footers (PDF p. 6 foots "1", PDF p. 45 foots "40", PDF p. 56 foots "51").

**Counts: 12 quotes — 11 OK, 1 MISCITED (Q4, fixed). 21 results — 17 OK, 1 WRONG (R9, fixed), 3 MISCITED/overstated (R14, R20, R21, all fixed). 7 scope claims confirmed, 0 refuted. 6 omissions added. 1 UNCHECKED block (Internet Appendix).**

| Item | Verdict | Checked against |
|---|---|---|
| Q1 (threshold list) | OK | verbatim, PDF p. 13 |
| Q2 (fn. 5, drop 273 sub-5% engagements) | OK | verbatim, PDF p. 13 footnote |
| Q3 (low thresholds ↔ more activism) | OK | verbatim, PDF p. 35 |
| Q4 (18.1% vs 9.7%) | **MISCITED → FIXED** | verbatim, but the sentence **starts on PDF p. 7 and finishes on PDF p. 8**; the card cited p. 8 only |
| Q5 (qualifies Greenwood–Schor) | OK | verbatim, PDF p. 26 |
| Q6 (53% / 61% / 50% / 18%) | OK | verbatim, PDF p. 7 |
| Q7 (fn. 2, private activism uncapturable) | OK | verbatim, PDF p. 10 |
| Q8 (abnormal turnover > 80%) | OK | verbatim, PDF p. 22 |
| Q9 (outcome CARs 6.4/8.8/6.0/2.7) | OK | verbatim, PDF p. 7 |
| Q10 (their own null on country characteristics) | OK as a quote — **but see the qualification added to §5**: Table 9 does not fully support it | verbatim, PDF p. 36 |
| Q11 (takeovers preceded by governance changes) | OK | verbatim, PDF p. 36 |
| Q12 (Illiquidity definition) | OK | verbatim, PDF p. 48, Table 4 notes |
| §4 Coffee–Palia wolf-pack definition | OK | verbatim, PDF p. 14 |
| §4 "no exact equivalent exists elsewhere" (13D purpose) | OK | verbatim, PDF p. 7 |
| §6 "we cannot distinguish … coordination … congregation" | OK | verbatim, PDF p. 10 |
| R1 (6.40\*\*\* [0.486] N=1,617; NA 7.00\*\*\* [0.641] N=1,027; Asia 6.43\*\*\* [1.238] N=213; Europe 4.75\*\*\* [0.898] N=377) | OK — all twelve figures match | Table 5 Panel A, PDF p. 49 |
| R2, R3 (all outcomes 6.42\*\*\* [0.78] N=850; Takeover 9.73\*\*\* [1.33] N=187; Mult+Takeover 18.1\*\*\* [4.20] N=58; Mult+NoTakeover 9.04\*\*\* [2.95] N=81; Restructuring 5.60\*\*\* [1.92] N=118; Board 4.48\*\*\* [1.45] N=272; Payout −0.16 [1.54] N=134) | OK — every number and every N matches | Table 7 Panel A, PDF p. 52 |
| R4 (Europe 8.77/10.8/25.1; NA 5.97/9.54/16.2; Asia 2.72 insignificant) | OK — and the card is right that **every** Asian category is insignificant at (−20,20) | Table 7 Panel B, PDF p. 52 |
| R5 (187 + 58 = 245 takeover-linked of 850) | OK | Table 7 Panel A |
| R6 (53/61/50/18%) | OK | PDF p. 7 |
| R7 (7.9% vs 4.7%) | OK | PDF p. 25 |
| R8 (all eight alphas and SEs) | OK — every figure matches | Table 8 Panel A, PDF p. 54 |
| R9 (window decomposition) | **WRONG → FIXED.** The claim "in all other months there is no positive abnormal return" is refuted by the paper's own table: the **value-weighted market-model alpha for engagements with outcomes in "All other months" is +5.842\*\* [2.917]**, significantly positive at 5%. The 14.2–18.9 and 26.4–28.2 ranges are correct. **Note this also refutes the paper's own p. 33 sentence** ("there are no significant abnormal returns generated by the activist, positive or negative") in both directions, since EW Carhart is −6.670\*\* and the no-outcome EW figures are −7.250\* and −11.677\*\*\* | Table 8 Panel B, PDF p. 55 |
| R10 (probit −0.007\*\*\* [0.001] N=89,515 col. 8; GLM −0.279\*\*\* [0.060] N=402 col. 11) | OK — exact, including the column assignment | Table 9, PDF p. 56 |
| R11 (1.797\* [0.972] adj R² −0.012 N=721 col. 2; −0.684 [0.878] col. 5, N=916) | OK — the card said N=721 for col. 2 (right) and did not give col. 5's N, which is 916 | Table 9, PDF p. 56 |
| R12 (Illiquidity −0.038\*\*\* / −0.031\*\*\* / −0.013) | OK — exact, and the card correctly identifies col. 4 (country FE, activist markets) as the one where it dies | Table 4 cols. 2–4, PDF p. 48 |
| R13 (turnover +80%) | OK as ASSERTED — Figure 2 is an image; the 80% is body text only. Label is correct | PDF p. 22, Figure 2 PDF p. 43 |
| R14 (wolf packs) | **MISCITED → FIXED.** 378 (21.7%) and 172 (11.8%) are Table 3 Panel A ✓; 13.82 [2.33] vs 6.32 [0.63], diff −7.50\*\*\* [1.93] are Table 5 Panel C ✓; 6.39 [2.04] is Table 5 Panel D ✓ (and is \*\*\*, which the card omitted). But **the 13.4% vs 8.0% stakes are not in any table** — they are body text on PDF p. 23, explicitly "unreported in the table". **Also flagged:** PDF p. 15 gives the same comparison as "13.4% versus 8.3%" — the paper prints two different stand-alone figures | Tables 3, 5C, 5D + PDF pp. 15, 23 |
| R15 (78% vs 46%, t=−8.11; takeover 15% vs 11%, t=−1.59) | OK | Table 7 Panel D, PDF p. 53 |
| R16 (7.34/6.94/4.27/4.87, t=2.21) | OK — exact | Table 5 Panel E, PDF p. 50 |
| R17 (IO_foreign US 0.063/0.110/0.180/0.209; domestic 0.037–0.049) | OK — exact | Table 4, PDF p. 48 |
| R18 (11% average stake; US 11, Japan 13, UK 13) | OK | PDF p. 16 text and Table 1, PDF p. 45 |
| R19 (806 days; 36/48/44/76%; t = −8.25/−4.32/−4.71) | OK — exact | Table 7 Panel C, PDF p. 52 |
| R20 (activism vs unsolicited bids) | **OVERSTATED → FIXED.** The three regional pairs are exact. "Everywhere" is false at country level: **Canada 0.6 vs 3.3, Norway 3.6 vs 4.8, Spain 0.2 vs 0.6** all run the other way | Table 2, PDF p. 46 |
| R21 (rule of law 0.022\*\*\*, common law −0.020\*\*\*, weak governance) | **OVERSTATED → FIXED.** Rule of law and Common law are exact. "Governance is weak" holds only in the country-year GLM (Quality of governance −5.488\*\*\*, col. 12); the firm-level probit coefficient is **−0.031, insignificant** (col. 9) | Table 9, PDF p. 56 |
| Per-country thresholds (Italy 0.02; Germany/Switzerland/UK 0.03; Canada 0.10; all others 0.05) | OK — checked country by country against the "Regulatory disclosure threshold" column | Table 1, PDF p. 45 |
| §2 probit sample sizes | **Internal inconsistency in the source, flagged in the card:** the Table 4 note says 114,978 firm-years, the Observations row prints **114,987** | Table 4, PDF p. 48 |
| Header: "ECGI WP N° 402/2014, May 2017, RFS forthcoming — not the published RFS article" | OK | PDF pp. 1–2 (ECGI cover, "May 2017") and PDF p. 4 ("Review of Financial Studies, forthcoming / 27 May 2014 / Revised 15 September 2016"). RFS pages 2933–2971 appear nowhere |
| §6 "The word premium/premia does not appear" | OK — **zero** hits for "premium" and zero for "premia" across all 59 pages. The takeover CARs are 41-day announcement returns, never bid premia; the card's warning not to report 9.73% as a premium is correct | grep over full text |
| §6 "No filing window is mentioned, in any country" | OK — **zero** hits for "ten days", "business days", "filing window". "Schedule 13D"/"13D" occurs exactly **twice**, on PDF p. 7 (stated purpose) and PDF p. 10 (13D Monitor, the vendor) — precisely as the card says | grep over full text |
| §6 "no reference to Maug/Kyle–Vila/Back" | OK as a *citation* claim — zero hits for "Kyle", "Amihud", "toehold", "noise trad". One hit for "Maug": **Ernst Maug as editor of the ECGI working-paper series on PDF p. 58**, i.e. the masthead, not a citation | grep over full text |
| §6 "Liquidity is a control, never an object" | OK — "liquidity"/"illiquidity" appears only in the Table 4 definition, the Table 4 and Table 9 covariate lists, and two sentences of PDF p. 20 describing those covariates. Never interacted, never on the right-hand side of a return regression as an object of interest | grep over full text |
| §5 "Internet Appendix not in this file" | **UNCHECKED (and unresolvable here)** — confirmed *absent*: the file ends at PDF p. 59 with the ECGI masthead. Referenced IA items are Table 11 (PDF p. 10), Table 15 (PDF p. 20), Table A17 (PDF p. 31), Table 18 (PDF p. 35) and Figure A4 (PDF p. 30), plus unnumbered IA discussions on PDF pp. 22 and 25. Anything the card sources there stays unverifiable | absence in PDF pp. 1–59 |
| PDF p. 24 fn. 13 (21 third-party takeover outcomes, 15 US, "materially unaltered") | OK | verbatim, PDF p. 24 |
| PDF p. 27 fn. 15 ("currently not available to us") | OK | PDF p. 27 |

**Omissions added by the verifier (each material to a liquidity × disclosure-rule × control-outcome position):**
1. **§4 / §7 pt. 6 — the raw threshold-vs-control-channel pattern in their own Tables 1 and 2.** Rank the activist markets by statutory threshold: Italy (2%) 13.3 engagements per 1,000 listed firms vs 1.6 unsolicited bids; Germany (3%) 7.3 vs 1.1; Switzerland (3%) 6.6 vs 4.9; UK (3%) 6.0 vs 4.1; US (5%) 19.6 vs 5.8; **Canada (10%) 0.6 vs 3.3 — the only country in the sample where the hostile-bid channel beats the activism channel.** Their own PDF p. 13 supplies the reading: the high-activism countries are ones "none of which are typically labeled as having active markets for corporate control". They print it as description and never regress it. Not identification, but the single strongest motivating fact available to us — and a referee question we should answer first.
2. **§4 — the Deutsche Börse pack (PDF p. 14).** Three funds held "publicly observable stakes above the disclosure threshold"; **eight "at the time did not disclose their holdings"**; combined the investors held 59% of voting rights; the regulator found no group. The threshold determines who is visible, not who is present — stated as fact in a competitor paper.
3. **§4 — the Atos Origin footnote (PDF pp. 14–15, fn. 6).** Three sequential disclosure events on one firm with three separate price reactions: Centaurus 5.5% stake → 7.8%; Pardus 7.3% → 1.7%; concert-party notification at 19.4% → a further 5.5%. A three-step measurement of the price of crossing the flag, buried in a footnote.
4. **§4 — target float composition (Table 1, PDF p. 45).** US targets: median 0.77 of shares held by institutions vs 0.43 for the FactSet US population; Japan 0.07 vs 0.04. Targets come from the institutionally-held end everywhere.
5. **§5 — their selection defence of the disclosure-CAR null (PDF p. 34).** "…since activists will have considered institutional ownership in picking targets, targets should have conditionally optimal institutional ownership; ownership would then appear unrelated to announcement returns." Substitute *liquidity* for *institutional ownership* and this is both a ready-made defence of a null we might otherwise fear and a warning that a cross-sectional liquidity–CAR regression cannot test our mechanism.
6. **§5 — the gap between their text and their Table 9.** PDF p. 34 says of the disclosure-CAR columns "none of the country-level measures are statistically significant" (col. 1 has Market cap/GDP 0.039\*, col. 2 has the threshold at 1.797\*) and of the outcome-CAR columns that country characteristics have no "meaningful explanatory power" (cols. 4–6 carry Rule of law 7.186\*\*, Common law 4.242\*, Board structure 10.649\*\*, IO_Foreign_U.S. 45.681\*/48.629\*, IO_Foreign Non-U.S. 26.282\*). If we cite Q10 as "their own null", cite the table with it.

**UNCHECKED (named, not triaged away):** everything sourced to the **Internet Appendix**, which is absent from this file — IA Tables 11, 15, A17 and 18 and Figure A4. Two of these matter for positioning: **IA Table 18** is where the institutional-ownership-to-number-of-outcomes relation lives (PDF p. 35 summarises it: total outcomes rise with domestic and foreign-US ownership; board outcomes rise with both; restructurings with domestic ownership; foreign non-US ownership negatively related to restructurings), and **IA Table 11** holds the entry-disclosure and exit counts. Neither can be verified from this document. If either is cited in draft_v3, obtain the published RFS Internet Appendix first.

**Overall verdict: SOUND WITH ONE SUBSTANTIVE CORRECTION.** The card's tables are extremely accurate — I checked roughly 120 printed numbers across Tables 1–9 and found no transcription error. The one WRONG item (R9) is a claim the card inherited from the paper's own overstated prose, and it matters, because R9 was doing work in §5 and §7 pt. 3. The card's central positioning claim survives intact and is if anything strengthened: Becht et al. hold the threshold margin, print the raw threshold-vs-control-channel pattern, and then explicitly delete the threshold variation (footnote 5) rather than identify off it. The window margin, the premium, and bidder entry are untouched by them — confirmed by exhaustive grep, not by impression.

## 9b. Published-version check (RFS 30(9), 2933–2971) + Internet Appendix — added by supplement reader, 2026-08-19

Source of truth: per-page `pdftotext -layout` re-extracts of
`research/txt_extracts/becht_2017_rfs_published.pdf` (39 PDF pages) and
`research/txt_extracts/becht_2017_internet_appendix.pdf` (17 pages), both read end to end.
**Published RFS page = published PDF page + 2932.** All twelve §8 quotes were re-matched as exact
substrings by an executed script, not by eye.

**Headline: every number in §3 survives to the digit and no table was renumbered. The two things
that changed are (a) the framing — the abstract and introduction are rebuilt around wolf packs and
Japan — and (b) the Internet Appendix is now in hand, which closes both UNCHECKED items and adds
one finding that matters more to our position than anything else in the paper.**

**The new finding, stated up front.** IA "Table 18" (IA pp. 11–12) regresses the **number of
outcomes** an engagement achieves on the same country characteristics as Table 9, outcome type by
outcome type. The **Disclosure Threshold** coefficient is **insignificant everywhere it matters**:
all outcomes 0.048 [0.110]; board outcomes 0.003 [0.057]; restructuring −0.046 [0.048]; and
**takeover outcomes 0.015 [0.025]**. The only significant threshold coefficient in the whole table
is on payout outcomes, 0.077\* [0.040]. Put together with Table 9: **the country disclosure
threshold predicts *whether* an activist shows up (−0.007\*\*\* firm-level, −0.279\*\*\* country-year)
but has no measured relation to *what the engagement achieves* — and specifically no relation to
takeovers.** That is the exact cell — threshold margin × control outcome — and the leading
international paper has looked at it and found nothing. §7's whitespace claim now rests on a
tested null rather than on an absence, which is a stronger position and a different sentence:
not "nobody has looked", but **"Becht et al. looked, cross-sectionally and without identification,
and found no threshold–outcome link; we look at a *change* in the rule and at the *window* margin
instead."** (added by supplement reader)

### Table and structure map (WP → published)

**Unchanged.** Tables 1–9, Figures 1–3, same panels, same contents.

| Object | WP PDF p. | RFS p. |
|---|---|---|
| Abstract (rewritten) | 3 | 2933 |
| Introduction | 6–9 | 2934–2936 |
| §1 Data description; threshold passage (Q1) and fn 5 (Q2) | 10–13 | 2937–2940 |
| Table 1 (per-country thresholds, ownership) | 45 | **2939** |
| Table 2 (engagements vs unsolicited bids per 1,000 listed firms) | 46 | **2941** |
| Wolf packs; Deutsche Börse; Coffee–Palia definition | 14–15 | 2940–2941 |
| Atos Origin three-step disclosure footnote | 14–15, fn 6 | **fn 6, 2941–2942** |
| Table 3 (wolf-pack and domestic/foreign counts) | 47 | **2942** |
| Wolf-pack aggregate stakes 13.4% vs 8.3% | 15 | **2943** |
| Table 4 (targeting probit, Illiquidity) | 48 | **2947** |
| Table 5 (disclosure CARs, Panels A–E) | 49–50 | **2949–2950** |
| Figure 2 (CAR + abnormal turnover); the ">80%" sentence (Q8) | 22, 43 | **2948**, Figure 2 on 2951 |
| Table 6 (outcomes by year and type) | 51 | **2953** |
| 7.9% vs 4.7% disclosure CAR split | 25 | **2954** |
| Table 7 (outcome CARs, Panels A–E) | 52–53 | **2955–2957** |
| Third-party takeover check (fn 13) | 24, fn 13 | **fn 13, 2952** |
| Table 8 (calendar-time alphas, Panels A–B) | 54–55 | **2963–2964** |
| "no significant abnormal returns … positive or negative" | 33 | **2965** |
| Table 9 (country characteristics) | 56 | **2966** |
| Selection defence of the disclosure-CAR null | 34 | **2967** |
| Q3, Q10, Q11 (country characteristics, the null, takeovers-preceded) | 35–36 | **2968** |
| Conclusion | 36–37 | 2968–2969 |

### Every §3 result → published version

| # | Verdict | Published location |
|---|---|---|
| R1 | **same** | Table 5 Panel A, p. 2949. Full 6.40\*\*\*[0.486] N=1,617; NA 7.00\*\*\*[0.641] N=1,027; Asia 6.43\*\*\*[1.238] N=213; Europe 4.75\*\*\*[0.898] N=377. (−10,10) column also identical: 6.14/6.06/3.93/6.97) |
| R2, R3 | **same** | Table 7 Panel A, p. 2955. All outcomes 6.42\*\*\*[0.78] N=850; Takeover 9.73\*\*\*[1.33] N=187; Multiple+Takeover 18.1\*\*\*[4.20] N=58; Multiple+NoTakeover 9.04\*\*\*[2.95] N=81; Restructuring 5.60\*\*\*[1.92] N=118; Board 4.48\*\*\*[1.45] N=272; Payout −0.16[1.54] N=134. **Added detail:** the text now says **880** of 1,740 engagements have ≥1 outcome, of which **850** have sufficient return data (p. 2954) — the WP card only had the 850 |
| R4 | **same** | Table 7 Panel B, p. 2955. Europe 8.77\*\*\*/10.8\*\*\*/25.1\*\*; NA 5.97\*\*\*/9.54\*\*\*/16.2\*\*\*; Asia all outcomes 2.72[3.48], and every Asian category still insignificant at (−20,20) |
| R5 | **same** | 187 + 58 = 245 takeover-linked of 850, Table 7 Panel A |
| R6 | **same** | p. 2934, verbatim (Q6) |
| R7 | **same** | p. 2954: 7.9% with outcomes vs 4.7% without, difference significant at 1% |
| R8 | **same** | Table 8 Panel A, p. 2963. EW Carhart 1.104[3.407] / −9.750\*\*\*[3.608] / 10.854\*\*\*[4.078]; VW Carhart 7.987\*\*[3.340] / 2.325[5.379] / 5.662[6.140]; EW MktModel 8.399\*\*[4.119]; VW MktModel 11.254\*\*\*[3.473]. Every regional row also matches |
| R9 | **same — and the verifier's WRONG finding is confirmed against the published article** | Table 8 Panel B, p. 2964. "Only months t=0" 14.213–18.859; "Only months with outcome announcements" 26.409–28.225; **"All other months": EW Carhart −6.670\*\*[2.573], no-outcome EW −7.250\*[3.674] and −11.677\*\*\*[3.436], and VW MktModel with outcomes +5.842\*\*[2.917]**. The paper's own prose at **p. 2965** still reads "there are no significant abnormal returns generated by the activist, positive or negative". **The RFS referees did not catch this; the card's correction stands against the published article and should be flagged if we ever cite R9** |
| R10 | **same** | Table 9, p. 2966: Disclosure threshold −0.007\*\*\*[0.001] N=89,515 (col. 8, probit) and −0.279\*\*\*[0.060] N=402 (col. 11, GLM) |
| R11 | **same** | Table 9, p. 2966: 1.797\*[0.972] on disclosure CAR (col. 2, adj. R² −0.012, N=721); −0.684[0.878] on outcome CAR (col. 5, N=916) |
| R12 | **same** | Table 4, p. 2947: Illiquidity −0.038\*\*\*[0.006] / −0.031\*\*\*[0.007] / **−0.013[0.008] once country FE enter**. Definition unchanged |
| R13 | **same, still ASSERTED** | p. 2948 text (Q8); Figure 2 on p. 2951 is an image with no SE |
| R14 | **same numbers, and one WP inconsistency is FIXED** | Table 3 Panel A, p. 2942: 378 (21.7%) engagements, 172 (11.8%) target firms; of the 378, 290 (76.7%) have two funds and 88 (23.3%) three or more. Table 5 Panel C, p. 2949: 13.82\*\*\*[2.33] vs 6.32\*\*\*[0.63], difference −7.50\*\*\*[1.93]. Table 5 Panel D: wolf-pack dummy 6.39\*\*\*[2.04], residual-wolf-pack 7.04\*\*\*[2.09]. **The WP printed the aggregate stakes as both "13.4% versus 8.0%" and "13.4% versus 8.3%"; the published article prints only 13.4% vs 8.3% (p. 2943), and it is still body text, not a table.** Use 8.3% |
| R15 | **same** | Table 7 Panel D, p. 2956: P(any outcome) 46% vs 78% (t −8.11\*\*\*); P(takeover) 11% vs 15% (t −1.59, insignificant); outcome CARs indistinguishable |
| R16 | **same** | Table 5 Panel E, p. 2950: 7.34\*\*\*/6.94\*\*\*/4.27\*\*\*/4.87\*\*\*, difference t = 2.21\*\* |
| R17 | **same** | Table 4, p. 2947: IO_foreign U.S. 0.063\*\*\*/0.110\*\*\*/0.180\*\*\*/0.209\*\*\*; IO_domestic 0.037\*\*\*–0.049\*\*\* |
| R18 | **same** | p. 2934 and Table 1, p. 2939: average stake 11% |
| R19 | **same** | Table 7 Panel C, p. 2956: 806 days; 36 / 48 / 44 / 76%; t = −8.25\*\*\* / −4.32\*\*\* / −4.71\*\*\*. **Added detail in the note:** Panel C is built from 150 outcomes across the 58 Multiple+Takeover engagements |
| R20 | **same, and the card's verifier qualification still holds** | Table 2, p. 2941. Asia 3.2 vs 0.5, Europe 3.4 vs 2.1, North America 11.7 vs 4.6; **Canada 0.6 vs 3.3, Norway 3.6 vs 4.8, Spain 0.2 vs 0.6** still run the other way. Published text adds the ratios: activism exceeds hostile bids "by 6.4 times (3.2/0.5)" in Asia, 2.5× in North America, 1.6× in Europe |
| R21 | **same, and the card's verifier qualification still holds** | Table 9, p. 2966: Rule of law 0.022\*\*\*, Common law −0.020\*\*\*, Quality of governance **−0.031 insignificant** in the firm-level probit (col. 9) but **−5.488\*\*\*** in the country-year GLM (col. 12). The p. 2968 prose still says "governance is relatively weak" without the qualification |

### Every §8 quote → published version

**All twelve are verbatim in the published article.** Only the pages change.

| # | Verdict | RFS page |
|---|---|---|
| Q1 (per-country thresholds) | **same, verbatim** | 2940 |
| Q2 (fn. 5 — drop the 273 sub-5% engagements) | **same, verbatim, still footnote 5** | **2940** |
| Q3 (low thresholds ↔ more activism) | **same, verbatim** | 2968 |
| Q4 (18.1% vs 9.7%) | **same, verbatim — and the page-straddle is gone; the sentence now sits whole on one page** | **2935** |
| Q5 (qualifies Greenwood–Schor) | **same, verbatim** | 2954 |
| Q6 (53% / 61% / 50% / 18%) | **same, verbatim** | 2934 |
| Q7 (fn. 2 — private activism uncapturable) | **same, verbatim, still footnote 2** | **2937** |
| Q8 (abnormal turnover > 80%) | **same, verbatim** | 2948 |
| Q9 (outcome CARs 6.4 / 8.8 / 6.0 / 2.7) | **same, verbatim** | 2935 |
| Q10 (their own null on country characteristics) | **same, verbatim** — and the §5 qualification stands: Table 9 (p. 2966) still carries Market cap/GDP 0.039\*, Disclosure threshold 1.797\*, Rule of law 7.186\*\*, Common law 4.242\*, Board structure 10.649\*\*, IO_Foreign_U.S. 45.681\*/48.629\*, IO_Foreign Non-U.S. 26.282\* | 2968 |
| Q11 (takeovers preceded by governance changes) | **same, verbatim** | 2968 |
| Q12 (Illiquidity definition) | **same, verbatim**, Table 4 notes | 2947 |

Also re-matched verbatim in the published article: the Coffee–Palia wolf-pack definition (2940–2941),
"no exact equivalent exists elsewhere" (2934), "we cannot distinguish … coordination … congregation"
(2936), the Deutsche Börse three-visible / eight-undisclosed passage (2941), the Atos Origin
footnote (fn. 6, 2941–2942), "none of which are typically labeled as having active markets for
corporate control" (2940), the selection defence of the disclosure-CAR null (2967), and the
third-party takeover check (fn. 13, 2952).

### §9 UNCHECKED items closed

| Item left open in §9 | Status now |
|---|---|
| **IA Table 18** — institutional ownership → number of outcomes | **CLOSED.** IA pp. 11–12. Dependent variables are counts of outcomes by type; N = 730–741; OLS with calendar-year FE and firm-level controls. **N. all achieved outcomes:** IO_Domestic 0.520\*\*\*[0.159] / 0.462\*\*[0.215] / 0.136[0.206]; IO_Foreign_U.S. 3.147[2.011] / 5.225\*\*[2.078] / 5.359\*\*[2.126]; IO_Foreign Non-U.S. insignificant throughout. **Board outcomes:** IO_Domestic 0.301\*\*\*/0.313\*\*/0.133; IO_Foreign_U.S. 2.452\*/2.941\*\*/3.258\*\*. **Restructuring:** IO_Domestic 0.230\*\*\*/0.225\*\*/0.222\*\*\*; **IO_Foreign Non-U.S. −0.715\*\*/−0.709\*\*/−1.043\*\*\***. **Takeover outcomes: every ownership coefficient insignificant.** The body's summary (p. 2967) is accurate but understates one thing worth having: **no ownership variable predicts the number of takeovers.** R² 0.049–0.157 |
| **IA Table 11** — entry-disclosure and exit counts | **CLOSED.** It is the IA's **Table 2**, "Activist engagements by entry and exit", IA p. 2 (the body's cross-reference number does not match the appendix's own caption — see the numbering warning below). Of 1,740 engagements, **1,270 had concluded by 31 December 2010 and 470 have no reported exit**; the **average holding period is 1.7 years (624 days)**. Entries by year: 2000: 48, 2001: 63, 2002: 66, 2003: 91, 2004: 138, 2005: 231, 2006: 354, **2007: 369 (peak)**, 2008: 228, 2009: 93, 2010: 59. Panel B gives exit rates by cohort (e.g., of the 2007 cohort, 21.7% exit within one year, 27.9% within two, 25.2% never exit in sample) |
| "Internet Appendix not in this file — Tables 11, 15, A17, 18 and Figure A4 unverifiable" | **CLOSED for all of them.** The appendix in hand contains: A1 data sources by country (IA p. 1); **A2 = the entry/exit table** (IA p. 2); A3 = the comparison with Brav–Jiang–Partnoy–Thomas (2008) (IA pp. 3–4); A4 = prior single-country disclosure-return studies (IA p. 5); **A5 = the country-interacted targeting probit, the body's "Table 15"** (IA p. 6); A6–A7 = raw returns and fixed-horizon alphas, the body's "Table A17" (IA pp. 7–9); **A8 = Figure 4, the domestic-vs-foreign outcome-probability scatter** (IA p. 10); **A9 = "Table 18"** (IA pp. 11–12); **A10 = ten pages of country case studies** (IA pp. 13–17) |

**Numbering warning for anyone citing the appendix.** The Internet Appendix numbers its own tables
**1–8** (plus one table captioned "Table 18" and one figure captioned "Figure 4"), while the article
body cross-references them as **Tables 11, 13, 15, 17 and 18 and Figure A4**. The two schemes do not
line up. **Cite by appendix section (A1–A10) and IA page, not by table number.**

### What the published version ADDS (added by supplement reader)

1. **A different abstract and a different sales pitch.** The published abstract leads with
   institutional ownership and wolf packs — "almost one-quarter of engagements are by multi-activists
   engaging the same target. These engagements perform strikingly better than single activist
   engagements" — and ends on "Japan is an exception, with high initial expectations and low
   outcomes" (p. 2933). The paper's fifth stated contribution is now "the first comprehensive
   evidence of hedge fund wolf packs internationally" (p. 2936). **The disclosure threshold, which
   is what we care about, has moved further into the background between WP and print.** That is good
   news for the whitespace claim and worth one sentence in our literature section.
2. **The Brav–Jiang–Partnoy–Thomas overlap audit** (IA A3, pp. 3–4), which did not exist in a form
   we could check. They obtained BJPT's actual data, took the 2001–2006 US window where the two
   samples should coincide, and hand-diagnosed 80 randomly chosen non-overlapping engagements: BJPT
   covers the *universe of activists* better (68% of BJPT-only cases are activists BFGW never
   listed), BFGW covers *all engagements of a given activist* better (63% of BFGW-only cases are
   activists BJPT lists but engagements BJPT missed). Disagreement about a specific data item is
   rare (3–8%). Disclosure CARs are statistically indistinguishable across the three buckets: in
   both samples 7.29\*\*\*[1.102] N=297, BJPT only 7.31\*\*\*[0.963] N=545, BFGW only 8.72\*\*\*[1.789]
   N=149 at (−20,20). **This is the best published evidence that hand-collected and vendor-collected
   activism samples agree on returns, and it is directly relevant to our own EDGAR-parser validation
   step in the referee checklist.**
3. **A table of prior single-country disclosure returns** (IA A4, p. 5) — a ready-made comparison
   set: US 6.5% (Boyson–Mooradian), 7.2% (BJPT), 3.6% (Greenwood–Schor), 5.7% (Klein–Zur); Germany
   4.4% (Bessler–Drobetz–Holler); Italy 1.8% (Croci–Petrella); Japan 5.6% (Uchida–Xu) and 1.8%
   (Hamao–Kutsuna–Matos); UK −1.9% (Becht–Franks–Mayer–Rossi, one fund).
4. **Fixed-horizon alphas** (IA A7, pp. 9–10) that the body only gestures at: value-weighted
   MktModel alphas for engagements with outcomes are 13.183\*\*\* (12m), 11.750\*\*\* (24m),
   10.642\*\*\* (36m), 9.047\*\*\* (full); Carhart 8.853\*\* / 7.686\*\* / 7.381\*\* / 6.255\*\*. Engagements
   without outcomes are negative and significant under Carhart equal-weighted at every horizon
   (−11.511\*\*\* to −9.652\*\*\*).
5. **Country-by-country shareholder-rights thresholds in the case studies** (IA A10, pp. 13–17) —
   a second institutional layer the card did not have, and one that bears directly on the
   *threshold margin* being about more than disclosure: **France** 5% of capital to call an EGM,
   0.5% to table a binding resolution; **Germany** 5% to call an EGM, shares held ≥ 3 months;
   **Netherlands** 10% to requisition an EGM, 1% for a non-binding resolution; **Japan** 3% held
   ≥ 6 months to requisition an EGM, 1% for a *binding* AGM resolution; **UK** easy requisition with
   binding resolutions. Sweden works through a nominations committee rather than a vote at all.
   **A country has several thresholds, and the disclosure threshold is only one of them** — a
   confound our own threshold-margin story has to name if we ever go cross-country.
6. **Two sub-threshold cases that are directly our pooled state** (IA A10). Wyser Pratte held
   **0.53%** of Lagardère and still ran a proxy campaign (IA p. 13). Perry Capital accumulated
   **4.7%** of NEC Electronics — below Japan's 5% disclosure threshold — and the *release of its
   letter* triggered a **10.6% abnormal return** (IA p. 16). The second is a priced activism event
   with no flag; it is the cleanest single illustration in the competitor set that the pooled state
   is economically live, and it is in an appendix nobody reads.
7. **The word "premium" now appears — but only in the Internet Appendix, and only as narrative.**
   Perry offered to buy 25% of NEC's stake in NECE "at a 65% premium" (IA p. 16), and F&C Asset
   Management "was subsequently acquired at a substantial premium in 2013. The takeover was
   facilitated by the board changes initiated by the activist" (IA p. 17). **Neither is measured.**
   §6's claim must be restated precisely: *the published article body contains zero occurrences of
   "premium", "premia" or "bidder" (executed grep); the Internet Appendix contains two narrative
   uses of "premium" and zero of "bidder".* The takeover premium is still never an estimated object.
8. Smaller additions: the Grateful Dead quote from Phil Goldstein of Bulldog Investors defending
   uncoordinated packs (p. 2940); citations to Brav–Dasgupta–Mathews (2016) on pack formation
   (p. 2940) and Appel–Gormley–Keim (2016) on passive ownership and board outcomes (fn. 22, p. 2967);
   fn. 1 (p. 2935) reporting that fund size (≥ 20 engagements) does not affect performance; fn. 11
   (p. 2948) that simple market-index-adjusted returns are 1.3 pp lower and still significant at 1%;
   and fn. 21 (p. 2965) conceding that the relative improvement of large engagements over time is
   concentrated in engagements *without* observable outcomes, with no test of why.

### What the published version DROPS or FIXES

1. **The WP's "13.4% versus 8.0%" figure is gone.** Only 13.4% vs 8.3% survives (p. 2943). The card's
   flagged inconsistency is resolved — use 8.3%.
2. **Nothing else.** No result, table, footnote or institutional fact in §§1–8 is missing from the
   published article.
3. **Two source-level defects the card flagged are NOT fixed and are in print:** the Table 4
   observation-count mismatch (note says 114,978 firm-years, the Observations row prints **114,987**,
   p. 2947), and the contradiction between the p. 2965 prose and Table 8 Panel B (R9).

### Still open after this pass

- Nothing is unverifiable any more. Both the article and its Internet Appendix are in hand and read.
- One judgement call left to the positioning stage: whether to lead §7 with the **null** from IA
  "Table 18" (threshold does not predict takeover outcomes) or with the **descriptive pattern** from
  Tables 1–2 (low-threshold countries have more activism and fewer hostile bids). They point the
  same way but carry different risks — the null is a tested result we would be arguing *around*,
  the pattern is uncontrolled. **Recommendation: lead with the null, because a referee who knows
  this paper will raise it, and it is much better raised by us.** The honest framing is that a
  cross-section of five threshold values across twenty-odd countries, with everything collinear
  with the legal system, has essentially no power to detect a threshold–outcome link — which is
  precisely the argument for a dated within-country change in the *window* margin instead.
