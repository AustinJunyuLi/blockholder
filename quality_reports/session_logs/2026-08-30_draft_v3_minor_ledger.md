# draft_v3 minor-finding ledger — 2026-08-30 fix round

Disposition of all 76 minor/note findings in
`quality_reports/reports/2026-08-30_draft_v3_team_review_findings.md`, after the fix round
(blocking findings 1–5 are tracked in the findings report and the team-review brief, not here).
Dispositions: **FIXED-ALREADY** (landed before this session, in the stopped author's uncommitted
work), **FIXED-NOW** (landed in this session), **DEFERRED** (with reason). Line references are to
the current `draft_v3.tex` unless noted.

## intro-lit (18)

1. Abstract compresses the C1 node record — **FIXED-ALREADY**. Abstract now carries the card's
   wording: eighteen of eighty nodes, largest contiguous block of nine, "verifies neither the full
   hypothesis nor a nonempty region".
2. "Three legs" against §6.2's five substantive legs — **FIXED-ALREADY**. Abstract and
   Introduction now enumerate six substantive legs (timing split, bindingness dose, stake at
   filing, bounded null, matched DiD, bidder entry by liquidity).
3. Kyle–Vila wrong journal/volume/pages — **FIXED-ALREADY**. `draft_v3.bib` now reads *The RAND
   Journal of Economics* 22(1): 54–71, per the card.
4. Abstract silent on the A(τ) failure while quoting the window record — **FIXED-ALREADY**. The
   abstract now states that the chord restriction behind the threshold margin and the composition
   ratios is measured to fail at the same calibration.
5. "Cut it in half" conflating calendar and business days — **FIXED-ALREADY**. The Introduction
   now says "shortened it, from ten calendar days to five business days".
6. Four bibliography entries departing from the record — **FIXED-NOW**. The open part was
   Cetemen–Cisternas–Kolb–Viswanathan: unverifiable volume/number/pages removed and `note =
   {Forthcoming}` added this session. The other three parts were already landed before this
   session (Norli names Øyvind/Charlotte/Ibolya; Becht "Grant, Jeremy"; the Bebchuk author
   field).
7. BBJJ bunching bucket's business-day unit unstated — **FIXED-ALREADY**. The unit is now stated
   at both cites ("eight to ten business days").
8. Ordóñez-Calafí–Bernhardt stake "at the threshold" — **FIXED-ALREADY**. Now "the smaller of the
   threshold and its unconstrained optimum, the threshold acting as an upper bound".
9. Admati–Pfleiderer liquidity sign — **FIXED-ALREADY**. Now "liquidity blunts the disciplining
   threat of exit by making exit less informative".
10. Window record's corner caveat absent from the 18–77 percent sentence — **FIXED-ALREADY**. The
    sentence now carries the caveat and points to §5's interior re-run and its route.
11. "The paper says this once" not true of the A(τ) record — **FIXED-ALREADY**. The phrase is gone
    from the Introduction; the conclusion's "stated once" refers to P1's applicability, the
    correct referent.
12. "At most T days later" versus the model's exact-deadline convention — **FIXED-ALREADY**. §2.1
    now adds "The model takes the deadline itself as the filing date, so filing early is outside
    what it claims."
13. 13G population narrower than the record — **FIXED-ALREADY**. §2.1 now names the three eligible
    classes (exempt investors, qualified institutional investors, passive holders below 20
    percent).
14. "Cleanest dated change" superlative — **FIXED-ALREADY**. The superlative is gone.
15. Kyle–Vila "disclosed and undisclosed trades" — **FIXED-ALREADY**. Now "split the market's
    inference between pooled and revealed trading but disclaim disclosure requirements by
    assumption".
16. "The others abstract from control transfers by name" overstating Admati–Pfleiderer —
    **FIXED-ALREADY**. §2.2 now distinguishes the three: Maug relabels, Kahn–Winton and
    Faure-Grimaud–Gromb set control transfers aside in terms, Admati–Pfleiderer simply has no
    bidder.
17. Draft dated a day before the record — **FIXED-ALREADY**. The date now reads 30 August 2026.
18. Introduction's T1(A) omitting the positive-sensitivity hypothesis — **FIXED-ALREADY**. Now
    "with the two cells both on path and the pooled cell's liquidity sensitivity strictly
    positive".

## model (11)

19. A3 record generalising the ticket-34 sweep — **FIXED-ALREADY**. rem:A3record now records the
    one probed node plus the three-node sweep, with the third node's no-fixed-point-on-any-edge
    form stated separately.
20. A6 record dropping the card's three scope flags — **FIXED-ALREADY**. rem:A6record now carries
    "not itself computed by any probe" (not curated), "a single-pass derivation and has not been
    independently checked" (not gate-checked), and the shipped-family scope sentence.
21. Nine environment titles printing MODEL_CARD section IDs — **FIXED-ALREADY**. Titles now read
    e.g. "No feedback: no within-window re-optimisation" and "TR: the primitive table
    restrictions"; no card §-numbers print.
22. Self-description of where the numerical records sit — **FIXED-ALREADY**. §3.5's lead-in now
    places rem:A3record and rem:A6record beside the hypotheses, rem:AtauRecord with the consuming
    results, and rem:P1record against Proposition 1, with no miscounted list.
23. Definition 3.7 asserting A6's continuity as definitional — **FIXED-ALREADY**. def:theta now
    states that single-valuedness, continuity and the self-map property are "the content of
    Assumption A6 rather than of this definition", pointing at rem:A6record's measured failure.
24. A3 middle-excursion figures being the grid maxima — **FIXED-ALREADY**. The remark now notes
    the refined per-interval maxima (3.07 and 2.69 × 10⁻⁴) and that the failure is understated.
25. A5 paragraph attributing the two root-count counterexamples to two of the three confirmations
    — **FIXED-NOW**. Now "Three independent calculations support this, one of them also recording
    two counterexamples: one producing zero roots and another producing three, once m₀ < 0."
26. Remark 3.5 stating the engagement-cost equivalence without the continuation-cost clause —
    **FIXED-ALREADY**. rem:Ctiming now splits the two readings and names what the
    continuation-cost hypothesis buys under the plan-completion reading.
27. A6 record dropping the coverage caveat and the second repair — **FIXED-ALREADY**. Both repairs
    are now named (t-constrained game with Kakutani and t ↓ 0; cutoff-indexed concentration
    family), and the coverage sentence ("probes at one node per claim class, together with the
    twenty-seven-node census, and no sweep over (κ, τ, T)") is restored.
28. (br-ii)'s scope sentence dropped — **FIXED-ALREADY**. The clause now states it is written
    against the reading h = π p(v̂, π), repairs the ambiguity rather than adding an independent
    restriction, and names the same object as clause (τ-i).
29. A(τ)'s C_h = 0 parenthetical dropped — **FIXED-ALREADY**. The assumption now states "the case
    C_h(π̄) = 0 has to be handled explicitly wherever it is consumed".

## existence (10)

30. Step 7(iii) using the superseded two-adjacent-roots argument — **FIXED-ALREADY** by the
    re-transcription of Appendix B from `proofs/P1_proof.md` at 65b8db3: the global form
    ("ρ′(P) < 0 for every P ≥ A, not merely at roots") is now printed.
31. Step 3 heading / Step 6 opening treating the flagged family as necessarily a continuum index
    set — **FIXED-ALREADY** (re-transcription): "the flagged family is empty or uncountable, and
    in neither case a finite nonempty indexed family".
32. Step 9(b) dominated-convergence credit and Λ_k = 0 branch — **FIXED-ALREADY**
    (re-transcription): the credit now runs L_j ≤ 1 with Gaussian integrability of |s| φ_s under
    clause (TR-i); the h.2 credit is gone.
33. Step 9(b) perturbation weight without the index range — **FIXED-ALREADY** (re-transcription):
    the display is restricted to integers n ≥ J with the n < J parenthetical.
34. Step 20's A8 restatement conventions — **FIXED-ALREADY** (re-transcription): the step adopts,
    for that step alone, inf ∅ := +∞ and inf ℝ := −∞, explicitly distinct from Step 13's
    totalisation.
35. S4 proof sketch saying Part E verifies continuity of the outer map — **FIXED-ALREADY**. The
    sketch now derives only the weakly-ordered and self-map halves from A3 and takes the bracket
    and continuity from A6.
36. S4 sketch's six disclaimers not matching the appendix — **FIXED-ALREADY**. The sketch's list
    now matches the appendix's six, with the κ = 1 withdrawal inside boundary extension.
37. S4 gloss on the upper-set engagement-flag hypothesis dropping "exactly" — **FIXED-ALREADY**.
    The gloss now reads "equal one *exactly* on an upper set" with the threshold index j_a.
38. rem:P1record rounding the payoff-scale residual range below the card's upper end —
    **FIXED-ALREADY**. The remark now carries 3.1 × 10⁻⁴ to 1.5 × 10⁻³ against the 10⁻⁹
    criterion.
39. def:theta building continuity into the definition (existence reviewer's flag of the same
    line) — **FIXED-ALREADY** (same repair as item 23).

## outcomes (7)

40. Table 1 caption asserting a strict inequality its H = 12 column violates — **FIXED-ALREADY**.
    The caption now states the weak form ("product W_T C_T ≤ 1 (attenuation), with no τ node
    above one"); the H = 12 chord-route sentence added this session is blocking-finding scope,
    tracked in the brief.
41. "Returning exactly 1" more precise than the record — **FIXED-ALREADY**. rem:T1record now says
    "returning 1.000 to within 3 × 10⁻¹⁶".
42. D1 and L1 result-status lines over-stating A5's cleanliness — **FIXED-ALREADY**. Both status
    lines now state that the retained cutoff-composition continuity clause is not consumed and
    point to its adverse evidence in rem:A6record.
43. Figure 1's printed title asserting attenuation — **DEFERRED**. The title is baked into
    `numerical_output/fig_disclosure.pdf`, which this round holds read-only; regenerating it is a
    `pyfig` pipeline change outside the round's scope. Flagged in the brief for Austin.
44. Figure 1 caption identifying the curves as "upper" and "lower" though they cross —
    **FIXED-NOW**. The caption now identifies the curves by line style and markers (solid with
    circle markers, dashed with square markers) and states that they cross near κ = 0.73.
45. "Cutoffs frozen at its baseline" describing only one of the four O-1 weights — **FIXED-NOW**.
    The prose now states that k₁ and k₀ stay at the baseline equilibrium throughout and only k_D
    moves, across the four values that generate the flagged weights.
46. Figure 1's opaque legend hiding the peak — **DEFERRED**. Same figure-PDF reason as item 43.

## empirics-readiness (13)

47. Power numbers quoted on their most optimistic basis; the SPEC-mandated second MDE missing —
    **FIXED-NOW**. The open parts landed this session: the stake leg's 0.85 pp and Candidate B's
    1.1–2.3 pp now say "on the post-re-parse projection". The DiD leg already quoted all three
    MDEs (5.8 pp today, 4.4 pp S1, 9.9 pp S2) with the N ≈ 4,950, w ≈ 0.394 basis named, and the
    referee checklist already said "after the re-parse".
48. Trivedi called the only published estimate — **FIXED-ALREADY**. Now "the only working-paper
    estimate of the same first stage"; the body and the bibliography agree.
49. Incumbent-defence moderator asserted buildable and misnamed — **FIXED-ALREADY**. The checklist
    now states rights-plan coverage is untested, names the best-effort EDGAR items, and carries
    the signed-bias fallback.
50. Bimodal pre-rule delay distribution attributed to BBJJ — **FIXED-ALREADY**. §6.1 now states
    the pre-rule distribution was not bimodal, with the mass rising into the deadline bucket.
51. Conclusion's ω_a question hanging the one-round regime boundary on the window margin's
    composition sign — **FIXED-NOW**. The rewritten conclusion carries ω_a as an open calibration
    input that is nowhere load-bearing; the 0.343 construction is gone from the conclusion.
52. Dropped sentence break in the Table 2 caption — **FIXED-ALREADY** (the stopped author's
    caption repair).
53. Main-sample cut at the structured-data mandate absent — **FIXED-ALREADY**. §6.2 now ends the
    main sample on 2024-12-17 and reports 2025 as an extension with its own parse-rate table.
54. Spec's headline designation reopened without acknowledgement — **FIXED-ALREADY**. Abstract and
    Introduction now say "The timing split is the specification's default headline; final
    selection remains pending."
55. Dose construction omitting the repeat-filer requirement and the imputation route —
    **FIXED-ALREADY**. The dose now requires at least two pre-period initial 13Ds, with the
    leave-one-out stratum mean confined to a robustness row.
56. RUNUP5 described as a fixed five-day window — **FIXED-ALREADY**. Now "a fixed
    five-trading-day window from the trigger".
57. Pre window said to end at the adoption date — **FIXED-ALREADY**. Now "2022-01-01 through
    2023-10-09", with 2023-10-10 beginning the separately reported stub.
58. Bidder-entry-by-liquidity leg with no paragraph in §6.2 — **FIXED-ALREADY**. Paragraph (f)
    now specifies both the within-13D interaction and the matched triple difference, with the
    8.8 / 19.8 pp rule-of-thumb MDEs labelled weakly powered projections.
59. Interpretive rule attributing the whole DiD estimate rather than the excess — **FIXED-ALREADY**.
    Now "Only an estimate's excess above 3 percentage points can be attributed to incumbent
    defence or selection; the first 3 points remain compatible with accumulation."

## global (16)

60. Figure 1's embedded title and axis label contradicting caption and text — **DEFERRED**. Same
    figure-PDF reason as item 43; flagged in the brief.
61. MODEL_CARD section numbers printed in environment titles — **FIXED-ALREADY** (same repair as
    item 21).
62. Verification-process register in paper voice — **FIXED-NOW**. This session's sweep removed the
    remaining instances ("changes any result's status", "stays proved, their proofs untouched",
    "executed committed check", "it moves no label", "the label rests on…", the withdrawn-and-
    re-verified parenthetical, and kin); the post-sweep scan over the register vocabulary is clean
    outside the file's `%`-comment provenance header.
63. "Not a fifth honesty category" dangling reference — **FIXED-ALREADY**. The phrase no longer
    appears.
64. Table caption broken mid-sentence (tab:fact1) — **FIXED-ALREADY** (same repair as item 52).
65. Appendix B Step 18 asserting and then withdrawing a Kakutani conclusion — **FIXED-ALREADY** by
    the re-transcription: the step is now titled "a possible route, outside the proposition and
    not established here" and draws no conclusion it retracts.
66. Φ carrying two meanings — **FIXED-NOW**. Appendix C's implicit-function map is now Ψ; Φ is
    the standard normal c.d.f. everywhere (Φ_s the signal c.d.f.), honouring Appendix B's
    reservation.
67. ϱ carrying three meanings — **FIXED-NOW**. The main-text chord scalar is now ρ_ch(τ), the
    Appendix B pricing residual is 𝔯_ℐ, and the Appendix C parameter radius is δ_ϑ; no ϱ remains.
68. Malformed author field printing "Jr. Jackson Robert J." — **FIXED-ALREADY**. The field now
    reads `Jackson, Jr., Robert J.`.
69. "Three legs" in abstract and §1 against §6.2's six parts — **FIXED-ALREADY** (same repair as
    item 2; the conclusion's list was completed to six this session under item 2's scope).
70. §5.5 and §7 enumerating different "three open questions" — **FIXED-NOW**. §5.5's enumerate now
    carries the canonical three (the A(τ) support condition; existence assumptions including the
    separating-plan incentive-compatibility question; constructive repair of A6's scoped
    continuity problem), and the conclusion names the same three explicitly, with ω_a separated
    as an open, non-load-bearing calibration input.
71. Figure 2's embedded title, axis label and legend placement — **DEFERRED**. Same figure-PDF
    reason as item 43 (`numerical_output/fig_fact1.pdf`).
72. 26 labels defined but never referenced — **DEFERRED**. Harmless (nothing breaks, no "??"
    prints); a 26-site tidy pass is deferred to keep this round's diff intended-only.
73. Seven uncited bibliography entries; one editorial note — **DEFERRED-with-reason**. The seven
    uncited keys are dead keys that never render; pruning them is the author's editorial call,
    deferred to keep this round's diff intended-only. (The editorial note half is cured: the
    Trivedi "Not peer reviewed" note was removed from the bib this session; the judgement already
    lives in the body.)
74. Back et al. quotation without pinpoint page; its T colliding with the window symbol —
    **DEFERRED**. Note-level readability: the quote self-labels its T as the trading horizon, and
    no pinpoint page for it is in the frozen record's extracts.
75. Three proof-local symbols reusing shapes (ϖ, 𝒟, 𝒩) — **DEFERRED**. The finding itself records
    that none is a defect under the standing proof-local notation convention; a rename would touch
    proof text for no defect.

## orchestrator (1)

76. "Only if and only if" in the conclusion — **FIXED-NOW**. The sentence now reads "the window
    margin attenuates if and only if a weight ratio times an unsigned composition ratio is at most
    one".

## Tally

FIXED-ALREADY: 57 · FIXED-NOW: 11 (items 6, 25, 44, 45, 47, 51, 62, 66, 67, 70, 76) ·
DEFERRED-with-reason: 8 (items 43, 46, 60, 71, 72, 73, 74, 75).
