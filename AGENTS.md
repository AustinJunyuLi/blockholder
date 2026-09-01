# AGENTS.md

`CLAUDE.md` is the canonical repository contract. Read it before substantive work.

One branch, `v4`, one worktree. `CONTEXT.md` is the glossary; use its vocabulary and its honesty
labels exactly.

## Rules needed on every task

- Preserve `research/model_v4/` and `sections_v3/` byte-for-byte. `MODEL_CARD.md` is the frozen
  theory authority. A theory-level defect stops the affected draft section and goes to Austin.
- E1 is the only empirical exercise. Its registered specification is
  `research/empirics_v4/e1_spec.md` and its single result authority is
  `empirics/output/e1_estimate.json`. Correct the spec with a dated amendment inside the file.
- E1 is descriptive. Make no causal claim from the before-after timing comparison.
- The August empirical record was deleted on 2026-09-01 and lives in history at `9b98089`.
  The same day's manuscript revision stripped those citations from `draft_v3`; the online
  appendix preserves the record exactly as viewed (`app:honesty`).
- The orchestrator owns git. Workers edit only assigned paths, preserve concurrent work, run no
  git, and report exact changes.

## Build gates

```bash
.venv/bin/python -m numerical_v4.smoke
PYTHONPATH=. .venv/bin/python empirics/test_e1.py
PYTHONPATH=. .venv/bin/python empirics/test_parse_13d.py
make clean && make all
xelatex -interaction=nonstopmode draft_v3.tex && biber draft_v3 && \
  xelatex -interaction=nonstopmode draft_v3.tex && xelatex -interaction=nonstopmode draft_v3.tex
xelatex -interaction=nonstopmode draft_v3_onlineappendix.tex
xelatex -interaction=nonstopmode draft_v3_onlineappendix.tex
```

Run applicable committed `t2_*` checks for `numerical_v4` changes. TeX delivery also requires zero
undefined references or citations and visual inspection of both PDFs.
