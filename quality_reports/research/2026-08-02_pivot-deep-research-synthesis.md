# Pivot deep-research — boss synthesis (pre-red-team draft)

**Date:** 2026-08-02 · **Method:** 13-worker ringer swarm (sonnet×5, opus×3, deepseek×4, k3×1;
zero GPT lanes by design), quote-grep and executed-proof checks; artifacts under
`C:/Users/ALi/.ringer/work/pivot-deep-research/<task>/report.json` (T1: `verdicts.json` +
`proofs/`). 12/13 substantive passes (2 recorded fails were check-root-cause, both recovered).

## Q1 — Is the pivot's position among the literature solid?

**Verdict: the INSTITUTION is open; the proposed HEADLINE is occupied; the positioning needs
one decisive rotation.**

1. **Novelty gate OPEN** (L6, ~40 dated searches, genuine null): no paper exploits realized
   post-Feb-2024 13D outcomes with takeover/premium variables. Polk-Buchheit-Riley-Stone
   (SSRN 4596959, published J. Fin. Reg. & Compliance 2024) is a 2001–2022 projection with
   CAR/volume outcomes only. Cetemen et al. (JF 2026) is pure leader-follower theory, no
   disclosure window. SEC/DERA has no post-implementation follow-up.
2. **The June blocker was a phantom** (L3b, CONTRADICTED×3): Johnson–Swem contains NO σ²T
   isomorphism — the filing window appears once, in an institutional footnote; no counterfactual
   varies it; "endogenous timing declared open" is also not in the text. Source of the phantom
   found (L5): draft_v2.tex line 130's own gloss projected the mapping onto J-S, and the June
   verification "verified" the draft's gloss, not the paper. The strategic reason for keeping
   the 2024 reform as a mere de-risk fact **dissolves**.
3. **But the pivot's page-1 headline is taken** (T2 kill + L3a + L2):
   - C-L 2025 (R&R RFS) already assert the capitalization interpretation of their own
     −13.7%/5.2pp: "All of the reduction in bid premium is due to activist intervention because
     the pre-announcement share price … incorporates the activist's signal about a potential
     acquirer."
   - "Completion up, conditional premium down via weakened resistance" is already in
     **Corum–Levit 2019** (fn. 29 + Prop 2) — a paper pivot.md never cites.
   - "Activist as intermediary/broker" is Burkart–Lee's verbatim abstract headline; the
     bidder-discovery/solicitation channel (pivot Prop 3) is Corum–Levit's solicitation effect.
4. **What is genuinely open:** (i) the legal disclosure **window as a TIME margin / deadline in
   an accumulation problem** — OCB have a static size threshold in a one-shot trade; B-L punt
   predisclosure accumulation; C-L 2019 make disclosure an instantaneous publication step;
   C-L 2025 make the campaign common knowledge; J-S collapse it to a lognormal cost draw;
   (ii) the realized-2024-reform empirics; (iii) the three-part gain-timing decomposition
   (filing/run-up/markup) — noting the third leg is a genuine extension of the two-part
   Schwert/BET convention, not inherited from it (L4).
5. **Citation landmines in pivot.md** (GPT-correlated sloppiness, as user suspected): its
   Celentano-Levine link [4] actually points to Burkart-Lee's RFS URL; **Schwert 1996 is cited
   for a mechanism his paper finds AGAINST** ("little substitution"; ≥67% of run-up is added to
   the bid) — the substitution result the pivot needs is Betton-Eckbo-Thompson-Thorburn (JF
   2014); Corum-Levit, Fishman 1988, Grossman-Hart (1980, both papers), CDF 2015, Boyson-
   Gantchev-Shivdasani 2017 all missing. **BDO is published JAR 2020** (pivot calls it an ECGI
   WP) and is the structurally closest DESIGN paper (EU disclosure reform DiD, toeholds,
   bidder-alerting) with the OPPOSITE bidder-side sign (preemptive-bid deterrence à la Fishman)
   — must be engaged head-on, not filed under "Alternative 3."
6. **All SEC institutional numbers verified verbatim** (L7; zero fabrications). Two riders: the
   final rule DROPPED proposed 13d-3(e) (cash-settled derivatives not deemed beneficial
   ownership → substitution channel live and measurable); the "≈3%" appreciation benchmark is
   the under-90%-accumulated subgroup median (~7 campaigns/yr), not a general figure (E1).

## Q2a — Are the pivot's attacks on the current draft correct? (T1, executed proofs)

Facts mostly right; inferences systematically overstated; three attacks are structural:

- **A1 PARTLY:** κ-parity, U-shaped informativeness, and the 2−√2≈0.5858 vs κ†≈0.5899
  coincidence all CONFIRMED numerically (0.7% apart; and the draft's own B.13 states the
  minimizer). But orientation (hump vs trough) is set by bid-entry curvature — economics —
  not the lattice (D8's trough flips orientation with the lattice unchanged). "Hump = artifact"
  is half-true: the lattice pins WHERE the extremum is, not WHETHER it's a max.
- **A2 PARTLY:** conditionality elements real; the Fig-H.10-vs-Appendix-F inconsistency is REAL
  (same cell, opposite words). Deeper than the pivot saw: the σξ=0.60 profile is essentially
  FLAT (total variation ≈1.25% of level, 3 interior turning points; the "certified trough" is a
  5×10⁻⁴ dip at κ=0.275, outside the figure's window). Both the caption and D8's counterexample
  marketing are over-strong.
- **A3 CONFIRMED (the pivot's best attack):** no ownership state, no τ, no post-crossing window;
  disclosure simultaneous with the trade — and the draft claims the 5%-vs-3% comparison in the
  abstract, intro, testable implications, and conclusion. Unsupported as written.
- **A4 CONFIRMED and STRENGTHENED:** disclosed bid probability 1.31% exact vs 17–81%
  nondisclosed. The deterrence is STRUCTURAL and runs through the disclosed PRICE, not the
  wedge — even m1<m0 cannot reverse it. Sale-facilitating activism requires a different bidder
  technology (activism moving S̄, K, or entry), which supports the pivot's redesign more
  forcefully than its own argument did.
- **A5 CONFIRMED, worse than alleged:** Δmin is per-share; the netting proof's own (1−h)
  weights give 0.0223 vs the coded 0.0770 (3.45×); float mass is 0 under Hold AND Quiet (56% of
  probability mass), not just −1 under PV (3.7%); the "machine-precision" decomposition claim
  fails by +6.7%/+11.7%. Fix is a rescaling, but W and Prop 7's κ*-vs-κ† wedge are currently in
  mismatched units.
- **A6i–A6iv:** real textual defects, all repairable in lines (the correct single-crossing proof
  already sits in App. B.1/E; the corner limit IS path-dependent (=b/(a+b), computed exactly)
  but concerns an off-path belief a one-line convention fixes; the contraction bound fails
  (1.037>1) while the true modulus is 0.579 — and the draft's "honest margins" remark contains
  an arithmetic slip (p*=0.847 attached to the wrong cell; missing /σξ). The ρ² two-Bernoulli
  charge is right about the construction, wrong that the draft concedes it; the real question
  is why B₂ shares ρ with B₁.
- **Bonus defects the pivot missed:** draft line 971 still asserts κ→1 posteriors → prior and
  Δact→0 — contradicted by the draft's own Remark at 828 and numerically false (Δact(0.95) =
  0.0321 vs Δact(0.50)=0.0351).
- **The draft's own referee exposure** (L5): the Corum-Levit characterization ("abstract from
  secondary-market inference and disclosure") is CONTRADICTED by CL §4 (Kyle market maker +
  13D publication + bidder entry) — the draft's "no existing framework does this jointly"
  sentence survives only if narrowed to stake-triggered branch-partitioning DURING trading;
  the premium finding is misattributed to AFS at lines 101/130 (it is C-L 2025's); the J-S
  "noise-trading cover" gloss is the draft's own invention.

## Q2b — Is the proposed mini-model sound? (T2 opus-max; T3 kimi, independent; convergent)

As specified, NO — fixable with named changes. P1 is an accounting identity (and its mechanism
is C-L 2025's); P2's C_xd<0 — the paper's ONLY novel margin — is assumed; P3's sign is assumed
and contradicts the author's own ∂p/∂π<0 (which sits on the pivot's "preserve" list); P4's
"separately measurable moments" confuses marginal with average objects. Unmentioned: P^F is a
SIGNALING-game object (multiplicity/refinement unaddressed; 2-D type + 2-D signal generically
fully separates, killing the needed noise; Item 4 purpose is cheap talk → needs 10b-5
misstatement cost); and the B-vs-P^F dilemma — either B is independent of P^F (capitalization
becomes tautology) or there is a pricing fixed point (which the pivot orders deleted). 8–10pp
is unrealistic as specified (18–22pp); 10–14pp for a neutralized version.

**The repair set (T2/T3 convergent):** dealer/deadline microfoundation C(x;d,L)≈(λ_L/2)x²/d
(makes C_xx>0, C_xd<0 THEOREMS; monotone in liquidity — answering the pivot's own §1.1
objection; yields horizon scaling → a quantitative 10-day→5-BD prediction and an endogenous
pre-filing run-up); model the window as a DEADLINE that binds only for some campaigns (SEC's
90%-by-day-5 heterogeneity becomes a corner solution, generating the empirical exposure
variable from inside the model); binary type + exogenous garbling + misstatement cost + stated
refinement; P3 as a certification-vs-deterrence elasticity inequality; P4 as a
sufficient-statistic formula with the reform's compliers as the marginal units. Port from D7:
rem:d7-testable (cross-sectional heterogeneity table), rem:d7-compstat(iii) (stake-threshold
discontinuity), Prop 14's statement FORM, and β(x)=β̄·λ(q,γ,ψ,α) discipline. "Promote Prop 14
to page 1" as written is incoherent — Prop 14's sharp form needs the λ the pivot deletes.

## Q2c — Are the empirical designs sound? (E1 opus; E2 deepseek; convergent)

As written, NOT credible for a causal headline at JFQA/RF:
- Population-average treatment intensity: the window binds materially on ~3% of campaigns
  (~7/yr); the 20% who use it acquire only 5.9% of their stake in it (≈0.1pp of shares
  outstanding). The pivot never states this.
- Leave-one-out activist exposure infeasible (1.65 filings/entity over 22 yrs; own fact1: 3 of
  259 filers with ≥3 filings) and confounded with campaign quality (SEC Table 6: 17.2% vs 5.7%
  filing CAR across exposure bins).
- The triple interaction has MDE 17–31pp on a 17pp base rate (≈18 exposed campaigns, ~3 bids at
  the SEC's binding margin). Not estimable.
- Bundled rulemaking (2-BD amendments contaminate "post-filing accumulation"; 13G deadlines
  moved too; XML Dec-2024 regime break), single-date treatment with undefined continuous-dose
  estimand, 2022-proposal/2023-adoption anticipation.
- The gain-decomposition test has a mechanical calendar-truncation artifact running OPPOSITE
  to the stated prediction; needs event-time-invariant restatement + as-if-5BD recut placebo.
- The week-10 gate is self-passing (2 of 5 margins are mechanical identities).
- fact1 hygiene: headline 75.6% relies on an undocumented 60-BD trim (untrimmed 70.8%);
  corporate-action pooling; 0.64–0.68 parse rates; self-reported trigger dates.
- Feasibility (E2): CRSP/WRDS access UNCONFIRMED (kill gate); no M&A database (Bloomberg
  checklist unrun); Item 5(c) extraction 4–8+ wks from zero; **the pivot's claimed
  merger-chronology "comparative advantage" does not exist in this repo** (check other repos);
  26-week schedule not executable as written.

**The fix that unlocks it (E1):** move exposure to the TARGET level — required-trading-days-
to-5% = (0.05 × shares outstanding)/(participation rate × pre-trigger 6-mo ADV) — predetermined,
defined for one-time filers, enables activist×quarter FE; then run near-term, well-powered
outcomes (stake at filing, filing timing, composition, filing-date CAR share, derivative usage),
restate the decomposition on event-time-invariant objects, and make the anatomy of activist
target gains + (if available) chronologies the headline. "The fallback should be the plan."
Realistic tier: RF/JFQA/JCF; RFS/JFE only as upside.

## Q3 — Boss recommendation (to be red-teamed)

**Adopt the pivot's DIRECTION; reject its CONFIGURATION. The window is the paper.**

Concretely: "Disclosure deadlines and activist stake formation" — a 10–14pp deadline-
accumulation model (dealer microfoundation; window binding for a model-generated subset) +
measurement-first empirics of the realized reform (target-level exposure; timing/accumulation/
composition outcomes; event-time-invariant gain anatomy; the SEC's own tables as the power
discipline) + the capitalization lemma demoted to measurement guidance (citing C-L 2025 and
BETT 2014 as the incumbents). Keep the current draft as a separate finished working paper
(stop investing; do not delete); transplant D7's testable remarks and Prop 14's form.
Six-month plan: weeks 1–2 = WRDS/CRSP go/no-go + Bloomberg checklist + narrowed 2022–2026
sample decision + the Gaussian-noise falsification the pivot suggests (cheap, one week, closes
the hump question); chronologies deferred unless they exist in the author's other repos.
Fallback if CRSP fails: EDGAR-only accumulation/composition paper (JCF tier).

**Rejected branches:** (a) defending the current paper as-is — killed not by the pivot's math
attacks (mostly repairable) but by the positioning exposure (Corum-Levit contradiction; AFS
misattribution; 5%-vs-3% claims without τ) and by A4's structural deterrence-only bidder
technology; (b) the pivot as configured — headline occupied (C-L 2025), theory rests on an
assumed cross-partial, empirics underpowered at its central test, schedule infeasible on two
unconfirmed access gates; (c) pure-theory window paper — journal-risk (June evidence: solo
junior pure theory rarely clears top-3) and wastes the reform.

## Known limitations of this synthesis
- Betton-Eckbo-Thorburn 2008 chapter text not directly verified (SSRN 403); one-day window
  variance vs Schwert noted from the 2025 successor survey.
- J-S conclusion based on the author-posted JFE version; if an earlier WP version contained a
  window mapping, the June note may have read that — does not change the referee-relevant fact.
- C-L 2025 is R&R at RFS: its final published form may add disclosure-timing content; check at
  each revision.
- Power calculations are back-of-envelope (E1's MDE arithmetic), not simulations.
