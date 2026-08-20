# 09 — E1 · Parser fixes with assert-based checks

**Lane:** empirics (`v4`, this machine)

**Routing:** per ADR-0005 — Sonnet for the edits and the checks (mechanical); Opus only if a fix does not hold and needs diagnosis; a separate agent runs the checks and the re-parse.

**What to build:** Three fixes to the 13D parser under `empirics/`, each shipped with a small assert-based check. The percent-of-class pattern matches two digits only and takes the first match on the page, so three-digit percents are truncated and the wrong reporting person's number can be picked up. The event-date handling is wrong for 2025 filings. The business-day arithmetic ignores federal holidays, which matters because the rule is written in business days. Then re-parse the whole filing universe.

**Blocked by:** None — this is the empirics lane's first ticket and everything downstream reads its output.

**Status:** done (2026-08-20) — re-parse deferred, see comments

- [x] Each of the three fixes has an assert-based check that fails on the old behaviour and passes on the new (5 checks in `empirics/test_parse_13d.py`; run as `.venv/bin/python -m empirics.test_parse_13d`)
- [ ] The universe re-parsed — **blocked, deferred**: raw filing texts are not cached on disk (only form.idx indexes + CRSP CSVs); a re-parse means re-downloading the universe. Not absorbed — see comments.
- [x] A hand audit of a sample of filings confirms the percent-of-class and event-date fields against the documents (builder: 12 filings; verifier: 3 more, independently sampled, all match)
- [x] A verifier who did not write the fixes runs the checks and matches (all claims CONFIRMED; one MISCITED: test invocation needs `-m`)
- [x] Session log entry and commit on `v4`

## Comments

- 2026-08-20 (Fable): all three bugs confirmed real before fixing. Real XML tag
  is `<dateOfEvent>` (the old `<eventDateRequiresFilingThisStatement>` does not
  exist in SEC schema). Percent fix = 3-digit cap + HTML detag + max across
  reporting persons. Holiday table 2021–2026 passed to `np.busday_count`.
- Hand audit surfaced 3 further parser bugs out of this ticket's scope, moved
  to addendum 09b (they block tickets 11/12): (i) EDGAR form-type rename
  `SC 13D`→`SCHEDULE 13D` ~2024Q3 — filter finds zero 2025 filings; (ii) no
  XML path for percent-of-class — None for 2025 filings; (iii) event-date
  label split across HTML tags in some pre-XML filings. Plus stale module
  docstring naming the old XML tag.
- 2026-08-20 (Fable, 09b close-out): all four addendum defects fixed + a 5th
  stacked one (hard 12-char slice truncated `SCHEDULE 13D/A` into originals).
  Root fix for the rename: alias map inside `list_filings`, so explicit
  caller tuples (facts.py) get both spellings. 11/11 checks; verifier caught
  the builder's form.idx counts being originals+amendments sums (true 2025Q1:
  538 SCHEDULE 13D + 2394 /A) and the facts.py call-site miss — both fixed
  and re-verified fresh ("nothing new").
- Committed `fact1_filings.csv` is all pre-XML (max date_filed 2024-12-16), so
  the XML event-date path is verified against live EDGAR fetches, not against
  committed pipeline output. Full re-parse to be bundled with the next ticket
  that needs fresh data (11/12), where the download is paid for once.
