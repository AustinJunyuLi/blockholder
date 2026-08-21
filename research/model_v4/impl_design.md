# `numerical_v4/` — implementation design

**Status: DESIGN, awaiting orchestrator review. No code written.**
Ticket 25 (T2e). Written against `MODEL_CARD.md` (stamp 2026-08-20, commit `0c9185b`) and the
`NUMERICAL CHECK REQUEST` blocks of `threads/thread1_turn1_answer.md` (D1, P1, L1, L3, L4, T1) and
`threads/thread1_turn2_answer.md` (D1, L1, L2 — turn-2 supersedes turn-1 where they differ).
House style is the existing `numerical/` package: pure functions, full type hints, dataclass
params, `NamedTuple` returns, tolerance constants imported from `numerical/params.py`.

---

## 0. What the checks actually demand — and which ones can fail

Before designing anything, sort the six requests by whether a bug can survive them.

| ID | Object | Two independent code paths? | Verdict |
|---|---|---|---|
| D1 | `f ≤ H ⟺ B(s,H−T) ≥ τ` | yes — date-by-date crossing scan vs one evaluation at `H−T` | **substantive** |
| D1 | `P^F − P_{c⁻} = R + J`; cell overlap; exhaustion | no — telescoping and a partition of a Python `if` | **wiring check** |
| L1 | `Δ^act = ΩM_F + (1−Ω)M_P` | no — same enumeration on both sides; the residual is machine noise by construction | **wiring check** |
| L2 | flagged objects invariant in κ | yes — the flagged path must never touch the κ-dependent array | **substantive** |
| L3 | enumerated `∂_κE[h]` vs `A'_κ C_h(π̄)` | yes — enumeration vs closed-form three-atom law | **substantive** |
| L4 | signs of `ΔΩ, Δπ̄, ΔS_P` under τ-tightening | yes — sign predictions that can come out wrong | **substantive** |
| T1 | `S(τ′)/S(τ) = W_τC_τ ≤ 1`; window iff | partly — the product identity is wiring, the `≤ 1` is substantive | **mixed** |
| P1 | multistart existence, residual < 1e-10 | yes | **substantive** |

**DECISION.** The check scripts report this classification in their JSON (`"kind": "substantive"` /
`"wiring"`). A wiring check that passes is not evidence for the theorem and must not be quoted as
such when a label moves. This is stated up front because two of the eight requests are identities
that hold by construction, and a design that pretends otherwise buys false confidence.

**DECISION.** To keep the substantive ones substantive: **the enumeration never imposes A(τ)**.
`E[h]` is computed by exact summation over pooled histories; the three-atom representation is built
separately in the chord module. L3's residual is the gap between them. Same rule for D1: the
`H−T` equivalence is checked against a genuine crossing scan, never against itself.

---

## 1. Discretisation of `s`

Every `s`-integral is a probability of an interval or an expectation of something affine in `s`
over an interval (`E[v|s] = μ_v + β(s−μ_v)` is affine; `Y` is affine in `v`). The integrands are
**piecewise** — they jump at plan cutoffs `k`, at `Γ` bin edges pulled back through each date's
stake increment, and at `τ`-crossing dates. Gauss–Hermite and a uniform mesh both converge at no
useful rate across a jump, and a uniform mesh additionally lands nodes on breakpoints by accident.
Closed form on intervals is exact here, because the pieces are `Φ`-differences and
truncated-normal means — the machinery `numerical/model.py::compute_conditional_means` already has.

**DECISION — breakpoint-first, analytic inside.**
1. Build the sorted breakpoint set `S_break` = plan cutoffs `k` ∪ `{s : ΔB_j(s,d) = Γ bin edge}`
   for every `j, d` ∪ `{s : B_j(s,d) = τ}` for every `j, d`. With `H = 10`, binary `Γ` and one
   Voice plan this is ≤ 11 + 11 + |k| ≈ 25 points.
2. On each open interval the plan index, the whole mark path, `D`, `c`, `f` are **constant**, and
   `b*`, `B^F`, `Q^F` are smooth.
3. Probabilities: `Φ(b)−Φ(a)`, exact. Conditional means of `v`: the truncated-normal formula,
   exact.
4. Anything not affine in `s` inside an interval (only the flagged price `P^F(s)`, which is a
   fixed point): **fixed-order Gauss–Legendre, 20 nodes per interval**, nodes strictly interior.

No global grid. The word "s-grid" appears in this design only for the flagged-price evaluation of
§4, where it is a per-interval Gauss–Legendre node set, never a uniform mesh.

**Open question (minor).** GL-20 per interval on `P^F(s)` is a guess at sufficiency. The build
should report the GL-20 vs GL-40 difference once; if it exceeds 1e-13 the order goes up. Cheap.

---

## 2. The plan menu — simplest card-conformant choice

**DECISION — `J = 3`: Exit, Hold, one Voice family.**

| `j` | `a_j` | `B_j(s,d)` | mark path `q_{j·}(s)` |
|---|---|---|---|
| 1 Exit | 0 | `b_0 → 0` in one day-0 block, then flat | all zeros (see below) |
| 2 Hold | 0 | flat at `b_0` | all zeros |
| 3 Voice | 1 | `b_0 + (b*(s)−b_0)·min(1,(d+1)/n(s))` | `n(s)` ones, then zeros |

`b*(s)` **strictly increasing** on the Voice interval (card §4.2 row); `n(s)` the number of
accumulation days, weakly decreasing in `s` (a stronger signal accumulates faster). `∂_d B ≥ 0`
and `∂_s B ≥ 0` hold. `b_0 < τ` is maintained (card §4.1, turn-2 audit D1-O1).

**DECISION — `Γ` is the binary buy-indicator `Γ(Δ) = 1{Δ ≥ γ̄} ∈ {0,1}` (M = 2 marks).**
Rationale: the premium object is `Δ^act = Δ_m E[h]` with `h = π·p`, and `π = Pr(a=1|·)`. The
coarsest `Γ` that carries `π` is "did the blockholder buy a block today". Everything coarser
carries nothing; everything finer multiplies the enumeration by `(M+2)/(M+1)` per mark (§4).

Note the deliberate flattening: **Exit and Hold pool perfectly in order flow.** They share the
all-zero mark path, so `v̂` on a pooled history is coarser than draft_v2's. `v̂` still matters
because it enters `P` and hence `p`, so this is a real modelling choice, not a free one.

**OPEN QUESTION 1 (for review).** Is collapsing Exit and Hold in order flow acceptable? The fix is
`Γ ∈ {−1,0,+1}` (M = 3), which costs **12×** the enumeration (`5^11 = 48,828,125` vs
`4^11 = 4,194,304`) — affordable but it turns the P1 multistart grid from an overnight run into a
week. Recommend M = 2 for the first build, M = 3 as a gated stress mode.

### A7 injectivity, and where the grid touches it

The card's A7 strong form wants `(j,s) ↦ (B_j^F, Q_j^F, a_j)` injective on the flagged set.

**Finding worth handing to ticket 24.** On this menu injectivity does *not* require `B^F` to be
monotone in `s` — and it is not. `c(s)` is weakly decreasing in `s` while `b*(s)` rises, so
`B^F = B(s, c(s)+T)` can jump down across a `c`-plateau boundary. But

```
B^F + Q^F = b*(s),   strictly increasing  ⟹  s recoverable  ⟹  (B^F,Q^F) injective.
```

So on a single-Voice-plan menu, **injective A7 reduces to strict monotonicity of the terminal
target `b*(·)` alone.** That is strictly weaker than the "`B^F` strictly increasing" reading the
§4.2 row invites. **Coordination point: ticket 24 owns the weakest menu condition A7′; this
design does not resolve it, and passes it the observation that `sum-monotone` may be the right
weakening, together with the note that cross-plan collisions only appear once a second Voice plan
is added.** The implementation assumes the strong injective form and exposes a probe so that
whatever A7′ lands can be tested on the same menu without touching the pricing layer:

```python
def a7_certificate(menu: Menu, params: ParamsV4) -> A7Certificate:
    """min |db*/ds| on the flagged set, count of flat sub-intervals,
    count of (B^F,Q^F) collisions at 1e-12, cross-plan collision count."""
```

**Named risk (see §9.1).** A discrete `s`-representation makes injectivity *vacuously true* —
distinct nodes always have distinct `b*` — and would hide a genuine continuum failure. Two guards:
(i) the flagged posterior is obtained by **inverting `b* = B^F + Q^F` with `brentq`**, never by a
grid-index lookup; (ii) `a7_certificate` fails the run if `min_s b*'(s)` on the flagged interval
drops below `1e-8`.

---

## 3. Calendar and the choice of `H`

`d = 0,…,H`; `T ∈ {1,…,H}`; the flag lands iff `B_j(s,H−T) ≥ τ`.

**DECISION — `H = 10`.** It is the minimum consistent with the requested `T ∈ {5,10}`.

Enumeration cost is `(M+2)^{H+1}` (§4). At `M = 2`:

| `H` | dates | histories | one evaluation | P1 grid (50 nodes × 30 seeds) |
|---|---|---|---|---|
| 6 | 7 | 16,384 | ~2 ms | minutes |
| **10** | **11** | **4,194,304** | **~0.6 s** | **~5 h (overnight)** |
| 12 | 13 | 67,108,864 | ~10 s | ~4 days |
| 15 | 16 | 4,294,967,296 | — | out of reach |

**Cost of the decision, stated plainly.** At `H = 10`, `T = 10` forces `c = 0` on every flagged
history — the blockholder must be over `τ` on day zero. That is exactly the corner the card's
`P_{−1}^P := E[Y]` convention was added for (turn-2 audit D1-R3). So the `T = 10` column of every
grid is a boundary case, not an interior window comparison.

**OPEN QUESTION 2 (for review).** Raise to `H = 12` so both `T = 5` and `T = 10` are interior?
Cost: 16× the enumeration; a full evaluation goes from 0.6 s to ~10 s and the P1 multistart grid
from overnight to ~4 days. Recommend: build at `H = 10`, and re-run D1/L1/L4/T1 (not P1) at
`H = 12` once the checks pass, as a robustness column.

---

## 4. Pooled-history enumeration — the count

A pooled public history is the order-flow path `X_{0:H}`, `X_d = q_{jd}(s) + z_d`, with
`z_d ∈ {−z̄,0,+z̄}` at probabilities `(κ/2, 1−κ, κ/2)`.

**Types collapse.** Because `Γ` is a coarse step map, the informed path depends on `(j,s)` only
through the **mark path** `θ = (q_0,…,q_H)`. The distinct `θ` are exactly the `s`-intervals of §1:

- Voice: one `θ` per accumulation length `n ∈ {1,…,H+1}` → **11 paths**
- Exit and Hold: the all-zero path → **1 path**
- **`N_θ = 12`** at `H = 10, M = 2, J = 3`

Each `θ` carries its interval's prior mass `w_θ(k)` and its truncated-normal `E[v|θ]`.

**History count.** With `z̄` set to one mark unit, `supp X = {−1,0,1,2}`, so

```
n_hist  ≤  |supp X|^(H+1)  =  4^11  =  4,194,304
```

(some paths are infeasible — `X_d = −1` on a date where every `θ` has mark 1 has zero mass under
every `θ`; the true feasible count is measured by the probe of §11, not predicted here).

**Combinatorics per `(H, marks)`, and where it explodes.**

```
n_hist = (M + 2)^(H+1)          N_θ = 1 + (H+1)·(M−1)
```

| `(H, M)` | `n_hist` | `N_θ` | `n_hist × N_θ` | verdict |
|---|---|---|---|---|
| (10, 2) | 4.19e6 | 12 | 5.0e7 | **chosen** |
| (12, 2) | 6.71e7 | 14 | 9.4e8 | robustness re-run only |
| (10, 3) | 4.88e7 | 23 | 1.1e9 | gated stress mode |
| (15, 2) | 4.29e9 | 17 | 7.3e10 | out |

**The cliff is at ~1e8 histories**: past that one evaluation exceeds a minute and the P1 multistart
grid exceeds a week. Every extra business day multiplies by `M+2`; every extra mark multiplies by
roughly `((M+3)/(M+2))^(H+1)`.

**DECISION — factor the likelihood, do not recurse.** Because `q_{θd}` is deterministic and noise
is i.i.d. across dates, the likelihood is a pure product over dates:

```
L[h, θ]  =  ∏_d Pr(z = X_d − q_{θd})  =  (1−κ)^{n0(h,θ)} · (κ/2)^{H+1−n0(h,θ)} · feasible(h,θ)
```

so **store only the integer exponent `n0` (int8) and a feasibility bool**, both independent of κ:
`4.19e6 × 12` int8 = 50 MB, computed once per menu. Regenerating `L` at a new κ is one
exponentiation. Three consequences:

1. The frozen-policy κ-sweep costs one exponentiation per κ — no re-enumeration (§6).
2. The k-dependence enters only through the prior vector `w(k)` (length `N_θ`), so an outer-solver
   iteration is one `(n_hist × N_θ)` weighted row-normalisation — ~0.15 s in numpy (§7).
3. `L` is a product, not a recursion, so history indices decode independently: **chunk over
   histories in blocks of 1e6** (float64 working set 96 MB) and the memory ceiling disappears.

**DECISION — no pruning by default.** At mid-κ every one of the 4.19M paths carries real mass
(`0.5^11 = 4.9e-4` for the modal path, `0.25^11 = 2.4e-7` for the least likely), so a probability
floor would discard mass the 1e-12 residual targets cannot absorb. Pruning is available for the
`M = 3` stress mode only, and when on, the discarded mass is written to the JSON so every residual
can be read against it.

---

## 5. Inner pricing fixed points

Per pooled history: `P = E[Y | H^P]` with

```
E[Y|·] = (1 − p(P))·(v̂ + π·Δ_V)  +  p(P)·(P + m_0 + π·Δ_m)
p(P)   = 1 − Φ((P + K + m_0 + π·Δ_m − S̄)/σ_ξ)
```

`P` appears on both sides with coefficient `p(P)`. The map's slope is
`p + p'(·)·(P + m_0 + πΔ_m − v̂ − πΔ_V)`, **which is not below 1 in general** — draft_v2 got
contraction free from the discount factor `δ = 0.95` multiplying the whole bracket, and `δ` does
not appear in the v4 card's §4.

**DECISION.** Do not iterate. Solve `g(P) = P − E[Y|·,P] = 0` by **vectorised bisection on a
certified bracket** (A2 bounds payoffs, so the bracket is `[min Y, max Y]`), 60 iterations →
~1e-18 relative, then one Newton polish. Per history a sign-change assert; histories that fail it
go to a `multiple_root_nodes` list in the JSON — that list is direct numerical evidence about A5,
which the whole stack leans on.

**OPEN QUESTION 3 (for review — for the theorist).** Does the card intend a discount factor on the
pricing fixed point? draft_v2 had `δ = 0.95`; the v4 card's §4.3 writes `P(I) = E[Y|I]` with no
discount, which removes the guaranteed contraction that made A5's uniqueness cheap. Bisection
handles it either way, but the answer changes whether A5 is an assumption or a consequence.

---

## 6. Flagged side, and the frozen-policy / equilibrium split

### 6.1 Flagged prices

Under injective A7 the flagged posterior conditions on `(B^F, Q^F, a=1)` **and nothing else** —
in particular not on the pooled history. So:

```
s = (b*)^{-1}(B^F + Q^F)      # brentq, per flagged node
v̂ = μ_v + β(s − μ_v)          # exact, π = 1
P^F = fixed point of §5 at (v̂, π=1)     # bisection
p, M_F                                    # from P^F
```

No enumeration, no κ. That is the whole content of L2 and it makes L2's check **cheap and
genuinely falsifying**: if any κ leaks into this path, the range over the 19-point κ grid is
nonzero. `M_F = Δ_m·E[h | D=1]` averages over the flagged `s`-intervals with the §1 GL nodes.

### 6.2 The two modes

L2, L4 and T1 all say "at fixed policies". L2's check freezes one equilibrium policy and moves κ.
This is the single most important architectural decision in the design and it is one line:

**DECISION — `evaluate()` is pure in the policy; the solver is never called from inside it.**

```python
class Policy(NamedTuple):        # frozen: cutoffs + menu + execution paths
    k: tuple[float, ...]
    menu: Menu

def evaluate(policy: Policy, params: ParamsV4) -> Outcomes:  ...   # no solver call
def solve_policy(params: ParamsV4, seed: int = 0) -> tuple[Policy, float]: ...

def frozen_policy_sweep(policy, params, kappas): # policy fixed, params.kappa moves
    return [evaluate(policy, params.replace(kappa=k)) for k in kappas]

def equilibrium_sweep(params, kappas):           # policy re-solved at each kappa
    return [evaluate(*solve_policy(params.replace(kappa=k))[:1],
                     params.replace(kappa=k)) for k in kappas]
```

Both modes share `evaluate` **verbatim** — that is the entire mechanism, and it is why the two
sweeps are comparable at all. A module-level guard asserts `policy.py` does not import `solver`,
so the purity cannot rot. The existing `numerical/` package already has this shape
(`compute_equilibrium_prices(k1,k0,kD,params)` is policy-parameterised; `compute_series_over_kappa`
is the equilibrium mode); v4 only needs to name it and enforce it.

**DECISION — freeze the τ grid.** The requests set `τ` at percentiles "of equilibrium Voice stake
paths", which depends on the equilibrium, which depends on `τ`. Circular. The τ values are
computed **once** from the baseline equilibrium's `b*(s)` distribution, frozen, and reused at every
node; the frozen values are written into the JSON provenance.

---

## 7. Outer solver — reuse map

The outer map is `k = T(k;ϑ)` on the ordered polytope `Θ`, `J−1 = 2` cutoffs here.
`numerical/solver.py`'s architecture transfers directly: grid-scan for sign changes, `brentq` on
the bracket **nearest the current iterate** (that is the branch-continuity device and it works),
damped update `α = 0.75`, warm start from the neighbouring grid node, multi-start fallback.

| Source | Disposition | Note |
|---|---|---|
| `numerical/params.py` tolerance constants | **verbatim import** | plus new `TOL_IDENTITY = 1e-12`, `TOL_INVARIANCE = 1e-10` |
| `ModelParams.replace` / `.baseline()` idiom | **verbatim pattern** | new dataclass `ParamsV4` — the field set barely overlaps, so a subclass would be a costume |
| `model.py::solve_price_fixed_point` | **adapted** | same scalar root, new `Y`, bisection not iteration (§5) |
| `model.py::bid_probability` | **adapted** | `p = 1 − Φ((P+K+m_0+πΔ_m−S̄)/σ_ξ)`, same shape |
| `model.py::compute_conditional_means` | **adapted** | truncated-normal interval means, new interval set |
| `model.py::compute_posteriors` | **new** | v3's one-shot signed order flow ≠ v4's multi-date path filter. Do not force a reuse |
| `solver.py::bracket_root` | **verbatim** | the nearest-bracket-to-target rule is the whole trick |
| `solver.py::solve_equilibrium` loop | **adapted** | 3 cutoffs → `J−1`; same damping, same convergence test |
| `solver.py::solve_valid` | **adapted** | multi-start list → seeded generator (P1 wants 30 seeds) |
| `solver.py::equilibrium_residual` | **adapted** | 3 conditions → `J−1` adjacent-plan indifferences, same collapsed-region positive-part handling |
| `numerical/accel.py` (Numba) | **skipped** | 1,062 lines duplicating the reference implementation. If speed bites, vectorise numpy first |
| `export_data.py::_write_csv`, `_fmt` | **verbatim copy** (12 lines) if CSVs are needed; JSON otherwise |
| `pyfig/` | **out of scope** for this ticket |

**Derivatives in κ.** `S_P = |∂_κ M_P|`, and `M_P` runs through a fixed point, so an analytic
derivative needs the implicit function theorem on 4.19M roots. Not worth it.
**DECISION — 4th-order Richardson-extrapolated central differences, `h = 1e-3`**: truncation
`O(h⁴) ≈ 1e-12`, roundoff `≈ eps/h ≈ 2e-13`, comfortably inside the 1e-10 targets with two orders
to spare. Analytic `∂_κ` is used only for the `A(τ)` weights, where it is a one-liner and L3 needs
the closed form anyway.

**OPEN QUESTION 4 (for review).** P1 asks for `|k − T(k)|_∞ < 1e-10` **and** "no profitable
adjacent-plan deviation above 1e-9". These are not commensurate — one is on the `s`-scale, the
other on the payoff scale, and which binds depends on the local slope of the payoff gap. Both are
far tighter than the existing `TOL_RESIDUAL = 5e-3`. Recommend reporting both plus the local
slope, and letting the theorist pick the binding one.

---

## 8. L3's chord — a deliberate split

L3 wants `π̄` down to `1e-4` with a 1e-10 residual. Driving the full model to a pooled engagement
share of `1e-4` means an extreme τ percentile, near-empty cells, and an object of size
`C_h ≈ ¼h''(0)·1e-8` measured against 1e-10 — two significant digits.

**DECISION — split the check.** L3 is a statement about the chord *functional*, not about the
enumeration. So:

- `π̄ ≥ 1e-2`: full-model route. Enumerated `∂_κE[h]` vs `A'_κ C_h(π̄)`. This is the substantive
  comparison and the enumeration resolves it.
- `π̄ < 1e-2`: standalone chord module. `h` is an explicit function, `C_h = h(0) − 2h(π̄/2) + h(π̄)`
  evaluated directly, Taylor claim `|C_h|/π̄²` compared across the two smallest `π̄`. Float64
  headroom here is ~8 digits (cancellation error `≈ eps·max|h| ≈ 2e-16` against a target of
  `1e-8`), so the quadratic claim is cleanly testable.

**OPEN QUESTION 5 (for review — for the theorist).** The requested absolute tolerance `1e-10` at
`π̄ = 1e-4` is only ~2 significant digits of the object under test. Recommend either a **relative**
tolerance (`residual/|C_h| < 1e-6`) or raising the smallest `π̄` to `1e-3`. The split above makes
the check pass either way, but the tolerance as written does not mean what it looks like it means.

---

## 9. Named risks — where discretisation could betray a theorem

**9.1 Injective A7 vs discrete `s` (largest).** A grid makes injectivity vacuously true; the
continuum failure mode (a flat interval of `b*`) is invisible to it, and on a flat interval the
true flagged posterior is an interval average the grid silently replaces by a point mass.
*Guards:* invert `b* = B^F + Q^F` with `brentq`, never a grid lookup; `a7_certificate` fails the
run below `min_s b*'(s) < 1e-8`; flat-interval and collision counts in every JSON.
*Coordination:* ticket 24 (A7′) owns the resolution.

**9.2 Chord smallness vs resolution (L3).** Catastrophic cancellation in `h(0) − 2h(π̄/2) + h(π̄)`,
plus the `∂_κ` step choice. *Guards:* the §8 split; Richardson differences; report the achieved
cancellation headroom beside the residual.

**9.3 Near-degenerate cells at extreme κ (L4, T1).** At `κ → 0` pooled order flow is fully
revealing and `π ∈ {0,1}`; at `κ → 1` the zero-noise branch vanishes and the pooling structure
changes discretely. A8 (`0 < Ω < 1`) can also fail if a τ percentile lands outside the Voice
support. Worst: T1's `C_τ = S_P(τ′)/S_P(τ)` divides two `O(π̄²)` quantities that can both approach
zero — a `0/0` that will report anything. *Guards:* κ never takes 0 or 1; assert cell mass ≥ 0.01
per D1's request and emit `degenerate_nodes` rather than crashing; **report `S_P` in levels beside
every ratio and mark any ratio computed on `S_P < 1e-12` as `"undefined"`.**

**9.4 `Γ` bin edges vs quadrature nodes.** A node on a `Γ` edge has an ambiguous mark path.
*Guard:* GL nodes strictly interior; a node within `1e-12` of a breakpoint is an assertion
failure, not a rounding decision.

**9.5 The `T = H` corner.** At `H = 10, T = 10` the flag requires `c = 0` — the boundary case the
`P_{−1}^P := E[Y]` convention was written for. *Guard:* JSON marks `T == H` nodes `"corner": true`;
Open question 2 offers the `H = 12` escape.

**9.6 A5 multiplicity.** §5's map is not a contraction. *Guard:* `multiple_root_nodes`.

**9.7 Wiring checks read as evidence.** *Guard:* the `"kind"` field of §0.

---

## 10. Check-script interface

Mirrors `quality_reports/fixes/d7_takeover_game_check.py` exactly: module docstring listing the
checks and the run command, seeded `RNG`, `OUT` beside the script, tolerance constants at the top,
`results = {"checks": [], "n_fail": 0}`, `record(name, ok, detail)` printing `[PASS]`/`[FAIL]`,
`main()` calling each check in order, `results["all_pass"]`, `json.dump(..., indent=2,
default=float)`, `sys.exit(0 if all_pass else 1)`.

v4 additions to the JSON, all of them things a reviewer needs and d7 did not have:

```json
{"provenance": {"model_card_stamp": "...", "commit": "...", "params_hash": "..."},
 "grid":       {"kappa": [...], "tau": [...], "T": [...], "H": 10, "M": 2, "tau_frozen_from": "baseline"},
 "counts":     {"n_hist": 4194304, "n_hist_feasible": 0, "n_theta": 12, "discarded_mass": 0.0},
 "checks":     [{"name": "...", "kind": "substantive|wiring", "pass": true, ...}],
 "degenerate_nodes": [], "multiple_root_nodes": [],
 "n_fail": 0, "all_pass": true}
```

**DECISION — one script per theorem ID**, because the ledger moves labels one ID at a time and each
request carries its own grid: `v4_d1_partition_check.py`, `v4_l1_decomposition_check.py`,
`v4_l2_invariance_check.py`, `v4_l3_chord_check.py`, `v4_l4_threshold_check.py`,
`v4_t1_attenuation_check.py`, `v4_p1_existence_check.py`.

**OPEN QUESTION 6 (for review).** Location: `quality_reports/fixes/` follows the D-series
precedent, but that directory is draft_v2's record. Recommend **`numerical_v4/checks/`** with JSON
beside each script, since v4 is a separate lane and the card is its own record.

---

## 11. Build plan

**Modules (8 files).**

```
numerical_v4/
  params.py    ParamsV4 dataclass, grids, ternary noise law, tolerance imports
  menu.py      plans, Γ, b*(s), s-breakpoints, legal clock (c, f, D, B^F, Q^F), a7_certificate
  pooled.py    history enumeration, the int8 exponent array, per-history P_d^P, R_d, R
  flagged.py   b* inversion, flagged posterior, P^F, p, J, M_F
  premium.py   π, h, Ω, ω_a, M_F, M_P, Δ^act, S, S_P, and the standalone chord C_h
  policy.py    Policy, evaluate() [pure in policy], frozen_policy_sweep, equilibrium_sweep
  solver.py    outer T(k), damped iteration, brentq bracketing, seeded multi-start
  checks/      seven d7-shaped scripts
```

**Order of construction.** Each step ends in something runnable.

1. `params.py` + `menu.py`. Self-check: the §1 breakpoint set, `a7_certificate` on the baseline
   menu, and the D1 equivalence `f ≤ H ⟺ B(s,H−T) ≥ τ` by two independent routes.
2. `flagged.py` + the flagged half of `premium.py`. **L2's check lands here** — cheap, exact, no
   enumeration, and it is one of the substantive ones. Getting a substantive check green before
   the expensive machinery exists is the point of this ordering.
3. `Ω` and `ω_a` in `premium.py`. These are deterministic in `(j,s)` — `D` does not depend on the
   noise at all — so L4's `ΔΩ ≥ 0` sign lands before any history is enumerated.
4. **Enumeration probe, the go/no-go gate.** `pooled.probe(H, M, menu)` reports the feasible
   history count, `N_θ`, the int8 array size, and one evaluation's wall time. **Gate: if feasible
   `n_hist × N_θ > 1e8`, stop and re-open Open questions 1 and 2 before writing pricing code.**
5. `pooled.py` in full: exponent array, chunked κ-exponentiation, vectorised bisection, `P_d^P`,
   `R_d`, `R`, `J`.
6. `premium.py` pooled half: `M_P`, `Δ^act`, `S_P`, Richardson `∂_κ`, the standalone chord.
7. `policy.py`. The purity guard goes in with the first line of `evaluate`.
8. `solver.py`, warm-started along the κ grid.
9. `checks/`, in ledger order D1 → L1 → L2 → L3 → L4 → T1 → P1.

**Smoke run** (the one runnable thing that fails if any of the logic is broken):

- **One equilibrium at baseline** — `κ = 0.5`, `τ` = median of the baseline Voice `b*(s)`,
  `T = 5`, `H = 10`. Prints `k`, the outer residual, `Ω`, `ω_a`, `M_F`, `M_P`, `Δ^act`, the
  identity residual `|P^F − P_{c⁻} − R − J|`, and `a7_certificate`.
- **One frozen-policy κ-sweep** — that policy held fixed, `κ ∈ {0.05,…,0.95}`. Prints
  `range_κ M_F` (must be `< 1e-10` — this is L2, and it is the assertion that fails loudest if κ
  has leaked into the flagged path) and the `S_P` profile.

Units follow the card's calibration card: `Ω, ω_a` in percent, `B^F` in percentage points of
shares, `M_F, M_P, Δ^act` in **premium percentage points** (never normalised indices), `R, J` in
basis points.

---

## 12. Open questions for the design review — consolidated

| # | Question | Recommendation |
|---|---|---|
| 1 | `Γ` with M = 2 collapses Exit and Hold in order flow. Acceptable? | M = 2 now; M = 3 as a gated stress mode at 12× cost |
| 2 | `H = 10` makes `T = 10` a `c = 0` corner. Raise to `H = 12`? | `H = 10` for the build; `H = 12` robustness re-run for D1/L1/L4/T1, not P1 |
| 3 | Is a discount factor intended on `P = E[Y|I]`? draft_v2 had `δ = 0.95`; the card has none, so A5's uniqueness is an assumption, not a consequence | ask the theorist; bisection works either way |
| 4 | P1's `1e-10` (cutoff scale) and `1e-9` (payoff scale) are not commensurate | report both plus the local slope; theorist picks the binding one |
| 5 | L3's absolute `1e-10` at `π̄ = 1e-4` is ~2 significant digits | relative tolerance `residual/\|C_h\| < 1e-6`, or smallest `π̄ = 1e-3` |
| 6 | Check scripts in `quality_reports/fixes/` or `numerical_v4/checks/`? | `numerical_v4/checks/` — v4 is its own lane |
| 7 | A7′ (ticket 24): does the weakest condition read "`B^F + Q^F` strictly monotone" rather than "`B^F` strictly monotone"? | hand ticket 24 the §2 finding; do not resolve here |

**Nothing is built until these are reviewed.** The gate at build step 4 is the second decision
point — if the feasible history count comes in above `1e8`, questions 1 and 2 re-open before any
pricing code is written.

---

## 13. Design review (Fable, orchestrator) — 2026-08-21

**Verdict: APPROVED with the rulings below. The build may proceed.**

The wiring/substantive classification, the breakpoint-first analytic treatment
of `s`, the factorised int8 likelihood, the `evaluate()` purity invariant, and
the step-4 go/no-go probe are all accepted as designed. Rulings on the seven
open questions:

1. **Γ marks:** M = 2 accepted for the build; M = 3 stays a gated stress mode.
   The Exit/Hold order-flow collapse is acceptable — no check in the request
   set needs the two separated in order flow, and their payoff difference
   survives through the stake paths.
2. **Calendar:** build at H = 10. The H = 12 robustness re-run is **mandatory
   for T1's window comparison** (and cheap enough for D1/L1/L4), optional
   nowhere else, excluded for P1. T = 10 nodes carry `"corner": true` as
   designed.
3. **Discount factor: none.** The card is the spec: `P(𝓘) = E[Y|𝓘]`, no δ.
   A5 stays an assumption; `multiple_root_nodes` is the evidence channel. If
   that list is nonempty at the baseline calibration, the builder STOPS and
   reports to the orchestrator before any pricing-dependent conclusion is
   drawn.
4. **P1 tolerances:** report both scales plus the local slope; the **binding
   verdict criterion is the payoff-scale one** (no adjacent-plan deviation
   above 1e-9) — that is the economic content of equilibrium; the cutoff-scale
   1e-10 is diagnostic only.
5. **L3 tolerance:** relative criterion `residual/|C_h| < 1e-6` for the
   standalone chord route (π̄ < 1e-2); absolute 1e-10 retained on the
   full-model route (π̄ ≥ 1e-2); smallest π̄ stays 1e-4. This amends the
   turn-1 check request as written; the amendment is quoted in the check JSON
   provenance ("tolerance amended per design review 2026-08-21").
6. **Check-script location: `quality_reports/fixes/t2_<id>_check.py` + json,
   per ticket 28.** The tickets outrank the design's preference; the D-series
   precedent stands. Package-internal probes and the smoke script live in
   `numerical_v4/` freely. (Design §10's proposed `v4_*` names are replaced
   by ticket 28's `t2_*` names.)
7. **A7′ is resolved** (ticket 24, `proofs/A7_construction.md`, pending its
   adversarial attack): A7′ = the composed terminal target `s ↦ b*_{j(s)}(s)`
   strictly increasing on the flagged signal region — exactly this design's
   "sum-monotone" finding, derived independently. The build implements the
   menu so A7′ holds (`a7_certificate` min-slope gate ≥ 1e-8 as designed;
   `brentq` inversion, never grid lookup). Note the two documents use
   different Voice families (pro-rata schedule `sh(d)` vs accumulation-length
   `n(s)`); A7′ sufficiency covers both, and only sufficiency is needed —
   the construction's necessity claim is family-specific and does not
   constrain this menu.

**Scope ruling for the build (ticket boundaries):** ticket 25 delivers the
`numerical_v4/` package (modules 1–8 of §11), the enumeration probe, and the
smoke run. The seven `t2_*` check scripts are **ticket 28's deliverable** and
are written by different agents against the built package — the builder does
not write them (build step 9 is re-scoped to "expose the API the checks
need").
