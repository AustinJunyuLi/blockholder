# Batch 2

Effort `xhigh`. Read `README.md`, then `checkpoint-1.md`. Write `runs/batch-2/plan.md` before the
first step.

## Objective

When the batch ends, all of these hold.

- Step 0 of `checkpoint-1.md` is applied: the wording nits in `proofs/04_inherited.tex` and
  `proofs/03_caught.tex`, the record fields in `numerical_v4/checks/t5_who_gets_caught.py`, and
  `PYTHONPATH=. .venv/bin/python -m empirics.test_fingerprints` is green with both audits on disk
  while still guarding that the runner leaves G2 to the audit.
- `figures/` holds the figures ticket 10 names that have a record behind them: Figure 1 from the
  T1 record, Figure 2 from the who-gets-caught record, and the E1 figure; each a PDF, each
  regenerating from a command the report lists, and each showing only cases the paper's results
  cover. There is no E2 figure.
- `paper.tex`, `appendix.tex` and `paper.bib` exist in the structure ticket 11 states. They
  compile in the order `CLAUDE.md` gives with zero errors, zero undefined references and zero
  undefined citations; the number guard is green; every theorem in `paper.tex` has its proof in
  `appendix.tex` and carries the label `checkpoint-1.md` records for it; every number renders from
  the E1 result file or a grid record.

## Inputs

- Tickets `.scratch/v5-paper/issues/10-figures.md` and `.scratch/v5-paper/issues/11-paper-writer.md`.
- `checkpoint-1.md`: the label each result holds, step 0, and the label scope carried forward
  from `checkpoint-0.md`.
- Grid records: `numerical_v4/checks/t2_t1_check.json` (T1, the κ profiles and the run-up share
  sweep), `numerical_v4/checks/t5_who_gets_caught.json` (the corollary at five nodes),
  `numerical_v4/checks/t2_threshold_revelation_check.json` (Condition D),
  `numerical_v4/checks/t2_l4_check.json` (the weight leg). All at mark 2, H 10, hash
  `fbacc963f39422c3`.
- `empirics/output/e1_estimate.json` with its gates and clock block. `empirics/output/e2_estimate.json`
  exists and reads NO-GO; nothing in the paper renders from it.
- The proofs under `proofs/`: `02_garbling.tex`, `03_caught.tex`, `04_inherited.tex`, which
  `appendix.tex` assembles. `05_existence.tex` is not assembled.
- `docs/brief_2026-09-01_referee.md` as input to the rewrite, and the inherited draft's prose
  where it still holds, never cited.

## Constraints

- Paths: `proofs/03_caught.tex` and `proofs/04_inherited.tex` for step 0 only;
  `numerical_v4/checks/t5_who_gets_caught.py`; `empirics/test_fingerprints.py`; `figures/`;
  `numerical_v4/checks/figures.py`; `empirics/fingerprints.py` for figure style only; `paper.tex`,
  `appendix.tex`, `paper.bib`; and the run directories `step0`, `10`, `11` and `batch-2` under
  `.scratch/v5-paper/runs/`.
- Labels, as `checkpoint-1.md` records them. PROVED: partition and factorisation, the flagged
  cell's κ-invariance, the garbling lemma, the threshold weight leg and the closed form of S_P,
  the clock dial, the who-gets-caught identity and characterisation. NUMERICAL: the threshold
  composition leg on the grid κ in [0.15, 0.85], mark 2, H 10, and any directional
  who-gets-caught sentence off the five-node record, which names the degenerate T = 10 cell at
  the point of claim. ESTIMATED: E1.
- Existence is absent: no existence statement and no sentence about it. The calibration policies
  are the solver's baseline cutoffs; the paper states results at fixed policies and does not call
  the calibration an equilibrium.
- E2 is absent: no E2 number, figure or sentence. E1 is not rerun.
- The threshold theorem's headline: the weight effect by proof, the composition effect on the
  calibration grid; Condition D is the conclusion restated (C_τ at most one), so the paper
  presents it as what the grid verifies, not as a condition on primitives.
- The grid a NUMERICAL claim rests on is named at the point of claim.
- Step 0 precedes the paper; ticket 11 needs ticket 10's figures; nothing else fixes the order.

## Done

- `.scratch/v5-paper/runs/step0/result.txt`: status PASS, with the test-suite output in `evidence`.
- `.scratch/v5-paper/runs/10/result.txt`: status PASS, with the regeneration command for each
  figure in `evidence`.
- `.scratch/v5-paper/runs/11/result.txt`: status PASS, with the number-guard output and the
  compile result for both files in `evidence`.
- `.scratch/v5-paper/runs/batch-2/plan.md`, written before the first step, and
  `.scratch/v5-paper/runs/batch-2/result.txt` in the batch shape, `approach` included.
