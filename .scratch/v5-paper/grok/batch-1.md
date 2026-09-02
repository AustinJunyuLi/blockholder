# Batch 1

Effort `high`. Read `README.md` in this directory first. Labels are result directories under
`.scratch/v5-paper/runs/`. Steps run in this order.

## Step 0: fixes from checkpoint 0

Read `checkpoint-0.md` in this directory. It lists the attack verdicts on `proofs/02_garbling.tex`
and `proofs/03_caught.tex`. If a verdict is FAIL, fix that proof once as the ticket's attack gate
says (label `02-fix` or `03-fix`, RESULT): the attacker's reasons are in the note; you may replace
one assumption with a cleaner one and must say so in the summary. If both verdicts are PASS,
there is nothing to do here.

## Step 1: who-gets-caught grid script (label `03-grid`)

Ticket `.scratch/v5-paper/issues/03-who-gets-caught.md`, grid check section.
`numerical_v4/checks/t5_who_gets_caught.py` exists from a killed run: 451 lines, never ran to a
record. Read it against the ticket's grid-check paragraph and finish it. It needs a `--nodes`
argument that limits the run to the first n calibration nodes; a provenance block (`mark`, `H`,
params hash) in its record; per node the two booleans (the corollary's condition holds; C_T at
most one) and the two sensitivities s_A and s_B, from the per-history, per-type mass matrix at
mark 2 rebuilt with the measure weights, splitting the T = 10 pooled cell by the types the T = 5
clock newly flags, with the point-derivative convention for S_P. Run it at `--nodes 1` only and
show the record it writes. Edit only that file. The full grid and the comparison against the T1
record are the orchestrator's. RESULT.

## Step 2: existence, only if clean (labels `05-write`, `05-self-attack`, `05-fix`)

Ticket `.scratch/v5-paper/issues/05-existence-if-clean.md`. `proofs/05_existence.tex` does not
exist. `numerical_v4/checks/t5_existence_conditions.py` exists from a killed run: 388 lines; its
docstring describes a certified-box argument (an interior ordered box around the solver's
candidate, single down-crossing of each adjacent-plan gap, a breakpoint-free Voice coordinate,
Miranda face signs). Read it. Use it if the proof you write is the one it checks; rewrite it if
not.

- `05-write`: state and prove existence of an equilibrium of the two-round model at order size
  two under conditions a script can check at every calibration node. Statement first, in the
  paper's notation, into `proofs/05_existence.tex`. The script takes `--nodes` and writes a
  provenance block. Run it at `--nodes 1` only. Return PASS if the proof is complete under its
  stated conditions and the script is written. Return ABSENT if no proof under grid-checkable
  conditions is available; then write a one-paragraph note under Comments in ticket 05, the only
  ticket edit allowed, write no proof file, and skip the two steps below. RESULT.
- `05-self-attack`: the attacker rule in the README. Read the statement at the top of
  `proofs/05_existence.tex`, the proof, and the four model sources; try to break it; where an
  inequality is doubted, recompute it at one node with a short script. VERDICT.
- `05-fix`: only when the self-attack returned FAIL. The writer fixes once; one assumption may be
  replaced by a cleaner one, said in the summary. RESULT. Whatever this returns, the step ends;
  no second self-attack. The Opus attack at checkpoint 1 decides the label.

The full condition grid is the orchestrator's check run; the label is decided by its record.

## Step 3: the E2 run (label `08`)

Ticket `.scratch/v5-paper/issues/08-e2-run-and-link-audit.md`, the run. Confirm the model
direction note dated 2026-09-02 is present in `empirics/spec.md` (it is committed; the git
evidence is the orchestrator's); FAIL if absent. Then:

```bash
PYTHONPATH=. .venv/bin/python -m empirics.fingerprints run e2
```

It writes `empirics/output/e2_estimate.json`, `e2_campaigns.csv`, `e2_runup_jump.pdf`. Report
every gate value (E2-G1, E2-G3, E2-G4) exactly as the result file holds them; a NO-GO is
reported, not repaired. Edit nothing outside `empirics/output/`. RESULT.

## Step 4: the E2 link audit (label `08-audit`)

A fresh subagent that did not run step 3. Draw sixty matched campaigns from
`empirics/output/e2_campaigns.csv` (seed 5, stratified by year), compare the CRSP issuer name
with the filing's subject name, write `empirics/output/e2_audit.csv` with one row per campaign
and the excerpt that supports each reading (mirror the columns of `e1_audit.csv` where they
apply), and write gate `E2-G2` into `e2_estimate.json` with PASS or NO-GO and the error count.
RESULT.

## End

Write `.scratch/v5-paper/runs/batch-1/result.txt` as the README says and stop.
