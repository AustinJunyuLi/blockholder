# Literature & originality referee report — framework_v3

Referee: literature-positioning & originality. Object: `framework_v3.qmd` (identical to
`framework_v3.pdf`). Date: 2026-08-19. Nothing in the repo was edited.

## Summary verdict (≤150 words)

The memo's *quotable gaps* are real and verbatim-accurate (C3), its misattribution fixes are
correct and important (C8a–c), and its venue metadata is almost all verifiable. But the two
load-bearing originality sentences are overstated in ways a JF/RFS referee will catch on page 1.
"First formalization of how the market learns about activism-driven control events" is false as
written — Kyle–Vila (1991), Back et al. (2018) and Cetemen et al. (JF 2026) all formalize exactly
that; Burkart–Lee themselves say the pre-disclosure problem "has been comprehensively studied by
Back et al. (2018)". "Nobody links market liquidity … to takeover premia" is contradicted by the
memo's own Section 4 anchors (Massa–Xu; Huang–Maharjan–Nanda) and by Maug (1998). Both survive
as narrower claims about the *disclosure partition*. Mello & Repullo (2004) — "Shareholder
Activism is Non-Monotonic in Market Liquidity" — is missing and must be confronted head-on.

## Claims table

| id | qmd line | claim | verdict | evidence (source + locus + quote/paraphrase) | proposed rewrite |
|---|---|---|---|---|---|
| C1 | 30–35 | inference partition is "the first formalization of *how the market learns about activism-driven control events*" | **WRONG** as written | (i) Kyle & Vila 1991, *RAND J. Econ.* 22(1):54–71, abstract via EconPapers: "A model of takeovers is investigated in which 'noise trading' provides camouflage that makes it possible for a large corporate outsider to purchase enough shares at favorable prices". (ii) `research/txt/burkart_lee_rfs2022.txt:1112–1114` (RFS p.1891): the pre-disclosure toehold problem "has been comprehensively studied by Back et al. (2018)". (iii) Cetemen–Cisternas–Kolb–Viswanathan, *JF* 81(3):1377–1435 (DOI 10.1111/jofi.70033): informed activists "time their trades in sequence to lower acquisition costs", leader–follower inference. (iv) `tmp_extract/Back-…-2018.txt:200–207`: the pre-disclosure-period debate, citing Bebchuk–Brav–Jackson–Jiang (2013). | "Pre-disclosure accumulation under a *fixed* disclosure horizon is well understood (Kyle–Vila 1991; Back et al. 2018; Cetemen et al. 2026), as is post-disclosure intervention choice *given* a toehold (Burkart–Lee 2022). We are the first to make the stake-triggered disclosure *rule* the object that partitions market inference — disclosed vs. inferred branches — and to price the takeover premium off that partition." |
| C2 | 35–38 | "Nobody — not OC&B, Cetemen et al., AFS, Johnson–Swem, or Celentano–Levine — links market liquidity or the disclosure rule to takeover premia, theoretically or structurally" | **OVERCLAIM** (true of the five named papers, false as a universal) | Named five hold up: AFS — no premium estimate anywhere (`research/txt/afs_jfe2022.txt`, only a "Market premium" *control* in Tables); Johnson–Swem — zero hits for `noise trad|accumulat|toehold|Kyle` in `tmp_extract/johnson-swem-2021-jfe.txt`; C&L — liquidity enters only as a reduced-form entry cost (below). Counterexamples: (i) Maug 1998, per `research/txt/burkart_lee_voss_2024.txt:325–326`: "In his comparison between takeovers and shareholder activism Maug (1998) emphasises how stock market liquidity affects the large shareholder's choice of intervention mode." (ii) Mello & Repullo 2004, *Finance Research Letters* 1:2–10, "Shareholder Activism is Non-Monotonic in Market Liquidity" (ref list, `research/txt/celentano_levine_2025.txt:1550`). (iii) Huang–Maharjan–Nanda, *JCF* 85 (2024) 102562: liquidity difference "reduce[s] acquisition premiums" (−4.46pp/SD, stock deals) — `tmp_read/dass2020.txt:55,146`. (iv) Massa–Xu, "The Value of (Stock) Liquidity in the M&A Market", *JFQA* — cited by the memo itself at §4. | "The empirical literature links liquidity to premia in reduced form (Massa–Xu; Huang–Maharjan–Nanda) and the theory literature links liquidity to the *mode* of intervention (Maug 1998; Mello–Repullo 2004). No paper — theoretical or structural — makes the *disclosure rule* the state variable that determines how liquidity maps into the premium; OC&B, Cetemen et al., AFS, Johnson–Swem and Celentano–Levine each hold one of the two levers fixed." |
| C3 | 42–45 | Back et al. call endogenizing the disclosure timing future work; Burkart–Lee "do not endogenize the acquisition of the toehold in anonymous, predisclosure markets" and leave the interaction open | **SUPPORTED** (quotable verbatim) | `tmp_extract/Back-…-2018.txt:1035–1039` (Ecta p.1454): "we assume that the horizon at which the activist's stake is disclosed is fixed and common knowledge… it might be interesting to endogenize the horizon"; next sentence names the 5% threshold. `research/txt/burkart_lee_rfs2022.txt:1111–1116` (RFS p.1891): "we do not endogenize the acquisition of the toehold in anonymous, predisclosure markets… We leave an analysis of how predisclosure and post-disclosure decisions interact to future work." | Quote both verbatim with page numbers (Ecta p.1454; RFS p.1891). Fix one slip: Back et al. call endogenizing the *horizon* future work (the 5% threshold is context, not the object). Also quote the immediately following BL sentence — "comprehensively studied by Back et al. (2018)" — and say why the partition survives it. |
| C4 | 46–51 | five named papers are the 2022–26 frontier, each "closes with a measurement section"; "a numerically verified headline result has no precedent" | **OVERCLAIM / partly WRONG** | Venues all check out: Burkart–Lee, *RFS* 35(4):1868–1896; LMM, *JF* 79(1) (repo bib) ; LMM "The Voting Premium", *JF* LXXXI(3), June 2026 (`research/txt/voting_premium_jf2026.txt:1`); Kakhbod–Loginova–Malenko–Malenko, "Advising the Management: A Theory of Shareholder Engagement", *RFS* 36(4):1319–1363; Chen–Gupta–Starmans, "Sustainable Investing and Market Governance", *JFE* 181:104273 (2026). But **Burkart–Lee has no measurement section**: headings run "1. The 'Equivalence' Benchmark … 4. Concluding Remarks" (`burkart_lee_rfs2022.txt:254–1080`). LMM 2024 ("VI. Implications for Empirical Research") and LMM 2026 ("E. Measurement", "VI. Empirical Implications") do. CGS is a sustainable-investing/price-informativeness paper — "in this space" is a stretch. "No precedent" is a taste assertion, unfalsifiable as stated; **UNCHECKED** for Kakhbod and CGS. | "Four of the five closest recent theory papers pair a single analytical mechanism with an empirical-implications section (LMM 2024 §VI; LMM 2026 §VI; …); Burkart–Lee 2022 closes on concluding remarks. We therefore prove the headline comparative static and label every numerical object as a regularity." Drop "no precedent"; drop CGS or justify its inclusion. |
| C5 | 52–55 | no published/SSRN-visible empirical work exploits Feb-2024; "one working paper engages the window trade-off theoretically" | **UNVERIFIABLE AS CITED** | `research/lit_frontier-scan.md:132`: "'Value-Destroying Activism' (NFA conference WP, **authors not confirmed** — portal page JS-blocked) — explicitly theorizes the 13D 5-day vs 10-day trade-off". The memo's sentence rests on a paper whose authors, title-of-record and existence were never confirmed. (SSRN sweep is another referee's assignment.) | Either identify the paper (authors, year, SSRN id) and cite it, or delete the clause. A JF referee will ask which paper; "one working paper" with no reference is worse than silence. |
| C6 | 57–61 | C&L "R&R at RFS"; "no trading, no price formation, and a stake fixed at the 5% statutory threshold"; −13.7% (−5.2pp); 36.6% | **SUPPORTED except "no trading/no price formation" (OVERCLAIM)** | Stake: `celentano_levine_2025.txt:517–518` — "The size of the activist stake (ν̄) is set to the statutory disclosure threshold of 5 percent". Premium: `:78` and `:707` — "the bid premium is 13.7 percent (5.2 percentage points) lower"; mean premium `:498` — "premium is 36.6 percent in our sample". But `:313`: "the term ξV(zt)νt reflects the costs arising from limited liquidity and information leakages associated with large share purchases" — liquidity *is* in the model, as a reduced-form entry cost. R&R status: SSRN 5506659 page reports R&R at RFS (also `lit/competitor_scope_tables.md` per `lit_frontier-scan.md:71`) — second-hand, so date-stamp it. | "…estimate activism's equilibrium effect on M&A with **no order-flow inference and no price impact** — liquidity enters only as a reduced-form entry cost — and a stake fixed at the 5% statutory threshold." Write "R&R at RFS (SSRN, Oct. 2025)" or drop the status line. |
| C7 | 65–69 | BEG (2012, ARFE) RPE vs forecasting efficiency; Goldstein (2023) lists RPE-oriented empirics **and** feedback × corporate-control frictions as open problems | **PARTIALLY SUPPORTED** | Goldstein 2023, *Review of Finance* 27(1):1–32, §3.2: "Bond, Edmans, and Goldstein (2012) distinguish between two types of efficiency. Forecasting price efficiency (FPE)… revelatory price efficiency (RPE)…". §5.2.a: "these measures of price informativeness are often linked to FPE and not to RPE" → RPE-measurement is flagged as open. §5.2.e: FPE/RPE divergence "is important for future research, such as when evaluating the effect of new information technologies". **No** corporate-control/takeover/governance item appears anywhere in §5.2 (grep of the whole future-research section returns zero hits for governance/corporate control/takeover/activism). | Keep the RPE framing and the RPE-measurement gap (quote §5.2.a). Delete "and feedback interacting with corporate-control frictions" or attribute it to Edmans–Goldstein–Jiang (2012, *JF* 67:933–971, prices and takeovers) rather than to Goldstein's open-problem list. |
| C8a | 336–338 | the −13.7% premium finding is Celentano–Levine, not AFS | **SUPPORTED — fix is required** | `draft_v2.tex:130` currently says AFS "estimate that activism *lowers* takeover bid premia relative to a no-activist counterfactual". No such number exists in `research/txt/afs_jfe2022.txt`; it is C&L's (`:707`). | Reattribute; also re-check Proposition `prop:d7-afs`, whose name encodes the wrong attribution. |
| C8b | 336–338 | delete the unsupported Johnson–Swem window-isomorphism sentence | **SUPPORTED** | `draft_v2.tex:130` claims J&S have a model "in which the pre-disclosure accumulation window plays the role of cumulative noise-trading cover". `tmp_extract/johnson-swem-2021-jfe.txt`: zero hits for noise trading / accumulation / toehold / Kyle; the only 13D mention is institutional ("Form 13-D within ten days", `:1041`). The prior brief `lit_frontier-scan.md:117` ("J&S owns the σ²T↔13D-window isomorphism") is wrong. | Delete, and attribute the window↔cumulative-noise mapping to Back et al. 2018 (Ecta p.1436: shortening the anonymous-trading period "has the effect of reducing cumulative noise trading"). |
| C8c / C10 | 336–338; 137–139 | EGJ (2015) prove region-wise uniqueness analytically — cite the posture, not "numerical uniqueness" | **SUPPORTED** | Edmans–Goldstein–Jiang, *AER* 105(12):3766–97, published PDF: "there is a range for which the equilibrium is unique and involves the speculator buying on good news and not trading on bad news"; and, formalized in Prop. 1, "there is a strictly positive range of parameters (κ_T ≤ κ < min(κ_SNB, κ_NT)) for which BNS is the only pure-strategy equilibrium under feedback". No numerical uniqueness verification. | `draft_v2.tex:702` and `:2235` ("we verify uniqueness numerically … following the methodological precedent of EGJ 2015") are a misattribution and must be rewritten: EGJ characterize uniqueness *analytically over parameter regions*; our claim is that we adopt their region-wise posture, not their method. |
| C8d | 336–338 | "LMM 2024 prove non-Kyle technologies are top-3-acceptable" | **OVERCLAIM (wording)** | `research/txt/levit_malenko_maug_jf2024.txt:154, 678–683, 850`: shareholders trade in a "competitive market"; "the share price is determined by the valuation of the marginal shareholder"; no market maker, no noise trader, no Kyle λ. So "non-Kyle" is accurate; "prove … acceptable" is not a theorem of theirs. | "A *JF* paper on trading and governance (LMM 2024) prices shares off the marginal shareholder rather than a Kyle market maker; the discrete order-flow technology used here is a defensible modelling choice, not a deviation from frontier practice." |
| C8e | 336–338; 224–226 | add LMM (2024, 2026), Burkart–Lee–Voss (2024), Chen–Gupta–Starmans (2026), Ben-David et al. (2026); CARs are price impact, not value creation | **SUPPORTED, with two metadata fixes** | BLV = ECGI WP 956/2024, "The Evolution of the Market for Corporate Control" (working paper, not a journal cite). Ben-David et al. is published: *JF* 2026, DOI 10.1111/jofi.70038 — **four** authors (Ben-David, Bhattacharya, **Ruidi Huang**, Jacobsen); the repo's NBER WP (`bendavid_missing_relation_jf2026.txt`) has three. Their claim, verbatim: "CAR is an unreliable measure of expected value creation" — the memo's §4 usage is fair. | Cite BLV as ECGI WP 956/2024 (or check for publication); add Ruidi Huang to the Ben-David bib entry. **Also add Burkart–Lee (2022) itself — it is quoted as the central gap but is absent from `bibliography.bib`.** |
| C9 | 201–203 | Corum–Levit 2019 Prop. 4 as the "non-monotonicity as identification device" template | **SUPPORTED (with a scope note)** | `research/txt/corum_levit_jfe2019.txt:949–950`: "Proposition 4 If the equilibrium exhibits only selection then Λ is strictly decreasing in b. If the equilibrium exhibits treatment then Λ is non-monotonic in b." Preceded by: the comparative statics of Λ w.r.t. b "can help to distinguish between the selection and the treatment effects in equilibrium". | Say what the device is: non-monotonicity in a *governance primitive* (board private benefits b) separates selection from treatment. Ours is non-monotonicity in *liquidity* separating an inference channel from an entry channel — an analogy, so label it as one. |
| C11 | 30–38, 336–338 | venues/attributions | **SUPPORTED (topical fit is the weak link)** | Ordóñez-Calafi & Bernhardt, "Blockholder Disclosure Thresholds and Hedge Fund Activism", *JFQA* 57(7):2834–2859 (DOI 10.1017/S0022109022000059) ✓. Cetemen, Cisternas, Kolb & Viswanathan, "Leader-Follower Dynamics in Shareholder Activism", *JF* 81(3):1377–1435 ✓. Kakhbod, Loginova, A. Malenko & N. Malenko, "Advising the Management: A Theory of Shareholder Engagement", *RFS* 36(4):1319–1363 ✓. | OC&B and Cetemen et al. are squarely in the space. Kakhbod et al. is engagement theory with no trading, no disclosure rule, no takeover; Chen–Gupta–Starmans is sustainable investing. Either widen the phrase ("governance-through-markets theory") or swap in Burkart–Lee–Voss (2024) and Corum–Levit (2019). |

## Originality assessment

**(a) Closest existing papers, and what they already do.** *Kyle & Vila (1991)* already formalizes
noise-trading camouflage enabling a control-seeking outsider to buy "at favorable prices", and
already delivers a liquidity-distorts-control-efficiency result. *Back et al. (2018, Ecta)* embeds
an activist in a continuous-time Kyle model with a fixed disclosure horizon; *Cetemen et al.
(JF 2026)* adds dynamic multi-activist inference. *Burkart & Lee (2022, RFS)* takes the toehold as
given and solves the takeover-vs-activism-vs-brokerage choice. *Ordóñez-Calafi & Bernhardt (2022,
JFQA)* designs the disclosure threshold, trading off adverse selection against discipline.
*Mello & Repullo (2004)* already titled a paper "Shareholder Activism is Non-Monotonic in Market
Liquidity". *Celentano & Levine (2025)* structurally estimates activism's effect on takeover
probability and premia. *Massa–Xu* and *Huang–Maharjan–Nanda (2024, JCF)* already estimate
liquidity→premium elasticities.

**(b) What is genuinely new.** Three things, and only three. (1) The *disclosure partition*: the
same primitive (a stake-triggered rule) simultaneously determines which states become common
knowledge and which remain order-flow inference, and the takeover premium is priced off both
branches. The proved κ-invariance of the disclosed branch, giving the cross-partial
∂²Δ/∂κ∂τ < 0, is a genuinely new comparative static — nobody above has a disclosure regime *and*
a bidder. (2) τ as a policy lever on **revelatory** (not forecasting) price efficiency — the RPE
framing is standard, but a *rule* as the lever on RPE in the corporate-control setting is not.
(3) The February 2024 five-business-day acceleration as a dated shock with a signed prediction
(attenuation) rather than a narrative.

**(c) Objections I would raise as referee.** (i) "Kyle–Vila and Back et al. already model
market learning about control events; your contribution is the *partition*, so stop saying
'first formalization'." (ii) "Mello–Repullo (2004) put non-monotonicity-in-liquidity in a title
twenty years ago; you do not cite them. What is new in your hump?" (iii) "Maug (1998) already
makes liquidity govern the intervention-mode choice; your 'nobody links liquidity to control'
sentence is unsustainable." (iv) "Your own §4 cites two papers estimating liquidity→premium
elasticities. Which sentence survives?" (v) "ω_P(τ) with ω_P′>0 is assumed, not derived. The
headline theorem is then a corollary of an assumption; the shock only tests the assumption's
sign." (vi) "Is the region-certified hump a theorem or a computation? If the latter, why is it in
the paper at all rather than an appendix?"

**(d) Is "revelation technology of the market for corporate control" credible or grandiose?**
Credible in substance, grandiose in delivery. The mechanism — a rule that partitions inference —
genuinely is a revelation technology in the mechanism-design sense, and RPE gives it a
respectable label (Bond–Edmans–Goldstein 2012). But "the market for corporate control" is
Manne's phrase for a very large object, and the model has one blockholder, one bidder, one
market maker, ternary order flow, and no auction. I would tolerate the phrase in the
introduction if the abstract says something narrower and checkable: "how the 13D disclosure rule
partitions market inference, and how that partition determines the sensitivity of takeover premia
to liquidity."

**(e) See the next section** for the citations to add and the misattributions to fix.

## Additional citations to add / misattributions to fix (full references)

**Must add (each is a referee-visible hole):**

1. Kyle, Albert S., and Jean-Luc Vila. 1991. "Noise Trading and Takeovers." *RAND Journal of Economics* 22(1): 54–71. — the original liquidity-camouflage-takeover model; C1 cannot stand without engaging it.
2. Mello, Antonio S., and Rafael Repullo. 2004. "Shareholder Activism is Non-Monotonic in Market Liquidity." *Finance Research Letters* 1(1): 2–10. — direct precedent for T4; must be distinguished (theirs: intervention incentives; ours: premium through the inference partition).
3. Burkart, Mike, and Samuel Lee. 2022. "Activism and Takeovers." *Review of Financial Studies* 35(4): 1868–1896. — quoted as the central gap yet **absent from `bibliography.bib`**.
4. Burkart, Mike, Samuel Lee, and Paul Voss. 2024. "The Evolution of the Market for Corporate Control." ECGI Finance Working Paper No. 956/2024. — also the cleanest cite for "Market liquidity plays no role in our analysis", which is why they are not a competitor.
5. Bebchuk, Lucian A., Alon Brav, Robert J. Jackson Jr., and Wei Jiang. 2013. "Pre-Disclosure Accumulations by Activist Investors: Evidence and Policy." *Journal of Corporation Law* 39(1): 1–34. — the policy debate the τ lever belongs to; Back et al. cite it for exactly this.
6. Massa, Massimo, and Moqi Xu. "The Value of (Stock) Liquidity in the M&A Market." *Journal of Financial and Quantitative Analysis* (verify volume/year at proof — the memo says 2013).
7. Huang, Sheng, Johan Maharjan, and Vikram K. Nanda. 2024. "Liquid Stock as an Acquisition Currency." *Journal of Corporate Finance* 85: 102562. — memo's 3-author citation is **correct**; the 4-author `tmp_read/dass2020.txt` (with Nishant Dass) is the earlier WP. Cite the published 3-author version.
8. Kakhbod, Ali, Uliana Loginova, Andrey Malenko, and Nadya Malenko. 2023. "Advising the Management: A Theory of Shareholder Engagement." *Review of Financial Studies* 36(4): 1319–1363.
9. Chen, Alvin, Deeksha Gupta, and Jan Starmans. 2026. "Sustainable Investing and Market Governance." *Journal of Financial Economics* 181: 104273. — cite it accurately or drop it; it is not an activism/takeover paper.

**Misattributions to fix in `draft_v2.tex`:**

- `:130` — AFS do **not** estimate a premium reduction; that is Celentano & Levine (−13.7%, −5.2pp). Rename `prop:d7-afs` accordingly.
- `:130` — Johnson & Swem have no accumulation-window/noise-cover mechanism. Delete the sentence; the isomorphism is Back et al.'s.
- `:702`, `:2235` — EGJ (2015) do **not** verify uniqueness numerically; they characterize it analytically over parameter ranges (AER 105(12), Prop. 1). Cite the *posture*, not the method.
- Ben-David et al. (JF 2026, DOI 10.1111/jofi.70038) has four authors: Ben-David, Bhattacharya, **Ruidi Huang**, Jacobsen.
- Bond, Edmans, and Goldstein. 2012. "The Real Effects of Financial Markets." *Annual Review of Financial Economics* 4: 339–360 — correct source for RPE/FPE; Goldstein (2023) *Review of Finance* 27(1): 1–32 is the survey that flags RPE measurement (§5.2.a) but **not** corporate-control frictions.

## Searches performed and access failures

| # | query / source | tool | date | outcome |
|---|---|---|---|---|
| 1 | Back et al. 2018 future-work + disclosure horizon | grep `tmp_extract/Back-…txt` | 2026-08-19 | verbatim found (p.1454, p.1436) |
| 2 | Burkart–Lee 2022 "three gaps" passage | grep `research/txt/burkart_lee_rfs2022.txt` | 2026-08-19 | verbatim found (p.1891) |
| 3 | Celentano–Levine: 13.7 / 5.2 / 36.6 / stake / liquidity | grep `research/txt/celentano_levine_2025.txt` | 2026-08-19 | all found; ξ liquidity cost found |
| 4 | AFS premium numbers | grep `research/txt/afs_jfe2022.txt` | 2026-08-19 | none (only a control variable) |
| 5 | Johnson–Swem noise/accumulation/toehold/Kyle | grep `tmp_extract/johnson-swem-2021-jfe.txt` | 2026-08-19 | zero hits |
| 6 | Corum–Levit Prop. 4 | grep `research/txt/corum_levit_jfe2019.txt` | 2026-08-19 | verbatim found |
| 7 | LMM 2024 trading technology; section headings of LMM24/LMM26/BL22 | grep `research/txt/*` | 2026-08-19 | marginal-shareholder pricing; BL has no measurement section |
| 8 | Kakhbod et al. RFS 2023 title | WebSearch | 2026-08-19 | confirmed |
| 9 | Chen–Gupta–Starmans JFE 2026 | WebSearch | 2026-08-19 | confirmed (sustainable investing) |
| 10 | Kyle & Vila 1991 abstract | WebSearch + WebFetch (EconPapers) | 2026-08-19 | abstract retrieved |
| 11 | Huang–Maharjan–Nanda JCF 2024 authors | WebSearch | 2026-08-19 | 3 authors confirmed, JCF 85:102562 |
| 12 | Ordóñez-Calafi & Bernhardt JFQA 2022 | WebSearch | 2026-08-19 | 57(7):2834–2859 confirmed |
| 13 | Cetemen et al. JF 2026 | WebSearch | 2026-08-19 | 81(3):1377–1435 confirmed |
| 14 | Ben-David et al. JF 2026 | WebSearch | 2026-08-19 | published, 4 authors, DOI 10.1111/jofi.70038 |
| 15 | Celentano–Levine R&R at RFS | WebSearch (SSRN 5506659) | 2026-08-19 | asserted by SSRN page; second-hand |
| 16 | Goldstein 2023 RPE + future research | WebFetch → local `pdftotext` | 2026-08-19 | §3.2 and §5.2 read directly |
| 17 | EGJ 2015 uniqueness | WebFetch → local `pdftotext` | 2026-08-19 | region-wise analytic uniqueness confirmed |
| 18 | theory paper on the 13D window ↔ premia (counterexample hunt) | WebSearch | 2026-08-19 | nothing academic surfaced; only law-firm client alerts |

**Access failures / unchecked:**

- `lit/maug-1998.pdf` and `lit/kahn-winton-1998.pdf` yield **no text** under `pdftotext` (image-only scans). Maug (1998) was assessed via Burkart–Lee–Voss's characterization; **Kahn & Winton (1998) UNCHECKED**.
- Whether Kakhbod et al. (2023) and Chen–Gupta–Starmans (2026) "close with a measurement section": **UNCHECKED** (paywalled; the C4 claim is already falsified by Burkart–Lee).
- Bolton & von Thadden (1998) and Cornelli & Li (2002) as C2 counterexamples: **UNCHECKED** (budget).
- The SSRN sweep for Feb-2024 empirical work is another referee's assignment; not attempted here.
- `ego-browser` was not needed — no paywall blocked a load-bearing claim.
