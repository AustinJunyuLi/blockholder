---
name: verify-blockholder
description: Full deterministic verification of the blockholder JMP pipeline — data, figures, both LaTeX compiles, D7/D8 derivation checks. Use before any commit, before claiming a revision complete, and in scheduled readiness runs. Pass FAST=1 to skip the 10-minute D8 sweep.
---

# Verify blockholder

Run all gates from the repo root. Every gate is PASS/FAIL. Report a table of
gate → result → evidence (log line or file count). Overall PASS requires all
gates green. Never claim success on partial evidence.

## Gates

1. **Data**: `make data` exits 0 AND exactly 16 CSVs exist in
   `numerical_output/data/`. (~10 min)
2. **Figures**: `make figures` exits 0 AND 19 PDFs exist (15 manuscript +
   4 slide variants). (~2 min)
3. **Manuscript compile**: `xelatex draft_v2.tex && biber draft_v2 && xelatex
   draft_v2.tex` — assert in the log: 0 errors, 0 "undefined references",
   0 citation warnings. (~5 min)
4. **Presentation compile**: same sequence in `pres/` for
   `presentation.tex` — same assertions. (~3 min)
5. **D7 check**: `.venv/bin/python quality_reports/fixes/d7_takeover_game_check.py`
   → JSON `all_pass: true`, MC-vs-closed-form err < 1e-3. (~1 min)
6. **D8 check** (skip when FAST=1):
   `.venv/bin/python quality_reports/fixes/d8_ge_dominance_check.py`
   → JSON `all_pass: true`, certified region ⊇ [0.35, 0.825]. (~10 min)

## Failure protocol

On any gate failure: stop, show the failing log excerpt, do NOT attempt fixes
inside this skill — report and hand back to the caller.
