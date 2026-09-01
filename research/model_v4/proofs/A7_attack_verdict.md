# Adversarial attack on `A7_construction.md` — verdict (ticket 24, Opus attack half)

Attacker: fresh Opus subagent, theory lane, 2026-08-21, repo `blockholder_v4_theory` @ branch
`v4-theory` (no git run). Target: `research/model_v4/proofs/A7_construction.md`.
Context read: `MODEL_CARD.md` (stamp 2026-08-20 · `0c9185b`, in full),
`threads/thread1_turn2_audit.md` (in full), `threads/thread1_msg3.md` §1,
`threads/thread1_turn2_answer.md` L2 block (lines 236–477, to check what L2 actually consumes).
No other file in `proofs/` was opened.

Stance: refute. Three outcomes only — **WRONG** (a card row, an audit finding, or an executed check
contradicts it) · **MISCITED** (claim stands, citation does not) · **UNCHECKED** (could not check).
Everything not listed under one of those survived the attack.

Executed check: `a7_check.py` (scratchpad), exact rational arithmetic, rebuilt from the **card**
definitions (`c = inf{d : B_V(s,d) ≥ τ}` by brute-force search over the calendar, `f = c+T`,
`B^F = B_V(s,f)`, `Q^F = b^*−B^F`) — not from the construction's closed forms. Output verbatim in §3.

---

## 1. Verdict table

| # | Claim / step | Verdict | Evidence |
|---|---|---|---|
| C-i | Tuple equivalence; sum reveals the terminal target | **survives** | `Q^F = b^*−B^F` is card §4.2's definition; the shear map is a linear bijection of ℝ². Executed check 4: `max|(B^F+Q^F)−b^*| = 0` exactly over 17,501 flagged grid points. Identical to audit L2-R1's own observation — correctly attributed to §4.2, not over-claimed. |
| C-ii | A7′ ⟹ on-path injectivity + explicit inverse + A7's identification clause | **survives, 4 repairs** | Injectivity argument is valid (Step 3). Repairs R1–R4 below: missing `Ω>0`; the "no Lusin–Souslin needed" boast; conditional-independence asserted from an unconditional statement; "Borel" cited to hypotheses that give dependence, not measurability. |
| C-iii-a | The pro-rata menu satisfies A7′ | **survives** | Check 5: A7′ holds on the flagged set of the menu (`True`); Step 7's derivation (only Voice flags ⟹ `b° = b^*`) is correct given Step 5's `b_0 < τ`. |
| C-iii-b | "…and is **conformant with every card §4.2 row**" | **WRONG** | The strict-pair patch *is* a card §4.2 row (`B_j(s,d)` row: "On the flagged set, `s↦(B_j^F,b_j^*)` must be **strictly** increasing for Voice"). CLAIM (iv) of the same file says the menu **violates** it, and executed check 5 confirms the violation (`patch: False`). CLAIM (iii) and CLAIM (iv) contradict each other as written. Repair: "conformant with every card §4.2 row **except** the strict-pair patch sentence, whose replacement is CLAIM (iv)". |
| C-iii-c | "A7 … is satisfiable — the stack's largest open risk is closed" | **survives with a repair (R5)** | True for the **on-path** form, which is what L2 consumes (verified against `thread1_turn2_answer.md` Steps 1–12: every use of `ι_F` sits inside a conditional expectation under the equilibrium law, so only on-path tuples are non-null). But the card's A7 *as written* is the joint form `(j,s)↦(B_j^F,Q_j^F,a_j)` injective on the flagged set, and **the construction's own menu fails it** — executed check 6: 41 signals below the Voice cutoff whose Voice-plan history would flag collapse to **1** distinct tuple, 40 collisions. Free fix: require `b^*` strictly increasing on **all of ℝ**, not only on `[k_{J−1},∞)`. |
| C-iv-a | The pro-rata menu violates the §4.2 strict-pair patch (numeric witness) | **survives** | Check 1 reproduces the table exactly in rationals; check 3 finds **7** strict downward steps of `B^F` across the flagged region; check 5: patch `False`, A7′ `True`. |
| C-iv-b | "the replacement is a strict weakening that all previously conformant menus survive" (Step 9, last sentence) | **WRONG** | Contradicted by the file's own WHERE-IT-FAILS case 3: a two-Voice-plan menu with `b^*_{j'}(k^+) < b^*_j(k^-)` satisfies the per-plan patch and violates A7′. So patch ⇏ A7′, and (by the witness) A7′ ⇏ patch: the two conditions are **non-nested**, not ordered. The replacement is still the right edit — A7′ is the condition L2 needs — but it is a substitution, not a weakening, and a menu conformant under the patch can fail under A7′. |
| S-1 | Step 1 — linear bijection, same σ-field | survives | Bimeasurable bijection of ℝ²; `a` carried unchanged. |
| S-2 | Step 2 — flagged region is a Voice region | **MISCITED** | `D_j = 1{a_j=1, c<∞, f≤H}` forces `a=1` from its **own definition** (card §4.2 `D_j` row: "`D=1 ⇒ a=1`"). Hypothesis 4 (A4's "only Voice plans cross") is not needed for this and is cited anyway. Harmless; drop the A4 citation or cite the `D_j` row. |
| S-3 | Step 3 — A7′ ⟹ injectivity, explicit inverse | survives, repair R2 | Injectivity is right. "A strictly increasing function on a Borel subset of ℝ has a strictly increasing inverse on its image, and a monotone function is Borel" is correct as a *subspace*-measurability statement; what is not free is that the **image** is Borel in ℝ, which for a general Borel `S_fl` is exactly Lusin–Souslin. The boast "No appeal to Lusin–Souslin is needed" is safe only in the continuous case the menu supplies (`S_fl` an interval, `b°` continuous ⟹ image an interval) or if the inverse is only claimed a.e. under the flagged law. Say which. |
| S-4 | Step 4 — σ-field logic and the identification clause | survives, repairs R1/R3/R4 | The chain `σ(𝖲_F, 1{D=1}) ⊆ σ(s) ⊆ σ(v,s,ξ)` and A1 ⟹ `z ⊥ σ(𝖲_F,1{D=1})` is correct. "The market knows the policy functions" is **not** smuggled: card §3(iii) makes on-path beliefs Bayes-consistent with the strategy profile, and L2's own h.6 fixes the policies exogenously — this is the ordinary sufficient-statistic construction the audit already cleared (audit §3.2, "no circularity"). Three defects, all one-line: **(R1)** the step conditions on `{D=1}` with no `Ω>0` / A8 hypothesis, while Step 6 concedes `S_fl` may be empty — this is L2's h.7 and audit L2-R3, and it is missing from the hypothesis list. **(R3)** what L2 consumes is `𝓗^P ⊥ (v,s,ξ) | 𝖲_F`; the displayed logic delivers only `z ⊥ σ(𝖲_F,1{D=1})`, and the conditional statement is asserted in words. Add: A1 gives `z ⊥ (v,s,ξ)` jointly and `𝖲_F ∈ σ(s)`, so `z ⊥ (Ξ, 𝖲_F, 1{D=1})` jointly, whence the conditional independence. **(R4)** "the tuple `𝖲_F` is a **Borel** function of `s`" is cited to hypotheses 2 and 5, which give functional *dependence* on `(j,s,τ,T)`, not measurability; measurability comes from §4.2's monotonicity plus D1's Step-8 line (`B_j(s,f_j(s)) = Σ_d 1{f_j(s)=d+T}·B_j(s,d)`, audit D1-R2). |
| S-5 | Step 5 — the menu and its row-by-row card conformity | survives, repairs R6/R7 | Bounds, `B_j(s,−1)=b_0` for all three plans, Exit weakly decreasing, Hold constant, Voice `∂_dB ≥ 0`, `∂_sB ≥ 0`, A2 finiteness, ordering by terminal stake (`0 < b_0 < b^*(s)`), and A4's "only Voice crosses" **derived** from `b_0 < τ` — all check out against card §4.2. `b^* < b̄` strictly is *consistent* with the card's `b^*∈[0,b̄]` (a sub-interval), and is in fact forced by strict monotonicity on an unbounded Voice region. **(R7)** the conformity sweep omits the two comparative-static rows: `B_j^F` row (`T'<T ⇒ B^F(T') ≤ B^F(T)`) and `Q_j^F` row (`T'<T ⇒ Q^F(T') ≥ Q^F(T)`). I checked both: `c` is `T`-free and `sh` is weakly increasing, so both hold on the menu — no error, but the sweep claims completeness it does not have. **(R6)** see below — the menu is defined against `[k_{J−1},∞)`, a policy object. |
| S-6 | Step 6 — crossing and flag structure | survives, nit | `c(s) = min{d : sh(d) ≥ (τ−b_0)/(b^*(s)−b_0)}` divides by `y = b^*(s)−b_0` without noting `y>0` (true on the Voice region by Step 5) and writes `min` without the empty-set case (`c=+∞`). The flag condition matches D1's clock equivalence: `y·sh(H−T) ≥ τ−b_0 ⟺ c ≤ H−T`. "Every flagged target satisfies `b^* ≥ τ`" is correct (`sh ≤ 1`). Executed check 3: smallest flagged `y` on the grid is exactly 1.25, as Step 6 predicts. |
| S-7 | Step 7 — A7′ holds on the menu | survives | Follows from Steps 2, 5, 6. |
| S-8 | Step 8 — necessity of A7′ "within the pro-rata family" | survives for a **single-Voice** menu; **MISCITED** as stated | I could not build a counterexample inside the Step-5 menu: the entire Voice path is `b_0 + y·sh(d)`, so `c`, `B^F` and `Q^F` depend on `s` **only** through `y = b^*(s)−b_0`; equal `b^*` ⟹ identical tuple ⟹ the "iff" holds. But the word **family** is load-bearing and wrong: enlarge the family to two Voice plans (different schedules or targets) and necessity fails — the file's own WHERE-IT-FAILS case 3 says the tuple can separate a pair on which `b°` repeats. Restate as "within any single-Voice menu of the Step-5 form", which is what the body actually proves. |
| S-9 | Step 9 — the witness table and the down-jump | **arithmetic survives, exact** | Recomputed from the definitions, not the closed forms: `y=2.4 → c=4, sh(6)=0.7, B^F−b_0=1.68, Q^F=0.72, sum=12/5`; `y=2.6 → c=3, sh(5)=0.6, B^F−b_0=1.56, Q^F=1.04, sum=13/5`. Flag threshold `(τ−b_0)/sh(7) = 1.25`, both flagged; `f = 6, 5 ≤ 9`, both file in time. The closed form `c = ⌈10/y⌉−1` matches brute force at **4000/4000** grid points. `B^F` falls while `b^*` rises: confirmed. `Q^F ≡ 0` on the `c+T=H` interval: confirmed. 7 strict downward steps of `B^F` across the flagged region. Only the final sentence fails (C-iv-b above). |
| S-10 | Step 10 — continuum-valued `B^F`, A5 selection | survives, **MISCITED** + repair R8 | The menu-specific argument is right (`B^F−b_0 = y·sh(c+T)` with `sh(c+T)>0` fixed on each `c`-interval and `y` ranging over an interval). But the cited justification — "an injective map out of a continuum of signals cannot land in a finite set", audit D1-R2 / L2-R1 — proves only that the **tuple** is continuum-valued, not the `B^F` coordinate: on this very menu `Q^F ≡ 0` on the lowest `c`-interval (executed check 4), so the coordinates trade the burden. The same over-reach sits in the card's A7 note ("Injectivity … forces `B^F` continuum-valued"); the true statement is "forces `(B^F,Q^F)` continuum-valued". **(R8)** "the selected pricing fixed points can be chosen continuous in `s`": A5 gives *uniqueness*, so nothing is "chosen", and A5's continuity is in *beliefs, cutoffs and parameters*, not in the flagged-tuple index. Continuity in `s` is an extra property, asserted where it must be argued (card §8 rule 7). |
| W-1..4 | WHERE IT FAILS cases 1–4 | all genuine | Cap binding (the card does allow `b^*=b̄`), quantized stakes, multi-Voice backtracking, feedback execution (correctly identified as upstream, audit L2-R2's territory). Case 3 is the one that kills Step 9's last sentence. |
| W-miss | Missing failure cases | **4 a referee would find** | See §4. |
| Mech | Mechanical scan | 1 banned word | `trivially` at line 231 (WHERE IT FAILS case 2, not inside a numbered proof step). The audit's own scan standard was "0 hits across the whole answer". Zero `\ref`/`\cite`/lemma-number hits; no bare `W`, `λ`, `ψ`, or bare `𝖲`; all eight template headings present; all six hypotheses used. |

---

## 2. Repairs, in the order they should be applied

**R-A (blocking the CLAIM block as written).** CLAIM (iii) must not say "conformant with every card
§4.2 row" while CLAIM (iv) says the menu violates a §4.2 row. Write: "conformant with every card
§4.2 row except the strict-pair patch sentence, whose replacement is CLAIM (iv)."

**R-B (blocking Step 9's last sentence).** Delete "so the replacement is a strict weakening that all
previously conformant menus survive." Replace with: "The two conditions are non-nested — the patch
does not imply A7′ once the menu carries two or more Voice plans (WHERE IT FAILS case 3), and A7′
does not imply the patch (Step 9's witness). A7′ is the condition L2 consumes; the patch is neither
necessary nor sufficient for it."

**R1.** Add `Ω = Pr(D=1) > 0` (A8) as a numbered hypothesis and cite it at Step 4. Step 6 concedes
`S_fl` may be empty; L2 carries this as its h.7 and audit L2-R3 already flagged the identical gap.

**R2.** Step 3: qualify "No appeal to Lusin–Souslin is needed" — it is free when `b°` is continuous
and `S_fl` is an interval (the menu's case), or when the inverse is claimed only a.e. under the
flagged law. For a general Borel `S_fl`, Borel-ness of the *image* is exactly the Lusin–Souslin
content.

**R3.** Step 4: display the conditional-independence line (`A1` ⟹ `z ⊥ (Ξ, 𝖲_F, 1{D=1})` jointly ⟹
`𝓗^P ⊥ Ξ | 𝖲_F`), which is the clause L2 Step 4 consumes. As written the step asserts the
conditional statement from an unconditional one.

**R4.** Step 4: cite §4.2 monotonicity + D1's Step-8 measurability line for "Borel", not hypotheses
2 and 5.

**R5 (substantive — this one changes the menu).** Take `b^*` strictly increasing on **all of ℝ**,
not only on `[k_{J−1},∞)`. Cost: nothing — it is compatible with every §4.2 row (`b^*` enters only
the Voice plan's path; Exit's terminal target stays 0, Hold's stays `b_0`). Gain: two things at
once. (a) The card's A7 as literally written — `(j,s) ↦ (B_j^F,Q_j^F,a_j)` injective on the flagged
set `{(j,s) : D_j(s)=1}`, which contains off-path pairs since `D_j` is defined for every `(j,s)` —
then holds on the menu, because only Voice ever flags and `b^*` separates every signal. Without it
the menu fails the card's own A7: executed check 6, 40 collisions. (b) It removes R6.

**R6 (substantive — order of quantifiers, matters for P1).** Step 5 defines the menu against "the
Voice region `[k_{J−1},∞)`" — but the menu is a **primitive** and `k_{J−1}` is a policy/equilibrium
object. As written, the menu is tailored to the policy it is supposed to support; and P1's Brouwer
argument needs the hypothesis to hold at **every** candidate `k ∈ Θ`, not only at the fixed point.
R5's global strict monotonicity severs the dependence. Correspondingly, the proposed §4.2 card edit
("the composed terminal target `s ↦ b^*_{j(s)}(s)` must be strictly increasing") places a
policy-dependent condition in a row that restricts primitives — it must be quantified: "for every
cutoff vector `k ∈ Θ`", which for a menu amounts to each `b^*_j` strictly increasing **and** no
backtracking of `b^*_j` across any admissible plan switch.

**R7.** Step 5: add the two omitted §4.2 comparative-static rows to the conformity sweep (both hold;
verified here).

**R8.** Step 10: drop "can be chosen" (A5 gives uniqueness) and either argue continuity of `P^F` in
`s` or state it as an open regularity point. A5 as cited does not deliver continuity in the
flagged-tuple index.

**R9 (card-edit text, CLAIM iv).** The proposed §5 A7 note should read "the **on-path** injective
form (fixed cutoff policy, tuples of positive-probability histories)", and should record that the
card's stronger joint `(j,s)` form additionally needs `b^*` strictly increasing off the Voice region
(R5). Its failure-boundary list should gain `Ω = 0` and the policy-dependence of R6.

**Answering the ticket's target 6 directly — does replacing the patch with A7′ break anything D1's
or L2's proofs use?** No. Per the audit's step descriptions and the L2 text: D1 Steps 1–5 use only
weak `∂_dB_j ≥ 0` / `∂_sB_j ≥ 0` and finiteness of the calendar; D1 Step 7's product formula uses
A4; D1 Steps 8/11 use measurability and the `P_{−1}^P` convention. None of them touches the
strict-pair patch. L2 uses A7 only through `ι_F` inside conditional expectations under the
equilibrium law (Steps 1, 3, 4, 8), so it needs **on-path** recovery only, and null-set hedging
covers the rest — A7′ supplies exactly that. The one thing the patch supplies and A7′ does not is
strictness of the `B^F` coordinate, which no step in D1, L1 or L2 uses.

---

## 3. Executed check — verbatim output

Script: `/private/tmp/claude-501/-Users-austinli-Projects-blockholder-v4/d06ccee3-762c-4331-a587-d3581e6a875e/scratchpad/a7_check.py`
(exact `fractions.Fraction` arithmetic; `c` obtained by brute-force search over the calendar from the
card's `c_j = inf{d : B_j(s,d) ≥ τ}`, never from the file's closed form; `b_0` normalised to 0 so
`y = b^*`, `τ = 1`).

```
==========================================================================
CHECK 1 - Step 9 witness table recomputed from the definitions
==========================================================================
  y=b*-b0   c  sh(c+T)    B^F-b0     Q^F    sum  f<=H  flag closed-form c
   2.4000   4   0.7000    1.6800  0.7200 2.4000  True  True             4
   2.6000   3   0.6000    1.5600  1.0400 2.6000  True  True             3
sh(H-T)=sh(7) = 0.8, flag threshold (tau-b0)/sh(7) = 1.25
exact sums: 12/5 13/5
B^F falls while b* rises: True

==========================================================================
CHECK 2 - closed form c = ceil(10/y)-1 against brute force, y in (0,10]
==========================================================================
grid points tested: 4000   mismatches: 0   []

==========================================================================
CHECK 3 - flagged region structure, down-jumps of B^F, monotonicity of b*
==========================================================================
  down-jump at y=1.4290: B^F 1.4285 -> 1.2861  (c 7 -> 6), b* rose 1.4285 -> 1.4290
  down-jump at y=1.6670: B^F 1.4998 -> 1.3336  (c 6 -> 5), b* rose 1.6665 -> 1.6670
  down-jump at y=2.0000: B^F 1.5996 -> 1.4000  (c 5 -> 4), b* rose 1.9995 -> 2.0000
  down-jump at y=2.5000: B^F 1.7496 -> 1.5000  (c 4 -> 3), b* rose 2.4995 -> 2.5000
  flagged y-grid points: 17501   distinct c values: [0, 1, 2, 3, 4, 5, 6, 7]
  B^F strictly-down steps: 7   up steps: 17493
  smallest flagged y on grid: 1.2500 (Step 6 predicts 1.25)

==========================================================================
CHECK 4 - sum recovery and injectivity on the flagged grid
==========================================================================
  max |(B^F+Q^F) - b*| over flagged grid: 0  (exact rationals)
  duplicate (B^F,Q^F) tuples at distinct signals: 0
  Q^F == 0 identically on the lowest c-interval (c+T=H)? True

==========================================================================
CHECK 5 - componentwise patch vs A7': which holds on the menu
==========================================================================
  card 4.2 patch (B^F strictly increasing on flagged set): False
  A7' (composed target b* strictly increasing on flagged set): True

==========================================================================
CHECK 6 - menu-level A7 (card wording: (j,s) injective on the flagged set)
        b* weakly increasing everywhere, strictly only on the Voice region
==========================================================================
  signals below the Voice cutoff whose Voice-plan history WOULD flag: 41
  distinct flagged tuples they produce: 1   collisions: 40
  -> menu-level (j,s) injectivity on the flagged set: FAILS
     (A7' still holds: the fixed policy never selects Voice there.)
```

Check 6's `b^*` is a legal Step-5 instance: continuous, weakly increasing on ℝ, strictly increasing
on the Voice region `[1,∞)`, image in `[b_0,b̄)`, `b^*>b_0` on the Voice region — flat at 3.0 below
the cutoff, which Step 5 permits. Since `D_j(s;τ,T)` is defined for every `(j,s)` pair (card §4.2),
those off-path Voice pairs are in the card's flagged set, and the map collapses them.

---

## 4. Failure cases the file is missing (target 7)

The four listed cases are all genuine. Four more a referee will find:

5. **Empty flagged region / `Ω = 0`.** Step 6 concedes `S_fl` may be empty and calls A7′ vacuous
   there — but Step 4 conditions on `{D=1}` regardless. L2 carries this as its own WHERE-IT-FAILS
   case 6 and as h.7. It belongs here, not in a parenthesis.
6. **The card's joint `(j,s)` form fails on this very menu** (executed check 6) whenever `b^*` is
   flat off the Voice region. Currently only hinted at in NOT CLAIMED; it is a failure case, and R5
   is its one-line fix.
7. **The menu is defined against the policy it must support** (R6). A hypothesis stated on
   `b^*_{j(s)}` cannot be checked before the equilibrium is solved, and P1's Brouwer argument needs
   it on all of `Θ`.
8. **The economic one, and the one a referee will press hardest.** Every A7′-satisfying menu is
   *fully separating*: the filing reveals `s` exactly. The construction shows such a menu **exists**;
   it does not show that a blockholder who dislikes revealing `s` before the bidder moves would
   choose the plan carrying it, nor that A3's single crossing survives on it. The file is honest —
   NOT CLAIMED defers this to P1 — but CLAIM (iii)'s "the stack's largest open risk … is closed"
   should read "…is relocated from A7 to P1": what has been closed is *existence of a qualifying
   menu*, and what remains open is *whether an equilibrium on such a menu exists*. This is the
   audit's L2-R1 consequence 2 ("the economic substance of L2 has migrated into A7") one step
   further along.

---

## 5. Overall verdict

**SURVIVES WITH REPAIRS.**

Nothing in the construction is mathematically refuted. The Step 9 arithmetic is exact — every number
in the witness table reproduces from the card definitions under brute-force crossing search, and the
closed form `c = ⌈10/y⌉−1` matches at 4000/4000 grid points. Step 8's necessity holds inside the
single-Voice menu and I could not break it there. Step 3's injectivity and Step 4's σ-field logic are
sound, and "the market knows the policy functions" is a legitimate on-path PBE step, not a smuggled
assumption. Target 4 confirmed against the L2 text itself: L2 consumes only on-path recovery.

Two **WRONG**s, both wording-level contradictions inside the file, both repairable without touching
the mathematics:
- **C-iii-b** — "conformant with every card §4.2 row" contradicts CLAIM (iv) (the strict-pair patch
  is a §4.2 row and the menu violates it; check 5).
- **C-iv-b** — "the replacement is a strict weakening that all previously conformant menus survive"
  contradicts the file's own WHERE-IT-FAILS case 3; the two conditions are non-nested.

Repairs required before the CLAIM (iv) card edits are applied: **R-A, R-B, R1, R5, R6, R9**
(substantive) and **R2, R3, R4, R7, R8** (one-line). The two card edits themselves are endorsed in
substance — the strict-pair patch is over-strong relative to its own stated rationale (injectivity
fails only if **both** tuple coordinates are flat, not if `B^F` is non-monotone) and A7′ is the
condition L2 actually consumes — but the §4.2 replacement text must be quantified over policies
(R6) and the §5 note must say **on-path** (R9).

No label moves. A7 remains a standing hypothesis; this file remains a construction awaiting the
ticket-27 proof-read.
