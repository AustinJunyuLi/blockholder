# 09 — E1 · Parser fixes with assert-based checks

**Lane:** empirics (`v4`, this machine)

**Routing:** per ADR-0005 — Sonnet for the edits and the checks (mechanical); Opus only if a fix does not hold and needs diagnosis; a separate agent runs the checks and the re-parse.

**What to build:** Three fixes to the 13D parser under `empirics/`, each shipped with a small assert-based check. The percent-of-class pattern matches two digits only and takes the first match on the page, so three-digit percents are truncated and the wrong reporting person's number can be picked up. The event-date handling is wrong for 2025 filings. The business-day arithmetic ignores federal holidays, which matters because the rule is written in business days. Then re-parse the whole filing universe.

**Blocked by:** None — this is the empirics lane's first ticket and everything downstream reads its output.

**Status:** ready-for-agent

- [ ] Each of the three fixes has an assert-based check that fails on the old behaviour and passes on the new
- [ ] The universe re-parsed; row counts before and after reported, and every difference explained rather than absorbed
- [ ] A hand audit of a sample of filings confirms the percent-of-class and event-date fields against the documents
- [ ] A verifier who did not write the fixes runs the checks and the re-parse and matches
- [ ] Session log entry and commit on `v4`

## Comments
