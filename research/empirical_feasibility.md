# Empirical Feasibility Audit — What Is Doable With In-Repo Assets + Free Data

**Strand:** empirical-feasibility (Task C of the repositioning swarm)
**Purpose:** Audit what the planned empirical anchoring (13D-acceleration DiD/event study; cross-country threshold contrasts; institutional facts) can actually rest on, given (a) what the repo's EDGAR pipeline produces today, (b) free data, (c) gated data whose access is unconfirmed. Every number below was computed first-hand in-session from repo files unless explicitly flagged second-hand.
**Compiled:** 2026-08-18, on branch `proposal`, machine where `empirics/data/` (gitignored) is populated.

---

## 1. What the pipeline produces today

### 1.1 Committed outputs (Fact 1 — disclosure-delay compression)
- **Code:** `empirics/edgar_fetch.py` (quarterly `form.idx` enumeration, ~4 req/s throttled fetcher, declared User-Agent), `empirics/parse_13d.py` (header fields, event date via XML tag or cover-page label regex, `pct_of_class` regex), `empirics/facts.py` (sampling + delay stats + figure).
- **Sample:** 300 SC 13D *originals* (amendments excluded by exact-form matching), seeded random draw, 150 from pre-window 2023Q2–Q3 (10-calendar-day rule) and 150 from post-window 2024Q3–Q4 (5-business-day rule). 251 unique subject CIKs, 259 unique filer CIKs.
- **Per-filing variables** (`fact1_filings.csv`): form, company, cik, date_filed, edgar_path, window, accession, filed, subject_cik, filer_cik, event (date of event requiring filing), pct_of_class, has_xml, delay_bdays, delay_cdays.
- **What Fact 1 already shows** (`fact1_summary.csv`): median delay **7.0 → 5.0 business days**; mean 9.63 → 6.4; p90 23 → 11.1; **share filed within 5 business days 35.7% → 75.6%** (share within 10 bd 80.6% → 88.9%). Parse rate only **0.68 pre / 0.64 post** (regex cover-page parsing). This is a real, paper-grade stylized fact already — the 2024 rule bit hard at the median and halved the right tail.
- `pct_of_class` extracted for 274/300 rows; median 9.49%, but range 0.0–99.99 with 62 rows <5% and 28 >50% — regex noise plus genuine non-standard filers (SPVs, groups, post-merger cleanups). Needs winsorizing/validation before use as "stake at first 13D".

### 1.2 Uncommitted assets on this machine (Fact 2 — partially EXECUTED, code not committed)
The README presents Fact 2 as WRDS-gated design only, but `empirics/data/` (gitignored, dated 2026-06-11) contains a first execution:
- `fact2_parsed.jsonl` — **9,234 SC 13D originals parsed, 2022Q1–2025Q4** (full universe of those quarters), adding subject/filer names, EDGAR accepted timestamp, and a **CUSIP for 7,970 (86%)**. Event date parsed for 4,638 (50%).
- `crsp_daily.csv` — **1.2 GB CRSP daily, 2021-01-04 → 2025-12-31, 11.88M rows, 14,092 unique PERMNOs**, columns incl. price, cap, return, volume, share-type flags. Sufficient for market-model CARs, Amihud illiquidity, size controls — no Compustat needed for a first pass.
- `wrds_evtstudy_edate.csv` — WRDS Event-Study-tool output: market-model CARs (21-day window, 220 estimation days) for **2,285 events** (from 3,518 uploaded CUSIP-date pairs → 65% match), 2022-01-04 → 2025-12-15. Pre/post split at 2024-02-05: 1,234 / 1,051 events. First-pass descriptive (UNVETTED, outlier-skewed): mean CAR 3.79% pre vs 12.77% post; **medians 1.57% vs 2.61%** — directionally consistent with the model's "more information released at filing post-rule" (contrast 1 of the Fact-2 design note), but the mean gap is driven by post-period outliers; medians are the honest summary.
- **Critical gaps:** (i) no code for any of this is committed (no CIK→CUSIP link script, no event-study harness) — reproducibility must be rebuilt; (ii) **the parser fails silently on the entire structured-data era**: event-parse rate is 66–68% for 2022–2024 but **0% for 2025**, and `has_xml=True` for zero of 9,234 rows, including post-2024-12-18 filings where the XML tag should exist. Likely cause: post-mandate filings carry the structured content as a separate XML document the 400 KB-truncated master-`.txt` fetch doesn't reach, and the cover-page label layout changed. This deletes most of the post-rule window from delay-based tests until fixed (est. 0.5–1 day: fetch the filing index/attachments, parse XML directly).

### 1.3 Post-rule sample sizes as the data stand
Post-rule (filed ≥ 2024-02-05) rows in `fact2_parsed.jsonl`: 4,176; with parsed event date: **1,235**; with event date *and* CUSIP: **1,048** — all concentrated in Feb–Dec 2024 because of the 2025 parse failure. Pre-rule: 5,058 / 2,849 with event+CUSIP. So the DiD's post leg is currently ~10.5 months, not the nominal ~2 years; fixing the 2025 parser roughly doubles the usable post window.

---

## 2. Test-by-test feasibility

Legend: **[FREE]** = EDGAR / open data / in-repo; **[GATED]** = WRDS-CRSP-Compustat/SDC/Activist Insight/Bloomberg — WRDS demonstrably worked from this machine on 2026-06-11 (the CRSP pull), but HANDOFF.md still lists "confirm UCL WRDS access" as an open author to-do, so treat standing access as **UNCONFIRMED**.

### 2.1 Test (i): DiD/event study around the 2024-02-05 13D acceleration
Required fields and status:
| Field | Source | Status |
|---|---|---|
| 13D filing events (date, subject, filer) | EDGAR form.idx + parser | [FREE] in hand (9,234 rows, 2022–2025) |
| Event date (trigger date) | parser | [FREE] 50% yield; 2025 broken (fixable) |
| Daily returns, prices, volume | CRSP daily | [GATED] **but a 2021–2025 snapshot is already on disk** — the whole study window is covered even if access lapses |
| Amihud illiquidity | computed: |ret|/(prc×vol) | derivable from the CRSP snapshot [FREE once data in hand] |
| Market-model factors | CRSP value-weighted return (in snapshot via caps) or Ken French daily factors | Ken French library is [FREE] |
| Size control | DlyCap in snapshot | covered |
| Book-to-market, sector | Compustat / CRSP | [GATED]; minimal version: log-cap + 2-digit SIC from CRSP header or EDGAR |
| Filer type (activist HF vs other) | filer-name regex + manual check | [FREE] crude; Activist Insight [GATED] does it properly |
| Controls for confounds | see §5 | [FREE] dummies |

**Minimal-viable version (no new gated data):** reuse the on-disk CRSP snapshot + rebuild the event-study harness (or rerun the WRDS event-study web tool if the account still works); sample = 13D originals 2022-01-01 → 2025-12-31 matched to US common stocks; regression `CAR[-1,+1] ~ Post × Amihud + Post + Amihud + log-cap + filer-type + year-quarter FE`, clustered by firm and month, exactly per the existing design note (`quality_reports/plans/2026-06-10_fact2-event-study-design.md`). Predictions: level up (β>0), liquidity slope flattened (δ<0).
**Free-data fallback if the CRSP snapshot must be replaced:** Stooq or Yahoo Finance daily bars for ~2–3k event tickers + Ken French factors. Caveats (practitioner-known, not verified in-session): Yahoo drops delisted tickers (survivorship bias toward non-acquired firms — fatal for a takeover-adjacent sample); Stooq's split/dividend adjustment is decent but delisting coverage patchy; neither gives PERMNO-stable identifiers. Adequate for a robustness check, not the primary spec.
**Caveat:** CARs computed off the *filing* date (as in the existing evtstudy output) measure the disclosure event; the model's κ interacts with the *accumulation* window — using the parsed event date for run-up windows ([−10,−1] pre-filing) is where the liquidity interaction should bite.

### 2.2 Test (ii): cross-country disclosure-threshold variation (3% vs 5% vs 10%)
Required: threshold-crossing notices per jurisdiction (initial stake, date, size), local daily prices, and a premium/announcement-return outcome.
- **Notices [FREE] but heterogeneous:** UK RNS + Takeover Panel table; BaFin, AMF, Consob, CNMV, AFM, FINMA registers; SEDAR+ (CA); ASIC (AU); EDINET (JP) (source list per `research/lit_institutional-facts.md` §7; formats not verified in-session). Each register is a bespoke scrape/parse job; none has an EDGAR-grade bulk API.
- **Prices [FREE-ish]:** Stooq/Yahoo cover UK/EU/CA/AU/JP large caps; delisted-name coverage is the known weakness — takeover targets delist, biasing premia measurement downward if unhandled.
- **Premia [GATED]:** SDC/Bloomberg premia-over-unaffected for non-US deals have no free substitute at scale.
- **Minimal-viable version:** scope to **UK only** as the out-of-sample leg: DTR-5 3%+1%-rung notices vs US 5% 13Ds, outcome = notice-date CAR from Stooq prices, question = does the liquidity–CAR slope differ under the stricter regime. Honest assessment: this is a **weeks-scale** project (register parsing, ticker mapping, price QA), and a one-country contrast with different market microstructure invites "everything differs" referee pushback. **Recommendation:** in the minimal package, demote (ii) to a calibration/motivation exhibit (thresholds × median delays × stake bunching from registers) rather than a regression leg; upgrade only if a RA or coauthor owns it.

### 2.3 Test (iii): institutional facts from the EDGAR pipeline
- **Stake-at-first-13D distribution [FREE, in hand]:** `pct_of_class` for ~86% of filings (median ≈ 10%). Needs cleaning (§1.1) and a bunching check just above 5%. Fact-quality: good.
- **Filing-delay distribution [FREE, in hand]:** Fact 1 committed; trivially extended to the full 2022–2025 universe (one flag change + ~1 h throttled fetching) once the 2025 parser is fixed.
- **Campaign→takeover transition rates [FREE but engineering-heavy]:** no outcome data in-repo today. Free route: for each 13D subject CIK, query EDGAR submissions API / full-text search (2001+) for subsequent **SC TO-T, SC 14D-9, DEFM14A, 8-K Item 1.01/2.01** within 6–18 months; classify outcome (acquired / standstill / withdrawn / persistent). Feasible stdlib-only with the existing fetcher; the work is endpoint-wrangling and dedup, est. 1–3 weeks including validation against a hand-checked subsample. Gated shortcut: Activist Insight/SDC outcome fields (days).
- **Intent coding (Item 4 "Purpose of Transaction"):** free from filing text; boilerplate-vs-concrete coding is the known discipline (BJPT-style, per `research/lit_institutional-facts.md` §8). Not started in-repo.

---

## 3. Binding constraint: takeover-premium measurement

The standard premium (offer price ÷ unaffected price − 1, 1-day or 4-week reference) is an **SDC/Bloomberg field — gated**, and it is the one variable with no complete free substitute. Assessment of alternatives:
1. **Hand-collect offer prices from EDGAR [FREE]:** for the subsample of 13D targets that receive a bid within 12 months (expected a few hundred, from test (iii)'s outcome matching), the offer price is in the SC TO-T / 8-K Item 1.01 press release / DEFM14A merger consideration. Unaffected price from the on-disk CRSP snapshot at a fixed pre-rumor date (e.g., −42 trading days). Effort: days of code + hand-verification; yields a *verified* premium measure for exactly the deals the paper's mechanism is about. This is the recommended primary route.
2. **CRSP-based CAR/run-up proxies [in hand]:** premium proxy = announcement CAR or run-up-adjusted CAR around deal announcement. Zero marginal cost, but squarely exposed to the **Ben-David–Bhattacharya–Jacobsen critique** (NBER WP 27976, rev. May 2025; per repo SNAPSHOT forthcoming JF 2026 — verify citation before use): announcement CARs fail to correlate with ex-post value-creation measures and are dominated by standalone-firm information. Handling: use CARs only as *information-revelation* measures (legitimate for 13D disclosure events, where the event IS the disclosure), never as deal-value measures; premiums proper come from route 1.
3. **Open M&A datasets:** no comprehensive free source exists; shared academic SDC extracts circulate but provenance/terms are murky — do not build on them.
4. **Validation anchors [FREE, second-hand]:** Celentano–Levine's mean premium 36.6% and activism→−13.7% premium effect (from `research/SNAPSHOT.md`; not re-verified in-session) give target magnitudes to sanity-check the hand-collected premium sample.

**Verdict:** premia are measurable for a few-hundred-deal subsample at days-to-weeks cost without SDC; the binding constraint is labor (outcome matching + offer-price extraction), not access.

---

## 4. Minimal empirical package (concrete)

**Sample:** all SC 13D originals filed 2022-01-01 → 2025-12-31 (9,234 parsed; extend forward quarterly), US-incorporated common-stock subjects matched to the on-disk CRSP snapshot (≈65–70% expected match; report attrition funnel). Event studies use filing dates; run-up windows use parsed event dates (post-fix).

| Variable | Exact source | Cost |
|---|---|---|
| Filing/event dates, CIKs, stake %, delay | `empirics/` pipeline (fix 2025 XML parsing first) | 0.5–1 d |
| CAR[-1,+1], CAR[-10,+1], run-up | on-disk CRSP snapshot + rebuilt market-model harness (or WRDS event-study tool) | 1–2 d |
| Amihud illiquidity, log cap, turnover | on-disk CRSP snapshot | 0.5 d |
| FF factors (robustness) | Ken French library | hours |
| Filer type (HF/activist flag) | name regex + manual spot-check | 1 d |
| Stake-at-first-13D + delay distributions (Fact 1 full universe) | existing code, flag change | 0.5 d |
| Deal outcomes + offer prices (premium subsample) | EDGAR SC TO-T / DEFM14A / 8-K via submissions API | 1–3 wk |
| B/M, sector, governance controls | Compustat [GATED — only if WRDS confirmed] | 1 d if access |
| Cross-country leg | registers + Stooq | weeks–months; **defer** |

**Effort ranking:** (1) 2025 parser fix → (2) Fact-1 universe extension → (3) Fact-2 regression on disk-resident data = **~3–4 days total** and already delivers "Fact 1 + Fact 2 + institutional distributions", i.e., a submittable empirical section. (4) Deal-outcome/premium subsample = **1–3 weeks**, unlocks the premium-sensitivity test (R2's sharpest form). (5) Cross-country regression leg = **weeks–months**, worst value-for-effort; keep as motivation exhibit only.

---

## 5. Risks and handling

1. **Short post window.** Nominal post-rule span Feb 2024 → Dec 2025 (23 months); *usable* post window is currently Feb–Dec 2024 because the parser misses the entire structured era. Fix the parser; then report power honestly and prefer medians/quantiles over mean-CAR contrasts (the existing first-pass mean gap 3.8%→12.8% is outlier-driven; medians 1.6%→2.6%).
2. **Bundled confounds in the post window.** (a) 13G deadline changes, compliance **2024-09-30** — shifts 13G↔13D composition inside the post period: handle by re-estimating on Feb–Aug 2024 only, and by filer-type FE. (b) Structured-data mandate **2024-12-18** — breaks measurement continuity (and currently the parser): treat Dec-18-2024 as a second regime break or end the main sample there, using 2025 as extension. (c) **T+1 settlement (2024-05-28)** — minor; robustness dummy. (d) **Universal proxy (mandatory for meetings after 2022-08-31)** sits *inside* the pre window: prefer pre = 2023+ or include a control. (Dates per `research/lit_institutional-facts.md` §1, primary-sourced there.)
3. **Selection into 13D.** Filing 13D (vs 13G vs staying <5%) is chosen; the model itself predicts the marginal filer changes post-rule. Handle: report filer-mix diagnostics pre/post (fund type, stake size, intent language); interpret β as reduced-form information-content change, not a structural parameter; do not instrument 13G eligibility without a defensible IV (index membership is the usual candidate).
4. **Ben-David et al. (JF 2026) CAR critique.** Never label a CAR "value creation". 13D-announcement CARs are defensible as *disclosure price impact*; deal-value statements require the hand-collected offer-price premium (route 1, §3). Cite the critique preemptively and show the premium-subsample CAR↔premium correlation as a measurement check.
5. **Measurement noise in parsed fields.** Parse rate 50–68% (event date), crude `pct_of_class` regex, silent 2025 failure discovered in-session — institute parse-rate reporting per quarter (the Fact-1 summary already does this per window) and hand-verify a 30-filing audit subsample before submission.
6. **Access fragility.** WRDS worked on 2026-06-11 but standing UCL access is unconfirmed (HANDOFF.md open to-do). Mitigation already in place: the full study window's CRSP data is on disk (gitignored — back it up off-repo; it does not survive a machine change). All EDGAR-side assets regenerate in ~1 h.
7. **Reproducibility debt.** The Fact-2 execution code (CIK→CUSIP link, evtstudy upload builder, regression) is not committed; rebuild and commit it when the empirical section is written, or the package cannot be defended.

**Blocking problems encountered during this audit:** none for the audit itself; the two material findings are the 2025 parser failure (fixable, §1.2) and the uncommitted Fact-2 code (§5.7).
