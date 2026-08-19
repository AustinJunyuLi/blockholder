# Literature Brief — Strand: activism-empirics

**Author:** LitResearcher_ActivismEmpirics
**Date:** 2025 (current session)
**Scope:** Six canonical empirical papers on hedge-fund/shareholder activism (Brav–Jiang–Partnoy–Thomas 2008 JF; Greenwood–Schor 2009 JFE; Gantchev 2013 JF; Clifford 2008 JCF; Klein–Zur 2009 JF; Becht–Franks–Grant–Wagner 2017 RFS), read with a view to (i) stylized facts usable as institutional anchors, (ii) data sources, (iii) which facts our theory paper (liquidity κ, 13D-style disclosure, exit/voice, bidder entry, takeover premia) could claim to explain or test.

**Access summary (honesty note):**
- Brav et al. 2008: full text — ECGI Finance WP 139/2006 PDF (May/Nov 2008 revision, essentially the JF article) from ecgi.global. Read in full.
- Greenwood & Schor 2009: full text — published JFE article PDF ("ARTICLE IN PRESS" version) from HBS (hbs.edu/ris). Read in full.
- Gantchev 2013: full text — author's accepted manuscript (Warwick WRAP repository), essentially the JF article. Read in full.
- Klein & Zur 2009: full text — NYU/ECGI working-paper PDF (ECGI WP 140/2006, the version of record pre-JF; JF 2009 version is paywalled). Read in full. Numbers below are from this version; the published version's headline figures are identical (10.2% / 5.1% etc. appear in the JF abstract as quoted by others).
- Becht et al. 2017: full text — ECGI Finance WP 402/2014 (May 2017 revision, marked "RFS forthcoming"; identical in structure to RFS 30(9):2933–2971). Read in full.
- Clifford 2008: **partial access only.** SSRN (abstract 971018) is Cloudflare-walled for both curl and the WebBridge browser; ScienceDirect serves a captcha; no OA mirror exists (checked OpenAlex, Semantic Scholar, OpenAIRE, EconStor, Wayback, author pages). What I did obtain: the **full abstract, the complete Introduction, and the opening snippet of every section from the publisher's own page** (via fetch), which contain all headline numbers, plus precise secondary characterizations inside Brav et al. (2008, p. 8), Klein & Zur (2009, fn. 11), Greenwood & Schor (2009, fn. 1) and Gantchev (2013, intro). Table-level detail (e.g., exact break-down of the 8%–21% active-vs-passive return wedge) is **not** first-hand. Flagged where relevant.

---

## 1. Brav, Jiang, Partnoy & Thomas (2008), "Hedge Fund Activism, Corporate Governance, and Firm Performance," *Journal of Finance* 63(4), 1729–1775.

**Access:** ECGI Finance WP 139/2006 PDF (`finalbravjiangthomaspartnoy.pdf`), ~60 pp. Read in full.

**Research question.** What do activist hedge funds do, to whom, and with what consequences? First large-sample, hand-collected study of U.S. hedge fund activism, 2001–2006.

**Methodology / data.** No model; descriptive + event-study + matched-sample and probit analysis. Sample construction is the contribution: bought the full list of 11,602 Schedule 13D filers 2001–2006 from LiveEdgar; hand-filtered to hedge funds (web/phone verification) → 311 funds; pulled all 13D/13D/A from EDGAR; excluded distress-financing, risk-arb, and closed-end-fund events → 236 funds / 1,032 events; added 27 sub-5% events found via Factiva + 13F cross-check. **Final: 1,059 events, 882 unique targets, 236 funds (2001–2006).** Factiva news search for motives/responses/outcomes; Schedule 14A for proxy material; 13F for positions/exit; CISDM + web for fund AUM; CRSP/Compustat/ExecuComp/IRRC (GIM index) for target attributes. Event study vs. CRSP value-weighted index; calendar-time 4-factor portfolios for long-run returns; industry/size/BM matched peers and probit for targeting.

**Key results (all estimated, no theory).**
- *Targeting:* targets are "value" firms (high BM, low Q) but **profitable** (ROA 2pp above peers, higher cash flow), low payout, low growth, low R&D, more takeover defenses (GINDEX +0.4), **higher institutional ownership (+8.3pp) and analyst coverage, and higher trading liquidity (lower Amihud) than matched peers** — activists need to accumulate fast and to rally fellow shareholders. Under-represented in top size quintile (capital constraint: 5% of a top-quintile firm ≈ $285–760M vs. median fund AUM $793M). Unconditional annual probability of being targeted ≈ 1.8%; −1 SD in Q → +0.49pp. They avoid R&D-heavy "opaque" firms (consistent with Kahn–Winton 1998).
- *Stakes:* median initial stake 6.3%, median max 9.1%; 95th pct max = 31.5%; median dollar stake $11.9M at cost. **Activism is minority, non-control investing.** ~22% of events are multi-fund co-filed 13Ds ("groups"); wolf-pack/cascade free-riding discussed.
- *Announcement returns:* ~**7–8% abnormal over (−20,+20)** around 13D filing (62% positive); **run-up of ~3.2% over (−10,−1) with abnormal volume spiking *before* the filing** — direct evidence of informed accumulation/leakage during the 10-day filing window (they discuss "wolf pack" vs "tipping" interpretations). Sub-sample where 13D = first public news: 8.4%. **No reversal over the following year** (calendar-time alphas revert to ~0 after +3 months).
- *Cross-section:* sale-of-company objective +8.54%, business strategy +5.95%, general "maximize value" +6.28%, capital structure +1.47% (n.s.), governance +1.73% (n.s.). Hostile initiation adds ~+3.9%. Pre-13F disclosure of the stake reduces the 13D return by −3.27pp (info already out), but returns remain +3.96% — argues intervention, not stock-picking. Exit after **failed** campaigns: −4% around the divestment 13D/A; exits after success ≈ flat.
- *Outcomes:* success 40.6%, partial 25.8% (≈2/3 combined), failure/withdrawal 21.4%. Hostile events: lower full success, higher partial success; overall success ≈ equal (68.1% vs 64.4%). Target response: accommodate 29.7%, negotiate 29.1%, fight 41.3%.
- *Real effects:* payout yield +0.3–0.5pp (on 2.2% base) within a year; book leverage +1.3–1.4pp; ROA +0.9–1.5pp and EBITDA/Sales +4.7–5.8pp by t+2 (slow); CEO pay −$1M and CEO turnover +12.4pp vs. peers one year out. No creditor expropriation (zero-LT-debt targets have slightly *higher* returns, 9.46% vs 7.21%). Attrition (delisting via sale) 18.2% — survivor-based performance analysis is biased *down*.
- *Horizon:* median 369 days for completed exits; imputed full-sample median 556 days; portfolio-turnover-implied ~22 months. Not short-term.
- *Returns to the fund:* mean deal holding-period return 42% raw / 33% annualized; +14.3pp annualized vs. size-matched portfolio; **median indistinguishable from benchmark — right tail drives the mean.** Announcement returns declined monotonically 15.9% (2001) → 3.4% (2006) — "arbitrage decay."

**Institutional facts.** 13D mechanics: file within **10 days** of crossing 5% with intent to influence; Item 4 = purpose; 13D/A "promptly" on material change (incl. dropping below 5%); 13G = passive alternative; 13F quarterly holdings (>$100M AUM, 45-day lag); mutual funds face 5%/10% concentration tax + ICA-1940 limits (why hedge funds do this, not mutual funds); ISS backed the activist in 23 of 32 media-covered votes.

**Referee-facing strengths/weaknesses.** Strengths: definitive sample, careful institutional detail, the anti-stock-picking battery (Pre-13F, exit returns, CEO/payout changes). Weaknesses a referee would attack: selection-on-unobservables in targeting; "success" coding is judgmental; market-reaction interpretation relies on equilibrium indeterminacy (they cite Maug 1998/Cornelli–Li 2002: returns understate ex-post benefits); 2001–2006 is one credit-cycle; no bidder/takeover mechanism modeled — "sale of company" is an outcome, not a price.

**Implications for repositioning our paper.**
- The **pre-filing run-up + volume spike before disclosure** is the single best empirical anchor for our model's "inferred vs disclosed" order-flow split: the market *infers* accumulation during the 10-day window before the 13D reveals it. Cite as the motivating fact for stake-triggered disclosure splitting inference.
- **Announcement CAR ≈ 7%** and **~9% median max stake** are the moments our model should speak to (minority gains to disclosure; small-stake activism).
- Their liquidity targeting result (targets are *more* liquid than peers) is a necessary moment any liquidity-κ theory must match — and the sign matters for how we frame the hump in R1.
- The 15.9%→3.4% decay and hostile/non-hostile equivalence are equilibrium-selection facts a structural version could target.
- Differentiate: they measure *expectations* of value creation; we model *where* the premium comes from (bidder entry conditional on price). We complement, not contradict.

---

## 2. Greenwood & Schor (2009), "Investor Activism and Takeovers," *JFE* 92(3), 362–375.

**Access:** published JFE PDF from HBS (Robin Greenwood's page, `Investor Activism and Takeovers_…pdf`). Read in full (14 pp. article).

**Research question.** Where do the large activism announcement returns come from? Answer: almost entirely from the activist's success in getting the target **acquired**.

**Methodology / data.** All Schedule 13D + DFAN14A filings on EDGAR, 1993Q3–2006Q3 (173,078 13Ds), cross-referenced to 13F filers to keep portfolio investors; hand-read "purpose of transaction" → **980 activist events / 811 unique pairs (784 by 139 hedge funds; 196 by 38 non-HF)**; passive 13D filings kept as a control group; CISDM for HF classification; CRSP delisting codes (2xx/3xx within 18 months) for takeover outcomes; Factiva for outcomes (16 subcategories). Abnormal returns = target minus a **factor-loading-weighted FF3 match portfolio** (loadings estimated on [t−110, t−10]); monthly version on 24 months. Takeover-incidence counterfactual: industry/size/prior-return matched firms, plus non-activist 13D filers, plus all small CRSP stocks. Final test: activist portfolio performance in the July–Sept 2007 credit crunch (DGTW-matched), using top-10 13F positions of the 16 most serial activists (144 stocks).

**Key results (all estimated).**
- Announcement CAR ≈ 3.5% (15-day); 18-month post-filing CAR ≈ 10.3% for the full sample.
- **The entire long-run effect is takeovers:** targets acquired within 18 months earn +5% announcement and **+25.85% post-filing CAR**; non-acquired targets earn 2.36% announcement and ≈0 thereafter (insignificant), *regardless of what else happened* (board seats, spinoffs — only spinoffs get +6.4% announcement). No accounting change (leverage, payout, capex, assets, shares) correlates with long-run returns for survivors (except ROA, ambiguously). Survivors do de-lever investment (capex/PP&E 36.5%→22.1%) and raise leverage.
- **Takeover incidence:** 18.1% of targets acquired within 12 months vs. 7.2% industry-size-return matched, 12.6% non-activist 13D filers, 4.7% all small stocks. 18-month: 21.9% vs. 9.1%. **Activism raises takeover probability by ~11pp.** Back-of-envelope: 11pp × 30% premium ≈ 3.3% ≈ observed announcement return — prices capitalize the *expected* takeover premium.
- Targets: small (2nd–3rd decile), low M/B, thin analyst coverage, industry underperformers over prior 24m. Mean stake 10.5%.
- **2007 natural experiment:** when buyout financing collapsed (Chrysler/Boots, Home Depot price cut), activist portfolios lost ~5% in the key week (CAR −1.0% EW / −1.1% VW, significant) and underperformed ~3pp over the crisis window — returns to activism load on takeover-market conditions.
- 15.7% of events initially about "corporate governance" end in takeover — demands morph into sale.

**Institutional facts.** 13D/13G/14A filing taxonomy; 13F $100M threshold; DFAN14A for proxy fights below 5%; CRSP delisting codes as takeover identification; the "putting companies into play" phrase; PE manager quote (Thomas H. Lee thanking Icahn/Peltz/JANA/Third Point "for teeing up deals").

**Referee-facing strengths/weaknesses.** Strengths: clean, falsifiable economic channel; the matched-incidence calculation; the 2007 out-of-sample confirmation; honest about the selection alternative (activists may just pick takeover-likely stocks — the non-activist 13D control (12.6%) is the best answer they have, and it is *not* dispositive). Weaknesses: matching cannot rule out unobserved "takeover-likeness"; the 30%-premium × 11pp identity is an accounting decomposition, not identification of the activist's causal effect on the *premium*; outcome coding ends at 18 months; says nothing about *why* a bidder pays — which is exactly the gap our theory fills.

**Implications for repositioning our paper.**
- **This is the paper our model most directly speaks to.** G&S reduce activism returns to E[takeover premium × Pr(takeover)] but treat both objects as primitives. Our model can claim to *endogenize the premium* (bidder enters based on the post-disclosure price; liquidity κ shapes the wedge) and to *endogenize the probability* (disclosure regime shifts bidder entry).
- Their 11pp/30%≈3.3% arithmetic is a ready-made calibration target for R1 (expected minority takeover gains) — and their finding that non-acquired targets earn ≈0 disciplines how much "voice"-only value our model should promise.
- The 2007 credit-crunch test is the template for an out-of-sample test of any liquidity channel: if premia are liquidity-driven, activism returns should co-move with financing/liquidity conditions — our R1/R2 make *cross-sectional* liquidity predictions they did not test. Cite as motivation, differentiate as mechanism.
- Borrow: their DFAN14A + 13D sampling is the cheapest replication base for any empirical section we add.

---

## 3. Gantchev (2013), "The Costs of Shareholder Activism: Evidence from a Sequential Decision Model," *JF* 107(3), 610–631.

**Access:** author's accepted manuscript, Warwick WRAP (wrap.warwick.ac.uk/139701/7/). Read in full.

**Research question.** Do the gross returns to activism cover its costs? Estimate the *unobservable* cost of each activist tactic from observed escalation/exit decisions.

**Model architecture (the only structural entry in this strand — read carefully).** Activism = **sequential decision process**: stage 0 = 13D filer with intentions but no demands; stage 1 = demand negotiations; stage 2 = board representation; stage 3 = (threatened) proxy contest. Escalate only after the cheaper tactic fails. At each node the activist compares continuation utility vs. selling at the current market value: continue iff −c_{n+1}/(π_{n+1}·θ·M) + (V/M − 1) ≥ 0, where c = stage cost, π = stage success probability, θ = stake, M = current market value of stake, V = target's *frontier* value. Two sufficient statistics: expected gross return of success (V/M − 1) and the (inverse) mark-to-market investment 1/(θM). Random-utility (Type I EV) errors → conditional logit per stage; **statistical backward induction** (Bas–Signorino–Walker 2008): estimate proxy-stage costs first, feed into earlier stages. **Identification of absolute costs** comes from constraining the coefficient on V/M − 1 to one (fixing the logit scale), justified by the break-even condition. **Frontier value V** is estimated by a censored quantile regression (Powell 1984) of Q on tercile ranks of size, asset turnover, market share, growth, R&D (EGJ 2012 matching variables), calibrated so the median implied improvement = 35.38% = the median *actual* improvement in successful campaigns. Stage duration is assumed fixed (supported by data: mean stage ≈ 7 months, no cross-stage variance).

**Data.** SEC 13D + all amendments, PREC/DEFN/PREN 14A proxy filings, SharkRepellent.net outcomes, 2000–2007; Dow Jones Newswires 13D list (~5,000 filings) → 171 hedge funds (129 families), **1,164 campaigns, 1,023 unique targets, 5,645 filings**; +21 non-public (sub-5%) campaigns from Brav et al.'s news sample; 13F for fund returns (Griffin–Xu method). Excludes REITs/bankrupt/blank-checks/ADRs.

**Key results.**
- *Funnel:* >2/3 of 13D filers quit before making demands; <20% of demand-makers seek a board seat; 10–12% threaten a proxy fight; **only 7% of campaigns reach a proxy fight.**
- *Success by stage:* negotiations 6.76%; board rep 39.33%; proxy contest 57.38%. Overall 29.17% (46% if board seats count as a demand — comparable to BJPT/G&S). Most successful demands: sale/privatization, restructuring, disclosure; least: dividends, CEO removal, comp.
- *Costs (structural, the headline):* **proxy contest $5.94M (95% CI 3.04–10.86); demand negotiations $2.94M (0.89–6.96); board representation $1.83M (0.46–4.32); full campaign ending in proxy fight $10.71M.** Sanity check vs. 2-and-20 break-even fees ($12.4M VW / $17.3M DGTW mean).
- *Net returns:* gross annualized VW alpha 4.02% / DGTW 5.75–7.61% → **net of costs 0.23% VW / 2.38% DGTW — costs eat ~2/3.** Raw annualized deal return 31.48%. Proxy stage has the *lowest* net returns (possibly value-destroying for the activist). Only the top quartile of campaigns beats the fund's own non-activist portfolio (90th pct net VW 56.5% vs 27.2% non-activist).
- *Ownership:* mean initial stake 8.27% (median 8.0%), mean max 9.11%; median within-stage change = 0 — **activists do not buy their way into influence** (ownership insignificant for success; results robust to excluding stakes >16%). 85% of S&P 500 firms require >25% to call special meetings — minority stakes stay minority.
- *Takeover robustness:* 104 SDC-identified acquisitions among targets. M&A events beat non-M&A by ~24pp gross (confirms G&S unconditionally), **but the difference becomes insignificant after controlling for stated objectives and after netting costs** — i.e., G&S's takeover effect is partly objective-selection.
- Targets: mean market cap $868.5M, Q=1.30, higher institutional ownership, small, no operational distress.

**Institutional facts.** Full 13D anatomy (Appendix A: 7 items, Item 4's ten enumerated purposes); 13D/A on >1% ownership change or intent change; 13G passive bar; proxy-threat vs proxy-fight distinction via PREN/DEFN 14A; anecdotal cost anchors (Bainbridge $1.8M in the 1980s; Whitworth ">$10M" for a short-slate campaign; Icahn's $5M Lazard fee on Time Warner); ISS ownership-threshold facts.

**Referee-facing strengths/weaknesses.** Strengths: first cost estimates; clean revealed-preference logic; transparent identification argument. Weaknesses a referee would attack: (i) the coefficient=1 restriction is an *assumption*, not an identification proof — costs are only as absolute as that normalization; (ii) frontier V is *calibrated* to realized successful-campaign returns — partly circular; (iii) costs are fixed across campaigns within a stage (relaxed only via activist dummies); (iv) logit errors, fixed stage durations, no strategic target (management is a passive wall); (v) exits may be portfolio-driven, not campaign-driven. Still: the only paper here with an explicit decision model — the natural empirical counterpart to cite for our theory's cost/timing structure.

**Implications for repositioning our paper.**
- **Borrow the escalation ladder** as the institutional description of "voice": quiet demand → board seat → proxy fight maps onto our Quiet Voice / Public Voice margin; his cost estimates ($1.8M/$2.9M/$5.9M per stage) give our voice-cost parameter *defensible magnitudes*.
- His "activists don't raise stakes during campaigns" (median change 0) is a useful simplification license for a static stake in our model — and also a hook: in our model the stake is chosen *ex ante* under liquidity; empirically the stake is set at entry.
- His M&A robustness (objectives explain the G&S result) gives us a referee-proof middle position: takeover premia matter, *conditional on the campaign's stated intent* — our model's bidder-entry channel is exactly such an intent-conditional mechanism.
- Cite for: costs of voice, success-by-stage, 7% proxy incidence, minority-stake discipline.

---

## 4. Clifford (2008), "Value Creation or Destruction? Hedge Funds as Shareholder Activists," *JCF* 14(4), 323–336.

**Access: PARTIAL.** Full text paywalled/bot-walled on all channels (SSRN Cloudflare; ScienceDirect captcha; no repository copy exists — verified OpenAlex/Semantic Scholar/OpenAIRE/EconStor/Wayback). Obtained **first-hand from the publisher page**: complete abstract, complete Introduction, and opening snippets of each section (data design, summary stats, organizational form, conclusion). Cross-checked against in-text descriptions in Brav et al. 2008 (1,902 firm-fund observations, 197 funds, 1998–2005), Klein & Zur fn. 11, Greenwood & Schor fn. 1, Gantchev 2013. Table-level results (e.g., the regression detail behind the return wedge, lock-up logits) are **not** first-hand.

**Research question.** Does hedge fund activism create value, or do hedge funds just pick good stocks? Identification: compare the *same* fund's **active (13D)** vs. **passive (13G)** blocks.

**Methodology (from intro/snippets + secondary).** All 13D filings by 197 hedge fund families, 1998–2005 (≈1,902 firm-fund observations per Brav et al.), with the same funds' 13G (passive, "investment purposes only") blocks as the within-fund control group. Logic: selection ability is held fixed across filing types, so the active/passive contrast isolates the value of *intended intervention*, and the 13G/13D choice itself is the activist's revealed intent. Also examines fund organizational structure (lock-ups, redemption notice periods) as determinants of who does activism, and fund-level holding-period returns on active vs. passive blocks.

**Key results (first-hand numbers from abstract/intro).**
- Event-window excess returns: **+3.39% active vs. +1.64% passive** (difference significant at 1%).
- **ROA +1.22% in the year after active targeting**, driven by **asset reduction (divestiture of underperforming assets)** more than cash-flow improvement; no evidence of myopic cash stripping/leverage spikes.
- Funds with **longer lock-ups and redemption-notification periods are more likely to be activists** — the fund's own liquidity structure enables illiquid, lengthy engagements.
- Funds earn **8%–21% higher annual returns on active than passive blocks** — the "revenue function" of activism compensates monitoring costs; first documentation that activists earn a premium on activist positions (Gantchev later nets out costs).
- Context numbers from section snippets: activism ≈ $50B of $1.4T industry; ~3% of long–short/event-driven funds in TASS/CISDM are activists.

**Institutional facts.** The 13D-vs-13G legal dichotomy as a revealed-intent meter (Rule 13d-1(a)/(b)); hedge-fund lock-up/notification practices as the enabling institutional feature; both facts directly usable.

**Referee-facing strengths/weaknesses.** Strengths: the within-fund active/passive design is the cleanest selection control in this literature. Weaknesses: the 13D/13G choice is itself endogenous (funds file 13D *because* they expect high returns — the design identifies intent, not the causal effect of intervention); 13G filers can be "closet activists"; JCF-tier exposition of robustness.

**Implications for repositioning our paper.**
- The **13D/13G margin is the sharpest institutional hook for our disclosure module**: the same investor self-labels intent at the 5% threshold; market reaction differs (+3.39% vs +1.64%) — direct evidence that *disclosure content* (not just the block) moves prices. Our model's disclosed-vs-inferred split should cite this as the cleanest measurement of the disclosure event's information content.
- Lock-up result supports treating the activist's horizon/commitment as a structural parameter.
- Differentiate: Clifford measures intent's value; we model how disclosure changes *inference and bidder entry* — complementary, and his design suggests an empirical design for any empirics we add (13D-vs-13G as treatment/intent).
- Caveat for our draft: do not cite Clifford for numbers beyond the four above unless the full text is later obtained (I flagged what is second-hand).

---

## 5. Klein & Zur (2009), "Entrepreneurial Shareholder Activism: Hedge Funds and Other Private Investors," *JF* 64(1), 187–229.

**Access:** NYU/ECGI WP 140/2006 full PDF (archive.nyu.edu). Read in full (~67 pp. incl. tables). (JF-published version is the same study; headline figures match.)

**Research question.** Compare **confrontational** activism by hedge funds vs. other entrepreneurial activists (individuals, PE, VC, family asset managers) — targeting, market reaction, success, and post-intervention redirection.

**Methodology / data.** All initial 13D/13D/A filings, sample primarily 2003–2005 (first filings traced back via 13D/A); keep only filings with an explicit confrontational purpose (excludes "reserve the right" and cooperative-only statements — the complement of Brav et al.'s full sample); hand-classify filers via web/Factiva → **151 hedge-fund campaigns (101 funds) + 154 other-entrepreneurial campaigns (134 investors: 58 individuals, 38 investment advisors, 16 asset managers, 9 PE, 5 VC, 8 ex-officers)**. Matched peers: 10 closest revenue firms in FF48 industry, then closest BM. Returns: size-adjusted (FF quintile portfolios), market-adjusted, industry-adjusted; windows [−30,+5] and [−30,+30]. Success = stated goal achieved within 1 year (13D/A + Factiva). Proxy fights/threats from Georgeson + Factiva. Logit/probit for targeting.

**Key results (all estimated).**
- *Targeting contrast:* hedge funds target **healthier, more profitable firms** (EBITDA/Assets 6.2%, Altman Z 2.47, prior-year abnormal return +12.3% — above even their controls), cash-richer; other activists target weaker, smaller firms (median MVE $70M vs $133M). Both groups: small, low M/B.
- *Announcement returns:* HF targets **7.3% [−30,+5] and 10.2% [−30,+30]** size-adjusted; others 4.4%/5.1%. Board-seat demand: +12.6%; "intends to buy the firm": +13.1%; mere "pursue alternatives": +4.3%. **One-year post-filing drift: +11.35% (HF), +17.8% (others)** — no reversal.
- *Success:* **HF 60%, others 65%** overall; board seats 73%/71%; buyback, CEO replacement, dividend initiation ~100% (small n); strategy changes ~50%. Aggressive objectives are *more* successful for HF (67% vs 47%).
- *Proxy weapon:* 40% of HF campaigns (31% others) involve actual/threatened proxy solicitation; threats alone earn +4.5–5.1% at announcement; proxy use predicts **board-seat** success (χ² 12.1/14.3) but not overall success — the threat, not the vote, is the instrument (contra Bebchuk's "myth of the shareholder franchise").
- *Market anticipates success:* successful-campaign targets earn 10.7% vs 2.6% (unsuccessful) at announcement — prices impound the *probability-weighted* outcome ex ante (same point BJPT make formally; important for any model of announcement returns).
- *Takeover incidence:* 22/151 HF targets (14.6%) and 19/154 others (12.3%) acquired within a year. For other activists, to-be-acquired targets earn 17.4% vs 3.25% at announcement; **for HF targets no difference** — hedge-fund activism is not (yet) purely takeover-oriented in this window; contrast with G&S.
- *Post-activism real effects:* **no profitability improvement in year 1** (EBITDA/Assets −0.024); HF targets double dividends (+11.2¢/share), raise leverage (+1.6–2.6pp), cut cash; other activists cut R&D and capex. Effects don't reverse in year 2 (small n). Two activist technologies: HF = free-cash-flow discipline; others = investment redirection.

**Institutional facts.** 13D purpose-statement taxonomy; the confrontational-only sampling rule (mirror image of Clifford's 13G control); Georgeson contested-solicitation data; 3(c)(1)/3(c)(7) exemptions; proxy-fight reimbursement norms (Pirate/Cornell example: $750k cost reimbursement in settlement).

**Referee-facing strengths/weaknesses.** Strengths: the two-group design; success coded against *stated* goals; the ex-ante-anticipated-success evidence. Weaknesses: small samples (n≈150/group); 2003–2005 bull-market window; success coding judgmental; confrontational-only sample truncates the (majority) cooperative activism that BJPT show dominates — external validity caveat; annual Compustat only.

**Implications for repositioning our paper.**
- **The market's ex-ante differentiation of successful campaigns (10.7% vs 2.6%)** is the cleanest empirical statement of what our model's price formation does: the post-disclosure price = probability-weighted outcome values. If our model delivers this as an equilibrium property, K&Z is the fact to cite.
- Their HF-vs-other contrast shows "voice" has (at least) two technologies — payout discipline vs. investment redirection — supporting a model where voice content matters, not just voice vs exit.
- Their takeover non-result for HF (acquired vs not: same announcement return) is a *counterpoint* to G&S — the takeover-only view is contested even in 2009; our model can position itself as reconciling: premia capitalize *expected* takeover gains (G&S's arithmetic) while voice has stand-alone value conditional on intent (K&Z, Gantchev's robustness).
- One-year drift (+11%/+18%) without reversal is the announcement-window fact any disclosure/inference model must not contradict (no post-event reversal = information, not price pressure).

---

## 6. Becht, Franks, Grant & Wagner (2017), "Returns to Hedge Fund Activism: An International Study," *RFS* 30(9), 2933–2971.

**Access:** ECGI Finance WP 402/2014 (May 2017, marked RFS-forthcoming; structurally identical to the published version). Read in full.

**Research question.** First cross-country study (23 countries): how do ownership structures and legal/institutional environments shape the incidence, outcomes, and returns of (publicly observable) hedge-fund activism?

**Methodology / data.** **1,740 publicly disclosed activist engagements, 2000–2010, 23 countries** (US 1,125, Japan 184, UK 165; ≥20 also in DE, IT, FR, KR, NL, CA); 330 activist funds; hand-collected for Asia/Europe/Canada; **13D Monitor** (commercial) for the U.S. Outcomes (board changes, payout, restructuring, takeover) identified via multi-language news searches (no 13D-equivalent abroad) with standardized taxonomy; FactSet/Lionshares for institutional ownership (Ferreira–Matos method; domestic/foreign-US/foreign-non-US splits); FactSet Fundamentals; CRSP/Datastream prices; country variables: disclosure thresholds, Djankov et al. (2008) anti-director rights, Aggarwal et al. (2009) G44 governance, rule of law, common-law dummy. Methods: country-specific market-model CARs around disclosure and outcome announcements; probit engagement likelihood; calendar-time FF4/Carhart alphas on monthly-rebalanced portfolios of ongoing engagements (EW and VW); wolf-pack = ≥2 disclosed HFs in the same engagement.

**Key results (all estimated).**
- *Incidence:* activism tracks **institutional ownership, especially foreign-U.S. institutional ownership** (≈2× the domestic-ownership coefficient; vs. foreign non-U.S. by 2.5–4.5×); domestic institutions *dampen* activism in Japan and Italy. Size not binding internationally (contrast BJPT). Targets: value tilt (low M/B, high cash, low investment, higher payout). Country level: more activism where rule of law is strong, **where disclosure thresholds are LOW** (relative to listed-firm counts, activism is densest in non-common-law, weaker-governance developed markets — IT, NL, DE, CH).
- *Stakes:* average 11% everywhere (US 11%, JP 13%, UK 13%); wolf packs aggregate 13.4% vs 8.3% solo.
- *Disclosure returns:* **US 7.0% / Asia 6.4% / Europe 4.8%** (−20,+20), with post-disclosure drift and >80% abnormal turnover; declining over time in North America (10.5%→5.8%), rising in Europe. **Wolf packs 13.8% vs 6.3% solo** — and not because of bigger stakes (residualized wolf-pack dummies still +6.4–7.0pp). **Domestic engagements 7.0% vs foreign 3.6–3.8%.**
- *Outcomes:* unconditional success ≥1 outcome = 53%; **North America 61%, Europe 50%, Asia 18%. Japan = "unfulfilled expectations": high disclosure returns, almost no outcomes** (Bull-Dog Sauce, J-Power; poison-pill thresholds, government refusal of TCI's stake increase). Outcome CARs average +6.4% (Europe 8.8%, NA 6.0%, Asia 2.7% n.s.). By type: takeover-plus-other-outcomes **+18.1%**, takeover-only +9.7%, restructuring +5.6%, board +4.5%, payout ≈ 0. **Multiple outcomes are additive (board 4.5% + restructuring 5.5% ≈ 10%)**; board changes precede takeovers (⅓ into the engagement vs. takeover at ¾; multiple-outcome engagements last ~806 days) — *governance change facilitates the sale*, qualifying G&S's pure "in play" story.
- *Engagement-period alphas (entry→exit):* with outcomes: **+8.0% VW / +1.1% EW annualized**; without outcomes: +2.3% VW (n.s.) / **−9.8% EW**; long-short 10.9–13.9%. Alphas are concentrated in disclosure months and outcome-announcement months; flat in between. Large-target engagements improved over time (targets grew $600M→$3.4B).
- *Wolf packs:* 22% of engagements; outcome probability 78% vs 46%; more of the profitable outcome types; not higher outcome CARs — packs raise the *probability*, not the *prize*.
- *Foreign activism:* domestic outperforms foreign everywhere; for the 24 US funds operating at home and abroad, domestic and foreign success probabilities are **negatively correlated** — the U.S. model doesn't export.
- *Post-2007:* outcome incidence (esp. takeovers) collapses (Europe 10%→3% of ongoing engagements) and stays low — echoes G&S's credit-crunch logic internationally.

**Institutional facts (gold for us).** **Disclosure thresholds vary: 5% in most countries, 2–3% in DE/IT/CH/UK, 10% in Canada** (as of 2000; robustness excluding sub-5% engagements preserves results). EU Takeover Directive mandatory-bid thresholds 30–33%; Section 16(b) short-swing rule and poison-pill ~10% triggers cap U.S. activist stakes; Japan's poison-pill triggers; Section 13(d)(3) "group" definition and the legal gray zone of wolf packs (Coffee–Palia "music fans" vs. concert parties; BaFin's Deutsche Börse non-finding; the Atos Origin concert-party counterexample with separate CARs for first/second/joint disclosure: 7.8%/1.7%/5.5%).

**Referee-facing strengths/weaknesses.** Strengths: unique international panel; outcome-based (not just returns) analysis; threshold/institution variation; wolf-pack measurement. Weaknesses: outcomes from news searches are non-standardized across languages/regimes (they admit it); disclosure-threshold variation is time-*invariant* in the sample (2000 snapshot) — cross-sectional, not a natural experiment; U.S. dominates the panel; FactSet ownership has known coverage biases; engagement alphas condition on the activist's choice to engage (they acknowledge the conditional-optimality point for why country variables don't predict returns).

**Implications for repositioning our paper.**
- **The cross-country disclosure-threshold variation (2%–10%) is the single best external anchor for our R2 "disclosure-attenuation" comparative static.** Becht et al. show incidence responds to thresholds; nobody has tested whether *premia/returns sensitivity to liquidity* varies with thresholds — that is precisely a testable implication our theory generates. This is arguably the strongest "theory-guided empirics" hook this strand provides.
- "Returns only with outcomes; outcomes resolve disclosure-date uncertainty" is direct international support for modeling announcement returns as expectation over terminal states (takeover vs. continuation) — matches our bidder-entry structure.
- Their sequencing fact (board change → takeover; 18.1% vs 9.7%) is evidence *for* a model in which voice changes the probability/terms of a subsequent control transaction — our public-voice branch can be read exactly this way; cite them (and against pure-G&S) accordingly.
- 11% average stake + mandatory-bid thresholds at 30%: institutional justification for our minority-blockholder assumption.
- The Atos concert-party event (sequential disclosures each moving the price) is a natural case study for disclosed-vs-inferred multi-blockholder extensions — note for robustness/discussion, not core.

---

## Cross-cutting synthesis for the repositioning

**A. The canonical fact base our theory can claim to organize (with citations):**
1. Announcement CAR ~7% (US; 4.8–6.4% abroad), no reversal, pre-disclosure run-up ~3% with volume spike in the 10-day filing window (BJPT 2008; BFGW 2017). → our disclosed-vs-inferred split is *the* microstructure of this fact.
2. Announcement price ≈ probability-weighted outcomes: 11pp takeover-probability increase × 30% premium ≈ observed CAR (G&S 2009); market separates eventual successes ex ante (K&Z 2009); returns exist only with outcomes internationally (BFGW 2017). → our model's price = E[terminal values | disclosure] is the theory of these facts.
3. Minority stakes (median initial 6.3–8.3%, max ~9–11%), no within-campaign accumulation (BJPT; Gantchev; BFGW). → justifies fixed-stake static model; stake choice is the ex-ante margin.
4. Voice is costly and sequential: $1.8M/$2.9M/$5.9M per stage; 2/3 quit before demands; 7% reach proxy; success rises with escalation (Gantchev). → calibration magnitudes for our voice-cost parameters and the Quiet/Public margin.
5. Target selection: small, value, high institutional ownership, **higher liquidity** (BJPT Table 3), cash-rich (K&Z). → the liquidity-κ theory must get the targeting sign right (targets liquid), then deliver the premium hump in κ conditional on targeting.
6. Disclosure-threshold variation 2–10% internationally; incidence responds (BFGW). → out-of-sample testing ground for R2.
7. Returns decay with competition/time (BJPT 15.9%→3.4%; BFGW NA 10.5%→5.8%) and collapse when takeover financing dries up (G&S 2007; BFGW post-2007). → equilibrium/comparative-static validation.

**B. Open disagreements our model can arbitrate:**
- G&S (takeover-only) vs. BJPT/K&Z (voice value beyond takeover) vs. Gantchev (objectives, not M&A per se, drive returns net of costs) vs. BFGW (takeovers *preceded by governance changes* are the most profitable). A model where disclosure changes both (i) voice payoffs and (ii) bidder entry can nest the four positions as different parameter regions — a genuine "explain the debate" selling point for a JF/RFS referee.

**C. Data-source playbook for any empirical section we add:** 13D/13D-A/14A/13F (EDGAR, LiveEdgar), 13D Monitor, SharkRepellent, Georgeson (proxy fights), Factiva outcome coding, CRSP delisting codes for takeovers, SDC for M&A, FactSet/Lionshares for international ownership, CISDM/TASS for fund attributes, GINDEX/IRRC for defenses, Amihud for liquidity. All consistent with the project's existing empirics/ EDGAR pipeline.

**D. Referee traps to avoid in our draft:** don't claim announcement CAR = value created (it's probability-weighted expectation — BJPT, K&Z explicit); don't ignore Gantchev's costs when citing "returns to activism"; acknowledge survivor bias in post-event operating results (BJPT §V, G&S §3.2); note sample periods all end ≤2010 (pre-2012 regime shifts: universal proxy did not yet exist, 13D window still 10 days).
