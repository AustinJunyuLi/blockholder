# draft_v3_trace.md — the trace sidecar for draft_v3

Assembled 2026-08-29 against the frozen theory record: **MODEL_CARD.md version stamp
2026-08-30 (F5 route R40-A applied + batched two-pass gate PASS + theory-record freeze;
commit 65b8db3)**. The card is the single source of truth for every labelled claim; the
draft claims nothing the card or a named file does not carry. This file maps, section by
section, each proposition / remark / estimate / figure in `draft_v3.tex` to its card row
or named source file (with line anchors where they are stable). Honesty labels take the
paper forms agreed for the December package:

- PROVED → numbered Proposition / Lemma / Theorem with a **Status** line carrying
  "(proved under the stated hypotheses; the hypotheses are assumptions about the
  equilibrium object, and the applicability discussion records where the implemented
  calibration satisfies or fails them)".
- NUMERICAL → "Remark (verified on the numerical grid)".
- ESTIMATED → estimate with standard error (only Trivedi's +0.348 / SE 0.130, quoted as
  someone else's estimate; the draft's own empirics are descriptives with no SEs claimed).
- CONJECTURE → omitted. Nothing in the draft is labelled a conjecture, and no claim was
  promoted above its card label.

Intermediate vehicle: the paper-voice statements and proofs in `sections_v3/`
(`model_section.tex`, `theorem_section.tex`, `proofs_core_lemmas.tex`,
`proofs_existence.tex`, `proofs_theorem_ge.tex`), which were themselves transcribed from
the card and the `research/model_v4/proofs/*.md` files. draft_v3 adapts them (reorganised
into §3 model / §4 existence / §5 outcomes; process metadata stripped; connective prose
rewritten); no statement was strengthened, weakened, or re-scoped.

---

## 1. Section-by-section map

### Front matter and §1 Introduction (`sec:intro`)

| Draft content | Source |
|---|---|
| Abstract: partition identity, two-round model, three results with conditionality, Feb-2024 anchor, the E1 filing-delay descriptive (median 6→5 bd; share within 5bd 38.9→67.1%, +28.2pp, no control group, no causal effect claimed) | MODEL_CARD §1 (position/object); result rows P1/T1/C1; HANDOFF_sign.md §8.1; `empirics/output/e1_estimate.json` (per_period medians/shares, difference_complete_case, `causal_claim: false`); `research/empirics_v4/e1_spec.md` (claim boundary) |
| 13D rule facts: 5% since 1968, 10 calendar days → 5 business days effective 2024-02-05 | `research/cards/_institutional_sec_33_11253.md`; `research/lit_institutional-facts.md` §1.1–1.3; \cite{SEC2023} |
| Threshold vs window margins as separate policy coordinates; UK 3% contrast | CONTEXT.md (threshold margin, window margin); lit_institutional-facts §4 (UK DTR 5) |
| "Existence" paragraph (conditional; A6/A3 measured to fail; 23/27 nodes converge) | Card P1 row (label + numerical status); §5 A6 note, §5 A3 note; §9 item 4 |
| "Attenuation" paragraph (S = (1−Ω)S_P; threshold unconditional; window iff W_T C_T ≤ 1, C_T unsigned) | Card T1 row (A)/(B)/(C) verbatim content |
| "From fixed policies to equilibrium" paragraph (region as named hypothesis; 18/80 nodes) | Card C1 row (PROVED + NUMERICAL node evidence) |
| Window record numbers 18–77%; composition leg carries; weight leg 3–14% shave | HANDOFF_sign.md §8.1 (t2_t1_check block 4 + H=12 robustness) |
| A(τ) failure numbers (23–767 values, 180 non-degenerate nodes) | Card §5 A(τ) evidence note (ticket 33; t2_atau_support_check) |
| Delay-compression facts (median 6→5 bd; share within 5bd 38.9→67.1%; +28.2pp, 95% cluster-bootstrap interval 21.8–34.8; descriptive, no control group; the pre-specified design for the market/takeover implications executed August 2026, viewed, preserved exactly as viewed in the online appendix, not the headline) | `empirics/output/e1_estimate.json` (per_period, difference_complete_case, inference); `draft_v3_onlineappendix.tex` §app:honesty (the viewed record, quoted from 9b98089) — see §6 below |
| "No paper combines the two margins, liquidity, and a control outcome" | competitor_map.md Part 3 (W1–W6) and Sweep summary ("none found") |
| Classics one-parameter answers; Maug's disclosure remark | lit_classic-exit-voice.md §A (cross-strand synthesis), Maug card §"Institutional facts" (p. 73) |
| Back-et-al isomorphism quote; CCKV pre-disclosure window; Kyle–Vila boundary | competitor_map Part 1 rows 5, 3; W3 refuter list (Kyle–Vila p. 54 n.1) |

### §2 Institutional setting and related literature (`sec:lit`)

| Draft content | Source |
|---|---|
| §2.1 Williams Act, 13D/13G split, 2022-02-10 proposal / 2023-10-10 adoption / 2024-02-05 effective / 2024-09-30 13G / 13D/A 2bd; UK 3%+1% rungs 2 trading days; EU ladder 4 trading days | lit_institutional-facts.md §1 (esp. §1.3 date confirmations), §4, §5.1; `research/cards/_institutional_sec_33_11253.md` (dates checked against the release text); \cite{SEC2022,SEC2023} |
| Window as "legal deadline attached to a partition, not a random horizon" | competitor_map W5 (random-horizon hazard 4) |
| Pooled state "pooled for the price-setting market"; Zeng leakiness; run-up begins on trigger date | competitor_map W3 sweep check; Zeng card (p. 1310 Q5, p. 1312 fn. 13) |
| BBJJ bunching 45.3% in 8–10bd bucket, ~20% on day 10 | `research/cards/bebchuk_brav_jackson_jiang_2013_jcl.md` R1–R2 (Table 2, p. 10); competitor_map Part 2 item 8 |
| §2.2 classics paragraph (Maug reversal; KW sign; FG complements; AP exit threat; EFZ; Norli) | lit_classic-exit-voice.md §§1–4 + §A; lit_liquidity-premia-empirics.md |
| "None of the four has a bidder, an offer, or a premium" | lit_classic-exit-voice.md §A ("Our paper's core objects … unclaimed") |
| §2.3 positioning: Kyle–Vila (disclaim disclosure; mixing split un-keyed), CDF 2015/2016 (presence common knowledge), Back et al. (σ²T isomorphism p. 1453; no acquirer/premium; endogenous horizon out of scope), CCKV (game inside unmodelled window), Corum 2025 (threshold/window fused, no counterparty), Corum–Levit (threshold occupied but sterile; flagged state off path), OCB (threshold as cap; interaction asserted not proved), Burkart–Lee (hand over the toehold) | competitor_map Part 1 rows + Part 2 hazards 2/3/11/14 + W1/W3/W4/W5 refuter lists, page-cited |
| §2.4 structural set (Gantchev; Johnson–Swem one-move filing; AFS liquidity-as-control, no control outcome; Celentano–Levine 5% calibration constant, window absent); BJPT/GS acquisition facts; Becht international returns | competitor_map Part 1 rows 1–3; lit_activism-empirics.md; lit_disclosure-structural-activism.md |
| Polk et al. (pre-rule only, no SEs, calendar-day mismeasurement 48% at Delta=10) | competitor_map Part 1 row 9 + reading note 9 |
| Trivedi (first stage +0.348 SE 0.130; nulls without MDE; frame never stated; not peer reviewed) | competitor_map Part 1 row 6 + reading note 6; `research/cards/trivedi_2026_ssrn.md` R2 (Table 2, p. 11) |

### §3 The model (`sec:model`)

Adapted from `sections_v3/model_section.tex` (which transcribes the card). Statement
labels are unchanged; the long numerical records for A3/A6 were compressed (numbers kept,
repo paths and process metadata removed) and moved as noted.

| Draft object (label) | Card source |
|---|---|
| §3.1 object/partition, Δ^act, R_d/R/J, margins | Card §1; §4.4 |
| §3.2 timing (two rounds), asm:nofeedback, asm:flagterm | Card §2 (items 2–4, incl. the two load-bearing clauses) |
| def:primitives (v, s, β, ξ, S̄, K, m0, m1, Δ_m, Δ_V, κ ternary noise, τ, T, b0, b̄) | Card §4.1 |
| def:plans (menu, a_j, B_j, b*_j, c_j, f_j, D_j, B^F, Q^F, Γ, X_d) | Card §4.2 |
| def:prices (H^P_d, F, S_F, I_H fill, cells, π, eq:entry, eq:Y, inner fixed point, P^P_{-1}, P_ND, R_d/R/J) | Card §4.3 (incl. the two conventions and their audit provenance) |
| def:U (eq:Uj, plan-locality, integrability) + rem:Ctiming | Card §4.3 U_j row; P1 row's timing-convention clause |
| asm:TR (TR-i…TR-iv, eq:m0 with the m0≥0 theorem sentence) | Card §4.1 m0 row; §5 A5 note (ticket 27); §4.2/4.3 table restrictions |
| def:cpbe (six requirements; weak inequalities; Brouwer on Θ; uniqueness not claimed) | Card §3 |
| asm:A1, asm:A2p (+ integrability rationale) | Card §5 A1, A2′ |
| asm:A3 + rem:A3record (two loci: three sign changes 1.5754434/1.5833333/1.5902426; excursions 2.4–2.8e-4; H,V,H,V; locus (ii) reversal at 1.659062163; n(s) route; ticket-34 account swept at all four; family-robustness) | Card §5 A3 + its evidence note (2026-08-27, 2026-08-28 sweep note, 2026-08-29 off-path scope note, curated t2_a3_ordered_plans_check) — compressed, numbers intact |
| asm:A4 | Card §5 A4 |
| asm:A5 + two-continuities paragraph (m0≥0 theorem; counterexamples 0/3 roots; clause (ii) fails with A6 at one locus; no result consumes the cutoff clause) | Card §5 A5 note (ticket 27; 2026-08-28 re-review audit finding 1) — compressed |
| asm:A6 + rem:A6record (k-dependence through pooled prices; cell-edge hyperplanes ∪ sole-generator collapse faces; weight ≥ min(κ/2,1−κ)^{d+1}; refuted vanishing-mass defusal; Hold-collapse face 4.441e-16 clean; T2 jumps 6.33e-3/1.09e-2/2.83e-2 at baseline, 0.16 at κ=0.15; chamber Θ+ exhibited, none at κ=0.15 node; 23/27 converge; hard-switch finding; repair identified not executed) | Card §5 A6 note (2026-08-27 panel; 2026-08-28 curation; 2026-08-29 off-path verification note) — compressed, every number intact |
| asm:A7 / asm:A7p / asm:A7J + satisfiability paragraph (pro-rata single-Voice menu; 40-collision executed check; failure boundary; burden moves to IC) | Card §5 A7 block + ticket-24 note (A7_construction.md, A7_attack_verdict.md) |
| asm:A8 | Card §5 A8 |
| asm:Atau (eq:atau; clauses τ-i, τ-ii) + "where the bite sits" paragraph | Card §5 A(τ) (incl. L3's bite finding: derivative pattern equivalent to mass/moment invariance; support is the whole content; one-round satisfies, no-disclosure does not; two-round OPEN) |
| asm:Abr (br-i…br-v) + sharpening paragraph (ρ := ½A_{1/2}+A_1; br-iii weakest) | Card §5 A(br) |
| asm:AGE | Card §5 AGE |
| def:theta (Θ, T, L_R, r_τ/r_T, eq:gPE, eq:BGE, R_r, η_r) | Card §4.5 |
| def:premium (h, eq:Dact, M_F/M_P, Ω = Pr(a=1)ω_a, π̄ upper support point vs mean, S/S_P, eq:chord, W/C ratios, margin subscript) | Card §4.4 |
| Degenerate π̄-as-mean exclusion sentence | Card §4.4 π̄ row (binding 2026-08-21 ruling) |

### §4 Equilibrium existence (`sec:existence`)

| Draft object | Source |
|---|---|
| Intro sentence (proposition not theorem; hypothesis enumeration rationale; "one verification episode … form of one hypothesis") | theorem_section.tex preamble; card P1 row's 2026-08-23 demotion record (A7′ vs A7-J mismatch) |
| Proposition 1 = P1 statement: (P-1)–(P-13); conclusion (i)–(v); "A5 is not assumed" paragraph; "A6 is read" paragraph incl. the bracket half and common bracket [s_lo, s_hi]; A8 addendum with H-ord + upper-set engagement flag; uniqueness not claimed | Card §6 P1 row, verbatim content (amended statement incl. 2026-08-30 re-derivation changes 1–2), via theorem_section.tex prop:P1. Footnote on the form mismatch = P1 row's demotion history, paper-voiced |
| Status line (paper form of PROVED, conditional) | Card P1 label + the agreed paper form |
| Proof sketch (Parts A–F) | `research/model_v4/proofs/P1_proof.md` Part A–F structure; proofs_existence.tex opening paragraph + closing "Scope of the conclusion" (six disclaimers) |
| rem:P1record — the single applicability remark, plain words: A6 continuity + A3 fail at the implemented calibration; "the proof needs the outer map continuous and single-valued, and it has measured jumps and stretches where no weakly increasing selection exists"; A(τ) pattern; nonexistence neither claimed nor shown; 23/27 converge; four unresolved nodes (κ∈{0.15,0.85}×(τ,T)∈{(0.05,5),(0.075,1)}), 30 seeds, residuals 1e-4–1e-3 vs 1e-9 | Card P1 row (numerical status clause); §5 A6/A3 notes; §9 item 4. Stated **once**, as instructed |
| Appendix B proof (full) | proofs_existence.tex → P1_proof.md (Steps 1–20, Parts A–F; h.1–h.17 ↔ (P-1)–(P-13) map in the file header). One adaptation: Step 18's "Card note, 2026-08-29" withdrawal rewritten in paper form (Kakutani conclusion unestablished; convex values/closed graph need a lemma not supplied; remark outside the claim) — substance unchanged, repair numbers and repo paths removed |

### §5 Liquidity and control outcomes (`sec:outcomes`)

| Draft object | Source |
|---|---|
| Lemma 1 = D1 (measurable D; clock equivalence; eq:runup-jump) + Status | Card §6 D1 row (via theorem_section lem:D1) |
| Lemma 2 = L1 (eq:L1; degenerate cases undefined-rather-than-imputed) + Status | Card §6 L1 row |
| Lemma 3 = L2 (flagged tuple ⇒ conditional independence ⇒ M_F κ-invariant) + Status | Card §6 L2 row |
| Lemma 4 = L3 (∂_κE[h] = A'_κ C_h; MVT identity; o(π̄²); "if" never "iff") + Status (PROVED under A(τ)) | Card §6 L3 row |
| rem:AtauRecord — the A(τ) numerical record: 200 nodes, 4,194,304 paths, gates (0.0 / 1.7e-16), 20 degenerate, 180/180 fail; support 23–767 values never 3; no mass at π̄/2; 0.57–91.8% off-support, 13.9% median node; Hausdorff 0.4608 vs <1e-12 at 0/18; A0'=A1' fails 0/180; chord residual up to 7.17pp; π̄=1 to 1.5e-13 half holds; 6 distinct pooled cells caveat; domain question | Card §5 A(τ) evidence note (ticket 33, t2_atau_support_check.py/.json), compressed with every number intact |
| Lemma 5 = L4 (leg 1 nesting; leg 2 share falls; leg 3 under A(br)) + Status | Card §6 L4 row |
| Theorem 1 = T1 ((A) factorisation; (B) W_τ C_τ ≤ 1; (C) iff W_T C_T ≤ 1; hypotheses (T-1)–(T-15); "no unconditional window sign") + Status | Card §6 T1 row, verbatim |
| Post-theorem discussion (weight effect exact form; two margins' different status; Feb-2024 lands on the unsigned margin) | T1 row; CONTEXT.md (weight/composition effect) |
| rem:T1record — window record (verified on the grid): Table 1 W_T/C_T/W_T·C_T at five τ quantiles (0.1818/0.1818/0.2055/0.4299/0.7724; legs 0.8559–0.9730 and 0.2124–0.7939); calibration k=(1.240576,1.531022), Ω=13.84%, ω_a=61.15%, M_F=0.553pp, M_P=0.223pp; H=12 column (0.1099/0.1099/0.2406/0.5772/1.0000, τ-ladder note); threshold margin 0/8 pairs, mass-reclassifying 0.5566/0.4780/0.8846; factorisation wiring (2.06e-16); L2 exact invariance (pooled M_P moves 0.0722pp; J moves 5,090bp); corner caveat Ω(T=10)=6.81e-4; "node evidence, not a sign" | HANDOFF_sign.md §8.1–8.2 (t2_t1_check blocks 1–4 + H12 robustness; t2_l2_check), which is the card T1 row's numerical record |
| Disclosure-regime paragraph + Figure 1 (fig_disclosure.pdf): ratios 1.064/1.184/1.136/0.378 at Ω=0.037/0.129/0.286/0.50; crossing Ω*=0.343; "regime comparison, not a window test; composition factor can exceed one" | Card §9 item 3 (O-1) + HANDOFF_sign.md §1–§3 (t1_o1_rerun_check); figure = `numerical_output/fig_disclosure.pdf` plotting `numerical_output/data/disclosure_attenuation.csv` (the O-1 object at baseline). Card row exists ⇒ figure included |
| Proposition 2 = C1 ((C-1)–(C-7); eq:C1; unused hypotheses named) + Status | Card §6 C1 row, verbatim |
| rem:C1record — 18/80 nodes; block T=5, τ-pct {50,70,90}, κ∈{0.65,0.75,0.85}; η_r min 0.0595 median 0.3467; L_R∈[0.264,0.501]; re-run reproduces; nodes verify pointwise inequalities only; not a fifth category; retired aspiration; B^GE_r = O((1−L_R)^{-3}) | Card §6 C1 row (numerical node evidence) + §7 (labels/dominance-and-contraction node definition) |
| §5.6 What is not claimed + three open questions | Card §9 (verbatim list + items 1–4, with item 4's scoped remainder) |
| Appendix A proofs (D1, L1, L2, L3, L4, full) | proofs_core_lemmas.tex → proofs/{L3,L4}_proof.md and threads/turn-1 answers, per card rows |
| Appendix C proofs (T1, C1, full; incl. the interleaved "Scope of the argument" note on T-15 and the A(τ) conditionality restatement) | proofs_theorem_ge.tex → proofs/T1_proof.md (fix round closed), proofs/C1_proof.md + rederive/C1_rederivation.md (N1, N2) |

### §6 Empirics (`sec:empirics`)

Rebuilt 2026-09-01 (section rewrite commit 0e1e5e2). The section is now "Did the clock move?
Filing-delay evidence": one registered exercise, E1, descriptive, every number drawn from the
run's result record. The earlier map of this section — the seeded n=98/90 Fact-1 sample and the
prospective seven-leg specification — cited artifacts deleted from the live tree on 2026-09-01
(deletion commit 235de22); that design survives only as the viewed record quoted in
`draft_v3_onlineappendix.tex` §app:honesty from history at 9b98089 (appendix section added in
1243cd4). The registered specification is `research/empirics_v4/e1_spec.md` (four dated
amendments, all 2026-09-01); the single result authority is `empirics/output/e1_estimate.json`.

| Draft content | Source |
|---|---|
| §6 opening: one exercise, descriptive; E1's question (did the realised trigger-to-filing delay fall after the window moved from ten calendar days to five business days on 2024-02-05); no control group, no effect identified on liquidity/returns/activism/bidder entry/premia/control, tests neither the invariance result nor the attenuation theorem; registered before the run; every number from the run's result record | `research/empirics_v4/e1_spec.md` (Question; Claim boundary; registration note); `empirics/output/e1_estimate.json` (`label: "descriptive"`, `causal_claim: false`, `spec` path) |
| §6.1 Protocol and population (sec:e1protocol): both EDGAR spellings taken, both amendment spellings excluded, enumeration collapses on accession; 616 pre (2023Q2–Q3) / 521 post (2024Q3–Q4), the near-census, not a sample; the campaign unit (subject firm, trigger date), earliest accession for simultaneous group filings; 461/435 eligible, 450/432 resolved, 14 unresolved (11 pre, 3 post) carried through the bounds; trigger = "Date of Event Which Requires Filing" (structured XML tag first, cover-page text second); filing = EDGAR acceptance timestamp, 17:30 ET roll to the next business day; federal business days; cluster bootstrap on the subject firm, 2,000 draws, seed 20260901, 95% percentile interval; complete-case with worst-case bounds; G1/G2/G3 registered as binding, all pass | e1_spec.md (Population with the first and second dated amendments; Unit; Measurement; Inference; Bounds; Gates); e1_estimate.json (enumerated, campaigns, per_period counts, inference block, gates block) |
| §6.2 Table (tab:e1): enumerated 616/521; eligible 461/435; resolved 450/432; unresolved 11/3; median 6 [6, 7] → 5 [5, 5]; share within 5bd 38.9% → 67.1%, worst-case [38.0, 40.3] / [66.7, 67.4]; difference +28.2pp, 95% bootstrap [+21.8, +34.8], worst-case [+26.3, +29.4]; caption's "Descriptive; no control group; no causal claim" | `empirics/output/e1_estimate.json` — the single result authority (per_period, difference_complete_case, inference, G1_worst_case_bound); row-level record `empirics/output/e1_delays.csv` (1,137 rows, status + reason on every row) |
| §6.2 Figure (fig:e1cdf): empirical CDF pre (450) vs post (432), dashed line at the five-business-day deadline; resolved campaigns only; no outcome screen, so the right tail stays visible | `empirics/output/e1_cdf.pdf` (on file), plotted from `empirics/output/e1_delays.csv` per e1_spec.md Outputs |
| §6.2 two readings: the compression is real and large (median bounds [6, 7] vs [5, 5] do not overlap; G1's lower bound clears zero); agreement in kind with the Commission's arithmetic (≈29% of 2022's initial filings already inside the amended deadline vs 38.9% here; earlier filing expected for ≈59% of timely 13D reports; "different samples and windows, the same direction"); BBJJ deadline-bucket mass (45.3% at 8–10bd, 16.5% inside 3bd, 7.1% beyond 15bd); Polk calendar-day misclassification (48% at their day-ten marker) | e1_estimate.json (medians, shares, bounds, G1 verdict); Release 33-11253 pp. 178, 193 via `research/cards/_institutional_sec_33_11253.md` §4.1; \cite{SEC2023}; `research/cards/bebchuk_brav_jackson_jiang_2013_jcl.md` R1 (Table 2, p. 10); competitor_map Part 1 row 9 + reading note 9 (Polk) |
| §6.3 The denominator and the audit (sec:e1audit): G2 differential coverage (unresolved 2.4% pre vs 0.7% post; gap 1.7pp against the registered 10pp cap); G3 blind hand-audit (60 filings, 20 per non-empty period-by-route stratum — pre-text, post-text, post-xml; the blind enforced by commit order; 0 of 60 disagreements against the registered threshold of 3; the 20 xml-route excerpts read LABEL NOT FOUND and were coded from the dateOfEvent element); three data-quality items stated rather than absorbed (14 unresolved, 3 of them Sageworth self-CIK rows; 10 of 521 post filings declaring a non-zero amendment number in the body, population stays as registered; no outcome screen) | e1_estimate.json gates block (G2 values, G3 verdict); e1_spec.md third and fourth dated amendments (stratum allocation; LABEL NOT FOUND; the amendment-number scan); e1_delays.csv (status/reason codes); audit sample `empirics/output/e1_audit_cases.csv` |
| §6.4 The viewed pre-specified record (sec:e1record): the seven-leg pre-specification (run-up/jump timing split, bindingness dose, stake at filing, bounded null from the Commission's tables, matched DiD on the bid hazard, bidder entry by liquidity, referee checklist) executed in August 2026 and viewed; preserved exactly as viewed in the online appendix; not the headline; no estimate in it cited as evidence in the main text | `draft_v3_onlineappendix.tex` §app:honesty ("The August 2026 empirical record, exactly as viewed"), quoting the record deleted from the live tree on 2026-09-01 (deletion commit 235de22) and preserved in history at 9b98089 |
| §6.5 The headline (sec:e1headline): the choice the earlier draft left pending is made — the filing-delay result of tab:e1; descriptive; establishes that the statutory clock moved in practice, nothing about returns/activism/bidder entry/premia; the candidates requiring return or takeover estimates retired with the viewed August record | e1_estimate.json (`headline_suppressed: false` — the registered gates passed, so the registered headline runs; the tab:e1 block); retired candidates preserved at §app:honesty (9b98089 provenance) |
| Independent reproduction | `quality_reports/verification/2026-09-01_e1_reproduction_verify.md` (fresh-session clean-clone rerun at 1f23867: e1_delays.csv bit-identical; e1_estimate.json identical outside the G3 block, whose `NOT RUN` rerun state is the expected consequence of not re-scoring the hand audit; test_e1.py 13/13, test_parse_13d.py 11/11) |

### §7 Conclusion (`sec:conclusion`)

No new claims. Restates: the identity (card §1); the three results and their conditionality
(card rows); the window record + A(τ) failure "in the same section because they are both
true" (HANDOFF §8 + ticket 33); the E1 filing-delay descriptive (median 6→5 bd; share
38.9→67.1%; +28.2pp with its bootstrap interval; worst-case bounds and the registered gates;
no control group, no causal claim — `empirics/output/e1_estimate.json`) and the preservation
sentence for the viewed August record (`draft_v3_onlineappendix.tex` §app:honesty, quoted
from 9b98089); three open questions (card §9 items 1–2 + A6 scoped remainder + the ω_a
anchor absence from HANDOFF §6).

### Appendices

Covered in §4/§5 rows above (Appendix A = D1–L4; Appendix B = P1, with the Step-18
adaptation noted; Appendix C = T1 + C1).

---

## 2. Figures: included vs dropped

**Included (2).**

1. `numerical_output/fig_disclosure.pdf` (Figure 1) — the O-1 disclosure-regime
   comparison at baseline. Card row: §9 item 3 (O-1) with the four ratios and Ω*;
   HANDOFF §1–§3. Plots `numerical_output/data/disclosure_attenuation.csv`.
2. `empirics/output/e1_cdf.pdf` (Figure 2, `fig:e1cdf` in §6.2) — the E1 empirical CDF of
   the trigger-to-filing delay, pre vs post, resolved campaigns. Source: the row-level record
   `empirics/output/e1_delays.csv`; the Outputs row of `research/empirics_v4/e1_spec.md`.

**Dropped (14), each for lack of a card row.** The 15 files in `numerical_output/` are
the one-round (draft_v2-era) numerical layer; the card's numerical records for the v4
model live in the executed t2_* checks (quoted as text/tables, not figures). Per the
assembly rule ("if a figure lacks a card row, drop it rather than argue for it"):

`fig_cutoff_structure.pdf`, `fig_cutoffs_kappa.pdf` (one-round cutoff objects; no card
row), `fig_nonmonotone.pdf` (the hump — card §9 explicitly does not claim it survives),
`fig_decomposition.pdf` (one-round base+activism minority-gains decomposition; object
not in the v4 card), `fig_prices.pdf` (one-round static prices), `fig_sensitivity_C0 /
_delta / _rho / _sigma_xi / _wedge.pdf` (one-round Δ^min sensitivity panels), 
`fig_noisy_rumor_precision.pdf` (one-round extension), `fig_welfare.pdf` (welfare —
card §9: not claimed), `fig_ge_decomposition.pdf` (one-round D8-era GE decomposition;
cited in the card only as the template pattern, no row), `fig_wedge_primitives.pdf`
(D7 tender-game λ — not in the v4 card). The v4 numerical evidence the card does carry
(t2_t1_check, t2_l2_check, t2_c1_region_check, t2_atau_support_check) has no figure
files; it enters the draft as Table 1 and the three numerical remarks.

## 3. Sentences/claims removed for lack of a row (count: 9 claim blocks)

Nothing in draft_v2's architecture was carried into draft_v3 without a v4 card row. The
removed material, enumerated:

1. The hump / non-monotone minority-gains result (draft_v2 R1) and its figure — card §9
   disclaims survival.
2. The welfare section and the κ-planner / threshold-planner analysis — card §9:
   welfare and optimal rule design not claimed.
3. The D7 tender-game microfoundation of the premium wedge (λ appropriability,
   \hat\lambda = 1−q(1−γ)ψ, the AFS reconciliation proposition) and
   `fig_wedge_primitives.pdf` — λ/ψ are D7 objects; the v4 card's Δ_m is a primitive,
   and no v4 row carries λ.
4. The noisy-rumor / intermediate-regime extension and its figure — one-round
   extension, no v4 row.
5. draft_v2's four-action dominance lemma (engaged exit / silent buy) — a one-round
   menu statement; the v4 card's menu is Def 4.2 and carries no such row.
6. draft_v2's posterior / price-decomposition propositions (π(X,D) closed forms,
   "activism premium" split) — one-round objects; the v4 analogues are D1/L1/L2.
7. draft_v2's cutoff-equation derivations and boundedness/self-map lemmas — superseded
   by the v4 polytope and P1; no v4 rows.
8. The one-round GE transfer material beyond what C1 consumes (the D8 ε-ball pattern is
   referenced in the card's C1 row as a template and appears in rem:C1record as such —
   that sentence is card-sourced).
9. draft_v2's timeline TikZ figure and notation appendix (notation is now Definition
   3.1–3.5 inline; no TikZ per house figure standards).

## 4. Honesty-label crosswalk (label → paper form), as executed

| Card label | Paper form in draft_v3 | Where |
|---|---|---|
| P1 PROVED (conditional) | Proposition 1 + Status "Proved under the stated hypotheses. The hypotheses are assumptions about the equilibrium object, and Remark 4 records where the implemented calibration satisfies or fails them." + the single plain-words applicability remark (rem:P1record) | §4 |
| D1, L1, L2 PROVED | Lemmas 1–3 + Status lines (L2's notes the confirming grid check) | §5.1–5.2 |
| L3 PROVED under A(τ) | Lemma 4 + Status naming the assumption and pointing to rem:AtauRecord | §5.3 |
| L4 legs 1–2 PROVED outright, leg 3 under A(br) | Lemma 5 + Status naming both | §5.3 |
| T1 PROVED at fixed policies | Theorem 1 + Status carrying (B)'s conditionality and (C)'s iff | §5.4 |
| C1 PROVED (region as hypothesis) + NUMERICAL nodes | Proposition 2 + Status + rem:C1record "verified on the numerical grid" | §5.5 |
| A3/A6/A(τ) NUMERICAL applicability evidence | Remarks 2 (rem:A3record), 3 (rem:A6record), 5 (rem:AtauRecord) — labelled as numerical records; "no label moves" stated where the card says it | §3, §5 |
| Window/threshold/L2 records NUMERICAL | rem:T1record "verified on the numerical grid" + Table 1 | §5.4 |
| E1 descriptives (JSON `label: "descriptive"`, `causal_claim: false`) | Table `tab:e1` + Figure `fig:e1cdf`; the caption's "Descriptive; no control group; no causal claim"; worst-case bounds reported beside the complete-case estimates, never instead | §6.1–§6.2 (sec:e1protocol, sec:e1result) |
| Trivedi ESTIMATED | "+0.348 with standard error 0.130" quoted as his estimate | §2.4 (sec:lit-structural) |
| CONJECTURE | none present; nothing promoted | — |

## 5. Notes for Austin

1. **Headline (§6.5, `sec:e1headline`)**: resolved on 2026-09-01. The `[headline choice
   pending]` marker and Candidates A/B/C left the draft with the §6 rebuild; the headline is
   the filing-delay result of Table `tab:e1`, stated descriptively, and the candidates that
   needed return or takeover estimates were retired with the viewed August record preserved
   at §app:honesty (9b98089 provenance). The result authority carries
   `headline_suppressed: false` — the registered gates passed, so the registered headline
   runs.
2. The deleted spec's pre-registered power numbers (1.1–2.3pp timing split; 0.85pp stake;
   4.4pp DiD) are quoted nowhere in the draft; the §6 sentences that carried them left with
   the seven-leg design. Where the design's numbers survive, it is as viewed-record content
   in §app:honesty quoted from 9b98089, never as live sourcing.
3. The two included figures: `fig_disclosure.pdf` is the one with a card row; `e1_cdf.pdf`
   enters under the registered spec's Outputs row (`research/empirics_v4/e1_spec.md`). If a
   v4 figure set is ever rendered from the t2_* checks, Table 1 and the three numerical
   remarks are the natural targets.
4. Nothing in the draft states an empirical value for ω_a (card §9); the conclusion
   names its absence as an open input, per HANDOFF §6.

## 6. Compile gates

`xelatex -interaction=nonstopmode draft_v3.tex && biber draft_v3 && xelatex … && xelatex …`
from the repo root: **0 errors; `grep -in "undefined" draft_v3.log` returns nothing**
(no undefined citations or references); 81 pages; both included graphics found. (Font
warnings acceptable per the gate; none fatal.)

---

## Amendment, 2026-08-30 (fix round after the team review)

This amendment records what the authorized fix round changed in the mapping above. The frozen
record (65b8db3) was not touched; `research/model_v4/**` and `sections_v3/**` were read-only
throughout.

1. **Appendix B source route.** Appendix B was re-transcribed **directly from
   `research/model_v4/proofs/P1_proof.md` at 65b8db3**, not from the intermediate
   `sections_v3/proofs_existence.tex`, whose content predated the R36–R56 wording batch, the
   R40-A substance batch and the gate repair round while its header carried the freeze stamp.
   The mirror is thereby superseded as a source for this draft; its disposition (re-sync or
   stamp stale) is Austin's call under the freeze and is recorded in the team-review brief.
   The re-transcription carried the repaired filing-date stake display, the flagged-family
   dichotomy, the perturbation branches with their n ≥ J restriction, the bracket clause, the
   robust threshold identification, and the A8 endpoint conventions; the ten blocking passages
   in the findings record are cured at source.
2. **Step 18 scope.** As printed, Step 18 is "a possible route, outside the proposition and not
   established here": it defines the best-response correspondence, states what a Kakutani
   argument would additionally need, and draws no conclusion. No step reads it.
3. **D1 repair.** The D1 display in Appendix A uses the filing-date-indexed form; eq:P1-BF no
   longer contradicts its own definition.
4. **Table 2 attrition arithmetic.** The caption now reports the full attrition: 300 sampled,
   198 parsed (102 pre and 96 post, reconciling 0.68 × 150 = 102 and 0.64 × 150 = 96), 10
   screened out by the 0–60 business-day band (4 pre and 6 post), 188 retained (98 pre and 90
   post). The screen is reported as a count per SPEC §2.3. *(Superseded 2026-09-01: Table 2
   (`tab:fact1`) and the seeded 300-filing sample left the draft with the §6 rebuild; the
   current table is `tab:e1` — see the 2026-09-01 amendment below.)*
5. **H=12 chord-route caveat.** rem:T1record now states that the enumerated pooled-support
   object is computationally unavailable at H = 12, so the column's composition ratio C_T is
   obtained from the chord closed form whose support condition A(τ) is measured to fail at this
   calibration, and that the H = 12 column is directional corroboration of the H = 10
   comparison rather than a second independent magnitude. The Table 1 caption carries the weak
   inequality and the reason the 0.9-quantile node returns 1.0000 (the τ ladder stops biting
   and the two flagged weights coincide).
6. **Same-round wording repairs** (detail in
   `quality_reports/session_logs/2026-08-30_draft_v3_minor_ledger.md`): repository
   workflow/register wording removed from the paper voice; the notation map applied
   (ρ_ch(τ) for the main-text chord scalar, 𝔯_ℐ for the Appendix B pricing residual, δ_ϑ for
   the Appendix C parameter radius, Ψ for the Appendix C implicit-function map, Φ reserved for
   the normal c.d.f.); the A5 counterexample-attribution sentence repaired; §5.5 and the
   conclusion now name the same three open questions with ω_a carried separately as an open,
   non-load-bearing input; the MDE basis ("on the post-re-parse projection") stated at the
   stake leg and Candidate B; the Figure 1 caption identifies curves by line style and markers
   and the O-1 prose states that k₁ and k₀ stay at baseline while only k_D moves; the
   conclusion's "only if and only if" is gone; the bib carries the Kyle–Vila, Norli, Becht and
   Bebchuk metadata corrections and the CCKV forthcoming note, and the Trivedi editorial note
   is removed from the References list.
7. **Final compile gates (this round).** Four-pass build (`xelatex` → `biber` → `xelatex` →
   `xelatex`): **0 errors; the undefined grep returns nothing; 86 pages**; both included
   graphics found. 150 labels, no duplicates; 821 refs, none unresolved; 39 citation keys, all
   present in the bib; no curly quotes or Unicode dashes; the 37 em-dash occurrences all sit
   inside formal statement environments; the workflow-register scan is clean outside the
   file's `%`-comment provenance header.

## Amendment, 2026-08-30 (second entry: proof split and deliverable folder)

Austin's directive of 2026-08-30: move the long proofs into an online appendix and place the
deliverables in a `deliverable/` folder. What changed, and what did not:

1. **The split.** `draft_v3.tex` no longer carries its appendices. The three proof sections
   (Proofs of the core lemmas; Proof of Proposition P1; Proofs of Theorem T1 and Proposition
   C1) moved **verbatim** to `draft_v3_onlineappendix.tex`, a standalone document at the repo
   root with its own copy of the preamble, numbered independently (sections A, B, C), sharing
   `draft_v3.bib` (it cites nothing, so it prints no bibliography). Verbatim is verified
   mechanically: the moved block equals HEAD's lines 1846–4882 line for line, the only
   difference being the trailing blank line before `\printbibliography`. The section map in
   §1 of this file (including the "### Appendices" subsection) therefore still describes the
   content row for row; only the container changed.
2. **Cross-references.** The online appendix resolves its 52 references into the main text
   (assumptions, definitions, lemmas, equations) through `xr-hyper` against `draft_v3.aux`;
   the main text must be built first. In the other direction the main text referenced exactly
   three appendix labels (`sec:proofs-core`, `sec:proofs-existence`, `sec:proofs-ge`) at ten
   sites; all ten are now the prose pointer "the online appendix" (five inside `\resultstatus`
   lines, whose label content is otherwise untouched). No `\ref` crosses from main text into
   the appendix.
3. **Main-text edits in the same pass** (the unslop/econ-register pass Austin ordered with the
   split): "features" → "parts" (§3.2); "which is the fact that" → "and that fact" (§2.4); the
   §4 opener no longer discusses the proposition-versus-theorem taxonomy and leads with what
   the section is for; one abstract sentence split in two. Formal statement bodies, status
   lines, hypothesis tags and every mathematical sentence are byte-identical to the post-fix
   round state; the 35 em dashes that remain all sit inside formal statement environments and
   are frozen-record transcription, so they stay.
4. **Deliverables.** `deliverable/draft_v3.pdf` (36 pages) and
   `deliverable/draft_v3_onlineappendix.pdf` (51 pages). The `.tex` sources stay at the repo
   root; gitignored build intermediates were deleted. The pre-existing uncommitted deletions
   under `deliverables/` (plural, the v2-era folder) are a user-side change this pass did not
   touch and did not commit.
5. **Gates (this pass).** Main: four-pass `xelatex`/`biber` build, 0 errors, 0 undefined
   references, 36 pages. Appendix: three-pass `xelatex`, 0 errors, 0 undefined, 51 pages; zero
   `??` in the extracted text (all `xr` references resolve). Unicode quote/dash scan clean on
   both sources and the bib. Intended-only diff review: 20 added lines in `draft_v3.tex`, each
   enumerated above; everything else is the cut.

---

## Amendment, 2026-08-30 (Gorbenko-style main-text restructure)

Austin's instruction, after the appendix split: the main text read like a math paper. The
reference style is Gorbenko--Malenko, "Auctions with Endogenous Initiation" (abstract under
150 words; results stated in plain numbered prose; no status lines, no numerical records, no
assumption essays in the body). The restructure below changes containers, titles, and prose
register only. **No statement, hypothesis list, equation, number, or honesty label was
strengthened, weakened, added, or dropped.** Every sentence deleted from the body survives
either in `draft_v3_onlineappendix.tex` or in the new §5.6 summary, and the map above still
describes the content row for row; this amendment records where each row now lives.

1. **Assumptions regrouped, 16 to 6.** The sixteen one-clause assumption environments are now
   six displayed assumptions: Assumption 1 (§3.2: no-feedback, flag termination, tie-break),
   Assumption 2 (§3.3: the primitives clauses, incl. the boundedness paragraph moved to
   follow it), Assumptions 3--6 (§3.5: the equilibrium object; identification on flagged
   histories; the threshold chord restriction; the bridge and the general-equilibrium region).
   **Clause content is verbatim**; each original `\label` sits on its clause, so `asm:A4` now
   prints as Assumption 1(c) and every existing `\ref` resolves unchanged. The map rows for the sixteen assumptions are
   unchanged in content; only the numbering changed.
2. **Assumption essays moved.** The A5 derived-vs-retained essay, the A7/A7-J identification
   essays, the A(τ) bite essay, and the A(br) essay left §3.5 for **appendix Section A
   (Discussion of assumptions)**. §3.5 keeps one short paragraph per grouped assumption
   saying what it is for and pointing to the appendix.
3. **Numerical records moved.** Remarks `rem:A3record`, `rem:A6record`, `rem:P1record`,
   `rem:AtauRecord`, `rem:T1record` (prose), and `rem:C1record` left the body for **appendix
   Section B (Numerical records)**, verbatim, labels intact. **Table 1
   (`tab:window-record`) stays in the main text**, now inside §5.6. Body pointers to these
   remarks became the prose pointer "the online appendix".
4. **Status lines deleted (9).** The `\resultstatus` lines under D1, L1, L2, L3, L4, T1, P1,
   C1 (and the remark-status line) are gone from the body. Their content was already
   duplicated: the hypothesis lists stay in the statements, and the applicability content is
   carried by the new §5.6 and appendix Section B. No honesty content was lost.
5a. **Pointer repairs inside statements and moved blocks (fidelity round, 2026-08-30).** Five
   sentences changed container or pointer only, substance untouched: inside Proposition 1,
   (P-5)'s "read as in the ``A6 is read'' paragraph below" became "read as in the reading of
   that clause given below" (de-codenaming removed the quoted phrase, so the pointer would have
   dangled), and the two-readings paragraph's "Remark~\ref{rem:A6record} records it measured to
   fail" became "the online appendix records it measured to fail"; in appendix Section A, the
   A(τ) essay's section pointer was dropped (the remark is local now), the A5 essay opens "Most
   of Assumption 3(c) is a theorem" (the clause is no longer "stated here"), and the A7 note
   opens "The weak identification wording of Assumption 4(a)" (the pronoun lost its antecedent);
   in appendix Section B, rem:C1record's "(C-1)--(C-7) above" became "(C-1)--(C-7) of
   Proposition~\ref{prop:C1}". The A(br) clause title carries its symbol again
   ("The chord--sensitivity bridge ($\Abr$)") because Lemma 5's frozen statement body prints
   "under A(br)" and needs the gloss.
5. **Result titles de-codenamed.** "Lemma 1 (D1: the disclosure partition ...)" became
   "Lemma 1 (The disclosure partition ...)", and likewise for L1--L4, T1, P1, C1. The
   codenames remain where the record needs them: the appendix proof titles, this trace file,
   and the frozen record itself.
6. **§5.5 "What is not claimed" deleted.** The non-claims sentence moved into the conclusion
   (one paragraph, same content); the three open questions now live only in the conclusion
   (they were duplicated). New **§5.6 "The model at the implemented calibration"
   (`sec:calibration`)** summarizes in prose: the two measured existence-hypothesis failures
   (with the plain-words sentence), the chord-restriction failure (23--767 vs three, 180/180),
   the window record with Table 1 (18--77%, composition leg, H=10 corner caveat and the H=12
   chord-route caveat, node-evidence-not-a-sign), and the 18/80 equilibrium-region nodes.
7. **Abstract and intro rewritten in register, not content.** The abstract is 146 words
   (question, mechanism, the two margins' different status, filers-moved fact, design). The
   intro's three result paragraphs say the same content in plain English; the proof-strategy
   sentence moved out of the intro (§4's proof sketch already carries it); the numerical
   paragraph keeps every number and gains a pointer to §5.6.
8. **Gates.** Main text: four-pass build, 0 errors, 0 undefined references, 31 pages (was 36
   at the split). Appendix: three-pass build against the refreshed main `.aux`, 0 errors, 0
   undefined references, zero `??` in the extracted text (every `xr` reference into the main
   text resolves, including the clause references such as "Assumption 3(a)"), 56 pages;
   sections print A (Discussion of assumptions), B (Numerical records, Remarks 1--6), C, D, E
   (proofs). Unicode quote/dash scan clean on both sources. The fidelity review of this
   restructure (fresh agent, none of it its own) is recorded in the session brief.

---

## Amendment, 2026-08-30 (fourth): prose rewrite of the main text — formal machinery reduced to two statements

Austin's directive: a natural, singular-author economics paper in British English, at most two
visible formal statements (fixed-policy attenuation and the general-equilibrium implication),
existence and the intermediate results as concise prose, technical proofs in the online appendix.
Only `draft_v3.tex` was edited; `draft_v3_onlineappendix.tex` is byte-identical to its state at
`adf97c6`, and the frozen record under `research/model_v4/` and `sections_v3/` was not opened for
writing.

**What now prints as a formal statement.** Two objects, and only two: **Theorem 1** (disclosure
attenuation at fixed policies, `thm:T1`) and **Proposition 2** (the dominance-and-contraction
implication in general equilibrium, `prop:C1`). Their bodies, hypothesis lists (T-1)--(T-15) and
(C-1)--(C-7), and displays `eq:T1B`, `eq:T1C`, `eq:C1` are unchanged in substance; the only edits
inside them replace pointers to objects that no longer print as environments with pointers to the
section that now carries the content (see "pointer repairs" below). The proposition counter is
advanced by `\setcounter{proposition}{1}` immediately before `prop:C1` so that it prints 2, leaving
1 to the existence anchor as in every earlier build.

**What became prose.** The existence proposition (P1), the disclosure-partition lemma (D1), the
two-cell decomposition (L1), the flagged-cell invariance (L2), the pooled interior-motion lemma
(L3) and the three-leg threshold lemma (L4). Each keeps its claim content in full:

- P1: the conclusion at every kappa in [0,1], the five conclusion clauses (perturbation family
  fixed once and used at every k, boundary handling by extension rather than restriction, flagged
  tuple beliefs as the point mass at the unique generating pair, the entry rule, flagged-component
  sequential optimality at every flagged pair), the thirteen hypotheses **(P-1)--(P-13) still
  printed and still tagged** (the online appendix cites those tags 67 times as literal text, so they
  cannot leave the main text), the A7-J on-path-versus-joint erratum footnote, the two readings
  (the pricing assumption not assumed here; the outer map read with a named tie-break-and-corner
  selection and a common bracket), the interior-crossing addendum with its two extra hypotheses,
  the proof route, and the six closing disclaimers. Anchor `\compatlabel{1}{prop:P1}`.
- D1: parts (a), (b), (c) still lettered, `eq:runup-jump` still displayed, the clock-equivalence
  gloss and the empirics counterpart retained. Anchor 1.
- L1: `eq:L1` still displayed, the Omega in {0,1} degeneracy and the "undefined rather than
  imputed" non-identification clause retained. Anchor 2.
- L2: the conditional-independence conclusion, the almost-sure footnote, the bidder-entry
  bookkeeping clause, and the "weak identification wording is not sufficient" paragraph retained.
  Anchor 3.
- L3: parts (a), (b), (c) still lettered, the minimal regularity, the Peano expansion, the uniform
  bound at the seam, and the "if and never iff" sentence retained. Anchor 4.
- L4: legs 1, 2 and 3 still named as legs, the leg-by-leg hypothesis split retained, and the
  paragraph on leg 3's inherited conditionality and clause (br-iii) retained. Anchor 5.

**Clause tags reinstated in Section 3.** The previous prose pass had dropped the clause markers the
online appendix cites literally. They are back, inline, with no new environments: (TR-i)--(TR-iv)
(12/15/10/2 appendix citations), the six requirements (i)--(vi) of the equilibrium definition
(cited as `def:cpbe`(i), (ii), (iii), (vi)), ($\tau$-i) and ($\tau$-ii), and (br-i)--(br-v)
(9/7/4/9/6 citations), each with the clause content transcribed from the state at `416600a`. The
symbols A(tau) and A(br) are named in the main text, which the appendix's frozen bodies print.

**Pointer repairs inside retained statements.** `Lemma~\ref{lem:D1}\,(b)` in Theorem 1(C) became
"the clock equivalence of Section 5.1"; (T-2) "Assumption 1(d)" became "the interior-crossing
condition"; (T-4)/(T-5)/(T-6)/(T-10)/(T-12) became the two-cell decomposition (11), the
flagged-cell invariance of Section 5.2, the partition result of Section 5.1, the pooled
interior-motion result of Section 5.3, and the three-leg threshold result of Section 5.3;
(T-9)/(T-11) name A(tau) and A(br) by symbol; (T-13) drops the assumption number. In Proposition 2,
(C-1) points to Section 3.4 and (C-5) to Section 3.5; the closing sign-constancy sentence names the
general-equilibrium condition rather than its number. In Section 6, the timing-split paragraph now
reads "the identity (10) and the flagged cell's kappa-invariance". In the introduction, one
"Proposition~\ref{thm:T1}" was corrected to "Theorem~\ref{thm:T1}". In Section 3.3 and the
conclusion, the two remaining `Assumption~\ref{...}` pointers (the integrability condition, and the
scoped continuity problem named among the open questions) became prose names, since no Assumption
environment prints.

**`sec:hypotheses`.** The deleted "Standing assumptions" subsection took its label with it; the
appendix cites it twice and Theorem 1's (T-8) once. The label is reattached to Section 3, so the
pointer now resolves to "Section 3" where it read "Section 3.5". This is the **only** printed value
in the entire cross-reference surface that differs from `adf97c6`.

**Gates.**
- Main text: `xelatex -> biber -> xelatex -> xelatex`, 0 errors, 0 undefined references, 0
  multiply-defined labels, 27 pages (31 at `adf97c6`).
- Online appendix: three passes against the refreshed `draft_v3.aux`, 0 errors, 0 undefined
  references, 56 pages, zero `??` in the extracted text.
- **Label-value diff against `adf97c6`.** HEAD's `draft_v3.tex` was built in a scratch directory and
  the `\newlabel` printed values compared for all 51 labels the online appendix resolves into the
  main text. 50 of 51 are byte-identical; the single difference is `sec:hypotheses` (3.5 -> 3),
  explained above. In particular every assumption clause number (1(a)--6(b)), every definition
  (1--7), the remark (1), the lemma anchors (1--5), `thm:T1` (1) and `prop:C1` (2) print exactly as
  before, so no appendix sentence changes meaning.
- Abstract: 146 words.
- Unicode quote/dash scan clean. Em dashes: 7 remain, all inside the bodies of Theorem 1 and
  Proposition 2, where the standing ruling keeps frozen-record transcription as written; the twelve
  that the prose conversion would have moved out of statement bodies were rewritten away.
- `deliverable/draft_v3.pdf` and `deliverable/draft_v3_onlineappendix.pdf` refreshed.

**Environmental note.** `biber` failed silently (exit 25, empty `.bbl`) on the first attempt because
its PAR extraction cache under `$TMPDIR/par-*` was incomplete (`Unicode::UCD: failed to find
unicore/version`). Deleting that cache directory fixed it. Nothing in the manuscript caused it and
nothing in the manuscript was changed for it.

---

## Amendment, 2026-09-01 (empirical layer rebuilt: E1 replaces the seeded sample and the prospective spec)

The manuscript's empirical layer was rebuilt on 2026-09-01: §6 of `draft_v3.tex` was rewritten
(commit 0e1e5e2) around the single registered exercise E1, and the superseded August design was
preserved, exactly as viewed, as `draft_v3_onlineappendix.tex` §app:honesty, "The August 2026
empirical record, exactly as viewed" (commit 1243cd4). The August record was deleted from the
live tree the same day (deletion commit 235de22) and lives in history at 9b98089; the appendix
quotes it from there. What changed in this map:

1. **New authorities.** Every empirical number in `draft_v3.tex` draws on
   `empirics/output/e1_estimate.json` (the single result authority), registered against
   `research/empirics_v4/e1_spec.md` (four dated amendments, all 2026-09-01); the row-level
   record is `empirics/output/e1_delays.csv` (1,137 accessions, a status and reason on every
   row) and the figure is `empirics/output/e1_cdf.pdf`. Independent clean-clone reproduction is
   recorded at `quality_reports/verification/2026-09-01_e1_reproduction_verify.md`
   (`e1_delays.csv` bit-identical; the JSON identical outside the G3 block, whose `NOT RUN`
   rerun state is the expected consequence of not re-scoring the hand audit; test_e1.py 13/13,
   test_parse_13d.py 11/11).
2. **§6 re-mapped.** The old §6 rows (the two-layer split; the seeded n=98/90 Table 2
   (`tab:fact1`) and Figure 2 (`fact1_delay.pdf`); the §6.2 seven-leg prospective map (a)–(f);
   the §6.3 headline shell) were replaced by rows for the five new subsections:
   `sec:e1protocol`, `sec:e1result` (Table `tab:e1`, Figure `fig:e1cdf`), `sec:e1audit`,
   `sec:e1record`, `sec:e1headline`. Rows elsewhere that cited the deleted artifacts were
   re-pointed: the abstract and intro empirical rows and the conclusion paragraph now draw on
   `e1_estimate.json` and the appendix's preservation pointer; the included-figures list
   carries `e1_cdf.pdf`; the honesty-label crosswalk carries the E1 descriptives row, and the
   Trivedi ESTIMATED row's location lost the deleted §6.2(b) leg. The BBJJ bucket and Trivedi
   first-stage rows, which had cited SPEC.md merely as the place a literature number was
   recorded, now point at the live cards (`bebchuk_brav_jackson_jiang_2013_jcl.md` R1–R2;
   `trivedi_2026_ssrn.md` R2), and the §2.1 date confirmations point at
   `_institutional_sec_33_11253.md` and lit_institutional-facts §1.3. Content of the deleted
   SPEC.md that survives only as viewed record is cited at §app:honesty with the 9b98089
   provenance, never as a live source.
3. **Headline shell resolved.** The "[headline choice pending]" state is gone: the headline is
   the E1 filing-delay result (§6.5, `sec:e1headline`), with `headline_suppressed: false` in
   the result authority. Notes-for-Austin items 1–2 were rewritten accordingly (the section
   heading's "in the shell" went with them), and the 2026-08-30 fix-round amendment's item 4
   (the old Table 2 attrition caption) is marked superseded in place.
4. **What did not move.** Every theory row (model card, HANDOFF_sign, sections_v3), the
   removed-claims enumeration, and the earlier rounds' compile-gate records are untouched. The
   frozen record under `research/model_v4/` and `sections_v3/` was not opened for writing, and
   this pass edited no file other than this one.
