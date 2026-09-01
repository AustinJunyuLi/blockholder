# A6-continuity panel — Analyst B (defuse brief) — filed verbatim 2026-08-27

**Filing note (orchestrator).** The second of two opposed-brief Opus panellists dispatched
2026-08-27 under Austin's authorization to rule on the re-derivation's withheld change 6 (N11).
This analyst's brief: defuse — build the vanishing-mass argument, probe the deviation-payoff
subtlety, test whether the perturbation-family choice reconciles the limits, probe the implemented
menu. Read-only on the repo; probes and raw findings filed at
`quality_reports/fixes/a6_panel_probes_2026-08-27/`. The opposed report is
`2026-08-27_A6_panel_substantiate.md`. Adjudication: card §9 item 4 (with §5 A6/A3 evidence notes)
and `quality_reports/session_logs/2026-08-27_follow-ups.md`. Report below is the agent's return,
unedited.

---

# ANALYST B — defusal brief on N11. Report.

## (1) VERDICT: **NARROWED**

I could not defuse it. The mechanism is real, it reaches `𝒯`'s returned cutoffs, and I measured it. But N11's *locus* is wrong in both directions, and the collapse face the paper's baseline would actually visit is provably clean.

**X, stated exactly.** Write `Λ_k(h) = ∫ L_{j_k(s)}(h|s) φ_s(s) ds`. Step 9(b)'s rule is: Bayes where `Λ_k(h) > 0`; the **k-independent** plan-uniform posterior where `Λ_k(h) = 0 < Λ_u(h)`; Step 9(c)'s reference root (also k-independent) where `Λ_u(h) = 0`. `Λ_k(h)` is continuous in `k`, and `L_j(h|·)` is a step function on the finitely many mark-and-flag level cells. Therefore the price at `h` can be discontinuous **only** on `∂{k : Λ_k(h) > 0}` — and generically is, the one-sided limit being the value concentrating at the touching interval endpoint and the value at the frontier being the plan-uniform mean. That set is contained in

> (finitely many **cell-edge hyperplanes** `{k_i = a}`, `a` ∈ the mark/flag cell edges) ∪ (the collapse faces `{k_{i-1} = k_i}`)

So: (a) N11 **misses** the cell-edge hyperplanes — non-collapsed vectors, and that is where the implemented instance's jumps actually live; (b) a collapse face is a discontinuity only when the collapsing plan is the *sole* on-path generator of some positive-probability history, which the implemented Hold-collapse face is not.

**Brief item 1 — the vanishing-mass defusal is refuted, and I could not rebuild it.** Step 11's bracket is `E_z[Σ_d P^P_d(H^P_d)(B_j(s,d) − B_j(s,d−1))]`, an expectation under the **deviator's own** noise law given `(s,j)`. Affected histories carry weight `Pr(z_{0:d}) ≥ min(κ/2, 1−κ)^{d+1}` — independent of the collapsing plan's population mass. The implementation is literally that object (`numerical_v4/pooled.py`: `EP[d][t] = np.dot(L_t, P_d)`; `numerical_v4/policy.py::plan_payoff` reads `res.EP[d][θ(j,s)]`).

**Brief item 2 — the tie-break does not absorb it.** The largest-weakly-increasing-selection resolves *s*-direction ties at fixed `k`; a `k`-discontinuity in the `U` levels passes straight through any pointwise-in-`k` selection. Nor does the crossing structure absorb it: `U_HOLD` does not move when `U_VOICE` jumps, so the adjacent-pair difference jumps by the full amount.

**Brief item 3 — the family does not reconcile the limits.** At fixed `n` the denominator is `≥ (t_n/J)Λ_u > 0`, so the whole price system is continuous in `k`; the discontinuity is created only by `t_n → 0`. The two limits do not commute — the family choice cannot fix an order-of-limits problem. Notably, `OFF_PATH_EPS = 1e-14` in `pooled.py` **is** a fixed-`t` constrained game, i.e. N11's own "standard repair", already shipped; and the reference it attaches, `Ev[t] = E[v | n(s)=t]` over the whole line, **is** Step 9(b)'s plan-uniform posterior restricted to that type.

**Brief item 4 — the implemented case.** Collapse is *not* live at the baseline (`k* = (1.2405757283, 1.5310222869)`, Hold width 0.290447), the Hold-collapse face is clean, and yet the jumps are live at non-collapsed vectors. A compact `Θ` interior to one chamber restores A6 at the baseline and contains `k*` — but that fails at κ = 0.15.

## (2) The counter-argument I could not overcome, verbatim

> A6 as the card states it is quantified over *all* best-response cutoffs: "All best-response cutoffs lie in a common compact ordered polytope Theta; T is continuous and maps Theta into itself." Steps 13-14 construct Theta from the *bracket* `[s_lo, s_hi]` — the union over adjacent pairs of every indifference signal, uniform in the conjecture. Any Theta built that way contains the cell-edge hyperplanes, and on it the constructed price system's `T` is provably discontinuous: I measured jumps of 6.3e-03, 1.09e-02 and 2.83e-02 in `T_2` on the paper's own menu and calibration. The chamber-interior `Theta+` that rescues A6 is not something Steps 13-14 supply — exhibiting it requires already knowing where `T` maps a small box into itself, i.e. already knowing roughly where the fixed point is. So A6 is satisfiable here, but only under a reading of Theta that the proof does not construct and that cannot be checked without effectively solving the model first. That is a real gap between the hypothesis as written and the object built.

## (3) Probe numbers

**Hold-collapse face is clean.** Exit and Hold share mark-path type 0 (Γ is a buy-indicator; Exit's day-0 decrement marks 0), so type-0 mass is `Φ_s([s_lo, k₂))` — a function of `k₂` alone. Varying `k₁ ∈ {0.5, 1.0, 1.2406, 1.40, 1.52, k₂}` at fixed `k₂`, last value = Hold fully collapsed: `max|EP − EP(k₁=0.5)| ≤ 4.441e-16`; `U_V(1.6)` bit-identical; `𝒯(k)` bit-identical. **The whole pooled price system, hence `𝒯`, moves with `k₂` alone.**

**The jump reaches `𝒯`, at non-collapsed vectors** (frozen τ = 0.090764058616, `k₁ = 1.2405757283`; left limits converged by δ = 1e-7):

| `n(s)` cell edge `S` | `𝒯₂(S⁻)` | `𝒯₂(S)` | jump in `𝒯₂` | `𝒯₁` jump |
|---|---|---|---|---|
| 1.583333333333 | 1.549728951 | 1.543395170 | **−6.334e-03** | 4e-09 |
| 1.659062162746 | 1.569659263 | 1.558798550 | **−1.086e-02** | 3e-09 |
| 1.749268649265 | 1.603724853 | 1.575443391 | **−2.828e-02** | 3e-09 |

At the first edge, `U_VOICE(s₀)` jumps `0.0362570819 → 0.0365064990` while `U_HOLD(s₀)` moves `< 1e-10` — **no cancellation**. Price at a date-7 history carrying an `X=2` mark: two-sided limits **1.543850 vs 1.400791** (a 0.143 gap; left limit stable over δ = 1e-4…1e-8, right value constant for all δ ≤ 1e-10 including 0).

**A6 *is* satisfiable at the baseline, on a chamber-interior Θ.** `k₂* = 1.5310222869` sits inside the open chamber `(1.517932397378, 1.583333333333)` between k-independent cell edges, 0.0131 above / 0.0523 below. On a 29-point grid `𝒯` is smooth there (max adjacent `|d𝒯₂| = 1.185e-03` at spacing 3.17e-03, slope ≈ 0.35), and `𝒯₂([1.525272, 1.550633]) = [1.529026, 1.537885]`, `𝒯₁(·) = [1.231449, 1.243303]`. So `Θ⁺ = [1.23, 1.245] × [1.5253, 1.5506]` is compact, ordered, self-mapping, discontinuity-free, and contains `k*`. Brouwer runs verbatim on it.

**But the chamber rescue fails on the card's own grid, and — the strongest thing here — ticket 34 is explained.** At κ = 0.15, τ = 0.05, T = 5 (one of the four sweep-UNRESOLVED nodes), `𝒯₂` jumps at edges by up to **−0.16**, the diagonal crossing at edge 1.583333333 is **destroyed** by the jump (gap +1.0e-07 just below → −6.70e-02 at it), and a fixed point sits **on** the edge 1.659062163. There, `U_H − U_V` = −1.765771e-03 just below (n=8) and +1.278166e-03 just above (n=7): it **jumps through zero, never crossing it**. `equilibrium_residual` gives cutoff 4.751e-10, payoff **1.766e-03**; the solver from its own seed gives payoff 1.488e-03, and from `k_init=(1.02,1.71)` it gives `k = (1.0260443221, 1.7104049079)`, cutoff 2.878e-11, payoff **3.055e-04**. Those bracket the card's ticket-34 record ("3.1e-4 – 1.5e-3"; "1e-14 – 1e-11") exactly.

**Honest attribution of that last result:** it is the ***s*-direction** jump (Step 15(i) / WHERE IT FAILS 4 — `n(s) = clip(ceil(...))` is integer-valued, so `B_VOICE(s,d)` steps in `s`), **not N11's *k*-direction one**. Worse, the pointwise argmax across edge 1.659062163 runs **VOICE below → HOLD above** (singletons, at *both* of that node's fixed points), so the preferred plan *decreases*: `𝒮(k)` is empty and **h.3/A3 fails**, upstream of A6. My `𝒯₂` jumps remain attributable to N11's mechanism, on these grounds: (α) can move `𝒯` in `k` only where a smooth level shift slides a branch across a fixed `s`-jump — at generic `k`, not pinned to the edges — whereas every jump I measured is bracketed at an edge to ±1e-8 *and* co-located with a measured `U_V(s₀;k)` level jump at a fixed `s₀` away from any edge.

## (4) Card recommendation: a **sharper §9 line**, not N11's as drafted

Full proposed text is in the findings file (§6). Its core: name the locus as the **cell-edge hyperplanes ∪ plan-unique-generator collapse faces** rather than "collapsed vectors"; state that the jump reaches `𝒯` because `U_j` weights those prices by the deviator's own noise law; record that the pinned menu's Hold-collapse face is clean by Exit/Hold mark pooling; give the measured `𝒯₂` jumps; note that a chamber-interior `Θ` rescues A6 at the baseline but is not what Steps 13–14 construct and fails at κ = 0.15; note Step 18's Kakutani route already removes h.6's continuity half. **The P1 label is untouched** — A6 is a listed hypothesis, so this is satisfiability, not derivability. Separately, the κ = 0.15 argmax reversal is a **different and larger** finding about h.3/A3 and ticket 34, and should not be folded into the A6 line.

## (5) UNCHECKED

- General-menu satisfiability of a chamber-interior `Θ` — verified on one menu, one calibration, a 29-point grid; not proved, and shown to fail at κ = 0.15.
- Whether a destroyed crossing can leave a calibration with **no** fixed point. At κ = 0.15 a crossing is destroyed yet two fixed points survive; nonexistence is demonstrated nowhere. Not swept over (κ, τ, T).
- Whether A3's monotone-preferred-plan clause survives at the κ = 0.15 node. The card records "the A3 and A6 proxies pass at every achieving seed"; I did not open the proxy definitions to reconcile that with the argmax reversal above. **This is the item I would escalate first.**
- Flag-coordinate contribution to the locus: in the implementation the flag enters through *aliveness* (`_alive_weights` drops atoms with `D=1, f≤d`), not mark feasibility, so τ-crossing pullbacks are additional candidate edges; I swept the `n(s)` edges only.

## Files (all scratchpad, read-only on the repo, no git run)

`/private/tmp/claude-501/-Users-austinli-Projects-blockholder-v4-theory/ab9c0696-e7f9-466e-8d38-08f559ee1613/scratchpad/` — `a6_B_findings.md` (the full write-up), `a6_B_struct.{py,json}`, `a6_B_sweep.{py,json,log}`, `a6_B_baseline.{py,json,log}`, `a6_B_chamber.{py,json,log}`, `a6_B_node15.{py,json,log}`, `a6_B_resid.py`, `a6_B_alt.py`, `a6_B_argmax.py`.
