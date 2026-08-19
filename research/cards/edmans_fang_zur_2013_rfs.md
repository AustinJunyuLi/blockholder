# Edmans, Fang & Zur (2013) — "The Effect of Liquidity on Governance"

**Venue / status:** *Review of Financial Studies* 26(6), 1443–1482 (2013), doi:10.1093/rfs/hht012, Advance Access 10 April 2013 — **PRIMARY for all page cites**. Working-paper version also read: NBER Working Paper No. 17567, November 2011 (46 numbered manuscript pages, 48 PDF pages). §§1–8 below were written from the WP; §9b records the re-basing onto the published article. **Cite the RFS pages (1443–1482) in draft_v3; WP pages are kept only as a provenance trail.**
**Full text from:** published — `research/txt_extracts/edmans_fang_zur_2013_rfs_published.pdf` (40 PDF pp.) / `.txt`; WP — `lit/edmans-fang-zur-liquidity-2013.pdf` (48 pp.) / `research/txt_extracts/efz2013_layout.txt` · **Reader:** opus, opus (published-version supplement) · **Read:** both full texts end to end (published: body, Figure 1, Tables 1–8, Appendix A.1–A.2, references)
**Page numbering used below:** §§1–8 quote the **WP's** printed manuscript page (printed p. N = PDF p. N+2). §9b gives the **published** RFS page for every one of them. Published RFS page = published PDF page + 1442 (PDF p. 1 = RFS p. 1443).
**Online Appendix:** the published version has one (Tables OA1–OA17), hosted on the RFS website; **not in hand** — see the open items at the end of §9b.
**Type:** empirical **Role for us:** antecedent (the canonical liquidity → exit-vs-voice measurement paper) and measurement template

## 1. Question

Does stock liquidity strengthen or weaken blockholder governance, and — crucially — does it change *which* governance channel a blockholder uses? The theory literature is split: the "Wall Street Walk" view (Coffee 1991; Bhide 1993; Maug 2002) says liquidity lets a blockholder sell instead of fixing the firm, so liquidity weakens governance; Kyle–Vila (1991), Maug (1998), Kahn–Winton (1998) and Faure-Grimaud–Gromb (2004) say liquidity *helps* voice (cheap accumulation, informative prices); Admati–Pfleiderer (2009), Edmans (2009) and Edmans–Manso (2011) say the act of selling is itself governance ("exit"), and liquidity strengthens it. EFZ ask which pattern the data show, using the *filing choice* (13D vs 13G) as a revealed measure of governance **intent** rather than waiting for realised exit or realised voice.

## 2. Model / data and method

**Design:** cross-sectional/panel probit of governance events on *lagged* liquidity, plus decimalization as a shock. Not a structural model; no formal 2SLS is reported (see §5).

**Sample.**
- Universe of hedge-fund block acquisitions, **1 January 1995 – 31 December 2010** (printed p. 13 / PDF p. 15).
- Activist hedge funds identified by an exhaustive Factiva keyword search following Brav et al. (2008) → **223 funds**; EDGAR then supplies each fund's *initial* 13D or 13G on a target; filing date and target PERMNO hand-collected (printed p. 14 / PDF p. 16).
- Raw hand-collected dataset: **709 initial Schedule 13Ds and 1,112 initial Schedule 13Gs, filed by 101 hedge funds** (printed p. 14). Of the 101 funds, **69 file both types**, i.e. engage in both passive and active monitoring (printed p. 3).
- After merging with Compustat/CRSP and controls: **88,742 firm-year observations**, of which **1,135** have at least one initial 13D or 13G by a hedge fund; those 1,135 split **490 13D / 645 13G** (printed pp. 18–19; Table 1 Panel A, printed p. 36). The original filing count was 1,821, so the merge loses ~38% of filings.
- Unconditional block-acquisition probability **1.3%**; conditional probability that a block filing is a 13D, **43.2%**.
- CAR sample for 13G announcements: **N = 630**.
- WPS (managerial incentive) sample: **N = 24,645** firm-years (S&P 1500 ∩ Execucomp); the 13D-vs-13G × WPS sample collapses to **N = 322**.

**Liquidity measures (exactly as defined).** Both are *daily-data* proxies, sign-flipped so higher = more liquid, and both are measured over **firm i's fiscal year immediately preceding the filing date** (Appendix A, printed p. 30):
- `AMRATIO_{i,t}` = Amihud (2002) illiquidity ratio = mean over the fiscal year of |RET_{i,d}| / (dollar VOLUME_{i,d}). Then **`LIQAM_{i,t} = −1 × ln(1 + AMRATIO_{i,t})`**.
- `FHT_{i,t}` = Fong, Holden & Trzcinka (2011) percent-cost proxy, built from the fiscal-year standard deviation of daily returns and the fiscal-year proportion of zero-return days. Then **`LIQFHT_{i,t} = −1 × ln(1 + FHT_{i,t})`**.
- The two are highly correlated (Pearson 0.750, Spearman 0.788) and highly persistent (own-lag Pearson/Spearman 0.85–0.94), Table 1 Panels C–D, printed p. 37.
- **Note for us:** these are *illiquidity* measures inverted — exactly the empirical counterpart of our κ. They are **annual, firm-level, pre-filing** — not a trade-level or intraday object.

**Outcome objects (three distinct dependent variables).**
1. `BLOCK_{i,t+1}` = 1 if a hedge fund files an initial 13D **or** 13G (i.e. a ≥5% block appears), 0 otherwise. → *entry* margin.
2. `13Dvs13G_{i,t+1}` = 1 if 13D, 0 if 13G, **conditional on a block having been formed** (N = 1,135). → *channel choice* margin.
3. `13DFILING_{i,t+1}` = 1 if 13D, 0 if 13G **or no block at all** (N = 88,742). → *unconditional voice* margin.
4. `CAR(−1,+1)` = 3-day market-adjusted abnormal return around the **13G** filing date (Eventus).

**Controls:** MV, Q, SGR, ROA, LEV, DIVYIELD, RDTA, HINDEX, NANLYST, plus year and Fama-French-12 industry fixed effects; SEs heteroskedasticity-robust and clustered by firm. Continuous variables winsorised at 1%/99%.

**Identification.**
- *Primary defence:* the LHS is a dated **event** (a Section 13 filing in t+1) regressed on **lagged** (fiscal-year-t) liquidity, so reverse causality from governance to liquidity is argued away rather than instrumented away (printed p. 17).
- *The "decimalization instrument":* US markets moved to decimal pricing between **August 2000 and April 2001**, cutting the minimum tick from 1/16 dollar to one cent. `DECIMAL` is defined two different ways depending on the regression *(corrected by verifier, printed p. 18 / PDF p. 20)*: in the **block-acquisition** regressions it equals 1 if **fiscal year t ends** after 31 January 2001 (NYSE/AMEX) or 9 April 2001 (Nasdaq); in the **13D-vs-13G** regressions, where a filing date exists, it is defined "more finely" as 1 if the **filing** occurs after those dates. Year fixed effects for 2001 and 2002 are dropped to avoid collinearity, all other year FE retained. **Important:** in every reported table `DECIMAL` is entered as a *substitute regressor* for LIQAM/LIQFHT — this is a reduced form / pre-post comparison, not a two-stage least squares or IV-probit. The paper's own words are "decimalization can instrument for liquidity"; no first stage, no excluded-instrument F-statistic, and no 2SLS coefficient is reported anywhere in this version.
- *Two supports for the exclusion story:* (i) split by `LOWPRC` (below-median year-end price), where a tick-size cut should bite harder — the first stage in levels is shown descriptively: on decimalization LIQAM (LIQFHT) rises by **0.368 (0.024)** in LOWPRC=1 versus **0.077 (0.007)** in LOWPRC=0, both differences significant at 1% (printed p. 22); (ii) replace `DECIMAL` with the actual **change** in liquidity from fiscal year t−1 to t+1 around the firm's decimalization year, dropping all other years (Table 2 Panel C).

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where (page / prop / table) |
|---|---|---|---|
| R1 | Liquidity raises the probability a hedge fund acquires a ≥5% block: LIQAM 0.079\*\*\* (0.013) no controls, 0.171\*\*\* (0.021) with controls; marginal effects 0.0026\*\*\* / 0.0045\*\*\*. LIQFHT 3.975\*\*\* (0.747) / 3.902\*\*\* (1.064); mfx 0.1295\*\*\* / 0.1062\*\*\*. N = 88,742 | ESTIMATED | Table 2 Panel A, printed p. 38 (PDF p. 40) |
| R2 | Economic size of R1: a one-standard-deviation rise in LIQAM (LIQFHT) raises block-acquisition probability by **0.47 (0.20) percentage point**, against an unconditional 1.3% | ESTIMATED | printed p. 21 (PDF p. 23) |
| R3 | Same on the decimalization shock: DECIMAL 0.299\*\*\* (0.024) no controls, 0.544\*\*\* (0.064) with controls; mfx 0.0094\*\*\* / 0.0158\*\*\*. Reduced form, not 2SLS | ESTIMATED | Table 2 Panel A cols (5)–(6), printed p. 38 |
| R4 | **The 13D-vs-13G tilt.** Conditional on a block, liquidity *lowers* the probability the filing is a 13D: LIQAM −0.152\*\*\* (0.046) / −0.169\*\*\* (0.064), mfx −0.0598\*\*\* / −0.0662\*\*\*; LIQFHT −4.047\* (2.456) / −6.662\*\* (3.260), mfx −1.5907\* / −2.6138\*\*; DECIMAL −0.295\*\*\* (0.084) / −0.492\*\* (0.236), mfx −0.1164\*\*\* / −0.1936\*\*. N = 1,135 | ESTIMATED | Table 4 Panel A, printed p. 42 (PDF p. 44) |
| R5 | Economic size of R4: a one-SD rise in LIQAM (LIQFHT) cuts the probability of a 13D by **6.88 (4.97) percentage points**, against a 43.2% base rate | ESTIMATED | printed p. 24 (PDF p. 26) |
| R6 | **Entry effect beats channel effect.** The *unconditional* probability of a 13D still rises with liquidity: LIQAM 0.103\*\*\* (0.026), mfx 0.0013\*\*\*; LIQFHT 3.851\*\*\* (1.435), mfx 0.0493\*\*\*; DECIMAL 0.309\*\*\* (0.088), mfx 0.0041\*\*\*. N = 88,742 | ESTIMATED | Table 6, printed p. 45 (PDF p. 47) |
| R7 | Exit-channel test on entry: LIQUIDITY × WPS is positive — LIQAM×WPS 0.019\* (0.010); LIQFHT×WPS 0.049\*\* (0.021). N = 24,645 | ESTIMATED | Table 3, printed p. 41 (PDF p. 43) |
| R8 | Exit-channel test on channel choice: LIQUIDITY × HIGHWPS is negative — LIQAM×HIGHWPS −2.390\* (1.298); LIQFHT×HIGHWPS −38.281\* (22.928); the level terms (0.722, s.e. 0.927; 7.337, s.e. 11.494) are insignificantly *positive*. N = 322, significance only at 10% | ESTIMATED (weak) | Table 5, printed p. 44 (PDF p. 46) |
| R9 | 13G announcement effect: CAR(−1,+1) = **0.007\*\*\*** (0.002) pooled, N = 630. High-LIQAM half 0.010\*\*\* (0.003) vs low half 0.004 (0.004); high-LIQFHT 0.009\*\*\* (0.003) vs low 0.005 (0.004); significant only in the liquid half | ESTIMATED | Table 7 Panel A, printed p. 46 (PDF p. 48) |
| R10 | In OLS with size and market-to-book controls, HIGHLIQAM adds **0.015\*\*** (0.007) and HIGHLIQFHT **0.010\*** (0.006) to the 3-day 13G CAR. N = 630, adj. R² 0.014 / 0.010 | ESTIMATED | Table 7 Panel B, printed p. 46 |
| R11 | DECIMAL bites only in low-priced stocks. Block acquisition: 0.551\*\*\* (0.083) if LOWPRC=1 vs 0.360 (0.281) if LOWPRC=0, difference 0.191\*\*\* (p = 0.000). Filing choice: −1.213\*\*\* (0.351) vs −0.165 (0.329), difference −1.048\*\*\* (p = 0.002) | ESTIMATED | Table 2 Panel B (printed p. 39); Table 4 Panel B (printed p. 43) |
| R12 | Liquidity *change* around decimalization predicts block acquisition **in t+2** (dependent variable is `BLOCK`~t+2~, not `BLOCK`~t+1~ — *corrected by verifier*; Δ = fiscal year t−1 to t+1 around the firm's decimalization year, industry FE only, no year FE): ΔLIQAM 0.128\*\* (0.055), ΔLIQFHT 9.228\*\*\* (2.782), N = 4,576 | ESTIMATED | Table 2 Panel C, printed p. 40 (PDF p. 42) |
| R13 | Cost-of-exit calibration: on days when 0.9–1.1% of shares outstanding trade, third-AMRATIO-quartile firms move 0.9–1.1% while fourth-quartile (most illiquid) firms move 2.2–2.4%; by FHT, 1.2–1.4% vs 2.5–2.6% | ESTIMATED (descriptive) | printed pp. 19–20 (PDF pp. 21–22) |
| R14 | The overall reading — liquidity does not switch governance off, it re-routes it from voice to exit and raises both — is an *interpretation* stacked on R4+R7+R8+R9, not itself estimated | ASSERTED | printed p. 28 (PDF p. 30) |

**Direction of the headline result, stated precisely (this is the one the positioning stage will lean on):** liquidity raises the *unconditional* rate of both channels (R1, R6) while *tilting the mix* toward 13G/exit conditional on a block (R4, R5). "Liquidity is bad for activism" is a misreading of this paper; "liquidity is bad for activism *conditional on entry*" is the correct reading.

## 4. Institutional facts used

All from the disclosure rule, and all on the **threshold** and **re-filing** margins — never on the initial 10-day filing window as a source of variation:
- **Block = a stake of at least 5%** (printed p. 4). This is the threshold margin; EFZ take it as fixed throughout.
- **13D signals activist intent; 13G signals passivity.** "Blockholders who intend to engage in activism are required to file Schedule 13D upon acquiring a block in a public firm and state their activist intentions." (printed p. 5). Stated 13D intentions listed in n. 6: change the CEO or board, pursue strategic alternatives, oppose or induce a merger, increase the dividend, induce a buyback, change corporate governance.
- **13D amendment burden (the "window" they actually use):** a 13D filer must re-file within **10 days** on a **1%** change in stake; a 13G filer re-files only on a **5%** change, and the deadline is **45 days after calendar year end** for qualified investors under Rule 13d-1(b)(1) (printed p. 11). This asymmetry is EFZ's whole reason for treating the filing choice as a costly, therefore informative, signal.
- **13G initial deadline:** 45 days after the end of the calendar year of acquisition for Rule 13d-1(b)(1) filers, **10 days after block acquisition for others** — and "The majority of hedge funds in our sample are not registered with the SEC and so do not fall under Rule 13d-1(b)(1)" (n. 15, printed p. 13). This is why EFZ argue the 13G CAR is not mechanical price pressure.
- **20% forces 13D regardless of intent:** "the SEC mandates that any investor who holds 20% or more needs to file Schedule 13D regardless of the intent" — for those, EFZ hand-read Item 4 "Purpose of the Transaction" to reclassify active vs passive (n. 17, printed p. 14).
- **The amendment rule is also a tax on EXIT, not only a signal (added by verifier — n. 13, printed p. 11 / PDF p. 13).** EFZ spell out the mechanism in a footnote the card's earlier framing missed: "if a 13D filer wishes to sell her entire block of 5%, it is unlikely that she will be able to do so within a short period of time (she does not have to sell within 10 days) due to price impact. This is because, after she has sold the first 1%, she must file a 13D within 10 days. Such a filing will lower the price at which she can sell her remaining 4%." **This is the disclosure rule acting directly on the exit margin** — flagging is what makes the blockholder's own unwinding costly — and it is the one place EFZ let the rule do economic work rather than measurement work. It is the closest antecedent in this paper to our partition having a price consequence.
- **Legal cost of mislabelling:** a 13G filer who later amends to 13D "might still be sued for fraudulently stating her intentions in the initial filing, as per the Delaware Court of Chancery's decision in the case of NACCO Industries Inc. v. Applica Inc." (printed p. 11).
- **"Investment only" 13Ds:** 53 of the 490 13D filings state purpose as investment only; EFZ classify them as voice, and note reclassifying them leaves Tables 4–6 unchanged and strengthens Table 7 (n. 14, printed p. 11).
- **Ex-post 13G→13D switches are rare:** 42 out of the 1,112 initial 13Gs; 31 out of 645 with controls (printed p. 7).
- **Decimalization dates:** conversion between **August 2000 and April 2001**; tick 1/16 dollar → one cent; NYSE/AMEX effective 31 January 2001, Nasdaq 9 April 2001 (printed pp. 6, 18).
- Data sources: EDGAR (filings, hand-collected date + PERMNO), CRSP daily (returns, volume), Compustat (financials), I/B/E/S (analyst coverage), Execucomp via Edmans-Gabaix-Landier (2009) scaled WPS with Core-Guay (2002) option deltas, Eventus (CARs).

## 5. Referee-facing strengths / weaknesses

**Strengths:**
- The *ex ante intent* measure is the paper's real contribution: a 13D/13G choice is observed at block formation for every block, so the sample is not conditioned on activism succeeding or on a campaign being newsworthy. This dodges the selection problem in proxy-fight or campaign-outcome samples (their explicit contrast with Norli–Østergaard–Schindele, printed p. 5).
- Focusing on hedge funds removes the "some blockholders legally cannot use voice" confound (mutual-fund diversification rules, pension "prudent man" rules, business ties).
- Two liquidity proxies from different families (cost-per-volume, percent-cost), both signed the same way, and both highly persistent — so the year-t measure is a defensible proxy for the liquidity the fund will face when it later exits.
- The three-outcome decomposition (entry / conditional channel / unconditional voice) is exactly the accounting that stops the result being over-read; few papers bother.
- Lagging liquidity behind a dated event is a genuinely cleaner timing argument than the usual governance-index-on-liquidity regression.

**Weaknesses / open flanks:**
- **The "instrument" is not an instrument in this version.** `DECIMAL` never appears in a two-stage estimate; it replaces liquidity as a regressor. So the coefficient magnitudes on `DECIMAL` are reduced-form pre/post differences, not LATEs, and there is no first-stage F, no over-identification check, and no exclusion test beyond the LOWPRC split. A referee can say the 2001 break is contaminated by the post-dot-com regime, Reg FD (Oct 2000), and the entry of a new cohort of activist funds; the year FE for 2001–2002 are *dropped*, which is precisely where a confound would sit.
- **No pre-trend or event-time plot for decimalization.** The design is a level shift with year FE, not a difference-in-differences with a control group.
- **The exit channel is inferred, never observed.** No trade-level data: EFZ never see a blockholder sell. R7/R8 rest on WPS interactions, and R8 — the sharpest exit test — has N = 322, 10%-level significance, and an insignificantly *positive* level coefficient. That is a thin plank for the paper's headline interpretation.
- **The 13G CAR is small and jointly consistent with undervaluation.** 0.7% pooled; the liquidity split is the only thing separating "exit governance" from "the fund thinks the stock is cheap", and the argument that undervaluation returns should *fall* in liquidity is theoretical, not tested.
- **Merge attrition:** 1,821 filings → 1,135 firm-years. Losses are concentrated in pink-sheet and small firms — i.e. exactly the illiquid tail that identifies the liquidity coefficient.
- Intent ≠ action: a 13D is a *stated* purpose. EFZ acknowledge and partly patch this (n. 14) but never validate intent against realised campaigns.
- The interaction-coefficient-in-probit issue is flagged (n. 26, printed p. 23) and addressed by an Ai–Norton measure and an LPM, but only in text — the numbers are not shown.
- **The liquidity coefficients and the DECIMAL coefficients are not two estimates of the same thing, and EFZ say so (added by verifier, printed p. 18 / PDF p. 20).** With year FE in place, "the inclusion of year fixed effects for our specifications with LIQAM and LIQFHT is conservative as it means that we are identifying only on the variation on liquidity that is not driven by decimalization." So Table 2 cols (1)–(4) and cols (5)–(6) are estimated off *orthogonal* variation. That is an honesty point in their favour, but it also means the DECIMAL columns cannot be read as a validation of the LIQAM columns — a referee comparing the two magnitudes is comparing different experiments.
- **G-index robustness is weaker than it reads (added by verifier, n. 21, printed p. 17).** Adding the Gompers–Ishii–Metrick index costs ~75% of the sample in Tables 2, 4 and 6 and 28% in Tables 3 and 5, and EFZ report only that results stay "significant using at least one liquidity measure in every table" — i.e. not both measures survive everywhere.

## 6. What they do NOT do (scope boundary)

- **Object.** They stop at *governance channel choice and announcement return*. No takeover premium, no bidder entry, no campaign outcome, no realised change in firm policy. The only price object is a 3-day CAR around a 13G.
- **Margin of the disclosure rule.** They use the 5% threshold and the 13D-vs-13G distinction as **fixed institutional furniture** that lets them read intent. They study **no margin of the rule as a variable** — no change in the threshold, and crucially **no variation in the filing window**. The only window they discuss is the 13D *amendment* deadline (10 days on a 1% change) and the 13G deadline (45 days after year end / 10 days), and both enter as *costs that make the filing choice informative*, never as treatment. Their shock is to **liquidity**, not to the rule.
- **Identification.** Lagged-liquidity probit plus a decimalization pre/post dummy. No structural estimation, no DiD with a control group, no theory of their own — the hypotheses H1–H6 are borrowed from existing models and tested, not derived.
- **Realised exit.** Explicitly contrasted with, and not attempted: "while many existing papers study actual exit (e.g., Parrino, Sias, and Starks (2003)) or actual voice (e.g., Norli, Ostergaard and Schindele (2009)), the threat of exit or threat of voice also exerts governance" (printed p. 3). They measure *intent*, and deliberately never measure the act.
- **Non-hedge-fund blockholders.** Sample restricted to activist hedge funds by construction; they say Gerken (2009) finds no liquidity effect on governance choices and attribute the difference to their hedge-fund focus (printed p. 7) — an unresolved conflict, not a settled one.
- **Endogenous liquidity from the block itself.** They control the direction (lagged liquidity) but never model liquidity as jointly determined with the blockholder's own trading — which is exactly what our κ does.

## 7. Implications for our position

**Where EFZ sit in the competitor map:** object = *governance channel choice* (13D vs 13G) and *13G announcement return*; margin = **none — the disclosure rule is a fixed measurement device, not a treatment**; identification = lagged-liquidity probit + decimalization reduced form. So EFZ occupy the *liquidity* axis and leave the entire *disclosure-rule margin* axis empty.

1. **They are the antecedent our liquidity channel must cite, and they are not a competitor for the position.** They establish empirically that liquidity moves the blockholder's *action choice* — the exact object our partition (flagged vs pooled) governs. But their control outcome is a 3-day CAR on a passive filing. Nothing in EFZ speaks to bidder entry, takeover premium, or campaign success. That is our whitespace and they do not touch it.
2. **They pin down the sign we must reproduce.** Any core model of ours must deliver, at minimum: κ↑ ⇒ more blocks formed (R1), κ↑ ⇒ conditional tilt away from public voice toward the pooled/quiet action (R4), and κ↑ ⇒ *unconditional* voice still rises (R6). Our four-action structure (exit / hold / quiet voice / public voice) maps to this cleanly, with 13G ↔ pooled state and 13D ↔ flagged state. R6 in particular is a discipline: a model that makes liquidity monotonically bad for public voice unconditionally is **refuted by their Table 6**, and a referee who knows this paper will say so.
3. **They validate the empirical proxy for κ.** LIQAM = −ln(1 + Amihud) over the pre-filing fiscal year is the standard, and CONTEXT.md already names "an Amihud-type illiquidity measure inverted" as our empirical κ. Using theirs verbatim costs us nothing and buys comparability. R13 (2.2–2.4% price impact for selling ~1% of shares in the illiquid quartile vs 0.9–1.1% in the third quartile) is a usable calibration target for the trading-cost side of the core model.
4. **Their identification weakness is our opening on the anchor.** EFZ's shock is to *liquidity* and it is a 2001 level break with no control group. Our anchor is a shock to the **rule** (the Feb-2024 window acceleration, 10 → 5 business days), which is dated, exogenous to any single firm, and has a natural comparison group. Positioning line: EFZ shocked liquidity and held the rule fixed; we hold liquidity as the driving variable and shock the *window margin* of the rule. Different treatment, different object, non-overlapping.
5. **A caution on the 13G side.** In EFZ, 13G is "exit or no governance" and they cannot separate the two — that ambiguity is the paper's soft spot. Our partition gives a *reason* the pooled state carries value (the market cannot condition on the block), which is a theoretical contribution over their inference-by-interaction. Do not, however, claim we resolve their ambiguity empirically unless we have trade-level data; we do not.
6. **Their policy lever is liquidity; ours is the rule — and they close on that lever explicitly (added by verifier, printed pp. 28–29 / PDF pp. 30–31).** EFZ end by entering "the public policy debate on the desirability of liquidity for the overall economy": against "the classical view [that] argues that liquidity is harmful for governance and advocate[s] restrictions on liquidity", they conclude liquidity "can be beneficial in attracting large shareholders to a firm, and enabling them to govern more effectively once they have acquired their stake." This is a *usable* positioning contrast, not just a citation: the paper that owns the liquidity axis proposes a liquidity-side policy lever and never considers the disclosure rule as an instrument at all. Our claim is that the rule is the lever a regulator actually moves — and in Feb 2024 did move.
7. **Version risk.** Everything above is the 2011 NBER WP. The RFS article is two years later; sample, table numbering and possibly the decimalization treatment could have changed in referee rounds (an RFS referee is exactly the person who would have demanded a real first stage). **Before any of these magnitudes is written into draft_v3, the RFS version must be fetched and the numbers re-checked.** Flag this to the positioning stage.

## 8. Quotes we may lean on (verbatim, page-cited)

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "We find that liquidity increases the likelihood that a hedge fund acquires a block in a firm." | Abstract, PDF p. 2 | The entry margin; our κ↑ ⇒ block formation |
| Q2 | "Conditional upon acquiring a stake, liquidity reduces the likelihood that a blockholder governs through voice (intervention) – as evidenced by the greater propensity to file Schedule 13Gs (passive investment) rather than 13Ds (active investment)." | Abstract, PDF p. 2 | The conditional tilt toward the pooled state |
| Q3 | "We use decimalization as an exogenous shock to liquidity to identify causal effects." | Abstract, PDF p. 2 | Their identification claim, quoted as claimed |
| Q4 | "Thus, decimalization can instrument for liquidity as it led to an increase in liquidity, but was unlikely to affect a hedge fund's governance strategy other than through liquidity." | printed p. 6 (PDF p. 8) | The exclusion restriction as stated; note no 2SLS follows |
| Q5 | "These steps lead to a dataset of 709 initial Schedule 13Ds and 1,112 initial Schedule 13Gs filed by 101 hedge funds." | printed p. 14 (PDF p. 16) | Sample size, raw |
| Q6 | "A one standard-deviation increase in liquidity as measured by LIQAM (LIQFHT) increases the probability of a block acquisition by 0.47 (0.20) percentage point." | printed p. 21 (PDF p. 23) | Magnitude, entry margin |
| Q7 | "A one standard deviation increase in LIQAM (LIQFHT) is associated with a 6.88 (4.97) percentage point decrease in the likelihood of filing 13D, compared to the 43.2% probability of such a filing conditional upon acquiring a block." | printed p. 24 (PDF p. 26) | Magnitude, channel margin |
| Q8 | "Blockholders who intend to engage in activism are required to file Schedule 13D upon acquiring a block in a public firm and state their activist intentions." | printed p. 5 (PDF p. 7) | Institutional fact: 13D = declared purpose |
| Q9 | "A 13D filer must subsequently re-file within 10 days upon a change in stake of 1%, which alerts the market to changes in her position and moves the price against her." | printed p. 11 (PDF p. 13) | Institutional fact: 13D/A amendment window (pre-2024) |
| Q10 | "In contrast, a 13G filer only needs to re-file for a change in stake of at least 5%, and the re-filing deadline is 45 days after the end of the calendar year (for qualified investors listed under Rule 13d-1(b)(1))." | printed p. 11 (PDF p. 13) | Institutional fact: the 13G/13D asymmetry that makes the filing choice informative |
| Q11 | "However, the SEC mandates that any investor who holds 20% or more needs to file Schedule 13D regardless of the intent." | printed p. 14, n. 17 (PDF p. 16) | Institutional fact: threshold margin has a second kink at 20% |
| Q12 | "In the full sample, firms experience a 0.7% average abnormal return to a 13G filing." | printed p. 27 (PDF p. 29) | The only price object in the paper — and how small it is |

## 9. Verification log

*(Filled by the verifier.)* Quotes Q1–Q12 were located by exact substring match against `research/txt_extracts/efz2013_layout.txt` (a `pdftotext -layout` re-extract of `lit/edmans-fang-zur-liquidity-2013.pdf`, page-marked) at the PDF pages stated; Q4 contains a typographic apostrophe in "fund's" in the source. The plain `research/txt_extracts/efz2013.txt` extract breaks words mid-token (e.g. "re -file", "th e") and should **not** be used for quote checking. Printed-page mapping (printed = PDF − 2) verified at PDF pp. 3, 6, 7, 13, 16, 23, 26, 29.

### Verifier pass (adversarial, 2026-08-19)

Source of truth: an **independent** per-page re-extract of `lit/edmans-fang-zur-liquidity-2013.pdf` built by the verifier (`pdftotext -f N -l N -layout`, 48 pages), not the reader's file. Quote matching was whitespace- and hyphenation-normalised. Printed-page mapping **printed = PDF − 2** independently re-confirmed by reading the page-foot folio on PDF pp. 3, 5, 7, 8, 13, 16, 23, 26, 29, 38, 40, 42, 43, 44, 46, 47, 48.

**Counts: 12 quotes OK, 0 WRONG, 0 MISCITED, 0 UNCHECKED. 14 results OK on numbers; 2 corrected for a mis-stated definition (see below). 0 scope claims refuted; 4 omissions added.**

| Item | Status | Checked against |
|---|---|---|
| Q1, Q2, Q3 | OK | PDF p. 2 (abstract, unnumbered) — exact match |
| Q4 | OK | PDF p. 8 = printed p. 6 — exact match |
| Q5 | OK | PDF p. 16 = printed p. 14 — exact match, in body not footnote |
| Q6 | OK | PDF p. 23 = printed p. 21 — exact match |
| Q7 | OK | PDF p. 26 = printed p. 24 — exact match |
| Q8 | OK | PDF p. 7 = printed p. 5 — exact match |
| Q9, Q10 | OK | PDF p. 13 = printed p. 11 — exact match |
| Q11 | OK | PDF p. 16 = printed p. 14, footnote 17 — exact match |
| Q12 | OK | PDF p. 29 = printed p. 27 — exact match |
| R1, R3 | OK | Table 2 Panel A, PDF p. 40. Every coefficient, SE, marginal effect and N = 88,742 matches the print |
| R2 | OK | PDF p. 23, printed p. 21: "0.47 (0.20) percentage point", "unconditional probability … of 1.3%" |
| R4 | OK | Table 4 Panel A, PDF p. 44. All six coefficients, SEs, mfx and N = 1,135 match |
| R5 | OK | PDF p. 26, printed p. 24: "6.88 (4.97) percentage point decrease", "43.2% probability" |
| R6 | OK | Table 6, PDF p. 47. LIQAM 0.103\*\*\*(0.026)/[0.0013\*\*\*], LIQFHT 3.851\*\*\*(1.435)/[0.0493\*\*\*], DECIMAL 0.309\*\*\*(0.088)/[0.0041\*\*\*], N = 88,742 — all match |
| R7 | OK | Table 3, PDF p. 43. Interactions 0.019\*(0.010), 0.049\*\*(0.021), N = 24,645 |
| R8 | OK | Table 5, PDF p. 46. −2.390\*(1.298), −38.281\*(22.928); levels 0.722(0.927), 7.337(11.494); N = 322 |
| R9, R10 | OK | Table 7 Panels A & B, PDF p. 48. All means, SEs, N = 630, adj. R² 0.014/0.010 |
| R11 | OK | Table 2 Panel B (PDF p. 41) and Table 4 Panel B (PDF p. 45). 0.551\*\*\*(0.083) vs 0.360(0.281), diff 0.191\*\*\* [0.000]; −1.213\*\*\*(0.351) vs −0.165(0.329), diff −1.048\*\*\* [0.002] |
| R12 | **CORRECTED** | Table 2 Panel C, PDF p. 42. Coefficients and N = 4,576 are right, but the dependent variable is `BLOCK`~t+2~, not `BLOCK`~t+1~; also industry FE only, no year FE. Card text amended |
| R13 | OK | PDF p. 22 = printed p. 20 (the card cited pp. 19–20; the sentence sits on printed p. 20) |
| R14 | OK as ASSERTED | PDF p. 30 = printed p. 28 — the sentence is a conclusion paragraph, correctly labelled |
| §2 `DECIMAL` definition | **CORRECTED** | PDF p. 20 = printed p. 18. The card said "= 1 for events after 31 Jan / 9 Apr 2001". The print defines it as fiscal-year-t *end* after those dates for the block regressions, and on the *filing date* for the 13D-vs-13G regressions. Card text amended |
| §2 correlations 0.750 / 0.788, persistence | OK | Table 1 Panels C–D, PDF p. 39. Own-lag Pearson 0.859 (LIQAM) / 0.846 (LIQFHT); Spearman 0.944 / 0.905 — the card's "0.85–0.94" is the correct range |
| §2 sample 1 Jan 1995 – 31 Dec 2010; 223 funds; 709 + 1,112 by 101 funds; 69 of 101 both | OK | PDF pp. 15, 16, 16, 5 (= printed 13, 14, 14, 3) |
| **DECISION-CRITICAL: "no 2SLS / no first stage / no F-stat"** | **OK — CONFIRMED, refutation attempted and failed** | Executed check: `grep -inE "2sls\|two-stage\|two stage\|first[- ]stage\|instrumental variable\|iv[- ]probit\|overidentif\|F-stat\|weak instrument"` over the full 48-page extract returns **zero hits**. `grep -in instrument` returns exactly three hits (printed pp. 4, 6, 6) — all prose. In Table 2 Panel A and Table 4 Panel A, `DECIMAL` occupies cols (5)–(6) *in place of* LIQAM/LIQFHT. The card's claim is correct as stated |
| **DECISION-CRITICAL: unconditional 13D probability still rises with liquidity** | **OK** | Table 6, PDF p. 47 — all three specifications positive and significant at 1%; conclusion (printed p. 28) states "the unconditional effect of liquidity on active intervention is positive" |
| §6 "no takeover premium / no bidder entry / no tender offer" | **OK — confirmed by executed grep** | `grep -in` for `takeover`, `premium`, `bidder`, `tender offer` over the full text: `premium`, `bidder` and `tender offer` return **zero hits**; `takeover` appears only twice, both in the reference list (Greenwood–Schor; Kyle–Vila titles) |
| §6 "no variation in the filing window" | **OK — confirmed by executed grep** | `window` appears once in the body (n. 28, alternative CAR windows (0,+1)/(0,+2)/(0,+3)); `10 days` appears only as the 13D *amendment* deadline and the non-1(b)(1) 13G deadline. No window is treated as variation |
| §6 Gerken (2009) conflict, printed p. 7 | OK | PDF p. 9 = printed p. 7 — but note EFZ *also* cite Gerken approvingly on printed p. 21 as consistent with their block-formation result. The conflict is confined to the *channel-choice* result |
| §4 42/1,112 and 31/645 13G→13D switches, printed p. 7 | OK | PDF p. 9 = printed p. 7 |
| §4 53 of 490 "investment only" (n. 14), NACCO, printed p. 11 | OK | PDF p. 13 = printed p. 11 |
| §4 20%-rule reclassification (n. 17), printed p. 14 | OK | PDF p. 16 = printed p. 14 |
| §4 LOWPRC descriptive first stage 0.368 (0.024) vs 0.077 (0.007) | OK | PDF p. 24 = printed p. 22 |

**Omissions added by the verifier** (each material to a liquidity × disclosure-rule × control-outcome position):
1. **§4 — n. 13, printed p. 11:** the 13D amendment rule is a **tax on exit**, not only a signalling cost. Selling the first 1% forces a filing within 10 days that moves the price against the remaining 4%. This is the one place EFZ let the disclosure rule act on an economic margin rather than serve as a measurement device, and it is the nearest antecedent in the paper to our partition carrying a price consequence.
2. **§5 — printed p. 18:** EFZ state that with year FE the LIQAM/LIQFHT specifications identify "only on the variation on liquidity that is not driven by decimalization". The liquidity columns and the DECIMAL columns therefore rest on *orthogonal* variation and are not mutual validation.
3. **§5 — n. 21, printed p. 17:** the G-index robustness check costs ~75% of the sample in Tables 2/4/6 and 28% in Tables 3/5, and survives only "using at least one liquidity measure in every table".
4. **§7 — printed pp. 28–29:** EFZ close by arguing *against restrictions on liquidity* as policy. The paper that owns the liquidity axis proposes a liquidity-side lever and never considers the disclosure rule as one. That is a sharper positioning contrast than "they leave the rule axis empty".

**Nothing decision-critical went unchecked.** The one live risk is the card's own §7 item 7: every number above is the **2011 NBER WP**, and the RFS (2013) article was not in hand. The RFS version is where a referee would most plausibly have forced a real first stage, so the "no 2SLS" finding is verified **for this version only** and must be re-run against RFS 26(6) before it is used to characterise the published paper.

**Overall verdict: the card is accurate.** Zero WRONG quotes, zero WRONG results, two definitional corrections, four omissions added. The two decision-critical claims (DECIMAL is reduced-form, not IV; unconditional 13D probability rises in liquidity) both survive adversarial checking against the print.

## 9b. Published-version check (RFS 26(6), 1443–1482) — added by supplement reader, 2026-08-19

Source of truth: a per-page `pdftotext -layout` re-extract of
`research/txt_extracts/edmans_fang_zur_2013_rfs_published.pdf` (40 PDF pages), read end to end.
**Published RFS page = PDF page + 1442.** Everything below is the published article; §§1–8 above
remain as written against the WP.

**Headline for the positioning stage: the two magnitudes the card leans on both survive.
+0.47 pp/SD on block acquisition is verbatim in print (p. 1458). −6.88 pp/SD on the 13D
choice survives as −6.9 (5.0) pp — rounded, not revised (p. 1461).**

**Decision-critical answer to the verifier's question: NO. The published version still has no
2SLS, no first stage, and no F-statistic.** An executed grep over the full 40-page extract for
`2sls|two-stage|two stage|first[- ]stage|instrumental variable|iv[- ]probit|overidentif|F-stat|weak instrument`
returns **two hits, both in footnote 27 (p. 1473)**, and both are about a *Heckman selection*
model, not about decimalization: "We do not conduct a Heckman selection or a nested logit as
all the explanatory variables in our regressions affect both the first stage (decision to acquire a
block) and the second stage (choice of governance mechanism conditional upon block
acquisition). We have not been able to come up with a valid instrument that convincingly affects
only the first-stage decision, but not the second-stage decision." `instrument` appears exactly
once more, on p. 1446: "All of our results remain robust to using this instrument." In Table 2
Panel A, Table 3 Panel A and Table 8, `DECIMAL` still occupies its own columns *in place of*
LIQAM/LIQFHT. **DECIMAL is a reduced-form substitute regressor in the published version too.**
The card's §5 weakness "the instrument is not an instrument" therefore stands against the RFS
article, not merely against the WP — and it is now *strengthened*, because the RFS referees saw
this and the authors state in print that they could not find a valid instrument.

### Table renumbering (WP → published)

| WP table | Published table | RFS page |
|---|---|---|
| Table 1 (summary/correlations) | Table 1, Panels A–E (Panel C = filings by fiscal year is **new**) | 1456–1457 |
| Table 2 Panels A–C (block acquisition) | Table 2 Panels A–C — unchanged | 1459–1460 |
| Table 3 (LIQ × WPS on entry) | **Table 6** | 1467 |
| Table 4 Panels A–B (13D vs 13G) | **Table 3** Panels A–B | 1462 |
| Table 5 (LIQ × HIGHWPS on choice) | **Table 7** | 1469 |
| Table 6 (unconditional 13D) | **Table 8** | 1470 |
| Table 7 Panels A–B (13G CAR) | **Table 4** Panels A–B, plus a **new Panel C** (holding-period returns) | 1463 |
| — | **Table 5** (operating-performance DiD) — **new** | 1466 |
| — | **Figure 1** (theory × hypothesis grid) — **new** | 1448 |
| — | **Appendix A.1** (legal issues) and **A.2** (variable definitions) — **new** | 1477–1479 |
| — | **Online Appendix Tables OA1–OA17** — **new**, not in hand | — |

### Every §3 result → published version

| # | Verdict | Published location and what changed |
|---|---|---|
| R1 | **same** | Table 2 Panel A, p. 1459. Every coefficient, SE, marginal effect and N = 88,742 identical to the WP |
| R2 | **same** | p. 1458 — "0.47 (0.20) percentage points" against the 1.3% unconditional rate, verbatim. The Introduction restates it as a **range**, "0.2%–0.5%" (p. 1445) |
| R3 | **same** | Table 2 Panel A cols (5)–(6), p. 1459: DECIMAL 0.299\*\*\*(0.024) / 0.544\*\*\*(0.064), mfx 0.0094 / 0.0158 |
| R4 | **same numbers, table renumbered** | **Table 3** Panel A, p. 1462. −0.152\*\*\*(0.046) / −0.169\*\*\*(0.064); −4.047\*(2.456) / −6.662\*\*(3.260); −0.295\*\*\*(0.084) / −0.492\*\*(0.236); all mfx and N = 1,135 identical |
| R5 | **changed (rounding only)** | p. 1461: "a **6.9 (5.0)** percentage point decrease", was "6.88 (4.97)". Base rate 43.2% unchanged. Introduction states it as "5%–7%" (p. 1445). **The substantive magnitude survives; cite 6.9 (5.0) pp, p. 1461** |
| R6 | **same numbers, table renumbered** | **Table 8**, p. 1470. LIQAM 0.103\*\*\*(0.026)[0.0013], LIQFHT 3.851\*\*\*(1.435)[0.0493], DECIMAL 0.309\*\*\*(0.088)[0.0041], N = 88,742. **Added:** an economic-magnitude sentence absent from the WP — a one-SD rise in LIQAM (LIQFHT) raises the probability of a 13D filing by **0.14 (0.09) percentage points**, against an unconditional 13D rate of **0.6%** (pp. 1468–1469) |
| R7 | **same numbers, extended** | **Table 6**, p. 1467. LIQAM×WPS 0.019\*(0.010), LIQFHT×WPS 0.049\*\*(0.021), N = 24,645 identical. **Added:** the level coefficients LIQAM 0.180\*(0.101), LIQFHT 8.326\*(5.042); a **third column on DECIMAL** — DECIMAL 0.508\*\*\*(0.079), DECIMAL×WPS 1.480\*(0.816); and a de-meaned economic-significance calculation (p. 1468): at mean WPS a one-SD liquidity rise adds 0.37 (0.47) pp to block probability, at +1 SD WPS it adds 0.49 (0.58) pp — **32% (23%) greater** |
| R8 | **same numbers, extended** | **Table 7**, p. 1469. −2.390\*(1.298), −38.281\*(22.928); insignificant levels 0.722(0.927), 7.337(11.494); N = 322. **Added:** a third column — DECIMAL 0.852(0.751), DECIMAL×HIGHWPS −0.854\*(0.463). Still 10%-level only, and the authors now say so in print: they "interpret the significance of the LIQUIDITY×WPS interaction term as **only suggestive evidence**" (p. 1473) |
| R9 | **changed — the WP numbers are now the *equal-weighted* column** | **Table 4** Panel A, p. 1463. The WP's 0.007\*\*\*(0.002) pooled, 0.010\*\*\*/0.004 (LIQAM split), 0.009\*\*\*/0.005 (LIQFHT split) reappear **identically** as `CAR_EW(−1,+1)`. **Added, and now the headline:** a value-weighted CAR with market-model beta over (−255,−46) — `CAR_VW(−1,+1)` pooled **0.008\*\*\*(0.002)**, high LIQAM **0.012\*\*\*** vs low 0.004, high LIQFHT **0.012\*\*\*** vs low 0.004. N = 630 unchanged. **Cite 0.8% (VW) / 0.7% (EW), p. 1461** |
| R10 | **changed — same way** | **Table 4** Panel B, p. 1463. The WP's HIGHLIQAM 0.015\*\*(0.007) and HIGHLIQFHT 0.010\*(0.006) are now cols (3)–(4), `CAR_EW`, identical. **Added** cols (1)–(2) on `CAR_VW`: HIGHLIQAM **0.017\*\*(0.007)**, HIGHLIQFHT **0.014\*\*(0.006)**. Adj. R² 0.014 / 0.012 / 0.014 / 0.010, N = 630 |
| R11 | **same** | Table 2 Panel B (p. 1459): 0.551\*\*\*(0.083) vs 0.360(0.281), difference 0.191\*\*\* [p = 0.000]. **Table 3** Panel B (p. 1462): −1.213\*\*\*(0.351) vs −0.165(0.329), difference −1.048\*\*\* [p = 0.002]. The descriptive levels first stage is now **rounded and SE-free**: LIQAM (LIQFHT) rises 0.37 (0.02) in LOWPRC = 1 vs 0.08 (0.01) in LOWPRC = 0, both differences 1% (p. 1458) — was 0.368 (0.024) vs 0.077 (0.007) |
| R12 | **same** | Table 2 Panel C, p. 1460: ΔLIQAM 0.128\*\*(0.055), ΔLIQFHT 9.228\*\*\*(2.782), N = 4,576. The published panel header **confirms the verifier's WP correction in print**: the dependent variable is `BLOCK`~t+2~ and the panel carries industry FE only, no year FE |
| R13 | **CHANGED — do not use the WP numbers** | Moved to **Online Appendix Table OA2**, described at p. 1457. On days when 0.9%–1.1% of shares outstanding trade, third-AMIHUD-quartile firms experience a **4.2%** return and fourth-quartile (most illiquid) firms **7.0%**; by FHT, **3.9%** vs **6.9%–7.0%**. The WP figures the card carried (0.9–1.1% vs 2.2–2.4%; 1.2–1.4% vs 2.5–2.6%) **do not appear in the published paper**. Published also adds Panels B and C for 0.4%–0.6% and 0.1%–0.3% volume days. **The calibration target for our trading-cost side is now 4.2% vs 7.0%, p. 1457 / Table OA2** |
| R14 | **same, still ASSERTED** | Conclusion, pp. 1476–1477. Wording tightened: "liquidity increases the frequency of both voice and exit and so improves blockholder governance overall" |

### Every §8 quote → published version

Published wording is authoritative. Where a quote changed, **use the published text and the published page.**

| # | Verdict | Published text / page |
|---|---|---|
| Q1 | **changed** | The abstract now reads only "Liquidity increases the likelihood of block formation." (p. 1443). The card's sentence survives, expanded, in the body: "First, we find that liquidity increases the likelihood that an activist hedge fund acquires a block (a stake of at least 5%) in a firm." — **p. 1445** |
| Q2 | **changed (wording)** | Abstract, p. 1443: "Conditional upon acquiring a stake, liquidity reduces the likelihood that the blockholder governs through voice (intervention)—as shown by the lower propensity for active investment (filing Schedule 13D) than passive investment (filing Schedule 13G)." (was "as evidenced by the greater propensity to file Schedule 13Gs … rather than 13Ds") |
| Q3 | **same** | Abstract, p. 1443, verbatim: "We use decimalization as an exogenous shock to liquidity to identify causal effects." |
| Q4 | **ABSENT — the "can instrument" claim is gone** | The WP sentence "Thus, decimalization can instrument for liquidity as it led to an increase in liquidity, but was unlikely to affect a hedge fund's governance strategy other than through liquidity" **does not appear in the published article**. Its second half survives, without the instrument framing, at **p. 1454**: "This event led to an increase in liquidity but was unlikely to affect a hedge fund's governance strategy other than through liquidity." The word "instrument" survives only as "All of our results remain robust to using this instrument" (p. 1446). **Do not attribute the "can instrument for liquidity" wording to RFS 2013** |
| Q5 | **changed (minor)** | p. 1452: "These steps lead to a dataset of 709 Schedule 13Ds and 1,112 Schedule 13Gs filed by 101 funds." ("initial" and "hedge" dropped) |
| Q6 | **changed (minor), number identical** | p. 1458: "A one-standard-deviation increase in liquidity as measured by LIQAM (LIQFHT ) increases the probability of block acquisition by 0.47 (0.20) percentage points." |
| Q7 | **changed (rounded)** | p. 1461: "A one-standard-deviation increase in LIQAM (LIQFHT ) is associated with a 6.9 (5.0) percentage point decrease in the likelihood of filing a 13D, compared with the 43.2% probability of such a filing conditional upon acquiring a block." |
| Q8 | **changed** | p. 1445: "Blockholders who intend to engage in intervention must file a Schedule 13D, as it legally entitles them to engage in the form of activism that they specify in Item 4 of the filing." (The WP's "state their activist intentions" phrasing is gone) |
| Q9 | **changed (minor)** | p. 1449: "A 13D filer must refile within ten days upon a change in stake of 1%, which alerts the market to changes in her position and moves the price against her." ("re-file"→"refile", "10 days"→"ten days") |
| Q10 | **changed, and materially extended** | p. 1449: "In contrast, a 13G filer only needs to refile for a change in stake of 5%, and the refiling deadline can be as late as forty-five days after the end of the calendar year (for "qualified institutional investors" listed under Rule 13d-1(b)(1))." **Immediately followed by a sentence the WP does not have — and the single most useful sentence in the paper for us: "These different filing deadlines also apply to the initial crossing of the 5% threshold."** That is EFZ naming the **window margin** in print (added by supplement reader) |
| Q11 | **changed** | The WP footnote is gone. Published equivalents: §4.2.3, p. 1475 — "any investor who holds 20% or more needs to file a 13D even if she intends to remain passive"; and Appendix A.1, p. 1478 — "A passive investor who crosses a 20% threshold must file a 13D regardless of its governance intent" |
| Q12 | **ABSENT as worded** | "In the full sample, firms experience a 0.7% average abnormal return to a 13G filing" does not appear. Replacement, p. 1461: "Table 4, Panel A, shows that, around a 13G filing, firms experience a **0.8% (0.7%)** average three-day value-(equally-)weighted abnormal return CAR_VW (−1,+1) (CAR_EW (−1,+1))." |

### WP → published page map for the cited passages

| Passage | WP printed p. | RFS p. |
|---|---|---|
| Abstract (Q1–Q3) | PDF p. 2 | 1443 |
| Sample period 1995–2010; Factiva → 223 funds; 709 + 1,112 by 101 funds | 13–14 | 1452 |
| 13D = declared purpose (Q8) | 5 | 1445 |
| Decimalization dates, tick 1/16 → $0.01 | 6, 18 | 1446, 1454 |
| Q4 exclusion-restriction sentence | 6 | 1454 (framing changed; see above) |
| Stated 13D intentions list (WP n. 6) | 5 | fn 7, 1449 (**list changed**: now CEO/board, capital structure, asset sales, merger, spin-off, dividend, cutting executive pay) |
| 13D amendment burden (Q9) / 13G asymmetry (Q10) | 11 | 1449 |
| NACCO v. Applica | 11 | fn 8, 1449 (**adds** "settled for $60 million") |
| **13D amendment as a tax on exit** (WP n. 13) | 11 | **fn 9, 1449** — reworded: "if a 13D filer wishes to sell her entire block of 5%, it is unlikely that she will be able to do so within ten days, due to price impact. (The median daily trading volume in our sample is 0.35%.) After she has sold the first 1%, she must file a 13D within ten days. Such a filing will lower the price at which she can sell her remaining 4%." The WP's confusing parenthetical "(she does not have to sell within 10 days)" is **dropped** and replaced by the 0.35% median-volume datum, which makes the mechanism sharper for us |
| DECIMAL definition (fiscal-year end vs filing date); year FE dropped 2001–02 | 18 | 1454–1455 (**adds** that 1995 is also dropped in the LIQAM/LIQFHT specifications) |
| Liquidity persistence 0.85–0.94 | 37 | Table 1 Panel E, 1457 |
| 53 of 490 "investment only" 13Ds | n. 14, 11 | §4.2.3, 1475 |
| 20% rule, hand-read Item 4 (Q11) | n. 17, 14 | §4.2.3, 1475 and Appendix A.1, 1478 |
| G-index robustness (~75% / 28% sample loss) | n. 21, 17 | **fn 16, 1454** (table numbers remapped: 75% in Tables 2, 3, 8; 28% in Tables 6, 7) |
| Ai–Norton / LPM caveat on probit interactions | n. 26, 23 | **fn 24, 1467** (now says the LPM interaction is "slightly stronger than in Table 6") |
| Gerken (2009) conflict | 7 | 1447 |
| LOWPRC descriptive first stage | 22 | 1458 (rounded) |
| Price-impact calibration | 19–20 | **Online Appendix Table OA2**, described 1457 (**numbers changed**) |
| Policy close ("restrictions on liquidity") | 28–29 | 1476–1477 |
| Conclusion (R14) | 28 | 1476–1477 |

### What the published version ADDS (added by supplement reader)

1. **A whole third result the WP card does not carry: 13G filings improve operating performance.**
   New **Table 5** (p. 1466). Each of the 645 13G targets is propensity-matched without
   replacement to a control firm on the full control vector plus FF-12 industry and year dummies;
   500 matched pairs survive (145 lost: financials required in t−1 and t+1, no replacement).
   Difference-in-differences t−1 → t+1: EBITDA/ASSET **+0.015\*** (t = 1.78), CFO/ASSET
   **+0.014\*** (t = 1.67). Stratified by liquidity (Panel D), the effect is **entirely in the liquid
   half**: high-LIQFHT EBITDA/ASSET **+0.033\*\*\*** (t = 2.67) and CFO/ASSET **+0.029\*\***
   (t = 2.43); high-LIQAM EBITDA/ASSET **+0.033\*\*** (t = 2.55); both low-liquidity subsamples
   are zero. This is the paper's **only real-outcome object**, and it is a matched DiD — a much
   better-identified design than anything in the WP. It does *not* reach our control outcome
   (no bidder, no premium, no campaign success), so §6 and §7 are unaffected, but the card can no
   longer say "the only price object is a 3-day CAR".
2. **Holding-period returns to 13G filings** — new **Table 4 Panel C** (p. 1463), N = 523. Mean raw
   holding-period return 23.2%; market-adjusted **5.3% (VW) / 5.0% (EW)** pooled, **9.2% / 8.8%**
   in the liquid half, insignificant in the illiquid half (p. 1464). Exit date is hand-built from the
   successive 13G that drops below 5%, or from 13Fs; 13Gs whose firm is acquired before exit are
   deleted. **Note for us: they delete exactly the takeover cases.**
3. **A full theory-to-hypothesis grid, Figure 1 (p. 1448),** restructuring the paper into voice-B /
   voice-G / exit against H1–H5. H3 is now three sub-hypotheses (H3a event return, H3b
   holding-period return, H3c operating performance) and H4 two (H4a entry, H4b choice). This is a
   template worth stealing for draft_v3's own predictions table.
4. **A non-hedge-fund-activist extension that resolves the Gerken (2009) conflict** (§4.1,
   pp. 1470–1472; Online Appendix Tables OA4–OA11). Repeating the Factiva search without the
   "hedge" filter gives **1,636 events by 91 hedge funds and 120 other institutions — 1,005 13Gs and
   631 13Ds**. Findings: H1 still holds (one-SD LIQAM (LIQFHT) → +0.56 (0.32) pp against a 1.8%
   base rate), but **H2 loses significance once controls are added**, and 13G announcement returns
   for non-hedge-fund activists are insignificant even pooled. EFZ conclude this is "consistent with
   Gerken (2009)". **This matters for our §5: the channel-choice result — the one our partition maps
   onto — is a hedge-fund-only result and EFZ now say so in print.**
5. **A size placebo on the LOWPRC split** (fn 20, p. 1458): splitting the sample by MV instead
   finds **no significant difference** in the DECIMAL coefficient, so LOWPRC is not proxying for
   size; and within both LOWPRC groups LIQAM and LIQFHT are both significantly positive. This
   partly answers the card's §5 complaint that the exclusion story rested on one split.
6. **A stack of robustness checks that did not exist in the WP,** all in the Online Appendix:
   multinomial logit over {no block, 13G, 13D} (OA12 — LIQAM and DECIMAL significantly favour 13G
   over 13D, LIQFHT marginally insignificant at p = 0.11); VEGA and LIQUIDITY×VEGA controls (OA13);
   LIQUIDITY² control (OA14); the 69 funds that file **both** 13Ds and 13Gs, where the H2 result is
   **stronger** than the full sample (OA15); firm fixed effects with an LPM (OA16, OA17, both
   significant at 5%); calendar-time long-run returns showing a positive event month and **no**
   pre- or post-event drift (OA3); persistence of liquidity conditional on a filing (OA1).
7. **Appendix A.1, "Legal issues surrounding 13D and 13G filings" (pp. 1477–1478) — new, and it is
   the best short statement of the rule in the competitor set.** It gives, in print: the 10-day
   initial 13D deadline from crossing 5%; the 10-day 13D/A amendment deadline on a 1% stake change
   or a change of purpose; the three classes of 13G filer (qualified institutional under
   13d-1(b)(1), exempt under 13d-1(d), passive); **passive investors must file the 13G within ten
   days of crossing 5%, while qualified institutions have forty-five days after calendar year end
   — unless the stake crosses 10%, in which case ten days after month end**; that a hedge fund
   registered as an investment adviser is a qualified institution and otherwise is not; the 20%
   rule; and the enforcement tail (civil suits by management or selling shareholders, SEC/DOJ
   penalties, vote prohibition, disgorgement). **Cite Appendix A.1, pp. 1477–1478 for the pre-2024
   rule** rather than the WP footnotes.
8. **A new detail useful for the cost-of-exit calibration:** median daily trading volume in the
   sample is **0.35% of shares outstanding** (fn 9, p. 1449). With the 5% threshold, that is roughly
   fourteen median-volume days to unwind a block — the arithmetic our window margin acts on.

### What the published version DROPS (added by supplement reader)

1. **The "orthogonal variation" concession is gone.** The WP sentence the verifier added to §5 —
   that with year FE "we are identifying only on the variation on liquidity that is not driven by
   decimalization", making the LIQAM and DECIMAL columns non-mutual-validation — **does not appear
   in the published article** (executed grep for `conservative|not driven by decimalization|
   orthogonal`: zero hits). §5's omission #2 is therefore **true of the WP only**. The
   *substantive* point still holds (year FE for 1996–2000 and 2003–2010 are in, 2001–02 out), but
   it can no longer be attributed to EFZ. **Do not cite RFS for it — argue it ourselves.**
2. **The ex-post 13G→13D switch counts (42 of 1,112; 31 of 645) are gone** — no such figures in the
   published article. §4 must drop that bullet or re-source it.
3. **The WP's price-impact numbers are gone** (see R13). Cite Table OA2 / p. 1457 instead.
4. The WP's policy close is softened: "the desirability of liquidity **for governance**" (not "for
   the overall economy"), and "facilitating governance through exit once they have acquired their
   stake" (not "enabling them to govern more effectively"). §7 item 6 should quote the published
   form, pp. 1476–1477.

### §9 UNCHECKED items closed by the published version

| Item left open in §9 | Status now |
|---|---|
| "no 2SLS / no first stage / no F-stat — verified **for the WP only**; must be re-run against RFS 26(6)" | **CLOSED.** Re-run against RFS 26(6): still no 2SLS, no first stage, no F-statistic. `DECIMAL` remains a substitute regressor in Tables 2, 3, 6, 7, 8. Footnote 27 (p. 1473) states the authors could not find a valid instrument for the selection problem |
| "sample, table numbering and possibly the decimalization treatment could have changed in referee rounds" | **CLOSED.** Sample identical (88,742 / 1,135 / 490 / 645 / 24,645 / 322 / 630 / 4,576). Table numbering **did** change — map above. Decimalization treatment **unchanged**: same two dates, same two definitions, same LOWPRC split, same Panel C change-in-liquidity check, plus the new MV placebo |
| §7 item 7 "version risk — the RFS version must be fetched and the numbers re-checked before any magnitude goes into draft_v3" | **CLOSED.** Fetched and re-checked. Every §3 magnitude either matches to the digit or is flagged above. **§7 item 7 can be struck** |
| "the interaction-coefficient-in-probit issue … addressed by an Ai–Norton measure and an LPM, but only in text — the numbers are not shown" | **STILL OPEN.** Published fn 24 (p. 1467) still reports them only in text, now adding that the LPM interaction is "slightly stronger than in Table 6". No numbers |

### Still open after this pass

- **The Online Appendix (Tables OA1–OA17) is not in hand.** Everything attributed to it above comes
  from the body's description of it, not from the tables themselves. The two things worth fetching:
  **Table OA2** (the price-impact calibration our trading-cost side would use) and **Table OA15**
  (the 69 both-filers subsample, which is the cleanest version of the channel-choice result and the
  one closest to our partition). Marked UNCHECKED, not WRONG.
- §5's "no pre-trend or event-time plot for decimalization" — still true in print. Table OA3 gives a
  calendar-time analysis for **13G filings**, not for decimalization. The DiD-with-control-group
  criticism of the decimalization design survives the published version intact.
