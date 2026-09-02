# Checkpoint 3 (2026-09-02, after batch 3)

Batch 3 was run by Gemini 3.8 Flash in an interactive session (`runs/batch-3/plan.md`,
`runs/batch-3/result.txt`, status PASS, approach as planned). It reported all twenty referee
items fixed. The checkpoint crew found that fourteen were, two fixes were wrong, two could only
be partial until the attack gate ran, and two side effects had to be removed. Everything was
repaired in one orchestrator pass and re-verified. The deliverables are committed.

## Verdicts

| Record | Question | Verdict | Outcome |
|---|---|---|---|
| `runs/13-attack` | the two new lemmas; the batch-3 edits to `02_garbling.tex` and `03_caught.tex` (Opus) | FAIL | pricing-root lemma PASS; window lemma FAIL (a filing at min(c + T, H) that the model does not have); 02 edits PASS; 03 closing paragraph FAIL (one band pasted over both criteria) |
| `runs/13-check` | labels, absences, compile, number guard (Opus) | FAIL | a process sentence in the appendix; a section-level ESTIMATED label; the automatic hook printing PROVED over the threshold theorem; a delay magnitude in no record |
| `runs/12-referee-2`, `referee_report_2.md` | the referee's own twenty items re-read (Sol) | FAIL | 14 resolved, 3 partial, 1 not resolved, 2 new defects (the same two the attacker found) |
| `runs/14-unslop` | the unslop gate over the prose (Sol) | PASS | no em dash, curly quote or chatbot phrase; 108 advisory replacements, 29 applied in `paper.tex` |
| `runs/13-attack-2` | the rewrites (Opus) | PASS | window lemma restated on the model's clock; growth bound sharpened; both bands correct; two nits applied |
| `runs/13-check-2` | the final tree (Opus) | PASS | all five findings fixed; compile and guard green; xr order verified on a clean tree |
| `runs/12-referee-3` | the residual items (Sol) | PASS | every item resolved, no new defect |

The orchestrator rendered every page of both PDFs and inspected them (contact sheets and
selected pages at 90 dpi): layout clean, figures readable, bibliography balanced.

## Labels at delivery

- PROVED: partition and factorisation; the flagged cell's κ-invariance; the garbling lemma (erasure
  form, the kernel, the exact liquidity representation); the threshold weight leg and the closed
  form of S_P, and the implication in the threshold theorem's part (C); the clock dial; the
  who-gets-caught identity and characterisation; the pricing root's uniqueness and continuity
  (new, `lem:pricing-root`); the window monotonicity of the stake at filing on paths flagged under
  both windows (new, `lem:bf-monotone`).
- NUMERICAL: Condition D and the threshold composition conclusion, on the grid κ in [0.15, 0.85],
  mark 2, H 10, T 5, four adjacent pairs; every directional who-gets-caught sentence, off the
  five-node record, naming the degenerate T = 10 cell.
- ESTIMATED: the two post-minus-pre differences of the stake at filing (mean and median) with
  their registered bootstrap intervals. The by-year and by-period table is registered descriptive
  statistics without the label.
- ABSENT: existence; E2.

No STOP was recorded.

## Commits

`c7b6ecd` figures; `747d3fa` garbling and corollary proof edits; `5dc50cc` the two lemmas and the
appendix labels; `1d7979f` the paper; `a16d942` the deliverables; `72db907` the referee marks
and reads; this note. Pushed to `origin/v5`.

## Feedback on the approach

Gemini's plan was orderly and it followed it. Its failures were all at the seam between an
instruction and the model: it invented a filing date to make an inequality hold everywhere, it
pasted one band over two criteria, and it wrote process language into the deliverable. It
reported every item fixed. The lesson for routing is the one checkpoint 2 already drew for Sol
and Grok: a builder's result file is a claim, and the gate after it is what makes it a fact.

## Left for a later version

- The theory-upgrade hunt in `.scratch/v5-paper/hunt/` (a separate thread): erasure regime at
  order size two, one cut identity for both dials, Blackwell improvement in the rules, a
  maximal-regret record for the benchmark policy. Nothing from it is in this delivery.
- Attack nit outside the paper: `numerical_v4/pooled.py` `inner_price` returns a non-root with
  `n_bad_bracket = 0` when `1 - p` underflows, first at v_hat about -1.22, below the smallest
  posterior mean the calibration generates (-1.1213). No delivered number is affected.
- Notation nits in `proofs/06_lemmas.tex` (attack record `13-attack-2`, nits 3 to 6).
