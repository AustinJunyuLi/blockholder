# 01 — Correspondence-route exploration: can Kakutani replace A3 and A6 in P1?

**Type:** research

**Status:** resolved

**Blocked by:** —

**Question.** Map the correspondence-based existence route precisely enough to rule GO / NO-GO /
GO-WITH-CHANGES on a proof campaign. The route as sketched on file: treat the outer best response
as a correspondence (dropping A6's single-valued continuity and A3's ordered-argmax input to it),
run Kakutani on the t-constrained game (the fixed full-support perturbation at scale t — the
implementation's `OFF_PATH_EPS` is this game at t = 1e-14), and take t ↓ 0. Deliverables, in the
ticket answer and nowhere else:

1. **The obstacle list**, each obstacle stated as the mathematical claim that would have to be
   proved, with its current status on file (established / sketched / open): non-emptiness,
   convexity, and upper hemicontinuity of the best-response correspondence on Θ at fixed t; the
   fixed-point survival through t ↓ 0 (what object survives, and in which equilibrium notion);
   the boundary κ ∈ {0,1} under the extension reading; sequential optimality of the flagged
   component when the pooled layer is correspondence-valued; measurability/selection at the end.
2. **What each obstacle needs** — the weakest additional hypothesis or the proof technique, and
   whether it re-imports anything the implemented calibration violates (the test: the final
   hypothesis set must be satisfied by the implemented menu and calibration, or the route buys
   nothing).
3. **The A3 question separated from the A6 question**: if the route absorbs the discontinuity but
   not the empty-selection loci, say so and name the weakest A3 replacement.
4. **The verdict**: GO (campaign tickets proposed, each a child of this effort with its own
   statement-to-prove), NO-GO (the obstacle that kills it, stated as the counterexample class or
   the missing mathematics), or GO-WITH-CHANGES (the changed target statement).

**Sources** (read-only; no card writes, no git): `research/model_v4/proofs/P1_proof.md` (Step 18
and the h.6/h.16 machinery), `research/model_v4/MODEL_CARD.md` (§3, §5 A3/A5/A6 notes, §9
item 4), the A6 panel pair in `threads/`, `rederive/P1_rederivation_2026-08-25.md`,
`sections_v3/proofs_existence.tex` (the paper-form Step 18 scope note), and the numerical record
(`quality_reports/fixes/t2_a6_*.json`, `t2_t34_account_sweep.json`) as the ground truth on what
the implemented map actually does at the edges.

**Discipline.** Everything CONJECTURE-grade. Claim the ticket (Status: claimed) before working;
resolve it (append `## Answer`, set Status: resolved) when done; append a one-line pointer to the
map's Decisions-so-far. Do not write the proof; do not touch the card, mirrors, sections, or
ledgers.

## Comments

## Answer

**Filed 2026-08-29 by the route-exploration agent. Everything below is CONJECTURE-grade.** No proof
was written; no card, mirror, section or ledger was touched; no git was run. Three probes were
executed read-only against `numerical_v4/` (each monkeypatches `_alive_weights` in memory and
restores it; nothing under `numerical_v4/` is modified on disk) and are **analysis-grade, not
curated t2 checks** — new evidence, single-pass, not independently reproduced, labelled as such
wherever they are cited. They are filed at
`quality_reports/fixes/p1_route_probes_2026-08-29/` with a README carrying their caveats, on the
`a6_panel_probes_2026-08-27/` precedent, because §4's verdict cites their numbers.
**They are new untracked files for the orchestrator to commit or discard; this ticket ran no git.**

### 0. Headline

The route removes **A6's continuity clause** and cannot remove **A3**. Step 18's correspondence is
`nonempty by h.3` — the words are in both the proof (`proofs/P1_proof.md` Step 18, line 957) and the
paper form (`sections_v3/proofs_existence.tex` line 903, "nonempty by Assumption A3"). The route
*assumes* A3; it does not derive it and cannot be made to. And A3's monotone-selection clause is
measured false **at a located fixed point** of the implemented map, under **every** off-path belief
family and **every** perturbation scale tested. So the effort's stated prize — existence freed of
*both* assumptions the calibration violates — is not available on this route. Half of it is, with
measured support, and that half is worth a campaign.

Note also that "P1 without A6" was never the right description of the best case: A6 has three parts,
and Steps 13–15 split them. Step 13 **derives** the self-map and ordering halves; Step 14's
**bracket** is assumed and Step 18 explicitly does not remove it; only Step 15's continuity is what
Kakutani buys. The honest best case is *P1 with A6's continuity clause deleted and derived, A6's
bracket clause retained, A3 retained*.

---

### 1. The obstacle list

Each obstacle is the claim that would have to be proved, with its status on file.

**O-1 — Nonemptiness of the best-response correspondence at fixed `t`.**
*Claim to prove:* for every `k ∈ Θ`, the pointwise argmax `s ↦ argmax_j U_j(s;k)` admits a weakly
increasing selection, i.e. `𝒮(k) ≠ ∅`.
*Status:* **OPEN, and measured FALSE at the implemented calibration.** This is exactly A3's second
clause — the clause Step 13 consumes — so it is not an obstacle the route can absorb; it is A3
wearing the correspondence's clothes. Both Step-18 texts concede it by citation. Measured failure:
card §5's A3 note, loci (i) and (ii); and see §3 below, where this exploration's probes change what
is known about locus (i) and confirm locus (ii).

**O-2 — Convexity of the values.**
*Claim to prove:* `𝔗(k)` is convex for every `k ∈ Θ`.
*Status:* **SKETCHED, and Step 18's one-line argument is not sufficient as written.** Step 18 says
the values are convex "because at an indifference plateau the admissible values of a component form
an interval and the ordering constraints cut the product of those intervals by half-spaces" — which
presumes the feasible set *is* a product of intervals. Worked through here:

- Write `j_{k'}(s) = 1 + N(s)` with `N(s) = #{i : k'_i ≤ s}`. Because `Θ`'s coordinates are
  **ordered**, the indicator vector of `{k'_i ≤ s}` is "the first `N` coordinates", so for
  `k^λ = λk' + (1−λ)k''` one gets `N^λ(s) ∈ [min(N',N''), max(N',N'')]` pointwise. Hence if
  `A(s) := argmax_j U_j(s;k)` is a **contiguous** set of plan indices for a.e. `s`, then
  `1 + N^λ(s) ∈ A(s)` and convexity follows. That is the missing hypothesis, and it is what makes
  Step 18's sentence true.
- Without contiguity convexity genuinely fails. Witness (`J = 3`): suppose `A(s) ⊇ {1,2}` on
  `(0,10)`, `A(s) ⊇ {1,3}` with `2 ∉ A(s)` on `(10,20)`, `1 ∈ A` below 0 and `3 ∈ A` above 20. Then
  `k' = (0,10)` and `k'' = (20,20)` are both feasible, but `k^{1/2} = (10,15)` assigns plan 2 on
  `(10,15)`, where plan 2 is strictly dominated. `𝔗(k)` is not convex.
- **Answer to the map's fog question as posed** ("two candidate cutoffs on either side of an `n(s)`
  edge — is the segment between them a best response?"): at a clean jump edge the answer is sharper
  than non-convexity. Where `U_H − U_V` **jumps through zero without crossing**, the argmax is a
  singleton on each side and the up-set boundary is the edge itself, so that coordinate of `𝔗(k)`
  is the **singleton `{edge}`** — convexity is trivial there. Where the argmax is **non-monotone**
  (loci (i) and (ii)) no cutoff vector is a best response at all and `𝔗(k) = ∅` — the set is
  **empty, not non-convex**. Convexity is simply not where the jump edges bite; O-1 is.
- *Re-import test:* contiguity of the argmax is **UNCHECKED at the implemented menu**. On the
  `J = 3` Exit/Hold/Voice menu the failure shape would be `{Exit, Voice}` optimal with Hold strictly
  dominated — not exotic, given `numerical_v4/params.py`'s `C0 = 0.014` is tuned to the Hold-collapse
  boundary. Cheap to probe.

**O-3 — Upper hemicontinuity / closed graph at fixed `t`.**
*Claim to prove:* `graph 𝔗` is closed in `Θ × Θ`.
*Status:* **ESTABLISHED in outline, and at a strictly weaker hypothesis than Step 18 claims.** Step
18 routes this through the maximum theorem and therefore demands **joint** continuity of `U_j` in
`(s,k)` — Step 15(i), which fails on this menu independently (`n(s)` is integer-valued;
`numerical_v4/solver.py:30–31`'s `N_GRID` note). That demand is avoidable. Take `k_n → k`,
`k'_n ∈ 𝔗(k_n)`, `k'_n → k'`. Fix any `s` off the finitely many components of `k'`: for large `n`,
`j_{k'_n}(s) = j_{k'}(s)` because `k'_n → k'` and the assignment is a step function; so
`U_{j_{k'}(s)}(s;k_n) ≥ U_j(s;k_n)` for every `j`, and passing to the limit needs only **continuity
in `k` at fixed `s`** — never continuity in `s`. The exceptional `s` form a finite, `Φ_s`-null set
where card §3(i) pins no convention (Step 17(i) already says so). So closed graph holds **provided
the correspondence is defined with `Φ_s`-a.e. pointwise optimality**, and the `s`-direction
discontinuity is irrelevant to it.
*What supplies the `k`-continuity:* the fixed-`t` game. At stage `n` the denominator is
`Z_n = (1−t_n)Λ_k + (t_n/J)Λ_u ≥ (t_n/J)Λ_u > 0` at every reachable history and `Λ_k` is continuous
in `k`, so the whole price system is continuous in `k` (`proofs/P1_proof.md` Step 9(b), the `Z_n`
display; panel **defuse** brief item 3; card §5's A6 note parenthetical "at fixed `n` the system is
continuous in `k`"). **Citation correction for the dispatch:** that claim is *not* in the `t2_a6_*`
JSONs — those record only the `t = 0` jumps. It is in the panel brief and the card note.
*Measured here for the first time (probe C, `t_blend_settle.py`):* across the `edge(8) = 1.583333333`
hyperplane at `(κ=0.5, τ₅₀, T=5)`, the shipped map steps `𝒯₂` by **6.334e−3 across a 1e−8 bracket**
(`1.5497289514 → 1.5433951704`), while a genuine continuous `t`-blend at `ε = 1e−6` steps by
**6.8e−6 across the same bracket** (`1.5433965447 → 1.5433897638`) and spreads the same total move
(5.7e−3) monotonically over a window of order `1e−5`. A **~930× reduction in the local step at a
fixed bracket**, consistent with continuity and inconsistent with a jump. This is the route's
positive claim, and it now has a measurement behind it at the very locus where the card records A6
failing.

**O-4 — Fixed-point survival through `t ↓ 0`.**
*Claim to prove:* the limit of fixed points of the `t`-constrained games is an equilibrium of the
unconstrained game.
*Status:* **OPEN — and this is where the route's honesty cost sits.** What is straightforward: `Θ`
is compact, so a sequence `k^{t_n}` of fixed points has a convergent subsequence `k^{t_n} → k⁰ ∈ Θ`.
What `k⁰` **is** is the hard part.
- Write `θ_t(k) = (1−t)Λ_k / [(1−t)Λ_k + (t/J)Λ_u]` for the weight the perturbed belief puts on the
  Bayes component at a history `h`. Each `θ_t` is continuous in `k`; the pointwise limit is
  `θ_0(k) = 1{Λ_k > 0}`, discontinuous exactly on `⋃_h ∂{k : Λ_k(h) > 0}`. **The convergence is not
  uniform**, and that is the order-of-limits problem the A6 panel named: the discontinuity is
  *created* by `t → 0`, so the two limits do not commute and no choice of family fixes it.
- Consequently the belief at a frontier history along `(t_n, k^{t_n}) → (0, k⁰)` is a blend
  `θ ∈ [0,1]` of the Bayes-concentration belief and the plan-uniform belief, with `θ` determined by
  the **rate** `Λ_{k^{t_n}} / t_n` — a property of the sequence, not of `k⁰`.
- **What the limit point therefore is:** an assessment that is *consistent* in the Kreps–Wilson
  sense — beliefs are limits of Bayes beliefs along fully mixed strategies converging to the limit
  strategy, with the **cutoff vector trembling as well as the plan mixture**. It is an **exact**
  equilibrium under that reading, **not** an ε-equilibrium; the loss is entirely in item (vi), not
  in optimality. But it is **not** an equilibrium under §3(vi) as P1's row currently reads it —
  "**one** full-support perturbation family … **fixed once** and used to define the price system at
  every `k ∈ Θ`" — because no `k`-independent family reproduces the sequence-indexed blend. That
  clause was folded in on 2026-08-25 to close re-derivation N6, and Analyst A's brief already
  identifies it as the clause that pins the `k`-freeness.
- **The escape that would make this harmless is refuted by the numerical record.** If the limit
  landed in a chamber interior, `Λ_{k⁰} > 0` at every relevant history, `θ = 1`, Bayes, no problem.
  But the located fixed points sit **on** the edges: `k₂ = 1.6590621627` to `1.06e−12` at node 15
  (`t2_a6_node15_check.json`), and the ticket-34 sweep found pins at `1.460178993` (offset `~1e−13`)
  and `1.517932397` (offset `~1e−12`) (card §5 A3 note, sweep note). Carry the card's own hedge:
  neither pin is its node's achieving basin, and existence at those nodes is neither claimed nor
  denied — they refute the interior-limit escape without being claimed as equilibria.

**O-5 — The boundary `κ ∈ {0,1}`.**
*Claim to prove:* the constrained game and its limit are defined at both endpoints.
*Status:* **ESTABLISHED, no separate treatment needed.** Step 9's perturbation is over **plans
only**; nature's noise law is untouched. So at `κ = 0` (support `{0}`) and `κ = 1` (support
`{±z̄}`) a history requiring an unavailable mark is null under **every** plan profile at **every**
`t`, hence off nature's path rather than the players', carrying no §3(vi) requirement — Step 9(a)'s
reachable-set definition and Step 9(d)'s extension reading transfer verbatim, and Step 9(c)'s
reference-belief convention covers the rest. The extension route survives; no cut to `κ ∈ [0,1)` is
reintroduced. **Low risk.**

**O-6 — Sequential optimality of the flagged component when the pooled layer is
correspondence-valued.**
*Claim to prove:* Step 12 survives unchanged.
*Status:* **ESTABLISHED.** Step 12 is **`k`-free end to end**. Step 12(a): the belief at
`σ_F(j',s)` is the point mass at `(j',s)` (Step 10, A7-J), so `v̂ = μ_v + β(s − μ_v)` — a function
of `s` alone — and `π = 1` on the flagged cell, hence
`P^F(σ_F(j',s)) = 𝒢_F(v̂(s)) =: P^F(s)` for every class member: **the price-invariance lemma the
dispatch asked about survives unchanged, and it is `k`-free, not merely `k`-continuous.** Steps
12(b)–(d) then cancel every `Q^F` and `b*` term and h.16 closes the cost, all without touching the
pooled layer. Uniqueness of the inner root, which makes `P^F(s)` a number rather than a selection,
comes from `m₀ ≥ 0` (Step 7) — not from A5, A6 or A3. Corroborated independently: card §5's A6 note
("the flagged layer is `k`-free under A7-J") and Analyst A §1 ("All of it is in the finite pooled
price vector. The flagged layer is `k`-free"). Making the **outer** map correspondence-valued
therefore cannot disturb Step 12.

**O-7 — Measurability and selection at the end.**
*Claim to prove:* the fixed point yields a measurable strategy and a measurably selected price
family.
*Status:* **ESTABLISHED, nothing new needed.** Kakutani returns a **cutoff vector**, so the plan map
`j_{k⋆}` is a step function and Borel by construction; the flagged family's measurable selection is
already delivered by A7-J plus §4.2's Borel clause at Step 6(c)–(d) (h.17-b), not by A5. **Low
risk.** The one wording consequence is O-3's: the conclusion carries `Φ_s`-a.e. optimality rather
than everywhere-optimality, which Step 17(i) already concedes is all card §3(i) pins.

---

### 2. What each obstacle needs, and whether it re-imports a violated hypothesis

| # | Weakest additional hypothesis / technique | Re-imports something the calibration violates? |
|---|---|---|
| O-1 | `𝒮(k) ≠ ∅` for every `k ∈ Θ` (A3's second clause, a.e. form). Nothing weaker keeps a *cutoff* conclusion — see §3. | **YES — this is the whole problem.** Measured false at a located fixed point under every family and every `t` (§3). |
| O-2 | Contiguity of `argmax_j U_j(s;k)` a.e. in `s`, for every `k ∈ Θ`. Proof technique: the ordered-coordinate lattice argument above. | **UNKNOWN — UNCHECKED at the implemented menu.** Not measured by any probe on file. |
| O-3 | Fixed `t > 0` and the a.e. definition of `𝔗`. Continuity in `k` at fixed `s` is then **derived** from Step 9(b)'s `Z_n ≥ (t/J)Λ_u > 0`, not assumed. **Step 15(i)'s joint continuity is NOT needed** and should be dropped from Step 18's statement. | **NO.** This is the route's genuine purchase: it retires the one clause the calibration measurably breaks (§5 A5 clause (ii) + A6 continuity, which "fail together, at one locus"), and probe C measures the repair working. |
| O-4 | Either (a) re-word §3(vi) to Kreps–Wilson consistency (trembles in cutoffs as well as plans), or (b) prove the limit lands where `Λ_{k⁰} > 0` at every relevant history. | **(b) re-imports a chamber-interior condition the record refutes** — the located fixed points sit on the edges. (a) is a **definitional change to §3(vi)**, i.e. Austin's call, not a proof step. |
| O-5 | None. Step 9(a)/(d) as written. | **NO.** |
| O-6 | None. Step 12 unchanged; A7-J and `m₀ ≥ 0` as already carried. | **NO.** A7-J is satisfied by the pinned pro-rata single-Voice menu (`proofs/A7_construction.md`, ticket 24). |
| O-7 | None. A7-J + h.17-b, as already carried. | **NO.** |
| — | Step 14's **bracket** (A6's surviving half). | Unchanged by the route; still assumed at the card's generality, still derivable in the four-action specialisation. |

The hard test the dispatch set — *the final hypothesis set must be satisfiable by the implemented
menu and calibration* — is passed by O-3, O-5, O-6, O-7; is unknown for O-2; and is **failed by
O-1**, which is A3.

---

### 3. The A3 question, separated from the A6 question

**The route absorbs the discontinuity and not the empty-selection loci.** Stated structurally, and
independent of any calibration: Kakutani cannot manufacture monotonicity. `𝔗(k)` is a set of
*cutoff vectors*, and a cutoff vector represents a weakly increasing step function by construction;
if the pointwise argmax is non-monotone on a positive-measure set, **no** cutoff vector is a best
response and the correspondence is empty, whatever the perturbation does to the beliefs. The two
ways out both change the conclusion rather than the hypotheses:

- **Enlarge the strategy space** to all measurable plan assignments (Fan–Glicksberg on behavioural
  strategies). Nonemptiness and convexity are then free — but the conclusion is a PBE, **not a
  cutoff PBE**, and every object downstream of §3 is cutoff-indexed (`Θ`, `𝒯`, `L_𝓡`, AGE's
  contraction, C1's `k̄_x`, Step 20's `s_F(k⋆)` threshold restatement). That is a different theorem.
- **Restrict the strategy space to cutoff rules** and take the best response *within* that class
  (an ex-ante-optimal cutoff vector). Nonemptiness is then free by compactness — but the fixed point
  is no longer **pointwise** optimal, so card §3(ii)'s date-0 optimality fails on a positive-measure
  set of `s`, exactly where the argmax is non-monotone. That is an equilibrium of a
  strategy-restricted game, and it would have to be declared as such.

**Weakest A3 replacement.** Precisely `𝒮(k) ≠ ∅` for every `k ∈ Θ`, in the `Φ_s`-a.e. form — "the
pointwise argmax admits a weakly increasing selection". A3's *first* clause (single crossing of
adjacent differences) is **not** needed by the route: Step 13 consumes only the second clause, and
a jump through zero without a crossing is compatible with single crossing anyway. So the campaign
can honestly drop half of A3. It cannot drop the other half, and the other half is the one that is
measured to fail.

#### New evidence from this exploration, and it cuts both ways

Three probes at `quality_reports/fixes/p1_route_probes_2026-08-29/` (`t_blend_a3_probe.py`,
`t_blend_diagnose.py`, `t_blend_settle.py`, with JSON beside each; **analysis-grade, single-pass,
mine alone, not gate-checked** — see that directory's README). Pre-registered
prediction: the A3 failure would be `t`-invariant. It was **falsified at locus (i)** and the
diagnosis is a finding in its own right.

**(a) `t` is irrelevant to the A3 pattern — the pre-registered mechanism claim holds.** At
`k₂ = edge(6) + δ` the dying type's alive mass is **exactly** `0.0` at `δ ∈ {1e−9, 1e−4, 2e−2}`
(measured), so Step 9(b)'s `k`-null case applies verbatim — `μ_n = L_jφ_s/Λ_u` **exactly and
`n`-free** — and every `t` returns the same reference belief. Confirmed by construction: switching
between the shipped hard switch and a continuous blend, at `ε ∈ {1e−14, 1e−9, 1e−6}`, **never**
changes the sign-change count. Continuity of the perturbation is not what moves this.

**(b) What *does* move it is the SHAPE of the off-path family, and here the implementation and the
card disagree.** `numerical_v4/pooled.py:225–235` floors every dead type at the **same**
`OFF_PATH_EPS = 1e-14`, i.e. **uniformly across types**. Card Step 9(b)'s plan-uniform limit is
`Λ_u(h) = Σ_{j'} ∫ L_{j'}(h|s')φ_s(s')ds'` — it integrates against the signal density, so it is
**mass-proportional**. The two agree exactly at a history exclusive to **one** dead type (the floor
cancels in the ratio — which is why Analyst A's `type_reference` verification and all three `𝒯₂`
jump measurements are unaffected). They disagree at a history reachable only by **two or more** dead
types, where one gives the equal-weighted average of the references and the other the
`φ_s`-weighted average. At the probed `k` five types are dead (7–11) and their line masses run
`0.031, 0.029, 0.027, 0.026, 0.742` — wildly unequal, so the disagreement is large. Measured:

| off-path family | sign changes of `U_V − U_H` at `k₂ = edge(6)+1e−4` |
|---|---|
| `switch_uniform` (**as shipped**), `ε = 1e−14 / 1e−9 / 1e−6` | **3** (excursion 2.69e−4) |
| `blend_uniform` (continuous), `ε = 1e−14 / 1e−9 / 1e−6` | **3** (excursion 2.69e−4) |
| `switch_massprop` (card-faithful), `ε = 1e−14 / 1e−9 / 1e−6` | **1** |
| `blend_massprop` (card-faithful + continuous), same `ε` | **1** |

So **locus (i) of card §5's A3 note does not reproduce under a Step-9(b)-faithful mass-proportional
family.** Stated at the grade it deserves: this is one `k`, one node, one single-pass probe, and my
`massprop` weight `Pr(n(s)=t)` is an approximation of `Λ_u` (it omits the Exit/Hold plans'
contribution and the `1/J` factor). It is **not** a claim that the card is wrong. It **is** a
concrete, cheap, falsifiable proposition that a landed evidence note may be measuring the
implementation's belief convention rather than the card's construction, and it should be verified
by someone who did not write it before anything is done with it. Related and separate: the card's
"the implementation's `OFF_PATH_EPS` = 1e-14 **is** the fixed-`t` constrained game" is, read
strictly, not what the code does — `if Wm[t] > 0.0: continue` is a hard switch at exactly-zero mass,
and the belief at an exclusive history is floor-size-independent, so the implementation faithfully
realises the **`t = 0`** card construction. The genuine continuous fixed-`t` game was **unmeasured**
before probe C. (Flagged for Austin; no card write from this ticket.)

**(c) Locus (ii) survives everything, and it is at a fixed point.** At `(κ=0.15, τ=0.05, T=5)`, at
the filed pinned point `k = (1.0202217805, 1.6590621627)`, the VOICE→HOLD argmax **reversal** across
edge `1.6590621627` holds in **8 of 8** variants — `{switch, blend} × {uniform, massprop} ×
{ε = 1e−14, 1e−6}` — with `U_V − U_H` running `+1.77e−3 / +2.39e−3 / +6.4e−4 / +1.90e−3` just below
and `−1.28e−3` just above in every case, and **5** sign changes over the bracket throughout. This is
the `s`-direction mechanism (`n(s)` integer-valued, so `B_VOICE(s,d)` steps in `s` —
Analyst B's own attribution, and `numerical_v4/solver.py:30–31`), and nothing in the belief family
or the perturbation scale touches it.

**The consequence for the route is decisive.** `𝒮(k) = ∅` at a `k` that is a **located fixed point**
of the implemented map. So the two escapes that would rescue O-1 are both closed: one cannot restrict
`Θ` to avoid the bad set (the bad set contains a fixed point, and the A6 note already records that a
chamber-interior `Θ` "cannot be exhibited without approximately locating the fixed point first" and
"no such chamber exists at the `κ = 0.15` node"), and one cannot argue the `t ↓ 0` limit avoids it
(the limit is pinned to the edge). Carry the card's hedge: existence at that node is neither claimed
nor denied, and the pin is not its node's achieving basin.

---

### 4. Verdict

**GO-WITH-CHANGES — and the change is a reduction in the ask, not a reformulation of it.**

*The NO-GO half, stated first and plainly.* The route **cannot** deliver P1 without A3. The
obstacle is O-1, and it is structural before it is empirical: Step 18's correspondence is nonempty
*by A3*, in both texts on file; and no repair keeps the conclusion a **cutoff** PBE with pointwise
optimality. The counterexample class is on the record and is confirmed here: **an open set of `k` on
which the pointwise argmax is non-monotone in `s`** — `H,V,H,V` at `(κ=0.5, τ₅₀, T=5)` above
`edge(6)`, over `k₂`-offsets `1e−9 … 2e−2`, and a `V→H` reversal with **5** sign changes at
`(κ=0.15, 0.05, 5)` **at a located fixed point**, the latter invariant across all eight
family/scale variants. On such `k`, `𝔗(k) = ∅` and Kakutani fails at its first hypothesis.

*The GO half.* The route **does** deliver A6's continuity clause, and better than Step 18 claims:
O-3 needs only continuity in `k` at fixed `s`, which the fixed-`t` game **derives**, so Step 15(i)'s
joint continuity — which fails on this menu independently — can be dropped from the route's
statement rather than carried. Probe C measures the repair working at the card's own failure locus
(local step in `𝒯₂` falling `6.334e−3 → 6.8e−6` at a fixed `1e−8` bracket). That is a real
improvement to the option-C conditional: the hypothesis set loses the clause §5's A5 and A6 notes
record failing together, and Step 12, the `κ` boundary, and measurability all come through
untouched. Whether to spend the campaign on half the prize is Austin's re-scoping decision, not
this ticket's.

**Proposed campaign tickets**, each a child of this effort with its own statement-to-prove:

- **02 — P1-t: existence in the fixed-`t` constrained game.** Prove `k⋆ ∈ 𝔗(k⋆)` for each fixed
  `t > 0`, with h.6's continuity clause **deleted and derived** from Step 9(b)'s `Z_n ≥ (t/J)Λ_u > 0`,
  Step 15(i) **dropped** (O-3's weaker route), Step 14's bracket and A3 **retained**, and the
  conclusion carrying `Φ_s`-a.e. optimality. Two-pass gate as usual.
- **03 — Convexity (O-2).** Prove `𝔗(k)` convex under a.e. contiguity of the argmax, with the
  ordered-coordinate lattice argument and the `(0,10)`/`(20,20)` counterexample as the two poles;
  then **measure contiguity on the implemented menu**. Blocks 02.
- **04 — The `t ↓ 0` bridge (O-4).** Not a proof ticket: state exactly what the limit object is
  (Kreps–Wilson-consistent assessment, trembles in cutoffs as well as plans), what §3(vi) would have
  to say to accept it, and what is lost if it does not. Decision ticket for Austin.
- **05 — The off-path family, implementation and card (§3(b)).** Independent verification of the
  uniform-vs-mass-proportional finding; if it holds, the implementation should realise the card's
  `Λ_u` and the genuine fixed-`t` blend, and the A3/A6 evidence record should be re-run against it.
  This ticket is prior to any card correction and touches nothing until verified.
- **06 — A3 (O-1), the real blocker.** Given 05, re-measure both A3 loci under the card-faithful
  family; locus (ii) is expected to stand. Then the open question is whether any hypothesis weaker
  than `𝒮(k) ≠ ∅` supports a cutoff conclusion — this exploration's answer is no, and 06 is where
  that is either confirmed or overturned.

### 5. The map's fog questions, answered

1. **Does Kakutani apply; are the values convex at the jump edges?** Upper hemicontinuity is fine
   and cheaper than Step 18 thinks (O-3). Convexity is **not** where the jump edges bite: at a clean
   jump the value is a singleton, and at the non-monotone loci the value is **empty**. Convexity's
   real failure mode is argmax non-contiguity, and it is unchecked (O-2).
2. **What does `t ↓ 0` lose?** Not optimality — the limit is an **exact** equilibrium, not an
   ε-equilibrium. It loses **item (vi)**: the belief at a frontier history is a sequence-rate-indexed
   blend, admissible under Kreps–Wilson consistency but not under P1's "one family, fixed once, at
   every `k`" (O-4).
3. **Can the move absorb A3's failure, or only A6's — and what is the weakest A3 replacement?**
   Only A6's. Weakest replacement: `𝒮(k) ≠ ∅` on `Θ`, a.e. form; A3's single-crossing half can be
   dropped, its monotone-selection half cannot (§3).
4. **The boundary `κ ∈ {0,1}`?** Delivered, with no separate treatment: the perturbation is over
   plans only, so Step 9(a)'s reachability and 9(d)'s extension reading carry verbatim (O-5).
5. **Which downstream results notice the changed hypothesis set?** Almost none. **No result row
   consumes P1's conclusion** — D1/L1/L2/L3/L4/T1/C1 are stated at fixed policies or at an
   exhibited equilibrium, and `HANDOFF_sign.md` mentions P1 only as a status note. What notices:
   P1's **own** Step 20 A8 restatement (unaffected — h.13/h.15 restrict the menu, not the map),
   card §3's definition (the a.e.-optimality wording, and item (vi) if ticket 04 lands), the two
   mirrors and `sections_v3/`.
