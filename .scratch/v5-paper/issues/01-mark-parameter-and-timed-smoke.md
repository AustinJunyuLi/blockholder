# 01 · Order size as a model parameter, timed smoke at the calibration horizon

**Lane:** theory code. **Routing:** kimi, effort medium, a task of minutes; an opus judge verifies
from the records after the check runs. **Blocked by:** none. **Blocks:** the check runs listed in
`orchestration.md` (Check runs), and through their records 03 grid, 05, 10.

**What to build.** `numerical_v4/params.py` carries `mark: int = 2`, the blockholder's per-round
order in noise lumps. `numerical_v4/pooled.py` enumerates order flow on the support
{-1, 0, ..., mark + 1} with the mark-path constraints generalised (a type trading `mark` in a round
cannot produce flow below `mark - 1`; an idle type cannot produce flow above 1), the likelihood
table generalised, and `n_hist` computed from the support size. `menu.py`, `flagged.py`,
`premium.py`, `policy.py`, `solver.py` are touched only where the support size is assumed.

The suite at order size two is three scripts: `t2_t1_check.py`, `t2_l4_check.py`,
`t2_threshold_revelation_check.py`. Each writes its JSON record next to itself with a provenance
block that carries `mark`, `H`, and the parameter hash. A block whose premise holds at order size
one only, the chord route through the ternary pooled law, reports `not_applicable` at
`mark >= 2`: `t1_block3_chord_magnitude`, `l4_pred4_quadratic_corollary`, `l4_pred5_A_prime_kappa_channel`.
A not-applicable block counts in neither `n_fail` nor the pass count and says why in its record.
`t2_atau_support_check.py` returns a one-line not-applicable record at `mark >= 2` without
computing. `t2_p1_check.py` and `t2_l3_check.py` stay in the tree and are not part of the suite.
The T1 record keeps the frozen-policy κ sweep of the run-up share R/(R+J) per node with its sign
of change across the grid.

**The worker runs no check script.** It runs the smoke at `mark=1` only. The smoke at `mark=2` and
the three suite scripts are check runs the orchestrator starts.

**State at the rewrite, 2026-09-02.** The code above is in the tree, uncommitted. The smoke at
`mark=2`, `H=10` passed at 993 s, 5.85 s per node, 7.07 GiB peak resident, convergence at all ten
κ nodes; its output is kept as `numerical_v4/smoke_output_mark2.txt`. The `mark=1` smoke matches
`smoke_output.txt` on every model number. What remains is the provenance stamp, the
not-applicable rules, and the suite list.

**Acceptance.**
- [ ] `.venv/bin/python -m numerical_v4.smoke --mark 1` matches `smoke_output.txt` on every
      printed model number (evidence: the diff in the report).
- [ ] `numerical_v4/smoke_output_mark2.txt` is present with the cost block and the convergence
      flags, from the run already made or from a rerun if `smoke.py`, `params.py` or `pooled.py`
      change.
- [ ] The three suite scripts write records with the provenance stamp; the not-applicable rules
      are in place; the A(τ) script short-circuits at `mark >= 2`.
- [ ] The worker changed no file outside `numerical_v4/` and ran no check script.
- [ ] Judge, after the check runs: reads the records, recomputes one node at `mark=2` at the T1
      baseline and matches its `M_F` and `M_P`; confirms every record carries `mark = 2`.

**Status:** code PASS (runs/01-rewrite, 2026-09-02), committed; judge verify pending on the T1 and L4 reruns the orchestrator started 2026-09-02 12:22 (checkpoint 1)

## Comments

2026-09-02, judgment on the first version. Four runs and no report: GLM 00:53 killed at 01:53;
GLM 01:53 stopped at 01:56; Kimi 02:08 stopped at 02:32; Kimi 02:33 stopped at 07:50 by the
orchestrator. The first run wrote the code; each later run found it and reran the scripts inside
its own session, polling a log for hours. The computation itself landed: the smoke at order size
two, the T1 record (3 h 28 min), the L3 record, the revelation record. The T1 record's block 3
fails with residual 4e-4 against 1e-10; that block tests the chord identity, which rests on the
ternary pooled law ADR 0003 retired, and the record shows six distinct pooled support points. It is
ruled not applicable at order size two, a label judgment recorded here and in the record. The
same ruling covers `l4_pred4`, `l4_pred5` and the A(τ) support script. The P1 check is out of the
suite: about 240 cold solves at about 236 s each is fifteen hours alone, and nothing the paper
states cites it. The T1 record's run-up sweep (share falling in κ from 0.740 to 0.459, no sign
change) is the E2 direction and entered `empirics/spec.md` by a dated note today. The record was
made without a `mark` stamp; its parameter hash `fbacc963f39422c3` equals the revelation record's,
whose provenance says `mark = 2`. The attempt count restarts at this rewrite (ADR 0004).

2026-09-02 08:46, L4 record. The L4 run the fourth worker launched at 06:28 (before the rewrite
edited the script at 08:31) finished ALL PASS in 8311 s and wrote `t2_l4_check.json`; its log is
kept as `runs/checks/t2_l4_check.worker-run-0628.log`. The record predates the provenance stamp,
like the T1 record: its `grid.order_size_mark = 2`, `grid.H = 10`, and its parameter hash
`fbacc963f39422c3` equals the revelation record's, whose provenance says `mark = 2`. Ruling, as
for T1: the record is accepted on that evidence and is not rerun, since the rewrite changed the
record's presentation only. Its `l4_pred4_quadratic_corollary` and `l4_pred5_A_prime_kappa_channel`
blocks show PASS and REPORTED; both are ruled not applicable at order size two and are not
evidence for anything the paper states. The weight leg (`l4_sign_Omega_up`, 16 steps, 0
violations) is the block the threshold theorem cites. The rewritten script labels these blocks
not applicable on any future run. The 30-minute cost estimate in the Check runs table was wrong:
the run alone took 2 h 18 min.
