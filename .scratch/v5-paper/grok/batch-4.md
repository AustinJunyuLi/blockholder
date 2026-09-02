# Batch 4

Effort `xhigh`. Read `README.md`, then `checkpoint-3.md`, then
`.scratch/v5-paper/issues/16-detection-frame.md` and, for the sections it inherits,
`.scratch/v5-paper/issues/15-theory-upgrade.md`. Write `runs/batch-4/plan.md` before the first
step.

## Objective

When the batch ends, all of these hold.

- Three new check scripts exist under `numerical_v4/checks/` with the provenance block of the
  existing ones, each run at `--nodes 1` inside the batch with its record written: the detection
  record (ticket 16), the cut record and the regret record (ticket 15, inherited). The full-grid
  runs, T in {3, 5, 10}, are the orchestrator's check runs at the checkpoint; every number in the
  paper renders from the record file so that the full run fills it without a prose edit.
- The appendix carries, with no label until the checkpoint's attack gate returns: the entry
  identity, the detection lemma, the upper-set lemma, the silence lemma, entry against the
  undetected, the Blackwell theorem with its corollaries and the strictness corollary, the
  trichotomy proposition, the threshold-margin restatement, the split identity, the one-crossing
  lemma, the reversal lemma, and the regret statement. Each has a full hypothesis list in the
  numbering of the standing conditions, which gain the noise channel, the flagged-tuple decoder
  and Borel regularity as ticket 15 states.
- `paper.tex` carries the new title, the abstract with the two central sentences of ticket 16
  (brackets left for the orchestrator), the introduction leading with the entry identity and the
  two detection technologies, the results in the order ticket 16 lists, the calibration section
  with levels first, the detection table, the split and the bands, then the remarks, and the
  conclusion with the fixed-policy scope. The net cut leg is named everywhere ticket 15 says.
- Every new statement has a self-attack record by a fresh context under the attacker rule of
  `README.md`; its verdict is advisory.
- `paper.tex` and `appendix.tex` compile in the order `CLAUDE.md` gives with zero errors, zero
  undefined references and zero undefined citations; the number guard, extended by one test per
  new record, is green against the one-node records.
- Every page of both PDFs has been rendered and inspected, and the inspection note lists what it
  found and what was fixed. The PDFs are not copied to `deliverable/`; the checkpoint delivers.

## Inputs

- Tickets 16 and 15 as above. Where they differ, 16 governs.
- The hunt memos and attack records under `.scratch/v5-paper/hunt/1-erasure-regime`,
  `2-one-cut-identity`, `3-blackwell-tightening`, `4-benchmark-regret`: statements, proofs and
  scripts to transcribe into the paper's numbering. The rest of the hunt directory, and every
  file under `gpt-pro-4` and `gpt-pro-5`, is not input and is never cited.
- `checkpoint-3.md`: the label every delivered result holds and the delivered tree's state.
- The committed records under `numerical_v4/checks/`: `t2_t1_check.json` (`kappa_profiles`,
  `node_table`), `t2_threshold_revelation_check.json` (coefficients, sign lists, pairs),
  `t5_who_gets_caught.json` (`t5_identity` rows, the clock cut split), and their scripts as the
  pattern for the new ones.
- `CONTEXT.md`, which now carries "Detection", "Silent history" and "Net cut leg".

## Constraints

- Paths: `paper.tex`, `appendix.tex`, `paper.bib`, `proofs/` (new files for the new statements;
  existing proof files only for the renaming, the corrected citation and the reconciliation
  sentence ticket 15 names), `numerical_v4/checks/` (new scripts and their one-node records; the
  number-guard test module), `figures/` and `numerical_v4/checks/figures.py` for the level figure
  and the Figure 2 legend, and the run directories under `.scratch/v5-paper/runs/`: `16-records`,
  `16-proofs`, `16-attack` (self-attack), `16-paper`, `16-check`, `batch-4`.
- Existing PROVED statements and their proofs are not edited beyond what ticket 15 lists; an edit
  outside that list reopens a gate and is a STOP.
- Labels stay as checkpoint 3 records them. New statements carry none. Prose cites a label as it
  stands and never promotes one; the two bracketed phrases of the abstract stay as brackets.
- The model is not changed: no new action, no order size other than two, no repricing, no
  change to `H` or to the calibration. T = 3 enters the new records only, as a stated grid
  extension; the existing proved comparisons and their records are untouched.
- Nothing in the paper mentions a hump, order size one, an execution response, E2, existence,
  the hunt, the external reviews or any earlier version. Fail twice, stop, per statement; a
  statement that fails its self-attack twice is written up as a STOP record and left out of the
  paper, and the abstract falls back as ticket 16 states.
- Compute: `PYTHONPATH=. .venv/bin/python`, one evaluation at a time, `--nodes 1` inside the
  batch; the compute lock protocol of `orchestration.md` applies.
- Prose: positive results only, plain words, no em dashes, sentence-case headings in markdown.
- Order inside the batch: records first, then the appendix statements and proofs, then the
  self-attack, then the paper prose, then the compile and guard, then the inspection.

## Done

- `.scratch/v5-paper/runs/16-records/result.txt`: PASS with the three record paths, the
  one-node values that the abstract's brackets will be chosen from (entry by detection state at
  the median node and κ = 0.5, the clock's level effect at κ = 0.85), and the guard output.
- `.scratch/v5-paper/runs/16-proofs/result.txt`: PASS with the list of statements and their
  hypothesis lists.
- `.scratch/v5-paper/runs/16-attack/result.txt`: one VERDICT per statement.
- `.scratch/v5-paper/runs/16-paper/result.txt`: PASS with the files changed and the number-guard
  output.
- `.scratch/v5-paper/runs/16-check/result.txt`: PASS with the compile log excerpt and the
  page-by-page inspection note.
- `.scratch/v5-paper/runs/batch-4/plan.md`, written before the first step, and
  `.scratch/v5-paper/runs/batch-4/result.txt` in the batch shape, `approach` included.
