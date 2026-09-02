# Brief 2: one cut identity for both dials

Read `.scratch/v5-paper/hunt/README.md` first. It holds the rules. This brief holds the
objective, the inputs, the constraints and what done means. The method is yours.

## Objective

Two parts. Part 1 is expected to be close to a transcription. Part 2 is the real mathematics.
Report each part with its own status in the memo; the RESULT block carries the weaker one.

### Part 1: the cut identity at the threshold margin

Decide whether the who-gets-caught corollary (`cor:caught`, `proofs/03_caught.tex`, parts (i)
to (vi)) holds verbatim for the threshold margin. The clock version compares T' < T at a
common tau; the threshold version compares tau' < tau at a common T, with

    A = C_P(tau, T),   B = C_F(tau', T) \ C_F(tau, T),   phi = P(B) / P(A),

the kernels h^{(tau)} and h^{(tau')} evaluated at each rule's own control-node information
set, s_A the kappa-derivative of E[h^{(tau)} | A], and the caught leg s_B defined as in
eq. (caught-sB) with the two rules exchanged for the two clocks. The conjecture is that (i)
nestedness, (ii) kappa-free masses, (iii) the cut identity, (iv) the band characterisation of
C_tau <= 1, (v) the criterion W_tau C_tau <= 1 and (vi) the readings all hold with the same
proofs, so that Condition D (`cond:D` in `proofs/02_garbling.tex`, which Theorem
`thm:g-threshold` shows is equivalent to C_tau <= 1) is the band condition "s_B lies weakly
between s_A and ((2 - phi)/phi) s_A" on what the tighter threshold removes from the pool.

The memo states the threshold version with its full hypothesis list (the analogues of (C-1)
to (C-3), each tied to the standing conditions) and either proves it or names the step that
does not transfer. If a hypothesis has to be added that the clock version does not need, say
which and why.

### Part 2: a sufficient condition on primitives for the band condition

Find a condition, stated on primitives or on kappa-free objects of the pooled cell, under
which the band condition of Part 1 holds at a threshold pair, hence C_tau <= 1. Requirements:

- It is checkable at a calibration node by a finite computation from objects the code
  exposes, with a stated tolerance. Name the objects (the pooled type law, the cell posteriors
  of Lemma g1, the kappa-free coefficients c_k of Lemma g3, type-level contributions to the
  sensitivity, whatever you use) and the computation.
- It implies the band condition at the kappa where it is checked, or on a stated interval of
  kappa, and the implication is proved.
- It holds where the grid holds. The facts: the record
  `numerical_v4/checks/t2_threshold_revelation_check.json` has Condition D holding on all
  eight adjacent pairs at every kappa in {0.15, 0.16, ..., 0.85}; it fails just below the
  grid, on the T = 5 pair (quantile 0.5 to quantile 0.3) for kappa in [0.1440, 0.1485]; the
  curvature hypothesis of Lemma g3(c) fails at every node; the kappa-free form of Remark
  `rem:g-Dstar` holds at no pair (the top coefficients c_k change sign). So a universal
  statement is false, and a condition that reduces to curvature of the kernel is known to
  fail. The target is a condition that separates the grid from the failure region.
- It has a reading. The paper wants one question for both dials: is what the tighter rule
  removes from the pool more noise-sensitive than what stays. Say what your condition says
  about who the threshold catches.

If no such condition can be found in the budget, the memo says what was tried, why each
attempt fails or is not checkable, and what the smallest open question is. That is a STOP for
Part 2, and it is a useful memo.

Why the paper wants it. Today the threshold dial's composition leg rests on Condition D, a
grid fact, and the clock's on a separate corollary. One identity, two dials, one question,
would let the paper state the composition effect once and check one band condition per node.

## Inputs

- `proofs/03_caught.tex`, the whole file.
- `proofs/02_garbling.tex`: setting, Lemma g1 to g3, Condition D, Theorem `thm:g-threshold`,
  Remarks `rem:g-Dstar` and `rem:g-cells`.
- `proofs/04_inherited.tex`: standing conditions (lines 257 to 297), `lem:threshold-weight`,
  `thm:clock`, `prop:factorisation`, `lem:flagged-kappa-free`.
- `numerical_v4/checks/t2_threshold_revelation_check.json` (the c_k per node, Condition D per
  pair and kappa node, W_tau, C_tau range) and `numerical_v4/checks/t5_who_gets_caught.json`
  (s_A, s_B, phi at the five clock nodes). Read the scripts
  `numerical_v4/checks/t2_threshold_revelation_check.py` and `t5_who_gets_caught.py` to see
  how the objects are computed; never run them.
- `.scratch/v5-paper/grok/checkpoint-0.md` and `checkpoint-1.md` for the label state and the
  failure numbers quoted above.
- For a computation of your own: `numerical_v4/params.py` (ParamsV4.baseline, replace),
  `numerical_v4/menu.py` (atoms, breakpoints), `numerical_v4/pooled.py` (pooled_pass),
  `numerical_v4/premium.py`.

## Constraints

- Effort: the highest you have. Part 2 is hard; give it the time.
- Paths: write only under `.scratch/v5-paper/hunt/2-one-cut-identity/`.
- Compute: you may run pooled passes under the lock rules of the README to check a candidate
  condition at a node (a pass is about 10 seconds). No cold solve. Your script and its record
  sit beside the memo.
- Statements in the standing-condition numbering; every added hypothesis named.
- Labels the parts would support: Part 1 PROVED after attack; Part 2 PROVED for the
  implication and NUMERICAL for the node check, or STOP. Say which.

## Done

- `.scratch/v5-paper/hunt/2-one-cut-identity/memo.md` in the README's shape, with a status per
  part and the RESULT JSON block.
- Optional: `statement.tex` in the conventions of `proofs/03_caught.tex`.
- Optional: a script and its record beside the memo.
- One reply to the parent as the README says.
