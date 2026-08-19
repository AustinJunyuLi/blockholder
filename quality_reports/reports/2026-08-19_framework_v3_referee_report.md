# Referee Report — `framework_v3` ("Disclosure, Liquidity, and Takeover Premia: Repositioning Framework v3")

**Date:** 2026-08-19 · **Object:** `framework_v3.qmd` / `framework_v3.pdf` (Aug 19, 2026 version, archived at
`quality_reports/rewrites/framework_v3_pre-review_2026-08-19.qmd`) · **Posture:** JF/RFS referee report on the
memo *as a research plan* (originality, methodology, results, empirical design), followed by the edits made.

**How this report was produced.** A bounded team of five parallel referee agents (theory validity;
literature positioning/originality; novelty/competitor scan with browser access; empirical design incl.
execution on the disk-resident data; facts/citation verification against primary sources), followed by two
independent adversarial verifiers (theory; lit/novelty/empirics/facts) who received the claims but not the
finders' reasoning, plus the orchestrator's own executed checks with the repo model. Agent reports are in
`research/review_v3/` (`theory_referee.md`, `lit_referee.md`, `novelty_scan.md`, `empirics_referee.md`,
`facts_verification.md`, `verify_theory.md`, `verify_facts.md`). Verification status is marked per finding:
**[V]** confirmed by an independent verifier or an executed check; **[F]** finder-only; **[O]** orchestrator's
own executed check.

---

## 1. Summary assessment

**Recommendation on the plan: major revision before any theory surgery or data work proceeds.** The angle
(the 13D disclosure rule as a policy lever on *revelatory* price efficiency in the market for corporate
control) is credible and the two "quotable gaps" (Back et al. 2018, Ecta p.1454; Burkart–Lee 2022, RFS
p.1891) are verbatim-accurate. But the memo overstates originality on page 1, its headline theorem T2 is not
proved as written and its economic sign is calibration- and margin-dependent, several results are labelled
"proved"/"certified" that are to-dos, and the empirical section is a well-read plan whose three headline
numbers shrink under inspection — including a pre-trend check on the disk data that shows **no break in 13D
announcement CARs at 2024-02-05**. Every problem is fixable; none is cosmetic.

**Five things that must change (each expanded below):**
1. **Originality claims** ("first formalization", "nobody links…", "no precedent", "no SSRN-visible work") are
   false or overclaimed; the defensible claim is the *disclosure partition* + the *deadline* as a lever.
   Kyle–Vila (1991), Mello–Repullo (2004), Cetemen et al. (JF 2026), Trivedi (SSRN 2026), Polk et al. (JFRC
   2024) and Corum (SSRN 2025) must be engaged. **[V]**
2. **T2** is a two-term product rule; the memo names only the weight term. Which margin τ moves decides the
   sign: moving quiet engagement into disclosure attenuates (a fortiori); moving the *disclosed buy* between
   flagged and pooled — the window/timing margin that the Feb-2024 shock actually moves — does **not**
   attenuate uniformly at fixed cutoffs at the paper's own calibration. And at baseline the disclosed branch
   carries only ~3.7% of mass, so the attenuation figure shows two curves within ~1%. **[O/V]**
3. **τ is not a primitive** in the model; existence is not "unconditional"; the GE region theorem for
   attenuation does not exist; the Celentano–Levine "rationalization" lives at λ < 0.07 while the calibration
   sits at λ = 0.86. **[V]**
4. **The empirical design** is a before/after with an interaction, not a DiD; 13G filers are not a control;
   the 10 p.m. ET filing cut-off and anticipation are unlisted confounds; H2's ratio statistic is ill-defined;
   H3 is underpowered and conditions on the outcome; F1 rests on 188 parsed filings (Manski bounds overlap);
   the `pct_of_class` parser is broken (100% → 0.0; 448 rows at 2.6%); half of the calibration rows have no
   model counterpart. **[V]**
5. **Facts:** Boyson et al. "70% within 2 years" is wrong (paper: >1/3; 22% risk-arb-excluded); C&L "+7.7pp"
   is "7.7 percent" (relative); Norli's 0.33%→0.73% is the baseline probit, not IV; CDF's 7% run-up is a
   60-day window from the NBER WP; κ† = 0.58 in the exported data. **[V]**

---

## 2. Originality and positioning (Section 1 of the memo)

| # | Memo claim (line) | Verdict | Evidence | Fix applied |
|---|---|---|---|---|
| O1 | "the first formalization of how the market learns about activism-driven control events" (l.30–35) | **WRONG** as written [V] | Kyle & Vila (1991, RAND 22:54–71) already model noise-trading camouflage enabling a control-seeking outsider to accumulate; Back et al. (2018) is exactly pre-disclosure learning under a fixed horizon (Burkart–Lee themselves: the toehold problem "has been comprehensively studied by Back et al. (2018)", RFS p.1891); Cetemen–Cisternas–Kolb–Viswanathan (JF 81(3):1377–1435, 2026) do dynamic activist inference. | Restated: the novelty is the *partition* (disclosed vs inferred branches priced by the same market) and the *rule* (deadline/threshold) as the lever, not "market learning". |
| O2 | "Nobody … links market liquidity or the disclosure rule to takeover premia" (l.35–38) | **OVERCLAIM** [V] | True of the five named papers; false as a universal: Maug (1998) makes liquidity govern intervention mode; Mello & Repullo (2004, FRL 1:2–10) "Shareholder Activism is Non-Monotonic in Market Liquidity"; Massa–Xu (JFQA 2013) and Huang–Maharjan–Nanda (JCF 2024) estimate liquidity→premium elasticities — cited by the memo itself in §4. | Restated as "no paper makes the disclosure *rule* the state variable mapping liquidity into the premium; each named paper holds one lever fixed"; Mello–Repullo added and must be distinguished from T4. |
| O3 | Gap quotes from Back et al. and Burkart–Lee (l.42–45) | **SUPPORTED, verbatim** [V] | Ecta p.1454 ("we assume that the horizon at which the activist's stake is disclosed is fixed … interesting to endogenize the horizon"); RFS p.1891 ("we do not endogenize the acquisition of the toehold in anonymous, predisclosure markets… We leave … to future work"). | Kept; page numbers added; the follow-on BL sentence acknowledged. |
| O4 | "Every top-3 theory paper … closes with a measurement section"; "A numerically verified headline result has no precedent" (l.46–51) | **OVERCLAIM / partly WRONG** [V] | Venues verified (BL RFS 35(4); LMM JF 79(1) & JF 81(3); Kakhbod et al. RFS 36(4); Chen–Gupta–Starmans JFE 181), but Burkart–Lee ends at "Concluding Remarks" (no measurement section); CGS is a sustainable-investing paper. "No precedent" is unfalsifiable. | Softened; CGS dropped from "this space"; Burkart–Lee–Voss (ECGI 956/2024, 2025 ECGI prize) and Corum–Levit (2019) named instead. |
| O5 | "No published or SSRN-visible empirical work exploits [the Feb-2024 shock]; one working paper engages the window trade-off theoretically" (l.52–55) | **WRONG** [V] | Trivedi, SSRN 6866499 (posted 3 Jun 2026): pre-registered DiD on the 5-bd deadline with 13G controls (+0.35 on share within 5 bd, p=0.007; nulls on lag/spreads/illiquidity proxy). Polk–Buchheit–Riley–Stone, JFRC 32(4) 2024 (published) on delay-period abnormal returns. The unnamed WP is Corum (Cornell), SSRN 4319599, "The Stick or the Carrot?…" (liquidity × regulation × activism; no premium). Bishop–Fos–Jiang–Partnoy (SSRN 6061814, 2026) work the HSR-disclosure margin. | Rewritten; competitors named and differentiated; "window open but closing" → "~12 months; the first-stage fact is already public". |
| O6 | Celentano–Levine: "no trading, no price formation, stake fixed at 5%" (l.57–61); "R&R at RFS" | **SUPPORTED except one word** [V] | Stake fixed at 5% (C&L txt l.518); liquidity enters as a reduced-form entry cost ξ (l.313) — so "no order-flow inference, no price impact" is the accurate phrase; R&R status confirmed via Levine's CV (date-stamp it). | Reworded. |
| O7 | Goldstein (2023) "lists RPE-oriented empirics and feedback interacting with corporate-control frictions as open problems" (l.65–69) | **PARTIALLY SUPPORTED** [F] | RoF 27(1) §5.2.a flags RPE measurement as open; no corporate-control/takeover item in §5.2. | Corporate-control clause attributed to EGJ (2012, JF) instead. |
| O8 | Frontier list / edit map (l.336–338) | Mostly SUPPORTED [V] | LMM 2024 use Walrasian clearing (no Kyle market maker) — a *precedent*, not a proof of "acceptability"; Ben-David et al. JF 2026 has four authors (add Ruidi Huang); Burkart–Lee (2022) missing from `bibliography.bib`; BLV = ECGI WP 956/2024. | Reworded; citations added to the edit map. |

**Referee's originality verdict.** Genuinely new: (i) the disclosure partition with a bidder pricing off both
branches; (ii) the rule as a lever on *revelatory* efficiency; (iii) the Feb-2024 deadline as a dated shock
with a signed prediction. Not new: market learning about accumulation (Kyle–Vila; Back et al.; Cetemen et al.),
non-monotonicity of activism in liquidity (Mello–Repullo), liquidity→premium reduced-form elasticities. The
phrase "revelation technology of the market for corporate control" is tolerable in an introduction if the
abstract states the narrower, checkable claim.

---

## 3. Model and methodology (Section 2 of the memo)

| # | Finding | Severity | Evidence | Fix applied to memo |
|---|---|---|---|---|
| M1 | **τ is not a primitive.** In draft_v2 D = 1{q=+1} and ω_P = 1−Φ(α_D) is an equilibrium mass pinned by k_D; "ω_P(τ), ω_P′>0" is a relabeling (or moves k_D, contradicting "fixed cutoffs"). [V] | MAJOR | draft_v2.tex l.391–433 | Two explicit margins defined: **threshold margin** τ_θ (a Quiet engagement is disclosed w.p. τ_θ; D=0 masses become (ω_E, ω_H, (1−τ_θ)ω_Q); disclosed-branch κ-invariance survives — checked in the referee report) and **window/timing margin** τ_w (the Public buy is flagged before pricing w.p. τ_w; τ_w=1 = draft_v2, τ_w=0 = the draft's no-disclosure benchmark). Back et al.'s isomorphism maps the window into κ, so the 2024 shock is a joint (dκ<0, dτ_w>0) movement — stated. |
| M2 | **Bidder information set** inconsistent: observes (P,D) but rule uses m̄(X,D); `lem:dropA7` asserts injectivity, contradicted by `app:proof-disclosed-invariance` (one price on all three disclosed cells). [V] | MINOR | draft_v2.tex l.662–674 vs l.2004–2016 | Restated as: (P,D) is a sufficient statistic for the payoff-relevant pair (V̂, m̄) — the disclosed cells share both, so pooling is payoff-irrelevant. |
| M3 | **Three-branch prune** by fiat: Hold's collapse is a baseline numerical fact ("Under this parameterization, the Hold region collapses", l.1010; `prop:cutoffs`: "may collapse", l.410). [V] | MINOR | draft_v2.tex l.410, l.1010 | Assumption (A2′) stated (Quiet weakly dominates Hold on the non-exit region); consequence π̄ ≡ 1 noted (makes (C*) a primitive inequality). |
| M4 | **Existence is not "unconditional"**: T is single-valued only under (A5a); `rem:A5margins` (l.696) says the baseline fails the conservative bound, §5 (l.1010) says it satisfies it (term (ii) of the appendix rule alone) — internal contradiction to resolve; δ = 0.95 in §5/params.py vs δ = 1 in the memo and `lem:transfer-netting`. [V] | MAJOR | draft_v2.tex l.564, 696, 1009, 2015; numerical/params.py | Assumption list corrected to (A1),(A2),(A4)+(A5a); contradiction and δ mismatch flagged as pre-surgery to-dos. |
| M5 | **No-manipulation remark**: EGJ AER 2015 attribution correct (R_H − R_L > 4x/3, verified in the published PDF), but in this menu the EGJ profile is *infeasible* (Exit liquidates the whole unit stake; Public buys). [V] | NOTE | draft_v2.tex l.167–169 | Reduced to one sentence with the right reason. |
| M6 | **D7 symbol labels wrong** in the memo (ϕ is dilution — D7 reserves φ for the normal density —, ψ pivotality, q the fringe-raid probability, γ portability); `q` collides with the order variable. [V] | MINOR | D7 tex l.68–73, 246–250 | Corrected; raid probability renamed r; dilution written ϕ. |
| M7 | Undefined symbols (Δ̃, m^R(a), m̄, m̃ vs m₁, ω's, h, p̄₁, Δ^min, C(s), S̄, K). [F] | MINOR | memo §2–3 | Notation block added. |
| M8 | LMM 2024 "prove non-Kyle technologies are top-3-acceptable" — wrong verb; their technology is Walrasian clearing over a continuum with bounded trade size. [V] | NOTE | levit_malenko_maug_jf2024.txt l.440–450 | Reworded as a precedent. |

**Methodological verdict.** Discrete ternary order flow with a competitive market maker is an accepted
technology (EGJ 2015 is the precedent, and EGJ prove region-wise uniqueness *analytically* — the draft's
"numerical uniqueness following EGJ" misdescribes them, l.702, l.2235). Brouwer existence + labelled numerical
uniqueness is acceptable **only if the headline comparative static is proved** — which is exactly what §4 below
says is not yet true.

---

## 4. Results — what is proved, what is true, and how big it is (Section 3 of the memo)

### 4.1 T2, the headline theorem — not proved as stated; sign is margin-dependent; magnitude ≈ 0 at baseline

* **Algebra.** The decomposition Δ^act = (m̃−m₀)[ω_P p̄₁ + (1−ω_P) E_{D=0}h(κ)] is correct and p̄₁ is genuinely
  κ-invariant (`app:proof-disclosed-invariance`). But the D=0 posteriors are homogeneous of degree zero in
  (ω_E, ω_H, ω_Q) (Prop `prop:posteriors`; `tab:d1-D0cells`), so E_{D=0}h is τ-free **only if** τ rescales all
  three non-disclosed masses proportionally — economically incoherent for a disclosure rule. The correct
  statement is a two-term product rule: ∂_τ|∂_κΔ^act| = (m̃−m₀)[−ω_P′·|∂_κE_{D=0}h| + (1−ω_P)·∂_τ|∂_κE_{D=0}h|].
  The memo's "one line" names only the first term. **[V]**
* **Threshold margin (Quiet → disclosed).** The second term is *also* negative (π̄ falls, and by the chord
  identity of `lem:d1-jensen` the interior κ-motion of E[h] vanishes as π̄↓0): |∂_κE_{D=0}h| falls from 0.0153
  (τ=0) to 0.00014 (τ=0.95) at baseline masses — attenuation holds *a fortiori* but needs a second lemma
  (two paragraphs, not one line). Consistent orchestrator check: lowering k_D at fixed (k₁,k₀) lowers the total
  variation of Δ^act over κ∈[0.15,0.85] monotonically (0.0176 → 0.0040 as ω_P: 0.037 → 0.50) — but most of that
  fall is present *without any disclosure flag* (no-disclosure regime: 0.0165 → 0.0106), because a buy order is
  intrinsically more revealing (X=+2 is reachable only from q=+1). **[O]**
* **Window/timing margin (Public buy flagged vs pooled) — the margin the Feb-2024 shock moves.** Comparing the
  disclosure regime (τ_w=1) with the no-disclosure regime (τ_w=0) at fixed cutoffs, the κ-sensitivity of Δ^act
  is **not** lower under disclosure for ω_P ≤ ~0.29: TV ratio (disc/no-disc) = 1.06 at ω_P=0.037 (baseline),
  1.19 at 0.129, 1.14 at 0.286; only at ω_P=0.50 does it fall (0.38). Pointwise slopes: disclosure is steeper
  at κ ≥ 0.7 for ω_P ≤ 0.29. So "stricter disclosure makes premia less liquidity-sensitive" is not a theorem in
  partial equilibrium; it is a calibration-dependent comparison whose sign depends on which margin moves. **[O]**
* **Magnitude at the paper's own baseline.** ω_P ≈ 0.037 (k_D = 2.26, μ=1, σ_s=0.707), so the memo's headline
  figure (`disclosure_attenuation.csv`, fig:disclosure) shows two curves whose ranges over κ∈[0.15,0.85] are
  0.01107 vs 0.01117 — a <1% difference, and by mean |slope| the *disclosed* regime is slightly more sensitive
  (0.0251 vs 0.0236). The calibration must be re-anchored so that ω_P is empirically meaningful (share of
  engagement that is disclosed) before T2 can be a headline. **[O]**
* **The T2 → H1 mapping is not derived.** T2 concerns the ex-ante expected activism premium Δ^act; H1 tests
  the liquidity slope of the *13D announcement return*, an object the static model does not define. It can be
  defined: the disclosure jump J(X) = P(X,1) − P_ND(X) (price with the flag minus the pooled price at the same
  order flow) is well-defined and, at baseline, E[J | D=1] rises with κ (0.33 at κ=0.2, 0.39 at 0.5, 0.42 at
  0.8; J(2)=0 since X=+2 already reveals the buy). Its response to τ_w is what H1 actually tests, and it must be
  derived and signed before H1 is called "the flagship test of T2". **[O; recorded as a to-do]**
* **GE "region version" (T3).** Does not exist in the repo; D8 bounds dk/dκ only; a cross-partial needs
  d²k/dκdτ, which no contraction modulus reaches. Feasible substitute: compare two first derivatives at τ′>τ
  with the D8 inversion-free bound B̄ evaluated at each τ (triangle inequality; a few days once τ is in
  `numerical/`). Labelled to-do. **[V]**

### 4.2 T4 (hump) — mostly right, one omission
Endpoint symmetry is proved at fixed cutoffs (noise symmetry + disjoint D=0 supports at κ→1); the step that
lifts it to full equilibrium (draft l.815–817) is asserted + numerically checked (gap 6.9e−7) — label it so.
The chord condition matches `lem:d1-jensen` (write "if", not "iff": C=0 unhandled). Certified interval
[0.35, 0.825] and L ≤ 0.836 match the D8 JSON; the σ_ξ=0.60 trough matches `prop:d8-counter`; the
"premium-sensitive" phrasing is consistent with `rem:d8-boundary`. **Omitted:** `rem:d5-vacuous` — (C*) cannot
fail on the calibration family, so hump/trough orientation is a pure GE object (chord diagnostic 16/20 cells);
the draft is more honest than the memo here. κ† = 0.58 in `baseline_series.csv` (0.59 is a solver-check κ;
0.60 is the argmax on D8's coarser grid — a resolution spread). Mello–Repullo (2004) must be cited and
distinguished. Symbol clash: draft_v2 already uses τ for the discount horizon (δ = e^{−rτ}, l.335). **[V]**

### 4.3 T5 (wedge) — proved, but the Celentano–Levine mapping is off-calibration
λ = 1 − r(1−γ)ψ, the A3 boundary and `prop:d7-afs` are proved (D7 + JSON, MC-checked). But
`lambda_crit_numeric` = 0.07 while the calibration λ = 0.861, and D7 targets the reversal at AFS, not C&L. C&L's
−13.7% is a selection-corrected treatment effect; M(π) is a cross-sectional ratio at fixed cutoffs. Either move
the calibration or drop "rationalizes". **[V]**

---

## 5. Empirical design (Section 4 of the memo)

**Verdict: a well-read plan, not committed empirics.** Findings, all executed against the disk data unless
marked [F]:

| # | Finding | Severity | Evidence | Fix applied |
|---|---|---|---|---|
| E1 | **No break in the outcome at the rule date.** Half-year median CAR (WRDS output, market model): 2022H1 4.4%, 2022H2 3.0%, 2023H1 1.7%, 2023H2 0.4%, **2024H1 1.0%**, 2024H2 6.0%, 2025H1 2.8%, 2025H2 0.8%. The memo's "1.6% → 2.6%" comes from 2024H2 (outside the memo's own main post window, straddling the 13G change) and from a **21-day** CAR window (`nrets`=21), not [−1,+1]; max post CAR 28.99 (2,899%). [V] | MAJOR | `wrds_evtstudy_edate.csv` | F3 rewritten as a signed prediction with its confound; the no-break fact stated; re-run on [−1,+1] required. |
| E2 | **H1 is a single-group before/after** with an interaction, not a DiD; 13G filers are not a control (different population, own treatment 2024-09-30); "non-activist 13D filers" are treated too. [V] | MAJOR | memo l.249–275 | Renamed; bindingness dose (filer's pre-rule median delay > 5 bd) as the triple-difference; calendar-time coefficient figure; placebo-date randomization inference; MDE stated (≈2.1pp/SD at n≈989 — larger than AFS's whole Amihud loading). |
| E3 | **Bundled confounds missing:** 13D/A deadline → 2 bd; EDGAR cut-off → 10 p.m. ET (same date; shifts event-day alignment mechanically); anticipation (proposed 2022-02-10, adopted 2023-10-10); T+1 sits *inside* the main post window; macro/M&A cycle. [V] | MAJOR | SEC Rel. 33-11253; `fact2_parsed.jsonl` has `accepted_after_4pm` | Full confound table; donut Oct-2023→Feb-2024; event day = first session after acceptance. |
| E4 | **Sample arithmetic:** the memo's own windows give ≈990 events in the WRDS output (301 post, 7 month-clusters; 1,226 post-window filings), not 9,234; F1 rests on 188 parsed filings (parse rate 0.68/0.64), Manski bounds [−7.9pp, +60.1pp] overlap; but F1 replicates on the full universe with a clean pre-trend (share ≤5 bd: 2022 31.9%, 2023 35.7%, 2024 70.6%; medians 7/7/5). [V] | MAJOR | `fact2_parsed.jsonl`, `fact1_summary.csv` | F1 restated with the universe numbers, parse rates, bounds, holiday calendar, bunching-at-5 framing. |
| E5 | **H2 ratio ρ ill-defined** (denominator negative for ~40% of events); windows filing- vs event-anchored inconsistently; CDF's 7% is a (−60,−1) run-up from the 2012 NBER WP (2001–2010), not a 9-day window — and the published JF 2015 (1994–2010) reports ≈3% run-up / ≈2.5% jump. [V] | MAJOR | `cdf_fos_jf2015.txt` l.431; JF 70(4) | Replaced by a stacked-window levels DiD (run-up / crossing→filing / jump), event-date anchored; benchmark corrected. |
| E6 | **H3** underpowered (~60/cell → t≈1.25 for an 8pp hump), joint hypothesis is intersection–union not Wald, conditions on the bid outcome, currency-vs-inference channels not separated. [F, arithmetic reproduced] | MAJOR | — | Demoted to "prediction the theory offers" with the design (terciles/quadratic + Lind–Mehlum, Schwert −42 with SDC-convention robustness, cash/stock split, P(bid\|q) reported); no promised numbers. |
| E7 | **Parser bugs:** `pct_of_class` regex cannot match 3-digit percentages (100.0% → 0.0), takes the first reporting person's row; 438 rows at exactly 2.59%, 307 at 0.0, 22.9% below 5%; `np.busday_count` ignores federal holidays. [V] | MAJOR | `parse_13d.py` l.105–106; `facts.py` l.65–70 | F2 flagged as not executable until fixed; the stake-at-filing test added as the sharpest post-rule prediction. |
| E8 | **Calibration table:** 4 of 10 rows have no model counterpart (run-up, stake, accumulation share, staged costs); "+7.7pp" should be "+7.7% (relative)"; Norli 0.33→0.73 is the baseline probit; Boyson "70%" wrong (>1/3; 22%); G&S 18.1% is unconditional vs Boyson's conditional object; Gantchev's stage order is negotiate $2.9M → board $1.8M → proxy $5.9M. [V] | MAJOR/MINOR | primary texts | Table split into targeted / signs / motivating panels with a model-object column; numbers corrected. |
| E9 | Amihud shown as a single-day formula; should be a pre-event [−250,−11] average, log-winsorized, with size controls. [F] | MINOR | — | Definition replaced. |
| E10 | "~3–4 days of work" for H1/H2 is optimistic by a factor of several once parser fixes, event-day realignment, dose construction and placebo inference are counted. [F] | NOTE | — | Estimate revised. |

---

## 6. Facts and citations — corrections table

| Item (memo line) | Was | Should be | Source |
|---|---|---|---|
| Boyson et al. (l.239) | "70% within 2 years" | "over one-third of activist targets receive a bid within 2 years; 22% for the risk-arbitrage-excluded 'activism merger' measure" (Boyson, Gantchev & Shivdasani, JFE 126, 2017) | paper text (grep: no "70") |
| C&L takeover-probability lift (l.329) | "+7.7pp" | "+7.7% (relative)" | celentano_levine_2025.txt l.71–78 |
| Norli et al. (l.325) | "0.33% → 0.73% (IV)" | baseline probit (fn.12, Table 3); IV described only as "somewhat larger" | norli2015.txt l.557–627 |
| CDF run-up (l.288–290, l.322) | "~7% vs ~3% on 2001–2010", cited to CDF 2015, used as if a 9-day window | The 7%/3% are the **2012 NBER WP** (18452, 2001–2010) numbers over (−60,−1); the **published JF 2015** (1994–2010) reports run-up ≈3% and a two-day jump ≈2.5% | cdf_fos_jf2015.txt l.425–432; JF 70(4) doi 10.1111/jofi.12260 [V] |
| κ† (l.201) | ≈0.59 | ≈0.58 (full-equilibrium argmax, 0.0206 grid); 0.60 on D8's coarser 0.025 grid — a grid-resolution spread, not a "channel-(A) peak" (the JSON's chanA argmax is the grid edge 0.30) | baseline_series.csv; d8 JSON [V] |
| F1 n (l.231) | "n = 300" | 300 sampled; 188 with a parsed delay (98/90); parse rates 0.68/0.64 | fact1_summary.csv |
| Sample (l.262) | "9,234 parsed" | 9,234 filings; 4,638 with event dates; ≈990 in the main-spec windows (301 post) | fact2_parsed.jsonl, WRDS output [V] |
| Greenwood–Schor (l.238, 329) | 18.1% and +11pp used interchangeably | 18.1% = raw 12-m acquisition rate; +11pp = vs 7.2% matched controls (12.6% non-activist 13D) | greenwood_schor_2009.txt |
| Ben-David et al. (l.225) | three authors implied | Ben-David, Bhattacharya, Huang & Jacobsen, JF 81:1263–1320 (2026) | Wiley |
| D7 symbols (l.113–117) | φ floor, q entry prob., ψ dilution | ϕ dilution (φ = normal density in D7), ψ pivotality, r fringe-raid probability, γ portability | D7 tex l.73 |
| Massa–Xu "public bidders"; HMN "−4.5pp" (l.310–311) | stated as fact | direction/venue verified; the sub-sample qualifier and exact coefficient not verified from the PDFs | A5 partial UNCHECKED |
| SEC dates (l.52–55, 269–273) | — | all six dates confirmed (SEC press release 2023-219 via browser + law-firm memos) | — |

---

## 7. Prioritized action list

**Applied to the memo in this round (see diff vs `quality_reports/rewrites/framework_v3_pre-review_2026-08-19.qmd`):**
all §1 restatements; τ split into τ_θ/τ_w with the Back-et-al. κ-mapping; T2 restated honestly with the
numeric evidence and the disclosure-jump object; existence assumption list; T3/GE labelled to-do; T4 with
`rem:d5-vacuous`, κ†=0.58, Mello–Repullo; T5 λ_crit caveat; §4 rewritten per E1–E10 (F1 universe numbers,
F2 parser gate, F3 as signed prediction with the no-break fact, H1 before/after + dose, H2 stacked levels,
H3 demoted, Amihud definition, confound table, calibration panels); numbers corrected; competitor paragraph;
risk register and execution sequence updated; notation block; changelog.

**For the author, before theory surgery:**
1. Decide which margin τ is the paper's object (τ_θ threshold vs τ_w window) and derive the sign of ∂_κ of the
   *disclosure jump* under each — this determines whether H1 tests T2 at all.
2. Resolve the (A5) contradiction (draft l.696 vs l.1010) and δ (0.95 vs 1); re-solve the three-branch model
   (π̄ ≡ 1) before re-quoting any D8 number.
3. Re-anchor the calibration so ω_P (disclosed share of engagement) is empirically meaningful; report the
   attenuation elasticity, not just the sign; decide whether to move λ below λ_crit or drop the C&L sentence.
4. Empirics: fix the two parsers; realign event days on acceptance time; build the bindingness dose; produce the
   calendar-time slope figure first; then decide whether H1 is a signed result or a bounded null.
5. Add to `bibliography.bib`: Burkart–Lee 2022; Kyle–Vila 1991; Mello–Repullo 2004; Cetemen et al. 2026 (present);
   Bebchuk–Brav–Jackson–Jiang 2013; Massa–Xu 2013; Huang–Maharjan–Nanda 2024; Trivedi 2026; Polk et al. 2024;
   Corum 2025; Bishop–Fos–Jiang–Partnoy 2026; Meles et al. 2026 (reverse causality of activism → liquidity).

**Verification outcome (Stage B):** B1 (theory): 14 confirmed / 1 miscited (κ† label) / 0 wrong; B2
(lit/novelty/empirics/facts): 18 confirmed / 2 miscited (post-window count 1,226 vs 1,381; spike at 2.59
not 2.6) / 1 wrong (the JF-2015 sample-year guess) / 0 unchecked; no finding refuted on substance.
B3 (consistency of the revised memo v3.1 against verified sources): 49/55 sub-facts matched; the 4
mismatches (Back et al. page 1452–1453 for the σ²T quote; ϕ vs φ for dilution; draft l.1010 not 1009; one
paraphrase shown as a quote) were fixed before rendering; one item (the k_D total-variation series) is the
orchestrator's own executed check, endpoints reproduced by B1.

**Open / unchecked after this round:** Kahn–Winton (1998) as a C2 counterexample (image-only PDF); Massa–Xu
public-bidder qualifier and HMN's exact −4.5pp (PDFs not opened); Burkart–Lee–Voss publication status; whether
Kakhbod et al./CGS close with measurement sections; the JF-2015 sample years for CDF; arXiv q-fin unswept.
