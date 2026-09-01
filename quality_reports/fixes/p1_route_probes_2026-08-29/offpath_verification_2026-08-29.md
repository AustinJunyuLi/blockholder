# Off-path family: independent verification of two exploration findings

**Date:** 2026-08-29
**Verifier:** fresh Opus agent — did **not** write the p1-existence-route exploration, did not
write the probes it filed, and read `.scratch/p1-existence-route/` only to obtain the findings'
wording. No git was run. Nothing under `numerical_v4/`, `research/model_v4/MODEL_CARD.md`, the
mirrors, `LABEL_LEDGER.md` or `proofs/P1_proof.md` was edited.
**Card stamp verified before relying on any card text:** `MODEL_CARD.md:3` reads
*"Version stamp: 2026-08-28 · re-review audit repairs (P1-row A5 clause + §5 A5 evidence note +
A($\tau$) lead + §4.4 O-1 parenthetical) · commit `59c0dfc`."* — matches the dispatch.
**Posture:** refute-first. Every claim below is either a quoted file line or an executed,
gated measurement; nothing is carried from the exploration's prose.

## The two findings, verbatim

**FINDING 1** (`.scratch/p1-existence-route/issues/01-route-exploration.md:298–303`):

> Related and separate: the card's "the implementation's `OFF_PATH_EPS` = 1e-14 **is** the
> fixed-`t` constrained game" is, read strictly, not what the code does — `if Wm[t] > 0.0:
> continue` is a hard switch at exactly-zero mass, and the belief at an exclusive history is
> floor-size-independent, so the implementation faithfully realises the **`t = 0`** card
> construction. The genuine continuous fixed-`t` game was **unmeasured** before probe C.

**FINDING 2** (same file, `:276–297`, headline sentence at `:292–294`):

> So **locus (i) of card §5's A3 note does not reproduce under a Step-9(b)-faithful
> mass-proportional family.**

## Verdicts

| # | Verdict |
|---|---|
| **F1** | **CONFIRMED** on both operative clauses (hard switch; not the fixed-$t$ game), **NARROWED** on the definite article in "the $t=0$ construction" — it realises the $t\downarrow0$ limit of a *uniform-floor* family, which is Step 9(b)'s limit only at type-exclusive histories. The card sentence's **first half is wrong**; its hedge is **right and now measured**. |
| **F2(a)** | **CONFIRMED.** Step 9(b) weights each dead type by likelihood-times-signal-mass, not equally. **No card/proof discrepancy**: card `:274`'s "plan-uniform posterior" and the proof's $\Lambda_u$ are the same object described over different indices. `pooled.py` implements a **third** object. |
| **F2(b)** | **CONFIRMED.** Rebuilt from scratch; the exploration's numbers reproduce (3→1 at $+10^{-4}$; $6.334\times10^{-3}$ and $6.8\times10^{-6}$; 8/8 at the pinned point, widened here to 10/10). |
| **F2(c)** | **NARROWED.** True over every offset the card's open-set claim ranges over, and the argmax does become weakly increasing there — but the failure is **relocated, not removed**: 3 sign changes at $+4\times10^{-2}$ … $+10^{-1}$ under the proof-faithful family, where the shipped family gives 1. $\mathcal S(k)=\emptyset$ on an open set of $k_2$ at this node under **both** families. |
| **F2(d)** | **CONFIRMED and widened.** 10/10 at the pinned point fp1 (the exploration tested 8); 18/20 across both fixed points, and 20/20 once the two off-spec rows (uniform floor at $\varepsilon=10^{-6}$, an injection ~110× Step 9(b)'s at the same $\varepsilon$) are excluded. Every Step-9(b) row and every row at `OFF_PATH_EPS` reverses at both fixed points. |

**`t2_a3_ordered_plans_check.py`/`.json` stays valid as the shipped-family record — I agree
explicitly.** My probe 2's shipped rows reproduce its locus-1 ladder counts (1/3/3/3/3/3/1/1) and
its three 7-dp crossing literals exactly; my probe 3's shipped rows reproduce its twelve filed
7-dp payoff strings, its $n(s)=8/7$ and the reversal at both fixed points. Nothing in that check
is withdrawn or weakened by anything below.

The same holds for `t2_a6_edge_jump_check` — with one addition the orchestrator should see: §1.8
finds that its filed jump magnitudes are **also** shipped-family-specific (the first edge moves
$6.33\times10^{-3}\to7.05\times10^{-3}$, +11.4%, under the proof-faithful family), while the
discontinuity they establish survives the family change. That is a scope label on the numbers,
not a withdrawal, and it is the one place where this verification reaches past the two findings
it was sent to check.

---

## Probes landed (all beside this file, all deterministic, no RNG)

| script | JSON | gates | failed |
|---|---|---|---|
| `v_offpath_family_facts.py` | `v_offpath_family_facts.json` | facts only, no gates | — |
| `v_offpath_locus1_ladder.py` | `v_offpath_locus1_ladder.json` | 10 | 0 |
| `v_offpath_locus2_node15.py` | `v_offpath_locus2_node15.json` | 5 | 0 |
| `v_offpath_switch_vs_fixedt.py` | `v_offpath_switch_vs_fixedt.json` | 5 | 0 |

Three of the four carry a **DECLARED POST-RUN-1 RESTRUCTURE** block in the module docstring, on
the `t2_a3_ordered_plans_check.py` precedent: the run-1 table and every run-1 miss are preserved
verbatim in the docstring and in the JSON (`prereg_run1`), and what changed is gate *form* and
ladder *length*, never a measured number. The restructures are (R1)–(R3), (S1), (T1) and each
says which pre-registration it replaces and why. Two of the three restructures exist because a
pre-registration was **refuted** — those refutations are findings `F-relocate` and
`F-uniform-1e6`, recorded ungated, and they are the substance of the F2(c) and F2(d) narrowings.

Each script monkeypatches `numerical_v4.pooled._alive_weights` in memory and restores it in a
`finally` block; nothing under `numerical_v4/` is written. **Probes 2 and 4 carry harness
control gates** (`P2`, `R1a`) requiring the patched `switch_uniform` replica at
$\varepsilon=$ `OFF_PATH_EPS` to reproduce the unpatched run's located crossings bit for bit;
both pass. **Probe 3 has no such gate** — it uses the same family constructor as probes 2 and 4
and inherits their validation, and its own `Q1` independently anchors the unpatched run against
the curated `t2_a3_ordered_plans_check` record.

---

## FINDING 1 — is `OFF_PATH_EPS` the fixed-$t$ constrained game?

### 1.1 What the code actually does

`numerical_v4/pooled.py:202` and `:225–235`, quoted exactly:

```python
OFF_PATH_EPS: float = 1e-14
...
    Wm, WVm, WAm = W.copy(), WV.copy(), WA.copy()
    if ref is not None:
        for t in range(n_theta):
            if Wm[t] > 0.0:
                continue
            if ref.D[t] == 1.0 and ref.f[t] <= d:
                continue                    # this type's flag would be public
            Wm[t] = OFF_PATH_EPS
            WVm[t] = OFF_PATH_EPS * ref.Ev[t]
            WAm[t] = OFF_PATH_EPS * ref.a[t]
    return W, Wm, WVm, WAm
```

`OFF_PATH_EPS`'s role, established by reading the whole 426-line belief construction and by
`grep`: it is the **type-level prior weight assigned to a mark-path type whose alive measure is
exactly zero**, and nothing else. It enters `market`, `num_v`, `num_a` at `:279–281`, hence
$\hat v$ and $\pi$ at `:286–287`, hence `inner_price`. It never touches `mass` (`:278`, guarded
by `if W[t] > 0.0`), so it cannot leak into a reported measure — the docstring at `:213` says so
and the code honours it. Elsewhere in the tree it appears only in
`quality_reports/fixes/t2_atau_support_check.py` (which re-implements the same floor) and in the
2026-08-27/29 probe directories.

Three properties follow directly and are decisive:

1. **It is a switch, not a perturbation.** `if Wm[t] > 0.0: continue` applies the floor **only**
   where the alive mass is *exactly* `0.0`. A type with mass $10^{-30}$ receives no floor. So
   $k\mapsto W^m$ is discontinuous on $\{k : W[t]=0\}$. Step 9(b)'s
   $w_n(j\mid s)=(1-t_n)\mathbf 1\{j=j_k(s)\}+t_n/J$ perturbs **every** type at **every** $k$ and
   is continuous in $k$ by construction. These are different maps.
2. **The value attached jumps too.** Below the transition the type carries its own shrinking
   atom's conditional mean $\mathbb E[v\mid \text{sliver}]$; at the transition it carries
   `ref.Ev[t]` $=\mathbb E[v\mid n(s)=t]$ over the **whole line** (`menu.py:324–358`). The jump
   is in the numerator as well as the weight.
3. **The floor size is invisible off path.** At a dead-only history $\varepsilon$ divides out of
   $\hat v=\text{num}\_v/\text{market}$. **This does not discriminate** — it is equally true of a
   genuine blend, where $W^m=(1-t)\cdot 0+(t/J)m_\theta$ and $t$ divides out identically. Step
   9(b) says as much at `P1_proof.md:534–536`: in the $\Lambda_k=0$ case
   "$\mu_n=L_j\varphi_s/\Lambda_u$ **exactly and $n$-free**". No gate below leans on it.

### 1.2 The card sentence and its hedge

`MODEL_CARD.md:308–310`, quoted exactly:

> The implementation's
> `OFF_PATH_EPS` $= 10^{-14}$ **is** the fixed-$t$ constrained game — the standard repair already
> shipped, with the switch relocated by $\sim10^{-9}$ rather than removed.

Adjudicated charitably and honestly, the hedge and the first half say different things. The
hedge concedes only that *a discontinuity survives*, which is compatible with a fixed-$t$ game at
a very small $t$. The first half asserts an **identification of the object**. The identification
is what fails, on three independent measurements.

### 1.3 Measurement (a) — at the shipped constant, the blend and the switch are the same map

`v_offpath_switch_vs_fixedt.py` §A. $\mathcal T_2$ = lowest up-crossing of $U_V-U_H$
(`t_blend_settle.py`'s own definition and 4001-point grid, so its filed numbers replay), at
$k_2=\text{edge}(8)\mp10^{-8}$, $(\kappa{=}0.5,\tau_{50},T{=}5)$, $k_1=k^\star_1$:

| family | $\varepsilon$ | $\mathcal T_2$ below | $\mathcal T_2$ above | local step |
|---|---|---|---|---|
| shipped (unpatched) | — | 1.5497289514 | 1.5433951737 | **6.3338e-03** |
| `switch_uniform` (replica) | 1e-14 | 1.5497289514 | 1.5433951737 | 6.3338e-03 |
| `switch_uniform` | 1e-09 | 1.5463875630 | 1.5433951656 | 2.9924e-03 |
| `switch_uniform` | 1e-06 | 1.5419532976 | 1.5433870652 | 1.4338e-03 |
| **`blend_uniform`** (genuine fixed-$t$) | **1e-14** | **1.5497289490** | **1.5433951737** | **6.3338e-03** |
| `blend_uniform` | 1e-09 | 1.5466872629 | 1.5433951683 | 3.2921e-03 |
| `blend_uniform` | 1e-06 | 1.5433965446 | 1.5433897671 | **6.7775e-06** |
| `blend_step9b` | 1e-14 | 1.5497289970 | 1.5426742046 | 7.0548e-03 |
| `blend_step9b` | 1e-06 | 1.5423576573 | 1.5426727181 | 3.1506e-04 |

Gate `R1b`: at $t=$ `OFF_PATH_EPS` the genuine fixed-$t$ blend and the shipped switch agree to
$2.4\times10^{-9}$ in $\mathcal T_2$ and to five significant figures in the step. The shipped
constant buys **none** of the fixed-$t$ game's continuity. The blend smooths only at
$t=10^{-6}$, and that row reproduces the exploration's probe C ($6.8\times10^{-6}$) as does the
shipped row ($6.334\times10^{-3}$).

### 1.4 Measurement (b) — how large $t$ would have to be

The blend smooths only where the floor $\varepsilon m_\theta/J$ dominates the dying sliver's
alive mass $\approx\varphi_s(s)\cdot|\text{offset}|$, i.e. below a half-width
$\varepsilon m_\theta/(J\varphi_s)$. At edge(8), dying type 9, $m_9=0.0272$,
$\varphi_s=0.40146$ (`v_offpath_switch_vs_fixedt.json`, `B_crossover_width`):

| $\varepsilon$ | half-width |
|---|---|
| **1e-14 (shipped)** | **2.262e-16** |
| 1e-12 | 2.262e-14 |
| 1e-09 | 2.262e-11 |
| 1e-06 | 2.262e-08 |

One double-precision ulp at edge(8) is $2.220\times10^{-16}$. So at the shipped constant the
window in which the fixed-$t$ game differs from its own $t\downarrow0$ limit is **one ulp wide**,
and $4.4\times10^{6}$ times narrower than `menu.breakpoints`' merge tolerance (gate `R3`). The
implementation cannot be inside that window at any representable $k$.

### 1.5 Measurement (c) — the hedge is right, and its mechanism is the breakpoint merge

`menu.py:244` merges near-duplicate breakpoints at `np.diff(arr) > 1e-9`. Sweeping
$k_2\uparrow\text{edge}(8)$ (`v_offpath_family_facts.json`, `switch_location_sweep`):

| offset below edge(8) | # breakpoints | dying type | $W[9]$ | dead? |
|---|---|---|---|---|
| 1e-08 | 20 | 9 | 4.014619e-09 | False |
| 2e-09 | 20 | 9 | 8.029237e-10 | False |
| **1e-09** | **20** | **9** | **4.014620e-10** | **False** |
| **9.9e-10** | **19** | **9** | **0.000000e+00** | **True** |
| 1e-12 | 19 | 9 | 0.000000e+00 | True |

The type dies between $10^{-9}$ and $9.9\times10^{-10}$ below the true edge — the merge
tolerance exactly. **The card's "$\sim10^{-9}$" is correct and its mechanism is now identified
and measured.** The merge silently reassigns a $10^{-9}$-wide sliver: `atoms`' `verify`
assertion samples at 0.15/0.85 of the atom, both of which land past the dropped edge, so it does
not fire.

### 1.6 Measurement (d) — the shipped $t\downarrow0$ limit is not Step 9(b)'s

This is where F1 and F2 are the same discrepancy on two axes. At
$(\kappa{=}0.5,\tau_{50},T{=}5)$, $k_2=\text{edge}(6)+10^{-4}$, floored types $\{7,\dots,11\}$,
counting **dead-only** pooled histories (every alive type has zero likelihood) reachable by **two
or more** dead types (`v_offpath_switch_vs_fixedt.json`, `C_multi_dead_histories`):

| date $d$ | histories | multi-dead-only | max $\lvert\Delta\hat v\rvert$ |
|---|---|---|---|
| 0–5 | 4 … 4096 | 0 | — |
| 6 | 16 384 | 729 | 2.996e-01 |
| 7 | 65 536 | 3 645 | 3.084e-01 |
| 8 | 262 144 | 15 309 | 3.055e-01 |
| 9 | 1 048 576 | 59 049 | 3.098e-01 |
| **10 = H** | 4 194 304 | **157 464** | **3.106e-01** |

Both beliefs are $\varepsilon$-free, so this gap **survives $t\downarrow0$** and is not a
fixed-$t$-versus-limit question at all (gate `R4`). Against $\hat v$ values running 0.85–2.23
(`v_offpath_family_facts.json`, type table) a gap of 0.31 is 15–35%.

### 1.7 F1 verdict

**CONFIRMED**, with one narrowing.

- "is a hard switch" — **confirmed** by the code (`:228`) and by §1.5's measured jump
  $4.01\times10^{-10}\to$ exactly $0.0$.
- "not the fixed-$t$ game" — **confirmed** by §1.3 (the fixed-$t$ game at $t=$`OFF_PATH_EPS` is
  the same map as the switch, to 5 s.f.), §1.4 (its distinguishing window is one ulp) and §1.6
  (it differs from Step 9(b)'s family at **every** $t$, not just in the limit).
- "realising **the** $t=0$ construction" — **narrowed**. It realises the $t\downarrow0$ limit of a
  *uniform-floor* family. That coincides with Step 9(b)'s limit at **type-exclusive** histories —
  which is why the A6 panel's `type_reference` verification stands, as the panel recorded
  (`threads/2026-08-27_A6_panel_substantiate.md:97`) — and differs from it on the 157 464
  multi-dead-type histories of §1.6.

**On the hedge:** it does not rescue the first half. "Relocated rather than removed" reports that
a discontinuity survives; the measurements show the identification itself is false, and that the
$\Theta$-continuity Step 18's route would buy is **not** present in the implementation at any
resolvable scale. The hedge's own content is independently correct and now has a mechanism.

### 1.8 A consequence for the A6 note I did **not** expect, and it cuts against my own draft

I first wrote that the A6 note's $\mathcal T_2$ jump measurements are untouched by the family,
on the panel's "the floor cancels at an exclusive history" reasoning. **The data refutes that,
and the correction belongs here rather than in a later round.** From §1.3's table, at the same
edge(8) $\pm10^{-8}$ bracket:

| family | $\varepsilon$ | local step |
|---|---|---|
| shipped | — | 6.3338e-03 |
| `blend_step9b` (proof-faithful, genuine fixed-$t$) | 1e-14 | **7.0548e-03** |

The jump **survives** the family change — A6's continuity clause still fails, which is the note's
actual conclusion — but its **magnitude moves by +11.4%**, and $\mathcal T_2$ above the edge moves
by $7.2\times10^{-4}$. So the A6 note's filed $6.33\times10^{-3}$ (and, by the same mechanism,
presumably its $1.09\times10^{-2}$ and $2.83\times10^{-2}$, which I did **not** measure) are
**shipped-family-specific numbers**, exactly as locus (i)'s three sign changes are. The A6
conclusion is family-robust; the A6 numbers are not. Amendment A is worded to say this rather
than the stronger thing I first drafted.

---

## FINDING 2 — does locus (i)'s A3 failure track the off-path family's shape?

### 2(a) What Step 9(b) actually specifies — quoted, not paraphrased

`research/model_v4/proofs/P1_proof.md`, Step 9(b). Line 496:

> $$w_n(j\mid s)=(1-t_n)\,\mathbf 1\{j=j_k(s)\}+\tfrac{t_n}{J},\qquad t_n:=\tfrac Jn\downarrow0,$$

Lines 504–507:

> $$\mu_n(j,s)=\frac{w_n(j\mid s)\,L_j(\mathcal H_d^P\mid s)\,\varphi_s(s)}
> {\sum_{j'\in\mathcal J}\int w_n(j'\mid s')\,L_{j'}(\mathcal H_d^P\mid s')\,\varphi_s(s')\,
> \mathrm ds'}.$$

Lines 528–531:

> write $Z_n=(1-t_n)\Lambda_k+(t_n/J)\Lambda_u$ for
> the denominator — the display above with $w_n$ expanded — where
> $\Lambda_k=\int L_{j_k(s')}(\mathcal H_d^P\mid s')\varphi_s(s')\,\mathrm ds'$ is the
> unperturbed aggregate, $\Lambda_u=\sum_{j'}\int L_{j'}(\mathcal H_d^P\mid
> s')\varphi_s(s')\,\mathrm ds'$ the plan-uniform one, and $t_n=J/n$ the perturbation mass.

Lines 534–536:

> *If $\Lambda_k=0$* — the $k$-null case — the $(1-t_n)$ term
> vanishes $\Phi_s$-a.e. in numerator and denominator alike, so $\mu_n=L_j\varphi_s/\Lambda_u$
> **exactly and $n$-free**, and there is nothing to pass to the limit.

**Answer to the discriminating question.** The limit density over $(j,s)$ is
$L_j(\mathcal H\mid s)\varphi_s(s)/\Lambda_u$. The **plan** weights are uniform — the $t_n/J$
cancels between numerator and denominator, so $j$ enters only through $L_j$. The **signal**
weighting is $\varphi_s$, and the whole thing is scaled by the likelihood. Grouping $(j,s)$ by
mark-path type $\theta(j,s)$ — which is what the implementation's type index is
(`menu.py:139–147`) — gives, for the finite-alphabet implemented menu,

$$\Lambda_u(\mathcal H)=\sum_\theta L_\theta(\mathcal H)\,m_\theta,\qquad
m_\theta:=\sum_{j'\in\mathcal J}\Pr\nolimits_s\bigl(\theta(j',s)=\theta\bigr),$$

$$\hat v(\mathcal H)=\frac{\sum_\theta L_\theta(\mathcal H)\,m_\theta\,\bar v_\theta}
{\sum_\theta L_\theta(\mathcal H)\,m_\theta},\qquad \bar v_\theta=\texttt{ref.Ev}[\theta].$$

So Step 9(b) weights each dead type by **likelihood-times-signal-mass**, *not* equally. On this
menu (`menu.py:6–11`: Exit and Hold both give the all-zero path at every $s$; Voice gives
$\theta=n(s)$) that is $m_0=2$ and $m_\theta=\Pr(n(s)=\theta)$ for $\theta\ge1$. Measured
(`v_offpath_family_facts.json`): $m_7\ldots m_{11}=0.0310,\,0.0290,\,0.0272,\,0.0256,\,0.7424$ —
a factor of 29 between the largest and smallest, so "uniform" and "mass-proportional" are far
apart here.

**Is the card's `:274` wording a discrepancy?** `MODEL_CARD.md:273–275` reads:

> Step 9(b)
> gives Bayes where $\Lambda_k(h) > 0$ but a $k$-free plan-uniform posterior on the frontier

**No — the same object described over a different index.** "Plan-uniform" names the plan
marginal of the perturbation ($t_n/J$ per plan); "mass-proportional" names the type weights it
*induces* through $\varphi_s$ and $L$. Both are $\Lambda_u$. There is no card-versus-proof
discrepancy here, and the exploration did not claim one — it flagged the tension for
adjudication, and the adjudication is that the two descriptions agree.

**What `pooled.py` implements is a third object.** `Wm[t] = OFF_PATH_EPS` for every floored type
(`:232`) is $m_\theta\equiv\text{const}$, so
$\hat v=\sum_\theta L_\theta\bar v_\theta/\sum_\theta L_\theta$ — likelihood-weighted but **not**
mass-weighted. It agrees with Step 9(b) exactly at a **type-exclusive** history (one type, the
weight cancels) and differs wherever two or more dead types reach the history (§1.6).

**Exactness of the family used to test this**, checked rather than assumed
(`v_offpath_family_facts.py`, `exactness_precheck`):

- At locus (i) the floored set is $\{7,8,9,10,11\}$ at **every** date $d=0\ldots H$, and each of
  those five has `ref.D`$=0$, `ref.f`$=\infty$, **constant on its whole $n(s)$ cell** (verified by
  a 201-point scan per cell). So Step 9(b)'s flag indicator is vacuous for them and
  $m_\theta=\Pr(n(s)=\theta)$ is **exactly** $\Lambda_u$'s weight for every type that is floored
  there.
- Type 0's mass is where the exploration's `uniform_type_mass` is wrong (it returns 0; the
  Step-9(b) value is 2). Inert: $W[0]\in[0.855,0.885]$ at **every** ladder offset, so type 0 is
  never floored. Gate `P3b` confirms the exploration's family and the exact Step-9(b) family give
  identical counts at every $\varepsilon$ and every offset.

### 2(b) Do the exploration's probes reproduce?

Yes, rebuilt independently rather than re-run:

- `t_blend_diagnose`'s headline (3 sign changes under uniform, 1 under mass-proportional, at
  $k_2=\text{edge}(6)+10^{-4}$, $\varepsilon$-invariant) reproduces in my probe 2 at that offset
  and across a longer ladder.
- `t_blend_settle`'s probe C ($6.334\times10^{-3}$ shipped, $6.8\times10^{-6}$ blend at
  $\varepsilon=10^{-6}$) reproduces to 5 s.f. and 2 s.f. respectively (§1.3).
- `t_blend_settle`'s part B (8/8 at the pinned point) reproduces and widens to 10/10 (§2d).

I also audited the exploration's `make()` for correctness, not just determinism: the
`_ORIG(..., ref=None)` call returns un-floored weights (so the `WVm.copy()` on the next line is a
no-op, harmless); the blend branch correctly perturbs live types as well as dead ones; and the
`ref.D[t] == 1.0 and ref.f[t] <= d` skip is applied before the floor in both branches. One
cosmetic asymmetry: in the blend branch a type whose flag would be public keeps $W[t]$ unscaled
by $(1-\varepsilon)$ instead of being set to $(1-\varepsilon)W[t]$. Immaterial at these scales; my
families do the same thing for comparability and it is declared in their docstrings.

### 2(c) The 1-vs-3 result at locus (i) — **NARROWED**

`v_offpath_locus1_ladder.py`, at the card's own protocol (node $(\kappa{=}0.5,\tau_{50},T{=}5)$,
$k_1=k^\star_1$, 6001-point grid, strict criterion $\mathrm{sign}(v_{[:-1]})\cdot
\mathrm{sign}(v_{[1:]})<0$, `brentq` at `xtol=1e-13`) — not the exploration's single point on a
4001-point grid. Anchors gated to $10^{-9}$ against the filed literals
($\tau_{50}=0.09076405861553302$, $k_1=1.2405757282617416$, edge(6), edge(8)).

Strict sign changes of $U_V-U_H$, $k_2=\text{edge}(6)+\text{offset}$:

| family | $\varepsilon$ | −1e-9 | 1e-9 | 1e-4 | 1e-3 | 5e-3 | 2e-2 | 3e-2 | **4e-2** | 5e-2 | 7e-2 | 1e-1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **shipped** | — | 1 | **3** | **3** | **3** | **3** | **3** | 3 | 1 | **1** | 1 | **1** |
| `switch_uniform` | 1e-14 | 1 | 3 | 3 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| `blend_uniform` | 1e-6 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| **`switch_step9b`** | 1e-14 | 3 | **1** | **1** | **1** | **1** | **1** | 1 | **3** | **3** | 3 | **3** |
| `switch_step9b` | 1e-6 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 3 | 3 | 3 |
| `switch_expl` (exploration's) | 1e-14 | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 3 | 3 | 3 |
| `blend_step9b` | 1e-14 | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 3 | 3 | 3 |
| `blend_step9b` | 1e-6 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 3 | 3 | 3 |

Bold entries in the shipped row are the card's own filed record; gate `P1a` reproduces it and
gate `P1b` reproduces the three 7-dp locations at $+10^{-9}$ — `1.5754434 / 1.5833333 /
1.5902426` — exactly.

**What is confirmed.** Over every offset the card's open-set claim ranges over
(`MODEL_CARD.md:191`, "verified at offsets $10^{-9}$ through $2\times10^{-2}$") the Step-9(b)
family gives **one** sign change (gate `P3`), and the pointwise argmax becomes **weakly
increasing** — word `E,V` with runner-up gaps 0.0115 and 0.0973, so a weakly increasing selection
**exists** and A3's second clause is not violated there (gate `P5b`). The exploration's headline
holds where it was tested.

**The two families are exactly complementary on all eleven offsets** — wherever one gives three
strict sign changes the other gives one, and both flip at the *same* boundary, between
$+3\times10^{-2}$ and $+4\times10^{-2}$. That is the cleanest statement of the finding: the
off-path family does not switch the A3 failure off, it swaps which half of the $k_2$ ladder
carries it.

**What narrows it.** At $+4\times10^{-2}$ through $+10^{-1}$ the Step-9(b) family gives **three**
sign changes with argmax word `E,V,H,V` — non-monotone — and these are precisely the offsets at
which the **shipped** family gives one. The flip sits between $+3\times10^{-2}$ (one) and
$+4\times10^{-2}$ (three). So $\mathcal S(k)=\emptyset$ on an open set of $k_2$ at this node under
**both** families; the proof-faithful family **relocates** locus (i)'s failure rather than
removing it (finding `F-relocate`, ungated — it refuted a pre-registration).

**A note on the argmax words, so two sampling conventions are not silently mixed.** My intervals
are cut at $s_{lo}$, the located sign changes, and $s_{hi}$, and sampled at midpoints — declared
in `v_offpath_locus1_ladder.py` under `P5a`. The leading `E` is therefore an artefact of that
choice: the first midpoint sits below $k_1$, in the ordinary Exit region. The card's locus (i)
wording is "H,V,H,V", measured under the panel's *buffered* geometry around the crossings. The
two conventions agree on the content that is gated and that matters — the `V,H,V`
non-monotonicity across the crossings, hence $\mathcal S(k)=\emptyset$. Amendment B is worded to
avoid asserting either word.

**What drives it — the reference measure, not the continuity.** Gate `P4b`: `blend_uniform`
(continuous, uniform reference) tracks the shipped hard switch at every offset and every
$\varepsilon$; `blend_step9b` (continuous, Step-9(b) reference) tracks `switch_step9b`. Gate
`P4`: the count is $\varepsilon$-invariant within each family at every offset except $-10^{-9}$,
the one offset where the dying type is still alive with a sliver mass ($4\times10^{-10}$)
comparable to the floor — the fixed-$t$ crossover of §1.4 showing up exactly where §1.4 predicts
(finding `F-eps`). The exploration's diagnosis of the mechanism is therefore **confirmed**; only
its inference about the consequence for A3 needed narrowing.

### 2(d) The pinned node $(\kappa{=}0.15,\,0.05,\,5)$ — **CONFIRMED and widened**

`v_offpath_locus2_node15.py`, at `t2_a3_ordered_plans_check.py`'s locus-2 protocol: both located
fixed points (fp1 $=(1.020221781,1.659062163)$, the pinned one; fp2 $=(1.0260443221,
1.7104049079)$), the 12-dp edge $1.659062162746$ at its own $\pm10^{-6}$ offsets, argmax over
$\{$EXIT, HOLD, VOICE$\}$ with a strict-singleton test.

Gate `Q1`: the shipped family reproduces the curated record — all twelve filed 7-dp payoff
strings, $n(s)=8$ below and $7$ above, VOICE below → HOLD above at both fixed points.

Gate `Q2b`: **all ten** family × scale rows at fp1 reverse VOICE → HOLD (the exploration filed
8 of 8; this widens it). $U_V-U_H$ just below runs $+6.44\times10^{-4}$ to $+2.39\times10^{-3}$
across the families and is $\approx-1.28\times10^{-3}$ just above in every one, with 5 strict
sign changes on both the 4001- and 6001-point grids.

Gate `Q2`/`Q3`: across **both** fixed points, 18 of 20 rows reverse. The two that do not are
`switch_uniform` and `blend_uniform` at $\varepsilon=10^{-6}$ **at fp2** ($U_V-U_H$ just below
$=-3.85\times10^{-5}$ instead of $+1.06\times10^{-3}$) — recorded as finding `F-uniform-1e6`,
ungated. Those two rows are off-spec on both axes: a uniform floor is not Step 9(b)'s reference,
and $\varepsilon=10^{-6}$ is $10^{8}$ times the shipped constant and injects ~110× more weight
per dead type than Step 9(b) does at the same $\varepsilon$ ($10^{-6}$ vs
$\varepsilon m_\theta/J\approx9\times10^{-9}$). **Every** Step-9(b) row at both scales and
**every** row at $\varepsilon=$ `OFF_PATH_EPS` reverses at **both** fixed points.

**So locus (ii) carries A3's verdict on its own, independently of the family** — which is what
keeps A3's overall verdict standing regardless of 2(c), and 2(c) does not in fact need it, since
the failure survives there too.

### 2(e) A third, independent implementation-vs-card gap, flagged not chased

`menu.type_reference` (`menu.py:341–357`) reads **one midpoint clock** per $n(s)$ cell for
`D[t]` and `f[t]`. At locus (i) that is harmless — a 201-point scan finds every floored type's
cell $(D,f)$-constant. At locus (ii) it is not: **type 11's cell spans $[-3.2426407,
1.4082483]$ with $D\in\{0,1\}$ and $f\in\{9,\dots,15,\infty\}$**, and type 11 is floored there
($m_{11}=0.742$, the dominant mass). A fully Step-9(b)-exact $\Lambda_u$ would restrict type 11's
mass to its unflagged sub-cell at each date. Both the shipped family and every family tested here
inherit this from `type_reference`, so it is orthogonal to the axis under test and cannot explain
any result above — but it is a third gap between the implementation and Step 9(b), and it is
recorded in `v_offpath_locus2_node15.json` (`exactness_caveat`) rather than left implicit. Not
verified beyond the cell scan; no claim is made about its size.

---

## Drafted amendments — DRAFTED ONLY, NOT APPLIED

Style follows the card's existing dated evidence notes: supersede by quoting the superseded text,
never silently rewrite; state what does **not** move.

### Amendment A — §5, A6 block, appended after the sentence at `MODEL_CARD.md:308–310`

**Mirror sites for the same superseded sentence** (verified 2026-08-29 against the stamp-`59c0dfc`
files): `research/model_v4/model_v4.md:369` and `research/model_v4/model_v4.tex:489–490`
(`\texttt{OFF\_PATH\_EPS} $=10^{-14}$ \textbf{is} the fixed-$t$ constrained game ---`). Both are
transcriptions and must be synced with whatever the card takes.

> *Off-path-family verification note added 2026-08-29 (independent verifier who did not write the
> route exploration; probes `quality_reports/fixes/p1_route_probes_2026-08-29/v_offpath_*`, 20
> gates across three checks, 0 failed).* **The sentence above beginning "The implementation's
> `OFF_PATH_EPS` $= 10^{-14}$ **is** the fixed-$t$ constrained game" is superseded: its first half
> is wrong, its hedge is right and now has a measured mechanism.** What `numerical_v4/pooled.py`
> `:225–235` ships is a **hard switch** — `if Wm[t] > 0.0: continue` floors a type only where its
> alive mass is **exactly** zero, so $k\mapsto W^m$ is discontinuous on $\{k:W[t]=0\}$, where Step
> 9(b)'s $w_n(j\mid s)=(1-t_n)\mathbf 1\{j=j_k(s)\}+t_n/J$ perturbs every type at every $k$ and is
> continuous in $k$. Three measurements: (a) at $t=$ `OFF_PATH_EPS` a genuine fixed-$t$ blend and
> the shipped switch are **indistinguishable** — $\mathcal T_2$ across the edge(8) $\pm10^{-8}$
> bracket agrees to $2.4\times10^{-9}$ and the local step to five significant figures
> ($6.3338\times10^{-3}$ both); the blend smooths only at $t=10^{-6}$ ($6.78\times10^{-6}$); (b)
> the window in which the fixed-$t$ game differs from its own $t\downarrow0$ limit has half-width
> $\varepsilon m_\theta/(J\varphi_s) = 2.26\times10^{-16}$ at $\varepsilon=10^{-14}$ — **one
> double-precision ulp** at edge(8), and $4\times10^{6}$ times narrower than `menu.breakpoints`'
> $10^{-9}$ merge tolerance; (c) the floor is **uniform across dead types** where $\Lambda_u$ is
> **mass-proportional**, so the shipped $t\downarrow0$ limit is not Step 9(b)'s: at
> $(\kappa{=}0.5,\tau_{50},T{=}5)$, $k_2=\text{edge}(6)+10^{-4}$, **157 464** dead-only pooled
> histories at $d=H$ are reachable by two or more dead types and on them the two $\hat v$ differ
> by up to $0.31$ — an $\varepsilon$-free gap, hence not a fixed-$t$-versus-limit question.
> **The hedge stands and is now measured:** the switch is relocated, not removed, and the
> relocation is `menu.breakpoints`' near-duplicate merge (`menu.py:244`, `np.diff > 1e-9`) — the
> dying type's alive mass is $4.01\times10^{-10}$ at $k_2=\text{edge}(8)-10^{-9}$ and **exactly
> $0.0$** at $\text{edge}(8)-9.9\times10^{-10}$. **Read the corrected claim as: Step 18's standard
> repair is *not* shipped; what is shipped is the $t=0$ limit of a uniform-floor family, and the
> $\Theta$-continuity the $t$-constrained game would buy is absent from the implementation at
> every resolvable scale.** **What does and does not move above:** the belief-snap agreement and
> the `type_reference` verification stand — they sit at **type-exclusive** histories, where the
> floor cancels and `type_reference` **is** Step 9(b)'s limit — and the continuity clause still
> fails under the proof-faithful family, so **the A6 conclusion is family-robust**. Its *numbers*
> are not: at the same edge(8) $\pm10^{-8}$ bracket a Step-9(b)-faithful fixed-$t$ blend at
> $t=10^{-14}$ gives a local step of $7.05\times10^{-3}$ against the shipped
> $6.33\times10^{-3}$, **+11.4%**, with $\mathcal T_2$ above the edge moving $7.2\times10^{-4}$.
> The filed jump magnitudes above — and the curated `t2_a6_*` checks that replay them — are
> therefore **shipped-family records**, valid as such and not withdrawn. (Measured at the first
> edge only; the $1.09\times10^{-2}$ and $2.83\times10^{-2}$ figures were not re-measured under
> the proof-faithful family.) No label moves and none is licensed — A6 is a hypothesis.

### Amendment B — §5, A3 block, appended to the locus (i) material

**Mirror sites for the locus (i) material** (verified 2026-08-29):
`research/model_v4/model_v4.md:255` and `research/model_v4/model_v4.tex:355`.

> *Off-path-family scope note added 2026-08-29 (independent verifier; probes
> `quality_reports/fixes/p1_route_probes_2026-08-29/v_offpath_locus1_ladder.py`/`.json`, 10 gates,
> 0 failed, whose shipped rows reproduce this note's counts at every ladder offset and its three
> $7$-dp crossing locations exactly).* Locus (i)'s failure is recorded **under the implemented
> off-path family**, whose floor is uniform across dead types where Step 9(b)'s $\Lambda_u$ is
> mass-proportional (A6 note, 2026-08-29 verification note). Under a **Step-9(b)-faithful
> mass-proportional family** the failure at this node is **relocated, not removed**: over the
> offsets quoted above ($10^{-9}$ through $2\times10^{-2}$) the count falls to **one** sign change
> and the pointwise argmax becomes **weakly increasing**, so $\mathcal S(k)\ne\emptyset$ there —
> but at offsets $4\times10^{-2}$ through $10^{-1}$, where the **shipped** family gives one, it is
> **three**, with the argmax **non-monotone across the crossings** in the same $\ldots$V,H,V
> pattern, so $\mathcal S(k)=\emptyset$ on an open set of $k_2$ at this node under **both**
> families. The two families are **exactly complementary** over the eleven offsets tested and
> flip at the **same** boundary, between $+3\times10^{-2}$ and $+4\times10^{-2}$: the family does
> not switch the failure off, it swaps which half of the ladder carries it. The
> driver is the **reference measure**, not the perturbation's continuity: a continuous fixed-$t$
> blend with a uniform reference tracks the shipped switch and one with the Step-9(b) reference
> tracks the mass-proportional switch, at every $\varepsilon\in\{10^{-14},10^{-9},10^{-6}\}$.
> **Locus (ii) is untouched**: the VOICE $\to$ HOLD reversal holds at **both** located fixed
> points under the shipped family, under the exact Step-9(b) family at both scales, and under
> every family at $\varepsilon=$ `OFF_PATH_EPS`, with all ten family $\times$ scale rows reversing
> at the pinned point (`v_offpath_locus2_node15.py`/`.json`, 5 gates, 0 failed) — **A3's verdict
> at this calibration does not depend on the family.**
> `t2_a3_ordered_plans_check.py`/`.json` **remains valid as the shipped-family record and nothing
> in it is withdrawn.** No label moves — A3 is a hypothesis; P1 stays PROVED as a conditional.

### Amendment C — optional, one sentence, wherever the third gap is best housed

> *Recorded 2026-08-29, unverified beyond a cell scan:* `menu.type_reference` reads one midpoint
> clock per $n(s)$ cell, and at $(\kappa{=}0.15, 0.05, 5)$ type 11's cell is **not**
> $(D,f)$-constant (it spans $[-3.2426407, 1.4082483]$ with $D\in\{0,1\}$, $f\in\{9,\dots,15,
> \infty\}$) while carrying the dominant plan-uniform mass $0.742$ — a **third** gap between the
> implementation's off-path construction and Step 9(b)'s $\Lambda_u$, common to every family
> tested and therefore orthogonal to the uniform-versus-mass-proportional finding. Size not
> measured; nothing above depends on it.

## What is not claimed

Nonexistence is neither claimed nor shown anywhere here. An edge-pinned fixed point of the
implemented cutoff map is not an equilibrium (fp1's payoff-scale residual is
$1.77\times10^{-3}$ against a $10^{-9}$ criterion), and the ticket-34 existence questions are
untouched. Every result is at one or two nodes, not swept over $(\kappa,\tau,T)$. No label moves
and none is licensed: A3 and A6 are hypotheses, and everything here is applicability evidence in
the A($\tau$) pattern. These probes are single-verifier: gated and pre-registered, but not yet
independently reproduced by a second agent.
