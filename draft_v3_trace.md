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
| Abstract: partition identity, two-round model, three results with conditionality, Feb-2024 anchor, descriptives, spec, headline pending | MODEL_CARD §1 (position/object); result rows P1/T1/C1; HANDOFF_sign.md §8.1; `empirics/output/fact1_summary.csv`; `research/empirics_v4/SPEC.md` one-page summary |
| 13D rule facts: 5% since 1968, 10 calendar days → 5 business days effective 2024-02-05 | `research/cards/_institutional_sec_33_11253.md`; `research/lit_institutional-facts.md` §1.1–1.3; \cite{SEC2023} |
| Threshold vs window margins as separate policy coordinates; UK 3% contrast | CONTEXT.md (threshold margin, window margin); lit_institutional-facts §4 (UK DTR 5) |
| "Existence" paragraph (conditional; A6/A3 measured to fail; 23/27 nodes converge) | Card P1 row (label + numerical status); §5 A6 note, §5 A3 note; §9 item 4 |
| "Attenuation" paragraph (S = (1−Ω)S_P; threshold unconditional; window iff W_T C_T ≤ 1, C_T unsigned) | Card T1 row (A)/(B)/(C) verbatim content |
| "From fixed policies to equilibrium" paragraph (region as named hypothesis; 18/80 nodes) | Card C1 row (PROVED + NUMERICAL node evidence) |
| Window record numbers 18–77%; composition leg carries; weight leg 3–14% shave | HANDOFF_sign.md §8.1 (t2_t1_check block 4 + H=12 robustness) |
| A(τ) failure numbers (23–767 values, 180 non-degenerate nodes) | Card §5 A(τ) evidence note (ticket 33; t2_atau_support_check) |
| Delay-compression facts (7.0→5.0 bd; 35.7→75.6% within 5bd) | `empirics/output/fact1_summary.csv` (see §6 below) |
| "No paper combines the two margins, liquidity, and a control outcome" | competitor_map.md Part 3 (W1–W6) and Sweep summary ("none found") |
| Classics one-parameter answers; Maug's disclosure remark | lit_classic-exit-voice.md §A (cross-strand synthesis), Maug card §"Institutional facts" (p. 73) |
| Back-et-al isomorphism quote; CCKV pre-disclosure window; Kyle–Vila boundary | competitor_map Part 1 rows 5, 3; W3 refuter list (Kyle–Vila p. 54 n.1) |

### §2 Institutional setting and related literature (`sec:lit`)

| Draft content | Source |
|---|---|
| §2.1 Williams Act, 13D/13G split, 2022-02-10 proposal / 2023-10-10 adoption / 2024-02-05 effective / 2024-09-30 13G / 13D/A 2bd; UK 3%+1% rungs 2 trading days; EU ladder 4 trading days | lit_institutional-facts.md §1, §4, §5.1; SPEC.md §2.6 (date confirmations); \cite{SEC2022,SEC2023} |
| Window as "legal deadline attached to a partition, not a random horizon" | competitor_map W5 (random-horizon hazard 4) |
| Pooled state "pooled for the price-setting market"; Zeng leakiness; run-up begins on trigger date | competitor_map W3 sweep check; Zeng card (p. 1310 Q5, p. 1312 fn. 13) |
| BBJJ bunching 45.3% in 8–10bd bucket, ~20% on day 10 | SPEC.md §4 (quoting BBJJ Table 2 / Fig. 1, pp. 10–11) |
| §2.2 classics paragraph (Maug reversal; KW sign; FG complements; AP exit threat; EFZ; Norli) | lit_classic-exit-voice.md §§1–4 + §A; lit_liquidity-premia-empirics.md |
| "None of the four has a bidder, an offer, or a premium" | lit_classic-exit-voice.md §A ("Our paper's core objects … unclaimed") |
| §2.3 positioning: Kyle–Vila (disclaim disclosure; mixing split un-keyed), CDF 2015/2016 (presence common knowledge), Back et al. (σ²T isomorphism p. 1453; no acquirer/premium; endogenous horizon out of scope), CCKV (game inside unmodelled window), Corum 2025 (threshold/window fused, no counterparty), Corum–Levit (threshold occupied but sterile; flagged state off path), OCB (threshold as cap; interaction asserted not proved), Burkart–Lee (hand over the toehold) | competitor_map Part 1 rows + Part 2 hazards 2/3/11/14 + W1/W3/W4/W5 refuter lists, page-cited |
| §2.4 structural set (Gantchev; Johnson–Swem one-move filing; AFS liquidity-as-control, no control outcome; Celentano–Levine 5% calibration constant, window absent); BJPT/GS acquisition facts; Becht international returns | competitor_map Part 1 rows 1–3; lit_activism-empirics.md; lit_disclosure-structural-activism.md |
| Polk et al. (pre-rule only, no SEs, calendar-day mismeasurement 48% at Delta=10) | competitor_map Part 1 row 9 + reading note 9 |
| Trivedi (first stage +0.348 SE 0.130; nulls without MDE; frame never stated; not peer reviewed) | competitor_map Part 1 row 6 + reading note 6; SPEC.md §4 |

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

| Draft content | Source |
|---|---|
| Two-layer status split (executed descriptives vs unrun spec) | SPEC.md §0; CONTEXT.md (clean result, honesty labels) |
| §6.1 Table 2 (tab:fact1): pre n=98 mean 9.63 median 7.0 p90 23.0, 35.7%/80.6%; post n=90 mean 6.40 median 5.0 p90 11.1, 75.6%/88.9%; parse rates 0.68/0.64; seeded ~150/window; 300 filings | `empirics/output/fact1_summary.csv`; `empirics/output/fact1_filings.csv` (300 rows); `empirics/README.md` (Fact 1 design) |
| Figure 2 (fact1_delay.pdf) | `empirics/output/fact1_delay.pdf` (executed, on file) |
| SEC cross-check: 59% expected earlier filing; 29% of 2022 filings already inside, against our measured 35.7% already inside pre-rule; "different samples, different windows, same direction" | SPEC.md §4 and §6 quoting Release 33-11253 pp. 178, 193 (via the card); \cite{SEC2023}; 35.7% = fact1_summary.csv |
| BBJJ bimodality; Polk calendar-day mismeasurement (48% at day-ten marker) | SPEC.md §4; competitor_map reading note 9 |
| §6.2 sample/split (trigger-date assignment; straddlers; pre ends at adoption 2023-10-10; FD* and the 10pm cut-off; re-parse precondition) | SPEC.md §2.2, §2.4, §2.5, §2.6 |
| (a) timing split (market model window; run-up/jump; stacked regression with flagged interaction; two-way clustering + wild bootstrap; H1 sign-free; H2 both branches; the one check that kills the identity; RUNUP5; LIQ definition and orientation note; run-up path figure, benchmark shape +0.90%/+1.61%, Zeng +2.8%) | SPEC.md §3.1–3.7 (esp. 3.4, 3.5.2); benchmark table (Zeng pp. 1309–1310; Polk Table 1 p. 523) |
| (b) bindingness dose (D_j pre-period share >5bd; binary split; filer clustering; mechanical first stage; Trivedi +0.348 SE 0.130, mean-lag null, frame never stated; dose×LIQ confound) | SPEC.md §4; competitor_map reading note 6 |
| (c) stake at filing (STK; BBJJ −0.001*/0.6pp per ten days hazard; 0.12pp arithmetic vs MDE) | SPEC.md §5 (quoting BBJJ Table A2 p. 37); the stake at filing object = CONTEXT.md / card §4.2 B^F |
| (d) bounded null (80/20/3/1 ladder; 20/3/1pp rungs; accumulation channel only; dollar figures disclaimed) | SPEC.md §6 (Release Table 3 p. 189, p. 188 prose; AUTHOR_BRIEF restrictions 1–3) |
| (e) matched DiD (never-13D 3:1 Mahalanobis on size/illiquidity/exact SIC2/exact quarter; pseudo-trigger; BID12 coding + hand audit; GS base rates 18.1%/7.2%; MDE 4.4pp > 3pp ceiling; "that sentence … is the leg's honest deliverable") | SPEC.md §8.1–8.6 (incl. §8.6's "must be the headline sentence of the DiD leg") |
| (f) referee checklist (control/bounded null both; ten confounds incl. EDGAR cut-off, calendar-day screens, defence channel; power arithmetic; 568 placebos; pseudo-trigger TD−63; 13G placebo; seven pre-quarters F-test p<0.10 blocking rule; parser validation with two stated gaps) | SPEC.md §12 (g) + §3.7, §8.7, §8.8; CONTEXT.md referee checklist |
| §6.3 headline shell: "[headline choice pending]"; Candidates A (partition test), B (reform slope change, both branches live, A(τ) conditionality named), C (bounded null); what each needs / what kills each; "The choice … is mine" | Task instruction (choice not made — not picked); candidate content = SPEC.md §3.4/§3.5.2/§6/§8.6; A(τ) conditionality = card §5 A(τ) note |

### §7 Conclusion (`sec:conclusion`)

No new claims. Restates: the identity (card §1); the three results and their conditionality
(card rows); the window record + A(τ) failure "in the same section because they are both
true" (HANDOFF §8 + ticket 33); the executed descriptives (fact1); the spec and pending
headline (SPEC); three open questions (card §9 items 1–2 + A6 scoped remainder + the ω_a
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
2. `empirics/output/fact1_delay.pdf` (Figure 2) — the executed Fact-1 delay
   descriptives. Source: executed pipeline output on file (`fact1_summary.csv`).

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
| Fact-1 descriptives | Table 2 + Figure 2; "descriptive statistics; no standard errors are claimed"; seeded-sample and parse-rate caveats | §6.1 |
| Trivedi ESTIMATED | "+0.348 with standard error 0.130" quoted as his estimate | §2.4, §6.2(b) |
| CONJECTURE | none present; nothing promoted | — |

## 5. Notes for Austin (in the shell)

1. **Headline shell (§6.3)**: verbatim marker in the draft is `\textbf{[headline choice
   pending]}`. Candidates A (partition test), B (reform slope change; both branches
   live), C (bounded null) each carry "what it needs / what kills it / scope". The
   closing line reads "The choice among A, B, and C is mine, and the December draft's
   headline subsection will be written into this shell once it is made."
2. The spec's pre-registered power numbers (1.1–2.3pp timing split; 0.85pp stake; 4.4pp
   DiD) are quoted on the post-re-parse projection basis stated in SPEC §3.6/§8.6; if
   the re-parse lands different counts, the draft's §6.2 sentences carrying them need
   the recomputed values.
3. The two figures included are the only two with card rows; if a v4 figure set is ever
   rendered from the t2_* checks, Table 1 and the three numerical remarks are the
   natural targets.
4. Nothing in the draft states an empirical value for ω_a (card §9); the conclusion
   names its absence as an open input, per HANDOFF §6.

## 6. Compile gates

`xelatex -interaction=nonstopmode draft_v3.tex && biber draft_v3 && xelatex … && xelatex …`
from the repo root: **0 errors; `grep -in "undefined" draft_v3.log` returns nothing**
(no undefined citations or references); 81 pages; both included graphics found. (Font
warnings acceptable per the gate; none fatal.)
