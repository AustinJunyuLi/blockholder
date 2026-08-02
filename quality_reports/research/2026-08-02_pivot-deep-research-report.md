# Pivot deep-research — FINAL REPORT

**Date:** 2026-08-02 · **Question:** should pivot.md (GPT-5.6 Sol Pro's recommendation) be adopted?
**Method:** 13-worker ringer verification swarm (sonnet×5, opus×3, deepseek×4, kimi-k3×1; zero GPT
lanes by user's correlation concern) with quote-grepped and executed-proof checks, followed by a
boss synthesis and ONE Fable-max adversarial red-team of the recommendation itself.
**Artifacts:** `C:/Users/ALi/.ringer/work/pivot-deep-research/<task>/` (reports, T1 proofs,
FABLE-redteam-adjudication/report.json); pre-red-team synthesis in
`2026-08-02_pivot-deep-research-synthesis.md` (same folder as this report); run records in
`~/.ringer/runs/pivot-deep-research-*.json`; live page `~/.ringer/artifacts/live/pivot-deep-research.html`.

---

## The three answers

### Q1 — Is the pivot's literature position solid?
**Half. The institution is genuinely open; the proposed headline is occupied.**

- **Open (verified):** No paper exploits realized post-Feb-2024 13D outcomes (L6: ~40 dated
  searches, honest null — Polk et al. is a 2001–2022 projection with no takeover variables,
  published in J. Fin. Reg. & Compliance; Cetemen et al. JF 2026 is pure leader-follower theory
  with no disclosure window; no SEC/DERA post-implementation follow-up). No theory paper models
  the filing **window as a time margin** (OCB = static size threshold; Burkart–Lee = exogenous
  toehold, punts predisclosure accumulation; Corum–Levit = instantaneous publication;
  C-L 2025 = campaign common knowledge; J-S = lognormal cost draw).
- **Occupied (verified):** the pivot's page-1 capitalization headline — C-L 2025's own text
  asserts the capitalization reading of their −13.7%/5.2pp result; "completion up, conditional
  premium down via weakened resistance" is already in **Corum–Levit 2019** (fn. 29), a paper
  pivot.md never cites; "activist as broker/intermediary" is **Burkart–Lee's verbatim abstract**.
- **The June blocker was a phantom:** Johnson–Swem contains **no σ²T/window mapping** — the
  filing window appears once, in an institutional footnote (L3b, read all 2,023 lines). The
  phantom traces to draft_v2.tex line 130's own gloss, which the June verification then
  "verified." The strategic reason for keeping the 2024 reform peripheral dissolves.
- **Institutional layer:** every SEC number in pivot.md verified verbatim against release
  33-11253 (L7; zero fabrications). Riders: the final rule **dropped** proposed 13d-3(e)
  (cash-settled derivatives not deemed beneficial ownership → substitution channel live); the
  "≈3%" appreciation figure is the under-90%-accumulated subgroup median, not a general number.
- **Pivot's citation defects (the GPT-correlated sloppiness you feared, confirmed):** its
  Celentano–Levine link points at Burkart–Lee's RFS URL; **Schwert 1996 is cited for a mechanism
  Schwert finds against** ("little substitution"; ≥67% of run-up is *added* to the bid) — the
  substitution result Prop 1 needs is Betton–Eckbo–Thompson–Thorburn (JF 2014); Corum–Levit,
  Fishman 1988, both Grossman–Hart 1980 papers, CDF 2015, Boyson–Gantchev–Shivdasani 2017 all
  missing; BDO is published (JAR 2020), is the structurally closest *design* paper (EU disclosure
  reform DiD on toeholds/control acquisitions), and predicts the **opposite** bidder-side sign
  (Fishman-style preemptive-bid deterrence) — it must be engaged head-on.

### Q2 — Are the theoretical construct and empirical strategies sound?

**The pivot's attacks on the current draft (T1, executed proofs):** facts mostly right,
severity systematically overstated; three are structural:
- **A3 confirmed (best attack):** no ownership state, no τ, no post-crossing window — and the
  draft claims the 5%-vs-3% comparison in abstract, intro, testable implications, conclusion.
- **A4 confirmed and strengthened:** disclosed bid probability 1.31% (exact) vs 17–81%
  nondisclosed, and the deterrence is **structural, running through the disclosed price** —
  no parameterization (even m₁<m₀) reverses it. Sale-facilitating activism needs a different
  bidder technology. This supports redesign more than the pivot's own wedge-based argument.
- **A5 confirmed, worse than alleged:** Δmin is per-share while the welfare netting uses share
  masses (float = −1 under PV on 3.7% of mass, **= 0 under Hold+Quiet on 56%**); coded Δmin is
  3.45× the proof's own weighting; the "machine-precision" identity misses by 6.7–11.7%.
- A1/A2 partly: κ-parity, U-shaped informativeness, and the 2−√2 ≈ κ† coincidence all real —
  but **orientation** (hump vs trough) is set by bid-entry curvature, not the lattice; and the
  H.10-vs-Appendix-F inconsistency is real but both sides oversell a near-flat profile (the
  "certified trough" is a 5×10⁻⁴ dip; total variation ≈1.25% of level).
- A6i–iv: real textual defects, all line-level repairable (correct single-crossing proof already
  in App. B.1/E; corner limit is path-dependent (= b/(a+b)) but off-path; contraction bound
  fails while the true modulus is 0.579). **New defects the pivot missed:** line-971 false
  κ→1 narrative (Δact(0.95)=0.032 vs 0.035 at κ=0.5 — 92% retained, not →0); an arithmetic slip
  in rem:A5margins (p*=0.847 attached to the wrong cell; missing /σξ).
- **The draft's own referee exposure (L5):** its Corum–Levit characterization ("abstract from
  secondary-market inference and disclosure") is contradicted by CL §4 (Kyle market maker + 13D
  publication + bidder entry) — the "no existing framework does this jointly" sentence survives
  only if narrowed to stake-triggered branch-partitioning during trading; and the premium
  finding is misattributed to AFS at lines 101/130 (it is C-L 2025's).

**The pivot's proposed mini-model (T2 opus-max + T3 kimi, independent, convergent):** as
specified, not yet a model — Prop 1 is an accounting identity whose mechanism C-L 2025 already
assert; Prop 2's C_xd<0 (the only novel margin) is assumed; Prop 3's sign is assumed and
contradicts the author's own ∂p/∂π<0; Prop 4 confuses marginal with average objects; the filing
price P^F is an unacknowledged signaling-game object; and the B-vs-P^F dilemma means you either
get a tautology or re-import the pricing fixed point the pivot orders deleted. 8–10pp is
unrealistic (18–22pp as specified). **Fix set:** dealer/participation-cap microfoundation
C(x;d,L) ≈ (λ_L/2)x²/d (makes C_xx>0, C_xd<0 theorems, monotone in liquidity — answering the
pivot's own §1.1 objection — and yields a quantitative 10-day→5-BD scaling plus endogenous
pre-filing run-up); window as a **deadline binding only for a model-generated subset** (the
SEC's 90%-by-day-5 heterogeneity becomes a corner solution and generates the empirical exposure
variable); neutralized signaling; Prop 3 as a certification-vs-deterrence elasticity inequality;
Prop 4 as a sufficient statistic with the reform's compliers as the marginal units. Port from
D7: rem:d7-testable, rem:d7-compstat(iii), Prop 14's statement form, β(x)=β̄·λ discipline.
(N.B. "promote Prop 14 to page 1" as written is incoherent — Prop 14's sharp form needs the λ
the pivot deletes.)

**The empirical designs (E1 + E2):** not credible as written for a causal headline —
- population-average treatment intensity ≈ **0.1pp of shares outstanding** (window binds
  materially on ~3% of campaigns; the 20% who use it acquire 5.9% of stake inside it) — never
  stated in pivot.md;
- leave-one-out activist exposure infeasible (1.65 filings/entity over 22 years; 3 of 259
  filers with ≥3 filings in this repo's own data) and confounded with campaign quality;
- the Post×Exposure×SaleIntent duration test has MDE 17–31pp on a 17pp base (~3 bids in the
  materially-exposed post-reform cell) — not estimable;
- bundled rulemaking (2-BD amendments move "post-filing accumulation"; 13G deadlines moved;
  Dec-2024 XML regime break); single-date continuous-dose treatment with unstated estimand;
- the gain-decomposition test carries a **mechanical calendar-truncation artifact running
  opposite to its stated prediction**; needs event-time-invariant restatement + an
  as-if-5-BD recut of pre-reform campaigns as the placebo;
- the week-10 gate is self-passing (two of five margins are mechanical identities);
- fact1 hygiene: the 75.6% headline depends on an undocumented 60-BD trim (untrimmed 70.8%),
  corporate-action pooling, 0.64–0.68 parse rates, self-reported trigger dates;
- feasibility: **CRSP/WRDS access unconfirmed (kill gate)**; no M&A database; Item 5(c)
  extraction 4–8+ weeks from zero; **the claimed merger-chronology "comparative advantage"
  does not exist in this repo** (verify whether it lives in your other M&A/Gorbenko projects);
  the 26-week schedule is not executable as written.
- **The repair that unlocks it:** target-level predetermined exposure — required-trading-days-
  to-5% = (0.05 × shares outstanding)/(participation rate × pre-trigger 6-month ADV) — defined
  for one-time filers, enabling activist×quarter fixed effects; near-term well-powered
  outcomes; extensive-margin counts at liquidity-decile×quarter; Lee bounds facing every
  conditional-on-filing estimate.

### Q3 — Is this ensemble the best achievable in the time frame?
**Not as configured by the pivot — and not as first configured by my own synthesis either.**
The Fable red-team (single max-effort call, passed first try) corrected my framing with the
swarm's own evidence, and I adopt its corrections:

> **The reform is the paper; the window is the model.** The JMP-grade paper is the *first
> realized evaluation of the SEC's 2024 13D acceleration* — headline: the chilling/substitution
> result (entry & composition dose-response on required-trading-days exposure, paired with
> Item 6 cash-settled-derivative substitution through the hole left by the dropped 13d-3(e),
> adjudicating DERA's own $810M/yr projection) — with the event-time-invariant gain anatomy as
> the second act and capitalization demoted to a measurement lemma (citing C-L 2025 and BETT
> 2014). The 10–14pp deadline-accumulation model is the disciplining lens, built **only after**
> a pre-registered, price-free, 2–3-week EDGAR first-stage pass shows some non-mechanical
> margin actually moved. Realistic tier: RF/JFQA with RFS upside earned by the chilling result;
> the null-everywhere world degrades honestly to a JCF-tier policy evaluation.

## The decision package (recommended)

**Gate 0 (week 1): advisor ratification.** No plan in this repo shows a faculty checkpoint on
abandoning a 92-page JMP direction on AI advice. Two-page decision memo (this report
compressed), advisor meeting first. *(Kill-severity process risk — red-team finding.)*
**Gate 1 (weeks 1–2):** WRDS/CRSP request + Bloomberg checklist, calendar-booked (these two
one-hour items have sat open since June 10 — the single most informative datum on schedule
realism). Sample decision: 2022–2026 core + SEC published tables as pre-period anchor.
**Gate 2 (weeks 2–4): pre-registered EDGAR-only first-stage pass** (no model writing yet):
untrimmed stake-at-filing distributions split by corporate-action status; Item 6 derivative
language pre/post; entry counts and composition by a coarse price-free exposure proxy; MDEs
computed now from SEC Tables 3/5/6. At least one non-mechanical margin moves → build the
deadline model; none moves → accounting lemma + corner model only, paper re-aimed at anatomy +
well-measured policy null.
**In parallel (bounded 1–2 weeks): hygiene pass on draft_v2.tex** before freezing it as a
standalone working paper — T1's enumerated fixes: delete/soften the four 5%-vs-3% claim sites;
fix line 971; rescale the welfare section (A5); fix rem:A5margins arithmetic; swap Lemma 5's
convexity sentence for the App. B.1 single-crossing argument; one-line corner convention;
narrow the contribution sentence to branch-partitioning; re-attribute AFS→C-L at lines 101/130;
reframe the J-S gloss as the paper's own interpretation; add Burkart–Lee.
**Clock:** re-baseline to ~9 months for a full draft; **Mar 2027 = milestone talk** (first-stage
facts + exposure measure + model skeleton + anatomy pilot), full draft summer 2027. Published
cut order if it slips: chronologies (already out) → signaling block → full deal-universe anatomy
(shrink to hand-collected acquired-target subsample) → 2010–21 backfill → EDGAR-only fallback.
**Scoop defense:** post the first-stage facts + design as an SSRN WP once the exposure design
locks (~month 4–5); re-run the L6 novelty sweep and the C-L 2025 publication check at each
revision.

## What survives from pivot.md, in one line each
Adopt: the abandonment of the liquidity-hump headline as the JMP; the 2024-reform centering;
the three-channel intuition; the gain-decomposition idea (restated event-time-invariant); the
Gaussian-noise falsification exercise (week 1, cheap closure). Reject: the capitalization
headline; the reduced-form C_x as stated; the activist-level exposure design; the triple
interaction; the 26-week clock; the "existing chronology advantage" premise; several citations
(list above). The pivot was right that a better paper exists and wrong about which paper it is.

## Residual caveats
- All-Anthropic-adjacent judgment tier (the red-team flagged itself): the factual layer is
  executed/quote-grepped and family-independent, but tier folklore may be correlated. Cheap
  insurance if desired: one GPT-lane read of the two-page decision memo, plus the advisor.
- C-L 2025 is R&R at RFS — recheck its published form at every revision.
- BET 2008 chapter verified only via the 2025 successor survey (SSRN 403'd); J-S conclusion
  based on the author-posted JFE version.
- Power numbers are analytic MDEs, not simulations.

---

## Addendum (2026-08-02, post-outline adversarial review)

The outline build's cross-family review (GPT-5.6 Sol, task W5b, 14 logged checks) surfaced one
substantive correction, adopted into the outline: **the RTD/exposure narrative must be timed at
the statutory trigger** --- the five-business-day clock starts when the activist CROSSES 5%
(SEC 33-11253), so the window constrains post-crossing accumulation, not assembly of the
initial threshold stake. RTD_i (formula unchanged) is now stated as trading days per five
percentage points of ownership at the participation cap; the binding condition is stated for
the post-trigger increment (window permits >= another 5pp iff RTD_i <= d). Design, data map,
and MDE arithmetic unchanged. Sol's other confirmed catches, all applied: Amihud sign-reading
slip in the empirics prose; residual equal-billing of model and evaluation in the framing;
Corum--Levit positioning-table Window cell (partial -> no); RTD notation unification; weeks 5--8
re-scoped to the critical path. Refuted after boss verification against sources: "empty
abstract" (file carries a full abstract), "29% reversed" (SEC lines 7742--44 support the
outline's reading --- 29% of ALL 2022 filings already within 5BD, = 41% of timely filings; a
clarifying denominator parenthetical was added; the W3 grounding record was already correct).

**Fable gate (same day):** the budgeted max-effort final gate reviewed the revised worktree
document (891s, PASS, confidence high): verdict **SHIP-WITH-EDITS**. It confirmed the
re-timing surgery is legally correct and near-totally consistent, confirmed the refutations of
Sol's F2/F3, and caught the surgery's own residue: the untimed pre-trigger phase sat inside
both trigger-anchored measurement windows --- the P0 anchor (G1) and the six-month ADV window
feeding "predetermined" RTD (G2), a toward-the-null bias concentrated in the high-exposure
tail. All eleven gate findings (G1--G11, incl. the nested-abstract page-1 defect G9 and a
misplaced bett2014 cite G7) were applied. Remaining risks, in the gate's order: CRSP/WRDS
access, Item 5(c) extraction burden, and the modal-null world --- all disclosed in the outline.
