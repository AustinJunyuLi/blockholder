# 01 · Order size as a model parameter, timed smoke at the calibration horizon

**Lane:** theory code. **Routing:** opus, default effort; a second agent verifies.
**Blocked by:** none. **Blocks:** 02 (grid verification), 03 (grid check), 05, 08 (via the direction note), 10.

**What to build.** `numerical_v4/params.py` gains `mark: int = 2`, the blockholder's per-round
order in noise lumps. `numerical_v4/pooled.py` enumerates order flow on the support
{-1, 0, ..., mark + 1} with the mark-path constraints generalised (a type trading `mark` in a round
cannot produce flow below `mark - 1`; an idle type cannot produce flow above 1), the likelihood
table generalised, and `n_hist` computed from the support size. `menu.py`, `flagged.py`,
`premium.py`, `policy.py`, `solver.py` are touched only where the support size is assumed.
`numerical_v4/checks/t2_t1_check.py`, `t2_l3_check.py`, `t2_l4_check.py`, `t2_atau_support_check.py`
and `t2_p1_check.py` run at `mark=2` and write their JSON records next to themselves, including
the frozen-policy κ sweep of the run-up share R/(R+J) per node (needed for the E2 direction note).

**Acceptance.**
- [ ] `.venv/bin/python -m numerical_v4.smoke` passes at `mark=2`, `H=10`, and prints wall time
      and peak resident memory for one node (evidence: the printed lines in the report).
- [ ] At `mark=1` every number the smoke prints matches the inherited `smoke_output.txt` to the
      printed precision (evidence: a diff).
- [ ] The inner fixed point converges at every calibration κ node at `mark=2` (evidence: the
      convergence flags in the smoke output).
- [ ] The five check scripts run at `mark=2` and write records; the T1 record includes, per node,
      the run-up share and its sign of change across the κ grid.
- [ ] Verifier who did not write the change reruns the smoke and one check and matches.

**Status:** open

## Comments
