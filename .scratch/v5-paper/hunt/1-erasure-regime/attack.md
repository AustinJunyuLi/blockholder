# Attack on memo 1, order size two is the erasure regime

I did not write the memo. I read `CLAUDE.md`, `CONTEXT.md`, section 3 of the spec, ADR 0003,
the standing conditions (S1) to (S11) in `proofs/04_inherited.tex`, `proofs/02_garbling.tex`
(Lemmas g1, g2, g3 with their proofs), `proofs/03_caught.tex`, the brief and the memo. I then
recomputed every claim I doubted. I ran no git command, started no pooled pass and no policy
solve, took no compute lock, and wrote only inside this hunt directory. I did read
`numerical_v4/pooled.py` to check what the model's mark path is.

## What I tried to break

The memo's proposition has three legs. Order size two garbles and never reveals. Order size one
never garbles upward. Order size three or more always reveals. The equivalence then follows by
elimination. I attacked each leg, the hypotheses that carry them, the two decision problems, the
explicit kernel at order size one, and the scope of every side claim.

## Scripts

All five run from the repository root with numpy and scipy only. They import nothing from
`numerical_v4` and need no lock.

- `attack_check.py`: Blackwell feasibility by linear program on a grid of liquidity pairs, both
  directions, at order sizes one, two, three and four; the Lemma g2 delete and redraw kernel
  rebuilt from the lemma's own words and checked against the target channel; support overlaps;
  the memo's two decision-problem values.
- `attack_check2.py`: the same comparisons through an L1 residual program, which returns how far
  from a garbling a pair is instead of a yes or no.
- `attack_check3.py`: the memo's two-action false-claim problem exactly as written, and longer
  paths against the one-round turn.
- `attack_check4.py`: a grid map of the pairs that are garblings but sit outside the memo's
  one-round region, at path lengths one, two and three.
- `attack_check5.py`: an exact rational check with no linear program, using the two-state
  Blackwell criterion (the convex order on the posterior law under a uniform prior).

## What survives

The order size two leg survives. I rebuilt the Lemma g2 kernel from the lemma's text, deletion
probability `(kappa' - kappa) / (2 - kappa)`, the erasure value emitted on deleted rounds and on
rounds outside the revealed set, and a redraw on survivors from the target conditional law given
the mark. Its row identity holds to 1.1e-16 at (0.15, 0.85), (0.3, 0.9), (0.7, 0.71), and the
product kernel over two rounds reproduces every one of the four two-round mark paths to the same
accuracy. The memo's extension to the closed interval also holds: at (0, 0.3), (0.5, 1) and
(0, 1) the error is exactly zero, so the memo is right that no limiting argument is needed. The
non-revelation argument is right as well. The two conditional supports meet at the single flow
value one lump, so any two distinct mark paths share a positive-probability history at every
kappa in (0, 1], and at kappa equal to one the supports are {-1, 1} and {1, 3}, which still meet.

The order size one leg survives. The two-action false-claim problem is exactly as the memo says:
with the loss chosen above the finite likelihood ratios at both nodes, claiming is optimal only
at the flow minus one lump, and the value is t/4 at 0.1, 0.3, 0.5, 0.7 and 0.9, matching the
memo to machine precision. It is strictly increasing, so the higher node cannot be a garbling of
the lower one. The linear program agrees over 1176 interior pairs on a 0.02 grid: not one pair
allows the higher node to be a garbling of the lower one. The multi-round extension is right too.
The value with two paths differing in q coordinates is 1 - (1 - t/2)^q, confirmed at q equal to
1, 2 and 3, and the two-round program finds no upward garbling for the four-path set or for the
two-path diagonal set. So the memo's failure of property 1 at order size one holds for every
admissible state set, which is what the proposition needs.

The memo's explicit reverse kernel at order size one is correct and its region is exactly right
for one round. Over the same grid, the linear program's answer to "is the lower node a garbling
of the higher one" agrees with `2 kappa' + kappa >= 2` at every pair with no exception, and the
memo's four by four kernel reproduces the target channel to 2.2e-16 throughout that region. The
correct-guess value formula, 1 - t/2 below two thirds and t above it, is confirmed at every node
I tried, including the kink.

The order size three leg survives. At order size three and four the supports are disjoint, and
the program confirms Blackwell equivalence in both directions at (0.2, 0.8), (0, 0.5) and
(0.5, 1). So property 2 fails there and property 1 holds trivially, which is the elimination the
proposition needs.

The added hypotheses are the right ones and they are named. (E1) states the independence across
rounds and of the type that Lemma g1 uses in its proof but that (S1) to (S11) do not state.
(E2) matches the model: `numerical_v4/pooled.py` builds a type as an accumulation length, with a
buying date executing exactly `mark` lumps and an idle date zero, so a mark is 0 or 2 lumps and
nothing else. (E3) is satisfied in the model, because the pooled cell of a policy carries several
accumulation lengths and therefore several distinct mark paths. I found no hidden use of the
order-size-one pooled law as the model's law, and no support assumption on the pooled posterior:
the non-revelation argument uses only that two distinct paths exist and that kappa is positive.

I therefore could not break the proposition. The verdict is PASS.

Nits:

1. The exact turn at two thirds is a one-round fact and does not describe the paper's experiment.
   The memo scopes it correctly, writing "one round also gives the exact Blackwell turn" and
   fixing the two-state space. That scoping is what saves it, and the paper must keep it. The
   necessity half fails for the full mark-path history. Counterexample: order size one, two
   rounds, mark paths (0, 0) and (1, 1), kappa = 0.55 and kappa' = 0.70. Then
   2 kappa' + kappa = 1.95 < 2, so the memo's rule says the two nodes are incomparable, yet the
   two-round experiment at 0.55 is an exact garbling of the two-round experiment at 0.70. The
   exact rational check certifies it with no linear program: the two posterior laws under the
   uniform prior have the same mean and every call payoff is weakly larger at 0.70, which is the
   two-state Blackwell criterion. The linear program independently returns a kernel with residual
   below 1e-16. The same happens at (0.62, 0.68) and at (0.45, 0.75), and at path length three
   also at (0.15, 0.9) and (0.25, 0.85). The region grows with the path length, so the sentence
   "otherwise they are incomparable" is true for one round and false for the model's history. The
   direction the paper actually needs is untouched: higher liquidity is never a garbling of lower
   liquidity at order size one, at every path length I checked. If any of this reaches the paper,
   the turn must be stated as a single-round fact and the word incomparable must carry the same
   qualifier.

2. The citation of Lemma g2 covers types, while (E3) admits mark paths. (E3) lets the state set
   be any subset of the mark-path cube, which may contain paths that no type in the model
   realises. Lemma g2 is stated and proved for every type. The memo writes "for every type and
   hence for every mark path", and that inference runs the wrong way for an unrealised path. The
   content is fine, because the conditional law of flow depends on the type only through its mark
   path and the g2 proof is verbatim a per-path argument, and I checked the kernel identity row by
   row for all four two-round paths. One clause fixes the wording.

3. Section 4 says the threshold theorem "already fixes order size two and uses Lemma g2". In
   `proofs/02_garbling.tex` the threshold theorem rests on the factorisation, the combinatorial
   weight leg and Lemma g3(b). Lemma g2 is not invoked in its proof. The conclusion, that nothing
   changes there, is right; the reason given is not.

4. "One round settles both only-if regimes" understates the memo's own work. A one-round failure
   does not by itself give the failure for an arbitrary, possibly non-product, state set of paths.
   The memo supplies the q-coordinate argument that does, so only the summary sentence is loose.

5. The memo says no calibration computation is needed, which is right, but (E3) is an added
   hypothesis about the model and is left unchecked. One line would close it: the pooled cell of
   a policy carries at least two accumulation lengths, so it carries at least two mark paths.
   Where it does not, the pooled premium is free of kappa and the threshold theorem's own
   non-degeneracy hypothesis already fails.

```json
{"verdict": "PASS", "reasons": "I could not break the proposition. The order size two kernel of Lemma g2, rebuilt from its own text, reproduces the target channel to 1.1e-16 at interior pairs and exactly at the endpoints (0,0.3), (0.5,1) and (0,1), and the two supports meet at one flow value, so no two distinct mark paths are separated at any kappa in (0,1]. At order size one a Blackwell program over 1176 interior pairs finds no upward garbling, the memo's two-action false-claim value is exactly t/4 and its multi-round value is exactly 1-(1-t/2)^q, and the reverse kernel matches its stated region 2*kappa'+kappa>=2 at every grid pair with residual 2.2e-16. At order size three and four the supports are disjoint and the nodes are Blackwell equivalent both ways. The added hypotheses (E1) to (E3) are named, are needed, and match the model, and I found no use of the order-size-one pooled law and no support assumption on the pooled posterior. Nits only: the exact turn at two thirds and the word incomparable are one-round facts and fail for the full history (at order size one, two rounds, paths (0,0) and (1,1), kappa=0.55 and kappa'=0.70 with 2*kappa'+kappa=1.95 the lower node is an exact garbling of the higher one, certified in exact fractions); the Lemma g2 citation covers types while (E3) admits unrealised mark paths; the threshold theorem uses Lemma g3(b), not Lemma g2; the summary sentence about one round understates the memo's own multi-round argument; and (E3) is left unchecked at the calibration."}
```
