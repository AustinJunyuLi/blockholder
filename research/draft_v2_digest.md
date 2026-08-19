# Manuscript Digest — `draft_v2.tex` ("Liquidity, Activism Disclosure, and Takeover Premia")

**Author:** TaskB_DigestAgent
**Date:** 2026-08-18 (current-turn date)
**Scope:** Full read of `draft_v2.tex` (all 3041 lines) + the two `\input` derivation records (`quality_reports/fixes/D7_takeover_game_microfound.tex`, 303 lines; `D8_GE_dominance_MCS.tex`, 214 lines). D1/D4/D5/D6 `.tex` files in `quality_reports/fixes/` are the archived sources of material already inlined in the draft (D4 = App. `app:bg`, D5 = App. `app:d5`, D6 = existence section); only D7/D8 are external inputs. Verification scripts (`dN_*_check.py`, JSON artifacts) were listed but not re-run.
**Access summary:** everything read first-hand from the repo. No external content used. Uncertainties flagged inline.

---

## 1. Section/subsection map

- **Abstract** — R2 (disclosure attenuation) headlined; R1 (hump with endpoint symmetry) as "supporting comparative static"; D7 wedge microfoundation and D8 certified region advertised.
- **§1 Introduction** (l. 90–103) — exit-voice framing; four-action model; two results; policy hook (US 5% vs UK 3%); roadmap. No data content.
- **§2 Related Literature** (l. 104–136) — three strands: exit/voice (Hirschman→Edmans), microstructure/feedback (Kyle, EGJ 2012/2015), activism×takeovers (Grossman-Hart; structural: Gantchev, AFS, J&S, C&L). Closest antecedent EGJ 2015; closest design competitor OC&B 2022. Contains the AFS misattribution (see §5).
- **§3 Model** (l. 138–378) — timeline (t=0,1,1.5,2); dominance Lemma `lem:dominance`; fundamentals (Gaussian v, signal s); ternary noise z with intensity κ; disclosure rule D=1{q=+1}; engagement cost C(s)=C₀e^{−χ·(s−μ)/σ_s}, success prob ρ, wedge m₁>m₀; bidder entry rule with Gaussian synergy ξ; pricing fixed point P=δE[Y|X,D]; PBE definition; standing assumptions (A1)–(A7).
- **§4 Equilibrium Characterization** (l. 380–996) — cutoff structure Prop 1; action probabilities; conditional means (Mills ratios); posteriors Prop 2; price fixed point and decomposition Prop 3; bid monotonicity; cutoff indifference equations; existence block (polytope Θ, Lemmas `bounded`/`selfmap`/`BP-BQ`/`monotone`, Brouwer Prop `existence`); A7-redundancy Lemma `dropA7`; A5 split into (A5a)/(A5b) with honest Remark `A5margins`; uniqueness-as-numerical-regularity Remark `numreg`; the hump block: endpoint-symmetry Lemma, channel-(A) Lemma `d1-jensen` under (C*), Hypothesis `d1-cutoffshift`, conditional-hump Prop `nonmonotone`; disclosure attenuation Prop `disclosure-attenuation` (proof sketch).
- **§5 Comparative Statics and Numerical Analysis** (l. 999–1091) — baseline calibration (Hold collapses, k₀=k₁); figures referenced; within-regime posterior comparative statics (proved); takeover-environment statics (proved); sensitivity in C₀, wedge, ρ, σ_ξ, δ (all numerical).
- **§6 Testable Implications** (l. 1094–1121) — five predictions: (1) cross-country attenuation; (2) zero-abnormal-volume predicts bids; (3) hump in Amihud quintiles; (4) 13D event-study return increasing in illiquidity; (5) 13D targets: lower bid hazard, higher conditional premia.
- **§7 Welfare Analysis** (l. 1124–1714) — welfare objects and transfer netting Lemma `transfer-netting`; liquidity planner κ* vs κ† (Lemmas `no-env-WB`/`no-env-other`, Prop `planner-wedge`, condition (W*)); disclosure-threshold planner (Lemma `reclass-jump`, Prop `disclosure-wedge`, hypotheses (i)–(ii)); first-best benchmark (Prop `firstbest-d2`, Cor `cons-vs-fb`).
- **§8 Extensions** (l. 1717–1802) — institutional box (13D 5%/5-business-days since 2024-02-05; UK DTR5 3%; EU TD; 30% mandatory-bid confounder); full-disclosure and no-disclosure benchmarks (definitions only); noisy-rumor regime (numerical flattening); GE disclosure Prop `ge-disclosure` (exact decomposition, net sign indeterminate).
- **§9 Conclusion** (l. 1804–1812).
- **App. A Notation** (l. 1823–1905) — symbol table + (A1)–(A7) table.
- **App. B Proofs** (l. 1908–2451) — proofs of Props 1–3, disclosed-branch invariance, truncated-normal lemma, bid monotonicity, within-regime statics, cutoff equations, minority decomposition, existence recap, uniqueness-as-regularity, D1 block (realized D=0 law table; posterior variance Lemma `d1-variance`, closed form strictly U-shaped; curvature Lemma `d1-curvature` and condition (C**)), D1-GE block (Lemma `d1-ift`, C¹ map + computable residual bound), extension posterior derivations.
- **App. `app:bg`** (D4, l. 2464–2666) — bargaining reading of (m₀,m₁): Condition `cond:bg` (threat-point shift d(1)−d(0)=λρΔ_eng); Nash split Lemma `bg-split`; wedge is ξ-free; reduced-form nesting Prop `bg-reduced` + set-identification Remark `bg-ident`; ρ² event tree Lemma `bg-tree`; A3 as conditional Theorem `bg-A3`; level-shape Prop `bg-levelshape`; state-dependent-wedge numerical regularity `nr:bg-statedep`; honesty ledger.
- **App. D7** (`\input`, 303 lines) — disagreement-node tender game solves λ = 1−q(1−γ)ψ.
- **App. `app:d5`** (l. 2682–2840) — A2-robustness: persuasion vs entrenchment cost regimes; endpoint symmetry re-proved; (GE-dom) conditional claim; the vacuity admission `rem:d5-vacuous`.
- **App. D8** (`\input`, 214 lines) — region theorem + certified counterexample.
- **App. Tables/Figures** (l. 2849–3041).

## 2. Named-result inventory (label — one-line statement — honesty — key assumption)

**Body/§3–§4:**
- `lem:dominance` — engaged exit and silent buy are (weakly/strictly) dominated; four-action menu is a result — proved — D=1{q=+1}, C(s)>0 (A2), m̃>m₀ (A3).
- `prop:cutoffs` (Prop 1) — PBE exists in weakly ordered cutoff strategies k₁≤k₀≤k_D over E/H/Q/P — proved (proof via App. B: single-crossing + (A5) fixed point + (A6) contraction for the *uniqueness* step; see tension below) — (A1) interiority, (A2), (A4), (A5); the B_P−B_Q>0 step leans on equilibrium bid deterrence (patched by `lem:BP-BQ`).
- `prop:posteriors` (Prop 2) — π(X,1)=1; closed-form π(X,0) rational in (ω,κ); π(−2,0)=0 — proved (Bayes; full support) — ternary noise law.
- `prop:price-decomp` (Prop 3) — price splits into standalone + activism-premium (standalone/takeover channels) — proved — conditional independence of bid indicator given (X,D).
- Bid monotonicity (`app:proof-bid-monotone`, unnumbered) — ∂p/∂P<0, ∂p/∂π<0 — proved — Gaussian ξ, (A3).
- `lem:bounded`, `lem:selfmap` — best-response cutoffs uniformly bracketed; T:Θ→Θ continuous, order-preserving — proved — (A1),(A2),(A4).
- `prop:existence` — monotone-cutoff equilibrium exists — proved via Brouwer on the cutoff polytope Θ — (A1),(A2),(A4).
- `lem:BP-BQ` — Public Voice slope exceeds Quiet Voice slope (η≥1 from trading; more under p(X,1)≤½) — proved; sufficient condition fails at baseline (p*=0.847) but is unnecessary — price-taking blockholder.
- `lem:monotone` — action correspondence nondecreasing in s; upper envelope convex — proved — slope ordering B(E)<B(H)=B(Q)<B(P).
- `lem:dropA7` — price-conditioned bidder identical to (X,D)-conditioning; (A7) redundant — proved modulo injectivity asserted "at any nondegenerate calibration" (not derived).
- `rem:A5margins` — honest admission: baseline violates the conservative (A5a) sufficient bound (0.805+0.947>1); A5a is a *maintained assumption* — n/a.
- `rem:numreg` — uniqueness is a numerical regularity (30/30 multistart convergence), not a theorem — numerical.
- `lem:endpoints` — Δ^min(0⁺)=Δ^min(1⁻) (same two-point D=0 posterior law {0,π̄} at both liquidity limits) — proved — noise symmetry P(z=+1)=P(z=−1), cutoff convergence.
- `lem:d1-jensen` — at fixed cutoffs, channel (A) of dΔ^min/dκ is strictly hump-shaped iff chord condition (C*): C(π̄)=h(0)−2h(π̄/2)+h(π̄)<0, h=πp — proved conditional on (C*) — exact finite-support Jensen.
- `hyp:d1-cutoffshift` — GE cutoff-shift channel B(κ) does not overturn single-peakedness — **numerically verified, not proved** (its name says so).
- `prop:nonmonotone` (R1) — Δ^min single-peaked with unique interior κ†; trough if (C*) fails — **conditional theorem** (C* + Hypothesis) — everything GE is the exposed flank.
- `prop:disclosure-attenuation` (R2) — at fixed cutoffs, |∂Δ^act/∂κ| is decreasing in disclosed mass ω_P — **proof sketch only**, explicitly partial equilibrium — disclosed-branch κ-invariance.
- Within-regime liquidity statics (`app:proof-cs-liquidity-within`) — ∂π(1,0)/∂κ=0, ∂π(−1,0)/∂κ≥0, ∂π(0,0)/∂κ≤0 — proved.
- Takeover statics (`app:proof-cs-takeover`) — ∂p/∂S̄>0, ∂p/∂K<0, sup|∂p/∂P|=φ(0)/σ_ξ — proved.

**Welfare (§7):**
- `lem:transfer-netting` — prices/premia net out of W; W = E[1{bid}(S̄+ξ−K−v−aΔ̃)+v+aΔ̃−aC] — proved — unit share mass, δ=1 normalization.
- `lem:no-env-WB`, `lem:no-env-other` — cutoff-shift terms do *not* vanish by envelope — proved.
- `prop:planner-wedge` — sgn(κ*−κ†)=sgn B(κ†) — conditional: single-peakedness is numerical regularity; (W*) a stated hypothesis; at baseline B(κ†)≈0 (equality case).
- `lem:reclass-jump` — reclassification jump Σ_P−Σ_Q = p₁*(S̄−K−E[v|k_D]−Δ̃)+σ_ξφ(T₁) — proved — Gaussian ξ truncation identity.
- `prop:disclosure-wedge` — k_D*<k_D^eq (underdisclosure) under (i) positive jump + (ii) G(k_D^eq)≥0 — conditional; **(ii) is unverified even numerically (draft says so, l. 1624–27)**.
- `prop:firstbest-d2`, `cor:cons-vs-fb` — first-best engages/discloses more; k_D^FB ≤ k_D* < k_D^eq — proved conditional on the same hypotheses.

**Extensions (§8):** `prop:ge-disclosure` — dΔ^act/dτ = transparency (≥0, fixed masses) + deterrence (≤0 via ω_Q+ω_P) exact decomposition; net unsigned — proved as decomposition, unsigned net.

**App. bg (D4):** `lem:bg-split` (proved), `prop:bg-reduced` + `rem:bg-ident` (θ only set-identified; proved), `lem:bg-tree` (ρ² two-draw; proved), `thm:bg-A3` (A3 conditional on `cond:bg`; proved-conditional), `prop:bg-levelshape` (proved), `nr:bg-statedep` (numerical).

**App. D7:** `lem:d7-floor` (free-rider floor b̂*=Z(a)−φ), `lem:d7-entry` (entry prob q=H(φ), state-blind), `lem:d7-bloc` (pivotal bloc tenders iff S_F≥φ+(1−γ)aδ_e) — all proved. `prop:d7-lambda` — λ=1−q(1−γ)ψ∈[0,1] in closed form — proved. `cor:d7-BG` — Condition BG's form derived — proved. `thm:d7-A3` — A3 holds iff not (F1 certain raids ∧ F2 γ=0 ∧ F3 unblockable) — proved. `prop:d7-afs` — measured premium M(π)=m̄/P strictly decreasing in π for λ<λ_crit — proved (fixed cutoffs, IFT on the price). Institutional primitives carried openly: equal-treatment offers, GH tie-breaking, exogenous (φ,τ_c), one-shot fringe.

**App. d5:** `prop:d5-a2` (ordering survives any persuasion-regime cost C′<Λ; A2 sufficient not necessary — proved); `def:d5-regimes`, `rem:d5-mech` (falsifiable signature); `lem:d5-twopoint`, `lem:d5-chord`, `lem:d5-Cstar` (proved); **`rem:d5-vacuous` — the curvature condition cannot fail anywhere in the calibration family (a(π)<0 throughout), so hump-vs-trough is produced entirely by the GE channel**; `lem:d5-endpoints` + `prop:d5-peak` (endpoint symmetry + existence of an interior maximizer — proved, unconditional); `claim:d5-singlepeak` (strict single peak under (GE-dom) — conditional); `rem:d5-conditional` (chord diagnostic matches orientation 16/20 cells).

**App. D8:** `lem:d8-pricing` (pricing layer C¹ under A5 — proved); `lem:d8-cutoff` (‖dk/dκ‖≤‖∂_κT‖/(1−L), inversion-free — proved under quantified A6); `lem:d8-weights` (explicit weight decomposition — proved); `thm:d8-region` — strict single peak *as a theorem* on regions satisfying checkable (R1) pointwise dominance + (R2) integral control — proved conditional on (C*)+A1–A7; `cor:d8-baseline` — certified interval [0.35,0.825] inversion-free, [0.30,0.85] exact-IFT, L≤0.836 — **computationally certified** (script + JSON); `prop:d8-counter` — at σ_ξ=0.60 cells, channel (A) single-peaked yet Δ^min is a trough; Hypothesis `d1-cutoffshift` false globally; region restriction not removable — certified numerics + proved logic; `rem:d8-boundary` (economic boundary: GE wins where entry is premia-insensitive).

## 3. Model architecture as written

- **Players:** one risk-neutral blockholder (initial stake normalized to 1 share, private signal s=v+ε); a noise trader; a competitive (zero-profit) market maker; one potential bidder with private synergy shock ξ~N(0,σ_ξ²). All risk-neutral.
- **Timing:** t=0 Nature draws v~N(μ,σ_v²), blockholder sees s. t=1 blockholder picks (q,a)∈{(−1,0),(0,0),(0,1),(+1,1)} = Exit/Hold/Quiet/Public (excluded actions eliminated by `lem:dominance`); noise z∈{−1,0,+1} with P(z=0)=1−κ, P(±1)=κ/2; market maker observes X=q+z∈{−2,…,2} and disclosure flag D=1{q=+1} simultaneously, sets P(X,D)=δE[Y|X,D]. t=1.5 bidder observes (P,D,ξ), enters iff Π_B=S̄−P+ξ−m̄(X,D)−K≥0. t=2 payoffs: bid ⇒ Y=P+m^R(a); else Y=v+aΔ̃.
- **Information structure:** ternary order flow is the load-bearing discreteness (contrasted with continuous-trading governance models, footnote l. 116); D is a *stake-triggered* flag mechanically tied to q=+1 — the disclosure threshold τ never appears as an explicit parameter in the model (it is implicit in k_D and surfaced only in §7.2/§8 and Prop `ge-disclosure`). π(X,D)=P(a=1|X,D); disclosed branch trivial (π=1, prices κ-invariant — proved in `app:proof-disclosed-invariance`); nondisclosed branch pools Hold and Quiet Voice (identical order-flow distributions), so inference is pinned by prior masses.
- **Equilibrium concept:** PBE = cutoff strategy + Bayes-consistent π + bidder rule + competitive price fixed point. **Two fixed points:** (i) inner price fixed point per cell (X,D), unique under (A5)/(A5a) — and Remark `A5margins` concedes the baseline fails the conservative sufficient bound, so (A5a) is maintained, not derived; (ii) outer **Brouwer** fixed point of the best-response map T on the cutoff polytope Θ (l. 567–623) — existence unconditional under (A1),(A2),(A4); uniqueness only under (A6) contraction, verified numerically (30-seed multistart, `rem:numreg`).
- **What is numerical:** uniqueness everywhere; the hump outside the D8-certified interval [0.35,0.825] (and its whole orientation per `rem:d5-vacuous`); κ†≈0.59; all §5 sensitivities; the noisy-rumor flattening; welfare alignment B(κ†)≈0; disclosure-planner hypothesis (ii) G≥0 (admittedly unverified).

## 4. Where the paper is heavy — cut-list

The draft carries ~1,100 lines of appendix scaffolding for one conditional headline. Defensive "epistemic ledger" subsections repeat the same proved/conditional/numerical triage five times (App. bg ledger, D7 ledger, D8 ledger, `rem:A5margins`, `rem:numreg`, `rem:d5-conditional`). Endpoint symmetry is proved three times (`lem:endpoints`, `lem:d5-endpoints`+`prop:d5-peak`, restated in D8). Concrete cuts:

1. **App. `app:bg` (l. 2464–2666, ~200 lines) → compress to ~2 pages.** Keep `cond:bg`, the ξ-free wedge, `thm:bg-A3`, `rem:bg-ident` (set-identification is referee bait but cheap). Delete the reconciliation arithmetic (l. 2618–19), `prop:bg-levelshape`, `nr:bg-statedep` (numerical curiosities). *Cost:* the ρ² event-tree lemma (`lem:bg-tree`) is a genuine subtlety a referee could attack; keep it as one remark.
2. **App. `app:d5` curvature material (l. 2738–2801) → cut or fold into D1.** `lem:d5-chord`/`lem:d5-Cstar` duplicate App. B's `lem:d1-curvature`. *Cost:* `rem:d5-vacuous` is the paper's most honest sentence (curvature condition vacuous on the whole calibration family ⇒ the hump is wholly GE); deleting it hides the weak point a sharp referee will find anyway. Keep the A2-robustness `prop:d5-a2` (one page, genuinely useful).
3. **Welfare §7 (l. 1124–1714, ~590 lines) → halve.** The κ*-vs-κ† wedge ends in "approximately equal at baseline" (low yield); the first-best subsection (l. 1629–1714) and `prop:disclosure-wedge` rest on hypothesis (ii) that the draft itself says is numerically untested — a top-3 referee will either demand the test or strike the proposition. Cut first-best entirely; downgrade `disclosure-wedge` to a remark. *Cost:* loses the normative "underdisclosure" hook — but OC&B 2022 owns optimal-threshold welfare language, so the loss is small.
4. **Extensions §8.1–8.2 (full/no-disclosure benchmarks, l. 1751–1765) → one paragraph.** They are definitions, not results. *Cost:* negligible. Keep noisy rumors (it is the only bridge to wolf packs/media) but label the flattening as numerical.
5. **Equilibrium-section meta material (l. 658–703: `dropA7`, A5a/A5b split, two honesty remarks) → one remark.** *Cost:* uniqueness/A5 questions get a shorter answer; acceptable.
6. **Testable implications 2 and 5 (l. 1106–08, 1118–20)** — zero-abnormal-volume and hazard-rate tests are the weakest (data needs: SharkRepellent; identification vague). *Cost:* minor; predictions 1, 3, 4 carry the empirical program.

## 5. Current framing and weakest narrative points

**Framing in 5 sentences.** (1) The paper asks how a stake-triggered disclosure threshold shapes the liquidity-sensitivity of takeover premia. (2) An informed blockholder chooses Exit/Hold/Quiet Voice/Public Voice; a market maker prices from (X,D); a bidder enters on (P,D,ξ); disclosure partitions inference into a disclosed branch (premium observed) and a nondisclosed branch (premium inferred). (3) The headline is disclosure attenuation (R2): stricter disclosure moves the premium onto the observable basis and lowers its liquidity sensitivity, with a cross-country prediction (UK 3% vs US 5%). (4) The supporting result (R1) is a conditional, single-peaked Δ^min(κ) with exact endpoint symmetry, certified as a theorem only on a D8 region; the wedge m₁>m₀ is microfounded by the D7 tender game (λ=1−q(1−γ)ψ). (5) Positioning: EGJ 2015 is the closest antecedent, OC&B the closest design paper, CCKV 2026 the dynamic pre-disclosure complement, and the structural-estimation papers (AFS, J&S, C&L) are cast as taking as exogenous what this paper makes equilibrium objects.

**Weakest points for a top-3 referee:**
1. **The headlined "disclosure-attenuation theorem" is a partial-equilibrium proof sketch.** Prop `disclosure-attenuation` holds cutoffs fixed and is sketched in four sentences; the paper's own `prop:ge-disclosure` then shows the GE net sign is indeterminate. The abstract's word "theorem" overclaims relative to what is proved where it matters.
2. **R1's conditionality is more fragile than the abstract admits.** The abstract says "under a transparent primitive condition on the price-elasticity of bids"; `rem:d5-vacuous` concedes that condition is vacuous on the entire calibration family, so the hump's sign is wholly a GE/numerical object outside the certified interval [0.35,0.825] — and `prop:d8-counter` proves it inverts at high σ_ξ. A referee who reads D5/D8 will find the abstract-to-appendix gap.
3. **The institutional mapping is loose and one citation is wrong.** D=1{q=+1} ties disclosure to a one-unit buy, not a 5% threshold or the 10→5-day window; the SEC-2024 shock and cross-country thresholds appear only in §6/§8 narrative, never inside the model. Worse, the draft attributes to AFS 2022 the "activism lowers bid premia 13.7%/5.2pp" estimate (abstract; l. 130; D7 `prop:d7-afs` motivation) — that estimate is **Celentano & Levine 2025** (AFS estimate announcement-return decompositions, no premia; see `research/lit_disclosure-structural-activism.md` ⚠ corrections). The J&S sentence claiming their accumulation window "is the lever the 2024 acceleration moves" is also unsupported by J&S (one footnote on the ten-day rule).

## 6. Provable vs numerically locked; shortest route to promote R2

- **Proved outright:** posteriors; price decomposition; bid monotonicity; dominance; existence (Brouwer); endpoint symmetry; disclosed-branch invariance; within-regime posterior statics; posterior-variance U-shape (`lem:d1-variance`, closed form); transfer netting; reclassification jump; D7 in toto (λ closed form, A3 boundary F1–F3, measured-premium reversal `prop:d7-afs` at fixed cutoffs); D8 lemmas and the region theorem as a *checkable-hypothesis* theorem.
- **Conditional (named hypotheses):** `prop:nonmonotone` ((C*) + cutoff-shift dominance); `prop:planner-wedge` ((W*) + numerical single-peak); `prop:disclosure-wedge` ((i) + (ii), (ii) untested); `thm:bg-A3` (Condition BG — discharged by D7).
- **Numerically locked:** uniqueness; the hump outside κ∈[0.35,0.825]; κ†; all sensitivity figures; rumor-regime flattening; GE-disclosure net sign; hypothesis (ii) of the disclosure wedge.
- **Shortest route to promote R2 to a clean theorem.** R2's fixed-cutoff core is already 90% proved: (a) disclosed branch κ-invariance is proved (`app:proof-disclosed-invariance`); (b) the D=0 block's κ-dependence is characterized in closed form (`lem:d1-variance` + the two-point law). The missing step is small: parameterize strictness τ as a shift of mass from the inferred to the disclosed branch (ω_P↑, e.g. via k_D or an explicit threshold in the q=+1 region), write Δ^act(κ;τ)=(m̃−m₀)[ω_P p̄₁ + (1−ω_P)·E_{D=0}h], and compute the cross-partial — its sign is one line because the disclosed component is κ-free. That yields a genuine fixed-cutoff theorem (upgrade the proof sketch). For the GE version, do not chase a global sign (D8's counterexample logic warns against it); instead reuse `lem:d8-cutoff`'s inversion-free bound to certify a *region* theorem for the cross-partial, exactly parallel to `thm:d8-region`. Estimated work: days, not weeks; all machinery exists in the repo.

## 7. Figures and tables (all in App. "Tables"/"Figures" unless noted)

- **fig:timeline** (l. 175–201, body) — TikZ timeline; no numerical content.
- **tab:notation, tab:assumptions** (App. A) — hand-written symbol/assumption tables; no numerical content. **tab:params** — hand-written baseline values; mirrors `numerical_output/data/baseline_params.csv` but not generated from it. **tab:d1-D0cells** (App. B) — analytical cell enumeration; no numerical content.
- **tab:example** — `\input{numerical_output/table_example.tex}`; baseline equilibrium prices/posteriors/payoffs. **Numerical.**
- **tab:disclosure-extensions** — `\input{numerical_output/table_disclosure_extensions.tex}`; posteriors under FD/ND/NR regimes at fixed cutoffs. **Numerical.**
- **fig:cutoff-structure** — signal-space partition at baseline (Hold collapsed). Numerical.
- **fig:nonmonotone** — the R1 hump, Δ^min(κ) with κ† dashed. Numerical.
- **fig:decomposition** — baseline vs activism components of Δ^min. Numerical.
- **fig:prices** — equilibrium prices by (X,D) with π annotations. Numerical.
- **fig:cutoffs-kappa** — cutoff paths in κ. Numerical.
- **fig:disclosure** — the R2 figure: Δ^act(κ) with vs without disclosure at fixed cutoffs. Numerical (partial-equilibrium object; matches Prop `disclosure-attenuation`).
- **fig:sensitivity-{C0,wedge,rho,sigma_xi,delta}** — five robustness sweeps. Numerical.
- **fig:noisy-rumor-precision** — rumor precision flattening Δ^min. Numerical.
- **fig:welfare** — W and components vs κ; caption itself restates the conditional/honesty caveats. Numerical.
- **fig:ge-decomposition** — D8 product: channel (A)/(B) split + hump/trough map over (S̄,σ_ξ). Numerical (certified).
- **fig:wedge-primitives** — D7 product: Δ^min under λ=1−q(1−γ)ψ, sweeping γ and q. Numerical.

All 15 PDFs regenerate from `numerical_output/data/*.csv` via `pyfig/` (`make figures`); the two `.tex` tables from `numerical/export_data.py` (`make data`). Nothing in the paper's displayed output is hand-computed except the static tables.
