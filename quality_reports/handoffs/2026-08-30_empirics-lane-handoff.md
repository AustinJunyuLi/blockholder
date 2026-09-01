# Handoff — empirics lane, 2026-08-30 (E2 execution after the sign landing)

> **Superseded 2026-09-01.** This handoff serves the August empirical record, deleted at
> `235de22` (history: `9b98089`; preserved as viewed in `draft_v3_onlineappendix.tex`
> §app:honesty). Its authority file `research/empirics_v4/SPEC.md` and its scripts no longer
> exist. The live empirical lane is E1 alone: spec `research/empirics_v4/e1_spec.md`, single
> result authority `empirics/output/e1_estimate.json`. Retained as a session record only.

**Lane:** empirics (`v4` worktree `/Users/austinli/Projects/blockholder_v4`).
**Trigger:** `HANDOFF_sign.md` §8 landed on `origin/v4-theory` (theory frozen `65b8db3`).
**Authority for every method, number and filter:** `research/empirics_v4/SPEC.md`.
This document is the session record and the next agent's entry point.

---

## 1. For Austin (one page)

**Done and verified**

- **Backup (SPEC §13 item 4 — closed).** 21-file manifest copied to
  `~/Library/Mobile Documents/com~apple~CloudDocs/blockholder_backups/empirics_data_2026-08-30/`,
  SHA-256 verified 21/21, row counts read back from the copy: `crsp_daily.csv`
  11,884,715 rows, `fact2_parsed.jsonl` 9,234, `wrds_evtstudy.csv` 49,116,
  `wrds_evtstudy_edate.csv` 2,285 (all match SPEC §11). `BACKUP_MANIFEST.txt` inside.
  The migration note's Dropbox path was never written (Dropbox root is empty on this
  machine); iCloud Drive is the live sync and satisfies "survives a machine change".
- **Placeholders (SPEC §0.1/§3.5.2/§5/§9/§13 item 1 — closed).** Already retired at
  local `00e6b96` (dated 2026-08-30 corrigendum; both branches kept live; grep gate
  passes — the only "absent as of 2026-08-20" hit is the corrigendum's historical
  quote). I rebased it onto origin's migration note `0384f8d`; divergence resolved,
  history linear. HANDOFF §8 re-read against the corrigendum: consistent.
- **Execution tooling committed** at `362f038`: `reparse_fact2.py` (fetch/parse/
  finalize/analyze stages; finalize now writes the canonical jsonl atomically),
  `link_cik_cusip.py`, `build_control_universe.py`, `bid12.py`,
  `test_bid12.py`, `research/empirics_v4/bid12_coding_rules.md`. Scripts only — no
  estimate produced yet.

**At risk**

- **SPEC §2.1's counts are duplicate-inflated.** `form.idx` lists each 13D twice
  (filer's and subject's CIK directories; verified: same accession, both paths).
  The old `fact2_parsed.jsonl` has 9,234 rows = **4,639 unique filings**. Every §2.1
  count, the §2.2 projection (N≈4,950) and every §3.6/§8.6 MDE sits on the inflated
  basis; realised N will be roughly half, moving every MDE adversely by ≈√2. The
  re-parse computes realised MDEs; they supersede the projections per your dispatch.
  Consequence: the DiD leg's MDE-vs-3 pp-bound gap (§6 vs §8.6) widens further.
- **Nothing is pushed.** Local `v4` = `origin/v4` + `00e6b96` + `362f038`.
- The BID12 coder (`bid12.py`) and its test file were written by the *other* session's
  agent and patched by mine for lock-batching; it has had a code review against the
  rulebook started but not completed. Treat it as unverified until step 5 below runs.

**Needs you**

- **The Cursor Agents Window session is still alive** and executing the same dispatch
  (it wrote `bid12.py`/`test_bid12.py`, ran a 30-firm BID12 smoke at 09:44, and may
  launch more lanes). Killing its processes does not stop its orchestrator — only you
  can pause/close that window. Until then two executors race the same caches and the
  SEC lock. All repo scripts are cache-idempotent so the worst case is wasted
  requests, not corruption — but decide which session owns the lane.
- Push decision on the two unpushed commits.

## 2. Live OS processes (survive this session; all cache-resumable)

| PID | What | End state |
|---|---|---|
| 91977 (+worker) | `reparse_fact2 --stage fetch` batch loop, ≤500-request lock holds, ≤60 iterations | filings cache → ~4,639 minus hard 404s; does **not** run finalize/analyze |
| 98438 / 98701 | `link_cik_cusip` re-run (submissions fetch, lock-batched by the script's single hold) | `empirics/output/cik_cusip_link.csv`, `_disagreements.csv`, `permno_cik_map.csv` |
| 92816 / 92817 | `bid12 extract-treated --ciks` smoke (2 firms) | a few `bid12_cache/` files |

The three lane-owning subagents were cancelled with this session; the processes above
keep running but nothing downstream of them fires automatically.

## 3. Next agent — finish in this order

1. **Confirm the fetch finished.** `ls empirics/data/filings | grep -cv _failures`
   ≈ 4,639 minus persistent 404s; `_failures.json` empty or same-accession stable.
   If the loop died early: `.venv/bin/python -m empirics.reparse_fact2 --stage fetch`
   (cache skips done files). Done when a run prints "0 to download".
2. **Finalize:** `.venv/bin/python -m empirics.reparse_fact2 --stage finalize` →
   4,639 rows; old file archived as `fact2_parsed_oldparser_2026-08-20.jsonl`;
   `accepted`/`accepted_after_4pm` carried; cusip carry-forward on most rows.
3. **Analyze:** `.venv/bin/python -m empirics.reparse_fact2 --stage analyze`
   (loads the 1.2 GB CRSP snapshot, minutes). **Do not pass `--link-file`** — that
   path keys on the idx-directory `cik` column, which post-dedup is not reliably the
   subject CIK (known defect, recorded here; the default carry-forward CUSIP route is
   the registered one). Report the §2.3 funnel, per-quarter parse rates (2025 was 0%
   pre-fix — the referee's first number), the trigger-date split, dose-filer counts,
   and the realised §3.6/§8.6 MDEs verbatim from `empirics/output/reparse_counts.json`.
   Supersede the SPEC's projected MDEs with a **dated post-registration note** (the
   2026-08-23/08-30 corrigenda are the pattern): realised numbers in, no prediction,
   test, sample rule or variable changed. Note the §2.1 duplicate-inflation finding
   (§1 above) explicitly — it explains the ~2× miss on N.
4. **Link + control universe:** verify `cik_cusip_link.csv` exists (one row per
   subject CIK, ~2,700) with agreement ≥ 95% against the reusable cover-page CUSIPs
   (else investigate the disagreements file before proceeding); then
   `.venv/bin/python -m empirics.build_control_universe` →
   `never13d_control_universe.csv` + summary (pool 14,092 PERMNOs → ~11,000 expected;
   E1–E6 exclusion funnel; amendment orphan rate reported). If `fact2_parsed.jsonl`
   was replaced after the link run (step 2), re-run the link first — cache makes it
   cheap — so committed outputs derive from the final jsonl.
5. **BID12 (long pole, SPEC §8.3).** Review committed `empirics/bid12.py` against
   `research/empirics_v4/bid12_coding_rules.md` (the authority, written before the
   pass). Smoke: DICE CIK 1645569 must find Lilly's `SC TO-T` 0001193125-23-180387
   (2023-06-30); Reata's 2023-07-11 8-K (Item 1.01 loan agreement) must NOT confirm
   (its real merger 8-K is 2023-07-31). Then `.venv/bin/python -m empirics.bid12
   extract-treated` over ~2,700 subject CIKs → `lookup-treated` →
   `bid12_events_treated.csv`, `bid12_treated.csv`, `bid12_ambiguous_cases.csv`,
   `bid12_run_meta.json` (rulebook SHA-256 inside). Ambiguous cases listed, never
   forced. `extract-control` after step 4's universe lands.
6. **Blind hand audit** (rulebook §10): 30 (firm, TD) pairs, stratified
   treated/control × pre/post, by a fresh agent that did not write the coder and does
   not see its output; disagreement > 10% blocks the leg.
7. **Estimation in SPEC order** once 1–6 land: H1 first (§3.4, sign-free — the
   partition check runs and reports first, SPEC §10), then H2 (§3.5, Branch A
   directionally selected with both branches live), dose (§4), stake (§5), matched
   DiD (§8), bidder-entry-by-liquidity (§9). Every estimate from a committed script,
   ESTIMATED label, MDE quoted with every null, session-log entry per SPEC §0 rule 1.

## 4. Hard rules

- SEC fair access: ~4 req/s per process, bulk pulls serialised through
  `/tmp/sec_edgar_bulk.lock` in ≤500-request holds with a release gap. Two lanes max.
- SPEC is methodologically frozen: realised numbers supersede projections only via
  dated corrigendum; never change a test, sample rule or variable post-estimate.
- `empirics/data` is a symlink to `../blockholder/empirics/data`; the backup (§1) is
  the only other copy — do not delete or bulk-rewrite the snapshot.
- `HANDOFF_sign.md` and the whole theory worktree are read-only here. Anything that
  looks like a theory problem goes in Austin's next one-pager, not in a fix.
- Commit on `v4` with explicit paths; do not push without Austin.

*Session log: dispatched 2026-08-30 ~09:16; backup + placeholder verification +
tooling commit done by 10:05; lanes handed off mid-flight as above.*
