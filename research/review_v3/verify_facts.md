# Verification — literature / novelty / empirics / facts (framework_v3 review)

Adversarial pass. Each claim was attacked against a primary source (raw page text,
paper text) or an executed recomputation. Verifier did not read the other referees'
reports.

## Tally

| verdict | n | ids |
|---|---|---|
| CONFIRMED | 18 | D-1, D-3, D-4, N-1, N-2, N-3, N-4, N-5, N-6, N-7, N-8, N-9, F-1, F-2, F-3, F-5, D-2a, D-2b |
| MISCITED | 2 | D-2c, D-2d |
| WRONG | 1 | F-4 (the "1994–2007?" guess for the published JF sample; local-file part confirmed) |
| UNCHECKED | 0 | — |

No claim was refuted on substance. The two MISCITED verdicts and the one WRONG
verdict are all locus/number slips inside claims whose economic point stands.

**Bonus refutation found while checking F-4** (not asked, but decision-relevant):
the memo's `~7% vs ~3%` run-up/jump row is attributed to "Collin-Dufresne–Fos
**2015**", but those are the **2012 NBER WP** numbers. The published JF 2015 paper
reports **~3% run-up and a ~2.5% two-day jump** on a 1994–2010 sample. See F-4.

## Table

| id | claim (short) | verdict | evidence (locus + quote / output) | note |
|---|---|---|---|---|
| D-1 | CAR medians by half-year; no break at 2024-02-05; pre/post 1.57/2.61; nrets=21; max 28.99 | **CONFIRMED** | Recomputed from `empirics/data/wrds_evtstudy_edate.csv` (2,285 rows). 22H1 4.38, 22H2 2.96, 23H1 1.69, 23H2 0.36, 24H1 1.01, 24H2 5.95, 25H1 2.80, 25H2 0.82 (%). pre n=1234 med=0.0157; post n=1051 med=0.0261. `nrets`==21 for 2,264/2,285. max car = 28.98810604 | Every number matches to 2 dp. 2024H1 (1.01) is indeed **below** 2023H1 (1.69) |
| D-2a | event parse rate .68/.66/.64/.000; `has_xml` all false | **CONFIRMED** | `fact2_parsed.jsonl`, 9,234 rows. By filing year: 2022 0.6813 (n=2319), 2023 0.6637 (2501), 2024 0.6401 (2184), 2025 0.0000 (2230). `has_xml==True` count = 0 in every year | |
| D-2b | full-universe delay: 2022 med 7.0 / 0.319 (n≈1400); 2023 7.0 / 0.357 (1530); 2024 5.0 / 0.706 (1231) | **CONFIRMED** | `np.busday_count`, filter 0≤delay≤60: 2022 n=1400 med=7.0 share≤5bd=0.3186; 2023 n=1530 med=7.0 0.3569; 2024 n=1231 med=5.0 0.7059 | Exact match |
| D-2c | filings dated 2024-02-05…2024-08-31 ≈ 1,381 | **MISCITED** | Executed: Feb 5–**Aug 31** = **1,226**; Feb 5–**Sep 29** = **1,381** | The 1,381 figure belongs to the Sep-29 window. Substance (a ~1.2–1.4k post-rule filing universe) stands; window label wrong |
| D-2d | `pct_of_class`: 6,189 parsed, med 9.55, 22.9% <5%, ≈448 rows exactly 2.6%, 307–347 exactly 0.0 | **MISCITED** | Executed: n=6189, median=9.55, share<5=0.2291, **`0.0` appears 307×** ✓. But **`2.6` appears 4×; the spike is at `2.59` with 438 rows** | Spike exists and is a parse pathology, but the value is 2.59 (438 rows), not 2.60 (448) |
| D-3 | 3-digit-% regex breaks; "100.0%"→0.0; `facts.py` busday w/o holidays; F1 rests on 188 filings | **CONFIRMED** | Executed against `empirics/parse_13d.py` `RE_PERCENT`: `"…ROW (11): 100.0%"` → **`00.0`**; `"…ROW (11): 100%"` → **`00`**; `"…ROW (11): 6.2%"` → `6.2` ✓. `empirics/facts.py:68` `np.busday_count(...)` — no `holidays=` arg. `empirics/output/fact1_summary.csv`: post n=90 parse_rate 0.64; pre n=98 parse_rate 0.68 → 188 | Regex is `([0-9]{1,2}(?:\.[0-9]+)?)\s*%` at parse_13d.py:105–106. Lazy `.*?` slides past the leading digit, so 3-digit percentages silently become 0.x |
| D-4 | post ≈301 events / 7 months; pre ≈688; sample ≈989 | **CONFIRMED** | Executed on `wrds_evtstudy_edate.csv`: post (2024-02-05…08-31) **n=301, 7 distinct months** (2024-02…2024-08); pre (2023-01-01…2024-02-04) **n=691**; total **992** | Pre/total are 691/992, not 688/989 — a 3-event slip, substance identical |
| N-1 | SSRN 6866499 Trivedi, Independent, 3 Jun 2026, "The Mandated Revelation Field…", DiD w/ 13G control, +0.35 p=0.007, nulls on lag/spread/illiquidity | **CONFIRMED** | SSRN page raw text: "Posted: 3 Jun 2026 Avaneendra Trivedi **Independent** Date Written: June 02, 2026"; "…finds that the rule moved the compliance share within five business days (plus 0.35, p = 0.007) but not the mean lag, the bid-ask spread, or the adverse-selection-proxy illiquidity" | Every element verbatim. **Context worth flagging:** the 13D DiD is one section of a much larger paper; the author's own novelty claim is "the conserved cross-statute aggregation and its deterministic drain calendar, **not** the existence of date-localized abnormal returns" |
| N-2 | Polk/Buchheit/Riley/Stone, SSRN 4596959 (Nov 2023), JFRC 32(4) 2024, delay abnormal returns + 10→5-day projection | **CONFIRMED** | SSRN 4596959: "Posted: 7 Nov 2023 … Ryan Polk Clemson … Steve Buchheit … Mark Riley … Mary S. Stone"; abstract: "how the 5-day deadline … will affect abnormal returns". Emerald: JFRC **Vol 32 No 4, pp. 516–538**, doi 10.1108/JFRC-01-2024-0016 | Published title is "Shrinking the 13D disclosure window will benefit **non-activist** investors" (SSRN's working title says "the investing public") |
| N-3 | Corum (Cornell), "The Stick or the Carrot?…", SSRN 4319599, rev. Apr 2025, activism+liquidity+regulation, no takeover premium | **CONFIRMED** | SSRN 4319599: "Last revised: 29 Apr 2025 Adrian Aycan Corum Cornell University – Johnson"; "I study a model of activist short-termism, where the activist can sell his stake in the target before the impact of his intervention is realized" | Abstract + keywords (Blockholder, Liquidity, Incentives, Myopia, Short-Termism) contain no takeover/premium object. Confirms the memo's non-overlap |
| N-4 | Bishop/Fos/Jiang/Partnoy, "Antitrust, Anti-Activism", SSRN 6061814 (2026), HSR toehold deters targeting pre-13D | **CONFIRMED** | SSRN 6061814, Posted 13 Jan 2026: "activists are less likely to target firms when a 'toehold' position would trigger HSR disclosure requirements prior to a Schedule 13D filing" | Bishop is Duke Law (not Berkeley — Berkeley is the RP series number); Jiang is Emory |
| N-5 | Kyle & Vila (1991), RAND JE 22(1):54–71, noise-trading camouflage enables profitable takeovers | **CONFIRMED** | RePEc/EconPapers `rje:randje:v:22:y:1991:i:spring:p:54-71`: noise trading "provides camouflage" letting a large outsider buy at favorable prices "so that takeovers become profitable" | Bibliographic + abstract both check out |
| N-6 | Mello & Repullo (2004), FRL 1(1):2–10 | **CONFIRMED** | RePEc `eee:finlet:v:1:y:2004:i:1:p:2-10`, March 2004, "Shareholder activism is non-monotonic in market liquidity" | Gist also confirmed: sign flips on whether the block constraint binds |
| N-7 | Burkart–Lee text: "comprehensively studied by Back et al. (2018)" right after the toehold sentence | **CONFIRMED** | `research/txt/burkart_lee_rfs2022.txt` l.1113–1116: "we do not endogenize the acquisition of the toehold in anonymous, predisclosure markets. This latter problem … has been comprehensively studied by Back et al. (2018)" | Exact, contiguous |
| N-8 | `bibliography.bib` has no Burkart–Lee (2022); Ben-David et al. JF 2026 has FOUR authors incl. Ruidi Huang | **CONFIRMED** | `grep -i burkart bibliography.bib` → 2 lines, both from the single entry `BurkartGrombPanunzi1998` (JPE 1998). No Burkart–Lee entry. Wiley DOI 10.1111/jofi.70038: "ITZHAK BEN-DAVID, UTPAL BHATTACHARYA, RUIDI HUANG, STACEY JACOBSEN, First published: 07 April 2026" | Huang is SMU. `bibliography.bib` also has no Ben-David entry at all |
| N-9 | 2023 amendments also (i) 13D **amendment** deadline 2 business days, (ii) EDGAR cut-off → 10 p.m. ET, both eff. Feb 5 2024 | **CONFIRMED** | SEC press release 2023-219 (raw page text): "shorten the deadline for initial Schedule 13D filings from 10 days to five business days and **require that Schedule 13D amendments be filed within two business days**". Skadden 2024-02 memo: "The EDGAR filing cut-off time will be extended from 5:30 p.m. ET to 10 p.m. ET"; "amendments are effective as of February 5, 2024" | The 10 p.m. change is *not* in the SEC press release; it is in the adopting release / Reg S-T. Two independent law-firm sources (Skadden, Foley Hoag) carry it |
| F-1 | C&L takeover effect is "**7.7 percent**" (relative), premium is "13.7 percent (5.2 percentage points)"; memo's "+7.7pp" unsupported | **CONFIRMED** | `research/txt/celentano_levine_2025.txt` l.71–72: "increasing the probability of takeover by **7.7 percent** when a campaign is launched"; l.77–78: "Bid premia are 13.7 percent (5.2 percentage points) lower" | The paper itself glosses it as "about 7 percent of deals … are marginal to activist intervention" — a *share of deals*, not a pp lift. `framework_v3.qmd:329` prints `$+7.7$pp` → **wrong unit** |
| F-2 | BGS 2017: >1/3 involved in a bid within 2 yrs (22% risk-arb-excluded); **no** "70% within 2 years" | **CONFIRMED** | JFE accepted MS (WRAP 133448) l.97–98: "**Over one-third** of firms targeted by hedge fund activists during 2000–2012 are involved in a takeover bid before or within two years of activist involvement"; l.105: "the probability of an activism merger is **22%**". `grep "70%"` → 1 hit, a table cell "16.70%*" | `framework_v3.qmd:239` "Boyson et al.'s $70\%$ within 2 years" has **no support in the paper** — it is roughly triple the actual statistic |
| F-3 | Norli 0.33→0.73 is footnote 12 on the **baseline probit (Table 3)**, not the IV probit | **CONFIRMED** | `tmp_read/norli2015.txt` l.567 (fn 12): "The likelihood increases from 0.33 to 0.73 percent points for the 10th and the 90th percentile respectively." It hangs off l.565 "the results presented in **Table 3**…". The IV probit is introduced at l.586–592 ("we also present results from an instrumental variable probit regression"), Table 4 at l.579 | `framework_v3.qmd:325` labels the number "(IV)" → **wrong specification** |
| F-4 | local txt = NBER WP 18452, 2001–2010, run-up ~7% over 60d→1d, jump ~3%; JF version sample 1994–2007? | **WRONG** (on the JF sample guess) / local part CONFIRMED | Local: `tmp_read/cdf_fos_jf2015.txt` header = "NBER WORKING PAPER SERIES … Working Paper 18452 … October 2012"; l.431: "Panel A includes data from the **2001-2010** sample period. There is a run-up of about **7%** between sixty days to one day prior to the filing day. The two-day jump … is around **3%**". **Published JF 70(4) (doi 10.1111/jofi.12260)**: "we identify 19,026 Schedule 13D filings from **1994 to 2010**"; "there is a run-up of about **3%** from 60 days to one day prior to the filing date. The two-day jump … is around **2.5%**" | Sample is 1994–**2010**, not 1994–2007. And the substantive kicker: the memo's `~7% vs ~3%` row cites CDF-Fos **2015** but reproduces the **2012 WP** numbers. Published values are 3% / 2.5% (drift 9%, not 13%) |
| F-5 | AFS: 13D CAR 6.34%, treatment share 75.2%, no takeover-premium estimate | **CONFIRMED** | `research/txt/afs_jfe2022.txt` l.110: "the average announcement return is **6.34%** for Schedule 13D filings but only 0.59% for Schedule 13G"; l.1177–1180: value creation 5.53−0.77 = 4.77% and stock picking 0.77% "represent **75.2%** and 12.2% … of the predicted announcement return of 6.34%". `grep -ic premium` → 7 hits, all either "illiquidity premium" (l.1028, Amihud) or the control variable "Market premium" in tables | The 75.2% is the treatment (value-creation) share of the announcement return in the AFS decomposition — the memo's label is fair. No takeover premium anywhere |

## Executed data checks (key output)

```
# D-1  wrds_evtstudy_edate.csv  (2285 rows; evtdate 2022-01-04 .. 2025-12-15)
          median  count  median_pct
2022H1  0.043767    277        4.38
2022H2  0.029631    266        2.96
2023H1  0.016890    304        1.69
2023H2  0.003581    326        0.36
2024H1  0.010118    284        1.01     <-- BELOW 2023H1; no break at 2024-02-05
2024H2  0.059541    243        5.95
2025H1  0.028016    296        2.80
2025H2  0.008217    284        0.82
pre n=1234 med=0.0157   post n=1051 med=0.0261
nrets: 21 -> 2264 rows (of 2285)      max car = 28.98810604
```

```
# D-2  fact2_parsed.jsonl (9234 rows; forms: SC 13D 6852 / SCHEDULE 13D 2382)
(a)        n  event_rate  has_xml==True
2022  2319.0    0.681328    0
2023  2501.0    0.663735    0
2024  2184.0    0.640110    0
2025  2230.0    0.000000    0
(b) busday delay, 0<=d<=60, by FILING year
         n  median  share_le5
2022  1400     7.0     0.3186
2023  1530     7.0     0.3569
2024  1231     5.0     0.7059
(c) filed 2024-02-05..2024-08-31 -> 1226      filed 2024-02-05..2024-09-29 -> 1381
(d) pct_of_class parsed n=6189  median=9.55  share<5=0.2291
    top values: 2.59 x438 | 0.00 x307 | 5.00 x70 | 9.90 x64 | 5.10 x52
    exactly 2.60 -> 4 rows      exactly 0.00 -> 307 rows
```

```
# D-3  parse_13d.RE_PERCENT executed
'(11): 100.0%' -> 00.0     # 3-digit % silently becomes 0.0
'W (11): 100%'  -> 00
'W (11): 6.2%'  -> 6.2     # 1-2 digit % fine
'(11)  12.59%'  -> 12.59
empirics/facts.py:68  np.busday_count(...)   # no holidays= argument
empirics/output/fact1_summary.csv: post n=90 (0.64), pre n=98 (0.68)  -> 188 filings
```

```
# D-4  memo windows on wrds_evtstudy_edate.csv
post 2024-02-05..2024-08-31: n=301, 7 months  [2024-02 .. 2024-08]
pre  2023-01-01..2024-02-04: n=691
total estimation sample:     992
```

## Access notes

- **SSRN**: `curl` and `WebFetch` both get **HTTP 403 "Content Blocked"** (Imperva),
  including the `api.ssrn.com` route (Cloudflare "Just a moment…"). The ego-browser
  task space **does** get through, but only with `settle: 8–10` and a following
  `wait(6)` — the first attempt with a short settle returned `chrome-error://`.
  All four SSRN abstracts were read as raw page text this way, not from search snippets.
- **google.com** is unreachable from the ego-browser task space (`chrome-error://`);
  `example.com`, Wiley, SEC and Emerald are all fine. `WebSearch` was used only to
  *locate* URLs, never as the evidence of record — every CONFIRMED verdict above rests
  on raw page text or an executed run.
- **sec.gov** press release read via the browser (as instructed); the fact-sheet PDF
  rendered blank in the text layer, so the 10 p.m. cut-off was verified from two
  law-firm memos (Skadden, Foley Hoag) instead of the SEC release itself.
- **Boyson–Gantchev–Shivdasani**: no local copy in the repo. Author sites 404; the
  JFE accepted manuscript was pulled from the Warwick repository
  (`wrap.warwick.ac.uk/id/eprint/133448`) and grepped directly.
- Nothing outside `research/review_v3/verify_facts.md` was modified.
