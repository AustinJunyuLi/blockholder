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
- Verifier: no WRONG verdicts; 1 MISCITED (test needs `-m` invocation);
  3-filing independent audit all match. Ticket 09 committed: b026872.
- 09b builder dispatched (Sonnet): form-type rename filter, XML percentOfClass
  path, detag-before-label event-date fix, stale docstring, >100% guard.
- 09b builder done: 4 defects + a 5th stacked one (12-char slice truncated
  `SCHEDULE 13D/A` → merged amendments into originals) fixed; >100% guard
  added; 10/10 checks fail-old/pass-new.
- 09b verifier: 7 CONFIRMED, 1 WRONG — builder's form.idx counts were
  originals+amendments sums (true 2025Q1: SCHEDULE 13D=538, /A=2394; 2024Q3:
  18/18). Substance of the rename stands. Verifier also caught that the fix
  never reached production: `facts.py:48` passes explicit
  `form_types=("SC 13D",)`, overriding the fixed default → ~132 renamed
  filings still dropped in the 2024Q3-Q4 window. Retry-with-evidence
  dispatched: alias map inside `list_filings` (root fix, all callers at once).
- 09b retry: root fix — bidirectional alias map inside `list_filings`, so
  every caller (incl. facts.py's explicit tuple) gets both spellings; 11/11
  checks; recovered 18+114 renamed filings in 2024Q3/Q4. Fresh re-verifier:
  all 5 checks confirmed, regex swept 624k real idx lines with 0 drops,
  "nothing new" → fix round closed. Orchestrator also killed a stale
  filesystem-wide `find /` a verifier had left running (34 min, wasteful).
- Workflow note (per native-workflow evidence rule): ticket 09 + 09b used 5
  Sonnet agents (2 builders, 2 verifiers, 1 retry+1 re-verify counted in
  those); 1 retry-with-evidence round; verifiers caught 1 WRONG (sum-vs-exact
  counts) and 1 production-path miss (facts.py call site) — both fixed.
- Theory handoff check (pre-ticket-10 gate): fetched origin/v4-theory —
  `research/model_v4/HANDOFF_sign.md` ABSENT (branch is at thread-1 setup
  commits). Ticket 10 spec will use a marked placeholder for the slope sign,
  as the ticket allows.
