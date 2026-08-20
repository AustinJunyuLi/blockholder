# Plan — Empirics lane, tickets 09–16 (2026-08-20)

**Status:** APPROVED (set via /goal by Austin)

## Goal
Work tickets 09–16 in `.scratch/v4-reposition/issues/`, in order, one at a
time. Fable orchestrates only (ADR-0005); every ticket gets fresh subagents
(Sonnet mechanical / Opus hard), a verifier who did not build, a commit on
`v4`, and a session-log line.

## Sequence
- **09 E1** parser fixes + assert checks + universe re-parse → verify → commit
- Before **10**: `git fetch origin v4-theory`, look for `HANDOFF_sign.md`;
  placeholder if absent
- **10 E2** empirical spec → **PAUSE: show Austin the spec before running anything**
- **11 E3** headline timing split → **12 E4** stake at filing → **13 E5**
  outcome coding → **14 E6** matched DiD bidder entry → **15 E7** run-up path
  figure → **16 E8** empirics section TeX
- Stop only when blocked on something only Austin can decide (logins, spec
  approval).

## Verification discipline (per ADR-0005 / native-workflow)
Finder ≠ verifier; verifiers refute (WRONG / MISCITED / UNCHECKED); executed
checks wherever one exists; one retry with evidence, then escalate
sonnet→opus; no silent losses.
