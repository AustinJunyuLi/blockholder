# Polk, Buchheit, Riley & Stone (2024) — "Shrinking the 13D disclosure window will benefit non-activist investors"

**Venue / status:** *Journal of Financial Regulation and Compliance*, Vol. 32, No. 4 (2024), pp. 516–538. DOI 10.1108/JFRC-01-2024-0016. Emerald Publishing. Received 26 Jan 2024; revised 1 May 2024; accepted 7 May 2024. Paper type: research paper. JEL: D43, G18, G32, G34, G38, M48, P51.
**Full text from:** `research/txt_extracts/polk_et_al_2024_jfrc.pdf` (23 pp) · **Reader:** opus · **Read:** full text, 23 pages (516–538), including all five tables, six figures, endnotes and Appendices 1–4
**Page numbering:** printed journal pages 516–538. Ligatures (fi/fl/ff) normalised in quotes; nothing else altered.
**Type:** empirical (descriptive event study)   **Role for us:** competitor (Feb-2024 acceleration set)

> **Extraction caveat — RESOLVED by the verifier.** Plain `pdftotext` renders this paper's minus signs as the control byte `\x02`, so negatives silently became positives. The fix is one pipe: `pdftotext -f N -l N -layout -raw file.pdf - | tr '\002' '-'`. All five tables have now been read with signs intact and Table 1's year-by-year grid is transcribed in §3 below. No number in this card now depends on an unsigned extraction.

## 1. Question

Does an activist investor earn more by waiting the full legal delay before filing Schedule 13D? The authors ask this in order to judge the SEC's *Modernization of Beneficial Ownership Reporting* rule (Release 33-11253), which cut the initial 13D deadline from 10 to 5 days effective 5 February 2024. Their stated aim is to "corroborate prior results under the historic 10-day maximum reporting regime" and to set "an updated 'baseline projection'" for what the five-day regime will do (p. 516). The policy conclusion — that shrinking the window helps non-activist investors — is in the title.

## 2. Model / data and method

Empirical archival, entirely on **pre-rule data**. No theory, no model.

**Sources** (p. 520): Audit Analytics Shareholder Activism database (filer/issuer identifiers); **trigger dates hand-scraped from raw EDGAR filings** — the R package `getFilings` to download every 13D, then Python to parse "the first date preceding 'Date of Event'" (Appendix 4, p. 538); Compustat Fundamentals Annual (industry, financials); CRSP (returns).

**Sample construction** (Appendix Table A1, p. 534):

| Step | N |
|---|---|
| Filed 13Ds, 2001–2022 | 42,378 |
| less: no machine-readable trigger date | (23,123) |
| less: trigger-to-filing gap > 12 days, or insufficient data for excess returns | (9,550) |
| less: trigger date later than filing date | (20) |
| **Final sample** | **9,685** |

Final sample = **9,685 initial Schedule 13D filings, 2001–2022, by 5,863 reporting entities in 5,037 unique firms** (p. 520). A broader retained set of 14,635 filings (11,924 unique filers, 7,037 first-time filers, 7,985 unique companies) appears in Table 2 (p. 525).

**Unit of observation:** one **initial** (original, non-amendment) Schedule 13D on a given issuer. *(corrected by verifier: this is **not** the same as a first-time filer — "about half of the original Schedule 13D filings are a shareholder's first filing with the SEC", p. 521; Table 2 puts it at 7,037 first-time filers out of 14,635 filings. The authors themselves lean on this: because only half are first-timers, they argue the returns reflect "the market reacting to the potential positive externalities associated with an activist investor rather than the presence of any specific investor", p. 521.)*

Key variable **"Delta" = number of days between the trigger date (the purchase that takes the filer past 5%) and the EDGAR filing date** — and **Delta is counted in calendar days**, while the legal window they are evaluating is in business days. See §5; this is now settled from the text, not inferred.

**Design.** Descriptive event study in two cuts:
- **(a) Event-time by day** relative to the trigger date: mean abnormal return per day (Table 1, pp. 522–523; Figure 1, p. 521) and abnormal trading volume (Figure 2, p. 524; volume benchmarked against NASDAQ volume, endnote 11). *(corrected by verifier: **Table 1 as printed runs day −10 to day +10 only**, ten columns per page across two pages. Its own note claims "each day from 15 days before the trigger date to 15 days after" — days ±11 to ±15 are nowhere in the table.)*
- **(b) Cumulated over the actual quiet period**: for each filing, sum the daily abnormal returns from the trigger date to the actual filing date, then group by Delta = 0 … 10 (Table 3, p. 526; Figure 3, p. 526). *(added by verifier)* The same cut is run on **abnormal trading volume** — **Figure 4, p. 527**, "Abnormal volume by delta" — and volume rises with Delta too: "there is a steady increase in abnormal trading volume as investors wait longer to file" (p. 521). The card previously had no entry for Figure 4; see R14.

The comparison that carries the policy claim is between filers who happened to file within five days and those who took 6–10 days (p. 517).

**What the design is not.** There is **no regression, no control group, no difference-in-differences, no matching, and no post-2024 data**. Excess returns are described only as "cumulative abnormal returns obtained from the Center for Research in Security Prices" — the expected-return model (market model? market-adjusted? estimation window?) is never stated. **No standard errors or confidence intervals appear anywhere in the paper**; significance is reported only as italics at the 0.05 level (Table 5), "n.s." (Table 4), and two p-values in prose.

**Robustness cuts** (§5, pp. 524–530): quarterly loss vs profit firms (untabulated, no significant difference); disclosed reason for filing, seven categories (Figure 6 Panels A–G, no significant deviation); target size, accelerated/large-accelerated filers vs others (Table 4, n = 5,170, all differences n.s.); small corporations under $75m market value (no statistical difference); R&D intensity quartiles (untabulated); presence of a Form 8-K within ±10 days of the trigger date (Table 5); pre-COVID (2018–2019) vs post-COVID (2021–2022) (Figure 5, **p. 527** — *page corrected by verifier*).

## 3. Results — with honesty labels

Label convention used here: **ESTIMATED\*** = a point estimate is printed but **no standard error or confidence interval is given anywhere in the paper**. I have not upgraded any of these to plain ESTIMATED.

| # | Result (one line) | Label | Where (page / prop / table) |
|---|---|---|---|
| R1 | Abnormal returns are "statistically above zero from the trigger date to the ninth day after the trigger date, falling to zero on day 10" | ESTIMATED\* — note they claim statistical significance here while printing no SE anywhere | p. 520; Figure 1, p. 521; Table 1, pp. 522–523. *(added by verifier: the Table 1 "Total" cell for day +10 is **−0.10%**, i.e. mildly negative, not zero. "Falling to zero" is their prose, not their number.)* |
| R2 | Mean abnormal return **0.90% on the trigger date** and a further **1.61% on day +1** | ESTIMATED\* | p. 520; Table 1 "Total" row, p. 523 |
| R3 | **Headline:** cumulated quiet-period excess returns rise monotonically-ish in Delta, from **1.34% at Delta = 0 to 5.09% at Delta = 10**; full row 1.34, 1.94, 1.84, 3.60, 1.63, 3.12, 3.02, 4.11, 4.32, 4.73, 5.09 | ESTIMATED\* | Table 3, p. 526; Figure 3, p. 526; stated pp. 517, 521, 530 |
| R4 | Filings per Delta bucket: 756, 633, 336, 312, 334, 281, 312, 560, 675, 878, **4,608**; **median Delta = 10** | ESTIMATED\* (counts) | Figure 3 and its note, p. 526 |
| R5 | Abnormal trading volume spikes at the trigger date to about **five times normal**, returning to normal by day +15 | ESTIMATED\* | pp. 520–521; Figure 2, p. 524 |
| R6 | Dropping firms with any Form 8-K within ±10 days of the trigger date, returns still rise **1.38% → 5.88%**; difference between Delta = 0 and Delta = 5 and between Delta = 0 and Delta = 10 is significant at p < 0.05 | ESTIMATED (with p-values, no SEs) | Table 5, p. 531; text p. 527; endnote 13 gives p < 0.01 |
| R7 | Size split: accelerated + large-accelerated filers **1.09% → 5.07%**; other issuers **1.73% → 6.17%**; **every** difference between the two groups is n.s. | ESTIMATED\* | Table 4, p. 530 (n = 5,170) |
| R8 | R&D intensity split: highest quartile **1.55% → 8.55%**, lowest quartile **1.46% → 6.68%** | ESTIMATED\* (untabulated) | p. 525, endnote 12 |
| R9 | No statistically significant difference in the Delta gradient between loss-making and profitable target quarters | ESTIMATED\* (untabulated) | p. 524. *(added by verifier: the sentence cross-references "(Figure 5)", but Figure 5 is the **pre-/post-COVID** figure, p. 527. The loss/profit split is not plotted anywhere. Another broken internal reference — see §5.)* |
| R10 | No significant deviation in the Delta gradient by the filer's disclosed reason for filing | ESTIMATED\* | Figure 6 Panels A–G, pp. 528–530 |
| R11 | No significant difference between pre-COVID (2018–2019) and post-COVID (2021–2022) return patterns | ESTIMATED\* | p. 518; Figure 5, **p. 527** *(page corrected by verifier)* |
| R12 | **~45% of original 13D filings in 2022 were filed before the final legal day**; separately, **25% of all filed 13Ds were filed within 5 days** and would be unaffected by the new rule | ESTIMATED\* | p. 520 and endnote 9, p. 532 |
| R13 | Cutting the window from 10 to 5 days "will reduce activist investors' opportunity to profit by legally delaying" and "will improve transparency and provide a more level playing field" | **ASSERTED** (the policy conclusion is an extrapolation from R3, not an estimate on post-rule data) | pp. 516, 518, 530 |
| R14 | **Abnormal trading volume also rises with Delta** — "a steady increase in abnormal trading volume as investors wait longer to file" | ESTIMATED\* *(added by verifier)* | p. 521; **Figure 4, p. 527**. This is the paper's only quantity-side evidence that something is *happening* in the window rather than merely accruing, and it is the closest they come to our post-trigger-accumulation mechanism |
| R15 | On days −10 to −1 the pooled abnormal return is flat and faintly negative every day (Total row: −0.05, 0.01, −0.09, 0.02, −0.05, −0.04, −0.05, −0.12, −0.03, −0.01) — **no pre-trigger run-up** | ESTIMATED\* *(added by verifier; recoverable only after the minus-sign fix)* | Table 1, p. 522 |

**Table 1 recovered in full *(added by verifier — the minus signs are back)*.** Daily mean abnormal return (%)
by year; columns are trading days relative to the trigger date. Printed pp. 522 (days −10…−1) and 523 (day 0…+10).
The table stops at ±10 despite its note claiming ±15.

*Days −10 to −1 (p. 522):*

| Year | −10 | −9 | −8 | −7 | −6 | −5 | −4 | −3 | −2 | −1 |
|---|---|---|---|---|---|---|---|---|---|---|
| 2001 | −0.10 | 0.55 | −0.08 | 0.14 | −0.04 | 0.00 | −0.32 | −0.32 | 0.13 | −0.16 |
| 2002 | 0.25 | 0.02 | 0.24 | 0.03 | 0.28 | −0.13 | 0.09 | −0.25 | 0.01 | 0.33 |
| 2003 | −0.07 | 0.24 | −0.08 | 0.03 | −0.18 | −0.04 | −0.12 | −0.16 | −0.16 | 0.08 |
| 2004 | 0.04 | 0.15 | −0.05 | −0.13 | −0.24 | 0.04 | −0.02 | 0.19 | 0.34 | −0.06 |
| 2005 | 0.05 | −0.09 | −0.07 | 0.11 | −0.04 | −0.11 | 0.09 | −0.22 | 0.04 | −0.23 |
| 2006 | 0.11 | 0.16 | −0.25 | 0.04 | −0.10 | 0.16 | 0.07 | 0.16 | 0.09 | 0.11 |
| 2007 | −0.02 | 0.00 | −0.12 | −0.03 | 0.02 | −0.17 | −0.08 | −0.11 | −0.10 | −0.16 |
| 2008 | −0.11 | −0.05 | −0.32 | 0.36 | −0.19 | −0.07 | 0.08 | −0.83 | −0.07 | 0.03 |
| 2009 | −0.41 | 0.03 | −0.01 | 0.67 | −0.95 | 0.08 | −0.05 | 0.05 | −0.24 | −0.43 |
| 2010 | −0.04 | −0.03 | −0.13 | −0.07 | 0.06 | 0.12 | 0.24 | −0.05 | −0.09 | −0.19 |
| 2011 | 0.09 | −0.11 | 0.01 | −0.21 | −0.13 | −0.07 | −0.02 | −0.17 | −0.41 | −0.53 |
| 2012 | −0.38 | 0.12 | 0.10 | 0.34 | −0.09 | 0.08 | −0.18 | 0.06 | 0.26 | 0.11 |
| 2013 | −0.03 | −0.01 | 0.02 | −0.31 | 0.29 | −0.02 | −0.08 | −0.28 | 0.66 | 0.14 |
| 2014 | 0.06 | −0.34 | 0.04 | 0.01 | 0.21 | 0.39 | −0.04 | −0.07 | −0.19 | 0.19 |
| 2015 | −0.23 | −0.15 | −0.09 | −0.14 | −0.12 | 0.08 | −0.18 | 0.14 | 0.09 | 0.15 |
| 2016 | −0.18 | 0.05 | 0.14 | −0.11 | −0.02 | −0.35 | −0.07 | 0.06 | −0.28 | 0.26 |
| 2017 | 0.08 | −0.20 | −0.06 | 0.08 | −0.10 | −0.26 | −0.29 | 0.24 | 0.08 | 0.07 |
| 2018 | −0.02 | −0.35 | −0.27 | −0.15 | 0.12 | −0.28 | −0.12 | 0.11 | −0.19 | 0.02 |
| 2019 | −0.17 | 0.29 | −0.01 | 0.21 | −0.12 | −0.15 | −0.09 | −0.23 | −0.08 | −0.12 |
| 2020 | −0.28 | −0.04 | −0.27 | −0.65 | 0.25 | −0.21 | −0.55 | −0.18 | −0.23 | −0.06 |
| 2021 | 0.05 | −0.30 | −0.09 | −0.21 | −0.02 | 0.09 | 0.22 | −0.24 | −0.19 | 0.00 |
| 2022 | 0.00 | −0.18 | −0.48 | 0.16 | −0.08 | 0.09 | 0.21 | −0.15 | −0.25 | 0.26 |
| **Total** | **−0.05** | **0.01** | **−0.09** | **0.02** | **−0.05** | **−0.04** | **−0.05** | **−0.12** | **−0.03** | **−0.01** |

*Trigger date and days +1 to +10 (p. 523):*

| Year | 0 | +1 | +2 | +3 | +4 | +5 | +6 | +7 | +8 | +9 | +10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2001 | 1.41 | 2.44 | 0.28 | −0.27 | 0.08 | 0.17 | 0.05 | 0.03 | 0.37 | 0.00 | −0.77 |
| 2002 | 1.43 | 1.44 | 0.48 | 0.06 | 0.00 | 0.19 | 0.13 | 0.56 | −0.04 | −0.12 | 0.20 |
| 2003 | 0.89 | 0.95 | −0.24 | −0.10 | 0.10 | 0.26 | 0.27 | 0.21 | 0.06 | 0.21 | 0.01 |
| 2004 | 0.91 | 1.72 | 0.75 | −0.19 | −0.37 | 0.10 | 0.03 | 0.29 | 0.13 | 0.01 | −0.11 |
| 2005 | 0.84 | 1.34 | 0.47 | 0.33 | 0.45 | 0.24 | 0.24 | −0.03 | 0.13 | −0.04 | −0.07 |
| 2006 | 1.60 | 2.12 | 0.23 | 0.03 | 0.20 | −0.02 | 0.15 | 0.13 | 0.16 | 0.16 | 0.12 |
| 2007 | 0.99 | 1.65 | 0.33 | 0.08 | 0.25 | 0.11 | 0.39 | 0.30 | 0.32 | 0.23 | −0.22 |
| 2008 | 0.14 | 1.95 | 0.43 | 0.34 | 0.19 | 0.10 | −0.04 | 0.09 | −0.17 | 0.27 | 0.13 |
| 2009 | 0.88 | 1.92 | 0.40 | 0.16 | 0.01 | −0.05 | 0.34 | 0.21 | 0.75 | 0.45 | 0.20 |
| 2010 | 0.37 | 1.24 | 0.27 | 0.07 | 0.20 | −0.17 | 0.35 | 0.08 | 0.29 | 0.25 | −0.16 |
| 2011 | 0.58 | 1.71 | 0.46 | −0.05 | −0.16 | −0.09 | −0.14 | −0.01 | 0.20 | 0.41 | −0.33 |
| 2012 | 1.06 | 1.57 | 0.53 | 0.13 | 0.06 | −0.04 | 0.20 | 0.34 | 0.24 | 0.06 | −0.17 |
| 2013 | 0.92 | 1.65 | 0.56 | −0.21 | 0.28 | 0.27 | 0.14 | 0.40 | 0.16 | 0.10 | 0.11 |
| 2014 | 0.78 | 1.59 | 0.23 | 0.12 | 0.16 | −0.02 | 0.59 | 0.21 | 0.10 | −0.07 | −0.19 |
| 2015 | 1.18 | 1.88 | 0.46 | 0.17 | 0.11 | 0.10 | 0.09 | 0.37 | 0.18 | 0.32 | 0.03 |
| 2016 | 0.81 | 1.96 | 0.43 | 0.12 | −0.16 | 0.19 | −0.02 | 0.06 | 0.46 | 0.49 | 0.52 |
| 2017 | 0.35 | 1.16 | 0.35 | 0.54 | −0.36 | 0.00 | 0.49 | 0.08 | 0.46 | 0.25 | −0.09 |
| 2018 | 0.75 | 1.02 | 0.08 | 0.22 | 0.06 | 0.06 | 0.02 | 0.33 | 0.32 | −0.16 | −0.02 |
| 2019 | 0.79 | 1.47 | 0.19 | 0.67 | 0.06 | 0.19 | 0.30 | −0.13 | 0.51 | 0.59 | −0.01 |
| 2020 | 0.79 | 1.36 | 0.30 | 0.00 | 0.33 | 0.04 | 0.26 | 0.61 | 0.22 | −0.06 | −0.03 |
| 2021 | 1.23 | 1.24 | −0.28 | −0.16 | −0.41 | 0.08 | 0.22 | 0.08 | 0.91 | 0.32 | −0.16 |
| 2022 | 0.73 | 1.62 | 0.10 | 0.47 | −0.06 | 0.79 | 0.11 | −0.14 | 0.40 | 0.28 | −1.04 |
| **Total** | **0.90** | **1.61** | **0.31** | **0.11** | **0.06** | **0.12** | **0.18** | **0.18** | **0.26** | **0.17** | **−0.10** |

**What the recovered signs buy us.** Three things the card could not say before:
1. **No pre-trigger drift.** Every pooled pre-trigger cell is between −0.12 and +0.02 — the run-up starts *at* the
   trigger, not before it. That is a clean (if unstandardised) placebo, and it is worth citing when we defend our
   own event window.
2. **Day +10 is negative (−0.10), not zero**, and 2022's day +10 is −1.04. Their "falling to zero on day 10" is a
   description, not the number.
3. **The daily series is tiny after day +2** (0.31, 0.11, 0.06, 0.12, 0.18, 0.18, 0.26, 0.17, −0.10), so the
   trigger date and day +1 alone are 2.51 of the **3.80** the pooled sample cumulates over days 0 → +10 (66%).
   But Table 3's Delta = 10 bucket cumulates **5.09** over the *same* eleven days. Late filers are therefore not
   simply collecting more days of the same drift — they are a **different, higher-return set of filings**, by
   roughly 1.3 percentage points over what the average filing earns across the identical window. Table 1 and
   Table 3 sit awkwardly together and no one in the paper reconciles them. This is a self-selection result hiding
   inside their own descriptive tables, it is the sharpest technical criticism available against the headline,
   and it was invisible without the signs. *(The 3.80 is the verifier's arithmetic on the Table 1 Total row; the
   paper never computes it.)*

**On R13 — how they "project" the 10 → 5 effect.** They do **not** estimate anything on post-2024 data; the sample ends in 2022 and the paper was submitted three weeks before the rule took effect. The projection is a **within-pre-period cross-sectional comparison**: filings with Delta ≤ 5 versus filings with Delta 6–10, treating the difference in cumulated quiet-period returns (roughly 5.09% − 3.12% ≈ 2 percentage points, or 5.09% − 1.34% ≈ 3.75pp against same-day filers) as what the rule will remove. The abstract labels this a "baseline projection", not an estimate of the rule's effect.

## 4. Institutional facts used

- **SEC, *Modernization of Beneficial Ownership Reporting*, Release No. 33-11253; 34-98704; File No. S7-06-22** — cuts the initial Schedule 13D deadline **from 10 to 5 days** once 5% ownership is reached; **effective 5 February 2024** (pp. 516, 517).
- **(added by verifier — decisive for §5)** The paper states the legal window in **business** days, twice, on p. 518: the rule "reduces the maximum delay after the 'trigger date' … **from 10 business days to 5**", and "RC Ventures/Ryan Cohen had **up to 10 business days** to file a 13D with the SEC". `business day` returns exactly these two hits in the whole paper; `calendar day` returns **0**.
- **(added by verifier)** Their own Figure A1 (p. 534) then labels the historic regime "**Day 0 to day 10**", with no business-day qualifier — the timeline diagram and the p. 518 prose disagree with each other.
- Endnote 2 (**p. 531** — *page corrected by verifier; endnotes 1–5 sit on p. 531, 6–13 on p. 532*): the rule "will similarly change the passive investor's 13G filing deadline from ten to five days (with exceptions that are beyond the scope of this study)".
- The rule requires 13Ds to be filed in **13D/G-specific XML format** going forward (p. 531, citing SEC 2023a p. 269) — the fix for their own parsing problem.
- Section 13 of the Exchange Act; 17 CFR §240.13d-1; filers who are beneficial owners of **more than 5%** of a class of equity securities, with interest in "changing or influencing control of the issuer" (p. 517; the endnote-1 text "CFR §240.13d-1" is printed on p. 531).
- SEC's own DERA economic analysis (SEC 2023b) used **2011–2021 data for noncorporate-action filings** and found significant positive excess returns from day 0 to "day 5 following the last legal filing date (day +15)" (p. 520). Endnote 8 (p. 532) records that SEC (2023b) defines a noncorporate-action filing as one "necessitated from an activist shareholder acquiring shares on the open market rather than from events like mergers and acquisitions or compensation awards".
- **(added by verifier)** **von Lilienfeld-Toal & Schnitzler (2020)**, "The anatomy of block accumulations by activist shareholders", *JCF* 62: **13,413 initial 13D filings in the CRSP universe, 2001–2016**; excess returns and volume spike at the trigger date and persist beyond the filing date; no difference by activist type (p. 519). This is the benchmark Polk et al. say they corroborate — our own numbers must be situated against **both**.
- **(added by verifier)** **Flugum, Lee & Southern (2023)**, *Financial Management* 52(3): EDGAR search-activity and IP-address evidence that activists **pass material nonpublic information to allied investment firms during the quiet period**, before the 13D is filed (pp. 519–520). Directly on our mechanism — information leaks inside the window — and the card previously had nothing on it.
- **(added by verifier)** **Bebchuk, Brav, Jackson & Jiang (2013)**, "Pre-disclosure accumulations by activist investors: evidence and policy", *J. Corp. L.* 39(1) 1–34, cited at p. 521 (and p. 532 references) as the standing study of pre-disclosure accumulation. Note this is the **same** paper Ordóñez-Calafi & Bernhardt cite for "disclosure thresholds constrain funds' positions" — the two literatures meet at exactly one citation.
- **(added by verifier)** **Watkins (2022)**, "Consequences of prescribed disclosure timeliness: evidence from acceleration of the Form 8-K filing deadline", *TAR* 97(7) 429–463, cited at p. 518. A prior study of an accelerated SEC filing deadline exists, with a real before/after design; Polk et al. cite it for motivation and do not adopt its method. That is both a template for our identification and a stick to beat theirs with.
- **(added by verifier)** The counterparty they name is **retail**: "in light of the heavy increase in options trading (Banerji, 2023), our findings provide evidence that activist investors may enjoy an increase in excess returns by delaying their filings **at the expense of retail investors**" (p. 518).
- SEC quoted as saying the 10-day deadline "contributes to information asymmetries that could harm investors" (p. 517, citing SEC 2023a p. 16).
- **Commissioner Hester Peirce's dissent** to the proposal — cited as the reason five days may not be the right cutoff either (p. 531).
- Worked example: **Ryan Cohen / RC Ventures LLC in Bed Bath & Beyond**, trigger date 24 Feb 2022, 13D filed 7 Mar 2022; 1,667,833 shares for $23.7m on the trigger date taking him to 6.1%; a further 1.94m shares for $32.1m and 1.67m call options for $1.8m *after* the trigger date; final position 9,450,100 shares (9.8%), $119m for 7,780,000 shares plus $1.8m for options (pp. 518–519, Appendices 2–3, pp. 535–537).
- The Cohen example is the paper's only demonstration of the mechanism our model cares about: **post-trigger, pre-filing accumulation**. They present it as a timeline, not as a variable. *(added by verifier)* Appendix 3 (p. 537) makes the accumulation explicit and line-item: of 35 purchases, **numbers 22–35 fall on 25 Feb–3 Mar 2022 — after the 24 Feb trigger and before the 7 Mar filing** — including the whole option position. **And their showcase filing has Delta = 11 calendar days**, which puts it off the right-hand edge of Tables 3, 4 and 5 (all of which stop at 10) while being comfortably legal at 7 business days. Endnote 4 (p. 531) also notes that "Cohen's sale of Bed Bath & Beyond is currently under SEC investigation".

## 5. Referee-facing strengths / weaknesses

**Strengths:**
- **They hand-built the trigger date**, which is the variable that matters and which is not available from Audit Analytics or the SEC directly (p. 538). Prior work grouped all filings together; this is the paper's stated contribution and it is a real one.
- Long sample (2001–2022) and the first to include the post-pandemic years.
- The Delta gradient survives every subsample they cut it on — profitability, reason for filing, firm size, R&D intensity, 8-K news, pre/post-COVID. The 8-K cut (R6) in particular removes the most obvious confound (contemporaneous corporate news) and the gradient is undiminished.
- Limitations are stated plainly and the paper does not claim causal identification.

**Weaknesses / open flanks — this is a soft target and we should say so precisely:**
- **No standard errors or confidence intervals anywhere.** Tables 1, 3 and 4 print means only. Significance appears in three places: Table 5 italics at 0.05, Table 4's "n.s." row, and two p-values in prose. A referee at a finance journal would stop here.
- **No control group and no post-rule data.** The 10 → 5 claim rests on comparing filers who *chose* short delays with filers who *chose* long ones, in the pre-period. Delta is self-selected: a filer still accumulating, or negotiating, or working on a complex position, files late. The paper never addresses this, so what it measures is the return earned *during* a longer accumulation, not the return caused *by* the legal allowance. That is our sharpest criticism and it is the whole ballgame for the policy claim.
- **Calendar days versus business days — SETTLED FROM THE TEXT, not an inference.** *(upgraded by verifier; the reader flagged this as unverifiable and it is not.)* Four printed facts pin it down:
  1. The legal window is **business** days, in their own words, twice on p. 518 — "from 10 business days to 5", and Cohen "had up to 10 business days to file".
  2. **Delta is calendar days.** The note under Tables 3, 4 and 5 defines it arithmetically: "if the trigger date is March 1 and the filing date of Schedule 13D is March 4, the delta is 3." March 1 → March 4 is three calendar days.
  3. Table A1's note caps the sample at "larger than **12 days** (the 10-day window plus weekends)" — a calendar-day cap, and one that is **too tight**: ten business days spans up to **14** calendar days when two weekends fall inside, so a filer using the window exactly as the law allows can be dropped from the sample.
  4. Their own Figure A1 (p. 534) then labels the historic regime "Day 0 to day 10" with no business-day qualifier, contradicting p. 518.

  The consequence is not cosmetic. **Delta = 10 is not "the historically allowed 10-day limit"** (p. 526); it is ten calendar days, which for most filings is *inside* the legal window with days to spare. The 4,608 filings piled at Delta = 10 are therefore not "filers who waited as long as legally possible" — that is the paper's central interpretive claim (Q5, p. 526) and it does not follow from a calendar-day Delta. **Their own headline example proves it:** Cohen triggered 24 Feb 2022 and filed 7 Mar 2022 — Delta = 11 calendar days, off the edge of every table, yet only 7 business days, three short of the limit. This is the single most useful thing we can say about this paper, because it is a measurement error in the treatment variable, sourced entirely from their own pages.
- **Massive attrition, non-random.** 23,123 of 42,378 filings (55%) are lost purely because the trigger date is not machine-readable, and they say so: "trigger dates in more than 50% of Schedule 13D filings are inaccessible due to inconsistent HTML formatting" (p. 531). Whether unparseable filings differ systematically (older filers, smaller law firms, paper filings) is not examined. A further 9,550 are dropped on the >12-day rule.
- **4,608 of 9,685 observations (48%) sit in the single Delta = 10 bucket**, and the gradient is not monotone — Delta = 4 (1.63%) is below Delta = 3 (3.60%) and Delta = 1 (1.94%). The "steady increase" language overstates a noisy pattern.
- **(added by verifier) Table 1 and Table 3 do not reconcile, and the gap is the selection effect.** Summing the Table 1 pooled daily returns over days 0 → +10 gives **3.80%**; Table 3's Delta = 10 bucket reports **5.09%** over the same eleven days. Late filers earn about 1.3pp more across an identical window than the average filing does — so the Delta gradient is substantially a *composition* effect, not an *elapsed-time* effect. The paper never computes the pooled cumulative and never notices. Combined with the calendar-day problem above, the treatment variable is both mismeasured and self-selected.
- **Internal inconsistencies** — *each one re-checked at the page cited by the verifier; all six confirmed, and two more found.* Text p. 520 says ~45% of 2022 originals were filed before the final day; endnote 9 (p. 532) says 25% of all filed 13Ds were within 5 days. Appendix Table A1 (p. 534) drops 23,123 filings and applies a >12-day cut; Appendix 4 (p. 538) says "we lose 23,820 Schedules 13D" and applies a **>30-day** cut, retaining 14,635. The limitations paragraph reverses the regimes — "compare the previous five-day and current 10-day 'quiet period'" — which is backwards (**p. 531**, *page corrected by verifier; the card said 530*). **Two further ones the card missed:** (a) Table 1's note promises "each day from 15 days before the trigger date to 15 days after", but the printed table runs **−10 to +10** — days ±11…±15 do not exist anywhere in the paper; (b) the loss-vs-profit result on p. 524 cross-references "(Figure 5)", but Figure 5 (p. 527) is the **pre-/post-COVID** figure, and the loss/profit split is never plotted. Also worth knowing: Table 4's note prints a `*/**/***` significance legend at the 0.1/0.05/0.01 levels that is never used, since every cell in that table is "n.s.". None of this is fatal but it signals light refereeing at the venue.
- Descriptive event-study design, published in a regulation-and-compliance journal — not a competitor for identification, only for territory.

## 6. What they do NOT do (scope boundary)

**Object.** Cumulated **abnormal return to the filer over the quiet period** (trigger date to filing date), plus abnormal trading volume. That is all. There is **no takeover premium, no bidder entry, no campaign success, and no liquidity measure**: grep over the full extracted text returns **0 hits** for `liquid*`, `Amihud`, `bid-ask`, `spread`, `turnover`, `takeover`, `premium`, `bidder` — **independently re-run by the verifier on a whitespace-insensitive index of a fresh `-layout -raw` extraction, all eight confirmed at zero.** The same run also returns **0 hits** for `standard error`, `confidence interval`, `t-statistic`, `regression`, `difference-in-difference`, `matching` and `placebo`, which is the mechanical confirmation of the no-inference point in §5. "Acquisition" and "merger" appear only in endnote 8 (defining what the SEC excluded) and in the boilerplate on the 13D cover page. The word "control" appears **twice** *(count corrected by verifier: the card said once)* — the statutory phrase "changing or influencing control of the issuer" (p. 517), and "Mr. Cohen **controls** RC Ventures LLC" in endnote 5 (p. 532). Neither is a control outcome; the paper never measures one.

**Margin.** The **window margin**, and only the window margin. The 5% threshold level is taken as given and never varied.

**Identification.** Descriptive event study on **pre-rule data only (2001–2022)**, comparing self-selected filing delays. No control group, no DiD, no post-2024 estimation, no regression, no standard errors.

**What they say is left open** (all from §6, pp. 530–531, and the abstract):

> "our analyses are unable to rule out idiosyncratic changes to regulations, court decisions or other market forces that" [specifically impact a small subset of firms but do not impact the market as a whole] (p. 530, sentence continues onto p. 531)

> "trigger dates in more than 50% of Schedule 13D filings are inaccessible due to inconsistent HTML formatting" (p. 531)

> "it may be the case that activist shareholders will adjust to exploit 'information asymmetry' over the investing public over a shorter time horizon after the five-day regime is implemented" (p. 531)

> "While we can give no assurance that the new five-day reporting regime is 'optimal,' our results suggest that reducing the reporting period from 10 to 5 days will improve transparency and provide a more level playing field for the investing public." (p. 518)

## 7. Implications for our position

**What they occupy:** object = **the filer's own abnormal return during the quiet period**; margin = **window (10 → 5 days)**; identification = **descriptive event study, pre-rule data, self-selected delay, no control group**.

They are on **our margin** — this is the paper that gets cited whenever someone says "the Feb-2024 window change has been done". So the positioning has to be exact:

1. **They share our margin but not our object.** They measure what the *blockholder* earns. We measure what happens to *control outcomes* — bidder entry, takeover premium, campaign success — which is what the Williams Act was written about and what OCB's threshold literature also never touches. The blockholder's own return and the minority's gain from control are different objects that can move in opposite directions; that is exactly our premium-wedge story. Naming this contrast is our cleanest separation from them.
2. **They share our margin but not our identification.** No control group, no post-rule data, no SEs, self-selected treatment. Our referee checklist (control group or bounded null, confound list, power/MDE, placebo, pre-trend, parser validation) is a strictly higher bar than anything in this paper. If our one clean result carries a control group and post-2024 data, we dominate them on identification without needing a new object.
3. **Liquidity is completely absent.** Zero liquidity measures in the paper. The interaction κ × window — our driving variable crossed with our margin — is untouched by the competitor closest to our anchor. This is the strongest single sentence available for our whitespace claim on the empirical side.
4. **They supply the benchmark number we must situate ourselves against.** The 1.34% → 5.09% delay gradient (Table 3) is the standing estimate of "what the window is worth to the filer". Our estimate of what the window is worth in *premium* terms should be reported next to it, with the difference in object made explicit.
5. **Their parsing problem is our methodological opening.** Over 50% of pre-2024 trigger dates are unrecoverable from HTML; the Modernization rule mandates XML from Feb-2024 onward. Our post-2024 parse is mechanically cleaner than anything possible pre-2024 — and their own attrition table is the citation that proves it. This also matters for the checklist's "parser validation" item: we can validate against the same EDGAR source and report a recovery rate against their 45%.
6. **Their open question is our question.** They concede that activists "will adjust to exploit 'information asymmetry' over the investing public over a shorter time horizon" (p. 531) — i.e. they have no model of how the blockholder re-optimises when the window shrinks. That is precisely what a model with κ and a window margin delivers. Cite this as the gap they name and cannot fill.

7. **(added by verifier) Their treatment variable is mismeasured, and we can say so from their own pages.** Delta is calendar days; the rule is business days (Q13/Q14/Q15). So "Delta = 10" is not the legal maximum, the 48% mass at Delta = 10 is not "filers waiting as long as legally possible", and their >12-calendar-day filter drops filings that used the window lawfully. This is a cleaner criticism than "no control group", because it is a measurement point, it is internal to their paper, and it applies to *any* future study that reuses their Delta. **Our own window variable must be constructed in business days against the actual filing calendar**, and we should say in one line that we do so.
8. **(added by verifier) Watkins (2022) is the identification template neither we nor they should ignore.** A published study of an accelerated SEC filing deadline (Form 8-K) already exists and is in their reference list (p. 533). If we run a before/after on the Feb-2024 change, that is the design we are extending — and the fact that Polk et al. cite it while running a pre-period cross-section is the fairest possible statement of the gap between the two papers.
9. **(added by verifier) The leakage evidence is on our side of the argument.** Flugum et al. (2023) show information moving to allied funds *inside* the quiet period (pp. 519–520). A model in which the window creates a tradable state — our "crossed but not yet flagged" cell — has an empirical counterpart already in print. Cite it when we motivate the window margin, not just the rule change.

**Risk to manage:** because they are on our margin and already published on it, a referee may read us as a follow-on. The defence is object plus identification, stated in one sentence in the introduction — *Polk et al. (2024) measure what the filer earns during the pre-disclosure window using pre-rule filings and self-selected delays; we measure what the window does to the takeover premium and bidder entry, with liquidity as the driving variable* — not "they were descriptive and we are rigorous".

## 8. Quotes we may lean on (verbatim, page-cited)

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "we compare excess returns associated with initial filings made by investors filing a Schedule 13D within five days (i.e. those that meet the modernization requirement) with those filing between 6 and 10 days (i.e. those that meet the historic requirement)." | p. 517 | Their whole identification strategy in one sentence — a pre-period cross-section of self-selected delays, no control group. |
| Q2 | "the excess returns increase from 1.34% for those filing on the trigger date to 5.09% for those filing on the tenth day following the trigger date" | p. 517 | The headline number, as they state it. |
| Q3 | "the authors establish an updated 'baseline projection' for expectations regarding how the Modernization final rule will impact activist investors and stock returns under a five-day reporting regime" | p. 516 | Their own word for it: a *projection* from pre-rule data, not an estimate on post-rule data. |
| Q4 | "we are left with 9,685 initial Schedule 13D filings over the period 2001–2022, representing 5,863 reporting entities invested in 5,037 unique firms" | p. 520 | Sample, exactly as printed. |
| Q5 | "The median number of days is 10, consistent with most shareholders waiting the full 10-day period before filing a Schedule 13D" | p. 526 (Figure 3 note) | Half the sample sits at the maximum Delta — the mass driving the headline gradient. |
| Q6 | "approximately 45% of original Schedule 13D filings in 2022 were filed before the final day to file" | p. 520 | The compliance margin; also, with Q7, an internal inconsistency. |
| Q7 | "25% of all filed Schedule 13Ds were filed within 5 days of the trigger date and would therefore be unaffected by the new rule." | p. 532 (endnote 9) | How much of the population the rule actually binds on — directly useful for our power/MDE calculation. |
| Q8 | "trigger dates in more than 50% of Schedule 13D filings are inaccessible due to inconsistent HTML formatting" | p. 531 | Their attrition problem; our parser-validation opening; the reason post-2024 XML data is cleaner. |
| Q9 | "it may be the case that activist shareholders will adjust to exploit 'information asymmetry' over the investing public over a shorter time horizon after the five-day regime is implemented" | p. 531 | The gap they name and cannot close — re-optimisation under a shorter window. That is a theory question, i.e. ours. |
| Q10 | "our analyses are unable to rule out idiosyncratic changes to regulations, court decisions or other market forces that" | p. 530 | Their own statement that confounds are unaddressed. *(Sentence runs onto p. 531: "…specifically impact a small subset of firms but do not impact the market as a whole.")* |
| Q13 *(added by verifier)* | "The Modernization of Beneficial Ownership Reporting rule reduces the maximum delay after the 'trigger date,' when a new owner meets or exceeds the 5% ownership level, from 10 business days to 5." | p. 518 | **The load-bearing quote for our critique.** They say *business* days here, and count Delta in *calendar* days everywhere else. |
| Q14 *(added by verifier)* | "For example, if the trigger date is March 1 and the filing date of Schedule 13D is March 4, the delta is 3." | p. 526 (Table 3 note; repeated verbatim under Tables 4 and 5) | The calendar-day definition, in their own worked example. Pair with Q13. |
| Q15 *(added by verifier)* | "larger than 12 days (the 10-day window plus weekends)" | p. 534 (Table A1 note) | Their sample cap, which mis-states the legal window: 10 business days can span 14 calendar days, so compliant late filers are dropped. |
| Q16 *(added by verifier)* | "about half of the original Schedule 13D filings are a shareholder's first filing with the SEC" | p. 521 | Stops us from describing their sample as first-time filers, and is their own reason for reading the returns as a market-wide activism reaction rather than an investor-identity effect. |
| Q17 *(added by verifier)* | "there is a steady increase in abnormal trading volume as investors wait longer to file" | p. 521 (Figure 4, p. 527) | The quantity-side counterpart to the return gradient — the closest they get to our post-trigger accumulation channel. |
| Q11 | "While we can give no assurance that the new five-day reporting regime is 'optimal,' our results suggest that reducing the reporting period from 10 to 5 days will improve transparency and provide a more level playing field for the investing public." | p. 518 | The policy conclusion, correctly labelled by them as unproven optimality — ASSERTED, not estimated. |
| Q12 | "Third, we note our analyses compare the previous five-day and current 10-day 'quiet period' allowed under the regulations governing Schedule 13D filings." | **p. 531** *(corrected by verifier)* | Printed exactly this way — the two regimes are reversed. Evidence for how lightly the venue refereed; use only if we need to characterise the competitor set's rigour, and quote it fairly. |

## 9. Verification log

**Verifier:** adversarial second reader, 2026-08-19.
**Method.** The PDF was re-extracted page by page with `pdftotext -f N -l N -layout -raw` and piped through
`tr '\002' '-'` — this paper encodes its minus sign as the control byte `\x02`, which plain extraction silently
drops. Pages were then indexed so every quote resolves to a printed page mechanically. Quote matching was run on
a whitespace-stripped index, because Emerald's PDF fuses words together across whole clauses
("Schedule13Dappears in theSECelectronic"), which defeats naive `grep -F`. Printed p. 516 = PDF p. 1 confirmed
from the front matter; mapping printed = 515 + PDF page holds throughout. Ligatures normalised; nothing else.

**Counts: OK 26 · WRONG 1 · MISCITED 4 · UNCHECKED 0.**

*(No UNCHECKED items. Everything the reader flagged as unverifiable — the minus signs, and the calendar-day
question — turned out to be checkable, and both were checked.)*

### Table 1 minus signs — the extraction problem, closed

`pdftotext … -layout -raw file.pdf - | tr '\002' '-'` recovers every sign. Both halves of Table 1 are now
transcribed into §3 in full (22 years × 21 days, plus the Total, Marginal return and Difference-in-marginal-return
rows). Tables 3, 4 and 5 were re-read the same way; **every number the card already quoted from them is correct
and correctly signed.** Three findings only visible with signs restored have been added to §3 and §5:
no pre-trigger drift; day +10 is −0.10% rather than zero; and Table 1's pooled cumulative (3.80%) falls 1.3pp
short of Table 3's Delta = 10 figure (5.09%), which exposes the gradient as substantially a selection effect.

### Quotes (§8)

| Quote | Verdict | Checked against |
|---|---|---|
| Q1 | **OK** | Exact, printed p. 517. |
| Q2 | **OK** | Exact, printed p. 517. |
| Q3 | **OK** | Exact, printed p. 516 (Originality/value). |
| Q4 | **OK** | Exact, printed p. 520. |
| Q5 | **OK** | Exact, printed p. 526, Figure 3 note. |
| Q6 | **OK** | Exact, printed p. 520. |
| Q7 | **OK** | Exact, printed p. 532, endnote 9. |
| Q8 | **OK** | Exact, printed p. 531. |
| Q9 | **OK** | Exact, printed p. 531. |
| Q10 | **OK** | Exact, printed p. 530; the continuation clause resolves on p. 531, as the card notes. |
| Q11 | **OK** | Exact, printed p. 518. |
| Q12 | **MISCITED → fixed** | Text is exact, but it is printed on **p. 531**, not p. 530. Corrected in §8 and §5. |
| Q13–Q17 | **OK** | Added by the verifier; each string-matched at the page given. |
| §6 block quotes (4) | **OK** | All four exact at pp. 530, 531, 531, 518 respectively. |

Twelve of twelve original quotes are verbatim. One page was off by one.

### Results (§3)

| Result | Verdict | Checked against |
|---|---|---|
| R1 | **partly WRONG → corrected** | The prose claim is quoted correctly from p. 520. But the card rendered it as fact: Table 1's day +10 Total is **−0.10%**, not zero. Amended to attribute "falling to zero" to their prose and print the number. Also noted: they say "statistically above zero" while publishing no standard error. |
| R2 0.90% / 1.61% | **OK** | Table 1 Total row, p. 523, exact. |
| R3 1.34 → 5.09 and the full row | **OK** | Table 3 "Average return" row, p. 526, read with signs: 1.34, 1.94, 1.84, 3.60, 1.63, 3.12, 3.02, 4.11, 4.32, 4.73, 5.09. Every one of the eleven matches. |
| R4 bucket counts and median | **OK** | Figure 3 note, p. 526: (756)(633)(336)(312)(334)(281)(312)(560)(675)(878)(4608). They sum to **9,685**, the stated sample — an internal consistency check the card had not run. Median Delta = 10 confirmed. |
| R5 volume ≈ 5× normal, back to normal by +15 | **OK** | pp. 520–521; Figure 2, p. 524. |
| R6 1.38 → 5.88, p < 0.05 at Δ=5 and Δ=10 | **OK** | Table 5, p. 531 and text p. 527, both exact. Endnote 13 (p. 532) does give p < 0.01, as the card says. |
| R7 1.09 → 5.07 / 1.73 → 6.17, all n.s., n = 5,170 | **OK** | Table 4, p. 530, exact including the n. |
| R8 R&D 1.55 → 8.55 / 1.46 → 6.68 | **OK** | p. 525 text; endnote 12 (p. 532) defines R&D intensity as R&D/total assets. |
| R9 loss vs profit | **OK, cross-reference broken** | p. 524 confirmed. Their "(Figure 5)" pointer is wrong — Figure 5 is the COVID figure. Flagged in §3 and §5. |
| R10 reason for filing | **OK** | p. 524 text; Figure 6 Panels A–G at pp. 528, 529, 530. |
| R11 pre/post-COVID | **MISCITED → fixed** | Result correct; Figure 5 is on **p. 527**, not p. 529. Corrected in §2, §3 and §5. |
| R12 45% / 25% | **OK** | p. 520 and endnote 9, p. 532. Both confirmed, and they are indeed different denominators. |
| R13 the policy conclusion | **OK as ASSERTED** | pp. 516, 518, 530. The abstract's own word is "baseline projection"; the sample ends 2022; there is no post-rule data. Label stands. |
| "No SEs or CIs anywhere" | **OK — mechanically confirmed** | `standard error`, `confidence interval`, `t-statistic`, `regression`, `difference-in-difference`, `matching`, `placebo`: **0 hits each**. Inference appears in exactly four places: Table 5's italics-at-0.05 note, Table 4's all-"n.s." row, p. 527's two p < 0.05 statements, and endnote 13's p < 0.01. Table 4 also prints a `*/**/***` legend it never uses. |

### Scope claims (§6) — independently re-run

`liquid*` **0** · `Amihud` **0** · `bid-ask` **0** · `spread` **0** · `turnover` **0** · `takeover` **0** ·
`premium` **0** · `bidder` **0** · `tender` **0**. **All nine confirmed at zero.** The whitespace-insensitive
index matters here: a naive grep on this PDF can miss hits inside fused word-runs, so a zero from plain `grep`
would not have been trustworthy. These zeros are trustworthy.

`control` **2** — one **WRONG** count in the card, which said one. The second is "Mr. Cohen controls RC Ventures
LLC" (endnote 5, p. 532). Neither is a control outcome, so the substance holds. `merger` 1 and `acquisition` 2,
both exactly where the card said (endnote 8, p. 532; the 13D cover-page boilerplate, p. 535).

### Venue / header

**OK.** Front matter p. 516: *JFRC* Vol. 32 No. 4, 2024, pp. 516–538, DOI 10.1108/JFRC-01-2024-0016, Emerald;
Received 26 January 2024, Revised 1 May 2024, Accepted 7 May 2024; JEL D43, G18, G32, G34, G38, M48, P51;
paper type "Research paper". 23 PDF pages. All as stated. Author affiliations also confirmed (Clemson; Alabama ×2;
Northern Illinois). Worth noting for how we characterise them: **all four authors are accountancy faculty**, and
the acknowledgements thank SEC DERA staff for insights into the proposal.

### The decision-critical question the reader could not settle — now settled

**Is Delta calendar days or the legal business-day window? Calendar days. Confirmed, four ways, from the text.**

1. p. 518, twice: the rule cuts the delay "from **10 business days** to 5", and Cohen "had up to **10 business
   days** to file". `business day` = exactly 2 hits; `calendar day` = 0.
2. The note under **Tables 3, 4 and 5** defines Delta arithmetically — "if the trigger date is March 1 and the
   filing date … is March 4, the delta is 3" — which is calendar subtraction.
3. **Table A1** (p. 534) caps the sample at "larger than 12 days (the 10-day window plus weekends)". Ten business
   days spans up to **14** calendar days, so this filter is too tight and drops lawful full-window filers.
4. **Figure A1** (p. 534) labels the historic regime "Day 0 to day 10", flatly contradicting p. 518.

**Their own headline example settles it beyond argument:** Cohen triggered 24 Feb 2022 and filed 7 Mar 2022 —
**11 calendar days**, which is off the right edge of every table in the paper, but only **7 business days**, three
inside the limit. So the interpretation carrying the whole paper — that the 4,608 filings at Delta = 10 are
"shareholders waiting the full 10-day period" (Q5) — does not follow from their measure. This is now stated as
established fact in §5 and §7, not as an inference, and it is the strongest thing we hold against this paper.

### Omissions added by the verifier

1. **§3 R14 / §8 Q17 — Figure 4, p. 527: abnormal *volume* rises with Delta.** The card had no entry for Figure 4
   at all. It is their only quantity-side evidence and the nearest thing in the paper to our post-trigger
   accumulation channel.
2. **§3 R15 — no pre-trigger run-up.** Recovered from the signed Table 1; every pooled pre-trigger cell lies in
   [−0.12, +0.02]. A usable placebo, and it strengthens *their* trigger-date measurement while weakening their
   Delta interpretation.
3. **§3 / §5 — Table 1 and Table 3 do not reconcile** (3.80% pooled vs 5.09% for the Δ=10 bucket over identical
   days). Self-selection visible inside their own descriptive tables. The paper never computes the pooled sum.
4. **§4 — von Lilienfeld-Toal & Schnitzler (2020)**, 13,413 initial 13Ds 2001–2016 (p. 519): the benchmark this
   paper corroborates, and a second number our estimate must sit beside.
5. **§4 — Flugum, Lee & Southern (2023)** (pp. 519–520): MNPI passed to allied funds *during* the quiet period.
   Published evidence for the "crossed but not yet flagged" state our model needs.
6. **§4 — Bebchuk, Brav, Jackson & Jiang (2013)** (p. 521): the standing pre-disclosure-accumulation study, and
   the single citation the OCB theory card and this empirical card share.
7. **§4 — Watkins (2022, TAR)** on the Form 8-K deadline acceleration (p. 518): a prior accelerated-deadline
   study with a real design, cited by them and not emulated. Our identification template.
8. **§4 — the retail-investor framing and the options channel** (p. 518, Banerji 2023).
9. **§4 — Appendix 3 read line by line** (p. 537): purchases 22–35 all fall between the trigger and the filing,
   the option position included. Their own exhibit is a picture of in-window accumulation.
10. **§4 — endnote 4, p. 531:** Cohen's BBBY sale is under SEC investigation. Worth knowing before we reuse the
    example.
11. **§4 — endnote 8, p. 532:** the SEC's "noncorporate action filing" definition, which is how DERA excluded
    M&A-driven filings. Directly relevant if we build a comparable sample.
12. **§5 — two further internal inconsistencies:** Table 1's note promises ±15 days and prints ±10; and the
    loss/profit result points at Figure 5, which is the COVID figure.
13. **§2 — "initial filing" ≠ "first-time filer".** Only about half the sample is the latter (p. 521). The card's
    unit-of-observation line has been corrected.

### Overall verdict

**The card was accurate on the numbers and wrong about what it could not check.** All twelve quotes are verbatim;
every headline figure — 1.34 → 5.09, 0.90/1.61, 9,685 / 5,863 / 5,037, 42,378, 55% attrition, n = 5,170,
1.38 → 5.88 — matches the print exactly, and the "no standard errors anywhere" and "zero liquidity/takeover/
premium/bidder" claims both survive mechanical re-checking. One count was **WRONG** ("control" appears twice, not
once) and four page citations were **MISCITED** (Q12 and the p. 530 regime-reversal → p. 531; endnote 2 → p. 531;
Figure 5 → p. 527, twice). Against that, the two things the reader marked as beyond reach were both recoverable
and both changed the card materially: the minus signs came back with a one-line pipe, and the calendar-versus-
business-day question is settled against the paper by four separate passages plus their own worked example.
**Net: this paper is weaker than the card credited it with being**, and the reason is not the missing control
group the reader emphasised — it is that the treatment variable does not measure the legal window it is named
after. That is the sentence to carry into our introduction.
