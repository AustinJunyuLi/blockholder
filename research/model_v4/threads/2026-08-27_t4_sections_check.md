# T4 — independent check of `sections_v3/` against MODEL_CARD.md

**Role.** Independent checker for ticket 08 (T4). I wrote none of the files checked. My only write
is this file; nothing under `sections_v3/` or `research/` was edited, and I ran no git command.

**Date.** 2026-08-27.

**Stamps verified before checking.**

- `research/model_v4/MODEL_CARD.md` — header line 3: *"Version stamp: 2026-08-27 · A6 panel
  resolution (§5 A6/A3 evidence notes + §9 item 4) · commit `ae9caea`"*. **Matches the contract.**
- `research/model_v4/model_v4.md` line 12 and `model_v4.tex` line 68 — both carry *"version stamp
  2026-08-27, A6 panel resolution, commit `ae9caea`"*. **Note regenerated to the card stamp.**
- Five of the six section files carry the same stamp in their headers. The sixth,
  `proofs_section.tex`, is a seven-line plumbing file (`\section{Proofs}`, `sec:proofs`, three
  `\input` lines) with no header block — correctly, since it states nothing.
- `sections_v3/v3_macros.tex` header cites a **stale** stamp — see finding **M-10**.

**Objects checked.** `sections_v3/model_section.tex`, `theorem_section.tex`, `proofs_section.tex`,
`proofs_core_lemmas.tex`, `proofs_existence.tex`, `proofs_theorem_ge.tex`, plus `v3_macros.tex` and
`standalone_v3.tex` as build plumbing.

**Binding inputs.** `MODEL_CARD.md` (wins over the note wherever they differ), `model_v4.tex`/`.md`,
`CONTEXT.md`, the fidelity contract, and — as *claims* rather than evidence — the writers'
`crosswalk_model_theorem.md` and `labels_map.md`.

**Source proofs read for the transcription-grain check.** `proofs/P1_proof.md` (Step 12 block and
the h.1–h.17 register), `proofs/L3_proof.md` (Steps 1–6, 14–19), `proofs/L4_proof.md`,
`proofs/T1_proof.md` (H17/H18 and the Step-15/16 material), `proofs/C1_proof.md` (H8),
`rederive/C1_rederivation.md` (H8 verdict), `threads/thread1_turn2_answer.md` (referenced for D1/L1/L2
provenance only).

**Grain.** Statement fidelity at full grain (every clause of every card §6 row, plus §1–§5 and §9
material carried into the model section). Proof fidelity at transcription grain, with deep samples at
P1 Step 12, the L3 chord steps, T1 Step 16's quantifier, and C1's norm-convention preamble.

**Coverage.** I read all six section files end to end, plus `v3_macros.tex`, `standalone_v3.tex` and
`sections_v3.bib` in full. No stretch of any proof file is vouched for unread.

---

## 0. Verdict vocabulary as applied

- **WRONG** — substance mismatch (dropped or weakened clause, wrong number, invented claim, label or
  conditionality deviation). Blocks landing. **Count: 0.**
- **MISCITED** — a pointer, attribution or provenance is off; substance intact. Never blocks.
- **UNCHECKED** — could not verify. Never blocks.
- **OK-RESTRUCTURED** — deliberate paper-form restructuring that preserves substance; listed so the
  record is complete.

Two things are reported outside the four classes, in §3: a build-plumbing risk that is not a
difference from the card, and the correction to item 13's premise.

---

## 1. Findings by file

### 1.1 `sections_v3/model_section.tex`

---

**M-1 · `asm:TR`, lines 176–209 · OK-RESTRUCTURED**

The card carries the primitive restrictions as sign-restriction columns across three tables (§4.1,
§4.2, §4.3). The section gathers them into one `assumption` environment with clauses (TR-i)–(TR-iv).
A table has no citable target and three results cite the block wholesale, so the restructuring is
declared and reasoned at crosswalk §0 row 25. I walked all four clauses against the three card
tables: every sign restriction, the `b_0 < \tau` maintained restriction, the Borel-for-Exit addition,
the continuum-valued stake-level note, the legal-clock objects with the `T' < T` monotonicities, and
the pricing/entry conventions are present and unreworded.

---

**M-2 · `rem:A3record`, lines 265–291 · MISCITED (pointers only)**

Substance is complete against card §5's A3 evidence note. I verified every number: the three sign
changes at `s = 1.5754434 / 1.5833333 / 1.5902426`; middle excursions `2.4`–`2.8e-4` against a
`1e-9` payoff tolerance; offsets `1e-9` through `2e-2`; the H,V,H,V argmax; "the selection set is
empty and the outer map $\Tmap$ is *undefined* there, not merely discontinuous"; the
`(κ=0.15, 0.05, 5)` VOICE→HOLD reversal across `s = 1.659062163` at both located fixed points; the
integer-valued `n(s)` route and the off-path price snap; the proxies-are-local-screens paragraph; the
candidate mechanical account with residuals `3.06e-4`–`1.77e-3` at `1e-11`-grade cutoff residuals,
"bracket the recorded range exactly"; the panellist's own recorded negative on the *k*-direction
mechanism; and "No label moves … A3 is a hypothesis, and Proposition~\ref{prop:P1} stays PROVED as a
conditional."

Card pointers dropped: "Step 15(i) / WHERE IT FAILS 4's card-legal counterexample, instantiated by
the solver's own `N_GRID` note", and the proxy script `t2_p1_fournode_recheck.py`.

**Verdict:** MISCITED. Non-blocking; the proof-file and implementation IDs are internal record
anchors and do not belong in paper prose. The A3 proxy script is, however, named nowhere in the
sections while every other record in the file is given as a `\texttt{}` string — an inconsistency
worth one line of the orchestrator's attention.

---

**M-3 · `rem:A6record`, lines 324–373 · MISCITED (pointers only)**

Substance is complete against card §5's A6 evidence note and against contract gate (c)'s enumerated
element list. Verified present: the continuity clause fails for the declared construction and the
locus is not the one first proposed; the locus is *cell-edge hyperplanes* ∪ *sole-generator collapse
faces*, "not the collapsed cutoff vectors as such"; the jump reaches `\Tmap` with weight at least
`min(κ/2, 1−κ)^{d+1}`, independent of the dying plan's population mass; the vanishing-mass defusal
refuted by both panellists independently; the tie-break is pointwise and passes the jump through; the
order-of-limits argument against a *k*-independent family; the `J ≥ 3` continuum-face lemma with
`μ_v + β(c − μ_v)` and "fails at every face point but at most one", explicitly **not gate-checked**;
the implemented menu excluded from that class with the Hold-collapse face measured clean at
`4.4e-16` and `\Tmap` bit-identical; the measured `\Tmap_2` jumps `6.33e-3 / 1.09e-2 / 2.83e-2` at
`≤ 2e-9` steps, independently measured to three significant figures, belief snap to `~1e-8`,
surviving-type controls `~3e-9`, robust at `1000×` the merge tolerance; `0.16` and the destroyed
diagonal crossing at `κ = 0.15`; `Θ⁺ = [1.23, 1.245] × [1.5253, 1.5506]` with all three caveats; "No
label moves and none is licensed"; P1 stays PROVED as a conditional "in the same pattern as
$\Atau$"; both repairs; the `1e-14` off-path floor as the shipped fixed-*t* constrained game with the
switch relocated by `~1e-9`; coverage (one node per claim class plus the 27-node census, not swept);
`23` of `27` converge and nonexistence neither claimed nor shown; both `threads/` panel files and the
probes directory named as `\texttt{}` strings, "analysis-grade and not curated executed checks".

Card pointers dropped: the constant name `OFF_PATH_EPS`; "Step 9(b)" as the source of the frontier
posterior; "Step 18" as the location of the *t*-constrained repair; the proof-local symbol `Λ_k`
(rendered as "the reaching weight").

**Verdict:** MISCITED. All four are internal anchors; Step 9(b) and Step 18 both exist in
`proofs_existence.tex` under the same numbers, so a reader can still find them.

---

**M-4 · `rem:AtauRecord`, lines 464–533 · MISCITED (two pointer losses) + OK-RESTRUCTURED**

This covers **checklist item 11**. Substance is complete: I verified every figure against card §5's
A(τ) evidence note — `4^{H+1} = 4,194,304`; 200 nodes over `κ ∈ {0.05,…,0.95}` × five frozen `τ`
percentiles × `T ∈ {1,2,5,10}` at frozen policies with `H = 10`; both gates (`0.0` exactly and
`1.7e-16`); the 20 degenerate nodes with `M_P = 0`, `C_h(0) = 0`, "holds vacuously and the node
decides nothing"; 180 non-degenerate nodes all failing; 23–767 atoms at 0 of 180; no mass at `π̄/2`
so `A_{1/2} ≡ 0`; `0.57%`–`91.8%` off-support with `13.9%` at the median node (`T=5`, median `τ`,
`κ=0.55`: 107 atoms, `A_0 = 0.768`, `A_1 = 0.093`); the `1e-3` coarsening leaving 6–332; the
floor-free law at most 51 atoms fewer; Hausdorff `0.4608` unchanged at mass `≥ 1e-6` against a
predicted `<1e-12` at 0 of 18 series; `π̄ = 1` to `1.5e-13` at 18 of 18 and the named-false
conjecture; `π̄ ∈ {0,1}` never interior so the small-`π̄` corollary has no instance; `A_0' = A_1'` at
0 of 180 with `|A_0' − A_1'| ∈ [0.041, 2.306]`, `A_0' ∈ [−2.146, 2.374]` against
`A_1' ∈ [−0.014, 0.429]`, both changing sign; `A_{1/2}' = −2A'_κ` recorded as **inherited**, exactly
`2|A_0'|`; the chord residual `0.0013`–`0.0717` (up to `7.17` premium pp) at 0 of 180 on the most
favourable of three kernel conventions, with recovered `|A'_κ| ∈ [0.042, 2.374]`, required
`[0.00023, 0.392]`, disjoint from `[0.997, 1.158]`; the (τ-i) diagnostic `0.085` and `0.018`
mass-weighted; "NUMERICAL-class *applicability* evidence at one calibration. No label moves, and none
is licensed"; L3, L4 leg 3 and T1 Part (B) staying PROVED as conditionals and saying nothing about
the implemented cell; the domain reading of the open question; the six-distinct-pooled-cells caveat
with its full explanation; and the script, JSON, 200 nodes, 920 enumerations, 1002 seconds and
`FAILS at calibration` verdict field.

**M-4a — the "(S1) and (S2)" pointer. MISCITED, and a real loss.**

- Card, §5 A(τ) note, support-half bullet, final sentence: *"This refutes L3 Step 18's (S1) and (S2)
  together at this calibration."*
- Section, lines 480–489: the bullet ends at *"…against a predicted `<10^{-12}`, at 0 of 18
  series."* The sentence is absent.

I checked whether the record link survives via the L3 proof, as the checklist asks. It does **not**.
The tex L3 proof (`proofs_core_lemmas.tex`:484–725) ends at Step 15; the source's Part IV — Steps 16
(Example A), 17 (Example B) and 18, where (S1)–(S2) are defined — is not transcribed as proof steps.
`grep -n "(S1)\|(S2)" sections_v3/*.tex` returns nothing. Examples A and B *are* carried, relocated
into the discussion after `asm:Atau` (model_section.tex:456–459), but the two named sufficient
conditions are carried nowhere.

Two consequences follow, and both are pointer-grade rather than substance-grade:

1. The measured failure is fully on the paper's record; what is lost is the named connection between
   that failure and the two conditions L3 identified as sufficient. A reader of the paper cannot
   recover the connection; a reader of the card can.
2. **Two in-paper sentences now point at content the paper does not contain.**
   `theorem_section.tex:127–129`: *"the discussion after Assumption~\ref{asm:Atau} … names the
   weakest sufficient conditions for the two-round case."* And `theorem_section.tex:446–448`, in
   `sec:not-claimed` item (1): *"…and names the weakest sufficient conditions for the two-round
   case."* The discussion after `asm:Atau` does the first three things those sentences claim (the
   bite is the support condition; a one-round market satisfies it; the no-disclosure structure does
   not) but names no sufficient conditions.

   **Minimal fix, either of:** add (S1)–(S2) to the `asm:Atau` discussion, or reword both sentences
   to *"…and names, on the record, the weakest sufficient conditions for the two-round case."*

*Related mechanism, reported once here rather than per-pointer:* because the tex L3 proof omits the
source's Steps 16–19, **every card pointer into L3's proof by step number has no in-paper anchor** —
"L3 Step 18" (§5 A(τ)) and "`proofs/L3_proof.md` Step 19" (§4.4's `π̄` row, the binding ruling).
This contrasts with P1, where `proofs_existence.tex` declares and delivers 1:1 step numbering with
`P1_proof.md` (Steps 1–20, verified), so every P1 audit citation resolves in the paper. The L3
material itself is not lost: Step 19's degeneracy argument is carried at
`proofs_core_lemmas.tex`:716–724 and again at `model_section.tex`:650–652.

**M-4b — `MIN_CELL_MASS`. MISCITED.**

- Card: *"the 50 `T=10` nodes sit at `Ω = 0.000681`, below `MIN_CELL_MASS` (`HANDOFF_sign.md`
  §8.1)."*
- Section, line 528–529: *"the fifty `T = 10` nodes sit at `Ω = 0.000681`, below the
  implementation's minimum cell mass."*

**Verdict:** MISCITED, and this one I judge *correct as paper prose*. `HANDOFF_sign.md` is an
internal inter-lane record and `MIN_CELL_MASS` an implementation constant; neither belongs in a
department-reviewer-facing section. The number and the comparison — the whole substance — survive.
No fix needed.

**M-4c–e — three further thinnings. MISCITED / OK-RESTRUCTURED.**

- "block 3's implied `[0.997, 1.158]`" → "the separately implied `[0.997, 1.158]`" (block reference
  dropped; the object and its gloss survive). MISCITED.
- "Example A's `|A'_κ| = 0.25`" → "a particular value of `|A'_κ|`" (Example A is a proof-file
  object). OK-RESTRUCTURED.
- "the two prior 'failures' remain misformulated tests; this is the first test that measures A(τ)'s
  own object" → carried in substance as *"Two gates pass first, so the object measured is the one
  Assumption~\ref{asm:Atau} is about"*; the repo-history half is dropped. OK-RESTRUCTURED.

---

**M-5 · `asm:Abr` and its trailing discussion, lines 535–579 · OK-RESTRUCTURED + MISCITED (pointers)**

This covers **checklist item 2**. I compared all five clauses word by word against the card's A(br)
block.

- **(br-i)** representation at both policies, with chord endpoints `π̄(τ)`, `π̄(τ')` and coefficients
  `A'_κ(τ)`, `A'_κ(τ')` — **verbatim in substance**.
- **(br-ii)** κ-localisation, the three support points and the kernel-as-function-of-the-posterior
  not moving with κ, `∂_κ M_P = Δ_m A'_κ C_h(π̄)` exactly with no composition-through-κ remainder,
  the "against the literal display this would restate (br-i)" caveat, the honest reading
  `h = π p(v̂,π)`, "repairs that ambiguity rather than adding a fourth independent restriction",
  "naming the same object as clause (τ-i)", and **"The trailing 'hence' is derivable, not assumed"**
  — all present.
- **(br-iii)** `|A'_κ(τ')| ≤ |A'_κ(τ)|` with the weakest sufficient form equality and the
  reclassification gloss — **verbatim**.
- **(br-iv)** `π̄` as the chord endpoint and **upper support point**, weakly increasing in
  `π̄_pr = P(a=1|D=0)`, *"the same function at `τ` and at `τ'`"*, identity branch excluded as
  degenerate — **verbatim in substance**.
- **(br-v)** `C_h(·)` and the kernel are the same functions of the posterior at both thresholds; the
  "two different functionals and the comparison is meaningless" consequence; `h = π p` with `p`
  priced off a cell whose composition the threshold moves, so "τ-invariance of `h` is real content,
  not bookkeeping" — **verbatim in substance**.

Post-block discussion (lines 568–579), against the card:

- "consumed by leg 3 of Lemma L4 and by Part (B) of Theorem T1, and by nothing else" ✔
- "(br-v) was independently required by three agents, one of whom confirmed that it is not implied by
  (br-i)--(br-iv)" ✔ (card: the T1 proof-reader, the L4 re-deriver as "(br-ii′)", and the T1
  re-deriver who confirmed both required and not implied)
- the ρ sharpening: `ρ := ½A_{1/2} + A_1` provably κ-free, `π̄ = π̄_pr/ρ`, so (br-iv) ⟺
  `ρ(τ')/ρ(τ) ≥ π̄_pr(τ')/π̄_pr(τ)` ✔
- level-symmetric inheritance: `ρ = ½` and `π̄ = 2π̄_pr`, "which forces `π̄_pr ≤ 1/2`, an inherited
  restriction on the domain of Assumption A(τ) that Lemma L4 does not resolve" ✔
- "(br-iii) is the clause with the least justification behind it, and it is the one to attack first"
  ✔

Dropped: *"Canonical name is (br-v); T1's proof carries it as H17"*, and the `rederive/` CHANGE
pointers. **MISCITED**, non-blocking — H17 is a proof-file hypothesis number, and (br-v) is consumed
by name at `proofs_theorem_ge.tex`:208.

Added by the section (not in the card's A(br) block), line 577–579: *"Because (br-i) carries the
representation \eqref{eq:atau} at both thresholds, the record in Remark~\ref{rem:AtauRecord} bears
directly on Assumption~\ref{asm:Abr} as well."* This is an inference the card licenses elsewhere (the
T1 row's (T-11), and the A(τ) note's statement that L4 leg 3 and T1 Part B inherit the
conditionality). It tightens the honesty record rather than loosening it. **OK-RESTRUCTURED.**

---

**M-6 · `def:premium`, lines 618–652 · OK-RESTRUCTURED + one MISCITED**

This is half of **checklist item 9**. Verified against card §4.4: `h = π p` with `h ≥ 0`, `h(0)=0`;
`Δ^act = Δ_m E[h(I_H)] ≥ 0`; `M_F`/`M_P` "each defined when its cell has mass";
`Ω = P(D=1) ∈ [0,1]` factoring as `P(a=1) ω_a`; `ω_a = P(D=1|a=1)` the disclosed share of
engagements; **`π̄` as the upper support point of the pooled engagement posterior in the
representation \eqref{eq:atau}** — the corrected gloss, carried exactly; the mean-vs-`π̄` block
(the share is the *mean*, κ-invariant as a mean-preserving spread, so not the quantity whose
κ-motion L3 describes; strictly below `π̄` in any non-degenerate case; equals `π̄/2` only under
level symmetry `A_0 = A_1`); `S = |∂_κ Δ^act|`, `S_P = |∂_κ M_P|`; the chord display maintained
non-positive with `|C_h|` weakly increasing; `A'_κ` bounded on `[0,1]`; `W_τ`/`W_T` with the worked
`W_T` example, at most 1 when `Ω` rises; `C_τ`/`C_T` with the worked `C_T` example, unsigned; and
the margin-subscript rule with the full `C`-overloading list (`C_h`, `C_j(s)`, `C_F`/`C_P`). The
degeneracy of the mean-reading — point mass at `π̄` with `A'_κ = 0` and zero interior motion for
every kernel, "degenerate, and it is excluded throughout" — is carried in the paragraph immediately
after, lines 650–652. **The π̄ upper-support-point ruling and the mean-vs-π̄ degeneracy note are both
complete.**

Dropped and judged:

- `ω_a` "**the calibration target**" — a substantive descriptor of the object, dropped. Nothing in
  the sections consumes it, and no result depends on it. **MISCITED** (minor).
- "`Ω` is draft_v2's `ω_P` — the O-1 numbers … are all `Ω`-type"; "`ω_a` renamed from bare `ω`";
  "`C_h` = draft_v2's `C(π̄)`, `lem:d1-jensen`". Cross-draft notation mappings and rename history.
  The (C\*) half of the `C_h` row *is* relocated, to `asm:Atau` (line 434). The `Ω`-type
  identification survives implicitly, since `rem:T1record` writes the O-1 numbers as `Ω` values.
  **OK-RESTRUCTURED.**
- The martingale reason for `E[Π_κ] = π̄/2` under level symmetry. The claim is carried; the reason
  is not. **OK-RESTRUCTURED.**

---

**M-7 · `def:theta`, lines 591–616 · OK-RESTRUCTURED**

The other half of **item 9**. Verified against card §4.5: the cutoff vector with its ordering and the
frozen-manuscript mapping; `Θ` nonempty, compact, convex; `ϑ`; `\Tmap` as the outer cutoff
best-response map, **"always written calligraphically, since upright `T` is the filing window"**;
`L_R = sup_R ‖D_k \Tmap‖` required below 1 by AGE; `r_τ = −τ`, `r_T = −T`, higher `r` tighter;
`eq:gPE` with **"the sign written inline rather than carried by a symbol"**; `k̄_x` and `k̄_{κr}`;
`eq:BGE`; the dominance-and-contraction region `R_r` with slack `η_r = g_r^PE − B_r^GE` and **"the
region may be empty"**.

Dropped: the bare sign restrictions `≥ 0` on `k̄_x`/`k̄_{κr}`/`B_r^GE` (all are magnitudes of
magnitudes and non-negative by construction); "C1 needs `g_r^PE > B_r^GE`" (relocated to `prop:C1`
(C-6) ✔); "`η_r > 0` at dominance-and-contraction nodes" (relocated to `rem:C1record` ✔); draft_v2's
`(k_1, k_0, k_D)` names (replaced by "that draft's triple of cutoffs"). **OK-RESTRUCTURED.**

---

**M-8 · A7 satisfiability discussion, lines 400–417 · MISCITED (one scoping addition + pointers)**

This is **checklist item 8**, against card §5's A7 note (ticket 24). Verified present: satisfiability
resolved for A7′; A7′ + a fixed cutoff policy + `Ω > 0` deliver the on-path injective form on
positive-probability flagged tuples with an explicit inverse; **the pro-rata single-Voice menu with
terminal target strictly increasing on all of ℝ, which also satisfies A7-J**; A7-J additionally needs
`b*` strictly increasing off the Voice region, a target flat below the Voice cutoff breaking it in an
executed check producing **forty collisions** while leaving A7′ intact; the **failure boundary** in
full — a binding stake cap, quantized stakes, a composed target repeating values across Voice-plan
switches, `Ω = 0`, and policy dependence when the condition is stated only at one equilibrium's
cutoffs; and "Menus satisfying A7′ are fully separating on the flagged set, so the burden moves to
the incentive compatibility of Proposition P1, not away." The turn-2 proof-read note is also complete
(lines 381–383 and 403–406): the weak wording permits two `(j,s)` pairs with different pooled paths —
L2's first failure case; the tuple is continuum-valued as a tuple with coordinates able to trade the
burden; injectivity plus measurability already gives the measurable inverse on standard Borel spaces.

**The one difference:** the card states the failure-boundary list unscoped, immediately after the
A7-J sentence. The section writes *"The failure boundary **for the on-path form** is …"* (line 412).
Two of the five items (a binding stake cap, quantized stakes) break both forms, so the scoping
narrows what the card asserts about A7-J.

**Verdict: MISCITED** — an attribution narrowed, not a clause dropped. Nothing consumes the failure
boundary; A7-J's own additional requirement is stated separately and correctly two sentences earlier.
**Minimal fix:** delete "for the on-path form".

Also dropped: the adversarial attack verdict **SURVIVES WITH REPAIRS** and the
`proofs/A7_construction.md` / `proofs/A7_attack_verdict.md` pointers. **MISCITED**, non-blocking.

---

**M-9 · The eight displays · no difference**

**Checklist item 7.** Each checked symbol for symbol against the card's §4.1–§4.5 originals.

| Display | Line | Card source | Result |
|---|---|---|---|
| `eq:entry` | 126–130 | §4.3 `p(I)` row | identical, including the `∈ (0,1)` |
| `eq:Y` | 132–135 | §4.3 `B`, `Y` row | identical |
| `eq:Uj` | 155–159 | §4.3 `U_j` row | identical, `− a_j C_j(s)` term carried |
| `eq:m0` | 184–187 | §4.1 `m_0, m_1` row | identical, with the `m̄(I) ≥ 0` consequence and the nonexistence/three-root gloss |
| `eq:atau` | 428–431 | §5 A(τ) | identical |
| `eq:chord` | 637–640 | §4.4 `C_h` row | identical |
| `eq:gPE` | 601–604 | §4.5 `g_r^PE` row | identical |
| `eq:BGE` | 608–613 | §4.5 `B_r^GE` row | identical, all three groups |

---

**M-10 · `sections_v3/v3_macros.tex`, lines 2–3 · MISCITED (provenance)**

- File header: *"transcribed verbatim from `research/model_v4/model_v4.tex` **lines 28-37** (card
  stamp **2026-08-23**)."*
- Actual: the macro block is `model_v4.tex` **lines 42–51**; lines 28–37 are `\documentclass` and
  `\usepackage` lines. And `model_v4.tex` carries stamp **2026-08-27**, not 2026-08-23.

The macro *bodies* are correct: I diffed them against `model_v4.tex`:42–51 and all ten are identical,
the single deliberate change being `\providecommand` for `\Tmap` (documented in the same header, and
see **F-1**). `\Atau` expands to `\mathrm{A}(\tau)` and `\Abr` to `\mathrm{A}(\mathrm{br})` — the
card's own forms. `\resultstatus` renders as a visible `\textbf{Status.}` paragraph, which is what
gate (b) requires.

**Verdict: MISCITED** on both counts. **Minimal fix:** amend the header to "lines 42–51 (card stamp
2026-08-27)".

---

### 1.2 `sections_v3/theorem_section.tex`

---

**T-1 · `lem:D1`, lines 30–49 · OK-RESTRUCTURED**

**Checklist item 4, D1 half.** All card-row clauses land: A1, A2′, A4, A5; the table restrictions;
§3(i)'s cutoff selection map (as `Definition~\ref{def:cpbe}\,(i)`); **both** §4.3 conventions named
explicitly in the statement (`P_{-1}^P = E[Y]` and `P_ND = P^P_{f^-}`), and defined in full at
`def:prices` including the "not a never-disclosed counterfactual" reading; the **Borel-for-Exit**
addition, named in the statement *with its scope* ("needed only for part (c) below because pooled
pricing integrates over every type") and stated in full at (TR-ii) with the "genuine addition for
Exit" reason; and the **`I_H` content** addition, named and supplied by `def:prices`. All three
conclusion parts are present at full strength: (a) measurable *and* maps every control-node history
into exactly one cell; (b) the clock equivalence for every Voice plan; (c) `B^F, R_d, R, J` with
`eq:runup-jump`.

**The one difference:** the card names "the **§4.1/§4.2** table restrictions"; the statement cites
all of `asm:TR`, which includes (TR-iv)'s §4.3 pricing and entry conventions. D1 over-assumes
relative to its card row. Gate (a) tests clause *completeness*, not minimality, and part (c) is a
statement about prices in any case, so nothing is weakened in substance. Worth noting that the
crosswalk's own row D1.5 says "(TR-i)–(TR-iii)", understating what the statement actually cites.
**OK-RESTRUCTURED.**

---

**T-2 · `lem:L1`, lines 57–71 · no difference**

**Checklist item 4, L1 half.** Every card clause: D1; the §4.3/§4.4 definitions; **A5, which pins
*the* version of `E[Y|I]`** — the version-pinning gloss carried verbatim; **A2′ together with (TR-i),
under which `Δ_m` is finite**; **A1, which puts every object on one probability space**. Conclusion
`eq:L1` at `0 < Ω < 1`; both degenerate branches; **"the average over the null cell is *undefined
rather than imputed*"**; and the closing **"That last clause is a non-identification statement, and it
is proved rather than asserted."** The proof discharges the non-identification clause as a genuine
argument at `proofs_core_lemmas.tex`:228–242, exhibiting the one-parameter family of versions.
Complete.

---

**T-3 · `lem:L2`, lines 79–93 · OK-RESTRUCTURED**

All card clauses land, including "at fixed cutoff **and execution** policies", **A7′ named as the
form** with the "consumed almost surely on the flagged set" reading and its reason in a footnote (the
footnote carries a *reading*, not conditionality — permitted), D1, the no-feedback timing, `Ω > 0`,
and the entry rule "carried as bookkeeping" with the "or any rule with the two properties named in
the proof" alternative. Same TR-bundle over-assumption as T-1 (card: §4.1/§4.2). **OK-RESTRUCTURED.**

---

**T-4 · `lem:L3`, lines 103–122 · no difference**

Every card clause: A(τ) with both new clauses named; `h(0)=0`; κ-free pooled mass and engagement
moment at fixed policies; D1 **by statement**; the minimal regularity with **Darboux doing the rest
and no continuity of `h''`**; the part-(c)-only clauses (second-order Peano expansion at `0+`, one and
the same kernel along the shrinking family); the **L4-seam** clause (`|A'_κ|` bounded *uniformly in
`π̄`*); all three conclusions with "an identity, not an approximation" on (b); and **"an 'if' and
never an 'iff'"** with its reason. Complete.

---

**T-5 · `lem:L4` leg 2, lines 141–143 · OK-RESTRUCTURED**

**Checklist item 12(a).**

- Card: *"the pooled engagement **share** falls, `π̄_pr(τ') ≤ π̄_pr(τ)`, with an exact identity for
  the gap"*.
- Section: *"…with an exact identity for the difference between the two shares."*

The writers declare the substitution at crosswalk row L4.7, citing CONTEXT.md's _Avoid_ on "gap".
**My judgement: the substitution was not required, and it changed no substance.** The _Avoid_ sits
under the **Whitespace** entry and targets positioning language ("a gap in the literature");
CONTEXT.md's own **Premium wedge** entry uses "gap" arithmetically (*"The gap in expected takeover
premium…"*), as does the card (§4.3's `U_j` row: *"Card gap closed here"*). The replacement names
exactly the object the proof produces: `eq:L4-share` at `proofs_core_lemmas.tex`:827–831 gives
`π̄_pr(τ) − π̄_pr(τ') = (ν/ρ_P)(1 − π̄_pr(τ'))`, an exact identity for the difference between the
two shares. All other leg-1/2/3 clauses and the two hypothesis lists check out, including
**"Nestedness is a *conclusion* of leg 1, not a hypothesis of it"** and the **sign-half-unused**
qualifier on `C_h ≤ 0`. **OK-RESTRUCTURED.**

---

**T-6 · `prop:P1`, lines 174–270 · no difference — gate (a)'s known trap is COMPLETE**

I walked contract gate (a)'s P1 trap list item by item against the statement. Every one lands:

| Card / contract clause | Landed |
|---|---|
| A7-J named as the joint form | (P-6), with the whole-flagged-pair-set and "including pairs no cutoff vector selects" |
| form-mismatch history available in text or footnote | footnote on (P-6) — contract explicitly permits either |
| h.16 continuation-cost clause | (P-10), with the trivially-true-on-single-Voice, live-only-on-multi-Voice, what-it-buys, no-date-0-optimality-to-fall-back-on, and **requirement (ii) fails at that node** consequences |
| two-readings timing convention | (P-12) plus `rem:Ctiming`, with "the result does not depend on the choice" |
| D1's hypotheses travelling | (P-7), the travelling clause emphasised |
| flag-terminates-the-pooled-round reading | (P-8), read together with `asm:flagterm` |
| definitional round-2 action-set hypothesis | (P-9), including "not a closure condition; the closure form is jointly unsatisfiable with finiteness, by cardinality" |
| §4.1–§4.3 table-restrictions block | (P-13), enumerated: (TR-iv)'s `Y`/price/entry, (TR-ii)'s Borel-for-Exit **needed directly and not by way of D1**, (TR-iii)'s `D=1⇒a=1` and the `c/f/B^F/Q^F/b*` definitions and `∂_s B_j ≥ 0` for Voice, (TR-i)'s distributional forms with `Δ_m > 0` |
| `m_0 ≥ 0` | (P-11) → `eq:m0` |
| `κ ∈ [0,1]` via the extension route | (ii), with boundary supports, "off nature's path rather than off the players'", no §3(vi) requirement, read by no step, **"No cut to `κ ∈ [0,1)` is taken"**, and the false-at-`κ=1` claim **withdrawn** |
| one-family / every-`k` / positive-probability off-path belief clause | (i), all three, with the reason (deviation payoffs defining `\Tmap` read off-path pooled histories) |
| A7-J supplying flagged-tuple beliefs on and off path as a **version** | (iii), including "a version is what a conditional law is", "any a.e.-equal version serves (iii) and (vi) equally", and "no tuple outside that image arises" by (P-9) |
| sequentially-optimal flagged component at **every** flagged pair | (v), with the price-invariance / order-cancels / (P-10)-makes-what-remains-constant mechanism |
| A5 **not assumed** (derived from `m_0 ≥ 0`) | trailing ¶1, all three parts (existence and uniqueness, continuity, measurable selection from A7-J + (TR-ii)) |
| A6 read as the tie-break-and-corner selection | trailing ¶2, with "without which a correspondence cannot be called continuous" and `Θ` nonempty per `def:theta` |
| A8-at-equilibrium, with H-ord for the single-threshold restatement | final ¶, H-ord named as Voice stake monotonicity across plans, plus the upper-set engagement-flag hypothesis |
| uniqueness not claimed | final sentence, and again at `def:cpbe` and `sec:not-claimed` |

The conclusion stem carries **"at every `κ ∈ [0,1]`"** in emphasis. **Complete; no difference.**

---

**T-7 · `rem:P1record`, lines 275–297 · no substantive difference**

Card's P1 numerical block: four sweep-unresolved nodes at `κ ∈ {0.15, 0.85} × (τ,T) ∈ {(0.05,5),
(0.075,1)}`, **STILL UNRESOLVED after 30 seeds each**, payoff-scale residual `3.1e-4`–`1.5e-3`
against a `1e-9` criterion, cutoff-scale `1e-14`–`1e-11`, A3 and A6 proxies pass at every achieving
seed, **UNCHECKED**, and the label resting on the proof plus the two 2026-08-25 passes rather than the
grid. All present, with the JSON named as a `\texttt{}` string (the `.py` is not named — trivial).

The section adds a cross-reference the card licenses: *"which, as Remark~\ref{rem:A3record} explains,
is not evidence that those hypotheses hold: the proxies are local screens…"*. Card §5's A3 note says
exactly this ("both are silent on these findings"). The second paragraph carries card §9 item 4's
"no label moves … P1 stays PROVED as a conditional, in the A(τ) pattern" and the relocated 4(c)
material (`23` of `27`, two fixed points at the worst probed node). **Complete.**

**Note for item 13: this remark contains no overfull hbox.** See **F-2**.

---

**T-8 · `thm:T1`, lines 302–339 · no difference**

Every clause of the card's T1 row lands: the fixed-policy frame with `0 < Ω < 1` and `S_P > 0`;
Part (A) with the exact factorisation **and** the total-variation aggregate over any κ-grid with no
differentiability required; Part (B) with `eq:T1B`, **"because *both* ratios lie in `[0,1]`"** and
**"No dominance condition is needed"**; Part (C) as an **iff**, with `W_T ≤ 1` **proved** from the
clock equivalence and the monotone Voice stake path, `C_T` **unsigned**, and the equivalent form
`eq:T1C` carrying all three quantifier clauses **verbatim** — "holds *on average along the tightening
path*, integrated over `[-T,-T']`, and exactly in the infinitesimal limit; read pointwise,
\eqref{eq:T1C} is false". Hypotheses (T-1)–(T-15) match the card's list one for one, including
PE-Ω's three parts (derivable rather than assumed; exactly what fails in GE; the term C1 bounds),
(T-8)'s "no standing hypothesis supplies this … carried in the proof", (T-9)'s π̄ ruling, (T-11) at
the threshold pair, (T-14) scoped to the local form only, and (T-15) "confirmed non-load-bearing".
Closing: **"No unconditional window sign is claimed."**

---

**T-9 · `rem:T1record`, lines 349–369 · MISCITED (records) + OK-RESTRUCTURED + one UNCHECKED**

**Checklist item 1.** Checked against card §9 item 3 and the card's §4.4/O-1 material.

*Verified exact:*

- The four ratios: `1.06397`, `1.18373`, `1.13631`, `0.37798` — **all four, exact.**
- The four `Ω` values: `0.037252`, `0.128950`, `0.285804`, `0.50` — **all four, exact.**
- "For Part~(C) the genuine window-margin record is **block 4 of the executed T1 check**: `W_T C_T <
  1` at **every checked node** at this calibration, with an **`H = 10` corner caveat**" — the whole
  claim, present.
- "That is NUMERICAL node evidence at one calibration and not a sign theorem, which Part~(C) does not
  claim."
- The disclosure-regime/window distinction, in full: the ratios "are regime-comparison composition
  outcomes; they are not `W_T C_T` and they measure no window pair"; "The analogy is useful only
  because it shows that a composition factor can exceed one, which is what motivates the genuine
  window-margin 'if and only if' above"; "the O-1 cut at `Ω* ≈ 0.343` is a disclosure-regime
  boundary, not a window boundary."

*Difference (i) — record names thinned. MISCITED.* The card names `t2_t1_check` block 4,
`HANDOFF_sign.md` §8.1 for the `H=10` caveat, `HANDOFF_sign.md` §3 and
`quality_reports/fixes/t1_o1_rerun_check.py` for the `Ω*` cut. The section writes "block 4 of the
executed T1 check" and "recorded in the handoff", and names no script. The substance survives
entirely. This is the *only* one of the five numerical-record remarks that does not give its records
as `\texttt{}` strings — `rem:AtauRecord`, `rem:A6record`, `rem:P1record` and `rem:C1record` all do.
**Minimal fix:** name `t2_t1_check` and `t1_o1_rerun_check.py` as `\texttt{}` strings for
consistency; "the handoff" is fine as paper prose (see M-4b).

*Difference (ii) — the O-1 descriptor. OK-RESTRUCTURED.* Card: O-1 "compares the public buy flagged
versus pooled **at fixed policies** in the static repo model." Section: "is a *disclosure-regime*
comparison **at a fixed filing window** in the static repository model." The card's descriptor
("public buy flagged versus pooled", "at fixed policies") is replaced by CONTEXT.md's definitional
property of the disclosure-regime margin (*"the comparison that toggles whether the market sees the
flag, at a fixed filing window"*). Both are true of O-1 and the substitute is glossary-sourced.

*Difference (iii) — a card-internal tension the section inherits. UNCHECKED, card-side.* Card §4.4's
`Ω` row says *"the O-1 numbers 0.037 / 0.129 / 0.286 / 0.50 and the **≈ 0.29 cut** are all Ω-type"*;
card §9 item 3 says *"The O-1 cut **Ω\* ≈ 0.343**"*. The section carries `0.343`, following §9 item 3
— the O-1-specific and later-dated text. I cannot determine from the card alone whether `≈ 0.29` and
`≈ 0.343` are two different objects or an internal inconsistency, so I do not adjudicate it. The
section's choice is defensible either way. **Flagged for the orchestrator.**

*Also checked, gate (d):* "window test" is the one occurrence in all six files, and it is used to
*name and reject* the misreading ("are sometimes read as a window test, is a *disclosure-regime*
comparison"), which is exactly CONTEXT.md's own scoping of the _Avoid_ ("window test (when a regime
comparison is meant)"). **Not a violation.**

---

**T-10 · `prop:C1` closing sentence, line 401 · MISCITED**

**Checklist item 10.** I determined which object the card means, as asked.

- Card §6 C1 row, final sentence: *"The sign-coherence hypothesis is confirmed unused in the boxed
  conclusion."*
- Card §6 C1 row, evidence chain: *"re-derivation PASS 2026-08-21 (PROVED-WITH-CHANGES: N1, N2
  added; **H8 unused**; …)"*.
- `proofs/C1_proof.md`:141 — *"**H8 — Sign coherence (used only to name `g_r^PE`, never to reach the
  conclusion).**"*
- `rederive/C1_rederivation.md`:15 — *"one is **confirmed unused** for the boxed conclusion (H8,
  exactly as the sheet says)"*.

**The card means H8.** H8 is the agreement of the *fixed-policy* liquidity-derivative sign with the
*equilibrium* sign. Assumption AGE's third clause is a different object — *sign constancy*, that the
equilibrium sign is constant on `R` — and AGE has no clause named "sign coherence" at all.

- Section, line 401: *"The sign-coherence hypothesis **of Assumption~\ref{asm:AGE}** is confirmed
  unused in this conclusion."*

The statement attributes the card's H8 finding to AGE. However, the proofs file discharges **both**
objects and keeps them apart, at `proofs_theorem_ge.tex`:713–724: *"The constancy clause of
Assumption~\ref{asm:AGE} … is not used: Step~7 derives constancy on a connected neighbourhood from
hypotheses~(C-5) and~(C-2) … **Nor is the coherence of the fixed-policy sign with the equilibrium sign
used.** That coherence has one job and it is a job of naming…"* — which is H8, correctly identified
and correctly discharged, with its naming role spelled out exactly as `C1_proof.md`:141 has it.

**Verdict: MISCITED, not WRONG.** Two reasons. The card's H8 record *does* exist in the sections — at
the proof site rather than the statement site. And the sentence as written asserts nothing false:
AGE's constancy clause is likewise unused, and the proof says so. What is off is the label on the
card's finding at the statement site.

The crosswalk propagates the same conflation rather than hiding it — §0 row 27: *"C1's row consumes
AGE's contraction clause **and the sign-coherence clause**"*. So this is one traceable slip, not two.

**Minimal fix (propose only; I made no edit):** replace line 401 with

> The sign-coherence hypothesis --- that the fixed-policy liquidity-derivative sign agrees with the
> equilibrium sign --- is confirmed unused in this conclusion; so is the sign-constancy clause of
> Assumption~\ref{asm:AGE}.

All of (C-1)–(C-7) are otherwise verbatim against the card row, including (C-1)'s three parts (one
fixed norm convention, induced operator norm with its dual pairings, "a mismatched pairing silently
voids the implication"), (C-2)'s both-coordinates and `κ ∉ {0,1}`, (C-5)'s explicit distinction of
`S^GE` from `def:premium`'s fixed-policy `S`, and (C-7)'s both halves.

---

**T-11 · `rem:C1record`, lines 408–430 · MISCITED (attribution) — item 3 answered YES**

**Checklist item 3: does the card actually record this retirement?** **Yes.** `MODEL_CARD.md`:485–489,
immediately below the §6 ledger table:

> The old aspiration line ("C1 PROVED on a named nonempty region, NUMERICAL off-region") is
> **retired as structurally undeliverable as worded** (the C1 proof-read's ruling): the deliverables
> are the three objects the C1 row now carries — the implication PROVED with the region as a
> hypothesis, the dominance-and-contraction nodes NUMERICAL, and a named-region promotion an open
> question with the D8 ε-ball pattern as its template.

Section, lines 424–429, carries all four parts: the retirement with the phrase **"retired as
structurally undeliverable as worded"** verbatim, and the three deliverables. Dropped: the
attribution "(the C1 proof-read's ruling)". **MISCITED**, minor.

Every number in the first paragraph checks out against the card's C1 Label cell: 18 of 80; the
largest contiguous block `T = 5`, τ-percentiles `{50,70,90}`, `κ ∈ {0.65, 0.75, 0.85}`; `η_r` minimum
`0.0595`, median `0.3467`; `L_R ∈ [0.264, 0.501]` everywhere; the executed committed check
independently re-run on 2026-08-22 with all values reproducing; "they verify the two pointwise
inequalities `L_R < 1` and `η_r > 0` together with supporting diagnostics" and **"they do *not*
verify the full antecedent (C-1)--(C-7) … and they do *not* exhibit a named nonempty region"**;
**"A dominance-and-contraction node is not a fifth honesty label"**; both records named; and the
re-derivation bonus `B_r^GE = O((1−L_R)^{-3})` with the cubic-bounded-away gloss.

---

**T-12 · `sec:not-claimed`, lines 432–466 · OK-RESTRUCTURED + MISCITED (one dangling pointer)**

**Checklist item 5 — the prose list, item for item.** Card §9 preamble carries eleven items; the
section carries all eleven, in card order:

| # | Card | Section | |
|---|---|---|---|
| 1 | a global window-margin attenuation sign | identical | ✔ |
| 2 | κ-invariance of `J` | "κ-invariance of the filing-day jump `J`" | ✔ |
| 3 | equilibrium uniqueness | identical | ✔ |
| 4 | a nonempty GE region as a theorem | "a nonempty general-equilibrium region as a theorem" | ✔ |
| 5 | endogenous filing before the deadline | identical | ✔ |
| 6 | noisy or partially revealing flagged-round trading | identical | ✔ |
| 7 | continuous-time execution | identical | ✔ |
| 8 | welfare or optimal rule design | identical | ✔ |
| 9 | that draft_v2's hump result survives | "that the frozen manuscript's hump result survives" | ✔ |
| 10 | that the prior calibration (`Ω ≈ 0.037`) is economically meaningful | "at `Ω ≈ 0.037`" | ✔ |
| 11 | any empirical value for `ω_a` | "for the disclosed share of engagements `ω_a`" | ✔ |

Only substitution: "draft_v2's" → "the frozen manuscript's", consistent throughout the six files
(draft_v2 is an internal repo name). **OK-RESTRUCTURED.** The card's meta-note that A7 satisfiability
"was never listed here and is now resolved" is not carried into the list, correctly — it is card
bookkeeping, and the resolution itself is stated at `model_section.tex`:406.

**Checklist item 6 — the open-questions list.** The card has four §9 items; the section carries three
(card 1, 2, 4) and relocates item 3's substance into `rem:T1record`. The relocation is announced in
the section's own lead-in (lines 442–443): *"Three questions remain open, in whole or in part … The
third was answered in substance on 2026-08-27; what survives of it is scoped below."*

*Was anything of card item 3 lost in the move?* I compared its eight elements against
`rem:T1record`: the "disclosure-regime analogy, not a window-margin test" framing ✔; the four ratios
✔; the four `Ω` values ✔; "regime-comparison composition outcomes … not `W_T C_T` … measure no window
pair" ✔; the composition-factor-can-exceed-one motivation for T1's genuine iff ✔; the block-4
`W_T C_T < 1` record with the `H = 10` caveat ✔; the `Ω* ≈ 0.343` disclosure-regime boundary ✔.
**Nothing substantive was lost.** What thinned is covered at **T-9(i)** (record names) and
**T-9(ii)** (the descriptor swap). The card's "this is a known fact on file, not a claim the card
makes" is card bookkeeping about why the item sits in §9 and does not translate into paper prose;
the section's "One distinction is worth stating because it is easy to lose" does the same work.

*Are items 1/2/4 complete?*

- **Item (1)** (card item 1): the support condition as the entire remaining bite; the one-round market
  that satisfies it; the no-disclosure structure that does not; L3, L4 leg 3 and T1 Part (B) all
  conditional on it; **"the largest single conditionality the ledger carries"** ✔. **One dangling
  pointer** — see **M-4a**: the claim that the paper "names the weakest sufficient conditions for the
  two-round case" is not met by the paper (line 448, and again at line 129). **MISCITED.**
- **Item (2)** (card item 2): A7′ menus fully separating; the burden did not disappear when
  satisfiability was resolved, it **moved** to incentive compatibility, which P1 does not settle; and
  the "relatedly" clause that P1 does not claim an A8-satisfying equilibrium exists, only that A8
  holding *at* an exhibited equilibrium puts both cells on path ✔. Complete. ("P1-adjacent" dropped —
  a card tag, not content.)
- **Item (3)** (card item 4): answered-in-substance status with the date; locus corrected;
  cross-reference to `rem:A6record`; and all three still-open parts — **(a)** a constructive `Θ` or
  the *t*-constrained Kakutani route which removes the continuity half, the repair identified rather
  than executed; **(b)** the complementary menu class with the implemented menu as an instance for
  its collapse face, where the collapse-face clause may be satisfiable; **(c)** nonexistence, neither
  claimed nor shown ✔. Card item 4(c)'s supporting numbers (`23/27`, two surviving fixed points) are
  relocated to `rem:P1record` and are present ✔. Dropped: the proof-local IDs "Step 18" and "h.6".
  **The (a)/(b)/(c) scoping is complete.**

---

### 1.3 `sections_v3/proofs_section.tex`

Three `\input` lines and the `\section{Proofs}` / `sec:proofs` pair that every result statement points
at. The single permitted plumbing edit, declared at `labels_map.md`:9–12. **No difference.**

---

### 1.4 `sections_v3/proofs_core_lemmas.tex`

---

**P-1 · D1 proof, lines 19–178 · no difference at transcription grain**

Thirteen steps carrying the source argument, with the three turn-2 repairs the card names visible in
the text: the **public-flag bridge** made explicit and identified as what part (a) turns on
(Step 6); `B^F` continuum-valued with `eq:D1-BFmeas` supplying its measurability (Step 10); and the
`P_{-1}^P` convention consumed where `T = H` forces `c = 0` (Step 11). The `P_ND`
same-order-flow reading is carried as load-bearing at Step 12 ("under a never-disclosed
counterfactual reading the middle terms would not cancel"). Step 9 derives why the core carries
`b_0 < τ`, and Step 13 records that no probability restriction entered Steps 4–9, which is the card's
A8 gloss. No new mathematics, no dropped step the statement needs.

---

**P-2 · L3 proof Step 6, lines 543–548 · OK-RESTRUCTURED — flagged as the one added argument**

The MVT chain (tex Steps 1–6) is a faithful transcription of `L3_proof.md` Steps 1–6, with the
source's generic `g` specialised to `h` (the source's Step 10 does that specialisation; the tex folds
it in). Verified line by line: the first difference `δ_h`, the arithmetic cancellation leaving the
coefficient `−2`, the continuity/differentiability of `δ_h`, the first MVT giving `t_1 ∈ (0, π̄/2)`,
the containment `[t_1, t_1 + π̄/2] ⊂ (0, π̄)`, the second MVT giving `ζ`, and the chained
`C_h(π̄) = ¼π̄²h''(ζ)` with "the identity is exact" and "every use of `h` beyond continuity was at
points of the *open* interval".

**The addition:** lines 543–548 supply a **Darboux route** — *"The statement's gloss that Darboux's
theorem does the rest names the alternative route … `h''` is a derivative on `(0,π̄)` and therefore
has the intermediate value property, so the arithmetic mean of its values at two points of a compact
subinterval is itself a value of `h''` at some point between them. Neither route uses continuity of
`h''`, which is why the hypothesis does not carry it."* `grep -i darboux proofs/L3_proof.md` returns
nothing: this argument is **not in the source proof**.

**Verdict: OK-RESTRUCTURED, flagged.** Three reasons it does not rise higher. It discharges a gloss
the **card's own L3 row** asserts ("Darboux does the rest, no continuity of `h''`"), which the
statement at `lem:L3`:109–110 must therefore carry and which would otherwise stand unexplained. It is
presented as *the alternative route* and is not load-bearing — the MVT chain is the proof. And it is
sound as stated. **This is the only place in the three proof files where the tex supplies an argument
the source does not carry;** the orchestrator may want it either sourced or trimmed.

---

**P-3 · L3 proof scope, lines 484–725 · MISCITED (mechanism, reported once)**

The tex L3 proof runs Steps 1–15 and stops. The source's Part IV — Steps 16 (Example A), 17
(Example B), 18 (the OPEN two-round question, where (S1)–(S2) are defined) — and Step 19 (the `π̄`
ruling) are **relocated rather than transcribed**: Examples A and B into the `asm:Atau` discussion
(`model_section.tex`:456–459), Step 19's degeneracy argument into tex Step 15's closing
(`proofs_core_lemmas.tex`:716–724) and again at `model_section.tex`:650–652. **(S1)–(S2) are
relocated nowhere.** Consequence and fix: see **M-4a**. Reported here once so it is not double-counted.

---

**P-4 · L4 proof, lines 727–948 · no difference**

Seventeen steps. Leg 1's inclusion derived (Step 4) with nestedness explicitly a *conclusion*; leg 2's
exact identity at `eq:L4-share` — matching the statement's "the difference between the two shares"
(T-5); Step 11 recording why engagement share one delivers leg 2 unconditionally and what a weakened
Step 5 would cost; Step 14 recording that **only the magnitude half** of the maintained orientation is
read and **"The sign half `C_h ≤ 0` is consumed at no step of this leg"**, matching the card row;
Step 15 recording that (br-iii) cannot be dispensed with; Step 17 handling the vanishing-chord
equality case. The closing paragraph carries the three limits (fixed policies with the concrete
re-optimisation counterexample; no strict inequality; nothing about the window margin).

---

### 1.5 `sections_v3/proofs_existence.tex`

---

**P-5 · The h → P register, header lines 12–20 · verified, no difference**

The header maps `P1_proof.md`'s h.1–h.17 onto the statement's (P-1)–(P-13) plus the two non-hypothesis
destinations. I verified the map against the source's hypothesis list and against where each is
actually consumed. h.5 (A5) is marked **STRUCK** and lands in the trailing "A5 is not assumed"
paragraph — correct, and the proof derives all three of A5's contents (Steps 7, 8, 6(c)). h.8 (A8),
h.13 (H-ord) and h.15 (upper-set engagement flag) land in the final A8 paragraph and are consumed at
Steps 19–20 — correct, and Step 20 names which of the three the standing hypotheses supply. Every
(P-n) is consumed at a named step, or its non-consumption is declared: **(P-10) is explicitly not
consumed under the sunk reading** (Step 12(d), "Under the sunk reading it is not consumed at all"),
and **(P-5)'s two halves are separated** — the ordering and self-map content *derived* at Step 13,
the bracket and continuity *assumed* at Steps 14 and 15.

The header's claim that **"Step numbering is 1:1 with the source (Steps 1-20, Parts A-F)"** is
correct: I checked both step lists.

---

**P-5b · P1 proof Step 9, lines 312–459 · no difference**

Step 9 carries statement clauses (i) and (ii) and I read all four sub-blocks. **(a)** defines
*reachability* as a whole-history property of the menu and the noise law alone — explicitly
independent of `k` and of the perturbation stage — and separates the noise *alphabet* (finite at
every κ, which is all Step 3 needs) from `supp(z_d)` (the subset carrying positive probability at the
maintained κ, which is what a zero-probability argument must be quantified over). **(b)** fixes the
one family at `eq:P1-wn` with `t_n = J/n ↓ 0` (and says why the mass is not written with a Greek
letter: `ε` is the signal noise), gives the stage-`n` joint density `eq:P1-mun`, and splits on the
denominator `eq:P1-Zn`: at `Λ_k > 0` dominated convergence with an explicit integrable envelope; at
`Λ_k = 0` the limit is exact, free of `n`, and **does not depend on `k`** — *"which is what makes one
family serve at every `k ∈ Θ`"*, the card's own clause, derived rather than asserted. The block also
argues why the **joint** posterior is required (π is a functional of the plan posterior, `v̂` of the
signal posterior; integrating the signal out first leaves `v̂` undefined) and why it is load-bearing
where least obvious (Step 13 evaluates the payoff to plans carrying zero probability under `k`, whose
execution bracket reads `k`-null histories). **(c)** supplies the reference-belief root convention,
argues that `E[Y]` will **not** serve because it is in general not a root of `P_I` at any belief
while the conclusion says "prices at their inner fixed points" without qualification, and admits
without hedging that the choice can move a component of `\Tmap`. **(d)** handles `κ ∈ {0,1}` exactly
as card clause (ii) does, including *"no cut to `κ ∈ [0,1)` anywhere"*, the extension framing, the
withdrawn false claim, and *"Nothing here asserts that the flagged cell carries positive probability
at `κ = 1`."*

Incidentally this closes a loose end in **M-3**: `Λ_k` and `Λ_u` are *defined* at lines 389–392, so
`rem:A6record`'s rendering of the card's `Λ_k(h)` as "the reaching weight" is a paper-prose choice
with the symbol available in the proof, not an anchor loss.

---

**P-6 · P1 proof Step 12, lines 540–689 · deep sample — faithful, two differences**

Compared clause by clause against `P1_proof.md`:659–773.

*Carried in full:* the quantification over **every** flagged pair with no assumption that `j = j_k(s)`
and the reason it can be ("without appealing to date-0 optimality"); the class `Q_j(s)` and the
shared-path derivation of `c_{j'} = c_j`, `f_{j'} = f_j`, `B^F_{j'} = B^F_j`, `a_{j'} = a_j = 1`; the
deviation tuple differing in the `Q^F` coordinate alone and lying in the image; **(a)** price
invariance `eq:P1-PFinv` with uniqueness of the inner root making `P^F(s)` a number rather than a
selection; **(b)** the `E[Y|·] = P^F(s)` valuation and *"No informational rent survives into round 2:
full separation is what A7-J buys, and \eqref{eq:P1-EYflag} is what it costs"*; **(c)** the
cancellation of every appearance of `Q^F_{j'}` and with it `b^*_{j'}`; **(d)** both readings, the sunk
reading constant outright, the plan-completion reading closed by (P-10), and the convention-free
conclusion; the **"where (P-10) bites"** paragraph, including the selected-`j` case where date-0
optimality already does the work and the non-selected case where it does not; the **refutation note**
that a class with differing *trading* terms cannot be built (`δ = 0` necessarily); and the **converse**
about (P-9), with the off-image belief problem, "*a* sufficient condition" not the weakest, and the
question declared **open**.

*Difference (i) — line 625. OK-RESTRUCTURED.*

- Source, `P1_proof.md`:710: *"so on flagged plans `$U_{j}(s;k)=B_j^F(s)P^F(s)-C_j(s)-E_j(s;k)$`"*
- Tex, line 625: *"so on flagged plans `$U_{j'}(s;k) = B_j^F(s)P^F(s) - C_{j'}(s) - E_j(s;k)$`"*

The tex's indexing is the consistent one for a general class member, and it matches the **source's own
next paragraph** (`P1_proof.md`:726: *"by (c) `$U_{j'}=B_j^FP^F-C_{j'}-E_j$` within the class"*).
This is a source-typo correction, not new mathematics. Downstream use is consistent: the tex's Step 15
(line 823) reads the same display back with the `j'` indexing.

*Difference (ii) — lines 577–582. OK-RESTRUCTURED.* The tex adds, at `eq:P1-PFinv`: *"It is
Assumption~\ref{asm:A7J} (A7-J) that pins the belief at the same signal for every class member …
The argument at this display is where the joint form of the injectivity hypothesis is indispensable
and its on-path form … is not enough: the tuples in question are generated by pairs the cutoff vector
need not select."* Sourced from the card's P1 row ("the form the proof consumes **where it pins
off-path flagged beliefs**") and from the source's own (a). It makes the form-mismatch history's
locus visible at the step that turns on it. **Non-blocking; an improvement.**

---

**P-7 · P1 proof Step 18, lines 897–912 · no silent strengthening**

Titled *"Step 18 (a strengthening recorded here, **not part of the proposition**)"* and closing
*"Definition~\ref{def:cpbe} fixes the Brouwer route for this proposition, so this is a remark and not
a part of the claim."* It states exactly what the Kakutani route removes (condition (ii) of Step 15
and A6's continuity clause) and what it does **not** remove (condition (i) and Step 14's bracket) —
matching card §5's A6 note ("Repairs on file, both outside §3's declared Brouwer-with-one-fixed-family
route: the *t*-constrained game + Kakutani + `t ↓ 0` (`proofs/P1_proof.md` Step 18)"). **No
difference.**

---

**P-8 · P1 proof Step 15 and the Scope block, lines 777–833 and 969–1024 · no difference**

Step 15 declares precisely where (P-5) assumes rather than derives, names (i) joint continuity and
(ii) transversality as the weakest replacement pair, and records — honestly and unprompted — that
plateaus are **structural** on exactly the menus (P-10) exists for, so on multi-Voice shared-path
menus (P-5) "is being assumed at a configuration where its own named sufficient condition provably
fails". It then points at `rem:A6record` for the measured failure. The six-part Scope block covers
uniqueness in all four forms, the A8 addendum's conditionality, the `κ` boundary extension, the
convention-dependence of the constructed object (including both undecided readings), the flagged
order's non-uniqueness, and the sufficient-not-necessary status of A7-J, (P-9), (P-10) and A6. This
is the register the contract's gate (b)/(c) intent asks for.

---

### 1.6 `sections_v3/proofs_theorem_ge.tex`

---

**P-9 · T1 proof Step 16, lines 350–402 · deep sample — no difference**

The card's T1 row carries the traceable change *"the quantifier **'on average along the tightening
path'** is added on the re-deriver's S28(ii)"*. All three of the statement's quantifier clauses are
proved separately, and a fourth sub-claim supports them:

- **(i)** `W_T C_T = exp(∫_{r_0}^{r_1} Λ)` via the fundamental theorem of calculus on `log S`, hence
  `W_T C_T ≤ 1 ⟺ ∫Λ ≤ 0`, with "the product criterion is the local criterion integrated along the
  tightening path. This is the 'on average' reading, and it is exact at finite scale." ✔ the card's
  "integrated over `[-T,-T']`".
- **(ii)** pointwise `Λ ≤ 0` ⟹ `W_T C_T ≤ 1`, with the strict version.
- **(iii)** `W_T C_T ≤ 1` gives `Λ(r*) ≤ 0` at **one** point only, by the mean value theorem for
  integrals, plus an explicit counterexample shape (Λ positive on the first half, sufficiently
  negative on the second) — *"The implication in this direction is 'at some point', never 'at every
  point'."* ✔ the card's **"false read pointwise"**.
- **(iv)** the two forms coincide exactly in the infinitesimal limit, with the `Λ(r_0) = 0` boundary
  case **named rather than resolved**. ✔ the card's "exactly in the infinitesimal limit".

Step 15 keeps (T-14)'s monotonicity clause separate from Step 12's integer-window inequality, noting
that nothing outside (T-14) forbids a dipping interpolant — a distinction the statement needs and the
card implies.

---

**P-9b · T1 proof Steps 6 and 12–14, lines 117–137 and 242–313 · no difference**

**Step 6** proves Part (A)'s total-variation clause at `eq:T1-tv` using Steps 2 and 3 in their
**constancy** form — *"`M_F` and `Ω` are one and the same number at the two nodes, which a vanishing
derivative at a single κ would not deliver"* — and records that **(T-8) is not used**, matching the
card's "no differentiability required". It then generalises to any degree-one positively homogeneous
aggregator, with the reason this matters for measurement conventions.

**Step 12** proves `W_T ≤ 1` rather than assuming it, from exactly the two ingredients the card row
names: the clock equivalence of `lem:D1`(b) and `∂_d B_j ≥ 0` for Voice from (TR-ii), with A4's
only-Voice-plans-cross closing the argument — *"a consequence of Lemma~\ref{lem:D1} and the monotone
Voice stake path rather than a hypothesis of the theorem"*. ✔ the card's "**proved**".

**Step 13** gives three independent reasons `C_T` carries no sign, any one sufficient: A(br) is
quantified over the *threshold* pair and none of (br-i)–(br-v) says anything about two window
environments; the window moves trade across the filing date through (TR-iii)'s signed `B^F`/`Q^F`
monotonicities, which a threshold change does not; and the pooled history's own "no flag by `d`"
coordinate changes its content under a tighter window, a composition change at the `T` margin that
(br-ii) excludes only at the κ margin. ✔ the card's "`C_T` is **unsigned**".

**Step 14** gives `eq:T1-ratio-T` and the exact finite equivalence `eq:T1-iff` — the object Step 16
then integrates — and closes by saying precisely what "the weight effect dominates the composition
effect" does and does not mean (*"it does not mean `|1−W_T| ≥ |1−C_T|`, and it does not mean
`C_T ≤ 1`"*).

---

**P-10b · C1 proof Steps 1–6, lines 504–656 · no difference**

Read in full. Step 1 derives `eq:C1-neumann` by an explicit Neumann series, consuming exactly the
submultiplicativity the norm preamble said Step 1 would need. Step 2 establishes the branch's twice
continuous differentiability by a contraction-mapping argument followed by the `C²` implicit function
theorem, and names where (C-3)'s **single-branch** clause is consumed. Steps 3 and 4 reproduce
`def:theta`'s `k̄_x` and `k̄_{κr}` rows as *derived* bounds, with the "partial, not total" caveat on
`∂_x \Tmap`. Step 5's `eq:C1-decomp` is an exact five-term identity grouped in four, with two
miscount checks written out (no `Δ_κκ` or `Δ_rr` can appear; the last term is the only place a second
derivative of the equilibrium map enters, which is why Step 4 exists) and the observation that the
term T1 discards at `eq:T1-three` under (T-7) reappears here. Step 6 bounds the remainder to
**exactly `eq:BGE`**, term for term, and audits the four-terms-into-three-groups mapping explicitly;
the only inequalities used are the triangle inequality and the fixed norm pairings. The
`O((1−L_R)^{-3})` bonus is derived here rather than asserted. **No new mathematics, no dropped step,
no clause the statement needs left unsupported.**

---

**P-10 · (T-15) non-consumption, lines 417–422 · no difference**

*"Hypothesis~(T-15), threshold-side smoothness, is consumed by no step of the proof above. That is
the content of the statement's 'confirmed non-load-bearing' …"*, with the available-but-unclaimed
smooth local reading of Part (B) and "if (T-15) fails nothing above moves." Consistent with
`T1_proof.md`:235 (*"No boxed conclusion of this file rests on it"*). Note the tex T1 proof does not
transcribe the source's Step 15 (the *threshold*-side local form), which is why (T-15) is consumed by
no tex step at all; the statement's qualifier is satisfied either way. Tex T1 step numbers are
therefore **not** 1:1 with `T1_proof.md` — and, correctly, the file header makes no such claim
(unlike `proofs_existence.tex`, which claims 1:1 and delivers it).

---

**P-11 · C1 proof norm-convention preamble, lines 434–500 · deep sample — no difference**

Four conventions fixed before the argument: the margin, the norm, the equilibrium objects, and the
region's regularity. The **norm** block carries the card's N1 in full and then some: one norm fixed on
`R^{J-1}` by (C-1); the *induced* operator norm for the matrices; the **dual** norm
`‖φ‖_* = sup_{‖w‖≤1}|φ(w)|` for the covectors `Δ_k`, `Δ_{κk}`, `Δ_{kr}`; the bilinear-form norms for
`\Tmap_{kk}` and `Δ_{kk}`; and the two consequences — the operator norm must be induced, hence
submultiplicative, because Step 1 needs `‖A^n‖ ≤ ‖A‖^n`; and **"the pairing must be the matching one,
because pairing a covector with a vector through a magnitude that is not the dual norm can make
\eqref{eq:BGE} *understate* the remainder it is meant to bound, which voids the implication
silently"** — which is card N1's *"a mismatched pairing silently voids the implication"*, with the
mechanism supplied. The `J − 1 = 1` collapse note is a harmless addition. The equilibrium-objects
block does the card's (C-5) work of separating `S^GE` from `def:premium`'s `S` and pinning that every
partial below is a partial of the **fixed-policy** map evaluated on the equilibrium branch.

---

**P-12 · C1 proof closing discussion, lines 710–747 · no difference — and it is where item 10 is
discharged**

Three blocks. *"Sign coherence is not consumed"* separates and discharges both objects (see **T-10**).
*"The hypotheses are relative to the norm"* records that `L_R`, both `k̄` bounds, `B_r^GE` and hence
`η_r` all depend on the norm, that spectral radius below one does not give operator norm below one in
a *given* norm, and that this is why (C-1) fixes one convention. *"What is not delivered"* records
that nonemptiness of `R_r` is neither claimed nor provable here, restates exactly what the
dominance-and-contraction nodes verify and do not, names what a node-to-region promotion would need
(a modulus of continuity for `η_r` and a genuine supremum for `L_R`, "neither of which more grid nodes
can supply"), and records that `η_r ≤ 0` carries no information about the sign because `B_r^GE` is a
triangle-inequality bound.

---

**P-13 · Proof run-in citation style, all files · OK-RESTRUCTURED**

**Checklist item 12(b).** Five of the eight proof headings use the ID-only form
(`Proof of Lemma~\ref{lem:D1} (D1)`); three use a short descriptive title. In-proof run-ins cite by
`\ref` plus a parenthetical card ID — `Assumption~\ref{asm:A6} (A6)`, `Assumption~\ref{asm:A7J}
(A7-J)`, `Assumption~\ref{asm:A2p} (A2$'$)`. This is what `labels_map.md`:6–7 prescribes and it is
forced by the environment setup: the seven `\newtheorem`s are independently and globally numbered, so
`\ref` yields a bare number and the ID must be written by the citing prose. Gate (e) shows **zero**
undefined references, so every run-in resolves. **No substance at stake; the convention is consistent
and it satisfies card §8 rule 2 (cite only IDs the card carries).**

---

## 2. Gate-by-gate and item-by-item summary

### Contract gates

| Gate | Result | Basis |
|---|---|---|
| **(a) Clause completeness** | **PASS** | Every card §6 row walked clause by clause; P1's trap list (contract lines 13–22) walked item by item and **complete** (T-6). Two over-assumptions (D1, L2 cite the whole TR block where the card names §4.1/§4.2) affect minimality, not completeness — T-1, T-3. |
| **(b) Labels verbatim, conditionality attached** | **PASS** | All eight `\resultstatus` strings match the card ledger's Label cells character for character, including the four conditional ones the contract enumerates. `\resultstatus` renders a visible **Status.** paragraph, not a footnote. No label weakened, none promoted, no conditionality demoted. The one footnote in a statement (`lem:L2`) carries a *reading*, not conditionality. |
| **(c) Evidence-note substance present** | **PASS** | Every element the contract enumerates for A(τ), A6, A3, P1 numerics and C1 is present, at **both** an assumption site and a result site: `rem:AtauRecord` + `lem:L3`/`lem:L4` trailing ¶ + `rem:T1record` ¶1; `rem:A6record` + `rem:P1record` ¶2; `rem:A3record` + `rem:P1record` ¶2; `rem:P1record` ¶1; `rem:C1record`. Verified element by element at M-2, M-3, M-4, T-7, T-9, T-11. |
| **(d) Vocabulary (`CONTEXT.md`)** | **PASS** | Systematic sweep over all six files: **zero** hits for depth, volume, turnover, certified, certificate, region-certified, activist, investor, fund, reporting regime, transparency requirement, 13D, key(s), hook, pitch, angle, framing, motivation, novelty. κ glossed as **noise-trading intensity** (4×). The A7 form is named every time it matters — the three bare-"A7" hits are the assumption's own title, A7′'s title, and a meta-sentence about naming. "dominance-and-contraction" 9×, never "certified". Disclosure-regime ≠ window margin kept (T-9). Three borderline hits adjudicated below. |
| **(e) Compile** | **PASS** | My own clean four-pass run from the repo root after deleting every aux artifact: `xelatex → biber → xelatex → xelatex`. `grep -in undefined standalone_v3.log` returns **nothing** (count 0), references and citations both. `standalone_v3.blg` clean. One `Overfull \hbox` — located and fixed-proposed at **F-2**. |

### Contract "Citations" clause — also checked

The contract binds the checker here too. Result: **clean, and vacuously so.**

`sections_v3/sections_v3.bib` contains **no entries** — a single comment line
(*"New citations introduced by the v4 theory sections (ticket 08). Root bibliography.bib holds the
draft_v2-era entries."*). **No new bibliographic data was shipped**, so the rule that a new entry
needs data verified from a file on hand cannot have been broken.

All four citations used are pre-existing root keys, and all four appear in `bib_inventory.md`:
`Kyle1985`, `EdmansGoldsteinJiang2015` (both `model_section.tex`:36–38, for the discrete ternary-noise
order-flow structure), `GlostenMilgrom1985` (:38, competitive pricing), `GrossmanHart1980` (:40, the
free-rider reason the premium is the minority welfare object). All four resolve — gate (e) reports
zero undefined citations, and `standalone_v3.blg` is clean. Repo records are `\texttt{}` strings and
never citations throughout, as the contract requires: I checked every record mention in
`rem:AtauRecord`, `rem:A6record`, `rem:P1record` and `rem:C1record`.

*Gate (d) borderline hits, all adjudicated as legal:*

1. **"window test"**, `theorem_section.tex`:363 — used to *name and reject* the misreading (*"are
   sometimes read as a window test, is a disclosure-regime comparison"*). CONTEXT.md's _Avoid_ is
   scoped "(when a regime comparison is meant)", which is precisely the misuse the sentence corrects.
2. **"gap"**, six hits, all in `proofs_core_lemmas.tex` — five are "chord gap" / "chord-gap sum", the
   proof-local arithmetic object at `eq:L3-gap`; one is "The gap that (br-ii) closes". The _Avoid_
   sits under CONTEXT.md's **Whitespace** entry and targets positioning language; the glossary's own
   **Premium wedge** entry uses "gap" arithmetically. Not a violation. (Related: T-5.)
3. **"information structure"**, `proofs_core_lemmas.tex`:913 — *"the coefficient is a property of the
   pooled information structure"*. The _Avoid_ sits under **Partition** and forbids substituting the
   phrase *for* "partition"; here it describes what the pooled cell reveals, and the partition is
   named as "partition" 18 times across the six files. Not the forbidden substitution. If the orchestrator
   wants zero ambiguity, "the pooled cell's information content" is a drop-in.

### Checklist items 1–13

| # | Item | Verdict | Where |
|---|---|---|---|
| 1 | `rem:T1record`'s O-1 paragraph: four ratios, four Ω values, the block-4 / `W_T C_T < 1` / `H=10` claim, the disclosure-regime vs window distinction | **MISCITED** (record names thinned) + **OK-RESTRUCTURED** (descriptor swap) + **UNCHECKED** (card's 0.29 vs 0.343) — all numbers exact | T-9 |
| 2 | The A(br) block: (br-i)–(br-v), ρ sharpening, level-symmetric inheritance, (br-iii) attack-first, (br-v) three agents | **OK-RESTRUCTURED**; substance complete. MISCITED on the H17 / rederive pointers | M-5 |
| 3 | Does the card record the C1 aspiration retirement? | **YES** — `MODEL_CARD.md`:485–489, carried verbatim in substance. MISCITED on the "(C1 proof-read's ruling)" attribution | T-11 |
| 4 | D1 and L1 carry every clause (D1's three parts, `P^P_{-1}`/`P_ND`, Borel-for-Exit; L1's A5 version-pinning, degenerate-cell non-identification) | **Complete.** OK-RESTRUCTURED on D1's TR-bundle over-assumption | T-1, T-2 |
| 5 | `sec:not-claimed` prose list vs card §9 preamble, item for item | **Complete** — all eleven, card order. OK-RESTRUCTURED (draft_v2 → the frozen manuscript) | T-12 |
| 6 | Open-questions list: item 3's relocation lossless; items 1/2/4 complete incl. 4's (a)/(b)/(c) | **Nothing of item 3 lost**; 1/2/4 complete. One MISCITED dangling pointer in item (1) | T-12, M-4a |
| 7 | The eight displays, symbol for symbol | **No difference** — all eight identical to the card | M-9 |
| 8 | A7 satisfiability discussion (pro-rata menu, forty collisions, failure boundary) | **MISCITED** — one scoping addition ("for the on-path form") + dropped attack-verdict pointers; substance complete | M-8 |
| 9 | `def:premium` and `def:theta` (π̄ ruling, mean-vs-π̄ degeneracy, W/C conventions, margin subscripts) | **Complete.** MISCITED on ω_a "the calibration target"; OK-RESTRUCTURED on the notation-history drops | M-6, M-7 |
| 10 | Which object does the card's "sign-coherence hypothesis … unused" mean, and is `prop:C1`'s attribution exact? | **MISCITED** — the card means **H8**, not AGE; the statement attributes it to AGE; the proofs file discharges both and keeps them apart, so the record survives. **Not WRONG.** Fix proposed | T-10 |
| 11 | `rem:AtauRecord`'s two dropped pointers: (S1)/(S2), and MIN_CELL_MASS | (a) **MISCITED, a real loss** — the L3 proof does **not** carry Step 18's (S1)/(S2), so the link survives only via the card; two in-paper sentences now dangle. (b) **MISCITED, correct as paper prose** — substance fully intact | M-4a, M-4b |
| 12 | Two writer-flagged wordings: L4 leg 2's "gap", and ID-only proof run-ins | (a) **OK-RESTRUCTURED** — no substance change; the substitution was not required but is harmless. (b) **OK-RESTRUCTURED** — forced by the environment setup, zero undefined refs | T-5, P-13 |
| 13 | The one overfull hbox in `rem:P1record` — locate and propose the minimal fix | **Premise corrected.** It is **not** in `rem:P1record`; it is the C1 proof's optional heading | F-2 |

---

## 3. Flags outside the verdict classes

---

**F-1 · `\Tmap` name collision — a latent defect in the intended consumer, declared by the writers**

`sections_v3/v3_macros.tex`:29 binds `\Tmap` with `\providecommand{\Tmap}{\mathcal{T}}` and documents
why. I verified the collision it guards against: **`draft_v2.tex`:54 carries
`\providecommand{\Tmap}{T}`**, and uses `\Tmap` about ten times in its own body (e.g. line 575).

Consequence: in the standalone driver the binding is correct (`standalone_v3.tex` deliberately omits
draft_v2's macro block, so `\Tmap` → `\mathcal{T}`). But **in `draft_v3.tex` — a draft_v2 copy
carrying that block forward — `\Tmap` will silently resolve to upright `T`**, which is the filing
window. All **104** uses of `\Tmap` across the six section files (counted) would then render the
outer best-response map as the window symbol, in direct contradiction of card §4.5 (*"always
calligraphic — upright `T` is the window"*) and card §8 rule 4.

This is **not a difference from the card** — the checked artifact is correct as it compiles today, and
the writers flagged it themselves in the macro header. But it is the single highest-consequence item
I found for the next step in this lane, and it must be resolved (rename one of the two `\Tmap`s)
before draft_v3 assembly. Recorded here so it is not lost between tickets.

---

**F-2 · The overfull hbox — item 13's premise corrected**

The orchestrator's spot review located the one overfull hbox in `rem:P1record`. **It is not there.**

`standalone_v3.log`:669 (my own clean run, and the writers' run before it):

```
Overfull \hbox (14.3809pt too wide) in paragraph at lines 435--436
[]\TU/lmr/m/n/10.95 Four
```

The line numbers are read in the file open at that moment, which the log's page trace shows is
`sections_v3/proofs_theorem_ge.tex`. Lines 434–435 there are:

```latex
\begin{proof}[Proof of Proposition~\ref{prop:C1} (C1: the dominance-and-contraction implication in general equilibrium)]
Four conventions are fixed first, because the statement's hypotheses are stated against them.
```

`amsthm` sets a `proof`'s optional argument as an unbreakable label box at the head of the first
paragraph, which is why the box begins with "Four". The heading text —
*"Proof of Proposition 8 (C1: the dominance-and-contraction implication in general equilibrium)."* —
is the longest of the eight and overruns by 14.38pt. (`rem:P1record`'s second sentence also begins
"Four nodes of the equilibrium sweep", `theorem_section.tex`:278, which is the likely source of the
misattribution.)

**Minimal fix (proposed; I made no edit).** Shorten the optional argument on
`proofs_theorem_ge.tex`:434 to match the pattern the other five lemma proofs already use:

```latex
\begin{proof}[Proof of Proposition~\ref{prop:C1} (C1)]
```

That is a one-line change, touches no prose, changes no cross-reference, and clears the box with
room to spare. If the descriptive title is wanted,
`(C1: the dominance-and-contraction implication)` also fits.

---

## 4. Counts and overall verdict

| Class | Count |
|---|---|
| **WRONG** | **0** |
| MISCITED | 13 |
| UNCHECKED | 1 |
| OK-RESTRUCTURED | 14 |
| Flags (outside the classes) | 2 |

MISCITED (13): M-2 (A3 record pointers), M-3 (A6 record pointers), M-4a ((S1)/(S2) drop **plus** the
two dangling "weakest sufficient conditions" claims), M-4b (`MIN_CELL_MASS`/HANDOFF §8.1), M-4c
("block 3"), M-5 (H17 + rederive pointers), M-6 (ω_a "the calibration target"), M-8 (A7 failure
boundary scoped to the on-path form, + attack-verdict pointers), M-10 (`v3_macros.tex` provenance:
wrong line range **and** stale stamp), T-9i (`t2_t1_check`, HANDOFF §8.1, HANDOFF §3,
`t1_o1_rerun_check.py`), T-10 (sign-coherence attributed to AGE rather than H8), T-11 (C1
proof-read ruling attribution), P-3 (L3 step-number anchors have no in-paper home).

UNCHECKED (1): T-9iii — the card's own `≈ 0.29` (§4.4 Ω row) against `Ω* ≈ 0.343` (§9 item 3). Not
adjudicable from the card; the section follows §9 item 3 and is defensible either way. Card-side;
for the orchestrator.

---

### OVERALL VERDICT: **LAND** — no WRONG findings.

All five contract gates (a)–(e) pass, including a fresh compile I ran myself from a clean state, and
the contract's Citations clause is clean (no new bib entries shipped). The thirteen MISCITED findings
are pointer, attribution and provenance issues with substance intact; by the ticket's own vocabulary
none blocks. The five most worth acting on before landing, none of them blocking:

1. **M-4a** — restore (S1)–(S2), or reword the two sentences (`theorem_section.tex`:129 and :448)
   that claim the paper names them.
2. **T-10** — re-attribute the sign-coherence sentence (`theorem_section.tex`:401) from AGE to H8;
   the crosswalk's §0 row 27 carries the same conflation and should be corrected with it.
3. **F-2** — shorten `proofs_theorem_ge.tex`:434 to clear the overfull hbox. The ticket located this
   in `rem:P1record`; that premise is wrong and the correction belongs on the record.
4. **F-1** — resolve the `\Tmap` collision before draft_v3 assembly (104 uses would silently render
   the outer map as the window symbol).
5. **M-10** — fix `v3_macros.tex`'s provenance header, wrong on both the line range (42–51, not
   28–37) and the stamp (2026-08-27, not 2026-08-23).

*Checker's note on independence:* I read the writers' crosswalk and labels map as claims and verified
them against the files rather than accepting them. The crosswalk is honest — it declares the "gap"
substitution (row L4.7) and the P1 footnote relocation (row P1.9) without being asked. Two places
where it does not match what I found: row C1.10 records the sign-coherence clause as landed "final
sentence inside `prop:C1`" without recording that an attribution to AGE was added (§0 row 27 shows
the conflation was upstream of the sentence, not introduced at it); and row D1.5 says "(TR-i)–(TR-iii)"
where the statement cites all of `asm:TR`. Neither is concealment; both are logged above.

---
---

# Repair-round delta check — 2026-08-27 (appended)

Same checker, same rules: no git, no edit to any file under `sections_v3/` or `research/` other than
this append. Five repairs landed after the pass above; each is verified below against the same
sources, and the compile was re-run by me from a clean state.

**State at check.** `proofs_core_lemmas.tex` 949 → **1108** lines (L3 Part IV appended, lines
726–883, inside the L3 proof); `theorem_section.tex` 467 → **470**; `proofs_theorem_ge.tex` 748 →
**747**; `v3_macros.tex` 39 → **47**. `model_section.tex` (652), `proofs_existence.tex` (1025),
`proofs_section.tex` (6) and `standalone_v3.tex` (72) unchanged. Card stamp re-confirmed unchanged at
2026-08-27 / `ae9caea`.

---

## R-1 · L3 Part IV (`proofs_core_lemmas.tex`:726–883) — **PASS at full grain**

Checked line by line against `proofs/L3_proof.md` Part IV (Steps 16–18, source lines 327–453) and
against the card.

**(S1)/(S2) — named, and verbatim against the source.** `proofs_core_lemmas.tex`:865–870 sets them as
an `enumerate` with `label=(S\arabic*)`:

- (S1) source: *"every pooled order-flow cell is either fully revealing of `a=0`, fully revealing of
  `a=1` up to the pooled cell's own ceiling `π̄`, or a single cell whose posterior is `π̄/2`"*; tex
  identical, one "or" added for parallelism.
- (S2) source: *"that middle cell's likelihood ratio is free of `κ`, which in Example A came from the
  two contributing types reaching the cell through noise events of equal probability"*; tex
  identical, "Example A" → "Step 16" (the tex does not use the name "Example A").

The framing sentence is also verbatim — *"it suffices to establish the support condition alone: that
the pooled cell's engagement-posterior law, at fixed policies, is supported on exactly three points
`0 < π̄/2 < π̄` with none of them varying with `κ`"* — and the tex adds *"which are the weakest
sufficient conditions this lemma can name"*, de-first-personing the source's *"stated as the weakest
sufficient condition I can name"*. That addition is what makes the two sentences at issue in **M-4a**
true; see **R-2**.

**The one-round market (Step 16) — transcribed exactly.** Every element checked: the mark `2z̄`
against a non-engaging `0`; the share `ρ = ½`; the admissibility argument (`Γ` a finite ordered
coarsening with no ceiling of `z̄` on its image; the non-engaging mark as the constant Hold path of
(TR-ii)); the ternary noise and `X_0 = q_0 + z_0`. The table `eq:L3-exampleA` is cell-for-cell
identical to the source's, both rows. The three posteriors and their masses are exact —
`π = 1` and `π = 0` each at `(2−κ)/4`, `π = ½` at `κ/2` — as is the reason the middle atom sits at
`½` (*"the two types reach `X_0 = z̄` through noise realisations of equal probability `κ/2`, which
cancels"*). Support `{0,½,1} = {0,π̄/2,π̄}` with `π̄ = 1` ✔. Weights
`A_1 = A_0 = (2−κ)/4`, `A_{1/2} = κ/2` ✔; derivatives `A_0' = A_1' = −¼`,
`A_{1/2}' = +½ = −2·(−¼)` ✔; **`A'_κ = −¼`** stated explicitly ✔. The moment check
`A_{1/2}·½ + A_1·1 = κ/4 + (2−κ)/4 = ½ = ρ` ✔. Both load-bearing features carried verbatim: the
informed mark strictly outside the reach of uninformed-plus-noise (`2z̄ > 0 + z̄`) pinning the
endpoints at every `κ`, and the share being exactly `½`, *"which is what the word 'symmetric' in
Assumption A(τ) carries"*.

*Example A′* (the `π̄`-free family, tex 772–789) is also exact: `A_1 = A_0 = α − cκ`,
`A_{1/2} = 1 − 2α + 2cκ`, `A'_κ = −c`, with `α = 0.4`, `c = 0.3`. I checked the arithmetic myself —
the three weights are `0.4 − 0.3κ ∈ [0.1,0.4]` and `0.2 + 0.6κ ∈ [0.2,0.8]`, all inside `[0.1,0.8]`,
summing to 1; and `ρ = A_{1/2}(π̄/2) + A_1π̄ = π̄[0.1 + 0.3κ + 0.4 − 0.3κ] = π̄/2`, `κ`-free as
claimed. The likelihood display `eq:L3-likelihood` and the Bayes return `P(a=1|i) = π_i` match the
source exactly.

**The no-disclosure structure (Step 17) — transcribed exactly.** The mark `z̄` against `0` with
`ρ ∈ (0,1)`; `X_0 ∈ {−z̄,0,z̄,2z̄}`. The table `eq:L3-exampleB` is row-for-row identical to the
source's, including both contributing-mass columns and both interior posteriors
`π_∓`. **Four atoms** ✔. The monotonicity argument is verbatim and I checked it: the likelihood ratio
at `X_0 = 0` is `(κ/2)/(1−κ)`, strictly increasing on `(0,1)`, so `π_−` rises; at `X_0 = z̄` it is
`(1−κ)/(κ/2)`, strictly decreasing, so `π_+` falls. **The two-term derivative** `eq:L3-twoterm`
matches the source display exactly, with the underbrace labels reworded from *"the term A(τ)
keeps"* / *"…has no room for"* to *"the term the representation keeps"* / *"…it has no room for"* —
avoiding a card ID inside a display, same content. The follow-through is complete: the second sum
generically nonzero; the first sum *not* proportional to `C_h(π̄)`, being
`Σ_i A_i'(h−ℓ_h)(π_i)` over four atoms; and the identification of the structure as the frozen
manuscript's own, with *"Step 9 transfers to that structure; Step 8's clean proportionality does
not."*

Two thinnings here, both correct. The source's explicit posterior list
`{0, π(−1,0), π(0,0), π̄}` and its symbols `p_0`, `p_1` are dropped — those are draft_v2 symbols the
card does not carry, and card §8 rule 2 forbids citing IDs the card lacks, so dropping them is
required, not optional. And the source's closing *"That is a limitation of A(τ), stated here rather
than discovered later"* is dropped, its substance carried by the preceding sentence.
**OK-RESTRUCTURED.**

**Step numbering — the card's pointer resolves; here is exactly how far the 1:1 goes.** Tex Steps
**16, 17 and 18 land on their source numbers**, so **the card's "L3 Step 18's (S1) and (S2)" pointer
(MODEL_CARD.md:360) resolves exactly**, which is what the repair was for. The alignment is not an
accident and it is worth recording how it is achieved: promoting the source's unnumbered "Step 8′"
to a numbered tex Step 9 pushes everything down by one, and merging the source's Steps 14 and 15 into
tex Step 15 pulls it back, so the offset cancels precisely at 16.

The consequence is that the 1:1 holds **from Step 16 onward, not throughout**: tex Step 14 is the
source's Step 13, and tex Step 15 merges the source's Steps 14, 15 and 19. I checked every card
pointer into L3's proof against this. Steps 16–18 ✔ resolve; "Part IV, Steps 16–18" (§5 A(τ) and §9
item 1) ✔ resolves; "Hypothesis 8" and "Hypothesis 1" (§5 A(τ)'s (τ-i)/(τ-ii) clauses) are hypothesis
IDs, not step numbers, and are unaffected. **One pointer still does not resolve:
`proofs/L3_proof.md` Step 19**, cited twice — at §4.4's `π̄` row (the binding upper-support-point
ruling) and at A(br)'s (br-iv) — because source Step 19 is folded, unnumbered, into tex Step 15's
closing. This is the residue of **P-3**, now reduced from *"Steps 16–19 have no in-paper anchor"* to
*"Step 19 only"*, and its content is carried in two places
(`proofs_core_lemmas.tex`:716–724 and `model_section.tex`:650–652). **MISCITED, non-blocking**, and
noted so the record is exact rather than rounded up to "fixed".

**Internal cross-references — all correctly re-pointed.** I checked each of the six references the
new material makes into earlier steps: *"The moment check of Step 15"* (source said Step 14 — tex 15
carries `eq:L3-equiv` and the moment definition ✔); *"By Step 15 it suffices"* ✔; *"By Step 16 that
decomposes"* ✔; *"Step 17 fails (S1) and (S2) simultaneously"* (source: "Example B fails" ✔);
*"by Step 9 it equals `Σ_i A_i'(h−ℓ_h)(π_i)`"* (source: "by Step 8′" — and tex Step 9 at line 610–612
does carry exactly that formula ✔); *"the coefficient pattern (+1,−2,+1) that Step 8 factors"* ✔.

**No circularity, and the bridging paragraph's claim is true.** Lines 726–729 say the three new steps
*"fix the assumption's domain … none of them is used in the derivation of parts (a)--(c) above."* I
verified this: parts (a)–(c) are delivered at Steps 8, 6 and 12–13, none of which cites 16–18, and
every citation the new steps make runs backwards (18→15, 18→16, 17→9, 16→15, 16→8).

**Declared deviation (a) — the "second place with an unverified domain" sentence. CARD-FAITHFUL, and
required.** The source's Step 18 closes: *"**Declared OPEN.** It sits next to the A7-satisfiability
question as the second place where a maintained hypothesis of this model has an unverified domain,
and it is load-bearing for L3, L4 and T1 jointly."* The tex replaces the first clause and keeps the
second, sharpened: *"…it is load-bearing for this lemma, for leg 3 of Lemma L4 and for Part (B) of
Theorem T1 jointly."*

The removal is not optional. The source sentence predates ticket 24, and the card's post-ticket-24
state contradicts it twice: §5's A7 note records **"Satisfiability is resolved for A7′"**, and §9's
preamble records *"A7 satisfiability … is now **resolved** (§5's A7 note, ticket 24)"*. Card §9 item 1
then makes A(τ)'s domain not the *second* such place but **"the largest single conditionality the
ledger carries."** Keeping the source sentence would have put a stale claim in the paper that the
card's own §5 and §9 refute. The replacement's scoping to leg 3 and Part (B) matches card §9 item 1
and the A(τ) note exactly. And the A7-adjacent question that *does* remain open — incentive
compatibility, card §9 item 2 — is carried separately and correctly at `sec:not-claimed` item (2),
so nothing was lost by the removal. **Card-faithful.**

**Declared deviation (b) — the added `rem:AtauRecord` pointers. CARD-FAITHFUL; the count is two, but
they do two different jobs and the declaration describes only one.** I grepped: exactly **two**
`rem:AtauRecord` references inside 726–883, at lines 855 and 876.

- **Line 876** is the one the declaration describes. It maps the measured failures onto the two
  conditions: *"Remark~\ref{rem:AtauRecord} records a support carrying 23 to 767 distinct posterior
  values with no mass at `π̄/2` at any node, **which is (S1)**, and interior atoms that move with `κ`
  at a two-sided Hausdorff distance reaching 0.4608 between adjacent-`κ` support sets, **which is
  (S2)**."* This is **MODEL_CARD.md:360**'s own claim — *"This refutes L3 Step 18's (S1) and (S2)
  together at this calibration"* — decomposed onto which measurement hits which condition. Both
  attributions are correct against the (S1)/(S2) just defined: 23–767 distinct posteriors with no
  mass at `π̄/2` refutes both halves of (S1); interior atoms moving with `κ` refutes (S2)'s
  `κ`-free likelihood ratio. The tex says the two are *"refuted together"*, matching the card's
  "together", and adds *"That is applicability evidence at one calibration and it moves no label"* —
  the card's own label discipline. **Card-faithful.**
- **Line 855 does a different job and is not covered by the declaration.** Tex Step 18's second
  paragraph argues that the two-round structure is where an endpoint below one could come from —
  which restates a conjecture the card records as **false**. The writer guards it in place:
  *"Whether it does so is a separate question from whether it could, and the answer at the
  implemented calibration is that it does not: Remark~\ref{rem:AtauRecord} records `π̄ = 1` at every
  non-degenerate node there, because unflagged Voice types still generate fully revealing pooled
  order flows. The conjecture that the two-round timing leaves the pooled cell with a top atom
  strictly below one is therefore false at that calibration, and nothing below rests on it."* This is
  card §5's `π̄`-half bullet almost word for word — *"that step's conjecture that 'the two-round
  timing … leav[es] the pooled cell with a top atom strictly below 1' is false at this
  calibration — unflagged Voice types still generate fully revealing order flows"* — attached at the
  very step the card names. **Card-faithful, and load-bearing:** without it the transcription would
  have imported a conjecture into the paper that the card has already recorded as refuted. The
  declaration's undercount is a description gap, not a text defect. **MISCITED (declaration), text
  card-faithful.**

**New labels — collision-free.** `eq:L3-exampleA`, `eq:L3-likelihood`, `eq:L3-exampleB`,
`eq:L3-twoterm` follow the file's `eq:L3-` prefix convention. I ran a duplicate check over every
`\label{...}` in all six files: **no duplicates anywhere**, and the compile reports zero undefined
references, so no forward reference is broken either.

**One compression, verified.** The source spells out the weight sum
`(2−κ)/4 + κ/2 + (2−κ)/4 = (4−2κ)/4 + κ/2 = 1`; the tex writes *"summing to one"*. I checked the
arithmetic: correct. **OK-RESTRUCTURED.**

---

## R-2 · `theorem_section.tex`:126–131 and :450–452 — **PASS; M-4a closed at both sites**

The openness paragraph now splits the attribution (lines 126–131):

> the discussion after Assumption~\ref{asm:Atau} shows that the support condition is the assumption's
> entire remaining bite, and exhibits a one-round market that satisfies it and a no-disclosure
> structure that does not; **the weakest sufficient conditions for the two-round case are named in
> the closing steps of the proof in Section~\ref{sec:proofs}.**

**The redirect is accurate.** (S1)/(S2) are named at `proofs_core_lemmas.tex`:865–870, in Step 18 —
the last step of the L3 proof, inside `proofs_core_lemmas.tex`, which is `\input` under
`\section{Proofs}` / `sec:proofs`. *"The closing steps"* is a true description of Steps 16–18. And the
first half remains true: `model_section.tex`:451–459 does show the bite is the support condition and
does exhibit both structures. Both halves of the sentence now point at content that exists.

**Line 452's Lemma-attribution is now true as written.** The `sec:not-claimed` item (1) sentence
attributes all four verbs to Lemma L3 rather than redirecting, so I checked each against the L3 proof
as it now stands: *"shows that the entire remaining bite … is its support condition"* → Step 15 ✔;
*"exhibits a one-round market that satisfies it"* → Step 16 ✔ (newly true); *"and a no-disclosure
structure that does not"* → Step 17 ✔ (newly true); *"names the weakest sufficient conditions for the
two-round case"* → Step 18 ✔ (newly true). Before the repair only the first was true of the Lemma.

Worth recording: this now matches **card §9 item 1's own attribution**, which credits all four to L3
(*"L3 proves the representation's entire remaining bite is the support condition, exhibits a
one-round market that satisfies it and the frozen manuscript's own no-disclosure structure that does
not, and declares the two-round case open with the weakest sufficient conditions named"*). The paper
and the card now say the same thing about the same object. **M-4a closed.**

---

## R-3 · `theorem_section.tex`:402–405 (`prop:C1` closing) — **PASS; T-10 closed, and it exceeds the fix I proposed**

New text:

> The sign-coherence hypothesis --- that the fixed-policy attenuation sign agrees with the
> equilibrium sign --- is confirmed unused in \eqref{eq:C1}: its work is one of naming, fixing when
> that conclusion may be called a survival of the fixed-policy sign. The sign-constancy clause of
> Assumption~\ref{asm:AGE} is likewise unused.

Checked against `proofs/C1_proof.md`:141–148, whose H8 reads
*"`sgn(∂_κΔ^act(k(ϑ),ϑ)) = sgn(dΔ^act(k(κ,r),κ,r)/dκ)` on `R_r`: **the fixed-policy and equilibrium
liquidity derivatives point the same way.** Card §4.5 defines `g_r^PE` with the **equilibrium** sign
but calls it the *fixed-policy* attenuation margin; H8 is exactly the clause that makes both halves
of that name true at once. The boxed conclusion (C) does **not** use H8 — Step 9 is where it is
consumed, and Step 9 is a statement about what (C) may be called."*

- **Names H8 by content:** ✔ *"the fixed-policy attenuation sign agrees with the equilibrium sign"*
  is H8's own sentence.
- **Carries H8's naming role:** ✔ *"its work is one of naming, fixing when that conclusion may be
  called a survival of the fixed-policy sign"* is the source's *"Step 9 is a statement about what (C)
  may be called"*. I did not propose this half; the writer added it, and it is what makes the
  sentence informative rather than merely corrected.
- **Discharges AGE separately, under the right name:** ✔ a second sentence, and it says
  **sign-constancy**, not "sign-coherence" — AGE has no clause by the latter name, which was the
  original defect.
- **Matches the card:** ✔ card's *"confirmed unused in the boxed conclusion"* → *"unused in
  \eqref{eq:C1}"*, and `eq:C1` **is** the boxed conclusion; the evidence chain's "H8 unused" is now
  correctly targeted.
- **Matches the proof:** ✔ `proofs_theorem_ge.tex`:713–724 (unmoved) separates the same two objects
  in the same order and assigns the same naming role. Statement and proof now agree.

**T-10 closed.**

---

## R-4 · `proofs_theorem_ge.tex`:17 and :434 — **PASS; F-2 closed**

Both run-ins are now ID-only: `[Proof of Theorem~\ref{thm:T1} (T1)]` and
`[Proof of Proposition~\ref{prop:C1} (C1)]`. All eight proof headings across the three files now use
the same ID-only form, which is a consistency gain over the mixed convention I recorded at **P-13**.

**Fresh four-pass compile, run by me from the repo root after deleting every aux artifact**
(`standalone_v3.{aux,bcf,bbl,blg,log,out,run.xml,pdf}`), exactly the contract's sequence:

| Check | Result |
|---|---|
| `grep -in undefined standalone_v3.log` | **0 hits** |
| `grep -n "^!" standalone_v3.log` | **0 hits** |
| `grep -n "Overfull\|Underfull" standalone_v3.log` | **0 hits** — the box is gone |
| `standalone_v3.blg` warnings/errors | **0** |
| Exit code | 0 |
| Output | **61 pages** (was 58; +3 from L3 Part IV) |

Gate (e) passes with a strictly cleaner log than at the original pass, which carried one overfull box.

---

## R-5 · `sections_v3/v3_macros.tex` — **PASS on provenance (M-10 closed); hardening is correct, with two one-line residuals**

**Provenance (M-10).** Header now reads *"transcribed verbatim from
`research/model_v4/model_v4.tex` **lines 42-51** (card stamp **2026-08-27**)."* Both corrections
match what I verified: the macro block is `model_v4.tex`:42–51, and the note carries stamp
2026-08-27. **M-10 closed.**

**The hardening (F-1) — judged in both directions, as asked.** `\Tmap` is now plain `\newcommand`,
with a comment saying the collision must fail loudly rather than merge silently.

- **Standalone driver: behaves as the comment claims. Verified empirically, not by reading.**
  `standalone_v3.tex` contains no occurrence of `Tmap` (checked), and no package it loads defines
  one, so `\Tmap` is undefined when `v3_macros.tex` is `\input` and plain `\newcommand` binds it to
  `\mathcal{T}`. The decisive evidence is R-4's compile: exit 0, **zero `^!` lines**, 61 pages. Had
  the name been pre-defined, `\newcommand` would have raised `! LaTeX Error: Command \Tmap already
  defined.` It did not. ✔
- **A draft_v3 carrying draft_v2's guard: behaves as the comment claims.** `draft_v2.tex`:54 is
  `\providecommand{\Tmap}{T}`, in its preamble, so in a draft_v2 copy `\Tmap` is defined before any
  body `\input` reaches `v3_macros.tex`. `\newcommand` on an already-defined control sequence is a
  hard LaTeX error, so the build stops rather than silently merging. ✔
- **Is failing loudly the right call?** Yes, and it is the correct answer to F-1. The previous
  `\providecommand` guard converted a semantic corruption into a *clean-compiling* PDF in which the
  outer best-response map renders as the filing window — invisible on inspection. The new binding
  converts it into a build-time stop that ticket 18 must resolve consciously, and the comment
  forecloses the lazy fix (*"it is not free to silence the error by re-adding a guard"*). The
  contradiction with card §4.5 and §8 rule 4 is named in the comment itself. **Good hardening.**

Two residuals, both one line, neither blocking:

1. **The comment's "104 uses" is now 107.** I re-counted: `\Tmap` appears **107** times across the
   six section files; the L3 Part IV addition added three. The 104 figure is the one I supplied in
   this report before that repair landed. Trivial, but it is a number in a comment that a future
   reader may take as current. **MISCITED.**
2. **The loud failure depends on an `\input` ordering the comment states but does not defend.** It
   holds only if `v3_macros.tex` is `\input` **after** draft_v2's macro block — which the comment
   assumes (*"`\Tmap` is already defined by the time this file is `\input`"*) and which is the normal
   arrangement, draft_v2's block being preamble. Under the reverse ordering the failure mode inverts
   silently: `\newcommand` binds `\mathcal{T}` first, draft_v2's `\providecommand` then no-ops by
   design, and draft_v2's own ~10 body uses of `\Tmap` render the filing window as the calligraphic
   outer map. That direction is not named. **One added sentence would close it** — e.g. "this
   requires that `v3_macros.tex` be `\input` after draft_v2's macro block; loading it earlier makes
   draft_v2's `\providecommand` no-op silently and corrupts draft_v2's own uses instead."
   **MISCITED.**

F-1 itself remains **open by design**: the hardening makes the collision impossible to miss, but
ticket 18 must still rename one of the two `\Tmap`s.

---

## Delta summary

| # | Repair | Verdict |
|---|---|---|
| 1 | L3 Part IV (Steps 16–18) — the only substantive new content | **PASS at full grain.** (S1)/(S2), Example A (incl. `A'_κ = −¼`), Example A′, Example B and the two-term derivative all transcribed exactly; both declared deviations card-faithful; labels collision-free; no circularity |
| 2 | Openness paragraph redirect + `sec:not-claimed` item (1) | **PASS.** Redirect accurate; the Lemma-attribution is now true as written and matches card §9 item 1. **M-4a closed** |
| 3 | `prop:C1` closing sentence | **PASS.** Names H8 by content, carries its naming role, discharges AGE's constancy clause separately and correctly. **T-10 closed** |
| 4 | ID-only run-ins at `proofs_theorem_ge.tex`:17, :434 | **PASS.** Fresh four-pass compile: 0 undefined, 0 `^!`, **0 Overfull**, biber clean, 61 pages. **F-2 closed** |
| 5 | `v3_macros.tex` provenance + `\Tmap` hardening | **PASS.** **M-10 closed**; hardening verified correct in both directions, empirically for the driver. Two one-line residuals (stale "104"→107; reverse-`\input`-ordering case unnamed) |

**Findings closed by this round:** M-4a (both sites), T-10, M-10, F-2. **Narrowed:** P-3, from
"Steps 16–19 have no in-paper anchor" to "Step 19 only". **New:** two MISCITED, both in the
`v3_macros.tex` comment (R-5). **Unchanged and still open by design:** F-1, for ticket 18.

**No repair introduced a WRONG, weakened a label, or added an unsourced claim.** The five landed
edits touch four files; I re-read every changed region in full and re-ran every gate.

### UPDATED OVERALL VERDICT: **LAND** — no WRONG findings, before or after the repair round; gate (e) now passes with a fully clean log (0 undefined, 0 errors, 0 overfull, 61 pages).
