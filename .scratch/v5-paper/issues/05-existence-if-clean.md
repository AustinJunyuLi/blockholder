# 05 · Equilibrium existence at the paper's calibration, only if clean

**Lane:** theory. **Routing:** writer Grok in batch 1 with a separate Grok subagent as self-attacker; Opus attacker at checkpoint 1; the condition run and its judge at checkpoint 1.
**Blocked by:** 01. **Blocks:** 11 (the writer needs to know whether it exists).

**What to attempt.** State and prove existence of an equilibrium of the two-round model at order
size two under conditions that hold at the paper's calibration nodes and can be checked by a
script. If the proof needs a condition that fails at any calibration node, the result is absent:
the ticket returns ABSENT, not FAIL, and the paper carries no existence statement and no sentence
about it. The fixed-policy results do not depend on this ticket. Write into `proofs/05_existence.tex`.

**Acceptance.**
- [ ] Either a proved statement with a grid record showing its conditions hold at every node and
      an attacker PASS, or ABSENT with a one-paragraph note in this ticket's comments.

**Status:** ABSENT (checkpoint 1, 2026-09-02). Attack on the implication PASS (`runs/05-attack`); condition (B3) fails at calibration node 1 (`runs/05-condition-judge`). The paper carries no existence statement.

## Comments

Checkpoint 1, 2026-09-02. The proof in `proofs/05_existence.tex` establishes existence of a cutoff
equilibrium at order size two under four named conditions on a box around the solver's candidate:
(B1) an interior ordered box, (B2) a Voice coordinate clear of k-free breakpoints, (B3) a unique
ordered down-crossing of each adjacent-plan payoff gap at every point of the box, (B4) Miranda face
signs. The independent attack passed the implication. The condition script at node 1 (tau quantile
0.1, T = 5, kappa 0.5) finds (B3) false: the Hold-Voice gap is a falling sawtooth in the signal,
declining on each plateau of the building count and jumping up at each plateau edge; at this node
it crosses zero at the candidate cutoff, falls to minus 5.8e-4, jumps by 6.5e-4 at the breakpoint
0.0136 above the box, stays positive on an island of width 1.6e-3 and prior mass 4.4e-4, then
crosses again. The judge reproduced the three crossings at 2001, 8001 and 32001 grid points and
under bisection, so the failure is a property of the model at this calibration. Two facts for the
record: the solver's candidate at node 1 is not an equilibrium at the P1 tolerance (the true
adjacent-plan deviation is 7.0e-5 against 1e-9; the solver's 241-point deviation grid steps over
the island), and (B2) clears only the box's own Voice coordinate while the breakpoint that breaks
single crossing sits just above it. The fixed-policy results do not depend on this ticket. The
paper states its results at fixed policies and does not call the calibration an equilibrium.
