# Ben-David, Bhattacharya, Huang & Jacobsen (2026) — "The (Missing) Relation between Acquisition Announcement Returns and Value Creation"

**Venue / status:** ***The Journal of Finance*** **Vol. LXXXI (81), No. 3, June 2026, pp. 1265–1320.** DOI **10.1111/jofi.70038**. Open access (Creative Commons Attribution-NonCommercial-NoDerivs). Initial submission 7 April 2024; accepted 14 February 2025. **Author list exactly as printed on the masthead: ITZHAK BEN-DAVID, UTPAL BHATTACHARYA, RUIDI HUANG, and STACEY JACOBSEN** (Ohio State + NBER; HKUST; Southern Methodist; Southern Methodist). *(Masthead verified 2026-08-19 against `research/txt_extracts/ben_david_et_al_2026_jf.pdf` — 56 pages, printed 1265–1320, **printed = PDF page + 1264**. See §9b.)*
**Version caveat (read this first):** the ticket named the paper as "Ben-David, Bhattacharya, **Huang** & Jacobsen (2026)". **The ticket was right and the WP was a three-author version.** The file §§1–8 below were read from is **NBER Working Paper No. 27976, October 2020, Revised May 2025** (`lit/bendavid-etal-jf2026-nber.pdf`, 98 PDF pages), which has **three** authors — Itzhak Ben-David, Utpal Bhattacharya, Stacey E. Jacobsen — and no Huang. **Huang joined between that WP and publication.** Cite the four-author form. **Every page number in §§1–8 is a WP page; §9b gives the WP → JF page map for the passages we use, and flags eight quotes that were re-edited in the published version.**
**Full text from:** `lit/bendavid-etal-jf2026-nber.pdf` (98 pp), re-extracted with page breaks to `research/txt_extracts/bendavid_jf2026_pages.txt`; also `research/txt/bendavid_missing_relation_jf2026.txt` (same content, no page markers) · **Reader:** opus · **Read:** full main text (printed pp. 1–55 plus references), Internet Appendix table/figure headers and the appendix sections cited in the main text.
**Page numbering used:** the **printed page numbers of this NBER WP** (main text 1–62; PDF page = printed page + 2). Internet Appendix pages are cited as "IA p. N" (its own 1–33 sequence, PDF pages 66–98; PDF p. 65 is the unnumbered Internet Appendix title page). Verified: PDF 10 → printed 8, PDF 16 → printed 14, PDF 53 → printed 51, PDF 64 → printed 62.
**Type:** empirical (measurement / methodology critique)   **Role for us:** measurement — it is the referee's stick for any empirical leg that uses announcement returns.

## 1. Question

Financial economists have used cumulative abnormal returns (CAR) around an acquisition announcement as *the* market-based estimate of the deal's net present value for five decades. The paper asks whether that identification survives contact with data: does announcement CAR actually correlate with what the deal turned out to be worth? It then asks the sharper question — even setting realized outcomes aside, does CAR at least reflect the information about the deal that was *already public* at the announcement? The answer to both is essentially no, and the paper then argues why: CAR is a blend of deal NPV and a much larger acquirer-specific signal that the announcement itself reveals.

## 2. Model / data and method

**Sample.** Thomson Reuters SDC Domestic M&A; announcements 1 Jan 1980 – effective by 31 Dec 2018; US publicly traded acquirer; ≥50% of shares sought; acquirer held <50% six months before; Compustat + CRSP coverage; non-missing deal value. LBOs, spinoffs, repurchases, self-tenders, recapitalisations, privatisations, stake purchases and partial-interest acquisitions excluded. Initial sample **47,543 deals**: 42,354 completed, 2,227 withdrawn, 2,962 not completed and not withdrawn (p. 8).

**Working samples** (they differ because outcome data differ, p. 14 Table I Panel A):
- Non-impairment: **6,128** (deals from 2003 on, deal value >$10m and ≥5% of acquirer market cap; 8,367 → 6,767 → 6,437 → 6,128, p. 11)
- Short-term abnormal ROA: **28,710**; Long-term abnormal ROA: **22,577**
- Completion: **39,585** (completed + withdrawn, 1980–2018)
- DGTW-adjusted 60-month BHAR: **27,355**

**Ex-ante measure (the object under attack).** Acquirer CAR from a market model (α, β estimated over days −361 to −61; CRSP value-weighted index), summed over **[−1, 1]** and **[−5, 5]**; plus **DealCAR [Announcement − 2, Close + 2]**, which resolves completion uncertainty at the cost of a long window (p. 8). Mean CAR[−1,1] = 0.9%, CAR[−5,5] = 0.8%, DealCAR = −1.1% (p. 14).

**Ex-post outcome measures (four, from four different sources).**
1. **Transaction-level goodwill non-impairment** — a hand-collected dummy for whether the goodwill created by *that specific transaction* was materially impaired within five years of the effective date. Built by taking every Compustat firm-level impairment of ≥5% of acquirer assets and reading the Notes to Consolidated Financial Statements in both the acquisition and impairment years to attribute the write-off to a named deal (pp. 9–11). This is the paper's genuinely new measure. 14.8% of sample transactions impair; the average impairment is 83% of transaction-level goodwill, 57% of the purchase price, 11% of acquirer assets (p. 11).
2. **Short-term abnormal ROA** — Chen et al. (2007) residual: post-acquisition industry-adjusted 3-year average ROA (t+1…t+3) regressed on the pre-acquisition 3-year average; Fama-French 48 industries (pp. 11–12).
3. **Long-term abnormal ROA** — same, with the post window moved to years t+4…t+6 (p. 12).
4. **Deal completion vs. withdrawal** dummy (pp. 12–13).
Validation of the outcome measures: they correlate 0.13–0.67 with each other despite different sources (p. 15); impairers suffer distressed delisting, poor operating/stock performance and CEO turnover (IA B, C, D); the market reaction to impairment news averages **−2.8%** (p. 10).

**Benchmark model (the alternative).** An OLS "characteristics-only" model using information available *at the announcement*: log market cap, leverage, free cash flow / lagged assets, Tobin's Q, prior-quarter market-adjusted return, relative deal size, and dummies for stock-only, mixed payment, diversifying, competed, hostile, public target (pp. 17–18).

**Designs.** (i) Univariate binning of outcomes on CAR vigintiles (Fig. 2); (ii) in-sample OLS of outcomes on CAR with/without characteristics and year × industry FE (Table II); (iii) subsample splits by decade (Fig. 3), by FF-12 industry (IA Fig. B2), by 29 deal/acquirer characteristics (IA Table B5), and a brute-force search over all interactions of 10 median-split dummies (IA Table B6); (iv) genuine out-of-sample: fit on the first half of the sample, predict the second (Table III, Fig. 4); (v) long-horizon validation via 60-month DGTW-adjusted BHAR decile spreads (Tables IV, V); (vi) a second-moment decomposition of `$CAR = CAR × acquirer market cap = NPV + X` under the identifying assumption that **|NPV| ∝ DealSize** and **|X| ∝ AcqMarketCap** (pp. 43, 48–51).

**Identification.** There is none in the causal sense and the paper does not claim any — this is a measurement-validity study: descriptive correlations, in- and out-of-sample prediction contests, and a variance-decomposition under a stated proportionality assumption.

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where (page / table) |
|---|---|---|---|
| R1 | Short-window CAR is unrelated to non-impairment and to short/long-term abnormal ROA: CAR[−1,1] coefficients −0.020 (0.105), 0.004 (0.012), −0.015 (0.014); CAR[−5,5] −0.008 (0.081), −0.001 (0.006), −0.004 (0.007); adjusted R² = 0.000 throughout | ESTIMATED | p. 18, Table II Panels A–C cols (1)–(2) |
| R2 | The long DealCAR[A−2, C+2] window is weakly significant for two outcomes — 0.089** (0.040) for non-impairment, 0.009** (0.003) for ST abROA — but a 1pp CAR fall raises impairment probability by only 0.09% against a 14.80% base rate ("less than a one-basis-point increase") | ESTIMATED | pp. 18–19, Table II col (3) |
| R3 | CAR does predict completion, correct sign, but trivially: 0.048* (0.023) raw, 0.050** (0.019) with characteristics; a 1pp CAR fall raises withdrawal probability by 0.05% against a 94.4% completion rate | ESTIMATED | pp. 18, 20, Table II Panel D |
| R4 | Adding CAR to a characteristics + year + industry FE regression does not raise adjusted R² at all (7.8% and 10.9% for ST/LT abROA with or without CAR) — "the explanatory power comes entirely from the controls and not from CAR" | ESTIMATED | p. 19, Table II cols (5) vs (7) |
| R5 | Pairwise correlations: the four ex-post outcomes correlate 0.13–0.67 with each other; their correlations with CAR[−1,1] and CAR[−5,5] run −0.01 to 0.02, and with DealCAR 0.01–0.05 | ESTIMATED (correlation matrix with significance stars) | pp. 14–15, Table I Panel B |
| R6 | Out-of-sample, characteristics-predicted outcomes load correctly and significantly on realisations (0.708***, 1.338***, 1.188***, 0.995***); CAR-predicted outcomes do not (26.039 (30.177), −0.855 (1.031), 6.573 (4.985)), except completion 1.090** (0.404) | ESTIMATED | p. 26, Table III Panel A |
| R7 | **CAR is not merely uninformative about realisations, it is orthogonal-to-wrong-signed on the *predictable* part of them**: regressing the characteristics-model prediction on CAR gives −0.104*** (0.005), −0.014*** (0.001), −0.010*** (0.003) for the three value outcomes and insignificant for completion | ESTIMATED | p. 26, Table III Panel B |
| R8 | 60-month DGTW-adjusted BHAR spread between top-three and bottom-three predicted deciles: characteristics model 9.2% / 10.7% / 9.4% / 7.9% (p = 0.005, 0.000, 0.000, 0.000); CAR model 0.1% / 2.8% / −0.8% / 2.8% (p = 0.986, 0.158, 0.726, 0.089) | ESTIMATED | p. 30, Table IV |
| R9 | "Listening" to CAR (withdraw on negative, complete on positive) yields a net 60-month return of **−5% mean / −17% median**; listening to characteristics yields **+21% / +26%** | ESTIMATED (portfolio means/medians; no SEs in table) | p. 36, Table V Panel C |
| R10 | Brute-force data mining finds no "golden subset": for non-impairment, 22,298 subsample regressions give correct sign and |t|≥2 in only 5% (1,091) of transactions in period 1, 3% (735) in period 2, and **0.26% (59/22,298) in both** | ESTIMATED (counts of estimates) | p. 24, IA Table B6 |
| R11 | Across 116 subsample regressions (4 outcomes × 29 characteristic splits) CAR is right-signed and 5%-significant in 19; in no subsample does it work for three or more outcomes | ESTIMATED (counts) | pp. 23–24, IA Table B5 |
| R12 | The 16-cluster grid inverts: the cluster with the **highest** average CAR (2.8% — not cash-only, private target, small acquirer, large relative size) has the **worst** ex-post outcomes (75.3% non-impairment vs. 85.2% sample mean; ST/LT abROA −0.8% vs. −0.2% mean) | ESTIMATED (cell means, no SEs reported) | p. 41, Table VI |
| R13 | Combined acquirer + target CAR for public targets (15–18% of samples) behaves exactly like acquirer CAR: insignificant for non-impairment and both abROA measures, significant but economically weak for completion | ESTIMATED | p. 21, IA Table B4 |
| R14 | Anticipation, truncation, selection and feedback are each tested and each fails to rescue CAR: excluding 1,047 explicitly-anticipated and 3,681 potentially-anticipated deals, or 28,266 repeat-acquirer deals, or extending the window to CAR[−41,1], or restricting to low-cancellation-probability deals, leaves CAR insignificant | ESTIMATED | pp. 32–35, IA Tables B1, B7–B10 |
| R15 | Under the bound |NPV / DealSize| ≤ 1, **91% of Cisco's deals (128 of 140)** and about **27% of all deals** (26.83% of positive-CAR, 26.90% of negative-CAR) imply economically impossible value creation/destruction | ESTIMATED (descriptive shares under an assumed bound) | pp. 44–46, Figs. 7–8 |
| R16 | Withdrawal does not reverse announcement CAR: only 53% of negative-announcement-CAR deals have positive withdrawal CAR, only 55% of positive-CAR deals have negative withdrawal CAR (2,141 withdrawn deals) | ESTIMATED (descriptive shares) | pp. 46–47, Fig. 9 |
| R17 | Second-moment decomposition: log|$CAR| loads 0.757*** (0.015) on log(acquirer market cap) vs 0.106*** (0.010) on log(deal size) — a ratio of ~6.5×; bin-level ~8×; acquirer-bin ~13×. Adjusted R² 0.684–0.981 | ESTIMATED | pp. 51–52, Table VII |
| R18 | Deal-related information never dominates $CAR at any relative size; at a merger of equals (relative size ≈ 1) it explains "about half" | ESTIMATED (coefficients with 95% CIs read off Fig. 11) | p. 52, Fig. 11 |
| R19 | The decomposition $CAR = NPV + X rests on the *assumed* proportionalities |NPV| ∝ DealSize and |X| ∝ AcqMarketCap; the claim that the acquisition trigger is what X captures is argued, not estimated | ASSERTED | pp. 43, 48 |
| R20 | Prescription: use a vector of publicly available characteristics rather than CAR to measure deal quality | ASSERTED (recommendation) | p. 55 |

## 4. Institutional facts used

- **SFAS 142** (FASB Statement 142), passed 2001, implemented 2002: acquirers must test goodwill for impairment on material events (and for much of the sample annually) and must report goodwill and impairment at the **reporting-unit** level rather than the firm level. This reporting-unit granularity is what makes transaction-level attribution possible at all, and it is why the impairment sample starts in **2003** (pp. 9, 11).
- **September 2011 FASB modification** of SFAS 142: formal fair-value/carrying-value comparisons are required only when qualitative indicators of impairment exist (p. 9 n.8).
- Data sources: SDC Domestic M&A (deals, rumour flags, high-tech dummy), CRSP (returns, value-weighted index), Compustat (accounting, firm-level goodwill impairment screen), hand collection from **Notes to Consolidated Financial Statements** in 10-Ks, **S&P Capital IQ M&A Rumors and Discussions** headlines for the anticipation tests (pp. 8–11, 32–33).
- Benchmarks: Fama-French 48 industries for ROA adjustment (p. 12); FF-12 for the industry split (p. 22); DGTW 5×5×5 size / book-to-market / momentum portfolios for long-run returns (p. 14 n.18).
- **(added by verifier) Completion rates split sharply by target status**: only **82% of public-target deals are completed** versus **97% of private-target deals** (p. 13 n. 16). The 94.4% headline completion rate is a private-target-weighted average.
- **(added by verifier) What actually causes withdrawal**: Jacobsen (2014), cited at p. 13 n. 15, finds that of withdrawn deals **14% are cancelled by regulatory or judicial obstacles and only 13% by target shareholders blocking or voting against the deal** — i.e. the shareholder-driven margin of the completion outcome is roughly one withdrawal in eight.
- **(added by verifier) Mean time to close a deal is 74 days** (p. 19), which is what makes DealCAR[A−2, C+2] "more than 10 weeks for which other information may be released".
- **(added by verifier) Pre-announcement run-up**: Betton et al. (2014) find run-ups **averaging 7%** in acquirers' prices before announcement (p. 32); the paper's own anticipation design sorts deals into terciles on the run-up window **CAR[−41, −2]** and re-runs on the middle tercile (p. 33, IA Table B8).
- **(added by verifier) Merger-arbitrage price pressure** (Mitchell, Pulvino & Stafford, 2004) is named by the authors, at p. 1 and again at p. 22, as one of the candidate explanations for CAR's failure — specifically for **public targets**. This is the one place where a liquidity/microstructure channel enters the paper, and it enters as a contaminant of announcement returns, not as an object.
- Literature census: of JF/JFE/RFS articles 1972–2021, 4.8% are M&A-related, 54.8% of those compute a value-creation measure, and **92.2% of those (202 articles) use CAR**, with no declining trend (p. 1 n.1).

## 5. Referee-facing strengths / weaknesses

**Strengths.**
- The new measure is the real contribution: a hand-collected, *transaction-level* goodwill impairment dummy, which fixes the standard problem that firm-level performance cannot be attributed to a particular deal. It is validated four ways (correlation with other outcomes, delisting/operating performance, a −2.8% market reaction to impairment news, CEO turnover).
- Four outcome measures from four data sources that agree with each other (0.13–0.67) but disagree with CAR (−0.01 to 0.02). This is the cleanest form of the argument: it is not that outcomes are unmeasurable, it is that CAR misses the measurable part.
- The out-of-sample Table III Panel B test is the one that hurts most and is hardest to dismiss: CAR fails to track even the *ex-ante predictable* component of outcomes, so "outcomes are noisy ex post" is not an escape.
- Exhaustive pre-emption of the standard defences (anticipation four ways, run-up terciles, truncation, selection, feedback, errors-in-variables by flipping CAR to the LHS, extreme-decile trimming, 22,298-regression brute force).
- Scale: 47,543 announcements, 1980–2018, public and private targets.

**Weaknesses / open flanks.**
- The variance decomposition that produces the headline "6× to 13×" rests entirely on the assumption |NPV| ∝ DealSize and |X| ∝ AcqMarketCap (p. 48). If value creation from a small acquisition can be large relative to the deal price — a platform technology, a patent, an acquihire that reprices the acquirer's whole product line — the assumption fails and so does the inference. The paper argues for the assumption but never tests it.
- The plausibility bound |NPV / DealSize| ≤ 1 (p. 44) is likewise assumed. The Microsoft/CyberX example ("a staggering 200× multiple") is rhetorically effective but is an assertion about what is credible, not a measurement.
- Goodwill impairment is a managerial-discretion variable. They concede the point and mitigate it (dummy rather than amount, ≥5%-of-assets screen, focus on extreme write-offs) but cannot eliminate it.
- The characteristics model wins a *prediction* contest, not a causal one. Its 7.9–10.7% five-year return spreads sit uncomfortably close to a documented anomaly: predicting long-run returns from firm size, Tobin's Q, past returns and payment form is what asset-pricing characteristics do anyway. The paper does not separate "the characteristics predict deal quality" from "the characteristics predict returns for reasons unrelated to the deal".
- Impairment tests are run at the reporting-unit level, so one successful target can mask a failed sibling. They address this by re-running on relatively large deals (p. 24 n.26) but the measurement error is one-directional.
- Almost everything is a null result. The paper's force depends on the reader accepting that power is adequate; no formal minimum-detectable-effect calculation is reported.

## 6. What they do NOT do (scope boundary)

**Object.** The object is **acquirer announcement CAR as a proxy for the acquirer's deal NPV** — total value creation, not its division. The paper says so explicitly when it turns to combined returns: *"We now assess whether the combined returns of the target and acquirer, which reflect total expected synergy gains (as opposed to the division of synergy gains), can predict outcomes."* (p. 21). The **takeover premium** — the offer price over the pre-bid price, i.e. precisely the division of surplus — is **never studied and never mentioned**. A text search of the full WP returns no occurrence of "premium" or "premia" except one accounting definition of goodwill ("the premium paid over the identifiable assets in nominal terms", IA p. 5). Target-side CAR appears only inside the combined-CAR construction for the 15–18% public-target subsample (p. 21).

**Margin.** **None.** There is no disclosure rule anywhere in this paper. Text search returns zero hits for "13D", "Schedule 13D", "blockholder", "activism/activist" (the only "Activision" hit is the Microsoft deal example), and zero hits for "liquidity" outside a reference title (Officer 2007). Neither the threshold margin nor the window margin is touched. **(verifier: all confirmed by grep over the page-marked extract — 13D 0 hits, blockholder 0 hits, activis* 1 hit = Activision, liquidit* 1 hit = Officer 2007 reference title, premi* 1 hit = the goodwill definition at IA p. 5, "five business days" 0 hits. The word "disclosure" occurs twice (pp. 11, 72), both about how comprehensively goodwill was disclosed before SFAS 142 — accounting disclosure, not a securities-filing rule.)**

**Identification.** Measurement validity by correlation and out-of-sample prediction, plus a variance decomposition under an assumed proportionality. **No causal design at all** — no DiD, no instrument, no structural estimation, no event-study identification claim beyond the CAR construction itself. They do not claim one.

**Stated future work / limits.** They explicitly decline to answer *why*: *"Though we do not claim to definitively answer this question, we argue that CAR is likely dominated by non-NPV information"* (p. 54), and close with *"More research is warranted on this issue"* (p. 55). They also concede their own ex-post proxies "may not fully capture the value generated by the acquisitions" (p. 29).

## 7. Implications for our position

**What this paper occupies:** object = acquirer (and combined) announcement CAR as a proxy for deal NPV; margin = none; identification = measurement validity, no causal design. It is not a competitor. It is a **measurement constraint** and a **referee weapon** — including one that can be pointed at us.

**7.1 The direct hit: any empirical leg of ours that uses announcement CARs as a proxy for a control outcome is now presumptively dead on arrival.**
Our control outcomes are bidder entry, takeover premium, and campaign success. If any of the three is operationalised as an announcement CAR — a 13D-filing CAR, an acquirer CAR, a combined CAR — a referee holding this paper can reject the design in one line: announcement returns do not correlate with realised outcomes, do not correlate with the predictable part of realised outcomes (R7), fail in every subsample anyone has looked in (R10, R11), and are driven 6–13× more by standalone-firm information than by the transaction (R17). Note especially that "we control for acquirer characteristics" is *pre-refuted*: they show formally that controlling for observables Zi cannot purge X, because X is unobservable and correlated with NPV, so α in `$CAR = α + βZ + ε` is not average NPV (p. 53).

**Concretely, for our design choices:**
- **Do not** use an acquirer or combined announcement CAR as the dependent variable standing for "the deal was good".
- **Do not** use the 13D-announcement CAR as a proxy for expected campaign success or expected control-outcome improvement. The paper's mechanism — the announcement reveals the *trigger*, and the trigger is about the standalone firm — transfers directly and arguably with more force to a 13D: a blockholder revealing itself tells the market about the blockholder, the target's standalone prospects, and the probability of a bid, all at once. Our own model says the flag is a partition of *states*, not a clean read on the control outcome; this paper is the empirical counterpart of that point and we should cite it that way.
- If a 13D-announcement return is used at all, it must be framed as **the market's revision of beliefs about the flagged state**, which is what our partition language already means, and never as an estimate of the value the campaign will create.

**7.2 The escape route: the takeover premium is a different object, and the paper says so.**
The premium — offer price over pre-bid price, our **premium wedge** m₁ − m₀ — is a *price*, not a return, and it is the *division* of surplus, not its total. The paper's scope sentence on p. 21 draws exactly this line, and its critique is aimed squarely at the total-synergy side of it. This is real whitespace for us and worth stating explicitly in draft_v3: our object is the transfer to target shareholders, which is contracted, observable in the deal terms, and does not require the market to have correctly valued anything. The premium's weaknesses are different (run-up contamination of the pre-bid reference price, toehold effects, deal-terms endogeneity) and must be defended on their own terms — but they are not *this* paper's weaknesses.
Caveat: the escape is partial. If we ever argue "a higher premium means more value was created", we are back inside their critique, because that argument needs the total. Keep the premium as a *transfer* claim.

**7.3 The template: what they say to do instead, and what it costs us.**
Their prescription is (p. 55) to use "a vector of publicly available characteristics" and, implicitly, realised ex-post outcomes. For our December package that means the credible empirical leg is a **realised** control outcome, not an expectational one:
- deal completion vs. withdrawal (they use it, it is cheap, it is in SDC, and it is the one outcome CAR weakly tracks);
- realised premium at the agreed offer price;
- campaign success as a realised event (board seat obtained, strategic action taken, target sold);
- and, if a firm-level value measure is ever wanted, **transaction-level goodwill impairment within five years** — their hand-collected measure is the template, and its construction recipe (Compustat firm-level impairment ≥5% of assets → read Notes to Consolidated Financial Statements in the acquisition and impairment years → attribute to a named deal) is reproducible from files in hand.
Deliverability warning: their impairment sample took manual reading of 10-K notes for thousands of deals and still starts only in 2003. That is not a December-package task. Completion/withdrawal and realised premium are.
**(added by verifier) Two numbers that constrain the completion-outcome leg before we commit to it.** Their 94.4% headline completion rate is private-target-weighted: **public-target deals complete only 82% of the time, private-target deals 97%** (p. 13 n. 16). So a completion outcome has usable variation only in the public-target subsample — which is also the subsample where a takeover premium exists, so the two candidate outcomes share a sample and a power problem. And of the deals that *do* fail, Jacobsen (2014) attributes only **13% to target shareholders blocking or voting the deal down**, against 14% to regulators and courts (p. 13 n. 15). Any story in which a blockholder's presence or flag changes completion is fishing in roughly one-eighth of the withdrawal margin. Put this into the MDE calculation, not the motivation.

**7.4 Two further constraints on any design we write.**
- Their benchmark result cuts both ways: **characteristics known at announcement predict outcomes with 7.9–10.7% five-year return spreads**. Any specification of ours in which liquidity or the disclosure rule moves a control outcome must control for the same standard vector (log market cap, leverage, FCF/assets, Tobin's Q, prior returns, relative size, payment form, target public status, diversifying, competed, hostile) or a referee will say the effect is that vector in disguise. This is now a checklist item.
- **(added by verifier) Merger-arbitrage price pressure is the one liquidity channel the paper concedes, and it points at our subsample.** At p. 1 and p. 22 the authors list "price pressure from merger arbitrageurs (e.g., public targets)" among the candidate explanations for CAR's failure, citing Mitchell, Pulvino & Stafford (2004). If our design touches announcement returns in public-target deals at all, this is a mechanical, liquidity-driven contaminant that has nothing to do with our κ, and a referee can use it against us in exactly the way this paper uses it. It is a second reason (beyond R7) to keep our outcomes realised rather than expectational.
- **(added by verifier) The run-up template.** Betton et al. (2014) report pre-announcement run-ups averaging **7%** (p. 32), and this paper's own anticipation design is a tercile sort on **CAR[−41, −2]** with the main test re-run on the middle tercile (p. 33, IA Table B8). That is a ready-made, cheap way to isolate "least anticipated" events, and it is directly transplantable to a 13D-filing sample where the pre-flag accumulation window is the object.
- Their **Feb-2024-style** identification worry appears in a different guise: they show that anticipated deals are the norm, not the exception (28,266 of ~40,000 announcements are by repeat acquirers, and their less-stringent "potential anticipation" flag captures 10–21% of samples). For our Feb-2024 acceleration anchor this reinforces the anticipation entry on the referee checklist — a shortened filing window changes *when* the market learns, and pre-announcement leakage is exactly the channel that makes the "before the flag" trading window empirically slippery.

**7.5 One-line index entry.** *JF 2026 (read as NBER WP 27976 rev. May 2025) · object: acquirer/combined announcement CAR as a proxy for deal NPV · margin: none · identification: measurement validity, no causal design · so-what: it disqualifies announcement CARs as a control-outcome proxy for us, and its p. 21 "total vs. division of synergy gains" line is the sentence that keeps the takeover premium a legitimate, separate object.*

## 8. Quotes we may lean on (verbatim, page-cited)

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "Over the last five decades, CAR has been used to measure value creation in over 92% of the articles in top finance journals studying value creation in acquisitions." | p. 1 | Establishing that CAR is the field default we are declining to use |
| Q2 | "We find no meaningful correlation between these measures and announcement returns." | p. 3 | The headline null |
| Q3 | "We now assess whether the combined returns of the target and acquirer, which reflect total expected synergy gains (as opposed to the division of synergy gains), can predict outcomes." | p. 21 | **The scope sentence** — the premium is the division, which they do not study |
| Q4 | "We conclude that the lack of relation between outcomes and CAR is systematic and not driven by a particular time period (e.g., the financial crisis), industry, or combination of deal and acquirer characteristics." | p. 25 | Pre-empting "but it works in my subsample" |
| Q5 | "acquirer CAR in the later sample is either not correlated with the predictable part of acquisition outcomes (Columns (7)–(8)) or has the wrong sign (Columns (1)–(6))" | p. 26 | The sharpest result: CAR misses even ex-ante public information |
| Q6 | "Consistent with our earlier findings—which show that CAR does not correlate with ex-post outcomes—we find that outcomes predicted by CAR also do not correlate with long-term returns." | p. 31 | Long-horizon validation of the null |
| Q7 | "The net effect of listening to CAR is −5% to −17%, while the net effect of listening to characteristics is 21% to 26%." | p. 35 | The economic cost of treating CAR as a signal |
| Q8 | "The transactions ranked as having the best performance according to CAR (2.8%) have the following acquisition characteristics: not limited to cash, private target, small acquirer, and large relative size. However, their ex-post outcomes are the worst: only 75% of them do not impair (versus a sample mean of 85.2%), and their average short- and long-term abnormal ROA is −0.8% (versus a sample mean of −0.2%)." | p. 41 | CAR-based inferences about deal *types* are inverted |
| Q9 | "Figure 7 shows that an astounding 91% of deals (128 out of the 140) are outside the plausible range." | p. 44 | The implausibility argument (Cisco) |
| Q10 | "At its best (around a relative size of 1, i.e., “a merger of equals”), deal-related information explains about half of the information contained in $CAR." | p. 52 | Upper bound on how much of CAR is ever about the deal |
| Q11 | "The information contained in CAR is influenced by acquirer-related information 6× to 13× more than deal-related information." | p. 55 | The headline decomposition |
| Q12 | "Researchers should avoid using CAR to measure deal quality." | p. 55 | The prescription, stated at its bluntest |
| Q13 | "Researchers, instead, should consider using a vector of publicly available characteristics that do a better job of predicting acquisition outcomes (e.g., Ellahie et al., 2025)." | p. 55 | What to do instead — the control-vector requirement for our own specs |
| Q14 | "The stock returns of the bidder at the time of the announcement of the bid may tell us more about how the market is reassessing the bidder’s business than it does about the value of the acquisition." | p. 43 (the authors quoting Grinblatt and Titman, 2002, p. 708) | The mechanism in one sentence; transfers to a 13D announcement |

*Note on Q14: this is the paper quoting a textbook, reproduced on p. 43 of the WP as a display quotation. Cite it as quoted-in.*

## 9. Verification log

**Verifier:** adversarial second read, 2026-08-19. Checked against `lit/bendavid-etal-jf2026-nber.pdf` directly (`pdftotext -f N -l N -layout`, printed page = PDF − 2) and against the page-marked extract `research/txt_extracts/bendavid_jf2026_pages.txt`. Every quote was matched as a distinctive fragment inside the page it is cited to; every number was read off the printed table.

**Counts: 34 OK · 1 WRONG · 0 MISCITED · 2 UNCHECKED.**

### Header / version
| Item | Verdict | Checked against |
|---|---|---|
| Three authors — Ben-David, Bhattacharya, Jacobsen; **no Huang** | **OK** | PDF p. 1 title block |
| "October 2020, Revised **May 2025**" | **OK** | PDF p. 1 (`pdfinfo` CreationDate 13 May 2025 corroborates) |
| NBER WP **27976** | **OK** | PDF p. 1 |
| "99 PDF pages" | **WRONG → fixed to 98** | `pdfinfo` reports **Pages: 98**. Structure: PDF 1–2 front matter, printed main text 1–62 = PDF 3–64, PDF 65 = unnumbered "Internet Appendix" title page, IA pp. 1–33 = PDF 66–98. The "99" is the artefact of splitting the extract on 98 form feeds. |
| Page rule printed = PDF − 2 | **OK** | spot-checked at four points (PDF 10→8, 16→14, 53→51, 64→62) |
| JF 81(3), 1265–1320 (2026) | ~~**UNCHECKED**~~ **CLOSED 2026-08-19 — masthead read, see §9b.** Volume, issue, page range and year all confirmed; a **fourth author (Ruidi Huang)** appears on the published version. |

### Results (§3)
| Item | Verdict | Checked against |
|---|---|---|
| Sample **47,543** deals (42,354 / 2,227 / 2,962), 1980–2018 | OK | p. 8 and p. 65 filter table |
| Working Ns **6,128 / 28,710 / 22,577 / 39,585**, BHAR 27,355 | OK | p. 14 Table I Panel A; p. 66 IA filter panels |
| Impairment funnel 8,367 → 6,767 → 6,437 → 6,128; 14.8% impair; 83% / 57% / 11% | OK | p. 11 verbatim |
| Mean CAR[−1,1] 0.9%, CAR[−5,5] 0.8%, DealCAR −1.1% | OK | p. 14 Table I Panel A (0.009 / 0.008 / −0.011) |
| R1 Table II coefficients −0.020 (0.105), 0.004 (0.012), −0.015 (0.014); −0.008 (0.081), −0.001 (0.006), −0.004 (0.007); adj R² 0.000 | OK | p. 18 Table II Panels A–C cols (1)–(2), every figure matches |
| R2 DealCAR 0.089** (0.040), 0.009** (0.003); 0.09% vs 14.80% base; "less than a one-basis-point increase" | OK | p. 18 Table II col (3); p. 19 text verbatim |
| R3 completion 0.048* (0.023) raw, 0.050** (0.019) with characteristics; 0.05% vs **94.4%** | OK | p. 18 Table II Panel D; p. 20 text |
| R4 adj R² 7.8% and 10.9% with or without CAR; "the explanatory power comes entirely from the controls and not from CAR" | OK | p. 18 Table II cols (5)/(7); p. 19 text verbatim |
| R5 outcome-outcome correlations 0.13–0.67; with CAR[−1,1]/[−5,5] −0.01 to 0.02; with DealCAR 0.01–0.05 | OK | p. 14 Table I Panel B and p. 15 text |
| R6 out-of-sample 0.708***/1.338***/1.188***/0.995*** vs 26.039 (30.177), −0.855 (1.031), 6.573 (4.985), 1.090** (0.404) | OK | p. 26 Table III Panel A, exact |
| **R7 −0.104*** (0.005), −0.014*** (0.001), −0.010*** (0.003), completion −0.008 (0.017)** | **OK** | p. 26 Table III Panel B, exact. Decision-critical; reproduced character for character. |
| R8 Table IV spreads 9.2 / 10.7 / 9.4 / **7.9**% (p = 0.005, 0.000, 0.000, 0.000) vs **0.1** / 2.8 / −0.8 / 2.8% (p = 0.986, 0.158, 0.726, 0.089) | OK | p. 30 Table IV, exact |
| §9(d) query: intro summarises the CAR spread as "**0.8% to 2.8%**" while Table IV col (7) prints **−0.8%** and col (5) prints **0.1%** | **Confirmed as the card describes** | p. 5 intro vs p. 30 table. The intro range is absolute-valued and omits the 0.1%. The card's own §3 R8 prints the signed table values, which is the right way round. |
| R9 "listening to CAR" −5% mean / −17% median; characteristics +21% / +26% | OK | p. 36 Table V Panel C — the paper's prose calls it a range "−5% to −17%", but the table's final row is explicitly Mean (−5%) and Median (−17%), so the card's mean/median split is right |
| R10 22,298 regressions; 5% (1,091), 3% (735), **0.26% (59/22,298)** in both | OK | p. 24 verbatim |
| R11 "significant at the 5% level for only 19 regressions"; "in no subsample does CAR achieve statistical significance for three or more outcome variables" | OK | p. 24. (The "116 = 4 × 29" arithmetic is the reader's, not the paper's; the paper prints only the 19 and the 5-subsample counts.) |
| R12 Table VI top-CAR cluster 2.8%, non-impairment 0.753 vs 85.2% mean, abROA −0.008 vs −0.002 mean | OK | p. 41 Table VI row 1 and text |
| R13 combined CAR, public targets **15%–18%** of samples, insignificant for the three value outcomes, significant-but-weak for completion | OK | p. 21 and IA Table B4 description |
| R14 1,047 explicit / 3,681 potential / 28,266 repeat-acquirer; CAR[−41,1]; low-cancellation tercile | OK | pp. 32–35 verbatim, incl. footnote shares 3–8%, 10–21%, 48–72% |
| R15 91% of Cisco's deals (128/140); 26.83% / 26.90% of all deals | OK | p. 44 and Figs. 7–8 on p. 46 |
| R16 53% / 55%; 2,141 withdrawn deals | OK | p. 47 text; p. 46 n. 41 |
| R17 0.757*** (0.015) vs 0.106*** (0.010); "about 6.5×"; bin ~8×; acquirer-bin 13×; adj R² 0.684–0.981 | OK | p. 51 Table VII and p. 52 text, all four figures verbatim |
| R18 "never reaches the critical point of dominating"; "about half" at relative size ≈ 1 | OK | p. 52 |
| R19 the |NPV| ∝ DealSize / |X| ∝ AcqMarketCap proportionalities are assumed | OK, and the ASSERTED label is right | pp. 43, 48; the paper argues them in prose and never tests them |
| R20 prescription | OK | p. 55 |
| §7.1's "controlling for observables cannot purge X" (p. 53) | OK | p. 53, eqs. (5)–(7) and the paragraph following — the card's paraphrase is faithful |

### Quotes (§8)
Q1 (p. 1) **OK** · Q2 (p. 3) **OK** · **Q3 (p. 21) OK — verbatim, the load-bearing scope sentence, matched character for character** · Q4 (p. 25) **OK** · Q5 (p. 26) **OK** · Q6 (p. 31) **OK** · Q7 (p. 35) **OK — note the card cites p. 35 in §8 and the same result to p. 36 Table V in §3 R9; both are right, prose on 35, table on 36** · Q8 (p. 41) **OK** · Q9 (p. 44) **OK** · Q10 (p. 52) **OK** · Q11 (p. 55) **OK** (a near-identical sentence with "$CAR" also appears on p. 52; the card quotes the p. 55 wording, correctly) · Q12 (p. 55) **OK** · Q13 (p. 55) **OK** · Q14 (p. 43) **OK** — it is a display quotation of Grinblatt & Titman (2002, p. 708); the same sentence also appears in the intro at p. 2 inside quotation marks. The card's "cite as quoted-in" note is correct.

### Scope claims (§6) — all greps run over the full 98-page extract
"13D" **0 hits** · "blockholder" **0 hits** · "activis*" **1 hit**, Activision Blizzard (p. 44) · "liquidit*" **1 hit**, the Officer (2007) reference title (p. 61) · "premi*" **1 hit**, the goodwill definition at IA p. 5 · "five business days" **0 hits** · "informed trad*" **0 hits**. "disclosure" **2 hits** (pp. 11, 72), both about how comprehensively goodwill was disclosed pre-SFAS 142 — accounting disclosure, not a securities filing rule. **§6 stands as written.**

### Omissions found and added
1. **Completion rates split 82% public / 97% private target** (p. 13 n. 16) — added to §4 and to §7.3. Material: it means the completion outcome the card recommends has usable variation only in the public-target subsample, the same subsample where a premium exists, so the two candidate outcomes share one sample and one power problem.
2. **Jacobsen (2014): only 13% of withdrawals are target shareholders blocking or voting the deal down** (14% regulatory/judicial), p. 13 n. 15 — added to §4 and §7.3. Material: it bounds the shareholder-driven margin of any completion design to about one withdrawal in eight.
3. **Merger-arbitrage price pressure** (Mitchell, Pulvino & Stafford, 2004) named at pp. 1 and 22 as a candidate explanation, specifically for public targets — added to §7.4. Material: it is the only liquidity/microstructure channel in the paper, it contaminates announcement returns mechanically, and it is aimed at exactly our subsample.
4. **Pre-announcement run-up averages 7%** (Betton et al. 2014, p. 32) and the paper's **CAR[−41, −2] run-up tercile design** (p. 33, IA Table B8) — added to §4 and §7.4. Material: a transplantable, cheap "least anticipated" filter for a 13D sample, and a number for how much is already in the price before the flag.
5. **Mean time to close 74 days** (p. 19) — added to §4; it is what makes DealCAR a 10-week window and is the reason DealCAR's weak significance is not evidence for CAR.

### Verdict
**The card is accurate.** Every decision-critical number reproduces from the printed tables, and the two sentences the position leans on — Q3 (p. 21, "as opposed to the division of synergy gains") and R7 (−0.104***) — are verbatim and exact. One factual error, the PDF page count, corrected. Two items remain unchecked and both are named rather than triaged: the published JF 81(3) masthead (the card already requires this before citation), and the Internet Appendix table contents beyond the headers the reader read, which are not needed for anything the card asserts.


## 9b. Published-version supplement-reader log — 2026-08-19

**Source read:** `research/txt_extracts/ben_david_et_al_2026_jf.pdf` — the published *Journal of Finance* article, 56 pages,
printed **1265–1320**, fetched via UCL's Wiley access (`research/txt_extracts/FETCH_LOG_C.md`, row `ben_david_et_al_2026_jf`).
**Page mapping: printed = PDF page + 1264** (anchored on PDF p. 1 folio 1265 and PDF p. 14 folio 1278, and consistent to PDF
p. 56 = 1320). **Reader:** opus. Extraction note: the Wiley download watermark (`15406261, 2026, 3, Downloaded from …`) is
injected into every page and was stripped before matching; hyphenated line breaks were rejoined.

### Masthead — the UNCHECKED item, now closed

| Field | Published value |
|---|---|
| Journal | *The Journal of Finance* — running head "VOL. LXXXI, NO. 3 • JUNE 2026" |
| Volume / issue / year | **81 (3), June 2026** |
| Pages | **1265–1320** (56 printed pages) |
| DOI | **10.1111/jofi.70038** |
| Authors, in printed order | **ITZHAK BEN-DAVID, UTPAL BHATTACHARYA, RUIDI HUANG, and STACEY JACOBSEN** |
| Affiliations | Ohio State + NBER · Hong Kong University of Science and Technology · Southern Methodist University · Southern Methodist University |
| Dates | Initial submission **7 April 2024**; accepted **14 February 2025** |
| Editors | Antoinette Schoar, Urban Jermann, Leonid Kogan, Jonathan Lewellen, Thomas Philippon |
| Licence | Open access, CC BY-NC-ND |
| Supporting Information | "Appendix S1: Internet Appendix. Replication Code." (printed p. 1320) |

**The tracker's "81(3), 1265–1320 (2026)" is exactly right. The card's three-author list was a property of the WP, not an error
in the ticket — Ruidi Huang (SMU) is the fourth author on the published version.** Any bibliography entry must be four authors.

### Headline numbers — all four survive into print, unchanged

| Card claim | Published verdict | JF page |
|---|---|---|
| **47,543 deals** (42,354 completed / 2,227 withdrawn / 2,962 neither) | **IDENTICAL**, same three-way split, same eight filters | **p. 1272**; repeated p. 1306 |
| **−0.104\*\*\* (0.005)**, −0.014\*\*\* (0.001), −0.010\*\*\* (0.003), completion −0.008 (0.017) | **IDENTICAL**, character for character; CAR[−5,5] row likewise −0.078\*\*\*/−0.009\*\*\*/−0.008\*\*\*/−0.011; observations 2,862 / 14,358 / 10,713 / 18,014 | **Table III Panel B, p. 1289** |
| **p. 21 "division of synergy gains" quote (Q3)** | **IDENTICAL, verbatim** — still the scope sentence, still about the public-target subsample at "15% to 18%" | **p. 1284** |
| **7.9–10.7% vs 0.1–2.8% spreads** (Table IV: 9.2 / 10.7 / 9.4 / 7.9 with p = 0.005/0.000/0.000/0.000, against 0.1 / 2.8 / −0.8 / 2.8 with p = 0.986/0.158/0.726/0.089) | **IDENTICAL**, every cell and every p-value | **Table IV, p. 1293** |

**Nothing changed numerically between the WP and the JF version in anything this card relies on.** Also re-confirmed in print:
22,298 brute-force regressions with 5% (1,091), 3% (735) and **0.26% (59/22,298)** (p. 1287); the **−2.8%** market reaction to
impairment news (p. 1274); outcome-measure correlations "range between 0.13 and 0.67", printed as 0.133\*\*\*, 0.127\*\*\*, 0.671\*\*\*
in Table I Panel B (pp. 1277–1278); the intro's "7.9% to 10.7%" vs "0.8% to 2.8%" summary (p. 1269); and the Table VI top-CAR
cluster at 2.8% CAR with 75% non-impairment vs an 85.2% mean (p. 1303).

### Published-version page map (WP page → JF page)

| # | Passage | WP p. | **JF p.** |
|---|---|---|---|
| 1 | Intro: the "7.9% to 10.7%" vs "0.8% to 2.8%" spread summary | 5 | **1269** |
| 2 | Sample construction, 47,543 deals and the eight filters | 8 | **1272** |
| 3 | Goodwill-impairment validation, incl. the −2.8% market reaction | 10 | **1274** |
| 4 | Outcome-measure correlations 0.13–0.67 (Table I Panel B) | 15 | **1277–1279** |
| 5 | **Q3, "as opposed to the division of synergy gains"** — the scope sentence | 21 | **1284** |
| 6 | Brute-force data mining, 22,298 regressions / 0.26% | 24 | **1287** |
| 7 | **Table III Panel B, the −0.104\*\*\* result** | 26 | **1289** |
| 8 | **Table IV, the 60-month DGTW-BHAR decile spreads** | 30 | **1293** |
| 9 | **Table VI + Q8, the inverted 16-cluster grid** | 41 | **1303** |
| 10 | Grinblatt–Titman (2002, p. 708) display quotation (Q14) | 43 | **1305** (and, as an in-line quotation, **1267**) |
| 11 | Q10 "a merger of equals" / half of $CAR; Q11 "6× to 13×" (Table VII) | 52, 55 | **1314** |
| 12 | Conclusion: Q12 "avoid using CAR", Q13 characteristics vector | 55 | **1316** |
| 13 | Q9 Cisco, "91% of deals (128 out of the 140)" | 44 | **1306** |
| 14 | Q7 "net effect of listening to CAR is −5% to −17%" | 35 | **1298** |
| 15 | Q4 "systematic and not driven by a particular time period" | 25 | **1287** |
| 16 | Q5 "or has the wrong sign" | 26 | **1288** |
| 17 | Q6 "outcomes predicted by CAR also do not correlate with long-term returns" | 31 | **1294** |
| 18 | Q1 "92% of articles in top finance journals"; Q2 "no meaningful correlation" | 1, 3 | **1266**, **1267** |

### WARNING — eight of the fourteen §8 quotes were re-edited and are NO LONGER VERBATIM (added by supplement reader)

Each quote in §8 was exact-string-tested against the published text (whitespace-normalised, hyphenation rejoined). **Six pass
unchanged: Q2, Q3, Q4, Q7, Q9, Q14.** The other eight fail. The differences are copy-editorial, not substantive — no number and
no claim moved — but **none of these eight may be pasted into a draft as a quotation from the published article.** Published
wording, to use instead:

| # | WP wording (as in §8) | **Published wording, JF p.** |
|---|---|---|
| Q1 | "…in over 92% of the articles in top finance journals…" | "…in **more than** 92% of articles in top finance journals studying value creation in acquisitions." — **p. 1266** |
| Q5 | "acquirer CAR in the later sample is **either** not correlated … (Columns (7)–(8)) or has the wrong sign (Columns (1)–(6))" | "the acquirer CAR in the later sample is not correlated with the predictable part of acquisition outcomes (**columns (7) and (8)**) or has the wrong sign (**columns (1) to (6)**)." — **p. 1288** |
| Q6 | "…CAR does not correlate with **ex-post** outcomes…" | "…CAR does not correlate with **ex post** outcomes…" (hyphen dropped throughout the published article) — **p. 1294** |
| Q8 | "only 75% **of them** do not impair (**versus** a sample mean of 85.2%) … (**versus** a sample mean of −0.2%)" | "only 75% do not impair (**vs.** a sample mean of 85.2%), and their average short- and long-term abnormal ROA is −0.8% (**vs.** a sample mean of −0.2%)." — **p. 1303** |
| Q10 | "(around a relative size of **1, i.e.,** 'a merger of equals')" | "(around a relative size of **one, that is,** 'a merger of equals'), deal-related information explains about half of the information contained in $CAR." — **p. 1314** |
| Q11 | "The information contained in **CAR** is influenced by…" | "the information contained in **$CAR** is influenced by acquirer-related information 6× to 13× more than deal-related information." — **p. 1314** (a second, differently-worded restatement sits at p. 1316) |
| Q12 | "Researchers should avoid using CAR to measure deal quality." *(standalone sentence)* | Now a subordinate clause: "In sum, **the results suggest that** researchers should avoid using CAR to measure deal quality." — **p. 1316** |
| Q13 | "**Researchers, instead, should** consider using … (e.g., **Ellahie et al., 2025**)." | "**Researchers should instead** consider using a vector of publicly available characteristics that do a better job of predicting acquisition outcomes (e.g., **Ellahie, Hshieh, and Zhang, 2025**)." — **p. 1316** |

**Q14 note updated:** in the WP the Grinblatt–Titman line appears once, as a display quotation on p. 43. In the published version
it appears **twice** — in-line in the introduction (p. 1267) and as a display quotation with the page cite printed as "(p. 708)"
at **p. 1305**. Cite the p. 1305 occurrence, which carries the source pagination.

### Still open

- **The JF Internet Appendix could not be fetched.** Wiley's supplement endpoint
  (`downloadSupplement?doi=10.1111%2Fjofi.70038&file=jofi70038-sup-0001-InternetAppendix.pdf`) returns a Cloudflare
  "Just a moment…" challenge; the replication-code ZIP sits behind the same wall. It is on the wall list at the foot of
  `FETCH_LOG_C.md`. **Practical consequence: none for this card.** §9's second UNCHECKED item — Internet Appendix table
  contents beyond the headers — remains open exactly as before, and the verifier's judgement that "they are not needed for
  anything the card asserts" still holds. Note the published IA renumbers relative to the WP's: the JF text points to
  **Table IA.I** (sample construction, p. 1272), **Table IA.VIII** (combined CAR, p. 1284) and **Table IA.X** (the 22,298
  regressions, p. 1287), so any future fetch should look for those labels, not the WP's B-series.
- The WP's own Internet Appendix (33 pages, inside `lit/bendavid-etal-jf2026-nber.pdf`) is still the only appendix we hold,
  and its table numbering (IA Table B6 etc., cited in §3 R10) does **not** match the published one.

**Counts after this pass: UNCHECKED 2 → 1.** No result was refuted; four headline numbers reproduce exactly; one author was
added to the byline; eight quotes need re-transcription before use.
