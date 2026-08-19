# Plan — Peer review of framework_v3 (angle, model, empirics) + edits

**Status:** COMPLETED 2026-08-19 (was APPROVED — user instruction 2026-08-19: "spin deep research workflow ... act as a journal
peer reviewer ... make edits"). Autonomous run; user not watching live.
**Delegation mode:** team of parallel `Agent` calls (user preference: not the dynamic Workflow
tool). Ceiling 12 agents; models set explicitly; finder ≠ verifier; adversarial verification.

## Goal
Referee framework_v3.qmd/pdf as a JF/RFS reviewer would: originality, positioning in the
literature, model validity (3-branch model, T2/T4/T5 proof plan), empirical design (F1–F4,
H1–H3, calibration table). Then edit framework_v3.qmd where the review finds real problems,
re-render framework_v3.pdf, and deliver a referee report.

## Stage A — 5 finders (parallel, background)
| id | model | scope | output |
|---|---|---|---|
| A1 theory-referee | opus | model consistency, T2 decomposition, τ primitive, Hold prune, bidder info set, D8 bound reuse, isomorphism claim | research/review_v3/theory_referee.md |
| A2 lit-positioning-referee | opus | positioning claims, quotes vs Back et al 2018 / Burkart–Lee 2022, "first formalization"/"nobody links" claims, frontier citations exist? | research/review_v3/lit_referee.md |
| A3 novelty-scan | opus | SSRN/Scholar/NBER scan for Feb-2024 13D shock papers and disclosure×liquidity×premia theory 2023–26 (ego-browser) | research/review_v3/novelty_scan.md |
| A4 empirics-referee | opus | identification of H1–H3, confounds, sample arithmetic vs repo data, spec fixes | research/review_v3/empirics_referee.md |
| A5 facts-verifier | sonnet | every number/citation in the qmd vs primary sources: WRONG/MISCITED/UNCHECKED | research/review_v3/facts_verification.md |

## Stage B — 2 verifiers (after A)
| B1 | opus | refute A1's substantive theory findings against draft_v2.tex/D7/D8 |
| B2 | opus | refute A2/A3/A4 factual claims + re-check A5's WRONG verdicts |

## Stage C — synthesis + edits (orchestrator)
- Referee report → quality_reports/reports/2026-08-19_framework_v3_referee_report.md
- Edit framework_v3.qmd (only for confirmed findings; honesty labels never weakened)
- `quarto render framework_v3.qmd` → framework_v3.pdf; sync framework_v3.md
- Optional B3 (sonnet): re-verify new claims introduced by the edits.

## Verification steps
- Each B verifier reports WRONG / MISCITED / UNCHECKED per claim, with evidence.
- quarto render exits 0; PDF opens; page count sane.
- Session log updated incrementally.
