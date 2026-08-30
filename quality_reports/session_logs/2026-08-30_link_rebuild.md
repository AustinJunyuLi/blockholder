# Session log — 2026-08-30 — CIK→CUSIP→PERMNO link rebuild + never-13D control universe

**Lane:** SPEC §11 rows 11/23 (§13 item 3, BLOCKING for the DiD). **Agent:** Mac-side
subagent (this session). **Constraint honoured:** nothing committed by this lane; all
work products left uncommitted for orchestrator review (the two output CSV triples are
untracked; `research/empirics_v4/link_rebuild_2026-08-30.md` is new).

## What happened, in order

1. Read SPEC §8.2/§11/§13 + feasibility §5.7; probed the on-disk assets. Established
   the snapshot's key defect: **CRSP header fields are current-only** — every PERMNO
   with an identified header (EQTY/FUND) trades through 2025-12-31, and the 3,407
   "X-stub" PERMNOs (no ticker, blank ShareType/SecurityType) are exactly the
   delisted securities. A last-row common-stock filter yields 3,827 and drops every
   acquired firm.
2. Wrote `empirics/link_cik_cusip.py` + `empirics/build_control_universe.py`
   (v1, last-row identity), smoke-tested the matcher on synthetic collisions
   (class shares, ticker reuse, IPO-after-filing, name fallback), started the
   submissions fetch (~2,950 docs cached).
3. **Mid-session multi-agent convergence** (see `2026-08-30_migration_note.md`):
   commit `362f038` harvested this tree's uncommitted files; the E4 lane rewrote
   `link_cik_cusip.py` after its v1-style run scored the validation gate at 0.7301,
   diagnosing identity-vintage mismatch. Committed E4 version (`906128b`): ticker
   join against full ticker history (18,654 spans), validation against full CUSIP
   history (16,692 spans), ever-flags universe (5,443). **Gate PASSED: 0.9522
   (896/941).** Verified the committed outputs on disk match the run log.
4. Updated `build_control_universe.py` to the E4 identity machinery
   (`build_crsp_identity`, ticker spans, CUSIP history) and added accession
   deduplication after the re-parse report (§0) found EDGAR double-lists every 13D
   (confirmed in the 2021 idx files: 3,101 rows → 1,557 unique filings).
5. **Process management:** killed PID 47079 — an orphaned duplicate of
   `build_control_universe` (v1 code, PPID 1, zero CPU, no sockets, starved at the
   lock). Justification: it would have produced last-row-identity outputs and
   double-fetched ~1,557 filings; killing a polling process leaks nothing. Documented
   here per transparency. My own first run (PID 53804) was stopped for the dedup
   patch; a later run (PID 73476) was SIGTERMED at ~22 min (background-task lifetime
   cap) after caching 1,411/1,557 texts; the resume completed.
6. SEC lock discipline: every fetch phase under `/tmp/sec_edgar_bulk.lock`; the BID12
   lane (`empirics.bid12 extract-treated`, PID 29378) held it in batches — polled at
   60 s, never touched its holds. All responses cached; re-runs are network-free.

## Realised numbers (full write-up: `research/empirics_v4/link_rebuild_2026-08-30.md`)

- Link: 1,019/2,735 subject CIKs matched (37.3%); validation gate **0.9522** on
  n=941 (PASS); 45 disagreements with mechanical reasons preserved.
- Reverse map: 5,212/5,443 common-US PERMNOs → CIK (95.8%); spot-check 300/300.
- Control universe: pool 5,443 − excluded 1,843 = **3,600 PERMNOs** (2,480 listed /
  1,120 delisted). 2021 gap contributed +340 exclusions no other route catches.
- Amendment contamination: 28.2% of sampled 13D/A subjects have no in-window
  original; 52.8% of those reach the pool; upper-bound residual ~3,200 pool PERMNOs.
  **Flagged as the material caveat** with a ~90-min bulk-fetch remediation costed.

## Files written by this lane (uncommitted)

- `empirics/output/never13d_control_universe.csv` (3,600 rows)
- `empirics/output/never13d_control_summary.csv`, `never13d_exclusion_detail.csv`
- `research/empirics_v4/link_rebuild_2026-08-30.md`
- edits to `empirics/build_control_universe.py` (E4-identity consistency + dedup;
  the file itself was committed in `362f038`, my edits are uncommitted)
- EDGAR caches (gitignored): ~1,557 filing texts 2021 + 200 amendments + ~1,300
  submissions docs; `form_2021_QTR1..4.idx`

## Anomalies for the orchestrator

- Background shells here die at ~20 min (SIGTERM); long fetch phases need chunking
  or resume-from-cache (the scripts are resumable by construction).
- The same ticket was executed by ≥2 lanes this session (migration fallout). Outputs
  converged; the committed link is the E4 lane's, the control universe is this lane's.
- SPEC §8.2's "~11,000 candidates" was pre-filter arithmetic; the documented
  common-stock filter leaves 5,443 and the universe is 3,600 — adequate for 3:1
  against the realised treated N (1,112–1,465) but tight inside exact SIC-2 ×
  quarter cells.
