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
- **Ticket 04 COMPLETE.** Batched card verifier (fresh opus): CFJ 58 OK /
  0 WRONG / 2 MISCITED; BLV 61/1/3; Zeng 41/0/1. All three decision-critical
  verdicts SURVIVE (whitespace holds — re-derived page map, re-ran greps;
  D7 safe + Q1 deletion confirmed at zero hits even for the fragment; IA.2
  numbers exact with no difference-test in the table note). The 1 WRONG (BLV
  Q7 "toward"→"towards", survivor count 8→7) and 6 MISCITED fixed in place.
  UNCHECKED (2, named, non-critical): published RoF text vs LSE AAM;
  ECGI site revision date (PDF metadata corroborates). All four ticket-04
  checkboxes now satisfied.
- **L3 re-derivation (statements-only, fresh opus): PROVED-WITH-CHANGES —
  counts as PASS after reconciliation.** All three parts derive independently;
  regularity sharpened (Darboux, weaker than C²); constant ¼ confirmed;
  π^{3/2} sign-violation example found independently (converges with the
  writer's). Seven changes, all hypothesis-explicitness: CH1 = π̄ ruling
  (already adjudicated); CH2 NEW — π̄ must be explicitly κ-free (conclusion
  FALSE otherwise; a first-order term appears); CH3 = kernel-through-posterior
  (already adjudicated); CH4/5 minimal regularity (improvement); CH6 A′_κ
  uniformity along π̄↓0 (the L3→L4 seam); CH7 if-not-iff (matches writer).
  Bonus supporting the π̄ ruling: under A(τ) the pooled share E[Π_κ] is
  exactly κ-invariant (mean-preserving spread). Card regeneration will fold
  CH1–CH3, CH6 into A(τ)/§4.4. Writer and re-deriver agree on substance —
  no adjudication conflict; L3 two-pass evidence COMPLETE pending ledger.
- **L4 re-derivation (statements-only, fresh opus): PROVED-WITH-CHANGES —
  PASS after reconciliation.** Legs 1-2 as stated; leg 3 with ONE added
  clause: (br-ii′) τ-invariance of the kernel h across thresholds — THE SAME
  GAP the T1 proof-reader found independently as "(br-v)". Adjudication:
  canonical name (br-v); A(br) becomes five clauses at regeneration; L4_proof
  and T1_proof cite it consistently. Also: (br-iv) SHARPENED to
  ρ(τ′)/ρ(τ) ≥ π̄_pr(τ′)/π̄_pr(τ) with ρ = ½A_{1/2}+A_1 provably κ-free
  (π̄ = π̄_pr/ρ — consistent with the π̄ ruling); (br-ii)'s trailing formula
  DERIVED not assumed; L3 citation redundant for leg 3 (chord product form
  direct from br-i+br-ii); C_h≤0 never used in leg 3 (no C_h=0 case split
  needed there); new H5 (Ω(τ′)<1) and H11 (common κ) made explicit;
  b_0<τ′ confirmed load-bearing. No writer-vs-re-deriver conflict — same
  conclusions, tighter hypothesis accounting. L4 two-pass evidence COMPLETE
  pending ledger (label target: PROVED under A(br) five-clause).
- **T1 retry fix LANDED** (fresh writer): H18 threshold-side smoothness closes
  T1-F1; H16 (no-feedback, numbered), H17 (=(br-v), T1-local); R1–R9 applied;
  five boxed displays byte-identical. Fresh checker dispatched (fix-round
  closure) + T1 re-deriver dispatched in parallel (statements-only via
  extracted T1_statement_sheet.md, committed).
- **Batch-1 repairs APPLIED, 18/18** (repair-b1, opus): L3 +H8 kernel clause
  +H9 D1-by-statement, Landau-Θ purged, two-derivations claim rewritten;
  L4 (br-iv) collapsed to support-point ruling with identity branch excluded,
  bare Δ purged, citations repointed; P1 h.11 closure form STRUCK (cardinality
  contradiction written out; definitional reading is the hypothesis), bare g
  → 𝒢_F, card §2.10 cites replaced by in-proof h.14 with card-gap flags,
  Step 5 split control-node/tower. Three near-substance flags all recorded
  conservatively, none resolved beyond mandate. Regeneration items now
  queued in-file: card payoff row (U_j), §4.3 Y-row ambiguity, §4.4 π̄ gloss,
  A(τ) kernel + κ-free-π̄ clauses, A(br) five-clause canonicalisation.
- **Core re-derivation (D1/L1/L2, statements-only, fresh opus): PASS.**
  L1 PROVED-AS-STATED (non-identification of the null cell proved, not
  asserted). D1 PROVED-WITH-CHANGES (Borel rider on non-Voice paths for
  part c; 𝓘_H content must be filled — card §4.3 has "—"). L2
  PROVED-WITH-CHANGES (A7′ consumed ALMOST SURELY on the flagged set — the
  only coherent on-path reading with continuum tuples; + A2/table
  restrictions, D1, explicit entry-rule condition as bookkeeping).
  Independent findings: ∂_κΩ=0 free at fixed policies but asserted nowhere
  (the §4.4 𝒮-row needs it); M_P κ-differentiability supplied by NO card
  hypothesis (card gap; T1 carries it as H7 in-proof); Lusin–Souslin
  confirmed fallback-only; §4.3 P_ND row wording fix ("not-yet-disclosed").
  Two L2 placebos specified (M_P and J must MOVE with κ) so the invariance
  check can't pass vacuously — ticket 28 should adopt them.
  **Two-pass evidence now COMPLETE for D1, L1, L2, L3, L4.** P1 and T1 pend.
- **Ticket 25 BUILD LANDED and accepted** (opus builder; 8 modules, 2,040
  lines + smoke_output.txt). Gate PASS (feasible 826,686 hist × 12 types =
  9.9e6, 10× under limit; 0.44 s/eval). Smoke: equilibrium residual 0.0
  payoff-scale; Ω=13.84%, ω_a=61.15%, M_F=0.553pp, M_P=0.223pp; a7_cert
  passes (0 collisions); multiple_root_nodes=0 — STRUCTURAL: P = V̂ +
  m̃p/(1−p) has strictly decreasing RHS, so A5 is a consequence here
  (converges with P1's h.12 derivation). **L2 frozen-sweep range_κ M_F =
  0.0 bit-identical** (substantive PASS). M_P hump-shaped in κ; |C_h|/π̄²
  → 0.2219 (L3 quadratic clean). Six deviations all named, all accepted
  (off-path 1e-14 belief floor implements §3(vi); solver injected as arg to
  preserve purity guard; per-type accumulation instead of chunking; 241
  bracket grid for sawtooth gaps; independent Δ^act summation; Menu
  excludes τ,T). Findings for the lane: Q^F ≡ 0 at T=5 on this family
  (ticket 28's Q^F T-monotonicity check vacuous at T≥5 — use small-T column
  or record vacuity); A3 single crossing is a CALIBRATION fact on sawtooth
  gaps (P1 WHERE-IT-FAILS material).
- **T1 fix-round CLOSED.** Fresh checker: T1-F1 discharged (H18 delivers all
  four things Step 15 signs; scope claim verified — nothing consumes it;
  boxed displays unchanged). Four one-clause citation items N1–N4 applied by
  the orchestrator per the checker's close-after-edit recommendation (N2 was
  the π̄-ruling one: H14 leg 2 restated as the share inequality with (br-iv)
  carrying it to the endpoint). T1 proof-read evidence now PASS-equivalent;
  awaiting its statements-only re-derivation for the second pass.
- **T1 re-derivation (statements-only, fresh opus): PASS** (PROVED-AS-STATED
  parts A/B/B-local/C; PROVED-WITH-CHANGES only on the "equivalently"
  quantifier — the integrated/average reading, identical to what the fix
  round adopted; ledger row gains the quantifier at regeneration).
  Strengthenings: H6 derivable outright (S4); H18 confirmed non-load-bearing;
  (br-v) confirmed required AND independent of (br-i)–(br-iv) — third
  independent confirmation; O-1 numbers + proved W_T≤1 force C_T>1, so the
  window analogue of L4 leg 3 is REFUTED at calibration (positioning fact
  for the paper). **T1 two-pass evidence COMPLETE. Six of seven results done
  (D1, L1, L2, L3, L4, T1); P1 re-derivation pending.**
- **P1 re-derivation (statements-only, fresh opus): PASS as
  PROVED-WITH-CHANGES.** Architecture agrees with the writer (scalar pricing
  reduction; A7′ inverse elementary; Brouwer on 𝒯). h.11 binds twice
  (sequential optimality + off-path beliefs — drop it and the flagged round
  is a continuum-signalling game with generic FOC failure). h.12 trades for
  A5: A5 DERIVABLE (third independent convergence: P1 writer, builder's
  structural uniqueness, re-deriver's counterexample when m_0<0). MAJOR CARD
  FINDING: A2's "prices and payoffs bounded" is FALSE under Gaussian v +
  unbounded flagged region → A2′ (finiteness clauses unchanged; local
  boundedness + E[max|U|]<∞). Also: objective row missing (h.13-obj —
  matches batch-1 card gap; NB collides with writer's h.13 stake-ordering,
  rename at regeneration); A6 continuity genuinely assumed, repair named;
  §2 gains flag-terminates-pooled-round reading; A8 honestly a condition on
  the fixed point. **ALL SEVEN RESULTS NOW HAVE TWO-PASS EVIDENCE. Ledger
  pass + card regeneration dispatched.**
- **TICKET 27 LEDGER PASS EXECUTED (commit 627642c).** Seven moves:
  D1 | CONJ→PROVED; L1 | CONJ→PROVED (as-stated); L2 | CONJ→PROVED (A7′
  on-path a.s.); L3 | CONJ→PROVED under A(τ); L4 | CONJ→PROVED (legs 1-2
  outright, leg 3 under A(br) five-clause); P1 | CONJ→PROVED (A2′, A5
  derived, definitional round-2 set, m_0≥0, objective row); T1 |
  CONJ→PROVED at fixed policies ("equivalently" quantified on-average).
  Full log in research/model_v4/LABEL_LEDGER.md. Card regenerated: A2→A2′,
  A(τ)+(τ-i)/(τ-ii), A(br) recorded (br-i..br-v), m_0≥0 adopted, π̄
  reglossed, 𝓘_H filled, P_ND reworded, U_j row added, flag-terminates
  reading in §2, §9 gains the OPEN A(τ)-membership item + the C_T>1
  refutation fact. C1 stays CONJECTURE (ticket 29 in flight). Fable
  reviewed the full diff before commit — approved; the regeneration's one
  beyond-brief edit (§4.2 Borel rider) accepted as required by D1's
  re-derivation verdict.
- **Ticket 29 (C1) LANDED — REGION NOT EMPTY.** C1_proof.md (H1-H8; Neumann →
  inversion-free bounds → 4-group chain rule → dominance ⟹ ∂_r𝒮 ≤ −η_r) +
  t2_c1_region_check.py/.json EXECUTED (2.9h, 80 nodes, 0 errors, 4 PASS /
  0 FAIL / 8 RECORD). 18/80 nodes certify; largest contiguous block T=5,
  τ∈{50,70,90}pct, κ∈{0.65,0.75,0.85} (9 nodes, η_r med 0.374). L_ℛ ∈
  [0.264,0.501] everywhere. Failure anatomy: 56 nodes g_r^PE=0 (clock
  quantisation makes Ω locally constant in τ — discretisation artifact),
  4 genuine GE dominations, 2 negative margins at κ=0.55. T=10 degenerate
  (Ω=6.8e-4, the known H=T corner; finite-difference only, 34/40
  attenuating). Fine grid (0.01) declined honestly (8h+), recorded in JSON;
  grid used 0.10. Card-owner flags: §4.5 norm unfixed for |·| bars; L_ℛ sup
  domain unstated; companion inversion-using bound certifies 22 vs 18 —
  worth adding as a second bound. Proof-reader dispatched.
- **C1 pipeline complete except re-run.** Proof-read PASS (0 FAIL, 13
  reporting repairs — applied 13/13, one came out stronger than framed);
  re-derivation PASS as PROVED-WITH-CHANGES (route identical term-for-term;
  ADDED N1 norm convention — dual-pairing counterexample shows wrong norm
  silently voids certificates, auditor confirmed the CODE uses correct
  pairings; ADDED N2 two-sided neighbourhood, κ∉{0,1}; H8 confirmed unused;
  𝒮 vs 𝒮^GE naming split needed — card §4.4 binds 𝒮 to fixed-policy;
  bonus: ℬ_r^GE = O((1−L_ℛ)^{-3}) — certified nodes cubically bounded away
  from L_ℛ=1, checkable log-log slope 3). Adjudicated label plan: C1
  theorem → PROVED (region-as-hypothesis, N1/N2/𝒮^GE folded in); 18 nodes
  → NUMERICAL after the separate re-run. Executed at final ledger update.
- **Ticket 28 SCRIPTS LANDED (3.1h runtime), committed with honest FAILs.**
  D1/L1/L3/L4 all_pass. L2 core EXACT (all κ-ranges 0.0, both placebos
  live) with one ancillary FAIL: the implemented pooled cell violates
  A(τ)'s orientation (M_P hump-shaped). T1: factorisation to 3.5e-18, O-1
  benchmark + composition factors exact, window product ≤1 everywhere incl.
  H=12 interior column (Block-4 paranoia flag raised and traced to the
  corner), one FAIL: chord-magnitude bridge off ~4× (implied |A′_κ|≈1 vs
  ternary 0.25). P1: 23/27 multistart (4 corner nodes at π̄_pr=0 fail the
  payoff criterion; all 27 pass the cutoff criterion; h.11 buys nothing on
  this menu — E[Y]−P^F ≡ 0). COMBINED FINDING (L2-placebo + T1-block3):
  **the two-round pooled cell FAILS A(τ) at the implemented baseline** —
  the card's OPEN item resolves NO at this calibration; the conditional
  legs (L3, L4-leg3, T1-B) stay PROVED as conditionals; L4's SIGNS hold
  numerically regardless (zero violations). Q^F ≡ 0 at EVERY T on the
  pinned menu (vacuity recorded). H=12 L1 column absent (gate 1.19e8 >
  1e8, honestly declined). Batched re-runner (fresh opus) dispatched for
  all 8 scripts (~6.5h). Ticket-30 legs dispatched in parallel: model-note
  writer (model_v4.tex+md) and HANDOFF two-round update (marked
  pre-verification).
- **Ticket 30 legs landed; Fable coherence read (part 1) done.** HANDOFF
  two-round entry committed (window ATTENUATES at implemented calibration,
  W_T·C_T = 0.1818/0.1818/0.2055/0.4299/0.7724 at H=10, 0.1099/…/1.0000
  chord-route at H=12; reversal vs repo model explained via T1's iff; A(τ)
  honesty section; provenance nit fixed by orchestrator — JSON's embedded
  stamp string predates the build). model_v4.tex+md+PDF committed (16pp,
  xelatex clean; Fable adjudicated the P1 corner-FAIL gloss from "solver
  coverage" to "cause undiagnosed" — the check itself ruled out seed
  coverage by a 30-seed re-run). Coherence spot-checks PASS: handoff
  numbers byte-faithful to t2_t1 JSON (both H=10 and H=12 columns, 0 nodes
  above one); model-note ledger table matches card §6 (7 PROVED + C1
  CONJECTURE-pending). Awaiting the 8-script re-runner; then final ledger
  update (C1 move + evidence fold-in + pre-verification flag flip), bundle
  assembly, coherence read part 2, final report.
