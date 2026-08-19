# Collin-Dufresne & Fos (2015) — "Do Prices Reveal the Presence of Informed Trading?"

**Venue / status:** *Journal of Finance* 70(4), 1555–1582, August 2015. Editor: Bruno Biais. Initial submission 31 August 2012; final version received 27 January 2015.
**Two versions read — read BOTH, and they differ on sample and on headline magnitudes.** The published version's **Internet Appendix** (`research/txt_extracts/collin_dufresne_fos_2015_internet_appendix.pdf`, 36 printed pages) was added and read on 2026-08-19 — see **§9b**.
- **PRIMARY: the published JF article**, `research/txt_extracts/collin_dufresne_fos_2015_jf.pdf` (28 pp, printed 1555–1582; a UCL Wiley download). This file landed on disk during this reading task; page-marked re-extract at `research/txt_extracts/cdf_jf_pages.txt` (`pdftotext -layout`). **Sample: 1994–2010, 19,026 Schedule 13D filings screened down to 3,126 events.**
- **SECONDARY: NBER Working Paper No. 18452, October 2012**, `research/txt_extracts/cdf_fos_jf2015.pdf` / `.txt` (50 pp); page-marked re-extract at `research/txt_extracts/cdf_fos_wp_layout.txt`. **Sample: 2001–2010, 9,580 filings → 1,725 events, ~173 events per year.**
- The task brief assumed only the WP was in hand and warned the published sample might differ. **It does.** Every magnitude below is tagged `[JF]` or `[WP]`. Where the internal notes carry a CDF number, check which version it came from before using it.
· **Reader:** opus · **Read:** full text of both versions (JF: all 28 pages, Tables I–IX, Figures 1–2, references; WP: sample-construction and announcement-return sections read in full, remainder skimmed for divergence)
**Page numbering used below:** for the JF version, the **printed journal page** (1555–1582); mapping to the PDF is printed = PDF page + 1554. For the WP, the working paper's own printed page; mapping is printed = PDF page − 1. Every citation says which version.
**Type:** empirical (market microstructure) **Role for us:** anchor (the institutional and trade-level evidence on what happens *inside* the disclosure window) and measurement — **not** a competitor on our object

## 1. Question

Do the standard empirical measures of adverse selection — Kyle's λ, PIN, price impact, effective and realized spreads, Amihud illiquidity — actually go *up* when informed traders are in the market, as Glosten-Milgrom and Kyle imply they should? The obstacle is that you normally cannot label a trade as informed ex ante. CDF solve this with a disclosure rule: Schedule 13D filers must retroactively publish their own transactions, and their information (they intend to change the firm) is demonstrably valuable and long-lived. So the paper is a test of a *measurement* premise in microstructure, using activist accumulation as the laboratory.

## 2. Model / data and method

**Design:** within-event comparison of daily liquidity measures on days the activist trades vs days he does not, inside the 60-day pre-filing disclosure window; plus a matched-stock difference-in-differences; plus event-fixed-effect panel regressions; plus two market-structure reforms used as splits. No structural estimation; the theory is outsourced to companion papers.

**Two companion theory papers, not one (added by verifier).** The card previously named only the first:
- **Collin-Dufresne & Fos (2014), "Insider trading, stochastic liquidity, and equilibrium prices"** — the Kyle extension with stochastic noise-trading volatility, cited at JF pp. 1557 and 1568 as the source of the *timing-selection* mechanism. (Published *Econometrica* 84(4), 2016.)
- **Collin-Dufresne & Fos (2015 WP), "Shareholder activism, informed trading, and stock prices"** — cited in **n. 4, JF pp. 1556–1557**, and much closer to our object: "a theoretical model in which activist shareholders can expend effort and change firm value. In that model the market price depends on the market maker's estimate of the activist's share ownership, since the latter determines the effort level of the informed trader, and hence the liquidation value of the firm. This model shows that a significant part of the valuable private information pertains to the activist's own holdings, which by definition is information known only to him." **That last clause is our partition, in their words.** Anyone positioning against CDF must read this companion, not just the microstructure one.

**Sample construction [JF].**
- Automatic EDGAR script identifies **19,026 Schedule 13D filings from 1994 to 2010**; all are then checked manually for trade information.
- Filters: CRSP share codes 10 or 11 only (drops certificates, ADRs, shares of beneficial interest, units, non-US incorporations, Americus Trust components, closed-end funds, preferred stock, REITs); price between $1 and $1,000; no derivative-involving events (options, warrants, swaps); **13D/A amendments excluded** (only original filings, to maximise the asymmetric-information content).
- **Final sample: 3,126 events**, described as the universe of qualifying filings 1994–2010.
- **[WP contrast]:** the 2012 WP screened **9,580** filings over **2001–2010** to **1,725** events.
- Composition [JF]: **62% NASDAQ, 29% NYSE, 9% Amex**; roughly **25% of events fall in the financial-crisis period**.
- Other data: CRSP (returns, volume, prices), TAQ (intraday trades and quotes).

**The trade-level data — what the disclosure rule actually hands them.** From each filing they extract: CUSIP, transaction date, transaction type (purchase/sell), size, price, **plus the filing date, the event date (the day the 5% threshold is crossed), and beneficial ownership at filing**. Sub-daily transactions are aggregated to daily totals with quantity-weighted average prices.

**Outcome objects.**
1. **Six high-frequency liquidity measures:** Kyle's λ (slope of return on signed order flow), dollar-weighted price impact (`pimpact`), Hasbrouck cumulative impulse response (`cumir`), the trade-related component of the variance of changes in the efficient price (`trade-related`), dollar-weighted realized spread (`rspread`), dollar-weighted effective spread (`espread`). CDF classify λ, pimpact, cumir, trade-related (plus Amihud and PIN) as *adverse-selection* measures and rspread, espread, daily bid-ask spread as *other*. All winsorised at 99.9%.
2. **Three low-frequency measures:** Amihud (2002) illiquidity, daily bid-ask spread, **PIN** (Easley et al. 1996) — reported in the Internet Appendix in the JF version, in the body in the WP.
3. Market-adjusted returns (`eret`, excess of the CRSP value-weighted index), order imbalance, abnormal volume, and buy/sell-directional versions of λ, pimpact and rspread.

**Identification.** There is no instrument and no policy shock. What does the work is:
- **Within-event, within-window variation**: days the filer trades vs days he does not, both inside the same 60-day window, with event fixed effects and heteroskedasticity-robust SEs clustered by event.
- **Matched-stock difference-in-differences**: matches on Fama-French (1997) industry, exchange, market cap, and annual return volatility; a robustness match on market cap and share price following Davies-Kim (2009).
- **Two market-structure reforms as splits:** the **1997 NASDAQ Order Handling Rules reform** (before which non-dealers found it hard to post limit orders) and the **start of NYSE autoquoting in early 2003** — used to switch the limit-order channel on and off.
- **A within-window regulatory discontinuity: the event date.** Because the filer has at most 10 days to file after crossing 5%, his flexibility drops discontinuously at the event date. CDF compare pre-event-date to post-event-date behaviour. **This is the closest thing in the literature to a test of the filing-window margin, and it is a comparison of behaviour *within* the window, not a comparison across window lengths.**

## 3. Results — with honesty labels

Bracketed figures are t-statistics unless stated.

| # | Result (one line) | Label | Where |
|---|---|---|---|
| R1 | **Run-up vs jump [JF].** Buy-and-hold excess return over the CRSP value-weighted index: **run-up of about 3% from 60 days to one day prior to the filing date**; **two-day jump at the filing date of about 2.5%**; post-filing **drift cumulating to a total of 9%** | ESTIMATED (Figure 2; significance shown in Internet Appendix) | JF p. 1563 for the run-up and jump; the 9% drift figure is on **p. 1564** — the sentence runs over the page break (*page corrected by verifier*) |
| R2 | **Run-up vs jump [WP] — DIFFERENT.** Same figure on the 2001–2010 sample: **run-up of about 7%** over (t−60, t−1); **two-day jump of about 3%**; **drift cumulating to 13%**. Do not mix R1 and R2 | ESTIMATED | WP p. 14 (PDF p. 15) |
| R3 | **Windowed announcement returns [both versions agree].** Cumulative excess return **≈6% in the (t−10, t+1) window** and **≈3% in the (t−1, t+1) window** around the filing date | ESTIMATED | JF p. 1556; WP p. 3 (PDF p. 4) |
| R4 | **THE HEADLINE: measured adverse selection FALLS on days the activist buys.** λ averages **14.3311** on informed-trade days vs **20.1644** on no-trade days inside the same 60-day window: difference **−5.8334\*\*\*** [t = −8.38], **"almost 30% lower"**. Matched-stock difference **−0.8126** [−0.63]; **diff-in-diff −5.0208\*\*\*** [−4.05] | ESTIMATED | JF Table III, p. 1566; text p. 1567 |
| R5 | Same direction for every other measure [JF Table III]: pimpact 0.0060 vs 0.0064, diff **−0.0004\*\*** [−2.18]; cumir 0.0013 vs 0.0015, **−0.0002\*\*** [−2.06]; trade-related 0.0654 vs 0.0673, −0.0019 [−0.99] (n.s.); rspread 0.0081 vs 0.0089, **−0.0008\*\*\*** [−3.43]; espread 0.0145 vs 0.0155, **−0.001\*\*\*** [−3.25]. In the diff-in-diff column only λ, rspread (**−0.0012\*\*\***) and espread (**−0.0014\*\*\***) survive | ESTIMATED | JF Table III, p. 1566 |
| R6 | **Amihud falls too [WP only in the body].** "Amihud's illiquidity measure decreases by more than 45% on days when Schedule 13D filers trade." In the JF this and PIN are moved to the Internet Appendix, where **PIN behaves like the other adverse-selection measures — lower when informed trading takes place**. **IA magnitudes now confirmed:** Amihud (`illiquidity`) 0.2662 on filer-trade days vs 0.5191 on no-trade days, **−0.2529\*\*\* [−17.08] = −48.7%** (so the WP's "more than 45%" survives into the JF sample, though the JF IA never prints a percentage); DiD −0.2142\*\*\* [−6.09]. **PIN is a *window*-level result, never a trade-day one:** 0.4385 over (t−60,t−1) vs 0.4943 over (t−420,t−361), **−0.0559\*\*\* [−13.1]**, DiD −0.0257\*\*\* [−3.52]; the IA text says "pin is more than 9% lower" (arithmetically 11.3%) | ESTIMATED [WP]; **ESTIMATED [JF-IA] *(closed by supplement reader)*** | WP p. 4 (PDF p. 5); JF p. 1567; **IA Table IA.VI, IA p. 19** (Amihud, baspread) and **IA Table IA.VIII + text, IA pp. 20, 22** (PIN) |
| R7 | **Prices still move.** Market-adjusted return is **0.0064\*\*\*** on informed-trading days vs **−0.0004** on non-trading days; difference **0.0068\*\*\*, t = 9.94**. So the trades *do* have price impact — the adverse-selection statistics simply fail to see it | ESTIMATED | JF Table II, p. 1565 |
| R8 | **Panel regression with event FE [JF Table IV].** `itrade` coefficients: λ **−3.4602\*\*\*** [−11.20], pimpact **−0.0004\*\*\*** [−2.69], cumir **−0.0001\*\*\*** [−5.01], trade-related −0.0017\* [−1.71], rspread **−0.0008\*\*\*** [−5.95], espread **−0.0009\*\*\*** [−4.40], order imbalance **−0.0411\*\*\*** [−7.03] | ESTIMATED | JF Table IV, p. 1570 |
| R9 | **The window bites.** `postevent` (days between the event date and the filing date) coefficients are negative — λ **−1.2623\*\*** [−2.06] — i.e. filers **choose to cross 5% when liquidity is already high**. The interaction `itrade × postevent` is **positive** and significant for trade-related (**0.0047\*\***, [2.04]) and order imbalance (**0.0254\*\***, [1.98]); positive but insignificant for λ (0.4685), pimpact, rspread, espread. F-test γ₁+γ₃ = 0 rejected only for λ (p = 0.0000) and marginally cumir (p = 0.0588) | ESTIMATED | JF Table IV, p. 1570; text pp. 1569–1571 |
| R10 | **Limit orders.** Of **12,576** trades uniquely matched to TAQ, only **52.8%** of purchases are classified buy-initiated by Lee-Ready — implying heavy limit-order use. The share rises **from 51.5% before the event date to 56.3% after**, i.e. filers switch toward market orders once the 10-day clock is running. Under a 70%-accurate Lee-Ready classifier, Bayes gives limit-order use of **46.25%** before vs **34.25%** after | ESTIMATED | JF pp. 1572, n. 22 |
| R11 | **Order-type interaction [JF Table V Panel B].** `itrade × above_vwap_buy` (market-order proxy): pimpact **+0.0008\*\*\*** [3.63], trade-related **+0.0030\*\*** [1.96] — adverse-selection measures rise when market orders are likelier; rspread **−0.0014\*\*\*** [−7.59] and espread **−0.0007\*\*** [−2.38] fall; λ **−0.7673\*\*** [−2.29] falls, so **"λ behaves more like a liquidity measure than an adverse selection measure"** | ESTIMATED | JF Table V, p. 1574; text p. 1573 |
| R12 | **Selection on volume.** The empirical p-value of event-date volume against the stock's own history averages **79%\*\*\*** (vs 50% under the null), **78%** over (t−1, t), **75%** over (t−4, t), **72%** over (t−9, t), **67%** over (t−29, t); net of the filer's own trades still **67%/66%/64%/62%/60%**, all \*\*\*; and **matched stocks are at 57–58%\*\*\*** — so filers trade when market-wide liquidity is high, which their own trading cannot cause | ESTIMATED | JF Table VI, p. 1575 |
| R13 | **What predicts an activist trading day [JF Table VIII]:** contemporaneous CRSP volume **+0.0666\*\*\*** [2.73], lagged market return **−0.3872\*** to **−0.4592\*\*** (they buy after the market falls), own turnover **+3.2082\*\*\*** [14.79] contemporaneous and **+1.1699\*\*\*** [6.56] lagged; **lead** turnover only marginal, and matched-stock liquidity insignificant throughout | ESTIMATED | JF Table VIII, p. 1578 |
| R14 | **The limit-order channel is not the whole story.** On NASDAQ pre-1997 (before the Order Handling Rules reform, when limit orders were hard for non-dealers), `itrade` on λ is still **−3.8967\*\*\*** [−8.58] with `itrade × before` **−3.4217\*\*\*** [−2.63]; F-test on the pre-period sum rejects for λ (p = 0.0000) and rspread (p = 0.0310). Same conclusion from the NYSE autoquoting split (Internet Appendix) | ESTIMATED | JF Table VII, p. 1576; text p. 1577 |
| R15 | **Directional measures work where pooled ones fail.** Buy-initiated pimpact is **+0.0003\*** [1.83] on informed days while sell-initiated pimpact is **−0.0012\*\*\*** [−4.64]; rspread falls for both but far more for buys (**−0.0015\*\*\***  vs −0.0003\*). Matched stocks show nothing (all insignificant) | ESTIMATED | JF Table IX, p. 1579 |
| R16 | **Accumulation size [JF Table I].** Average (median) ownership at filing **7.51% (6.11%)**; the average (median) filer buys **3.8% (2.8%)** of outstanding shares in the 60 days before filing — **899,692 (298,807) shares** costing **$16.4 ($2.5) million**; on days with nonzero informed volume he buys **0.5% (0.2%)** of shares outstanding; informed trades are **31.5% (25.4%)** of daily turnover ("real PIN"); filers trade on **31.1%** of days. **[WP: ownership 7.68% (6.20%)]** | ESTIMATED (descriptive) | JF Table I, p. 1562; WP p. 10 |
| R17 | **Intensity peaks 10 days before filing.** Probability the filer trades at least one share on a given day is **≈25%, rising to 50% ten days prior to the filing date**; daily purchases rise from 0.03–0.05% of shares outstanding to **0.15–0.20%** near t−10, then fall back to 0.06–0.10%. On the event date itself the filer buys **close to 1%** of outstanding shares vs 0.10–0.15% on adjacent days | ESTIMATED (descriptive) | JF pp. 1560–1561, Figure 1 |
| R18 | **Who gains.** For an average event, the filer takes a **$22 million stake in a $293 million market-cap firm (the 7.51% average) and expects $0.8 million** ($0.4m on the 60-day trades, $0.4m on the pre-window position), while **shareholders gain $15 million**. **[WP: $1.13 million on a $30 million stake in a $404 million company]**. **IA table now read — the $293m firm is the *fourth* market-cap quintile, Q4:** Trading Profit **403,214\*\*\* [9.24]**, Total Profit **801,141\*\*\* [7.59]**, Value Created **15,000,273\*\*\* [5.56]**. Full ladder (Mkt Cap / Trading / Total / Value Created): Q1 19.8m / 43,998\*\*\* / 56,590\*\*\* / 908,857\*\*; Q2 52.9m / 104,907\*\*\* / 192,926\*\*\* / 2,607,513\*\*\*; Q3 120.0m / 216,250\*\*\* / 298,363\*\*\* / 4,226,135\*\*\*; Q5 1,346.3m / 907,584\*\*\* / 1,818,721\*\*\* / 33,239,501\*\*\*. **Definitional caution:** "Value Created" is `(p_post − p₀)·SHOUT` — value created for **all** shareholders including the filer, not "other shareholders"; the IA's own contrast is Q5 shareholders +$33m vs filers +$1.8m | ESTIMATED (Internet Appendix in JF) — **numbers now verified *(closed by supplement reader)*** | JF p. 1564; WP p. 3; **IA text pp. 11–12, 14; Table IA.IV, IA p. 13**; definitions eqs. (IA.1)–(IA.3) |
| R19 | The interpretation — that the two channels (timing selection and limit orders) *jointly* explain the anomaly, with neither sufficient alone — is the paper's synthesis of R9–R15 | ASSERTED (well supported) | JF pp. 1573, 1580 |
| R20 | **(added by verifier) The contamination is at the WINDOW level, not just the trade-day level.** Comparing average liquidity measures over the whole 60-day disclosure window (t−60, t−1) against the *same calendar window one year earlier* **(t−420, t−361)**: "none of the adverse selection measures indicate the presence of informed traders during the 60-day disclosure period. Instead, **four out of six measures indicate that adverse selection is significantly lower on average during the 60-day period**." Same conclusion under the diff-in-diff. This longer window is also what lets them estimate **PIN**, which is likewise lower when informed trading takes place. **The four are now named:** λ −3.3274\*\*\* [−3.36], cumir −0.0002\*\* [−2.16], illiquidity −0.0413\*\*\* [−4.12], pin −0.0559\*\*\* [−13.1]; pimpact (0.0000) and trade-related (0.0005) are the two insignificant ones. **DiD column:** λ −4.5788\*\* [−2.31], illiquidity −0.0726\*\*\* [−4.24], pin −0.0257\*\*\* [−3.52], rspread −0.0012\*\*\* [−2.74], baspread −0.0016\*\* [−2.32]; pimpact, cumir, trade-related, espread insignificant | ESTIMATED — **levels now read *(closed by supplement reader)*** | JF p. 1567; **IA Table IA.VIII, IA p. 22**, text IA pp. 20, 23 |
| R21 | **(added by verifier) Inside the window, the filer's trading tracks uninformed activity almost perfectly.** Closer to the event date both 13D trading and uninformed trading activity rise, peaking at the event date; the correlation between the two series is **80% over (t−60, t−1) and 96% over (t, t+9)**. And `itrade` coefficients are economically and statistically weaker after the event date, "consistent with the selection and limit order mechanisms being **less likely to operate during the postevent date period**" | ESTIMATED — **both correlations verbatim in the IA *(closed by supplement reader)*** | JF p. 1571; **IA p. 25** ("The correlation between the two series is 80% during the (t-60,t-1) period and 96% during the (t,t+9) period"); Figure IA.6, IA p. 27 |
| R22 | **(added by verifier) The announcement gain is permanent.** "there is no evidence of reversal in the buy-and-hold return during the 120-day period after the filing date" — so the filing-date jump is not price pressure. **IA now read:** Figure IA.5 runs (t−60, t+120); "we see that there is no reversal. The abnormal buy-and-hold return over the (t-40,t-120) period is slightly above 1%." Separately, Table IA.III gives the announcement return with t-stats: filing-date **1.12%\*\*\* [5.79]**, (t−1,t+1) **0.80%\*\*\* [7.77]**, (t−2,t+2) **0.49%\*\*\* [5.50]**, 121 daily observations each | ESTIMATED — **verified *(closed by supplement reader)*** | JF p. 1564, n. 13; **IA pp. 9–11, Table IA.III, IA p. 10** |
| R23 | **(added by verifier) The post-filing drift is an early-sample artefact [WP].** Most 13D filings become public within one day of filing, "with some exceptions in the early part of the sample when filings became public with a short delay. Such delays might explain the post-filing drift". Restricting to **2003–2010** (Figure 5 Panel B), "the post-filing drift in returns does not exist in the later part of the sample… there is no trend in the abnormal return after the filing date." The JF drops this discussion entirely | ESTIMATED | WP p. 15 (PDF p. 16) |

## 4. Institutional facts used

This is the paper in our reading list that leans hardest on the disclosure rule as *institution*, and its statements are the cleanest available for our anchor.

- **Threshold + window, stated together [JF p. 1556]:** "Rule 13d-1(a) requires investors to file with the SEC within 10 days of acquiring more than 5% of any class of securities of a publicly traded company if they have an interest in influencing the management of the company." (This is the pre-2024 10-day rule; the Feb-2024 acceleration to 5 business days is outside the paper's sample.)
- **The Item 5(c) 60-day transaction history — the source of all trade-level activist data [JF p. 1556]:** "Item 5(c) of Schedule 13D requires the filer to report the date, price, and quantity of all trades in the target company executed during the 60 days that precede the filing date." Quoted from the form itself in n. 3: filers must "… describe any transactions in the class of securities reported on that were effected during the past sixty days or since the most recent filing of Schedule 13D, whichever is less, …"
- **Three separate triggers for a 13D [JF p. 1559, n. 7]:** (i) an investor's position exceeds the 5% threshold; (ii) a group acting together exceeds 5%; (iii) **a previously established position changes by more than 1% of shares outstanding, either positive or negative**. CDF keep only original filings and drop 13D/A amendments.
- **"Event date" vs "filing date" is a formal distinction in the data:** the event date is the day ownership crosses 5%; the filing date is the day the form reaches the SEC; the 10 days separate them. CDF extract both.
- **Filers count the window in business days [JF p. 1561, n. 11]:** "we find that Schedule 13D filers often interpret the 10-day period in terms of business days and not calendar days. This is why event dates are clustered during the (t − 12, t − 9) period prior to the filing date." **This is a directly usable institutional fact for our window-margin work: the empirical event-to-filing gap is a business-day object, exactly as the 2024 rule text is.**
- **Information becomes public only at filing [JF p. 1563]:** "Only when they file with the SEC, 10 days after their holdings reach the 5% threshold, does the information become public." That is our *partition* stated as an institutional fact.
- **The window constrains behaviour [JF p. 1569]:** "Schedule 13D filers have at most 10 days to file with the SEC after the event date (the day when their ownership reaches 5%). Because of this time constraint, they have less flexibility with respect to their trading strategy after the event date."
- **Filings become public with a short lag [WP p. 14]:** hand-checking a representative sample shows most 13D filings become public within one day of filing, with exceptions in the early part of the sample. Relevant to any of our event-study timing (the T+1 confound on the referee checklist).
- **Market-structure dates used:** NASDAQ Order Handling Rules reform **1997**; NYSE **autoquoting from early 2003**; Reg NMS mentioned as having converged exchange structures.
- Data sources: EDGAR (13D filings and Item 5(c) transaction tables), CRSP, TAQ, Lee-Ready (1991) trade signing.

## 5. Referee-facing strengths / weaknesses

**Strengths:**
- **The identification of "informed" is institutional, not statistical.** They do not assume some trader type is informed; the law makes the trader label himself, retroactively, with dated transactions. That is a genuinely rare research asset and is why the paper is in the JF.
- **The comparison is within-event and within-window**, so it is not contaminated by cross-firm differences in liquidity or by the general level of activism.
- **They stress-test their own preferred mechanism.** The 1997 NASDAQ reform and the 2003 NYSE autoquoting splits are designed to *break* the limit-order explanation, and they report that the result survives — i.e. they argue against their own tidiest story.
- **The matched-stock volume result (R12) is the strongest single piece of evidence**: activists' own trading cannot raise the volume of matched stocks, so the 57–58% matched p-values are clean evidence of market-wide liquidity timing.
- Directional measures (R15) are a constructive contribution, not just a negative result.
- Sample is the *universe* of qualifying filings, not a convenience sample.

**Weaknesses / open flanks:**
- **Heavy reliance on the Internet Appendix.** PIN, Amihud, the announcement-return significance bounds, the profit calculations, the NYSE autoquoting test, the trade-matching procedure, and the market-order-proxy validation all live there. The card's R6 and R18 therefore rest on numbers we have not seen in the file we hold. **Flag: if a claim of ours depends on the Amihud or PIN result, the Internet Appendix must be fetched.**
- **Selection into the sample is severe and directional.** Only 13Ds *with* trade information survive — that is, only cases where the filer actively accumulated across the threshold. Their own n. 12 concedes this: "we restrict our sample to cases in which the Schedule 13D filer actively accumulates shares and crosses the 5% threshold." Quiet accumulators who stop below 5% are structurally invisible.
- **"Informed" is coarse.** A day is labelled informed if the filer traded at all; no intensity weighting in the main test.
- **The matched-stock DiD kills half the results.** In Table III column (5), pimpact, cumir and trade-related all lose significance. The robust survivors are λ, rspread and espread — and CDF themselves conclude that λ behaves like a liquidity measure rather than an adverse-selection measure (R11). A hostile referee can reframe the paper as "the two measures that survive are the two that were never adverse-selection measures".
- **No counterfactual window.** The post-event-date test (R9) is the only handle on the filing window, and it compares behaviour before vs after the event date *within* a fixed 10-day rule — it cannot say what a 5-day rule would do. The point estimates on the interaction are mostly insignificant.
- **The two channels are not separately quantified.** They are shown to both operate; no decomposition of how much of the −30% in λ each explains.
- **Version divergence is material; the drift half of it has a stated cause, the run-up half does not** *(corrected by verifier — the card previously said "neither version discusses this", which is refuted by WP p. 15)*. The run-up more than halves (7% → 3%) and the drift falls (13% → 9%) when the sample is extended back to 1994. On the **drift**, the WP explicitly diagnoses the cause: early-sample filings became public with a delay, and in Figure 5 Panel B (2003–2010 only) the drift vanishes altogether (R23). On the **run-up**, neither version offers an explanation for the 7% → 3% change. So: do not describe the divergence as wholly unexplained, and do *not* treat the 9% (or 13%) drift as a stable feature of the modern regime — CDF's own evidence says it is not.
- **The results are NASDAQ-driven (added by verifier, JF p. 1568).** 62% of the sample is NASDAQ, 29% NYSE, 9% Amex. Splitting by exchange, "the results are stronger for the sample of NASDAQ-listed stocks. While for several liquidity measures the results are less significant for stocks listed on the NYSE, those measures still do not reveal the presence of informed trading." (The ~25% of events in the financial crisis are *not* driving anything — dropping them leaves the results intact.)
- **The timing story and the "informed trading creates liquidity" story are not fully separated (added by verifier, JF n. 20, p. 1569).** CDF list the alternative explicitly: informed trades may *attract* uninformed volume — mutual funds facing redemptions placing large trades where price impact is least (Gantchev–Jotikasthira 2013), "falsely informed" value traders acting as liquidity providers (Cornell–Sirri 1992), and high-frequency traders producing a "hot-potato" volume increase. The matched-stock volume test (R12) is what partly adjudicates, and CDF say so at p. 1575. This matters for us: R12 is the load-bearing result behind the claim that filers *select* liquid days rather than *create* them.

## 6. What they do NOT do (scope boundary)

- **Object.** Microstructure liquidity measures and the return process around a filing. **No governance outcome at all** — no campaign success, no board seat, no takeover premium, no bidder entry, no firm policy change. The only "outcome" is a price/liquidity statistic. The paper's own stated implication is entirely about measurement: "standard adverse selection measures are not robust to informed trading by strategic traders with long-lived information who can choose when and how to trade" (p. 1580).
- **Margin of the disclosure rule.** They use the **threshold** (5%) and the **window** (10 days) as *fixed institutional furniture that generates the data*. **Neither margin varies.** The pre-/post-event-date comparison (R9, R10) is the nearest they come to studying the window, and it is a comparison of the filer's behaviour on the two sides of the 5%-crossing *within* a fixed 10-day regime — not a comparison of regimes. **There is no analysis of what a different window length would do.** The Feb-2024 acceleration is after their sample and is nowhere mentioned.
- **Identification.** Within-event fixed effects, matched-stock DiD, and two market-structure reform splits. **No instrument, no rule change, no structural estimation.** The theory is explicitly outsourced to the companion working paper.
- **Liquidity is not treated as exogenous or causal.** The paper's whole point is that activists *choose* liquid days — so liquidity and informed trading are simultaneously determined. They estimate correlations under fixed effects and interpret them, deliberately, as evidence about *measurement*, not about the causal effect of liquidity on anything.
- **They do not study 13G filers, or activists who never cross 5%,** and by construction they exclude amendments (13D/A).
- **They do not decompose the announcement return** into a control-value component and an information component. The $15 million shareholder gain (R18) is a back-of-envelope in the Internet Appendix, not an estimate of a premium.

## 7. Implications for our position

**Where CDF sit:** object = *microstructure liquidity measures and pre-filing returns*; margin = **the threshold and window are the data-generating institution, not the treatment**; identification = within-event FE + matched-stock DiD + two market-structure reforms. They own the *trade-level inside-the-window* territory and leave the control-outcome axis completely empty.

1. **This is our anchor paper for the institution, not a competitor on the object.** Nobody in the competitor set has our combination of κ (liquidity) × a *varying* disclosure margin × a *control outcome*. CDF confirm the third leg is untouched: their only outcome is a spread.
2. **They give us the single most important modelling fact: the pooled state is where the accumulation happens, and the flag is what ends it.** R17 (trading intensity peaking at t−10, the filer buying ~1% of shares outstanding on the event date itself) and R9 (`postevent` liquidity is high because filers *choose* when to cross) are exactly our blockholder deciding when to move from the pooled to the flagged partition. Our core model should reproduce: accumulation concentrated just before the flag, and endogenous timing of the crossing toward high-κ states.
3. **They complicate the naive empirical proxy for κ, and we must say so before a referee does.** If the blockholder times his trades to high-liquidity days, then *measured* Amihud/λ around activist events is endogenous to the blockholder's own strategy — measured illiquidity **falls** while a stake is being built (R4, R6). **And the contamination is at the window level, not the day level (added by verifier — R20, JF p. 1567):** averaged over the whole 60-day disclosure window and compared to the same calendar window a year earlier, four of six adverse-selection measures are *significantly lower*. So excluding trade days is not enough; the entire pre-filing window is contaminated. Any regression of ours that puts a contemporaneous liquidity measure on the right-hand side of an activism outcome inherits this. **Practical rule for our empirics ticket: measure κ well outside the accumulation window (as Edmans-Fang-Zur and Norli et al. both do, at t−1 to t−4), and never contemporaneously — and note that "outside" has to mean outside the whole 60-day window, not merely off the trade days.**
4. **R10 is the closest existing evidence on the window margin, and it points the right way for us.** Filers use limit orders 46% of the time *before* crossing 5% and only 34% *after*, when the 10-day clock is running — i.e. **shortening the time available shifts the blockholder from patient to aggressive execution.** That is a direct, dated, measured behavioural response to the window constraint. A shorter window (10 → 5 business days) mechanically compresses the aggressive phase. This is the mechanism our window-margin prediction should be built on, and CDF is the citation.
5. **The Item 5(c) 60-day transaction table is the empirical instrument for our window work.** It is longer than either the old 10-business-day or the new 5-business-day window, so a single filing's own transaction table brackets the whole window on both sides of the event date. Norli et al. use the same field. Combined with CDF's finding that filers count in **business days**, this makes the Feb-2024 acceleration measurable inside filings we can parse. Pass this to the empirics ticket.
6. **Do not claim CDF study the disclosure rule as a margin.** They do not. Claiming so would be caught immediately — the paper is famous and the reader will know it. The correct positioning sentence is: *CDF show what activists do inside the window under a fixed rule; we ask what changes when the rule moves.*
7. **Their run-up/jump split is a useful decomposition for our premium wedge.** The (t−60, t−1) run-up is value that leaks into the price *before* the flag; the two-day jump is the flag's own information content; the post-filing drift is the market slowly pricing the expected control outcome. In our language: the run-up is what the pooled state already reveals through order flow, the jump is the partition's information, and the drift is the expected engagement value. **But quote the JF numbers (3% / 2.5% / 9%), not the WP's (7% / 3% / 13%).**
8. **CDF name our partition themselves, as an open gap — this is the strongest single positioning sentence available (added by verifier, JF pp. 1557–1558).** After listing their two mechanisms, they add a third they do not pursue: *"We note that standard asymmetric information models also typically assume that the presence of the insider is common knowledge. In practice, market makers may have to learn that an insider is present from the order flow. This may also affect the relation between adverse selection measures and informed trading."* Combined with n. 4's companion-model line — that "a significant part of the valuable private information pertains to the activist's own holdings, which by definition is information known only to him" — CDF have written down the pooled state and declined to model it. **Our partition is not a gap we assert; it is a gap the anchor paper names in its own introduction.** This should go in the positioning memo verbatim.
9. **The window mechanism has a cleaner one-sentence citation than R10 (added by verifier, JF p. 1558):** "before their ownership crosses the 5% threshold, Schedule 13D filers are more likely to use limit orders than after, when they have only 10 days left to trade." Use that in the introduction; keep R10's 46.25% / 34.25% Bayes numbers for the body, and note they rest on an assumed 70%-accurate Lee-Ready classifier (n. 22), not on a measurement.
10. **Version hygiene.** The internal note that prompted this card cited the WP sample (2001–2010). The JF sample is 1994–2010 and the run-up magnitude more than halves. Anywhere our notes carry "7% run-up", that is the WP number and must be corrected or explicitly labelled.

## 8. Quotes we may lean on (verbatim, page-cited)

Unless marked **[WP]**, all quotes are from the published JF article and cite its printed page.

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "Rule 13d-1(a) requires investors to file with the SEC within 10 days of acquiring more than 5% of any class of securities of a publicly traded company if they have an interest in influencing the management of the company." | JF p. 1556 | The threshold and the pre-2024 window, in one sentence — our anchor |
| Q2 | "Item 5(c) of Schedule 13D requires the filer to report the date, price, and quantity of all trades in the target company executed during the 60 days that precede the filing date." | JF p. 1556 | The 60-day transaction history — the field that makes window-margin empirics possible |
| Q3 | "The final sample comprises the universe of all Schedule 13D filings that satisfy the above criteria from 1994 to 2010, which totals 3,126 events." | JF p. 1559 | Published sample and period |
| Q4 | "identify 9,580 Schedule 13D filings during 2001-2010." **[WP]** | WP p. 9 (PDF p. 10) | The WP's different sample — the version-divergence flag |
| Q5 | "The average (median) stock ownership on the filing date is 7.51% (6.11%)." | JF p. 1561 | Blocks are just over the threshold — the threshold binds |
| Q6 | "the probability that a Schedule 13D filer trades at least one share on a given day is approximately 25% and reaches 50% 10 days prior to the filing date." | JF p. 1561 | Accumulation intensity peaks against the window |
| Q7 | "Rule 13d-1(a) requires Schedule 13D filers to file with the SEC within 10 days after the event date. When we consider the distance between the event date and the filing date, we find that Schedule 13D filers often interpret the 10-day period in terms of business days and not calendar days." | JF p. 1561, n. 11 | The window is counted in **business days** — matches the 2024 rule text |
| Q8 | "Only when they file with the SEC, 10 days after their holdings reach the 5% threshold, does the information become public." | JF p. 1563 | The partition (pooled → flagged) as an institutional fact |
| Q9 | "there is a run-up of about 3% from 60 days to one day prior to the filing date. The two-day jump in excess return observed at the filing date is around 2.5%." | JF p. 1563 | Run-up vs announcement jump — **published** magnitudes |
| Q10 | "There is a run-up of about 7% between sixty days to one day prior to the filing day. The two-day jump in excess return observed at the filing date is around 3%." **[WP]** | WP p. 14 (PDF p. 15) | The WP's larger run-up — do not mix with Q9 |
| Q11 | "the cumulative return in excess of the market is about 6% in the (t − 10, t + 1) window around the filing date and about 3% in the (t − 1, t + 1) window around the filing date." | JF p. 1556 | The two announcement windows both versions agree on |
| Q12 | "on an average day when Schedule 13D filers trade, the measured price impact (λ) is almost 30% lower relative to the sample average." | JF p. 1557 | The headline: measured adverse selection FALLS during accumulation |
| Q13 | "trades and 20.16 on days with no informed trades, that is, it is almost 30% lower on days with informed trades." (continuing "the average λ is 14.33 on days with informed" from p. 1566) | JF pp. 1566–1567 | The λ levels behind the 30% |
| Q14 | "Thus, measured adverse selection and stock illiquidity are lower not only when informed trading takes place, but also relative to stocks with similar characteristics." | JF p. 1567 | The matched-stock DiD conclusion |
| Q15 | "Amihud's illiquidity measure decreases by more than 45% on days when Schedule 13D filers trade." **[WP]** | WP p. 4 (PDF p. 5) | Amihud — our own κ proxy — moves the "wrong" way during accumulation |
| Q16 | "Schedule 13D filers have at most 10 days to file with the SEC after the event date (the day when their ownership reaches 5%). Because of this time constraint, they have less flexibility with respect to their trading strategy after the event date." | JF p. 1569 | The window as a binding constraint on execution — our window-margin mechanism |
| Q17 | "the percentage of trades classified as buy-initiated transactions increases from 51.5% before the event date to 56.3% after the event date." | JF p. 1572 | Behaviour shifts from limit to market orders once the clock starts |
| Q18 | "Instead, measured adverse selection decreases and measured liquidity increases on days when insiders trade." | JF p. 1580 | The conclusion in one line |
| Q19 *(added by verifier)* | "We note that standard asymmetric information models also typically assume that the presence of the insider is common knowledge. In practice, market makers may have to learn that an insider is present from the order flow. This may also affect the relation between adverse selection measures and informed trading." | JF pp. 1557–1558 — **spans the page break**: everything up to "…from the order flow. This" is on p. 1557, "may also affect…" resumes on p. 1558. Search the two halves separately | **The pooled state, named by the anchor paper as an unmodelled gap** — our partition, in their words |
| Q20 *(added by verifier)* | "This model shows that a significant part of the valuable private information pertains to the activist's own holdings, which by definition is information known only to him." | JF pp. 1556–1557, n. 4 (describing the companion paper Collin-Dufresne & Fos 2015 WP) — **the footnote spans the page break** at "…a significant / part of the valuable…". Search the two halves separately | The private information *is* the stake — the object the disclosure rule reveals |
| Q21 *(added by verifier)* | "before their ownership crosses the 5% threshold, Schedule 13D filers are more likely to use limit orders than after, when they have only 10 days left to trade" | JF p. 1558 | The window-margin mechanism in one sentence — cleaner than Q17 for an introduction |
| Q22 *(added by verifier)* | "none of the adverse selection measures indicate the presence of informed traders during the 60-day disclosure period. Instead, four out of six measures indicate that adverse selection is significantly lower on average during the 60-day period." | JF p. 1567 | Measured κ is contaminated across the whole window, not only on trade days |
| Q23 *(added by verifier)* | "It shows that the post-filing drift in returns does not exist in the later part of the sample." **[WP]** | WP p. 15 (PDF p. 16) | The 9%/13% drift is a pre-2003 disclosure-delay artefact — do not carry it into a modern-regime event study |

## 9. Verification log

*(Filled by the verifier.)* Q1–Q3, Q5–Q9, Q11–Q14, Q16–Q18 were located by substring match (whitespace-normalised) against `research/txt_extracts/cdf_jf_pages.txt`, a page-marked `pdftotext -layout` re-extract of `research/txt_extracts/collin_dufresne_fos_2015_jf.pdf`; Q4, Q10, Q15 against `research/txt_extracts/cdf_fos_wp_layout.txt`, the equivalent re-extract of `research/txt_extracts/cdf_fos_jf2015.pdf` (NBER WP 18452).

**Three quotes required rejoining a PDF line-wrap hyphenation** (the hyphen is a typesetting artefact, not printed text, or is a genuine hyphen split across a line break) and will NOT match the raw extract as a single string — a verifier should search the fragments:
- **Q1**: source lines break as "Rule 13d-1(a) requires in- / vestors to file with the SEC within 10 days of acquiring more than 5% of any / class of securities of a publicly traded company if they have an interest in influ- / encing the management of the company." (JF PDF p. 2)
- **Q13**: spans the PDF p. 12 → p. 13 page break ("the average λ is 14.33 on days with informed" | "trades and 20.16 …").
- **Q15**: uses a typographic apostrophe in "Amihud's".
Also note: the raw `research/txt_extracts/collin_dufresne_fos_2015_jf.txt` and `cdf_fos_jf2015.txt` extracts carry no page markers and a Wiley download banner is interleaved on every JF page; use the `_pages`/`_layout` files for checking.

Page mappings verified: **JF printed = PDF + 1554** (checked at PDF pp. 1, 2, 5, 7, 9, 13, 15, 18, 26 → printed 1555, 1556, 1559, 1561, 1563, 1567, 1569, 1572, 1580). **WP printed = PDF − 1** (checked at PDF pp. 5, 10, 11, 15 → printed 4, 9, 10, 14).

### Verifier pass (adversarial, 2026-08-19)

**The JF PDF exists** — `ls research/txt_extracts/collin_dufresne_fos_2015_jf*` returns both the 465 KB PDF and a `.txt`. Nothing had to fall back to the WP.

Source of truth: **independent** per-page re-extracts of *both* PDFs built by the verifier (`pdftotext -f N -l N -layout`; JF 28 pages, WP 50 pages), not the reader's files. Quote matching was whitespace- and hyphenation-normalised. Page mappings independently re-confirmed from the running heads and folios: **JF printed = PDF + 1554** (checked at PDF pp. 1, 2, 3, 5, 7, 8, 9, 11, 12, 13, 14, 15, 18, 21, 24, 25, 26) and **WP printed = PDF − 1** (checked at PDF pp. 3, 4, 5, 10, 15, 16).

**Counts: 18 original quotes — 18 OK, 0 WRONG, 0 MISCITED, 0 UNCHECKED. 19 results — 18 OK, 1 page corrected. 1 §5 claim REFUTED and rewritten. 6 omissions added (R20–R23, Q19–Q23, plus the second companion paper and the NASDAQ/endogenous-volume weaknesses).**

| Item | Status | Checked against |
|---|---|---|
| Q1, Q2, Q11 | OK | JF PDF p. 2 = printed 1556. (Q1's line-break hyphenation is real; normalised matching handles it) |
| Q3 | OK | JF PDF p. 5 = printed 1559 |
| Q5, Q6, Q7 | OK | JF PDF p. 7 = printed 1561 |
| Q8 | OK | JF PDF p. 9 = printed 1563 |
| Q9 | OK | JF PDF p. 9 = printed 1563 |
| Q12 | OK | JF PDF p. 3 = printed 1557 — "the measured price impact (λ) is almost 30% lower relative to the sample average" |
| Q13 | OK | Spans JF PDF pp. 12→13 = printed 1566→1567, exactly as the card's note says |
| Q14 | OK | JF PDF p. 13 = printed 1567 |
| Q16 | OK | JF PDF p. 15 = printed 1569 |
| Q17 | OK | JF PDF p. 18 = printed 1572 |
| Q18 | OK | JF PDF p. 26 = printed 1580 |
| Q4 | OK | WP PDF p. 10 = printed 9 |
| Q10 | OK | WP PDF p. 15 = printed 14 |
| Q15 | OK | WP PDF p. 5 = printed 4 |
| **DECISION-CRITICAL: JF run-up 3% / jump 2.5% / drift 9% vs WP 7% / 3% / 13%** | **OK on all six numbers** | JF PDF pp. 9–10: "there is a run-up of about 3% … The two-day jump … is around 2.5%. After that the excess return remains positive and the postfiling 'drift' cumulates to a total of 9%." Sample stated as 1994–2010. WP PDF p. 15: "run-up of about 7% … two-day jump … around 3% … post-filing 'drift' cumulates to a total of 13%", sample stated as 2001–2010. The divergence is real and version-linked |
| **DECISION-CRITICAL: ~6% over (t−10, t+1) in both versions** | **OK** | JF PDF p. 2 = printed 1556 and WP PDF p. 4 = printed 3 — both give "about 6% in the (t − 10, t + 1) window … and about 3% in the (t − 1, t + 1) window" |
| **DECISION-CRITICAL: measured λ / PIN / spreads fall ~30% while activists accumulate** | **OK — but the "~30%" attaches to λ ONLY, and the card is correctly precise about this** | Table III (JF PDF p. 12): λ 14.3311 → 20.1644, −5.8334\*\*\* [−8.38]; the other declines are far smaller in relative terms (pimpact ≈ 6%, cumir ≈ 13%, rspread ≈ 9%, espread ≈ 6.5%). PIN is reported only as "lower when informed trading takes place" (JF p. 1567), with no percentage. Amihud's "more than 45%" is WP-only. **A positioning memo must not write "λ, PIN and spreads all fall ~30%" — that would be WRONG; the card does not** |
| **DECISION-CRITICAL: the limit-to-market-order switch once the 10-day clock starts** | **OK** | JF PDF p. 18 = printed 1572: 12,576 uniquely matched trades, 52.8% of purchases classified buy-initiated, rising "from 51.5% before the event date to 56.3% after". n. 22 on the same page gives the Bayes inversion under an assumed 70%-accurate Lee-Ready classifier (Cornell–Sirri 1992): 46.25% limit-order use before vs 34.25% after. Corroborated independently at printed p. 1558 and in the conclusion (p. 1580) |
| **DECISION-CRITICAL: JF sample 1994–2010 (19,026 → 3,126) vs WP 2001–2010 (9,580 → 1,725)** | **OK** | JF PDF p. 5: "we identify 19,026 Schedule 13D filings from 1994 to 2010"; "which totals 3,126 events". WP PDF p. 10: "identify 9,580 Schedule 13D filings during 2001-2010"; PDF p. 11: "consists of 1,725 events … on average 173 events take place each year" |
| **DECISION-CRITICAL: "the Internet Appendix was not read"** | **WAS a real limitation — now CLOSED (see §9b, 2026-08-19)** | The JF body routes to the Internet Appendix for: PIN and Amihud levels (p. 1567, n. 15), the announcement-return confidence bounds and the (t−2,t+2)/(t−1,t)/t regressions (p. 1564), the 120-day no-reversal test (n. 13), **all** of the profit calculations behind R18 (p. 1564), the NYSE-autoquoting test (n. 24), the trade-matching procedure and the market-order-proxy validation (p. 1572), the abnormal-trading-activity series behind the 80%/96% correlations (p. 1571), and the definitions and summary statistics of every liquidity measure (p. 1565). **R6, R18, R20, R21 and R22 all rest on it.** It is not in the repo and was not fetched |
| R4, R5 | OK | Table III, JF PDF p. 12 = printed 1566. Every level, difference, matched difference, DiD estimate and bracketed t matches the print, including the DiD column where only λ (−5.0208\*\*\*), rspread (−0.0012\*\*\*) and espread (−0.0014\*\*\*) survive |
| R7 | OK | Table II, JF PDF p. 11 = printed 1565. eret 0.0064\*\*\* vs −0.0004, difference 0.0068\*\*\*, t = 9.94 |
| R8, R9 | OK | Table IV, JF PDF p. 16 = printed 1570. All `itrade`, `postevent` and interaction coefficients and t-stats match; F-test p-values 0.0000 (λ) and 0.0588 (cumir) confirmed. The interpretive claim is verbatim at printed p. 1569: "This suggests that Schedule 13D filers choose to cross the 5% ownership threshold at times when stock liquidity is higher" |
| R11 | OK | Table V Panel B, JF PDF p. 20 = printed 1574. λ −0.7673\*\* [−2.29], pimpact 0.0008\*\*\* [3.63], trade-related 0.0030\*\* [1.96], rspread −0.0014\*\*\* [−7.59], espread −0.0007\*\* [−2.38] |
| R12 | OK | Table VI, JF PDF p. 21 = printed 1575. Volume 79/78/75/72/67%, net 67/66/64/62/60%, matched 57/58/57/58/58%, all \*\*\* |
| R13 | OK | Table VIII, JF PDF p. 24 = printed 1578. crspvol_t 0.0666\*\*\* [2.73], mkt_{t−1} −0.3872\* to −0.4592\*\*, to_it 3.2082\*\*\* [14.79], to_{it−1} 1.1699\*\*\* [6.56]; lead turnover 0.2106 [1.36]–0.2398\*; every `liqm` term insignificant |
| R14 | OK | Table VII, JF PDF p. 22 = printed 1576. `before` = 1994–1997 (pre-NASDAQ Order Handling Rules reform); itrade −3.8967\*\*\* [−8.58], itrade × before −3.4217\*\*\* [−2.63]; F-test p = 0.0000 (λ), 0.0310 (rspread) — and 0.0501 (pimpact), which the card omits but which only strengthens it |
| R15 | OK | Table IX, JF PDF p. 25 = printed 1579. Buy pimpact 0.0003\* [1.83], sell −0.0012\*\*\* [−4.64]; rspread buy −0.0015\*\*\* [−8.57] vs sell −0.0003\* [−1.79]; matched-stock Panels C–D all insignificant |
| R16 | OK | Table I, JF PDF p. 8 = printed 1562. 7.51% (6.11%), 3.8% (2.8%), 899,692 (298,807) shares, $16.4m ($2.5m), 0.5% (0.2%) per trading day, 31.5% (25.4%) informed turnover, 31.1% of days |
| R17 | OK | JF PDF p. 7 = printed 1561. 25% → 50% at t−10; 0.03–0.05% → 0.15–0.20% → 0.06–0.10%; "close to 1% of outstanding shares on the event date, compared to 0.10% to 0.15% on the days" adjacent |
| R18 | OK | JF PDF p. 10 = printed 1564. $22m stake in a $293m market-cap company (7.51%), expects $0.8m = $0.4m on 60-day trades + $0.4m on the initial position; other shareholders gain $15m. WP PDF p. 4 = printed 3 gives $1.13m on a $30m stake in a $404m company |
| R1 page | **CORRECTED** | The 9% drift figure sits on JF printed p. 1564, not 1563 — the sentence runs over the page break. Card amended |
| §5 "Version divergence is … unexplained … Neither version discusses this" | **REFUTED — rewritten** | WP PDF p. 16 = printed 15: the WP attributes the post-filing drift to early-sample publication delay and shows in Figure 5 Panel B, restricted to 2003–2010, that "the post-filing drift in returns does not exist in the later part of the sample." The *drift* divergence has a stated cause; only the *run-up* divergence is unexplained. Card rewritten and the finding added as R23 / Q23 |
| §2 filters, composition, matching, reform dates | OK | JF printed p. 1559 (share codes 10/11, $1–$1,000, no derivatives, 13D/A excluded); printed p. 1568 (62% NASDAQ / 29% NYSE / 9% Amex, ~25% crisis); printed p. 1567 (Fama–French 1997 industry, exchange, size, low-frequency volatility, plus the Davies–Kim 2009 robustness match in the footnote); printed p. 1577 n. 24 (NYSE autoquoting "in early 2003"); printed p. 1576 (NASDAQ 1997 reform) |
| §4 three 13D triggers (n. 7), Item 5(c) form language (n. 3), business-day counting (n. 11), Reg NMS | OK | JF printed pp. 1559, 1556, 1561, 1568 respectively — all four verbatim |
| §5 "their own n. 12 concedes" the accumulation-selection restriction | OK | JF PDF p. 10 = printed 1564, footnote 12 (the WP has the same sentence with "accumulate" rather than "accumulates") |
| §6 "no governance outcome at all — no takeover premium, no bidder entry" | **OK — confirmed** | Read in full; the only outcomes are liquidity statistics, returns, order imbalance and volume. The $15m shareholder gain (R18) is a back-of-envelope in the Internet Appendix, exactly as the card says |
| §6 "neither margin varies; no analysis of what a different window length would do; Feb-2024 nowhere mentioned" | **OK — confirmed** | The only window handle is the pre-/post-event-date split inside a fixed 10-day regime (Table IV). Nothing in either version considers a counterfactual window length |
| Header: JF 70(4), 1555–1582, Aug 2015; Biais; submitted 31 Aug 2012; final 27 Jan 2015 | OK | PDF p. 1 running head "VOL. LXX, NO. 4 • AUGUST 2015", folio 1555; PDF p. 26 footer "Initial submission: August 31, 2012; Final version received: January 27, 2015 / Editor: Bruno Biais" |
| Q19, Q20 *(verifier-added)* | OK, but **each spans a page break** | Verified half-by-half: Q19a on JF PDF p. 3, Q19b on PDF p. 4; Q20a on PDF p. 2, Q20b on PDF p. 3. Noted in the quote table so a future checker does not read the split as a fabrication |
| Q21, Q22, Q23 *(verifier-added)* | OK | JF PDF p. 4 = printed 1558; JF PDF p. 13 = printed 1567; WP PDF p. 16 = printed 15 |

**Omissions added by the verifier** (each material to a liquidity × disclosure-rule × control-outcome position):
1. **§7 item 8 + Q19 (JF pp. 1557–1558) — the most important find in this pass.** CDF list a *third* mechanism they do not pursue: standard models assume the insider's presence is common knowledge, whereas "in practice, market makers may have to learn that an insider is present from the order flow." That is our pooled state, named as an open gap by the anchor paper itself.
2. **§2 + Q20 (n. 4, JF pp. 1556–1557) — a second companion theory paper the card missed.** Collin-Dufresne & Fos (2015 WP), "Shareholder activism, informed trading, and stock prices", endogenises activist effort and firm value, with the price depending on the market maker's estimate of the activist's ownership, and states that "a significant part of the valuable private information pertains to the activist's own holdings". Anyone positioning against CDF must read this one, not only the stochastic-liquidity Kyle paper.
3. **R20 + Q22 + §7 item 3 (JF p. 1567) — the κ-measurement contamination is at the WINDOW level.** Averaged over the whole 60-day window against the same calendar window a year earlier, four of six adverse-selection measures are significantly *lower*. The card's practical rule ("never measure κ contemporaneously") was too weak; it now says "outside the whole 60-day window".
4. **R21 (JF p. 1571).** 13D trading and uninformed trading activity correlate **80%** over (t−60, t−1) and **96%** over (t, t+9); and `itrade` weakens after the event date, "consistent with the selection and limit order mechanisms being less likely to operate during the postevent date period" — a direct window-margin result.
5. **R23 + Q23 + the §5 rewrite (WP p. 15).** The post-filing drift is a pre-2003 disclosure-delay artefact and vanishes in 2003–2010. This both corrects a WRONG card claim and warns our own event study off carrying a 9%/13% drift into the modern regime.
6. **§5 (JF p. 1568 and n. 20, p. 1569).** Results are stronger on NASDAQ and weaker on NYSE; and the "endogenous volume" alternative — informed trades *attracting* uninformed volume — is one CDF name but only partly rule out, with the matched-stock test (R12) doing the adjudicating.
7. **R22 (n. 13, JF p. 1564).** No reversal in the buy-and-hold return over the 120 days after filing, so the filing-date jump is information, not price pressure — needed before the card's §7 item 7 reads the jump as the partition's information content.

**Decision-critical items I could NOT fully check, named rather than triaged:**
- **The Internet Appendix.** ~~Not in the repo, not fetched.~~ **RESOLVED 2026-08-19 — fetched and read in full; see §9b. All five items below are closed.** R6 (Amihud, PIN), R18 (all profit figures, including the $15m shareholder gain the card uses), R20, R21 and R22 rest on numbers that exist only there. The JF body states each finding in words, which is what I verified; the magnitudes behind them are unverified. **If a claim of ours turns on the Amihud/PIN result or on the $0.8m-vs-$15m split, fetch the Internet Appendix first.**
- Everything else was checked against the print.

**Overall verdict: the card is accurate and the version discipline is its best feature — but one §5 claim was wrong and has been rewritten.** 18/18 quotes verbatim, 18/19 results exact with one page correction, one refuted claim, seven omissions added. All six decision-critical items in the brief survive checking, with one sharpening: the "~30%" fall belongs to λ alone, not to λ *and* PIN *and* spreads jointly — the card was already precise about this, and a positioning memo must stay precise too.


## 9b. Internet-Appendix supplement-reader log — 2026-08-19

**Source read:** `research/txt_extracts/collin_dufresne_fos_2015_internet_appendix.pdf` — "Internet Appendix for 'Do Prices
Reveal the Presence of Informed Trading?'", 38 PDF pages, printed folios 1–36 (**IA printed = PDF page − 1**; PDF p. 1 is the
unnumbered Wiley cover sheet, PDF p. 38 blank). Extracted from the Wiley supplement ZIP `jofi12260-sup-0001-Appendix.zip`, file
`JF_MS20120199_IA_Collin-Dufresne_Fos.pdf` (see `research/txt_extracts/FETCH_LOG_C.md`, row
`collin_dufresne_fos_2015_internet_appendix`). **Reader:** opus, full text, `pdftotext -layout` with a page index.
All cites below are **IA printed pages**, never journal pages.

**Structure.** Five numbered parts mirroring the article's sections, plus references:
I. Supplementary Results for Section I (IA pp. 1–8: sample description, Figure IA.1, Table IA.I industry classification,
Table IA.II probit of 13D-target selection, Figure IA.2 pre-event trading strategy, Figures IA.3 Icahn/Chesapeake case) ·
II. Supplementary Results for Section I *[sic — the IA's own mislabel; it is Section II material]* (IA pp. 8–14: announcement
returns, Figures IA.4–IA.5, Table IA.III, and **§C Profits**, Table IA.IV) · III. Supplementary Results for Section III
(IA pp. 14–18: definitions of every liquidity measure, eqs. (IA.4)–(IA.14), Table IA.V summary statistics) ·
IV. Supplementary Results to Section IV (IA pp. 18–26: Table IA.VI low-frequency measures, Table IA.VII Davies–Kim matching,
**Table IA.VIII the 60-day-window comparison**, Table IA.IX five-panel robustness) · V. Supplementary Results for Section V
(IA pp. 25–34: Figure IA.6 abnormal-volume decomposition, Figure IA.7 intraday, TAQ matching, Table IA.X order imbalance,
Table IA.XI NYSE autoquoting, Table IA.XII selection on observables).

### The five open items → verdicts

| Item | Verdict | IA location | The printed numbers |
|---|---|---|---|
| **R6 — Amihud** | **CLOSED, magnitude corroborated** | Table IA.VI, **IA p. 19** | `illiquidity` 0.2662 (filer-trade days) vs 0.5191 (no-trade days), Diff **−0.2529\*\*\* [−17.08]**, matched Diff −0.0387 [−1.47] (n.s.), **DiD −0.2142\*\*\* [−6.09]**. `baspread` 0.0212 vs 0.0232, **−0.002\*\*\* [−6.65]**, DiD −0.0018\*\*\* [−2.72]. −0.2529/0.5191 = **48.7%**, so the WP's "more than 45%" holds in the JF's 1994–2010 sample as well — but **the JF IA never prints a percentage**, so "more than 45%" must still be cited to the WP, p. 4 |
| **R6 — PIN** | **CLOSED, with a scope correction** | Table IA.V **IA p. 18**; Table IA.VIII **IA p. 22**; text **IA p. 20** | PIN is **never estimated on filer-trade days** — it is not in Table IA.VI. It appears only at the 60-day-window level: 0.4385 over (t−60,t−1) vs 0.4943 over (t−420,t−361), **Diff −0.0559\*\*\* [−13.1]**, matched Diff −0.0301\*\*\* [−6.97], **DiD −0.0257\*\*\* [−3.52]**. IA text: "pin is more than 9% lower during the 60-day disclosure period" (the ratio is arithmetically 11.3%). Unconditional baseline mean over (t−421,t−361): **0.4899**, sd 0.2233 (Table IA.V) |
| **R18 — all profit figures** | **CLOSED, every figure verified** | text **IA pp. 11–12**, Table IA.IV **IA p. 13**, text **IA p. 14** | See below |
| **R20 — the 60-day window comparison** | **CLOSED, four measures named** | Table IA.VIII **IA p. 22**, text **IA pp. 20, 23** | See below |
| **R21 — 80% / 96% correlations** | **CLOSED, verbatim** | text **IA p. 25**, Figure IA.6 **IA p. 27** | "The correlation between the two series is 80% during the (t-60,t-1) period and 96% during the (t,t+9) period." |
| **R22 — no 120-day reversal** | **CLOSED, plus two figures the card did not have** | Figure IA.5 + text **IA pp. 10–11**, Table IA.III **IA p. 10** | See below |

### R18 in full — Table IA.IV, "Profits from Informed Trades" (IA p. 13)

| Market CAP quantile | Market CAP | Trading Profit | Total Profit | Value Created |
|---|---|---|---|---|
| Q1 – low | 19,773,876 | 43,998\*\*\* [4.52] | 56,590\*\*\* [3.97] | 908,857\*\* [2.17] |
| Q2 | 52,884,243 | 104,907\*\*\* [5.71] | 192,926\*\*\* [4.22] | 2,607,513\*\*\* [2.99] |
| Q3 | 119,969,759 | 216,250\*\*\* [7.31] | 298,363\*\*\* [6.01] | 4,226,135\*\*\* [3.37] |
| **Q4** | **293,003,259** | **403,214\*\*\* [9.24]** | **801,141\*\*\* [7.59]** | **15,000,273\*\*\* [5.56]** |
| Q5 – high | 1,346,301,018 | 907,584\*\*\* [13.73] | 1,818,721\*\*\* [11.08] | 33,239,501\*\*\* [8.09] |

So the JF body's headline sentence is **the Q4 row**, rounded: IA p. 12 verbatim — "a Schedule 13D filer who acquires a $22
million stake in a $293 million market cap company (i.e., a 7.51% stake, which is the average stake size in our sample) expects
to benefit $0.8 million. This can be further broken down into a $0.4 million profit on trades during the 60-day period and a
$0.4 million profit on the initial ownership, purchased prior to the 60-day window." **The $0.8m-vs-$15m split is exactly
Total Profit 801,141 vs Value Created 15,000,273 in the same row.**

Three definitional cautions for anyone quoting the split **(added by supplement reader)**:
1. **"Value Created" is not "other shareholders' gain."** Eq. (IA.3): `Value Created = (p_post − p₀)·SHOUT` — the whole firm's
   announcement gain, filer included. The IA's own like-for-like contrast is at IA p. 14: "shareholders of companies in the fifth
   market cap quantile gain $33 million during an average event whereas Schedule 13D filers gain $1.8 million."
2. **Total Profit is a downward-biased estimate by construction.** Eq. (IA.2) values the pre-window stake at the price of the
   *first disclosed transaction*; IA p. 12: "This assumption is most likely to cause a downward bias in estimated total profits."
3. **`p_post` is the average price over the week after the filing**, not the filing-day close (IA p. 11). A window-margin paper
   using this ratio must say so.

### R20 in full — Table IA.VIII, "Liquidity Measures during the 60-Day Disclosure Period" (IA p. 22)

Baseline window is **(t−420, t−361)**, i.e. the same calendar window one year earlier. (Table IA.V's summary statistics use
(t−421, t−361) — a one-day discrepancy inside the IA itself, immaterial but worth knowing before replicating.)

The **four out of six** significantly-lower adverse-selection measures are: **λ** 19.0011 vs 22.3285, −3.3274\*\*\* [−3.36];
**cumir** 0.0015 vs 0.0017, −0.0002\*\* [−2.16]; **illiquidity** 0.4611 vs 0.5025, −0.0413\*\*\* [−4.12]; **pin** −0.0559\*\*\* [−13.1].
The two insignificant ones are **pimpact** (0.0066 vs 0.0066, 0.0000 [−0.21]) and **trade-related** (0.0691 vs 0.0686, 0.0005 [0.24]).
Other liquidity measures: rspread −0.0014\*\*\*, espread −0.0012\*\*\*, baspread −0.0020\*\*\*.
**DiD (column 7)** survivors: λ −4.5788\*\* [−2.31], illiquidity −0.0726\*\*\* [−4.24], pin −0.0257\*\*\* [−3.52],
rspread −0.0012\*\*\* [−2.74], baspread −0.0016\*\* [−2.32].

One IA sentence worth having verbatim, IA p. 23, because it is CDF's own reading of *why* the window-level differences weaken
under matching — and it is the selection story our κ-timing rule depends on: "The reduction in statistical significance of the
differences in liquidity measures indicates that Schedule 13D filers are more likely to trade when aggregate liquidity is high."
**(added by supplement reader)**

### R22 in full, and the one number that differs between versions

- **No reversal, verbatim, IA p. 10:** "When we compare Figure IA.5 and Figure 2, we see that there is no reversal. The abnormal
  buy-and-hold return over the (t-40,t-120) period is slightly above 1%."
- **Table IA.III (IA p. 10)** gives the announcement return the JF body only describes: indicator on **(t−2,t+2) 0.0049\*\*\* [5.50]**,
  **(t−1,t+1) 0.0080\*\*\* [7.77]**, **filing date t 0.0112\*\*\* [5.79]**; constants 0.0006/0.0006/0.0007\*\*\*, 121 daily observations,
  R² 0.203 / 0.337 / 0.220. IA p. 10: "the three-day abnormal return, reported in column (2), is 2.4% (0.8% times 3)."
- **NUMBER THAT CHANGED — drift 9% (body) vs 10% (IA).** IA p. 10 reads "a run-up of about 3% … The two-day jump … is around
  2.5%. After that the excess return remains positive and the post-filing 'drift' cumulates to a total of **10%**." The JF body
  (printed p. 1564) says **9%**. Run-up (3%) and jump (2.5%) are identical. The gap is a **horizon** difference, not a conflict:
  the body's Figure 2 runs to t+40, the IA's Figure IA.5 to t+120, and the extra 80 days add the "slightly above 1%" the same
  paragraph reports. Cite 9% for (t−60, t+40) and 10% for (t−60, t+120). **(added by supplement reader)**
- **The IA independently corroborates R23 for the JF sample**, which the verifier had only from the WP — IA p. 11: "An
  untabulated result suggests that the price drift after the filing date is not positive in the recent period (2003 to 2010)."
  R23 therefore rests on both versions, not the WP alone. **(added by supplement reader)**

### Other IA content this pass surfaced (added by supplement reader)

1. **Selection on observables is tested and only partly explained away** (Table IA.XII, IA p. 33; text IA pp. 33–34): controlling
   for market-wide and stock-specific liquidity factors leaves the `itrade` effect present though weaker, and CDF concede
   "this may be because we are not using sufficiently precise instruments."
2. **Table IA.IX has five panels, not the two the body implies** (IA p. 26): A full sample, B pre-crisis (<2007), C NASDAQ,
   D NYSE, **E (t−30, t)**. Panel E matters to us: shortening the accumulation window from 60 to 30 days leaves λ
   (−3.5582\*\*\* / −2.4045\*\*\*) and the spreads significant but kills pimpact and matched cumir. That is the closest thing in the
   paper to a *window-length* comparative static, and it is in the IA, not the body.
3. **TAQ matching arithmetic** (IA p. 28): 292,551 disclosed 13D transactions → 108,706 TAQ matches (**37%**) → **12,576**
   uniquely matched trades — the sample behind the limit-order/market-order result (R10 in the body).
4. **A probit of what gets targeted** (Table IA.II, IA p. 4; 35,011 / 32,570 observations) and an industry table (Table IA.I,
   IA p. 3). CDF's own summary, IA p. 5: "our results are robust to any bias in terms of industry and firm characteristics."
5. **A worked case study** — Icahn Capital LP / Chesapeake Energy, Figure IA.3 and text IA pp. 5–8, with the actual per-share
   prices ($14.54 pre-window vs $15.70 in-window). Usable as an illustration in a talk.

### What may now be written

- The **$0.8m-vs-$15m split is verified** and may be cited to IA Table IA.IV, IA p. 13 — with caution (1) above about what
  "Value Created" means.
- "Amihud falls ~49% on filer-trade days" is now sayable from the **JF** sample (IA Table IA.VI), rather than only from the WP.
- "PIN is lower during the disclosure window" is sayable; **"PIN is lower on days the filer trades" is not** — CDF never estimate it.
- All five items the verifier named as decision-critical-and-unchecked are now checked. **UNCHECKED 5 → 0. Nothing was refuted.**
  The single arithmetic discrepancy found (drift 9% vs 10%) is a horizon difference, resolved above.
