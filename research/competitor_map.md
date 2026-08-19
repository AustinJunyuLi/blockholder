# Competitor map and whitespace table — ticket 02

**Date: 2026-08-19.** Built from `research/cards/` (42 verified cards, ticket 01 + the 2024–26 sweep) and `research/cards/INDEX.md`.
Every cell below is traceable to a card section and page. Quotes are copied verbatim from a card's §6 or §8;
where a card records a full-text grep, the grep is cited rather than paraphrased as "they never mention X".
Vocabulary is `CONTEXT.md`'s: position, whitespace, competitor set, anchor, threshold margin, window margin,
partition, control outcome, premium wedge, honesty label.

**Scope of this file.** Part 1 is the competitor table (11 rows = the `CONTEXT.md` competitor set, the author's
own `proposal/` included). Part 2 lists the occupied cells a position must not claim. Part 3 enumerates
whitespace cells along three axes with a refutation check and a rating for each. The fresh 2024–26 SSRN / NBER /
journal-forthcoming sweep is **done** (`research/sweep_2024_26_A.md`, `research/sweep_2024_26_B.md`): its two carded
hits are in the "2024–26 sweep additions" sub-table at the end of Part 1, its query counts and "none found"
statement are in the Sweep summary below that, and each Part-3 item carries a one-line **Sweep check**. One DIRECT
hit could not be obtained and is flagged for manual download.

---

## PART 1 — The competitor table

Margin column reads: which margin of the disclosure rule the paper occupies, and whether it enters as a **LEVEL**
(a fixed value used or varied), a **CHANGE** (a dated move in the rule), or **background** (named in prose,
never a model object or a treatment).

| Paper (card file) | Venue / stage | Object studied | Margin of the disclosure rule | Identification | Liquidity's role | What the paper explicitly does NOT do — verbatim, page-cited | Source (card §, page) |
|---|---|---|---|---|---|---|---|
| `celentano_levine_2025.md` | SFI Research Paper 25-81 (24 Oct 2025); **R&R, *Review of Financial Studies*** (venue from SFI/RePEc/author page, not the PDF). **Every page cite in this row is to the PDF read, whose own title page is dated 1 Oct 2025** — not necessarily the 24-Oct deposit *(added by verifier)* | Takeover volume, **bid premium**, CEO turnover, shareholder value — jointly, in general equilibrium | **None.** 5% enters once, as the calibration constant ν̄ ("set to the statutory disclosure threshold of 5 percent", p. 16) — **background**. Window absent; 2024-02-05 never mentioned | Structural SMM, 52,666 firm-years 2001–2019, no design-based variation, no shock | **Absent.** One clause inside the scalar entry cost ξ (Q1, p. 10); zero hits for Kyle / Amihud / market maker / order flow / bid-ask / price impact | "Modeling the marginal costs of each stage of an activist campaign, and the activists' decision to escalate a campaign, is beyond the scope of this paper." (p. 10, fn. 5) | §6, §7; §8 Q1, Q2, Q6, Q11; §9 scope greps |
| `johnson_swem_2021_jfe.md` | *JFE* 139 (2021) 29–56, published | Campaign frequency, settlement, proxy fights, 3-day announcement CAR — campaign success, **no control outcome** | **None.** The ten-day window appears once, in background fn. 13 (p. 39); **the 5% threshold is never stated** and the word "disclosure" occurs zero times in the article — **background** | Structural MLE (closed-form likelihood), 2,434 hedge-fund campaigns 1999–2016, plus reduced-form validation regressions | **Absent as a variable, named as a cost.** "round trip liquidity costs" is one of four items inside the lognormal draw L̃ (Q1, p. 32); price impact named on p. 30 (Q13). No target-stock liquidity proxy in any specification; OA greps return `liquid*` 0 | "Activists in our model differ only by their average cost of proxy fighting." (p. 52) | §6, §7; §8 Q1, Q2, Q7, Q13; §9 + §9b greps |
| `cetemen_cisternas_kolb_viswanathan_2026_jf.md` | *Journal of Finance*, forthcoming 2026 (read as **NY Fed Staff Report 1030**, rev. Jul 2025 — not the JF typeset article) | Predictability of informed order flow E[θᴸ]; ex-ante firm value; average price around a disclosure event | **None.** 13D appears three times, all prose/footnotes; the 10→5 business-day change is fn. 8, p. 11 — **background** and a compliance cost in §5.3. Neither margin is a parameter, a choice or a comparative static | Theory only. No data, no estimation, no calibration; §4.2 reinterprets other people's estimates | **Driver** — σ (noise-trading volatility) is the comparative static, **and the sign runs against the usual story**: as σ → ∞ manipulation does not vanish (Thm 2(iii.1), p. 24) | "Our model is then best interpreted as taking place in such a pre-disclosure window when the activists have superior information and are gearing up to quickly finalize their positions and attack." (p. 11) | §6(a)–(e), §7; §8 Q3, Q4, Q9, Q12; §9 greps (premium/tender/merger = 0) |
| `albuquerque_fos_schroth_2022.md` | *JFE* 145(2), 153–178 (2022) (read as **ECGI WP 685/2020**) | 13D/13G announcement return and its treatment / stock-picking / selection decomposition; ΔROA, sales turnover, proxy contest | **13D-vs-13G as the choice object, but neither margin as a treatment.** 5% is a sample-selection device — **background**; the 10-day window is used once, to drop 28,663 exempt February-14 filers (p. 24) — **background** | Structural MLE on a discrete-choice + selection model, 69,937 filings 1996–2017, no rule change, no design-based variation | **Control variable.** Amihud illiquidity is one of twelve firm characteristics in x; loads +0.021\*\*\* / +0.019\*\*\* on µ_D / µ_G, read as an illiquidity premium (p. 27) | "Investors may take into account the price impact of their trading before crossing the 5% ownership threshold. We leave these extensions for future research." (p. 41) | §6, §7; §8 Q1–Q3, Q9–Q11, Q13; §9 R12 grep (`13.7` = 0 hits) |
| `back_et_al_2018_ecta.md` | *Econometrica* 86(4), 1431–1463 (2018), published | Economic efficiency P̄(0,0) (the initial share price) and endogenous market illiquidity λ̄ | **Window discussed twice and then collapsed into σ²T** — p. 1453: reducing T "isomorphic to reducing noise trading volatility". So the window is a **LEVEL**, but only as a rescaling of σ, not as a partition. Threshold: motivation only (fn. 13, p. 1436) — **background** | Theory only. Zero hits for regress / data / standard error / estimate; one "sample" hit, pointing at somebody else's evidence (p. 1452) | **Driver, and the paper separates two liquidities on purpose:** exogenous noise-trading volatility σ vs endogenous Kyle lambda λ̄, which can move in opposite directions (p. 1443) | "Allowing T to be a choice variable would be an interesting extension, but it is beyond the scope of this paper." (p. 1435, fn. 10) | §6, §7; §8 Q1–Q3, Q7, Q8; §9 greps |
| `trivedi_2026_ssrn.md` | SSRN working paper, "June 2026"; independent researcher, no affiliation, **not peer reviewed**, self-disseminated | Realised filing lag; share filed within five business days; Δ Corwin–Schultz spread; Δ Amihud; forward abnormal monthly return. **No control outcome** | **Window margin, as a CHANGE.** 2024-02-05, ten calendar days → five business days. 5% mentioned once, descriptively (p. 2), never varied | **DiD**, 13D treated (148) vs 13G control (185), 333 filings, 133 event-date clusters, ±180 days, event-date-clustered SEs, self-hosted pre-registration; plus an OOS predictive test with permutation nulls | **Outcome / nuisance.** Amihud and spread are DiD *outcomes* (both null); κ = 10% is a participation cap in the bounds program. Never a driver: no cross-sectional liquidity split, no interaction of any kind | "the 2024 rule moved timing compliance at the margin without detectable repricing, which raises a mechanism question and is more interesting than a clean positive" (p. 11) | §6, §7; §8 Q1, Q5, Q6, Q10; §9 greps (takeover/premium/stake/activis*/block* = 0) |
| `corum_2025_ssrn.md` | Working paper, 15 Apr 2025 (SSRN 4319599); no journal, no R&R stated | Expected NPV of an implemented intervention V\*; probability of effort ρ\*; mass of value-destroying entrants µ\*_B | **Two scalars, η (entry) and λ (exit), each = the fraction of the stake tradable before disclosure bites — formally *threshold* objects (LEVEL), with the window reforms mapped onto them** (fn. 22, p. 26). He calls the 10→5 initial-window change *proposed*, not adopted, and assigns the *adopted* 2024 rule to the exit side | Theory only. No data, no figures, no tables, no simulations; one numerical example in fn. 31 | **Driver, but two-state.** With probability λ (η) noise trading is "very high" and the market maker infers nothing; otherwise it infers perfectly (p. 74). No depth, no price impact, no Kyle λ, no continuous noise variance | "In contrast to these papers, in my paper, there is no other player that affects the firm value other than the blockholder." (p. 9) | §6, §7; §8 Q3–Q5, Q8, Q10; §9 greps (bidder/premium/tender/merger = 0 in 77 pp) |
| `corum_levit_2019_jfe_published.md` | *JFE* 133(1), 1–17 (2019), published | Probability of a takeover θ\*; proxy-fight frequency; announcement CARs. Expected premium π\* exists but takes two values and carries **no comparative static in any of the seven Predictions** | **Threshold LEVEL — occupied but sterile.** ᾱ *is* the 13D trigger, calibrated ᾱ ∈ [5%, 10%] (p. 10), and simultaneously the liquidity break and the pill trigger; no proposition, corollary or prediction is a comparative static in ᾱ. **Window: absent** (`13G` = 0 hits; "days" only in "in the old days") | Theory only, plus one descriptive frequency (232 proxy fights, 1994–2015, no SE, no controls) | **Fused with the threshold.** "the stock is perfectly liquid (illiquid) for small (large) orders" (Q1, p. 10) — a step function at ᾱ; the Kyle formulation is demoted to fn. 23 with no proof anywhere | "Assuming that the activist cannot launch a proxy fight before the bidder arrives is for simplicity. Identifying the activist's effect on the takeover, which is the focus of this section, is challenging when a proxy fight is only used as a threat." (p. 10, fn 25) | §4, §6, §7; §8 Q1–Q6, Q8, Q9, Q12 |
| `polk_buchheit_riley_stone_2024_jfrc.md` | *Journal of Financial Regulation and Compliance* 32(4), 516–538 (2024), published | The **filer's own** cumulated abnormal return over the quiet period (trigger date → filing date), and abnormal trading volume | **Window margin only.** The rule change (10 → 5, 2024-02-05) is the motivation, but it is evaluated on **pre-rule data only** — a cross-section of self-selected delays, i.e. a **LEVEL** comparison offered as a projection of a CHANGE. 5% taken as given | Descriptive event study, 9,685 initial 13Ds, 2001–2022. **No control group, no post-rule data, no regression, no standard errors, no placebo** | **Absent.** Verifier grep on a fresh `-layout -raw` extraction: `liquid*`, `Amihud`, `bid-ask`, `spread`, `turnover`, `takeover`, `premium`, `bidder` all **0 hits** | "it may be the case that activist shareholders will adjust to exploit 'information asymmetry' over the investing public over a shorter time horizon after the five-day regime is implemented" (p. 531) | §6, §7; §8 Q1, Q3, Q8–Q10, Q13–Q15 |
| `bishop_fos_jiang_partnoy_2026.md` | HKU Jockey Club GRI Paper Series 2026/006, working paper (the PDF names **no journal**; running header is the placeholder `Journal Name`) | P(firm-month contains an activism announcement) — i.e. target selection; and industry HHI | **The HSR antitrust notification threshold, not a 13D margin.** 13D's 5% is used **only to define "toehold"** (p. 23); the 13D window appears in prose (fn. 15, p. 19; p. 36) with **no effective date, no 13D/A, no 13G** — **background** | Discontinuity in a polynomial-control LPM at the HSR dollar threshold, 1.27m firm-months 2000–2024, firm/year FE, double-clustered; plus a same-3-digit-SIC DiD on HHI they refuse to call causal | **Absent.** `liquid`, `Amihud`, `volume`, `price impact` = **0 hits** in 46 pp; `turnover` has one hit, a reference title | "We are careful in this section not to draw causal conclusions, particularly given the complexity of identifying the potential relationship between an appropriate control group and trends in industry consolidation." (printed p. 29) | §4, §6, §7; §8 Q4–Q6, Q8, Q10, Q11 |
| `author_proposal_outline_2026.md` | The author's own research proposal + execution plan, Aug 2026. **Unpublished; not a paper.** Per ADR-0004 it "does not reserve the Feb-2024 anchor" | Campaign entry and target composition; stake at filing and trigger-to-filing accumulation; Item 6 derivative language; filing return (secondary); filing delay and 6/12-month bid hazard (**descriptive, CIs only**) | **Window margin only, as a CHANGE** (Feb-2024), entering as `d` in the cost `C(x;d,L)` and in the cap `Δx̄_i(d)`. **Threshold not occupied as a disclosure margin** — 5% is only the clock-start and a scale factor. (A *control*-threshold prediction is occupied: λ_app jumps at the blocking threshold 1−τ_c) | Continuous-dose (`RTD_i × Post`) generalised DiD on the 13D filer population, **no control group**; activist × quarter + liquidity-decile × quarter + size-decile × quarter FE; ≥500 placebo dates, ≥500 RTD permutations | **Nuisance.** Liquidity enters twice — as the cost shifter λ_L(L) and as the ADV denominator of RTD — and liquidity deciles are then absorbed by fixed effects. No control outcome is ever asked to move *with* liquidity | "The activist's stake is not solved as an endogenous signal." (`model.tex:432-435`) and "Endogenising the filing price is left for separate work." (`model.tex:447-448`) | §6, §7; §9 Q1, Q4–Q6, Q8, Q10 |

### Reading notes — one line per row, for what the row cannot carry

1. **Celentano–Levine.** The headline "activism cuts the bid premium 13.69%" is a *marginal* counterfactual conditional on a campaign; **in general equilibrium the same paper reports −0.60%** (36.70 vs 36.92, Table 5, p. 44). No standard error appears anywhere in Tables 4–9, and the friction that drives it, c_m(ν̄) = 0.135, has SE 0.047 against c_m(0) = 0.151 (SE 0.011). Also: the venue line (SFI 25-81, RFS R&R) is external metadata, not in the PDF, and a 17 Nov 2025 revision was not obtained.
2. **Johnson–Swem.** The σ²T / window↔noise-trading object our old notes attributed to them **is not in the paper**; it belongs to Back et al. (2018). Their filing is a *point in time* — buying and filing are one move (Q3, p. 32) — so there is nothing to endogenise; the card's instruction is "do not claim they leave endogenous T open; claim they never model it."
3. **CCKV.** Their whole three-period game sits **inside** an unmodelled pre-disclosure window; the crossing is outside the model altogether, and no agent ever learns that a blockholder holds a block (fn. 16, p. 15). Six of eight propositions are proved only in an Internet Appendix we do not hold, and the σ → 0 half of the liquidity theorem routes through one of them.
4. **Albuquerque–Fos–Schroth.** There is **no takeover-premium result anywhere in the paper** — `13.7` returns 0 hits, `takeover` 3 hits (all footnotes/references). Their own fn. 16 (p. 34) concedes that a 13G price may already embed the option of a later 13D, i.e. they see the partition and treat it as a downward bias.
5. **Back et al.** The window **collapses into σ²T** (p. 1453) — in their world a shorter window is a re-parameterisation, not a mechanism. Theorem 2(i) is two one-way implications, **not an iff**, and it is silent exactly where the empirically relevant technologies live (their own bounded Examples 4–5, neither convex nor concave). Do not cite it as an "if and only if".
6. **Trivedi.** The only positive result is a first stage on *compliance timing* (+0.348, p = 0.007), and the author himself notes it does not clear his Harvey–Liu–Zhu t > 3 hurdle (p. 11). **The paper never states the sampling frame behind its 333 filings** — cite R2 as "a working paper reports the window bit on compliance", never as "the window bite is established". Its two microstructure nulls were added after the pre-registration lock (Q10, p. 25).
7. **Corum (2025).** The threshold/window distinction is **conflated by construction**: a 10→5 business-day change and a lower stake trigger both simply "reduce η" (fn. 22, p. 26). His own algebra already breaks the entry/exit symmetry (Prop. 7(ii)(b) has V\* rising in η and flat in λ) and his prose never says so. His headline, Corollary 2, **has no proof anywhere in 77 pages**.
8. **Corum–Levit.** The threshold is **occupied but sterile**: ᾱ is one scalar doing three jobs (liquidity break, 13D trigger, pill trigger), so no comparative static in it is stated or interpretable as policy — and in half the parameter space (b ≤ Δ) it is **inert entirely** (p. 14). Worse for a premium position: π_{γ/α} decreases in α and α\* = ᾱ, so in their model a *higher* threshold means a *lower* premium (p. 8), and condition (8) implies π_{γ/α} < π_b (p. 9). The flagged state never occurs on path.
9. **Polk et al.** Their treatment variable is **mismeasured from their own pages**: the legal window is business days (p. 518) and Delta is counted in calendar days (Table 3 note, p. 526), so the 48% of the sample piled at Delta = 10 is not "filers waiting as long as legally possible" — their own showcase example (Cohen/BBBY) has Delta = 11 calendar days but only 7 business days. Table 1 and Table 3 also fail to reconcile by ~1.3 pp, which is composition, not elapsed time.
10. **Bishop et al.** HSR is a **private** notice plus a 30-day purchase freeze; 13D is a **public** flag. Their clock *stops* accumulation, the 13D window *permits* it. The running variable is not centred at the discontinuity (the cutoff sits at ln 20 ≈ 3.0 in 2000 drifting to ≈ 3.9 by 2025), and there is no RD apparatus and no figure in the paper. Their one sentence on our comparative static (Q11, p. 36) is labelled ASSERTED.
11. **The author's proposal.** Its dose `RTD_i ∝ S_out/ADV` is nearly collinear with its own liquidity-decile × quarter and size-decile × quarter fixed effects; `φ` is never calibrated; and its novelty claim ("no study of realised post-February-2024 Schedule 13D outcomes", 2 Aug 2026) is **refuted** by Trivedi, posted 3 June 2026. Its own power arithmetic implies an average accumulation effect "on the order of one tenth of a percentage point of shares outstanding" (`empirics.tex:114-117`). **(added by verifier — `INDEX.md` §4 item 9, missing from this file and decision-critical for the anchor's motivation): the "$810 million a year in foregone shareholder value" figure the proposal repeats three times is not in SEC Release 33-11253.** The release was checked page by page: `810` returns two hits, both footnote numbers; the Commission's own annualised foregone-value figure is **$49 million/year** (p. 211), and it disclaims even that ("do not represent estimates of the benefit of the final rule amendments", p. 211). **Strike the $810m.**

### 2024–26 sweep additions (neighbours, not competitors)

Two papers the 2026-08-19 sweep turned up and carded. Neither is a competitor on the full position: each occupies at
most one of the three legs — GMM is a competitor **on the object cell only** (its own card's header word) *(fixed by rows-verifier)*. Same seven columns as above.

| Paper (card file) | Venue / stage | Object studied | Margin of the disclosure rule | Identification | Liquidity's role | What the paper explicitly does NOT do — verbatim, page-cited | Source (card §, page) |
|---|---|---|---|---|---|---|---|
| `zeng_2026_ras.md` | *Review of Accounting Studies* 31, 1301–1341 (2026), **published**, open access (accepted 31 Mar 2026) | Daily **insider (officer/director) trading**, in basis points of shares outstanding, in the trigger-date → filing-date window. **No control outcome is ever an outcome variable** | **Neither margin, as LEVEL / background plumbing.** 5% and the 10-day rule define the event dates and the sample screen; neither is varied, interacted or shifted. **Pre-2024 regime only** — sample ends 2022 and Release 33-11253 is never mentioned; every "2024" hit is a citation or accessed-on date | Within-firm event-window vs matched control-window OLS (same firm, ±3–7 months), 2002–2022; one within-window ordering test (Table 3); one enforcement placebo DiD (SDNY × Bharara, Table 8). **No policy DiD, no structural model, no instrument** | **Nuisance control.** `illiquidity` 11 hits (**two** variable-definition lines p. 1337, a summary-stats row, a method sentence, seven control-variable rows) *(composition fixed by rows-verifier — the old list summed to 10; card §6)*; `Amihud` 1; `bid-ask` / `spread` / `market depth` / `turnover` **0 each**. The two standalone body uses of "liquidity" are insiders' *personal* "liquidity needs or diversification" (p. 1318) | "Sixth, while this study does not aim to disentangle insiders' motives, I acknowledge that concerns, such as control rights or job security, may arise in confrontational activist campaigns." (p. 1322) | §4, §6 grep table, §7; §8 Q1–Q7, Q12 |
| `gryglewicz_mayer_morellec_2025.md` | Working paper, **2 Dec 2025**; presented SFS Cavalcade NA 2025 and FTG Summer 2025 (acknowledgements). The PDF names **no journal and no R&R**; **"CEPR DP21226", the AFA 2026 slot and the earlier titles are external metadata from the sweep, not in the file** *(fixed by rows-verifier — card §9 check 4)* | The blockholder's **stake path θ_t** and firm policies (effort, pay, investment, leverage, default, stock price), plus one binary event — the blockholder buying the residual 1 − θ and going private | **None — background, and only just.** The rule appears once, in fn. 13, p. 20, as prose justifying the free scalar φ. Grep over 73 pp: `13D` **0**, `13G` **0**, `Schedule` **0**, `Williams` **0**, `window` **0**, `days` **0**, `filing` **0**; `5%` **1**, never a parameter and never varied. Not a LEVEL, not a CHANGE, not a partition | Theory only. Continuous-time, closed-form; **no data, no estimation, no calibration** anywhere | **Absent as market liquidity, and a naming hazard.** `Kyle` **0**, `market maker` **0**, `noise` **0**, `order flow` **0**, `Amihud` **0**, `depth` **0**, `volume` **0**, `turnover` **0**, `bid-ask` **0**. "Liquidity shock" means a jump in the **blockholder's own holding cost π** (the phrase appears on pp. 5 and 33 only; §6 spans pp. 32–33) *(pages fixed by rows-verifier — card §4/§9 check 3)*; "price impact" is the slope of the pricing function p(θ), not a microstructure object | "In the benchmark model, we abstract from elements that would introduce exogenous trading dynamics and are not key to our main findings." (p. 32), and of §6, the section that carries the word liquidity: "We sketch the equilibrium in this setting." (p. 32) | §4 greps, §6, §7; §8 Q1–Q9 · **card verified 2026-08-19: 40 OK / 0 WRONG / 4 MISCITED / 1 UNCHECKED; every §3 label stands** *(fixed by rows-verifier — the "verifier still running" note was stale)* |

**Reading notes on the two additions.**

- **Zeng.** She is an antecedent and a measurement template, not a rival: the window is scenery that dates the event. What she hands us is evidence that the window is *already leaky* — the price run-up "begins precisely on the trigger date" (p. 1310, Q5), the median filer uses nine of ten calendar days (p. 1309, Q2), and the target's own insiders buy through the gap via stock-surveillance vendors and IR contact. Two constraints follow. (i) **Our pooled state must be worded "pooled for the price-setting market"** — Zeng documents a named group that is partially flagged before the filing, and a referee who knows the paper will ask. (ii) Her only liquidity-adjacent cut is a median-market-cap split on an Internet-Appendix robustness table (IA Table IA.2, p. 1322), *insignificant and slightly larger in big firms* — so the honest claim is "the only look was a size split whose sign runs the other way", not "nobody looked". Her Internet Appendix is **not bundled** with the article; every IA number in the card is quoted from the body text.
- **Gryglewicz–Mayer–Morellec.** A competitor on the **object cell only**: the endogenous stake path ending in a lumpy full acquisition is theirs, in continuous time with closed forms (Prop. 7, p. 28), as is the bimodal-ownership reinforcement result. But there is no bidder (the only acquirer is the blockholder already in the stock), no premium, no partition — "Trading decisions are observable to investors" (p. 6, Q5) — and no private information at all. Their φ is **the reduced form of our threshold margin, written down and never differentiated**: Prop. 5 sets the entry stake equal to the fraction buyable before the price adjusts, and fn. 13 says that fraction exists because of the 5% report. Two hazards: their "liquidity shock" is a holding-cost jump, and **their κ is the effort-cost parameter** — a direct symbol collision with ours.

### Sweep summary

**(a) Modalities and query counts.** Two independent sweeps, 2026-08-19, both excluding the 11 competitor-set papers and every other card already on disk.
- `research/sweep_2024_26_A.md` — **20 distinct queries**: 12 Google Scholar (`as_ylo=2024&as_yhi=2026`), 4 SSRN native search, 4 NBER site search. SSRN's date-range and journal-browse widgets were not reachable without a subscribed session, so recency was pursued by query wording; the NBER programme recent-papers path 404s.
- `research/sweep_2024_26_B.md` — **47 logged source visits / queries** across journal forthcoming and advance-article lists (JF Early View 16 titles, RFS advance 89, RoF 28, RAPS 9, JFE via four ScienceDirect searches, JCF, Econometrica forthcoming 35, Management Science Articles in Advance, JFQA FirstView 20), working-paper series (ECGI 8 title searches, CEPR 7 phrase searches (rows 25–31; the sweep's own §4 summary line says six) *(fixed by rows-verifier)*, arXiv 5 API queries, SFI/RePEc, NY Fed Staff Reports, Fed Board FEDS), and **seven conference sources** (AFA 2025 and 2026, WFA 2025, SFS Cavalcade NA 2025 and 2026, SFS Cavalcade Asia-Pacific 2025, EFA 2025) — five screened by full-text keyword grep of the programme PDF/page, the two SFS Cavalcade ConfTool sources (NA 2026, Asia-Pacific 2025) by title/author queries *(count fixed by rows-verifier: the list has seven, not six; sweep B rows 41–47)*.

**(b) "None found" — the headline result of the sweep.** **No 2024–26 paper combines liquidity × the 13D disclosure rule × a control outcome.** Sweep B records "DIRECT — none found" in terms: "No 2024–2026 paper combines the 13D threshold/window (or a close analog) with market liquidity and a control outcome in the way the competitor set does. The closest candidates below occupy at most two of the three legs, or occupy an analog rule rather than the 13D margin itself." Query families that returned **zero results outright**: Scholar `"stealth accumulation" activism` (2024–2026); Scholar `"Release 33-11253"` (2024–2026); SSRN `13D 13G activist campaign success liquidity`; ScienceDirect JFE `activism toehold liquidity` and JFE `"takeover premium" liquidity` (2024–2026); CEPR `disclosure threshold takeover premium`, `blockholder disclosure toehold`, `"13D vs 13G"`; arXiv `abs:"Schedule 13D" AND abs:activism`, `abs:blockholder AND abs:disclosure`, `abs:"13D" AND abs:activism`; SFS Cavalcade NA 2026 ConfTool (six title/author queries, "No contributions" on every one). Source-level "none found" was returned by JF Early View, RFS/RoF/RAPS advance articles, JFE, Econometrica forthcoming, Management Science Articles in Advance, JFQA FirstView, the SFI series, Fed Board FEDS, and every conference programme screened. **Two soft walls to record rather than triage away:** NY Fed Staff Reports' search UI would not server-render GET results (the static listing showed zero keyword hits), and SSRN's date-range and journal-browse controls were unusable without a login — so neither absence is airtight.

**(c) The one DIRECT hit not obtained — for the author to fetch manually.**

> **Payne-Mann, Carmen; Stice-Lawrence, Lorien; Wong, Yu Ting Forester — "Potential Activism & the Threat of Public Campaigns."** SSRN working paper (USC Marshall School of Business Research Paper, sponsored by iORB), 27 Dec 2024. <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5076900>
>
> **WALL.** `Delivery.cfm/5076900.pdf` throws a browser certificate/privacy error (`chrome-error://chromewebdata/`), reproduced on a fresh link and a second URL variant; it is **not** a Cloudflare interstitial, so there is nothing to wait out, and `curl` returns an HTML challenge page. Only the abstract was captured.
>
> **Why it matters and why it must be read before ticket 03 closes.** Per the abstract captured in sweep A, it uses the **13D/13G split** to build a "Potentially Activist" middle category (private engagement short of a public 13D campaign) and reports **M&A activity, executive turnover and returns** for those stakes that fall between the activist and non-activist levels *(wording fixed by rows-verifier to match sweep A's abstract capture)*. That is a **control-outcome result keyed to the disclosure-type margin** — i.e. it is the only sweep hit that could bear on **W7** (the 13D/13G purpose partition on a control outcome, currently rated NARROW). Until the PDF is in hand, W7's rating is provisional in a way the other ratings are not. **Action: the author should download the PDF manually from a logged-in SSRN session and hand it to a reader.**

**(d) ADJACENT hits — titles only, not read, not carded.** One line each; venue and URL as recorded in the sweep files. None was opened beyond the abstract/gist unless noted.

- **Bogousslavsky, Fos & Muravyev, "Informed trading intensity"** — *Journal of Finance* 79 (2024), published. <https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.13320> — ML measure of informed trading, trained and validated on Schedule 13D trades purely as a labelled data source. Liquidity heavy; 13D as data only; no control outcome. *Not read — not carded.*
- **Choi, Joenväärä, Rösch & Tiu, "Market Quality of Informed Trades"** — SSRN WP, 23 Jun 2025. <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5317851> — ~500,000 13D transactions matched to TAQ; activists show higher execution quality but higher price impact. Observes behaviour inside the window; no rule change, no control outcome. *Not read — not carded.*
- **Duong, Pi & Sapp, "Betting on my enemy: Insider trading ahead of hedge fund 13D filings"** — *Journal of Corporate Finance* 93 (2025), published. <https://www.sciencedirect.com/science/article/abs/pii/S0929119925000628> — corporate insiders buy ahead of a 13D becoming public, ~12% average profits (14.5% absent prior contact with the activist). Same window as Zeng, smaller hedge-fund-activist sample, personal-gain framing; no control outcome. Zeng's card names it as a concurrent paper she distinguishes herself from (p. 1306). *Not read — not carded.*
- **Freund, Phan, Sun & Vo, "The role of stock liquidity in blockholder governance: Evidence from corporate social responsibility"** — *Financial Review* (2025), published. <https://onlinelibrary.wiley.com/doi/abs/10.1111/fire.12410> — identification is decimalization, not the 13D rule; 13D/13G only splits active from passive; outcome is CSR/firm value. *Not read — not carded.*
- **Meles, Pellegrino, Salerno et al., "The hidden costs of hedge fund activism: insights into market liquidity dynamics"** — *European Journal of Finance* (2026), published. <https://www.tandfonline.com/doi/abs/10.1080/1351847X.2026.2655250> — reverse direction: activism (dated by the 13D) *causes* liquidity deterioration. Liquidity as outcome; 13D as event-dating device. *Not read — not carded.*
- **Lee, Kim & Kim, "Does Mandatory Bid Rule Discourage Acquisitions above the Threshold?"** — ECGI Finance Working Paper (2024). <https://www.ecgi.global/publications/working-papers/does-mandatory-bid-rule-discourage-acquisitions-above-the-threshold> — staggered global adoption of an ownership-stake threshold that triggers an obligatory tender offer; finds no discouragement of above-threshold acquisitions. A **threshold-rule analog on a control outcome, cross-country, no liquidity** — the nearest thing in the sweep to W8a, and worth a card if a threshold-margin position is chosen. *Not read — not carded.*
- **Eckbo, Malenko & Thorburn, "Corporate Takeovers: Theory and Evidence"** — ECGI Finance WP N° 1030/2025, survey essay. <https://www.ecgi.global/publications/working-papers/corporate-takeovers-theory-and-evidence> — end-to-end survey of takeover theory and evidence with target boards as pivotal sellers. No 13D, no liquidity. *Not read — not carded.*
- **Israelsen, Schwartz-Ziv & Weston, "Block Diversity and Governance"** — *Review of Corporate Finance Studies*, advance article (2025). <https://academic.oup.com/rcfs/advance-article/doi/10.1093/rcfs/cfaf011/8193724> — textual analysis of 13D/13G-family filings; nonfinancial blocks ~6× more likely to self-identify as activist and priced as creating more value. 13D/13G as data source, not as the rule; no liquidity. *Not read — not carded.*
- **Chabakauri et al. (2022)** — named in Zeng's card (p. 1306, p. 1307) as a concurrent paper: **insiders detect activist trades ahead of the public by filtering aggregate order flow, and retain ownership to defend control rights.** *Outside the 2024–26 sweep window, not read; candidate for a later reader* — it is the only paper anyone has named that puts **order-flow inference + a control-rights outcome** in the same model, so it is a live refuter candidate for **W3** and **W8** and should be carded before draft_v3 states either.

---

## PART 2 — The occupied cells (hazards)

Cells a proposal must **not** claim as new. Owner and page in each line. Ten of the eighteen items restate an `INDEX.md` §4 hazard (items 20, 22, 24–29
and the two §4 corrections 4 and 8); the rest are added from the cards. *(fixed by verifier: the file previously
said "Items 1–10 are `INDEX.md` §4 items 20–29", which does not hold — §4 items 22, 23, 25, 27 and 28 land at
Part 2 items 12, 14, 17 and, until this pass, nowhere at all.)*

1. **The hump in liquidity.** Maug **Proposition 7 (p. 83)** already proves initial shareholders' wealth is non-monotone in liquidity with an interior φ\*; Edmans (2009) **Proposition 3 (p. 2496)** proves market efficiency and investment are inverse-U in ν with peak ν\* = α/(1−α), *holding α fixed*; LMM (2024) **Proposition 7 (printed p. 31)** prove a non-monotone-in-depth welfare result in full. Draft_v2's R1 is grid-certified only. Either name a different object **and** a different mechanism, or drop it. *(Edmans's own n. 7, p. 2485, is the cleanest citation that his hump needs an exogenous stake — Prop. 4, p. 2498, kills it once α adjusts.)*
2. **Window → noise-volatility isomorphism.** Back et al., **p. 1453**: "what matters is σ²T … reducing the trading horizon T is isomorphic to reducing noise trading volatility and keeping T fixed." Any claim that a shorter window is "less informed trading" is a re-parameterisation of their model, not a mechanism.
3. **The market learning that an informed activist is present from order flow.** CCKV own it: pricing is P_t = E[Wᴸ+Wᶠ | F_t] with endogenous W, and **Theorem 1 (p. 17)** breaks the Kyle unpredictability property. Order-flow inference about an intervention cannot be claimed as novel.
4. **A random deadline in a Kyle model.** Caldentey & Stacchetti (2010), *Econometrica* 78(1), 245–283, plus Baruch (2002) and Back–Baruch (2004), cited at **CDF (2016) p. 1450**; in those models λ is a *super*martingale. What is unoccupied is a deadline that is a **legal filing window with a partition attached**, not merely a random horizon.
5. **Activism → takeover premium as a structural number.** Celentano–Levine, **Table 4 Panel A, p. 43** (marginal −13.69%) and **Table 5, p. 44** (GE −0.60%). Any premium claim of ours has to be stated against these, and never by citing the −13.69% as an equilibrium effect.
6. **Threshold × takeover, cross-country — already tested, and null.** Becht et al.'s Internet Appendix **"Table 18" (IA pp. 11–12)**: Disclosure Threshold on **takeover outcomes = 0.015 [0.025]**, insignificant, as it is for all outcomes (0.048 [0.110]), board (0.003 [0.057]) and restructurings (−0.046 [0.048]); only payout is significant (0.077\* [0.040]). Read with their Table 9, where the threshold *does* predict whether an activist shows up. Lead with this null; do not walk around it.
7. **The Feb-2024 window DiD, first stage on filing timing.** Trivedi, **Table 2, p. 11**: compliance share +0.348 (SE 0.130, p = 0.007); mean lag null (+1.89, t = 0.48). Raw means 0.39 → 0.80 treated against 0.27 → 0.34 control (p. 10).
8. **Pre-rule window-use descriptives.** Polk et al., **Table 3, p. 526** (1.34% at Delta = 0 rising to 5.09% at Delta = 10, 9,685 filings 2001–2022) and BBJJ, **Table 2 / p. 10–11** (45.3% of activist filings in the 8–10 day bucket, ~20% on day 10, median stake 6.3%).
9. **Liquidity → takeover premium in OLS.** Dass et al. (2020), **p. 25 / Table 8 Panel A, printed p. 58**: −4.46 to −4.67 pp per SD of *acquirer-minus-target* Relative Liquidity, stock deals only, against a 26.8% mean premium — **OLS only, the DiD does not reach this regression**. Massa & Xu (2013), **p. 1483**: a 1-SD rise in **target** liquidity gives a 10% higher offer premium (public acquirers), 4,691 US deals 1987–2007, cross-sectional. Note the two disagree on which side's liquidity matters.
10. **Ben-David et al.'s stick.** Announcement CARs are a contested proxy for deal NPV; this is the reason the object should be the **premium** (a transfer) rather than the CAR. (`ben_david_et_al_2026_jf.md`; eight of fourteen quotes were copy-edited between the WP and JF 81(3) — re-transcribe before quoting.)
11. **The threshold as a cap on the secret stake.** Ordóñez-Calafi & Bernhardt, **p. 2836**: crossing reveals the position, so in equilibrium the activist's position is min{ᾱ, α\*} and the policy "becomes an upper bound on its position and hence trading profits". Their full welfare ranking of investors / activist / regulator over the threshold (Prop. 4, p. 2847) is theirs.
12. **"The activist's presence raises the probability of a takeover."** Corum–Levit, **Corollary 1 and Proposition 5**, PROVED. Also theirs: the sell-side/buy-side credibility asymmetry, the selection-vs-treatment framing, and "a stake cap limits activist credibility".
13. **Activism vs takeover as modes of getting control.** Burkart & Lee, **Prop. 3, p. 1881** (PROVED), and Burkart–Lee–Voss, **Prop. 1** (the tender-offer / brokered-sale cutoff). Also BLV's Prop. 3 on activism displacing hostile bids.
14. **A premium above the free-rider price.** Burkart–Lee's **Lemma 2, p. 1877** makes the bid price equal the full post-takeover value; their **Internet Appendix Prop. 1 (IA pp. 12–13)** already produces a strictly higher "commitment" premium — via legal risk ε, not via liquidity or disclosure. So "a wedge is obtainable" is not new; *where ours comes from* has to be.
15. **Reputation for proxy fighting.** Johnson–Swem own it, structurally estimated; do not model repeated campaigns or type learning.
16. **The 13D announcement-return decomposition.** AFS, **75.2% treatment / 12.2% stock picking / 12.6% selection** of 6.34% (p. 3), plus the standing private cost of activism, C = 4.6 pp ≈ $2.43m (p. 28). Any use of announcement returns as our outcome invites this decomposition as a referee demand.
17. **Liquidity → 13D-vs-13G channel choice.** Edmans–Fang–Zur: a 1-SD rise in LIQAM cuts P(13D | block) by 6.88 pp against a 43.2% base (printed p. 24), and raises P(block) by 0.47 pp (printed p. 21). Note there is **no first stage in print either** — fn. 27, p. 1473 of the RFS version says they could not find a valid instrument. Never describe it as instrumented.
18. **Liquidity → incidence of costly voice, and trade-level facts inside the window.** Norli et al. (baseline probit 0.33% → 0.73% from the 10th to the 90th liquidity percentile, Table 3 col. 2) and Fos (2017) own "liquidity predicts activism" within the US. Collin-Dufresne & Fos (2015) own what activists actually do inside the window: ~3% run-up (JF, 1994–2010), measured λ almost 30% *lower* on trade days (p. 1557), and the shift from patient to aggressive execution once the clock runs — "before their ownership crosses the 5% threshold, Schedule 13D filers are more likely to use limit orders than after, when they have only 10 days left to trade" (p. 1558); the 46.25% / 34.25% Bayes figures behind it rest on an assumed 70%-accurate Lee-Ready classifier (n. 22).

---

## PART 3 — Whitespace

Three axes:

- **OBJECT** — bidder entry · takeover premium / premium wedge · campaign success · stake at filing / toehold · filing delay · 13D-vs-13G choice · price informativeness · blockholder's own return · industry structure.
- **MARGIN** — threshold level · threshold change · window length · window change (Feb-2024) · 13D/13G purpose partition · **the partition itself** (flagged vs pooled state) · none.
- **IDENTIFICATION** — theory (which tool: monotone comparative statics · information design · tender-offer game · Kyle-type trading) · structural · DiD on the Feb-2024 change with a control group · cross-sectional · calibration.

Each item below gives (a) the cell, (b) the closest cards (refuter candidates), (c) why each does not occupy it,
with a page-cited quote or a card-recorded grep, and (d) a rating: **CLEAR** (no card within one move) /
**NARROW** (a card is one assumption away — named) / **CONTESTED** (someone could argue it is occupied — named).

---

### W1 — Window **length** as a determinant of the **takeover premium**, in theory. **CLEAR**

**(a)** A model in which the length of the pre-flag filing window enters the equilibrium takeover premium (or the premium wedge m₁ − m₀), so that ∂premium/∂window is a signed object.

**(b)–(c) Refuter candidates.**
- **Back et al. (2018)** — has the window, has no premium. Verifier grep: `takeover / bidder / tender offer / acquirer / premium` return 5 hits total, all in prose about Kyle–Vila, a campaign-goal list, and three reference titles. "The firm is never sold; there is no acquirer and no premium in the model" (§6). And the window is not a window: "reducing the trading horizon T is isomorphic to reducing noise trading volatility" (p. 1453).
- **Corum–Levit (2019)** — has the premium, has no window. Full-text grep in §4: `13G` = 0 hits; "days" appears only in the phrase "in the old days" (p. 2); "window" only as *event window*. "After trading, the activist's ownership in the target becomes public." (p. 10) — disclosure is instantaneous.
- **Burkart & Lee (2022)** — has the premium (degenerate, Lemma 2) and **explicitly hands the interaction over**: "we do not endogenize the acquisition of the toehold in anonymous, predisclosure markets… We leave an analysis of how predisclosure and post-disclosure decisions interact to future work." (p. 1891).
- **Corum (2025)** — has η/λ but no counterparty: "there is no other player that affects the firm value other than the blockholder." (p. 9); `bidder / premium / tender / merger` = 0 hits in 77 pp.
- **Faure-Grimaud & Gromb (2004)** *(added by verifier — `INDEX.md` §4 item 18, missing from this file)* — the liquidity-and-blockholder theory closest to a price object, and it declines the whole lane twice: "Our model does not deal with control transfers per se" (p. 999), and p. 988 names the stealth-accumulation literature (Kyle–Vila, Kahn–Winton, Maug, Noe) as the branch they are opting out of. No takeover, no premium, no rule.

**(d) CLEAR.** No card holds both a window and a premium. The closest thing to a claim on this cell is Burkart & Lee's own sentence declaring it open.

**Sweep check (2024–26).** Neither addition touches this cell. Zeng has no premium object at all (`premium` **0** hits over pp. 1301–1341, card §6 grep table) and no theory. GMM have no premium and no window: `premium` **0**, `tender` **0**, `bidder` **0**, and `window` **0**, `days` **0**, `13D` **0** over 73 pp (card §4). **CLEAR stands.**

---

### W2 — **Control outcome** (bidder entry / takeover premium / campaign success) × **window CHANGE** (Feb-2024) × **DiD with a control group**. **CLEAR** on the cell; hard on execution

**(a)** A design-based estimate of what the 2024-02-05 acceleration did to a control outcome, using a comparison group that is not the treated 13D filer population.

**(b)–(c) Refuter candidates.**
- **Trivedi (2026)** — same margin, same shock, **has a control group**, wrong object. Full-text search across 25 pages: **`takeover` = 0, `premium` = 0, `toehold` = 0, `stake` = 0, `activis*` = 0, `block*` = 0** (§6). His outcomes are the filing lag, the compliance share, Δspread, ΔAmihud and a forward return.
- **Polk et al. (2024)** — same margin, no post-rule data and no control group. Their own word for what they do is a projection, not an estimate: "the authors establish an updated 'baseline projection' for expectations regarding how the Modernization final rule will impact activist investors and stock returns under a five-day reporting regime" (p. 516, card Q3). The comparison is *within* the pre-rule cross-section — filings with Delta ≤ 5 against filings with Delta 6–10 (card §9, R13 note) — never treated against untreated. Verifier grep on the full text: `takeover / premium / bidder / liquid* / Amihud / spread / turnover` = **0**. *(fixed by verifier: the sentence previously quoted "our analyses compare investors who filed voluntarily within five days with those who waited the full ten" as if verbatim; that string is in neither the article nor the card. The substance stands; the quotation did not.)*
- **The author's proposal** — same margin and shock, **no control group by design**: "The reform has a single adoption date and no untreated group… Identification therefore uses cross-sectional variation in how tightly the common deadline constrains each target, rather than a treated-versus-control comparison." (`empirics.tex:7-11`). Its bid-hazard leg is "Confidence intervals only" (`empirics.tex:143-146`).
- **Bishop et al. (2026)** — asserts our comparative static and never estimates it: "A shorter disclosure window compresses the time during which activists can accumulate shares quietly, limiting feasible toeholds above 5%." (printed p. 36), and they never state the 2024-02-05 effective date at all.

**(d) CLEAR.** But two execution warnings from the cards, and neither is a reason to downgrade the cell — only to design around it. (i) **13G is structurally unusable as a control for a control outcome**: 13G filers disclaim control intent by definition, and selection into 13D-vs-13G is itself plausibly responsive to the window change (`trivedi_2026_ssrn.md` §7). (ii) Power: the author's own SEC-table arithmetic implies ~3% of non-corporate-action campaigns (≈7/year) were materially constrained (`empirics.tex:108-112`), and Dass et al.'s premium DiD died on 19 usable treated acquirers. (iii) **(added by verifier — `INDEX.md` §4 item 15)** BBJJ argue a *second* channel that runs through the same treatment: "tightening the disclosure requirements under Section 13(d) will not only alert the market to the investor's presence but also incumbent directors and executives—who can then put takeover defenses in place more quickly" (p. 28, card Q20). On a control outcome that is a confound with the *opposite* sign to the accumulation channel, and their proposed moderator — whether the charter precludes a low-trigger pill (pp. 28, 31) — is a heterogeneity split we can actually build.

**Sweep check (2024–26).** No refuter; **one execution warning added.** Zeng's sample screen keeps only 13Ds filed **1–13 calendar days** after the trigger date — "Therefore, I focus my analyses on the 13Ds within 13 days of the trigger date whose filing date insiders can reasonably anticipate." (p. 1312, fn. 13, Q4). Under the five-business-day rule that screen stops being neutral: the filing-date cluster moves left, so any calendar-day filter of that shape changes sample composition on the two sides of 2024-02-05. **Put this on the referee checklist's EDGAR-cut-off line alongside T+1.** Her sample ends 2022 and Release 33-11253 is never mentioned (card §6). GMM have no window and no data. **CLEAR stands.**

---

### W3 — The **partition itself**, rule-keyed: an on-path flagged/pooled split triggered by a stake threshold **and a date**. **CLEAR** (with a named boundary)

**(a)** An equilibrium in which both states occur on path, the market's inference differs across them, and which state the world is in is determined by the *rule's* parameters (stake trigger + filing deadline), not by the trader's own indifference or by an action she chooses.

**(b)–(c) Refuter candidates.**
- **CCKV (2026)** — a single, permanently pooled state. "All these expressions hold on and off the equilibrium path, as an activist's trades are hidden from others." (fn. 16, p. 15); "No agent in the model ever learns that a blockholder holds a block" (§6a); and they interpret the whole model as living inside the pooled state (Q4, p. 11).
- **Corum–Levit (2019)** — the flagged state is **off path**. α\* = ᾱ exactly, and α > ᾱ rests on an assumed off-path belief µ(α) = 1 (p. 14). Disclosure never informs anyone in equilibrium; it only truncates the stake.
- **Ordóñez-Calafi & Bernhardt (2022)** — crossing reveals instantly, so the activist never crosses: "in equilibrium, the activist's position does not cross the disclosure threshold" (p. 2836). There is no "crossed but not yet flagged" cell; a window destroys the mechanism.
- **Corum (2025)** — introduces the purpose partition and **proves it irrelevant**: "as I show in the analysis, this particular disclosure threshold does not make any difference for the results" (p. 19).
- **Collin-Dufresne & Fos (2016)** — the opposite assumption, and they list it as future work: "Fourth, we assume that the presence of the insider is common knowledge." (p. 1464).
- **Collin-Dufresne & Fos (2015)** — they *name* the gap and decline it: "standard asymmetric information models also typically assume that the presence of the insider is common knowledge. In practice, market makers may have to learn that an insider is present from the order flow." (JF pp. 1557–1558).
- **Maug (1998)** *(added by verifier — `INDEX.md` §4 item 13, the single cleanest whitespace sentence in the antecedents and absent from this file)* — he touches stake disclosure exactly once and assumes it away **by timing**: pre-trade publicity would kill the liquidity and the quantities F can trade, while a post-trade regulatory filing "does not affect F's trading strategy" (p. 73, card Q5). A 13D rule is **neither** of his two cases — it is a trigger at a stake threshold plus a *finite* window, so part of the accumulation is pooled and part flagged. The partition is exactly the case his dichotomy skips.
- **Kyle & Vila (1991)** — **the one card within one move, and the reason this item carries a boundary.** Their mixing equilibria already contain an endogenous pooled/revealed split (pp. 62–63, 69–70). But disclosure is disclaimed on page one: "The model abstracts from disclosure requirements. We do not require the large trader to notify the market if he purchases or sells a significant amount of stock." (p. 54, n. 1), and they have exactly one round of trading (pp. 55–56), so there is no dimension in which to state a date-keyed partition.

**(d) CLEAR** for the *rule-keyed* partition (stake + date). **Do not state it as "the market never learns" or "no one has a pooled/revealed split"** — Kyle–Vila refute that wording in one citation. The defensible sentence is: theirs is endogenous, un-keyed and available only where the trader happens to be indifferent; ours is imposed by a legal trigger and a legal deadline, present in every parameter configuration.

**Sweep check (2024–26).** No refuter, but Zeng sharpens the wording. She documents that the pooled state is **leaky for one named group** — the target's own managers, via stock-surveillance vendors and IR contact, with the price run-up beginning "precisely on the trigger date" (p. 1310, Q5). So our pooled state must be written *pooled for the price-setting market*, with Zeng cited for why insiders are a documented exception (card §7 item 1). GMM have no partition at all: "Trading decisions are observable to investors, who rationally take this information into account when determining their demand for shares." (p. 6, Q5). **CLEAR stands.**

---

### W4 — **Threshold level** and **liquidity** as two separate parameters, moving a **control outcome**, PROVED. **NARROW**

**(a)** A model with κ (noise-trading intensity) and ᾱ (the disclosure trigger) as *separate* primitives, delivering a signed ∂(control outcome)/∂ᾱ holding κ fixed, and a signed cross-partial.

**(b)–(c) Refuter candidates.**
- **Corum–Levit (2019)** — they fuse them by construction: "Parameter ᾱ can also be interpreted as a disclosure threshold (e.g., regulation 13D). Moreover, buying up to ᾱ shares does not trigger a poison pill if such exists. Empirically, ᾱ ∈ [5%, 10%]." (p. 10), immediately after "the stock is perfectly liquid (illiquid) for small (large) orders" (p. 10). One scalar, three jobs — so they can never move one without moving the others, and they move none.
- **Ordóñez-Calafi & Bernhardt (2022)** — **the card one assumption away.** They *do* have both parameters separately (µ for liquidity, ᾱ for the threshold), and they *do* state the interaction: "We show that high liquidity can lead the costs of adverse selection in financial markets to outweigh the benefits of managerial disciplining, thereby reducing the optimal threshold, whereas the opposite is the case when liquidity is low." (p. 2854) — carried into the conclusion (p. 2856) and taken as far as a policy contingency ("industry-specific thresholds based on liquidity measures", p. 2854). **But it sits in the Discussion with no proposition behind it (ASSERTED), and the object is managerial discipline and real investment, not a control outcome:** `bidder`, `premium` and `tender` return **0 hits** in the full text, and all three body hits of "takeover" sit in one paragraph on p. 2854.

- **Corum (2025)** *(added by verifier)* — a second card that *fuses* the two rather than separating them, and so cannot occupy the cell either: η and λ are simultaneously the threshold objects and the liquidity parameters (fn. 22, p. 26; Online Appendix E, p. 74). Like Corum–Levit he cannot move one holding the other fixed.
- **Edmans (2014) survey** *(added by verifier — `INDEX.md` §4 item 14)* — the field's own statement that this cell is empty: theory models "do not predict a discontinuity at 5%", and "Particular attention could be paid to how the effectiveness of governance depends on block size" (p. 45). A survey does not occupy a cell, but it is the cleanest external warrant that the threshold *level* is unmodelled.

**(d) NARROW.** The one assumption between OCB and this cell is the object: swap the incumbent's binary business plan for a bidder with a premium. That is a real modelling step (it requires a counterparty and a free-rider condition they do not have), but a referee who knows OCB will say the comparative static was already stated. The honest position sentence is: *OCB assert the liquidity × threshold interaction on managerial discipline; we prove it on a control outcome* — and it is only worth saying if the honesty label really is PROVED.

**Sweep check (2024–26).** Neither touches it. In Zeng the 5% level is fixed scenery and Amihud is a nuisance control whose coefficient wanders in sign across tables (−0.025\*\* Table 2 col. 3, +0.154\*\*\* Table 8 col. 4) with no discussion (card §5, §6). In GMM `5%` returns **1** hit, fn. 13 p. 20, and is never a parameter. **NARROW stands.**

---

### W5 — The window as a **legal deadline attached to a partition**, inside a Kyle-type trading model. **CLEAR** (with a named boundary)

**(a)** A continuous- or multi-period trading model in which T is the *filing deadline*, triggered by the blockholder's own crossing of a stake threshold, known in length, and at which the market's information set jumps.

**(b)–(c) Refuter candidates.**
- **Back et al. (2018)** — T is fixed, exogenous, common knowledge, and the extension is declared out of scope twice: "Allowing T to be a choice variable would be an interesting extension, but it is beyond the scope of this paper." (p. 1435, fn. 10) and, first on the future-work list, "we assume that the horizon at which the activist's stake is disclosed is fixed and common knowledge… it might be interesting to endogenize the horizon." (p. 1454). Their only disclosure-rule channel is *precision*: "changes in disclosure rules that lead to changes in the precision of disclosed ownership information" (p. 1453) — σ_x, not a partition.
- **CDF (2016)** — "Second, we assume that the horizon is fixed." (p. 1464). Their §4.1 comes within touching distance of a priced flagged/pooled split of *order flow* (p. 1461) and disposes of it in one paragraph — and it is about noise traders, not about the informed trader's presence.
- **The random-horizon literature** — Caldentey & Stacchetti (2010), Baruch (2002), Back–Baruch (2004), cited at CDF (2016) p. 1450, own the *random* deadline (there λ is a supermartingale, the opposite drift to CDF 2016). CDF's own 2016a "Insider Trading With a Random Horizon" WP is cited at p. 1458 fn. 10 and is not in the repo.
- **CCKV (2026)** — the window is a modelling convenience, not an object: "material adjustments to positions or intentions can be disclosed with a delay—historically, up to 10 days—so trades effectively remain hidden for some time" (p. 10), and their named future work item (i) is precisely about "time-horizon effects: on the one hand, the usual insider 'splitting trades' logic would say that trades should be small away from the end-game; but at the same time, that is when beliefs are most responsive" (p. 35).

**(d) CLEAR** — but state it as *a legal filing window with a partition attached*, never as "nobody has made the horizon non-fixed", which is refutable in one citation (hazard 4 in Part 2). CCKV's named open direction (i) is the strongest external warrant that the time-horizon version of this problem is live and unclaimed.

**Sweep check (2024–26).** Neither touches it. GMM is the only continuous-time addition and it is not a Kyle model: `Kyle` **0**, `market maker` **0**, `noise` **0**, `order flow` **0** over 73 pp (card §4), the blockholder has no private information (card §5), and there is no horizon or deadline of any kind. **CLEAR stands.**

---

### W6 — Liquidity κ as the **driver**, with the disclosure rule moving the **slope** of a control outcome in κ (draft_v2's T2, "disclosure attenuation"). **CLEAR**

**(a)** An interaction, not a level: ∂²(control outcome)/∂κ ∂(rule), estimated or proved. The empirical version is a liquidity × window-change interaction; the theory version is disclosure attenuation.

**(b)–(c) Refuter candidates.**
- **Trivedi (2026)** — the only paper on our anchor with liquidity in it, and it runs the other way round: liquidity is a **DiD outcome** (Δ Corwin–Schultz +0.0013, t = 0.26; Δ Amihud +0.41, t = 0.50), never a conditioning variable. The card records: "Trivedi never estimates any interaction of any kind. … they measure a **level** effect of the rule **on** liquidity; we measure the **slope** of control outcomes **in** liquidity" (§7). Note his nulls have SE 0.0051 and 0.81 with **no MDE reported** — they are uninformative, not zero, and they *protect* the use of liquidity as a pre-treatment moderator.
- **Polk et al. (2024)** — zero liquidity measures of any kind (grep confirmed on both the reader's and the verifier's extraction).
- **The author's proposal** — liquidity deciles are absorbed by fixed effects; there is no dPremium/dκ-style object anywhere in it (card §7, whitespace item 3).
- **Massa–Xu, Dass et al., Edmans–Fang–Zur, Becht et al.** — all hold the legal environment fixed and estimate levels, never a rule × liquidity interaction. Becht is the only one with threshold variation and it is cross-sectional and neutralised (fn. 5).
- **Edmans & Holderness (2017) survey** *(added by verifier — `INDEX.md` §4 item 28, absent from this file)* — the field's map asks for exactly this cell: future theories should carry "more complex microstructure features… that have so far been analyzed in pure-trading models in which firm value is exogenous and thus trading has no effect on governance" (pp. 76–77), and its interactions bullet names "takeovers (Corum and Levit, 2016)" as an open interaction (p. 76). Its **one** empirical liquidity × pre-filing-accumulation result — Gantchev & Jotikasthira (2016), activists camouflage purchases by timing them to liquidity-driven institutional selling (p. 28) — is the nearest existing neighbour to our accumulation margin and is never linked to the 13D that follows or to any control outcome.

**(d) CLEAR** as a slope/interaction claim. The level relations it sits on top of are all occupied (Part 2, items 8–9, 17–18), so the sentence must be about the *slope*, e.g. *Massa and Xu (2013) estimate the liquidity–premium slope holding the legal environment fixed; we ask what the disclosure rule does to that slope.*

**Sweep check (2024–26).** No refuter, and Zeng makes the cell sharper rather than smaller. Her only liquidity-adjacent cut is a **median-market-cap split on an Internet-Appendix robustness table** (IA Table IA.2, described p. 1322): the effect is *slightly more pronounced in larger firms, difference not statistically significant* — a size split, not a liquidity test, and its sign runs against a naive thin-stock story. Nobody asks whether the pre-filing leakage is larger in thin stocks *conditional on size*, even though her own mechanism (blockholders trading 29.8% of daily volume on trading days, Table 1 Panel B, p. 1316) is mechanically a κ story; a κ-interaction on her design is available and unclaimed (card §7 item 2). GMM's "liquidity shock" is a jump in the blockholder's own holding cost π (p. 5, Q7) — a naming hazard, not an occupant. **CLEAR stands.**

---

### W7 — The **13D-vs-13G purpose partition** as an economically load-bearing object on a **control outcome**. **NARROW**

**(a)** A model or estimate in which whether the blockholder's *purpose* is flagged (13D) or not (13G) changes bidder entry, the premium, or campaign success.

**(b)–(c) Refuter candidates.**
- **Albuquerque–Fos–Schroth (2022)** — **the card one object away.** The 13D/13G choice *is* their model, structurally estimated on 69,937 filings, and they already see the pooling: "the stock price reaction to initial Schedule 13G filings may already incorporate the possibility of subsequent 13D filings. The implication is that the true treatment effect may be larger than we estimate." (fn. 16, p. 34), and "It remains unclear, however, whether a transaction costs differential would exist, unless the market not only forecasts the intention to cross the 5% threshold that triggers either Schedule 13D or 13G filing, but also the type of filing." (p. 15). What they do not have is any control outcome: `13.7` = 0 hits, `takeover` = 3 hits (footnotes and one reference).
- **Edmans–Fang–Zur (2013)** — 13D vs 13G is the dependent variable, but the only price object in the paper is a 0.7% average abnormal return on a 13G filing (printed p. 27). No control outcome anywhere.
- **Corum (2025)** — introduces α₀′/α₁′ for the purpose split and proves it irrelevant (p. 19, p. 20 fn. 17). Irrelevant *in his model*, because his market maker's only inference channel is the trade disclosure and a non-intervening blockholder carries no NPV — once the flag changes a control outcome the purpose partition is load-bearing again.
- **Bishop et al. (2026)** — the HSR "investment-only" exemption is a purpose test enforced ex post by reading communications (printed pp. 35–36), with $600k–$11m penalties. A different statute, and no control outcome is estimated.

**(d) NARROW.** AFS is one object away — they have the structural machinery for the purpose choice and concede the pooling; adding a control outcome is a step a good structural team could take. The defensible differentiation is that their partition is *the blockholder's declaration of purpose*, ours is *the market's information set*, and those are different objects (`albuquerque_fos_schroth_2022.md` §7).

**Sweep check (2024–26).** Neither addition touches it — but see the sweep summary item (c): **Payne-Mann, Stice-Lawrence & Wong (SSRN 5076900) is the one DIRECT hit not obtained, and it is a control-outcome result keyed to the 13D/13G split.** Until that PDF is read, this rating is provisional in a way the others are not. Zeng extends her analysis to 13Gs (p. 1327, Q9) but the object stays insider trading, and she reports the Item 4 purpose taxonomy only descriptively (36.6% investment-only / 43.3% communicated / 20.0% explicit activism, p. 1315). GMM: `13G` **0** hits. **NARROW stands.**

---

### W8a — **Bidder entry** × **threshold level**, in theory. **NARROW**

**(a)** ∂(bidder entry)/∂(disclosure threshold), signed, with liquidity held fixed.

**(b)–(c) Refuter candidates.**
- **Corum–Levit (2019)** — **one derivative away.** ᾱ *is* the 13D threshold, α\* = ᾱ, and Corollary 1 gives θ\* increasing in α. They simply never state a comparative static in ᾱ, because it is also the liquidity break and the pill trigger. And the threshold is **inert in half their parameter space**: in the selection region b ≤ Δ, h\*(α) = θ_b π_b is independent of α (p. 14). Their only policy sentence is margin-free: "Policies and regulations that undermine shareholder activism, but do not directly affect bidders, will still have a negative effect on takeovers." (p. 11, Prediction 5).
- **Becht et al. (2017)** — the empirical version, and it is a **null**: threshold on takeover outcomes 0.015 [0.025] (IA "Table 18"); and they *drop* the 273 sub-5% engagements to neutralise the variation (fn. 5).
- **Kyle & Vila (1991)** — a single raider behind an assumed entry barrier (p. 55), so no entry margin exists.

**(d) NARROW.** The move Corum–Levit declined to make is one derivative, and a referee who knows the paper will say so. The separation that survives is exactly what they cannot do: ∂/∂ᾱ **holding liquidity fixed**, which their fused scalar forbids (see W4).

**Sweep check (2024–26).** No refuter, one near-miss to note. GMM's φ **is** the reduced form of the threshold margin: Prop. 5 sets the entry stake exactly equal to the fraction buyable before the price adjusts, and fn. 13 (Q1) says that fraction exists because of the 5% report — and they never differentiate with respect to it (card §7). Outside the carded set, the sweep's nearest neighbour is **Lee, Kim & Kim (ECGI 2024)** on the Mandatory Bid Rule, a threshold-rule analog on a control outcome with no liquidity; not read, not carded. **NARROW stands.**

### W8b — **Bidder entry** × **window** (length or the Feb-2024 change), in theory. **CLEAR**

**(b)–(c)** Corum–Levit have **no time dimension at all** (§4: no filing window, no deadline, no "business days", no 13D/A, no 13G in 17 pages). Burkart–Lee–Voss *do* have bidder entry as an equilibrium object (n_B\*) but **no disclosure rule anywhere in 70 pages**: `disclos` = 0, `13D` = 0, `Schedule` = 0, `window` = 0, `filing` = 0 — and they sign off on liquidity too: "Market liquidity plays no role in our analysis" (printed p. 9). Celentano–Levine have no entry margin at all: one acquirer arrives per period with exogenous quality (§6). Edmans–Goldstein–Jiang have the object empirically and ask for the theory: "Our findings thus suggest the need for new takeover theories to explain why market prices should impact acquisition likelihood." (p. 966), and "to date the possibility of asymmetric learning has not yet been incorporated into the theoretical takeover literature" (p. 936).

**(d) CLEAR.** Adding a disclosure rule to BLV is more than one assumption (they have neither a rule nor a market), and Corum–Levit cannot state a window comparative static in a model with no time. **Standing risk on this cell, and it is not closable from the repo *(added by verifier)*:** every BLV cite above is to **ECGI WP 956/2024 (Feb 2024)**, the only version in hand. ECGI records the paper as **last revised 29 Dec 2025** and that revision was not obtained (`INDEX.md` §2). A revision is exactly where the disclosure/liquidity extension we are relying on them *not* to have would appear, so the `disclos` = 0 / `13D` = 0 / "Market liquidity plays no role" evidence is **as of Feb 2024 only**. Fetch the Dec-2025 PDF before this cell is claimed in draft_v3.

**Sweep check (2024–26). GMM's card addresses this cell by name and it survives.** "There is no bidder: the only acquirer is the blockholder already in the stock, and entry in this paper means the blockholder's own *initial* purchase θ₀ = φ, not a rival's arrival. There is no window: `window`, `days`, `13D` return 0 hits" (card §7 item 1). Their "takeover" is the incumbent reaching θ = 1 — "the blockholder conducts an immediate lumpy trade toward one (acquires the entire firm) and thereafter stops trading" (p. 28, Prop. 7(2)). **CLEAR stands** — with one new constraint on the *object* side: the **endogenous stake path ending in a lumpy full acquisition is now theirs, in continuous time with closed forms**, so our contribution must sit in the partition and the control outcome, never in the stake path (card §7).

---

### W9 — **Filing delay as a choice** — endogenous timing of the flag. **NARROW** *(rating changed by verifier from CLEAR: the *empirical* version of "the delay is chosen and it is priced" is already occupied — see Polk et al. and BBJJ below)*

**(a)** The blockholder chooses *when* inside the legal window to file (or when to cross), and that choice is priced.

**(b)–(c) Refuter candidates.**
- **Back et al. (2018)** — "Allowing T to be a choice variable would be an interesting extension, but it is beyond the scope of this paper." (p. 1435, fn. 10).
- **Johnson–Swem (2021)** — buying and filing are one instantaneous act: "In each stage game, A moves first and decides whether to initiate a campaign by purchasing shares in the target firm and filing a 13-D (13-D) or to ignore the opportunity (Ignore)." (p. 32). The card's instruction: they never model it, and they do not leave it open — a search for "future research / future work / beyond the scope / we abstract / do not model" returns exactly one hit, about activist heterogeneity.
- **CCKV (2026)** — the crossing is outside the model altogether (§6b).
- **The author's proposal** — filing delay is present but declared non-behavioural: "Filing-delay compression and accumulation after the legal deadline are mechanical consequences of compliance and cannot establish a behavioural response." (`empirics.tex:166-168`).
- **Polk et al. (2024)** — **(added by verifier: the card the original list omitted, and the reason for the downgrade.)** Their question *is* this cell, empirically: "Does an activist investor earn more by waiting the full legal delay before filing Schedule 13D?" (card §1). Delta — the self-selected trigger-to-filing delay — is their running variable, and it is priced: cumulated quiet-period excess return rises from **1.34% at Delta = 0 to 5.09% at Delta = 10** (Table 3, p. 526; 9,685 filings, 2001–2022). They never model the choice, and there is no control group, no regression and no SE — but a referee will say the pricing of the realised delay is in print.
- **BBJJ (2013)** — **(added by verifier)** the delay *distribution* as behaviour: 45.3% of activist filings land in the 8–10 business-day bucket and ~20% on day 10 (Table 2, p. 10), with the day-0 turnover puzzle explicitly handed to future research (p. 28). Again descriptive, and again on the same object.
- **CDF (2015)** — the closest *evidence*, and it is measurement under a fixed rule rather than a model of the choice: "Schedule 13D filers have at most 10 days to file with the SEC after the event date… Because of this time constraint, they have less flexibility with respect to their trading strategy after the event date." (p. 1569), and the limit-order shift at p. 1558.

**(d) NARROW** *(was CLEAR — changed by verifier).* The **modelled, priced choice** of a filing date inside a legal window is unoccupied: no card writes the timing decision into an equilibrium. But the *cross-section* of realised delays and their returns is occupied by Polk et al. (Table 3, p. 526) and their distribution by BBJJ (Table 2, p. 10), so the claim must be stated as "nobody models the delay as a choice", never as "nobody has looked at filing delay", which is refutable in one citation. Note also the boundary from W5: a *random* horizon is occupied; a *chosen* filing date inside a legal window is not.

**Sweep check (2024–26).** No change; Zeng is the closest and she reinforces the verifier's NARROW rather than moving it. She *describes* the realised delay in detail — median trigger-to-filing gap nine calendar days (p. 1309, Q2), late filing common and unenforced (p. 1312 fn. 13, Q3), filings clustering at (t+9, t+13) — and never models it as a choice. GMM have no filing at all (`filing` **0**). **NARROW stands.**

---

### W10 — **Price informativeness** × a disclosure-rule margin. **NARROW**

**(a)** ∂(price informativeness)/∂(threshold or window), in a model where the rule is a primitive.

**(b)–(c) Refuter candidates.**
- **Edmans (2009)** — **one assumption away, and he names the assumption.** Proposition 3 (p. 2496) gives the inverse-U of market efficiency in liquidity **holding α fixed**; Proposition 4 (p. 2498) kills it once α is endogenous; and on p. 2499 he names the 5% Section 13(d) trigger as a reason α may fail to respond to liquidity. So the disclosure rule is the *pin* that preserves his hump, and he never models it. His n. 7 (p. 2485) states the whole contrast in two sentences.
- **Edmans–Manso (2011)** — the 5% trigger is named once, in fn. 7, and declined; there is **no** liquidity effect in their core model.
- **Back et al. (2018)** — efficiency is the object (P̄), but the rule is σ_x precision or σ²T; no partition, no threshold.

**(d) NARROW.** Edmans (2009) is one modelling step away (endogenise the trigger he names), and he supplies the argument for why exogenous-stake comparative statics are legitimate. Any claim here must cite p. 2499 explicitly or it reads as unaware.

**Sweep check (2024–26).** Neither touches it. GMM have a stock price and a price-impact slope but no informativeness object and, decisively, **no private information**: every price is set by agents who correctly anticipate effort (card §5). Zeng has no price object as an outcome — the 13D/13G price reaction is background motivation only (card §6). **NARROW stands.**

---

### W11 — **Optimal window design** (a regulator choosing the deadline), with a welfare ranking of investors / blockholder / regulator. **NARROW**

**(a)** The OCB welfare architecture, re-run on the window margin: does the ordering of preferred deadlines differ from the ordering of preferred thresholds, and why?

**(b)–(c) Refuter candidates.**
- **Ordóñez-Calafi & Bernhardt (2022)** — own it on the **threshold level**: "Proposition 4 derives the consequences of disclosure thresholds by characterizing the ordering of the optimal threshold policies for investors, the activist, and a welfare-maximizing regulator representing society." (p. 2847), with the caveat that agreement exists only in the non-binding region (p. 2856). They have **no window at all**, and they hand the empirics to others, naming *threshold* variation only (p. 2855).
- **Corum (2025)** — has a policy taxonomy (A)–(D) and an instrument ranking, but both margins are absorbed into η and λ, so "how long you may wait" and "how much you may hold" are the same parameter move (fn. 22, p. 26).

**(d) NARROW.** The template is OCB's and must be cited as such. The card itself frames the move: *OCB rank the three parties over the threshold level; we rank them over the window, and the ordering differs because the window, unlike the level, lets the blockholder keep buying after crossing.* That last clause is the substantive claim and it is not in any card.

**Sweep check (2024–26).** Neither addition has a regulator, a welfare object, or a policy instrument. GMM's one policy question is about *control rights* (staggered boards), not disclosure, and they leave the risky-debt variant of it unanalysed (App. 28). **NARROW stands.**

---

### W12 — The **premium wedge microfounded from the partition** — a tender-offer game in which the bidder's inference depends on whether the block is flagged. **CLEAR** on the mechanism, **NARROW** on the existence of a wedge

**(a)** m₁ − m₀ (or a λ-scaled appropriability coefficient) arising because the bidder or the market conditions on *whether disclosure has occurred*.

**(b)–(c) Refuter candidates.**
- **Burkart & Lee (2022)** — Lemma 2 (p. 1877) forces the bid price to equal the full post-takeover value, so free-riding leaves no wedge; and their IA Prop. 1 (IA pp. 12–13) produces a wedge **above** that price, but through a legal-commitment channel in ε, with a comparative static that runs the "wrong" way (more legal risk → smaller premium). Two escape routes are pre-closed in fn. 11 and fn. 12, p. 1884 (freeze-outs harm bidders; "improved merger terms" maps onto regular activism).
- **Burkart–Lee–Voss (2024)** — revelation happens, but **by action**: "The very fact that L abstained from making a tender offer credibly reveals that the possible value improvements are truncated" (printed p. 39). Chosen by the blockholder, not imposed by a rule.
- **Kyle & Vila (1991)** — "We do not model in this article where the premium v comes from; it is exogenously specified." (p. 56). With v exogenous, a rule could change *whether* a takeover occurs, never *at what price*.
- **Corum–Levit (2019)** — they have a signed premium statement and it runs against a naive story: condition (8) implies π_{γ/α} < π_b (p. 9), and π_{γ/α} decreases in α (p. 8), so with α\* = ᾱ a *higher* threshold means a *lower* premium.

**(d) CLEAR** for the mechanism (partition → inference → premium); **NARROW** for the bare claim "a wedge above the free-rider price exists", which Burkart–Lee's IA already delivers by another route. The card's instruction stands: cite IA Prop. 1 when defending the wedge, and say plainly that ours comes from the partition, not from ε.

**Sweep check (2024–26). GMM's card addresses this cell by name and it survives, for a structural reason worth borrowing.** There is no partition to work with — trades are observable from the outset (p. 6, Q5) and prices are set by competitive price takers (p. 12, Q6) — and no premium object (`premium` **0**, `tender` **0**). The price jump at θ\* is "a jump in the *pricing function of a monopsonist buying inelastic supply*, not a bid premium paid to induce tendering" (card §7 item 2). Their p. 20 sentence — they raise the free-rider problem, note it would kill entry, and neutralise it by assumption with no Grossman–Hart citation (`Grossman` **0** hits) — is an **opening, not an occupant**: our partition is a microfoundation for the assumption they make by hand (Q3). **CLEAR / NARROW stands.**

---

### W13 — **Campaign success** × window CHANGE. **CLEAR** on occupancy, weak on power

**(b)–(c)** Johnson–Swem own campaign success structurally with no window and no threshold (`disclosure` = 0 hits in the article; OA `disclos*` = 0). Becht et al. own outcomes cross-country on the threshold **level**, with the takeover-outcome coefficient null (IA "Table 18"). Gantchev owns the cost ladder behind success, with the 5% threshold as a sampling frame and the ten-day window "stated in Appendix A and never used" (§6). Trivedi has no campaign object at all.

**(d) CLEAR** — but note Gantchev's data say roughly two in five flagged campaigns are about who owns the firm (sale-of-company 31.55%, activist bids 10.52%, PDF p. 23), which is an argument for the *control outcome* rather than campaign success as the object.

**Sweep check (2024–26).** Neither touches it. Zeng: `campaign` **2** hits (a wolf-packing definition and one prose mention), never an outcome; `proxy fight` / `proxy contest` / `board seat` **0 each**. GMM: `campaign` **0**, `proxy` **0**. **CLEAR stands.**

---

### W14 — Cells that look open but are **really occupied** (do not stumble in)

| Cell that looks open | Owner, with page |
|---|---|
| "Liquidity has a hump-shaped effect on governance" | Maug Prop. 7 (p. 83); Edmans (2009) Prop. 3 (p. 2496); LMM (2024) Prop. 7 (printed p. 31) *(fixed by verifier: p. 32 is the discussion sentence "Proposition 7 reveals a new force…"; the proposition is printed on p. 31)* |
| "A shorter window means less informed trading" | Back et al., p. 1453 (σ²T isomorphism) |
| "The market infers an intervention from order flow" | CCKV, Thm 1, p. 17 |
| "Nobody has a non-fixed horizon in a Kyle model" | Caldentey–Stacchetti (2010) and Baruch/Back–Baruch, via CDF (2016) p. 1450 |
| "Activism moves the takeover premium" (as a number) | Celentano–Levine, Table 4 p. 43 and Table 5 p. 44 |
| "The threshold changes what an engagement achieves" | Becht et al., IA "Table 18" — **tested, null** (0.015 [0.025]) |
| "Nobody has run a DiD on the Feb-2024 change" | Trivedi, Table 2 p. 11 (compliance share +0.348, p = 0.007) |
| "Nobody has documented how the 10-day window was used" | BBJJ, Table 2 / pp. 10–11; Polk et al., Table 3 p. 526 |
| "Liquidity is priced in takeover premia" | Massa–Xu p. 1483 (+10%/SD, target side); Dass et al. p. 25 (−4.46 to −4.67 pp/SD, acquirer side) |
| "Stake at filing responds to the window change (dose DiD)" | **The author's own `proposal/`** — object, margin and dose all occupied (`empirics.tex:133-138`); ADR-0004 says it does not *reserve* the anchor, but re-entering the identical cell is a duplication, not a position |
| "The threshold caps the secret stake" | OCB, p. 2836 |
| "An activist's presence raises takeover probability" | Corum–Levit, Cor. 1 / Prop. 5 (theory). **And empirically** *(added by verifier)*: Greenwood & Schor, **p. 372, Table 6** — 18.1% of activist targets acquired within 12 months vs 7.2% matched, an ~11 pp gap; long-run abnormal returns are **entirely** a takeover phenomenon (acquired +25.85%, t = 7.9, vs independent +2.85%, t = 0.6, p. 369, Table 4 Panel B). **Klein & Zur** is the standing counterexample on the same object for hedge-fund targets |
| "The activism announcement return is a takeover premium in disguise" *(added by verifier)* | Greenwood & Schor, pp. 368–369, Table 4 Panel A: [−10,+5] CAR **5.72%** for targets acquired within 18 months vs **2.36%** for those that stay independent. Any model of ours must reproduce the acquired/independent split, and Klein & Zur (2009) find the conditioning does *nothing* on their hedge-fund sample — cite both or a referee will |
| "Activism targets are the liquid firms" *(added by verifier)* | Brav et al. (2008), Table 3, printed p. 46: Amihud difference vs matched peers **−0.075 (t = −3.99)** — but **43.4% of targets sit in the third liquidity quintile** of the CRSP universe. The non-monotone pattern our hump would predict is **already in print, unremarked**; the contribution has to be the mechanism and the margin, not the pattern |
| "Activism substitutes for hostile takeovers" | Burkart–Lee Prop. 3 (p. 1881); BLV Prop. 3 |
| "Liquidity predicts 13D vs 13G" | Edmans–Fang–Zur (printed p. 24) — and it is a reduced form, never instrumented (fn. 27, p. 1473) |
| "Liquidity predicts activism incidence" | Norli et al. (Table 3 col. 2); Fos (2017) |
| "Activists time trades to liquid days inside the window" | Collin-Dufresne & Fos (2015), p. 1557 |
| "A blockholder chooses between intervention modes" | BLV, printed p. 8: only four papers do so — Shleifer–Vishny, Bebchuk–Hart, Maug, Burkart–Lee |
| "The 13D announcement return is mostly treatment" | AFS, p. 3 (75.2 / 12.2 / 12.6) |
| "A blockholder's stake path that builds gradually and ends in a lumpy full acquisition" | **Gryglewicz–Mayer–Morellec (2025)**, Prop. 7, p. 28, in continuous time with closed forms — and the bimodal reinforcement result with it *(added by the 2024–26 sweep)* |
| "Insiders and managers trade ahead of the 13D flag" | **Zeng (2026)**, *RAS* 31, 1301–1341, on 2002–2022 filings *(added by the sweep)*; also Duong–Pi–Sapp, *JCF* 93 (2025), ~12% average insider profits, and Chabakauri et al. (2022) via order-flow filtering — the last two **not read, not carded** |

**Sweep check (2024–26).** Two rows added above. No previously-listed owner was displaced, and the sweep found no
2024–26 paper that vacates any cell in this table.

---

### Summary of ratings

| # | Cell | Rating |
|---|---|---|
| W1 | Window length → takeover premium, theory | **CLEAR** |
| W2 | Control outcome × Feb-2024 window CHANGE × DiD with a control group | **CLEAR** (execution hard: 13G unusable as control; power) |
| W3 | Rule-keyed on-path partition (stake trigger + date) | **CLEAR** (boundary: Kyle–Vila own the un-keyed pooled/revealed split) |
| W4 | Threshold level and liquidity as separate parameters, on a control outcome, PROVED | **NARROW** — OCB one object away (Q9, p. 2854, ASSERTED) |
| W5 | Legal filing deadline with a partition attached, in a Kyle-type model | **CLEAR** (boundary: random horizons occupied) |
| W6 | Rule × liquidity **interaction** (slope, not level) on a control outcome | **CLEAR** |
| W7 | 13D/13G purpose partition → control outcome | **NARROW** — AFS one object away (fn. 16, p. 34; p. 15) |
| W8a | Bidder entry × threshold level, theory | **NARROW** — Corum–Levit one derivative away |
| W8b | Bidder entry × window, theory | **CLEAR** |
| W9 | Filing delay as a choice (endogenous flag timing) | **NARROW** — *(re-rated by verifier)* the modelled choice is open; the realised delay is priced by Polk et al. (Table 3, p. 526) and distributed by BBJJ (Table 2, p. 10) |
| W10 | Price informativeness × disclosure margin | **NARROW** — Edmans (2009) p. 2499 names the pin |
| W11 | Optimal **window** design with a three-party welfare ranking | **NARROW** — OCB own the architecture on the threshold |
| W12 | Premium wedge microfounded from the partition | **CLEAR** on mechanism / **NARROW** on "a wedge exists" (Burkart–Lee IA Prop. 1) |
| W13 | Campaign success × window CHANGE | **CLEAR** on occupancy; power-limited |

**Effect of the 2024–26 sweep on these ratings: none.** Zeng and Gryglewicz–Mayer–Morellec were checked against
every W-item above and neither occupies any of them; sweep B's own verdict is "DIRECT — none found". Three things
did change without moving a rating: W2 gains an execution warning (Zeng's 1–13-calendar-day screen is not neutral
across 2024-02-05), W3 gains a wording constraint (our pooled state is *pooled for the price-setting market* —
insiders are a documented exception), and W8b gains an object-side constraint (the stake path ending in a full
acquisition is now GMM's). **One rating is provisional for a reason outside the cards: W7**, because the sweep's
only DIRECT hit — Payne-Mann, Stice-Lawrence & Wong (SSRN 5076900), a control-outcome result keyed to the 13D/13G
split — is behind a wall and has not been read.

**Nothing in this file restates a card's claim beyond what its own §6, §7 and §8 say. Where a card and prior notes
disagreed, the card wins.**

---

## Verification log

**Adversarial verifier, 2026-08-19.** A separate agent from the builder; never saw the builder's reasoning.
Method: every Part-1 quote and every Part-3 quote re-grepped against the **text extract or the PDF itself**
(`grep -nF` on a distinctive fragment, then `pdftotext -f N -l N -layout` to confirm the printed page); every
"= 0 hits" scope claim re-run as a fresh full-text count; every page/§ cite opened in the owning card. Verdicts:
**OK** / **WRONG** (contradicted by the card or the source) / **MISCITED** (true, citation off) / **UNCHECKED**.

### Part 1 — the competitor table (11 rows, 7 cells each = 77 cells)

| Row | Verdict | Checked against |
|---|---|---|
| `celentano_levine_2025` | 6 OK / 1 MISCITED (venue cell) | Quote at PDF p. 11 = printed p. 10, fn. 5 (`pdftotext -f 11`); scope grep re-run on `celentano-levine-2025-ssrn.txt`: Kyle / Amihud / market maker / order flow / bid-ask / price impact **all 0**; 52,666 firm-years = card §2. **MISCITED:** the venue cell named the 24-Oct SFI deposit while every page cite is to the 1-Oct-2025 PDF the card actually read — provenance added in place. |
| `johnson_swem_2021_jfe` | 7 OK | Q7 at printed p. 52 (PDF p. 24) confirmed; `disclos*` = **0** in the article, `liquid*` = **0** in the Online Appendix; fn. 13 confirmed on printed p. 39; 2,434 campaigns = card §2. |
| `cetemen_..._2026_jf` | 7 OK | Quote at PDF p. 12 = **printed p. 11** (page footer read directly); `13D` = exactly **3** hits; premium / tender / merger = **0**; fn. 8's 2-business-day text confirmed on printed p. 11; Thm 2(iii.1) at p. 24 = card R14. |
| `albuquerque_fos_schroth_2022` | 7 OK | "We leave these extensions for future research" confirmed with the printed **41** on the following line; 69,937 filings and the 28,663 dropped February-14 filers = card §2; Amihud +0.021\*\*\*/+0.019\*\*\* = card R5. |
| `back_et_al_2018_ecta` | 7 OK | fn. 10 confirmed on printed p. 1435 (JSTOR page header read); fn. 13 = the 13D/13F disclosure note on p. 1436; the σ²T sentence on p. 1453; p. 1443's "activism → liquidity" passage. **The row's "5 hits total" is exact**: 5 distinct lines (1 Kyle–Vila prose, 1 campaign-goal list, 3 reference titles). |
| `trivedi_2026_ssrn` | 7 OK | Quote on p. 11; scope grep re-run: takeover / premium / toehold / stake / activis\* / block\* **all 0** over 25 pp; κ = 10% participation cap = card §7. |
| `corum_2025_ssrn` | 7 OK | Quote at printed p. 9; bidder / premium / tender / merger = **0** over 77 pp; fn. 22's proposed-vs-adopted split confirmed on p. 26; the two-state liquidity microfoundation at p. 74 = card Q8. |
| `corum_levit_2019_jfe_published` | 7 OK | fn. 25 confirmed on printed p. 10; `13G` = **0**; "days" only in "in the old days"; "window" only as *event window*; none of the seven Predictions is a comparative static in the premium (card §3, R-none). |
| `polk_buchheit_riley_stone_2024_jfrc` | 7 OK | Quote at PDF p. 16 = printed **531**; scope grep re-run: liquid\* / Amihud / bid-ask / spread / turnover / takeover / premium / bidder **all 0**; 9,685 filings = card §2. |
| `bishop_fos_jiang_partnoy_2026` | 7 OK | Quote at PDF p. 30 = printed **29**; liquid / Amihud / volume / price impact = **0**, turnover = 1; 1.27m firm-months = card §7. |
| `author_proposal_outline_2026` | 7 OK | Both quotes located in `proposal/sections/model.tex` at **lines 434–435** and **447–448**; `empirics.tex` lines 7–11, 108–112, 114–117, 133–138, 143–146 and 166–168 all read and matching. |

**Part 1 totals: 76 OK / 0 WRONG / 1 MISCITED / 0 UNCHECKED.**

### Part 2 — the occupied cells (18 items + the section header)

- **Section header — WRONG, fixed.** "Items 1–10 are `INDEX.md` §4 items 20–29" does not hold: §4 items 22, 23, 25, 27 and 28 land at Part 2 items 12/14/17 or (before this pass) nowhere. Replaced with an accurate sentence.
- **Item 1 — MISCITED, fixed.** LMM (2024) Proposition 7 is printed on **p. 31**, not p. 32 (p. 32 carries the discussion sentence "Proposition 7 reveals a new force…"). Corrected here and in W14. Maug Prop. 7 p. 83 and Edmans Prop. 3 p. 2496 / Prop. 4 p. 2498 / n. 7 p. 2485 all confirmed against the cards.
- **Items 2, 3, 4, 5 — OK.** Back p. 1453 grepped in the source; CCKV Thm 1 p. 17 = card §9 Q8; Caldentey–Stacchetti at CDF (2016) p. 1450 = card §5 + fn. 6; CL Table 4 p. 43 (−13.69) and Table 5 p. 44 (36.70 vs 36.92) = card R6/R6b.
- **Item 6 — OK, executed check.** Re-read `becht_2017_internet_appendix.txt` directly: the Disclosure Threshold row prints `0.048 | 0.003 | 0.077* | -0.046 | 0.015` — takeover **0.015**, as claimed.
- **Items 7, 8 — OK.** Trivedi Table 2 +0.348/0.130/2.69/0.007 = card R2; Polk Table 3 1.34 → 5.09 = card R3; BBJJ 45.3% / median 6.3% = card R1/R4.
- **Item 9 — OK.** Dass −4.46/−4.67 pp, Table 8 Panel A printed p. 58 = card R3 (and the card's own warning that the SD used is the full-sample one is worth carrying); Massa–Xu "10%" text p. 1483, coefficient 12.151 Table 7 p. 1482, 4,691 deals 1987–2007 = card §2.
- **Items 10–18 — OK.** OCB p. 2836 = card Q1; Corum–Levit Cor. 1 / Prop. 5 = card §9 item 1; BL Prop. 3 p. 1881 and BLV Prop. 1 (printed p. 16) / Prop. 3 (printed p. 27); BL Lemma 2 p. 1877 and **IA Prop. 1 located directly in `burkart_lee_2022_internet_appendix.txt` (Section E, "Two-tier tender offer", statement at IA p. 12)** — executed check; AFS 75.2/12.2/12.6 of 6.34% p. 3 and C = 4.6 pp ≈ $2.43m p. 28; EFZ 6.88 pp / 43.2% printed p. 24, 0.47 pp printed p. 21, fn. 27 p. 1473; Norli Table 3 col. 2, Fos (2017), CDF λ "almost 30% lower" JF p. 1557 and the limit-order sentence p. 1558 with the n. 22 Bayes caveat.

**Part 2 totals: 17 OK / 1 WRONG (section header) / 1 MISCITED (item 1) / 0 UNCHECKED.**

### Part 3 — whitespace (W1–W14)

| Item | Verdict | Scope grep I re-ran, and what I found |
|---|---|---|
| W1 | OK; rating CLEAR stands | Back: takeover 5 / bidder 1 / tender offer 0 / acquirer 0 / premium 1 — **5 distinct lines**, all Kyle–Vila prose, a campaign-goal list, or reference titles. Corum–Levit: `13G` 0, "days" only in "in the old days". Corum: bidder/premium/tender/merger 0. BL p. 1891 quote found verbatim. **Cross-sweep of all 40 cards found no card holding a window-as-length *and* a premium in theory.** Omission added: Faure-Grimaud–Gromb (p. 999, p. 988). |
| W2 | **WRONG (quote), fixed**; rating CLEAR stands | The string *"our analyses compare investors who filed voluntarily within five days with those who waited the full ten"* is **in neither the Polk article nor the Polk card** — replaced with the card's verified p. 516 quote plus the actual Delta ≤ 5 vs 6–10 comparison. Trivedi's six zero-counts and Polk's eight zero-counts re-run and confirmed. Bishop's p. 36 sentence found at PDF p. 37. Omission added: BBJJ p. 28 takeover-defence confound. |
| W3 | OK; rating CLEAR (with boundary) stands | CCKV fn. 16 found; OCB p. 2836 found; CDF (2016) "Fourth, we assume that the presence of the insider is common knowledge" found on p. 1464; Corum p. 19 found (txt renders "di¤erence"); Kyle–Vila n. 1 found. Omission added: **Maug p. 73** — `INDEX.md` §4 item 13, the cleanest whitespace sentence in the antecedents, entirely absent from this file. |
| W4 | OK; rating NARROW stands | OCB: bidder 0 / premium 0 / tender 0; `takeover` = **3 body occurrences, all on printed p. 2854** (PDF p. 21) as claimed, plus 2 reference titles. p. 2854 and Prop. 4 p. 2847 quotes found. Omissions added: Corum (2025) as a second *fusing* card; Edmans (2014) p. 45. |
| W5 | OK; rating CLEAR (with boundary) stands | Back fn. 10 p. 1435 and the p. 1454 future-work item found (hyphenated across lines); CDF (2016) "Second, we assume that the horizon is fixed" p. 1464 found; CCKV p. 10 and p. 35 quotes found. |
| W6 | OK; rating CLEAR stands | Trivedi R4/R5 (+0.0013, SE 0.0051; +0.41, SE 0.81) = card; Polk's zero liquidity counts re-run. Omission added: **Edmans & Holderness pp. 76–77 + Gantchev & Jotikasthira (2016) at p. 28** — `INDEX.md` §4 item 28, absent from this file and the nearest existing empirical neighbour to the accumulation margin. |
| W7 | OK; rating NARROW stands | AFS fn. 16 p. 34 and the p. 15 "transaction costs differential" sentence both found in the WP text; EFZ 0.7% printed p. 27 = card Q12; Corum p. 19 / p. 20 fn. 17 found. |
| W8a | OK; rating NARROW stands | Corum–Levit Prediction 5 p. 11 found; Becht IA takeover coefficient re-read from the IA text (0.015); Kyle–Vila single-raider assumption = card. |
| W8b | OK; rating CLEAR stands, with a standing risk now flagged | BLV re-grep on the held text: `disclos` 0, `13D` 0, `Schedule` 0, `window` 0, `filing` 0 — confirmed; "Market liquidity plays no role in our analysis" found (printed p. 9); EGJ p. 966 and p. 936 both found. **Added:** every BLV cite is to the Feb-2024 WP; ECGI records a 29 Dec 2025 revision that is not in the repo. |
| W9 | **rating WRONG (CLEAR → NARROW), fixed**; refuter list was incomplete | The cell as written ("the blockholder chooses when to file… and that choice is priced") does not restrict to theory, and **Polk et al. price the realised delay** (1.34% at Delta = 0 → 5.09% at Delta = 10, Table 3, p. 526, 9,685 filings) while **BBJJ distribute it** (45.3% in the 8–10-day bucket, Table 2, p. 10). Both cards were missing from the refuter list. Re-rated NARROW; the modelled choice stays open and the claim is now worded so. |
| W10 | OK; rating NARROW stands | Edmans Prop. 3 p. 2496, Prop. 4 p. 2498 and the Section 13(d) sentence at p. 2499 all confirmed in the card's §6; Edmans–Manso fn. 7 = card. |
| W11 | OK; rating NARROW stands | OCB Prop. 4 quote found at printed p. 2847; "industry-specific thresholds based on liquidity measures" found at printed p. 2854; Corum fn. 22 p. 26 found. |
| W12 | OK; rating CLEAR/NARROW stands | BL Lemma 2 p. 1877 and **IA Prop. 1 located in the IA file itself**; BLV p. 39 "abstained from making a tender offer" found; Kyle–Vila "it is exogenously specified" p. 56 found; Corum–Levit p. 8 / p. 9 = card R16 + §9 item 4. |
| W13 | OK; rating CLEAR stands | JS `disclos*` = 0 in the article and OA; Gantchev's window "stated in Appendix A and never used" = card §9 (ten days appears twice, PDF pp. 19 and 37); Gantchev 31.55% / 10.52% = card R19; Trivedi has no campaign object. |
| W14 | MISCITED (LMM page), fixed; 3 rows added | LMM Prop. 7 → printed p. 31. Rows added: Greenwood & Schor's ~11 pp takeover-probability gap (p. 372, Table 6) and the acquired/independent CAR split (pp. 368–369) with Klein & Zur as the standing counterexample; and Brav et al.'s Amihud −0.075 (t = −3.99) with **43.4% of targets in the third liquidity quintile** — the non-monotone pattern is already in print. |

**Part 3 totals: 11 OK / 2 WRONG (W2's fabricated quote; W9's rating) / 1 MISCITED (W14) / 0 UNCHECKED.**

### Omissions added by the verifier

1. **`INDEX.md` §4 item 9 — the $810m is not in SEC Release 33-11253.** Added to reading note 11. The proposal repeats it three times; the release's own figure is $49m/year (p. 211) and the Commission disclaims it. Decision-critical for the anchor's motivation.
2. **§4 item 13 — Maug p. 73.** Added to W3. A 13D rule is neither of his two disclosure cases; that seam is the position.
3. **§4 item 14 — Edmans (2014) p. 45.** Added to W4. "Theory models do not predict a discontinuity at 5%."
4. **§4 item 15 — BBJJ p. 28.** Added to W2 as a third execution warning: faster disclosure also speeds up the *defences*, a confound with the opposite sign on a control outcome; their low-trigger-pill moderator is an estimable split.
5. **§4 item 18 — Faure-Grimaud & Gromb pp. 999, 988.** Added to W1.
6. **§4 item 28 — Edmans & Holderness pp. 76–77, and Gantchev & Jotikasthira (2016) at p. 28.** Added to W6.
7. **Greenwood & Schor (p. 372, Table 6; pp. 368–369, Table 4) and Klein & Zur.** Added to W14 — two cards in the repo that own the *empirical* "activism → takeover" cell and were named nowhere in this file.
8. **Brav et al., Table 3, printed p. 46.** Added to W14 — the third-quintile concentration is the hump's shape, already in print.
9. **BLV's Dec-2025 revision.** Added to W8b as a standing, non-closable risk.

### Overall verdict

**The file survives the attack.** Two substantive defects: one fabricated quotation (W2/Polk) and one rating that
was too generous (W9). Two citation slips (LMM's Proposition 7 page, twice; the Part-2 header's §4 mapping). Every
other page cite, quote and zero-count I re-ran against the source held up, several of them exactly — Back's "5 hits
total" and OCB's "three body hits of *takeover*" are correct to the hit. The main weakness was **omission**: six
`INDEX.md` §4 items and four cards in the repo (Maug, Faure-Grimaud–Gromb, Edmans–Holderness, Greenwood–Schor /
Klein–Zur / Brav et al.) had no line anywhere in the file. All are now added.

**Not checkable from the repo, and named rather than triaged away:** (i) every CCKV page cite is to the **NY Fed
Staff Report 1030**, not the JF typeset article — the JF pagination is unverified and must not be cited as
"*Journal of Finance* 2026, p. n"; (ii) **BLV's 29 Dec 2025 revision** is not held, so W8b's and W12's evidence is
as of Feb 2024 only; (iii) six of CCKV's eight propositions live in an Internet Appendix the repo does not hold,
which is what Part 1 row 3's liquidity cell rests on.

### Rows verification (sweep additions)

**Adversarial rows-verifier, 2026-08-19** — a separate agent from the map builder and from the two card verifiers;
scope limited to the material added after the main map pass: the "2024–26 sweep additions" sub-table and its two
reading notes, the Sweep summary, the 14 Part-3 "Sweep check" lines and the two W14 rows added by the sweep. Method:
every cell and quote re-checked against the two **verified** cards (`research/cards/zeng_2026_ras.md`,
`research/cards/gryglewicz_mayer_morellec_2025.md`, both now carrying a §9 log), every sweep number re-counted in
`research/sweep_2024_26_A.md` / `_B.md`, and the load-bearing quotes re-grepped in
`research/txt_extracts/zeng_2026_ras.txt` and `…gryglewicz_mayer_morellec_2025_ownership_dynamics.txt`.

| Item | Verdict | What was checked |
|---|---|---|
| Zeng row (8 cells) | 7 OK / 1 WRONG (fixed) | Venue, object, margin, identification cells all = card header/§4/§6/§7; the Q7 scope quote grepped verbatim in the extract (line-wrapped, p. 1322). **WRONG:** the `illiquidity` = 11 breakdown summed to 10 — the variable-definition hits are **two** (p. 1337 ×2), per card §6. |
| GMM row (8 cells) | 5 OK / 3 MISCITED (fixed) | Greps, object, identification and both scope quotes ("In the benchmark model…", "We sketch the equilibrium…") confirmed in the extract. **MISCITED:** (i) "CEPR DP21226" was presented as paper metadata — card §9 check 4 shows it is **not in the PDF**; (ii) the "liquidity shock" page cite — the phrase is on pp. 5 and 33 only; (iii) the trailing "verifier still running, §3 provisional" note was **stale** (card verified 40/0/4/1, all §3 labels stand). |
| Reading notes (Zeng, GMM) | 2 OK | Every page cite (Q5 p. 1310, Q2 p. 1309, IA.2 p. 1322; Prop. 7 p. 28, Q5 p. 6, Prop. 5 / fn. 13, the κ symbol collision) matches the cards' §6/§7. The sub-table's lead-in sentence "neither is a competitor" was softened: GMM's own card header says **competitor on the object cell only**. |
| Sweep summary (a) — counts | 1 WRONG / 1 MISCITED (both fixed) | Sweep A's 20 queries (12 Scholar / 4 SSRN / 4 NBER) confirmed row by row; sweep B's 47 log rows confirmed, as are JF 16 / RFS 89 / RoF 28 / RAPS 9 / JFE ×4 / Econometrica 35 / JFQA 20 / ECGI 8 / arXiv 5. **WRONG:** "six conference programmes" followed by a list of **seven** (rows 41–47), two of which were ConfTool title/author searches rather than PDF greps. **MISCITED:** "CEPR 6 phrase searches" — the log has **seven** (rows 25–31); sweep B's own §4 line says six. |
| Sweep summary (b) — "none found" | OK | The quoted DIRECT-none-found paragraph is verbatim sweep B §2. All eleven zero-result query families verified in the logs (arXiv rows 34 and 36 correctly excluded — they returned one out-of-window hit each). Source-level list and both soft walls (NY Fed row 38; SSRN login) match. |
| Sweep summary (c) — Payne-Mann | OK / 1 wording fix | SSRN 5076900, 27 Dec 2024, USC Marshall / iORB, the certificate-error wall and "abstract only" all = sweep A's DIRECT row. Wording fixed: it is the *outcomes* (M&A activity, turnover, returns) that fall between activist and non-activist levels. |
| Sweep summary (d) — ADJACENT list | OK | All nine lines = sweep A/B ADJACENT rows (venues, URLs, magnitudes: Duong ~12% / 14.5%; Israelsen ~6×; Eckbo N° 1030/2025), plus Chabakauri et al. (2022) from Zeng's card §4/§6 (pp. 1306–1307), correctly marked outside the sweep window and not carded. |
| Part-3 Sweep checks W1–W13 (14 lines) | 14 OK | Every Zeng/GMM claim follows from the cards' §6/§7: Zeng `premium` 0, `campaign` 2, `proxy fight`/`board seat` 0, Amihud sign wander (−0.025\*\* / +0.154\*\*\*), 29.8% of daily volume (Table 1 Panel B, p. 1316), the Item 4 taxonomy (36.6 / 43.3 / 20.0, p. 1315), the fn. 13 1–13-day screen (Q4, p. 1312) and the 13G extension (Q9, p. 1327); GMM's zero-counts, Prop. 5 / fn. 13, Q5 p. 6, Q6 p. 12, App. 28, `Grossman` 0. Two claims not stated in either card were checked directly in the GMM extract and hold: `horizon` **0** and `deadline` **0** (W5's "no horizon or deadline of any kind"). **No rating is changed by any Sweep-check line, and no card forces one.** |
| W14 — two rows added | 2 OK | GMM row: Prop. 7, p. 28, closed-form, plus the bimodal reinforcement result (card §7, R8 PROVED). Zeng row: *RAS* 31, 1301–1341, 2002–2022 (card header/§2); Duong–Pi–Sapp and Chabakauri correctly marked *not read, not carded*. No previously listed owner displaced. |

**Counts for the sweep additions: 32 OK · 2 WRONG (both fixed) · 4 MISCITED (all fixed) · 0 UNCHECKED.**

**Companion edits in `research/cards/INDEX.md`** (same pass): the 42-card count re-derived by `ls` (44 non-underscore
files − INDEX − the superseded Corum–Levit card) and the 11 / 15 / 14 / 2 split re-counted row by row — **OK**; the
GMM row's and the §2 bullet's "verifier still running" caveats replaced with the card's real tally (40 / 0 / 4 / 1)
and the CEPR/AFA metadata tagged as external; the Zeng row's empty verifier cell filled with 30 / 3 / 2 / 5.

**Not fixed, outside this pass's scope:** `INDEX.md` §3 ("UNCHECKED items by card") has **no line for Zeng or for
GMM** — Zeng's five Internet-Appendix items, IA Table IA.2 among them, are decision-critical and are listed only in
the card — and §3's own header still says "19 of the 39 indexed cards" against a 42-card index.
