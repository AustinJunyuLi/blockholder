# Session log — 2026-08-30 (afternoon) — link gate, BID12 coder repair, H1/H2 estimated

**Lane:** empirics, worktree `v4`. Continues `2026-08-30_reparse.md` and the
11:05 mid-session state in `research/empirics_v4/bid12_status_2026-08-30.md`.
SPEC unchanged throughout — no test, sample rule, or variable was modified
after any estimate; the one implementation bug found post-estimate is
disclosed below with both estimates reported (§0 rule 1).

## 1. CIK→PERMNO/CUSIP link — gate PASSED (commit 906128b)

The 73.0% failure was diagnosed as **identity-vintage drift, not linkage
error**: the validation compared a filing-date cover-page CUSIP against
CRSP's current-only `HdrCUSIP`. Repairs (both on CRSP history, per the
dispatch): the CIK→PERMNO join matches the ticker against the PERMNO's whole
observed ticker history with tie-breaks on the ticker's own date span; the
validation compares the cover CUSIP against the PERMNO's whole observed
CUSIP history. **The denominator rule never changed** (matched CIKs carrying
a reusable cover-page CUSIP).

- Agreement **896/941 = 0.9522 ≥ 0.95** (was 660/904 = 0.7301). Matched
  1,019/2,735 CIKs; 12 ambiguous-ticker collisions preserved unmatched.
- Header-only comparison on the same rows scores 0.7216 — the gap is drift.
- 45 residual disagreements preserved with mechanical reasons
  (15 absent-from-CRSP-window, 14 same-issuer-different-issue, 12 owned by
  another PERMNO, 2 non-equity lines, 1 leading-zero artifact, 1
  subject/filer header collapse — the Walmart/Symbotic degeneracy).
- Determinism verified: a full cached re-run reproduced all three outputs
  bit-for-bit (SHA-256 match) and the same gate line.

## 2. BID12 coder — rulebook violations repaired (commit f5804f8)

A fresh read-only review found the four handoff-listed violations still
present plus three smaller issues (tender-header verification skipped for
route-B hits; 8-K truncation could confirm; bare acquire/acquired missing;
unextracted firms emitted hard 0; 60 KB header truncation silent; route-B
name-missing swallowed; fixture-calibrated regexes unregistered). All
repaired; semantics registered in **rulebook §5.1** (dated calibration
addendum); 35/35 synthetic checks. The bulk treated extraction (restarted
11:10 by the prior session under the pre-repair code) was **left running by
design**: it fills verdict-free raw caches; a watcher chain clears the
verdict-carrying event caches on its exit, re-runs the live fixtures under
the repaired coder, and only then re-derives and runs the lookup. Full
incident record: `bid12_status_2026-08-30.md` §4b.

## 3. Filer-type control (§11 row 19) — hand check landed

Top-200 filers by count hand-coded by a dedicated agent (methods:
`research/empirics_v4/filer_type_coding_2026-08-30.md`; table:
`empirics/output/filer_type_overrides.csv`, covering 23% of filings),
applied over the name-regex fallback. Estimation-sample distribution:
591 activist-HF / 436 other / 66 corporate. Judgment calls documented
per name (conservative default to "other").

## 4. H1 — the partition test (§3.4) — ESTIMATED

Script: `empirics/estimate_h1.py` (committed). Sample: the registered
§2.3 funnel (4,639 → 3,710 → 3,356 → 1,465 → 1,112; matches
`reparse_funnel.csv` exactly), minus 19 market-model failures, minus 100
stub rows (all 8 straddlers inside them), minus 14 variable-missing →
**N = 979** (444 pre / 532 post; 1,958 stacked rows; 891 firm / 47 month
clusters). 103 same-day filers carry a genuine zero-length run-up (no delay
screen, §2.3 filter 5).

> **β̂2 (partition) = +0.58 pp, two-way SE 1.56 pp, t = +0.37, quoted
> p = 0.741 (wild-month bootstrap, the conservative of 0.712/0.741).**
> β̂1 (pooled LIQ slope) = +0.67 pp (SE 2.84 pp); flagged-cell slope
> β̂1+β̂2 = +1.24 pp (SE 1.93 pp). **MDE(β2) = 4.38 pp.**

Decision table row 1: **|β̂2| < MDE → uninformative (bounded null) — "the
two cells cannot be told apart; the partition is not visible in prices."**
Not the "against" cell either: that requires β̂1 ≈ 0 *and* β̂1+β̂2 ≠ 0;
both slopes are ≈ 0. Robustness rows agree: FD*≡FD β2 = +0.59 pp
(p 0.725); Zeng-style 1–13-day screen β2 = −0.24 pp (p 0.913, N 779);
full-funnel β2 = +0.43 pp (p 0.834).

**§0-rule-1 disclosure — implementation bug found by the post-estimate
review and fixed:** the first run computed JUMP's [FD*−1, FD*+1] bracket
on calendar dates, so ~49% of jump windows spanned 2 trading days instead
of 3 (Monday filings lost the preceding Friday) — a mismatch to §3.1's
trading-day convention that attenuated the flagged cell. First estimate:
β2 = +0.95 pp (p 0.586, N 976). Corrected estimate (above): β2 = +0.58 pp
(p 0.741, N 979). Both are bounded nulls; the correction is logged here
rather than silently absorbed. No spec object changed.

Sanity anchors: mean RUNUP +3.9% (Zeng: +2.8%); median delay 6.0 → 5.0
business days pre→post (fact1: 7.0 → 5.0 on the CRSP-matched subset);
median PRE42 ≈ 0 (no pre-trigger drift). The extreme tails are real market
data, not artifacts — the largest (RUNUP +832%, JUMP +805%) is Janover
(JNVR), the April 2025 $4.00 → $37.70 melt-up, verified against raw CRSP
rows. **No winsorization** (none is registered); the tails are reported
as-is.

## 5. H2 — the reform slope change (§3.5) — ESTIMATED

Script: `empirics/estimate_h2.py` (committed; shares H1's sample
construction). Same N = 979.

- **§3.5.2 partition-refutation check, first:** δ̂(JUMP) = +0.54 pp
  (p 0.928) vs δ̂(RUNUP5) = +0.02 pp (p 0.997) → **partition NOT refuted**
  (nothing is significant on JUMP).
- **RUNUP5:** δ̂ = +0.02 pp, SE 4.42 pp, quoted p 0.997, clustered
  **MDE 12.4 pp** (design-formula MDE 9.9 pp). β̂(LIQ, pre-period slope) =
  +4.14 pp (SE 3.95 pp, t = +1.05) — §3.5.1's β < 0 prediction is not
  confirmed; the pre-period slope is undetectable at this variance.
- **JUMP:** δ̂ = +0.54 pp, SE 4.15 pp, quoted p 0.928, MDE 11.6 pp.
- Defences: per-day run-up δ̂ = −1.39 pp (p 0.341); identical-window-length
  (wlen = 5) subsample δ̂ = +4.18 pp (p 0.478, N 242).

Decision table row 2: **bounded null on both series** — reported with the
MDE quoted, never as "no effect". Branch A/B language does not attach
(neither branch is distinguishable from zero at this power).

## 6. The load-bearing finding: realised variance is ~3× the §3.6 assumption

§3.6 assumed σ(JUMP) = 0.12 and σ(RUNUP) = 0.15 (open item 15: "every §3.6
MDE scales linearly in them — recompute"). Realised, on the estimation
sample: **σ(RUNUP) = 0.53, σ(JUMP) = 0.38, σ(RUNUP5) = 0.55**, driven by a
nano-cap-heavy 13D universe with genuine melt-up tails. Every timing-split
MDE therefore scales up ~3–3.5×: the projected 1.1–2.3 pp detection range
becomes **~4.4 pp (H1's β2) and ~10–12 pp (H2's δ)** at realised variance
and realised clustering. The timing-split legs are materially less powered
than the SPEC's projections — the bounded-null outcomes above are the
arithmetically expected result, and the December text should quote the
realised MDEs. Within-sample sd of log ILLIQ = 2.93, IQR = 4.30 (§3.6's
required reporting, carried in `h1_estimate.json`).

## 7. Still in flight at time of writing

- Treated BID12 extraction (pre-repair process, raw caches) + the
  watcher chain that re-derives under the repaired coder; then recall
  check and the blind 30-pair audit (rulebook §10).
- `build_control_universe` (E1–E6 funnel) queued behind the SEC lock;
  then extract-control.
- Dose (§4), stake (§5), DiD (§8), bidder-entry (§9) estimates pending
  their inputs.

*Session: continuation of the 2026-08-30 empirics lane; commits 906128b
(link), f5804f8 (BID12 repairs), plus the H1/H2/filer-coding unit.*
