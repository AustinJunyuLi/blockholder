# Session note, v5 delivery (2026-09-02)

## What shipped

`deliverable/paper.pdf` (19 pages) and `deliverable/appendix.pdf` (27 pages), built from
`paper.tex`, `appendix.tex`, `paper.bib` and the proof files `proofs/04_inherited.tex`,
`proofs/02_garbling.tex`, `proofs/03_caught.tex`, `proofs/06_lemmas.tex`, with the figures under
`figures/` drawn by `numerical_v4/checks/figures.py` from the committed records. The number guard
(`empirics.test_fingerprints`, 26 tests) is green; the compile in the `CLAUDE.md` order has zero
errors, undefined references or citations; no Type 3 font; the unslop gate passed. The referee's
twenty items are marked fixed in `.scratch/v5-paper/referee_report.md`, verified in
`referee_report_2.md` (three reads).

## Every label

PROVED: partition and factorisation; flagged cell κ-invariance; the garbling lemma; the threshold
weight leg, the closed form of S_P and the implication in the threshold theorem; the clock dial;
who gets caught (identity and characterisation); the pricing root's uniqueness and continuity;
the window monotonicity of the stake at filing on paths flagged under both windows.
NUMERICAL: Condition D and the threshold composition conclusion on the grid κ in [0.15, 0.85],
mark 2, H 10, T 5, four adjacent pairs; directional who-gets-caught sentences off the five-node
record, each naming the degenerate T = 10 cell.
ESTIMATED: the two post-minus-pre differences of the stake at filing with their registered
bootstrap intervals.
ABSENT: existence (the paper carries no statement and no sentence about it; the calibration's
policy is the benchmark policy and is never called an equilibrium); E2 (gate E2-G1 NO-GO).

## STOPs

None.

## Record

Checkpoint notes: `.scratch/v5-paper/grok/checkpoint-0.md` to `checkpoint-3.md`. Batch plans
and results under `.scratch/v5-paper/runs/batch-1` to `batch-3` (gitignored, on this machine).
External input: `.scratch/v5-paper/external/gpt-sol-existence.md`, input not authority. The
theory-upgrade hunt under `.scratch/v5-paper/hunt/` belongs to a separate thread and is not part
of this delivery.
