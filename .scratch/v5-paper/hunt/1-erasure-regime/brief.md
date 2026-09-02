# Brief 1: order size two is the erasure regime

Read `.scratch/v5-paper/hunt/README.md` first. It holds the rules. This brief holds the
objective, the inputs, the constraints and what done means. The method is yours.

## Objective

Decide the following conjecture; prove it, disprove it, or sharpen it into the true statement.

Conjecture. Take the paper's noise: one lump of size one, values -1, 0 and +1 with
probabilities kappa/2, 1 - kappa and kappa/2. Let the blockholder's order on a building round
be b lumps, b a positive integer, so a round's pooled order flow is X = m + z with the mark
m in {0, b}. Consider the pooled experiment about the mark path over the rounds 0 to H (the
paper's object: Lemma g1 and Lemma g2 in `proofs/02_garbling.tex`). Then the experiment at
kappa' is a garbling of the experiment at kappa for every pair 0 < kappa < kappa' < 1, and the
experiment is not fully revealing at any kappa in (0, 1), if and only if b = 2.

What the memo must settle:

- The precise statement. Say what "garbling for every pair" and "not fully revealing" mean,
  whether the endpoints kappa in {0, 1} are included, whether one round suffices or the full
  history is needed, and whether the statement is about the mark path only or about the type
  (the paper's type is the pair plan and signal; at fixed policies the mark path is a function
  of the type).
- The three regimes b = 1, b = 2, b >= 3, each proved. A claim that one finite experiment is a
  garbling of another is established by an explicit Markov kernel; a claim that it is not is
  established by an explicit decision problem, or a finite linear program, at which the
  supposedly less informative experiment does strictly better. At b = 1 the memo states where
  in (0, 1) informativeness turns.
- Whether the b = 2 half is already Lemma g2 of `proofs/02_garbling.tex`, and if so, say so
  and cite the lemma rather than re-proving it.
- Optional, only if cheap: the same question for a noise lump with support {-L, ..., L} and a
  symmetric law. Which order sizes, if any, give an erasure form there. One paragraph is
  enough; skip it if it costs more than that.

Why the paper wants it. ADR 0003 makes the order size the one change from the inherited
model, defended today by one paragraph. A referee will ask whether the order size was chosen
to make the theorem work. A proposition that order size two is the only size at which the
noise garbles building without confounding it answers that question.

## Inputs

- `proofs/02_garbling.tex`: the setting paragraph, Lemma g1 (erasure form), Lemma g2
  (garbling in kappa), Lemma g3 (representation), and their proofs.
- `docs/adr/0003-doubled-order-size-and-existence.md`.
- `CONTEXT.md`, entries "Order size", "Liquidity", "Pooled cell".
- Standing conditions (S1) to (S11), `proofs/04_inherited.tex` lines 257 to 297.

## Constraints

- Effort: xhigh. This is expected to be a short proof and a two-line counterexample; spend the
  effort on the exactness of the statement, not on length.
- Paths: write only under `.scratch/v5-paper/hunt/1-erasure-regime/`.
- Compute: none is needed. If you write a script (for instance the linear program at b = 1),
  it uses numpy or scipy only, does not import `numerical_v4`, and needs no lock.
- The statement is phrased in the model's objects (mark path, pooled flow, cell event,
  posterior) so it can sit next to Lemma g1 in the appendix.
- Label the result would support: PROVED after the attack gate, or FAIL. Say which.

## Done

- `.scratch/v5-paper/hunt/1-erasure-regime/memo.md` in the shape the README gives, with the
  RESULT JSON block.
- Optional: `statement.tex` beside it, in the conventions of `proofs/02_garbling.tex`.
- Optional: the script and its output beside the memo.
- One reply to the parent as the README says.
