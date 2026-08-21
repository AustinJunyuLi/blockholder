# Zeng, Jean (Jieyin) (2026) — "Do managers learn about their firm's ownership changes before public disclosure?"

**Venue / status:** *Review of Accounting Studies* (2026) 31:1301–1341, https://doi.org/10.1007/s11142-026-09958-z. Received 24 Apr 2023, accepted 31 Mar 2026, published online 8 May 2026. Sole author, National University of Singapore. Based on the author's May 2020 Berkeley (Haas) dissertation; earlier title "Do Managers Exploit Private Information about Their Firm's Investor Base?" (p. 1339).
**Full text from:** `research/txt_extracts/zeng_2026_ras.txt` (extracted from `research/txt_extracts/zeng_2026_ras.pdf`) · **Reader:** opus · **Read:** full text, pp. 1301–1341 (41 printed pages; PDF page *i* = printed page 1300+*i*).
**Page numbering:** printed journal pages of the published RAS version (1301–1341), as they appear in the running heads.
**Internet Appendix — READ 2026-08-21.** `research/txt_extracts/zeng_2026_ras_internet_appendix.pdf` / `.txt` (Springer supplementary file linked from the article landing page; 13 pp of content + 1 blank, Tables IA.1–IA.9 and Figures IA.1–IA.2, all of them). **Page numbering for IA items: PDF page index of the supplementary file** — only its p. 1 carries a printed number, so every other page is cited as "IA PDF p. *n*". Everything the IA settles is in **§9b**; the body-text-only caveats below have been updated accordingly.
**Type:** empirical (event-window / pooled event-day OLS) **Role for us:** antecedent + measurement (institutional plumbing of the trigger-date → filing-date window); **not** a competitor.

## 1. Question

Do corporate insiders find out that a blockholder is accumulating their stock *before* the Schedule 13D/13G that discloses it, and do they trade on that knowledge? The paper is framed as a *managerial-learning* study: prior work asks whether managers learn from prices; Zeng asks what specific content they learn (ownership changes) and through which channel (stock-surveillance vendors plus direct investor-relations contact), using insiders' own Form 4 trades as the observable trace (pp. 1302–1303). The 13D/13G setting is chosen because the trigger date (5% crossing) and the filing date bracket a short, dated, legally-created window of asymmetric information (p. 1309).

## 2. Model / data and method

**Design.** No model. Pooled event-day OLS comparing daily insider trading in a *pre-disclosure* window against a *control period* built from the same firm's trading days 3–7 months before and 3–7 months after the filing date (p. 1318). Two pre-disclosure windows: (TD−20, FD−1) and (TD−5, FD−1), where TD = trigger date (blockholder crosses 5%) and FD = 13D/13G filing date (p. 1320). Firm and year fixed effects; heteroskedasticity-robust *t*-statistics. No difference-in-differences on any disclosure rule; the only DiD in the paper is a legal-risk placebo (SDNY × post-Bharara, Table 8 col. 3/6, p. 1331).

**Data.** EDGAR 13Ds and 13Gs 2002–2022; Thomson Reuters Insider (Form 4, officers and directors, open-market P and S only); CRSP; Compustat Quarterly; Capital IQ investor conferences (from 2008); Wei Jiang's hedge-fund-activist list + HFR + 13F.

**Screens.** 13Ds: 40,650 → 3,758 after nine mechanical screens → **2,689** after hand review for open-market acquisition, by 1,071 unique filers on 2,052 target firms (pp. 1311–1312). 13Gs: 141,266 → 43,693 → minus 28,050 exempt filers, 1,437 private-placement-linked, 324 index funds → **13,882**, by 3,208 filers on 5,754 targets (pp. 1316–1317).

**Window screen (load-bearing for us).** Only 13Ds filed **1 to 13 calendar days** after TD are kept; late filings are dropped because "the insiders cannot predict the filing date," and 13 days is chosen because filings cluster in (t+9, t+13) (p. 1312 fn. 13). Median TD→FD gap in sample: **nine calendar days** (p. 1309).

**Outcome variables.** Daily insider purchases / sales / net purchases as fraction of shares outstanding in basis points, non-zero values winsorized at 1%. Controls: daily market-adjusted return, daily abnormal volume, past-30-day return and volume, size, BTM, Amihud illiquidity, volatility, past insider purchases/sales.

**Mechanism proxies.** (i) `Communicated` — 13D filer voluntarily discloses pre-filing contact with management (21% of filers, p. 1325); (ii) `Near` — Great-Circle distance filer-to-target below sample median (2,330 filings with zip codes); (iii) `IR Investment` — count of investor conferences management attended in the prior year (1,735 filings, Capital IQ from 2008).

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where (page / table) |
|---|---|---|---|
| R1 | 13D disclosure moves price: +2.8% run-up TD→FD, +1.9% on FD and the next five days, **+6.1% total by FD+20**; 13G: +0.9%, +0.4%, **+1.7%**; no reversal over six months | ESTIMATED — **all four headline numbers now reproduced off Fig. IA.1 itself** (§9b): 13D TD = 0.73%, FD = 3.47% (diff 2.74), day +20 = 6.06%; 13G TD = 0.63%, FD = 1.61% (diff 0.98), day +18 = 1.68%. **Still no SE/t anywhere and no confidence band on the figure.** *(verifier: the intro, p. 1303, instead states "6%" for 13Ds and 1.7% for 13Gs over a (t−10, t+10) window — a different window from the 6.1% figure, so quote the window whenever you use the number.)* | p. 1309–1310; Fig. IA.1, IA PDF p. 1 |
| R2 | Insiders buy 0.040 bp/day more over (TD−5, TD−1) = +67.8%, and 0.091 bp/day more over (TD, FD−1) = +154.5% vs control; sales fall 0.034 bp/day (−25.4%) over (TD−20, TD−6) | ESTIMATED — **significance now checked in IA Table IA.1**: t = 2.884 (p = 0.004), t = 6.657 (p = 0.000), t = −2.967 (p = 0.003). Control means 0.059 bp (purchases) / 0.135 bp (sales) confirmed. Nothing before TD−5 is significant (§9b) | p. 1319–1320; Table IA.1, IA PDF p. 3 |
| R3 | Cumulative insider purchases by FD are 45% above control; cumulative sales 8% below | ESTIMATED — figure readings described in body text; no SE | p. 1319 (Figs. 2–3, printed in the article) |
| R4 | Pre-disclosure dummy: purchases +0.017 (t=1.93, *), sales −0.016 (t=−1.66, *), net +0.032 (t=2.75, ***) on (TD−20, FD−1); on (TD−5, FD−1): purchases +0.057 (t=3.33, ***), sales +0.002 (t=0.09), net +0.056 (t=2.48, **). N = 482,641 / 443,418 | ESTIMATED | p. 1321, Table 2 |
| R5 | Insider purchases **peak precisely on the trigger date** — the day the blockholder crosses 5% | ESTIMATED (figure-based; the peak itself is read off Fig. 2, not a coefficient) | pp. 1304, 1319 |
| R6 | Contemporaneous return and volume load positively (Daily Returns 0.337, t=3.17), i.e. insiders do learn from prices — but the pre-disclosure effect survives, so prices/volumes do not fully explain it | ESTIMATED | p. 1321–1322, Table 2 |
| R7 | Post-large-trade test (611 non-overlapping blockholder trades >20% of daily volume): insider purchases +0.335 (t=3.16), net +0.344 (t=3.03) in the five days *after* vs five days *before*; rules out reverse and joint causality | ESTIMATED | p. 1324, Table 3 |
| R8 | Cross-section: `Communicated` +0.089 (t=2.86, N=2,689); `Near` +0.077 (t=1.94, N=2,330); `IR Investment` +0.068 (t=2.14, N=1,735) | ESTIMATED | p. 1326, Table 4 |
| R9 | 13Gs replicate: purchases +0.074 (t=8.01), sales +0.009 (t=1.11, ns), net +0.064 (t=5.24) on (TD−5, FD−1); N = 2,206,048 | ESTIMATED | p. 1328, Table 5 |
| R10 | By role: 13D executives +0.021 (t=2.63); **13D independent directors +0.008 (t=0.78, insignificant)**; 13G executives +0.025 (t=3.50), 13G independent directors +0.040 (t=3.13). Text claims "both … adjust their trading" | ESTIMATED — the text's "both" claim is ASSERTED for the 13D independent-director cell | Table 6 on p. 1329; the "both" sentence on p. 1328. N = 482,641 (13D cols), 2,206,048 (13G cols) |
| R11 | By investor type: 13D institutional +0.043 (t=3.40); **13D non-institutional +0.004 (t=0.14, insignificant)**; 13G non-institutional +0.129 (t=5.28), institutional +0.032 (t=2.34) | ESTIMATED — the text's "both" claim is ASSERTED for the 13D non-institutional cell | Table 7 on p. 1330; the "both" sentence on p. 1329. N = 143,357 / 339,284 / 747,662 / 1,458,386 |
| R12 | Enforcement intensity does not deter: SEC Budget 0.053 (t=0.77) 13D / **+0.115\*\* (t=2.43) 13G**; SEC Staff **+0.067\* (t=1.67) 13D** / **+0.071\*\* (t=2.44) 13G**; SDNY×PostBharara −0.113 (t=−1.04) / −0.098 (t=−0.35) | ESTIMATED — but the *interpretation* ("no evidence that insider trading declines") is ASSERTED; **three of the four enforcement-intensity coefficients are positive and significant** (two at 5%, SEC Staff 13D at 10%) *(verifier: card previously said "two of four"; the 13D SEC-Staff coefficient carries one star)* | Table 8 on p. 1331 |
| R13 | Robustness: results hold by firm size, pre/post-2010, filing FE, pre-only control window, macro controls, and on the 2,150 13Ds with no explicit activism plan | ESTIMATED — **all six tables (IA.2–IA.7) now read**. Five of the six replicate cleanly (filing FE, pre-only control, macro controls, nonconfrontational subsample, both period halves). **The size split (IA.2) does not say what the body says it says — see §9b(b) and §7.2** | p. 1322; Tables IA.2–IA.7, IA PDF pp. 4–10 |
| R14 | Pre-disclosure insider net purchases predict higher revenue growth and ROA over the 120 trading days *following the disclosure* | ESTIMATED — **IA Table IA.9 now read**. Revenue holds in all four quarters (13D 0.007\*\* / 0.010\*\*\* / 0.011\*\*\* / 0.006\*\*). **ROA does not**: for 13Ds only q and q+2 are significant (0.004\*\*, 0.000, 0.006\*\*, 0.001), so "and ROA" is a half-claim. Design is a filing-level cross-section (N ≈ 2,300) with industry × year FE, not a causal estimate; and it spans quarter q *through* q+3, not the "120 trading days following" | p. 1310 fn. 11; Table IA.9, IA PDF pp. 12–13 |
| R15 | Blockholder accumulation path: mean ownership 3.0% at TD−20 → 4.6% at TD−1 → >1% bought on TD itself → 6.9% by FD; 4.02% already held at TD−5. Panel B also: mean (median) filer buys 4.2% (3.1%) of shares over 60 days, trades on 15 (13) days = 35.7% (31%) of trading days, is 29.8% (21.6%) of daily volume when trading, and makes 6.2 (4) large trades | ESTIMATED (means from hand-collected Item 5(c); the path itself is plotted in IA Fig. IA.2 and only *described* in the body) | Panel B stats pp. 1316–1318; path p. 1319; **the 4.02% figure is on pp. 1305 and 1323, not p. 1318** *(page corrected by verifier)* |

## 4. Institutional facts used

- **Threshold margin.** 5% beneficial ownership triggers 13D (intent to influence) or 13G (passive) — used as the *level* and never varied (pp. 1303, 1309).
- **Window margin — the pre-2024 regime only.** Rule 13d-1(a): file within **10 days** of crossing 5% (p. 1303); footnote 13 says "10 calendar days" (p. 1312). Sample median TD→FD gap = 9 calendar days; filings cluster at (t+9, t+13) (pp. 1309, 1312).
- **Late filing is common and unenforced.** "a significant number of 13Ds were filed late" (p. 1312 fn. 13); Item 5(c) requires all 13D filers to report their trades over the prior 60 calendar days, but "due to lack of enforcement, only 2,327 13D filers actually do so" out of 2,689 (p. 1314 fn. 14).
- **Exempt 13G filers** need not file within 10 days and may file up to 45 days after calendar year-end; excluded as informationless (p. 1317).
- **Item 4 (Purpose of Transaction) taxonomy:** 36.6% investment-only, 43.3% intend/have communicated with management, 20.0% state explicit activism goals; 66% of 13Ds filed by hedge funds (p. 1315).
- **Form 4** insider reporting within two business days under §16a (p. 1318). **13F** 45 calendar days after quarter end (p. 1309). **T+3** settlement, the basis of DTCC custodian reports (p. 1308 fn. 9).
- **Stock-surveillance industry.** Grew out of 1980s takeover battles / proxy solicitation; vendors named (Ipreo, CapitalBridge, Q4 Web Systems, Ilios Partners); they buy DTCC daily custodian-position reports, which only the issuer can authorise (p. 1308).
- **NIRI/CFO surveys (Appendix 1, p. 1332).** 94% of firms monitor their investor base; 57% subscribe to a surveillance service; in 2015, only 20% of IR officers first learned of an activist from an SEC filing, 49% from direct contact by the investor, 20% from a surveillance firm. A 2014 Rivel survey: 64% use a vendor (83% large-cap, 44% small-cap) (p. 1307 fn. 7).
- **What the 13D announcement return is made of (added by verifier, p. 1303 fn. 4).** Albuquerque et al. (2022) estimate structurally that **74.8%** of the 13D announcement return is expected value creation through intervention and **13.4%** is stock-picking; Edmans, Fang and Zur (2013) show 13G filers govern via exit threats. This is the decomposition our premium story has to live with, and Zeng imports it wholesale.
- **Concurrent papers she distinguishes herself from (added by verifier, pp. 1306–1307).** Chabakauri et al. (2022): insiders detect activist trades ahead of the public by **filtering aggregate order flow**, and **retain ownership to defend control rights**. Duong et al. (2025): a smaller hedge-fund-activist sample, insiders trade ahead for personal gain. Zeng's stated difference is the *channel* (IR/surveillance, not order-flow filtering) and the *frame* (learning, not control or profit).
- **Large-trade cutoff robustness (added by verifier, p. 1323 fn.).** The >20% of daily volume definition is robust to 10% and 30% cutoffs.
- **Enforcement proxies:** SEC annual budget authority (constant 2011 $) and authorised FTE headcount from SEC Annual Reports / Congressional Budget Justifications; Preet Bharara SDNY tenure Aug 2009–Jun 2014 (pp. 1330–1331).

## 5. Referee-facing strengths / weaknesses

**Strengths**
- The trigger date is a hand-verifiable, legally-dated, *private* event; the paper exploits that TD is unknown to the market until FD, which makes the "purchases peak exactly on TD" fact striking rather than mechanical.
- The post-large-trade design (Table 3) is a genuine within-window ordering test that discriminates the paper's story from reverse and joint causality — not just a robustness table.
- Hand-collection of Item 5(c) trade schedules for 2,327 filings gives the blockholder's daily accumulation path, which almost no 13D paper has. This is the single most reusable asset in the paper for us.
- Three independent mechanism proxies (disclosed communication, geography, IR conference count) all point the same way.
- Extends to 13Gs and to passive filers, and to the 2,150 filings with no stated activism plan — so the result is about *ownership-change detection*, not about activism conflict.

**Weaknesses / open flanks**
- **The control-period design is not identification.** `Pre_disclosure` compares event-window days to same-firm days 3–7 months away. Anything that makes a firm attractive to a blockholder *and* to its own insiders in the same fortnight (a fresh cheap valuation, a stalled sale process) loads on the dummy. The paper's defence is timing (R7), not exogeneity.
- **Two "both groups" claims are not supported by their own tables.** *(verifier: both confirmed against the printed tables.)* Independent directors on 13Ds: 0.008, t=0.78, no stars (Table 6 col. 2, p. 1329) against the text's "both executives and independent directors adjust their trading" (p. 1328). Non-institutional filers on 13Ds: 0.004, t=0.14, no stars (Table 7 col. 1, p. 1330) against "abnormal insider purchases occur in both institutional and non-institutional filings" (p. 1329).
- **Table 8 arguably cuts against the paper's own reading.** SEC Budget and SEC Staff enter *positively and significantly* in the 13G columns. The author reads this as "no deterrence"; a referee can read it as the enforcement proxies picking up a time trend, which then also indicts the year fixed effects elsewhere.
- **Selection on the window itself.** Dropping every 13D filed later than 13 days after TD removes exactly the filers with the most to hide, and it is the sample cut most exposed to the 2024 window change (see §6).
- **A third "both groups" overclaim, now confirmed in the Internet Appendix.** The body says the size split shows learning "occurs in both large and small firms" (p. 1322); in IA Table IA.2 **neither small-firm coefficient is significant** (t = 1.27 and t = 1.64) and no test of the difference is printed anywhere. Same pattern as R10 and R11 — this is a habit, not an accident, and a referee who pulls the IA will find three instances.
- Typographical slip on p. 1331: "As reported in Table 8, 8 find no evidence…".
- Amihud illiquidity is a nuisance control, and its coefficient wanders in sign across tables (−0.025** in Table 2 col. 3, +0.154*** in Table 8 col. 4) with no discussion.

## 6. What they do NOT do (scope boundary)

**Object.** The dependent variable is always **daily insider (officer/director) trading in basis points of shares outstanding**. The *price reaction* to 13D/13G is used only as background motivation and as a reason the setting is interesting (p. 1309). No control outcome is ever an outcome variable.

**Grep counts over the full text (pp. 1301–1341), which the positioning stage asked for:**

| Term | Count | Where / what it is |
|---|---|---|
| `illiquidity` | **11** *(corrected by verifier; card said 10)* | 2 in the Appendix 4 variable definition (p. 1337) + 1 summary-stats row (Table 1 Panel C, p. 1317) + 1 in the method text (p. 1320) + 7 control-variable rows in Tables 2, 4 (×2), 5, 6, 7, 8 |
| `liquidity` (standalone, not "illiquidity") | 4 | 2 in the body, both p. 1318, meaning insiders' *personal* "liquidity needs or diversification"; 2 in the reference list (Agarwal et al. 2015; Edmans–Fang–Zur 2013) |
| `Amihud` | 1 | Appendix 4 variable definition, p. 1337 |
| `bid-ask`, `spread`, `market depth`, `turnover` | 0 each | absent |
| `order flow` | **1** *(corrected by verifier; card said 0)* | p. 1307, summarising Chabakauri et al. (2022): "insiders filter out activist trades from aggregate order flows due to their private knowledge about firm fundamentals". Her own design has no order-flow variable, but the *concept* is engaged once, and against the one theory paper closest to us |
| `noise` | 1 | p. 1302, "stock prices, which aggregate information and contain noise" — a literature remark, not a construct |
| `takeover` | 2 | p. 1308 ("corporate takeover battles of the 1980s", industry history) and one reference title (Greenwood–Schor, p. 1340) |
| `premium` | **0** | never appears |
| `bidder`, `tender offer`, `proxy fight`, `proxy contest`, `board seat` | 0 each | absent |
| `campaign` | 2 | p. 1310 (wolf-packing definition) and p. 1322 ("confrontational activist campaigns") — never an outcome |
| `control contest` | 1 | p. 1307, one sentence on why firms monitor |
| `control right` | 4 *(added by verifier)* | pp. 1305, 1306, 1322, 1327 — every occurrence is a motive she names and then **explicitly disclaims** ("rather than focusing on insiders' profit motives or control concerns", p. 1307), or a pointer to Chabakauri et al. (2022) |
| `hostile` | 1 | p. 1303, "preparing for potential activist threats or hostile bids" — a motive listed, then dropped |
| `activis*` | 33 | filer *type* and literature, never a measured outcome |

So: **market liquidity is present only as an Amihud control** (never a treatment, never an interaction, never a split); **no control outcome exists anywhere in the paper.**

*(added by verifier)* Two qualifications a referee will make, both stand:
- She **does** run a size split (median market cap, IA Table IA.2, described p. 1322), so "nobody has looked at anything liquidity-adjacent" is too strong. But now that the table has been read (§9b), the body's gloss is only half right: **the direction reverses by window.** On the long window (TD−20, FD−1) larger firms lead, 0.032\*\* vs 0.026 (ns); on the **short window (TD−5, FD−1) the smaller-firm point estimate is the bigger one, 0.066 vs 0.041\***, and it is insignificant only because its standard error is larger (t = 1.64). No test of the difference is printed. The split is a nuisance-robustness table, not a liquidity test, and it does **not** deliver a clean null against a thin-stock story.
- Control outcomes are absent from **her** design, but she names a concurrent paper where control defence *is* the object: Chabakauri et al. (2022) "show that corporate insiders detect activist trades ahead of the public and **retain ownership to defend control rights**" (p. 1306). Duong et al. (2025) is the other concurrent paper (hedge-fund activists, personal-gain framing). Neither is in this file.

**Margin.** The 5% threshold and the 10-day window are used as **LEVEL / background plumbing** — they define the event dates and the sample screen. Neither is varied, interacted, or shifted. There is **no comparison across thresholds** (no UK 3%, no 5% vs 10%) and **no comparison across window lengths.**

**Feb-2024 acceleration: absent.** The sample ends in 2022; SEC Release 33-11253 (13D window 10 → 5 business days from 2024-02-05) is never mentioned. Every "2024" hit in the file is a citation year or an accessed-on date (pp. 1331, 1340). The word "amend" appears once, and refers to 13D/A amendments dropped in screening (p. 1312), not to the rule amendment.

**Identification.** No policy DiD on the disclosure rule; no structural model; no instrument. Within-firm event-window vs control-window comparison, plus one within-window ordering test (Table 3) and one enforcement placebo DiD (SDNY × Bharara, Table 8 cols. 3 and 6). The author's own limitation statements are quoted below (Q7, Q10, Q14).

**Self-declared limits.** She does not attempt to separate insiders' motives ("this study does not aim to disentangle insiders' motives", p. 1322), cannot observe surveillance-vendor purchases directly ("While I cannot directly observe firms' use of stock-surveillance services", p. 1305), acknowledges the enforcement proxies are noisy (p. 1331), and cannot recover 13G filers' pre-filing trade schedules at all (p. 1317).

## 7. Implications for our position

**Where it sits.** Object = *insider (officer/director) trading in the pre-disclosure window*. Margin = *neither* — the 5% threshold and the 10-day window are fixed scenery, used to date the event. Identification = *within-firm event-window vs matched control-window OLS*, 2002–2022. It occupies none of our three coordinates: not liquidity as a driver, not a rule margin as a treatment, not a control outcome. **It is not a competitor and does not consume our whitespace.**

**What it hands us — the anchor gets stronger, not weaker.** Zeng documents, with hand-collected filer trade schedules, that the trigger-to-filing window is *already leaky*: the price runs up 2.8% before the filing (p. 1309), the target's own insiders buy through it, and the leakage begins on the day the 5% line is crossed. That is direct evidence that the **window margin** — not the threshold level — is where information actually moves. Our claim that shortening 10 → 5 business days is an economically live change gains an antecedent: there is measurably something in that window to compress.

**What it constrains.** Three things.

1. **The pooled state is not clean.** Our partition assumes the market is in the *pooled* state until the flag. Zeng shows a specific set of agents — the target's own managers, via surveillance vendors and IR contact — are partially flagged before the filing, and that they trade on it. If we want the partition to be the market's information structure, we should say explicitly that our "pooled" state is pooled *for the price-setting market*, and cite Zeng for why insiders are a documented exception. A referee who knows this paper will ask.

2. **Liquidity is where Zeng has nothing, and the one thing that looked like a pre-emption does not pre-empt us.** Two body-text uses of the word, both about insiders' personal liquidity needs; Amihud only as a nuisance control (§6 table); the Internet Appendix adds **no** liquidity content — the standalone word "liquidity" appears **zero** times in all 13 IA pages, and `Illiquidity` appears six times, once as a control row in each of Tables IA.2–IA.7 (§9b). *(rewritten 2026-08-21 after reading IA.2.)* The size split we were worried about is **not** the clean null the body's one-liner implies. On the window that matters most for us — **(TD−5, FD−1)**, the one whose length the Feb-2024 rule compresses — the **smaller-firm coefficient is 61% larger** than the larger-firm one (0.066 vs 0.041\*), and it fails significance only on its standard error (t = 1.64 vs 1.95). IA.2 prints **no test of the difference**, so the body's "the difference is not statistically significant" is an assertion, not a result. So the honest sentence is: *the only liquidity-adjacent cut in the paper is a two-way median-market-cap split on a robustness table; it does not test liquidity, it reports no difference test, and in the short window its point estimate runs with, not against, a thin-stock story.* Market cap is a poor κ proxy anyway (her median target is a $186m firm with mean Amihud 0.384, Table 1 Panel C, p. 1317, so the whole sample is thin). Nobody in this paper asks whether the pre-filing leakage is larger in thin stocks *conditional on size* — even though her own mechanism (blockholders trading 29.8% of daily volume on trading days, 6.2 large trades of >20% of volume each, p. 1316 Table 1 Panel B; and **1.34% of shares outstanding traded on the trigger day alone**, Fig. IA.2, §9b) is *mechanically* a κ story: in a thin stock the blockholder's footprint is bigger, so detection is easier. A κ-interaction on her own design is directly available and unclaimed.

   **One honest caveat that cuts the other way, and it is new from the IA.** The `Illiquidity` control loads **negatively and significantly** on daily net insider purchases in the smaller-firm subsample (−0.025\*, −0.033\*\*) and is insignificant in the larger-firm one (0.076, 0.055) — and it is most negative of all in the nonconfrontational subsample (−0.046\*\*\*, −0.053\*\*\*, IA.7). Read naively that says insiders net-buy *less* in more illiquid stocks. It is a level control, not an interaction with `Pre_disclosure`, so it does **not** test whether the *leak* is bigger in thin stocks — but it is the one number in the paper a referee can wave at a κ story, and we should pre-empt it by running the interaction ourselves.

3. **Empirical craft we should copy, and one trap.** Copy: the trigger-date extraction script from the 13D cover page, the Item 5(c) 60-day trade-schedule hand-collection, and the control-period construction (same firm, ±3–7 months). The trap: her sample screen keeps only 13Ds filed **1–13 calendar days** after TD (p. 1312 fn. 13). Under the post-Feb-2024 five-business-day rule that screen is no longer neutral — the filing-date cluster moves left, so a naive "1–13 day" filter applied across 2024-02-05 changes the composition of the sample on both sides of the cut-off. Our referee checklist's "EDGAR cut-off" line should name this explicitly.

**Net.** Use Zeng as an **antecedent for the window margin and a measurement template**, cite her for the fact that the pre-filing window carries information and that firms actively buy the technology to detect blockholders in it, and note in one line that liquidity and control outcomes are absent from her design.

## 8. Quotes we may lean on (verbatim, page-cited)

*Copied character-for-character from `research/txt_extracts/zeng_2026_ras.txt`; end-of-line hyphenation introduced by the PDF extractor has been closed up (e.g. "cross- ing" → "crossing"). Curly apostrophes as in the source.*

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "Under Rule 13d-1(a), investors must file a 13D within 10 days after crossing the 5% threshold if they intend to influence management, whereas passive investors without this intent must file a 13G." | p. 1303 | The rule as she states it — both margins, pre-2024 regime |
| Q2 | "In my sample, the median number of days between trigger and filing dates is nine calendar days." | p. 1309 | Window is *binding in practice*: the median filer uses nearly all of it |
| Q3 | "Even though Rule 13d-1(a) requires 13D filers to submit the form within 10 calendar days of the trigger date, a significant number of 13Ds were filed late." | p. 1312 fn. 13 | Compliance is imperfect; a window-margin design must handle late filers |
| Q4 | "Therefore, I focus my analyses on the 13Ds within 13 days of the trigger date whose filing date insiders can reasonably anticipate." | p. 1312 fn. 13 | The sample screen that becomes non-neutral across 2024-02-05 |
| Q5 | "Notably, the price run-up begins precisely on the trigger date" | p. 1310 | Information moves at the threshold crossing, before the flag |
| Q6 | "Furthermore, I control for time-variant firm and stock characteristics, including size, book-to-market ratio, illiquidity, and volatility." | p. 1320 | Evidence that liquidity enters only as a nuisance control |
| Q7 | "Sixth, while this study does not aim to disentangle insiders’ motives, I acknowledge that concerns, such as control rights or job security, may arise in confrontational activist campaigns." | p. 1322 | Her explicit scope disclaimer on control-related motives |
| Q8 | "The SEC has historically prioritized insider trading cases involving major corporate events, such as earnings announcements and acquisitions, rather than investor-based events like 13D/13G filings." | p. 1311 | Enforcement is thin at exactly the margin we study |
| Q9 | "Overall, the similar insights gained from extending the analyses to 13Gs demonstrate that managers systematically extract information about blockholder accumulations, regardless of investor intent, demonstrating a broader pattern of learning about investors’ trades beyond activism contexts." | p. 1327 | Her own generality claim — the object is detection, not activism |
| Q10 | "As reported in Table 8, 8 find no evidence that insider trading declines when enforcement intensity increases." | p. 1331 | Enforcement null [typo "8 find" is in the published text] |
| Q11 | "Exempt investors need not file within 10 days of crossing the 5% equity stake and can file up to 45 days after calendar year-end." | p. 1317 | The window margin already varies by filer class — a design seam |
| Q12 | "Furthermore, monitoring helps firms anticipate voting outcomes and detect potential activism or control contests early." | p. 1307 | The only sentence linking her setting to control outcomes — and it is motivation, not measurement |
| Q13 | "Rule 13d-1(a) requires all 13D filers to disclose their daily trading information over the past 60 days, but due to lack of enforcement, only 2,327 13D filers actually do so." | p. 1314 fn. 14 | Parser-validation warning for our own Item 5(c) collection |
| Q14 | "However, I acknowledge that these proxies are noisy and may not perfectly capture actual enforcement intensity." | p. 1331 | Her own limitation on the enforcement leg |

## 9. Verification log

**Verifier: opus, adversarial, 2026-08-19.** Source of record: `research/txt_extracts/zeng_2026_ras.pdf` re-extracted per page with `pdftotext -f N -l N -layout`; the `.txt` used only for whole-file greps. **Page mapping independently confirmed on two pages:** PDF p. 12 → running head "1312", PDF p. 41 → running head "1341", so printed = PDF + 1300. Holds.

**Counts: 30 OK · 3 WRONG · 2 MISCITED · 5 UNCHECKED.**

**Quotes (§8) — 14/14 OK.** Every quote whitespace-normalised (curly quotes, en-dashes, end-of-line hyphenation closed) and matched as an exact substring against the per-page extract; each returned exactly one page and that page equals the cited page. Q1 p.1303, Q2 p.1309, Q3 p.1312, Q4 p.1312, Q5 p.1310, Q6 p.1320, Q7 p.1322, Q8 p.1311, Q9 p.1327, Q10 p.1331, Q11 p.1317, Q12 p.1307, Q13 p.1314, Q14 p.1331. Q10's "8 find" typo is genuinely in the published text (p. 1331, line under Table 8) — not a transcription error.

**Results (§3).**
- R1 OK on values (2.8 / 1.9 / 6.1; 0.9 / 0.4 / 1.7; no six-month reversal — p. 1309–1310). Label kept ESTIMATED but annotated: no SE or t is printed for any of these, and the intro (p. 1303) gives "6%" over (t−10, t+10) — a different window. Noted in the table.
- R2 magnitudes OK against body print (0.040 / +67.8%, 0.091 / +154.5%, 0.034 / −25.4%, pp. 1319–1320). Significance **UNCHECKED** (IA Table IA.1). Label split accordingly.
- R3 OK (45%, 8%, p. 1319). R5 OK — "peak precisely on the trigger date itself" p. 1319, and "peak precisely on the trigger day" p. 1304.
- R4 OK exactly: 0.017*(1.93), −0.016*(−1.66), 0.032***(2.75), 0.057***(3.33), 0.002(0.09), 0.056**(2.48); N 482,641 / 443,418 (Table 2, p. 1321).
- R6 OK: Daily Returns 0.337***(3.17), Table 2 col. 1.
- R7 OK: 0.335***(3.16), 0.344***(3.03), 611 non-overlapping large trades ≥10 trading days apart (p. 1323), Table 3 N = 5,589 (p. 1324).
- R8 OK: 0.089***(2.86) N 2,689; 0.077*(1.94) N 2,330; 0.068**(2.14) N 1,735 (Table 4, p. 1326).
- R9 OK: 0.074***(8.01), 0.009(1.11), 0.064***(5.24), N 2,206,048 (Table 5, p. 1328).
- **R10 discrepancy CONFIRMED.** Table 6 col. 2 (p. 1329): 0.008, t = 0.78, no stars. Text p. 1328: "Table 6 shows that both executives and independent directors adjust their trading". The card's charge stands. **MISCITED** on page only — Table 6 is on p. 1329, not "1328–1329"; fixed.
- **R11 discrepancy CONFIRMED.** Table 7 col. 1 (p. 1330): 0.004, t = 0.14, no stars. Text p. 1329: "abnormal insider purchases occur in both institutional and non-institutional filings". Stands. **MISCITED** on page — Table 7 is on p. 1330; fixed.
- **R12 WRONG (understated).** All six coefficients match the print (Table 8, p. 1331), but the card said "two of four enforcement coefficients are significantly positive". SEC Staff 13D is **0.067\* (1.67)** — one star. So **three of four** are positive and significant (13G Budget 0.115** and 13G Staff 0.071** at 5%; 13D Staff at 10%). Corrected in R12. This *strengthens* the card's own criticism.
- R13 → **UNCHECKED** (IA.2–IA.7). R14 → **UNCHECKED** (IA.9). Labels changed from ESTIMATED; only the author's prose descriptions are printed.
- **R15 MISCITED.** The path (3.0% → 4.6% → >1% on TD → 6.9%) is on p. 1319 and comes from IA Fig. IA.2, described in body; the **4.02% at TD−5 is on pp. 1305 and 1323, not pp. 1318–1319**. Page fixed and Table 1 Panel B's other statistics added.

**Scope claims (§6) — greps re-run independently over the whole file, case-insensitive, hyphenation closed.**
- `illiquidity` = **11**, not 10 (pp. 1317, 1320, 1321, 1326×2, 1328, 1329, 1330, 1331, 1337×2). **WRONG** on the count; fixed with the correct composition. Substance unaffected: still nuisance-control only.
- `liquidity` standalone (not "illiquidity") = **4** — p. 1318 ×2 (insiders' personal "liquidity needs or diversification"), p. 1339 (Agarwal et al. 2015), p. 1340 (Edmans–Fang–Zur 2013). Card **OK**.
- `Amihud` = 1 (p. 1337) **OK**. `bid-ask` 0, `spread` 0, `market depth` 0, `turnover` 0 — **OK**.
- `order flow` = **1**, not 0 (p. 1307, Chabakauri et al. 2022). **WRONG**; row added.
- `premium` = **0 — OK, confirmed**. `bidder` 0, `tender offer` 0, `proxy fight` 0, `proxy contest` 0, `board seat` 0 — **all OK**.
- `noise` = 1 (p. 1302) OK. `takeover` = 2 (pp. 1308, 1340) OK. `campaign` = 2 (pp. 1310, 1322) OK. `control contest` = 1 (p. 1307) OK. `hostile` = 1 (p. 1303) OK. `activis*` = 33 OK.
- `control right` = 4 (pp. 1305, 1306, 1322, 1327) — **not in the card**; row added. Does not overturn "no control outcome", but a referee will cite it.
- **"5%/10-day as fixed scenery" — CONFIRMED.** No threshold is varied, no window length is compared, no interaction with either. The only within-paper window variation is the exempt-13G 45-day carve-out (Q11), which she uses to *exclude* filings, not to identify.
- **"Feb-2024 absent" — CONFIRMED.** `five business` = **0** hits. `business day` = 2 and both are unrelated (T+3 settlement p. 1308; Form 4 two-business-day reporting p. 1318). All three `2024` hits are bibliographic (Kacperczyk–Pagnotta 2024 cited p. 1331 and p. 1340; an "Accessed June 5, 2024" URL p. 1340). `amend` = 1 (p. 1312, 13D/A filings dropped in screening). Release 33-11253 never appears.
- **fn. 13 sample screen — CONFIRMED and slightly sharper than the card states.** p. 1312: "I exclude those filed later than 13 days after the trigger date **and those filed on the trigger date**." So the kept range is 1–13 calendar days, as the card says, and the *lower* bound is a real exclusion too — same-day filers are dropped. Both Q3 and Q4 verbatim.

**Version / venue (check 4) — OK.** PDF p. 1 front matter: "Review of Accounting Studies (2026) 31:1301–1341", DOI 10.1007/s11142-026-09958-z, "Received: 24 April 2023 / Accepted: 31 March 2026 / Published online: 8 May 2026", sole author Jean (Jieyin) Zeng. 41 printed pages, ends with the Springer rights notice.

**Omissions found and added (check 5).**
1. **p. 1303 fn. 4 — the announcement-return decomposition.** Albuquerque et al. (2022): 74.8% intervention value, 13.4% stock-picking. Material: it is the split our own premium claim has to survive. Added to §4.
2. **pp. 1306–1307 — the two concurrent papers.** Chabakauri et al. (2022): insiders filter activist trades out of **aggregate order flow** and **retain ownership to defend control rights**; Duong et al. (2025): hedge-fund activists, personal-gain framing. The first is the paper closest to our coordinates (order flow × control defence) and the card did not name it at all. Added to §4 and §6.
3. **p. 1322 / IA Table IA.2 — the size split.** Effect *slightly more pronounced in larger firms, difference not statistically significant*. Material because §7.2 claimed nobody looked at anything liquidity-adjacent; they did, coarsely, and the sign runs against a naive thin-stock story. Added to §6 and §7.2, and the §7.2 claim rewritten.
4. **p. 1317 Table 1 Panel C — the sample is thin throughout.** Median target market cap $186m (mean $1,036m); Illiquidity mean 0.384, median 0.142. Strengthens the κ-interaction case but also means there is little cross-sectional liquidity range to exploit within her sample. Added to §7.2.
5. **p. 1323 fn. — large-trade cutoff robustness** (10% and 30% alternatives to the 20%-of-volume definition). Relevant if we reuse the Table 3 design. Added to §4.
6. **p. 1312 — same-day filers are excluded** as well as late ones. Added above; matters for anyone rebuilding the screen.

**UNCHECKED and decision-critical — ~~named, not triaged away~~ RESOLVED 2026-08-21, see §9b.** R13's size-split result (IA.2) was the single most decision-critical claim in this card for our positioning: if a referee reads IA.2 as "liquidity/size already tested and null", our κ opening narrows. The Springer supplementary file has now been pulled and read in full; **all five IA-dependent items are closed** — IA.2 (verdict in §9b(b)), R2's SEs (IA.1), IA.3–IA.7, R14 (IA.9), the control-period means 0.059 bp (13D, IA.1) and 0.048 bp (13G, IA.8), and Figs. IA.1–IA.2 (read as rendered images, §9b(e)). Nothing decision-critical remains unchecked on this card.

**Overall verdict: the card SURVIVES.** Its two headline "text vs table" catches (R10, R11) are correct against the printed tables, its Table 8 criticism is correct and in fact understated, the `premium` = 0 and Feb-2024-absent claims hold exactly, and the fn. 13 screen is as described. Three small grep/count errors and two page slips fixed; five IA-dependent results relabelled UNCHECKED; six omissions added, of which the Chabakauri (2022) order-flow/control-rights link and the IA.2 size split are the two that change how we should write §7.

---

*Reader's own checks, recorded as claims — not treated as verification:*
- File identity: running heads "Review of Accounting Studies (2026) 31:1301–1341", DOI 10.1007/s11142-026-09958-z, title and author match the assignment. 41 printed pages + 1 blank trailing form-feed page. Not truncated: text runs from the abstract through the closing Springer rights notice on p. 1341.
- All 14 quotes above located by whitespace-normalised exact substring match against the extracted text; each returned exactly one page. Q1's hyphenation closed as noted in the §8 header.
- Grep counts in §6 produced by case-insensitive `re.findall` over the whole file; `liquidity` reported net of the 10 `illiquidity` hits.
- **Unchecked:** every number attributed to an Internet Appendix table (R2, R3, R13, R14 and the control-period means 0.059 bp and 0.048 bp) — the IA is not in this PDF and was read only through the body text's own description. **← superseded 2026-08-21: the IA has been fetched and read in full; see §9b.**

---

## 9b. Internet Appendix (verified 2026-08-21)

**Source of record.** `research/txt_extracts/zeng_2026_ras_internet_appendix.pdf`, the Springer
supplementary file linked from `link.springer.com/article/10.1007/s11142-026-09958-z`; text layer
re-extracted with `pdftotext -layout` to `…_internet_appendix.txt`, and pp. 1–2 (the two figures)
additionally rendered at 300 dpi with `pdftoppm` and read as images, because their content is
vector chart, not text. **14 PDF pages, 13 with content; ALL of Tables IA.1–IA.9 and Figures
IA.1–IA.2 are present and were read.** Only PDF p. 1 carries a printed page number ("1"), so IA
items below are cited by **PDF page index**. Reader: opus.

Order in the file: Fig. IA.1 (p. 1) · Fig. IA.2 (p. 2) · IA.1 (p. 3) · IA.2 (p. 4) · IA.3 (p. 5) ·
IA.4 (p. 6) · IA.5 (p. 7) · IA.6 (pp. 8–9) · IA.7 (p. 10) · IA.8 (p. 11) · IA.9 (pp. 12–13).

---

### (a) Table IA.2 — the decision-critical table, verbatim

**Title (IA PDF p. 4):** "Internet Appendix Table IA.2 / Unexpected Insider Trading Prior to 13D
Filings: / Analyzing Variation by Market Capitalization". Dependent variable in all four columns:
**Daily Net Insider Purchases**. Columns 1–2 use the window **TD−20 to FD−1**; columns 3–4 use
**TD−5 to FD−1**. Columns 1 and 3 are **Smaller firms**, columns 2 and 4 **Larger firms** (median
market-cap split). Robust *t*-statistics in parentheses; stars as in Table 2 (\*\*\* 1%, \*\* 5%, \* 10%).

| | (1) Smaller, TD−20→FD−1 | (2) Larger, TD−20→FD−1 | (3) Smaller, TD−5→FD−1 | (4) Larger, TD−5→FD−1 |
|---|---|---|---|---|
| **Pre-disclosure** | **0.026** | **0.032\*\*** | **0.066** | **0.041\*** |
| *t* | **(1.27)** | **(2.46)** | **(1.64)** | **(1.95)** |
| Illiquidity | −0.025\* (−1.75) | 0.076 (0.80) | −0.033\*\* (−2.22) | 0.055 (0.49) |
| Size | −0.171\*\*\* (−6.03) | −0.121\*\*\* (−4.00) | −0.185\*\*\* (−6.05) | −0.128\*\*\* (−3.99) |
| Daily Returns | 0.386\*\*\* (2.58) | −0.392 (−1.56) | 0.306\*\* (1.99) | −0.358 (−1.28) |
| Firm & Year FE | Y | Y | Y | Y |
| **N** | **241,360** | **241,264** | **221,590** | **221,811** |
| R-squared | 0.021 | 0.036 | 0.022 | 0.037 |

**Unique search strings for a verifier** (whitespace-normalised exact substrings of the IA text; each
returns IA PDF p. 4 and nothing else):

| # | String (verbatim) | Where |
|---|---|---|
| IA-Q1 | `Pre-disclosure            0.026             0.032**               0.066            0.041*` | IA p. 4, coefficient row |
| IA-Q2 | `(1.27)            (2.46)                (1.64)           (1.95)` | IA p. 4, *t*-stat row |
| IA-Q3 | `N                          241,360            241,264               221,590        221,811` | IA p. 4, sample sizes |
| IA-Q4 | `Illiquidity               -0.025*           0.076                 -0.033**         0.055` | IA p. 4, the only liquidity-adjacent coefficient in the split |
| IA-Q5 | "This table explores size heterogeneity by dividing the sample firms into larger and smaller firms based on the median market capitalization and then replicates Table 2 Columns 3 and 6 for each of the two subsamples." | IA p. 4, table note — **the whole note; there is no difference test in it** |

**The body-text gloss the v4 position leans on** (p. 1322 of the article, verbatim, one hit):
"While unexpected insider trading is slightly more pronounced in larger firms, the difference is not
statistically significant, suggesting that managerial learning about blockholder trades occurs in
both large and small firms (Internet Appendix Table IA.2)."

---

### (b) Verdict on IA.2 — one plain sentence

**IA.2 weakens the gloss rather than supporting it: the "larger firms" direction holds only in the
long window (0.032\*\* vs 0.026), reverses in the short window closest to the trigger date, where the
small-firm estimate is 61% bigger than the large-firm one (0.066, t = 1.64, vs 0.041\*, t = 1.95),
and the table prints no test of the difference at all, so "the difference is not statistically
significant" is an assertion and "occurs in both large and small firms" is contradicted by the two
insignificant small-firm cells.**

Three consequences, stated flatly:

1. **Our κ opening is not closed.** The one thing a referee could have used against us — "she already
   tested size and found nothing bigger in small firms" — is not what the table says on the window
   whose *length* the Feb-2024 rule compresses. Small-firm point estimates are the larger ones there.
2. **The insignificance is a standard-error story, not a coefficient story.** 0.066 with t = 1.64
   implies SE ≈ 0.040; 0.041 with t = 1.95 implies SE ≈ 0.021. The small-firm SE is roughly twice the
   large-firm SE on nearly identical N (221,590 vs 221,811). Thin stocks are noisy, not quiet.
3. **The "both" habit is now three-for-three.** Same overclaim pattern as R10 (Table 6, independent
   directors) and R11 (Table 7, non-institutional filers) — recorded in §5.

---

### (c) The rest of the appendix — what bears on our position

**Table IA.1 (IA PDF p. 3) — 13D event-window means, *with the t-statistics the body omits*.** This is
the strongest single piece of evidence in the whole paper for **our window-margin anchor**, and it was
invisible from the article. Daily insider purchases, bp of shares outstanding; control mean **0.059**:

| Window | 13D obs. | Control | Diff. | % Diff. | *t* | *p* |
|---|---|---|---|---|---|---|
| TD−30 to TD−21 | 0.043 | 0.059 | −0.016 | −27.0 | −1.637 | 0.102 |
| TD−20 to TD−6 | 0.050 | 0.059 | −0.009 | −15.8 | −1.158 | 0.247 |
| **TD−5 to TD−1** | 0.099 | 0.059 | **0.040** | **67.8** | **2.884** | **0.004** |
| **TD to FD−1** | 0.150 | 0.059 | **0.091** | **154.5** | **6.657** | **0.000** |
| FD to FD+10 | 0.093 | 0.059 | 0.034 | 57.7 | 3.479 | 0.001 |
| FD+10 to FD+20 | 0.041 | 0.059 | −0.018 | −30.5 | −1.859 | 0.063 |

Sales (control mean **0.135**) move only in two windows: TD−20 to TD−6 at −0.034 (−25.4%, *t* = −2.967,
*p* = 0.003) and FD to FD+10 at −0.029 (−21.3%, *t* = −2.136, *p* = 0.033). **Sales do NOT fall inside
the disclosure window** — TD to FD−1 is +0.023 (*t* = 1.203, ns). So the whole net effect inside the
window is purchase-driven.

*Why this matters to us:* the abnormal buying is **confined to the legally created interval**. It is
flat-to-negative and insignificant for the whole month before TD−5, jumps at TD−5, peaks in
(TD, FD−1) at +154.5% of the control mean, and is gone by FD+10. That is not a slow drift that a
shorter window would merely re-time — it is a step function whose support *is* the window. Search
string: `day TD to FD-1                  0.150        0.059       0.091      154.5       6.657      0.000`.

**Table IA.8 (IA PDF p. 11) — the 13G mirror is even sharper.** Control mean 0.048; TD−5 to TD−1
+0.030 (+63.6%, *t* = 6.015); **TD to FD−1 +0.132 (+274.9%, *t* = 25.711)**; everything outside the
window insignificant. Sales also rise inside the window here (+0.036, +25.6%, *t* = 5.672) — the body
does not mention this — but net is still purchase-dominated 0.132 vs 0.036. Search string:
`day TD to FD-1                  0.179         0.048        0.132    274.900      25.711      0.000`.

**Table IA.3 (IA PDF p. 5) — the leak is *bigger* in the modern period, not decaying.** Pre-2010 vs
post-2010 on net purchases: long window 0.036\*\* (2.10) vs 0.029\* (1.80); **short window 0.039 (1.40)
vs 0.076\*\* (2.14)** — the post-2010 short-window effect is nearly double the pre-2010 one and is the
only one of the two that is significant. N = 234,326 / 248,315 / 215,186 / 228,232. Again **no
difference test is printed**, though the body claims one ("the difference is not statistically
significant", p. 1322). For us this is good news twice over: the phenomenon is alive in the sample
half that abuts our 2024 experiment, and the body's second "no significant difference" claim rests on
the same missing test as the first.

**Tables IA.4–IA.7 — five clean replications, one of which changes the interpretation.**

| Table | What changes | Pre-disclosure, net purchases (TD−20→FD−1 / TD−5→FD−1) | N |
|---|---|---|---|
| IA.4 (p. 6) | filing FE instead of firm × year FE | 0.031\*\*\* (2.60) / 0.055\*\* (2.45) | 482,641 / 443,418 |
| IA.5 (p. 7) | pre-only control window (−7 to −3 months) | 0.030\*\* (2.42) / 0.048\*\* (2.12) | 286,426 / 247,203 |
| IA.6 (pp. 8–9) | + GDP, CPI, unemployment (all insignificant) | 0.033\*\*\* (2.77) / 0.056\*\* (2.49) | 482,641 / 443,418 |
| IA.7 (p. 10) | 2,150 **nonconfrontational** 13Ds only | **0.042\*\*\* (3.01) / 0.076\*\*\* (2.89)** | 382,761 / 351,533 |

**IA.7 is the one that matters for our framing.** The effect is *larger* on the subsample where the
filer states no activism plan (0.076\*\*\* vs 0.056\*\* in the full sample). So the pre-filing leak is
about **ownership-change detection**, not about anticipating a control fight. That supports Zeng's own
generality claim (Q9) and it protects our position from a referee who says "your window story is
really a control-contest story" — in her data the window leaks *hardest* where there is no stated
control contest. Note also that IA.7 carries the most negative `Illiquidity` loadings anywhere
(−0.046\*\*\*, −0.053\*\*\*) — see the caveat in §7.2.

**Table IA.9 (IA PDF pp. 12–13) — the performance-prediction claim is half a claim.** 13D Panel A,
`I (Abnormal Net Purchases)` on ΔREV: 0.007\*\* (2.53), 0.010\*\*\* (3.23), 0.011\*\*\* (3.57), 0.006\*\*
(2.07), N = 2,302 / 2,179 / 2,096 / 2,019. On ΔROA: **0.004\*\* (2.01), 0.000 (0.23), 0.006\*\* (2.36),
0.001 (0.23)**, N = 2,482 / 2,359 / 2,273 / 2,184. 13G Panel B is uniformly significant on ΔREV
(0.004\*\* in all four quarters, N ≈ 11,400–11,700) and fades on ΔROA by q+3 (0.002, t = 1.33). Design:
filing-level cross-section, industry and year FE, robust *t*. Two honest points: **(i)** fn. 11's
"higher revenue growth and improved return on assets (ROA)" is supported for revenue and only
half-supported for ROA on 13Ds; **(ii)** fn. 11 says "over the 120 trading days following the
disclosure" but IA.9 runs from **quarter q — the quarter in which the filing occurs, part of which
precedes the disclosure — through q+3**, which is roughly 250 trading days, not 120. Cite fn. 11 only
with that correction.

---

### (d) Grep counts over all 13 IA pages (case-insensitive)

`premium` **0** · `takeover` **0** · `bidder` **0** · `spread` **0** · `order flow` **0** · `Amihud` **0** ·
`noise` **0** · `2024` **0** · `business day` **0** · `5 business` **0** · standalone `liquidity`
(net of `Illiquidity`) **0** · `Illiquidity` **6** — exactly one control row in each of Tables
IA.2–IA.7. **The Internet Appendix adds nothing to the liquidity, premium, control-outcome or
window-length axes.** §6's scope-boundary verdict is unchanged and now covers the appendix too.

---

### (e) The two figures, read off the rendered pages

Values below are **pixel extractions from the 300-dpi renders** (axis calibrated on the printed tick
labels, series traced by continuity), accurate to about ±0.1 pp — they are the reader's own
measurements, not printed numbers, and should be labelled NUMERICAL if used.

**Fig. IA.1 Panel A (13D).** Flat and slightly negative before the crossing: −0.01% at TD−20, trough
**−0.51% at TD−5**, −0.22% at TD−1. Then **+0.73% at TD** — a one-day move of about **+0.95 pp, the
largest single day anywhere before the filing**. Through the normalised window: 1.31% (20%), 1.80%
(40%), 2.19% (60%), 2.65% (80%), **3.47% at FD**. So **TD → FD = +2.74 pp**, which reproduces the
body's "+2.8%" (p. 1309) exactly. Post-filing: 4.85% at FD+1 (a **+1.38 pp jump on the day *after*
the filing, larger than the filing day itself** — relevant to how we set the CAR window in our own
event study), 5.48% at FD+5 (so FD→FD+5 = +2.01, body says +1.9%), **6.06% at FD+20** (body: 6.1%).
**Panel B (13G):** −0.04% at TD−20, 0.63% at TD, **1.61% at FD (TD→FD = +0.98, body says +0.9%)**,
peak 1.88% at FD+8, 1.68% at FD+18 (body: 1.7% total). **No confidence band is plotted in either
panel, so R1 still has no standard error of any kind.**

*Confirmed:* Q5's "the price run-up begins precisely on the trigger date" (p. 1310) is exactly right
for 13Ds — the pre-TD path drifts *down*, and the first upward move is the segment TD−1 → TD.

**Fig. IA.2 (13D filer accumulation path).** Ownership (left axis): **3.02% at TD−20 → 4.58% at
TD−1 → 5.97% at TD → 6.90% at FD**, confirming R15's 3.0 / 4.6 / 6.9 exactly. Daily volume traded by
the filer (right axis): ≈0.05% of shares outstanding per day from TD−20 to TD−10, rising to 0.18% at
TD−1, then **1.34% on the trigger day itself** — roughly **7× the previous day and 27× the TD−20
baseline** — then decaying through the window: 0.42% (20%), 0.26% (40%), 0.21% (60%), 0.17% (80%),
0.075% (FD).

**Two numbers we should take straight into the position.** (i) The blockholder's footprint is a
one-day spike of ~1.34% of shares outstanding on the crossing day; in a thin stock that is an enormous
share of daily volume, which is the κ mechanism stated in her own data. (ii) Only about **0.93 pp of
accumulation happens inside the whole trigger-to-filing window** (5.97% → 6.90%), and it is
front-loaded. So shortening the window 10 → 5 business days truncates the *tail* of the accumulation,
not its bulk — a quantitative discipline on how large a stake-size effect we should predict from the
Feb-2024 rule, and a caution against overclaiming one.

---

### (f) Status of every previously-UNCHECKED item on this card

| Item | Was | Now |
|---|---|---|
| IA.2 size split (decision-critical) | UNCHECKED | **READ — body gloss only half-supported; see (b)** |
| R2 significance (IA.1) | UNCHECKED | **OK — t = 2.884 / 6.657 / −2.967 as reported in (c)** |
| Control means 0.059 (13D) / 0.048 (13G) | UNCHECKED | **OK — IA.1 p. 3, IA.8 p. 11** |
| R13 tables IA.3–IA.7 | UNCHECKED | **OK — five clean replications; IA.3 and IA.7 add content, see (c)** |
| R14 (IA.9) | UNCHECKED | **PARTLY MISCITED — revenue holds, 13D ROA is 2-of-4, and the horizon is q…q+3, not "120 trading days following"** |
| Figs. IA.1–IA.2 | UNCHECKED | **OK on every body number; read as images, see (e)** |

**Net effect on the card: the position gets stronger, not weaker.** The one result that could have
pre-empted our κ angle does not, the window-margin anchor gains a printed *t* = 6.657, and the
appendix contains no liquidity, premium, control-outcome or rule-length content of any kind. Two new
weaknesses were found against the paper (a third "both groups" overclaim in IA.2, and the ROA/horizon
slippage in fn. 11 vs IA.9), and one honest caveat against us (the negative `Illiquidity` level
control) is now on the record in §7.2.
