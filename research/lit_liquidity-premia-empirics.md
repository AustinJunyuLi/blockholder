# Literature Brief — Strand: liquidity–premia empirics

**Author:** LitResearcher_LiquidityPremiaEmpirics
**Date:** 2026-08-18 (current session)
**Scope:** The missing empirics strand — what is measured about liquidity, activism disclosure, and takeover premia. Papers: Edmans–Fang–Zur (2013, JFE); Norli–Østergaard–Schindele (2015, RFS); Collin-Dufresne–Fos (2015, JF); Fos (2017, JF); the liquidity→premia literature (Dass–Huang–Maharjan–Nanda 2016/2020 WP → published as Huang–Maharjan–Nanda 2024, JCF; Massa–Xu 2013, **JFQA not JFE**; Officer 2007, JFE); plus the AFS (2022) illiquidity-loading tension.

**Access summary (honesty note — version flags matter here):**
- EFZ 2013, Norli et al. 2015, CDF 2015, Fos 2017: read in full from **working-paper extractions**, not the published versions (`tmp_read/efz2013.txt` = NBER WP 17567; `norli2015.txt` = CCGR WP 1/2014; `cdf_fos_jf2015.txt` = NBER WP 18452, which **lacks** the published JF version's market-maker detection analysis; `fos2017.txt` = July 2015 SSRN draft). Headline numbers below are WP-version numbers; published versions may differ slightly. Flagged per-paper.
- Dass et al.: both versions local (`tmp_read/cicf391.txt` = May 2016 CICF version; `tmp_read/dass2020.txt` = June 2020 ECGI WP 018/2020), read in full. **Publication correction:** published as Huang, Maharjan & Nanda (2024), *Journal of Corporate Finance* 85, 102562 — **without Dass**; JCF intro verified first-hand via web, tables second-hand but consistent with the local 2020 WP.
- Massa & Xu (2013): **JFQA 48(5), 1463–1497** (the task's "JFE" was wrong — corrected). Read first-hand from the LSE OA accepted version. Officer (2007, JFE 83(3), 571–598): **abstract-only, second-hand.**
- AFS (2022, JFE): full model covered in `lit_disclosure-structural-activism.md`; here only the illiquidity-loading facts, extracted from `research/txt/afs_jfe2022.txt`.

---

## 1. Edmans, Fang & Zur (2013), "The Effect of Liquidity on Governance," *JFE* 109(1), 152–177

**Access:** NBER WP 17567 (Nov 2011) full text. **Research question:** does liquidity help governance — via voice (13D) or exit (13G)?

**Design.** No own formal model; organizes the theory conflict (Coffee/Bhide/Maug 2002: liquidity weakens voice; Kyle–Vila/Maug 1998/Kahn–Winton: liquidity aids block formation). Data: 101 activist hedge funds, all initial 13D/13G filings 1995–2010 (1,821 filings → 1,135 filing firm-years: 490 13D / 645 13G) in 88,742 Compustat/CRSP firm-years. Liquidity: −ln(1+Amihud), −ln(1+FHT). Identification: (a) filing event on **lagged** liquidity; (b) **decimalization 2001** (NYSE/AMEX Jan 31, Nasdaq Apr 9), cross-validated by a low-price-stock split (liquidity rose more there) and a changes spec.

**Key numbers (estimated).** (H1) Liquidity **raises block acquisition**: 1 SD liquidity → +0.47 (Amihud) / +0.20 (FHT) pp against a 1.3% unconditional probability. (H3) **Conditional on a block**, liquidity **cuts 13D propensity**: −6.88/−4.97 pp vs 43.2% base — liquidity shifts voice→exit. (H5) Unconditional 13D incidence still **rises** with liquidity (block-formation effect dominates). (H6) 13G filing CAR(−1,+1) = **+0.7%**, but **0.9–1.0% in high-liquidity** vs 0.4–0.5% (ns) in low-liquidity firms — exit disciplines only where the exit threat is credible (price is informative). (H2/H4) The 13G shift loads on high managerial wealth-performance sensitivity (WPS) firms. Price-impact calibration: selling 1% of shares moves price 0.9–1.1% (liquid tercile) vs 2.2–2.4% (illiquid quartile).

**Institutional facts.** 13D within **10 days** of crossing 5% with intent; 13G re-file only on ≥5% change (45 days after year-end for qualified investors); ≥20% forces 13D regardless of intent; NACCO v. Applica makes misstated 13G intent fraud; 53/490 13Ds marked "investment only"; 42/1,112 13G→13D switches.

**Referee-facing.** Strengths: intent-based filing-type measure; decimalization cross-checks. Weaknesses: 13G is consistent with exit *and* no-governance — the discriminating test rests on 322 obs at 10% significance; decimalization is a single time-series shock (2001 confounds); no price-informativeness test despite the theory being about it.

**Implications for us.** The **sign a κ-theory must match: liquidity ↑ activism incidence** (unconditionally), while liquidity shifts the *mode* toward exit. Our Quiet/Public margin is the natural model counterpart of their 13G/13D split; their Table 4 magnitudes are the targeting moments for calibration.

---

## 2. Norli, Østergaard & Schindele (2015), "Liquidity and Shareholder Activism," *RFS* 28(2), 486–520

**Access:** CCGR WP 1/2014 (Apr 2014) full text. **Research question:** is liquidity's role to finance voice (accumulate a stake and recoup intervention costs via informed trading) or to enable exit?

**Design.** Reduced-form, no structural estimation (flag: my pre-assignment expectation of a structural model was wrong). Annual probit of activism incidence on liquidity (Hasbrouck effective cost; Amihud robustness), 1994–2007Q3, NYSE/AMEX/Nasdaq. Sample: 8,783 non-management filings → 998 activism firm-years → **385 contested events** (they deliberately exclude merger-arb and tender-offer filings — 13D samples are "contaminated" by them). Identification: liquidity lagged to t−2/t−4; IV-probit with **decimalization** instrument (post-2001 × pre-period Ln(sales), exploiting that actively traded stocks gained most liquidity) and other-industries' liquidity; instrument–liquidity correlation ≈0.27; exogeneity not rejected for Hasbrouck.

**Key numbers.** Liquidity (t−2) probit coef 10.27 (z=3.30): 10th→90th percentile liquidity raises activism probability **0.33%→0.73%** (+0.40pp ≈ 71% of the 0.56% unconditional); IV: +0.79pp (142%). **Exit-vs-voice margin:** liquidity×overvaluation interaction negative — liquidity's voice effect **halves** for plausibly-overvalued firms (0.68pp at 10th-pct vs 0.33pp at 90th-pct overvaluation, diff p=0.035) — activists trade instead of intervening when there is nothing to fix. **Pre-disclosure accumulation (Table 8–9):** 259 targets with 13D trade data; 76% of activists trade, 95% of 11,518 trades are buys; they acquire **4.25pp = 54% of the final block in the year before announcement**; average trading profit **$1.56M (8.5% return)**; liquidity (t−3) positively predicts the fraction acquired (coef 40.98, t=2.52). Activists hold ~9% at announcement; proxy contests in 86% of events.

**Institutional facts.** 13D Item 5(c) discloses trades over the **60 days pre-filing** (the mechanism for measuring accumulation); Rule 14a-11 adopted 2010, vacated 2011.

**Referee-facing.** Strengths: hand-collected contested-solicitation events; two lag structures + IV; trade-level mechanism evidence. Weaknesses: rare events (<1%); overvaluation proxies admittedly noisy; trades invisible below 5% (95 cases); activism excludes private engagement.

**Implications for us.** This is the **direct evidence that κ funds voice**: liquidity raises activism probability ~2× and the pre-disclosure accumulation share. Their overvaluation interaction is the empirical template for our model's claim that liquidity's effect is *state-dependent* (voice where gains are large, exit/trading otherwise).

---

## 3. Collin-Dufresne & Fos (2015), "Do Prices Reveal the Presence of Informed Trading?," *JF* 70(4), 1553–1582

**Access:** NBER WP 18452 (Oct 2012) full text — **caveat:** sample 2001–2010 (published JF version uses 1994–2007 and adds a market-maker detection exercise not in this WP; numbers below are WP-version).

**Research question.** Do standard liquidity/adverse-selection measures (Kyle λ, PIN, Amihud) detect *identifiable* informed trading? Sample: 1,725 original 13D events, 2001–2010 (from 9,580 filings), no derivatives.

**Key numbers.** **Stakes:** mean ownership at filing **7.68%** (median 6.20%); in the 60-day pre-filing window they buy **3.8% mean / 2.8% median of shares outstanding** (avg $25.6M), over ~15 trading days, at ≈**30% of daily volume**. Post-trigger (crossing 5% → filing): **1.8% of outstanding ≈ 23% of the final stake**, at 0.8%/day vs 0.3%/day pre-trigger; near filing, daily purchases rise to 0.2–0.3% of outstanding, trade probability 30%→50%, share of volume 5%→10–15%. **Prices do NOT reveal them:** on filer trade days λ = 12.35 vs 16.85 (−30%), Amihud −46%, PIN 0.4298 vs 0.5000 (−7pp, t=−10.85); price impact 62→50 bps; both λ and Amihud hit **local minima around the filing date** — the market becomes *measurably more liquid* while the informed trader is in the market. Yet information enters prices anyway: **run-up ~7% over (t−60,t−1), filing-day jump ~3%**, post-filing drift to 13% total (drift absent post-2003). Trade-day market-adjusted return +0.62% vs −0.04%. Average filer profit **$1.13M** on a $30M stake ($0.60M trading + $0.53M on the initial position); replicating portfolio α = 0.09%/day VW (t=3.04). Filers trade more aggressively when liquidity is high and on down-market days.

**Institutional facts.** 10-day filing window; 60-day Item 5(c) lookback; triggers: crossing 5%, group formation, ±1% for existing filers.

**Referee-facing.** Strengths: ex-ante identified informed traders at ~30% of volume — detection should be maximal, and still fails, consistently across nine measures. Weaknesses: filers *choose* liquid days (acknowledged); the "private information" is own future activism (self-referential); measures may miss short-lived info.

**Implications for us.** **This is the load-bearing fact for our inference architecture**: order flow carries no detectable adverse-selection signature during accumulation — the market learns from the *disclosure event*, not from order-flow inference. Our κ-inference split must therefore generate "prices rise smoothly (price pressure), but standard liquidity measures do not deteriorate." The run-up/jump decomposition (7%/3%) and the $1.13M profit bound are the calibration targets for the value of the 10-day window — and hence for the Feb-2024 shortening to 5 business days.

---

## 4. Fos (2017), "The Disciplinary Effects of Proxy Contests," *JF* 72(2), 655–690

**Access:** July 2015 SSRN draft full text. **Correction to the assignment brief:** this draft contains **no close-vote RDD and no ex-post real-effects-by-vote-outcome analysis** (that design belongs to other papers); the author explicitly concedes "finding an instrument for proxy contests at the firm level is hard, if not impossible" (fn 11). Treat any RDD characterization as unverified for the published version too.

**Design.** Census of 1,061 proxy contests 1994–2012 (873 firms) hand-collected from EDGAR PREC14A/DEFC14A; Carhart CARs −24m/+24m; probit of contest incidence (N=58,405 firm-years); matched-firm comparisons; within-firm regressions on the *estimated* contest probability P̂C (the **threat** design).

**Key numbers.** Frequency: 56/yr (68/yr post-2006) vs 17/yr in 1979–1994 — contests substituted for hostile takeovers. Hedge funds sponsor 57% (70% post-2002). Outcomes: 47% voted (dissidents win 26%/lose 21%), 25% settled, 15% withdrawn, **6% delisted/taken over**. Stated goals: undervaluation 41%, governance 39%, strategy 28%, **sale of target 27%**. **Returns:** pre-announcement CAR **−10%** by month −2 (targeting follows underperformance); announcement (−1m,+1m) CAR **+6.5%**, no reversal; sale-goal contests +10% announcement but negative post-drift; business-strategy contests recover from −20% to −10% by +24m; governance/capital-structure goals: small pop, no long-run gain. **Liquidity sign (again positive):** Amihud illiquidity coef −0.0944 (APE −0.0013, t=−2.23) — 1 SD liquidity raises contest probability 0.13pp vs 0.55% unconditional; targets are more liquid than matches (0.458 vs 0.676) and become more liquid pre-contest. **Threat effect:** per unit P̂C, leverage +3.1pp, cash −2.7pp, investment −12.8pp, dividends +9.5pp — and nearly identical for non-targets: the mere *threat* disciplines.

**Implications for us.** Voice here is a *control-adjacent* instrument (27% of contests seek a sale; 6% end in takeover) — supports our bidder-entry margin being downstream of public voice. The threat regressions are the evidence that voice need not be consummated to move real policy — our Quiet-voice branch has an empirical counterpart. The +6.5% announcement CAR with a −10% pre-drift contrasts with 13D run-ups (CDF): contests are *news about underperformers*, 13Ds are *news about accumulation* — different price objects our model should not conflate.

---

## 5. Liquidity → takeover premia: the canonical empirics

### 5a. Dass–Huang–Maharjan–Nanda (2016 WP / 2020 ECGI WP 018) → published as Huang–Maharjan–Nanda (2024, *JCF* 85, 102562, without Dass)

**Access:** both WPs read in full locally; JCF version verified via intro (first-hand) — numbers below from the local WPs. **Hypothesis (acquisition currency):** liquid acquirer stock is better payment currency, especially when the target is less liquid; targets accept **lower premia** for more liquid stock. A simple bargaining model delivers: premium falls in acquirer liquidity, rises in target liquidity (stock deals only).

**Design.** SDC/CRSP/Compustat; 2016 version: 4,966 deals 1985–2012 (2,501 public-target; premium N=2,306); 2020 version: 10,627 deals 1985–2018 (3,032 public-target; premium N=2,837); mean premium 25.9%/26.8%. Identification **changed across versions**: 2016 used Russell 1000/2000 reconstitution IV (1st-stage R2000 coefs 0.100**/0.080***; 2nd-stage premium on instrumented acquirer liquidity −0.111***, stock deals only, tiny N≈126–131); **2020 drops Russell** and uses two liquidity policy shocks — 1997 tick-size reduction ($1/8→$1/16) and 2001 decimalization — with PSM-DID (671–1,024 matched pairs), changes regressions, and low-price stratification (LowPrice×Decimal −0.137*** for stock-deal premia, null for cash).

**Key numbers (the premia–liquidity elasticity anchor).** Stock deals: relative (acquirer−target) liquidity coef −0.021** (Amihud) / −0.050*** (spread); **1 SD higher acquirer−target liquidity difference ⇒ premium −4.5 to −4.7pp ≈ 17% of the 26.8% mean**; cash deals null throughout (the falsification that isolates the currency channel). Acquirer liquidity negative, target liquidity positive in separate regressions. Acquirer 3-day CAR +0.47–0.64% per 1 SD (mean −3.65%); 1 SD liquidity raises P(acquisition) by +3.2pp and P(stock deal) by +2.1pp; stock-payment share +4.5pp per 1 SD. Target blockholders weaken the premium sensitivity (interaction +0.037***/+0.101*** — each blockholder cuts it by 3.7–10.1pp). Pre-deal, acquirers do stock splits and more earnings guidance to boost liquidity. **Run-up caveat:** premium measured vs price 2 days pre-announcement; the pre-announcement run-up itself positively predicts premia (coef 0.078–0.129).

### 5b. Massa & Xu (2013), "The Value of (Stock) Liquidity in the M&A Market," *JFQA* 48(5), 1463–1497

**Access:** LSE OA accepted version, read first-hand. **Opposite-signed complement to 5a.** 4,691 completed US acquisitions of public targets, 1987–2007; liquidity = PC1 of volume/turnover/Amihud/spread; OLS/probit + Heckman (no quasi-experimental IV — the referee-facing weakness). Key numbers: 1 SD higher **target** liquidity ⇒ **+10% higher offer premium** (public acquirers; premium vs target MV **63 days pre-announcement**), +2% 3-day CAR, +5% long CAR, +2.4pp completion probability; private acquirers pay significantly smaller liquidity premia; effect stronger in high-liquidity times; institutional ownership strengthens it. No cash/stock difference in their premium tests. Channel: liquid targets are worth more to *public bidders and institutions* (post-merger portfolio liquidity), i.e., a **demand/bidding-competition** channel.

### 5c. Officer (2007), "The Price of Corporate Liquidity: Acquisition Discounts for Unlisted Targets," *JFE* 83(3), 571–598

**Abstract-level only (second-hand):** unlisted targets sell at **15–30% discounts** vs comparable listed targets — liquidity proxied by listing status. Use as the extreme-illiquidity bound of the premium–liquidity gradient.

**Reconciliation for the brief.** The two signs are consistent once the objects are distinguished: premium **rises in target liquidity** (Massa–Xu demand channel) and **falls in acquirer−target liquidity difference** (currency channel). Both papers: cash deals null, blockholder presence attenuates. Neither addresses 13D windows or pre-disclosure run-ups.

---

## 6. The AFS (2022) tension — illiquidity loads positively on expected returns for BOTH filing types

From `research/txt/afs_jfe2022.txt` (full model in the disclosure-structural brief; facts here are first-hand from the text). In the structural estimation (Table 3A, preferred spec), **Amihud illiquidity loads positively and nearly identically on expected announcement returns for 13D and 13G: β_D = 0.021***, β_G = 0.019*** (SE 0.002); with Amihud SD 0.426, 1 SD ⇒ ≈+0.9pp on both** (my arithmetic from their Table 2; they do the SD exercise only for B/M). Authors' interpretation (§5.1): "investments in less liquid securities appear to be compensated by higher expected returns regardless of the filing schedule, consistent with an illiquidity premium as in Amihud (2002)," while "stock market liquidity facilitates Schedule 13D or 13G filings." Because β_D ≈ β_G for all firm characteristics, **illiquidity is purely stock-picking — it carries zero treatment effect**; only investor experience separates μ_D from μ_G. Reduced-form contrasts: OLS on 13D returns gives only 0.004** for Amihud; probit of 13D-vs-13G on Amihud = 0.172*** (illiquid firms more likely 13D targets); mean Amihud 0.47 (13D) vs 0.23 (13G). Headline decomposition confirmed: mean 13D announcement return 6.34% = treatment 4.77% (**75.2%**) + stock-picking 0.77% (12.2%) + selection 0.80% (12.6%); 13G mean 0.59%. **No counterfactual varies liquidity or the disclosure window.** Note: their CAR starts at t−30 explicitly because of CDF's pre-filing impact — the run-up is folded *into* "announcement returns," not separated.

**Why this is a tension for us.** If a repositioned model predicts premia/announcement-return sensitivity to liquidity κ *through the activism/disclosure channel*, AFS's headline says the activist-specific component is liquidity-neutral in levels, while stock-picking is illiquidity-tilted. Our empirical spec must therefore separate (i) the Amihud level premium (common), (ii) targeting selection (illiquid firms), and (iii) the treatment/takeover-premium elasticity (the object our κ comparative statics are about).

---

## Synthesis

### A. Moments a repositioned theory must match

1. **Sign of liquidity in targeting: positive.** EFZ: +0.47pp per SD vs 1.3% base (blocks); Norli: 0.33%→0.73% activism probability 10th→90th liquidity, IV-confirmed; Fos: +0.13pp vs 0.55% base; AFS reduced form: illiquid firms are *more* likely 13D (selection) even though liquidity facilitates filings — the model must say which margin dominates. A κ-hump in *premia* must coexist with a roughly monotone liquidity→targeting relation.
2. **Mode split: liquidity shifts voice→exit conditional on a block** (EFZ −6.88pp on 13D share; Norli: liquidity's voice effect halves for overvalued firms). Our Quiet/Public margin is exactly this object.
3. **Run-up vs jump:** ~7% run-up over 60 days vs ~3% filing-day jump (CDF); activists buy 3.8% of outstanding pre-filing, 1.8% post-trigger, at 30% of daily volume — **while measured adverse selection falls**. The market learns from disclosure, not order flow. Any inference-based model must reproduce "smooth price pressure, no detectable Kyle-λ signature."
4. **Stakes:** 6.2–7.7% at disclosure (CDF/EFZ); ~9% at announcement (Norli); 54% of the block accumulated in the pre-announcement year at 8.5% trading profit.
5. **Announcement returns:** 13D ~6.3% (75% treatment — AFS), 13G ~0.6–0.7%, higher for liquid targets (EFZ); proxy contests +6.5% (−1,+1m) on a −10% pre-drift (Fos).
6. **Premia–liquidity elasticity:** +10% premium per SD of *target* liquidity (Massa–Xu, public bidders); −4.5pp per SD of *acquirer−target* liquidity difference in stock deals, ≈17% of the mean premium, cash deals null (Dass/Huang et al.); unlisted discount 15–30% (Officer, second-hand). Target blockholders attenuate the premium sensitivity.
7. **Level premium:** expected returns load +0.9pp/SD on Amihud for *both* filing types (AFS) — a control variable any premium–liquidity regression must partial out.

### B. Empirical design these papers imply for "premia became less liquidity-sensitive after the Feb-2024 13D acceleration"

The natural experiment: SEC 13D modernization (initial filing 10 calendar days → **5 business days**, compliance 2024-02-05). The literature hands us the pieces:
- **Baseline regression** (Dass/Huang et al. template): premium vs target price ≥42–63 days pre-announcement (Massa–Xu's 63-day base avoids run-up contamination — important, since run-up predicts premia at 0.078–0.129 and the run-up is itself the disclosure window's product); premium_it = β·Liq_it + β₂·Liq_it×PostFeb2024 + controls + FE. Our R2 predicts β₂ has the sign that flattens β (attenuation of κ-sensitivity).
- **Treatment intensity split:** the shock binds only for deals preceded by 5% crossings with control intent — interact with an activist-exposure measure (prior 13D/13G from the repo's EDGAR pipeline, wolf-pack presence, G&S-style "in play" targets); non-activist deals are the within-period placebo, cash deals the within-deal placebo (Dass's falsification logic).
- **Run-up/jump re-measurement** (CDF template): the 5-day window should shift returns from the (t−10,t−1) run-up into the filing-day jump; CDF's 7%/3% decomposition on 2001–2010 is the pre-period benchmark; their finding that λ/PIN/Amihud *fall* during accumulation says not to expect the window shortening to show up in adverse-selection measures — measure returns, not liquidity proxies.
- **Selection correction** (AFS template): the filing-type choice is endogenous and illiquidity-tilted; a Heckman/structural correction or at minimum 13G-control comparisons are needed before attributing elasticity changes to disclosure rather than to who files.
- **Out-of-sample:** cross-country threshold variation (3% UK/DE/ES/IT/NL, 5% US/FR/JP/AU, 10% CA; Becht et al. 2017 data) as a levels test of the same comparative static; Massa–Xu's public/private-acquirer split is the template for elasticity-difference tests.
- Data: all inputs match the repo's existing stack (EDGAR 13D/G pipeline; CRSP daily for Amihud/turnover; SDC for premia).

### C. Unresolved tensions the paper could arbitrate

1. **Sign of liquidity in premia:** target liquidity *raises* premia (Massa–Xu demand) but acquirer−target liquidity difference *lowers* them (currency). A model with bidder entry + a blockholder can say which object κ maps to — nobody has unified the two.
2. **Illiquidity level vs treatment:** AFS find a positive illiquidity loading on expected returns for *both* filing types (pure stock-picking) while EFZ find 13G returns *higher for liquid* targets. Is the liquidity–return relation an Amihud level effect, a targeting selection effect, or a treatment effect? Our decomposition (disclosed/inferred branches) is built to answer exactly this.
3. **Prices reveal nothing, yet run up 7%:** CDF's negative result on λ/PIN sits uneasily with the large pre-filing run-up — information enters via price pressure that standard measures miss. A model where disclosure (not order-flow inference) moves the posterior explains both facts; the tension is currently unexplained.
4. **Voice without consummation:** Fos's threat regressions (policies move for non-targets) vs G&S's takeover-only returns — how much of the premium is ex-ante probability-weighting of a control event vs realized intervention? Our bidder-entry channel nests both.
5. **Which window matters:** EFZ/CDF show the 10-day window is where accumulation rents live ($1.13M/event); AFS show filing-*type* choice is the first-order margin; no paper measures how premia respond when the window halves (Feb 2024). That is the empty empirical cell our theory already speaks to.
