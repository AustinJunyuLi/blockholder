# Albuquerque, Fos & Schroth (2020/2022) — "Value Creation in Shareholder Activism: A Structural Approach"

**Venue / status:** Published as *Journal of Financial Economics* 145(2), 153–178 (2022). **The version read here is the working paper: ECGI Finance Working Paper N° 685/2020, July 2020 (paper dated July 8, 2020; SSRN abstract 3639636).** All page numbers, numbers and quotes below are from the WP; the published JFE version was NOT consulted and may differ.
**Full text from:** `lit/albuquerque-fos-schroth-2022-wp.pdf` (84 PDF pages) · re-extracted with `pdftotext -layout`; `research/txt/afs_jfe2022.txt` is the same WP without page markers · **Reader:** opus · **Read:** full text, 84 PDF pages (ECGI front matter pp. i–iv, body printed pp. 1–41, references pp. 42–43, tables/figures pp. 44–56, Internal Appendix pp. 1–20)
**Page-numbering convention:** printed page number of the WP body (PDF page = printed page + 5; verified against the printed folios on PDF pp. 13 = "8" and 46 = "41"). Internal Appendix pages restart at 1 and are cited as "IA p. N". **(corrected by verifier)** The four ECGI front-matter pages and the paper's own abstract page carry **no printed page numbers** — there is no "p. i". The ECGI abstract is PDF p. 3, the paper's abstract PDF p. 5; both are cited below as "abstract (PDF p. 5)".
**Type:** structural (structural estimation of a discrete-choice + selection model)   **Role for us:** competitor

## 1. Question

How much of the well-known ~6% abnormal return around a Schedule 13D filing is actually *created* by the activist, and how much is stock picking or a selection artefact? The observed 13D–13G return gap (**6.34% vs 0.59%, p. 1** — corrected by verifier; the 6.33% figure the earlier draft of this card put on p. 1 is Table 2's *observed* 13D mean, p. 45, repeated on pp. 24 and 28) cannot be read as value creation, because the investor chooses which schedule to file and the two return distributions censor each other. AFS build a structural model of the 13D-versus-13G filing choice and estimate it by maximum likelihood, so that the counterfactual ("what would this firm have returned had the same investor filed 13G?") is recovered rather than assumed. They then ask whether the recovered treatment component predicts real outcomes, and what the estimated private cost of activism implies for efficiency.

## 2. Model / data and method

**Model (Section 2, pp. 8–15).** One investor has already acquired a stake in one target and must file either Schedule 13D (activist) or Schedule 13G (passive). Valuation gains are ∆_D = µ_D + ε_∆D and ∆_G = µ_G + ε_∆G with independent normal errors; µ_D, µ_G are common knowledge. Before filing, the investor does due diligence and sees noisy signals s_D = ∆_D + ε_sD, s_G = ∆_G + ε_sG, again normal, with separate precisions by filing type. The investor is risk-neutral and files 13D iff EU_D = E(∆_D|s_D) − C > EU_G = E(∆_G|s_G) (Eq. 1, p. 10). Defining z ≡ EU_D − EU_G, the econometrician sees {z>0} = "13D". Truncated-normal algebra (Arnold et al. 1983) gives the observed 13D mean E(∆_D|z>0) = µ_D + ρ_zD σ_∆D λ_D(α) (Eq. 7, p. 13) and hence the three-way decomposition (Eq. 9, p. 14):

E(∆_D|z>0) = (µ_D − µ_G) [treatment] + µ_G [stock picking] + ρ_zD σ_∆D λ_D(α) [sample selection].

Risk aversion is isomorphic to a re-labelled cost (Appendix A, IA pp. 2–3).

**Functional forms that buy tractability:** everything normal (returns and due-diligence noise); linear index µ_Di = x'_i β_D, µ_Gi = x'_i β_G; **the cost of activism C is a single scalar, constant across all 69,937 filings** (p. 15). The model is silent on *why* activism creates value ("Our model is silent about how the valuation gains come about", p. 9) and on *which* characteristics drive expected returns ("Our model is silent about which characteristics influence expected returns and why", p. 16 — *added by verifier*).

**What the scalar C actually absorbs (§2.6, pp. 14–15 — *added by verifier*; this qualifies any use of the 4.6pp number as a calibration target).** AFS list five things folded into the one parameter: (i) pecuniary costs of affecting control; (ii) the disutility of return and due-diligence-signal risk (the risk-averse model is isomorphic after re-labelling C); (iii) **a penalty for 13Ds filed only to harvest the larger announcement return with no intention to engage** — cheap talk in the form choice is priced into C, not modelled; (iv) the activist's **private benefits** from a large stake (Coffee, 2017), so "C should be viewed as the activism cost **net of** these private benefits"; (v) the transaction cost of accumulating the stake, including pre-flag price pressure (Q11/Q13 below).

**Stake and trading:** the stake size is exogenous and the model has no trading, no market maker, no price impact and no liquidity. Footnote 6 (p. 8) says so explicitly and points to Back et al. (2018) for that. Liquidity enters only as a *regressor*: Amihud illiquidity is one of twelve firm characteristics in x.

**Disclosure rule:** the 5% threshold and the 13D/13G form choice are the institutional backdrop, but neither the threshold level nor the filing window is a modelled margin. The filing window appears only as a sample-cleaning device (dropping 14 February 13G filings by exempt investors).

**Data (Section 4, pp. 23–24).** EDGAR universe 1996–2017: 50,708 13D and 171,051 13G filings; after de-duplication and CRSP/Compustat merge, 23,391 13D and 121,373 13G; after dropping 28,663 February-14 13G filings and requiring non-missing characteristics, **final sample 69,937 filings — 8,703 Schedule 13D and 61,234 Schedule 13G**, of which 7,551 are by activist hedge funds (2,539 13D / 5,012 13G in Table 2; Appendix C reports 2,523 / 4,219 in the estimation subsample). Outcome variable is the CAR over [t−30, t+10] on the Fama–French three-factor model; the window starts 30 days early because Collin-Dufresne and Fos (2015) show pre-filing price appreciation reflects the activist's own trades (p. 17).

**Estimator:** joint maximum likelihood on filing choice and return, parameter vector θ = {β_D, β_G, C, σ²_∆D, σ²_∆G, σ²_sD, σ²_sG} (p. 18). Identification of C comes from the first-order condition (Eq. 13, p. 20) that equates the variance-weighted average inverse Mills ratio across the 13D and 13G subsamples — i.e. **C is identified by the relative amount of selection in the two subsamples**, not by any cost data. Benchmarked against OLS + Probit and against a two-step Heckman.

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where (page / prop / table) |
|---|---|---|---|
| R1 | Announcement-return decomposition for 13D filings: **treatment 75.2%, stock picking 12.2%, sample selection 12.6%** — i.e. 4.77% / 0.77% / 0.80% of a model-predicted announcement return of 6.34% | ESTIMATED (structural, ML; components are functions of estimated β̂'s) | Abstract (unnumbered, PDF p. 5, and ECGI abstract PDF p. 3); text pp. 3, 32–33, 34; Table 6 Panel A p. 51 (PDF p. 56); Table 5 p. 50 (PDF p. 55); Figure 4 Panel A p. 56 (PDF p. 61) |
| R2 | Estimated private cost of activism C = **0.046 (4.6 percentage points of the ex post stake value), SE 0.003, p < 0.01**, ≈ $2.43 million; net mean activist return 1.73% | ESTIMATED | p. 28; Table 3 Panel B col. (4), p. 48 |
| R3 | Firm characteristics load **equally** on µ_D and µ_G, so the treatment effect is explained almost only by *investor experience* variables, not by target characteristics | ESTIMATED | pp. 26–27; Table 3 Panel A, p. 47 |
| R4 | +10 prior 13D filings ⇒ next 13D return +≈19 bp but next 13G return −≈25 bp (β̂ = 0.178 / −0.219 in spec. 4); prior 13G experience loads −0.165 on µ_D | ESTIMATED | p. 26; Table 3 Panel A col. (4), p. 47 |
| R5 | Amihud illiquidity loads **positively and equally** on both µ_D (0.021***) and µ_G (0.019***) — read by the authors as an illiquidity premium, not a governance-liquidity effect | ESTIMATED | p. 27; Table 3 Panel A, p. 47 |
| R6 | Treatment and stock-picking components predict ∆ROA (+2.98pp and +1.38pp per SD) and ∆sales turnover (+7.5pp, +2.5pp); once included, the raw CAR loses significance | ESTIMATED | pp. 35–36; Table 7 Panels A–B, p. 52 (N = 5,356) |
| R7 | Higher treatment component predicts a **lower** probability of a proxy contest next year (−0.0491***, SE 0.0149) | ESTIMATED | pp. 36–37; Table 7 Panel C, p. 52 (N = 5,032) |
| R8 | The structural model matches the 13D filing frequency (0.124 data vs 0.124 model vs 0.021 Probit) and correlates 0.535 with actual choices vs Probit's 0.254, while matching return moments as well as OLS | ESTIMATED / NUMERICAL (10,000 simulated samples) | pp. 30–32; Table 5, p. 50 |
| R9 | **60%** of observed 13G filings satisfy µ̂_D − µ̂_G > 0; if the activism cost were shared by all shareholders, the average gain is **$35.6 million per 13G filing, ≈ $60 billion per year** (untabulated) | ESTIMATED, but the dollar aggregate is an untabulated counterfactual the authors themselves call only an upper bound | pp. 37–38, 41 |
| R10 | Activist-hedge-fund subsample: treatment **92.4%**, stock picking **−4%**, selection **11.6%**; implied C between 3% and 4% of stake size; correlation of estimated treatment with full-sample treatment 0.9955 | ESTIMATED | pp. 6, 39–40; Appendix C, IA pp. 10–14 |
| R11 | Two-step Heckman understates selection in 13D mean returns and overstates it in 13G; ML selection is about double the Probit IMR at high values | ESTIMATED / ASSERTED (shown graphically, Figure A1) | pp. 22, 30–31; Appendix B, IA pp. 4–5 |
| R12 | **NO result on takeover premia, bidder entry, or M&A outcomes of any kind** — see §6 | — | full-text search, see §6 |
| R13 | *(added by verifier)* Repeated-campaign robustness: a prior Schedule 13D filing on the same target by **any** filer in the previous 365 days loads **positively on both** µ_D and µ_G ("a positive complementarity between past activism and future large investments, passive or active"); a prior 13G filing shows no such effect | ESTIMATED | §7.2, p. 40; table in Appendix (Table A6, PDF p. 78) |

*Note on internal consistency (revised by verifier — both figures confirmed present):* the selection component is 0.80% in Table 6 / §6.1 (p. 33) but is stated as "on average 0.83%" in the Internal Appendix (IA p. 19 = PDF p. 80). The observed 13D mean CAR is 6.33% in Table 2 (p. 45) but the decomposition is taken over the model-*predicted* 6.34% (Table 5, p. 50); the abstract and Figure 4 use the percentage shares. **Two further inconsistencies the verifier found:** (a) the intro states the observed 13D mean as **6.34%** (p. 1) where Table 2 gives 6.33%; (b) the mean net activist return is **1.74%** on p. 4 and **1.73%** on p. 28. (c) Footnote 15, p. 34 explains a third gap — the t+10 return in Figure 4 differs from Table 2 because Table 2 winsorises over the full sample and Figure 4 over 13D filings only. Cite the numbers with their page, not as one canonical figure.

## 4. Institutional facts used

- The SEC requires beneficial owners of ≥ 5% of a class of equity to file Schedule 13D if they intend to affect management, else the shorter Schedule 13G (footnote 1, p. 1).
- **10-day filing window and the 45-day exempt-investor route**: "Exempt investors are not required to file within 10 days of crossing the 5% equity stake and can file up to 45 days after calendar year-end" (p. 24). This is used only to justify dropping 28,663 February-14 13G filings, whose mean CAR is −0.08% (insignificant) versus 0.59% for other 13G filings.
- 78% of investors who ever filed a 13D also filed at least one 13G in the sample (pp. 2, 25); 74% of activist hedge funds filed both (p. 39). This is the justification for treating the two schedules as a genuine binary choice.
- *(added by verifier)* **How AFS themselves place the liquidity literature**: footnote 2, p. 2 — "Several papers have looked at the choice between active and passive strategies. For example, Edmans et al. (2013) study activist hedge funds and show that stock liquidity predicts filing Schedule 13D versus Schedule 13G. Giglia (2016) discusses incentives to file Schedule 13G versus Schedule 13D." EFZ is filed under *filing-choice determinants*, not under governance-through-liquidity. Giglia (2016) is a citation our 13D/13G section should pick up.
- Data sources: EDGAR (filings), CRSP (returns/volume/prices), Compustat (firm characteristics), Thomson Reuters (institutional ownership); activist-hedge-fund list supplied by Wei Jiang (footnote 10, p. 17).
- Sample period 1996–2017. **Nothing in the paper touches the 2024 window change** (it predates it).

## 5. Referee-facing strengths / weaknesses

**Strengths:**
- The identification is transparent and stated as first-order conditions: β̂_D is an OLS orthogonality condition corrected for selection (Eq. 12, p. 19); Ĉ trades off the two subsamples' inverse Mills ratios (Eq. 13, p. 20). A referee can see exactly which moment moves which parameter.
- The cross-equation restriction is *tested*, not assumed: the structural model beats Probit badly on filing choice (0.535 vs 0.254 correlation) without losing on return moments (Table 5).
- Out-of-model validation: the recovered treatment component predicts ROA, sales turnover and (negatively) proxy contests — a real prediction the decomposition did not target.
- Parameter stability across the very different hedge-fund subsample (treatment correlation 0.9955) is a strong robustness signal.

**Weaknesses / open flanks:**
- **C is one scalar for 69,937 heterogeneous filings** (p. 15). The authors admit the reason is parsimony and lack of proxies. Any cross-sectional variation in campaign cost is loaded onto the return parameters instead.
- Everything is normal, and the selection correction is exactly the normality of z. There is no distributional robustness check.
- The estimated due-diligence noise is enormous (σ̂_sD = 5.581 vs σ̂_∆D = 0.219, Table 3 Panel B, p. 48). The model "wins" partly by making private information nearly worthless — which is a strange conclusion for a paper about informed activists, and sits oddly against Collin-Dufresne–Fos (2015) evidence the same authors cite.
- The [t−30, t+10] window deliberately absorbs the activist's *pre-filing trading* profits into the "announcement return", so the object decomposed is not a clean announcement effect.
- The $60bn cost-sharing counterfactual is untabulated and the authors themselves disclaim it as an upper bound with no renegotiation and no distortions (p. 38).
- The stake is exogenous; the very margin (how much to buy, and when the buying is revealed) that generates the price run-up they are correcting for is outside the model.
- *(added by verifier — their own stated limitation, and it is exactly our object)* **Footnote 16, p. 34:** "Note that it is often the case that Schedule 13D filings are preceded by Schedule 13G filings on the same target firm, by the same or other investors. Hence, the stock price reaction to initial Schedule 13G filings may already incorporate the possibility of subsequent 13D filings. The implication is that the true treatment effect may be larger than we estimate." That is a statement about the *market's* partition of states — the 13G price already prices an option on a later 13D — which is our object, conceded by them as a downward bias.
- *(added by verifier)* **Their own reduced-form Probit runs the other way on liquidity.** In Table 4 col. (5), p. 49 (PDF p. 54), the Probit for "13D v. 13G filing" loads Amihud illiquidity at **+0.172\*\*\*** (SE 0.019): more *illiquid* firms are more likely to be flagged 13D. Read together with R5 and with the text on p. 27 ("stock market liquidity facilitates Schedule 13D or Schedule 13G filings"), the paper's liquidity story is not internally tidy, and Table 4 is the number a referee will find first.

## 6. What they do NOT do (scope boundary)

**Object.** The object is the **13D/13G announcement return** and its decomposition, plus two post-filing performance outcomes (ROA, sales turnover) and one governance outcome (proxy contest). **The paper contains no result on takeover premia, bidder entry, deal completion, or M&A volume.**

I checked this by exhaustive full-text search of the WP, because our earlier notes attributed a "−13.7% / 5.2pp" takeover-premium result to AFS:
- `takeover` occurs **three** times in the whole document, all in the literature review or references: footnote 4 (p. 7) "the role of activist hedge funds in corporate takeovers"; footnote 5 (p. 7) "economic synergies in takeovers"; and the title of the Greenwood–Schor (2009) reference (p. 43).
- `premium` / `premia` occurs **twice in body prose and otherwise only as the "Market premium" row** of Tables 3, 4, A2 and A6 — the Fama–French **market excess return** factor added in specification (4), described on p. 25 as "three stock return risk factors, the market excess return, SMB, and HML"; its estimate is 0.000** / 0.000*. **(corrected by verifier: the earlier "only as the Market premium row" was too strong.)** The prose hit is on p. 27, "consistent with an **illiquidity premium** as in Amihud (2002)" — this card's own Q9. Neither is a takeover premium.
- `merger`, `acquirer`, `tender offer` occur only in reference titles. *(verifier addition:)* `bidders` and `M&A` do occur once in body prose — footnote 18, p. 38, citing Li et al. (2018) on the welfare losses of M&A transactions in which "targets are acquired by the most overvalued rather than the most synergistic bidders" — but only to contrast their own welfare loss, which is *forgone 13D filings*. Still no M&A result of their own.
- The strings `13.7` and `5.2 pp` / `5.2 percentage` do not occur anywhere in the document.

**Verdict: the "−13.7% / 5.2pp premium" result is NOT in this paper.** The later reader is right and the earlier note is wrong. It should be re-attributed (Greenwood–Schor 2009 and Boyson–Gantchev–Shivdasani 2017 are the obvious candidates in the activism-mergers literature; neither was checked here).

**Margin.** Neither margin of the disclosure rule is studied. The 5% threshold is a sample-selection device, not a treatment; the 10-day window is used once, to drop exempt filers. There is no rule change, no cross-country threshold variation, and no time-series variation in the rule.

**Trading and liquidity.** Explicitly out of scope. Footnote 6, p. 8: *"We take the stake size as given and focus on the activist's choice to be an active or a passive investor. Back, Collin-Dufresne, Fos, Li and Ljungqvist (2018) provide a model of an activist's trading behavior and study the trade off between the impact of activist investors on firm value and market liquidity."*

**Mechanism.** p. 9: *"Our model is silent about how the valuation gains come about."*

**Named future work** (Conclusion, p. 41): heterogeneous costs of activism, heterogeneous due-diligence precision, and — directly on our turf — *"Investors may take into account the price impact of their trading before crossing the 5% ownership threshold. We leave these extensions for future research."*

## 7. Implications for our position

**What AFS occupies:** object = 13D/13G *announcement return* (and post-filing firm performance); margin = **none** — the disclosure rule is background, not a treated margin; identification = **structural MLE on a selection model**, cross-section 1996–2017, no design-based variation.

**What this leaves open for us — three things, all clean:**

1. **The control outcome is untouched.** AFS is the reference paper on "how much value does 13D activism create", and it says nothing about takeover premia, bidder entry or campaign success. Our control-outcome object does not collide with theirs. We must, however, stop citing them for a premium number: the correction in §6 has to propagate into `draft_v3` and any lit table.

2. **The window margin is untouched, and they say so.** Their conclusion names the price impact of pre-threshold trading as future work. That is exactly the window-margin mechanism (how much trading happens before the flag). Our Feb-2024 acceleration anchor cannot be scooped by AFS; it is the extension they declined.

3. **Liquidity is a control variable for them, a driving variable for us.** Their R5 is a real constraint to respect, not to fight: in their cross-section Amihud illiquidity loads *equally positively* on 13D and 13G expected returns, which they read as a plain illiquidity premium (p. 27). Any liquidity result we claim on announcement returns must clear that hurdle. They also flag that this **contrasts with Edmans, Fang and Zur (2013)** (p. 27). **(Corrected by verifier — the earlier claim that they "do not resolve it" is wrong.)** p. 27 says verbatim: "We discuss potential reasons for this difference in sub-section 5.4." §5.4 (pp. 30–31) then gives a *general* answer without naming EFZ again: structural and reduced-form loadings systematically differ in sign whenever a characteristic also drives the filing choice, because "expected returns in the model serve two purposes". So the disagreement is *addressed by construction*, not left open — and any liquidity-first claim we make on announcement returns has to survive that argument, not merely point at the disagreement. What is genuinely unresolved is the direction conflict inside their own Table 4 (see §5).

**Constraints AFS imposes on us:**
- The naive 13D announcement return is the wrong left-hand side for "value created": three-quarters treatment, but a quarter is stock picking plus selection. If our empirical leg uses announcement returns as an outcome, a referee will ask for the AFS decomposition. Preferring a control outcome (premium, bidder entry, campaign success) sidesteps this — another argument for the CONTEXT.md broadening.
- Their $2.43m / 4.6pp cost estimate is the standing number for the private cost of voice. If our core model has an engagement cost parameter, this is the calibration target, and we should say so.
- Their partition is *the form choice* (13D vs 13G), i.e. the blockholder's declaration of purpose, not the market's information set. Ours is the market's partition into flagged and pooled states. Those are different objects and the distinction should be stated explicitly in the positioning paragraph, because a referee will otherwise read "13D choice model" and see overlap.

**Deliverability note:** AFS's data build (EDGAR 1996–2017, CRSP/Compustat/Thomson) is heavy but not exotic, and our `empirics/` EDGAR pipeline already enumerates 13D filings. We are not competing with them on structural estimation and should not try.

## 8. Quotes we may lean on (verbatim, page-cited)

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "We take the stake size as given and focus on the activist's choice to be an active or a passive investor." | p. 8, fn. 6 | Scope boundary: stake and trading exogenous |
| Q2 | "Back, Collin-Dufresne, Fos, Li and Ljungqvist (2018) provide a model of an activist's trading behavior and study the trade off between the impact of activist investors on firm value and market liquidity." | p. 8, fn. 6 | They hand the liquidity margin to Back et al., not to themselves |
| Q3 | "Investors may take into account the price impact of their trading before crossing the 5% ownership threshold. We leave these extensions for future research." | p. 41 | The window margin is declared future work — our whitespace |
| Q4 | "Our model is silent about how the valuation gains come about." | p. 9 | No control-outcome mechanism |
| Q5 | "We find that the average treatment effect of activism, which is equal to the difference in expected returns from filing Schedule 13D instead of Schedule 13G, represents 75.2% of the observed Schedule 13D announcement return, that is, 4.77% of 6.34%." | p. 3 | The headline decomposition, this version's numbers |
| Q6 | "We assume that C is constant across all filings in the data." | p. 15 | Engagement cost is a scalar, not a distribution |
| Q7 | "The estimated cost of activism is 4.6 percentage points (Panel B of Table 3) of the ex post value of the filer's stake." | p. 28 | Calibration anchor for a voice cost |
| Q8 | "Exempt investors are not required to file within 10 days of crossing the 5% equity stake and can file up to 45 days after calendar year-end." | p. 24 | The only appearance of the filing window; used for sample cleaning |
| Q9 | "Similarly, we find that investments in less liquid securities appear to be compensated by higher expected returns regardless of the filing schedule, consistent with an illiquidity premium as in Amihud (2002)." | p. 27 | Their liquidity finding — a constraint on our announcement-return claims |
| Q10 | "Conversely, this finding implies that stock market liquidity facilitates Schedule 13D or Schedule 13G filings" | p. 27 | Liquidity → filing propensity, their reading |
| Q11 | "For instance, buying towards a 5% target is likely to cause upward price pressure before reaching it and filing with the SEC." | p. 15 | They see the pre-flag price-impact channel and fold it into C rather than model it |
| Q12 | "in the activist hedge fund sample, treatment represents 92.4%, stock picking represents −4%, and sample selection bias represents 11.6% of the average predicted announcement returns." | p. 40 | Robustness subsample decomposition |
| Q13 | *(added by verifier — the sentence immediately after Q11, and the sharper one for us)* "It remains unclear, however, whether a transaction costs differential would exist, unless the market not only forecasts the intention to cross the 5% threshold that triggers either Schedule 13D or 13G filing, but also the type of filing." | p. 15 | AFS name **pre-flag anticipation of both the crossing and the type** as an open question. That is our partition, stated as an unknown by the competitor |
| Q14 | *(added by verifier)* "the stock price reaction to initial Schedule 13G filings may already incorporate the possibility of subsequent 13D filings. The implication is that the true treatment effect may be larger than we estimate." | p. 34, fn. 16 | Their conceded downward bias, and it is a partition/pooling argument |
| Q15 | *(added by verifier)* "Then, C should be viewed as the activism cost net of these private benefits." | p. 15 | Guard-rail on citing 4.6pp / \$2.43m as "the" cost of voice |

*Ligature/encoding note:* the AFS PDF extracts cleanly; quotes are character-for-character, including the typographic apostrophe (’) rendered here as ' in Q1/Q2/Q7. **Verifier: all fifteen quotes re-matched against a fresh `pdftotext -layout` extraction of `lit/albuquerque-fos-schroth-2022-wp.pdf`; every one is present verbatim on the page cited.**

## 9. Verification log

**Verifier:** adversarial second reader (Opus), 2026-08-19. **Method:** independent re-extraction of `lit/albuquerque-fos-schroth-2022-wp.pdf` with `pdftotext -layout`, page-marked (85 form-feeds → 84 printed pages + trailer); every quote matched by whitespace-normalised substring search with the PDF page recovered from the marker, then cross-checked against the printed folio. `research/txt/afs_jfe2022.txt` was NOT used. **Counts: OK 34 · WRONG 3 · MISCITED 2 · UNCHECKED 1.**

### Quotes (§8)

| Q | Verdict | Checked against |
|---|---|---|
| Q1 | OK | fn. 6, printed p. 8 (PDF 13, folio "8") — verbatim |
| Q2 | OK | fn. 6, p. 8 — verbatim |
| Q3 | OK | Conclusion, p. 41 (PDF 46, folio "41") — verbatim |
| Q4 | OK | p. 9 — verbatim |
| Q5 | OK | p. 3 — verbatim, including "4.77% of 6.34%" |
| Q6 | OK | p. 15 — verbatim |
| Q7 | OK | p. 28 — verbatim |
| Q8 | OK | p. 24 — verbatim |
| Q9 | OK | p. 27 — verbatim |
| Q10 | OK | p. 27 — verbatim |
| Q11 | OK | p. 15, §2.6 — verbatim |
| Q12 | OK | p. 40 — verbatim, minus sign is U+2212 |
| Q13–Q15 | OK | pp. 15, 34 — added by verifier from the source |

### Results (§3)

| # | Verdict | Executed check |
|---|---|---|
| R1 | **OK** | 75.2 / 12.2 / 12.6 on abstract (PDF 5), pp. 3, 32–33, 34; 4.77 / 0.77 / 0.80 / 5.53 in Table 6 Panel A (PDF 56 = p. 51); predicted 6.34% in Table 5 (PDF 55 = p. 50). Label ESTIMATED correct |
| R2 | **OK** | Table 3 Panel B (PDF 53 = p. 48): C = 0.046\*\*\* (0.003) in cols (2)(3)(4), 0.051\*\*\* (0.003) in col (1); "$2.43 million" and "1.73%" both on p. 28. *But see the inconsistency note — p. 4 says 1.74%* |
| R3–R5 | OK | Table 3 Panel A (PDF 52 = p. 47) and Table 4 (PDF 54 = p. 49): Amihud 0.021\*\*\* / 0.019\*\*\*; 13D Exp. 0.178\*\*\* / −0.219\*\*\*; 13G Exp. −0.165\*\*\*. Twelve target-firm characteristics confirmed by count on p. 16 |
| R6 | OK | 2.98 / 1.38 pp (ROA) and 7.5 / 2.5 pp (sales turnover) on p. 36; Table 7 Panels A–B, N = 5,356 (PDF 57 = p. 52) |
| R7 | OK | Table 7 Panel C: −0.0491\*\*\* with [0.0149], N = 5,032 |
| R8 | OK | Table 5 Panel A: Data 0.124 / Reduced form 0.021 / Model 0.124; corr 0.254 vs 0.535; 10,000 simulated samples per the caption |
| R9 | OK | "A striking 60% of Schedule 13G filings", "$35.6 million per Schedule 13G filing", "about $60 billion on average per year (untabulated)" — all p. 38 |
| R10 | OK | 92.4 / −4 / 11.6 on p. 40 (also summarised p. 6); correlation 0.9955 on p. 39 |
| R11 | **UNCHECKED** | Figure A1 / Appendix B are in the Internal Appendix (PDF pp. 68–69). The claim "ML selection is about double the Probit IMR at high values" is read off a *plot*; the verifier could not put a number on "about double" without the underlying data. The direction claim (Heckman understates 13D selection, overstates 13G) is consistent with pp. 22 and 31 but is not independently checkable here. **Decision-critical? No** — nothing in §7 rests on R11 |
| R12 | **OK on substance** | Independent full-text grep: `takeover` = 3 hits (fn. 4 p. 7, fn. 5 p. 7, Greenwood–Schor reference p. 43); `13.7` = **0 hits**; `5.2 pp` / `5.2 percentage` = **0 hits**; `merger`/`acquirer`/`tender offer` only in reference titles. **The "−13.7% / 5.2pp premium" result is confirmed absent from this paper.** Two sub-claims in §6 were overstated and are corrected there |
| R13 | OK (added by verifier) | §7.2, p. 40 |

### WRONG items (corrected in place)

1. **§1 — "6.33% vs 0.59% in their data, p. 1".** p. 1 says **6.34%** vs 0.59%. 6.33% is Table 2 (p. 45) and pp. 24, 28. Corrected in §1 and in the consistency note.
2. **§6 — "`premium`/`premia` occurs only as the Market premium row".** False: "illiquidity premium" appears in body prose on p. 27, and is this card's own Q9. Corrected; the takeover-premium conclusion is unaffected.
3. **§7 pt 3 — "they note this contradicts Edmans, Fang and Zur (2013) and do not resolve it".** False: p. 27 says "We discuss potential reasons for this difference in sub-section 5.4", and §5.4 (pp. 30–31) supplies a general structural-vs-reduced-form sign argument. Corrected; the strategic consequence changed (we must clear their argument, not merely cite an open disagreement).

### MISCITED items (fixed)

4. **"Abstract p. i" / "ECGI front matter pp. i–iv".** Those pages carry no printed numbers. Two abstracts exist: ECGI (PDF p. 3) and the paper's own (PDF p. 5). Header and R1 now cite PDF pages.
5. **§6 — "`merger`, `acquirer`, `tender offer` occur only in reference titles".** True for those three strings, but `bidders` and `M&A` occur in body prose in fn. 18, p. 38. Noted; conclusion unaffected.

### Omissions added (§2, §4, §5, §8)

- **fn. 16, p. 34** — 13Ds are often preceded by 13Gs on the same target, so the 13G price reaction may already embed the option of a later 13D; AFS concede the true treatment effect may therefore be *larger*. This is a statement about the market's flagged/pooled partition, i.e. our object, and it was missing entirely. → §5, Q14.
- **p. 15, the sentence after Q11** — "It remains unclear, however, whether a transaction costs differential would exist, unless the market not only forecasts the intention to cross the 5% threshold … but also the type of filing." The card quoted the setup and dropped the punchline. → Q13.
- **§2.6, pp. 14–15 — what C absorbs.** Risk aversion, a penalty for insincere 13D filings, and *private benefits of control* (so C is a cost **net** of private benefits). §7 recommends 4.6pp / \$2.43m as a calibration target; that recommendation needs this qualification. → §2, Q15.
- **fn. 2, p. 2** — AFS classify Edmans–Fang–Zur (2013) as showing "stock liquidity predicts filing Schedule 13D versus Schedule 13G", and cite **Giglia (2016)** on 13G-vs-13D incentives. New citation for us. → §4.
- **Table 4 col. (5), p. 49** — the reduced-form Probit loads Amihud illiquidity at **+0.172\*\*\*** on the 13D-vs-13G choice: more illiquid ⇒ more likely 13D. This cuts against their own p. 27 gloss and is the number a referee finds first. → §5.
- **§7.2, p. 40** — repeated-campaign robustness (prior 13D on the same target loads positively on both µ_D and µ_G). → R13.
- **p. 16** — "Our model is silent about which characteristics influence expected returns and why", a second silence statement. → §2.
- **fn. 15, p. 34** — the Figure 4 / Table 2 gap is winsorisation, not a modelling difference. → consistency note.

### Overall verdict

**The card stands.** The decomposition, the cost estimate, the sample sizes, the CAR window, the fn. 6 hand-off to Back et al. (2018), and the p. 41 future-work sentence are all confirmed verbatim and on the pages cited, and the central negative claim — **no takeover-premium result anywhere in AFS, "13.7" absent** — is independently confirmed. Three factual errors and two citation errors were corrected; the only one that changes a strategic conclusion is the Edmans–Fang–Zur item in §7. One result (R11) is UNCHECKED and nothing depends on it.

