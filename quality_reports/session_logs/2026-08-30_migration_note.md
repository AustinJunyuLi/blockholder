# Session log — 2026-08-30 — environment migration mid-execution

**What happened.** The pre-registered execution (SPEC `research/empirics_v4/SPEC.md`,
triggered by the HANDOFF_sign.md §8 landing on `origin/v4-theory`, frozen 65b8db3) was
dispatched as a five-agent team on the Mac (`/Users/austinli/Projects/blockholder_v4`)
at ~09:14 UTC+1. At ~09:18 UTC+1 the session migrated to a Linux box (`/workspace`,
fresh clone of `origin`, branch `v4` at c5d92fd). Cursor could not transfer local git
state; nothing committed was lost (all committed work was pushed), but **all uncommitted
agent work products on the Mac are unreachable from this environment** and the affected
lanes were re-dispatched here from scratch.

**Lost-from-view (uncommitted, Mac-only):** the SPEC placeholder edit, the re-parse
script and its partial filings cache, the link-rebuild code, the BID12 rulebook/code.
All four were re-dispatched here at ~08:20 UTC with identical instructions.

**SPEC §13 item 4 (operational risk #1) — backup status UNKNOWN, needs Austin.** The
snapshot-backup agent ran on the Mac only (the 1.2 GB CRSP snapshot at
`/Users/austinli/Projects/blockholder/empirics/data` is not reachable from this box).
It was instructed to copy the 21-file manifest to
`~/Dropbox/blockholder_backups/empirics_data_2026-08-30/` with SHA-256 verification and
row-count readback, but it had been running ~4 minutes at migration and its completion
cannot be verified from here. **Austin: check that path on the Mac.** If the copy is
absent or partial, the snapshot is still intact on the Mac's disk — the backup simply
needs re-running there, or the snapshot needs copying into this environment.

**Blocked in this environment until the CRSP snapshot arrives** (`empirics/data/crsp_daily.csv`):
- §2.3 funnel filter 3 (CRSP match) and every post-match count; §3.6/§8.6 MDEs are
  being computed on parsed counts marked PROVISIONAL (pre-CRSP-match).
- The CIK→PERMNO join, validation against the 7,970 reusable CUSIPs, and the never-13D
  control universe (SPEC §11 rows 11/23) — link code and the EDGAR-side map are being
  built and fixture-tested now; the join is one re-run when the snapshot lands.
- All estimation (H1 §3.4 onward) — needs CARs/LIQ off `crsp_daily.csv`.

**Running here now (EDGAR-only or text-only lanes):** SPEC placeholder retirement
(§0.1, §3.5.2, §5, §9, §13 item 1 + dated corrigendum); the §2.2 re-fetch and re-parse
(~9,400 filing texts, throttled, cached, resumable); the CIK→CUSIP link's EDGAR side
plus the 2021 exclusion-set pull; the BID12 rulebook, coder, fixtures, and
treated-side coding pass once the re-parse lands. SEC bulk pulls are serialised through
`/tmp/sec_edgar_bulk.lock` in ≤500-request batches at the existing 4 req/s throttle.
