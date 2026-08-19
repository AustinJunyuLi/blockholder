# JUDGE 3 — Scorecard, ticket 03 positioning tournament (2026-08-19)

Adversarial pass. Every proposal's decision-critical citations were opened in the owning card
(or the institutional fact sheet / D7 record / digest / feasibility audit) and confirmed or
refuted; the check log is at the foot. Map ratings quoted below were re-read in
`research/competitor_map.md` Part 3, not trusted from the proposals.

## Score table

| Proposal | A Whitespace | B Anchoring | C Main result | D Empirics | E December | F Continuity | Total | Rank |
|---|---|---|---|---|---|---|---|---|
| P1 window × premium (tender game) | 4 | 5 | 4 | 3 | 4 | 5 | **25** | 3 |
| P2 rule-keyed partition (info design) | 4 | 3 | 4 | 4 | 5 | 5 | **25** | 2 |
| P3 Kyle deadline (MCS) | 5 | 5 | 4 | 3 | 4 | 4 | **25** | 4 |
| P4 Feb-2024 control-outcome DiD | 5 | 5 | 4 | 5 | 5 | 4 | **28** | **1** |
| P5 13D/13G purpose partition | 3 | 5 | 4 | 2 | 4 | 4 | **22** | 5 |

Tie at 25 broken on: theory deliverability and identity-centrality (P2) > on-object but
design-weak empirics (P1) > proof risk, deferred power, structural departure (P3).

## P1 — window length → takeover premium (W1 + W12)

- **A = 4.** W1 rated CLEAR and W12 CLEAR-on-mechanism both re-verified in the map; the
  NARROW half of W12 (Burkart–Lee IA Prop. 1) is disposed of exactly as the map instructs
  ("a wedge exists" cited to BL, ours from the partition). One soft joint: the strict
  result needs the pivotality jump at 1−τ_c to bind at 6–10% 13D stakes, i.e. τ_c read as
  a blocking/squeeze-out threshold — self-flagged in §9.
- **B = 5.** Anchor confirmed line-by-line in `_institutional_sec_33_11253.md`: five
  business days effective 2024-02-05 (§1, pp. 1, 10); Table 3 p. 189 80/20 split (§4.4);
  late rate ≈29% post Rule 0-3 (p. 178 n. 695, §2/§4.1). D7's λ jump is in Prop.
  d7:lambda's regime comparison + Remark d7:compstat(iii), and `d7_takeover_game_check.py`
  does test a pivotality jump — "PROVED and check-verified" holds. Greenwood–Schor 18%
  confirmed (p. 372, Table 6), with the looseness that 18.1% is *activist* targets.
- **C = 4.** Statement is precise (monotonicity, discontinuity at pivotality, cross-partial).
  Proof route is half-built: D7 is proved; the Kyle accumulation block is new but standard;
  "the jump survives composition" is a one-line argument, not a proof. Label PROVED on named
  primitives is realistic; the measured-premium denominator risk (Prop. d7:afs) is named
  honestly. Minor imprecision: the wedge is written with one ρ where D7's fold gives
  m̃−m₀ = ρ²(1−θ)λΔ_eng (Remark d7:fold) — immaterial to the sign claims.
- **D = 3.** The level test (premium on stake-at-filing vs a "10% short-form blocking"
  threshold) is cross-sectional; the change test is a before/after interaction with **no
  control group** — P1 itself calls it "honest quantification, not a causal design".
  Confound list is complete (EDGAR cut-off same date, 13G compliance 2024-09-30 capping the
  post window, T+1, BBJJ pill split, Ben-David). Power: change-test MDE 7–8 pp against an
  effect the SEC tables cap at a 3–20% constrained share — likely underpowered.
- **E = 4.** D7 half done; accumulation block 3–4 weeks is credible; empirics 8–10 of ~19
  weeks is tight but feasible; fallbacks (NUMERICAL + tender half; level test + calibrated
  bound) are real.
- **F = 5.** The most recognisable descendant on objects: the wedge (m₁−m₀), D7, κ, the
  partition — draft_v2's headline machinery, re-anchored.
- **Biggest flaw:** the strict/discontinuous part of the headline rests on a pivotality
  reading that is empirically strained at typical 13D stakes, and the empirical change leg
  has no untreated group.
- **Steal:** the D7-fed wedge with the pivotality discontinuity — the best premium
  microfoundation on the table, portable into P2's flagged cell or P4's sign model.

## P2 — the rule is the partition (W3 + W11 extension)

- **A = 4.** W3 rated "CLEAR (with a named boundary)" re-verified; both boundary wordings
  are respected verbatim (Kyle–Vila un-keyed split; "pooled for the price-setting market"
  per Zeng). W11 is claimed as extension only, with OCB Prop. 4 (p. 2847) cited as template —
  correctly hedged. Chabakauri standing risk acknowledged. Docked one for the CCKV
  misquotation (below) landing on the cell's central refuter.
- **B = 3.** Two citation defects found on checks. (i) "CCKV — 'No agent in the model ever
  learns that a blockholder holds a block', p. 11": that string is the *card's* §6(a)
  summary sentence, not a paper quote; the card's p. 11 quote is Q4 ("best interpreted as
  taking place in such a pre-disclosure window"). Substance true, quotation and page
  fabricated. (ii) "(feasibility §5.1)" for the MDE numbers: `empirical_feasibility.md` has
  no §5.1 and no MDE content anywhere — the arithmetic is P2's own and plausible, the cite
  is not. Everything else checked out (Maug p. 73 via map W3; Zeng Q5 p. 1310 verbatim;
  digest §6 "days, not weeks" verbatim; 2,849/1,048 = feasibility §1.3).
- **C = 4.** The most credible proof route of the five: every needed piece (existence,
  disclosed-branch κ-invariance, price decomposition) is already PROVED in draft_v2, and
  the digest's own §6 names this exact promotion as "days, not weeks". Labels (PROVED
  fixed-cutoff / region-certified GE / NUMERICAL off-region) match the D8 record. The
  self-assessment is honest: the fixed-cutoff attenuation is nearly mechanical, and the
  content must live in the pooled cell where the D8 counterexample can flip signs.
- **D = 4.** Sharp, signed, two-equation prediction (run-up vs filing jump, κ-split, and
  the post-2024 compression); runs on data in hand in ~1 week; placebo (pseudo-triggers at
  TD−63) is clean; Zeng's non-neutral 1–13-day screen is handled; the opposite-signed
  IA.2 size split is owned. No control group — justified via map W2 and bounded by
  magnitudes (CDF ~3%, Zeng 2.8%). December's clean result is an *information* outcome,
  not a control outcome; the premium leg is specified-only.
- **E = 5.** Strongest deliverability: 3–4 weeks core rebuild on proved machinery, days for
  the fixed-cutoff theorem, 1–2 weeks GE certification, ~1 week split empirics; and the
  stated fallback (representation + fixed-cutoff attenuation + split empirics) is already a
  full draft.
- **F = 5.** Keeps κ, the branch structure, bidder entry, the D7 wedge and the honesty
  labels, and *improves* draft_v2 by deriving the flag from the rule's two keys instead of
  the ad-hoc D = 1{q = +1} — exactly the digest's institutional-looseness complaint fixed.
- **Biggest flaw:** the headline cross-partial is close to an accounting identity once the
  flagged cell is κ-invariant; a referee will ask where the mechanism is, and the answer
  lives in the pooled cell whose GE sign is only region-certified.
- **Steal:** the (τ, T) two-key derivation of the disclosure flag, and the run-up/filing
  split as the cheap sharp test — both portable into any winner.

## P3 — the filing deadline as a partition device (W5 + W6)

- **A = 5.** W5 and W6 both rated CLEAR, re-verified; the W5 boundary (random horizons
  occupied — Caldentey–Stacchetti via CDF 2016 p. 1450) is respected verbatim, and W6 is
  stated as a slope claim against Massa–Xu's level, exactly as the map demands. No claim
  found that the map or a card refutes.
- **B = 5.** Cleanest citation record of the five. Confirmed: Table 3 p. 189 (80%), Table 6
  pp. 225–226 (Amihud 0.13→0.08 across the constraint columns), the ≈34% deadline mode
  (p. 178), CDF's Item 5(c) at JF p. 1556 (card Q2), Massa–Xu Table 7 p. 1482, Trivedi §7's
  selection warning verbatim. The "mechanical trade report" gloss on Item 5(c) is P3's
  interpretation, flagged as its own mitigation, not attributed to the card.
- **C = 4.** Statement precise (increasing differences of X_T in (κ, T); cross-partial ≥ 0
  for any stake-monotone control outcome). Tool is right (Topkis / single-crossing on the
  Bellman objective), but this is the furthest from proved machinery of the three theory
  proposals — nothing in draft_v2 proves a multi-period Kyle comparative static — and the
  named risk (terminal-flag manipulation breaking single-crossing) is real. Labels honest:
  PROVED under a named condition, NUMERICAL off-region, composition "else grid-certified".
- **D = 3.** Interaction design with the pre-rule κ-slope as bounded null is sound, and the
  13G-run-up placebo (13G deadlines unchanged until 2024-09-30) is the cleverest placebo of
  the five. But power/MDE is deferred ("formal MDE in the spec first") — a checklist item
  punted — and the December clean result is the run-up κ-slope, an information outcome; the
  control-outcome legs (bid hazard, premia) are "specified and piloted" only.
- **E = 4.** 8–11 weeks, no new data, credible fallbacks (region theorem; premium as spec +
  bounded pilot). Proof risk is the main schedule risk and is priced in.
- **F = 4.** Architecture intact (informed blockholder, noise κ, flag, bidder, D7
  downstream) but the trading stage is rebuilt as discrete-time linear-Gaussian Kyle —
  a bigger departure from draft_v2's ternary one-round structure than P1's or P2's.
- **Biggest flaw:** the in-hand December result is off-object (a run-up slope, not a control
  outcome), and the clean cross-partial needs the filing to be the bidder's dominant
  information source — its own §9 concedes the attenuation if the bidder reads prices.
- **Steal:** the 13G-run-up placebo window, and the Topkis/Riccati proof skeleton for the
  accumulation block any window-margin theory needs.

## P4 — control outcomes of the Feb-2024 acceleration (W2; fallback W13)

- **A = 5.** W2 rated "CLEAR on the cell; hard on execution" re-verified, and all three
  execution warnings are answered in the design: 13G unusable → matched never-13D controls;
  power → bounded null as headline; BBJJ defence channel → low-trigger-pill split with a
  signed-bias argument. Trivedi is cited with the map's exact mandated wording ("a working
  paper reports the window bit"). No refuted claim found.
- **B = 5.** Every anchor verified: Fact 1 (35.7%→75.6%, median 7.0→5.0 bd) is in-repo
  (`empirical_feasibility.md` §1.1); Trivedi +0.348 (SE 0.130, p = 0.007, t < 3 caveat)
  matches card R2; SEC Table 2 p. 181 (20% non-corporate-action) and Table 3 p. 189 (~3%,
  ≈7/yr) match the fact sheet; Greenwood–Schor p. 372 Table 6 confirmed; and the Dass cite
  is exactly right including the verifier's correction — "premium DiD died on **<19**"
  matches fn. 27 ("even smaller" than 19 for the premium split).
- **C = 4.** The main result is an estimand plus a bound plus a conditional sign — precise,
  and the honesty labels (ESTIMATED + PROVED-conditional) are realistic. One scope caveat:
  the bounded null bounds the *accumulation* channel (≤ ~3 pp via the 3% constrained tail);
  the BBJJ defence-speed channel binds on every campaign, constrained or not, so the bound
  is not a bound on the total effect — P4 handles it as confound (iv) but the "small
  footprint" headline needs that caveat attached. Power is named as the biggest risk and
  quantified.
- **D = 5.** The only proposal that answers every referee-checklist item on data in hand:
  a real control group (matched never-13D, 3:1) chosen *because* the map's W2 warning kills
  13G; a bounded null; the full dated-confound calendar (EDGAR cut-off same day, adoption
  anticipation, T+1, 13G 2024-09-30, XML 2024-12-18) with a main post window of Feb–May
  2024; concrete MDEs (6–10 pp bid hazard; ~15 pp premium, descriptive); ≥500 placebos;
  a quarterly pre-trend event study that blocks causal language if it fails; parser
  validation (30-filing audit, busday asserts). Minor: the premium MDE arithmetic is
  optimistic at n ≈ 50/side, but that leg is pre-committed as descriptive.
- **E = 5.** 16-week plan inside ~19 weeks, every leg on in-hand data (parser fix is the
  known 0.5–1 day), and each failure mode has a named fallback (W13 success coding;
  descriptive premium). The only position whose December clean result is a control outcome
  with a control group.
- **F = 4.** The triad is intact and the recognisable pieces are named (accumulation under
  noise cover, D7's λ, §6's bid-hazard prediction), but the paper becomes empirics-first
  with a companion sign model — the largest identity shift among the five, short of P5's
  margin swap.
- **Biggest flaw:** if the tournament demands a headline *detection*, this cannot promise
  one — the honest headline may be the bound itself, and the bound does not cover the
  defence channel.
- **Steal:** the matched never-13D control group plus the bounded-null framing, and the
  dated-confound calendar with the Feb–May 2024 main window — any winner should run this
  empirical leg.

## P5 — the 13D/13G purpose partition (W7; fallback W6)

- **A = 3.** W7 is rated NARROW and — decisively — **provisional**: the sweep's only DIRECT
  hit (Payne-Mann, Stice-Lawrence & Wong, SSRN 5076900, a control-outcome result keyed to
  the 13D/13G split) is unread behind a wall, and the map says W7's rating is "provisional
  in a way the other ratings are not". P5's contingency plan is exemplary, but a position
  whose cell can be occupied by an unread abstract is a weaker claim than the four verified
  cells above. The AFS disposal itself is good (declaration vs information-set distinction,
  card §7 verbatim).
- **B = 5.** Anchors verified: 20% override (EFZ n. 17, printed p. 14 — exact), NACCO v.
  Applica (EFZ card, printed p. 11), purpose taxonomy 36.6/43.3/20.0 (Zeng p. 1315), EFZ's
  0.7% 13G CAR (printed p. 27; published 0.8% VW / 0.7% EW), Greenwood–Schor 18.1/7.2.
  Minor: Zeng's Q1 (p. 1303) states the intent split under Rule 13d-1(a); P5's parenthetical
  cites 13d-1(b)/(c) — correct law, but not the rule number in the cited quote.
- **C = 4.** Statement precise (purpose partition load-bearing; gap widening in κ; 13D cell
  κ-invariant). The invariance half reuses proved draft_v2 results
  (`app:proof-disclosed-invariance`, `lem:d1-variance` — both confirmed in the digest), but
  the three-state flag with a mixing 13G cell is genuinely new and "the cross-partial sign
  follows" is asserted; the D8-style monotonicity risk is self-flagged. Labels realistic.
- **D = 2.** The workhorse leg (entry ~ purpose flag × lagged Amihud) has no exogenous
  variation of any kind — no dated change, no instrument — and the purpose flag is
  endogenous by construction; "selection into 13D is the object, not a nuisance" is a
  reframing, not an identification. The sharp leg (20% boundary) is power-poor with
  bunching manipulation, self-acknowledged. This is the EFZ fn. 27 critique absorbed at
  full force.
- **E = 4.** 7–9 weeks is credible and the fallback (W6 slope design on the in-hand 13D
  sample) is real; 13G enumeration is a flag change but ~4× the parse volume; thin 20%
  bins flagged.
- **F = 4.** Machinery recognisable (κ, partition, bidder entry, D7's λ) but the margin
  swaps from threshold/window to purpose and the Feb-2024 anchor is dropped — permitted by
  ADR-0003, but a visible departure.
- **Biggest flaw:** the position bets on an unread paper not occupying its cell, and its
  workhorse empirics have no exogenous variation even if the bet pays off.
- **Steal:** the 20% eligibility override as a source of fuzzy variation, and the AFS
  declaration-vs-information-set sentence for the related-work section.

## Near-identity note

P2 and P3 are near-identical in *position*: both put a rule-keyed partition inside a
Kyle-flavoured trading model and run liquidity-slope empirics on the pre-filing run-up.
They differ in tool (information design on draft_v2's cutoff base vs monotone comparative
statics on a new discrete-time Kyle market) and in which map cell they headline (W3 vs
W5/W6), but a merged version would lose nothing. P1 is adjacent to both (same window
margin; object and empirical leg differ).

## Ranking and justification

**1. P4 (28). 2. P2 (25). 3. P1 (25). 4. P3 (25). 5. P5 (22).**

**Winner — P4.** It is the only proposal whose December deliverable is a clean empirical
result *on a control outcome* with *a control group*, in a cell the map rates CLEAR, with
every checklist item answered on data in hand and a citation record that survived all six
checks — including getting the Dass fn. 27 correction right. Its honesty about power is a
feature for a department review: the bounded null is a defensible headline precisely
because the SEC's own tables cap the constrained tail, and the companion model gives the
per-campaign sign. The residual concerns — the bound covers only the accumulation channel,
and the paper's centre of gravity shifts from theory to empirics — are real but priced in.

**Runner-up — P2.** The strongest theory deliverability of the five: the main result is the
promotion of draft_v2's disclosure attenuation to a fixed-cutoff theorem using machinery
already proved in the repo (the digest's own "shortest route": days, not weeks), it occupies
the cell CONTEXT.md calls the paper's identity, and its fallback is already a full draft.
It loses to P4 because its December clean result is an information outcome rather than a
control outcome, and because of the two citation defects found on checks — the CCKV
quotation attributed to p. 11 (a card summary sentence, not a paper quote) and the
nonexistent "feasibility §5.1" MDE cite. If the author weights theory ambition above the
empirical leg, the order reverses; the natural package is P2's model with P4's empirics.

## Check log (citation → verdict)

- P1: 33-11253 §1 (5 bd, 2024-02-05) — CONFIRMED. Table 3 p. 189 (20%) — CONFIRMED (§4.4).
  Late rate 29%, p. 178 n. 695 — CONFIRMED. D7 λ jump at 1−τ_c + check script — CONFIRMED
  (Prop. d7:lambda regime comparison; Remark d7:compstat(iii); `d7_takeover_game_check.py`
  tests `pivotality_jump`). GS 18% — CONFIRMED (p. 372, Table 6; activist targets). BL
  Lemma 2 p. 1877 / p. 1891 / IA Prop. 1 — CONFIRMED via map W12 (executed check logged
  there). Wedge written with ρ vs D7's ρ² — IMPRECISION, not refuted.
- P2: Maug p. 73 — CONFIRMED via map W3. Zeng Q5 p. 1310 — CONFIRMED verbatim. CCKV "No
  agent…" cited to p. 11 — **REFUTED as cited** (card §6(a) summary; p. 11 is Q4).
  "feasibility §5.1" MDE cite — **REFUTED** (no such section; no MDE content in
  `empirical_feasibility.md`). Sample 2,849/1,048 — CONFIRMED (§1.3). Digest §6 "days, not
  weeks" — CONFIRMED. W3 rating — CONFIRMED.
- P3: Table 3 p. 189 (80%) — CONFIRMED. Table 6 pp. 225–226 (Amihud 0.13→0.08) — CONFIRMED.
  34% deadline mode p. 178 — CONFIRMED. CDF Item 5(c) JF p. 1556 — CONFIRMED (card Q2).
  Massa–Xu Table 7 p. 1482 — CONFIRMED via map Part 2 item 9. Trivedi §7 selection —
  CONFIRMED verbatim.
- P4: Fact 1 (35.7→75.6; 7.0→5.0) — CONFIRMED (`empirical_feasibility.md` §1.1). Trivedi
  +0.348, p = 0.007, t < 3 caveat — CONFIRMED (card R2). SEC Table 2 p. 181 (20%) —
  CONFIRMED. Table 3 (~3%, ≈7/yr) — CONFIRMED (§4.4). GS p. 372 Table 6 — CONFIRMED. Dass
  fn. 27 "<19" — CONFIRMED (card verifier's own correction). BBJJ p. 28 Q20 — CONFIRMED via
  map W2.
- P5: Zeng Q1 p. 1303 — CONFIRMED in substance (rule number in quote is 13d-1(a), not
  (b)/(c)). EFZ n. 17 p. 14 (20% override) — CONFIRMED. NACCO p. 11 — CONFIRMED. Zeng
  p. 1315 taxonomy — CONFIRMED. AFS fn. 16 p. 34 — CONFIRMED via map W7. AFS §7
  declaration-vs-information-set — CONFIRMED verbatim in card.
