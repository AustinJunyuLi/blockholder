# ANALYST B — defusal brief on N11 (A6 continuity at collapsed vectors). Findings.

Worktree `/Users/austinli/Projects/blockholder_v4_theory`, branch v4-theory, HEAD 5a0829c.
Read-only; all writes in scratchpad. No git run.

## VERDICT: **NARROWED** (not DEFUSED-PROVED, not STANDS-as-N11-states-it)

The mechanism N11 names is real and it DOES reach `T`'s returned cutoffs — measured, at the
implemented calibration, at **non-collapsed** cutoff vectors. But N11's locus is wrong in both
directions, and the one collapse face the paper's baseline actually visits is provably clean.

---

## 1. The vanishing-mass defusal (brief item 1) — REFUTED, and I could not rebuild it

`T` is built from `U_j(s;k)` and the pooled-execution bracket is (P1_proof Step 11)

    U_j(s;k) = [flagged continuation]  -  E_z[ sum_{d<=f_j} P^P_d(H^P_d) (B_j(s,d) - B_j(s,d-1)) ]

The expectation is over the noise `z` **under the plan the deviator imagines playing**, conditional
on `(s,j)`. So a history generated only by the vanishing plan enters `U_j` with weight
`Pr(z_{0:d}) >= min(kappa/2, 1-kappa)^{d+1}` — bounded away from zero and **independent of the
collapsing plan's population mass**. The population mass never multiplies this term.

The implementation is literally this object: `numerical_v4/pooled.py` computes
`EP[d][t] = np.dot(L_t, P_d)` with `L_t` the type's own noise likelihood, and
`numerical_v4/policy.py::plan_payoff` reads `res.EP[d][theta(j,s)]`.

Measured (probe 3, frozen-tau baseline, sweep across `k2 = 1.583333`):
`U_VOICE(s0)` jumps `0.0362570819 -> 0.0365064990` (+2.494e-4) at the same `k` where
`U_HOLD(s0)` moves `0.0359582433 -> 0.0359582433` (< 1e-10). **No cancellation in the difference.**

## 2. Where the price system is actually k-discontinuous (sharper than N11)

Let `Lam_k(h) = int L_{j_k(s)}(h|s) phi_s(s) ds`. Step 9(b)'s rule is:
`Lam_k(h) > 0` -> Bayes under k; `Lam_k(h) = 0 < Lam_u(h)` -> plan-uniform posterior,
**independent of k**; `Lam_u(h) = 0` -> Step 9(c) reference root, independent of k.

`Lam_k(h)` is continuous in `k` (integrand bounded, `phi_s ds` atomless). Hence the price at `h` can
be discontinuous **only** on `bd{k in Theta : Lam_k(h) > 0}` — and generically is: the one-sided
limit is the value concentrating at the touching interval endpoint, the value AT the frontier is the
plan-uniform mean. (They could coincide by accident; nothing rules that out pointwise.)

`L_j(h|.)` is a step function, constant on the finitely many mark-and-flag level cells, so

    discontinuity locus  SUBSET  U_i U_{a in A} {k_i = a}   UNION   U_i {k_{i-1} = k_i}

with `A` = the finite set of cell edges. **Two consequences, both against N11's wording:**
 (a) it MISSES the cell-edge hyperplanes — non-collapsed vectors, and these are where the
     implemented instance's jumps actually live;
 (b) a collapse face is a discontinuity only if the collapsing plan is the SOLE on-path generator of
     some positive-probability history. The implemented Hold-collapse face is not (see 4a).

## 3. Perturbation family (brief item 3) — does NOT reconcile the limits

Under the row's single uniform-over-plans family with weight `t_n = J/n`:
at fixed `n` the denominator is `>= (t_n/J) Lam_u > 0`, so the whole price system is **continuous in
k**; the discontinuity is created only by `t_n -> 0`. The two limits (`n -> inf` and `k -> k0`) do
not commute. So the family choice cannot fix it — the order of limits is the problem.

Note: `numerical_v4/pooled.py` `OFF_PATH_EPS = 1e-14` is exactly a fixed-`t` constrained game, i.e.
N11's own "standard repair", already in the shipped code. Its `TypeReference` docstring records the
phenomenon in the implementers' own words: *"the outer map T(k) jumps by ~0.1 in the cutoff whenever
a type's mass crosses zero -- which is exactly where the equilibrium sits."*
And the reference value it attaches, `Ev[t] = E[v | n(s) = t]` over the whole signal line, **is**
Step 9(b)'s plan-uniform posterior restricted to that type. So the code implements the proof's
limit rule, with the switch relocated by ~1e-9 (the breakpoint dedup) rather than removed.

## 4. The implemented case (brief item 4) — numbers

Menu: J=3, Exit/Hold/one Voice family; `Gamma` = buy-indicator, so **Exit and Hold pool perfectly**
at mark-path type 0 (`menu.py` docstring: "Exit and Hold pool perfectly in order flow").
Baseline (reproduced: `solve_policy` at frozen tau = 0.090764058616):
`k* = (1.2405757283, 1.5310222869)`, `|k-T(k)| = 2.596e-11`, payoff residual 0 — matches
`numerical_v4/smoke_output.txt` SMOKE 1. **Hold region width 0.290447 — collapse is NOT live at the
baseline.** Off-path types at k*: t=10, t=11 (zero mass, floored). Marginal on-path type: t=9.

### 4a. Hold-collapse face is CLEAN (probe 2A)
Type-0 mass is `Phi_s([s_lo, k2))` — a function of `k2` alone. Varying `k1` in
{0.5, 1.0, 1.2406, 1.40, 1.52, k2} at fixed `k2 = k2*` (last value = Hold fully collapsed):

    max |EP - EP(k1=0.5)| over all dates and types  <=  4.441e-16
    U_V(1.6) = 0.040113093715 at every k1 (bit-identical)
    T(k)     = (1.25054030, 1.41006135) at every k1 (bit-identical)

**The whole pooled price system, hence `T`, depends on `k` only through `k2`.** So the collapse face
`{k1 = k2}` — the collapse P1 Step 16 says the frozen manuscript's baseline takes — carries no
discontinuity at all on this menu.

### 4b. But the jumps ARE live, at non-collapsed vectors (probe 3, frozen tau, k1 = 1.2405757283)
Sweeping `k2` across the `n(s)` cell edges. Left limits converge by delta = 1e-7; value AT the edge:

| edge `S` (n(s) cell top) | `T_2(S-)`   | `T_2(S)`    | jump in `T_2` | `T_1` jump |
|---|---|---|---|---|
| 1.583333333333 | 1.549728951 | 1.543395170 | **-6.334e-03** | 4e-09 |
| 1.659062162746 | 1.569659263 | 1.558798550 | **-1.086e-02** | 3e-09 |
| 1.749268649265 | 1.603724853 | 1.575443391 | **-2.828e-02** | 3e-09 |

All three are non-collapsed vectors (Exit, Hold, Voice all carry positive mass). `T_1` is continuous
throughout, consistent with 4a. Price at a diagnostic date-7 history carrying an `X=2` mark
(feasible only for the alive types {9,10,11}), tau = 0.05 run: `P_7(h)` two-sided limits
**1.543850 vs 1.400791**, a jump of 0.143 in the price — a genuine two-sided-limit gap, not a
numerical artifact (left limit converged over delta = 1e-4..1e-8; right value constant for all
delta <= 1e-10 including 0 and > 0).

### 4c. A6 IS satisfiable at the implemented calibration, on a chamber-interior Theta (probe 4)
`k2* = 1.5310222869` lies in the open chamber `(1.517932397378, 1.583333333333)` between consecutive
**k-independent** cell edges (the `n(s)` and tau-crossing pullbacks) — 0.0131 above the lower edge,
0.0523 below the upper. The breakpoint list also carries `k2` itself, but that one moves with the
cutoff and probe 4's grid shows `T` smooth through it. On that chamber `T` is
continuous: over a 29-point grid, max adjacent `|dT_2| = 1.185e-03` at spacing 3.17e-03 (slope
~0.35), and at the lower edge the two-sided values agree to 3.5e-09. `T_2` is monotone increasing
there, and
    `T_2([1.525272, 1.550633]) = [1.529026, 1.537885]`,  `T_1(...) = [1.231449, 1.243303]`
so the compact ordered box `Theta+ = [1.23, 1.245] x [1.5253, 1.5506]` satisfies
`T(Theta+) SUBSET Theta+` with `T` continuous on it. **Brouwer runs verbatim on `Theta+`, and the
baseline equilibrium is inside it.**

### 4d. BUT the chamber rescue is calibration-dependent — and it fails on the card's own grid
At `kappa = 0.15, tau = 0.05, T = 5` (one of ticket 34's four sweep-UNRESOLVED nodes), probe 5 sweeps
`k2` over [1.30, 2.10] with the edges bracketed at +-1e-7. `T_2` jumps at the edges by up to
**-0.16** (1.749268649: 1.675112972 -> 1.510436155, i.e. -0.1647), and at 1.583333333 the sign change of
`T_2(k2) - k2` happens **across the edge** (gap +1.0e-07 just below, -6.70e-02 at it): that diagonal
crossing is destroyed by the jump. A second fixed point sits **exactly on** the edge
`k2 = 1.659062163`, where `T_2` is locally constant (pinned at a jump point of `U_H - U_V` in `s`).
So the implementation docstring's "which is exactly where the equilibrium sits" is literally
realised at this node, and no chamber-interior Theta contains that fixed point.

### 4e. A confound to state plainly: two mechanisms share one locus in this menu
`n(s) = clip(ceil(n_scale*(H+1)*(1-g(x))), 1, H+1)` is integer-valued, so `B_VOICE(s,d)` — and hence
`U_VOICE(.;k)` — **jumps in `s`** at exactly the same cell edges. That is Step 15(i) / WHERE IT
FAILS 4, not N11. Measured at `k = (1.020221781, 1.659062163)`, kappa = 0.15:
`U_H - U_V` = -1.765771e-03 just below the edge (n=8) and +1.278166e-03 just above (n=7) — it
**jumps through zero, never crossing it**; `equilibrium_residual` reports cutoff scale 4.751e-10 and
**payoff scale 1.766e-03**, and the reported "local gap slope" 152.16 is just that jump divided by
2e-05. The solver from its own seed lands at `k=(1.007467669,1.561305096)`, payoff 1.488e-03; from
`k_init=(1.02,1.71)` (a genuine crossing, n=7 both sides) it lands at `k=(1.0260443221,1.7104049079)`,
cutoff 2.878e-11, payoff **3.055e-04**. Those two numbers bracket the card's ticket-34 record
("best payoff-scale residual 3.1e-4 - 1.5e-3, best cutoff-scale residual 1e-14 - 1e-11") exactly.
**So ticket 34's four unresolved nodes look like the `s`-direction jump, not N11's `k`-direction
one.** Attribution of my `T_2` numbers to N11's mechanism is nonetheless sound on these grounds:
mechanism (alpha) can move `T` in `k` only where a smooth level shift slides a branch's sign across a
fixed `s`-jump, which happens at generic `k`, *not* pinned to the cell-edge hyperplanes; every jump I
measured is bracketed at an edge to +-1e-8 **and** co-located with a directly measured `U_V(s0;k)`
level jump at a fixed `s0` away from any edge (4b), which is (beta) and only (beta).

### 4f. Brief item 2: the tie-break does NOT absorb it — and h.3 itself fails at kappa = 0.15
The largest-weakly-increasing-selection tie-break resolves `s`-direction ties **at fixed `k`**; a
`k`-discontinuity in the `U` levels passes straight through any selection that is pointwise in `k`.
Nor does the crossing-point structure absorb it: `U_HOLD` does not move when `U_VOICE` jumps (4b), so
the adjacent-pair difference jumps by the full amount.
Stronger, at kappa = 0.15 the tie-break has nothing to select from. Pointwise argmax over all three
plans across the cell edge 1.659062163, at **both** of that node's fixed points:

    k = (1.020221781, 1.659062163)   s=edge-1e-06 (n=8): U_E .0331035 U_H .0366608 U_V .0384266 -> VOICE
                                     s=edge+1e-06 (n=7): U_E .0331035 U_H .0366608 U_V .0353827 -> HOLD
    k = (1.0260443221, 1.7104049079) s=edge-1e-06 (n=8): U_E .0332206 U_H .0367977 U_V .0378606 -> VOICE
                                     s=edge+1e-06 (n=7): U_E .0332206 U_H .0367977 U_V .0347621 -> HOLD

Singleton argmax on both sides, Voice below and Hold above: the preferred plan **decreases** in `s`,
so `S(k)` — h.3's set of weakly increasing selections — is **empty**, Step 13's construction has no
input, and no cutoff vector represents the best response. That is h.3/A3 (WHERE IT FAILS 5, reached
by a route the file does not list: an `s`-step in `U_VOICE`, not a non-monotone cost), **upstream of
A6 and a different hypothesis from the one N11 indicts.** Caveat retained: the card records that
"the A3 and A6 proxies pass at every achieving seed" at these nodes; I did not open the proxy
definitions to reconcile that with these numbers.

---

## 5. What I could NOT overcome (verbatim, as the counter-argument to my own brief)

> A6 as the card states it is quantified over *all* best-response cutoffs: "All best-response
> cutoffs lie in a common compact ordered polytope Theta; T is continuous and maps Theta into
> itself." Steps 13-14 construct Theta from the *bracket* `[s_lo, s_hi]` — the union over adjacent
> pairs of every indifference signal, uniform in the conjecture. Any Theta built that way contains
> the cell-edge hyperplanes, and on it the constructed price system's `T` is provably discontinuous:
> I measured jumps of 6.3e-03, 1.09e-02 and 2.83e-02 in `T_2` on the paper's own menu and
> calibration. The chamber-interior `Theta+` that rescues A6 is not something Steps 13-14 supply —
> exhibiting it requires already knowing where `T` maps a small box into itself, i.e. already
> knowing roughly where the fixed point is. So A6 is satisfiable here, but only under a reading of
> Theta that the proof does not construct and that cannot be checked without effectively solving the
> model first. That is a real gap between the hypothesis as written and the object built.

Second, smaller residue: Step 9(c) already concedes the reference-belief convention "can change
`U_j(s;k)` on a `Phi_s`-null set of signals, hence can move `T_i(k)`". So "the jump is confined to
off-path `(j,s)` pairs" holds only up to null sets, and `T_i` is an infimum over a pointwise
condition. Not new damage (NOT CLAIMED 13 owns it), but it blocks a clean confinement lemma.

## 6. Card recommendation — a SHARPER §9 line, not N11's line as drafted

Proposed replacement for pass-2 change 6 (numbered item 4 under §9's "added at this regeneration"):

> 4. **Whether A6's continuity of `T` is satisfiable on a `Theta` the proof constructs — OPEN, and
>    the locus is not the one the re-derivation named.** Step 9(b) makes the pooled price at a
>    history `h` Bayes-under-`k` where `Lam_k(h) > 0` and the `k`-independent plan-uniform posterior
>    where `Lam_k(h) = 0`. `Lam_k(h)` is continuous in `k` and `L_j(h|.)` is a step function on the
>    finitely many mark-and-flag cells, so the price can be discontinuous only on
>    `bd{k : Lam_k(h) > 0}`, and generically is — a set contained in the finitely many
>    **cell-edge hyperplanes** `{k_i = a}`
>    together with the collapse faces `{k_{i-1} = k_i}`, and **not** confined to the collapsed
>    vectors §3 admits. The jump reaches `T`: `U_j`'s pooled-execution bracket integrates those
>    prices against the *deviator's own* noise law (`proofs/P1_proof.md` Step 11), so their weight
>    does not vanish with the collapsing plan's population mass. On the pinned pro-rata menu the
>    collapse face the baseline would visit is clean — Exit and Hold share mark-path type 0, so the
>    whole pooled price system moves with the Voice cutoff alone — but `T_2` jumps by 6.3e-03 to
>    2.8e-02 across the `n(s)` cell edges at the baseline calibration, and by up to 0.16 at
>    kappa = 0.15, where a fixed point sits **on** an edge. A compact `Theta` interior to a single
>    chamber restores A6 at the baseline and contains `k*`; Steps 13-14 build `Theta` from the
>    bracket rather than from a chamber, and the chamber reading cannot be checked without
>    effectively solving the model. Step 18's Kakutani route already removes h.6's continuity half.
>    The P1 **label is untouched**: A6 is a listed hypothesis, so this is a satisfiability question,
>    not a derivability one.

## 7. UNCHECKED

- General-menu satisfiability of a chamber-interior Theta. Verified numerically on one menu, one
  calibration, a 29-point grid; not proved, and shown in 4d to FAIL at kappa = 0.15.
- Whether A3's monotone-preferred-plan clause survives at the kappa = 0.15 node. The 3.055e-04
  payoff residual at a genuine crossing is a profitable deviation somewhere else on the grid, which
  is what a downward `s`-step in `U_VOICE` produces; the card records that "the A3 and A6 proxies
  pass at every achieving seed", and I did not open the proxy definitions to reconcile this.
- The flag-coordinate contribution to the locus. In the implementation the flag enters through
  *aliveness* (`_alive_weights` drops atoms with `D=1, f<=d`), not through mark feasibility, so the
  tau-crossing breakpoints are additional candidate edges; I swept the n(s) edges only.
- Whether a destroyed crossing can leave a calibration with **no** fixed point at all. At kappa=0.15
  a crossing IS destroyed (edge 1.583333333, gap +1.0e-07 below -> -6.70e-02 at it) yet two fixed
  points survive — one pinned on the edge 1.659062163, one interior at 1.7104049079 — so nonexistence
  is not demonstrated anywhere. Not swept over (kappa, tau, T).
