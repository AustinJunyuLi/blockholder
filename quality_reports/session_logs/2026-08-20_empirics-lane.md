# Session log — 2026-08-20 — Empirics lane (tickets 09–16)

**Goal:** run tickets 09–16 in order, fresh subagents per ticket (ADR-0005),
commit + log after each, theory-handoff check before 10, pause after 10 for
Austin's spec approval. Plan:
`quality_reports/plans/2026-08-20_empirics-lane-tickets-09-16.md`.

## Ticket 09 — E1 parser fixes
- Dispatched: Sonnet builder (3 parser fixes + assert checks + re-parse),
  then a fresh verifier.
- Builder done: all 3 bugs confirmed + fixed (percent regex 3-digit + max
  across persons + HTML detag; event-date XML tag was wrong — real tag is
  `<dateOfEvent>`; federal-holiday table added to busday_count). 5 checks
  fail-old/pass-new. 12-filing hand audit. Universe re-parse BLOCKED: raw
  filing texts are not cached on disk (only form.idx + CRSP CSVs) — re-parse
  means re-download; deferred, not absorbed.
- Builder surfaced 3 extra parser bugs out of ticket scope: (i) EDGAR renamed
  form type `SC 13D`→`SCHEDULE 13D` ~2024Q3 → current filter finds ZERO 2025
  filings; (ii) percent-of-class has no XML path → None for 2025 filings;
  (iii) event-date label split across HTML tags in some pre-XML filings.
  Decision (Fable): (i) and (ii) block downstream tickets 11/12 — fix as a
  09b addendum after 09 verifies, before moving on. (iii) lower priority,
  bundled into 09b.
