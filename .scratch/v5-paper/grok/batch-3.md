# Batch 3

Effort `xhigh`. Read `README.md`, then `checkpoint-2.md`. Write `runs/batch-3/plan.md` before the
first step.

## Objective

When the batch ends, all of these hold.

- Every item in `.scratch/v5-paper/referee_report.md` is marked in that file as fixed, with the
  fix named, or as STOP, with the reason. Blocking items 1, 2, 3, 5, 6, 7, 8 and 10 and every
  minor item are fixes; blocking item 4 is fixed by two short lemmas (the pricing root's
  uniqueness and continuity in the posterior summaries; the stake at filing weakly increasing in
  the window at fixed policies) written into the appendix with full hypothesis lists in the
  numbering of the standing conditions, and by either a record field for the calibration
  sentence on B^F or its deletion; blocking item 9 is fixed as checkpoint 2 decides the ESTIMATED
  scope.
- The two lemmas carry no label until the orchestrator's attack gate returns; the paper's
  sentences that rest on them cite the lemma and no label until then.
- `paper.tex` and `appendix.tex` compile in the order `CLAUDE.md` gives with zero errors, zero
  undefined references and zero undefined citations, and the number guard is green.
- Every page of both PDFs has been rendered and inspected, and the inspection note lists what it
  found and what was fixed, including the production items (fonts embedded as Type 42 or Type 1,
  no orphan words at page tops, Figure 2 labels readable at print size).
- `deliverable/paper.pdf` and `deliverable/appendix.pdf` are the compiled PDFs.

## Inputs

- Tickets `.scratch/v5-paper/issues/13-author-fix.md` and
  `.scratch/v5-paper/issues/14-compile-and-deliver.md`.
- `.scratch/v5-paper/referee_report.md`: ten blocking items and ten minor items, each with a
  location; the checks with no finding at its end.
- `checkpoint-2.md`: the label each result holds, the triage of the referee items, the decisions
  taken on the ESTIMATED scope, the framing, the public Q^F and the two lemmas.
- `.scratch/v5-paper/external/gpt-sol-existence.md`, section B only, as input to the framing;
  never cited.
- The records the paper renders from, unchanged: `empirics/output/e1_estimate.json` and the grid
  records under `numerical_v4/checks/`.

## Constraints

- Paths: `paper.tex`, `appendix.tex`, `paper.bib`, `proofs/02_garbling.tex` and
  `proofs/03_caught.tex` for the hypothesis clauses, the informal sentence and the stale comment
  the referee names, a new `proofs/06_lemmas.tex` for the two lemmas, `figures/` and
  `numerical_v4/checks/figures.py` for the figure fixes, `deliverable/`,
  `.scratch/v5-paper/referee_report.md` for the fixed or STOP marks, and the run directories
  `13`, `14` and `batch-3` under `.scratch/v5-paper/runs/`.
- A blocking item that needs a new run is a STOP, recorded with its reason. Items that do not
  depend on it are still fixed.
- Labels stay as checkpoint 2 records them. PROVED: partition and factorisation, the flagged
  cell's κ-invariance, the garbling lemma, the threshold weight leg and the closed form of S_P,
  the clock dial, the who-gets-caught identity and characterisation. NUMERICAL: the threshold
  composition leg on the grid κ in [0.15, 0.85], mark 2, H 10, T 5, four adjacent pairs;
  directional who-gets-caught sentences off the five-node record, naming the degenerate T = 10
  cell. ESTIMATED: as checkpoint 2 scopes it. A referee item that argues a label goes to the
  orchestrator as a STOP.
- Existence and E2 stay absent. The calibration's policy is the benchmark policy and is never
  called an equilibrium. The clock pair (10, 5) is in trading rounds and is a model comparison,
  not the reform; the calibration is not changed.
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
