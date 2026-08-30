# Independent verification — E6 estimates (ticket 11 checkbox)

**Verifier:** fresh session, did not write any of the scripts under test.
**Date:** 2026-08-30 · **Branch:** `v4` · **Commits under test:** `cf8d311` (H1+H2),
`f912605` (dose §4 + stake §5), `bdd6323` (pseudo-trigger placebo §3.7),
`b040896` (§6 bounded-null sources).
**Method:** read the scripts against SPEC §2.3/§2.5/§2.6/§3.1–§3.5/§3.7/§4/§5/§6;
preserved all committed outputs to `/tmp/verify_preserve/`; re-ran every script with
`.venv/bin/python` from the manifest inputs; diffed re-run vs preserved; recomputed two
spot quantities independently (own pandas/numpy code, not their scripts); re-grepped the
SEC release text directly. Re-run outputs were byte-compared and the committed files then
restored from the preserved copies (working tree left clean).

**Concurrent-edit note.** While this verification ran, another session landed an
uncommitted SPEC.md corrigendum (mtime 13:16) superseding the §2.1/§3.6/§4/§5/§8.6 *count
and power* figures with the realised re-parse values ("printed → realised"; the §4 hunk
explicitly keeps the dose construction unchanged). Every SPEC sentence this report's
findings rest on — §2.3 filters, §2.5/§2.6, §3.1–§3.5, §3.7, the §4 construction and
specification equation, §5's cleaning and FE rules, §6's ladder — is outside those hunks
and was re-confirmed present in the current working-tree text. The corrigendum's §4 count
update (189/1,710 in the dose window) matches `reparse_counts.json:dose_filers` exactly.

**Re-run reproduction summary (the core mechanical check):**

| Output | Re-run result |
|---|---|
| `h1_estimate.json` | identical except `generated_at` (timing field) |
| `h1_sample.csv` | **bit-identical** (`cmp` clean, 1,093 rows) |
| `h2_estimate.json` | identical except `generated_at` |
| `dose_estimate.json` | identical except `generated_at` |
| `stake_estimate.json` | identical except `generated_at` |
| `placebo_h1h2_estimate.json` | identical except `generated_at` |

Seed fields exist in all five JSONs (20260830/…31/…32/…33/…34) and the wild bootstrap
reproduces exactly under them. `h1_estimate.json` records
`inputs.fact2_jsonl_sha256 = cc0e3f9d…f748f`; the current
`empirics/data/fact2_parsed.jsonl` hashes to the same value. The other four outputs record
seeds but **no input hash** (the chain is protected only via H1's hash plus the
bit-identical `h1_sample.csv`); `crsp_daily.csv` is identified by basename only. Noted as a
record-keeping gap, not a mismatch.

---

## 1. `cf8d311` — H1 (§3.4) and H2 (§3.5)

### H1 claimed numbers

| Claim (commit message) | Verdict | Evidence |
|---|---|---|
| N = 979 main sample | **MATCH** | Re-run prints 979; independent recount from `h1_sample.csv`: 1,093 rows − 100 stub (all 8 straddlers inside the stub set — overlap verified) − 14 variable-missing = **979** (446 pre / 533 post). Chain from `reparse_funnel.csv` step 4 (1,112) − 19 model failures = 1,093 ✓ |
| β2 = +0.58 pp | **MATCH** | Re-run 0.0057661; my own from-scratch OLS on the committed CSV: 0.0057661482510145 |
| two-way SE 1.56 | **MATCH** | 0.0156343; my own CGM two-way (firm + TD-month, intersection = unique pairs): 0.0156342597201860 |
| wild-month p 0.741 (quoted, conservative) | **MATCH** | 0.7408741 reproduced (normal p 0.7123 < wild; max quoted per §3.4) |
| MDE 4.38 pp | **MATCH** | 2.802 × 1.5634 = 4.3807 |
| FD*≡FD robustness p 0.725 | **MATCH** | 0.7248725 (N 979) |
| Zeng 1–13-calendar-day screen p 0.913 | **MATCH** | 0.9127913 (N 779) |
| Full-funnel robustness p 0.834 | **MATCH** | 0.8341834 (N 1,075) |
| 103 same-day filers kept with zero-length run-ups | **MATCH (basis caveat)** | 103 is the full-frame count (`fdstar ≤ td` over the 1,093); the main sample holds **95**. Commit quotes the full-frame number alongside the main-sample N |
| Filer-type 591/436/66 "in the estimation sample" | **MISMATCH of label (number real)** | 591/436/66 sums to 1,093 = the full-funnel-with-model frame. The actual main estimation sample (979) is **523/394/62** (my count from the committed CSV). The JSON field is computed on the full frame. Estimate unaffected; the words "estimation sample" are wrong |
| Realised σ RUNUP 0.53 / JUMP 0.38 / RUNUP5 0.55 | **MATCH (basis caveat)** | On the full frame: 0.5307 / 0.3803 / 0.5399 → 0.53 / 0.38 / 0.54. On the main estimation sample: 0.5376 / 0.3954 / 0.5496 → 0.54 / 0.40 / 0.55. The session log's phrase "on the estimation sample" is exact only for RUNUP5; the ~3×-vs-§3.6 conclusion holds on either basis. The H2 JSON's own `sigma_realised` (JUMP 0.3954, RUNUP5 0.5496, main-sample, ddof=1) is internally consistent — my recomputation agrees to 4 dp |
| Funnel "matches `reparse_funnel.csv` exactly" | **MATCH** | 4,639 → 3,710 → 3,356 → 1,465 → 1,112 in both, incl. 214 flagged-second / 139 exact-duplicate detail |
| Extreme tails real (Janover, RUNUP +832% / JUMP +805%, $4.00→$37.70) | **MATCH** | Independently pulled PERMNO 24072 (= JNVR) from raw `crsp_daily.csv`: 2025-04-04 close $4.00 → 2025-04-07 close $37.70 (DlyRet +842.5%, vol 25.0m). The max-runup sample row (accession 0001213900-25-029871, TD 2025-04-04) is this event |

### H2 claimed numbers

| Claim | Verdict | Evidence |
|---|---|---|
| Partition-refutation check runs first; δ(JUMP) p 0.928 vs δ(RUNUP5) p 0.997, not refuted | **MATCH** | `partition_check_first` block present and first in output; p 0.9279928 / 0.9974998; `partition_refuted: false` |
| δ(RUNUP5) = +0.02 pp, MDE 12.4 | **MATCH** | 0.0001752 (≈ +0.02 pp); realised MDE 12.393. My independent OLS/CGM: δ and SE match to 15 s.f. |
| δ(JUMP) = +0.54 pp, MDE 11.6 | **MATCH** | 0.0053945; MDE 11.621 |
| Per-day defence null | **MATCH** | δ = −1.39 pp, p 0.341, N 882 (97 zero-length run-ups drop out as 0/0 — verified no inf leakage is possible: zero-length windows have run-up exactly 0.0) |
| Identical-window (wlen = 5) defence null | **MATCH** | δ = +4.18 pp, p 0.478, N 242 |
| γ(Post) not reported from the YQ-FE spec | **MATCH** | §3.5 collinearity note honoured; no `post_td` column in the H2 design |

### §0-rule-1 disclosure (JUMP-window bug)

**MATCH.** `quality_reports/session_logs/2026-08-30_link-coder-h1h2.md` §4 carries both the
first-run estimate (β2 = +0.95 pp, p 0.586, N 976) and the corrected estimate
(β2 = +0.58 pp, p 0.741, N 979), with the cause named (calendar-date bracket vs §3.1's
trading-day convention; Monday filings lost the Friday). The current code's
`trading_day_window` implements the trading-day bracket. One internal typo in the same log:
"N = 979 (444 pre / 532 post)" — 444 + 532 = 976 (the *first* run's N); the corrected run
is 446/533 per the committed JSON and my independent recount.

## 2. `f912605` — dose (§4) and stake (§5)

| Claim | Verdict | Evidence |
|---|---|---|
| 127 of 1,103 filers have ≥ 2 pre-period filings (old 2,004/2,016 duplicate-inflated) | **MATCH** | Re-run identical. Cross-check: `reparse_counts.json:dose_filers` shows 189/1,710 in the same window *without* the trigger-parsed + 0–90-day-band requirements the script applies (disclosed in commit and log) — the 127/1,103 is the band-applied figure |
| Primary dose N = 249; imputed fallback N = 731 load-bearing | **MATCH** | Re-run: 249 / 731 |
| φ on RUNUP5/JUMP/STK null, p 0.36–0.97; MDE 17.0/8.6/7.5 pp | **MATCH** | 0.620 / 0.362 / 0.966; MDEs 17.01 / 8.62 / 7.51 |
| E-dose, imputed-dose, within-tercile variants null | **MATCH** | p range 0.31–0.87 across the six rows |
| First stage −7.25 days, t = −5.03 (mechanical, labelled) | **MATCH** | −7.2533, t −5.031; labelled "mechanical validity check, not a finding" with the Trivedi +0.348/0.130 benchmark quoted accurately |
| corr(D, LIQ) = −0.027 | **MATCH** | −0.0272 |
| Stake: 81 rows < 5% tail; winsor [1.66, 93.53]; sd 18.57 vs assumed 8 | **MATCH** | 81; [1.6649, 93.528]; 18.5700 |
| γ(Post) = −0.98 pp, wild p 0.714, MDE 6.55 | **MATCH** | −0.9754, p_wild 0.7139, MDE 6.548 (trend + quarter-of-year FE, γ identified — §5's deliberate FE difference implemented) |
| δ(LIQ×Post) = −2.16, p 0.120; YQ-FE variant agrees | **MATCH** | −2.1637 p 0.1195; YQ-FE −2.1879 p 0.1174 (γ correctly null/absorbed there) |
| Bunching histogram + BBJJ benchmark carried | **MATCH** | Both present in the JSON; raw median 9.43% vs BBJJ 6.3% contrast stated |

## 3. `bdd6323` — pseudo-trigger placebo (§3.7)

| Claim | Verdict | Evidence |
|---|---|---|
| N = 1,071 pseudo rows, 22 model failures, full-funnel basis | **MATCH** | Re-run identical (1,093 − 22) |
| pseudo-H1 partition −0.19 pp, quoted p 0.754 → clean | **MATCH** | −0.00188, p 0.7545 |
| pseudo-H2 JUMP +0.21 pp, p 0.727 → clean | **MATCH** | +0.00211, p 0.7272 |
| pseudo-H2 RUNUP5 −2.01 pp, p 0.081 → borderline flag recorded, no demotion | **MATCH** | −0.02007, p 0.0811; the flag and its reasoning (real RUNUP5 δ null at p 0.997) are in the commit message |
| 13G placebo flagged pending | **MATCH** | `not_run` field present. Note: §3.7's *third* bullet (quarterly LIQ-slope pre-trend F-test, 2022Q1–2023Q3) appears in no commit and is not listed in `not_run` — pending, not claimed |

## 4. `b040896` — §6 bounded-null sources re-grepped from the release text

All greps run by me directly against `research/txt_extracts/sec_release_33_11253.txt`:

| §6 figure | Verdict | Evidence (line numbers in the .txt) |
|---|---|---|
| Table 3 ladder: 1,907 / 463 / 78 / 16 campaigns; 80% / 20% / 3% / 1%; 173 / 42 / 7 / 1 per year | **MATCH** | lines 9924–9932 |
| 97% / 3% prose | **MATCH** | line 9896ff ("about 97 percent … remaining three percent"); restated at 12187 and 12395 (SPEC's "pp. 234 and 238") |
| Table 2: 3,067 of 15,724 = 20% non-corporate-action | **MATCH** | line 9586 (3,067 + 12,657 = 15,724 ✓) |
| 29% of 2022 initial 13Ds already inside the amended deadline | **MATCH** | line 9431 (cross-ref line 2457) |
| "earlier filing for about 59 percent of timely Schedule 13D reports" | **MATCH** | line 10127 |
| $49m/yr = $23m (col 1) + $26m (col 2); $26m line-wrapped | **MATCH** | Table 5 row (5) line 10930 ($23M/$26M/$13M/$7M); prose lines 10967–10969 with the "…$26\nmillion…" wrap exactly as the commit notes |
| $42m adaptation ($49m − $7m col 4) | **MATCH** | lines 10973–10975 |
| $36m adaptation ($49m − $13m col 3), n. 773 | **MATCH** | line 10999 |
| Commission's disclaimer ("do not represent estimates of the benefit of the final rule amendments") | **MATCH** | line 10977 |
| Table 6 sample 2,370 | **MATCH** | lines 9789, 10668, 11652 |
| No "$810 million" anywhere | **MATCH** | grep for `810 million` / `$810`: zero hits |

## 5. Script-vs-SPEC deviations found

None material to any verdict. In descending order of consequence:

1. **LIQ standardisation population** — `estimate_h1.py:668-670` standardises log-ILLIQ
   within quarter over the **full-funnel-with-model frame (1,093 rows)**, before the
   straddle/stub/missing restrictions cut to 979. SPEC §3.6 describes the §3.2
   standardisation as "within-sample". Re-standardising within quarter on the main sample
   shifts LIQ by up to 0.67 sd (mean 0.02 sd) and moves H1's β2 from +0.577 pp to
   +0.482 pp — against an MDE of 4.38 pp the bounded-null verdict is unchanged. Every
   downstream script inherits the committed LIQ from `h1_sample.csv`, so the package is
   internally consistent; the deviation is from the SPEC's most natural reading.
2. **Dose regression adds LIQ to the controls** — `estimate_dose.py:110-111`; §4's written
   specification is `y = α + φ(D×Post) + ψD + γPost + X'θ + δ_SIC2 + δ_YQ` with X = §3.3's
   controls (no LIQ). Motivated by §4's own confound paragraph (D–LIQ correlation), and the
   two *registered* diagnostics (corr(D, LIQ), within-tercile re-run) are both present —
   but the extra control is not in the registered equation.
3. **Placebo sample basis** — §3.7 says "re-run H1 and H2" (main-sample estimates);
   `estimate_placebo_h1h2.py` runs on the full-funnel rows (1,071) without the
   straddle/stub exclusions. **Disclosed** in the commit message ("full-funnel basis").
4. **90-day band inside the dose construction** — `estimate_dose.py:91-92`; §4's
   construction sentence names no band (§2.3 filter 2 is the sample funnel's).
   **Disclosed** in the commit message and session log.
5. **Firm-only clustering robustness row not emitted** — §3.4 registers "firm-only
   clustering is a robustness row, never the headline"; `ols_clustered` computes `V_a` but
   `run_h1` never reports it (`estimate_h1.py:464-502`). Omission, not misstatement.
6. **CUSIP→PERMNO tie-break unregistered** — when several eligible PERMNOs share a cusip8,
   the one with the most valid observations in [TD−126, TD−6] wins
   (`estimate_h1.py:535-545`); §2.3 filter 3 is silent on ties. Also noted: the funnel's
   link route is cover-page CUSIP → CRSP (`reparse_counts.json`: "provisional: cusip
   carried forward from old-parser file"), i.e. these estimates do **not** consume the
   rebuilt CIK→PERMNO link of `906128b`; the CUSIP values themselves are old-parser
   extractions carried forward (CUSIP extraction had no known bug in §2.2's list).
7. **BIND_j never estimated** — the binary dose is built (`estimate_dose.py:100`) but no
   regression uses it; §4 designates the continuous dose as primary, so this is a
   registered-secondary row not run.

Methodological observations (SPEC silent, no verdict impact): wild-bootstrap p reported as
`n_ex/B` without the (+1)/(B+1) finite-sample correction; no HC1-style small-sample scaling
on the CGM variance; §3.1's TOTAL window is never computed (no registered regression uses
it); H2/dose/stake/placebo JSONs carry seeds but no input hashes.

## 6. Overall verdict

**MATCH.** Every number claimed in the four commit messages reproduced exactly on an
independent re-run from the manifest inputs (five of six outputs identical up to the
`generated_at` timing field; `h1_sample.csv` bit-identical), and the two quantities I
recomputed without their code (main-sample N; the H1/H2 coefficients and two-way clustered
SEs via my own OLS + CGM implementation) agree to 15 significant digits. The SEC release
figures behind the bounded null all re-grep clean, including the line-wrapped $26m and the
absence of any $810m figure. The §0-rule-1 disclosure of the JUMP-window bug is present
with both estimates.

Caveats travelling with this verdict (none rises to a MISMATCH of substance):

- Three documentation imprecisions quote full-frame (1,093-row) numbers while saying
  "estimation sample": the filer-type distribution (591/436/66 vs main-sample 523/394/62),
  the 103 same-day filers (95 in the main sample), and the σ basis in the session log
  (σ(JUMP) = 0.38 is the full-frame value; the estimation sample gives 0.395, carried
  consistently inside `h2_estimate.json` itself). Plus the log's "444/532" pre/post typo.
- The seven deviations in §5, all minor; the largest sensitivity (LIQ standardisation
  population) moves the headline coefficient by 0.1 pp against a 4.38 pp MDE.
- The §3.7 pre-trend F-test bullet remains unrun and unflagged (not claimed by any commit).
