# Session log — 2026-08-30 (afternoon, part 2) — dose (§4) and stake (§5) estimated

Continues `2026-08-30_link-coder-h1h2.md`. Scripts `empirics/estimate_dose.py`
and `empirics/estimate_stake.py`; records `empirics/output/dose_estimate.json`
and `stake_estimate.json`. No spec object changed; both estimates share H1's
sample construction (N=979 main sample).

## Dose (§4) — ESTIMATED: nulls everywhere, and the primary sample collapsed

**The repeat-filer premise did not survive the re-parse.** §4 expected
"2,004 of ~2,016 pre-period filers" to have ≥2 pre filings (old-parser,
duplicate-inflated basis). Realised: **127 of 1,103 filers** have ≥2
pre-period filings (0–90-day band applied to the dose construction too, so
stale trigger parses cannot inflate D). The primary multi-filer dose
regression therefore runs on **N = 249**; the stratum-imputed robustness row
(filer-type × size-tercile × illiquidity-tercile means, pre-period
estimation only, per §4) carries **N = 731**.

- φ̂ (D×Post) on RUNUP5: +3.83 pp (quoted p 0.620, **MDE 17.0 pp**)
- φ̂ on JUMP: +3.14 pp (p 0.362, MDE 8.6 pp)
- φ̂ on STK: +0.14 pp of stake (p 0.966, MDE 7.5 pp)
- E-dose and imputed-dose variants: nulls (p 0.31–0.85)
- Within-liquidity-tercile: nulls in all three terciles
- **First stage (mechanical validity check, labelled as such):** post-period
  delay of high-D filers falls 7.25 days more (t = −5.03) — direction as
  expected; Trivedi's published analogue is a different outcome scale
  (+0.348 SE 0.130 on the within-5-days share).
- **corr(D, LIQ) = −0.027** — the feared dose–liquidity collinearity is
  negligible in this sample.

Decision row 3: **uninformative** — every |φ̂| is far below its MDE. The
mechanism leg cannot speak at realised repeat-filer rates; this compounds
the reparse session log's finding that the §4 stratum-imputation fallback
is load-bearing.

## Stake at filing (§5) — ESTIMATED: bounded null; power premise also failed

Cleaning per §5: 1,067/1,093 rows carry STK; 7 dropped (≤0 or >100);
**81 in the 0–5% tail** (Fact-1 analogue: 62/300 — similar rate);
winsorised [1.66, 93.53]; bunching histogram in 0.25-point bins over [4, 8]
written to the record. Raw distribution: median 9.43% / mean 16.47% /
p90 40.78% / p95 61.72% — far more dispersed than the BBJJ activist-HF
benchmark (6.3 / 8.8 / 14.6 / 21.2), as expected for an all-filer 13D
universe.

- **Primary γ̂ (Post, trend + quarter-of-year FE): −0.98 pp of stake**
  (two-way SE 2.34, t = −0.42, wild-month p 0.714). Point direction
  supportive (stake falls), magnitude far under its **MDE 6.55 pp**.
- δ̂ (LIQ×Post): −2.16 (wild p 0.120, MDE 3.57 pp); the YQ-FE variant
  agrees (−2.19, p 0.117). Insignificant; point sign leans Branch B (fall
  concentrated in illiquid names), stated as a point-sign observation only.
- **Decision row 4: uninformative** (|γ̂| < MDE). Not "against" (γ̂ > 0
  significant is the against case).

**Power premise failed.** §5 assumed a winsorised sd of 8 pp (BBJJ-scale);
realised **18.57 pp** (fat right tail — p90 above 40%). The projected
0.65–0.85 pp MDE becomes **6.55 pp clustered** (3.37 pp design formula).
The BBJJ days–stake gradient's mechanical prediction (0.12 pp) remains
~1/55 of the MDE: a detectable γ̂ would have to be behavioural, and the
December text must quote the realised MDE.

## Session pattern

Three of the package's variance assumptions (σ-JUMP, σ-RUNUP, sd-STK) are
now replaced by realised values ~3× larger across the board; every timing-
split and level leg is correspondingly less powered than SPEC §3.6/§5
projected. No test or sample rule changed — the estimates are reported with
their realised MDEs, per §0 rules 2–3 and §13 items 15–16.
