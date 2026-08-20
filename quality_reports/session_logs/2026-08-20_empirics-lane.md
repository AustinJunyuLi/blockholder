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

## Ticket 10 — E2 pre-specified empirical design
- Sonnet inventory done → `research/empirics_v4/data_inventory.md`: 9,234
  parsed 13D originals 2022–2025 (but built with the OLD parser — 2025 event
  dates ~0% parsed, renamed 2024Q3+ filings missing → re-fetch+re-parse is a
  flagged pull), CRSP daily 2021–2025 (11.88M rows), WRDS CARs for 2,285 of
  3,518 events. Gaps: no CIK→CUSIP link code in repo; takeover premium has no
  free source.
- Opus spec writer dispatched → `research/empirics_v4/SPEC.md`; slope sign as
  marked placeholder (handoff absent), both branches specified. Opus verifier
  next, then commit, then PAUSE for Austin.
- SPEC.md written (1,078 lines, one-page summary + §0–§13). Design choices the
  writer made and the reason each:
  - **H1 is sign-free.** The partition test (run-up carries the liquidity
    slope, filing-day jump does not) needs no handoff, so the headline is not
    hostage to the theory lane. H2 (the post-2024 slope change) carries the
    placeholder with BOTH branches written out. One check refutes the paper's
    identity either way: if the jump moves with liquidity like the run-up
    does, there is no partition.
  - **RUNUP5 (fixed 5-trading-day window from the trigger) is primary for the
    before/after test**, because RUNUP's length changes mechanically at the
    reform AND because Polk et al.'s own Table 1 vs Table 3 gap (3.80% pooled
    vs 5.09% at Delta=10) shows the delay cross-section is composition, not a
    window effect.
  - **Post is assigned on the TRIGGER date, not the filing date** (the
    deadline attaches to the crossing); straddlers excluded and counted.
  - **Pre window ends at ADOPTION (2023-10-10), not at the effective date**,
    for anticipation. NB those two dates are second-hand from P4 — open item 13.
  - **`Post` is collinear with year-quarter FE**, so γ is unidentified in the
    CAR regressions; §5 (stake level) drops YQ FE and uses a trend instead.
    Caught in pre-specification, which is the point.
  - **Bounded null written as a three-rung LADDER** from SEC Table 3 p. 189
    (20 pp / 3 pp / 1 pp), because "3 pp" is a judgement about what counts as
    a materially cut campaign, not a number the SEC computed.
- **The finding that matters and was not anticipated by the ticket:** the
  matched DiD's best MDE (4.4 pp after the re-parse; 9.8 pp on the ~20%
  non-corporate-action subset) is LARGER than the 3 pp bounded null. The
  design cannot separate the accumulation effect from zero even at its own
  ceiling — it can only rule out a large effect. Written into §6 and §8.6 as
  the leg's headline sentence before any estimate exists.
- Card facts that CORRECTED the position documents (all now in the spec):
  (i) Brav et al.'s Amihud −0.075 [t=−3.99] is a matched-sample MEAN
  DIFFERENCE, not a regression coefficient, and Amihud appears in no estimated
  equation in that paper; (ii) Greenwood–Schor is 18.1% treated / 7.2% matched
  control (Table 6 p. 372) with NO standard errors and three inconsistent
  counts in the paper; (iii) Trivedi's +0.348 (t=2.69) is the SECONDARY
  outcome — his primary (mean calendar-day lag) is null, p=0.63;
  (iv) BBJJ's days→stake gradient is 0.06 pp/day and NEGATIVE, so the reform's
  mechanical accumulation effect (~0.12 pp) is a quarter of our 0.65 pp MDE;
  (v) BJPT: activist targets pile into the THIRD liquidity quintile (43.4%),
  so our LIQ variation is compressed vs the CRSP universe.
- Opus verifier (did not write spec): all 5 card corrections HOLD (quoted from
  cards); manifest 100% pass vs disk (every DISK row + 3 coverage claims
  exact); arithmetic reproduces except two BLOCKING items → retry round sent
  to writer: (1) §2.1 counts computed on filing date but labelled trigger-date
  → §3.6's w is 0.230 not 0.269; (2) stake MDE used N≈8,000 vs the spec's own
  ~4,950 → 0.83 pp clustered, not 0.65. Six non-blocking fixes sent too.
- SEC dates CLOSED against the release (curl, live): adopted 2023-10-10 ✓,
  effective 2024-02-05 ✓, XML mandate 2024-12-18 ✓ (card's 2023-12-18 was the
  voluntary date); proposal was 2022-02-10 (2022-03-10 is the Federal Register
  publication). Open items 13.x downgraded accordingly.
- Two dates flagged UNVERIFIED against the SEC release: proposal/adoption
  (2022-03-10 / 2023-10-10, second-hand from P4) and the structured-XML
  mandate (2024-12-18, from the feasibility doc — the institutional card has
  only "voluntary compliance … December 18, **2023**"). Both are blocking for
  ticket 11 because the sample window is cut on them.
- Ticket 10 verifier round (independent Opus, cards + disk + arithmetic + live
  SEC release). 2 blocking, 6 non-blocking; all 8 applied to SPEC.md.
  - **BLOCKING 1 — the split bug.** §2.1's count table was headed "Pre/Post
    (TD ...)" but every cell was computed on `date_filed`, while §2.5 assigns
    Post on the TRIGGER date. Reproduced the verifier's numbers exactly:
    TD split 3,586/1,052 (with CUSIP 3,000/897), so **w = 0.230, not 0.269**.
    Trigger-year is 1,550/1,616/1,199 (not the filing-year 1,580/1,660/1,398),
    plus 273 filings with triggers dated 2014–2021 and 183 straddlers. Table
    now shows BOTH splits, labelled, with the TD one marked as the design's.
    Every downstream number recomputed and re-verified in-session: timing
    split 1.28/1.60 today (was 1.21/1.52), 0.98/1.22 after re-parse; DiD
    5.8/4.4/9.9 pp (was 5.5/4.4/9.8). Headline conclusion unchanged — the
    DiD's best MDE (4.4 pp) still exceeds the 3 pp bound.
  - **BLOCKING 2 — stake MDE sample.** Used N≈8,000 (filings with a parsed
    stake), but Post needs a parsed trigger date, so N is the ~4,950 trigger
    sample. Corrected to SE 0.233 → **MDE 0.65 pp raw, 0.85 pp clustered**
    (was 0.65 clustered). Still ~7× the 0.12 pp mechanical gradient, so the
    argument survives; §5, §10 row 4 and §12 updated.
  - Non-blocking: proposal date is **2022-02-10** (Release 33-11030) — the
    2022-03-10 in P4 is the Federal Register date; adoption 2023-10-10 and
    effective 2024-02-05 both CONFIRMED, so open item 13 CLOSED (nothing is
    cut on the proposal date). Structured-data mandate **2024-12-18 CONFIRMED**
    in release §II.G (the card's 2023-12-18 is the voluntary date) → open item
    14 CLOSED. Trivedi's Amihud null relabelled "uninformative" (no MDE, no
    CI) not "precise". §3.6's 1.1–2.3 pp range now says which series each end
    comes from (JUMP low, RUNUP high). §8.7 placebo day count stated with its
    convention: **568 holiday-adjusted** (593 raw weekdays), computed from the
    repo's own `FEDERAL_HOLIDAYS` table — verifier said 570; I print the
    reproducible number and the command. §3.5's collinearity clause now
    carries the qualifier that it is false in §2.6's robustness sample, where
    2024Q1 holds both regimes.
- Retry round closed: writer applied all 8 fixes (reproduced TD counts
  independently first: 3,586/1,052, w=0.230); recomputed MDEs — timing
  1.28/1.60 pp today, 0.98/1.22 post-re-parse; DiD 5.8/4.4/9.9; stake
  0.65/0.85 on N≈4,950. Re-verify by the same (independent) verifier:
  everything reproduces, NOTHING NEW; verifier conceded its own stake-SE
  (stale w) and day-count (568 is repo-reproducible) arithmetic.
- Workflow note (ticket 10): 1 Sonnet inventory + 1 Opus writer + 1 Opus
  verifier, 1 retry round; verifier caught 2 blocking errors (filed-vs-trigger
  split mislabel, stake N) and closed 2 unverifiable dates against the SEC
  release; writer won 2 arithmetic disputes on re-check.
- Ticket 10 committed. PAUSED for Austin: spec approval required before any
  estimation (ticket 11+).
