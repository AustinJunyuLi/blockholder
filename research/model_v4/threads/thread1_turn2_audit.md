# Audit — Thread 1, turn 2 (proofs of D1, L1, L2)

Source under audit: `research/model_v4/threads/thread1_turn2_answer.md` (verbatim, never edited;
read through the paste mangling — missing `=` between displayed lines, a stray `* ` where a `+`
stood in D1 Step 12, a stray `1.` where `= 1.` stood in L2 Step 7).

Auditor: Claude Code (theory lane), 2026-08-20, repo `blockholder_v4_theory` @ `6f36b1d`.
Stance: adversarial — every numbered step was attacked before it was passed.
Role: this is the **Opus proof-read half** only. Per the handoff protocol
(`quality_reports/handoffs/2026-08-19_theory-lane-handoff.md`, §"The GPT Pro protocol"), a PROVED
label needs **independent re-derivation PASS *plus* Opus proof-read PASS**. This audit supplies the
second. **All three results stay CONJECTURE** until Thread 2 re-derives them. GPT's own "PROVED"
claim moves nothing.

Finding classes: **FAIL** (a step's cited hypotheses/earlier steps do not deliver it, or the math is
wrong — blocks) · **REPAIR** (the claim stands; a step uses something true but uncited, or asserts
where it should argue — never blocks) · **OBSERVATION** (a card gap or a note for later turns).

---

## 0. Verdicts

| Result | Verdict | Failing steps | Repairs | Claim vs card |
|---|---|---|---|---|
| D1 | **PASS** | none | D1-R1, D1-R2, D1-R3 | **refinement** |
| L1 | **PASS** | none | L1-R1 (cosmetic) | **refinement** |
| L2 | **PASS** | none | L2-R1 … L2-R4 | **refinement** |

**Mechanical scans.**
- Banned words (`clearly` / `it follows` / `standard` / `obviously`, plus `evidently`, `trivially`,
  `straightforward`, `well-known`, `of course`, `easily seen`, `routine`): **0 hits** across the
  whole answer. Turn 1's clean record holds now that there are actual proofs.
- draft_v2 lemma numbers, `\ref`, `\cite`, `lem:`/`prop:`/`thm:`/`app:`/`eq:`, external references
  (`et al`): **0 hits**. Every citation is a card ID (A1–A5, A7, A8), a numbered hypothesis, or an
  earlier step.
- **Unused hypotheses: 0.** D1 h.1–4 all used; L1 h.1–2 both used; L2 h.1–7 all used (h.2 only at
  Step 2, h.4 only at Step 9, h.5 only at Step 1 — once is enough).
- **Bare steps (no citation): 0.** All 13 + 7 + 12 steps carry a hypothesis or step citation.
- NOTATION DELTA completeness: D1 "None" and L1 "None" are honest (neither introduces a symbol).
  L2's eight declared symbols are the complete set of non-§4 symbols it uses — checked line by line.

---

## 1. D1 — rule-keyed partition and timing split

### 1.1 Claim vs the card's ledger row

Card row: *"D = 1{a=1, c(τ)+T ≤ H} maps every control-node history into exactly one cell, and each
flagged history yields B^F, R_d, R, J with P^F − P_{c^-}^P = R + J."*

The turn-2 CLAIM adds (i) **measurability** of D, and (ii) the clock equivalence
`f_j ≤ H ⟺ B_j(s,H−T) ≥ τ` for every Voice plan. Both are strictly more than the row asserts. (ii)
already sits in the card's §4.2 `f_j` row but was never in the ledger statement.
**Classification: refinement.** The card's D1 row is updated accordingly.

### 1.2 Step-by-step

**Steps 1–2 — PASS.** Upper level sets of a weakly increasing `s ↦ B_j(s,d)` are intervals
unbounded above (or empty, or the whole line), hence Borel; `{c_j ≤ H−T} = ⋃_{d=0}^{H−T}{B_j(s,d) ≥
τ}` is exactly the statement that an infimum over a finite date set is attained below `H−T` iff some
member qualifies. Both correct. The union needs `H−T ≥ 0`, which `T ∈ {1,…,H}` (h.1) supplies, and
needs date `0` in the calendar, which card §2 supplies.

**Hypothesis 1's monotonicity is genuinely a card restriction.** Checked: card §4.2, `B_j(s,d)` row —
*"for Voice: ∂_d B_j ≥ 0 and ∂_s B_j ≥ 0"*. Both directions are there. WHERE-IT-FAILS case 1 ("a
Voice stake path may fall after first reaching τ") is therefore a legitimate necessity demonstration
for a hypothesis the card actually carries, not a hidden assumption smuggled in as a failure case.

**Steps 3–6 — PASS.** `c_j + T ≤ H ⟺ c_j ≤ H−T` including `c_j = +∞` (both sides false under
`∞+T = ∞`). Step 4 (⟹) is where `d`-monotonicity is used and is the only place it is needed; Step 5
(⟸) needs no monotonicity at all. Step 6's flat-at-τ case is correct, if slightly redundant — the
whole argument runs on weak inequalities, so a path that sits exactly at τ never needed separate
treatment.

**Edge cases the audit stressed, all clean:**

| Edge | Resolution |
|---|---|
| `T = H`, so `H−T = 0` | Date 0 is in the calendar (card §2: `d = 0,…,H`), so `B_j(s,0)` is a genuine calendar value and the equivalence reads `f_j ≤ H ⟺ B_j(s,0) ≥ τ`. The `B_j(s,−1) = b_0` convention is a *pre*-calendar initial condition and is not needed here. No break. |
| `c = +∞` | Step 5's contrapositive: if `B_j(s,H−T) ≥ τ` then `c_j ≤ H−T`. So `c = ∞ ⟹ B_j(s,H−T) < τ`, the second indicator is 0, `D = 0`. Consistent. |
| Voice plan crossing **after** `H−T` (`c_j` finite, `c_j > H−T`) | Same contrapositive: `c_j > H−T ⟹ B_j(s,H−T) < τ ⟹ D = 0`. Step 7's product formula returns 0, which is also the economically right answer (crossed too late for the filing to land before the control node). **The product formula does not break.** |

**Step 7 — PASS on the math, REPAIR on the citation.**
`D_j = 1{a_j=1}·1{B_j(s,H−T) ≥ τ}` reproduces the card's `D_j = 1{a_j=1, c_j<∞, f_j ≤ H}`: `f_j ≤ H`
already forces `c_j < ∞`, and non-Voice plans are zeroed by the first factor (h.2 / A4: only Voice
plans cross in the core). Correct.

> **D1-R1 (REPAIR).** The CLAIM partitions *control-node **public** histories*; Steps 7–8 establish
> that `D` is measurable with respect to `σ(j,s)`. The bridge from "function of the plan and signal"
> to "function of what is observed at the control node" is **the card's §4.3 row**
> (`𝓗_d^P = (X_0,…,X_d; flag landed by d)` — the flag is a coordinate of the public history *by
> construction*) together with A4's public filing at exactly `f_j`. That bridge is true and
> card-backed, and it is **never cited**. Step 8's phrase "its observed flag coordinate is
> measurable" gestures at it without naming the source. Add it as a numbered hypothesis and cite it
> at Steps 7 and 9. Non-blocking: the fact exists in the card, so nothing is lost.

**Step 8 — PASS, but the finiteness argument is incomplete as written. This is the step the audit
was asked to stress, and it does not survive intact.**

> **D1-R2 (REPAIR).** **A2 plus a finite calendar do *not* make `B^F` finite-valued.** A2's
> finiteness covers the plan menu, `Γ`'s image (order marks), the noise support, and the calendar
> horizon. It says nothing about the *stake level*: card §4.2 puts `B_j(s,d) ∈ [0,b̄]` with `s`
> continuous (Gaussian) and imposes only weak monotonicity — no card row discretises the stake path.
> So `B^F = B_j(s,f_j)` is **continuum-valued in general**, and so is `Q^F = b_j*(s) − B^F`.
>
> The step does not actually over-claim: it says the *pooled* alphabet is finite and calls the
> augmenting tuple only "measurable". Read strictly, it is right. What is missing is the argument for
> that measurability, which is asserted, not shown. It is one line and should be written in: `f_j` is
> finite-valued and measurable (Steps 1–5), so
> `B_j(s,f_j(s)) = Σ_{d=0}^{H−T} 1{f_j(s) = d+T}·B_j(s,d)` is a finite sum of measurable functions,
> each measurable by Step 1. Likewise `Q^F`. And "the control-node history space is a finite union of
> measurable components" must be read as a finite union *over the pooled alphabet*, each element
> carrying a measurable — not finite — fibre in `(B^F,Q^F,a)`.
>
> **The consequence the step does not address:** a continuum-valued flagged tuple means the flagged
> information set is continuum-indexed, so A5's "each public-history pricing map has a unique fixed
> point" must be read as a family of fixed points **measurably selected** across a continuum of
> flagged tuples, not a finite list. A5's own wording ("continuous in beliefs, cutoffs and
> parameters") supplies the selection, so this is repairable from the card — but it must be said,
> because D1 Step 11 and L2 Steps 8–9 both consume it.
>
> This finding locks with **L2-R1** below: A7's injective form *requires* `B^F` to be
> continuum-valued (an injective map out of a continuum of signals cannot land in a finite set). D1's
> instinct toward finiteness and L2's injectivity hypothesis are pulling in opposite directions, and
> the card must resolve it in favour of the continuum.

**Steps 9–10 — PASS.** Disjointness and exhaustion from preimages of `{0}` and `{1}`; Step 10's
observation that no probability restriction entered is correct and is the exact repair of the
handoff's named hazard (the interior-crossing condition belongs in a hypothesis, A8, and only where
positive mass is genuinely needed).

**Step 11 — PASS, with a live edge case the step does not cover.**

> **D1-R3 (REPAIR).** `R_d = P_d^P − P_{c^-}^P` and `R = P_{f^-}^P − P_{c^-}^P` both need
> `P_{c^-}^P`. When `c_j = 0`, `c^-` is date `−1`, and **the card defines no pooled price there**:
> §4.3 gives `𝓗_d^P = (X_0,…,X_d; …)` for `d ≥ 0` only. The `B_j(s,−1) = b_0` convention covers the
> stake, not the price.
>
> This is not an exotic corner. At `T = H` the flag requires `B_j(s,0) ≥ τ`, i.e. `c_j = 0` on
> **every** flagged history — so at the tightest window in the grid, the entire run-up path is
> measured from an undefined base. Repair: add the card convention `P_{−1}^P := 𝔼[Y]` (the
> pre-trading pooled price under the prior), exactly parallel to `B_j(s,−1) = b_0`. Step 11 then
> holds verbatim.

**Steps 12–13 — PASS.** The timing split is add-and-subtract on `P_ND(𝓗_{f^-}^P)`, which h.4 defines
as the same-realised-order-flow counterfactual and therefore equal to `P_{f^-}^P`. Nothing but
bookkeeping, and Step 13 says so in the words msg 2 asked for. The stray `* ` in the paste is a
mangled `+`; with it restored the algebra is exact.

### 1.3 One card gap D1 exposes

> **D1-O1 (OBSERVATION — card gap, not a proof defect).** Nothing in the card excludes `b_0 ≥ τ` —
> a blockholder who already holds at or above the threshold before the calendar starts. Then A4's
> "`c` is the first date the path reaches τ" is violated in substance (the path reached τ before date
> 0), while `c_j = inf{d ∈ {0,…,H} : …}` silently re-dates the legal clock to the calendar. For Voice
> plans `d`-monotonicity rescues it (`B_j(s,0) ≥ b_0 ≥ τ ⟹ c_j = 0`); for Exit/Hold it does not, and
> A4's "only Voice plans cross in the core" is what currently keeps it harmless. Recommend the card
> either impose `b_0 < τ` or state explicitly that a pre-existing crossing is outside the core.

---

## 2. L1 — premium cell decomposition

### 2.1 Claim vs the card's ledger row

Card row: *"Whenever 0<Ω<1, Δ^act = ΩM_F + (1−Ω)M_P."* The turn-2 CLAIM adds both boundary
degenerations (`Ω=1 ⟹ Δ^act = M_F`; `Ω=0 ⟹ Δ^act = M_P`) and the status of the null-cell average.
**Classification: refinement.** Card row updated.

### 2.2 Step-by-step — the answer to "is anything actually missing?": **no. This is clean.**

**Steps 1–2 — PASS.** `1{D=1} + 1{D=0} = 1` pointwise (h.1 gives binary + measurable); multiply by
the integrable variable and use linearity. h.2's integrability is what licenses splitting a finite
expectation into two finite ones, and it is genuinely automatic here (`h = πp ∈ [0,1]`, `Δ_m` finite),
which the hypothesis says.

**Step 3 — PASS. The conditioning identity is exactly right.** `𝔼[X1_A] = Pr(A)·𝔼[X|A]` when
`Pr(A) > 0` **is** the definition of conditional expectation given a positive-probability event —
not a theorem being leaned on, and the step says so ("the defining property of conditioning on an
event with positive probability"). `Δ_m` is a constant (card §4.1) and pulls out. Matching against
card §4.4: `M_F ≡ Δ_m 𝔼[h|D=1]`, `M_P ≡ Δ_m 𝔼[h|D=0]`, so `Pr(D=1)Δ_m𝔼[h|D=1] = Ω M_F` is
substitution of definitions, nothing more. Correct both times.

**Steps 4–6 — PASS. Both boundary degenerations are correct.** At `Ω=1`: `Pr(D=0) = 0` and the
integrand is bounded, so the second expectation vanishes; conditioning on a probability-one event
returns the unconditional mean, so `M_F = Δ_m𝔼[h] = Δ^act`. Symmetrically at `Ω=0`. And the
statement that the *other* cell's average is undefined (rather than zero, or than anything else) is
the correct and honest reading.

**Step 7 — PASS.** The remark that a full-support-perturbation limit may be *inserted* into a
zero-weight term but is a convention, not an identified conditional expectation, is right and is
consistent with the card's equilibrium notion (vi). It correctly refuses to let an off-path
convention do work.

> **L1-R1 (REPAIR — cosmetic).** The interiority condition `0<Ω<1` lives in the CLAIM's antecedent
> and is invoked inside Step 3, but is not a numbered hypothesis — while L2 lists `Ω>0` as its
> Hypothesis 7. Make the two consistent: either list it, or state in both that it is a case split
> carried by the claim.

**L1-O1 (OBSERVATION).** Step 2 uses the card §4.4 definition `Δ^act = Δ_m𝔼[h(𝓘_H)]` without citing
it. Acceptable — card §4 definitions are shared vocabulary, not hypotheses, and the template asks
steps to cite *hypotheses or earlier steps*. Logged so the pattern is deliberate rather than drifting.

---

## 3. L2 — flagged-cell direct liquidity-invariance

### 3.1 Claim vs the card's ledger row — the refinement the card must absorb

Card row: *"At fixed cutoff and execution policies, A7 makes the flagged posterior, price, entry
probability and M_F invariant to κ."*

The turn-2 CLAIM (a) names A1, A4, A5 alongside A7, (b) requires **A7 in its injective-recoverability
form**, (c) requires **Ω > 0**, and (d) promotes the conditional-independence statement into the
claim itself. Its LABEL CLAIMED block goes further and states outright that the card's *primary*
A7 wording — "identifies the informed component" — **is not sufficient** if it permits two `(j,s)`
pairs with different pooled paths.

**Classification: refinement**, unambiguously — stronger and more honest hypotheses, no silent
weakening anywhere. The card's L2 row and a note under A7 are both updated.

### 3.2 The three steps the audit was asked to stress — all three are correct

**Step 3 — the σ(W)-measurability claim. PASS, and it is true in this model.** Checked object by
object, at fixed policies:

| Object | Why it is `σ(W)`-measurable | Source |
|---|---|---|
| `j` | the fixed cutoff policy maps `s ↦ j`, and `s ⊂ W` | h.6 |
| `D` | `D = 1{a_j=1}·1{B_j(s,H−T) ≥ τ}` — a function of `(j,s)` | **D1 Step 7** |
| `B^F` | `B_j(s, c_j(s;τ)+T)`, a function of `(j,s,τ,T)` | card §4.2 |
| `Q^F` | `b_j*(s) − B_j^F`, a function of `(j,s,τ,T)` | card §4.2 |
| `a` | `a_j`, fixed by the plan index | card §4.2 |

The property that makes all of this true is that **the pooled stake path carries no feedback from
realised order flow or prices**. Checked against the card and it holds: §2 timing bullet 2 states
*"No within-window re-optimisation"*, and §4.2 writes the objects as `B_j(s,d)`, `q_{jd}(s)` and
`Q_j^F = b_j*(s) − B_j^F` — the notation itself encodes that the arguments are `(j,s,d)` and
`(j,s,τ,T)`, never the realised history. **The task's specific check — that `Q_j^F` cannot depend on
the realised pooled history — is confirmed: `Q_j^F = b_j*(s) − B_j^F` is a function of `(j,s,τ,T)`
alone.**

Given that, the displayed identity collapses to a triviality in the right way: `σ(𝖲_F) ⊆ σ(W)` and
`{D=1} ∈ σ(W)`, so conditioning on `(W, 𝖲_F, D=1)` is conditioning on `σ(W)` restricted to a
`σ(W)`-event, and A1's `𝐳 ⟂ W` gives `Pr(𝐳 ∈ A)` on both sides. The parenthetical "the middle
probability may vary with κ" is correct and honest — it is the *only* place κ appears in the step.

> **L2-R2 (REPAIR).** The no-feedback property is **not among L2's numbered hypotheses**. Hypothesis
> 6 says the policies are held fixed *as κ varies*, which is a different statement: a feedback rule
> `B_j(s,d,𝓗_{d−1}^P)` could be "held fixed across κ" and still make `f`, `B^F` and `Q^F`
> noise-dependent — at which point `𝖲_F` is no longer `σ(W)`-measurable and **Steps 3 and 6 both
> fail**. The property is true and card-backed (§2 + §4.2), so nothing is lost, but it is
> load-bearing and must be lifted into a numbered hypothesis and cited at Steps 2, 3 and 6.

> **L2-R3 (REPAIR).** Step 3 conditions on `{D=1}` without citing h.7 (`Ω > 0`), which is what makes
> that conditioning defined. h.7 is cited only at Step 11. Cite it from Step 3 onward.

> **L2-R4 (REPAIR).** Step 3's "`D` is a function of `W`" **is D1's Step-7 product formula**, and D1
> is not among L2's hypotheses — L1 does list it as its Hypothesis 1. Add D1 to L2's hypothesis list.

**Step 4 — the factorization. PASS. Legitimate, and there is no circularity.** Taking the three
equalities in turn:

1. **Tower.** `σ(𝖲_F, 1{D=1}) ⊆ σ(W, 𝖲_F, 1{D=1})`, so iterating is valid; and
   `𝓗^P = Υ_{j,s}(𝐳) = Υ_{ι_F(𝖲_F)}(𝐳)` by Steps 1–2. Correct.
2. **Middle equality — the one queried.** By Step 3 the conditional law of `𝐳` given
   `(W, 𝖲_F, D=1)` is the unconditional law, so the inner expectation equals
   `∫ u_2(Υ_{ι_F(𝖲_F)}(z)) dP_κ(z)` — **a function of `(ι_F(𝖲_F), κ)` and hence `σ(𝖲_F)`-measurable
   at fixed κ**. The same computation with the coarser conditioning gives the same integral, which is
   exactly `𝔼[u_2(𝓗^P)|𝖲_F, D=1]`. **Legitimate.**
3. **Pull-out.** That factor is `σ(𝖲_F)`-measurable and bounded (`u_2` bounded), so it comes out of
   the outer conditional expectation. Correct.

**On circularity:** conditioning on a σ-field generated by a function of `W` is the ordinary
sufficient-statistic construction, not a loop. The reason nothing leaks is that A1 gives
`𝐳 ⟂ W` *jointly*, hence `𝐳 ⟂ (W, 𝖲_F, 1{D=1})` — so no conditioning built out of `W` can inform
about `𝐳`, and no conditioning on `𝐳`-generated objects appears anywhere in the step. **No
circularity.**

Worth noting what the conditional independence *reduces to* here: `ι_F` recovers `s` exactly, so
conditional on `𝖲_F` the signal is degenerate and the content is `(v,ξ) ⟂ 𝓗^P | s`, which A1
delivers directly. See L2-R1 — that is a comment on A7's strength, not on the step.

> **L2-O2 (OBSERVATION — nit).** Step 4 concludes that the factorization "proves the required
> conditional-independence statement" without naming the characterization it uses
> (`𝔼[u_1u_2|𝒢] = 𝔼[u_1|𝒢]𝔼[u_2|𝒢]` for all bounded measurable `u_1,u_2` ⟺ conditional independence
> given `𝒢`). Not a banned-word hit and the algebra is fully displayed, so this does not bounce —
> but name the characterization in the `.tex` write-up.

**Step 6 — κ-invariance of the joint law of `(W, 𝖲_F, D)`. PASS. This is where the result lives and
it is right.** The argument decomposes into three facts, each verified:

1. **`W`'s law is κ-free.** Card §4.1: `v ~ N(μ_v,σ_v²)`, `ε ~ N(0,σ_ε²)`, `ξ ~ N(0,σ_ξ²)`. No κ in
   any of them. κ appears in exactly one card row — `z_d`, where `Pr(z_d=0) = 1−κ`,
   `Pr(z_d = ±z̄) = κ/2`. A1 gives the independence, h.6 states the confinement. ✓
2. **`𝖲_F` and `D` are κ-free *functions* of `W`.** Established in Step 3 (table above), at fixed
   policies. ✓
3. **Therefore the joint law of `(W, 𝖲_F, D)` is the pushforward of a κ-free law under a κ-free map,
   hence κ-free** — and the conditional law `Pr(W ∈ · | 𝖲_F, D=1)` can be chosen identically across
   κ. ✓ The "up to conditional null sets" hedge is harmless and mildly over-cautious: the null sets
   are determined by the law of `(𝖲_F, D)`, which the same argument makes κ-free, so they coincide
   too.

**The ordering of Steps 5 → 6 is the load-bearing logic, and it is correct.** Step 5 removes `𝓗^P`
— the one object whose law genuinely does move with κ — from the posterior; Step 6 then only has to
show that what remains is κ-free. Reversing them would not work. The proof says exactly this, and
Step 12 names κ's single entry point and disclaims the GE channel, as msg 2 required.

### 3.3 Steps 8–10 — consistency with the card, checked arithmetic

| Check | Result |
|---|---|
| `Y` at `a=1` | Card §4.3: `Y = (1−𝖡)(v+aΔ_V) + 𝖡(P+m_0+aΔ_m)`. At `a=1`: `(1−𝖡)(v+Δ_V) + 𝖡(P+m_0+Δ_m)`. Card §4.1: `Δ_m = m_1 − m_0`, so `m_0+Δ_m = m_1`. Step 8's `𝖡(P+m_1)` is **exact**. ✓ |
| entry rule at `π=1` | Card §4.3: `p = 1 − Φ((P+K+m_0+πΔ_m−S̄)/σ_ξ)`. At `π=1`: `1 − Φ((P+K+m_1−S̄)/σ_ξ) = Pr(ξ > P+K+m_1−S̄) = Pr(S̄+ξ−K−P−m_1 > 0)`. Step 8's `𝖡 = 1{S̄+ξ−K−P−m_1 ≥ 0}` and Step 10's `p` are **exact** (`≥` vs `>` is a null-set difference for continuous `ξ`). ✓ |
| `π = 1` on the flagged cell (Step 7) | A4 gives `D=1 ⟹ a=1` (card §4.2, `D_j` row), so conditioning on `D=1` makes `Pr(a=1|·) = 1`. Matches card §4.3, `π(𝓘)` row: "`= 1` on `𝒞_F`". ✓ The paste's stray `1.` is the `= 1`. |
| `h = πp = p` on `D=1` (Step 11) | Card §4.4: `h = πp`. With `π=1`, `h = p`. ✓ |
| `M_F = Δ_m𝔼[p|D=1]` κ-free (Step 11) | Needs **both** that each `p` is κ-free (Step 10, pointwise in the flagged tuple) **and** that the law of `𝖲_F` given `D=1` is κ-free (Step 6). Step 11 states both. Neither alone suffices — `p` varies across flagged tuples because `P^F` does. ✓ |

**Step 9 — is A5's uniqueness genuinely needed? Yes, and the reasoning is stated, not assumed.**
Step 8 delivers a κ-free pricing *map*; the object the model uses is a *selected fixed point*. Step 9
says in its own words that without uniqueness "an extraneous fixed-point selection could vary with κ
even when the map itself does not". That is precisely the right reason, it is written out rather than
waved at, and WHERE-IT-FAILS case 3 makes it a named failure mode. Confirmed: **A5 is load-bearing at
Step 9, not decorative.**

### 3.4 The substantive finding

> **L2-R1 (REPAIR — the important one).** **A7's injective form is in tension with the card's weak
> `∂_s B_j ≥ 0`, and L2 is only as strong as A7-injective.**
>
> Because `Q^F = b_j*(s) − B^F`, the flagged tuple `(B^F, Q^F, a)` carries the same information as
> `(B_j^F, b_j*(s), a_j)`. Card §4.2 requires only **weak** monotonicity of `s ↦ B_j(s,d)`, and
> `b_j*(s) = B_j(s,H)` inherits that. So on any interval of signals where the path and the terminal
> target are both flat, two distinct `s` values produce an **identical** flagged tuple and injectivity
> fails there. Under the card as written, WHERE-IT-FAILS case 1 is therefore not a remote pathology —
> it is the generic case.
>
> Weakest repair that saves L2: strengthen §4.2 on the flagged set to **strict** monotonicity of
> `s ↦ (B_j^F, b_j^*)` for Voice plans, or index the plan menu so the tuple separates plans. Either
> is a hypothesis, and a named hypothesis is a result.
>
> Two consequences to carry:
> 1. **It locks with D1-R2.** Injective A7 *requires* `B^F` to be continuum-valued — an injective map
>    out of a continuum of signals cannot land in a finite set. D1 Step 8's pull toward finiteness and
>    L2 h.5's injectivity are the same fact seen from opposite ends, and the card must resolve it in
>    favour of the continuum.
> 2. **The economic substance of L2 has migrated into A7.** With `𝖲_F` pinning `(j,s)` exactly, the
>    conditional-independence step is nearly immediate — `s` is known, and A1 finishes it. L2 is a
>    clean and correct proof; what it proves is that *if* the flagged tuple is a sufficient statistic
>    for `(j,s)`, invariance follows. Whether A7-injective is **satisfiable** in the two-round model
>    is not addressed by any step, and L2 does not claim it is. This inherits turn-1 audit item **U3**:
>    draft_v2's analogous injectivity claim was itself a referee finding (M2). **Thread 2 must attack
>    A7's satisfiability, and a later turn should exhibit a plan menu on which injective A7 holds.**

> **L2-O1 (OBSERVATION).** Hypothesis 5 says the map is injective, "equivalently, the map has a
> measurable inverse on its image". These are not equivalent by fiat — injective + measurable ⟹
> measurable inverse is a *theorem* (Lusin–Souslin), available here because `{1,…,J}×ℝ` and the tuple
> space are standard Borel. Harmless, and in fact favourable: the hypothesis as written asks for no
> more than injectivity. State it that way so a referee does not read the second clause as an extra
> assumption.

---

## 4. Notation audit (Task 2)

Baselines: card §4; `draft_v2.tex` (grepped); turn-1 audit §(d) rulings, which remain binding.

| # | Proof-local symbol | Collision found | Ruling |
|---|---|---|---|
| P1 | `W := (v,s,ξ)` | **Three live meanings.** draft_v2: `W(κ) = W_min + W_B + W_bid` is **total surplus** (`:1170`), with `W_min`, `W_B`, `W_bid` across `:1131–1345`; and `W(s) = Λ(s) − C'(s)` is the D5 **wedge** (`:2710`). Card §4.4: `W_τ, W_T` are the **weight-effect ratios**. | **must-rename → `Ξ := (v,s,ξ)`.** `\Xi` has 0 hits in draft_v2 and none in the card. Mnemonic: it contains `ξ`. And extend the bare-symbol rule: **never a bare `W`** — the only admissible `W`s are `W_τ` and `W_T`. |
| P2 | `𝖲_F := (B^F,Q^F,a=1)` | `S̄` is baseline synergy — 12 occurrences in draft_v2 (`:300, 304, 320, 497`) and card §4.1. Distinguishers are sans-serif and the mandatory `F` subscript, which is weak on a page that also carries `𝒞_F`. | **tolerable-with-note.** Proof-local to L2. Rule: **never a bare `𝖲`**; the `F` subscript is mandatory; and it must be introduced once as *"the filing message `F` augmented by the flagged order `Q^F`"*, tying it to the card's existing `F = (B^F, a=1)`. |
| P3 | `𝓗^P` for `𝓗_{f^-}^P` | The card's `𝓗_d^P` is the general pooled history; a subscript-free `𝓗^P` reads as "any pooled history". | **tolerable-with-note.** Write the `f^-` subscript at first appearance in every proof; never use the shorthand for a generic pooled history. |
| P4 | `𝐳^H = (z_0,…,z_H)` | Superscripts in the card are **regime** labels (`P` pooled, `F` flagged, `P_d^P`, `B^F`, `Q^F`), so `𝐳^H` reads as "noise in regime H". | **tolerable-with-note.** Prefer `z_{0:H}`. No hard collision — `\bar z` and `z_d` are card symbols and draft_v2 has neither. |
| P5 | `ι_F` | `\iota` has **0 hits** in draft_v2 and none in the card. | **fine.** |
| P6 | `G_{j,s}` (noise → pooled history) | **Heavy.** draft_v2's `G_{EH}, G_{HQ}, G_{QP}` are the **adjacent-action payoff gaps** (`:2690–2730`) — precisely the objects P1's existence proof will need; `G` is also D7's bargaining surplus in `N(x) = x^θ(G−x)^{1−θ}` (`:2523`) and the sign object at `:1688`. | **must-rename → `Υ_{j,s}`.** `\Upsilon` has 0 hits in draft_v2 and none in the card. (`Λ`, `Ψ`, `Φ`, `Θ`, `Π`, `Σ` are all taken; `g` is reserved for L3's mean-value form per msg 2 §1.1.) |
| P7 | `u_1, u_2` (bounded test functions) | draft_v2's `U(q*,a*|s)` is the blockholder's utility (`:1163`). Subscripted lowercase is distinguishable, and these never leave Step 4. | **tolerable-with-note.** Strictly proof-local; **never a bare `u`**. |
| P8 | `𝖹` (generic scalar in the check request) | `z_d` / `z̄` are the card's noise mark and its size. A capital `𝖹` next to them invites a misread, for a symbol that is a placeholder in one numerical request and appears in no proof. | **must-rename → drop it.** Write "each object listed above" in the check request. One fewer symbol. |

Turn-1's four must-rename rulings (`ψ→Γ`, bare `ω→ω_a`, `a_κ→A'_κ`, delete `σ_κ`) were all obeyed:
the turn-2 answer uses none of the retired symbols. Bare `λ` does not appear. `κ` is noise-trading
intensity throughout, with no drift toward depth, volume or turnover.

---

## 5. Counts and what moves

**FAIL 0 · REPAIR 8 (D1-R1/R2/R3, L1-R1, L2-R1/R2/R3/R4) · OBSERVATION 4 (D1-O1, L1-O1, L2-O1,
L2-O2).**
Banned-word hits **0**. draft_v2/external citation hits **0**. Unused hypotheses **0**. Bare steps
**0**. Claim-vs-card: **three refinements, zero drift.**

**Nothing blocks.** No step failed, so the one-retry rule does not fire and no proof is bounced. Every
repair is either a card fact that exists but is uncited, or a card convention that must be added
(`P_{−1}^P`, strict monotonicity on the flagged set, `b_0 < τ`).

**No label moves.** Per the protocol, PROVED needs independent re-derivation PASS **plus** Opus
proof-read PASS. This audit is the second half only. **D1, L1 and L2 remain CONJECTURE**, each with
"proof on file; Opus proof-read PASS 2026-08-20; awaiting Thread 2 re-derivation" recorded in the
ledger. The single largest risk carried forward is **L2-R1** — if A7-injective is not satisfiable in
the two-round model, L2 is correct but vacuous.
