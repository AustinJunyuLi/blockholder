# Brief 4: a rigorous bound on the benchmark policy's regret at every node

Read `.scratch/v5-paper/hunt/README.md` first. It holds the rules. This brief holds the
objective, the inputs, the constraints and what done means. The method is yours.

## Objective

A record `regret.json` beside the memo that gives, at each of the ten calibration nodes, a
rigorous upper bound on the benchmark policy's maximal interim regret.

Definitions. A calibration node is a pair (T, tau) with T in {5, 10} and tau one of the five
values of the threshold ladder, at kappa = 0.5, mark 2, H = 10 (the `provenance` block of
`numerical_v4/checks/t2_threshold_revelation_check.json` has the ladder and the benchmark
cutoffs `frozen_k` at full precision). The benchmark policy is the cutoff pair `frozen_k`
at every node. At a node, with `res` the pooled pass at `atoms(frozen_k, p)` and `U_j(s)` the
plan payoff `numerical_v4.policy.plan_payoff(j, s, res, p)`, the regret at a signal s is

    R(s) = max over j in {Exit, Hold, Voice} of U_j(s)  minus  U_{j(s)}(s),

where j(s) is the plan the benchmark cutoffs assign to s. The quantity to bound is the
essential supremum of R over s in [s_lo, s_hi] under the signal law (a bound on the supremum
off a null set is enough).

Rigorous means proved, not sampled. R is piecewise smooth in s. Its breakpoints are the set
`numerical_v4.menu.breakpoints(frozen_k, p)`: the two cutoffs, the jump points of n(s), and
the pull-backs of every tau-crossing date. Between consecutive breakpoints, every ingredient of
U_j(s) at a fixed pooled pass is a smooth closed-form function of s (the target b*(s), the
posterior mean of v, the stake path, the engagement cost); the pooled pass itself does not
move with the deviating s. How you turn that into a certified bound on each piece is your
choice (a derivative bound times the sample step plus the sample maximum, exact maximisation,
a monotonicity argument, interval arithmetic). The memo proves that the method bounds the
supremum on every piece, and the record states the method and its tolerance. A uniform grid
alone is not acceptable: the solver's 241-point grid stepped over a 1.6e-3-wide island at
node 1 and reported zero regret there.

The record reports per node: the bound; the piece (interval between breakpoints) on which it
is attained and that piece's prior mass; every piece with positive regret, its endpoints, its
prior mass, the alternative plan that wins there and the bound on that piece; the assigned
plan's payoff level at each cutoff for scale; the parameter hash; and the wall time. The memo
adds one table with the ten bounds.

Reference numbers, to reconcile rather than reproduce. At node 1 (T = 5, tau = 0.09239820)
the node's own solved candidate is k-hat = (0.9425042193, 1.8472640726), not the benchmark
policy; at k-hat the Hold-Voice gap has a regret island (1.8608, 1.8625) of width 1.6e-3, prior
mass 4.4e-4 and peak 7.0e-5, and regret zero elsewhere to solver tolerance; see
`.scratch/v5-paper/runs/05-condition-judge/result.txt` and the plateau table in
`/tmp/judge05_gap.json`. The benchmark cutoffs were solved at the median threshold and T = 5,
so at every other node the benchmark is not that node's candidate and its regret may be larger
and sit elsewhere. The memo says how the node-1 numbers at the benchmark relate to the
numbers at k-hat.

Why the paper wants it. The paper states every result at the benchmark policy, which is not
an equilibrium of its game. One number per node, "the largest gain any type can get by
switching plans is at most R-bar", tells the reader how far the benchmark is from a best
response. It changes no label. The memo says where the number would go (one sentence and one
table row in the calibration section) and which label the sentence would carry (NUMERICAL, off
this record).

## Inputs

- `numerical_v4/checks/t2_threshold_revelation_check.json`, `provenance` block: `frozen_k`,
  `tau_ladder`, `params_hash`, `mark`, `H`.
- `numerical_v4/params.py` (`ParamsV4.baseline()`, `.replace(tau=..., T=...)`, `s_lo`,
  `s_hi`, `hash_str`), `numerical_v4/menu.py` (`breakpoints`, `atoms`, `b_star`, `n_days`,
  `legal_clock`, `stake_path`), `numerical_v4/policy.py` (`plan_payoff`, `engagement_cost`),
  `numerical_v4/pooled.py` (`pooled_pass`, called with `with_runup=True`),
  `numerical_v4/flagged.py` (`flagged_price_at`).
- `numerical_v4/solver.py`, `equilibrium_residual`: the 241-point method that missed the
  island. Read it for what not to do; you may call it on an existing pooled pass if you want
  its number for comparison, since it does not start a pass when `res` is given.
- `.scratch/v5-paper/runs/05-condition-judge/result.txt` and `/tmp/judge05_gap.json`.

## Constraints

- Effort: high on the certification argument, ordinary on the code.
- Paths: write only under `.scratch/v5-paper/hunt/4-benchmark-regret/`.
- Compute, exactly as the README says: take the lock once for the whole run with
  `what` = "hunt 4 regret record, ten pooled passes", release it when the script exits. Ten
  pooled passes at about 10 seconds and 6 GB each, in sequence, never in parallel. No cold
  solve, no check script, no smoke, H unchanged. Keep total wall time under about five
  minutes; if a node needs more, say so and stop.
- The script is deterministic and re-runnable and writes the record last.
- Nothing is written under `numerical_v4/`.

## Done

- `.scratch/v5-paper/hunt/4-benchmark-regret/regret.py` and `regret.json`.
- `.scratch/v5-paper/hunt/4-benchmark-regret/memo.md` in the README's shape. Part 1 is the
  record's claim ("at the benchmark policy the maximal interim regret at node n is at most
  R-bar_n, by method M with tolerance t"), part 2 the certification argument, part 3 the
  computation, part 4 the cost. RESULT status PASS if a certified bound exists at every node,
  FAIL if the method cannot certify, STOP if blocked.
- One reply to the parent as the README says.
