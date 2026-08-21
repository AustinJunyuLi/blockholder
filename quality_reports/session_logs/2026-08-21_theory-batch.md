# 2026-08-21 — Theory batch run (waves A–D)

**Goal:** execute tickets 04, 05, 21–30 per the batch-run section of
`quality_reports/plans/2026-08-20_theory-lane-agentic.md`. Fable orchestrates;
Opus writes/verifies; Sonnet plumbs. Fable personally does: ticket-24 A7
reasoning, ticket-25 design review, adjudications, final coherence read.
Stop at ticket 30's GPT paste (bundle handed to Austin, not pasted).

**Orchestration note:** subagents write files but do NOT run git — the
orchestrator commits/pushes centrally after each landed unit, to avoid
concurrent index.lock races in the shared worktree. Same per-unit commit
cadence the tickets ask for.

## Wave A dispatch (start)

- L3 writer (opus), L4 writer (opus), P1 writer (opus) — proofs to
  `research/model_v4/proofs/`. Writers independent: L4 must not read L3's
  proof file; all cite card-ledger statements only.
- impl-design (opus) — ticket 25 design doc only; STOP before build for
  Fable review.
- O-1 re-run (opus) — ticket 05 repo-model check + provisional
  HANDOFF_sign.md.
- lit-fetch (sonnet) — ticket 04 full texts (Chabakauri 2022 priority;
  Burkart–Lee–Van Schepdechen Dec-2025 rev; Zeng internet appendix) to
  scratchpad; Opus readers follow.
- Fable: ticket-24 A7 satisfiability construction, inline.

## Incremental notes

- **Ticket 05 (T1, O-1 re-run) DONE.** Committed claim located in
  `quality_reports/reports/2026-08-19_framework_v3_referee_report.md:113-120`
  (referee's [O] finding), independently re-executed in
  `research/review_v3/verify_theory.md:32,42-53`. Reproduced in the current
  repo model by `quality_reports/fixes/t1_o1_rerun_check.py` (5 checks, all
  pass, JSON on disk, byte-identical across runs and cwds). **Every committed
  number matches to the last printed digit** — ratios 1.06397 / 1.18373 /
  1.13631 / 0.37798 vs committed 1.0640 / 1.1837 / 1.1363 / 0.3780; baseline
  masses, pointwise-slope claim and figure-magnitude claim all reproduce too.
- **New beyond the committed claim:** ADR-0007's "Ω ≲ 0.29" is a grid point,
  not the crossing. Bisection puts the sign flip at **k_D* = 1.28618,
  Ω* = 0.3428**. Failure region is wider than recorded; the decision is
  unaffected, but anything quoting 0.29 as the boundary should quote 0.343.
- **Sign published (PROVISIONAL, PE, fixed cutoffs):** flagging the public buy
  RAISES κ-sensitivity — the empirics spec's **Branch B, δ < 0** — magnitude
  +6.4% at baseline (curves 0.9% apart in range), so a bounded null is the
  realistic empirical outcome. `research/model_v4/HANDOFF_sign.md`, with a
  "Two-round model" placeholder for tickets 25/30.
- **ω_a data anchor: ABSENT, stated plainly.** No repo card measures the
  disclosed share of engagements; Becht et al. 2017 fn.2/fn.15, Norli et al.
  2015 n.10 and Edmans 2014 p.35 each say the denominator is unobservable.
  Three bounded proxies recorded with sources and labelled for what they are
  (BJPT 97.5% upper bound; Gantchev 98.2% upper bound, self-declared
  non-random; SEC 2022 13D/13G split 12.1%, wrong unit). They straddle Ω*,
  so the sign is not yet anchored on data — flagged as the highest-value
  calibration input the project can acquire.
- Note for the orchestrator: the `blockholder_v4_theory` venv was empty;
  `requirements.txt` installed into it so the check script runs.
- **Ticket 22 (L4 proof) LANDED** (`proofs/L4_proof.md`, 545 lines). Legs 1-2
  (nestedness, Ω↑) proved outright from D1's clock equivalence; leg 3 (𝒮_P↓)
  needs a named bridging hypothesis **A(br)** (chord–sensitivity bridge, 4
  clauses; br-iii is the genuinely unjustified one). Step 9/11/13 = the
  newly-flagged-is-Voice arithmetic. Extra hypothesis b_0 < τ' < τ. Two
  adjudication items for Fable at card-regeneration time: (1) intended label
  should read "PROVED under A(br)", not "under nested reclassification";
  (2) π̄ definitional tension — §4.4 gloss ("pre-order pooled engagement
  share") vs A(τ)'s chord upper support point; factor two under A_0=A_1
  martingale reading. Fable to rule before the card is regenerated.
- **Ticket 24 (A7 construction) DRAFTED by Fable** (`proofs/A7_construction.md`):
  A7′ = composed terminal target strictly increasing on the flagged region;
  sum B^F+Q^F reveals b*; pro-rata Exit/Hold/Voice menu satisfies A7′ and
  VIOLATES the card's strict-pair patch (B^F jumps down at crossing-date
  boundaries — numeric witness 1.68→1.56). A7′ necessary within pro-rata
  family. Opus adversarial attack dispatched; card edits wait on it.
- Wave A agent fates so far: lit-fetch (sonnet) PASS — all 3 texts obtained
  (CFJ via LSE eprint; BLV Dec-2025 via ECGI long-timeout; Zeng IA via
  Springer supplement). Ticket's "Van Schepdechen" author name corrected to
  Voss by repo evidence. o1-rerun (opus) PASS. L4-writer (opus) PASS.
- **Ticket 05 verifier (fresh opus): PASS.** Re-run exit 0, JSON byte-identical,
  independent recompute matched all four ratios to 5 dp, all six ω_a anchors
  verified verbatim. 1 WRONG (handoff said "Five checks", JSON has six) and
  1 MISCITED (referee-report range 113–120 → 114–124) — both repaired by the
  orchestrator, JSON regenerated (exit 0, 6/6 pass), committed. Non-blocking
  note kept: TOL_MATCH=5e-3 is loose vs 4dp record (passed at 3.1e-5).
- **Ticket 25 design review (Fable) DONE** — appended as impl_design.md §13.
  APPROVED with 7 rulings: M=2; H=10 with mandatory H=12 robustness for T1;
  NO discount factor (card is spec; multiple_root_nodes nonempty at baseline
  = builder stop-and-report); P1 verdict binds on payoff scale; L3 relative
  tolerance amendment (logged as approved deviation from turn-1 request);
  check scripts stay at quality_reports/fixes/t2_* per ticket 28 (tickets
  outrank design preference); A7′ resolved by ticket 24's construction —
  design's independent "sum-monotone" finding converged with it. Build
  dispatched (opus).
- **Tickets 21 (L3) and 23 (P1) LANDED** (proofs committed). L3: mean-value
  chord form proved; ∂_κE[h]=A′_κ·C_h derived twice independently; A(τ)
  derivative restrictions shown equivalent to κ-invariant pooled mass+moment
  (only the support condition has bite); draft_v2's own pooled law FAILS
  A(τ) (worked example); two-round-cell membership declared OPEN with named
  sufficient conditions S1/S2. P1: pricing fixed point reduced to (v̂,π);
  under added h.12 (m_0≥0) inner existence+uniqueness DERIVED (A5's real
  content = continuity in k); sequential optimality needs new h.11 "flagged
  closure" — card's "under A1–A7" overstates; A6 continuity assumed with
  weakest replacement named; A8 given bite only under h.13.
- **Fable ruling (π̄), now firm:** π̄ = UPPER SUPPORT POINT of the pooled
  posterior in A(τ), not the pooled engagement share; share = E[Π_κ],
  κ-invariant under A(τ), = π̄/2 only in the level-symmetric case. Both L3
  and L4 flagged the same tension independently; card §4.4 gloss to be
  corrected at ticket-27 regeneration. T1 writer instructed accordingly.
- **Dispatched:** impl-builder (opus), batch-1 proof-reader for L3/L4/P1
  (fresh opus, turn2-audit format), T1 writer (opus; carries A(br) verbatim
  + π̄ ruling + O-1 numbers as the window failure case).
- **Ticket 04, BLV Dec-2025 card LANDED.** D7 appropriability SAFE (no
  lambda/q/gamma/psi analogue; bargaining still one exogenous Nash weight).
  Paper now JF-FORTHCOMING. 11 of 19 old-card quotes broke in revision —
  including the headline whitespace quote Q1 "Market liquidity plays no role
  in our analysis" (DELETED; replacement lean: the Kyle/Kyle–Vila abstraction
  at printed pp. 54–55). Margin still unoccupied; fn. 13 concedes disclosure
  regulation + liquidity limit stakes, then abstracts. Draft_v3 must not cite
  the dead quote.
- **Ticket 24 COMPLETE.** Attack verdict: SURVIVES WITH REPAIRS (nothing
  refuted; witness table exact in rational arithmetic; Step 8 necessity and
  Step 4 σ-field logic confirmed; L2 verified to consume on-path form only).
  All repairs R-A/R-B/R1–R9 applied by Fable: b* now strictly increasing on
  ALL of ℝ (R5 — fixes the 40-collision joint-form failure and the R6
  policy-dependence), patch↔A7′ shown NON-NESTED (patch neither necessary
  nor sufficient), conditional-independence line displayed, Ω>0 added as
  hypothesis 7, four new failure cases (sharpest: A7′ menus fully separating
  — risk relocated to P1's incentive compatibility). Card edited per ticket
  24: §4.2 strict-pair patch REPLACED by A7′ (quantified over Θ); §5 A7 note
  marks satisfiability RESOLVED; stamp bumped (surgical, regeneration pends
  ticket 27).
- **Ticket 04, CFJ card LANDED — the whitespace verdict: NO REFUTATION.**
  Chabakauri–Fos–Jiang (RoF 2026, 30(3) 921–948 — repo's "(2022)" cite is
  wrong) has no disclosure rule in the model (pp. 11–18: zero hits for
  disclosure/13D/Schedule), no bidder/tender/premium in 79 pages. Partition
  whitespace HOLDS. Live risks carded: they own third-party inference of
  activism from pooled order flow; their Table 6 splits pre-filing at the
  10-day deadline; Table 10 col.5 has an Amihud null on 13D CARs. Version
  read: LSE AAM (Feb 2025) — page cites must be re-mapped before draft_v3.
- **Ticket 26 (T1 proof) LANDED** (812 lines). 𝒮=(1−Ω)𝒮_P from L1+L2+PE-Ω
  (H6, shown available under frozen cutoffs, fails in GE — C1's term); ALSO
  proved for the total-variation aggregate (so theorem and O-1 evidence share
  a functional). Threshold: W_τC_τ≤1 with BOTH ratios in [0,1] (L4 legs 1+3,
  A(br) carried). Window: W_T≤1 DISCHARGED from D1's clock equivalence
  (removes turn-1 h.6); exact iff proved both directions; no window sign.
  Ledger wording repair flagged: "equivalently" false if read as
  finite⟹local-at-every-value (Step 21c: one point only, by mean value).
  O-1 read through the factorisation: composition factors 1.105/1.359/1.591/
  0.756 — composition flips the sign, weight always attenuates.
- **Batch-1 proof-read (fresh opus): L3 PASS, L4 PASS, P1 PASS.** FAIL 0,
  REPAIR 18, OBSERVATION 12; all executed checks reproduce (P1's inner fixed
  point: 20k random draws, 0 multiplicity, 0 sign failures; L3's numbers to
  ≤2e-18). Substantive: P1-R1 h.11's primary form UNSATISFIABLE with finite
  menu (survives on definitional reading — adjudicated: definitional form
  becomes THE hypothesis); L4-R1 π̄ two-reading agnosticism must collapse
  (adjudicated: support-point reading, identity branch excluded as degenerate
  per L3 Step 19); L3-R1 kernel-depends-on-posterior-only made explicit;
  L3-R2 "two independent derivations" claim dropped (hypothesis sets proved
  equivalent by L3's own Step 14); P1-R8 intermediate-date pricing rescoped
  to tower expectation. Card gaps for regeneration: no blockholder payoff
  row (U_j); §4.3 Y-row ambiguity; A(τ) to carry the kernel clause.
- **Dispatched:** repair-b1 (opus — applies the 18 repairs + notation fixes
  with the adjudications above); 4 statements-only re-derivers (opus):
  core D1/L1/L2, L3, L4 (amended statement + A(br) verbatim), P1 (amended
  statement + h.11 definitional + h.12). Re-derivers forbidden from proofs/
  and threads/. T1 proof-reader (batch 2) still out; builder still out;
  card-verifier still out. Live agents: 8.
