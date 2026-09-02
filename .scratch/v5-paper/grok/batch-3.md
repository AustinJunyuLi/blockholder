# Batch 3

Effort `high`. Read `README.md`, then `checkpoint-2.md`. Text in angle brackets is the
orchestrator's to fill from checkpoint 2; the brief is final when none is left.

## Objective

When the batch ends, all of these hold.

- Every item in `.scratch/v5-paper/referee_report.md` is marked in that file as fixed, with the
  fix named, or as STOP, with the reason.
- `paper.tex` and `appendix.tex` compile in the order `CLAUDE.md` gives with zero errors, zero
  undefined references and zero undefined citations, and the number guard is green.
- Every page of both PDFs has been rendered and inspected, and the inspection note lists what it
  found and what was fixed.
- `deliverable/paper.pdf` and `deliverable/appendix.pdf` are the compiled PDFs.

## Inputs

- Tickets `.scratch/v5-paper/issues/13-author-fix.md` and
  `.scratch/v5-paper/issues/14-compile-and-deliver.md`.
- `.scratch/v5-paper/referee_report.md`: `<the blocking items and the minor items>`.
- `checkpoint-2.md`: the label each result holds and what the checker's pass settled.

## Constraints

- Paths: `paper.tex`, `appendix.tex`, `paper.bib`, `figures/`, `deliverable/`,
  `.scratch/v5-paper/referee_report.md` for the fixed or STOP marks, and the run directories
  `13`, `14` and `batch-3` under `.scratch/v5-paper/runs/`.
- A blocking item that needs a new theorem or a new run is a STOP, recorded with its reason.
  Items that do not depend on it are still fixed.
- Labels stay as checkpoint 2 records them: `<the label of each result>`. A referee item that
  argues a label goes to the orchestrator as a STOP.
- Every number keeps rendering from its result file, and the unslop gate applies to the prose
  one last time: plain words, no em dashes, nothing about earlier versions or attempts.
- Ticket 14 needs ticket 13's fixes; nothing else fixes the order.

## Done

- `.scratch/v5-paper/runs/13/result.txt`: status PASS or STOP, with the marked report and the
  number-guard output in `evidence`.
- `.scratch/v5-paper/runs/14/result.txt`: status PASS, with the compile log excerpt and the
  page-by-page inspection note in `evidence`.
- `.scratch/v5-paper/runs/batch-3/plan.md`, written before the first step, and
  `.scratch/v5-paper/runs/batch-3/result.txt` in the batch shape, `approach` included.
