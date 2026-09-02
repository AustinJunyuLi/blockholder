# Attack on memo 3: tightening is a Blackwell improvement

I did not write the memo. I read `CLAUDE.md`, `CONTEXT.md`, section 3 of the spec, ADR 0003, the
standing conditions (S1) to (S11), `proofs/02_garbling.tex`, `proofs/03_caught.tex`,
`proofs/04_inherited.tex` (including `lem:flagged-kappa-free` step by step), the brief and the
memo. I then read the model code that fixes the objects the memo names: `numerical_v4/menu.py`,
`numerical_v4/flagged.py`, `numerical_v4/pooled.py`, `numerical_v4/params.py`.

I could not break the theorem or its three corollaries. Below are the lines I tried, what each
one hit, and the numbers I recomputed.

## What the theorem says and why each branch is exact

The claim is that the looser rule's tagged date-d output is a garbling of the tighter rule's
tagged date-d output, type by type. The proof splits the type set into three sets that are fixed
by the type alone: pooled under the tighter rule, flagged under both, and newly flagged. Each
branch of the kernel reads only the observed output, so the three do not interfere: the tag F or
P is observed, and inside the flagged part the branch is chosen by a function of the recovered
type.

Branch one is the identity. It is exact because the mark path is a function of the type and does
not read the rule, so a type pooled under both rules faces the same flow law and the same
all-zero flag coordinates. I checked the rule invariance in the source: `menu.mark_path` and
`menu.stake_path` take only the plan and the signal, and `menu.legal_clock` is the only place
where the threshold and the window enter.

Branch two and branch three both need the tighter flagged tuple to pin the type. That is (S14),
and it is the only load-bearing addition. Branch three then redraws the noise, which is exact
because the noise is independent of the type, the memo's (S12). Nothing else in the proof does
work.

## The attack lines that failed

**The date-d information set.** This was my main line. The memo's (S13) puts the whole tuple
(B^F, Q^F, a = 1) in the flagged information set at every depth d, and the recovery step needs
Q^F, not B^F alone. If the flagged order were submitted only at the control node, then at a date
d between the filing and the horizon the market would hold B^F and the filing date but not Q^F,
recovery would fail, and I can build a pair of types with the same B^F and different later mark
paths that breaks the order at that depth. The model does not do that. `numerical_v4/pooled.py`
drops a type from the pooled cell at the date its flag lands (`_alive_weights` skips atoms with
`D == 1 and f <= d`), and `run_up` prices the filing day as `J = P^F - P_{f-1}^P`, where `P^F`
comes from `flagged.flagged_price_at`, which inverts `B^F + Q^F`. So the flagged round is the
filing date, the tuple is public from that date, and the date-d form of (S13) is the model's own
convention rather than an invented one. The line fails.

**The necessity example living outside the model.** The example gives the two types stake
increments of one half while their marks are zero, which looked at first like a stake path that
the order-size-two model cannot produce. It is inside the model. Step 4 of
`lem:flagged-kappa-free` sets the mark as `q_{jd} = Gamma(B_j(.,d) - B_j(.,d-1))` with Gamma a
coarsening ordered in the increment, and `menu.mark_path` does the same. The order the market
sees is two lumps on a buying date whatever the stake increment is, so the memo's sentence that
the coarsening need not reveal the size of every increment is supported. I re-checked the example
arithmetic: both types cross at date 1, both file at date 2 under T' = 1, neither files under
T = 2, the tuples are equal at (2, 0, 1), and the mark paths are (0, 1, 1) and (0, 0, 1). The
linear programme finds no kernel at kappa in {0, 0.3, 0.5, 1}, so the example is a counterexample
under (S13), as claimed.

**The mark path being rule dependent.** Under the tighter rule a newly flagged type buys the
remainder at the filing date instead of continuing to accumulate, so its behaviour after the
filing is not the looser rule's behaviour. This does not touch the proof, because branch three
needs the looser rule's marks and the kernel knows the looser rule and the recovered type. In the
code the mark path is the same object under both rules in any case.

**The state the price uses.** The step from theta to (v, a) needs the output to be conditionally
independent of v given theta and the conditional law of theta given (v, a) to be rule invariant.
Both hold: the output is a function of the type and the noise, and the noise is independent of
(v, epsilon, xi). Integrating the kernel identity against rho(dtheta | v, a) gives the claim.

**The premium corollary.** The Jensen step needs the barycentre to stay in the curvature set. The
memo takes the closed convex hull of the two essential ranges, so it does, and the kernel h is
bounded by (S8), so integrability is not an issue. The direction is right: Z at the looser rule
is a conditional expectation of Z at the tighter rule, so convexity raises the tighter premium.
The model's pricing map depends on the information set only through (pi, v-hat) and carries no
rule label, which is what makes the same map serve both rules.

**The endpoints and the corner.** Nothing in the kernel needs kappa interior or the window
interior or either cell to carry mass. The endpoint claim is about the primitive noise law, and
it is correct there.

**The cross comparison.** The memo says a tighter rule at higher kappa and a looser rule at lower
kappa have no general order and gives a three-type example at kappa = 0 against kappa = 1. The
example is realisable in the model: two Voice types can share an accumulation length and still
have different crossing dates, because the crossing date reads the target as well. The
endpoints are not needed. The linear programme finds both directions infeasible at (0, 1),
(0.15, 0.85), (0.3, 0.7) and (0.45, 0.55).

**The fiber condition.** The memo says the minimal replacement for (S14) is that the looser
output law depends on the flagged type only through the tuple. That is right and it is both
necessary and sufficient: a flagged tighter output is a point mass, so the kernel row at that
tuple must equal the looser law of every type in the fiber, and the pooled branch is exact
already.

## What I recomputed

Scripts sit beside this file and run from the repository root. No script under
`numerical_v4/checks/` was run, `numerical_v4.smoke` was not run, no pooled pass and no policy
solve was started, so no compute lock was needed. The only import from the package is
`numerical_v4/menu.py`, which is arithmetic on the signal line.

`attack_check.py`, record `attack_check.json`.

- The memo's kernel, built explicitly from the tighter output, against the looser experiment:
  13500 cases over random models in the class, both margins, kappa in {0, 0.15, 0.5, 0.85, 1},
  every depth d <= H. Largest error 0.0 exactly, no fiber collision.
- An independent linear-programme test that asks whether any row-stochastic kernel works: 36
  cases, all feasible.
- The posterior variance corollary: no violation.
- The necessity example and the cross comparison, as described above.
- Calibration facts at the frozen cutoffs (0.9425017266871091, 1.8484512098302512) and the
  reported ladder: `max |B^F + Q^F - b*(s)| = 0.0` at every flagged node tested, minimum slope of
  b* on the flagged atoms 2.199e-4, zero collisions, and the flagged sets nest both in the
  threshold and in the window. So (S14) holds at the calibration by an exact identity plus a
  strictly positive slope, which is what the memo's part 3 says.

`attack_extra.py`, record `attack_extra.json`. Coverage, so that a clean pass is not a pass on
empty cases: over 1200 configurations, 438 have at least one newly flagged type and 330 have at
least one type flagged under both rules. The alternative convention, in which a flagged path
keeps its pre-filing pooled history, is feasible in all 72 linear programmes, which is the
memo's claim. The reverse order fails in all 10 probes where the tighter rule catches someone, so
the order is strict there.

`attack_search.py`, record `attack_search.json`. A wider class than the calibration menu: any
weakly increasing stake path, any binary mark path the coarsening can produce, a strictly
increasing terminal target. 34560 linear programmes, of which 10148 have a strictly larger
flagged set under the tighter rule. Not one infeasible case. This is the strongest evidence I
have: it asks for any kernel, not the memo's kernel, and it found no counterexample.

`attack_bite.py`, record `attack_bite.json`. Where the order has bite at the frozen grid.

## Verdict reasoning

The statement is proved as written, the hypotheses are named and each is used, the two examples
are correct under the stated convention, and the memo is plain about what the result does not
give, in particular that it signs neither S nor S_P. The label the result would support is
PROVED, which the memo correctly does not award itself.

Nits: none of these is a hole and none of them changes the verdict.

1. The theorem writes "In particular, there is a Markov kernel K_d". The kernel is the definition
   of the order being used, not a consequence of it. Read as a definition, the sentence is
   backwards.
2. (S14) carries the accounting identity B^F + Q^F = g(s) only at the tighter rule. Corollary 2's
   sentence that Z_r = (1, E[v | s]) for prior-almost every signal flagged by rule r uses the
   identity at the looser rule too. The fix is one clause, since the looser flagged region sits
   inside the tighter one and `menu.legal_clock` defines Q^F as b*(s) - B^F at every rule. The
   containment of the flagged points in the curvature set does not depend on the fix, because the
   set is defined as the closed convex hull of the two essential ranges.
3. The necessity example is convention dependent, and the memo does not say so. Under the
   alternative convention the memo itself discusses, where a flagged path keeps its pre-filing
   history, the two types are separated by rounds 0 and 1 and the one round the tighter output
   drops carries the same mark for both, so a kernel does exist. I checked it: feasible at kappa
   in {0, 0.3, 0.6, 1}. The example shows that (S14) cannot be dropped under (S13), which is the
   convention in force, and the sentence should say so.
4. Corollary 3 puts the identity map on the flagged cell when it applies Lemma g2 in kappa. That
   step needs the flagged output to be free of kappa, including any appended flagged price. It is
   free of kappa, but the one line that says so is missing at the place it is used.
5. The theorem includes kappa in {0, 1}. That is correct for the order. The calibration never
   evaluates there: `ParamsV4.kappa_floor` is 1e-3 and the grid runs on [0.15, 0.85]. A reader
   may want the endpoint claim marked as a statement about the primitive law.
6. The memo's restatement of (S7) writes "the common strategic order mark", where common means
   common across the two rules. That invariance is (S11) plus the fixed execution policy, not
   (S7). In the code it holds because the mark path never reads the threshold or the window.
7. Part 4 does not say where the result bites at the paper's own grid. At T = 5 the reported
   ladder reclassifies (flagged mass 0.1042, 0.0810, 0.0579, 0.0347, 0.0116), so the order is
   strict. At T = 10, which is the corner T = H, only a type crossing on date 0 can file, and
   every threshold in the ladder gives the same flagged set with mass 0.000681, so the two
   experiments coincide and the order is an equality there.
8. The RESULT block lists only `memo.md` under `files_changed`, which was right when it was
   written. This attack adds four scripts and four records in the same directory.

```json
{"verdict": "PASS", "reasons": "The kernel construction is exact on all three branches and the branches are chosen by functions of the observed output, so the looser tagged experiment is a garbling of the tighter one at every depth, at both margins, at every kappa in [0,1] and at T = H. (S14) is the only load-bearing addition, it holds at the calibration by the exact identity B^F + Q^F = b*(s) with min slope 2.199e-4 and zero collisions, and the memo's necessity example shows it cannot be dropped under (S13). My main attack line, that the date-d flagged information set cannot contain Q^F before the control node, fails: the model makes the flagged round the filing date, so the tuple is public from that date. A search over a wider model class, 34560 linear programmes asking for any kernel rather than the memo's kernel, with 10148 cases that actually reclassify, found no counterexample; the posterior variance corollary, the alternative convention paragraph and the three-type non-order example all check out, the last also at interior kappa. Eight nits, none of them a hole."}
```
