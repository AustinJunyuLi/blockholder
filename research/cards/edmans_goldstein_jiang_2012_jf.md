# Edmans, Goldstein & Jiang (2012) — "The Real Effects of Financial Markets: The Impact of Prices on Takeovers"

**Venue / status:** Journal of Finance 67(3), 933–971, June 2012 (published)
**Full text from:** `research/txt_extracts/edmans_goldstein_jiang_2012_jf.pdf` (Wiley published version, 39 printed pages, pp. 933–971) · **Reader:** opus · **Read:** full text, 39 pages (body + Appendix A data + Appendix B likelihood + references)
**Page numbering:** printed *Journal of Finance* pages (933–971), verified against the running heads. PDF page 1 = printed p. 933.
**Type:** empirical (simultaneous-equations / control-function IV)   **Role for us:** anchor (the canonical "prices → takeovers" causal estimate) and antecedent for the feedback logic

> **Premise correction for the positioning stage.** The task brief described this paper as "theory + empirics" with "propositions with PROVED labels". It is **not**. A search of the full text returns **zero** occurrences of *proposition*, *theorem*, *lemma*, *corollary* or *proof*. Section I is titled "Model Specification" but it is an **econometric** specification — equations (1)–(14) are estimating equations (quantile/CLAD frontier, a bivariate probit-with-endogenous-regressor system, a control function, an FIML likelihood), not a game with equilibrium objects. The "trigger" and "anticipation" effects are named reduced-form channels, not derived results. **No result in this paper can carry a PROVED label.** The paper itself says the theory does not yet exist (Q6, Q7 below).

## 1. Question

Does a low market valuation cause a firm to become a takeover target? Prior work (Palepu 1986; Ambrose–Megginson 1992; Rhodes-Kropf–Robinson–Viswanathan 2005; Agrawal–Jaffe 2003; Bates–Becher–Lemmon 2008; Cremers–Nair–John 2009) finds a weak or absent link, casting doubt on the disciplinary-takeover story. EGJ argue the link is hidden by three endogeneity problems — an **anticipation effect** (forward-looking prices are inflated by takeover probability, reverse causality), omitted variables (a technology shock raises both price and bid probability), and measurement error (raw valuation ≠ undervaluation). They fix the measurement error with a "discount to frontier value" and the simultaneity with an instrument for price that is orthogonal to fundamentals.

## 2. Model / data and method

**No theory model.** The object estimated is a two-equation simultaneous system, eqs. (8)–(9), p. 944:

- `Discount = γ₀X + γ₁Z₁ + γ₂Z₂ + δξ + η′`, and `Takeover* = μ₁Discount + μ₂X + μ₃Z₁ + ξ`, with `Takeover = 1{Takeover* > 0}`. `δ < 0` is the anticipation shrinkage; `ρ = corr(η, ξ) = δσ²_ξ < 0`, so OLS/probit **under**estimates μ₁ (p. 944).
- Estimation: Rivers–Vuong (1988) control function / FIML (Appendix B, eq. B3, pp. 967–968). The anticipation coefficient δ is recovered ex post by regressing residual discount (eq. 11) on the Gourieroux et al. (1987) generalized residual ξ̂ (eq. 14, p. 959).

**Left-hand-side construction — the "discount".** `Discount = (V* − V)/V*` where the *frontier value* V* is the (1−α)th percentile valuation among peers, estimated by Koenker–Bassett (1978) quantile regression with Powell's (1984) CLAD non-negativity constraint (eqs. 1–3, p. 942). Two valuation metrics (Q = enterprise value / book value; EV/Ebitda) × two frontier definitions (three-digit-SIC industry peers; firm characteristics — SalesRank, R&D, ATO, MktShr, Growth, BetaAsset in tercile ranks, plus Age and Age²) = **four Discount measures**. α is **calibrated to 0.20** from the median takeover premium: pooling within three-digit SIC and adding 38% to targets' pre-acquisition equity value puts the median target at the **77th percentile** of its industry, rounded to the 80th (p. 942).

**Instrument.** `MFFlow` = mutual-fund price pressure from *hypothetical* (not actual) trades mechanically implied by investor flows, summed over the four quarters of a calendar year (Appendix A, p. 967). Only funds with `Outflow_{j,t} ≥ 5%` of prior-quarter total assets enter; sector funds are excluded (8.5% of funds, 8.7% of aggregate absolute flows, fn. 16 p. 952); the dollar flow is scaled by the stock's dollar trading volume. Figure 2 (plotted p. 952, described p. 953) shows no pre-event price decline, a large and persistent post-event drop, and **full reversal only by month 24**.

**Sample.** SDC M&A, **1980–2007**. All bids (completed or not); excludes partial stakes, minority squeeze-outs, buybacks, recapitalizations, exchange offers, and deals with a pre-bid stake > 50% or a final holding < 50% → **13,196 deals**; requiring CRSP/Compustat and dropping financials (SIC 6000–6999) and utilities (SIC 4000–4949) → **6,555 deals** (p. 946). Universe = all non-financial, non-utility Compustat/CRSP firm-years; summary stats N = 118,942 (Table I Panel B, p. **948**; Panel A definitions p. 947). Regression N ≈ **100,160/100,166** (Q) and **79,100/79,103** (EV/Ebitda). Unconditional annual takeover frequency **6.18%–6.24%**. Standard errors clustered at the firm level (Takeover equation) and double-clustered by year and firm (Discount equation).

**Where liquidity enters.** `Amihud` (Amihud 2002 illiquidity) is a **Z₁ control**, not the object of study: it "impacts both Discount and Takeover" because illiquidity "deters toehold accumulation" (Betton–Eckbo 2000) and depresses valuation (p. 951).

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where (page / table) |
|---|---|---|---|
| R1 | Without instrumentation, a 1 pp rise in Discount raises takeover probability by 0.8–3.3 bp; an interquartile change gives 0.4–1.6 pp against a 6.2% base rate | ESTIMATED | p. 953; Table II Panel A, p. 954 (Discount coef. 0.282***, t = 15.34, dPr/dX 3.28%, IQ 1.58%, down to 0.070***, t = 4.30, IQ 0.41%) |
| R2 | **Headline trigger effect:** instrumented, a 1 pp rise in Discount raises takeover probability by **11.6–15.9 bp**; an interquartile change gives **5.65–7.55 pp** vs. 6.2% unconditional | ESTIMATED | p. 956; Table III, pp. 957–958 (1.371***, t = 4.24, dPr/dX 15.66%, IQ 7.55%; 0.989***/3.67; 1.512***/4.51; 1.101***/3.64) |
| R3 | The instrument is not weak; the system is not exogenous — both rejected in all four specifications | ESTIMATED | Table III p. 958: Stock–Yogo F = 95.38 / 167.15 / 38.00 / 91.39, all p = 0.00; exogeneity Wald 7.71 / 8.21 / 7.93 / 8.04, p = 0.01 / 0.00 / 0.01 / 0.01 |
| R4 | **Anticipation effect:** shocks to takeover propensity shrink the discount; headline δ̂ = −0.163*** (t = −32.40); across both tables δ̂ runs −0.140*** to −0.381*** | ESTIMATED | Table IV, p. 960 (−0.163 / −0.140 / −0.266 / −0.193); Table V Panel B, p. 965 (−0.272 / −0.343 / −0.375 / −0.381) |
| R5 | For the average firm a 1 pp rise in takeover probability cuts the discount by **≈1.2 pp**, of which only **0.4 pp** is attributable to next-year anticipation given a ~40% average premium; the residual 0.8 pp is future-year anticipation or omitted variables | ESTIMATED (the 1.2) + ASSERTED (the 0.4/0.8 split, a back-of-envelope decomposition, not separately estimated) | p. 960 |
| R6 | **Illiquidity decomposition:** a one-unit rise in Amihud raises Discount by 8.38 pp, of which 1.69 pp (≈20%) works *indirectly* through reduced takeover probability and 6.69 pp directly on price | ESTIMATED (inputs) / ASSERTED (the decomposition arithmetic) | p. 961 |
| R7 | Amihud illiquidity **lowers** takeover propensity in every specification (deterring toehold accumulation) | ESTIMATED | Table II p. 954 (−0.034***, t = −4.05, to −0.023***); Table III p. 958 (−0.124***, t = −4.50, to −0.050***) |
| R8 | The trigger effect is stronger for financially driven takeovers (LBOs / financial sponsors): IQ change → 2.11–2.29 pp vs. an unconditional 1.38–1.45% | ESTIMATED | pp. 963–964, Table V Panel A |
| R9 | Discount correlates positively with the takeover premium (7.2%), acquirer return (1.8%) and total return (7.4%); the Premium–Discount relation "is still far from one" | ESTIMATED | pp. 961–962 (regressions themselves are in the Internet Appendix, not in the article) |
| R10 | Robust to α ∈ [0.10, 0.30]; to dropping firms within 2.5% of a tercile cutoff (IQ 6.0–7.8%); to removing aggregate and industry merger waves; to defining Takeover as completed deals only (76.5% of the sample) | ESTIMATED (tabulated in the Internet Appendix, not the article) | p. 963 |
| R11 | Institutional ownership (`Inst`) **raises** takeover propensity — 0.196*** (t = 4.16) instrumented, and 0.469*** in the financially driven subsample | ESTIMATED | Tables III p. 957, V p. 964 |

## 4. Institutional facts used

- **Takeover premium magnitudes.** Median takeover premium **37%–39%** over 1980–2002 (Andrade–Mitchell–Stafford 2001); bidder returns ≈ 0, so targets capture nearly all gains (Jensen–Ruback 1983; Betton–Eckbo–Thorburn 2008). **38%** is the number added to targets' pre-acquisition equity value to calibrate α = 0.20 (pp. 941–942); **~40%** is the average premium used in the anticipation decomposition (p. 960).
- **Cross-check on α:** ~20% of closed-end funds trade at a premium to NAV, 80% at a discount (Bradley et al. 2010, p. 942).
- **Deal filters:** SDC "Form of the Deal"; > 50% pre-bid stake and < 50% final holding excluded (p. 946). Financials and utilities excluded "because takeovers are highly regulated in these industries" (p. 946).
- **Data sources:** SDC (M&A), CRSP (returns, age, Amihud), Compustat (accounting), Thomson Reuters/CDA Spectrum (institutional holdings, mutual-fund holdings), CRSP (fund flows).
- **(added by verifier) Blockholders are in the paper's justification, not its model.** `Inst` is included partly because "Mikkelson and Partch (1989) and Shivdasani (1993) find that block ownership increases the probability of a takeover attempt", and because institutional ownership concentration "facilitates coordination among shareholders, thus reducing the Grossman and Hart (1980) free-rider problem in takeovers" (p. 950). That is the only economic role blockholding plays here — and it is the exact mechanism our premium wedge sits on.
- **(added by verifier) Activism × valuation simultaneity already has a published precedent they cite.** Bradley et al. (2010) "show that the discount at which a closed-end fund is traded affects and reflects the probability of activism at the same time" (p. 938), and "activist shareholders are more likely to target closed-end funds that are trading at deeper discounts" (p. 939). This is EGJ's own analogue of our object in a setting with an observable frontier value (NAV).
- **(added by verifier) Premium pass-through fact.** Schwert (1996), cited at p. 936 fn. 3, finds "the offer price increases almost dollar-for-dollar with the target's pre-bid runup"; EGJ note "He does not explore the effect on takeover probability." Relevant to the premium wedge and to what a runup does to the bid.
- **(added by verifier) Takeover base-rate time series.** Figure 1, p. 949: annual takeover frequency ranges "from about 3% to above 8%" over 1980–2006, and aggregate Discount and takeover frequency move together except in 2002–03.
- **(added by verifier) Premium measurement window.** `Premium` = the percentage increase in the target's stock price over the **[−60, 0] window** relative to the announcement date (p. 961; robustness to [−40, 0] and to the actual premium paid, fn. 21).
- **(added by verifier) The Amihud variable is not reconstructable from the article.** Table I Panel A (p. 947) defines `Amihud` as the "yearly average of the **square root of (Price×Vol)/|Return|**" — the *reciprocal* of Amihud (2002) illiquidity, and with a square root — and Panel B (p. 948) reports **no summary statistics for Amihud at all**. So the units behind "a one unit increase in Amihud" (the 8.38 / 1.69 / 6.69 decomposition, R6) cannot be recovered from the printed paper. Cite the ≈20% share, not the levels.
- **NOT used, anywhere in the paper:** Schedule 13D, the 5% threshold, any filing window, any disclosure rule. `13D` and `Schedule` return **zero hits** in the full text; `disclos*` occurs exactly once, in "previously disclosed portfolio" describing mutual-fund holdings (p. 951). `blockhold*` occurs only in the reference list. Toeholds appear only as the channel through which Amihud is signed (p. 951).

## 5. Referee-facing strengths / weaknesses

**Strengths:**
- The instrument is genuinely non-fundamental and its first stage is strong (F = 38–167), with a documented no-pre-trend, full-reversal-by-24-months price path (Fig. 2, p. 952) — the closest thing in this literature to an exogenous price shock.
- The exclusion restriction is defended on three explicit named threats (fund skill, fund performance, sector concentration), two of which are argued to *attenuate* rather than inflate (p. 951–952), plus sector-fund exclusion and year fixed effects.
- The frontier-value measurement innovation is independently useful and is calibrated to an institutional fact (the 38% median premium) rather than chosen freely.
- The gap between Table II and Table III (a 5–10× jump) is itself the paper's evidence that the anticipation effect is real, and it is corroborated by a formal exogeneity test.

**Weaknesses / open flanks:**
- **No mechanism, no theory.** The paper cannot say *why* prices move takeover probability, and admits the required theory does not exist (Q6, Q7).
- **One average effect for the whole sample.** By construction (residual-on-residual regression), the trigger and anticipation coefficients cannot be interacted with governance or any other Z₁ variable (p. 961, fn. 20, and p. 966). No heterogeneity — which is exactly the margin a liquidity × disclosure paper needs.
- Governance indices (G-index, E-index) drop two-thirds of the sample and are relegated to the Internet Appendix (fn. 15, p. 950).
- Only 0.4 of the estimated 1.2 pp anticipation shrinkage is attributable to next-year anticipation; the authors themselves call the pinned-down part "economically modest" (p. 938).
- Key robustness (α sweep, tercile-cutoff exclusion, merger waves, completed deals, the Premium/AcquirerRET regressions) lives in an Internet Appendix, not the article — none of it is independently checkable from this PDF.
- The frontier-value X variables are not fully exogenous to acquirers; the tercile-rank device is a mitigation, not a fix (pp. 940–941).
- **(added by verifier) They tried and rejected the class of instrument our design would reach for.** p. 959: "Valid instruments could come from the 'supply side,' such as capital inflows to buyout funds or interest rates that proxy for the ease of financing. However, such instruments suffer from low power because they fail to generate variation in the cross-section." A single dated rule change (Feb-2024) is exactly a supply-side, no-cross-section instrument. Our design must supply the cross-sectional variation EGJ say is missing (e.g. pre-period liquidity, or distance to the 5% threshold), or it inherits their stated power problem.
- **(added by verifier) The one governance result they do report is a null.** fn. 15, p. 950: in the subsamples where they exist, the entrenchment index is "uncorrelated with takeover probability in equilibrium" and the shareholder-rights index likewise under EV/Ebitda; both are positively correlated with Discount. Bates, Becher, and Lemmon (2008) similarly find GIM antitakeover measures do not reduce takeover likelihood (fn. 15 cont., p. 951).

## 6. What they do NOT do (scope boundary)

**OBJECT:** takeover *likelihood* (a firm-year binary bid indicator) — **not** the takeover premium, not bidder entry conditional on a blockholder, not campaign success. The premium enters twice, both times instrumentally: as the 38% calibration input for α, and as a 7.2% correlation in §IV.A. There is **no** premium regression in the paper.

**MARGIN:** **none.** No disclosure rule of any kind — no 13D, no 5% threshold, no filing window, no threshold or window margin. The 5% that does appear is the mutual-fund outflow cut-off (Appendix A, p. 967), unrelated to ownership disclosure.

**IDENTIFICATION:** IV / control-function on a cross-firm-year panel, 1980–2007, with a fund-flow price-pressure instrument. No DiD, no event study, no rule change, no structural estimation. Liquidity (Amihud) is a **control**, never a treatment and never interacted.

**Declared out of scope, in their words:**
- Mechanism: *"While our paper demonstrates that market prices have an effect on takeover probability, it is silent on the mechanism behind this effect."* (p. 965)
- Theory: *"Our findings thus suggest the need for new takeover theories to explain why market prices should impact acquisition likelihood."* (p. 966); and earlier, *"to date the possibility of asymmetric learning has not yet been incorporated into the theoretical takeover literature"* (p. 936).
- Heterogeneity: *"we are only able to estimate an average trigger effect and an average anticipation effect across the full sample, rather than allow these effects to depend on firm characteristics such as governance"* (p. 966).
- Activism: named only as an *untested extension* — *"The feedback loop may apply to other corrective actions, such as CEO replacement, shareholder activism, and regulatory intervention."* (p. 938).
- Heterogeneity, again: *"In future research it would be interesting to extend our analysis to study the firm-level determinants of these effects."* (p. 966).

**(added by verifier) They do not just call for a theory — they specify what it must contain (p. 966).** Before the "need for new takeover theories" sentence, EGJ give an argument that *no symmetric-information model can produce their result*: under free-riding (Grossman and Hart (1980)) the bidder must pay the potential value V\* regardless of the current price; even with bidder bargaining power the parties bargain over the *underlying* Discount₀, not the observed Discount; if a high valuation is fundamental news both sides agree a higher price is warranted, and if it is mispricing both sides agree it should not raise the price — so "Regardless of the source of a high market valuation, it has no effect on takeover likelihood if viewed symmetrically by the bidder and the target." The vacancy they declare is therefore precisely an **information-partition** vacancy, not a generic modelling gap.

## 7. Implications for our position

**What they occupy.** OBJECT = takeover likelihood (bidder entry). MARGIN = none. IDENTIFICATION = fund-flow IV, 1980–2007 US panel. That is one cell of the (object × margin × identification) grid, and it is a crowded, well-defended one.

**What they leave open — three pieces of whitespace this card certifies:**

1. **The disclosure rule is untouched.** EGJ never mention Schedule 13D, a stake threshold, or a filing window. Our **threshold margin** and **window margin** are both empty ground relative to this paper. The Feb-2024 acceleration post-dates their 1980–2007 sample entirely.
2. **The blockholder is absent from the mechanism.** Their bidder responds to a *price*, and the price moves because of *anonymous mutual-fund flows*. Nobody in EGJ chooses whether to be flagged. Our **partition** (flagged vs. pooled) has no counterpart here. Institutional ownership enters only as a scalar control `Inst`, and it *raises* bid probability (R11) — a fact worth citing when we argue that concentrated ownership and control outcomes interact.
3. **Liquidity is a nuisance parameter, not a driving variable.** Amihud is a Z₁ control whose only modelled roles are toehold deterrence and the illiquidity discount. Our κ is the treatment; here it is a covariate. Their p. 961 decomposition (8.38 pp total = 1.69 indirect via takeover probability + 6.69 direct) is nevertheless the single most useful number they give us: it is an **existing, published estimate that liquidity moves control outcomes**, and it is small (≈20% of the illiquidity discount runs through takeovers). It sets the order of magnitude our estimates should be compared against, and it is a citation we can use to say the channel is real but unexamined.

**What constrains us.**
- **The anticipation effect is our identification problem too.** If a stricter disclosure rule changes expected bidder entry, prices move in anticipation, and any naive regression of a control outcome on a rule change is attenuated for exactly EGJ's reason. Our design must say what plays the role of MFFlow, or bound the bias. This is the referee checklist's "anticipation" line, and EGJ is the citation that makes it mandatory rather than optional.
- **The premium wedge is only weakly disciplined by data.** EGJ report a 7.2% correlation between Discount and Premium and note the relation "is still far from one" (p. 962), which is consistent with an acquirer capturing part of the gain — i.e. with a λ < 1 appropriability coefficient of the kind our tender game produces. It supports the wedge's existence without pinning its size.
- **They have declared the theory vacancy for us.** Two sentences (Q6, Q7) say the takeover literature lacks a model in which market prices affect acquisition likelihood, and that asymmetric learning has not been incorporated. Our core model — where the market's *partition* determines what the bidder infers — is a direct answer to a gap that a 2012 *JF* paper stated in print and that (per this card) they did not fill themselves. That is a strong opening line for the positioning stage.

**(added by verifier) The vacancy is shaped like our partition, and they even sketch the mechanism.** p. 966 shows any symmetric-information model gives a *zero* price → takeover-likelihood effect (see §6), so the theory they call for must be an asymmetric-information one. And on p. 936 they sketch the required asymmetry themselves: "target shareholders learn the firm's true value from the market price and thus demand a takeover price that is closely linked to the market price … but the acquirer has additional information on the firm's potential value under his management." That is our flagged/pooled partition in prose — one side reading the market, the other side knowing more — with the disclosure rule as the instrument that moves which side knows what. Positioning line: EGJ specified the hole (p. 966), sketched its shape (p. 936), and left it empty.

**(added by verifier) Their instrument choice is a warning about ours.** p. 959 rules out supply-side instruments (buyout-fund inflows, interest rates) "because they fail to generate variation in the cross-section" — the same defect a single dated rule change has. Pair the Feb-2024 date with a cross-sectional dimension, or expect the referee to cite EGJ p. 959 back at us.

**Caution for the positioning stage.** Do not cite EGJ as theory. Do not attribute a proposition to them. The correct citation form is "EGJ (2012) *estimate*" or "EGJ (2012) *call for*", never "EGJ (2012) *show* [analytically]".

## 8. Quotes we may lean on (verbatim, page-cited)

*Line-break hyphens introduced by the PDF layout have been closed up; every other character (including curly quotes and em-dashes) is as printed.*

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "An interquartile decrease in valuation leads to a seven percentage point increase in acquisition likelihood, relative to a 6% unconditional takeover probability." | p. 933 | The headline magnitude; our benchmark for "how big is a control-outcome effect" |
| Q2 | "Third, considering the full feedback loop—the combination of the trigger effect and the anticipation effect—our results suggest that the anticipation effect could become an impediment to takeovers. The anticipation of a takeover boosts prices, deterring the acquisition of underperforming firms." | p. 937 | The self-defeating feedback logic; the anticipation threat our own design must handle |
| Q3 | "In addition, our paper has a number of wider implications outside the takeover market. The feedback loop may apply to other corrective actions, such as CEO replacement, shareholder activism, and regulatory intervention." | p. 938 | They flag activism as an *extension they did not run* — our whitespace |
| Q4 | "Illiquidity directly affects takeover likelihood as it deters toehold accumulation, which in turn affects takeover success rates (Betton and Eckbo (2000)). In addition, it causes firms to trade at a discount (Amihud (2002))." | p. 951 | The only place liquidity is given an economic role; shows it is a control, not a treatment |
| Q5 | "Thus, while it is well known that illiquidity reduces a firm’s market valuation, this decomposition demonstrates that approximately 20% of this effect arises indirectly through the reduced takeover probability." | p. 961 | The one published liquidity → control-outcome magnitude in the paper |
| Q6 | "While our paper demonstrates that market prices have an effect on takeover probability, it is silent on the mechanism behind this effect." | p. 965 | Scope boundary: mechanism explicitly out of scope |
| Q7 | "Our findings thus suggest the need for new takeover theories to explain why market prices should impact acquisition likelihood." | p. 966 | Scope boundary: they call for the theory our core model supplies |
| Q8 | "While our analysis is able to identify the trigger and anticipation effects separately, we are only able to estimate an average trigger effect and an average anticipation effect across the full sample, rather than allow these effects to depend on firm characteristics such as governance, due to limitations of the data and methodology described earlier." | p. 966 | Scope boundary: no heterogeneity — the margin we exploit |
| Q9 | "Note that to date the possibility of asymmetric learning has not yet been incorporated into the theoretical takeover literature." | p. 936 | The declared theory vacancy; our partition is an answer to it |
| Q10 | "We reiterate the caveat that we are only able to attribute a portion of the endogeneity to the anticipation effect; the anticipation effect that we are able to pin down is economically modest." | p. 938 | Honest limit on the anticipation magnitude; keeps us from over-citing R5 |
| Q11 | "Importantly, while the relationship between Premium and Discount remains highly significant, it is still far from one. This suggests that the acquirer does indeed enjoy part of the gains from buying a discounted target" | p. 962 | Empirical support for an appropriability coefficient λ < 1 in the premium wedge |
| Q12 | "Since bidder returns are close to zero on average (Jensen and Ruback (1983), Betton, Eckbo, and Thorburn (2008)), the target captures almost the entire value gains from the takeover." | p. 941 | Calibration fact for the premium wedge; the 37–39% median premium sits in the same paragraph |

## 9. Verification log

**Verifier:** independent agent, 2026-08-19. **Checked against:** `research/txt_extracts/edmans_goldstein_jiang_2012_jf.pdf` re-extracted page by page with `pdftotext -f N -l N -layout`, plus a page-mapped flattening of the `.txt` (PDF p. 1 = printed p. 933; map confirmed by the printed folio "958" and the running heads). Not against the card author's reasoning, which the verifier never saw.

**Counts:** OK 34 · WRONG 2 · MISCITED 3 · UNCHECKED 3.

### Header / venue
| Item | Verdict | Checked against |
|---|---|---|
| JF 67(3), 933–971, June 2012 | OK | p. 933 masthead "VOL. LXVII, NO. 3 • JUNE 2012"; page map ends at 971 |
| 39 printed pages, PDF p. 1 = printed 933 | OK | 39 form feeds; folio "958" on PDF p. 26 |

### Quotes (§8) — all twelve re-grepped whitespace-exact against the printed page named
| # | Verdict | Note |
|---|---|---|
| Q1 p. 933 | OK | abstract, exact |
| Q2 p. 937 | OK | em-dashes as printed |
| Q3 p. 938 | OK | |
| Q4 p. 951 | OK | |
| Q5 p. 961 | OK | curly apostrophe in "firm's" as printed |
| Q6 p. 965 | OK | |
| Q7 p. 966 | OK | |
| Q8 p. 966 | OK | |
| Q9 p. 936 | OK | |
| Q10 p. 938 | OK | |
| Q11 p. 962 | OK | truncation mid-sentence is faithful |
| Q12 p. 941 | OK | |

### Results (§3) and method claims (§2)
| Claim | Verdict | Checked against |
|---|---|---|
| Zero hits for proposition / theorem / lemma / corollary / proof → no theory, no PROVED label available | **OK** | `grep -icE` on the full text: 0 / 0 / 0 / 0 / 0. Section I is "Model Specification" but contains only estimating equations (1)–(14). The premise correction at the head of this card stands. |
| R2 headline: 1.371***, t = 4.24, dPr/dX 15.66%, IQ 7.55%; 0.989***/3.67; 1.512***/4.51; 1.101***/3.64; IQ range 5.65–7.55 pp vs 6.18–6.24% base | OK | Table III, printed pp. 957–958, all four columns match digit for digit (IQ = 7.55 / 5.65 / 7.48 / 6.25) |
| R2 "12–16 bp" per 1 pp | **MISCITED → fixed** | actual dPr/dX = 15.66 / 11.58 / 15.87 / 12.64 % per 100 pp, i.e. **11.6–15.9 bp**. Corrected in the table. |
| R3 weak-instrument F = 95.38 / 167.15 / 38.00 / 91.39, p = 0.00; exogeneity Wald 7.71 / 8.21 / 7.93 / 8.04, p = 0.01 / 0.00 / 0.01 / 0.01 | OK | Table III, p. 958. ("Stock–Yogo" attribution is right: Stock and Yogo (2005) is named at p. 956 and in the references, p. 971.) |
| N = 100,160 / 100,166 / 79,100 / 79,103 | OK | Tables II–V |
| R1 "1–3 bp", IQ 0.4–1.6 pp | **MISCITED → fixed** | Table II Panel A, p. 954: 0.282***/15.34, dPr/dX 3.28%, IQ 1.58% … 0.070***/4.30, IQ 0.41%; dPr/dX runs 0.84–3.28%, so **0.8–3.3 bp**. Corrected. |
| R4 δ̂ "= −0.163*** (t = −32.40) **to −0.375\*\*\***" | **WRONG → fixed** | Table IV p. 960 gives −0.163 / −0.140 / −0.266 / −0.193; Table V Panel B p. 965 gives −0.272 / −0.343 / −0.375 / **−0.381*** [−12.24]**. The stated range endpoint was not the extremum. Rewritten as −0.140 to −0.381 with the headline −0.163 named. |
| R5 1.2 pp = 0.163/0.136; 0.4 pp from next-year anticipation given a ~40% premium; 0.8 pp residual | OK | p. 960 verbatim arithmetic; p. 936 adds "one-third of this estimated decrease". Label split (ESTIMATED + ASSERTED) is right — the 0.4 is a back-of-envelope, not an estimate. |
| R6 Amihud decomposition 8.38 = 1.69 (= −0.124 × −0.136) + 6.69, ≈20% indirect | OK | p. 961, verbatim. Label split (ESTIMATED inputs / ASSERTED arithmetic) is right. **But see the added §4 caveat: the Amihud variable's printed definition is inverted and it has no summary statistics, so the "one unit" scale is not reconstructable.** |
| R7 Amihud "−0.034*** to −0.026**" in Table II | **WRONG → fixed** | Table II p. 954: −0.034*** (−4.05), −0.023*** (−2.84), −0.027*** (−2.62), −0.026** (−2.54). Endpoint corrected to −0.023***. (Also worth knowing: in Table V Panel A, p. 964, two of the four Amihud coefficients fall to 10% significance.) |
| R8 IQ 2.11–2.29 pp vs 1.38/1.45% unconditional | OK | Table V Panel A, p. 964 (2.29 / 2.11 / 2.21 / 2.23) |
| R9 correlations 7.2% / 1.8% / 7.4%; "far from one" | OK | p. 962 |
| R10 α ∈ [0.10, 0.30]; 2.5% tercile exclusion → IQ 6.0–7.8%; merger waves; completed deals 76.5% | OK | p. 963 |
| R11 Inst 0.196*** (4.16) and 0.469*** | OK | Table III p. 957; Table V Panel A p. 964 |
| Sample: SDC 1980–2007, 13,196 → 6,555 deals, financials/utilities dropped | OK | p. 946 |
| Summary stats N = 118,942 "Table I Panel B, p. 947" | **MISCITED → fixed** | Table I *begins* p. 947 (Panel A definitions); **Panel B is on p. 948**. |
| Figure 2 "(p. 952)" no pre-trend / reversal by month 24 | **MISCITED → fixed** | Figure and caption are on p. 952; the "no significant decline … recovering by the end of the 24th month" text is on **p. 953**. Both now cited. |
| α = 0.20 from 38% median premium → 77th percentile, rounded | OK | p. 942 (paper says "Rounding to the nearest decile"); Bradley et al. (2010) closed-end-fund cross-check same page |
| Eqs (8)–(9), δ < 0, ρ = δσ²_ξ < 0, probit underestimates μ₁ | OK | p. 944 |
| Rivers–Vuong (1988) control function; FIML eq. (B3) pp. 967–968; Gourieroux et al. (1987) generalized residual eq. (14) p. 959 | OK | pp. 945, 959, 967–968 |
| MFFlow: hypothetical trades, 5% outflow cut-off, scaled by dollar volume, summed over four quarters | OK | Appendix A, p. 967; discussion p. 951 |
| Sector funds excluded: 8.5% of funds, 8.7% of aggregate (unsigned absolute) flows | OK | fn. 16, p. 952 |
| Governance indices drop ≈ two-thirds of the sample, relegated to Internet Appendix | OK | fn. 15, p. 950 |

### Scope claims (§6) — every "they do not do X" grepped
| Claim | Verdict | Evidence |
|---|---|---|
| `13D` — zero hits | OK | `grep -ic "13D"` = 0 |
| `Schedule` — zero hits | OK | 0 |
| `blockhold*` — reference list only | OK | 2 hits, both in the bibliography (Edmans 2009; Edmans–Manso 2011) |
| `disclos*` — exactly once, "previously disclosed portfolio", mutual funds, p. 951 | OK | 1 hit, p. 951 |
| No filing window / five business days | OK | `five business` = 0; `window` = 3 hits, all event-study windows ([−60, 0], [−1, +1], [−40, 0]) |
| The only 5% in the paper is the mutual-fund outflow cut-off | OK | Appendix A, p. 967, and p. 951 |
| No premium regression in the article | OK | p. 962 states the Premium/AcquirerRET regressions "appear in the Internet Appendix" |

### Omissions found and added (marked "(added by verifier)" in place)
1. **p. 966 — the symmetric-information impossibility argument.** EGJ do not merely call for a theory; they argue no symmetric-information model can generate their result (free-riding à la Grossman–Hart (1980); bargaining over Discount₀ not Discount; news and mispricing both leave takeover likelihood unaffected). The vacancy is an *information-partition* vacancy. **Added to §6 and §7** — this is the single most positioning-relevant thing the card was missing.
2. **p. 936 — they sketch the required asymmetry.** Target shareholders learn value from the price and demand a premium above it; the acquirer knows more about value under his management. That is our partition in prose. **Added to §7.**
3. **p. 959 — they consider and reject supply-side instruments** (buyout-fund inflows, interest rates) because "they fail to generate variation in the cross-section". A single dated rule change has the same defect. **Added to §5 and §7.**
4. **p. 950 — the blockholder economics EGJ do lean on:** Mikkelson–Partch (1989) and Shivdasani (1993) on block ownership raising takeover-attempt probability, and institutional concentration reducing the Grossman–Hart free-rider problem. **Added to §4.**
5. **pp. 938–939 — Bradley et al. (2010):** the closed-end-fund discount "affects and reflects the probability of activism at the same time", and activists target deeper-discount funds. The published precedent for our simultaneity, in a setting with an observable frontier value. **Added to §4.**
6. **p. 936 fn. 3 — Schwert (1996):** offer price rises almost dollar-for-dollar with the pre-bid runup, and he "does not explore the effect on takeover probability". Premium-wedge relevant. **Added to §4.**
7. **p. 947 Table I Panel A + p. 948 Panel B — the Amihud variable is not reconstructable.** The printed definition ("square root of (Price×Vol)/|Return|") is the reciprocal of Amihud (2002) illiquidity, and Panel B reports no summary statistics for Amihud at all. Cite the ≈20% share from R6, never the levels. **Added to §4.**
8. **fn. 15 pp. 950–951 — the governance null:** entrenchment and shareholder-rights indices are uncorrelated with takeover probability in the subsamples where they exist; Bates–Becher–Lemmon (2008) agree. **Added to §5.**
9. **p. 949 Fig. 1 — takeover base rate ranges ~3% to above 8% annually, 1980–2006**, and comoves with aggregate Discount except 2002–03. **Added to §4.**
10. **p. 961 — Premium is measured over the [−60, 0] window** relative to announcement. **Added to §4.**

### UNCHECKED (left in place, marked here — not triaged away)
1. **Everything in the Internet Appendix.** R9's Premium/AcquirerRET *regressions*, R10's entire robustness battery (α sweep, tercile-cutoff exclusion, merger-wave removal, completed-deals-only), and the governance-subsample results of fn. 15 are outside this PDF. The card already says so; the verifier confirms none of it is checkable from the article. **Decision-critical:** if we cite the Premium–Discount relation as evidence for λ < 1 (§7), we are citing an unpublished-in-article regression on the strength of one sentence, p. 962.
2. **The claim that the interquartile *change* in Discount corresponds to the stated pp figures** rests on the paper's own IQ row; the interquartile range itself is not printed for the instrumented specification, so the arithmetic cannot be re-derived. Not material — the IQ row is what we would cite anyway.
3. **Prior-literature characterisations in §1** (Palepu 1986, Ambrose–Megginson 1992, etc. finding "a weak or absent link") were verified only as EGJ's own summary at pp. 933–935, not against those papers.

### Overall verdict
**The card is sound and unusually careful.** Its central premise correction (no theory, no PROVED label) is confirmed by grep, and all twelve quotes are verbatim on the pages named. Two coefficient-range endpoints were wrong (δ̂ and Table II Amihud), three page citations were off by one page or by figure-vs-text, and four rounding statements were loose; all are fixed above. The one substantive gap was §6/§7 missing EGJ's **p. 966 argument that a symmetric-information model cannot produce their result** — which is a stronger and more usable statement of the theory vacancy than the "need for new takeover theories" quote the card leans on, and it is now added.
