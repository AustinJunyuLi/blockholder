# 03 · Who gets caught: signing the clock's composition ratio

**Lane:** theory. **Routing:** writer opus `high`; re-deriver opus `high`; grid check opus default.
**Blocked by:** 01 for the grid check only. **Blocks:** 11.

**What to prove.** Let A be the pooled cell at the longer clock T and B ⊂ A the histories the
shorter clock T' < T newly catches. At fixed policies the cell masses do not depend on κ. Prove the
identity for the noise sensitivity of the pooled expectation after the cut: with s_A and s_B the
κ-sensitivities of the conditional expectations of h on A and on B,
∂_κ E[h | A \ B] = (P(A) s_A − P(B) s_B) / (P(A) − P(B)), and conclude that the composition
ratio C_T is at most one if and only if |s_B| ≥ |s_A| whenever s_A and s_B share a sign, with the
mixed-sign case stated. State it as a corollary of the clock theorem in the paper's notation, in
`proofs/03_caught.tex`, with the one-sentence economic reading: the clock lowers noise sensitivity when
it catches the histories the market was reading most from order flow.

**Grid check.** A script under `numerical_v4/checks/` reconstructs the per-history, per-type mass
matrix at `mark=2` (the pooled pass keeps only the sum over types; rebuild it from the likelihood
table and the alive weights, using the measure weights, not the market weights), splits the T=10
pooled cell by which types the T=5 clock newly flags, computes s_A and s_B as point derivatives
of within-subset conditional expectations, and records at every calibration node whether the
corollary's condition holds and whether C_T ≤ 1, using the point-derivative convention for S_P.

**Acceptance.**
- [ ] Corollary statement and proof; re-deriver PASS.
- [ ] Grid record at every node with both booleans and the two sensitivities.
- [ ] The record's C_T ≤ 1 verdicts agree with the T1 check's at the same nodes under the same
      convention (evidence: a comparison table in the report).

**Status:** open

## Comments
