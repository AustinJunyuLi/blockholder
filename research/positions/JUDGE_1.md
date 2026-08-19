# JUDGE 1 — Ticket 03 positioning tournament (2026-08-19)

Adversarial check executed: for each proposal I opened ≥3 decision-critical citations in the
owning card/record and confirmed or refuted. Cards/records opened in full or by targeted grep:
`_institutional_sec_33_11253.md`, `greenwood_schor_2009_jfe.md`, `maug_1998_jf.md`,
`cetemen_cisternas_kolb_viswanathan_2026_jf.md`, `zeng_2026_ras.md`,
`collin_dufresne_fos_2015_jf.md`, `trivedi_2026_ssrn.md`, `dass_huang_maharjan_nanda_2020.md`,
`edmans_fang_zur_2013_rfs.md`, `albuquerque_fos_schroth_2022.md`,
`author_proposal_outline_2026.md`, `quality_reports/fixes/D7_takeover_game_microfound.tex`,
`research/draft_v2_digest.md`, `research/empirical_feasibility.md`.

## Score table

| Proposal | A Whitespace | B Anchoring | C Main result | D Empirics | E December | F Continuity | Total | Rank |
|---|---|---|---|---|---|---|---|---|
| P1 window × premium (tender game) | 5 | 4 | 4 | 3 | 4 | 5 | **25** | 4 |
| P2 rule-is-the-partition (info design) | 5 | 4 | 4 | 4 | 5 | 5 | **27** | **1** (tiebroken) |
| P3 deadline as partition device (MCS) | 5 | 5 | 4 | 4 | 4 | 5 | **27** | **2** (tiebroken) |
| P4 Feb-2024 matched DiD | 5 | 4 | 4 | 5 | 4 | 4 | **26** | 3 |
| P5 purpose partition 13D/13G | 3 | 5 | 4 | 3 | 4 | 4 | **23** | 5 |

P2 and P3 tie at 27; the tie is broken on the tournament's stated weighting (deliverability is
first-class, spec §Further Notes) — P2's proved core already exists in the repo, P3's apparatus
is new. No two proposals are near-identical in position; P2/P3/P1 are the same *family*
(window/partition theory) on different cells (W3 / W5+W6 / W1+W12).

## Reasons

### P1 — Window length and the takeover premium
- **A 5.** Claims W1 (map: CLEAR) with W12 as mechanism (CLEAR on mechanism) — both ratings
  quoted correctly. Disposals verified: Back p. 1453 (σ²T), BL Lemma 2 p. 1877 + p. 1891
  future-work hand-off, BL IA Prop. 1 (ε-channel) correctly cited as the "wedge exists" owner,
  GMM Prop. 7 p. 28 stake-path concession, CL −13.69% marginal / −0.60% GE stated correctly.
  W8b explicitly *not* claimed, with the BLV Dec-2025 standing risk named.
- **B 4.** Anchor and binding fact confirmed (Rule 13d-1(a), §1; Table 3 p. 189: 20% <100%;
  late rate ≈29% p. 178 n. 695). The D7 jump claim is **confirmed in the record**
  (`prop:d7-lambda` + comparative-statics remark (iii): "as α crosses 1−τ_c from below … λ
  jumps up"; check script exists). Two slips: the wedge is written (1−θ)λρΔ_eng but the D7
  fold preserves ρ²(1−θ)λΔ_eng (one ρ dropped); and the 18% power anchor is Greenwood–Schor's
  *acquired*-within-12-months frequency (R7, p. 372), re-labelled "bid within 12 months".
- **C 4.** Statement is precise (signs, discontinuity at the pivotality boundary,
  cross-partial). Proof route credible: tender-game half already PROVED and check-verified;
  the accumulation half (√(κT) law) is new but standard Kyle. Label PROVED-on-named-primitives
  is realistic; the measured-vs-standalone premium risk (prop:d7-afs) is named honestly.
- **D 3.** Confound list is complete and correctly dated (EDGAR cut-off same-day, 13G
  2024-09-30, XML 2024-12-18, T+1, BBJJ defence channel, Ben-David discipline). But: no
  control group (acknowledged, bounded instead), **no pre-trend item**, no parser-audit item,
  and the change test's MDE ≈ 7–8 pp on ~300 bids is a bound, not a detection. The level test
  is cross-sectional calibration against the proved λ jump — honest, but the weakest checklist
  among the four serious empirics.
- **E 4.** Half the theory is done and verified; accumulation block 3–4 weeks; empirics 8–10 of
  ~19 weeks; fallbacks real (NUMERICAL + tender-game half stands; level test + calibrated
  bound). Slight optimism on the hand-collection yield.
- **F 5.** The most recognisable descendant on the object side: (m₁−m₀), D7, κ as driver, the
  partition — draft_v2's headline machinery, re-anchored. Drops (four-action menu, R1, welfare,
  D8) all land in occupied cells, per the map.

### P2 — The rule is the partition
- **A 5.** Claims W3 (map: CLEAR with a named boundary) and respects **both** boundary wordings
  verbatim (Kyle–Vila own the un-keyed split; pooled = pooled *for the price-setting market*,
  Zeng cited for the leak). Disposals verified: Maug Q5 p. 73 (verbatim-checked against the
  card's fixed quote), CL p. 14 off-path μ(α)=1, OCB p. 2836, Corum p. 19, Back p. 1453, CDF
  p. 1464, BL p. 1891. Chabakauri named as the uncarded live refuter — correct per sweep (d).
- **B 4.** Anchor confirmed (§1, pp. 1, 10). Sample arithmetic confirmed against feasibility
  §1.3 (2,849 pre / 1,048 post; parser fix 0.5–1 day, doubles the post leg). Occupied
  magnitudes confirmed: CDF ~3% (JF p. 1563), Zeng 2.8% run-up (R1, pp. 1309–1310). **One
  miscite:** CCKV's "No agent in the model ever learns that a blockholder holds a block" is
  quoted as paper text at p. 11; it is the *card's* §6(a) summary sentence — the paper's
  support is fn. 16, p. 15 (p. 11 carries Q4 instead). Substance confirmed, attribution
  refuted.
- **C 4.** The representation + decomposition + fixed-cutoff attenuation is stated precisely,
  and the proof route reuses machinery the digest independently confirms as proved
  (disclosed-branch κ-invariance; Brouwer existence; price decomposition) — "days, not weeks"
  per digest §6. Labels (PROVED fixed-cutoff / region-certified GE / NUMERICAL off-region)
  match what the repo can actually earn. The interior-crossing collapse risk (baseline
  collapses Hold) and the D8 sign-flip risk are named honestly.
- **D 4.** The timing-split implication is sharp and falsifiable (sign pattern across κ, not
  just a flattening), powered inside occupied magnitudes (MDE ≈ 0.8 pp vs CDF 3% / Zeng 2.8%).
  Confounds handled including Zeng's non-neutral 1–13-day screen; pseudo-trigger placebo at
  TD−63; no 13G control correctly justified via W2. Missing: explicit pre-trend series and
  parser-audit item; the December clean result is a *price* object, with the control-outcome
  (premium) leg only specified.
- **E 5.** The strongest deliverability profile: core rebuild reuses proved draft_v2 blocks
  (3–4 weeks), fixed-cutoff attenuation days, GE region 1–2 weeks on the D8 template, split
  empirics ~1 week on disk data — and the stated fallback (representation + fixed-cutoff
  attenuation + split empirics) is already a full draft.
- **F 5.** Fixes draft_v2's exact referee-found flaw (digest §5.3: D=1{q=+1} is an ad-hoc
  one-unit buy, not the rule) by deriving the branch structure from the rule's two keys. κ,
  bidder entry, D7 λ as the flagged-cell microfoundation, honesty labels — all recognisable.

### P3 — The filing deadline as a partition device
- **A 5.** Claims W5 (CLEAR; boundary respected verbatim — random horizons owned by
  Caldentey–Stacchetti/Baruch/Back–Baruch via CDF 2016 p. 1450) and W6 (CLEAR; the
  slope-vs-level wording follows the map's instruction exactly, Massa–Xu Table 7 p. 1482
  cited). W9 sidestepped with the correct modal-deadline fact (≈34%, 33-11253 p. 178).
- **B 5.** Every check passed, including two non-obvious SEC-table facts: Table 3 p. 189 (80%
  complete) and **Table 6 pp. 225–226 — Amihud 0.13 → 0.08 across the constraint columns**
  (confirmed; the anchor's bite covarying with liquidity is real and correctly read). Item
  5(c) as a 60-day mechanical trade report confirmed (CDF card §4, JF p. 1556). Trivedi's
  nulls (+0.41, t=0.50) used exactly as the map instructs (uninformative nulls that *protect*
  κ as pre-treatment). Zeng IA.2 p. 1322 characterised correctly.
- **C 4.** Increasing differences of the flagged stake X_T in (κ, T) plus the composed
  cross-partial is a real new theorem with real economic content; the MCS route
  (single-crossing on the Bellman objective, order-preserving Riccati) is credible for the
  linear-Gaussian class. Label PROVED-under-named-condition / NUMERICAL off-region is
  realistic. The named break (terminal-flag manipulation of what the filing reveals) is the
  honest weak joint, and the Item 5(c) mitigation is self-flagged as contestable.
- **D 4.** Interaction-not-level identification with a bounded null (pre-rule slope as
  benchmark); the **13G placebo is the best placebo on the table** (13G deadlines unchanged
  until 2024-09-30 — confirmed against the institutional card §1); ≥500 placebo dates cover
  pre-trends; confound list complete and dated. Power is deferred ("formal MDE in the spec
  first") and the control-outcome leg is only "specified and piloted" by December.
- **E 4.** 8–11 weeks is realistic in total, but the model+proofs line (5–7 weeks) builds a
  *new* dynamic apparatus from zero — nothing in the repo proves a single step of it yet,
  unlike P2. Fallbacks (region theorem, NUMERICAL, premium as spec+pilot) are credible.
- **F 5.** One informed blockholder, noise κ, a disclosure flag partitioning information, D7
  downstream — the triad intact and the supervisor's draft visible throughout; the trading
  layer is rebuilt but the objects are draft_v2's.

### P4 — Feb-2024 matched-control DiD
- **A 5.** Claims W2 with the map's exact rating quoted ("CLEAR on the cell; hard on
  execution"). All four nearest-row disposals verified: Trivedi (object greps = 0), Polk
  (pre-rule projection, p. 516), the author's proposal (`empirics.tex:7-11` no untreated
  group; `:143-146` CIs only), Bishop (asserts at printed p. 36, never estimates). W13
  fallback correctly rated.
- **B 4.** Fact-1 anchor numbers confirmed (35.7%→75.6%; median 7.0→5.0 bd). SEC Table 3
  (~3%, ≈7/yr) and Table 2 p. 181 (20%) confirmed. Greenwood–Schor base hazard confirmed
  (18.1%, p. 372 Table 6). **Dass fn. 27 rendered as "<19 treated acquirers" — exactly right**
  per the verifier-fixed card (19 is the stock-payment count; premium is *fewer*). **One
  refuted parenthetical:** "(t>3)" attached to Trivedi's R2 — the card prints t = 2.69 and the
  author's own statement that it does *not* clear the HLZ hurdle of 3 (p. 11); at best garbled
  shorthand for the hurdle, on the one citation where the map prescribes the wording.
- **C 4.** ESTIMATED + PROVED-conditional is the right label pair. The theory leg verifiably
  reuses proved blocks (proposal R1 quadratic cost — card §3 R1 confirmed PROVED; D7 λ), and
  the entry sign is honestly conditioned (proposal R11's unsigned ε_cert vs ε_det structure).
  The result is a bound plus a conditional sign — precise, credible, modest by design.
- **D 5.** The only proposal that answers **every** referee-checklist item on data in hand:
  matched never-13D controls (13G rejection justified via Trivedi §7), the bounded null
  promoted to a result, a complete dated confound list with a Feb–May 2024 clean window,
  explicit MDEs (6–10 pp), ≥500 placebos, a quarterly pre-trend event study **with a
  fail-blocks-causal-language gate**, and parser validation (30-filing audit, busday asserts).
  Power is the known, honestly-priced cost.
- **E 4.** The 16-week week-by-week plan is the most concrete of the five and every input is
  on disk; it is also the most labour-heavy, and the outcome-matching yield is an unproven
  engineering assumption (feasibility §2.3: 1–3 weeks, est.). Fallbacks (W13 coding,
  descriptive premium) are real.
- **F 4.** The triad is intact and §6's bid-hazard prediction is recognisable, but the centre
  of gravity moves from theory to empirics: draft_v2 is a pure-theory paper and P4's
  companion model is one-shot algebra. A recognisable descendant, but the thinnest
  theoretical continuity of the window-family proposals.

### P5 — The purpose partition (13D vs 13G)
- **A 3.** Claims W7, rated **NARROW and provisional**: the named card (AFS) is disposed of
  correctly (fn. 16 p. 34 verified verbatim; the §7 declaration-vs-information-set distinction
  is indeed stated in the card), but the cell's rating is provisional for a reason the
  proposal cannot dispose of — Payne-Mann, Stice-Lawrence & Wong (SSRN 5076900) is the sweep's
  one DIRECT hit and is behind a wall, unread. The contingency section is exemplary and
  honest, but the brief's rule is that a NARROW cell may be used only with the named card
  disposed of — and one potential occupant is undecidable today.
- **B 5.** Every check passed: the 20% override (EFZ n. 17, printed p. 14 — verified),
  NACCO v. Applica (EFZ p. 11), 13G-without-control-purpose (Zeng Q1 p. 1303, substance
  confirmed; the 13d-1(b)/(c) pin-cite is the proposal's own and correct), the Zeng purpose
  taxonomy (36.6/43.3/20.0, p. 1315), GS base rates (p. 372), EFZ's no-instrument concession
  (fn. 27, p. 1473), the 0.7% 13G CAR (WP p. 27; survives in print as 0.8/0.7 VW/EW).
- **C 4.** The load-bearing-and-liquidity-tilted purpose partition is stated precisely, the
  proof route verifiably reuses proved draft_v2 blocks (Prop 2/3 posteriors,
  disclosed-branch invariance, `lem:d1-variance` — all confirmed in the digest), and the
  labels (PROVED fixed-cutoff / NUMERICAL region) are realistic. The 13G-mixture monotonicity
  risk (D8 logic) is named. Content risk: the pooled-13G composition assumption is exactly
  where AFS's structural type-choice model already disciplines the economics.
- **D 3.** The workhorse leg is a cross-sectional lagged-Amihud interaction with **no dated
  shock and no instrument** — the proposal itself cites EFZ's fn. 27 concession that this
  class of design could not be instrumented. The sharp leg (20% boundary) is power-poor and
  specced-only; placebos (EFZ 0.7% CAR, QII 13Gs) are thin; selection into 13D is declared
  "the object, not a nuisance", which is true but does not by itself give a bounded null for
  any causal reading.
- **E 4.** 7–9 weeks, all inputs on disk, and the fallback is genuine (theory alone, or revert
  to the W6 slope design on the in-hand 13D sample). 13G enumeration is a flag change on an
  existing fetcher. Realistic — conditional on the position surviving the Payne-Mann read.
- **F 4.** Blockholder, κ, partition, bidder entry, D7 λ — recognisable; but it drops the
  Feb-2024 anchor entirely (permitted by ADR-0003) and re-keys the partition to the
  declaration margin, the furthest move from draft_v2's window/threshold language among the
  five.

## Flaw / steal

- **P1 — biggest flaw:** the strict/discontinuous part of the headline leans on the pivotality
  jump at 1−τ_c, which at realistic 6–10% 13D stakes forces τ_c into a squeeze-out/short-form
  reading — a referee can call the jump an artifact of the equal-treatment, one-shot-fringe
  primitives (its own §9 concedes this).
- **P1 — steal:** the W12 discipline — "a wedge exists" cited to Burkart–Lee IA Prop. 1, with
  ours sourced from the partition, not ε — and the proved λ(α) jump as flagged-cell
  microfoundation.
- **P2 — biggest flaw:** the fixed-cutoff attenuation is nearly mechanical (a κ-invariant
  flagged cell makes shifting mass attenuate by construction) — the headline risks reading as
  a decomposition, not a mechanism, exactly as its §9 admits.
- **P2 — steal:** the boundary-safe W3 wording (rule-keyed, present in every parameter
  configuration; pooled *for the price-setting market*) and the staging whose fallback is
  already a full draft.
- **P3 — biggest flaw:** the clean cross-partial wants the filing to be the bidder's dominant
  information source; if the bidder reads the public pooled-state price path, the stake
  channel attenuates and the result survives only on a region — the Item 5(c)
  mechanical-report mitigation is its most contestable choice.
- **P3 — steal:** the 13G placebo (13G deadlines unchanged until 2024-09-30) and the Table 6
  fact (Amihud 0.13→0.08 across constraint columns) as anchor evidence that the window's bite
  covaries with liquidity.
- **P4 — biggest flaw:** power — the constrained tail is capped at ~3% (≈7 campaigns/year), so
  the matched DiD detects only 6–10 pp on a ~17% base; the position stands only if the bounded
  null is accepted as the headline rather than as a consolation.
- **P4 — steal:** the bounded-null-as-headline framing and the checklist apparatus (matched
  never-13D controls, pre-trend fail-gate, 30-filing parser audit, `busday` asserts).
- **P5 — biggest flaw:** W7 is provisional — if the walled Payne-Mann et al. PDF delivers its
  abstract, "first to key a control outcome to 13D-vs-13G" dies, and the workhorse empirical
  leg has neither a shock nor an instrument.
- **P5 — steal:** the pre-committed Payne-Mann pivot structure (replicate-as-validation, then
  add slope and model) and the 20% eligibility override as a rule-keyed variation.

## Ranking and justification

**1. P2 (27) · 2. P3 (27) · 3. P4 (26) · 4. P1 (25) · 5. P5 (23).**

**Top two.** P2 and P3 are the same family at equal score and deserve the tiebreak spelled
out. P2 wins it on the tournament's stated first-class criterion: its core is the paper's
declared identity (CONTEXT.md: the disclosure rule *is* the market's partition), its proof
route reuses blocks the digest independently marks proved (the fixed-cutoff promotion is
"days, not weeks"), its fallback is already a full draft, and it directly repairs the
institutional-mapping flaw the referee review found in draft_v2 — all at the cost of a
headline that risks reading as a decomposition and one citation slip (the CCKV gloss quoted as
paper text). P3 has the meatier new theorem (increasing differences of the flagged stake in
(κ, T); a legal deadline as a partition event inside Kyle) and the cleanest citation record of
the five — every check passed, including two non-obvious SEC-table facts — but nothing of its
dynamic apparatus exists yet, its global sign depends on a single-crossing condition that can
fail, and its December control-outcome leg is pilot-only. On risk-adjusted December
deliverability P2 edges it; on scientific content P3 edges P2; the weighting in ADR-0003 and
the spec decides for P2. Either is a defensible winner; P4 is the best *empirical* package
and the correct fallback if the author wants the empirics to lead.
