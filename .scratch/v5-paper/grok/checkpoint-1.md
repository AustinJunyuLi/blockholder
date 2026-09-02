# Checkpoint 1 (2026-09-02, after batch 1)

Batch 1 returned PASS on every step (`runs/batch-1/result.txt`). Seven Opus verdicts at this
checkpoint, all PASS. Two results leave the paper on the facts: existence is absent because a
condition fails at the first calibration node, and E2 is absent because gate E2-G1 is NO-GO.
This note carries the labels every result holds now, step 0 of batch 2, the records, and the
feedback on how batch 1 was approached.

## Verdicts

| Record | Question | Verdict | Outcome |
|---|---|---|---|
| `runs/04-attack-2` | the clock theorem after the batch-1 hypothesis fix; did the rest of the file move wording only | PASS | `thm:clock` PROVED; all four inherited results pass the gate |
| `runs/05-attack` | the existence implication (B1) to (B4) implies an equilibrium | PASS | the implication holds; seven nits, no hole |
| `runs/05-condition-judge` | is the (B3) failure at node 1 the model or the script | PASS (the model) | existence ABSENT |
| `runs/03-grid-review` | does the grid script measure the corollary's objects; node 1 against T1 | PASS | full grid run started |
| `runs/03-grid-judge` | the five-node record against the T1 record | PASS | grid record stands, committed d88418a |
| `runs/08-judge` | is the E2 link rule implemented as registered; is the audit sound | PASS | E2-G1 NO-GO stands; E2 ABSENT |
| `runs/01-verify` | T1 and L4 rerun records at mark 2, one-node recompute | PASS | records committed 5a199b5 |

## Labels at this moment, for ticket 11

- Partition and factorisation (04): PROVED. Flagged cell is κ-free (04): PROVED.
- Garbling lemma (02): PROVED. It contributes to neither leg on this grid (checkpoint 0).
- Threshold dial (02): the weight leg and the closed form of S_P in κ are PROVED; the composition
  leg is NUMERICAL on the grid κ in [0.15, 0.85], mark 2, H 10, resting on the four T = 5 pairs,
  tightest margin W_τ C_τ = 0.772, failing just below the grid (checkpoint 0 has the numbers).
  The paper names the grid at the point of claim and never says "for every κ".
- Clock dial (04): PROVED, by attack 2 at this checkpoint.
- Who gets caught (03): PROVED for the cut identity and the two-sided characterisation of
  C_T at most one in s_B. The grid record (`numerical_v4/checks/t5_who_gets_caught.json`, five
  τ nodes, T = 5 against T = 10, frozen baseline policy, κ = 0.5) has the condition holding and
  C_T at most one at every node, in agreement with the T1 record's verdicts. Any directional
  sentence is NUMERICAL off that record and names, at the point of claim, that the T = 10
  flagged cell is degenerate at every node (Ω = 6.8e-4, below the code's 0.01 floor; T = 10 is
  the corner T = H). A sentence that cannot carry that clause is not written.
- Existence (05): ABSENT. The paper carries no existence statement and no sentence about it. The
  calibration policies are the solver's baseline cutoffs; the paper states every result at fixed
  policies and does not call the calibration an equilibrium.
- E1 (06, 07): ESTIMATED, status GO, three gates PASS. E1 is not rerun: a rerun resets its
  audit gate. The clock paragraph renders from the E1 result file.
- E2 (08): ABSENT. E2-G1 link coverage is 0.737 against 0.8 (E2-G2 PASS with 0 errors, E2-G3
  and E2-G4 PASS). No E2 number, figure or sentence. The registered design stays in
  `empirics/spec.md` as committed.

## Step 0 of batch 2

Wording and record fields only; no label changes, no new claims. The checkpoint-2 diff confirms
that only wording and additive fields moved.

- `proofs/04_inherited.tex`: (1) `lem:partition` Step 6 says a cell is "empty of histories";
  the word is null. (2) In `thm:clock` the clause "κ ↦ M_P(κ,τ,T') is differentiable" is
  implied by the factorisation hypotheses at T'; drop it or mark it as a restatement. (3) Lines
  219 and 639 exceed the column wrap.
- `proofs/03_caught.tex`: (C-1) to (C-3) should name the flagged-endpoint κ-invariance
  `thm:clock` now demands; citing the clock theorem's hypotheses does it.
- `numerical_v4/checks/t5_who_gets_caught.py`: the record carries the degeneracy flag (flagged
  cell mass below 0.01 at T = 10) and `corner_T10_equals_H` as T1 does; `S_P_FLOOR` is 1e-12 as
  in T1; the provenance says T1's C_T is total variation and names the point route through T1's
  `M_P_pp` profiles; the report says B is a set of atoms and type 5 is partly caught. The rerun
  that refreshes the record is the orchestrator's.
- `empirics/test_fingerprints.py`: green with both audits on disk (E1-G2 PASS from ticket 07,
  E2-G2 PASS from batch 1), and still guarding that the runner leaves G2 to the audit. Today
  `E1GateTest.test_g2_is_left_for_the_independent_audit` is red because it asserts NOT RUN
  against a result file the audit has written. Code, not spec.

## Records

- Verdicts: `runs/04-attack-2`, `runs/05-attack`, `runs/05-condition-judge`, `runs/03-grid-review`,
  `runs/03-grid-judge`, `runs/08-judge`, `runs/01-verify`. Result records: `runs/05` (ABSENT),
  batch 1's step records, and `runs/checkpoint-1/step0.diff` with the node-1 copies of the two
  grid records.
- Grid records committed: `t2_t1_check.json`, `t2_l4_check.json` (01 reruns),
  `t5_who_gets_caught.json` (five nodes), `t5_existence_conditions.json` (node 1, (B3) false).
  `t2_threshold_revelation_check.json` (Condition D) was committed at checkpoint 0. Parameter
  hash `fbacc963f39422c3` is the frozen τ; `a5705efe39ed0a0c` is the baseline τ = 0.05 (the
  existence record hashed the baseline while running the ladder, moot with 05 absent).
  `t2_l3_check.json` is an older unstamped record, left untracked; nothing reads it.
- Commits: 003cb64 (ADR 0007 and the handoff), 1fe7c58 (04 fix and nits), bb0a946 (existence
  absent), a6328b5 (E2 run and audit), a122239 (batch-1 workflow as plan record), d88418a
  (who-gets-caught grid), 5a199b5 (T1 and L4 records).
- Two facts for the record from `runs/05-condition-judge`: the solver's candidate at node 1 is
  not an equilibrium at the P1 tolerance (adjacent-plan deviation 7.0e-5 against 1e-9; the
  241-point deviation grid steps over a 1.6e-3 island), and (B2) clears only the box's own Voice
  coordinate while the breakpoint that breaks single crossing sits 0.0136 above it. Neither
  touches a fixed-policy result.

## Feedback on the approach

Batch 1 ran before the plan rule, so its plan is the workflow Grok wrote,
`.grok/workflows/v5-batch-1.rhai` (committed a122239), read with the batch result.

What the plan got right. Step 0's three files are independent and ran together. Every prompt
carried the gates, so no subagent needed the README. The branches were right: ABSENT or STOP on
05 skips the self-attack and the fix, a FAIL on the E2 run skips the audit, and the closer
prefers the on-disk result over the workflow's own status. The audit design was made
reproducible (seed, sort key, allocation rule) and written into the gate block, and the judge
reproduced all sixty rows from it. Every file changed was reported; the judge found nothing
touched outside `empirics/output/`. Both negative outcomes were reported as they came out.

Where another order would have cost less. The 05 step wrote a 318-line proof and ran a
self-attack before the cheapest check: probing (B3) at the solver's candidate takes one pooled
pass, about twenty seconds, and returns false. Ordering by cost of information (the cheap
falsifier first, the expensive construction after) would have returned ABSENT in the first hour.
The brief pointed the step at the certified-box route and at writing the proof first, so part
of this cost is the brief's; ADR 0007 is the fix on that side.

Where another check before calling a step done would have cost less. After the E2 audit wrote
gate values into a result file, nobody ran `empirics.test_fingerprints`; it is red on a test that
predates the batch, and it would have surfaced at ticket 11's checker, the most expensive place.
The registered tests of a lane are the check that closes a step in that lane. Smaller: the
`05-fix` entry reads SKIP in the batch steps map and PASS in its file; the audit CSV was
finished after its result file; and the per-node time reported for the grid (1013 s) included
two cold solves, so the full grid took 857 s for five nodes rather than the 85 minutes the
report implied. Report fixed and per-node cost separately, and write the result file last.

To carry into batch 2. Plan first, in `runs/batch-2/plan.md`. Run the cheap falsifier before
the expensive construction. Close every step in a lane with that lane's registered check (the
number guard and the compile sequence for the paper). Write result files last.
