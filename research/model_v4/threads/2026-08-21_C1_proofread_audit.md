# Audit — C1 (GE region certificate), adversarial proof-read

Source under audit: `research/model_v4/proofs/C1_proof.md` (committed, 718 lines).
Auditor: fresh Opus proof-reader, ticket 27 pipeline batch 3, 2026-08-21, repo
`blockholder_v4_theory` @ branch `v4-theory`. **Wrote nothing under audit.**
Stance: adversarial — every step attacked before it was passed; the four-group chain rule was
re-derived from scratch rather than read; every quoted number was recomputed from the committed
JSON.

Read: the proof; `MODEL_CARD.md` (§3, §4.1–§4.6, §5, §6, §7, §8, §9);
`threads/thread1_turn1_answer.md` §C1; `quality_reports/fixes/t2_c1_region_check.py` and
`t2_c1_region_check.json`; `quality_reports/fixes/d8_ge_dominance_check.py` (precedent);
`numerical_v4/smoke_output.txt` (one cited line). **No other `proofs/` or `rederive/` file was
opened** — cross-file claims about T1's internals are logged UNCHECKED, not passed.

Finding classes, per the turn-2 convention: **FAIL** (a step's cited hypotheses or earlier steps do
not deliver it, or the math is wrong — blocks) · **REPAIR** (the claim stands; something true is
uncited, asserted where it should be argued, or reported in a way that misleads — never blocks) ·
**OBSERVATION** (a card gap or a note for later turns).

---

## 0. Verdict

| Result | Verdict | Failing steps | Repairs | Observations | Claim vs card |
|---|---|---|---|---|---|
| C1 (A)–(D), Steps 1–12 | **PASS** | none | C1-R1 … C1-R13 | C1-O1 … C1-O7 | **refinement** |

**Claim vs card.** Card §6's C1 row reads *"On a named region where $L_{\mathcal R}<1$ and
$g_r^{PE} > \mathcal B_r^{GE}$, the fixed-policy attenuation sign survives in equilibrium."* The
proof (i) names four more hypotheses the row does not carry (H3 interior single branch, H4 $C^2$
premium, H5 non-vanishing equilibrium liquidity derivative, H7 smooth strictness domain), (ii)
strengthens the conclusion from a sign to a **rate** $\partial_r\mathcal S\le-\eta_r$ plus a
finite-scale integral form (D), and (iii) separates $g_r^{PE}$'s *name* (H8) from its *use* (Steps
8, 10), which the row conflates. Nothing is silently weakened. **Refinement**, on the turn-2 test.

**Mechanical scans.**

- **Banned words** (`clearly`/`it follows`/`standard`/`obviously`, plus `evidently`, `trivially`,
  `straightforward`, `well-known`, `of course`, `easily seen`, `routine`, `as usual`,
  `one can see`): **0 hits**.
- **`\ref` / `\cite` / `\label` / `lem:` / `prop:` / `thm:` / `app:` / `eq:` / `sec:` / `et al`:
  **0 hits**. Every upstream citation is a card ID (A5, A8, A($\tau$), AGE, D1, L1, L2, T1), a card
  section, a numbered hypothesis, or an earlier step.
- **draft_v2 references: 1 hit**, line 408 — *"draft_v2's baseline collapses Hold, $k_1=k_0$"*. Not
  a lemma number; a calibration fact, and card §4.5's $k$ row itself licenses the
  $(k_1,k_0,k_D)$ mapping. **Tolerable-with-note** under card §8 rule 2.
- **Repo-path citations: 5**, all to the companion script, its JSON, the card, and
  `numerical_v4/smoke_output.txt`. Rule 2 governs *pasted answers to the theorist*, who cannot see
  the repo (rule 1); this file is an in-repo artefact and the card itself cites repo paths
  throughout. **Not a violation.**
- **Unused hypotheses: 0.** H1 [all], H2 [1–4, 7, 12], H3 [1, 5, 12], H4 [5, 6, 9], H5 [7],
  H6 [8, 10], H7 [3, 4, 5], H8 [9] — each traced to a step that actually consumes it. H2b is
  *deliberately* unused and says so (see C1-R13 for the wording).
- **Bare steps (no citation): 0.** All twelve steps cite a hypothesis, a card row, or an earlier
  step. Step-by-step: 1 (H2, H2a, H3) · 2 (H2a) · 3 (H7, S1, S2) · 4 (S3, S2) · 5 (H4, S1, H7) ·
  6 (S5, S3, S4, H4) · 7 (H2, H5, S5) · 8 (S5, card §4.5, S6, S7, H6) · 9 (H8, S1–S8) ·
  10 (S5, S8, H6) · 11 (S1–S10) · 12 (H2b, H3, S1).
- **NOTATION DELTA completeness: incomplete.** Ten symbols used and not in card §4 are missing from
  the table — see **C1-R9**. One binding card §4.6 ruling is violated — see **C1-R8**.

**Counts. FAIL 0 · REPAIR 13 · OBSERVATION 7 · UNCHECKED 3.** Nothing blocks; the one-retry rule
does not fire. **No label moves** (see §5).

---

## 1. Attack 1 — the Neumann step and the H2a/H2b split

**Steps 1, 2, 3, 4 — PASS. The split is coherent and the boxed conclusion really does need only
H2a.**

Traced where each reading is required:

| Step | What it needs | Reading |
|---|---|---|
| 1 (invertibility of $I-D_k\mathcal T$) | $\lVert D_k\mathcal T(k(\vartheta);\vartheta)\rVert<1$ at the equilibrium point only | **H2a** |
| 2 (Neumann bound) | same operator, same point | **H2a** |
| 3, 4 (derivative bounds) | every $\mathcal T$ derivative is evaluated at $(k(\vartheta);\vartheta)$ | **H2a** |
| 12 (global uniqueness remark) | contraction on all of $\Theta$ | H2b, and it is not claimed |

Step 1's chain is valid: $\lVert(I-D_k\mathcal T)u\rVert\ge\lVert u\rVert-\lVert D_k\mathcal T
u\rVert\ge1-L_{\mathcal R}>0$ for $\lVert u\rVert=1$ is the reverse triangle inequality, and bounded
below on a finite-dimensional space gives injective hence bijective. Step 2's telescoping is the
standard partial-sum argument written out: $(I-A)\sum_{n\le N}A^n=I-A^{N+1}$ with
$\lVert A^{N+1}\rVert\le L_{\mathcal R}^{N+1}\to0$. Correct, and it is *written*, not waved at.

Using the region-wide supremum $L_{\mathcal R}$ in place of the pointwise norm is a valid weakening,
since $t\mapsto(1-t)^{-1}$ is increasing on $[0,1)$. No step is voided by that slack.

The companion script measures exactly H2a: `contraction_bound_L_R.reading` in the JSON states
*"$L_R$ here is $\lVert D_kT\rVert$ AT the equilibrium $k^*(\theta)$, node by node — the
along-the-path reading. AGE's sup over the whole polytope is NOT computed."* The proof and the
script agree, and both disclaim the stronger reading. **No over-read.**

> **C1-R10 (REPAIR).** Step 1 defines $\Psi$ *"on the interior of $\Theta$ times $\mathcal R_r$"*
> and takes H2's $C^2$ clause over that whole domain. Only a neighbourhood of the graph
> $\{(k(\vartheta),\vartheta):\vartheta\in\mathcal R_r\}$ is needed — which is exactly the domain
> **H4 chooses for $\Delta^{\mathrm{act}}$**, three hypotheses earlier. The asymmetry matters
> because card §5's AGE says *"on a candidate region $\mathcal R$ the outer map is twice
> continuously differentiable"* **without saying over which $k$** — the identical ambiguity that
> H2a/H2b flags for the norm. The proof flags it for the norm and takes the strong reading silently
> for the smoothness. Repair: restrict Step 1's domain to a neighbourhood of the graph, and add a
> third card-owner flag to NOTATION DELTA. Non-blocking — the hypothesis granted is *stronger* than
> the one used, so no logical gap; it is an unflagged strengthening, not a hole.

> **C1-R13 (REPAIR — wording).** H2b is described as *"**not** used by any step below"*, and three
> lines later as *"what would upgrade Step 1's local uniqueness to a global one on Step 12"*, with
> the H2 bracket listing `[Steps 1–4, 7, 12]`. Step 12 does use it. Reword to "no step in the proof
> of (A)–(D) uses it; Step 12 discusses what it would add."

---

## 2. Attack 2 — the four-group chain rule for $\partial^2_{r\kappa}\Delta^*$

**Step 5 — PASS. Re-derived independently from the implicit function theorem; the identity is
exact and no cross-term is dropped.**

Writing $\Delta^*(\kappa,r)=\Delta^{\mathrm{act}}(k(\kappa,r),\kappa,r)$ and differentiating in
$\kappa$:
$$\partial_\kappa\Delta^*=\sum_j\Delta_{k_j}\partial_\kappa k^j+\Delta_\kappa.$$
Differentiating that in $r$, with $\kappa$ held fixed, each of $\Delta_{k_j}$ and $\Delta_\kappa$
carrying an explicit $r$ slot and an implicit one through $k(\kappa,r)$:
$$
\partial^2_{r\kappa}\Delta^*
=\underbrace{\Delta_{\kappa r}}_{1}
+\underbrace{\sum_l\Delta_{\kappa k_l}\partial_rk^l}_{2}
+\underbrace{\sum_j\Bigl(\sum_l\Delta_{k_jk_l}\partial_rk^l+\Delta_{k_jr}\Bigr)\partial_\kappa k^j}_{3}
+\underbrace{\sum_j\Delta_{k_j}\partial^2_{\kappa r}k^j}_{4}.
$$
This is the proof's display term for term. Three checks the derivation was stressed on:

1. **No $\Delta_{k\kappa}[\partial_\kappa k]$ term is missing.** Differentiation is in $r$ at fixed
   $\kappa$; $\Delta_{k_j}$'s $\kappa$-dependence — explicit and through $k$ — is frozen. Correct.
2. **Order-independence.** Doing $\partial_r$ first gives
   $\Delta_{r\kappa}+\Delta_{rk}[\partial_\kappa k]+(\Delta_{\kappa k}+\Delta_{kk}[\partial_\kappa k])
   \cdot\partial_rk+\Delta_k\cdot\partial^2_{r\kappa}k$, whose absolute-value bound is
   $\lvert\Delta_{kr}\rvert\bar k_\kappa+\lvert\Delta_{\kappa k}\rvert\bar k_r+
   \lvert\Delta_{kk}\rvert\bar k_\kappa\bar k_r+\lvert\Delta_k\rvert\bar k_{\kappa r}$ — **the same
   $\mathcal B_r^{GE}$**, term for term. The bound does not depend on which order the mixed
   derivative is taken in, which it must not, given H4's $C^2$.
3. **Every term lands in one of the three groups of $\mathcal B_r^{GE}$**: group 2 →
   $\lvert\Delta_{\kappa k}\rvert\bar k_r$; group 3 → $(\lvert\Delta_{kr}\rvert+
   \lvert\Delta_{kk}\rvert\bar k_r)\bar k_\kappa$; group 4 → $\lvert\Delta_k\rvert\bar k_{\kappa r}$.
   Group 1 is the fixed-policy term subtracted off in (B). **No orphan term.**

**Step 4 — PASS, same exercise on $\mathcal T$.** Differentiating $\partial_\kappa k^i=\sum_j
\mathcal T^i_{k_j}\partial_\kappa k^j+\mathcal T^i_\kappa$ in $r$ reproduces the proof's component
display exactly, including the $\mathcal T^i_{k_j}\partial^2_{\kappa r}k^j$ term that is moved to
the left as $(I-D_k\mathcal T)\partial^2_{\kappa r}k$.

**The norm pairings are the right ones**, checked one by one against $\lVert\cdot\rVert_\infty$:
$\lvert\mathcal T_{\kappa k}\rvert=\max_i\sum_l\lvert\mathcal T^i_{\kappa k_l}\rvert$ is the
induced bound on $\lVert\mathcal T_{\kappa k}[u]\rVert_\infty$;
$\lvert\mathcal T_{kk}\rvert=\max_i\sum_{j,l}\lvert\cdot\rvert$ likewise for the bilinear form;
$\lvert\Delta_k\rvert=\sum_j\lvert\Delta_{k_j}\rvert$ is the $\ell^1$ dual of $\ell^\infty$, which
is what a *scalar* output requires. The script implements the same pairings —
`abs_T_kk = max(|T_k1k1| + 2|T_k1k2| + |T_k2k2|)` and
`abs_D_kk = |D_k1k1| + 2|D_k1k2| + |D_k2k2|`, the off-diagonal counted twice in both. **Proof and
code agree on the norm; the NOTATION DELTA card-owner flag is warranted and honest.**

> **C1-R9 (REPAIR — NOTATION DELTA incomplete).** The table claims to list *"symbols used here that
> are not in card §4"*. Ten are missing. (i) $\mathcal T_{\kappa r}$, $\mathcal T_{\kappa k}$,
> $\mathcal T_{rk}$, $\mathcal T_{kk}$ — card §4.5 *names* $\bar k_{\kappa r}$ but never displays
> its formula, so these four subscript shorthands appear nowhere on the card. (ii) $\Delta_\kappa$
> and $\Delta_{\kappa r}$ — the card's $\mathcal B_r^{GE}$ row carries $\Delta_{\kappa k}$,
> $\Delta_{kr}$, $\Delta_{kk}$, $\Delta_k$, but the $g_r^{PE}$ row writes the cross-derivative out
> as $\partial_{\kappa r}\Delta^{\mathrm{act}}$, never as $\Delta_{\kappa r}$. (iii) The bars
> $\lvert\partial_x\mathcal T\rvert$ used in the CLAIM are the one pairing the preamble list does
> *not* fix (Step 3 writes $\lVert\partial_x\mathcal T\rVert$ instead). (iv)
> $\mathcal B_r^{GE,\text{sharp}}$, introduced in Block 9 and used in a displayed ratio.
> (v) $h_\kappa,h_\tau$ (Block 2, stencil steps) — and **$h$ is a live card symbol**, §4.4's
> engagement-premium kernel $h=\pi p$. Rename these two; the turn-2 notation audit retired symbols
> for less. (vi) $r_0,r_1$ (Step 10). All cosmetic, none load-bearing.

---

## 3. Attack 3 — the triangle inequality, the absolute value, and where H8 does *not* bite

**Steps 6, 7, 8 — PASS. The sign handling is correct and H8 is genuinely absent from the boxed
conclusion.**

Step 7's identity $\mathcal S=\lvert\partial_\kappa\Delta^*\rvert=\operatorname{sgn}(d\Delta^{
\mathrm{act}}/d\kappa)\,\partial_\kappa\Delta^*$ is trivial *pointwise*; what the proof needs and
correctly isolates is that it is an identity **of functions** with a *constant* $\pm1$ prefactor,
which is AGE's constancy clause, and that the prefactor is not $0$, which is H5. The proof says both
are needed and they are: constancy alone permits the degenerate constant value $0$; non-vanishing
alone permits a crossing. **Two separate assertions, correctly separated.**

Step 8's sign algebra, checked:
$$\operatorname{sgn}\!\Bigl(\tfrac{d\Delta^{\mathrm{act}}}{d\kappa}\Bigr)\Delta_{\kappa r}
=-\Bigl[-\operatorname{sgn}\!\Bigl(\tfrac{d\Delta^{\mathrm{act}}}{d\kappa}\Bigr)
\partial_{\kappa r}\Delta^{\mathrm{act}}\Bigr]=-g_r^{PE},$$
which is card §4.5's $g_r^{PE}$ row read literally — the card writes the **total** derivative
$d\Delta^{\mathrm{act}}/d\kappa$ inside the $\operatorname{sgn}$, i.e. the equilibrium one, exactly
as the proof reads it. The rest is $\lvert\pm1\cdot x\rvert=\lvert x\rvert$, so Step 6's bound
survives the multiplication untouched. Then
$$\partial_r\mathcal S=-g_r^{PE}+\operatorname{sgn}(\cdot)[\text{remainder}]
\le-g_r^{PE}+\mathcal B_r^{GE}=-\eta_r<0.$$

**Is H8 used?** No. The chain above consumes only card §4.5's *definition* of $g_r^{PE}$ (which
already carries the equilibrium sign), Step 6, Step 7 and H6. H8 asserts the *fixed-policy* sign
matches; it enters only at Step 9, and Step 9 is a statement about what (C) may be **called**. The
proof's claim that "the boxed conclusion (C) does not use H8" is **verified**. Step 9 then correctly
observes that without H8, $g_r^{PE}$ would be a cross-derivative oriented by the equilibrium sign
while the fixed-policy comparative static ran the other way — in which case the ledger's phrase
"the fixed-policy attenuation sign" would be a misnomer, but (C) would still hold. That is precisely
the right thing to say, and the script reports the disagreement count rather than assuming
coherence (`n_sign_incoherent_nodes: 0` over 80 nodes).

**Step 10 (Part D) — PASS.** FTC on $[r_0,r_1]$ with $r_1>r_0$: $\mathcal S(r_1)-\mathcal S(r_0)
=\int\partial_r\mathcal S\le-\int\eta_r<0$. Orientation correct (higher $r$ = tighter, card §4.5).

> **C1-R11 (REPAIR).** Step 10's strict inequality rests on *"$\eta_r>0$ (H6) and continuous on a
> segment of positive length"*, and continuity of $\eta_r$ is **asserted, not argued**. It is true
> and derivable from what is already on the table: $g_r^{PE}$ is continuous by H4's $C^2$ clause
> plus Step 7's constant sign, and $\mathcal B_r^{GE}$ is continuous because every factor in it is a
> continuous derivative of $\mathcal T$ or $\Delta^{\mathrm{act}}$ (H2, H4) divided by the
> **region-constant** $1-L_{\mathcal R}$. One line; write it in. (Measurability plus positivity
> would also suffice for the integral, which is a cheaper route if the writer prefers.)

> **C1-R5 (REPAIR — card-owner flag, and the one the NOTATION DELTA is missing).** Card §4.5 does
> not say **at which cutoff vector** $\partial_{\kappa r}\Delta^{\mathrm{act}}$ in $g_r^{PE}$, or
> $\Delta_k$, $\Delta_{kk}$, $\Delta_{\kappa k}$, $\Delta_{kr}$ in $\mathcal B_r^{GE}$, are
> evaluated. Step 8's algebra requires all of them at $k(\vartheta)$ — the equilibrium cutoff vector
> **at the same $\vartheta$** — because that is where Step 5's identity puts them. Read at any other
> frozen policy, Step 8's cancellation of the first group against $-g_r^{PE}$ fails and the
> certificate is comparing unlike objects. This is a reading of a card object exactly parallel in
> kind to the two the proof does flag (the norm, and H2a/H2b), and it is the one left unflagged. Add
> it as a third card-owner row. Non-blocking: the proof is internally consistent throughout: every
> $\Delta$ derivative is at $k(\vartheta)$, and the script evaluates the stencil at
> $x_0=(k_1^*,k_2^*,\kappa,\tau)$, which is the same point.

---

## 4. Attack 4 — H4's smoothness demands, and the integer window

**H4, H7, WHERE IT FAILS 6 and 7 — PASS. The restriction to $r_\tau$ is honest and complete.**

The certificate is claimed only for $r_\tau=-\tau$. Checked in four places and consistent in all
four:

| Where | What it says |
|---|---|
| H7 | for $r_T=-T$ *"the $r_T$ instance additionally needs a smooth window interpolation"*, imported from T1 |
| WHERE IT FAILS 6 | without it, *"$\partial_{\kappa r_T}\Delta^{\mathrm{act}}$ — hence $g_{r_T}^{PE}$ itself — is undefined"*, and *"only the threshold instance $r_\tau=-\tau$ is available from the card alone"* |
| Block 8 | *"No $r_T$ certificate is computed … and this block is a record"* |
| NOT CLAIMED 6 | *"No window-margin sign, and no window certificate"* |

And the script agrees: `provenance.strictness_coordinate` = *"$r=r_\tau=-\tau$. $r_T=-T$ is NOT
differentiated: T ranges over $\{1,\dots,H\}$ in the card and is an int in the code."* The $T=5$
against $T=10$ comparison is filed as `window_margin_discrete_record`, verdict **RECORD**, not
PASS/FAIL. **Nothing is claimed for the window.** This is the cleanest part of the file.

**The sharper attack — does H4 hold at the nodes that certify?** WHERE IT FAILS 7 splits the
quantised-clock failure into (i) $\Delta^{\mathrm{act}}$ jumps in $\tau$, so H4 fails, and (ii)
between jumps $\Delta^{\mathrm{act}}$ is locally *constant* in $\tau$, so $g_r^{PE}=0$ and H6 fails
for a reason that has nothing to do with GE. The obvious adversarial reading is that these exhaust
the possibilities — so any node with $g_r^{PE}\ne0$ must be a node whose $\tau$-stencil straddles a
jump, i.e. **the 18 certified nodes would be exactly the nodes where H4 fails.** That reading is
**refuted by the data**, and by a diagnostic the script computes for precisely this purpose and the
proof never quotes: see **C1-R3**.

Executed spot-check, verbatim:

```
certified n=18   tau_kink_ratio finite = 18
kink at certified: min 0.04672   median 0.3173   max 0.6734
nodes with tau_kink_ratio > 1: 19, and every one of them is a null-margin node
  (cells (5,q10), (5,q30) and all of T=10) where |d_tau Delta| is at rounding scale
```

`tau_kink_ratio` is $\lvert\partial^2_{\tau\tau}\Delta^{\mathrm{act}}\rvert h_\tau/
\lvert\partial_\tau\Delta^{\mathrm{act}}\rvert$ — a curvature-to-slope ratio that blows up if a jump
sits inside the stencil. At every certified node it is below $0.68$, so the second-order term is a
fraction of the first over one stencil width. The certified nodes sit in smooth $\tau$-patches. The
attack fails, and the evidence that defeats it is already on disk.

> **C1-R3 (REPAIR — the most valuable one).** The script computes `tau_kink_ratio` at every node
> with the comment *"the implemented legal clock takes $c=\lceil\cdot\rceil$, so tau-kinks are
> possible inside a stencil"* — it is the only executed evidence bearing on H4, the hypothesis the
> LABEL CLAIMED section calls unverifiable. It is in no `checks` entry and in no line of the
> OUTCOME. Report it: max $0.673$ over the 18 certified nodes, and every ratio above one attached to
> a node whose $\tau$-slope is rounding noise. It converts WHERE IT FAILS 7(i) from an unaddressed
> hazard into a hazard that was measured and did not bite.

---

## 5. Attack 5 — the JSON against the OUTCOME section

Every number in the OUTCOME was recomputed from `t2_c1_region_check.json`. **Executed spot-checks,
verbatim:**

```
n nodes 80 ; certified 18 ; cert T set [5] ; tau_pct set [50, 70, 90]
eta min 0.0595354  median 0.346716  max 1.72273
L_R min 0.263587   max 0.500818   any L>=1: False
null-margin 56  dominated 4  negative 2   sum 62
dominated: (5,q50,0.35) (5,q50,0.55) (5,q70,0.35) (5,q90,0.25)
negative:  (5,q70,0.55) (5,q90,0.55)
block size 9  all certified True  signs {-1.0}  eta min 0.2282  median 0.3739
low-kappa (T=5, q50/q70/q90, kappa<=0.45): 12 nodes, 9 certified, signs {+1.0}
sign changes: 10 slices, exactly 1 each, all between kappa=0.45 and 0.55
Omega at T=10: single value 0.0006813 at all 40 nodes
worst equilibrium residual 4.162e-11 ; k_order_ok all True ; multiple_root_nodes 0
sign_coherent True at all 80 nodes
B/B_sharp: median 2.086  max 10.298 ; certified_sharp 22
median realised remainder / B_r^GE = 0.2192
two readings of dDelta*/dkappa: max rel diff 0.001791
checks: 4 PASS, 8 RECORD, 0 FAIL ; all_pass True ; wall 10339 s ; empty_region False
```

**Every figure the OUTCOME quotes is reproduced exactly**: 18 of 80; $\eta_r$ min $0.0595$ /
median $0.3467$ / max $1.7227$; $L_{\mathcal R}\in[0.264,0.501]$; the nine-node block with $\eta_r$
min $0.2282$ and median $0.3739$; 56 / 4 / 2 with the named node coordinates; $\Omega=0.00068$;
residual $4.2\times10^{-11}$; factor $2.09$ median and $10.3$ max; 22 sharp-certified;
$0.22$ median realised remainder; $1.8\times10^{-3}$ first-derivative agreement; four PASS and eight
RECORD; $10\,339$ s. The claim *"nine of them in one contiguous sign-homogeneous block"* checks out
against `certified_kappa_by_cell`, and *"9 of 12 nodes certify but not contiguously"* on the
low-$\kappa$ side is right on the natural reading (the three live-margin $\tau$ cells at
$\kappa\le0.45$) with a hole in each cell. **No fabricated number, and no number rounded in a
favourable direction.**

WHERE IT FAILS 2's external citation also checks out. `numerical_v4/smoke_output.txt` line 95:
*"non-monotone: M_P is hump-shaped in kappa (peak near kappa = 0.55, 1 sign change(s) in
dM_P/dkappa)"*. Verbatim support for the claim as made.

### The reporting defects

> **C1-R1 (REPAIR — the substantive one).** **Every aggregate magnitude in the OUTCOME pools 56
> rounding-scale nodes with 24 live-margin ones, and each one moves when you split them.** At the 56
> null-margin nodes $g_r^{PE}$ and $\mathcal B_r^{GE}$ are both at $10^{-13}$, so every ratio built
> from them is a ratio of noise. Recomputed both ways:
>
> | Statistic | As reported (80 nodes) | Live margin (24) | Null margin (48 with $\mathcal B>0$) |
> |---|---|---|---|
> | realised remainder $/\;\mathcal B_r^{GE}$, median | 0.22 | **0.094** | 0.31 |
> | realised remainder $/\;\mathcal B_r^{GE}$, max | 1.00 | **0.306** | 1.00 |
> | $\mathcal B_r^{GE}/\mathcal B_r^{GE,\text{sharp}}$, median | 2.09 | **2.41** | 1.92 |
> | $\mathcal B_r^{GE}/\mathcal B_r^{GE,\text{sharp}}$, max | 10.3 | **8.29** | 10.3 |
>
> The direction is not uniform — the bound is *tighter* than reported on live nodes (0.094 not 0.22)
> and the Neumann step is *costlier* (2.41 not 2.09) — so this is sloppiness, not spin. But the
> proof already knows the split matters: it flags it for exactly one figure (*"where the ratio
> reaches 1.00 … both at rounding scale ($\sim2.6\times10^{-13}$)"*, verified: nodes $(10,q50,0.35)$
> and $(10,q50,0.45)$ with $\mathcal B=1.6/2.6\times10^{-13}$) and then quotes four other pooled
> figures without it. Report every ratio on the live-margin subset, with the null-margin count
> beside it.
>
> Related, and part of the same repair: `BOUND_SLACK = 1e-6` is an **absolute** tolerance in the
> containment test. At the 56 null nodes, where $\lvert\text{remainder}\rvert$ and
> $\mathcal B_r^{GE}$ are both $\sim10^{-13}$, the slack alone passes them, so
> `bound_contains_ift_remainder`'s *"n_checked: 80, 0 violations"* has an effective coverage of 24.
> (The containment does in fact hold at all 80 without the slack — max ratio $1.00$ — so nothing is
> being hidden; the headline count is just larger than the evidence behind it.)

> **C1-R2 (REPAIR — the independent check is thinner than the OUTCOME suggests).** The four-corner
> re-solve is the file's *only* route to $\partial^2_{r\kappa}\Delta^*$ that shares no arithmetic
> with the bound — the JSON calls it *"the certificate's only substantive verdict"*. It runs at 8
> validation nodes. **Four of those 8 are null-margin nodes**, and **only 2 of the 18 certified
> nodes are validated at all** ($(5,q50,0.25)$ and $(5,q50,0.85)$). Worse, the figure the OUTCOME
> quotes is the wrong one:
>
> ```
> four-corner remainder / bound, LIVE validation nodes:  max 0.3102
> four-corner remainder / bound, DEAD validation nodes:  0.07383, 0.5115, 0 (and one 0/0)
> ```
>
> **The quoted "at most 0.51 of the bound" comes from $(10,q10,0.55)$, where $\mathcal B=7.6\times
> 10^{-13}$ and the remainder is $3.9\times10^{-13}$** — pure noise. On live nodes the true figure
> is $0.31$.
>
> In the same breath, the OUTCOME omits the *better* evidence. The check
> `ift_matches_resolved_equilibrium` reports `max_rel_diff_cross = 0.535`, which looks alarming and
> is never mentioned. Recomputed node by node:
>
> ```
> cross-derivative, |numeric - ift| / max:   q10 T5 0.778 (dead)   q50 k=.25 0.00377
>   q50 k=.55 0.00161   q50 k=.85 0.00282   q90 k=.55 0.000221   T10 nodes 1.23, 1.00, n/a (dead)
> max on LIVE nodes only: 0.00377
> ```
>
> **On every live-margin validation node the two independent readings of the equilibrium
> cross-derivative agree to better than 0.4 %.** That is the single strongest piece of evidence in
> the run — it is what licenses the free implicit-function reading at the 72 unvalidated nodes — and
> it is not in the proof. Report the live/dead split for both figures, and state plainly that the
> independent route touches 2 of the 18 certified nodes.

> **C1-R4 (REPAIR).** Block 7 (the finite-scale secant) is requested in the NUMERICAL CHECK REQUEST
> and **never answered** in the OUTCOME. The JSON has it: `finite_scale_secant_orientation`,
> `n_pairs: 64`, `n_same_orientation: 45`. Nineteen adjacent-$\tau$ pairs disagree in orientation
> between the fixed-policy and equilibrium secants. Block 7 is explicitly *"not the certificate"*,
> so this changes nothing — but a request that goes out must come back, and a 19/64 disagreement
> rate is the kind of number a reader will want beside Part (D)'s finite-scale claim.

> **C1-R12 (REPAIR — an understatement, worth sharpening because it strengthens the finding).**
> The Block 9 conclusion says the Neumann step *"is what most uncertified $T=5$ nodes with a live
> margin fail on"*. Checked: the four nodes the sharp companion certifies and the card bound does
> not are **exactly** the four "genuine GE failure" nodes $(5,q50,0.35)$, $(5,q50,0.55)$,
> $(5,q70,0.35)$, $(5,q90,0.25)$. The remaining two uncertified live nodes have $g_r^{PE}<0$ and no
> bound of any size could save them. So: **every uncertified live-margin node that any bound could
> rescue is rescued by dropping the Neumann step.** "Most" should read "every one that could be."

---

## 6. Attack 6 — what is actually claimable (the label-target question)

**LABEL CLAIMED and Step 11 are consistent, and the section is right to claim CONJECTURE.**

Step 11 states the gap precisely: certified nodes promote to a certified region only with a modulus
of continuity, $\eta_r\ge\eta_{\min}-M\delta/2$ on the hull of two adjacent nodes, positive exactly
when $\eta_{\min}>M\delta/2$ — and *"the companion script does not estimate $M$"*. It adds the
matching point about $L_{\mathcal R}$: a supremum over $\mathcal R$ cannot be read off finitely many
nodes. NOT CLAIMED 4 repeats it. LABEL CLAIMED reason 2 closes the loop: *"the row's antecedent ('a
named nonempty region') is not yet met either."* **No drift between the three.** The words "the
region is NOT empty" in the OUTCOME heading are the only place a reader could over-read, and the
same paragraph ends *"nine certified nodes are still nine nodes and not a region."*

**The label-target answer.** Three distinct objects, three different labels, and only the middle one
is in dispute:

1. **The theorem — (A), (B), (C), (D) as *conditional* statements** ("on a region where H2–H8 hold,
   …"). This is a pure implication. Its truth does not depend on any region being nonempty, and it
   is the object this file actually proves. **Eligible for PROVED** once card §6's two-pass gate is
   met (this proof-read plus an independent re-derivation), with $\mathcal R_r$ carried as a named
   hypothesis — which is exactly what card §7 means by *"Region-certified is not a fifth label: it
   is PROVED with the region named in the hypothesis."*
2. **The 18 nodes. NUMERICAL, and nothing more.** Card §7's definition — *"verified on a grid by an
   executed, committed check script with committed output"* — fits them exactly. They are evidence
   that H2–H8 are jointly satisfiable at the maintained calibration; they are not a region.
3. **"C1 PROVED on a named nonempty region $\mathcal R_r$" — not available, and not available from
   any run of this script.** That phrase asserts the antecedent, and asserting it needs a set with
   interior plus a supremum over that set. Step 11's $M$ is unestimated and $L_{\mathcal R}$ is
   measured pointwise. **No amount of grid refinement fixes this**; it needs a Lipschitz estimate,
   not more nodes.

So the honest ledger row after two-pass evidence would read: *"C1 — the certificate implication —
**PROVED**, with $\mathcal R_r$ a hypothesis and H2–H8 named in full; **NUMERICAL**: 18 of 80 nodes
satisfy the hypothesis set at the maintained calibration, 9 of them contiguous and
sign-homogeneous; the promotion of certified nodes to a certified region is **OPEN**."** That is
strictly what the file supports, and it is what LABEL CLAIMED reason 2 is already circling without
naming.

> **C1-O5 (OBSERVATION — for the card owner).** Card §6's aspiration line, *"C1 PROVED on a named
> nonempty region, NUMERICAL off-region, dropped if the region is empty"*, asks for something the
> executed route cannot deliver **as worded** — and the reason is structural, not a shortfall of
> this run. The line should be re-worded to the three-object split above, or Step 11's modulus of
> continuity should be added as a named deliverable of a follow-on ticket. See **C1-O2** for a
> template that already exists in this repo.

### Staleness in the LABEL CLAIMED section

> **C1-R6 (REPAIR).** **Reason 3 is stale against the current card and understates C1's inheritance
> in one place while overstating it in another.** It says *"T1 is CONJECTURE with its own open
> items"*. The current card §6 gives **T1 = PROVED at fixed policies** (proof-read + fix round
> closed + re-derivation PASS, 2026-08-21), and card §6's header records that seven of eight results
> moved with C1 alone left untouched. It also lists *"L2 rides on A7 in its injective form"* as an
> open item; card §5's A7 note and card §9 both say **A7 satisfiability is resolved** (ticket 24) —
> what remains open is card §9 item 2, whether an equilibrium in which the separating plan is
> *chosen* exists. The two items reason 3 gets right are A($\tau$)'s applicability to the two-round
> pooled cell (card §9 item 1, OPEN — correct) and A(br) with (br-v) being assumed (correct). Rewrite
> reason 3 as: *C1 inherits T1's* conditionality *— A($\tau$) OPEN for the two-round pooled cell,
> A(br)(br-i)–(br-v) assumed, A7′ satisfiable but its equilibrium selection open — not T1's label.*
> **Non-blocking: reasons 1 (protocol) and 2 (no named region) each independently keep C1 at
> CONJECTURE, so the label does not move either way.**

> **C1-R7 (REPAIR).** H4 declines to cite *"Card §5's A2 (bounded prices and payoffs)"*. On the
> current card there is no A2: it is **A2′**, and its flat-boundedness clause was found **false**
> and replaced by local boundedness plus $\mathbb E[\max_j\lvert U_j\rvert]<\infty$. The proof's
> point survives and in fact strengthens — A2′ is *further* from supplying differentiability than
> A2 was — but the reference should read A2′.

> **C1-R8 (REPAIR — a binding notation ruling).** Card §4.6, binding since the turn-2 notation audit:
> *"$u_1,u_2$ proof-local, **never a bare $u$**."* The proof uses a bare $u$ at line 178 (*"let $u$
> satisfy $\lVert u\rVert=1$"*) and line 181, and bare $u,v,A$ at line 168
> ($\lvert A[u,v]\rvert\le\lvert A\rvert\lVert u\rVert\lVert v\rVert$). Rename — the natural choices
> are $w$ for the unit vector and $(w_1,w_2)$ for the multilinear arguments; $w$ has no card meaning
> and $\Xi$, $\Upsilon$, $\iota_F$ are already spoken for.

---

## 7. Observations

> **C1-O1 (OBSERVATION — stamp).** The proof and the JSON both declare *"stamp 2026-08-21 · commit
> `a175202`+"*. The card on disk reads *"Version stamp: 2026-08-21 · post-ledger regeneration ·
> commit `627642c`"*. The date matches and the `+` suffix presumably means "or later", but the
> hashes differ and git was out of scope for this audit, so the ordering is not established here.
> **Substantive consequence, checked directly:** every card object C1 consumes — §4.5's
> $L_{\mathcal R}$, $r_\tau/r_T$, $g_r^{PE}$, $\bar k_x$, $\bar k_{\kappa r}$,
> $\mathcal B_r^{GE}$, $\eta_r$, $\mathcal R_r$ rows; §5's AGE verbatim; §5's A5 and A8; §3's
> non-uniqueness; §4.4's $\mathcal S$; §4.1's $T\in\{1,\dots,H\}$ — **is present and unchanged in the
> current card**, and H2's AGE quotation is byte-for-byte the card's §5 text. The only places the
> stamp gap shows are C1-R6 (T1's label, A7's status) and C1-R7 (A2 → A2′), both in prose, neither
> in a step. Card §3's *"Uniqueness is **not** claimed"* is also quoted correctly by Step 12.

> **C1-O2 (OBSERVATION — the precedent already solved half of Step 11, and half of Block 9).**
> `quality_reports/fixes/d8_ge_dominance_check.py`, the architectural precedent, does **two things
> C1's OUTCOME presents as novel or unavailable**. (i) Its docstring names *three* bounds — *"exact
> $\lvert B_{ift}\rvert$, sharp $(\sum W)\lVert dk/d\kappa\rVert$, loose
> $(\sum W)\lVert d_\kappa T\rVert/(1-L)$"* — i.e. the sharp/loose ladder that Block 9 offers to the
> card owner as a new finding is a **second independent instance** of a distinction D8 already
> carried. That makes the recommendation stronger, not weaker, and it should be cited as such.
> (ii) Its region certification is *"(R1) pointwise dominance off an eps-ball around the channel-A
> peak and (R2) integral control inside it"* — a worked construction for certifying a **region**,
> including the neighbourhood of the peak, rather than a set of nodes. That is a live in-repo
> template for exactly the promotion Step 11 declares open, and Part (D)'s integral form is the
> natural (R2) analogue. Recommend the follow-on ticket start there rather than from a bare
> Lipschitz estimate.

> **C1-O3 (OBSERVATION).** The OUTCOME reports *"zero nodes with $k_1\ge k_2$ (H3's interiority held
> everywhere it was looked at)"*. The script's test is `k_order_ok = k1 < k2` — strict **ordering**,
> which rules out the collapse faces of $\Theta$ but not its outer box faces. H3 asks for
> $k(\vartheta)\in\operatorname{int}\Theta$, which is more. The parenthetical hedge *"everywhere it
> was looked at"* is doing real work and is correctly placed; flagged so a later reader does not
> promote it to "H3 verified."

> **C1-O4 (UNCHECKED — three cross-file claims, per the protocol, reported rather than triaged).**
> `proofs/T1_proof.md` was out of scope for this audit, so three claims stand unverified:
> (a) Step 5's *"The third term of T1's Step 2 display, $(\partial_\kappa\Omega)(M_F-M_P)$"*;
> (b) Step 5's *"which is what T1's NOT CLAIMED 2 said C1 would have to bound"*; (c) H7's *"the same
> added hypothesis T1 carries as its H15"*. (a) is **consistent with** card §6's T1 row, which names
> PE-$\Omega$ ($\partial_\kappa\Omega=0$ at fixed policies) and says *"it fails in GE, which is C1's
> term"* — and the identification is structurally right: at frozen $k$, $D$ is a function of $(j,s)$
> alone, so $\Omega$ is $\kappa$-free; in GE the channel is $\Omega_k\cdot\partial_\kappa k$, which
> is inside Step 5's group 3/4. (c) is **consistent with** the T1 row's *"a smooth window
> interpolation for the local form"*, though the number H15 is not confirmable from the card. The
> related WHERE IT FAILS 7 reference to *"T1's H18"* is consistent with the card's T1 evidence chain
> (*"T1-F1 discharged by H18"*). None of these is load-bearing for (A)–(D); all three are
> attribution, not inference. **Thread 2's re-derivation should confirm them against T1 directly.**

> **C1-O5** — see §6.

> **C1-O6 (OBSERVATION — card gap).** Card §6's C1 row names two hypotheses ($L_{\mathcal R}<1$ and
> $g_r^{PE}>\mathcal B_r^{GE}$). The honest set is H2–H8 — the row omits H3 (interior equilibrium on
> a single branch), H4 ($C^2$ premium), H5 (non-vanishing equilibrium liquidity derivative) and H7
> (a smooth strictness domain), and it does not distinguish H8 (naming) from H6 (use). This is
> expected of a one-line CONJECTURE row, but the row **must absorb all of them before any label
> moves** — otherwise C1 would be labelled against a statement the proof does not prove. Same
> discipline the D1/L2/P1/T1 rows already show after the ticket-27 regeneration.

> **C1-O7 (OBSERVATION — a causal inference, not an established one).** The OUTCOME attributes the
> single sign change on all ten slices to *"the smoke run's $M_P$ hump"*. The smoke file does show
> $M_P$ hump-shaped with a peak near $\kappa=0.55$ (verified verbatim), and the sign changes all sit
> between $\kappa=0.45$ and $0.55$. But the smoke figure is a **frozen-policy** $M_P$ sweep and the
> sign that changes in the certificate run is that of the **equilibrium** $d\Delta^*/d\kappa$. The
> coincidence is striking and the attribution is very likely right; it is an inference the JSON does
> not establish, and the OUTCOME states it as fact. One hedging word fixes it.

---

## 8. What moves

**Nothing blocks.** FAIL 0 — no step's cited hypotheses fail to deliver it, and the two derivations
the audit re-did independently (the four-group chain rule of Step 5, the $\mathcal T$ cross-
derivative of Step 4) came out term for term identical to the file's. The sign handling of Steps 7–8
is correct, and the claim that H8 is absent from the boxed conclusion is **verified**, not merely
plausible. Every one of the roughly two dozen numerical claims in the OUTCOME reproduces exactly
from the committed JSON.

**Thirteen repairs, none blocking.** The three that matter are reporting defects, not proof defects:
**C1-R1** (pooled statistics over 56 rounding-scale nodes), **C1-R2** (the independent check reaches
2 of the 18 certified nodes, and the quoted tightness figure is from a dead node while the strongest
live-node evidence is omitted), and **C1-R3** (the script's own H4 diagnostic is computed, is clean,
and is never reported). Taken together the picture they change is not the verdict but the *weight*:
the certificate is better supported on the live-margin nodes than the OUTCOME's pooled figures
suggest, and less broadly cross-validated than "eight validation nodes" suggests.

**No label moves.** Card §6 requires an adversarial proof-read PASS **and** an independent
statements-only re-derivation PASS, by different agents. This file is the first half only.
**C1 remains CONJECTURE**, with "proof on file; adversarial proof-read PASS 2026-08-21; awaiting
re-derivation" the appropriate ledger note. Even with both passes, §6's claim-target must be the
three-object split of §6 above: the implication PROVED with $\mathcal R_r$ a named hypothesis, the
18 nodes NUMERICAL, and the node-to-region promotion OPEN.

**Largest risk carried forward:** not the proof, but Step 11. The certificate's economic content is
regional and the run delivers nodes. **C1-O2** points at an in-repo construction (D8's $\varepsilon$-
ball plus integral control) that has already done this once in this project; Part (D) is the piece
of C1 that plugs into it.
