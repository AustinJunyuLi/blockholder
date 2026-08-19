# P3 — The filing deadline as a partition device

## 1. Object
Bidder entry and the expected takeover premium on a 13D-flagged target, determined by the stake carried into the flagged state.

## 2. Margin
The window margin: a LEVEL in the theory (window length T a primitive of the rule), the dated CHANGE (10 calendar days → 5 business days, 2024-02-05) in the empirics. A deadline attached to the partition: crossing 5% starts the clock; filing flips the market from pooled to flagged.

## 3. Anchor
Rule 13d-1(a) as amended by SEC Release 33-11253: initial 13D "within five business days" of crossing 5%, effective 2024-02-05 (`_institutional_sec_33_11253.md` §1: p. 1, p. 10). The release's own numbers show the window binds and its bite covaries with liquidity: 80% of campaigns complete accumulation by the amended deadline (Table 3, p. 189); pre-trigger Amihud runs 0.13 → 0.08 across Table 6's constraint columns (pp. 225–226).

## 4. Main result to be proved
**Statement.** In a discrete-time linear-Gaussian Kyle market on t = 1,…,T with a rule-keyed disclosure event at T (stake trigger plus legal deadline): (i) per-period trading intensity is nonincreasing in T and the flagged stake X_T(κ, T) has increasing differences in (κ, T); (ii) any control outcome monotone in the flagged stake therefore satisfies ∂²/∂κ∂T ≥ 0: shortening the window flattens the slope of the control outcome in liquidity.

**Tool.** Monotone comparative statics: Milgrom–Shannon single-crossing on the Bellman objective; Topkis; order-preserving Riccati comparison.

**Proof route.** Linear strategies ⇒ Gaussian filtering; posterior variance and price impact follow recursions whose terminal condition the deadline sets, the map order-preserving in it. The quadratic Bellman cross-partials in (x_t; κ), (x_t; −T) reduce to signs of recursion coefficients (single-crossing in closed form); Topkis yields increasing differences of X_T. The post-flag stage (bidder entry, or draft_v2's D7 tender game) is monotone in X_T; composition preserves the cross-partial under a stated condition, else grid-certified.

**Expected honesty label.** PROVED for (i) and the cross-partial sign under the named single-crossing condition; NUMERICAL off-region (D8 certification pattern).

**Biggest technical risk.** The terminal flag invites manipulation of what the filing reveals, which can break single-crossing; Item 5(c) makes the filing a mechanical trade report, not a choice (`collin_dufresne_fos_2015_jf.md` §4, JF p. 1556); failing that, a region theorem.

## 5. Empirical design
**Object and sample.** κ-slope of the pre-filing run-up and of control outcomes, pre/post 2024-02-05; parsed 13D universe 2022–2025 matched to on-disk CRSP 2021–25; κ = pre-trigger Amihud, inverted.
**Identification.** Interaction, not level: outcome on κ × Post with controls, year-quarter FE, two-way clusters. No control group exists for control outcomes (13G filers disclaim control intent; selection is rule-responsive; `trivedi_2026_ssrn.md` §7): a continuous-dose slope comparison with a bounded null (pre-rule κ-slope as benchmark); Trivedi's null level effect on Amihud protects κ as pre-treatment.
**Confounds.** EDGAR cut-off same day (33-11253 §3, p. 9); anticipation from Oct-2023 adoption; T+1 (2024-05-28); 13G compliance (2024-09-30); structured-data mandate (2024-12-18); business-day windows throughout (Zeng's calendar-day screen is not neutral across the change, map W2).
**Power/MDE.** ~4–5k matched events (~2,800 pre / 1,000+ post after the 2025 parser fix); formal MDE in the spec first; target: flattening a third of the pre-rule slope. Premium leg (few-hundred deals) power-limited.
**Placebo.** κ × Post on 13G run-ups (deadlines unchanged until 2024-09-30); ≥500 placebo dates pre-2024.
**Run by December on data in hand:** run-up κ-slope interaction (~3–4 days per `empirical_feasibility.md` §4). **Specified and piloted:** bid hazard and hand-collected premia. Zeng's only liquidity-adjacent cut is a median-market-cap split (IA Table IA.2, p. 1322), not a liquidity test; a κ-interaction on her design is unclaimed.

## 6. What is new vs the competitor map
**Cells occupied.** W5 (rated **CLEAR**), boundary respected verbatim: the random horizon is occupied (hazard 4; CDF 2016 p. 1450), so the claim is never "the horizon is non-fixed" but "a legal filing window with a partition attached". W6 (rated **CLEAR**): Massa and Xu (2013) estimate the liquidity–premium slope holding the legal environment fixed (Table 7 p. 1482); we ask what the disclosure rule does to that slope; Trivedi measures only a level effect of the rule on liquidity, never an interaction (card §7).
**Nearest rows, and why each does not occupy the cell.**
- Back et al. (2018) and CDF (2016): T fixed, exogenous, common knowledge (CDF p. 1464); a shorter T "is isomorphic to reducing noise trading volatility" (Back et al. p. 1453). Ours is a partition event, not a rescaling of σ.
- CCKV (2026): the window is a convenience ("trades effectively remain hidden for some time", p. 10) inside a permanently pooled state (fn. 16, p. 15); their named open direction (i), time-horizon effects (p. 35), is the strongest external warrant.
- GMM (2025): no window, deadline, or partition; the continuous-time endogenous stake path ending in lumpy full acquisition is theirs (Prop. 7, p. 28); this position never touches the stake path.
**Rows sidestepped.** W9 (chosen filing delay, NARROW): the filing lands at the deadline, the modal behaviour (≈34%, 33-11253 p. 178).

## 7. Deliverability by December
Model: 3–4 weeks. Proofs: 2–3 weeks; certification script: 1 week. Empirics: parser fix 0.5–1 day; run-up interaction ~3–4 days; outcome matching plus premium subsample 1–3 weeks. Total ≈ 8–11 weeks. **What could fail:** single-crossing fails globally → region theorem, NUMERICAL outside it; premium-subsample power → premium leg ships as a spec with a bounded pilot. No new data sources or coauthors; continuous time only as a flagged extension.

## 8. Supervisor continuity
A reader of draft_v2 recognises: one informed blockholder trading against noise κ in a Kyle market; a disclosure flag partitioning the market's information; a bidder and premium wedge downstream (the D7 tender game reused post-flag); the ADR-0004 identity intact. Dropped: the four-action menu, the hump R1 (Maug Prop. 7 p. 83; Edmans 2009 Prop. 3 p. 2496; LMM 2024 Prop. 7), the welfare planner, threshold margins, the rumor extension; each sits in an occupied cell.

## 9. Self-assessed weakest point
The clean cross-partial wants the filing to be the bidder's dominant information source, but the pooled-state price path is public too; if the bidder reads prices rather than the flag, the stake channel attenuates and the result survives only on a region — and the Item 5(c) mitigation (mechanical trade report; bidder conditions on (flag, price)) is the most contestable choice.
