# Batch 2

Effort `xhigh`. Read `README.md`, then `checkpoint-1.md`. Text in angle brackets is the
orchestrator's to fill from checkpoint 1; the brief is final when none is left.

## Objective

When the batch ends, both of these hold.

- `figures/` holds the figures ticket 10 names, each as a PDF, each regenerating from a command
  the report lists, and each showing only cases the paper's results cover.
- `paper.tex`, `appendix.tex` and `paper.bib` exist in the structure ticket 11 states. They
  compile in the order `CLAUDE.md` gives with zero errors, zero undefined references and zero
  undefined citations; the number guard is green; every theorem in `paper.tex` has its proof in
  `appendix.tex` and carries the label checkpoint 1 records for it; every number renders from a
  result file or a grid record.

## Inputs

- Tickets `.scratch/v5-paper/issues/10-figures.md` and `.scratch/v5-paper/issues/11-paper-writer.md`.
- `checkpoint-1.md`: the label each result holds, and the label scope carried forward from
  `checkpoint-0.md`.
- The records every figure and every theory number comes from: `<T1 record, who-gets-caught
  record, existence condition record if 05 is present, and any other record checkpoint 1 names>`.
- `empirics/output/e1_estimate.json` and `empirics/output/e2_estimate.json` with their gates.
- The proofs under `proofs/`, which `appendix.tex` assembles.
- `docs/brief_2026-09-01_referee.md` as input to the rewrite, and the inherited draft's prose
  where it still holds.

## Constraints

- Paths: `figures/`, `numerical_v4/checks/figures.py`, `empirics/fingerprints.py`, `paper.tex`,
  `appendix.tex`, `paper.bib`, and the run directories `10`, `11` and `batch-2` under
  `.scratch/v5-paper/runs/`.
- The paper carries the labels checkpoint 1 gives: `<the label of each result>`. Prose states
  the label a result holds.
- Existence (05): `<present, with label ...>` or `<absent, so the paper carries no existence
  result and says nothing about it>`.
- E2: `<the four gate outcomes; whether the exercise is in the paper>`. An exercise whose gate
  reads NO-GO is absent from the paper, with no sentence about it.
- The threshold theorem's headline wording: `<the named condition it carries, or none>`.
- The grid a NUMERICAL claim rests on is named at the point of claim.
- Ticket 11 needs ticket 10's figures and checkpoint 1's labels; nothing else fixes the order.

## Done

- `.scratch/v5-paper/runs/10/result.txt`: status PASS, with the regeneration command for each
  figure in `evidence`.
- `.scratch/v5-paper/runs/11/result.txt`: status PASS, with the number-guard output and the
  compile result for both files in `evidence`.
- `.scratch/v5-paper/runs/batch-2/plan.md`, written before the first step, and
  `.scratch/v5-paper/runs/batch-2/result.txt` in the batch shape, `approach` included.
