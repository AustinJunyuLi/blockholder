# Theory referee report — framework_v3

Reviewer: theory referee (JF/RFS standard). Object: `framework_v3.qmd` §2–§3 (l.71–220),
checked line-by-line against `draft_v2.tex`, `quality_reports/fixes/D7_*.tex`,
`quality_reports/fixes/D8_*.tex`, the JSON artifacts, and `numerical_output/data/*.csv`.
All line numbers are repo line numbers. Nothing was edited.

## Summary verdict (≤150 words)

The memo's simplification is a real improvement in exposition but the headline theorem T2 is
**not proved as stated**. Its "one-line cross-partial" is a two-term product rule with only one
term named: `E_{D=0} h(κ)` is *not* τ-free under any economically natural reading of "stricter
disclosure," so the claimed sign needs a second lemma (which, fortunately, goes the same way —
I verify this numerically below). Three further blocks are overclaimed: existence is not
"unconditional" (the best-response map is only single-valued under (A5a), which the paper's own
`rem:A5margins` says the baseline fails); the T2 "general-equilibrium region version" does not
exist anywhere in the repo and the D8 bound does not reach a cross-partial; and the
Celentano–Levine mapping in T5 lives at λ < 0.07 while the calibration sits at λ = 0.861. τ is
currently a relabeling of an equilibrium object, not a primitive. Fixable in weeks, not days.

## Findings table

| id | severity | memo claim (qmd line) | issue | evidence (file:line) | suggested rewrite / fix |
|----|----------|----------------------|-------|----------------------|-------------------------|
| **T-1** | **MAJOR** | l.170–175 "the cross-partial sign is one line given the proved κ-invariance of the disclosed branch" | The τ-derivative of `(1−ω_P)·|∂_κ E_{D=0}h|` has **two** terms. κ-invariance of the disclosed branch bounds neither `∂_τ E_{D=0}h` nor `∂_τ|∂_κ E_{D=0}h|`. The posteriors `π(X,0)` are homogeneous of degree 0 in `(ω_E,ω_H,ω_Q)` (draft_v2.tex:2246–2270, Table `tab:d1-D0cells`), so the second term vanishes **iff** τ rescales those three masses proportionally — which is not what "stricter disclosure" means. | draft_v2.tex:2246–2270; draft_v2.tex:988–998 (`prop:disclosure-attenuation`, proof labelled "Proof sketch") | State the reweighting law for τ explicitly, then prove the extra lemma. See Q2 for the exact statement and the numeric evidence that the extra term reinforces rather than overturns. |
| **T-2** | **MAJOR** | l.136–137 "Existence follows from Brouwer's theorem … proved, unconditional under (A1), (A2), (A4)" | The map `T` is only a **function** (hence Brouwer-eligible) if the *inner price fixed point* is unique on each cell — that is (A5)/(A5a). `app:proof-disclosed-invariance` uses it explicitly. `rem:A5margins` states the baseline **fails** the paper's own sufficient bound (0.805 + 0.947 > 1). Without uniqueness `T` is a correspondence and one needs Kakutani + convex values, which is not established. | draft_v2.tex:696 (`rem:A5margins`); draft_v2.tex:2015 ("By Assumption (A5), this fixed point admits a unique solution"); draft_v2.tex:564 ("Under Assumptions (A1)–(A5)") | "Existence holds under (A1), (A2), (A4) **and (A5a)**, where (A5a) is a maintained assumption, not a derived inequality (the baseline does not satisfy the conservative sufficient bound)." Delete "unconditional". |
| **T-3** | **MAJOR** | l.174–183 "**Theorem T2 (general equilibrium, region version):** reusing the D8 inversion-free bound … the attenuation sign is certified on a checkable region" | Written in the indicative; **no such object exists in the repo**. D8 certifies single-peakedness of `Δ^min` in κ, a *first*-derivative statement. Attenuation is a cross-partial in (κ,τ). The Neumann bound controls `dk/dκ`; it does not bound `dk/dτ` (no ∂_τT column exists — τ is not in the model) and cannot bound `d²k/dκdτ` at all. | D8_GE_dominance_MCS.tex:110–135 (`lem:d8-cutoff`), :168–190 (`thm:d8-region`); grep for "attenuation" returns no D-series file | Label as **to-do**. Aim at the first-derivative form (see Q9), which reuses D8 twice and avoids the cross-partial entirely. |
| **T-4** | **MAJOR** | l.208–212 "M(π)=m̄/P strictly decreasing in π for λ<λ_crit … the object that rationalizes Celentano–Levine's −13.7%" | The JSON gives `lambda_crit_numeric = 0.07`; the paper's own calibration is `lambda = 0.8614`. The reversal therefore does **not** hold at the model's baseline — it holds in a corner 12× below it. D7 itself targets the result at Albuquerque–Fos–Schroth, not Celentano–Levine. | d7_takeover_game_check.json (`afs_measured_premium_reversal`: λ_crit 0.07; `calibration_consistency`: λ 0.8614); D7_takeover_game_microfound.tex:273 ("exactly as in \citet{AlbuquerqueFosSchroth2022}") | "…rationalizes a *negative measured* activism–premium effect **in the low-appropriability region λ<λ_crit≈0.07**, which the baseline calibration (λ≈0.86) does not occupy; the empirical mapping is to AFS's cross-sectional premium ratio, and the Celentano–Levine estimate is a different (selection-corrected treatment) object." |
| **T-5** | **MAJOR** | l.118–130 "disclosure strictness is now an explicit parameter τ … ω_P = ω_P(τ), ω_P'(τ)>0" | In draft_v2 `D = 1{q=+1}` and `ω_P = 1−Φ(α_D)` is an **equilibrium mass** determined by the cutoff `k_D`. As written, τ is a relabeling: either it moves `k_D` (contradicting "at fixed cutoffs" in T2), or it is not in the model at all. The memo never gives τ a domain, a payoff role, or a mapping. | draft_v2.tex:391–410 (`prop:cutoffs`), :425–433 (ω definitions); memo l.157 "At fixed cutoffs" vs l.161 `ω_P(τ)` | Add the disclosure technology explicitly (see Q3 for the cleanest option: τ = probability a Quiet engagement is publicly disclosed). |
| **T-6** | MINOR | l.100–107 "The bidder observes (P,D)… Π_B = S̄ − P + ξ − **m̄(X,D)** − K" | Inconsistent objects in one display. The draft's justification (`lem:dropA7`) asserts the map `(X,D)↦P` is **injective**; the paper's own Appendix B **disproves** injectivity on the disclosed branch (`P*(x,1)` is the *same* for all x∈{0,1,2}), and that branch has mass ω_P, not measure zero. | draft_v2.tex:662–674 (`lem:dropA7`); draft_v2.tex:2004–2016 (`app:proof-disclosed-invariance`) | Write `m̄(P,D) ≡ E[m^R | P,D]` in the entry rule and prove the sufficient-statistic claim on the *payoff-relevant quotient*, not by injectivity. See Q1. |
| **T-7** | MINOR | l.126–127 "the window length maps to inferred-branch noise through the Back et al. (2018) isomorphism T ↔ σ²T" | The citation is accurate, but it points the **opposite way** from the memo's use: Back et al. say a shorter window is isomorphic to *less noise trading*. In the memo's model that is a reduction in **κ**, not an increase in τ. So the 2024 rule change moves both arguments of `∂²Δ/∂κ∂τ` and the policy experiment does not identify the τ channel. | tmp_extract/Back-ACTIVISMSTRATEGICTRADING-2018.txt:985–988 ("reducing the trading horizon T is isomorphic to reducing noise trading volatility"); memo l.337 (already commits to deleting an "unsupported window-isomorphism sentence") | Either (a) restrict τ to the *threshold* margin (5% vs 3%) and let the window map into κ, stating the confound; or (b) keep both and prove the sign under a stated joint movement `(dκ,dτ)`. Do not present it as a clean τ-experiment. |
| **T-8** | MINOR | l.185–203 "T4 — the liquidity hump, **honestly stated**"; item 2 presents the chord condition as selecting hump vs trough | The draft is **more** honest than the memo here. `rem:d5-vacuous` proves the curvature condition **cannot fail** anywhere on the calibration family, so it "cannot distinguish a hump from a trough there"; hump/trough orientation is produced *entirely* by the GE channel. The memo's T4 omits this. | draft_v2.tex:2799–2806 (`rem:d5-vacuous`); draft_v2.tex:2829 ("neither necessary nor sufficient for the peak"; chord matches orientation in 16/20 cells) | Add one sentence: "(C\*) holds identically on the paper's calibration family, so it selects nothing there; the hump/trough orientation is a pure GE object, and the chord second difference is retained only as a 16/20 diagnostic." |
| **T-9** | MINOR | l.88 "Hold folds into the trading decision; it collapses at baseline anyway" | Hold's collapse is a **baseline numerical fact plus a parameter-contingent remark**, not a theorem. `prop:cutoffs` says the Hold region "*may* collapse" when χ=0; `rem:tie` explains the mechanism but proves nothing. Removing Hold by fiat also silently sets `π̄ = ω_Q/(ω_H+ω_Q) = 1`. | draft_v2.tex:410 ("the Hold region may collapse"); draft_v2.tex:654 (`rem:tie`); draft_v2.tex:1010 ("Under this parameterization, the Hold region collapses") | State the assumption that does the work: `A(Q) − A(H) ≥ C(s)` for all `s ≥ k_1` (engagement net benefit dominates the cost on the whole non-exit region), which makes Hold strictly dominated. Then note π̄ ≡ 1. See Q4. |
| **T-10** | MINOR | l.113–117 "with free-rider floor φ, entry probability q, and dilution ψ" | Labels are wrong and one symbol is overloaded. In D7: φ = **dilution** (charter/freeze-out), ψ = **pivotality factor**, q = probability of a **fringe raid** (`q = H(φ)`), γ = portability. Meanwhile `q` is already the blockholder's order at l.83. | D7_takeover_game_microfound.tex:68–70, :246–250 ("Dilution φ is two-edged"; "ψ a pivotality factor") | "…with fringe-raid probability `r`, portability γ, dilution φ, and pivotality factor ψ, `λ = 1 − r(1−γ)ψ`." Rename to free the symbol `q`. |
| **T-11** | MINOR | l.201 "the interior peak κ† ≈ 0.59" | The exported equilibrium data put the argmax at **0.58** (`baseline_series` 0.5824 on a 35-point grid; `ge_decomposition` 0.575; `welfare` 0.58). 0.59 is the draft's solver-check κ, and D8's channel-(A) peak is 0.60 (a different object). | numerical_output/data/baseline_series.csv (argmax κ = 0.5824); d8_ge_dominance_check.json (`channelA_peak_kappa` 0.60); draft_v2.tex:701 (`rem:numreg`, "κ\*=0.59") | Write "κ† ≈ 0.58 (full-equilibrium argmax); the fixed-cutoff channel-(A) peak is κ ≈ 0.60." |
| **T-12** | MINOR | l.93–96 "δ a normalization (unit share mass, δ = 1 in the baseline)" | §5 of the draft uses **δ = 0.95** for the (A5) sufficiency check; `lem:transfer-netting` uses δ = 1. The two are not reconciled anywhere, and δ enters the inner-fixed-point contraction directly. | draft_v2.tex:1009 ("δ/σ_ξ = 0.95/0.40 = 2.375"); draft_v2.tex:1183–1185 ("δ=1") | Pick one and say which; if δ=1, redo the (A5a) margin arithmetic. |
| **T-13** | NOTE | l.202 "the hump lives where bidder entry is premium-sensitive" | **Consistent** with D8, contrary to a natural first reading. `rem:d8-boundary` says GE feedback dominates where entry is premia-*in*sensitive (high σ_ξ) — the same statement contrapositively. No change needed. | D8_GE_dominance_MCS.tex:~205 (`rem:d8-boundary`: "the liquidity hump … should be strongest where takeover entry is most sensitive to expected resistance") | — |
| **T-14** | NOTE | l.338 "Levit–Malenko–Maug 2024 prove non-Kyle technologies are top-3-acceptable" | LMM prove nothing of the kind — this is a publication-norm claim, not a theorem. Their technology is *Walrasian market clearing* over a continuum of shareholders with a bounded trade size x, no noise trader and no order-flow inference at all. The example is valid; the verb is not. | research/txt/levit_malenko_maug_jf2024.txt:440–450 ("In equilibrium, the market must clear…"), :1421, :1436 ("The market clears if and only if D(p) = …") | "LMM (JF 2024) publish a top-3 trading model with no Kyle market maker at all (Walrasian clearing with a bounded trade size); a discrete-noise inference technology is at least as standard." |
| **T-15** | NOTE | l.215–219 no-manipulation remark | The EGJ attribution is **correct** (Case 2, sufficient condition `R_H − R_L > 4x/3`). But in this model the remark is close to vacuous: Exit sells the *entire* unit stake (payoff independent of Y, `lem:dominance`(i)), and Public Voice buys and discloses. There is no action that shorts the firm while retaining exposure to a corrective decision. | research/lit_feedback-takeover-theory.md:73 (EGJ Case 2, `R_H − R_L > 4x/3`); draft_v2.tex:167–169 (`lem:dominance` proof (i)) | Keep it, but state the reason it is satisfied trivially: the menu contains no "sell while retaining a stake" action, so the Goldstein–Guembel/EGJ manipulation profile is not feasible. One sentence, not a lemma. |
| **T-16** | NOTE | l.20 "provable headline theorem"; l.155 "T2 — Disclosure attenuation (the headline theorem)" | The draft's own version is labelled **"(Partial Equilibrium)"** and its argument is a **"Proof sketch"** closing with □. The memo upgrades "sketch" to "theorem" and "proved" without adding an argument. | draft_v2.tex:988–998 | Say "T2 upgrades the existing PE proof *sketch* to a theorem" and give the missing steps. |
| **T-17** | NOTE | §2–§3 throughout | Undefined symbols (full list in Q11). The worst offenders: `Δ̃` (l.112), `m^R(a)` (l.112), `m̃` (l.161, never linked to the `m_1` of l.113), `h` (l.162), `Δ^min` (l.187 — never defined in the memo), and the engagement cost `C(s)`, which is never mentioned yet is what separates Quiet from Exit. | memo l.112, 113, 161–162, 187 | Add a five-line notation block before §2.1. |

## Detailed notes per question

### Q1. Bidder information set — **inconsistent as written; fixable**

The memo (l.100–107) says the bidder observes `(P, D)` and then writes the threshold in terms of
`m̄(X, D)`. The draft handles this with `lem:dropA7` (draft_v2.tex:662–674), whose proof asserts:
the map `(X,D) ↦ P` is "injective on the realized support at any nondegenerate calibration". That
is **asserted with a parenthetical, not derived** — and it is *false on the disclosed branch*, by
the paper's own Appendix B: `app:proof-disclosed-invariance` (draft_v2.tex:2004–2016) proves
`P*(x,1)` is **identical** for all `x ∈ {0,1,2}`. Three cells, one price. The lemma's escape hatch
("on the measure-zero set where two cells share a price…") does not apply: the disclosed branch
carries mass `ω_P`, roughly 20% at the baseline.

The claim the bidder actually needs is weaker and is true: `P` is a **sufficient statistic** for
the bidder's problem because the only payoff-relevant functionals of `(X,D)` are `V̂(X,D)` and
`m̄(X,D)`, and on the disclosed branch both are constant across `x` (so the pooling is harmless),
while on `D=0` the four cells carry four distinct posteriors `{0, π(-1,0), π(0,0), π̄}`
(draft_v2.tex:2253–2266) and hence generically distinct prices.

**Honest statement for the memo.** Replace l.103/l.107 with

> The bidder observes `(P, D)` and enters iff `Π_B = S̄ − P + ξ − m̄(P,D) − K ≥ 0`, where
> `m̄(P,D) ≡ E[m^R | P, D]`. Because the price and the disclosure flag are jointly a sufficient
> statistic for the pair `(V̂, m̄)` — the only cell objects entering the bidder's payoff — this
> coincides with conditioning on `(X, D)`; in particular the three disclosed cells share one price
> *and* one posterior, so the pooling is payoff-irrelevant.

That is a two-line proof and it removes a false injectivity claim from the paper.

### Q2. **THE HEADLINE THEOREM T2 — the single most important item**

**(a) Is the decomposition correct?** Yes. The memo's display (l.160–163) is
`prop:disclosure-attenuation`'s display (draft_v2.tex:990–994) with `P(D=0) = 1 − ω_P` substituted
and `E[π(X,0)p(X,0) | D=0]` rewritten as `E_{D=0} h(κ)` using `h(π) = π p(π)` (draft_v2.tex:775,
`eq:d1-hdef`). No error.

**(b) Is `p̄_1` truly κ-invariant?** Yes, and this part is genuinely proved.
`app:proof-disclosed-invariance` (draft_v2.tex:2004–2016) shows `D=1 ⟹ X = 1+z` with `z` independent
of `(v,s,ξ)`, so conditioning on `X` reveals only the noise draw; `π(x,1)=1` and
`E[v|X=x,D=1]=μ_P` for all `x`, hence one price and one `p̄_1` on the whole branch. (It does invoke
(A5) for uniqueness of the inner fixed point — see T-2.)

**(c) Does `E_{D=0} h(κ)` depend on τ? — YES.** This is where T2 breaks.

From Table `tab:d1-D0cells` (draft_v2.tex:2253–2266), with `A = ω_E`, `B = ω_H + ω_Q`, `Q = ω_Q`,
`p_0 = 1−κ`, `p_1 = κ/2`, the four `D=0` posteriors are `0`, `Q p_1/(A p_0 + B p_1)`,
`Q p_0/(A p_1 + B p_0)`, and `π̄ = Q/B`. Every one of these is **homogeneous of degree zero** in
`(A, B, Q)`, and so are the `D=0`-conditional cell weights. Therefore:

- **`E_{D=0} h` — and its κ-derivative — is invariant to τ if and only if τ rescales
  `(ω_E, ω_H, ω_Q)` by a common factor.** I confirmed this numerically: rescaling all three masses
  by 1.0 / 0.8 / 0.5 gives `|∂_κ E_{D=0}h|` = 0.015290 in all three cases (exact to six digits).
- Under the **economically natural** reading — a stricter regime forces *quiet activists* to
  disclose, so mass moves `ω_Q → ω_P` — `π̄ = (1−τ)ω_Q / (ω_H + (1−τ)ω_Q)` **falls strictly in τ**,
  and with it the whole `D=0` law. Same numeric experiment, baseline masses
  `(ω_E,ω_H,ω_Q,ω_P) = (0.35, 0.05, 0.40, 0.20)`, `h` evaluated at the draft's premium/entry
  primitives, `κ = 0.5`:

  | τ | ω_P(τ) | π̄(τ) | `|∂_κ E_{D=0}h|` |
  |---|--------|-------|------------------|
  | 0.00 | 0.200 | 0.889 | 0.015290 |
  | 0.25 | 0.300 | 0.857 | 0.014754 |
  | 0.50 | 0.400 | 0.800 | 0.011786 |
  | 0.75 | 0.500 | 0.667 | 0.005225 |
  | 0.95 | 0.580 | 0.286 | 0.000143 |

  A **100-fold** move in the factor the memo treats as τ-free.

**Verdict: (iii) wrong as stated, but the conclusion is rescuable — and in fact reinforced.**
The correct product rule is

    ∂/∂τ |∂_κ Δ^act| = (m̃−m₀) [ −ω_P'(τ)·|∂_κ E_{D=0}h| + (1−ω_P(τ))·∂_τ|∂_κ E_{D=0}h| ] .

The memo names only the first bracketed term. The claim "the cross-partial sign is one line given
the proved κ-invariance of the disclosed branch" is **false**: κ-invariance of the disclosed branch
delivers the *κ*-derivative formula (l.168–172), which is fine, but says nothing about the second
term.

**Exactly what τ must do for T2 as written to be true.** Precisely one of:

1. **(Knife-edge, unstated in the memo.)** τ reweights `(ω_E, ω_H, ω_Q)` proportionally. Then
   `∂_τ E_{D=0}h ≡ 0` by degree-zero homogeneity and the memo's sentence is literally correct. But
   this means the newly-disclosed types are a *proportional mixture of exiters, holders and quiet
   activists*, which is economically incoherent for a disclosure rule (exiters have nothing to
   disclose) and additionally makes `p̄_1` τ-dependent (harmless for T2, since `p̄_1` is still
   κ-free).
2. **(Natural, requires an extra lemma.)** τ moves quiet activists into the disclosed branch. Then
   the second term is *also negative* — the table above — so attenuation holds **a fortiori**, but
   it needs the lemma `∂|∂_κ E_{D=0}h|/∂π̄ ≥ 0`. This is provable from `lem:d1-jensen`
   (draft_v2.tex:841–898): the entire interior motion of `E_κ[h]` equals the probability-weighted
   gap between `h` and its chord on `[0, π̄]`, and for `h ∈ C²` that gap is `O(π̄²)` and vanishes as
   `π̄ ↓ 0`. Two paragraphs, not one line.
3. **(Dangerous.)** τ moves Exit/Hold mass into the disclosed branch. Then `π̄` **rises**, the second
   term is positive, and the sign is ambiguous. Rule this out explicitly.

**Suggested rewrite of l.170–175:**

> Since the disclosed component is κ-free, the liquidity sensitivity satisfies
> `|∂Δ^act/∂κ| = (m̃−m₀)(1−ω_P(τ))·|∂_κ E_{D=0}h(κ; τ)|` — note the inferred-branch term itself
> depends on τ through the residual quiet mass. Under the disclosure technology of §2.2, in which
> a stricter regime moves quiet engagement into the disclosed branch,
> `π̄(τ) = (1−τ)ω_Q/(ω_H+(1−τ)ω_Q)` is strictly decreasing in τ, and by the chord identity of
> Lemma `lem:d1-jensen` the interior motion of `E_κ[h]` is the probability-weighted chord gap of `h`
> on `[0, π̄]`, which is nondecreasing in `π̄` and vanishes as `π̄ ↓ 0`. **Both** factors therefore
> fall in τ, so `|∂Δ^act/∂κ|` is strictly decreasing in τ pointwise in κ. (Under a τ that instead
> drew proportionally from all three non-disclosed branches, the second factor would be exactly
> τ-invariant by degree-zero homogeneity of the `D=0` posteriors, and only the first term would
> operate.)

**One economics warning a referee will raise even after the fix.** With the natural τ, T2 becomes
close to an accounting identity: τ removes activism from the branch where activism must be
inferred, so of course inference sensitivity falls. Sell it as the *policy* statement it is (a
disclosure rule is a lever on revelatory efficiency), not as a discovered mechanism, and put the
weight on the GE version (Q9), where the cutoff response is the genuinely non-obvious part.

### Q3. τ as a primitive — currently a relabeling; here is the cleanest fix

In draft_v2 `D = 1{q=+1}` (draft_v2.tex:158, `prop:cutoffs`) and `ω_P = 1 − Φ(α_D)`
(draft_v2.tex:429) — an equilibrium mass, not a primitive. So `ω_P(τ)` with `ω_P'(τ) > 0` is either
(i) a statement that τ shifts `k_D`, which contradicts T2's "at fixed cutoffs" and makes ω_P
endogenous, or (ii) empty.

**Cleanest minimal change.** Add one primitive: `τ ∈ [0,1]` = the probability that a *Quiet*
engagement is nonetheless publicly disclosed (interpretation: the shorter window / lower threshold
catches accumulations that the old regime let stay quiet). Formally, `D = 1{q=+1} ∨ 1{a=1, ζ ≤ τ}`
with `ζ ~ U[0,1]` independent of everything.

Consequences, all checkable:

- `ω_P^{disc}(τ) = ω_P + τ ω_Q`, so `ω_P'(τ) = ω_Q > 0` — τ is now a genuine primitive with the
  memo's stated property.
- **`D=0` posteriors.** Masses become `(ω_E, ω_H, (1−τ)ω_Q)`; the chord endpoint becomes
  `π̄(τ) = (1−τ)ω_Q / (ω_H + (1−τ)ω_Q)`, strictly decreasing. Table `tab:d1-D0cells` goes through
  verbatim with `Q ↦ (1−τ)ω_Q`, so `lem:endpoints` and `lem:d1-jensen` survive unchanged.
- **Does κ-invariance of the disclosed branch survive?** Yes, and this is the load-bearing check.
  The disclosed branch now has two sub-blocks: `q=+1` cells (`X = 1+z`) and disclosed-quiet cells
  (`X = z`). In *both*, conditioning on `X` reveals only `z`, which is independent of `(v,s,ξ)`;
  the argument of `app:proof-disclosed-invariance` (draft_v2.tex:2007–2012) applies to each block.
  So `p̄_1(τ)` is a two-cell average that is still κ-free. **T2's first factor is safe.**
- **Cost.** The three-branch prune is partly undone: there are now four *observable* cells
  (disclosed-buy, disclosed-quiet, inferred, exit). If that is unacceptable, the cheaper variant is
  to let τ scale the *disclosure threshold on the stake* so that Public Voice is triggered at a
  smaller purchase — but then τ moves `k_D` and the "fixed cutoffs" framing must be dropped.
- **Feedback.** A quiet activist who is disclosed with probability τ has a different payoff, so τ
  shifts `k_0` and `k_D` in general equilibrium. T2 at fixed cutoffs is therefore a genuinely
  *partial*-equilibrium statement, exactly as `prop:disclosure-attenuation` already labels itself.
  Say so.

### Q4. Three-branch pruning

**Is Hold's collapse a theorem?** No. `prop:cutoffs` says "When engagement costs are constant
(i.e., χ=0), the Hold region **may** collapse" (draft_v2.tex:410); `rem:tie` (draft_v2.tex:654)
gives the mechanism ("if the engagement net benefit is too small the Q region is empty") — note
this is the *opposite* collapse, `k_0 = k_D`, not `k_1 = k_0`. §5 reports collapse as a **baseline
numerical fact**: "Under this parameterization, the Hold region collapses (k_0=k_1)"
(draft_v2.tex:1010). `prop:existence` even relies on the collapse face being *reachable*, not
*forced* (draft_v2.tex:622–624).

**Assumption needed to remove Hold by fiat.** Hold and Quiet have equal payoff slopes
(`B(H)=B(Q)=1`, draft_v2.tex:582) and are separated purely by the intercept gap `A(Q)−A(H)` against
the cost `C(s)` (`lem:monotone`, draft_v2.tex:645). So the clean sufficient condition is

> **(A2′)** `A(Q) − A(H) ≥ C(s)` for every `s ≥ k_1` — equivalently `C(k_1) ≤ A(Q) − A(H)` given
> that `C` is strictly decreasing (A2). Then Hold is weakly dominated by Quiet on the entire
> non-exit region and the menu is `{E, Q, P}`.

This is a *joint* restriction on an equilibrium intercept and a primitive cost, so it is not fully
primitive; a fully primitive version is `C_0 ≤ inf_{k∈Θ}[A(Q;k) − A(H;k)]`, which the bounded-price
argument of `lem:bounded` (draft_v2.tex:589) makes well defined.

**What changes downstream.**

- **`D=0` inference law.** With `ω_H = 0`, `π̄ = ω_Q/ω_Q = 1` **identically**. Table
  `tab:d1-D0cells` collapses to atoms `{0, Q p_1/T_-, Q p_0/T_0, 1}`. This is a *simplification*
  and arguably a gain: the chord `[0, π̄]` becomes the fixed interval `[0,1]`, so (C\*) becomes a
  genuinely primitive condition rather than one that moves with the equilibrium. It also kills the
  draft's awkward "π̄ ≈ 0.96 at the extreme κ where Hold reappears infinitesimally"
  (draft_v2.tex:770).
- **`lem:endpoints`.** Survives intact. Its proof uses only (i) noise symmetry `P(z=+1)=P(z=−1)` and
  (ii) the fact that on `D=0` the supports `{−2,0}` (Exit) and `{−1,+1}` (`q=0`) are disjoint at
  `κ→1` (draft_v2.tex:2818–2824, `lem:d5-endpoints`). Neither uses Hold. Note the proof's last
  sentence — "the two limits coincide because the equilibrium indifference system is identical at
  the two extremes" (draft_v2.tex:815–817) — is asserted, not shown; it is the weakest link in the
  "proved" label and should be tightened or the lemma restated at fixed cutoffs.
- **`lem:d1-jensen` / chord condition.** Survives with `π̄ ≡ 1`; (C\*) becomes
  `h(0) − 2h(1/2) + h(1) < 0`, i.e. `h(1) < 2h(1/2)`, a one-inequality primitive condition. Good.

**Honest wording for l.88:** "The four-branch menu is pruned to three under (A2′), a cost condition
under which Quiet weakly dominates Hold on the whole non-exit region; the baseline calibration of
draft_v2 already sits on this collapse face (k₀=k₁). The prune sets `π̄ ≡ 1`, which makes the chord
condition (C\*) a genuinely primitive inequality rather than an equilibrium-dependent one."

### Q5. The Back et al. isomorphism — **supported as a citation, but it cuts against the memo**

The quotation is real. Back, Collin-Dufresne, Fos, Li and Ljungqvist write that what matters is the
cumulative noise trading over the trading period, so "reducing the trading horizon T is isomorphic
to reducing noise trading volatility" (tmp_extract/Back-ACTIVISMSTRATEGICTRADING-2018.txt:986–988),
in a passage explicitly about the 13D pre-disclosure window debate (:979–983). **Verdict:
supported.**

But the direction is the problem. Back et al. map window length into **noise-trading volume** — in
the memo's model, into **κ**. The memo instead maps it into **τ** (l.126–127). Two consequences:

1. **There is no formal object corresponding to "window length" in the memo's model.** It is a
   one-shot game with a single noise parameter κ. The mapping is a narrative bridge, not a
   reparameterization.
2. **The policy experiment is confounded.** If the 2024 acceleration moves both κ (down, via the
   Back isomorphism) and τ (up, via more/earlier disclosure), then the observed change in
   `dΔ/dκ` is not the cross-partial the theorem is about. `|∂_κ Δ^act|` is a function of κ itself,
   so a simultaneous shift in κ contaminates the comparison of pre- and post-2024 slopes.

**Suggested fix.** Split the two margins explicitly: let τ be the *threshold/scope* margin (5% vs
3%, which types must file) and let the *window* margin enter through κ, citing Back et al. for the
latter. Then the 2024 rule is a joint movement `(dκ < 0, dτ > 0)` and the memo should state which
sign it predicts for the composite, or use the cross-country threshold contrast (5% vs 3%) as the
clean τ experiment. Note the memo already contains, at l.337, a commitment to "delete the
unsupported Johnson–Swem window-isomorphism sentence" — swapping the citation to Back et al. does
not repair the underlying issue, which is that the memo's model has no time dimension.

### Q6. Existence "unconditional" — **not honest**

`prop:existence` (draft_v2.tex:617–624) is indeed stated "Under Assumptions (A1), (A2), (A4)", and
its inputs `lem:bounded` (:589) and `lem:selfmap` (:604) carry the same list. So the memo's citation
is *literally* faithful to the draft. But:

1. The section preamble says "Under Assumptions (A1)–(A5)" (draft_v2.tex:564).
2. `lem:bounded`'s proof needs the intercepts `A(·)` to be well defined, i.e. the pricing function
   and `p` to be *determined* by `k` — the inner price fixed point must exist and be **unique**, or
   `T` is a correspondence and Brouwer does not apply.
3. `app:proof-disclosed-invariance` says so outright: "By Assumption (A5), this fixed point admits a
   unique solution" (draft_v2.tex:2015).
4. `rem:A5margins` (draft_v2.tex:696) is explicit that the baseline **fails** the conservative
   sufficient bound: `δp* ≈ 0.805` plus feedback `0.947` exceeds 1, and "We therefore state
   Assumption (A5a) as a maintained assumption, not a derived inequality."
5. Separately, §5 claims the opposite: "The baseline parameters satisfy the sufficient condition for
   Assumption (A5): δ/σ_ξ = 2.375 < 1/φ(0) ≈ 2.507" (draft_v2.tex:1009). **This contradicts
   `rem:A5margins`.** Flagging as an internal contradiction the memo must resolve before it can say
   anything about (A5) at all (see also T-12 on δ).

**Exact assumption list to state:** (A1) signal monotonicity, (A2) strictly positive strictly
decreasing engagement cost, (A4) [bracket/regularity], **(A5a) inner-price fixed point single-valued
on each cell**, plus (A3) for `m̃ > m₀` wherever `lem:dominance` is invoked to justify the menu
(draft_v2.tex:169). Existence of the inner fixed point is free by Brouwer on the compact price
interval `[0, δȲ]`; only *uniqueness* — hence single-valuedness of `T` — requires (A5a).

**Suggested rewrite of l.136–139:** "Existence follows from Brouwer's theorem on the cutoff polytope
Θ under (A1), (A2), (A4) together with (A5a), the maintained single-valuedness of the inner price
fixed point. (A5a) is an assumption, not a theorem: the conservative sufficient bound of draft_v2 is
violated at the baseline, though the fixed point is located numerically without difficulty at every
κ."

### Q7. T4 items, checked one by one

| item | memo | repo | verdict |
|------|------|------|---------|
| (a) endpoint symmetry | "proved" | `lem:endpoints` draft_v2.tex:796–825; `lem:d5-endpoints` :2812–2826 | **Proved at fixed cutoffs**, using only noise symmetry `P(z=+1)=P(z=−1)` and the disjointness of the `D=0` supports at κ→1. Survives the 3-branch prune (Hold is nowhere used). **Caveat:** the last sentence of the proof, "the equilibrium indifference system is identical at the two extremes" (:815–817), is what upgrades the fixed-cutoff statement to a full-equilibrium one, and it is asserted. The remark that follows concedes the endpoints are "degenerate grid-edge solves (large residuals)" (:830). Either restate at fixed cutoffs, or prove the limiting indifference system claim. |
| (b) chord condition | `C(π̄) = h(0) − 2h(π̄/2) + h(π̄) < 0`, `h = π·p` | `eq:d1-chord` draft_v2.tex:791; `eq:d1-hdef` :775 | **Matches exactly.** The memo's "iff" is slightly stronger than `lem:d1-jensen`, which proves `C<0 ⟹` hump and `C>0 ⟹` trough, leaving `C=0` unhandled. MINOR wording. |
| (c) certified interval / L | `[0.35, 0.825]`, `L ≤ 0.836` | `cor:d8-baseline` D8:...; d8_ge_dominance_check.json: `L_max_on_path = 0.83575`, `loose_sumW_dT_over_1mL.certified_interval = [0.35, 0.825]` | **Both match.** Worth adding: on that loose (inversion-free) bound, R1 holds at only 84% of off-ball grid points on the full `[0.30,0.85]` grid — the `[0.35,0.825]` interval *is* the certified sub-region. The exact-IFT bound certifies `[0.30, 0.85]`. |
| (d) κ† ≈ 0.59 | 0.59 | baseline_series.csv argmax **0.5824**; ge_decomposition.csv **0.575**; welfare.csv **0.58**; d8 JSON channel-(A) peak **0.60** | **Off by one grid step.** 0.59 traces to `rem:numreg` (draft_v2.tex:701) where it is a *solver-check* κ. See T-11. |
| (e) counterexample σ_ξ = 0.60 | yes | `prop:d8-counter` D8:194 — troughs at `(σ_ξ, S̄) = (0.60, 1.44/1.54/1.64)`, minimizers `κ ∈ {0.275, 0.35, 0.475}`, `∫|B| = 0.021` vs channel-(A) amplitude `0.0069` | **Matches.** |
| (f) "the hump lives where bidder entry is premium-sensitive" | — | `rem:d8-boundary`: "GE feedback therefore dominates precisely in the high-σ_ξ corner … the liquidity hump should be strongest where takeover entry is most sensitive to expected resistance (low effective σ_ξ)" | **Consistent** — the two statements are contrapositives, not a contradiction. No change needed (T-13). |
| (g) `rem:d5-vacuous` | not mentioned | draft_v2.tex:2799–2806: the curvature condition "cannot fail" on the calibration family, "and so cannot distinguish a hump from a trough there. **Consequently the hump/trough orientation … is produced entirely by the general-equilibrium cutoff-shift channel**" | **The memo hides this, and it must not.** T4 item 2 presents (C\*) as the hump/trough selector; on the paper's own family it selects nothing. The draft is more honest at :2829 ("neither necessary nor sufficient for the peak"; chord matches orientation 16/20 vs pointwise curvature 8/20). See T-8. |

### Q8. T5

- **`λ = 1 − q(1−γ)ψ`** — matches `prop:d7-lambda` (D7:161–180) exactly, `λ ∈ [0,1]` proved, MC-verified
  to `5.0e-4` against 2M draws (`d7_takeover_game_check.json`, `mc_game_vs_closed_forms`). ✓
- **A3 boundary** — `thm:d7-A3` (D7:223–241): `λ = 0` iff all three of (F1) `q=1`, (F2) `γ=0`,
  (F3) `ψ=1` (non-pivotal bloc, or fringe synergy a.s. exceeds `φ + Δ_eng`), under maintained
  `θ < 1` and `ρΔ_eng > 0`. 48 cells verified. The memo's gloss "iff not (certain raids ∧ γ=0 ∧
  unblockable)" is a fair paraphrase; add "given θ<1 and ρΔ_eng>0". ✓ (but see T-10 on symbol labels)
- **`M(π) = m̄/P` strictly decreasing for `λ < λ_crit` at fixed cutoffs** — matches `prop:d7-afs`
  (D7:259–281). ✓
- **"rationalizes Celentano–Levine's −13.7%" — I would push back hard.** Three separate problems:
  1. **Wrong region.** `λ_crit ≈ 0.07` (JSON); the paper's own calibration is `λ = 0.8614` (JSON,
     `calibration_consistency`). The reversal is a statement about a corner the model does not
     occupy. A referee will ask why the calibration was not moved, or why the two are presented
     together.
  2. **Wrong target.** D7 itself points the result at Albuquerque–Fos–Schroth — "Activism then lowers
     measured bid premia **exactly as in \citet{AlbuquerqueFosSchroth2022}**, through the price
     channel" (D7:273), and the testable predictions at D7:286 are all AFS-facing. The memo
     re-labels it onto Celentano–Levine without redoing the mapping; its own l.337 note ("the −13.7%
     premium finding is Celentano–Levine 2025, not AFS") shows it knows the two are different papers.
  3. **Wrong object.** `M(π) = m̄/P` is a *cross-sectional measured-premium ratio* comparing states
     that differ in the market's posterior, at fixed cutoffs, fixed primitives, fixed everything.
     Celentano–Levine estimate an *equilibrium/selection-corrected treatment effect* of activism on
     realized premia. Equating a comparative static in a posterior with a treatment effect requires
     an argument that the cross-section of `π` is the empirical contrast, and the memo gives none.

  **Suggested rewrite of l.209–212:** "…is the model's account of a *negative measured* activism–
  premium relation: it operates through the denominator (the price already impounds the inferred
  engagement), holds for `λ < λ_crit ≈ 0.07`, and delivers the AFS cross-sectional predictions of
  D7. Whether it also accounts for Celentano–Levine's −13.7% is a separate mapping question, since
  their estimand is a selection-corrected treatment effect and the paper's baseline sits at
  `λ ≈ 0.86`."

### Q9. Is the GE region version of T2 done? — **No. It is a to-do written in the indicative.**

I searched `quality_reports/` for any attenuation derivation: the string appears only in planning
documents (`plans/2026-06-04_track-b-design-section2-theorem-stack.md`,
`plans/2026-06-06_jmp-direction-deep-research.md`), a revision prompt, and a passing mention in D7.
There is **no D-series appendix, no script, and no JSON artifact** for a GE attenuation result. D8
is entirely about single-peakedness of `Δ^min` in κ.

**What a GE proof would need beyond `lem:d8-cutoff`.** The D8 machinery gives
`‖dk/dκ‖ ≤ ‖∂_κT‖/(1−L)` (D8:120–135) — a bound on the *first* derivative in κ only. Attenuation as
the memo states it is `∂²Δ^act/∂κ∂τ`, which in GE expands to terms in `dk/dτ`, `dk/dκ`, and crucially
`d²k/dκdτ`. The first is a mechanical addition (a second finite-difference column `∂_τT` and the
same Neumann bound, **once τ is in the model** — which today it is not, Q3). The third is not
reachable from a contraction modulus: it needs `C²` control of `T` and a bound on `D²T`, which
nothing in the repo supplies.

**The statement to aim for instead — avoid the cross-partial entirely.** Compare two *first*
derivatives at two τ levels:

> **Theorem (GE attenuation on a certified region).** Fix `τ' > τ`. Suppose on
> `[κ_lo, κ_hi]` the partial-equilibrium slope gap satisfies
> `|∂_κΔ^act|_k(κ;τ)| − |∂_κΔ^act|_k(κ;τ')| > B̄(κ;τ) + B̄(κ;τ')`,
> where `B̄` is the inversion-free bound `(Σ_i W_i)·‖∂_κT‖/(1−L)` of `lem:d8-cutoff` evaluated at each
> τ. Then `|dΔ^act/dκ|(κ;τ') < |dΔ^act/dκ|(κ;τ)` for every `κ ∈ [κ_lo, κ_hi]`.

Proof is two lines from the triangle inequality on `dΔ/dκ = E' + B` at each τ. It reuses D8
verbatim, needs no second derivative, and produces exactly the same "certified region" rhetoric the
memo wants.

**Feasibility, honestly.** Adding τ to `numerical/params.py` and `numerical/model.py`, re-solving,
and running the D8 script at two τ values: **a few days**. Proving the extra PE lemma of Q2 (chord
gap nondecreasing in `π̄`): **days**. The literal cross-partial in GE: **unclear, and I would not
attempt it** — the counterexample logic of `prop:d8-counter` (D8:194) already shows the GE channel
can overturn a PE sign in this model, so a global cross-partial claim is likely false anyway.

### Q10. No-manipulation remark

The **attribution is correct.** EGJ 2015 (AER 105(12)) Case 2 — where the corrective action makes
firm value non-monotone in the state — introduces a manipulation motive (the positively informed
speculator sells to induce a value-reducing decision), and the repo's own reading note records the
sufficient condition as `R_H − R_L > 4x/3`
(research/lit_feedback-takeover-theory.md:73). The memo's l.219 matches.

**Is the remark needed?** Barely. In this model the blockholder's menu is `{Exit, Quiet, Public}`,
and `lem:dominance`(i) establishes that Exit sets the end-of-period holding to `h = 1 + q = 0`, so
the exiter "retains no claim on the firm's terminal value" (draft_v2.tex:167). A manipulator needs to
*push the price/decision the wrong way while keeping exposure* to the resulting value change. The
menu contains no such action: exit is a full liquidation, and Public Voice buys. So the EGJ profile
is **infeasible**, not merely unprofitable.

**Verdict: keep it, one sentence, and give the right reason.** Something like: "EGJ's Case-2
manipulation profile — sell to induce a value-destroying decision while retaining exposure — is not
in the feasible set here: Exit liquidates the entire unit stake (Lemma `lem:dominance`), so the
manipulator would hold no claim on the manipulated outcome. No side condition on primitives is
needed." Stating it as "the analog of EGJ's `R_H − R_L > 4x/3`" over-promises a condition the model
does not need. If the memo later adds partial exit (`q = −1/2`), the remark becomes substantive and
the analogy earns its keep.

### Q11. Does it simplify? Is it JF/RFS-acceptable? Notation.

**Does it simplify?** Partly. The 4→3 branch prune is real (one fewer cutoff, `π̄ ≡ 1`, a primitive
(C\*)). But the memo simultaneously *adds* τ, and the honest version of τ (Q3) re-splits the
disclosed branch into two sub-blocks, giving back most of what the prune saved. Net: roughly a wash
on state-space size, a clear gain on interpretability. That is still worth doing — but do not claim
it as "fewer moving parts" (memo l.359) without noting the τ device's cost.

**Is a discrete ternary-noise static model with Brouwer existence + numerical uniqueness acceptable
at JF/RFS?** Discrete order flow: yes, and EGJ 2015 is exactly the precedent
(research/lit_feedback-takeover-theory.md:78). Brouwer + numerical uniqueness: acceptable **only if
the headline comparative static is proved**, which the memo itself asserts (l.49) — and which T2
currently is not (T-1) and T4's GE version is not (T-8, and `prop:d8-counter` shows it is false
globally). The repo's own lit note warns that the EGJ precedent is *stronger* than what the draft
invokes it for: "EGJ prove uniqueness analytically within regions by enumeration … they never rely
on numerical fixed-point search for the core result. A referee will notice this"
(research/lit_feedback-takeover-theory.md:76). I am that referee, and I do notice.

**On LMM (memo l.338).** See T-14: LMM's technology is Walrasian market clearing over a continuum of
shareholders with a bounded trade size `x` and *no* order-flow inference at all
(research/txt/levit_malenko_maug_jf2024.txt:440–450, :1421). It is a fine existence proof that
top-3 outlets publish non-Kyle trading, but LMM "prove" nothing about acceptability, and the memo
should not say they do.

**Undefined symbols in §2–§3** (each used without definition):

| symbol | first use | what it is (from draft_v2) |
|--------|-----------|----------------------------|
| `Δ̃` | l.112 | expected engagement improvement, `ρΔ_eng` — never defined in the memo |
| `m^R(a)` | l.112 | realized premium, `m^R(1)=m̃`, `m^R(0)=m₀` |
| `m̄(X,D)` | l.103 | `m₀ + π(X,D)(m̃ − m₀)` |
| `m̃` vs `m₁` | l.161 vs l.113 | memo introduces `m₁ > m₀` at l.113 then uses `m̃` at l.161 and never links them (`m̃ − m₀ = ρ²(1−θ)λΔ_eng`, D7:227) |
| `ω_E, ω_H, ω_Q, ω_P` | l.124 | region probabilities, draft_v2.tex:425–433 |
| `h` | l.162 | `h(π) = π·p(π)`, `eq:d1-hdef` |
| `p̄_1` | l.168 | disclosed-branch bid probability |
| `S̄`, `K` | l.103 | standalone synergy scale, entry cost |
| `ψ, γ, φ, q` | l.115–117 | mislabeled — see T-10 |
| `λ_crit` | l.210 | ≈0.07 numerically; no analytic characterization |
| `Δ^min` | l.187 | **never defined in the memo at all** — it is `E[m^R(a)·1{bid}]`, `eq:minority` |
| `C(s)` | never | the engagement cost — never mentioned, yet it is what separates Quiet from Exit and what (A2′) restricts |
| `τ` | l.121 | no domain, no payoff role, no mapping — see Q3 |

### Q12. Other things a referee would flag

1. **"Proved" inflation.** l.20 "provable headline theorem"; l.155 "the headline theorem"; l.174
   "one line". The draft's corresponding object is `prop:disclosure-attenuation`, explicitly titled
   "**(Partial Equilibrium)**", closed by a "*Proof sketch*" (draft_v2.tex:988–998). The memo
   upgrades the label without adding the argument. (T-16)
2. **Internal contradiction in the draft on (A5).** draft_v2.tex:1009 says the baseline *satisfies*
   the (A5) sufficient condition; draft_v2.tex:696 says it *does not*. Both cannot stand, and the
   memo's existence claim rides on the wrong one. (T-2, Q6)
3. **`δ` mismatch.** Memo l.95 "δ = 1 in the baseline" vs draft_v2.tex:1009 "δ/σ_ξ = 0.95/0.40". δ
   enters the inner-fixed-point contraction directly, so this is not cosmetic. (T-12)
4. **T2 and T4 are about different objects and the memo never says so.** T2 is about `Δ^act`; T4 is
   about `Δ^min = m₀·P(bid) + Δ^act` (`eq:decomp`, draft_v2.tex:719). A reader will assume the
   endpoint symmetry and the certified region apply to the headline object. They apply to the sum.
5. **Symbol collision on `q`:** the blockholder's order (l.83) and the fringe-raid probability
   (l.115). (T-10)
6. **`lem:dropA7`'s injectivity claim is contradicted by the paper's own Appendix B.** Worth fixing
   in the draft regardless of the memo. (T-6, Q1)
7. **The memo cites "Corum–Levit 2019, Prop. 4 template" (l.203) for non-monotonicity as an
   identification device.** I did not verify this against `research/txt/corum_levit_jfe2019.txt`
   — **OPEN**, flagged for the author.
8. **`lem:endpoints`'s equilibrium-limit sentence** (draft_v2.tex:815–817) is the load-bearing step
   that makes "endpoint symmetry (proved)" a full-equilibrium statement, and it is one asserted
   sentence backed by a numerical gap of `6.86e-7`. At JF/RFS this is a fixed-cutoff lemma plus a
   numerical remark, and should be labelled that way.

## What is proved vs. to-do

| object | status in repo | memo's label | correct label |
|--------|----------------|--------------|---------------|
| Disclosed-branch κ-invariance (`π(X,1)=1`, one price, constant `p̄_1`) | proved, draft_v2.tex:2004–2016 | "proved" (l.148, l.174) | **proved** (modulo (A5a) for inner-fixed-point uniqueness) |
| `D=0` posteriors closed form, `π(−2,0)=0` | proved, `prop:posteriors` draft_v2.tex:447–466 | "proved" (l.149–151) | **proved** |
| Dominance / menu pruning to `{E,H,Q,P}` | proved, `lem:dominance` draft_v2.tex:160–172 | "proved" (l.152) | **proved** (uses (A2), (A3)) |
| Bid monotonicity `∂p/∂P < 0` | proved, `app:proof-bid-monotone` draft_v2.tex:2115 | "proved" (l.109) | **proved** (at fixed `m̄`) |
| Existence (Brouwer on Θ) | proved, `prop:existence` draft_v2.tex:617 | "proved, **unconditional** under (A1),(A2),(A4)" (l.137) | **proved under (A1),(A2),(A4),(A5a)** — not unconditional |
| Uniqueness | not proved; numerical regularity, `rem:numreg` draft_v2.tex:701 | "labeled numerical regularity, never a theorem" (l.138–140) | **correct as labeled** ✓ |
| Endpoint symmetry `Δ^min(0⁺)=Δ^min(1⁻)` | `lem:endpoints` draft_v2.tex:796; fixed-cutoff part solid, equilibrium-limit step asserted | "proved" (l.152, l.189) | **proved at fixed cutoffs**; the full-equilibrium limit is asserted + numerically checked |
| Channel-(A) single-peakedness under (C\*) | proved, `lem:d1-jensen` draft_v2.tex:841 | "proved, conditional on (C\*)" (l.199) | **correct** ✓ — but add that (C\*) cannot fail on the calibration family (`rem:d5-vacuous`) |
| Certified region `[0.35,0.825]`, `L ≤ 0.836` | proved + machine-checked, `thm:d8-region` + `cor:d8-baseline` + JSON | "computed, machine-checked" (l.191) | **correct** ✓ |
| GE counterexample at σ_ξ=0.60 | proved + certified, `prop:d8-counter` | "certified counterexample" (l.201) | **correct** ✓ |
| `λ = 1 − q(1−γ)ψ` closed form | proved, `prop:d7-lambda` + MC check | "proved, closed form" (l.117) | **correct** ✓ (symbol labels wrong) |
| A3 iff-boundary | proved, `thm:d7-A3` + 48 cells | "all proved" (l.209) | **correct** ✓ (add maintained `θ<1`, `ρΔ_eng>0`) |
| `M(π)` reversal for `λ<λ_crit` | proved at fixed cutoffs, `prop:d7-afs`; `λ_crit≈0.07` | "the object that rationalizes Celentano–Levine's −13.7%" (l.210) | **proved, but off-calibration (baseline λ=0.86) and targeted at AFS, not CL** |
| **T2 partial equilibrium (κ-slope decreasing in τ)** | `prop:disclosure-attenuation` — **"Proof sketch"**, PE only, no τ | "the headline theorem … one line" (l.155, l.174) | **NOT PROVED as stated** — needs the τ reweighting law + the `∂|∂_κ E h|/∂π̄ ≥ 0` lemma |
| **T2 general equilibrium (region version)** | **does not exist anywhere in the repo** | written in the indicative, "the attenuation sign is certified" (l.176–183) | **TO-DO** — see Q9 for the statement to aim for |
| **τ as a model primitive** | **does not exist in draft_v2** | "explicit parameter τ, not a narrative" (l.120) | **TO-DO** — see Q3 |
| No-manipulation lemma | not written | "draft_v3 states an explicit sufficient condition" (l.216) | **TO-DO**, and likely vacuous (Q10) |
| Window ↔ noise isomorphism | Back et al. quote is real; no model object | "the window length maps to inferred-branch noise" (l.126) | **citation supported, mapping unsupported** — window maps to κ, not τ |

## Open questions for the author

1. **Which reweighting law does τ obey?** Until this is written down, T2 has no truth value. My
   recommendation is the disclosure-probability device of Q3, under which the theorem holds *a
   fortiori* — but say so and prove the second factor's monotonicity.
2. **Do you intend τ to include the window margin?** If yes, Back et al. put the window in κ and the
   policy experiment is confounded (Q5). If no, the 2024 acceleration is not a τ experiment and the
   empirical section's identification claim needs rewording.
3. **Which (A5) statement is right** — draft_v2.tex:696 or draft_v2.tex:1009? And is δ = 1 or 0.95?
4. **Will you move the calibration to `λ < λ_crit ≈ 0.07`**, or drop the Celentano–Levine
   "rationalization"? Both are defensible; presenting `λ = 0.86` and the `λ < 0.07` reversal side by
   side is not.
5. **Does removing Hold change the baseline numerics?** With `π̄ ≡ 1` the chord `[0, π̄]` is fixed, so
   `κ†` and the certified interval should be re-solved on the three-branch model before any of the
   D8 numbers are re-quoted in draft_v3.
6. **Is the equilibrium-limit step of `lem:endpoints` (draft_v2.tex:815–817) provable**, or should
   endpoint symmetry be demoted to a fixed-cutoff lemma plus a numerical remark?
7. **Corum–Levit 2019 Prop. 4 as the "identification device" template (l.203)** — I did not verify
   this. **OPEN.**
