# Attack on the benchmark-regret record

I judged `regret.json` and `memo.md` in this directory against the model code in `numerical_v4/`.
I did not write them. I read `CLAUDE.md`, `CONTEXT.md`, the hunt `README.md`, the brief, the memo,
`regret.py`, the record, and then `policy.py`, `menu.py`, `flagged.py` and `pooled.py`. My own
script is `judge_regret.py` beside this file. It runs from the repository root as
`PYTHONPATH=. .venv/bin/python .scratch/v5-paper/hunt/4-benchmark-regret/judge_regret.py`. It took
the compute lock once, ran one pooled pass at node 1, and released the lock in a `finally` block.
Total wall time was 8.6 seconds. I ran no solve, no script under `numerical_v4/checks/`, no smoke,
and no git command.

## Do the closed forms equal plan_payoff

Yes, on every branch the record uses. I re-derived each branch by hand from `plan_payoff` and then
tested it numerically.

Exit. `terminal_stake` is zero and the only non-zero increment is the day-zero sale of `b0`, so the
payoff collapses to `b0 * res.EP[0][0]`, a constant. The script uses exactly that expression.

Hold. The stake path is flat, so the trade cost is exactly zero and the payoff is
`b0 * ((1 - Ep0) v_h + EpP0 + Ep0 m0)`, affine in s. The script matches, and `p.m0` is the right
premium because `a = 0` for Hold in `plan_payoff`.

Voice, pooled. Increments are `(b - b0)/n` on dates `0..n-1` and zero after, so the trade sum is
`(b - b0) * A_n` with `A_n` the average of `res.EP[d][n]` over `d < n`. The memo's equation (1) and
the script's `exec_price` are that object. The script writes `Ep * p.m1` where `plan_payoff` writes
`Ep * (p.m0 + p.Delta_m)`; at this calibration `p.m0 + p.Delta_m == p.m1` holds as an exact float
equality, which I checked.

Voice, flagged. Here the memo's step matters. `inner_price` returns the root of
`(1 - p)(P - V) - p m1 = 0` at posterior one, and that equation is algebraically identical to
`P = EY`, where `EY` is the expectation `plan_payoff` builds from `P_F` and `p_F`. So the reported
`max_residual` is exactly `|P - EY|`, and substituting `EY = P` turns
`b EY - (1 - r_f)(b - b0) P_F` into `B^F P_F`. The memo's equation (2) is therefore right, and the
error it leaves behind is at most `b_bar` times the root residual, which the record measures at
2.5e-16. The script's `exec_coeff` sums `res.EP[d][n]` over `d = 0..min(f, n-1)` and divides by n,
which is the flagged trade sum. One point the memo does not say: at all ten nodes every flagged
piece has `r_f = 1` and `min(f, n-1) = n - 1`, so the flagged branch runs in one sub-case
everywhere, and node 1 exercises it at n = 5, 4, 3, 2 and 1.

Numerically, at node 1 I compared the script's branch evaluator with `plan_payoff` at 60 interior
points of each of the 17 pieces, for all three plans, 3060 comparisons. The largest absolute
difference was 6.9e-17. The gap between the script's `inner_price` at `v_h(s)` and
`flagged_price_at`, which inverts `b*` with brentq before pricing, is inside that number.

## Are the derivative bounds valid

Yes. I re-derived equations (3) to (7).

Equation (3) is the exact derivative of (1). Equation (4) bounds it term by term: `b*'` is largest
at the point of the closed piece nearest `mu_v` because `(1 + x^2)^{-3/2}` falls in `|x|`, and
`max_bprime` clamps `mu_v` into `[lo, hi]`; `Y_n` is affine in s so `|Y_n - A_n|` is maximal at an
endpoint; `b*(s) < b_bar`; `Ep_bid` is a probability average and lies in `[0, 1]`, so
`(1 - e_n) beta >= 0`; and `chi > 0` makes the cost term largest at the left endpoint. `L_E = 0` is
exact and `L_H` is the exact slope.

Equation (5) is the correct implicit derivative. With `a = 1 - p = Phi(u)` and
`u = (P + K + m1 - S_bar)/sigma_xi`, the fixed point gives `P - V = (1 - a) m1 / a`, hence
`P - V + m1 = m1 / a` and `dP/dV = a^2 / (a^2 + (m1/sigma_xi) phi(u))`. Since `m1 = 0.3 > 0` and
`phi >= 0`, the ratio is in `(0, 1]` and `dP/ds = beta dP/dV` lies in `(0, beta]`. Equation (6) is
correct for the same reason: `a` rises in P, so `(1 - a)/a` falls in P, and the root is bracketed by
`V` below and by `V + m1 (1 - a(V))/a(V)` above. The code applies (6) with `v_max` for the base and
`a` at `v_min` for the tail, which is conservative and valid because `beta > 0` makes V rise in s.
The `|P_F|` bound is then the larger of the two endpoint absolute values, which bounds the absolute
value on any interval. Equation (7) follows from differentiating (2) with `B^F <= b_bar`.

Numerically, at node 1 I compared finite differences of every branch and of every payoff gap on a
20001-point grid on each piece against the claimed constants. No difference exceeded its constant
by more than the rounding noise of a difference quotient, and the only near-equality case is the
Hold branch, whose constant is the exact slope. On the flagged pieces I checked the price bracket,
the `|P_F|` bound and the slope directly: `dP_F/ds` stayed in `[0, beta]` with maximum 0.500000 at
`beta = 0.5`.

## Is the breakpoint set complete

Yes. What must stay constant on a piece is the assigned plan, `n(s)`, the crossing date c, the
filing date f and the flag D. The cutoffs handle the plan. The jumps of `n(s)` are the pull-backs of
`g(x) = 1 - m/(n_scale (H+1))` for m = 1 to H+1, and the clip to `[1, H+1]` removes the rest. Inside
an n plateau, `c = ceil(ratio n) - 1` changes only where `ratio n` hits an integer m in 1 to n, that
is where `b*(s) = b0 + (tau - b0) n / m`, and the loop over `d` covers exactly `m = min(d+1, n)` for
m = 1 to n. The onset of D is the case m = n, that is `b*(s) = tau`, and it is in the list. f is
c + T and D is `1{f <= H}`, so neither adds a point. Candidates with `y >= b_bar` have no preimage
in the support, so dropping them loses nothing.

I checked this empirically rather than only by reading. At all ten nodes I sampled 200 interior
points of every piece of the certifier's partition and recomputed the assigned plan, `n(s)` and the
whole Voice clock. The signature was constant on every piece of every node. At all ten nodes the
partition starts exactly at `s_lo` and ends exactly at `s_hi`, so nothing outside the support is
certified and nothing inside is skipped. The certifier keeps the unmerged candidate set, so the 1e-9
merge in `menu.breakpoints` cannot hide a narrow piece, and the record's piece counts match the
merged counts at every node, which means the merge in fact removed nothing here.

Closures and cutoffs are handled correctly. Each piece is certified on its closed interval with the
one-sided branch formula. The breakpoints are finitely many and the signal law has a density, so the
essential supremum over the support is bounded by the maximum over pieces. Two of the three positive
pieces at node 1 attain their maximum at an endpoint that is a cutoff or an `n(s)` jump; that is the
correct one-sided limit, and the interior values converge to it, so those bounds are close to tight
rather than artefacts.

## Is the cover inequality applied with the right radius, and is the float allowance enough

Yes. The grid is `linspace(lo, hi, nseg + 1)` with `nseg = ceil((hi - lo)/1e-5)`, so the spacing is
`(hi - lo)/nseg` and every point of the closed piece is within half that of a sample point. The code
uses `0.5 (hi - lo)/nseg` as the radius, which is the right number, and it recomputes the radius from
the actual `nseg` rather than from the 1e-5 target. I reproduced `nseg` and the radius from the piece
endpoints for every reported piece at all ten nodes with zero deviation, and I reproduced every
`certified_upper` as `sample_max + L radius + 5e-12` exactly.

The allowance covers the residuals with about five orders of magnitude to spare. The measured
evaluation error against `plan_payoff` is 6.9e-17, the flagged root residual contributes at most
`b_bar` times 2.5e-16, and the pooled price residual is 1.5e-16. The memo's three quoted residual
and radius numbers match the record exactly.

## Does the script compare all three plans

Yes. For each piece it loops over all plans other than the assigned one, so both alternatives are
evaluated on every piece, and the piece bound is the larger of the two certified uppers, floored at
zero. It never compares only adjacent plans. The record stores both alternative rows for every
reported piece, and I checked that each reported piece carries exactly two of them.

## The one-node recompute

I recomputed node 1 (T = 5, tau = 0.092398203874295259) with one pooled pass under the lock. The
pass took 6.4 seconds with maximum price residual 1.49e-16. Feeding that single pass into the
record's own `certify_node` reproduced the node bound bit for bit at 9.6232195520347914e-05, the
attaining piece [1.8608284620211166, 1.8895347974857488] with Voice assigned and Hold the winning
alternative, and all three positive pieces with zero deviation. The cutoff payoff levels reproduce
from `plan_payoff`.

I then attacked the bound directly. On every one of the 17 pieces I searched for the supremum of R
on a mesh of about 1e-6, refined four times around the best point, using the branch formulas that I
had already validated against `plan_payoff`. No piece beat its recorded bound. The global maximum was
9.5932662747e-05 at s = 1.86082846202112, which is the record's sample maximum and its attaining
piece, and `plan_payoff` itself returns the same regret at that point. So the bound is above the true
supremum and about 3e-07 above it, which is the cover term.

The node-1 numbers reconcile with the reference island as the memo says. The island quoted in the
brief belongs to the node's own solved candidate k-hat and its own pooled pass, not to the benchmark
policy. Both sit immediately to the right of the same `n(s)` jump at 1.8608284620. At the benchmark
the peak is larger, 9.59e-05 against 7.0e-05, and the piece is wider, which is what one expects from
a policy solved at a different node.

## What I could not check

Nodes 2 to 10 rest on the same code path with a different pooled pass, and I ran one pass only, as
instructed. For those nodes I verified the piece structure, the signature constancy on every piece,
the record's internal arithmetic, and that the flagged branch runs in the same sub-case as at node 1.
The certification argument is node-independent and the script is deterministic, so the node-1
recompute carries over. A reader who wants the same direct evidence at every node needs ten passes.

Nits: `complete_breakpoints` filters the tau crossing pull-backs to the support but not the `n(s)`
jump pull-backs, unlike `menu.breakpoints`. At this calibration all eleven jumps lie strictly inside
the support, which I checked, so the partition is exactly the support at all ten nodes and nothing
changes. If a jump ever fell outside, the certifier would extend the partition past the support and
could report a bound attained off support. Nit: the memo says the code applies equation (6) "at the
interval endpoints", which understates what the code does; it takes the base from `v_max` and the
tail factor from `v_min`, and that mixture is what makes the bound valid. Nit: equations (5) and (6)
need `m1 > 0` and the memo does not name that hypothesis, though (S9) plus `m0 > 0` delivers it. Nit:
the memo's part 1 says "mesh width at most 1e-5", which is the segment width; the cover radius is
half of it, and the record is clear about this. Nit: the record's `positive_regret_pieces` filter is
`bound > 0`, and since the 5e-12 allowance is always added, the filter is really "not certifiably
unprofitable by more than the allowance"; the `positive_sample_witness` flag records the difference
and the memo explains it.

```json
{"verdict": "PASS", "reasons": "The closed-form branches equal plan_payoff on every piece: 3060 comparisons at node 1 agree to 6.9e-17, and the flagged simplification B^F P_F is exact because the inner_price root makes EY equal P_F, with the residual measured at 2.5e-16. Equations (3) to (7) are correct on the closure of each piece; b*' peaks at the point nearest mu_v, Y_n is affine so its extreme is at an endpoint, and the implicit derivative gives dP_F/ds in (0, beta] because m1 > 0, which finite differences confirm at max 0.500000. The breakpoint set is complete: the cutoffs, the eleven n(s) jumps, and the crossings b* = b0 + (tau - b0) n/m for m = 1..n cover every change of plan, n, c, f and D, and 200 interior points per piece at all ten nodes show a constant signature, with the partition spanning exactly [s_lo, s_hi]. The cover uses the half actual mesh spacing, reproduced with zero deviation from the piece endpoints at every node, and the 5e-12 allowance dominates every measured residual. All three plans are compared on every piece. The node-1 recompute with one pooled pass reproduces the bound bit for bit at 9.6232195520347914e-05, and a 1e-6 mesh with refinement over all 17 pieces finds a true supremum of 9.5932662747e-05 at s = 1.86082846202112, under the bound and confirmed by plan_payoff. Only nits remain, listed above."}
```
