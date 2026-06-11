# Manuscript-wide mathematical consistency audit — draft_v2.tex

**Date:** 2026-06-11
**Scope:** `/Users/austinli/Projects/blockholder/draft_v2.tex` (3,041 lines) + spliced records `quality_reports/fixes/D7_takeover_game_microfound.tex`, `D8_GE_dominance_MCS.tex` (via `\input`); cross-checked against D1–D8 derivation records, `quality_reports/fixes/*.json`, and `numerical_output/data/*.csv`. Read-only audit; no repo file edited (this report is the only new file).
**Numerical probes:** solver re-runs at κ∈{0.05,0.2,0.5,0.8,0.95}, ω/posterior recomputation, πTT′ slack reproduction, welfare.csv argmax checks.

**Inventory: 51 theorem-like results** (28 lemmas, 17 propositions, 3 theorems, 3 corollaries) **+ 1 hypothesis, 1 conditional claim, 1 condition, 1 numerical regularity, 2 definitions, 9 assumptions** (A1–A7 inline + formal A5a/A5b). **Issues: 4 CRITICAL, 10 MAJOR, 9 MINOR.**

---

## 1. Results inventory

Proof-source key: `inline` = proof environment at statement; `app:X` = appendix subsection; `D-rec` = backed by a derivation record in `quality_reports/fixes/`. Match: OK / GAP / FAIL.

| # | Label | Type | Line | Statement gist | Proof source | Stmt–proof match | Assumptions cited / actually used |
|---|-------|------|------|----------------|--------------|------------------|-----------------------------------|
| 1 | `lem:dominance` | Lem 1 | 159 | Engaged exit & silent buy dominated; 4-action menu is a result | inline | OK (part ii honestly conditional) | A2, A3 cited & used |
| 2 | (PBE) | Def 1 | 367 | Equilibrium concept | — | — | — |
| 3 | `prop:cutoffs` | Prop 1 | 390 | Monotone-cutoff PBE exists, k1≤k0≤kD | app:proof-cutoffs (1911) | GAP: Step 1's B_P>B_Q claim is equilibrium-dependent ("ensuring p(X,1) sufficiently lower"), not derived; Step 3 invokes A6/Banach (covered by "Standing Assumptions" blanket) | Standing (blanket) / uses A1,A2,A3,A5,A6 |
| 4 | `prop:posteriors` | Prop 2 | 446 | Posterior formulas π(X,D) | app:proof-posteriors (1966) | OK — formulas match line-by-line | none needed; Bayes only |
| 5 | `prop:price-decomp` | Prop 3 | 514 | Price = standalone + activism premium channels | app:proof-price-decomp (2092) | OK ("unique price" presumes A5, uncited in statement) | A5 implicit |
| 6 | `lem:bounded` | Lem 2 | 588 | Uniform bracket for best-response cutoffs | inline | OK | cites A1,A2,A4; uses bounded prices (needs A5a-type uniqueness for P well-defined) |
| 7 | `lem:selfmap` | Lem 3 | 603 | T continuous, maps Θ into itself | inline | GAP: continuity of "prices" as function of cutoffs needs unique inner fixed point = A5(a), not cited | cites A1,A2,A4; uses A5a, slope ordering |
| 8 | `prop:existence` | Prop 4 | 616 | Existence via Brouwer | inline | GAP: same A5(a) + slope-ordering omission (see M5) | cites A1,A2,A4 |
| 9 | `lem:BP-BQ` | Lem 4 | 625 | B(P)>B(Q) whenever p(X,1)≤½ | inline | FAIL: footnote self-contradicts and quotes stale numbers (see C4); "+1 from trading" inconsistent with eq:U-affine slopes (M5) | none cited; uses pricing structure |
| 10 | `lem:monotone` | Lem 5 | 644 | Monotone best response given slope ordering | inline | OK (conditional on eq:slopes, which is itself problematic — M5) | A1, A2 + slope ordering |
| 11 | `lem:dropA7` | Lem 6 | 661 | (A7) redundant if bidder conditions on P | inline | GAP (minor): injectivity "at any nondegenerate calibration" is itself an A7-like premise | none |
| 12 | `ass:A5a`/`ass:A5b` | Assum 1–2 | 678/690 | Inner-price contraction; cross-cutoff stability | maintained | — (honest) | — |
| 13 | `lem:endpoints` | Lem 7 | 795 | Δmin limits equal at κ→0⁺,1⁻ | inline + app:proof-d1-variance; D1-rec | OK (limit statement; remark 827 warns) | Standing; fixed-masses step + UHC-type interchange (D1 record states UHC as hypothesis; body proof is terser) |
| 14 | `lem:d1-jensen` | Lem 8 | 840 | Channel (A) hump under (C*), fixed cutoffs | inline | OK (exact finite-support Jensen) | (C*) |
| 15 | `hyp:d1-cutoffshift` | Hyp 1 | 905 | GE channel does not overturn (A) | — (numerical; falsified globally by D8) | OK — honestly labelled | A6 for C¹ |
| 16 | `prop:nonmonotone` | Prop 5 | 918 | Conditional hump, unique interior κ† | inline (combines 13–15) | OK as conditional; minor: stated "on [0,1]" with Δmin(0)=Δmin(1) though κ∈(0,1) (m3) | (C*) + Hyp 1 |
| 17 | `prop:disclosure-attenuation` | Prop 6 | 987 | PE: |∂Δact/∂κ| decreasing in ω_P | proof *sketch* only | GAP: claimed monotonicity in ω_P not established (M4) | A5 via disclosed invariance |
| 18 | `lem:transfer-netting` | Lem 9 | 1182 | P and m^R net out of W | inline; D2-rec | OK (identity verified numerically: W=W_min+W_bid+W_B exact) | δ=1 normalization |
| 19 | `lem:no-env-WB` | Lem 10 | 1290 | W_B cutoff-shift term survives envelope | inline; D2-rec | OK | — |
| 20 | `lem:no-env-other` | Lem 11 | 1336 | Same for W_min, W_bid | inline; D2-rec | OK | — |
| 21 | `prop:planner-wedge` | Prop 7 | 1357 | sgn(κ*−κ†)=sgn B(κ†) | inline; D2-rec | OK (single-peak carried as Numerical Regularity inside statement — honest) | (W*) + NR |
| 22 | `lem:reclass-jump` | Lem 12 | 1496 | Σ_P−Σ_Q closed form | inline; D2-rec | FAIL: Σ_Q assumes no bids on D=0 branch — contradicts model (C2) | A4; Gaussian ξ |
| 23 | `prop:disclosure-wedge` | Prop 8 | 1541 | Underdisclosure given (i),(ii),NR | inline; D2-rec | OK internally, but inherits C2 through Σ_Q | (i),(ii),NR — all carried in statement (good) |
| 24 | `prop:firstbest-d2` | Prop 9 | 1635 | First-best action rule | inline; D2-rec | FAIL: −m̃ term in eq:fb-engage contradicts transfer netting (M1); single-crossing direction (decreasing) sets up C1 | Gaussian ξ |
| 25 | `cor:cons-vs-fb` | Cor 1 | 1662 | k_D^FB ≤ k_D* < k_D^eq | inline; D2-rec | FAIL: (a) direction error (C1); (b) quantifier slip on G (M2) | (i),(ii),NR |
| 26 | `prop:ge-disclosure` | Prop 10 | 1790 | GE disclosure trade-off decomposition | **no proof anywhere** | GAP (M3) | none cited |
| 27 | `lem:truncnorm` | Lem 13 | 2021 | Truncated-normal means | inline | OK (standard) | — |
| 28 | `lem:d1-variance` | Lem 14 | 2290 | Posterior variance strictly U-shaped | inline; D1-rec | OK — algebra independently verified (f(0)=f(1)=0; V′(0)=−Q²/2B²; V′(1)=Q²/B² all check) | fixed masses |
| 29 | `lem:d1-curvature` | Lem 15 | 2336 | h″ sign ⇔ πTT′≤2 (C**) | inline; D1-rec | OK — algebra verified; baseline 0.42/slack 1.58 reproduced exactly from model (T(1)=0.943, T′=0.45) | P″≈0 |
| 30 | `lem:d1-ift` | Lem 16 | 2370 | C¹ cutoff map + computable B bound | inline; D1/D3-rec | OK conditional on quantified A6 | A6 cited & used |
| 31 | `cond:bg` | Cond 1 | 2498 | Appropriable threat-point shift | — | — (now derived by D7, cor:d7-BG) | — |
| 32 | `lem:bg-split` | Lem 17 | 2517 | Nash rent closed form + IR | inline; d4-rec | OK | cond:bg |
| 33 | `prop:bg-reduced` | Prop 11 | 2567 | Reduced form = constant-θ case + converse | inline | OK (converse construction checks) | cond:bg |
| 34 | `lem:bg-tree` | Lem 18 | 2581 | ρ² = two independent draws | inline | OK | independence of B₁,B₂ |
| 35 | `thm:bg-A3` | Thm 1 | 2599 | A3 conditional on cond:bg; sharp boundary | inline | OK | cond:bg, θ<1 — cited & used |
| 36 | `prop:bg-levelshape` | Prop 12 | 2631 | Level enters Δmin via κ-free coefficients | inline | OK (E[ξ1{bid}]=σξφ(t) verified) | Gaussian ξ |
| 37 | `nr:bg-statedep` | NumReg 1 | 2658 | Single peak survives state-dep wedge | numerical; D4-rec | OK — all quoted numbers (0.0722→0.0829, peak 0.0776, amp 0.0107, κ*≈0.59→0.60) in D4 record / d4_bargaining_check.py; **κ\* symbol collision (M8)** | baseline calibration |
| 38 | `prop:d5-a2` | Prop 13 | 2707 | Ordering robust to any cost with C′<Λ | inline | FAIL: premise "Λ(s) strictly positive" contradicts model's own eq:UH-UQ ⇒ Λ≡0 at fixed prices (C3) | cites A1,A3–A7; Λ>0 unproved & false |
| 39 | `def:d5-regimes` | Def 2 | 2726 | persuasion vs entrenchment cost | — | inherits C3 (boundary is C′<0, not C′<Λ) | — |
| 40 | `lem:d5-twopoint` | Lem 19 | 2760 | Φ^D0 = ω_H g(0)+ω_Q g(π̄) | inline | FAIL: wrong masses; Exit atom dropped (M6) | two-point law |
| 41 | `lem:d5-chord` | Lem 20 | 2774 | g″ closed form, finite | inline | OK (verified) | affine m̄, P(π)=m̄(π) |
| 42 | `lem:d5-Cstar` | Lem 21 | 2788 | g″<0 ⇔ T(π)/σξ<1 | inline | OK (exact) | same |
| 43 | `lem:d5-endpoints` | Lem 22 | 2806 | Same two-point law at both κ limits | inline | OK; masses (ω_E; ω_H+ω_Q) — **contradicts lem:d5-twopoint's masses** (M6) | fixed cutoffs |
| 44 | `prop:d5-peak` | Prop 14 | 2814 | Endpoint symmetry + interior maximizer | inline | OK (Weierstrass; survives M6 since only "fixed function of cutoffs" is needed) | continuity + cutoff convergence (stated) |
| 45 | `claim:d5-singlepeak` | NamedClaim 1 | 2821 | Unique peak under (GE-dom) | inline | OK conditional | (GE-dom) stated |
| 46 | `lem:d7-floor` | Lem 23 | D7:105 | Free-rider floor b̂*=Z−φ | inline; d7-rec | OK (selection institution flagged in ledger) | GH tie-break selection |
| 47 | `lem:d7-entry` | Lem 24 | D7:122 | Entry iff c_F≤φ, state-blind | inline | OK | one-shot fringe |
| 48 | `lem:d7-bloc` | Lem 25 | D7:139 | Blocking rule | inline | OK ("one-line computation" hand-wave for above-floor offers honestly parked in ledger) | equal-treatment offers |
| 49 | `prop:d7-lambda` | Prop 15 | D7:161 | d(1)−d(0)=λδe; λ=1−q(1−γ)ψ | inline; d7-rec | OK — layer-cake step verified; MC check passes (err 5e−4, n=2e6) | E|S_F|<∞, atomless G |
| 50 | `cor:d7-BG` | Cor 2 | D7:203 | cond:bg's form derived | inline | OK (λ>0 caveat handled) | — |
| 51 | `thm:d7-A3` | Thm 2 | D7:223 | A3 fails iff F1∧F2∧F3 | inline; d7-rec (48-cell iff check) | OK | θ<1, ρΔ_eng>0 cited & used |
| 52 | `prop:d7-afs` | Prop 16 | D7:258 | Measured-premium reversal, λ_crit>0 | inline; d7-rec (λ_crit=0.07) | OK; denominator positivity leans on A5 beyond its stated form (m6) | A5, fixed cutoffs |
| 53 | `lem:d8-pricing` | Lem 26 | D8:86 | Pricing-layer IFT, ℓ<1 | inline | GAP: proof claims δ/σξ<1/φ(0) gives uniform ℓ̄<1 — contradicts rem:A5margins (M7) | A5 |
| 54 | `lem:d8-cutoff` | Lem 27 | D8:112 | Inversion-free bound B̄ via Neumann | inline | OK | quantified A6 cited & used |
| 55 | `lem:d8-weights` | Lem 28 | D8:139 | Weight decomposition | inline | OK | smoothness of ingredients |
| 56 | `thm:d8-region` | Thm 3 | D8:167 | Strict single peak on certified region | inline; d8-rec | OK; parenthetical definition of E(κ) (frozen-cutoff "type") inconsistent with the path-partial E′ the proof integrates (m8) | A1–A7, quantified A6, (C*), (R1)–(R2) — all cited |
| 57 | `cor:d8-baseline` | Cor 3 | D8:184 | Certified intervals [0.30,0.85]/[0.35,0.825] | d8 JSON | OK — every number matches `d8_ge_dominance_check.json` (L=0.8358, A*=5.56e−3, ball 2.5e−5 vs margin 4.7e−3) | — |
| 58 | `prop:d8-counter` | Prop 17 | D8:192 | Certified troughs at σξ=0.60 ⇒ Hyp 1 false globally | d8 JSON | OK — minimizers {0.275,0.35,0.475}, depth 2.8e−3, ∫|B|=0.021 vs 0.0069 all match JSON | (i)=rem:d5-vacuous, (ii)=certified numerics |

Assumptions: A1 (interiority, line 270), A2 (decreasing cost, 266), A3 (m̃>m0, 284), A4 (interior bids, 300), A5 (unique pricing FP + sensitivity, 354), A5a/A5b (678/690), A6 (contraction, footnote 378 / app), A7 (price separation, 296; shown droppable by lem:dropA7). Summary table at 1888–1905 consistent with inline statements.

---

## 2. Statement–proof matching (category 2 findings)

**2.1 [C1] `cor:cons-vs-fb`(a) proves the wrong direction.** `prop:firstbest-d2` (1657–1659) establishes that Σ_P−Σ_Q inherits monotonicity from "E[v|s] entering with a *negative* sign" in eq:reclass-real — i.e. the jump is **strictly decreasing** in s (T₁ is s-free by disclosed-branch invariance). The corollary's proof (1678–1681) then asserts: jump positive at k_D^eq + single-crossing ⇒ "its zero k_D^FB lies at a strictly **lower** signal." For a decreasing function positive at k_D^eq the zero lies strictly **higher**. Numerical check with the manuscript's own formula at the baseline: jump(k_D^eq=2.261) = 0.0131·(1.44−0.15−1.6306−0.225) + 0.4·φ(2.2228) = **+0.0061 > 0**, zero at s ≈ **3.19 > 2.26**. So k_D^FB > k_D^eq under eq:reclass-real, contradicting (a) and destroying the sandwich in (b). (The conclusion may be rescuable under the *correct* two-lottery jump — see 2.2 — whose s-slope is positive because p̄_Q > p̄₁; but then lem:reclass-jump and prop:firstbest-d2 must be re-derived.) Same text in the D2 record (D2_welfare_planner.tex:670–700), so this is a record-level error, not transcription drift; the record's "[Corollary G-slip]" fix addressed the two roles of G but not this direction error.

**2.2 [C2] §6.3 assumes bids occur only on the disclosed branch — contradicting the model.** Line 1451–1452: "a takeover arrives only after a public-voice disclosure"; lem:reclass-jump's proof (1517–1518): "Under Quiet Voice D=0 no raider is summoned, so Σ_Q = v+Δ̃−C(k_D)." But the bid technology (eq:bid-prob, line 319) gives positive bid probability at every reached (X,D), and `prices.csv` confirms p(X,0) ∈ {0.81, 0.55, 0.33, 0.17} at the baseline — *larger* than the disclosed p(X,1)=0.013. The whole Δmin analysis of §4–5 is driven by D=0 bids (the integrand h(π)=πp(π) lives on D=0 cells). Σ_Q omits the D=0 bid lottery, so eq:reclass-real and everything downstream (prop:disclosure-wedge's term (i), prop:firstbest-d2, cor:cons-vs-fb) is derived from an object inconsistent with the model. Note the *numerical* probe (1611–1618) maximizes the true eq:welfare-net-d2 (D=0 bids included) and still finds k_D* < k_D^eq, so the conclusion of Prop 8 has numerical support even though the analytic reclassification term is mis-derived.

**2.3 [C3] `prop:d5-a2`'s premise Λ(s)>0 is false in the model.** The proposition (2708) asserts Λ(s) — the *gross* (pre-cost) Quiet-over-Hold value slope — "is strictly positive on the relevant range under (A1), (A3)–(A7)." But Hold and Quiet share (q,h,D)=(0,1,0), so by the manuscript's own eq:UH-UQ (1947–1950) the gross gap U_Q−U_H+C(s) = δE_z[p(X,0)(m̃−m0)+(1−p(X,0))Δ̃] is **constant in s** at fixed prices: Λ ≡ 0. Consequences: (i) the "persuasion regime" C′(s)<Λ(s) collapses to C′(s)<0, i.e. exactly A2, so the appendix's headline ("ordering survives **any** cost profile … includes a flat cost") is vacuous as stated; (ii) the flat-cost paragraph (2720–2721: "the threshold condition reduces to Λ(s)>0, which holds under the Standing Assumptions") is false, and with C′=Λ=0 the gap G_HQ is constant in s — no single crossing — which is precisely the **two-cutoff collapse** the body's own footnote 271 describes ("when χ=0 … the equilibrium collapses to the two-cutoff case"). Body line 268 and D5 summary item 2 ("only the level of k₀ shifts") contradict footnote 271. The body's advertised A2-dispensability rests on this.

**2.4 [C4] `lem:BP-BQ` footnote contradicts itself and the pipeline.** The condition is p(X,1) ≤ ½ ⟺ 𝒯 ≥ 0 ⟺ eq:BPBQ-suff. The footnote (641) claims the condition "holds at the baseline, where the disclosed takeover probability is p★=0.8473 (𝒯=−1.025…)". p★=0.8473 > ½ and 𝒯<0 mean the condition **fails** by the lemma's own equivalence — the sentence refutes itself. Moreover the quoted p★ contradicts the current pipeline: `prices.csv` gives the disclosed-branch p(X,1)=**0.0131** (so the condition in fact holds, comfortably). The same stale pair (p★≈0.847, feedback bound 0.9474, δp★≈0.805) drives rem:A5margins (695–698), whose headline concession "the baseline does not satisfy [A5a's sufficient rule]: 0.805+0.947>1" is computed from numbers that do not correspond to the current calibration (they back out to S̄−K−P≈0.69, e.g. an older S̄≈0.84 with P=0, vs the current S̄=1.44). With p★=0.013 the direct term is δp★≈0.012, and the stated sum is <1. These numbers also contradict the manuscript's own deterrence claim at 1016 (p(X,1)<p(X,0) — which the CSV supports). Source: spliced verbatim from D6_equilibrium_foundations.tex (lines 66–67, 293, 405–409), which carries the same stale values; no JSON/CSV artifact supports 0.847.

**2.5 [M1] eq:fb-engage deducts the premium m̃ from social surplus.** prop:firstbest-d2's engagement rule (1640–1641) contains p₁*(S̄+E[ξ|bid]−K−**m̃**−E[v|s]−Δ̃). By lem:transfer-netting the premium is a pure transfer and appears in W only through the bid-selection threshold T₁ (already embodied in p₁* and E[ξ|bid]); a −m̃ in the surplus bracket double-counts the transfer (it matches a bidder-only surplus reading, inconsistent with eq:welfare-net-d2). Identical in the D2 record (line 647), so again a record-level slip.

**2.6 [M2] cor:cons-vs-fb(b) quantifier slip.** Hypothesis (ii) is stated at k_D^eq (G(k_D^eq)≥0, 1669), but the proof of (b) evaluates "dW/dk_D|_{k_D^FB} = G(k_D^FB) ≥ 0" (1694) — a different point. G ≥ 0 at one point does not give G ≥ 0 at the other; the sandwich needs G(k_D^FB)≥0 (or G≥0 on an interval) as a hypothesis.

**2.7 [M3] `prop:ge-disclosure` has no proof.** Prop 10 (1790–1800) is a formal proposition containing sign assertions ("The transparency effect … is nonnegative"; "this channel is nonpositive whenever …") with no proof environment, no appendix derivation (app:extensions-derivations covers only the ND/NR posterior formulas), and no D-record. The chain-rule display is definitional, but the embedded sign claims are substantive and unproven.

**2.8 [M4] `prop:disclosure-attenuation` claims more than its sketch shows.** The conclusion "|∂Δact/∂κ| is decreasing in ω_P" is a cross-strategy comparative static, but the premise fixes the cutoffs (which pin ω_P). Varying ω_P requires moving k_D, which also changes ω_Q, hence π(X,0) and p(X,0) — the sketch (996) addresses only the weight P(D=0)=1−ω_P and ignores the induced change in the conditional term E[π(X,0)p(X,0)|D=0]. As stated, the monotonicity does not follow.

**2.9 [M5] eq:slopes vs eq:U-affine: two incompatible slope conventions.** Main text (581–585) declares B(E)=0, B(H)=B(Q)=1, B(P)=1+η with η>0 "from the trading term … slope of +1", citing eq:U-affine. But eq:U-affine's own coefficient (1936) is B_{q,a}=δh·E_z[1−p(X,D)], giving B(H)=B(Q)=δE_z[1−p(X,0)]≠1 and B(P)−B(Q)=δ[2(1−p̄₁)−(1−p̄_Q)], whose sign is **not** unconditional: it requires p̄_Q > 2p̄₁−1 (equivalently lem:BP-BQ's p̄₁≤½, or the deterrence ordering). The −qP trading term contributes zero slope in v̂; the "+1" is the extra share's standalone slope, which is actually δ(1−p̄₁)<1. At the current baseline the ordering holds easily (p̄₁=0.013 ⇒ gap ≈ 1.25>0), but the *stated* justification is wrong, and prop:existence/lem:selfmap inherit the ordering without citing any condition for it. The appendix proof of prop:cutoffs (1952) papers over the same step with an equilibrium-dependent assertion.

**2.10 [M6] `lem:d5-twopoint` mis-assigns the two-point masses.** It writes Φ^D0 = ω_H·g(0) + ω_Q·g(π̄). Per lem:d5-endpoints (2807, same appendix), Table tab:d1-D0cells, and D1's lem:endpoints, the π=0 atom carries the **Exit** mass ω_E and the π̄ atom carries the **pooled** q=0 mass ω_H+ω_Q. Correct: Φ^D0 = ω_E·g(0) + (ω_H+ω_Q)·g(π̄). As written the Exit cells' baseline-premium contribution (m₀p at π=0, nonzero since g(0)=m₀p(0)>0) is dropped and Hold mass is misplaced. Downstream use in prop:d5-peak survives (only "fixed function of the cutoffs" is needed), but the lemma as stated is false.

**2.11 [M7] `lem:d8-pricing` proof contradicts rem:A5margins.** D8:105 claims "the body's sufficient condition δ/σξ<1/φ(0) gives a uniform ℓ̄<1." ℓ = δ[p + p_P(P+m̄−V̂)] contains the direct term δp, which δ/σξ<1/φ(0) does not bound; rem:A5margins (697) makes exactly this point ("the displayed feedback number does not by itself establish |Ψ′|<1"). The signed ℓ may still be <1 along the path (p_P<0 helps when P+m̄>V̂), but the stated justification is the inequality the manuscript elsewhere concedes is insufficient.

**2.12 Honest-labelling (positive findings).** The conditional architecture is generally exemplary: Hypothesis 1, (C*), (C**), (GE-dom), (W*), (i)/(ii), Condition BG, and the Numerical Regularities are all carried *inside* statements; D8 both certifies the hump on a region and certifies the global failure of Hypothesis 1 — statements and artifacts agree exactly.

---

## 3. Assumption audit (category 3)

| Assumption | Stated | Used in proofs of | Issues |
|---|---|---|---|
| A1 interiority | 270 (+footnote 271) | prop:cutoffs Step 1; lem:bounded/selfmap/monotone; prop:existence; prop:disclosure-wedge corners | footnote 271 (χ=0 ⇒ two-cutoff collapse) contradicts D5/§268 flat-cost claims (C3) |
| A2 decreasing cost | 262–266 | lem:dominance(i); prop:cutoffs Step 1; lem:bounded (H/Q crossing); lem:monotone tie-break | D5 quantifies dispensability incorrectly (C3) |
| A3 m̃>m0 | 284 | lem:dominance(ii); bid-monotonicity; within-regime CS (2163); derived in thm:bg-A3/thm:d7-A3 | consistent |
| A4 interior bids | 300 | lem:bounded; prop:existence; jump positivity reading (1604) | cited where used ✓ |
| A5 unique pricing FP | 354 | prop:cutoffs Steps 2–3; disclosed invariance; prop:price-decomp; prop:d7-afs; lem:d8-pricing | **not cited** by lem:selfmap/prop:existence though needed for the price map to be a function (M5); footnote 355's "sufficient condition" covers only the sensitivity clause (m4); line 1010 repeats it as "the sufficient condition for A5" |
| A5a/A5b | 678/690 | IFT layers (D8), rem:A5margins | maintained honestly; margin numbers stale (C4) |
| A6 contraction | footnote 378; quantified D8:114 | prop:cutoffs Step 3 (Banach); lem:d1-ift; hyp:d1-cutoffshift; lem:d8-cutoff; planner NR | uniqueness consistently downgraded to numerical regularity ✓ |
| A7 separation | 296 | conditioning shorthand | shown droppable (lem:dropA7) yet kept in Standing Assumptions footnote — consistent but redundant; lem:dropA7's own premise is A7-like (m9) |
| prop:d5-a2 cites "(A1),(A3)–(A7)" | — | for Λ>0 and strict monotonicity of G_EH,G_QP "by (A4),(A5)" | neither delivers those properties (C3, M5) |

---

## 4. Notation consistency (category 4) — 15 load-bearing symbols + collisions

| Symbol | Status |
|---|---|
| κ, k1,k0,kD, X, σξ, m0,m1,m̃,m^R,m̄, Δmin/Δact/Δ/Δ̃ | Consistent throughout; the Δ-family is explicitly disambiguated (721, 2473) ✓ |
| **κ\*** | **Collision (M8):** eq:two-programs (1272) defines κ\*=argmax W vs κ†=argmax Δmin; but rem:numreg (702: "the hump peak κ★=0.59") and nr:bg-statedep (2660: "interior maximizer κ\*≈0.59") use κ\* for the Δmin maximizer = κ†. A reader of §6.2 will misread both. |
| q | Body: blockholder trade q∈{−1,0,+1} (152). Body §3.4 (288–290) *also* uses q = fringe-raid probability in λ=1−q(1−γ)ψ, three paragraphs later, undefined-collision in the same section; D7's notation footnote (D7:73) flags α, τ_c, φ but not q. |
| ψ | D7 pivotality ψ vs price-map Ψ_fp (A5a) — different glyphs, acceptable. |
| λ | Appropriability λ (body §3.4, D4, D7) vs inverse-Mills λ_L,λ_U (432, subscripted) vs λ_sd — workable; plus Λ collision: D4's Λ (threat-point fraction, 2535–2537) vs D5's Λ(s) (Quiet-over-Hold slope, 2699) in adjacent appendices. |
| γ | D7 portability (flagged as local) vs lem:truncnorm's γ (standardized threshold, 2023) — appendix-local, low risk. |
| h | Share count h=1+q vs integrand h(π)=πp(π) — **flagged by the authors themselves** (footnote 1177) ✓ |
| T | Heavy overload: bid threshold T(X,D) (2120), T₁ (1511), D1's T(π) (859, threshold); D5's T(π)=m̄(π)a(π) (2789, *different function, same name*, in a sibling appendix cross-referenced by D8); pooled masses T₋,T₀ (2249); best-response map 𝒯 (\Tmap); t(κ) (D8). The D1-vs-D5 T(π) clash is the risky one. |
| Φ | Normal CDF vs equilibrium functional Φ(k,κ)=Δmin (2376, D8:82) vs Φ^D0 (2761) — overload; f doubles as signal density (D8:82). |
| W | Total surplus W(κ) vs D5's net-slope W(s)=Λ−C′ (2700) vs D8 weights W_i — W(s) is a genuine clash with the welfare section. |
| p | Bid probability p(P,D)/p(X,D) vs noise probabilities p₀,p₁ — indexed, acceptable. |
| g | lem:d1-variance's g(x) (scaled second moment) vs D5's g(π)=m̄p vs nr:bg-statedep's g(κ)=κ−½ — three meanings. |
| α | Standardized cutoffs α_i vs D7 bloc stake α vs completion prob α(P,D) (344) — D7 flags its α ✓ |
| δ | Discount δ vs D7's realized improvement δ_e — subscripted ✓ |

---

## 5. Numbers consistency (category 5)

**Verified against artifacts/pipeline (all match):**
- κ†≈0.59, Δmin(κ†)≈0.078 (1421): welfare.csv argmax W_min=0.0776 at κ=0.58 (grid 0.03); D1_GE_check_out.json grid_argmax 0.6, 0.077558 at 0.59; D2 record ✓. κ\*≈κ† (1422–1424, 1710): welfare.csv argmax W_tot = argmax W_min = 0.58 ✓.
- Endpoints Δmin(0.05)≈Δmin(0.95)≈0.067 (1428): D2 verify 0.066968/0.067814 ✓. Amplitude ≈14% (2660, 2829): 13.65–13.9% in records ✓.
- Cutoff path "0.657→0.822→0.743 at κ=0.2,0.5,0.8" (895): solver re-run gives 0.6574/0.8217/0.7429 — exact ✓.
- dk/dκ ≈ (−0.0599,−0.0599,+0.0982) (2411): D1_GE_check_out.json −0.05993/−0.05993/+0.09824 ✓.
- max πTT′=0.42, slack 1.58 (2352): reproduced from model price P(π̄)=1.3871 ⇒ max=0.4243, slack 1.5757 ✓.
- Endpoint micro-gaps 0.07020822/0.07020753, 6.86e−7, ≈3.6e−5, π̄≈0.96 (829–836, 768): D1_prop6_endpoint_variance.tex (0.959, 3.6–3.8e−5) ✓.
- D8 numbers (957–960, cor:d8-baseline, prop:d8-counter): L=0.8358≤0.836; A*=5.56e−3; ball 2.55e−5 vs margin 4.75e−3; [0.30,0.85] exact-IFT; [0.35,0.825] inversion-free; troughs (0.60,{1.44,1.54,1.64}) at κ_min {0.275,0.35,0.475}, depth 2.80e−3; ∫|B|=0.0207 vs A*=0.0069 — all match d8_ge_dominance_check.json ✓.
- 16/20 chord, 8/20 pointwise, 4/20 troughs all at σξ=0.60 (2829): phase0_robustness.md "chord agree 16 / pointwise agree 8 / 4 troughs at σξ=0.6" ✓.
- nr:bg-statedep (2660): λ_sd grid {±0.2,±0.4}, peak 0.0776, amp 0.0107, swing 0.0722→0.0829, κ\* 0.59→0.60 — all in D4_bargaining_microfound.tex:722–746 (d4_bargaining_check.py Part D) ✓. (Note: `d4_bargaining_driver_out.json` is a *different* exercise with η∈{±0.3,±2,±5}.)
- Partial probe (0.20,2.51,1.71),(0.50,2.26,2.16),(0.80,2.40,1.80) (1617–1618): D2_welfare_planner.tex:622–623, tagged VERIFIED D2_welfare_verify3.py ✓.
- m̃=0.28, wedge 0.20, ρ=0.9 reconciliations R1–R3 (2619): arithmetic checks ✓; λ=0.8614 microfounded baseline & wedge 0.20: wedge_primitives.csv + d7 JSON ✓; λ_crit=0.07: d7 JSON ✓.
- δ/σξ=2.375<1/φ(0)≈2.507 (1010) ✓; a(π)-negative window [−1.09,−0.73] and S̄≲0.71 non-vacuity bound (2757, 2800) ✓ by hand.
- π(0,0)>π(−1,0) (1106): prices.csv 0.737>0.412 ✓; p(X,1)<p(X,0) ∀X (1016): 0.0131 < {0.81,0.55,0.33,0.17} ✓; π̄=1 at interior κ, ω_H≈0 (767): probe ✓; multistart residuals ~4e−10 (702): phase0 4.13e−10 ✓; tab:example cutoffs 0.82/2.26 (2860): baseline_cutoffs.csv ✓; ge_decomposition.csv satisfies chanA+chanB=total ✓.

**Mismatches:**
- **p★=0.8473 / 𝒯=−1.025 / δp★≈0.805 / feedback 0.9474** (641, 697): contradict prices.csv (disclosed p=0.0131) and the manuscript's own deterrence claim; only source is D6's tex (no JSON/CSV). See C4.
- **E[π|D=0] "0.85→0.58→0.85" (897):** recomputed from the model: 0.79 (κ=0.05) / 0.68 (0.2) → 0.58 (0.5) → 0.63 (0.8) / 0.76 (0.95). Midpoint matches; the 0.85 endpoints do not reproduce under E[π|D=0]=ω_Q/(1−ω_P) at any tested κ. (M9)
- **Stale artifact:** `D2_welfare_numerics.md` (attempt 4) headlines "κ\*(0.29) < κ†(0.59), SIGN NEGATIVE," contradicting the final record (D2_welfare_planner.tex), the manuscript, and the current welfare.csv (both argmaxes ≈0.58). Its W_bid (~0.0055) reflects a superseded welfare definition (current: ~0.14). Risk of citing the wrong artifact. (M10)
- **Minor gate tension:** D5 says "4/20 cells trough" (phase0 gate); D8 certifies troughs in only 3 of those 4 ((0.60,1.34) has depth 5.9e−5, below D8's gate). Not contradictory, but the differing trough criteria are unstated. (m7)

---

## 6. Cross-reference integrity (category 6)

- **Hardcoded result number:** D7:256 "the body's Proposition~3" — currently resolves correctly (Prop 3 = prop:price-decomp, which is indeed the pricing decomposition described), but it is a literal number that will silently break if any earlier proposition is added/removed. Replace with `\ref{prop:price-decomp}`.
- 1456: "By Proposition~\ref{prop:cutoffs} the difference U_P−U_Q is strictly increasing in s" — prop:cutoffs does not state this; it is asserted in the appendix proof Step 1 / follows from lem:monotone+lem:BP-BQ. Semantic misattribution.
- 1145: "Δmin(0)=Δmin(1)>0 (Lemma~\ref{lem:endpoints})" — the lemma proves equality of *limits*, not strict positivity; ">0" is imported silently (it is true numerically).
- D3_prop8_IFT.tex ("Proposition 8" = old numbering of the hump result) is **not** `\input` — its content was rewritten into the body (lem:endpoints/lem:d1-jensen/prop:nonmonotone/lem:d1-ift); no stale labels from it (`eq:dmin`, `prop:hump`, `rem:decomp`) leak into draft_v2.tex ✓.
- D4 ledger (2666) still lists "Open: the appropriability coefficient λ … is not derived from a complete tender-game equilibrium" — contradicted by the updated scope statement (2470) and by Appendix D7 itself, which derives λ. Stale ledger line.
- All figure labels referenced in audited text (fig:ge-decomposition, fig:nonmonotone, fig:decomposition, fig:cutoffs-kappa, fig:disclosure, fig:noisy-rumor-precision, sensitivity figs, etc.) are defined ✓. Guarded `\newtheorem` duplicates (731, 2459, 2671, D7:60, D8:67) are no-ops, so hypothesis/numreg/condition numbering is single-sequence ✓.

---

## 7. Issue table

| ID | Severity | Location | Description | Suggested fix |
|----|----------|----------|-------------|---------------|
| C1 | CRITICAL | draft_v2.tex:1674–1681 (cor:cons-vs-fb(a)); D2_welfare_planner.tex:686–688 | Zero of the *decreasing* jump Σ_P−Σ_Q claimed to lie at a strictly *lower* signal; under eq:reclass-real at baseline the zero is s≈3.19 > k_D^eq=2.26, so k_D^FB>k_D^eq — corollary (a) false as proved, (b) sandwich collapses | Re-derive with the correct two-lottery jump (see C2), whose s-slope is +(p̄_Q−p₁*)β>0 under deterrence; or restate (a) for the lower-set disclosure region the decreasing jump actually implies |
| C2 | CRITICAL | draft_v2.tex:1451–1452, 1517–1518 (lem:reclass-jump), affects 1541–1714 | "Takeover arrives only after public-voice disclosure" / "Under Quiet Voice no raider is summoned" contradicts eq:bid-prob and prices.csv (p(X,0)=0.17–0.81>0); Σ_Q omits the D=0 bid lottery on which §4–5's entire Δmin analysis rests | Recompute Σ_Q with the D=0 lottery: Σ_P−Σ_Q=(p₁*−p̄_Q)(S̄−K−E[v|s]−Δ̃)+σξ(φ(T₁)−E_zφ(T_{X,0})); re-sign hypotheses (i); propagate to Props 8–9, Cor 1 |
| C3 | CRITICAL | draft_v2.tex:2707–2712, 2720–2721, 268 vs 271(fn) and 1947–1950 | prop:d5-a2 premise "Λ(s) strictly positive under (A1),(A3)–(A7)" false: by eq:UH-UQ the gross Hold/Quiet gap is s-free at fixed prices (Λ≡0); persuasion regime degenerates to A2; flat-cost claims contradict footnote 271 (χ=0 ⇒ two-cutoff collapse) | Either restate with Λ≡0 (ordering survives iff C′<0, i.e. A2; flat cost ⇒ collapse face, weak ordering only) or introduce a genuine s-dependent gross gap (e.g. proportional improvement Δ̃(s)) and prove Λ>0 from it; align body line 268 and D5 summary with footnote 271 |
| C4 | CRITICAL | draft_v2.tex:641(fn), 695–698; source D6_equilibrium_foundations.tex:66–67,293,405–409 | Footnote claims eq:BPBQ-suff "holds at the baseline" while quoting p★=0.8473, 𝒯=−1.025 — which *violate* the condition p(X,1)≤½ — and contradict prices.csv (disclosed p=0.0131, condition actually holds) and line 1016's deterrence ordering; rem:A5margins' "baseline fails A5a's sufficient rule (0.805+0.947>1)" is computed from the same stale numbers | Recompute the disclosed-branch p★, 𝒯, δp★, and the A5a feedback bound at the current calibration (S̄=1.44); the corrected numbers *strengthen* both claims (condition holds; direct term tiny) |
| M1 | MAJOR | draft_v2.tex:1639–1643 (eq:fb-engage); D2_welfare_planner.tex:647 | First-best engagement rule subtracts the premium m̃ inside the social-surplus bracket; premium is a transfer per lem:transfer-netting (it belongs only in the selection threshold T₁) | Drop −m̃ from the bracket (keep it inside T₁/p₁*) and re-verify the engagement cutoff |
| M2 | MAJOR | draft_v2.tex:1669–1670 vs 1693–1696 | Cor 1(b) hypothesis states G(k_D^eq)≥0 but the proof needs and uses G(k_D^FB)≥0 | State (ii′): G≥0 at k_D^FB (or on [k_D^FB,k_D^eq]) |
| M3 | MAJOR | draft_v2.tex:1790–1800 | prop:ge-disclosure: formal proposition with embedded sign claims (transparency ≥0; deterrence ≤0 under conditions) and no proof anywhere (no appendix, no D-record) | Add a short appendix derivation (the transparency-channel sign needs the disclosed-branch invariance + monotone weight argument), or downgrade to a Remark/Observation |
| M4 | MAJOR | draft_v2.tex:987–996 | prop:disclosure-attenuation's conclusion "|∂Δact/∂κ| decreasing in ω_P" not delivered by the sketch: varying ω_P moves k_D, changing π(X,0), p(X,0); only the (1−ω_P) weight channel is argued | Restate as the weight-channel statement actually proved (disclosed component κ-invariant; inferred component weighted by 1−ω_P, *holding the conditional sensitivity fixed*), or prove the total monotonicity |
| M5 | MAJOR | draft_v2.tex:581–586, 616–623, 635–641, 1952 | eq:slopes (B(H)=B(Q)=1, B(P)=1+η, η>0 unconditional, "trading contributes +1") inconsistent with eq:U-affine's exact B=δhE_z[1−p]; B_P−B_Q=δ[2(1−p̄₁)−(1−p̄_Q)] needs p̄_Q>2p̄₁−1 (delivered by lem:BP-BQ's condition or deterrence); prop:existence/lem:selfmap also omit A5(a) from their hypothesis lists though the price map must be single-valued | State the slope ordering as a hypothesis discharged by lem:BP-BQ's condition (now correctly verified, see C4 fix); add A5(a) to the existence-block hypotheses; fix the "+1 trading" sentence |
| M6 | MAJOR | draft_v2.tex:2760–2765 vs 2806–2812 | lem:d5-twopoint: Φ^D0=ω_H g(0)+ω_Q g(π̄) has wrong masses (drops Exit atom; misplaces Hold); same appendix's lem:d5-endpoints and D1's Table give (ω_E at π=0; ω_H+ω_Q at π̄) | Φ^D0=ω_E g(0)+(ω_H+ω_Q) g(π̄); check the tower-identity sentence still reads correctly |
| M7 | MAJOR | quality_reports/fixes/D8_GE_dominance_MCS.tex:105 (lem:d8-pricing proof) | "the body's sufficient condition δ/σξ<1/φ(0) gives a uniform ℓ̄<1" — false (ℓ contains the direct δp term); contradicts rem:A5margins' explicit concession | Justify ℓ<1 along the path via the signed form (p_P<0 with P+m̄>V̂ at the relevant cells) or cite A5a as maintained |
| M8 | MAJOR | draft_v2.tex:702, 2660 vs 1271–1275 | κ\* used for the Δmin hump peak in rem:numreg and nr:bg-statedep, but §6.2 formally defines κ\*=argmax W and κ†=argmax Δmin (the wedge κ\*−κ† is a headline object) | Rename the two appendix/remark uses to κ† |
| M9 | MAJOR | draft_v2.tex:896–898 | "E[π|D=0] traces 0.85→0.58→0.85" — recomputation gives 0.79/0.68→0.58→0.63/0.76 (κ=0.05/0.2→0.5→0.8/0.95); endpoints unsupported by any artifact | Recompute and quote the actual span (e.g. 0.79→0.58→0.76 on [0.05,0.95]); the qualitative drift claim survives |
| M10 | MAJOR | quality_reports/fixes/D2_welfare_numerics.md; draft_v2.tex:2666 | Stale artifacts contradicting final results: D2_welfare_numerics.md headlines κ\*=0.29<κ†=0.59 (NEGATIVE wedge) vs final record/manuscript/welfare.csv (≈0, both ≈0.58–0.59; W_bid definition changed); D4 ledger line still lists λ-derivation as "Open" though D7 (input two lines later in the compiled doc) derives it | Mark D2_welfare_numerics.md as superseded (or move to an attic); update D4's ledger sentence at 2666 |
| m1 | MINOR | draft_v2.tex:1145 | ">0" attributed to lem:endpoints, which proves only equality of limits | cite the numerical remark for positivity |
| m2 | MINOR | draft_v2.tex:1456 | "By Proposition prop:cutoffs the difference U_P−U_Q is strictly increasing" — property lives in lem:monotone/lem:BP-BQ/appendix Step 1 | repoint the reference |
| m3 | MINOR | draft_v2.tex:923–926 | prop:nonmonotone states single-peakedness "on [0,1]" and Δmin(0)=Δmin(1) though κ∈(0,1) (230) and endpoints are limits (836 says read as limit) | write Δmin(0⁺)=Δmin(1⁻), as prop:d5-peak already does |
| m4 | MINOR | draft_v2.tex:354–355, 1010 | Footnote's "sufficient condition δ/σξ<1/φ(0)" covers only A5's sensitivity clause, not the assumed uniqueness; line 1010's "baseline satisfies the sufficient condition for (A5)" invites confusion with A5a (which rem:A5margins says fails under the conservative rule) | scope the footnote ("sufficient for the sensitivity bound") |
| m5 | MINOR | draft_v2.tex:288–290; 2699 vs 1124; 2789 vs 859; 2376/D8:82 | Symbol collisions: q (trade vs raid probability, same section); W(s) (D5 wedge) vs W(κ) (welfare); T(π) means two different functions in D1 vs D5; Φ(k,κ) functional vs normal CDF; three g's; Λ (D4 fraction vs D5 slope) | rename D7/body raid probability (e.g. q_F), D5's W→𝒲 or ω-free letter, D5's T→ℒ, functional Φ→𝔇 |
| m6 | MINOR | D7_takeover_game_microfound.tex:277–281 | prop:d7-afs IFT denominator positivity attributed to A5, which as stated does not bound the combined term (same A5/A5a gap as M7) | cite A5a / the maintained ℓ<1 |
| m7 | MINOR | draft_v2.tex:2829 vs D8:194 | "4/20 troughs" (phase0 gate) vs 3 certified troughs in D8 ((0.60,1.34) depth 5.9e−5 below D8's gate); criteria differ silently | state the trough gate in one of the two places |
| m8 | MINOR | D8_GE_dominance_MCS.tex:169 | thm:d8-region's parenthetical "E(κ)=Φ(k(κ̄₀),κ)-type fixed-cutoff paths" mismatches the path-partial E′(κ)=∂Φ/∂κ(k(κ),κ) used in eq:d1-decomp and in the proof | define E′ as the path-partial, drop the frozen-cutoff parenthetical |
| m9 | MINOR | draft_v2.tex:661–673 | lem:dropA7's proof premises price injectivity "at any nondegenerate calibration" — an A7-equivalent regularity, so the redundancy claim is calibration-conditional, not unconditional | state injectivity as the hypothesis of the lemma |

---

## 8. What is solid

prop:posteriors, prop:price-decomp, the truncated-normal toolkit, lem:d1-variance/lem:d1-curvature (algebra independently re-derived), the transfer-netting lemma (numerically exact identity), the no-envelope lemmas, the entire D7 tender game (layer-cake step verified; 48-cell iff boundary and MC checks pass), and the D8 region-theorem/counterexample machinery (every quoted number traceable to `d8_ge_dominance_check.json`) are internally consistent and properly conditionalized. The manuscript's epistemic-status discipline (proved vs conditional vs numerically verified) is unusually good; the failures above are concentrated in (i) the §6.3–6.4 disclosure-planner block, (ii) the D5 A2-robustness appendix's Λ premise, and (iii) stale D6-era baseline numbers.
