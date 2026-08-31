# BID12 blind audit result — treated half (2026-08-31)

Registered design: SPEC §8.3, rulebook §10, protocol
`bid12_audit_protocol.md`. This is the treated half of the documented
split draw. Blocking remains **4 of 30**. Three treated-half
disagreements would escalate. This file does not clear the DiD leg.

## Rulebook

Auditor verified SHA-256
`e95c4f9f87d4224597f91b659251fd3b7f8d81ca748843ef7cc4a2c9255de0c6`
against `bid12_audit_manifest.json`. That hash matches
`bid12_run_meta.json` after the completeness-test re-lookup.

Readings were written to
`empirics/output/bid12_audit_readings.csv` at 01:46, then sealed as
`bid12_audit_readings_sealed_2026-08-31_sessionB.csv` at 01:47, after
the 01:45 pairs file and before this adjudication opened the key.

A second independent auditor, which did not read the coder, wrote
`bid12_audit_readings_sessionA_2026-08-31.csv` at 01:55. Same 15
verdicts (13 zeros, one 1, one ambiguous). The protocol file was
restored from the first sealed copy.

## Counts

| cell | n | auditor 1 | auditor 0 | auditor ambiguous |
|---|---|---|---|---|
| treated_pre | 8 | 1 | 7 | 0 |
| treated_post | 7 | 0 | 6 | 1 |
| treated half | 15 | 1 | 13 | 1 |

Coder: 1, 13 zeros, 1 empty/`ambiguous=1`. **Disagreements: 0 of 15**
on both independent readings. No escalation. The control half is still
required.

Four extra ambiguous events among the sampled firms were listed in
`bid12_audit_ambiguous.csv` and do not count against the 15.

## The two non-zero readings (agreement)

**Agrify Corp, TD 2024-01-25, auditor 1, coder 1.** Item 1.01 8-K filed
2024-04-22: Nature's Miracle Holding expects to acquire Agrify by reverse
triangular merger. Section 5 row 1 confirms. The later termination does
not matter (rulebook §7).

**Datavault AI Inc., TD 2025-10-23, auditor ambiguous, coder empty.**
Two in-window merger 8-Ks fire merger patterns with no clean target or
acquirer direction (section 5 row 6). Section 7 leaves BID12 empty.

## Blindness record

- The auditor (a fresh agent, model Opus) did not write the coder and
  attested it never read `empirics/bid12.py`, `empirics/test_bid12.py`, any
  verdict-carrying output (`bid12_treated.csv`, `bid12_events_treated.csv`,
  `bid12_control.csv`, `bid12_ambiguous_cases.csv`, `bid12_run_meta.json`),
  the key (`bid12_audit_key.csv`, `bid12_audit_ambiguous.csv`), the coder's
  event cache (`bid12_cache/events/`), or any session log. Its evidence came
  only from the raw caches (`submissions/`, `texts/`, `fts/`,
  `fts_pages/`); no live re-fetch was needed (largest primary document 72 KB
  against the 2 MB cap; nothing truncated at a decision point).
- Seal ordering verified by file mtimes: readings written 01:46, snapshotted
  01:47 (`empirics/output/bid12_audit_readings_sealed_2026-08-31_sessionB.csv`),
  key first opened by the orchestrator 01:48. A reading produced after seeing
  the key is not evidence; none was.

## Result per pair (coder vs auditor)

| cell | firm | CIK | TD | coder | auditor |
|---|---|---|---|---|---|
| treated_pre | CARVER BANCORP INC | 0001016178 | 2022-12-20 | 0 | 0 |
| treated_pre | OVERSTOCK.COM, INC | 0001130713 | 2023-10-12 | 0 | 0 |
| treated_pre | All American Gold Corp. | 0001409430 | 2022-09-01 | 0 | 0 |
| treated_pre | C-Bond Systems, Inc | 0001421636 | 2023-01-17 | 0 | 0 |
| treated_pre | ENETI INC. | 0001587264 | 2023-12-15 | 0 | 0 |
| treated_pre | MedMen Enterprises, Inc. | 0001776932 | 2021-01-11 | 0 | 0 |
| treated_pre | Agrify Corp | 0001800637 | 2024-01-25 | 1 | 1 |
| treated_pre | Guerrilla RF, Inc. | 0001832487 | 2023-09-06 | 0 | 0 |
| treated_post | NUVEEN NEW JERSEY QUALITY MUNI | 0001087786 | 2024-06-05 | 0 | 0 |
| treated_post | My City Builders, Inc. | 0001556801 | 2025-01-22 | 0 | 0 |
| treated_post | Boxlight Corp | 0001624512 | 2025-06-11 | 0 | 0 |
| treated_post | Datavault AI Inc. | 0001682149 | 2025-10-23 | ambiguous | ambiguous |
| treated_post | Starbox Group Holdings Ltd. | 0001914818 | 2024-05-07 | 0 | 0 |
| treated_post | Amentum Holdings, Inc. | 0002011286 | 2024-12-17 | 0 | 0 |
| treated_post | Solarius Capital Acquisition Cor | 0002065948 | 2025-07-17 | 0 | 0 |

**Disagreements: 0 of 15 (0%).** No disagreement write-ups are owed.

The single BID12 = 1 pair (Agrify) agrees on the event itself, not merely the
value: coder and auditor both record first bid 2024-04-22, 8-K accession
0001213900-24-034983 (Nature's Miracle merger term sheet; rulebook §5 row 1,
target-direction "expects to acquire the Company"; §7 counts the bid although
the deal was terminated 2024-05-19).

The single ambiguous pair (Datavault AI) agrees on the value: per the
protocol's counting rule an ambiguous coder cell agrees only with a matching
independent reading, and the auditor independently landed on ambiguous
(§5 row 6) for the same evidence.

## Ambiguous events among sampled firms (adjudicated additionally; not counted against the 30)

`bid12_audit_ambiguous.csv` lists 4 events:

1. **Datavault AI 2026-08-19 8-K** (0001104659-26-098835) — the event behind
   the ambiguous pair above. Adjudication: ambiguous stands. The auditor's
   reading is that Datavault is substantively the acquirer (WDT/BankWyse
   deal), but the 8-K is written purely in merger-sub/surviving-company
   language: no `acquir` substring appears, and both "wholly owned subsidiary
   of" instances are followed by "the Company", which the target pattern's
   negative lookahead blocks. The rulebook's acquirer-rejection vocabulary is
   built around "acquire", so this drafting style has no path to §5 row 2 and
   lands on row 6. This produces ambiguity, not a false positive — BID12 is
   not inflated. **Rulebook-coverage observation, flagged for Austin:** a
   merger 8-K drafted without the "acquire" stem cannot be direction-resolved
   by the registered table. The registered rule is frozen; no fix was adopted
   inside the audit. (Same firm's NYIAX 8-K of 2026-03-19 reads the same way;
   the auditor noted the window runs to 2026-10-23 and is not yet closed —
   immaterial to the reading, which rests on filed evidence.)
2. **Agrify 2021-10-05 8-K** (0001013762-21-000191) — pre-TD (TD
   2024-01-25), outside the window; no bearing on the pair value.
3. **Agrify 2024-05-20 8-K** (0001213900-24-044908) — in-window but later
   than the confirmed first bid of 2024-04-22 that carries the pair; the
   timing is consistent with the termination announcement (deal terminated
   2024-05-19). No bearing on the value.
4. **Guerrilla RF 2021-10-27 8-K** (0001213900-21-054809) — pre-TD (TD
   2023-09-06), outside the window; no bearing on the pair value.

## Process record: mid-audit regeneration

The audit ran across a live repair by the other session:

- 01:31 the post-pass chain completed and wrote the treated outputs
  (3,546 events; 1,595 ambiguous; 3 CIKs missing extraction).
- 01:34 the orchestrator drew the treated half against those outputs
  (manifest listed 5 ambiguous events among sampled firms).
- 01:39 the other session regenerated the treated outputs (3,547 events;
  1,361 ambiguous; 0 CIKs missing — the 3 outstanding CIKs were extracted and
  a further fix retired 234 ambiguous rows), and declared the 01:34 draw
  invalid in its status note.
- 01:45:35 the other session redrew with the same seed against the
  regenerated outputs (4 ambiguous events among sampled firms; the dropped
  5th row is unidentifiable from current files — overwritten).
- 01:46 the auditor sealed its readings; 01:48 the key was revealed.

The drawn **pairs are identical across the two draws** (the sealed readings'
15 (CIK, TD) keys equal the redrawn pairs file exactly, firm by firm), so the
regeneration did not touch the sample; the key the readings were compared
against is the current (01:39) coder output, which is the correct object to
audit. Blindness was unaffected: the auditor's evidence was the raw caches
throughout, and no coder output was opened before the seal. The audit is
therefore valid for the coder outputs now on disk; had the redrawn pairs
differed, the audit would have been rerun against the new draw.

## Items relayed to the orchestrator / Austin (from the audit and the coder's status note)

1. The Datavault rulebook-coverage observation above (§5 direction
   vocabulary; registered rule frozen — any change is a post-registration
   decision for Austin, not the audit).
2. Coder status note §9: **S2 (corporate-action Item-4 coding) does not
   exist, so S2 is not a sample** — flagged gap in the registered design's
   sample set.
3. Coder status note §9: **Gate 4 remains a recorded fail on the universe
   rate (S1/H1 = 18.66%)** — recorded, not resolved.

## Verdict so far

Treated half: 0 of 15. Quote as "0 of 15 so far", not as a 15-pair
threshold. The DiD may be computed after control lookup. It may not be
quoted as a result until the control half is audited.
