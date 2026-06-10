---
date: 2026-06-06
type: research
status: DECISION-SUPPORT
branch: jmp-upgrade-2026-05
title: "JMP Direction — Deep-Research Findings & Recommendation (top-10 swing)"
method: deep-research workflow (107 agents, 24 sources fetched, 111 claims → 25 adversarially verified, 23 confirmed / 2 killed)
---

# JMP Direction — Deep-Research Findings & Recommendation

> **Author's chosen constraints (the search aperture).** Open to ANY field; STRUCTURAL approach (theory disciplined by estimation on real data); FLEXIBLE timeline (2028+); willing to learn ANY toolkit. Existing edge to leverage only if it helps: corporate-finance theory, Kyle–Back microstructure, activism, mandatory disclosure, takeover premia, Bayesian games, fixed-point methods.

> **Evidence standard.** Every claim below survived 3-vote adversarial verification against primary sources. Two plausible claims were **killed** (§5) — read them; they change the strategy. The research also has real **coverage gaps** (§6): the exotic far-field pivots were *not* verified, so "open to anything" is only partially answered by evidence.

---

## 1. Bottom line

The verified evidence points to **one winning archetype**, not a topic:

> **Framework-level theory, disciplined by structural estimation on newly machine-readable regulatory microdata, powered by one of the new structural-ML toolkits.**

The decisive, transferable edge is **not** the topic — it is the **toolkit** (§4). The topic that best combines framework novelty × structural feasibility × your comparative advantage is **an information-design reframing of mandatory disclosure, made structurally estimable on the 2024 Schedule 13D XML data** (the synthesis recommendation, §7). This is my interpretation built on the verified findings, flagged as such.

---

## 2. The three verified candidate directions (ranked)

### D1 — Activism / disclosure design, made STRUCTURAL  *(highest leverage FOR THIS candidate)*
- **Why.** The 5% Schedule 13D threshold is a *focal, genuinely contested* policy parameter — Ordóñez-Calafi & Bernhardt (JFQA 57(7), 2022) show tighten-vs-relax is a real welfare trade-off (uninformed investors can prefer lower thresholds; activists can prefer higher). It maps onto your existing edge directly.
- **The shock.** SEC 2024 rule: initial 13D deadline cut from within 10 days → **5 business days**; amendments now due within **2 business days** of a triggering event (was "promptly"); effective Feb 5, 2024.
- **The identification UNLOCK.** Same rule mandates all 13D/13G filings in a **13D/G-specific machine-readable XML** (distinct from XBRL), mandatory **Dec 18, 2024** — converting decades of HTML/ASCII free-text filings into parseable, filing-level **beneficial-ownership position data** (stake size, %, holder identity, control intent).
- **Enriched choice set.** Formal SEC guidance: cash-settled derivatives can confer beneficial-ownership status; certain engagement activities can trigger group formation (13(d)(3)/13(g)(3)) — i.e. derivative stake-building and coordinated engagement become modelable margins.
- **Honest caveats.** (i) The shock is a **uniform common change to all >5% filers** — no built-in cross-sectional control, so "clean natural experiment" is a design aspiration, not a guaranteed DiD. (ii) **Scooping risk by 2028**: empiricists have a 3–4-year head start on this exact data. (iii) See §5 — the claim that this niche is "wide open / pure-theory-dominated" was **REFUTED**.
- **Ceiling.** Top-15 reliably; top-10 if the structural model genuinely uses the new data to identify something a reduced-form paper cannot (e.g., the disclosure-cost / activist-type distribution).

### D2 — Information design / Bayesian persuasion as a disclosure LENS  *(framework-level, your edge reframed)*
- **Why.** Information design is the formal **dual of mechanism design** (Kamenica 2019, Ann. Rev. Econ.; Bergemann–Morris 2019, JEL): mechanism design fixes the information and chooses the game; information design fixes the game and chooses the **information allocation**. Named finance applications already exist: **stress tests** (Goldstein–Leitner; Inostroza–Pavan; Orlov et al.), **OTC markets** (Duffie–Dworczak–Zhu, JF 2017), **bank-run mitigation** (Ely 2017).
- **The move.** Reframe *mandatory disclosure* as an **optimal information-provision** problem — the regulator/firm chooses the disclosure rule (threshold, timing, granularity) as a persuasion design. This generalizes your static disclosure-threshold result into a framework-level statement.
- **Ceiling.** Top-10 *if* paired with a structural-estimation leg (otherwise it is "pure theory," which §5 and placement norms penalize). Toolkit to acquire: information design + a structural estimator.

### D3 — Intermediary / dynamic asset pricing, made ESTIMABLE  *(highest ceiling overall; biggest stretch)*
- **Why.** He–Krishnamurthy (2013, AER 103(2)) is the canonical continuous-time workhorse: a capital-constrained **intermediary** (not the household) is the marginal investor; risk premia spike **nonlinearly** when intermediary capital is scarce. It is the exemplar of the theory-plus-discipline template.
- **The gap = the opportunity.** HK2013 is **CALIBRATED, not ESTIMATED** (m=4 from bank-ownership data, 0.52 debt/asset from Flow of Funds, validated against MBS-spread crisis moments — but no GMM/MLE). Being among the **first to make a continuous-time GE intermediary model genuinely structurally estimable** (via the PINN solve-and-estimate toolkit, §4) is a framework-level contribution.
- **Honest caveats.** Furthest from your current human capital; highest execution risk; the enabling toolkit is 2024–2025 vintage with no established top-10 track record yet (§6).

**Far-field frontiers the brief named but the research did NOT verify:** climate/transition finance, fintech/crypto & on-chain market structure, networks/contagion, banking/macroprudential. These were dropped by budget/filtering (§6) — **their ceilings are unranked here.** "Open to anything" is therefore only partially answered; ranking them needs a second targeted pass.

---

## 3. What is "actually winning" — weak evidence, stated honestly

The brief asked for specific structural-theory-plus-estimation **JMPs that placed top-10 in 2023–2026, and why**. **No such individual placement case studies survived verification** (§6). The one verified award data point — 2025 AFA Dimensional First Prize (top *non-corporate* JF paper) to Catherine–Miller–Sarin, "Social Security and Trends in Wealth Inequality" (JF 80(3)) — is a **best-paper award, not a placement**, is **empirical not structural**, and prior years (behavioral trading 2024; macro/intangibles 2023) show **no clean multi-year trend**. Treat as topic-momentum noise, not signal.

---

## 4. The decisive edge: structural-ML toolkits (this is the real takeaway)

These are transferable across **all** directions above and are where a 2028 theorist gains an unfair advantage:

1. **LLM-derived economic measurement — with a mandatory discipline.** Ludwig–Mullainathan–Rambachan ("LLMs: An Applied Econometric Framework," NBER w33344, forthcoming Ann. Rev. Econ. 2026): valid downstream inference **requires combining LLM outputs with a small human-labeled validation sample**; absent it, "seemingly innocuous choices (which model, which prompt)" can flip parameter **magnitude, significance, and even sign**. Operationalized via Prediction-Powered Inference / Design-based Supervised Learning. → This is the gating discipline for any 13D-text-derived measure (e.g. parsing activist intent).
2. **LLM hidden states encode more than the text says.** Buckmann–Nguyen–Hill (Bank of England SWP 1150, 2025): a **linear probe on hidden states beats the model's own text output** for county- and firm-level statistics (extracts 9 firm-level financials for ~1,986 US firms). A concrete measurement primitive. Caveat: part may be memorization of public training data.
3. **Neural Network Estimator (NNE).** Wei–Jiang (Marketing Science 44(1), 2025): trains shallow nets to map data moments → structural parameters using **model-simulated data only** — no integrals over unobservables, no non-smooth objective. **Lower RMSE than SMLE** in consumer-search, largest edge at low compute. → Directly applies to **microstructure/activism games that are easy to simulate but hard to estimate classically.**
4. **AI ≡ structural estimation.** Igami ("AI as Structural Estimation," Econometrics Journal 23(3), 2020): AlphaGo's two-step architecture **is** two-step CCP/CCS estimation (SL policy net = Hotz–Miller 1993 CCP; RL value net = HMSS 1994 / BBL 2007 CCS). → A recipe for DNN/RL inside familiar dynamic-game estimators.
5. **Deep learning that SOLVES *and* ESTIMATES continuous-time GE finance models.** Fan et al. (Computational Economics 65(6), 2025): one PINN jointly handles the HJB, Kolmogorov-Forward, and moment conditions — **collapsing the solve-then-estimate barrier** that made structural estimation of continuous-time GE finance prohibitive. → This is what makes **D3 estimable, not just calibratable.**

---

## 5. REFUTED claims (killed 0-3) — these change the strategy

1. ❌ *"The disclosure/activism literature is dominated by pure game-theoretic models without structural estimation → open opportunity for a theory+structural JMP."* **Refuted 0-3.** Do **not** assume the structural-activism niche is empty; scope the existing structural work before committing. This downgrades D1's "wide open" appeal.
2. ❌ *"2025 AFA top corporate-finance (Brattle) prize went to a reduced-form mortgage lock-in paper → empirical corp/household finance is winning the flagship."* **Refuted 0-3.** No basis to infer empirical-is-winning from this.

---

## 6. What the research could NOT establish (coverage gaps)

- **No concrete top-10 JMP placement examples** survived verification — part (a) of the brief is only weakly addressed. The *archetype* is established; *named exemplars* are not.
- **No verified FTG / AFA / WFA / EFA student-award-by-direction data.**
- **Climate/transition finance, fintech/crypto/on-chain, networks/contagion, banking/macroprudential: unverified and unranked** (8 candidate claims budget-dropped). The far-field pivots are not covered.
- **Source quality:** toolkit + regulatory claims rest on primary/peer-reviewed sources (high confidence). The household-momentum and "clean natural experiment" framings are the weakest interpretive elements.

---

## 7. Recommendation (interpretation, built on the verified findings)

**The intersection of "highest ceiling" and "fastest for you" is a single synthesis direction:**

> **Reframe optimal mandatory disclosure (the 13D threshold/timing/granularity) as an information-design problem (D2 framework novelty), and make it structurally estimable on the 2024 13D XML data using NNE / LLM-validated measurement (D1 feasibility + §4 toolkits).**

This (a) reuses your disclosure/activism/Bayesian-games human capital, (b) clears the "pure theory" bar that §5 and placement norms penalize, (c) is harder to scoop than a reduced-form DiD because the contribution is the *estimable framework*, not the shock, and (d) gives a clean fallback: even if the structural leg is hard, the information-design theory + the new data descriptive work stands.

**Contrast with Track B** (the continuous-time Back-CDF extension, see `2026-06-06_track-b-design-section2-theorem-stack.md`): Track B is *pure theory* whose headline (disclosure-attenuation) the static paper already proves — a framing contradiction and a top-15/10 pure-theory ceiling. The synthesis direction above dominates it on every axis the verified evidence rewards.

### Immediate next moves
1. **Second deep-research pass** on the *unranked* frontiers (climate, crypto/on-chain, networks, banking) so "open to anything" is actually answered before committing.
2. **Scope the existing structural-activism/disclosure literature** (refuted-claim #1) — confirm the niche is not already occupied.
3. **Toolkit spike:** a 2-week NNE prototype estimating the *existing static model* on simulated data — validates feasibility at near-zero risk before any pivot.

---

## 8. Verified sources
- Ordóñez-Calafi & Bernhardt, "Blockholder Disclosure Thresholds and Hedge Fund Activism," JFQA 57(7), 2022 — cambridge.org/core/journals/.../3A56BF8A41948A79931DDE3920BFA71E
- SEC Press Release 2023-219 — sec.gov/newsroom/press-releases/2023-219
- Federal Register 2023-22678, "Modernization of Beneficial Ownership Reporting" — federalregister.gov/documents/2023/11/07/2023-22678
- He & Krishnamurthy, "Intermediary Asset Pricing," AER 103(2), 2013 — mfm.uchicago.edu/wp-content/uploads/2020/07/He-Krishnamurthy-Intermediary-Asset-Pricing.pdf
- Kamenica, "Bayesian Persuasion and Information Design," Ann. Rev. Econ. 11, 2019 — annualreviews.org/.../annurev-economics-080218-025739
- Ludwig, Mullainathan & Rambachan, "LLMs: An Applied Econometric Framework," NBER w33344 / SSRN 5094968
- Buckmann, Nguyen & Hill, "Revealing economic facts: LLMs know more than they say," Bank of England SWP 1150, 2025 — arxiv.org/pdf/2505.08662
- Wei & Jiang, "Estimating Parameters of Structural Models Using Neural Networks," Marketing Science 44(1), 2025 — arxiv.org/pdf/2502.04945
- Igami, "Artificial Intelligence as Structural Estimation," Econometrics Journal 23(3), 2020 — arxiv.org/pdf/1710.10967
- Fan et al., "Deep Learning for Solving and Estimating Dynamic Macro-finance Models," Computational Economics 65(6), 2025 — link.springer.com/article/10.1007/s10614-024-10693-3
- AFA Prizes — afajof.org/prizes/

---

# PART II — Pass 2 (2026-06-08): Frontier directions within corporate finance / M&A / microstructure

> Second deep-research pass, scoped per author request to **corporate finance, M&A, and microstructure only** (climate and banking excluded; crypto in-scope only as DEX/AMM microstructure). 107 agents, 24 sources, 113 claims → 25 verified (**24 confirmed, 1 killed**). Award/working-paper evidence is strong; confirmed top-journal placements are thinner (see caveats).

## II.1 The convergence (this is the headline)

Both passes independently land on the same place: **the author's existing Kyle–Back × activism lineage is not something to abandon — it is the platform.** The aggressive "direction change" the author was willing to make turns out to be a change of **method** (theory → theory + structural estimation), not a change of **topic**. The single best direction reuses essentially everything already built (the κ noise-trading comparative statics, the fixed-point solver, the activism model) and adds a structural-estimation leg using the new toolkits.

This also **reframes Track B**: Track B tried to *extend* Back–CDF as pure theory and hit the framing contradiction (§9.1). Pass 2's verdict is the cleaner move — don't extend Back–CDF as theory; **be the first to structurally *estimate* its central price-impact decomposition** on the newly machine-readable data.

## II.2 Ranked frontier directions (verified)

### ★ D1 (TOP PICK) — Structurally estimate the two-channel price-impact decomposition
- **The open seam.** Collin-Dufresne & Fos (SSRN 2330561) and Back–Collin-Dufresne–Fos–Li–Ljungqvist (Econometrica 2018, ECTA14917) decompose equilibrium price impact into **(i) a classic Kyle asymmetric-information term + (ii) a NEW moral-hazard/governance term** (a novel source of adverse selection). Total price impact is constant while the two components fluctuate over **distinct state variables** — so they are in principle **separately identifiable** — but this has **never been done structurally.** The liquidity–efficiency sign is parameter-dependent (can flip), which is exactly the author's κ-comparative-statics machinery.
- **Why it fits.** This is the author's literal comparative advantage (continuous-time Kyle–Back, activism, fixed-point methods). Running start is maximal.
- **Data / identification.** 2024 13D/13G **XML mandate** → machine-readable activist accumulation paths; **Tick-Size-Pilot market-maker-profitability files** (Appendices B/C) → a rare observable dealer-economics moment. **Toolkit:** PINN solve-and-estimate for the continuous-time GE model + NNE for the limited-information posterior.
- **Ceiling:** high. **Competition:** medium — theory is known and senior authors are active, so novelty MUST come from the estimation leg (separating the two channels) + a fresh mechanism, not from re-deriving the model. **Execution:** medium-**high** — jointly identifying two latent price-impact channels is genuinely hard.
- **⚠ Mandatory scooping check (the gating open question):** *Has anyone already structurally estimated the two-channel decomposition?* Resolve this **before** committing — it is the whole bet.

### D2 — Market / exchange design (microstructure mechanism design)
- **The hottest award magnet right now:** Daniel Chen, "Optimal Exchange Design" (2025 WRDS-TME Best Paper); FTG 2025 First Prize Nurisso, "Learning by Lending Securities" (→ JFE 2026); FTG 2024 Runner-Up Blonien, "Size Discovery in Slow Markets." Regulator-relevant (fees, fragmentation, size discovery, securities lending).
- **But:** **most crowded** microstructure-theory lane (multiple recent prize winners) and **furthest from the activism/disclosure edge.** Data: tick-size/access-fee pilots, 600+ derived MIDAS metrics (free, 8,000+ securities). Best as a **secondary framing or combined with D1**, not the headline.

### D3 — M&A / corporate-control: toehold & takeover-auction structural theory
- **Award-validated:** FTG 2024 **First Prize** Xiaobo Yu, "A General Theory of Holdouts" (Columbia → CU Boulder) — a framework nesting takeovers/debt-restructuring/sovereign debt. The **toehold puzzle** (Betton–Eckbo–Thorburn, JFE 2009) is a still-open anomaly: across 10,000+ control bids only ~13% bid with a toehold, ~3% acquire pre-offer despite large premia; the auction model predicts a **bimodal** optimal rule (zero, or above ~9%).
- **The seam:** the holdout *headline* is taken (just won), but **toehold/bidding/payment-structure structural estimation is comparatively under-exploited** and squarely in the author's M&A + Bayesian-games scope. Data: SDC/Refinitiv M&A + 13D accumulation. **Toolkit:** AlphaGo-as-two-step CCP/CCS for the dynamic bidding game; NNE for auction parameters. **Ceiling:** high. **Competition:** medium.

### D4 — Corporate-bond / fixed-income market structure (the data-secure hedge)
- **Most accessible data of the four:** TRACE microdata (WRDS Standard/Enhanced + FINRA academic agreement, 36-mo delay incl. 144A, masked dealer IDs); curated FINRA bibliography active through Jan 2026; Treasury TRACE extends to govvies.
- **But least connected to the edge** — requires porting Kyle–Back to **OTC/search** microstructure (learnable, non-trivial). Best as a **structural-feasibility hedge** or a second empirical setting for a D1/D2 mechanism. **Ceiling:** medium-high.

## II.3 Data accessibility — the decisive practical filter
- **Turnkey (build the structural leg on these):** Tick-Size-Pilot public + MM-profitability files · 600+ derived **MIDAS** metrics · **TRACE** microdata · **2024 13D/13G XML**.
- **Gated / not turnkey (do NOT bet the estimation leg on these without securing early access):** raw MIDAS proprietary order-book feeds (~1B records/day, HFT domain) · **CAT** — access/governance **in flux** per the SEC's **April 16, 2026 concept release** · **firm-level Form PF** — public OFR API is aggregated/rounded/masked, granular data is FOIA-exempt → needs a regulator special-access arrangement (this gates any private-markets/PE/private-credit structural direction).

## II.4 Killed / honest caveats
- ❌ **Killed 0-3:** "exemptive relief permanently eliminated PII from the CAT." Don't rely on it.
- **Awards ≠ journals.** FTG/WRDS-TME are JMP/seminar recognitions and strong *leading* indicators, but the verified record is **heavier on awards/working papers than on confirmed top-5-econ / top-3-finance journal acceptances** (confirmed journal placements: Nurisso JFE 2026; the ECTA 2018 / JFE 2009 lineage). The placement-tier inference is softer than ideal.
- **Foundational ≠ frontier.** The Kyle–Back-activism lineage (2015–2018) and toehold theory (2009) are *platforms*, not 2023–26 frontier findings — novelty must live in the **unexploited structural-estimation leg.**
- **Crypto/DEX:** in-scope as microstructure but **produced no surviving verified claims** — unranked here.
- **Tick-Size Pilot** data collection ended March 2019 (files remain public, but it's a historical experiment).

## II.5 Updated recommendation
**D1 is the pick** — structurally estimate the two-channel (asymmetric-information vs. moral-hazard/governance) price-impact decomposition on the 2024 13D XML + Tick-Size-Pilot data, using PINN solve-and-estimate + NNE. It is the maximal-running-start, highest-fit direction; it converts the author's entire existing apparatus from a pure-theory paper into a structural one; and it dominates Track B. **D3 (toehold structural)** is the strong M&A alternative if the D1 scooping check comes back occupied. **D2/D4** are framings/hedges, not headlines.

**Gating next step before any commitment:** a focused **scooping-check pass** on whether the two-channel decomposition (or the toehold-puzzle structural resolution) has already been estimated in a recent working paper — this is the single fact that decides D1 vs D3.

## II.6 Pass-2 verified sources
- Back, Collin-Dufresne, Fos, Li & Ljungqvist, Econometrica 2018 — onlinelibrary.wiley.com/doi/abs/10.3982/ECTA14917
- Collin-Dufresne & Fos, "Insider Trading, Stochastic Liquidity, and Equilibrium Prices" — papers.ssrn.com/sol3/papers.cfm?abstract_id=2330561
- FTG Best Paper Awards — financetheory.org/about/best-papers-awards
- Daniel Chen, "Optimal Exchange Design" (2025 WRDS-TME) — economics.princeton.edu/news/daniel-chen-wins-the-2025-wrds-tme-best-paper-award/
- Betton, Eckbo & Thorburn / toehold puzzle — ecgi.global/publications/working-papers/merger-negotiations-and-the-toehold-puzzle
- SEC Tick-Size Pilot data — sec.gov/data-research/tick-size-pilot-program/tick-size-pilot-data-resources
- SEC MIDAS — sec.gov/securities-topics/market-structure-analytics/midas-market-information-data-analytics-system
- SEC CAT concept release (2026-37, Apr 16 2026) — sec.gov/newsroom/press-releases/2026-37-...
- OFR Hedge Fund Monitor / Form PF — financialresearch.gov/hedge-fund-monitor/datasets/fpf/
- FINRA TRACE academic data — finra.org/filing-reporting/trace/trace-independent-academic-studies
- Wei & Jiang, NNE, Marketing Science 44(1) 2025 — arxiv.org/abs/2502.04945
