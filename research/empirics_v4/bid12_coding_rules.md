# BID12 outcome coding — operational rulebook

**Ticket:** `.scratch/v4-reposition/issues/13-e5-outcome-coding.md` (E5) · **Lane:** empirics (`v4`)
**Written:** 2026-08-30, **before** the coding pass (ticket requirement).
**Registered definition:** SPEC §8.3 (`research/empirics_v4/SPEC.md`). This document is the
*operational* rulebook under that definition. It does not widen or narrow the registered
rule; it fixes routes, regexes, and conventions that the SPEC leaves to implementation.
Anything that would change the rule itself is reported to the orchestrator, not adopted here.

---

## 1. The registered rule (verbatim from SPEC §8.3)

> `BID12 = 1` if, within **365 calendar days** of TD (or pseudo-TD), the firm is the
> subject of any of: `SC TO-T`, `SC TO-C`, `SC 14D9`, `DEFM14A`, `PREM14A`, or an `8-K`
> carrying Item 1.01 or Item 2.01 whose text names a merger or acquisition agreement for
> the firm itself.

Fixed corollaries (SPEC §8.3 bullets):

- The clock starts at **TD**, not FD — identical for treated and control.
- A firm **already under an announced bid at TD** is **excluded** from both groups.
- **Withdrawn and completed bids both count** — entry is the object, not completion.
- **Bids by the 13D filer itself count**, and are also reported separately.
- **Ambiguous cases are listed as ambiguous, never forced.**
- Thirty-filing hand audit, stratified treated/control × pre/post 2024-02-05, blind;
  disagreement > 10% blocks the leg.

## 2. Form list, exactly

Counted (exact EDGAR form strings, originals only):

| Form | Filed by | Route |
|---|---|---|
| `SC TO-T` | bidder (third-party tender offer) | A + B |
| `SC TO-C` | either side (tender-offer communications) | A + B |
| `SC 14D9` | target (solicitation/recommendation statement) | A |
| `DEFM14A` | target (definitive **merger** proxy — the "M" form; distinct from annual-meeting `DEF 14A`) | A |
| `PREM14A` | target (preliminary merger proxy) | A |
| `8-K` with Item 1.01 or 2.01 | target | A, **text confirmation required** (§5) |

**Not counted** (explicitly, because they are near-misses a referee will ask about):

- Amendments: `SC TO-T/A`, `SC 14D9/A`, etc. An amendment evidences a bid whose original
  filing is the event; counting amendments would double-count and would smear bids whose
  originals predate the window into it. The original is what is dated.
- `SC14D9C` (target tender-offer *communications*), `SC14D9F` — distinct form strings,
  not in the registered list.
- `SC TO-I` (issuer tender offer — the firm repurchasing its **own** shares; not a
  takeover bid), `SC 13E3` (going-private), `DEFA14A` (additional soliciting material),
  `DEF 14A` / `PRE 14A` (annual-meeting proxies — note the space; not merger forms).
- `8-K` without Item 1.01 or 2.01 in its `items` field (e.g. Item 8.01 press releases
  announcing a deal but reporting no definitive agreement — the agreement 8-K follows and
  is what is dated).

Form strings were verified against the on-disk quarterly indexes
(`empirics/data/form_2023_QTR2.idx`, `form_2024_QTR3.idx`): the spellings above are the
only variants in the sample era.

## 3. The clock

- Window: **`event_date ∈ [TD, TD + 365 calendar days]`**, both endpoints inclusive.
- Calendar days, never business days (the rule is written in calendar days).
- `event_date` = the EDGAR **filing date** of the bid-event filing (`filingDate` in the
  submissions API; `file_date` in full-text search). The filing date is the first
  publicly timestamped evidence of the bid that EDGAR carries.
- Pseudo-TD for controls: identical arithmetic on the inherited pseudo-trigger date.

## 4. The two routes

### Route A — the firm's own submissions feed

`https://data.sec.gov/submissions/CIK{10-digit}.json`, via the throttled fetcher
(`empirics.edgar_fetch.fetch`, ~4 req/s, declared User-Agent). The `filings.recent`
table carries `form`, `filingDate`, `accessionNumber`, `items`, `primaryDocument`;
firms with more filings than the recent table holds are completed from the paginated
`filings.files[]` JSONs, so the full 2021-01-01 → 2026-12-31 extraction window is
covered for every firm.

**Verified property (2026-08-30, probed live):** the submissions feed indexes a filing
under **both** the filer's and the subject company's CIK. Bidder-filed `SC TO-T` /
`SC TO-C` therefore **do** appear in the target's own feed (verified on
DICE Therapeutics CIK 1645569: bidder Eli Lilly's `SC TO-T` 0001193125-23-180387 of
2023-06-30 is present in DICE's feed). Route A alone is therefore expected to carry high
recall; route B is the recall backstop and the independent check.

From route A, counted directly by form string: `SC TO-T`, `SC TO-C`, `SC 14D9`,
`DEFM14A`, `PREM14A`. `8-K` rows are counted only after text confirmation (§5).

### Route B — EDGAR full-text search over bidder-filed forms

`https://efts.sec.gov/LATEST/search-index?q=%22{core name}%22&dateRange=custom&startdt=2021-01-01&enddt=2026-12-31&forms=SC%20TO-T,SC%20TO-C`
(multi-form parameter verified live). One query per firm; results paginated
(`from`/`size`, 100 per page, up to 10 pages) and de-duplicated by accession (the
search indexes each document in a filing, so one filing yields several hits).

A route-B hit is accepted **only if the target's own CIK appears in the hit's
`display_names`** (which list every entity on the filing with its CIK). This is
load-bearing: a name search for "Reata Pharmaceuticals" returns an `SC TO-T` for
*Zynerba* (Reata is mentioned in the text), and fund-family filings dominate name
search results generally. CIK verification is the gate; name matches without a CIK
match are discarded and logged in the run metadata as discarded route-B hits.

Route-B events are merged with route-A by accession; an event found by both is labelled
`A+B`. The route label is carried into the output so recall can be measured
(`A only` vs `B only` vs `A+B`).

### Bidder identity (for the filer's-own-bid flag)

For every `SC TO-T` / `SC TO-C` event, the master submission header
(`https://www.sec.gov/Archives/edgar/data/{cik}/{accession-with-dashes}.txt`, first
~40 KB — verified to resolve under the target's CIK directory as well as the filer's)
is parsed for `SUBJECT COMPANY` / `FILED BY` Central Index Keys (same regexes as
`empirics/parse_13d.py`). This both (i) verifies the event really names the target
(subject CIK must equal the firm's CIK, else the event is marked ambiguous) and
(ii) yields the bidder CIK. For route-B hits the bidder CIK is taken from
`display_names` (the non-target CIKs) and cross-checked with the header when fetched.

## 5. The 8-K text-confirmation rule

An `8-K` with Item 1.01 or 2.01 in-window is a **candidate**, not an event: Item 1.01
covers *any* material definitive agreement (credit facilities, supply contracts,
leases, licences), and both items also cover transactions where the firm is the
**acquirer**, not the target. (Worked example found during development: Reata's
2023-07-11 8-K, indexed with Item 1.01, is a **loan agreement** — three weeks before
its actual merger agreement of 2023-07-28, reported 2023-07-31.)

The candidate's `primaryDocument` is fetched and reduced to plain text
(`html.unescape` **before** tag stripping — `&#160;` entities otherwise break item
headings; tags stripped; whitespace collapsed). Decision rules, applied to the whole
document:

**Positive merger patterns** (any one required):

- `agreement and plan of (merger|reorganization|consolidation)`
- `merger agreement`
- `business combination (agreement|transaction)`
- `(cash )?(tender|exchange) offer ... (shares|stock) of`
- `plan of merger`

**Direction patterns — firm is the TARGET** (any one required to confirm), with
"the Company" or the firm's core name interchangeable:

- `merged with and into (the Company|{name})`
- `(the Company|{name})[^.]{0,120}wholly[- ]owned subsidiary of` **not followed by `the Company`/`{name}`** (negative lookahead — otherwise the acquirer-side structural phrase "Merger Sub, a wholly owned subsidiary of the Company" false-fires; calibrated on the Salesforce debt 8-Ks of 2021-06-30/2021-07-12, which recite the Slack merger parties)
- `acquisition of (the Company|{name})` · `acquire (the Company|{name})`
- `(the Company|{name}) will be acquired`
- `tender offer for (all|any) ... (shares|stock) of (the Company|{name})`
- `(the Company|{name}) would become a (wholly[- ]owned )?subsidiary`

**Direction patterns — firm is the ACQUIRER** (rejection evidence):

- `(the Company|{name})[^.]{0,80}(has agreed to|will|plans to)? ?acquir` without a
  target-direction match
- `acquisition by (the Company|{name})`
- `(the Company|{name})[^.]{0,80}(entered into|sign)[^.]{0,80}to (acquire|purchase)`

**Defence-instrument patterns** (`rights agreement`, `rights plan`, `poison pill`,
`stockholder/shareholder rights`): a rights-plan 8-K (Item 1.01 on a Rights
Agreement) discusses "tender offer" at length and would otherwise pile into the
ambiguous bin. A rights plan is a *defence*, not a bid.

**Non-merger-instrument patterns** (`underwriting agreement`, `credit agreement`,
`loan agreement`, `indenture`, `senior notes`, `notes due`, `supply/lease/license/
collaboration/settlement/separation/distribution/master services/employment/
consulting agreement`, `asset purchase agreement`, `purchase and sale agreement`):
the instruments that dominate Item 1.01 volume. `stock purchase agreement` is
deliberately **absent** — an acquisition of the firm can be structured as one, so
those fall through to ambiguous.

**Decision table** (evaluated top to bottom; first matching row decides):

| # | merger pattern | target direction | acquirer direction | defence / instrument | verdict |
|---|---|---|---|---|---|
| 1 | yes | yes | no | any | **confirmed** |
| 2 | yes | no | yes | any | rejected — firm is acquirer |
| 3 | yes | no | no | defence | rejected — rights plan, not a bid |
| 4 | yes | no | no | non-merger instrument | rejected — instrument, not a bid |
| 5 | yes | yes | yes | any | **ambiguous** |
| 6 | yes | no | no | none | **ambiguous** |
| 7 | no | — | — | any | rejected — non-merger Item 1.01/2.01 |
| 8 | text unfetchable / truncated | — | — | — | **ambiguous** (reason recorded) |

Rows 3–4 require the *absence* of target direction: a genuine merger 8-K that
mentions the firm's rights plan (merger agreements routinely condition on plan
redemption) or the buyer's financing ("credit agreement") still carries
target-direction language and is confirmed by row 1. All six positive fixtures
in `empirics/test_bid12.py` confirm via row 1.

**Direction-pattern notes** (both were calibrated against live 8-Ks, 2026-08-30):
the firm name in patterns is an alternation of the full core name and its first
token when distinctive (8-K bodies shorten the firm to its first token after
first reference — "merged with and into Reata"); the bare phrase "a wholly owned
subsidiary of the Company" is **not** acquirer evidence (holdco/double-dummy
structures describe the target's own vehicle that way — VMware 2022), only a
party *becoming* or *surviving* as one is.

**§5.1 Calibration addendum (2026-08-30, pre-audit).** A read-only review of
the coder against this rulebook found four divergences; the coder was repaired
to this addendum before the final treated pass was derived, and the audit
should read this section as part of the operational rule. No registered rule
(SPEC §8.3) and no decision-table row changes.

1. **Acquirer bullet 1, bare form.** The auxiliary "(has agreed to|will|plans
   to)" is optional, so plain past tense fires ("the Company acquired X").
   Two guards keep it acquirer-side only, both required or the bare form
   false-fires on this rulebook's own target phrasings and flips row-1
   confirmations to row-5 ambiguous: (i) a passive-voice lookbehind — the
   pattern does not fire when "acquir*" is immediately preceded by
   "be"/"been"/"being" ("the Company will be acquired" stays target); (ii) a
   lookahead — it does not fire on the noun phrase "acquisition of the
   Company" ("… and the acquisition of the Company is expected to close …"
   stays target).
2. **Row 8's truncated-text rule applies to the verification document too —
   with a completeness test, not a byte-count test.** The SGML header is
   self-terminating: a tender-event header is *truncated* only when the
   fetched bytes do not contain the `</SEC-HEADER>` close tag (header block
   incomplete → **ambiguous**, "tender-header-truncated", never confirmed).
   Hitting the 60 KB fetch cap with the close tag present is NOT truncation:
   the cap only cuts the filing body, which the verification never reads.
   (Calibration, treated pass 2026-08-31: 363/363 byte-capped headers carried
   the complete header block; the earlier byte-count rule had made 129/129
   SC TO-T events ambiguous — route B would never have confirmed anything.)
   An 8-K text that hits its byte cap (2 MB primary / 1.5 MB master .txt) IS
   **ambiguous** ("text-truncated"), per row 8 as written — there the body
   itself, which carries the agreement language, is cut.
3. **Tender verification semantics (§4).** "For every SC TO-T / SC TO-C
   event" means regardless of route: a route-B `display_names` bidder does
   not substitute for the header check. Unavailable header (permanent fetch
   failure) → ambiguous ("tender-header-unavailable"). SUBJECT CIK present
   but ≠ the firm → ambiguous (as written). SUBJECT CIK unreadable in a
   parsed header → ambiguous ("tender-subject-unreadable"). The bidder is
   the header's FILED BY CIK; the route-B cross-check is "FILED BY appears
   **among** the filing's non-target `display_names` CIKs" (display_names
   list merger subs alongside bidders, so a first-entry comparison would
   misfire) — absence → ambiguous ("bidder-disagrees-header").
4. **Fixture-calibrated pattern extras**, in the coder and registered here so
   the blind audit sees exactly what fires. Target-side additions:
   "(the Company|{name}) … to be acquired"; "all … outstanding (shares|stock)
   … of (the Company|{name})"; "(each|every) share … of (the Company|{name}) …
   converted into". Acquirer-side additions: "(the Company|{name})'s
   acquisition of"; "(the Company|{name}) … (completed|consummated) … (its)
   acquisition of"; "(the Company|{name}) … to purchase (shares|assets|stock)".
5. **Unextracted firms are unresolved, not zeros** (§7). A (firm, TD) row
   whose event extraction has not run leaves BID12 **empty** with
   `extraction_status = not-extracted`; "no in-window evidence ⇒ 0" presumes
   the search ran. Firms whose route-B query cannot run for lack of a usable
   name are surfaced (`fts-empty-core-name` in the record errors, counted in
   the run metadata), never silently dropped.

The verdict and the specific patterns fired are recorded per candidate in
`confirm_detail`, so the audit can retrace every decision without re-fetching.

## 6. The already-under-bid exclusion

Registered: *a firm already under an announced bid at TD is excluded from both groups.*

Operational detection: **a confirmed bid event dated strictly before TD**. Two flags are
emitted per (firm, TD):

- `excluded_prior_bid` — **primary**: a confirmed event in `[TD − 365, TD − 1]`.
  A bid announced within the prior year is plausibly still live at TD (bids resolve in
  months, not years), which is the economically meaningful reading of "already under an
  announced bid". The 365-day lookback is exactly covered by the extraction window
  (2021-01-01 start vs TDs from 2022-01-01).
- `prior_bid_any` — sensitivity: a confirmed event anywhere in `[2021-01-01, TD − 1]`.
  The gap between the two flags is failed bids followed by a fresh 13D more than a year
  later; the count is reported in the status note.

A bid event dated **exactly on TD** is *not* an exclusion — it falls in the outcome
window `[TD, TD+365]` and codes BID12 = 1. "Already under a bid" means the announcement
*preceded* the trigger.

Exclusion is emitted as a flag; rows are not silently dropped (the attrition is
downstream's to report, per SPEC §2.3's funnel rule).

## 7. Withdrawn vs completed; filer's own bid; ambiguity

- **Withdrawn and completed bids both count.** No attempt is made to detect bid outcome;
  entry is the object. (Consequence: no completion/withdrawal parsing anywhere in the
  coder.)
- **Filer's own bid** (`filer_own_bid`): per treated row, 1 if any in-window confirmed
  event's bidder CIK equals the 13D's `filer_cik`, or — for text-confirmed 8-K events
  where no bidder CIK exists — the 13D filer's normalized core name appears in the
  confirming document text. Counted in BID12 like any other bid, and reported separately.
- **Ambiguous, never forced.** Ambiguous events are listed in
  `empirics/output/bid12_ambiguous_cases.csv` with the reason. In the per-filing lookup:
  a confirmed in-window event ⇒ BID12 = 1; no in-window evidence ⇒ BID12 = 0; **only
  ambiguous in-window evidence ⇒ BID12 is left empty** (`ambiguous = 1`) pending the
  hand audit's adjudication. Ambiguous cases are never forced to 0 or 1.

## 8. Extraction window and universe

- Bid events are extracted once per firm over **2021-01-01 → 2026-12-31**, which covers
  TD + 365 for TDs through 2025-12-31 and TD − 365 for TDs from 2022-01-01. The BID12
  lookup is then a pure function of the event table and the TD — deterministic, and
  re-runnable from cache with zero network.
- Treated universe: unique `subject_cik` in `empirics/data/fact2_parsed.jsonl`,
  re-deduplicated at run time; the file's mtime and MD5 are recorded in
  `empirics/output/bid12_run_meta.json` at each run (a re-parse by another ticket may
  replace the file; the subject-CIK set is header-derived and stable).
- Control universe: when `empirics/output/never13d_control_universe.csv` and
  `permno_cik_map.csv` land (SPEC §11 row 23, another ticket), the same extraction runs
  over the control CIKs unchanged — one command, same cache.

## 9. What this coding cannot see (registered limitation, SPEC §8.3)

A bid contemplated and abandoned before any filing leaves no trace in EDGAR. BID12
measures **filed** bid entry. Stated as a limitation in the paper, not patched.

## 10. Audit design (fixed before the pass)

- **Sample:** 30 (firm, TD) pairs from the coded output, stratified
  treated/control × {TD < 2024-02-05, TD ≥ 2024-02-05} — 7–8 per cell; a cell short of
  observations draws the balance from its paired cell. All ambiguous cases in the sample
  window are additionally included for adjudication (they do not count against the 30).
- **Blind:** the auditing agent did not write the coder and does not see its output. The
  auditor receives this rulebook (hash-stamped) and the 30 (CIK, TD) pairs, re-derives
  BID12 from raw EDGAR by hand, and only then is the coder's output revealed.
- **Disagreement rule:** disagreement = share of the 30 where auditor BID12 ≠ coder
  BID12 (an empty/ambiguous coder value that the auditor resolves counts as agreement
  only if the auditor's independent reading matches the post-adjudication value).
  **Disagreement > 10% (≥ 4 of 30) blocks the leg** (SPEC §8.3, §8.9); the coding rule
  is then fixed where the audit found it wrong, and the pass is re-run.
- **Inputs left clean for the auditor:** this rulebook,
  `empirics/output/bid12_events_treated.csv`, `empirics/output/bid12_treated.csv`,
  `empirics/output/bid12_ambiguous_cases.csv`, and `empirics/output/bid12_run_meta.json`
  (which carries this file's SHA-256 so the auditor can verify the rulebook version).

---

*Rulebook hash: recorded in `empirics/output/bid12_run_meta.json` at each run.*
