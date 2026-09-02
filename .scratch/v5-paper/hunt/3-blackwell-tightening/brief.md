# Brief 3: tightening is a Blackwell improvement

Read `.scratch/v5-paper/hunt/README.md` first. It holds the rules. This brief holds the
objective, the inputs, the constraints and what done means. The method is yours.

## Objective

Decide the following conjecture; prove it, disprove it, or sharpen it.

Conjecture. At fixed policies (S11), for tau' < tau at a common window T, or for T' < T at a
common threshold tau, the market's control-node experiment about the blockholder's type
(the pair plan and signal) under the tighter rule is Blackwell more informative than under
the looser rule, at every common kappa in (0, 1).

What the memo must settle:

- The statement with its full hypothesis list in the standing-condition numbering. Say which
  conditions carry the proof and where each is used. Say exactly what the control-node
  information set contains on each cell (the flagged tuple on the flagged cell, the pooled
  history with the public flag coordinate on the pooled cell; see (S6), (S7), (S8) and
  Steps 1 to 6 of `lem:flagged-kappa-free`), and whether the pre-filing pooled history on a
  flagged path matters for the claim.
- The proof, by an explicit garbling kernel from the tighter rule's output to the looser
  rule's output, or a counterexample. Name the hypothesis that makes a flagged type
  identified (the strictly increasing composed terminal target on the flagged region, the
  hypothesis `lem:flagged-kappa-free` carries) and say what happens without it.
- Whether the comparison is about the type or about the pair (v, a) the price depends on, and
  why the two coincide here.
- The endpoints kappa in {0, 1} and the corner T = H: included or excluded, and why.
- Corollaries, each with hypotheses:
  (a) the expected posterior variance of engagement, E[Var(a | I_H)], weakly falls when the
      rule tightens;
  (b) the expected premium Delta_act weakly rises when the rule tightens if the map h of
      eq. (g-kernel) in `proofs/02_garbling.tex` is convex on the convex hull of the pairs
      (pi, v-hat) that the control-node cells of both rules generate, and weakly falls if
      concave; state the hull exactly and say whether the flagged posteriors (pi = 1) sit in
      it;
  (c) anything else that follows at no extra cost, for instance the same order at every depth
      d <= H, or the composition of this ordering with the garbling in kappa of Lemma g2
      (is "tighter rule at higher kappa" ordered against "looser rule at lower kappa"? if
      not in general, say so in one line).
- What the result does not give. In particular whether it says anything about the noise
  sensitivity S or S_P. Be plain about it.
- What is and is not obvious. A referee may call the theorem a triviality. The memo says
  where the content sits (which hypothesis does the work, what breaks without no-feedback
  timing or without the strictly increasing target) so the paper can present it as the spine
  of the two-dial framing rather than as a headline.

Why the paper wants it. It gives a first theorem under the framing "tightening always improves
what the market knows; the sensitivity results say how the improvement is composed, into a
kappa-free flagged part and a silence part".

## Inputs

- `proofs/04_inherited.tex`: standing conditions (lines 257 to 297); `lem:flagged-kappa-free`
  (its hypothesis list and Steps 1 to 6 on the information set, the sandwich and the
  measurable inverse); `lem:partition`; `lem:threshold-weight` (i); `thm:clock`, the weight
  leg (nested flagged cells at both margins).
- `proofs/02_garbling.tex`: the setting, eq. (g-kernel), Lemma g1, Lemma g2 (the garbling in
  kappa, for comparison of kernels), Lemma g3(c) (the Jensen step you may reuse).
- `proofs/03_caught.tex`, the setup paragraph: the kernels h^{(T)} and h^{(T')} are evaluated
  at different information sets under the two rules.
- Calibration facts, for the "identified flagged type" hypothesis: `numerical_v4/menu.py`
  (`b_star` is strictly increasing on the whole line; `legal_clock`).
- `CONTEXT.md` for names.

## Constraints

- Effort: xhigh.
- Paths: write only under `.scratch/v5-paper/hunt/3-blackwell-tightening/`.
- Compute: none is needed. A numerical illustration (for instance E[Var(a | I_H)] at two
  rules at one node) is optional and needs the lock rules of the README; skip it if the
  machine is busy.
- Label the result would support: PROVED after the attack gate, or FAIL. Say which.

## Done

- `.scratch/v5-paper/hunt/3-blackwell-tightening/memo.md` in the README's shape, with the
  RESULT JSON block.
- Optional: `statement.tex` in the conventions of `proofs/04_inherited.tex`.
- One reply to the parent as the README says.
