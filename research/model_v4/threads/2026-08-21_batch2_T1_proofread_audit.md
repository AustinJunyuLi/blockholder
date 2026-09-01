# Audit — T1 (partition attenuation theorem), batch-2 proof-read

Source under audit: `research/model_v4/proofs/T1_proof.md` (committed, 813 lines). Not edited.

Auditor: fresh Opus proof-reader (theory lane), ticket 27 batch 2, 2026-08-21, repo
`blockholder_v4_theory` @ branch `v4-theory`. The auditor wrote none of the file under audit.
Stance: adversarial — every one of the 22 numbered steps was attacked before it was passed.
Role: this is the **Opus proof-read half only**. A PROVED label needs **independent re-derivation
PASS *plus* proof-read PASS** (card §6 preamble, §7). **T1 stays CONJECTURE. No label moves.**

Context read in full: `MODEL_CARD.md` (stamp 2026-08-21 · `a175202`+), `threads/thread1_turn1_answer.md`
§T1, the card ledger's T1 row, `threads/thread1_turn2_audit.md` (format), `HANDOFF_sign.md` §3
(O-1 record), and — by permission, for transcription checking only — `proofs/L4_proof.md`'s top
block (the verbatim A(br) statement and the CLAIM). No other proof file was opened.

Finding classes: **FAIL** (a step's cited hypotheses/earlier steps do not deliver it, or the math
is wrong — blocks) · **REPAIR** (the claim stands; a step uses something true but uncited, or
asserts where it should argue — never blocks) · **OBSERVATION** (a card gap or a note for later).

---

## 0. Verdicts

| Part | Steps | Verdict | Failing steps | Repairs | Claim vs card |
|---|---|---|---|---|---|
| A — factorisation | 1–8 | **PASS** | none | T1-R1, T1-R2, T1-R3 | refinement |
| B — threshold margin | 9–15 | **FAIL at Step 15**; 9–14 PASS | **15** | T1-R4, T1-R6 | refinement **+ one weakening the ledger must absorb** (T1-O6) |
| C — window margin | 16–22 | **PASS** | none | T1-R5, T1-R9 | refinement |
| Template / mechanical | — | **PASS** | none | T1-R7, T1-R8 | — |

**Overall: FAIL — one failing step (Step 15), non-propagating.** Step 15 is consumed by no other
step; the boxed conclusions of Part A (Step 6, Step 7), Part B (Step 13) and Part C (Steps 18, 20,
21) are untouched by it. The repair is one added hypothesis, not a re-argument. Everything else in
the file survived the attack.

**Mechanical scans.**

- Banned words (`clearly` / `it follows` / `standard` / `obviously` / `evidently` / `trivially` /
  `straightforward` / `well-known` / `of course` / `easily seen` / `routine`): **0 hits**, grepped
  case-insensitively across the whole file.
- draft_v2 lemma numbers, `\ref`, `\cite`, `lem:`/`prop:`/`thm:`/`app:`/`eq:`, `et al`,
  `Lemma N`/`Proposition N`/`Theorem N`/`Appendix X`: **0 hits**. Every citation is a card ID
  (D1, L1, L2, L3, L4, A1–A8, A(τ), A(br)), a numbered hypothesis H1–H15, an earlier step, or a
  card section row.
- Reserved bare letters: **0 hits** for bare `$W$`, bare `$C$`, bare `\lambda`, `\psi`, bare
  `\omega`, `\chi`. `W`/`C` always carry a margin subscript (`W_τ`, `W_T`, `W_{O1}`, `C_τ`, `C_T`,
  `C_{O1}`, `C_h`). Card §8 rule 4 respected in full.
- **Unused hypotheses: 0.** H1–H15 are each consumed by at least one step. (The bracketed
  step-lists are under-inclusive — see T1-O7 — but no hypothesis is idle.)
- **Bare steps (no citation): 0.** All 22 steps cite a hypothesis, an earlier step, or a named card
  row.
- **NOTATION DELTA completeness against card §4: two misses** — `Ω^*` and `I` (see T1-R8).
  The nine declared entries are accurate and each symbol is defined at first use.

---

## 1. Executed check — the composition arithmetic (attack priority 4)

Script: `/private/tmp/claude-501/-Users-austinli-Projects-blockholder-v4/d06ccee3-762c-4331-a587-d3581e6a875e/scratchpad/t1_audit_check.py`
(scratchpad, not committed). Inputs are the committed ratios and Ω values as printed in T1's
WHERE IT FAILS case 1, plus the raw `TV flagged` / `TV pooled` columns of `HANDOFF_sign.md` §3.

```
(1) C_O1 = committed ratio / (1 - Omega)
     Omega    1-Omega     ratio         C_O1     file     |diff|
  0.037252   0.962748   1.06397     1.105139   1.1051   3.86e-05
  0.128950   0.871050   1.18373     1.358969   1.3590   3.09e-05
  0.285804   0.714196   1.13631     1.591034   1.5910   3.38e-05
  0.500000   0.500000   0.37798     0.755960   0.7560   4.00e-05
max |C_O1 - file value| = 4.00e-05  ->  MATCHES to 4 d.p.

(2) cross-check from raw TV columns: ratio == TV_F/TV_P, and
    C_O1 == [TV_F/(1-Omega)] / TV_P
     Omega   TV_F/TV_P  committed   C_O1 raw
  0.037252     1.06392    1.06397     1.1051
  0.128950     1.18378    1.18373     1.3590
  0.285804     1.13624    1.13631     1.5909
  0.500000     0.37801    0.37798     0.7560

(3) Step 21c counterexample shape, built inside H15's freedom.
    rho(r) = -0.8(r--7.5) - 0.02;  Omega constant so Omega_r = 0
    integral of rho over [-10.0,-5.0] = -0.100000
    W_T C_T = exp(integral)        = 0.904837   (<= 1 : True)
    nodes in first half with rho>0 = 99001 of 100000
    rho(r0) = +1.9800  (local criterion VIOLATED at r0)
    rho(r1) = -2.0200
    => finite attenuation with pointwise amplification on the first half: 21c's shape is realisable under H15.
```

**Verdicts on the executed material.**

1. **The four composition factors are correct.** `1.1051 / 1.3590 / 1.5910 / 0.7560` reproduce
   `ratio/(1−Ω)` to 4 × 10⁻⁵ — i.e. exactly, at the printed precision. The file's arithmetic is
   sound and its rounding is honest.
2. **The reading of the O-1 ratio is confirmed at source.** `HANDOFF_sign.md` §3's table is
   `k_D | Ω | TV flagged | TV pooled | ratio`, and `TV_F/TV_P` reproduces each committed ratio to
   ~5 × 10⁻⁵, so the ratio T1 divides by `1−Ω` is the regime-level total-variation ratio, not a
   cell-level object. Ω values, ratios, `k_D^* = 1.28618`, `Ω^* = 0.3428 (≈0.343)` and the
   "earlier record quoted ≲0.29" remark all match `HANDOFF_sign.md` lines 28–29, 57–62, 73–79
   verbatim. **Zero miscitations in WHERE IT FAILS case 1.**
3. **Step 7's TV functional is the one O-1 computes.** `HANDOFF_sign.md` line 44: *"Measure
   κ-sensitivity as the total variation of `Δ^act` across the grid (mean |slope| is …)"*. T1's
   claim that the record uses total variation, and uses both TV and mean absolute slope, is
   accurate — and Step 7's positive-homogeneity generalisation covers mean absolute slope
   explicitly, so the theorem and the evidence are about the same functional. Attack priority 1's
   last question answers in the file's favour.
4. **Step 21c's counterexample shape is realisable, not rhetorical.** Block (3) builds one inside
   H15's own freedom: hold Ω constant across the interpolated interval (permitted — Step 16 gives
   only a weak inequality), so ρ = ∂_r log 𝒮_P, and choose any C¹ 𝒮_P > 0 realising a ρ that is
   positive on the first half. The endpoint comparison returns W_T C_T = 0.905 ≤ 1 (attenuation)
   while ρ > 0 on 99% of the first half (amplification at every intermediate window there). The
   step's warning is a live configuration, and WHERE IT FAILS case 8 is a real caution.

---

## 2. Part A — the fixed-policy factorisation (Steps 1–8): **PASS**

**Step 1 — PASS.** H2 licenses L1 at the policy in question; H3 is the card's L1 row transcribed
**verbatim** (checked character by character against card §6). Writing `Ω(κ,τ,T)` here, before
Step 4 removes κ, is the right order.

**Step 2 — PASS on the conclusion, REPAIR on the justification.**

> **T1-R1 (REPAIR).** The step applies the product rule to `Ω(κ)M_F(κ)` citing **boundedness**
> (A2) for Ω and M_F and differentiability (H7) for M_P only. Boundedness is not differentiability:
> as written, the three-term display differentiates a product two of whose factors have not been
> given derivatives. The derivatives do exist — `∂_κM_F = 0` by H4 and `∂_κΩ = 0` by H6 — but both
> are cited only afterwards, at Steps 3 and 4. Nothing is circular and the conclusion is right; the
> citation is simply the wrong one. Cleanest repair, one line and no display: by H4 and H6 both Ω
> and M_F are constants in κ, so `κ ↦ Δ^act` is an affine image of `κ ↦ M_P`, differentiable by H7
> with derivative `(1−Ω)∂_κM_P`. The three-term expansion then survives as exposition ("one term
> per factor that can carry κ"), which is what it is really doing.

**Step 3 — PASS.** H4 consumed with L2's own stack named, including the conditional "if A7's
injective form is unsatisfiable, this step is void and so is everything after it" — correct and
appropriately brutal. The card citation attached to it is now stale (T1-R7).

**Step 4 — PASS.** H6 consumed; the remark that `(M_F−M_P)` is discarded for a zero coefficient and
not for smallness is exactly the right thing to say.

**Step 5 — PASS. This is the best step in the file, and it does deliver what attack priority 1
asks.** Checked in pieces: (i) `D = 1{a_{j(s)}=1}·1{B_{j(s)}(s,H−T) ≥ τ}` — H9's clock equivalence
is stated for Voice plans only, but non-Voice plans are zeroed by the first factor whatever their
clock does, so the product formula is right for the whole menu; (ii) the no-feedback timing of card
§2 makes `B_j(s,d)` a function of `(j,s,d)` with no realised order flow or price in it, and H5
freezes `k`, so `j(s)` is a function of `s` — hence D is a function of `s` alone; (iii) the law of
`s = v+ε` is `N(μ_v, σ_v²+σ_ε²)`, and κ appears in exactly one card row (the `z_d` row, §4.1), so
`Ω = Pr(D=1)` carries no κ. **So yes: D1's clock equivalence plus the no-feedback timing do deliver
that frozen cutoffs make D a function of `s` alone, hence Ω κ-free.** The step is also right that
what does the work is the *freezing of `k`*, not any property of the rule.

> **T1-R2 (REPAIR).** Two citations are missing from a step that carries the whole PE restriction.
> (a) **The no-feedback timing is not a numbered hypothesis of this file.** It enters only inside
> H4's quoted L2 statement, but Step 5's use of it is independent of L2 — it is deriving H6, not
> invoking L2. Card §2 bullet 2 says in terms: *"L2 Steps 3 and 6 fail without this; cite it as a
> numbered hypothesis."* Same species as the turn-2 audit's L2-R2, and the card's instruction is
> explicit. Lift it to H16 and cite it at Step 5. (b) "**by A1** the law of `s` carries no κ": A1
> gives independence and positive variances; the κ-freedom of the law of `s` is card §4.1's
> distributional rows plus the fact that κ appears only in the `z_d` row. Cite both, as the turn-2
> audit did for L2 Step 6.

**Step 6 — PASS.** `|1−Ω| = 1−Ω` on `(0,1)` by H2; the boxed factorisation follows. Both recorded
consequences are correct: `𝒮>0 ⟺ 𝒮_P>0` because `1−Ω` is strictly positive; and `|·|` is
differentiable at a non-zero argument, so `𝒮_P` inherits whatever differentiability `∂_κM_P` has
in a policy coordinate. Note the second consequence is **conditional** — it transfers
differentiability, it does not create it. Step 20 respects that (H15 supplies the antecedent);
Step 15 does not (see §3).

**Step 7 — PASS, and it genuinely needs no differentiability.** Verified: the `ΩM_F` terms cancel
between grid nodes because both factors are κ-constant, `1−Ω > 0` pulls out of each absolute
value, and summing gives `𝒮^TV = (1−Ω)𝒮_P^TV`. Only H2 (at every node), H3, H4 and H6 are used —
H7 nowhere. The positive-homogeneity generalisation is also correct: if `A(cx) = cA(x)` for `c ≥ 0`
then `A` applied to the increment vector inherits the scalar, which covers total variation, mean
absolute slope and sup-norm alike.

> **T1-R3 (REPAIR).** Step 7 advertises that differentiability is not used, then consumes H6 in a
> form H6 does not state. **H6 is written as a derivative** (`∂_κΩ(κ,τ,T)=0`), and a vanishing
> derivative at a point does not give "Ω common to both nodes"; Step 7 needs Ω **constant in κ**
> across the whole grid. Step 5 derives constancy outright (D is a function of `s` alone), so
> nothing is lost — restate H6 as *"Ω(·,τ,T) is constant in κ at every policy compared"*, with the
> derivative form as its corollary. Then the file's cleanest result stops leaning on the one word
> it claims not to need.

**Step 8 — PASS.** `∂_κM_P = Δ_m A'_κ C_h(π̄)` is (br-ii) verbatim; the absolute values need
`Δ_m > 0` (card §4.1, H1) and the mean-value substitution is H12's amended L3 form applied inside
`|·|`. `𝒮_P = O(π̄²)` as `π̄↓0` is right given L3's own `h ∈ C²` near zero (which makes
`g''(ζ(π̄))` bounded near 0); T1 does not cite that, but it travels inside H12.

> **T1-O1 (OBSERVATION).** Step 8 is printed under the "Part A" heading but is consumed only by
> Step 11 and the check request. WHERE IT FAILS case 2 says "Part A and Part C survive: neither
> uses H11 or H12" — true of Steps 1–7, false of the section as laid out. Move Step 8 under Part B,
> or note in the heading that Part A's conclusion is Steps 1–7.

---

## 3. Part B — the threshold margin (Steps 9–15): **FAIL at Step 15**

**Step 9 — PASS.** Step 6 twice and one division; denominators positive by H2 and H8 at `(τ,T)`.
The remark that H5 is what makes the two sides "the same model with one primitive changed rather
than two different equilibria" is the right guard and is not decorative.

**Step 10 — PASS. The A(br) citation is clause-accurate here.** H14 leg 1 (Ω weakly rises as τ
falls) is L4's leg 1, which L4's top block certifies as *proved outright* on D1's clock
equivalence, the §2 timing, fixed policies, `b_0 < τ` **at both compared thresholds**, and A1 —
**no A(br) clause and no chord machinery**. T1 cites it that way and adds nothing. `0 ≤ W_τ ≤ 1`
then needs H2 at `(τ',T)` for the numerator and at `(τ,T)` for the denominator; H2 covers both.

**Step 11 — PASS on the citation, REPAIR on one link of the restated chain.** Checked clause by
clause against L4's top block, which is the transcription source:

| Chain item | Clause T1 assigns | Correct? |
|---|---|---|
| 1. `τ'<τ` weakly lowers `π̄_pr` | H14 leg 2, proved outright | ✓ L4 leg 2 is exactly this, and is unconditional given `Ω(τ')<1` — supplied by H2 |
| 2. lower `π̄_pr` ⟹ lower `π̄` | (br-iv) endpoint linkage | ✓ and this is the clause that keeps the π̄ ruling honest, as the step says |
| 3. lower `π̄` ⟹ smaller `|C_h|` | A(τ)'s maintained monotonicity (H11) | ✓ **but see T1-R4** |
| 4. `|A'_κ(τ')| ≤ |A'_κ(τ)|` | (br-iii) | ✓ verbatim |
| 5. multiply the two factors | Step 8's product form, which needs (br-ii) | ✓ and the step says so |
| "items 3–5 unavailable without (br-i)" | representation at **both** policies | ✓ correct dependency |

**No window-side condition leaked into the threshold proof.** Checked: Part B cites H2, H5, H8,
H9, H10, H11, H12, H13, H14 and Steps 6, 8, 9–12. H15 (the window interpolation) is cited nowhere
in Steps 9–14, and no `T'`, `W_T`, `C_T`, `Ω_{r_T}` or `B^F(T')/Q^F(T')` object appears. The window
`T` appears only as a fixed common argument. Clean.

> **T1-R4 (REPAIR — the substantive one at this margin).** Chain item 3 compares `|C_h(π̄(τ'))|`
> with `|C_h(π̄(τ))|`, i.e. it evaluates **one chord functional at two policies**. A(τ) maintains
> that `|C_h|` is weakly increasing in `π̄` *at a policy*; (br-i) fixes only the endpoints and the
> weight-derivative coefficients at the two policies; (br-ii) freezes the support points and the
> kernel **along κ**, not along τ; and (br-iv) is careful to say "the same function at τ and τ'"
> for the *endpoint* map and has no counterpart for `h`. So the inequality needs an unstated
> premise: **the chord functional `C_h(·)` — hence the univariate section of `h` — is the same
> function at τ and τ'.** This is uncomfortable rather than fatal, because it is the exact analogue
> of the argument Step 17 uses to *refuse* a window transfer (reason 3: "the conditioning event
> itself moves with the policy"): at fixed policies, changing τ moves which histories are pooled,
> which moves the pooled price `P`, which enters `h` through `p`. Non-blocking here, because Step
> 11 cites L4 leg 3 rather than re-deriving it — the premise belongs to L4's clause list. Repair:
> add a clause (br-v) "the chord functional is the same at τ and at τ'", or extend (br-i) to say
> the representation holds *with the same kernel section*.

**Step 12 — PASS.** Nonnegativity from H2 and from `𝒮_P` being an absolute value over a positive
denominator (H8).

**Step 13 — PASS.** Two factors in `[0,1]` multiply into `[0,1]`; multiplying Step 9's identity by
the positive `𝒮(κ,τ,T)` preserves the inequality. The structural remark ("no dominance condition
appears") is correct and is the honest contrast with Part C.

**Step 14 — PASS, with a wording nit.** "Strict exactly when `W_τ<1` or `C_τ<1`" is right for two
factors in `[0,1]`. The null case is characterised as "no `(j,s)` has `τ' ≤ B_j(s,H−T) < τ`" — this
should be *no positive-probability set of Voice `(j,s)`*: a null set of signals can be reclassified
without moving Ω, and non-Voice plans in that band are irrelevant because `a_j = 0` zeroes D at
both thresholds. Harmless as stated (it is a sufficient condition), imprecise as an "exactly when".

**Step 15 — FAIL.**

> **T1-F1 (FAIL).** The step writes
> `∂_{r_τ}𝒮 = −Ω_{r_τ}𝒮_P + (1−Ω)∂_{r_τ}𝒮_P` and then signs both terms. **No hypothesis in
> H1–H15 delivers the existence of either derivative in `r_τ`.**
>
> - `Ω_{r_τ}`: the step justifies its **sign** from H14 leg 1, which is a weak inequality between
>   two thresholds — monotonicity, not differentiability. A monotone function is differentiable
>   almost everywhere, never everywhere, and the step is stated at an arbitrary τ.
> - `∂_{r_τ}𝒮_P`: the parenthetical derives `𝒮_P`'s differentiability from Step 6's second
>   consequence plus H8 — but Step 6's second consequence is **conditional** ("`𝒮_P` inherits the
>   differentiability of `∂_κM_P` in any policy coordinate"). That `∂_κM_P` is differentiable in
>   `r_τ` is asserted nowhere. H7 gives differentiability in **κ** only.
>
> This is not pedantry: the card permits a concrete failure. Card §4.2 requires only **weak**
> `∂_s B_j ≥ 0`, and the 2026-08-21 A7′ row constrains only the **composed terminal target**
> `s ↦ b*_{j(s)}(s)`, not the interior date `B_j(s,H−T)`. A flat stretch of `s ↦ B_j(s,H−T)` inside
> the Voice region therefore puts an **atom** in the law of the stake at `H−T`, at which
> `τ ↦ Ω(τ)` jumps and `Ω_{r_τ}` does not exist. The very construction the card blesses for A7′
> leaves this door open.
>
> The asymmetry is what makes this a FAIL rather than a nit: the writer was scrupulous at the
> window margin, carrying H15 explicitly and recording that "the interpolation is an added
> hypothesis and is carried as one" — and then took the analogous threshold smoothness silently,
> in the step whose stated purpose is "symmetry with Part C".
>
> **Scope: non-propagating.** No later step cites Step 15; Part B's boxed conclusion is Step 13,
> which is finite-difference throughout. **Repair (one hypothesis, no re-argument):** add a
> threshold analogue of H15 — `τ ↦ Ω(τ,T)` and `τ ↦ ∂_κM_P(κ,τ,T)` continuously differentiable on
> the compared interval with `𝒮_P > 0` there — and cite it at Step 15. Alternatively restate Step
> 15 as explicitly conditional ("wherever these derivatives exist"). Either way the sentence "H14
> leg 1 gives `Ω_{r_τ} ≥ 0`" must become "H14 leg 1 plus differentiability gives …".

---

## 4. Part C — the window margin (Steps 16–22): **PASS**

**Step 16 — PASS, and the inclusion runs in the direction the step claims.** Attacked directly:
take a history flagged under the **longer** window `T`, so `B_j(s,H−T) ≥ τ` by H9. `T' < T` gives
`H−T' > H−T`, and `∂_d B_j ≥ 0` for Voice plans (H10) gives `B_j(s,H−T') ≥ B_j(s,H−T) ≥ τ`; `a_j`
is untouched by the window, so H9 read the other way at `T'` gives `D_j(s;τ,T') = 1`. Hence
**`𝒞_F(τ,T) ⊆ 𝒞_F(τ,T')`** — the *tighter* window's flagged set is the **larger** one, which is
the direction printed. Non-Voice histories need no check because `a_j = 0` puts them in neither
flagged set (H10/A4). Monotonicity of the measure then gives `Ω(τ,T') ≥ Ω(τ,T)`, which needs the
law of `(j,s)` to be the same at both windows — H5, cited. `H−T' ≤ H` is fine since `T' ≥ 1`.
Discharging turn-1 T1's hypothesis 6 is legitimate and is the file's second real contribution.

**Step 17 — PASS. All three reasons check out, including the one that is easy to get backwards.**
Reason 1: verified against L4's top block — every A(br) clause names τ and τ′ and none quantifies
over windows, so H14 has no window leg to cite. Reason 2: `B^F(T') ≤ B^F(T)` and `Q^F(T') ≥ Q^F(T)`
are card §4.2 rows, at fixed policies. Reason 3, the direction check: "no flag by `d`" means
`f = c+T > d`, i.e. `c > d−T`; under `T' < T` the excluded set is `{c ≤ d−T'}`, and `d−T' > d−T`,
so the tighter window **does** rule out more crossing dates. Concretely at `d=8`: `T=10` excludes
`c ≤ −2` (nothing), `T'=5` excludes `c ≤ 3`. The step is right.

**Step 18 — PASS.** Step 6 twice, one division, and multiplication by a positive number in both
directions. Both `𝒮_P>0` requirements are carried by H8, which names `(τ,T)` and `(τ,T')`
explicitly. The iff is exact and, as the step says, economically empty until `C_T` is measured.

**Step 19 — PASS.** `1/W_T = (1−Ω(τ,T))/(1−Ω(τ,T'))` is correct arithmetic, and the two
disclaimers ("it does not mean `|1−W_T| ≥ |1−C_T|`", "it does not mean `C_T ≤ 1`") are the right
guards against reading the ledger's "dominates" as a comparison of magnitudes.

**Step 20 — PASS on the boxed iff, REPAIR on one asserted sign.** The algebra is exact:
`∂_r𝒮/𝒮 = ∂_r𝒮_P/𝒮_P − Ω_r/(1−Ω) = ρ`, and `𝒮 > 0` makes `sgn(∂_r𝒮) = sgn(ρ)`. H15 supplies
everything the derivatives need (C¹ extensions, `Ω ∈ (0,1)`, `𝒮_P > 0`), and the file is explicit
that H15 is an added hypothesis.

> **T1-R5 (REPAIR).** "**By Step 16, `Ω_{r_T} ≥ 0`**" is not delivered. Step 16 is a two-point
> comparison of **integer** windows; H15 asks only for a C¹ extension **agreeing with the card's
> integer-valued objects at the endpoints**, which leaves the interpolant free to fall in between.
> Nothing in the file forbids `Ω_r < 0` at an intermediate `r`. The boxed iff does not use the sign
> (it is pure algebra given `𝒮 > 0`), so the step's conclusion stands — but the reading "the first
> term is the attenuating weight effect" does use it, and so does Block 5's predicted sign
> "`Ω_{r_T} ≥ 0` everywhere". Repair: add monotonicity of `r ↦ Ω(r)` to H15, where it costs
> nothing, and cite H15 rather than Step 16 for it.
>
> Note the symmetry with T1-F1: the threshold local form has monotonicity but no derivatives; the
> window local form has derivatives but no monotonicity. Each is missing exactly the half the other
> one has.

**Step 21 — PASS. All four parts verified independently.**

- **(21a)** `𝒮 > 0` and C¹ on `[r_0,r_1]` (H15 + Step 6), so `log 𝒮` is C¹ and FTC applies;
  `∂_r log 𝒮 = ρ` is Step 20. Orientation checked: `r_0 = −T < r_1 = −T'` because `T' < T`, and
  `𝒮(r_1)/𝒮(r_0) = 𝒮(τ,T')/𝒮(τ,T) = W_T C_T` matches Step 18. `exp` strictly increasing gives the
  iff in both directions. **Correct.**
- **(21b)** Integral of a nonpositive continuous function is nonpositive; strict on a subinterval
  of positive length gives a strictly negative integral. **Correct.**
- **(21c)** Mean value theorem for integrals needs exactly continuity on the closed interval, which
  H15 gives. `r^* ∈ (r_0,r_1)` with `ρ(r^*) = (r_1−r_0)^{-1}∫ρ ≤ 0`. **Correct — and the
  counterexample shape is realisable**, built and run in §1 block (3): W_T C_T = 0.905 ≤ 1 with
  ρ > 0 on 99% of the first half.
- **(21d)** The limit is the one-sided difference quotient of `r_1 ↦ 𝒮(r_1)/𝒮(r_0)` at `r_1 = r_0`,
  where the function equals 1; H15's *open* interval `I` supplies differentiability there. Both
  one-way statements are correct, and naming `ρ(r_0)=0` as undetermined at first order rather than
  resolving it is the right call. **Correct.**

**Step 22 — PASS.**

> **T1-O5 (OBSERVATION).** "The committed O-1 record supplies a measured instance of the amplifying
> branch at low Ω and of the attenuating branch at Ω = 0.50" reads, in isolation, as if O-1
> measured `W_T C_T`. WHERE IT FAILS 1b and NOT CLAIMED 7 explicitly deny that, and the sentence
> does point at case 1 — but one clause ("of the analogous rule-on/rule-off product") would remove
> the tension for a reader who meets Step 22 first.

---

## 5. The ledger's "equivalently" (attack priority 5)

**The writer's reading is right on the mathematics and incomplete on the remedy.** 21c is correct:
`W_T C_T ≤ 1` does **not** imply `ρ(r) ≤ 0` at every window value, and §1 block (3) exhibits a
configuration where it fails on half the interval. So the ledger's two forms are not
interchangeable under a pointwise reading of the second.

**But there is an interpretation under which the ledger is fine, and the file's own Step 21a
supplies it.** (21a) proves `W_T C_T = exp(∫ρ)`, hence

> `W_T C_T ≤ 1` **⟺** `∫_{−T}^{−T'} [∂_r𝒮_P/𝒮_P − Ω_r/(1−Ω)] dr ≤ 0`.

That is an *exact* two-way equivalence at finite scale. The ledger row writes its second criterion
without a quantifier; read as an **average along the tightening path** it is exactly equivalent to
the product form, and read as **pointwise at each `r`** it is strictly stronger (21b one way only).
The row is therefore ambiguous, not wrong.

> **T1-R9 (REPAIR — card-owner-facing, supersedes the file's own flag).** The file's flag says "if
> the row is kept as-is, it should be read in the infinitesimal sense". That discards the better
> reading. The repair is to **add the quantifier**, not to demote the row to an infinitesimal
> statement: e.g. *"… `W_T C_T ≤ 1`, equivalently `∫ρ ≤ 0` along the tightening path, where
> `ρ = ∂_{r_T}𝒮_P/𝒮_P − Ω_{r_T}/(1−Ω)`; pointwise `ρ ≤ 0` is the local (marginal) form and is
> sufficient, not necessary."* Card §5's A(τ)-style phrasing already shows the house style for this.
> Still a wording repair, still no label move.

---

## 6. Cross-consistency with the π̄ ruling (attack priority 6): **clean**

No step uses the share reading. Checked every occurrence: Step 8 (chord endpoint), Step 11 item 2
(explicitly separates the share from the support point and attributes the link to (br-iv)), Step 14
(lists `π̄_pr` and `π̄` as distinct objects), WHERE IT FAILS 3 (br-iv gloss), Block 3 (demands
separate columns and names the conflation as the likely implementation error), NOTATION DELTA (both
declared). **Zero silent share-readings.**

The ruling's own arithmetic also checks out independently: applying A(τ)'s representation to
`h = id` gives `∂_κ𝔼[Π_κ] = A'_{1/2}π̄/2 + A'_1π̄ = −A'_κπ̄ + A'_κπ̄ = 0`, so the share is
κ-invariant as H11 states; and `𝔼[Π_κ] = π̄(A_{1/2}/2 + A_1) < π̄` whenever `A_0 + A_{1/2}/2 > 0`,
which is every non-degenerate case. Both halves of the ruling are true, not just asserted.

> **T1-O4 (OBSERVATION).** The file never states that the ruling's share `𝔼[Π_κ]` and its own
> `π̄_pr = Pr(a=1|D=0)` are the **same number** (tower property: the mean pooled posterior is the
> pooled prior share). As printed, a reader meets three objects — `π̄`, `𝔼[Π_κ]`, `π̄_pr` — where
> there are two. One sentence in the NOTATION DELTA fixes it and makes (br-iv) visibly a link
> between two objects rather than three.

---

## 7. Transcription check — A(br) and the L4 legs (attack priority 2)

Compared T1's H13 with `L4_proof.md`'s top block, clause by clause. **(br-i), (br-ii), (br-iii)'s
inequality and (br-iv) are transcribed accurately**, including the "same function at τ and τ'"
qualifier in (br-iv) and the "no composition-through-κ remainder" in (br-ii). Punctuation differs
(colons for periods); no content differs.

> **T1-O2 (OBSERVATION).** L4's leg numbering is ambiguous **in the source**: its VERDICT block and
> its Part headings number Ω / π̄_pr / 𝒮_P as legs 1 / 2 / 3, while its CLAIM lists four items
> (inclusion, Ω, π̄_pr, 𝒮_P) and says "Legs 1–3 are unconditional … leg 4 is conditional on A(br)"
> under that second numbering. T1's H14 uses the verdict/part numbering **and states each leg's
> content in words**, so every citation resolves correctly and there is no error in T1. Flagged so
> the re-deriver checks the words, not the numbers.

> **T1-O3 (OBSERVATION).** Two things in L4's A(br) block do not travel into T1. (a) (br-iii)'s
> gloss — "weakest sufficient form: equality — reclassification changes *which* histories are
> pooled, not the κ-responsiveness of the pooled weights" — is dropped from a quote labelled
> verbatim; harmless, but it is the sentence that tells a referee how weak (br-iii) really is.
> (b) More substantively, L4 records that under the level-symmetric reading `π̄ = 2π̄_pr`, so
> `π̄ ≤ 1` forces **`π̄_pr ≤ 1/2`** — "a restriction on A(τ)'s domain that L4 inherits and does not
> resolve". That restriction travels with Part B and is nowhere in T1: every Part B conclusion
> silently inherits a cap on the pooled prior engagement share. It belongs in H11 or in WHERE IT
> FAILS 3.

---

## 8. Card citations and template

> **T1-R7 (REPAIR — stale stamp, four live citations).** The header and H1 stamp the card at
> **2026-08-20 · `0c9185b`**; the live card is **2026-08-21 · `a175202`+**, and the card's own
> stamp line rules that "an answer written against a stale stamp is re-asked, not accepted". The
> one place it bites substantively: **H4, WHERE IT FAILS 6, LABEL CLAIMED 3 and NOT CLAIMED 5 all
> say the card records A7's injective-form satisfiability as *open*.** Card §5's A7 note now
> records it as **resolved** (ticket 24: A7′ + a fixed cutoff policy + `Ω>0` deliver the *on-path*
> injective form with an explicit inverse; a satisfying menu exists — the pro-rata single-Voice
> menu; adversarial verdict SURVIVES WITH REPAIRS). T1 therefore **understates** what is available
> — conservative, never overstating — so no step's logic changes and nothing is blocked. But four
> citations are false as citations, and the file never mentions the A7′ row that §4.2 now carries.
> Re-stamp and re-point those four.

> **T1-R6 (REPAIR — WHERE IT FAILS 4 is too narrow).** The `𝒮_P = 0` case is attributed entirely to
> the `π̄ ↓ 0` corner ("the small-π̄ corner is exactly where the ratio form loses resolution").
> Step 8's own product form gives two further routes at `π̄` bounded away from zero: `A'_κ = 0`
> (pooled weights κ-insensitive) and `C_h(π̄) = 0` with `π̄ > 0` (kernel affine across the three
> support points). The second is not hypothetical — card §5's A(τ) row says in terms that "**the
> `C_h = 0` case must be handled explicitly**", and L4's leg-3 claim carries "with equality whenever
> `C_h(π̄(τ)) = 0`", a qualifier T1's H14 transcription drops. Add both routes to case 4, and carry
> L4's equality qualifier into H14.

> **T1-R8 (REPAIR — NOTATION DELTA misses).** Card §8 rule 3 asks for **every** symbol not in §4.
> Two are missing: **`Ω^*`** (the sign boundary, used in WHERE IT FAILS 1, Block 6 and NOT CLAIMED
> 10) and **`I`** (the open window interval, H15). `k_D^*` is borderline — `k_D` appears in card
> §4.5 only as a draft_v2 alias inside the `k` row — and should be declared alongside `Ω^*` as
> O-1-record notation. The nine declared entries are otherwise complete and correct: checked line
> by line, and the closing paragraph's claim that the reserved bare letters appear nowhere in the
> file is **confirmed by grep** (0 hits).

> **T1-O6 (OBSERVATION — the ledger row must absorb a weakening).** Claim-vs-card is a refinement
> in two directions — Step 16 discharges the card row's window hypothesis, Step 21 pins
> "equivalently" — but the threshold leg is **weaker** than the ledger row. The row states, at
> fixed policies, "threshold tightening attenuates 𝒮" **unconditionally**; T1 proves it only under
> **A(τ) and A(br)**, and A(τ)'s applicability to the two-round pooled cell is OPEN (H12). If this
> file lands, the row must read "under A(τ) and A(br)" or the ledger overstates what exists. The
> file's own LABEL CLAIMED already says this ("PROVED under A(τ) and A(br) at fixed policies"); the
> card has not caught up.

> **T1-O7 (OBSERVATION).** The bracketed step-lists on H1–H15 are under-inclusive: H13 and H14 are
> also consumed at Step 15, H2 at Steps 10, 12, 13, 16 and 21, H8 at Step 21. No hypothesis is
> unused and no step is bare, so the mechanical scan passes; the brackets are a navigation aid that
> is slightly out of date with the steps.

---

## 9. Counts and what moves

**FAIL 1** (T1-F1, Step 15) · **REPAIR 9** (T1-R1 … T1-R9) · **OBSERVATION 7** (T1-O1 … T1-O7).

Banned-word hits **0**. draft_v2 / `\ref` / `\cite` / external-citation hits **0**. Reserved
bare-letter hits **0**. Unused hypotheses **0**. Bare steps **0**. NOTATION DELTA misses **2**.
Executed arithmetic: **4 of 4 composition factors reproduce to 4 × 10⁻⁵**; O-1 citations **0
miscitations against `HANDOFF_sign.md` §3**; Step 21c's counterexample shape **realisable, built
and run**.

**What blocks.** Step 15 only. It is consumed by no other step, so Parts A and C and Steps 9–14 of
Part B stand as written; the fix is one added hypothesis (a threshold analogue of H15) or one
conditional clause. Under the one-retry rule this is a single-step repair round, not a bounce of
the file.

**No label moves.** This audit is the proof-read half only. **T1 remains CONJECTURE**, and would
land — after an independent re-derivation PASS — as *"PROVED at fixed policies under A(τ) and
A(br)"*, with Part A and Part C free of A(τ)/A(br) and resting instead on L1, L2 (hence A7-injective)
and PE-Ω. The largest risks carried forward are unchanged from upstream: A(τ)'s applicability to the
two-round pooled cell (OPEN per L3) and A(br)'s four clauses, to which T1-R4 would add a fifth.
