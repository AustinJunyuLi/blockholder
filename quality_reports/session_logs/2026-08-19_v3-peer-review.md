# Session log — 2026-08-19 — framework_v3 peer review + edits

## Goal
Referee framework_v3 (positioning, model validity, empirics; originality/methodology/results)
with a bounded agent team, then edit the qmd and re-render. Plan:
quality_reports/plans/2026-08-19_v3-peer-review-plan.md.

## Key context
- framework_v3 = Stage-2 synthesis of the 9-strand lit review (research/lit_*.md, SNAPSHOT.md).
- User preference: agent team via Agent tool, not the Workflow tool (memory file).
- Papers behind paywalls: use ego-browser skill (user logged in); local PDFs in lit/, tmp_*/,
  research/txt/.

## Log
- 01: plan + log written; dispatching Stage A (5 finders).
- 02: Stage A dispatched (A1 theory/opus, A2 lit/opus, A3 novelty/opus, A4 empirics/opus, A5 facts/sonnet). Orchestrator doing independent read of prop:disclosure-attenuation while waiting.
- 03: Orchestrator numeric check (repo model, fixed k1,k0, vary kD): baseline ω_P≈0.037 → the R2 figure's
  two curves differ by <1% (TV 0.01107 vs 0.01117 over κ∈[0.15,0.85]) — attenuation is quantitatively
  negligible at baseline. Moving mass to Public (kD↓) does lower κ-sensitivity monotonically, faster
  than the pure (1−ω_P) weight effect ⇒ composition term reinforces at baseline but is not "one line".
  κ† = 0.58 in baseline_series.csv (memo says ≈0.59). D8 rem:d8-boundary phrasing consistent with memo.
- 04: MAJOR results finding (orchestrator, repo model, fixed cutoffs k1=k0=0.8217): comparing the
  disclosure regime (τ=1) with the no-disclosure regime (τ=0) — i.e. moving the Public mass from
  disclosed to inferred — the κ-sensitivity of Δ^act is NOT uniformly lower under disclosure:
  TV over κ∈[0.15,0.85]: ω_P=0.037: 0.01758 vs 0.01653 (ratio 1.06); ω_P=0.129: 1.19; ω_P=0.286: 1.14;
  ω_P=0.50: 0.38. Pointwise slopes: disclosure steeper at κ≥0.7 for ω_P≤0.29. So T2's economic claim
  is calibration-dependent in PE; only the weight identity is "one line". The kD-threshold experiment
  attenuates monotonically but mostly for reasons present without disclosure too (TV falls 0.0165→0.0106
  under no-disclosure as ω_P 0.04→0.5). To be reported as MAJOR in the referee report + memo edits.
- 05: A1 theory referee DONE (opus, 20 tool uses, 161k tokens) → research/review_v3/theory_referee.md.
  17 findings: T2 not proved as stated (two-term product rule; τ reweighting law unstated); existence
  not "unconditional" (needs A5a; draft has internal contradiction l.696 vs l.1009); GE region T2 does
  not exist (to-do); T5 C&L mapping off-calibration (λ_crit=0.07 vs λ=0.86 — verified in D7 JSON);
  τ not a primitive; Back isomorphism maps window→κ not τ; κ†=0.58; D7 symbol labels wrong.
  Orchestrator note: A1's "attenuation a fortiori" is for the Quiet→Public margin; my τ=1 vs τ=0
  experiment (Public flagged vs pooled = window margin) shows the reverse for ω_P≤0.29 — both go in.
- 06: A2 lit referee DONE (opus, 51 tool uses) → research/review_v3/lit_referee.md. C1 "first
  formalization" WRONG (Kyle–Vila 1991; Back et al; Cetemen et al JF 2026); C2 overclaim (Maug 98,
  Mello–Repullo 2004 "Activism non-monotonic in liquidity", Massa–Xu, HMN); C3 gap quotes verbatim
  (Ecta p.1454, RFS p.1891); C4 Burkart–Lee has no measurement section; C6 C&L has a liquidity entry
  cost; C7 Goldstein 2023 lists RPE measurement, not corporate-control frictions; Ben-David has 4
  authors; Burkart–Lee absent from bibliography.bib. Kahn–Winton unchecked (image PDF).
- 07: A3 novelty scan DONE (opus, 40 tool uses; ego-browser used for SSRN/Scholar/SEC) →
  research/review_v3/novelty_scan.md. "No SSRN-visible empirical work" FALSE: Trivedi SSRN 6866499
  (Jun 2026) pre-registered DiD on the Feb-2024 change (13G control; +0.35 share within 5bd; nulls on
  spreads); Polk–Buchheit–Riley–Stone published JFRC 32(4) 2024; "one WP" = Corum (Cornell) SSRN
  4319599; Bishop–Fos–Jiang–Partnoy 2026 (HSR margin); confounds incl. EDGAR 10pm cut-off change,
  13D/A 2-bd deadline. Theory triple (deadline × liquidity × premium) still unclaimed. arXiv unswept.
- 08: A4 empirics referee DONE (opus, 19 tool uses; ran disk data) → research/review_v3/empirics_referee.md.
  Data findings: half-year median CAR shows NO break at 2024-02-05 (2024H1 1.0% < 2023H1 1.7%); the
  1.6→2.6 medians are 21-day-window CARs; main-spec sample = 989 events / 301 post / 7 month clusters;
  F1 rests on 188 parsed (Manski bounds overlap; parse rate>0.72 needed); F1 replicates on full universe
  with pre-trend (31.9%/35.7%/70.6%); pct_of_class regex bug (100% → 0.0; 448 rows at 2.6%); H1 is
  before/after not DiD; 13G invalid control; 10pm cut-off + anticipation confounds missing; H2 ratio
  ill-defined; H3 underpowered + outcome-conditioned; 4/10 calibration rows have no model counterpart;
  G&S 18.1% vs Boyson 70% are non-comparable objects; CDF 7% is a 60-day run-up.
- 09: A5 facts verifier DONE (sonnet, 103 tool uses, 246k tokens) → research/review_v3/facts_verification.md.
  35 SUPPORTED / 2 WRONG (Boyson "70% within 2 years" — paper says "over one-third"/22%; C&L "+7.7pp"
  is "7.7 percent" relative) / 1 MISCITED (Norli 0.33→0.73 is baseline probit, not IV) / 3 partial
  UNCHECKED (BLV pub status; Massa–Xu "public bidders"; HMN exact −4.5pp). Orchestrator check: local CDF
  text is NBER WP 18452 (2001–2010, run-up 7% over (−60,−1)); JF version sample differs (per A4).
- 10: Dispatching Stage B verifiers: B1 (opus) refutes theory findings incl. orchestrator's τ=1 vs τ=0
  result; B2 (opus) refutes lit/novelty/empirics/facts decision-critical claims (re-runs data checks).
- 11: B1 verify-theory DONE (opus, 21 tool uses): 14 CONFIRMED / 1 MISCITED (the "channel-(A) peak 0.60"
  label — 0.60 is Dmin's argmax on D8's coarser grid) / 0 WRONG. O-1 and O-2 reproduced independently
  (ratios 1.064/1.184/1.136/0.378; jump 0.331/0.391/0.421). Also: τ symbol clash with δ=e^{−rτ}.
  Referee report + memo draft (scratchpad framework_v3_new.qmd, 635 lines) updated accordingly.
- 12: B2 verify-facts DONE (opus, 49 tool uses; ego-browser for SSRN/SEC): 18 CONFIRMED / 2 MISCITED
  (1,226 vs 1,381 window count; pct spike 2.59×438) / 1 WRONG (JF sample guess) / 0 UNCHECKED. Bonus:
  published CDF JF 2015 (1994–2010) reports run-up ≈3%, jump ≈2.5% — memo's 7%/3% are 2012 NBER WP
  numbers. Trivedi/Polk/Corum/Bishop et al. all confirmed; Kyle–Vila & Mello–Repullo exist; bib lacks
  Burkart–Lee and Ben-David. Memo draft + report corrected. Next: install v3.1, render, sync md, B3 check.
- 13: B3 memo-consistency check DONE (sonnet, 17 tool uses): 49/55 match; 4 citation-precision fixes
  applied (Back σ²T quote pp.1452–1453; dilution symbol ϕ; draft l.1010; v3 quote wording); TV series
  restated from the kD=2.26 start (0.0176→0.0040 vs 0.0165→0.0106, endpoints reproduced by B1).
  framework_v3.qmd/pdf/md re-rendered (16 pp). Referee report final.

## End of session (2026-08-19)
Deliverables: quality_reports/reports/2026-08-19_framework_v3_referee_report.md (referee report);
framework_v3.qmd/.pdf/.md revised to v3.1 (original at quality_reports/rewrites/framework_v3_pre-review_2026-08-19.qmd);
agent reports research/review_v3/*.md (5 finders + 3 verifiers). Agents used: 8 (A1–A5, B1–B3):
opus ×6, sonnet ×2; verification caught 1 label error (κ† "channel-A"), 3 number/locus slips, and 4
citation-precision items in the revised memo; no substantive finding refuted.
Open for the owner: choose the paper's primary margin (τ_θ vs τ_w); derive the disclosure-jump slope;
resolve (A5)/δ; re-anchor calibration; parser fixes; H1 calendar-time figure. Unchecked residue listed
at the end of the referee report.
