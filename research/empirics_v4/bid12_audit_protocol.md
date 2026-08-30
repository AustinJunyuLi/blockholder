# BID12 blind hand audit — auditor protocol

**Written:** 2026-08-30, before the audit runs. **Registered design:** SPEC §8.3
and `bid12_coding_rules.md` §10 (both frozen). This document does not change the
audit design; it fixes the procedure the auditing agent follows so the blindness
requirement is operationally real rather than nominal.

---

## 1. What the audit decides

Disagreement above 10% — **4 or more of the 30 sampled (firm, TD) pairs** —
**blocks the DiD leg** (SPEC §8.3, §8.9; rulebook §10). Blocking is not advisory:
if the audit blocks, the coding rule is fixed where the audit found it wrong and
the coding pass is re-run. A fix that would touch the **registered** rule (SPEC
§8.3 itself, or a decision-table row in rulebook §5) is reported to the
orchestrator and to Austin, never adopted inside the audit.

## 2. Blindness — the operational requirements

The auditing agent:

1. **did not write the coder** and has not read `empirics/bid12.py`;
2. receives, as its entire input: this protocol, `bid12_coding_rules.md`
   (hash-stamped; the auditor verifies the SHA-256 against
   `bid12_audit_manifest.json`), and `empirics/output/bid12_audit_pairs.csv`
   — which carries **CIK, firm name, trigger date, stratum, and nothing else**;
3. **records its own BID12 reading for every pair, in a file it writes, before
   any coder output is revealed.** The recorded file is the audit; a reading
   produced after seeing the key is not evidence;
4. only then is `empirics/output/bid12_audit_key.csv` revealed, and the
   disagreements are counted and adjudicated.

The auditor must not read `empirics/bid12.py`, `empirics/output/bid12_treated.csv`,
`bid12_events_treated.csv`, `bid12_control.csv`, `bid12_ambiguous_cases.csv`, or
`bid12_run_meta.json` before step 3 is written to disk. Those files carry the
coder's verdicts.

**The coder's raw caches are open to the auditor; its event caches are not.**
Settled here, before the auditor exists, so blindness is not renegotiated
mid-audit. `empirics/data/bid12_cache/{submissions,texts,headers,fts,fts_pages}/`
hold what EDGAR returned — filing tables, document text, submission headers,
search results — with no verdict in them, and reading them saves live fetches
and puts the auditor on the same evidence the coder saw.
`empirics/data/bid12_cache/events/` carries the per-firm coded event table,
including the ambiguity flags and `confirm_detail`, and is **off limits** until
the readings are recorded. One caveat that follows from §5.1 item 2: a cached
document may have hit the coder's byte cap. If a cached text or header looks
truncated at the point the reading turns on, the auditor re-fetches it from
EDGAR rather than reading the truncation as the document.

## 3. What the auditor does per pair

Re-derive BID12 from raw EDGAR by hand, under the rulebook as written
(**including §5.1**, the calibration addendum — it is part of the operational
rule and the coder implements it):

- window `[TD, TD + 365]`, calendar days, **both endpoints inclusive**
  (rulebook §3), dated on the EDGAR **filing date**;
- counted forms exactly as rulebook §2 lists them — originals only, no
  amendments, and none of the listed near-misses (`SC TO-I`, `SC 13E3`,
  `DEFA14A`, `DEF 14A`, `SC14D9C`, …);
- an `8-K` with Item 1.01 or 2.01 is a **candidate**, not an event: read the
  document and apply the §5 decision table, top to bottom, first matching row
  deciding;
- `SC TO-T` / `SC TO-C` require the §4 header verification — the SUBJECT
  COMPANY CIK must be the firm's own — regardless of how the filing was found
  (§5.1 item 3);
- a confirmed bid dated strictly before TD is **not** BID12; it is the
  already-under-bid exclusion (rulebook §6), and a bid dated **exactly on TD**
  **is** BID12 = 1;
- **ambiguous is a permitted answer and is never forced to 0 or 1** (rulebook
  §7). Record it as ambiguous with the reason;
- record, per pair: `bid12` (1 / 0 / ambiguous), the accession and date of the
  first in-window event if any, and one line of reasoning naming the rulebook
  row that decided it.

Two failure modes the rulebook was calibrated against, worth naming because
they are where a hand reading most often diverges: an Item 1.01 8-K that is a
**loan or credit agreement**, not a merger agreement; and an 8-K in which the
firm is the **acquirer**, not the target.

## 4. Counting the disagreement

Per rulebook §10: disagreement is the share of the 30 where the auditor's BID12
differs from the coder's. An **empty (ambiguous) coder value counts as agreement
only if the auditor's independent reading matches the post-adjudication value**
— an ambiguous coder cell that the auditor reads as a clear 1 or 0 is a
disagreement unless the adjudication lands on the auditor's reading.

Ambiguous cases listed in `bid12_audit_ambiguous.csv` are adjudicated
additionally and **do not count against the 30**.

Every disagreement is written up individually: what the auditor read, what the
coder recorded, and which of the two the rulebook supports. "The coder is
probably right" is not an adjudication.

## 5. The stratification split — a documented decision, not a dropped cell

Rulebook §10 fixes the sample as 30 pairs stratified **treated/control ×
pre/post 2024-02-05**, 7–8 per cell, drawn once. The control cells cannot be
drawn until the control-side lookup exists, and that lookup is downstream of
matching, which is downstream of the control extraction.

**Decision (2026-08-30):** the treated half (15 pairs, 8 pre / 7 post) is drawn
and audited as soon as the treated coding lands; the control half is drawn with
the **same seed** and audited when the control-side lookup lands. The manifest
records `single_draw: false` and carries the split note.

Three consequences, stated rather than left implicit:

1. **No cell is dropped.** All four cells are audited; only the timing differs.
2. **The blocking threshold stays on the 30.** The treated half alone cannot
   clear the leg: 4 disagreements out of the full 30 block it, so a treated-half
   result is reported as "k of 15 so far", never rescaled to a 15-pair
   threshold. Three or more disagreements in the treated half alone already
   makes blocking likely and is escalated immediately rather than waiting.
3. **The control half sits inside the DiD's critical path.** The DiD estimate
   may be computed once the control lookup lands, but it **may not be quoted as
   a result until the control half of the audit has passed**. Any estimate
   produced in between carries that caveat in its session-log entry.

## 6. Outputs

| File | Written by | When |
|---|---|---|
| `empirics/output/bid12_audit_pairs.csv` | sampler | before the audit |
| `empirics/output/bid12_audit_manifest.json` | sampler | before the audit |
| `empirics/output/bid12_audit_readings.csv` | **the auditor** | before any key is revealed |
| `empirics/output/bid12_audit_key.csv` | sampler | revealed after the readings |
| `research/empirics_v4/bid12_audit_result_2026-08-30.md` | orchestrator | after adjudication |

The result note records: the rulebook SHA-256 the auditor verified, the counts
per cell, the disagreement count and share, every disagreement written up
individually, the adjudication of each, and the pass/block verdict against the
10% rule.
