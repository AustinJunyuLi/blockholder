# BID12 blind hand audit: full result, 30 of 30 (2026-08-31)

Registered design: SPEC §8.3, rulebook §10, protocol
`bid12_audit_protocol.md`. Both halves of the documented split draw are
now audited, each by a fresh agent that did not write the coder.

**Verdict: 0 disagreements of 30. The audit does not block the leg.**
Blocking was 4 of 30 (disagreement above 10%). The treated half was 0 of
15 on two independent readings; the control half is 0 of 15.

What this clears and what it does not. It clears the outcome coder,
which is what the audit is about. It does not clear the §8 estimate:
the matching stage fails its own balance gate, `did_estimate.json`
carries `NOT ESTIMATED`, and the §8.8 pre-trend F-test blocks causal
language on its own. See `did_matching_2026-08-31.md`.

## Part A: the treated half

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

## Treated-half verdict

0 of 15, on two independent readings. No escalation (the trigger was 3).

---

# Part B: the control half (2026-08-31, 09:27 to 09:40)

## Draw and rulebook

`bid12_audit_sample --side control --seed 20260830`, run after the
control-side BID12 lookup landed (839 matched-control rows, 602 distinct
linked CIKs, 0 not-extracted). The draw merged into the existing pairs
file rather than overwriting it: 30 pairs, four cells, 8 / 7 per cell,
and the 15 treated (CIK, TD) keys are identical to the sealed treated
readings, checked key by key.

A defect in the sampler was found and fixed **before** this draw ran. On
a `--side control` call the key file was being built from the already
merged pairs frame and then merged again against its own prior copy, so
the 15 treated rows landed twice: once carrying verdicts, once blank. An
adjudication joining readings to the key on (side, CIK, TD) would have
matched the blank copies and scored 15 spurious disagreements, which
would have blocked the leg on an artefact. The merged key now holds one
verdict-carrying row per pair, checked in `test_bid12_audit_sample.py`.

The auditor verified rulebook SHA-256
`e95c4f9f87d4224597f91b659251fd3b7f8d81ca748843ef7cc4a2c9255de0c6`
against `bid12_audit_manifest.json`.

## Blindness record

A fresh agent, which had not written the coder and had not read
`empirics/bid12.py`. Its declared input was the protocol, the rulebook,
and `bid12_audit_pairs.csv`. It attested it did not open the coder or
its tests, `bid12_audit_key.csv`, `bid12_audit_ambiguous.csv`, any
verdict-carrying output, `bid12_cache/events/`, the other auditor's
readings, any session log or status note, or `git log` / `show` /
`diff`. The only coder file it read is `empirics/edgar_fetch.py`, the
throttled fetcher, which carries no coding logic.

Seal ordering by file mtime: readings written 09:38:04 to
`bid12_audit_readings_control.csv`, sealed 09:40:17 as
`bid12_audit_readings_sealed_control_2026-08-31.csv`, key first opened
by the orchestrator 09:40:34. The pairs and key were snapshotted at
09:27:59, before the auditor started.

One thing the auditor did beyond the protocol, and it is worth
recording. Protocol §2 opens the `fts/` cache, but that cache stores the
coder's route-B results **after** its CIK gate. To keep route B
independent the auditor re-ran all 15 full-text-search queries live
against `efts.sec.gov`, de-duplicated by accession, and applied the §4
`display_names` CIK gate itself. The live results reproduce the cache
exactly.

## Result per pair (coder vs auditor)

| cell | firm | CIK | pseudo-TD | coder | auditor |
|---|---|---|---|---|---|
| control_pre | CONMED Corp | 0000816956 | 2022-01-06 | 0 | 0 |
| control_pre | Perma-Pipe International | 0000914122 | 2022-04-01 | 0 | 0 |
| control_pre | Corcept Therapeutics | 0001088856 | 2022-03-28 | 0 | 0 |
| control_pre | China Pharma Holdings | 0001106644 | 2023-08-22 | 0 | 0 |
| control_pre | SoundThinking | 0001351636 | 2023-05-09 | 0 | 0 |
| control_pre | Regional Management | 0001519401 | 2021-12-31 | 0 | 0 |
| control_pre | G1 Therapeutics | 0001560241 | 2023-09-27 | **1** | **1** |
| control_pre | KKR Real Estate Finance Trust | 0001631596 | 2023-05-10 | 0 | 0 |
| control_post | Interlink Electronics | 0000828146 | 2024-05-28 | 0 | 0 |
| control_post | Commvault Systems | 0001169561 | 2024-02-13 | 0 | 0 |
| control_post | Inogen | 0001294133 | 2024-10-30 | 0 | 0 |
| control_post | Supernus Pharmaceuticals | 0001356576 | 2024-03-28 | 0 | 0 |
| control_post | Treace Medical Concepts | 0001630627 | 2024-10-30 | 0 | 0 |
| control_post | Porch Group | 0001784535 | 2024-08-09 | 0 | 0 |
| control_post | FinWise Bancorp | 0001856365 | 2024-02-07 | 0 | 0 |

**Disagreements: 0 of 15.** No write-ups owed.

The single BID12 = 1 pair agrees on the event, not merely the value.
G1 Therapeutics: coder and auditor both record the first in-window event
as `SC TO-C` `0001104659-24-086802`, filed 2024-08-07, Pharmacosmos A/S
tender offer, with the §4 header verifying SUBJECT COMPANY CIK
0001560241 as the firm's own.

Both failure modes the rulebook was calibrated against appeared in this
half and both were read correctly. CONMED is the **acquirer** in four
in-window merger 8-Ks (In2Bones, Biorez) plus a notes offering that
merely recites a merger agreement. Regional Management, SoundThinking,
Porch, China Pharma and Corcept produce credit, securitisation, licence
and collaboration Item 1.01s that are not merger agreements.

## Full-audit counts

| cell | n | 1 | 0 | ambiguous | disagreements |
|---|---|---|---|---|---|
| treated_pre | 8 | 1 | 7 | 0 | 0 |
| treated_post | 7 | 0 | 6 | 1 | 0 |
| control_pre | 8 | 1 | 7 | 0 | 0 |
| control_post | 7 | 0 | 7 | 0 | 0 |
| **all 30** | **30** | **2** | **27** | **1** | **0** |

0 of 30 is 0%, against the registered blocking threshold of above 10%.

Eleven ambiguous events among the sampled firms are listed in
`bid12_audit_ambiguous.csv` and adjudicated separately; they do not
count against the 30.

## Control-side ambiguous adjudications

Five are Supernus `SC TO-C` / `SC TO-T` events carrying
`subject-cik-mismatch` (2021-10-12, 2021-10-25, 2025-06-16 x2,
2025-07-02). These are Supernus's **own outbound** offers, for Adamas in
2021 and Sage in 2025: the full-text name match catches Supernus as
bidder and the header's SUBJECT COMPANY is someone else. §4 correctly
makes them ambiguous rather than events. All five are outside the
window in any case. The auditor reached the same reading independently.

Two are G1 Therapeutics 8-Ks (2024-08-07 and 2024-09-18) that the coder
marks ambiguous under §5 row 5, target and acquirer direction both
firing. They have no effect on the pair, which is carried to BID12 = 1
by the form-list `SC TO-C`. They are discussed in the next section,
because the auditor predicted them from the rulebook text without
having seen the coder.

The four treated-side ambiguous events are adjudicated in Part A.

## Two rulebook-coverage observations, for Austin

Both come from the control-half auditor. Neither was acted on: the
registered rule is frozen and a change is a post-registration decision.
What makes these worth Austin's time is that the **coder independently
landed on the same two cases**, from the other side of the blind, which
is about as strong as corroboration of a specification gap gets.

**1. §5.1 item 4's added patterns leave their gap operator undefined,
and a wide reading false-fires.** The pattern
`(the Company|{name}) … to purchase (shares|assets|stock)` is registered
as acquirer-side evidence. Read with a permissive gap it also matches
ordinary target-side merger boilerplate. In G1's own 2024-08-07 8-K it
matches "each option **to purchase shares** granted under **the
Company**'s equity incentive plans", which adds acquirer direction to a
document that also carries target direction and flips a §5 row 1
confirmation into a row 5 ambiguous. That is exactly what the coder's
`confirm_detail` records for that filing: `target:1;acquirer:1`. The §5
patterns written with `[^.]{0,80}` are unambiguous; the §5.1 item 4
additions written with an ellipsis are not.

**2. The bare acquirer form of §5.1 item 1 cannot see the sentence
subject.** In G1's 2024-09-18 Item 2.01 8-K it matches "…Parent, as the
parent of Purchaser, **acquired** control of the company", where the
grammatical subject is Parent and the firm is plainly the target. The
two registered guards (a passive-voice lookbehind and an "acquisition
of" lookahead) do not cover that shape.

Neither observation changes any verdict in this audit. G1's BID12 = 1
rests on the form-list tender events, which are decided by §2 and §4
without touching §5. The exposure is a **treated-side case resting on an
8-K alone**, where the reading would turn entirely on how the ellipsis
is read. The coder's own treated pass has 1,323 ambiguous 8-Ks, 768 of
them on §5 row 6, so this is the population where it would bite.

A third, minor observation: **§3 has no intra-day tie-break.** G1's
first in-window evidence is two filings on the same filing date, a
form-list `SC TO-C` and a row-1-confirming 8-K. The rulebook dates
events on the filing date and gives no ordering within a date. Only the
`first_event_form` label turns on it, never the verdict.

## Verdict

**0 disagreements of 30. The registered hand audit passes and does not
block the DiD leg.** The BID12 outcome coder is audited on both sides,
by two fresh agents, against a hash-verified rulebook, with readings
sealed before either key was opened.

The leg is blocked elsewhere, on two independent registered grounds
recorded in `did_matching_2026-08-31.md`: the §8.2 match fails its
balance gate after the predeclared 0.20-caliper rerun, and the §8.8
pre-trend joint F-test returns p = 0.021, which is below 0.10 and
blocks causal language on its own terms.
