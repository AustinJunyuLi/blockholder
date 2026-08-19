# Norli, Østergaard & Schindele (2015) — "Liquidity and Shareholder Activism"

**Venue / status:** *Review of Financial Studies* 28(2), 486–520 (2015), doi:10.1093/rfs/hhu070, Advance Access 7 October 2014, © The Author 2014; editor Laura T. Starks, executive editor David Hirshleifer, one anonymous referee — **PRIMARY for all page cites**. Working-paper version also read: CCGR (BI Norwegian Business School) WP **No. 1/2014**, cover-dated April 2014 (the same PDF's back-matter contents lists it as "April 2013" — an internal inconsistency in the WP), 53 PDF pages. §§1–8 below were written from the WP; §9b records the re-basing onto the published article. **Cite the RFS pages (486–520) in draft_v3.**
**Full text from:** published — `research/txt_extracts/norli_ostergaard_schindele_2015_rfs_published.pdf` (35 PDF pp.) / `.txt`; WP — `research/txt_extracts/norli2015.pdf` (53 pp.) / `research/txt_extracts/norli2015_layout.txt` · **Reader:** opus, opus (published-version supplement) · **Read:** both full texts end to end (published: body, Figures 1–2, Tables 1–9, Appendix A activist types, Appendix B instruments + Table B.1, references)
**Page numbering used below:** §§1–8 quote the **WP's** printed manuscript page (printed p. N = PDF p. N+2). §9b gives the **published** RFS page for every one of them. Published RFS page = published PDF page + 485 (PDF p. 1 = RFS p. 486).
**No online appendix.** Everything in the published article is in the article; Appendices A and B are printed (pp. 516–518). Nothing about this paper is left unverifiable.
**Type:** empirical **Role for us:** antecedent (the direct empirical statement of "liquidity lets an activist accumulate cheaply, so liquidity causes voice") and measurement template for pre-event accumulation

## 1. Question

Does stock liquidity make costly shareholder *voice* more likely, and does it do so through the specific channel the theory names — the activist buying shares at a price that does not yet reflect the value his own intervention will create? Maug (1998), Kahn & Winton (1998) and Winton & Li (2006) say yes: liquidity lets the activist recoup the cost of a campaign through informed trading, defeating the free-rider problem. Coffee (1991) and Bhide (1993) say no: liquidity makes walking away cheap, so it substitutes for intervention. NOS pick *costly, observable, formal* voice — contested proxy solicitations — precisely because the theory's mechanism only bites when activism is expensive, and then go and look at the activist's actual trades.

## 2. Model / data and method

**Design:** annual firm-level probit of an activism dummy on lagged liquidity with year fixed effects, plus an IV-probit, plus a cross-sectional OLS of pre-event accumulation on liquidity. Not structural; no natural experiment in the DiD sense.

**Sample.**
- Firms listed on **NYSE, AMEX and Nasdaq**, common equity, requiring CRSP and Compustat coverage.
- Activism events hand-collected from **EDGAR**, from filings by non-management relating to contested proxy solicitations: forms **PREC14A, PREN14A, PRRN14A, DEFC14A, DEFN14A, DFRN14A, DFAN14A, DEFC14C**.
- Period: **1994 through the third quarter of 2007** (deliberately stopping before the Lehman default). Voluntary EDGAR filings from Q3 1993 are included where they are contested proxy material; mandatory EDGAR filing for all US public companies began **6 May 1996** (printed p. 8).
- Funnel (printed p. 9): 8,783 unique non-management forms → first-filing-of-a-sequence rule → **998** activism firm-years → −174 not found in CRSP → −135 not NYSE/AMEX/Nasdaq common equity → −98 missing market cap or book-to-market → −88 filings following a *friendly negotiated merger agreement* → **503** cases → −118 tender offers and "bear hugs" → **385 activist events**. About 87% are proxy contests; 12% involve shareholder proposals.
- Regression samples are smaller again from missing controls: the preferred probit has **63,396 firm-year observations and 354 activism events**.
- **Unconditional probability of activism in the sample: 0.56%** — roughly 28 events per year, with the annual frequency ranging 0.11%–0.83%.
- Activists are genuine blockholders: mean ownership at announcement ≈ **9%** overall (9–11% for hedge funds, shareholder committees and individuals; >15% for industrial owners; ≈0% for workers' unions). Hedge funds are involved in almost half of events (47.3%), shareholder committees 29% (28.8%), individuals 13% (13.2%). 83% of campaigns propose alternative director nominees (Table 1 Panel C: 82.6%). Type split (Panel A): proxy contest 86.0%, shareholder proposal 11.2%, both 0.8%, other 2.0%.
- **Stated purposes are heavily control-flavoured even after takeover events are stripped (added by verifier — Table 1 Panel C, printed p. 35 / PDF p. 37).** Categories overlap; the shares are: change in the board of directors **82.6%**, corporate governance/voting 42.6%, business strategy 42.3%, **sale of target assets or sale of the target company 34.3% (132 events)**, operating efficiency 26.0%, CEO/director pay 22.6%, **removal of a takeover defence 18.4% (71 events)**, payout 16.4%, replace the CEO 15.6%, capital structure 7.8%, **prevention of an acquisition/merger 3.6%**, **prevention of a take-over 3.6%**. This matters for us: NOS remove *acquirer-sponsored* solicitations from the event definition, but the surviving campaigns are not control-free — over a third state sale of the company as a purpose.
- **Trading sub-sample:** trades hand-collected from Schedule 13D and SC 13D/A. Of the 354 core-sample events, trades found in 197; 157 with no trade information; of those, 88 had activist ownership below 5% (so no reporting duty) and 7 unknown ownership. Removing those 95 leaves **259 event firms — 197 with trades, 62 with no trades — and 11,518 recorded trades** spanning event days −252 to +40.

**Liquidity measures (exactly as defined).**
- **Primary: `L` = the Hasbrouck (2009) effective trading cost measure, multiplied by −1**, so higher = more liquid. Taken from Joel Hasbrouck's website. Annual, firm-level.
- **Secondary: the Amihud (2002) trade impact measure, multiplied by −1**, winsorised at the 1st and 99th percentiles (they note the raw measure has outliers "close to 500 times larger than the average liquidity").
- Timing variants: contemporaneous with controls (t−1), the **preferred lag t−2**, and a long lag averaged over t−4 and t−3. In the trading regressions liquidity is at **t−3** so that the liquidity window never overlaps the trade-recording window.
- Two further constructions: **orthogonalised liquidity** (residual of L(t−2) on the Herfindahl of institutional ownership, institutional holdings, institutional breadth and cross-sectional average liquidity) and a **median-split dummy**.
- **Note for us:** the primary proxy is an *effective-cost* (percent-cost) measure, not Amihud. Amihud is the robustness. This differs from Edmans-Fang-Zur, whose primary is Amihud. If we cite both papers as "the Amihud channel", we are wrong about NOS.

**Outcome objects.**
1. `ACT_it` = 1 if firm *i* experiences shareholder activism (a contested proxy solicitation by a non-management filer) in year *t*. → *incidence of costly voice*.
2. The **fraction of the target firm's outstanding shares acquired by the activist** over the 252 trading days ending on the day before the activism announcement. → *pre-event accumulation*.
There is **no** return, premium, or campaign-success outcome anywhere in the paper.

**Controls:** three ownership-structure variables (Herfindahl of 13F institutional ownership, institutional holding, institutional breadth à la Chen-Hong-Stein), abnormal performance at t−1 and t−2 (Fama-French 3-factor + momentum, rolling 12–60 month betas), volatility, analyst coverage (I/B/E/S), Nasdaq dummy, log market cap, book-to-market, log sales, cash, dividend yield, R&D. **Year fixed effects throughout** — the authors are explicit that identification is purely cross-sectional, because both activism and market liquidity trend up over the sample. z-values from Huber-White robust standard errors.

**Identification.**
- Baseline: lag liquidity to t−2 (controls at t−1) so that ownership changes in t−1 cannot drive the measured liquidity.
- **IV-probit with two instruments** (Appendix B, printed pp. 45–46):
  (i) **Decimalization × pre-2001 average Log(Sales).** A dummy equal to one from 2001 onward, interacted with the firm's average sales over 1994–2001 (divided by 100 for scaling). The interaction is what creates cross-sectional variation — a bare decimalization dummy would only pick up time variation, which the year fixed effects already absorb. Justified by Furfine (2003) and Chakravarty-Wood-van Hess (2004) finding decimalization bit harder for more actively traded stocks; size proxies for trading activity, and sales are used rather than market cap because sales do not move with the stock price.
  (ii) **Average liquidity of firms in industries other than firm i's**, at t−2, using Fama-French 49 industries.
  Correlations of the instruments with Hasbrouck liquidity: **0.26** and **0.27**; with Amihud liquidity: **0.05** and **0.10**.
  **The model is an ML IV-probit, not a two-stage estimator** *(added by verifier, printed p. 46)*: "The coefficients are estimated simultaneously by maximum likelihood, but we present the results from a 'first stage' regression". So Table B.1 is a *display* first stage, which is why no F or Cragg-Donald statistic exists anywhere — a referee point that should be made precisely rather than as "they forgot to report it".
  First stage in Table B.1: both instruments strongly significant (Hasbrouck: other-industry liquidity −7.50, z = −18.90; decimalization×sales −0.17, z = −35.54; Amihud: −6.17, z = −12.56 and −0.71, z = −15.64). *(Verifier note: Table B.1's own N — 60,728 Hasbrouck / 58,957 Amihud, 354 / 346 events — does not match the IV columns it is supposed to underlie, Table 4 col. (2) at 62,025 / 349 and Table 5 col. (4) at 57,689 / 346. An unexplained inconsistency in the WP.)*
  **Amemiya-Lee-Newey overidentification test does not reject instrument validity: p = 0.430 (Hasbrouck), p = 0.841 (Amihud).**
  **Wald test of exogeneity: p = 0.214 for Hasbrouck (cannot reject that liquidity is exogenous) but p = 0.040 for Amihud (rejected).** This is the paper's own admission that the IV is not obviously needed under its preferred measure.

## 3. Results — with honesty labels

Parentheses in Tables 3–7 contain **z-values**, not standard errors (Huber-White robust). In Table 9 they are t-values.

| # | Result (one line) | Label | Where (page / table) |
|---|---|---|---|
| R1 | **Baseline probit.** Liquidity raises the probability of activism. Hasbrouck L(t−1): coefficient **12.77 (z = 4.81)**, N = 63,555, 355 events, pseudo-R² 0.029. Preferred Hasbrouck L(t−2): **10.27 (z = 3.30)**, N = 63,396, 354 events, pseudo-R² 0.027 | ESTIMATED | Table 3, printed p. 37 (PDF p. 39) |
| R2 | **The 0.33 → 0.73 number, correctly attributed.** This is the **baseline probit, Table 3 column (2)** — not the IV. Moving liquidity from its 10th to its 90th percentile (other covariates at their means) raises the predicted probability of activism **from 0.33% to 0.73%**, i.e. a **+0.40 percentage point** change, Wald p = 0.000 (delta-method SEs). That is **71.2%** of the 0.56% unconditional probability. In column (1), L(t−1), the same discrete change gives **+0.47 pp**, = **84.9%** of the sample probability | ESTIMATED | printed p. 17 and n. 12 (PDF p. 19); Table 3 bottom panel, printed p. 37 |
| R3 | **IV-probit (Hasbrouck).** Instrumented L(t−2) coefficient **19.2 (z = 2.5)**, N = 62,025, 349 events. Discrete 10th→90th change in liquidity now raises activism probability by **+0.79 pp** (p = 0.043) = **142.3%** of the sample probability — roughly *double* the OLS-probit effect and much less precisely estimated | ESTIMATED | Table 4 col. (2), printed p. 38 (PDF p. 40) |
| R4 | Other Hasbrouck robustness: long lag L(t−4,t−3) **5.9 (z = 2.3)**, Δ = +0.25 pp (p = 0.018), 44.2%; orthogonalised L(t−2) **8.1 (z = 3.2)**, Δ = +0.28 pp (p = 0.002), 49.6%; median-split dummy **0.2 (z = 3.4)**, Δ = +0.28 pp (p = 0.000), 50.1% | ESTIMATED | Table 4 cols. (1),(3),(4), printed p. 38 |
| R5 | **Amihud versions are uniformly weaker.** L(t−1) **0.9 (z = 2.2)**, Δ +0.13 pp (p = 0.023), 22.1%; L(t−2) **1.2 (z = 2.4)**, Δ +0.15 pp (p = 0.012), 26.4%; L(t−4,t−3) **0.7 (z = 1.7)**, Δ +0.10 pp (p = 0.079), 17.3%; **IV Amihud 4.6 (z = 4.9)**, Δ **+1.36 pp** (p = 0.084), **237.2%** of sample probability | ESTIMATED | Table 5, printed p. 39 (PDF p. 41) |
| R6 | **Overvaluation attenuates the liquidity effect (Hasbrouck).** With overvaluation = Ln(Volatility/Institutional Holding): interaction **−1.86 (z = −3.6)**, liquidity level **11.82 (z = 3.9)**; Ai-Norton average interaction effect **−0.06 (avg z = −2.2)**. Discrete 10th→90th liquidity change raises activism by **0.68 pp** at the 10th overvaluation percentile vs **0.33 pp** at the 90th — difference **0.36 pp, p = 0.035**, i.e. "approximately halved". N = 63,396, 354 events | ESTIMATED | Table 6 col. (1), printed p. 40 (PDF p. 42) |
| R7 | Same pattern for the other three overvaluation proxies: Volatility (int. −15.73, z = −2.7; 0.64 vs 0.41, diff 0.23, p = 0.030); Ln(1/Institutional Holding) (−2.18, z = −3.9; 0.94 vs 0.49, diff 0.45, p = 0.013); mutual-fund-inflow **price pressure** (−1.57, z = −3.8; 0.51 vs 0.31, diff 0.20, p = 0.020) | ESTIMATED | Table 6 cols. (2)–(4), printed p. 40 |
| R8 | With Amihud liquidity, the overvaluation interaction survives in sign but weakens: average interaction effects −0.01 to −0.08 (avg z −1.8 to −2.1); the 10th-vs-90th probability difference is 0.10, 0.10, 0.10, 0.08 with p = **0.146**, 0.048, **0.095**, 0.043 — i.e. two of four are insignificant at 5% | ESTIMATED (weak) | Table 7, printed p. 41 (PDF p. 43) |
| R9 | **Pre-event accumulation is pervasive.** Across 259 event firms, activists traded before the announcement in **76%** of cases; **11,518** trades; **95% are purchases**; mean trade **$346,000**, median **$16,000** | ESTIMATED (descriptive) | Table 8, printed p. 42 (PDF p. 44) |
| R10 | **Size of accumulation and profit.** Activists that trade acquire on average **4.25% of the target's outstanding shares** in the 252 trading days before announcement — **54% of the block they hold at announcement**. Mean trading profit **$1.56 million**, = **8.5%** of the announcement-date value of the shares acquired. Hedge funds specifically: 88% trade, 4.89 pp acquired, 61% of own block, $2,117k, **9.9%** | ESTIMATED (descriptive) | Table 8, printed p. 42; text printed pp. 25–26 |
| R11 | **The mechanism regression.** Regressing the fraction of shares acquired in the 252 days pre-announcement on liquidity at t−3 with controls at t−2: Hasbrouck **40.98 (t = 2.52)** on all data (N = 311, R² 0.175) and **40.97 (t = 2.07)** dropping zero-trade and sub-5% cases (N = 232, R² 0.197). Amihud **3.75 (t = 2.38)** (N = 298) and **3.93 (t = 1.94)** (N = 221) | ESTIMATED | Table 9, printed p. 43 (PDF p. 45) |
| R12 | The reading that informed pre-activism trading is "a substantive driver behind the positive effect of liquidity on activism" is an inference stacking R1+R6+R9+R11; nothing tests the profit channel against an alternative (e.g. liquid firms are simply easier to attack for unrelated reasons) | ASSERTED | printed p. 3 and p. 27 |

**The correction the positioning stage needs.** The internal note describing "a baseline probit marginal effect of about 0.33 → 0.73" is **right about the source but easy to misstate**: 0.33% and 0.73% are the *predicted probabilities of activism* at the 10th and 90th percentiles of liquidity in the **baseline (non-IV) probit**, Table 3 column (2). The marginal effect is the **difference, +0.40 pp**. The **IV** figure is a different and much larger number: **+0.79 pp** (Hasbrouck) or **+1.36 pp** (Amihud). Do not report 0.33 → 0.73 as an IV result and do not report +0.40 pp as "0.33".

## 4. Institutional facts used

- **The 5% threshold and the 13D transaction schedule are the paper's data source, not its treatment.** "Rule 13D-1(a) of the Securities and Exchange Act requires active investors to file with the SEC to disclose the acquisition of more than 5% of any class of securities of a publicly traded company. The Schedule 13D filing includes trading dates, prices and quantities traded during the 60 day period before the filing date." (printed p. 12). **This 60-day transaction-history window inside Item 5 is the entire reason trade-level activist data exists.** NOS exploit it exactly as Collin-Dufresne & Fos do.
- **Their stitching procedure** (printed p. 12): for each target, take the 13D closest to (and no more than one year before) the activism announcement; add all SC 13D/A amendments. So the observable trade window is 60 days back from *each* filing, chained — "if an activist's most recent 13D-filing occurs 6 months prior to the announcement date, we have information about his trades for a period of 8 months back from the announcement date." Early trades are lost if the activist filed more than one 13D in the year.
- **Below 5% there is no reporting duty**, which is why 88 of the 157 no-trade cases are censored rather than genuinely trade-free (printed pp. 12–13). This is a *threshold-margin* censoring problem and NOS handle it by dropping those observations.
- **Risk arbitrage forces a 13D:** "The SEC has established that risk arbitrageurs who acquire target shares following announcement of a tender offer for the purpose of tendering or exchanging the stocks in the merger are not eligible to file form 13G but must file the 13D form" (printed p. 10, citing the Faith Colish SEC No-Action Letter, 24 March 1980). This is their argument that a 13D is a *contaminated* proxy for activist intent — hence their preference for proxy-contest filings.
- **Rule 14a-8** allows shareholder proposals but management may exclude proposals nominating directors or directly conflicting with management policy; such proposals are usually only advisory. Proxy access rules under amended Rule 14a-8 took effect **from 2012** and so do not apply to the sample; **Rule 14a-11 was vacated by the D.C. Circuit in July 2011** (printed pp. 3, 8). Consequence: "In our sample, proxy contests are the only means of nominating alternative directors."
- **Rule 14a-12** permits soliciting before the proxy statement is filed (printed p. 8, n. 6).
- **EDGAR mandatory from 6 May 1996**; the low event counts in 1994–95 are an artefact of voluntary filing (printed pp. 8, 10).
- **Decimalization** on NYSE, AMEX and Nasdaq in **2001** — used only as the time component of an instrument, dummy = 1 from 2001 onward.
- Data sources: EDGAR; CRSP; Hasbrouck's website (effective trading costs); Compustat; I/B/E/S; Thomson Financial CDA/Spectrum s34 for 13F institutional ownership; Thomson Reuters mutual-fund holdings + CRSP flows for the price-pressure proxy; Ken French's website for factors.

## 5. Referee-facing strengths / weaknesses

**Strengths:**
- **The costliness of the event is the point.** By restricting to contested proxy solicitations — and *removing* tender offers, bear hugs and friendly merger-related filings — NOS make sure the theoretical mechanism (activism is expensive; trading profits must cover it) actually applies to the events being counted. This is a sharper object than "a 13D was filed", and they say so, citing Gantchev (2013) that two-thirds of 13D filers never make any formal demand.
- **They see the trades.** Sections 3.2 and 4.4 are the paper's real contribution: 11,518 hand-collected transactions, 95% purchases, 54% of the eventual block bought in the year before the announcement, 8.5% average return on that capital. This is direct evidence for the accumulation channel rather than an inference from a filing choice.
- **Table 9 closes the loop.** Liquidity at t−3 predicts the *amount* accumulated, not just the *incidence* of activism. That is the mechanism test the theory literature had been asking for.
- **The overvaluation interaction is a genuine, signed prediction** from Kahn-Winton and Winton-Li, tested with four different proxies, all agreeing. A paper that only found "liquidity → more activism" would be much weaker.
- Year fixed effects with an explicit statement that identification is cross-sectional — an unusually honest framing of what the coefficient means.
- The instruments are documented in full, with a first stage, an overid test, and an exogeneity test **that the authors report even though it partly undercuts them**.

**Weaknesses / open flanks:**
- **The instruments are weak by their own numbers.** Correlations with Amihud liquidity of **0.05 and 0.10** are very low, and the Amihud IV coefficient jumps to a 237%-of-baseline effect — the classic weak-instrument blow-up. No first-stage F or Cragg-Donald statistic is reported anywhere; only z-values on individual instruments.
- **The exogeneity test contradicts itself across measures** (p = 0.214 Hasbrouck, p = 0.040 Amihud). A referee will ask which measure we are supposed to believe, and note that the IV is only "needed" under the measure for which the instruments are weakest.
- **"Other-industry average liquidity" is a shaky exclusion restriction.** Market-wide liquidity waves plausibly correlate with market-wide activism waves (funding conditions, the activist-capital cycle) — exactly the confound year fixed effects cannot absorb at the firm level once you use *cross-sectional* industry averages.
- **Reverse causality is deflected, not solved.** Liquidity at t−2 could still be driven by an activist quietly accumulating below 5% — precisely the behaviour the paper documents. Their own Table 8 says accumulation happens in the 252 days before announcement, which for a t−2 measure is close.
- **Selection on observed events.** Voice that succeeds privately, or that is threatened and never filed, is invisible. The paper concedes that private engagement may matter and that data on it do not exist (printed p. 10, n. 10).
- **Trade data are censored at 5% and chained across amendments**, so the 4.25%/54% figures are conditional on a 13D existing, i.e. on the activist having crossed 5%. Sub-5% campaigns are structurally missing.
- **No outcome.** The paper never asks whether the activism worked, what it did to price, or what it did to control. The dependent variable is "did a contested solicitation happen". *(Verifier: confirmed by executed grep — the words `premium` and `bidder` appear nowhere in the paper, and there is no event study, CAR, or abnormal-return outcome; "abnormal performance" appears only as a lagged control.)*
- **They remove the control-outcome events on purpose, and say why (added by verifier — n. 9, printed p. 10).** "Greenwood and Schor (2009) argue that documented positive returns from hedge funds' activism are driven by their profits from takeover-related strategies. Hence, we should expect a non-negligible fraction of hedge funds' 13D filings to relate to such investments and we exclude from our sample all events related to (friendly or hostile) mergers." **This is the single most useful sentence in the paper for our positioning**: the leading empirical statement of "liquidity causes voice" is built on a sample from which the takeover channel has been deliberately excised, on the stated ground that the takeover channel is where the returns are. Our object is exactly the thing they cut out.
- Minor: the reference list miscites Amihud (2002) to the *Journal of Accounting and Economics* (it is the *Journal of Financial Markets*) — harmless, but a sign the WP was not final.

## 6. What they do NOT do (scope boundary)

- **Object.** Incidence of a contested proxy solicitation, and the size of the activist's pre-announcement stake accumulation. **No announcement return, no takeover premium, no bidder entry, no campaign win/loss, no post-campaign performance.** They say so directly: "Rather than focusing on the effectiveness of activism and its effect on firm valuation, we investigate the impact of stock liquidity on shareholders' incentives to take an active role in the first place." (printed p. 6).
- **Margin of the disclosure rule: none is treated.** The 5% threshold and the 13D Item-5 60-day transaction history are used purely as a **data-generating device**. There is no variation in the threshold, and **no variation in the filing window** — the 10-business-day window is never mentioned as an object of study, and the 60-day look-back is treated as a fixed feature of the form. The disclosure rule is scenery, not treatment.
- **Identification.** Cross-sectional probit with year FE plus an IV-probit. **No difference-in-differences, no event study, no structural estimation, no theory of their own** — the hypotheses are lifted from Maug (1998), Kahn-Winton (1998) and Winton-Li (2006). Decimalization enters only as one leg of an instrument, never as a shock analysed in event time.
- **Exit is not measured.** They study "the choice between voice and no-governance using a sample of investors identified by their observed election of voice" (printed p. 5). The exit channel is discussed in the literature review only.
- **They explicitly decline to treat a 13D filing as an activism event** for their purposes: "A 13D filing is therefore a less suitable definition of an activist event for our purposes because the mechanism that we test in this paper necessitates a high cost of activism." (printed p. 5).
- **They explicitly do NOT claim a contradiction with Edmans-Fang-Zur.** "The apparent contradiction of this result with our findings is due to differences in empirical design." (printed p. 4). They reconcile: EFZ estimate a *relative* effect conditional on a block; NOS estimate an *unconditional* effect on costly voice, and note their result is consistent with EFZ's Table 6 (unconditional 13D probability rising in liquidity).
- **Informal / private engagement is out of scope and acknowledged as such** (printed p. 10, n. 10).

## 7. Implications for our position

**Where NOS sit:** object = *incidence of costly voice* + *pre-event accumulation*; margin = **none — the disclosure rule supplies the data, not the variation**; identification = cross-sectional probit with year FE + IV-probit with two weak instruments. They own the *accumulation* mechanism on the liquidity axis and leave the entire disclosure-rule margin axis empty.

1. **This is the paper that names our mechanism out loud.** "Liquidity lets the activist buy at a price that does not yet reflect his own intervention" is exactly the force that makes our public-voice action attractive when κ is high. NOS is the empirical citation for that force existing; Maug (1998) is the theoretical one. Cite both, and be precise that NOS measure *accumulation*, not *profit from control*.
2. **Together with EFZ they bracket the sign, and the bracket is not a contradiction.** EFZ: κ↑ ⇒ tilt away from 13D *conditional on a block*. NOS: κ↑ ⇒ more *costly proxy voice* unconditionally. Both are consistent with EFZ's own Table 6. Our model must reproduce all three facts at once; if it cannot, we have the wrong core model, and a referee who knows this literature (this is Edmans's own field) will find it. NOS spell out the reconciliation on printed pp. 4–5 — that passage is worth reproducing in our literature section because it saves us the argument.
3. **R11 is the closest thing in the literature to a direct estimate of our κ → accumulation channel**, and it is quantitatively small in coverage: N = 232 in the tightest specification, t = 2.07. A referee could reasonably ask whether the whole accumulation channel rests on ~200 firms. That fragility is an argument for our anchoring on the *rule* rather than on liquidity: the Feb-2024 window change gives a much larger and cleaner treated population than 232 hand-collected campaigns.
4. **Their censoring problem is our threshold margin.** NOS lose 88 events because the activist held under 5% and therefore never had to report trades. That is not a nuisance — it is the **threshold margin doing exactly what our model says it does**: partitioning the world into flagged and pooled states, with the pooled state unobservable. We can cite their footnote as institutional evidence that the threshold *creates* the partition, and note that their data limitation is our economic object.
5. **The 60-day Item-5 transaction window is the empirical handle for our window margin.** NOS (printed p. 12) and Collin-Dufresne & Fos both rely on it. If our empirical leg wants to measure how much accumulation happens *inside* the filing window, this is the field that carries it. Worth flagging to the empirics ticket: the Item-5 look-back is 60 days, which is *longer* than either the old 10-business-day or the new 5-business-day filing window, so the window change is observable inside a single filing's own transaction table.
6. **Do not overclaim their identification.** They do not have a natural experiment. Their decimalization use is an *interacted instrument*, weaker than EFZ's already-weak reduced form. Positioning line: the liquidity × activism literature has never had clean exogenous variation in the *rule*; it has only ever had contested variation in *liquidity*. That is the whitespace.
7. **The whitespace is not merely unoccupied — NOS cut it out by hand (added by verifier).** Their n. 9 (printed p. 10) excludes *all* merger-related events because Greenwood–Schor (2009) show activist returns are driven by takeover-related strategies; their event funnel then drops a further 118 tender-offer and bear-hug solicitations (Q2). Yet Table 1 Panel C shows **34.3% of the surviving campaigns still state sale of the company as a purpose and 18.4% state removal of a takeover defence** (printed p. 35). Two positioning lines follow, and they are stronger than "nobody has done it": (i) the leading liquidity → voice estimate is identified off a sample from which the control channel was deliberately removed, on the stated ground that the control channel is where the returns are; (ii) even so, control objectives are stated in a third of the remaining events, so the two channels are not cleanly separable in the data — which is an argument for modelling them jointly, as we do, rather than for another sample split.
8. **Version risk.** These are the CCGR WP numbers (April 2014). The RFS article (28(2), 486–520, 2015) is a year later and went through referee rounds where the weak-instrument issue would have been raised. **Re-check every magnitude against the RFS version before it enters draft_v3.**

## 8. Quotes we may lean on (verbatim, page-cited)

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "We identify 385 shareholder activist events, for which the majority (87 percent) are filings concerning proxy contests and the rest are related to shareholder proposals or other types of disputes." | printed p. 2 (PDF p. 4) | Sample and the object they count |
| Q2 | "We identify 118 such events, leaving us with 385 activist events." | printed p. 9 (PDF p. 11) | The exclusion of takeover-related solicitations — i.e. control outcomes are deliberately removed |
| Q3 | "Our main measure of liquidity is the effective trading cost measure of Hasbrouck (2009) multiplied by −1." | printed p. 13 (PDF p. 15) | Their κ proxy — Hasbrouck, not Amihud |
| Q4 | "For the specification in column (2), such an increase in liquidity generates a statistically significant 0.40 percentage points increase in the likelihood of activism." | printed p. 17 (PDF p. 19) | The baseline marginal effect |
| Q5 | "The likelihood increases from 0.33 to 0.73 percent points for the 10th and the 90th percentile respectively." | printed p. 17, n. 12 (PDF p. 19) | The 0.33 → 0.73 figures — **baseline probit, not IV** |
| Q6 | "the unconditional probability of activism in the sample is only 0.56%" | printed p. 17 (PDF p. 19) | The base rate the effect is scaled against |
| Q7 | "Rule 13D-1(a) of the Securities and Exchange Act requires active investors to file with the SEC to disclose the acquisition of more than 5% of any class of securities of a publicly traded company. The Schedule 13D filing includes trading dates, prices and quantities traded during the 60 day period before the filing date." | printed p. 12 (PDF p. 14) | Institutional fact: the threshold, and the Item-5 60-day transaction history that makes trade-level activist data possible |
| Q8 | "For each target firm, we search back in time for the 13D filing that is closest to the activism announcement date." | printed p. 12 (PDF p. 14) | Their chaining procedure; the observability window is filing-driven |
| Q9 | "The SEC has established that risk arbitrageurs who acquire target shares following announcement of a tender offer for the purpose of tendering or exchanging the stocks in the merger are not eligible to file form 13G but must file the 13D form." | printed p. 10 (PDF p. 12) | Institutional fact: 13D is not a pure activism signal — a caution for any 13D-based design of ours |
| Q10 | "However, Gantchev (2013) documents that two-thirds of 13D-filing blockholders never go on to make any formal demands to their target." | printed p. 5 (PDF p. 7) | The gap between filing a 13D and paying the cost of voice |
| Q11 | "The apparent contradiction of this result with our findings is due to differences in empirical design." | printed p. 4 (PDF p. 6) | The NOS-vs-EFZ reconciliation, in their own words |
| Q12 | "The second column shows that shareholder activists trade in the target firm prior to the activism announcement in 76% of the 259 cases." | printed p. 25 (PDF p. 27) | Pre-event accumulation is the norm, not the exception |
| Q13 | "activist shareholders that trade in the target firm, on average acquire a total of 4.25% of the target firm's outstanding shares during the 252-day period prior to the announcement. This makes up 54% of the activist's holdings at the time of the announcement." | printed p. 26 (PDF p. 28) | The size of pre-flag accumulation |
| Q14 | "Using the Hasbrouck (2009) measure of liquidity, we cannot reject the null that liquidity is exogenous (p-value of 0.214). However, using the Amihud (2002) measure, this null is rejected (p-value of 0.04)." | printed p. 46 (PDF p. 48) | Their own exogeneity test, and its inconsistency across measures |

## 9. Verification log

*(Filled by the verifier.)* Q1–Q14 were located by exact substring match against `research/txt_extracts/norli2015_layout.txt` (a `pdftotext -layout` re-extract of `research/txt_extracts/norli2015.pdf`, page-marked) at the PDF pages stated; Q13 contains typographic apostrophes in "firm's" and "activist's". Printed-page mapping (printed = PDF − 2) verified at PDF pp. 3, 4, 6, 7, 11, 12, 14, 15, 19, 27, 28, 39, 48. Table values in §3 read from Tables 3–9 and B.1 at PDF pp. 39, 40, 41, 42, 43, 44, 45, 49.

### Verifier pass (adversarial, 2026-08-19)

Source of truth: an **independent** per-page re-extract of `research/txt_extracts/norli2015.pdf` built by the verifier (`pdftotext -f N -l N -layout`, 53 pages), not the reader's file. Quote matching was whitespace- and hyphenation-normalised. Printed-page mapping **printed = PDF − 2** independently re-confirmed by reading the page-foot folio on PDF pp. 3, 4, 6, 7, 10, 11, 12, 14, 15, 19, 27, 28, 36, 37, 39–45, 47, 48, 49.

**Counts: 14 quotes OK, 0 WRONG, 0 MISCITED, 0 UNCHECKED. 12 results OK on every number. 0 scope claims refuted; 4 omissions added.**

| Item | Status | Checked against |
|---|---|---|
| Q1 | OK | PDF p. 4 = printed p. 2 |
| Q2 | OK | PDF p. 11 = printed p. 9 (end of the sample funnel) |
| Q3 | OK | PDF p. 15 = printed p. 13 |
| Q4, Q5, Q6 | OK | PDF p. 19 = printed p. 17. Q5 is footnote 12, attached to the column-(2) sentence — attribution in the card is exactly right |
| Q7 | OK | PDF p. 14 = printed p. 12 |
| Q8 | OK | PDF p. 14 = printed p. 12 |
| Q9 | OK | PDF p. 12 = printed p. 10 (Faith Colish No-Action Letter is n. 8 on the same page) |
| Q10 | OK | PDF p. 7 = printed p. 5 |
| Q11 | OK | PDF p. 6 = printed p. 4 |
| Q12 | OK | PDF p. 27 = printed p. 25 |
| Q13 | OK | PDF p. 28 = printed p. 26 |
| Q14 | OK | PDF p. 48 = printed p. 46 (Appendix B) |
| **DECISION-CRITICAL: 0.33 → 0.73 is the BASELINE probit, Table 3 col. (2), 10th vs 90th percentile, +0.40 pp, against a 0.56% base rate** | **OK — confirmed on all four elements** | Table 3, PDF p. 39: col. (2) L(t−2) = 10.27 (3.30), N = 63,396, 354 events, pseudo-R² 0.027, "Change in probability … 0.40 (0.000)", "Change relative to sample probability of activism 71.2%". Body text PDF p. 19 gives "0.40 percentage points" for column (2) and "the unconditional probability of activism in the sample is only 0.56%"; n. 12 on the same page gives "0.33 to 0.73 percent points". The 0.33/0.73 pair appears **only** in that footnote and **only** for the baseline. The card's warning against reporting it as an IV result is correct |
| R1 | OK | Table 3, PDF p. 39. Col. (1) 12.77 (4.81), N = 63,555, 355 events, R² 0.029, Δ 0.47 (0.000), 84.9% — all match |
| R2 | OK | See decision-critical row above |
| **DECISION-CRITICAL: IV +0.79 pp (Hasbrouck) / +1.36 pp (Amihud)** | **OK** | Table 4 col. (2), PDF p. 40: IV Liquidity(t−2) 19.2 (2.5), N = 62,025, 349 events, Δ 0.79 (0.043), 142.3%. Table 5 col. (4), PDF p. 41: IV Amihud 4.6 (4.9), N = 57,689, 346 events, Δ 1.36 (0.084), 237.2% |
| R4 | OK | Table 4 cols. (1),(3),(4), PDF p. 40 — 5.9 (2.3)/0.25/44.2%, 8.1 (3.2)/0.28/49.6%, 0.2 (3.4)/0.28/50.1% |
| R5 | OK | Table 5, PDF p. 41 — 0.9 (2.2), 1.2 (2.4), 0.7 (1.7), 4.6 (4.9) with the stated Δ, p-values and percentages |
| R6 | OK | Table 6 col. (1), PDF p. 42 — −1.86 (−3.6), 11.82 (3.9), Ai-Norton −0.06 (−2.2), 0.68 vs 0.33, diff 0.36 (0.035), N = 63,396, 354 events |
| R7 | OK | Table 6 cols. (2)–(4), PDF p. 42 — every coefficient, z, probability pair, difference and p-value matches |
| R8 | OK | Table 7, PDF p. 43 — avg interaction −0.01/−0.08/−0.01/−0.01 (z −1.8/−2.1/−1.9/−1.9); differences 0.10, 0.10, 0.10, 0.08 with p 0.146, 0.048, 0.095, 0.043 |
| **DECISION-CRITICAL: primary measure = Hasbrouck effective cost ×(−1); Amihud is robustness** | **OK** | Q3 (printed p. 13) plus the table titles: Table 3 "using the Hasbrouck (2009) effective trading cost measure"; Table 5 "using the Amihud (2002) trade impact measure" appears under §4.2 Robustness checks (printed p. 19). The card's warning that this differs from Edmans–Fang–Zur is correct |
| **DECISION-CRITICAL: 54% of the block bought in the year before announcement; 8.5% return** | **OK** | Table 8, PDF p. 44 (printed p. 42), row "All": 259 target firms, 76% w/trade, N = 11,518, 95% buys, mean $346k, median $16k, **4.25** percentage points acquired, **54%** of own block, mean profit **$1,563k**, **8.5%**. Hedge-fund row 143/88%/7,753/93%/$457k/$39k/4.89/61%/$2,117k/9.9% also matches |
| R11 | OK | Table 9, PDF p. 45 — Hasbrouck 40.98 (2.52) N = 311 R² 0.175, 40.97 (2.07) N = 232 R² 0.197; Amihud 3.75 (2.38) N = 298 R² 0.186, 3.93 (1.94) N = 221 R² 0.208 (the card omitted the two Amihud R²; added here) |
| R12 | OK as ASSERTED | printed pp. 3 and 27 — correctly labelled an inference, not an estimate |
| **DECISION-CRITICAL: the 13D Item-5 60-day transaction table as data source** | **OK** | Q7 verbatim at PDF p. 14 = printed p. 12, plus the chaining procedure (Q8) and the sub-5% censoring discussion on printed pp. 12–13 |
| §2 sample funnel 8,783 → 998 → −174 → −135 → −98 → −88 → 503 → −118 → 385 | OK | printed pp. 8–9 (PDF pp. 10–11), verbatim; arithmetic checks (998 − 495 = 503; 503 − 118 = 385) |
| §2 trading sub-sample 197 with trades / 157 without / 88 sub-5% / 7 unknown / 259 remaining / 11,518 trades | OK | printed pp. 12–13 (PDF pp. 14–15) |
| §2 IV instrument correlations 0.26, 0.27 (Hasbrouck) and 0.05, 0.10 (Amihud); overid p = 0.430 / 0.841; Wald exogeneity p = 0.214 / 0.040; first-stage coefficients | OK | Appendix B, PDF p. 48 = printed p. 46, and Table B.1, PDF p. 49 = printed p. 47. All eight numbers match the print exactly |
| §2 "sales rather than market cap because sales do not move with the stock price" | OK | Appendix B, PDF p. 47 = printed p. 45, verbatim justification |
| §4 Rule 14a-11 vacated by the D.C. Circuit, July 2011 | OK | n. 4, PDF p. 5 = printed p. 3 |
| §4 amended Rule 14a-8 effective from 2012; "proxy contests are the only means of nominating alternative directors"; EDGAR mandatory 6 May 1996 | OK | PDF p. 10 = printed p. 8 |
| §4 0.56%, ~28 events/year, annual range 0.11%–0.83%, low 1994–95 counts an EDGAR artefact | OK | PDF p. 12 = printed p. 10 |
| §5 Amihud (2002) miscited to the *Journal of Accounting and Economics* | **OK — confirmed** | Reference list: "Amihud, Y., 2002, … Journal of Accounting and Economics, 5, 31–56." (correct venue is *Journal of Financial Markets*) |
| §5 "no first-stage F or Cragg-Donald statistic reported anywhere" | **OK — confirmed by executed grep** (`Cragg`, `F-statistic` return zero hits), and now **explained**: the estimator is ML, so Table B.1 is a display first stage. Card text amended |
| §6 "no takeover premium, no bidder entry, no announcement return, no campaign win/loss" | **OK — confirmed by executed grep** | `premium` and `bidder`: **zero hits**. `takeover` appears only in the bear-hug exclusion passage, n. 9, Table 1 Panel C purpose rows, and two reference titles. No `CAR`, no event study, no abnormal-return outcome |
| §6 "no variation in the filing window; the 10-business-day window is never mentioned" | **OK — confirmed by executed grep** | `10 days`, `ten days`, `business day` all return **zero hits** in the full 53-page text. Only the 60-day Item-5 look-back appears |
| §6 EFZ reconciliation (Q11 and the "consistent with EFZ Table 6" reading) | OK | printed pp. 4–5 (PDF pp. 6–7), read in full. NOS state their result "is consistent with a second result provided by EFZ, which shows that higher liquidity increases the (unconditional) probability that hedge funds file a 13D against the alternative of not filing" |
| Header: CCGR WP No. 1/2014, cover dated April 2014, back-matter contents listing "April 2013" | **OK — the internal inconsistency is real** | PDF p. 1 cover reads "No. 1/2014 … April 2014"; PDF p. 52 contents entry for 1/2014 reads "April 2013" |
| Header: published as *RFS* 28(2), 486–520 (2015) | **UNCHECKED** | Not verifiable from the PDF in hand — the WP carries no publication note. Low stakes (the card already treats every magnitude as WP-only and flags version risk), but the venue/volume line is an external claim |

**Omissions added by the verifier** (each material to a liquidity × disclosure-rule × control-outcome position):
1. **§2 — Table 1 Panel C, printed p. 35:** the stated purposes of the 385 campaigns include **sale of target assets or of the target company in 34.3%** of events and **removal of a takeover defence in 18.4%**. The card previously reported only "83% propose alternative directors". The surviving events are not control-free.
2. **§5 — n. 9, printed p. 10:** NOS exclude *all* merger-related events precisely because Greenwood–Schor (2009) show activist returns come from takeover-related strategies. The takeover channel is cut out of the sample by design and by stated intent.
3. **§7 item 7 (new):** the two facts above, turned into positioning lines — the whitespace was excised by hand, and control objectives survive in a third of the events anyway, which argues for modelling the channels jointly rather than splitting the sample again.
4. **§2 / §5 — printed p. 46:** the IV-probit is estimated by **maximum likelihood**, with Table B.1 a display-only "first stage"; and Table B.1's sample sizes (60,728 / 58,957) do not match the IV columns they underlie (62,025 / 57,689).

**Nothing decision-critical went unchecked.** The one UNCHECKED item is the published-venue line in the header (RFS 28(2), 486–520), which the PDF cannot confirm; it does not bear on any magnitude, and the card already flags that every number is the WP's.

**Overall verdict: the card is accurate, and unusually careful on the one number most likely to be misquoted.** Zero WRONG quotes, zero WRONG results, one explanatory correction (ML IV-probit), four omissions added. All five decision-critical claims — 0.33 → 0.73 as baseline not IV, the IV magnitudes, Hasbrouck as primary, the 54% / 8.5% accumulation figures, and the Item-5 60-day table as the data source — survive adversarial checking against the print.

## 9b. Published-version check (RFS 28(2), 486–520) — added by supplement reader, 2026-08-19

Source of truth: a per-page `pdftotext -layout` re-extract of
`research/txt_extracts/norli_ostergaard_schindele_2015_rfs_published.pdf` (35 PDF pages), read end
to end. **Published RFS page = PDF page + 485.** Quote matching was whitespace-, hyphenation- and
punctuation-normalised and run as an executed script, not by eye.

**Headline: this is the cleanest of the three re-basings. Every number in §3 survives to the digit.
No table was renumbered, no table was added or dropped, no sample changed. The paper the referees
saw is the paper the WP already was.**

**Decision-critical answer to the verifier's question: NO, there is still no first-stage F-statistic.**
The IV-probit is still estimated by maximum likelihood, and Table B.1 is still a display-only
"first stage" — the published Appendix B (p. 517) carries the WP sentence verbatim: "The
coefficients are estimated simultaneously by maximum likelihood, but we present the results from a
'first-stage' regression in which the endogenous variable, liquidity, is regressed on the
instruments and all other exogenous variables in Table B.1." Executed grep over the full 35-page
extract for `F-statistic|Cragg|weak instrument` returns **zero hits**. So §5's criticism stands
against the published article, and it must be phrased as the card already phrases it — the
estimator does not produce an F, rather than "they forgot to report one".

**The Table B.1 sample-size inconsistency the verifier found in the WP survives into print.**
Table B.1 (p. 517) reports N = 60,728 (Hasbrouck) and 58,957 (Amihud) with 354 / 346 events, while
the IV columns it underlies — Table 4 col. (2) and Table 5 col. (4) — report N = 62,025 / 349
events and 57,689 / 346 events. Unexplained in the published version too.

**The venue line is now confirmed, closing the one UNCHECKED item in §9.** Title page: *The Review
of Financial Studies* 28(2), 486–520, 2015; doi:10.1093/rfs/hhu070; Advance Access publication
7 October 2014; © The Author 2014. Editor **Laura T. Starks**, executive editor David Hirshleifer,
one anonymous referee; **Alex Edmans is thanked in the acknowledgements** (p. 486) — worth knowing,
since the EFZ reconciliation in §1 is almost certainly a referee-round product.

### Table and structure map (WP → published)

**Unchanged throughout.** Tables 1–9, Table B.1, Figures 1–2, Appendix A (activist types) and
Appendix B (instruments) all keep their numbers and their contents.

| Object | RFS page |
|---|---|
| Abstract | 486 |
| §1 Relation to Existing Literature (EFZ and BJN reconciliation) | 489–491 |
| §2 Data and Sample Selection; funnel; Table 1 | 491–496 |
| §2.2 preactivism trading, 13D Item-5 procedure | 497 |
| Figure 1 (activism by year) / Figure 2 (net fraction traded, event time) | 495 / 498 |
| Table 2 (targeted vs non-targeted firm characteristics) | 501 |
| Table 3 (baseline probit, Hasbrouck) | 502 |
| Table 4 (Hasbrouck robustness incl. IV) | 504 |
| Table 5 (Amihud) | 506 |
| Table 6 / Table 7 (overvaluation interaction, Hasbrouck / Amihud) | 509–510 / 512 |
| Table 8 (preactivism trading descriptives) | 513 |
| Table 9 (liquidity → amount accumulated) | 514 |
| §4 Conclusion | 515 |
| Appendix A (activist types) / Appendix B + Table B.1 | 516 / 517–518 |

### Every §3 result → published version

| # | Verdict | Published location |
|---|---|---|
| R1 | **same** | Table 3, p. 502. Col. (1) L(t−1) 12.77 (4.81), N = 63,555, 355 events, pseudo-R² 0.029; col. (2) L(t−2) 10.27 (3.30), N = 63,396, 354 events, pseudo-R² 0.027. Every control coefficient also matches |
| R2 | **same — the 0.33 → 0.73 / +0.40 pp attribution is confirmed in print** | Table 3 bottom panel, p. 502: "Change in probability … 0.47 (0.000)" and "0.40 (0.000)"; "Change relative to sample probability of activism 84.9% / 71.2%". Body, p. 503: the +0.40 pp sentence for **Column (2)**, the 0.56% unconditional rate, and the 71.2%. Footnote 12 on the same page: "The likelihood increases from 0.33 to 0.73 percent points for the 10th and the 90th percentile respectively." **The 0.33/0.73 pair still appears only in that footnote and only for the baseline probit.** The card's warning against reporting it as an IV number holds |
| R3 | **same** | Table 4 col. (2), p. 504: IV liquidity(t−2) 19.2 (2.5), N = 62,025, 349 events, Δ 0.79 (p = 0.043), 142.3% |
| R4 | **same** | Table 4 cols. (1), (3), (4), p. 504: 5.9 (2.3) / Δ0.25 (0.018) / 44.2%; 8.1 (3.2) / Δ0.28 (0.002) / 49.6%; 0.2 (3.4) / Δ0.28 (0.000) / 50.1% |
| R5 | **same** | Table 5, p. 506: 0.9 (2.2) / Δ0.13 (0.023) / 22.1%; 1.2 (2.4) / Δ0.15 (0.012) / 26.4%; 0.7 (1.7) / Δ0.10 (0.079) / 17.3%; **IV Amihud 4.6 (4.9) / Δ1.36 (0.084) / 237.2%**, N = 57,689, 346 events |
| R6 | **same** | Table 6 col. (1), p. 509: interaction −1.86 (−3.6), level 11.82 (3.9), overvaluation proxy −0.08 (−2.7), Ai–Norton average interaction −0.06 (avg z −2.2), 0.68 (0.001) vs 0.33 (0.001), difference 0.36 (0.035), N = 63,396, 354 events. Body p. 510: "the effect is approximately halved" |
| R7 | **same** | Table 6 cols. (2)–(4), p. 509: −15.73 (−2.7) / −2.18 (−3.9) / −1.57 (−3.8); levels 13.33 (4.0) / 16.25 (4.20) / 11.21 (3.5); differences 0.23 (0.030) / 0.45 (0.013) / 0.20 (0.020) |
| R8 | **same** | Table 7, p. 512: average interaction effects −0.01 (−1.8), −0.08 (−2.1), −0.01 (−1.9), −0.01 (−1.9); differences 0.10 (0.146), 0.10 (0.048), 0.10 (0.095), 0.08 (0.043), N = 60,279, 346 events. Two of four still insignificant at 5% |
| R9 | **same** | Table 8 row "All", p. 513: 259 target firms, 76% with trades, 11,518 trades, 95% buys, mean $346k, median $16k |
| R10 | **same** | Table 8, p. 513: 4.25 percentage points acquired, 54% of own block, mean profit $1,563k, 8.5%. Hedge-fund row 143 / 88% / 7,753 / 93% / $457k / $39k / 4.89 / 61% / $2,117k / 9.9% |
| R11 | **same** | Table 9, p. 514: Hasbrouck 40.98 (2.52) N = 311 R² 0.175 and 40.97 (2.07) N = 232 R² 0.197; Amihud 3.75 (2.38) N = 298 R² 0.186 and 3.93 (1.94) N = 221 R² 0.208 |
| R12 | **same, still ASSERTED** | Intro p. 488 ("informed trading is a substantive driver behind the positive effect of liquidity on activism") and §3.4 close, p. 515. Correctly labelled |

### Every §8 quote → published version

Thirteen of fourteen survive; the changes are punctuation and one "percent"→"%".

| # | Verdict | RFS page and the published wording where it differs |
|---|---|---|
| Q1 | **changed (typography only)** | p. 487: "…the majority (**87%**) are filings concerning proxy contests, **and** the rest are related to shareholder proposals or other types of disputes." (WP: "87 percent", no comma) |
| Q2 | **same, verbatim** | p. 493 |
| Q3 | **same, verbatim** | p. 498 |
| Q4 | **same** (only "column"→"Column") | p. 503 |
| Q5 | **same, verbatim** | p. 503, footnote 12 |
| Q6 | **same, verbatim** | p. 503 |
| Q7 | **changed (punctuation only)** | p. 497: "…trading dates, **prices, and** quantities traded during the **60-day** period before the filing date." The 5%-threshold sentence preceding it is unchanged |
| Q8 | **same, verbatim** | p. 497 |
| Q9 | **same, verbatim** | p. 494 (Faith Colish No-Action Letter is footnote 8 on the same page) |
| Q10 | **same, verbatim** (the sentence now opens with "However," in a different position) | p. 490 |
| Q11 | **same, verbatim** | p. 489 |
| Q12 | **same, verbatim** | p. 512 |
| Q13 | **same, verbatim** | p. 513 |
| Q14 | **changed (one word)** | p. 518: "…However, using **Amihud's (2002)** measure, this null is rejected (p-value of 0.04)." (WP: "using the Amihud (2002) measure") |

### WP → published page map for the other cited passages

| Passage | WP printed p. | RFS p. |
|---|---|---|
| Sample funnel 8,783 → 998 → 503 → 385 | 8–9 | 493 |
| EDGAR mandatory 6 May 1996; Rule 14a-8; "proxy contests are the only means of nominating alternative directors" | 8 | 492 |
| Rule 14a-12 | n. 6, 8 | fn 6, 492 |
| Rule 14a-11 vacated, D.C. Circuit, July 2011 | n. 4, 3 | fn 4, 489 |
| Activism frequency 0.11%–0.83%, ~28 cases/year, 0.56% | 10 | 494 (Figure 1 on 495) |
| Table 1 Panels A–C (incl. 34.3% sale-of-company, 18.4% takeover-defence removal) | 35 | **496** |
| Greenwood–Schor exclusion of all merger-related events (WP n. 9) | n. 9, 10 | **fn 9, 494** |
| Risk-arbitrage 13D rule (Q9) | 10 | 494 |
| 13D Item-5 60-day transaction table (Q7) and the chaining procedure (Q8) | 12 | **497** |
| Sub-5% censoring: 197 with trades / 157 without / 88 sub-5% / 7 unknown / 259 remaining / 11,518 trades | 12–13 | **497** |
| Private engagement out of scope (WP n. 10) | n. 10, 10 | fn 10, 494 |
| "Rather than focusing on the effectiveness of activism…" (§6 scope) | 6 | **491** |
| "…choice between voice and no governance using a sample of investors identified by their observed election of voice" | 5 | **490** |
| "A 13D filing is therefore a less suitable definition of an activist event…" | 5 | **490** |
| EFZ reconciliation (Q11 and the "consistent with EFZ's unconditional result" reading) | 4–5 | **489–490** |
| Instrument construction, correlations 0.26 / 0.27 and 0.05 / 0.10, ML statement, Wald and Amemiya–Lee–Newey tests | 45–46 | **517–518** |
| Table B.1 | 47 | **517** |
| Amihud (2002) miscited to the *Journal of Accounting and Economics* | reference list | **reference list, 518 — the miscitation survives into the published RFS article** |

### What the published version ADDS (added by supplement reader)

1. **A much longer §1 "Relation to Existing Literature" (pp. 489–491), and it is the part of this
   paper most useful to us.** The WP's short EFZ paragraph becomes two full pages that (i) restate
   EFZ's design, (ii) give the reconciliation in two distinct forms — if voice and threat-of-exit
   are **not substitutes**, "investors' selection of one does not imply rejection of the other"; and
   if blocks are accumulated for non-governance reasons, EFZ's result "implies that liquidity has a
   relatively stronger effect on investment in undervalued firms than it has on the likelihood of
   voice" (p. 490) — and (iii) add an entirely new discussion of **Bharath, Jayaraman & Nagar (2013)**,
   concluding that "threat of exit and voice are distinct and concomitant governance mechanisms"
   (p. 491). **This is the literature's own statement that the two channels coexist rather than
   trade off, published in RFS, and it is the strongest external support in hand for our
   four-action structure. Cite RFS pp. 489–491, not the WP.**
2. **Footnote 7 (p. 493) — a correction to how §2 describes the funnel.** Friendly negotiated
   mergers, tender offers and bear hugs are **not deleted from the estimation sample**; they are
   "kept in the sample as **nonactivism** events", i.e. recoded as zeros. The footnote adds that
   "removing these cases from our analysis altogether has no effects on the results", and that
   keeping them is the conservative choice under the null. **§2's funnel wording ("−88 … −118 …")
   should be read as event-definition steps, not sample deletions.**
3. **A stated filing-sequence rule with a count** (p. 493): a gap of more than one year in a filing
   sequence starts a new intervention, and this "occurs in 20 cases, representing about 2% of our
   filing sequences."
4. **Figure 2 is trimmed** (p. 498): the ten largest trades are dropped for the graph, so the figure
   uses 11,508 of the 11,518 trades. The tables still use all 11,518.
5. **A short-sale-constraint reading of Table 6 col. (3)** (p. 511) that the WP card does not carry
   and that matters for our exit channel: low institutional ownership proxies for short-sale
   constraints, and the liquidity effect on voice is smaller there — "By itself, this result is also
   consistent with Edmans (2009)… **However, all our other proxies for overvaluation have similar
   effects** as the proxy for short-sale constraints. This is consistent with Kahn and Winton (1998)
   and Winton and Li (2006), but not with Edmans (2009), and suggests that our results are indeed
   driven by a diminished incentive for voice rather than by threat of exit." **This is NOS
   explicitly ruling out the exit interpretation of their own interaction result** — useful if we
   want to claim the two papers measure different margins rather than the same one.
6. **A new closing line on trading venues** (p. 515): fragmentation of equity trading across new
   venues is offered as the reason the liquidity–activism link will keep mattering. NOS's implied
   policy lever, like EFZ's, is **market structure — not the disclosure rule.** Same positioning
   contrast as EFZ, from the other side of the literature.

### What the published version DROPS

Nothing material. No result, table, quote or institutional fact in §§1–8 is absent from the
published article.

### §9 UNCHECKED items closed by the published version

| Item left open in §9 | Status now |
|---|---|
| Header: "published as *RFS* 28(2), 486–520 (2015)" — **UNCHECKED**, not verifiable from the WP | **CLOSED.** Confirmed from the article's own title page: RFS 28(2), 486–520 (2015), doi:10.1093/rfs/hhu070, Advance Access 7 Oct 2014 |
| §7 item 8 "version risk — re-check every magnitude against the RFS version before it enters draft_v3" | **CLOSED.** Every magnitude re-checked; all identical. **§7 item 8 can be struck** |
| "no first-stage F or Cragg-Donald statistic reported anywhere" — verified for the WP | **CLOSED and unchanged in print.** Zero hits for `F-statistic|Cragg|weak instrument` in the published article; the ML explanation is printed at p. 517 |
| §6 "no premium, no bidder, no announcement return, no campaign outcome" — verified for the WP | **CLOSED and unchanged in print.** Executed grep over the published article: `premium` and `bidder` return **zero hits**. There is still no event study, CAR, or outcome variable of any kind |
| §6 "no variation in the filing window; the 10-business-day window is never mentioned" | **CLOSED and unchanged in print.** `10 days`, `ten days`, `business day`, `filing window`: **zero hits** in the published article. Only the 60-day Item-5 look-back appears. **The window margin is still untouched by the leading liquidity → voice paper** |
| Table B.1 N mismatch (60,728 / 58,957 vs 62,025 / 57,689) | **CLOSED as a finding, not fixed.** The inconsistency is in the published article too |
| Amihud (2002) miscited to *J. Accounting and Economics* | **CLOSED as a finding, not fixed.** The miscitation is in the published reference list, p. 518 |

### Still open after this pass

Nothing. There is no online appendix and no supplementary material for this article; every claim in
the card is now checked against the published text.
