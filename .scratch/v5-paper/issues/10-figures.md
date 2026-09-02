# 10 · Figures at order size two

**Lane:** theory code and empirics. **Routing:** Grok in batch 2.
**Blocked by:** 01, 06, 08. **Blocks:** 11.

**What to build.** Figure 1: noise sensitivity S and its two factors against κ under the two
clocks at the calibration, from the mark-2 T1 record, with no gap in the κ grid and a title that
matches what the figure shows. Figure 2: the who-gets-caught grid record (condition holds, C_T ≤ 1)
across nodes. Figure 3 and 4 come from the E1 and E2 result files (already produced by the runs;
this ticket only checks style and labels). All figures under `figures/` as PDF, produced by a
script under `numerical_v4/checks/figures.py` or `empirics/fingerprints.py`.

**Acceptance.**
- [ ] Each figure regenerates from a command listed in the report.
- [ ] No figure shows a case the paper's theorems do not cover.

**Status:** closed at checkpoint 2 (commit eb4a03b; audited in `runs/batch-2/audit-step0-figures.md`). Was: open; Grok batch 2. E2 is NO-GO (checkpoint 1), so the E2 figure is absent; the figures are Figure 1 (T1 record), Figure 2 (who-gets-caught record) and the E1 figure.

## Comments
