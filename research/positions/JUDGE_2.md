# JUDGE 2 — Ticket 03 positioning tournament (2026-08-19)

Adversarial check completed: reading list + all five proposals read in full; ≥3 decision-critical
citations per proposal opened in the owning card and confirmed or refuted (log at the bottom).
No proposal or card edited. No commit.

## Score table

| Proposal | A Whitespace | B Anchoring | C Main result | D Empirics | E December | F Continuity | Total | Rank |
|---|---|---|---|---|---|---|---|---|
| P1 window × premium (tender game) | 5 | 4 | 4 | 3 | 5 | 5 | **26** | 3 |
| P2 rule-as-partition (info design) | 5 | 4 | 4 | 4 | 5 | 5 | **27** | **1** |
| P3 Kyle deadline (MCS) | 5 | 5 | 4 | 4 | 4 | 4 | **26** | 4 |
| P4 Feb-2024 control-outcome DiD | 5 | 4 | 4 | 5 | 5 | 4 | **27** | **2** |
| P5 purpose partition (13D/13G) | 3 | 4 | 3 | 3 | 4 | 4 | **21** | 5 |

P2 and P4 tie at 27; tie broken on ADR-0003's weights (whitespace, fact-anchoring, deliverability)
and the referee findings in the spec — see the justification below. P1 and P3 tie at 26; broken by
risk-adjusted deliverability (P1's theory is half-proved in-repo; P3's is all-new).

## Per-proposal reasons

### P1 — window length × takeover premium
- **A (5).** Claims W1 (map: CLEAR) with W12 as mechanism (CLEAR on mechanism); every disposal
  checked and confirmed — Back's window has no premium and collapses into σ²T (p. 1453), BL's
  premium is degenerate (Lemma 2, p. 1877) with the interaction handed to future work (p. 1891),
  GMM own the stake path (Prop. 7, p. 28), CL own the sign (−13.69% marginal / −0.60% GE). Honestly
  declines W8b; flags the BLV Dec-2025 standing risk.
- **B (4).** Anchor verified: 5-business-day deadline effective 2024-02-05 (institutional card §1,
  pp. 1, 10); Table 3 p. 189's 20%-not-complete confirmed; late rate ≈29% at p. 178 n. 695
  confirmed. Two slips: the wedge formula prints one ρ where D7 (`thm:d7-A3`, `rem:d7-fold`) has
  ρ²(1−θ)λΔ_eng (one ρ is folded into D̃_eng — monotonicity unaffected); and Greenwood–Schor's
  18.1% (p. 372, Table 6) is *acquired* within 12 months (delisting-coded), not "bid".
- **C (4).** Statement is precise and signed, with the pivotality discontinuity as a signature no
  Back-et-al. variance rescaling produces. Route is half-proved in-repo (D7's λ jump at 1−τ_c
  confirmed in `D7_takeover_game_microfound.tex` line 249) plus a standard-class Kyle accumulation
  block. Label PROVED-on-named-primitives is realistic for the tender half. Risk (measured premium
  divides by a run-up-capitalizing price, `prop:d7-afs`) named honestly.
- **D (3).** Weakest checklist of the top four. The primary level test regresses the premium on
  stake-at-filing — the model's own endogenous object — with no control group and no bounded null;
  the change test is an honestly-labelled bounded before/after, but anticipation (adopted
  2023-10-10) is unaddressed, no pre-trend and no parser audit are mentioned. Confound list and the
  two placebos are strong; power arithmetic is the right order.
- **E (5).** D7 half proved and check-verified; the `params_with_endogenous_wedge` hook exists;
  12–15 weeks against ~19, with a NUMERICAL fallback that leaves the tender-game half standing and
  a level-test-plus-bound fallback if the premium subsample undershoots.
- **F (5).** The wedge (m₁−m₀), D7, κ as driver and the partition are draft_v2's spine; drops
  (four-action menu, R1, welfare, D8) are each justified by an occupied cell.
- **Biggest flaw:** the strict result rides on the pivotality jump at 1−τ_c, which at realistic
  6–10% 13D stakes forces τ_c to be read as a 90% squeeze-out / 10% blocking threshold — a referee
  can call the jump an artifact of the equal-treatment, one-shot-fringe primitives.
- **Steal:** the discontinuity-at-pivotality signature as the answer to Back et al.'s isomorphism —
  the one object in the tournament a σ²T rescaling provably cannot produce.

### P2 — the rule is the partition
- **A (5).** Claims W3 (map: CLEAR with a named boundary) and respects both boundary wordings
  verbatim (Kyle–Vila own the un-keyed split; Zeng owns the insider leak — "pooled for the
  price-setting market"). W11 extension (NARROW) disposes of OCB correctly (Prop. 4, p. 2847 as
  template). Chabakauri named as the uncarded standing risk. Every nearest-row disposal (CCKV,
  Corum–Levit, OCB, Corum, Back, CDF 2016) confirmed against the map.
- **B (4).** Anchor verified (33-11253 §1, pp. 1, 10); Maug p. 73 and Zeng p. 1310 confirmed;
  sample counts (~2,849 pre / ~1,048 post) match `empirical_feasibility.md` §1.3 exactly; CDF ~3%
  and Zeng 2.8% run-up magnitudes confirmed. Two imprecisions: the CCKV sentence "No agent in the
  model ever learns that a blockholder holds a block" is quoted at "p. 11" — the card records it as
  its own §6(a) summary, with textual support at fn. 16, p. 15 (p. 11 is Q4's page); and §9's
  "CCKV's Theorem 1 (p. 17) warns order-flow inference need not be monotone" mischaracterizes a
  *predictability* theorem (E[θᴸ|F₀] ≠ 0, card R3/Q8).
- **C (4).** Five-part statement, each piece routed to proved draft_v2 machinery (Brouwer
  existence, disclosed-branch invariance, `lem:d1-variance`) — the digest independently rates the
  fixed-cutoff step "days, not weeks". Layered labels (PROVED at fixed cutoffs / region-certified
  GE / NUMERICAL off-region) are the most realistic in the field. Named risks are the right ones
  (interior crossing; D8-style GE sign flip). Held back from 5 by its own §9: the fixed-cutoff
  attenuation is nearly mechanical, so the contribution's weight sits in the pooled cell.
- **D (4).** The run-up/filing-CAR split by κ × Post is sharp, runs on disk data in ~1 week, and
  carries a real placebo (pseudo-triggers at TD−63) plus the full confound list including Zeng's
  non-neutral 1–13-day screen. Pre-rule slope serves as the bounded null. Two gaps: no parser audit
  beyond the fix, and the December-runnable leg measures information revelation, not a control
  outcome — the premium leg is specced only.
- **E (5).** 7–11 weeks of work against ~19, mostly reassembly of proved pieces; the fallback
  (representation + fixed-cutoff attenuation + split empirics) is the only one in the tournament
  that is *already a full draft*.
- **F (5).** The most literal descendant: CONTEXT.md calls the partition "the paper's identity",
  and P2 derives draft_v2's ad-hoc D = 1{q = +1} branch structure from the rule's two keys (τ, T).
  κ, bidder entry, the D7 wedge and the honesty labels all survive.
- **Biggest flaw:** the headline attenuation is close to an accounting identity at fixed cutoffs —
  if the pooled-cell content (where GE can flip signs) doesn't carry weight, a referee calls it a
  decomposition, not a mechanism.
- **Steal:** the two-cell premium decomposition with a κ-invariant flagged cell — the cleanest
  possible statement of why the *rule*, not the trader, moves the liquidity-sensitivity.

### P3 — the filing deadline as a partition device
- **A (5).** Claims W5 (CLEAR, boundary respected verbatim: never "non-fixed horizon", always "a
  legal filing window with a partition attached") and W6 (CLEAR; the Massa–Xu sentence matches the
  map's instructed wording). Disposals confirmed: Back p. 1453, CDF p. 1464, CCKV pp. 10/35, GMM
  Prop. 7. W9 sidestepped explicitly and correctly.
- **B (5).** Cleanest anchoring in the field, every item verified: §1 pp. 1/10; Table 3 p. 189's
  80%; Table 6 pp. 225–226's Amihud 0.13→0.08 across constraint columns (the bite-liquidity
  covariance is real and in the right direction); p. 178's ≈34% file-on-deadline; CDF's Item 5(c)
  at JF p. 1556; Massa–Xu's slope at Table 7, p. 1482; Trivedi §7 for 13G selection.
- **C (4).** Increasing-differences statement is precise and the MCS/Riccati route is classical and
  credible. Two soft spots: the control outcome enters only as "any outcome monotone in the flagged
  stake" — borrowed monotonicity, so the control-outcome content is thinner than P1's; and the
  terminal flag invites manipulation of what the filing reveals, which can break single-crossing
  globally (named honestly, with the Item-5(c) mechanical-report mitigation its author flags as the
  most contestable choice).
- **D (4).** κ-slope interaction with the pre-rule slope as bounded null; Trivedi's null level
  effect correctly re-purposed as protection for κ-as-pre-treatment; the 13G-run-up placebo is
  valid and clever (13G deadlines unchanged until 2024-09-30, institutional card §1); anticipation
  and the Zeng screen handled. Gaps: formal MDE deferred to the spec, no pre-trend or parser audit.
- **E (4).** 8–11 weeks and no new data, but the theory is entirely new (5–7 of those weeks) with a
  named global-failure mode; the fallback (region theorem + NUMERICAL off-region) is the known D8
  pattern, which keeps it at 4 rather than 3.
- **F (4).** Triad intact and D7 reused post-flag, but the one-shot ternary trading stage of
  draft_v2 becomes a multi-period linear-Gaussian Kyle market — a real change of trading technology
  a supervisor will notice.
- **Biggest flaw:** the clean cross-partial wants the filing to be the bidder's dominant
  information source while the pooled-state price path is public; if the bidder reads prices, the
  stake channel attenuates and the result survives only on a region.
- **Steal:** the 13G-run-up placebo (deadlines unchanged until 2024-09-30) and the
  Trivedi-null-protects-κ move — both transplantable to any Feb-2024 empirical leg.

### P4 — Feb-2024 control-outcome DiD
- **A (5).** Claims W2, quoting the map's rating exactly ("CLEAR on the cell; hard on execution"),
  and answers both named execution warnings: 13G rejected as control (selection on intent, rule-
  responsive — Trivedi §7) in favour of matched never-targets; the power cap converted into the
  bounded-null headline. Disposals of Trivedi (wrong object), Polk (no control group), the author's
  proposal (no untreated group) and Bishop (asserts, never estimates) all confirmed. W13 fallback
  correctly rated.
- **B (4).** Fact 1 (35.7%→75.6%, median 7.0→5.0 bd) confirmed against `empirical_feasibility.md`
  §1.1; SEC Table 3's 3%/7-per-year cap and Table 2's 20% non-corporate-action share confirmed;
  Greenwood–Schor p. 372, Dass's fn. 27 "<19 treated acquirers" (matches the verifier-corrected
  card), the proposal's PROVED R1, Zeng's fn. 13 screen and BBJJ's Q20/pill moderator (pp. 28, 31)
  all confirmed. One bad phrasing: "(t>3; trivedi §3 R2)" reads as a claim about the statistic —
  the card has t = 2.69 with the author's own caveat that it does *not* clear the HLZ hurdle of 3.
- **C (4).** The main result is an empirical statement with a bound, plus a companion model signing
  the per-campaign effect under one stated condition, built from proved pieces (proposal R1's
  quadratic cost, D7's λ). ESTIMATED + PROVED-conditional is the most honest label set in the
  field; the named risk (power) is the right one. Not a 5: the theory leg is a signing exercise,
  not a result, so the paper's theorem content is thin by design.
- **D (5).** The only proposal that answers every checklist item on a control outcome with data in
  hand: a real control group (3:1 matched never-targets) *and* a bounded null that is itself a
  result (SEC Table 3 ⇒ population ATE ≤ ~3 pp); exhaustive confounds with dates (EDGAR cut-off,
  adoption-anticipation, T+1, 13G compliance, XML, BBJJ's defence channel with a signed-bias
  argument); computed MDEs (9–10 pp; 6–7 pooled; premium leg honestly descriptive per Dass's
  power failure); ≥500 placebos; a quarterly pre-trend event study whose failure blocks causal
  language; a 30-filing parser audit with busday asserts.
- **E (5).** A 16-week week-by-week plan with no theory risk and every failure mode pre-assigned a
  fallback (parser fix fails → Feb–Dec 2024 post leg; matching yield → W13 success coding; premium
  too small → pre-committed descriptive). The most certain December package of the five.
- **F (4).** The triad is intact and the design is literally draft_v2 §6's bid-hazard prediction
  grown into a design, with the D7 wedge recognisable — but the paper's centre of gravity moves
  from theory to empirics, and the core model is the thinnest of the top four.
- **Biggest flaw:** the DiD coefficient (as opposed to the bound) is exposed to rule-responsive
  selection into the treated population — the rule changes who files, so the treated group's
  composition shifts by construction; and the whole position re-anchors on the experiment the
  referee review flagged as used by three other papers.
- **Steal:** the bounded-null-as-headline move ("small footprint *because the tail is small*") —
  any empirical leg, including the winner's, should carry its version.

### P5 — the purpose partition (13D vs 13G)
- **A (3).** Claims W7, rated NARROW and — uniquely — *provisional*: the named card (AFS) is
  disposed of correctly (the declaration-vs-information-set distinction is verbatim in AFS card
  §7; fn. 16, p. 34 confirmed), but the walled Payne-Mann paper is, per its abstract, a
  control-outcome result keyed to exactly this split, and P5's own contingency section concedes
  that "first" dies if the abstract holds. No other finalist carries an undisposible occupancy
  risk on its headline cell.
- **B (4).** Anchors verified: the 20% override (EFZ n. 17, printed p. 14), NACCO v. Applica (EFZ
  p. 11), Zeng's purpose taxonomy (36.6/43.3/20.0, p. 1315), EFZ's 0.7% 13G CAR, GS's 18.1/7.2.
  One gloss presented as a citation: Zeng's Q1 (p. 1303) states the purpose split under Rule
  13d-1(a); P5's "Rule 13d-1(b)/(c)" is its own (legally correct) attribution, not the card's.
- **C (3).** The statement is precise and the labels honest, but the proof route covers only the
  pricing half: draft_v2's Prop 2/Prop 3 posteriors and the invariance lemma price the flags, yet
  the *declaration equilibrium* — who chooses 13G vs 13D at a fixed economic state, with
  mislabelling risk as the cost — is not in draft_v2's machinery (its D is mechanically tied to
  q = +1, not chosen), and P5's 2–3-week theory budget does not price that gap. At fixed cutoffs
  the load-bearing result is again near-mechanical (κ-invariant flagged + κ-variant pooled).
- **D (3).** The workhorse leg (entry ~ purpose flag × lagged Amihud) is exactly the design EFZ
  concede is uninstrumented (fn. 27, p. 1473 — confirmed), with selection into 13D as the object
  rather than a controlled nuisance; the sharp leg (the 20% boundary) is power-poor ("thin bins",
  its own §9) and manipulation-exposed, with no event count given for override-bound filers
  2022–25. Placebos (EFZ's 0.7% CAR, QII 13Gs) are thin; no pre-trend in a cross-sectional design.
- **E (4).** Cheapest plan (7–9 weeks) with a genuinely credible fallback (theory alone; empirics
  revert to the W6 slope design on the in-hand 13D sample); 13G enumeration is a fetcher flag
  change per the feasibility audit. Docked for the underbudgeted declaration-equilibrium theory.
- **F (4).** Blockholder, κ, partition, bidder entry and D7's λ all recognisable, and dropping the
  Feb-2024 anchor is ADR-0003-licensed — but the window margin, draft_v2's most concrete rule
  object, leaves the paper with it.
- **Biggest flaw:** the headline "first" is hostage to an unreadable walled paper, and the
  workhorse empirics are the design the literature's own card concedes is uninstrumented.
- **Steal:** the pre-committed Payne-Mann contingency structure (replicate-as-validation, then add
  slope and model) — the template for how the winner should handle its own standing risks (BLV's
  Dec-2025 revision, Chabakauri).

## Near-identical positions

P1 and P3 are close cousins: both put window *length* in the theory and the Feb-2024 change in the
empirics, both accumulate under Kyle-flavoured noise and hand the flagged stake to a D7-style
post-flag stage. They differ in tool (tender-game discontinuity vs monotone comparative statics)
and headline cell (W1+W12 vs W5+W6), so they are substitutes, not complements — at most one should
survive, and P1's proved half edges it. P2 overlaps both on the partition but is distinct in object
(the information structure itself).

## Ranking and justification of the top two

**1. P2 (27) — winner. 2. P4 (27) — runner-up (tie broken). 3. P1 (26). 4. P3 (26). 5. P5 (21).**

P2 wins the tiebreak on ADR-0003's own weights. On whitespace it occupies the identity cell itself
(W3, CLEAR) with both named boundaries respected verbatim — the strongest positional claim
available, since CONTEXT.md names the partition as the paper's identity — while P4 occupies a
design cell (W2, CLEAR) on the anchor the referee review flagged as crowded. On deliverability,
P2's theory is reassembly of proved draft_v2 machinery (the digest independently budgets the
fixed-cutoff step in days), its runnable empirical leg is one week on disk data, and its fallback
is already a full draft; P4 has no theory risk but its core model is the thinnest in the field.
Both referee findings in the problem statement — "modelling judged messy" and "anchored on a
natural experiment already used by three other papers" — cut for P2 and against P4.

P4 is the runner-up because it is the best *empirical* design in the tournament and it is not
close: the only proposal answering every referee-checklist item (real matched control group,
bounded null as itself a headline, dated confounds, computed MDEs, placebos, pre-trends with a
causal-language circuit-breaker, parser audit) on a control outcome, on data in hand, with a
16-week plan and pre-assigned fallbacks. It loses the top spot because its theorem content is thin
by design, its DiD coefficient (unlike the bound) is exposed to rule-responsive selection into the
treated population, and a position built on the Feb-2024 anchor earns no bonus for existing — the
cell is CLEAR, but the framing fight ("three other papers use this shock") is one P2 never has to
have. The natural synthesis — P2's partition core with P4's bounded-null empirics as its
control-outcome leg — is exactly what the author's checkpoint should consider.

## Verification log (decision-critical citations opened and checked)

- **P1:** institutional card §1 (pp. 1, 10 — confirmed), §4.4 Table 3 p. 189 (20% — confirmed),
  §4.1 p. 178 n. 695 (29% — confirmed); `greenwood_schor` R7 (18.1% *acquired*, p. 372 — object
  slip found); `burkart_lee_2022_rfs` R3/R21/§7 (Lemma 2 p. 1877, IA Prop 1 ε-channel, "cite R21,
  say ours comes from the partition" — confirmed, P1 complies); D7 .tex (λ jump at 1−τ_c confirmed;
  ρ² vs ρ slip found); `celentano_levine` via INDEX §4.4 (−13.69% / −0.60% — confirmed).
- **P2:** `cetemen_..._2026_jf` §6(a)/Q4/Q8 (p. 11 misattribution of the "No agent" summary found;
  Thm 1 = predictability, not monotonicity — mischaracterization found); `zeng_2026_ras` R1 (2.8%
  run-up — confirmed), Q5 p. 1310 (confirmed); `maug_1998_jf` via INDEX §4.13 (p. 73 — confirmed);
  `empirical_feasibility.md` §1.3 (2,849/1,048 — confirmed); draft_v2 digest (existence, invariance,
  `lem:d1-variance`, "days, not weeks" — confirmed).
- **P3:** institutional card §4.4 (80% — confirmed), §4.5 Table 6 pp. 225–226 (Amihud 0.13→0.08 —
  confirmed), §4.1 p. 178 (34% — confirmed); `collin_dufresne_fos_2015_jf` Q2 (Item 5(c), JF
  p. 1556 — confirmed); `massa_xu_2013_jfqa` R6 (Table 7, p. 1482 — confirmed); `trivedi_2026_ssrn`
  §7 (13G selection — confirmed).
- **P4:** `empirical_feasibility.md` §1.1 (Fact 1 — confirmed), §1.2–1.3 (parser fix doubles post
  leg — confirmed); `trivedi_2026_ssrn` R2 (+0.348, t = 2.69, HLZ caveat — "(t>3" phrasing flagged
  as reading against the card); `dass_huang_maharjan_nanda_2020` fn. 27 ("<19" — confirmed,
  verifier-corrected form); `author_proposal_outline_2026` R1 (PROVED — confirmed);
  `bebchuk_brav_jackson_jiang_2013_jcl` Q20/R18 (p. 28; pp. 28, 31 — confirmed); institutional card
  §4.3 Table 2 p. 181 (20% — confirmed).
- **P5:** `zeng_2026_ras` Q1 p. 1303 (purpose split stated under Rule 13d-1(a) — P5's "(b)/(c)"
  attribution is a gloss), p. 1315 taxonomy (confirmed); `edmans_fang_zur_2013_rfs` Q11 (20%
  override, n. 17, printed p. 14 — confirmed), NACCO (printed p. 11 — confirmed), fn. 27 p. 1473
  (no instrument — confirmed); `albuquerque_fos_schroth_2022` §7 (declaration-vs-information-set
  distinction — verbatim, confirmed), fn. 16 p. 34 (confirmed); `greenwood_schor` R7 (confirmed).

No decision-critical claim in any proposal was refuted outright; the defects found are one
misattributed page (P2), one mischaracterized theorem (P2), one dropped exponent (P1), one
object slip (P1), one against-the-card phrasing (P4), and one rule-number gloss (P5).
