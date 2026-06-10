---
date: 2026-06-10
type: implementation-plan
status: EXECUTED 2026-06-10 (Claude-side deliverables complete; author handoffs in quality_reports/session_logs/2026-06-10_milestone-execution.md)
branch: jmp-upgrade-2026-05
title: "Nine-Month Milestone Implementation Plan (theory-led hybrid, due ~March 2027)"
inputs: 2026-06-10_two-path-feasibility-decision.md (§4); route choices confirmed by author 2026-06-10
---

# Nine-Month Milestone — Implementation Plan

## Context

The 2026-06-10 feasibility report settled the strategy (hybrid, theory-led) and fixed the 0–9-month deliverable:
**milestone talk (~March 2027) = two new theorems + a data fact + sharp positioning vs three named competitors.**

Author decisions taken 2026-06-10:
- **Theorem A route: Grossman–Hart free-rider tender game** (primary), BGP toehold variant as documented fallback.
- **Empirics live in this repo** under a new `empirics/` package; raw data gitignored.

Why this is feasible in 9 months — the repo already contains most of the scaffolding:
- Theorem A gap is *precisely characterized*: `draft_v2.tex` App. B (`app:bg`, l.2435–2646) proves the wedge from Nash bargaining **conditional on Condition BG** (appropriability λ>0, `cond:bg` l.2469–72; Thm `thm:bg-A3` l.2570–78: wedge = ρ²(1−θ)λΔ_eng). The draft's own words (l.2440–41): λ "can only be pinned by a complete tender-game equilibrium." Theorem A = build that tender game. Full derivation record exists: `quality_reports/fixes/D4_bargaining_microfound.tex` (906 lines) + verification scripts.
- Theorem B gap is *bounded and instrumented*: Hypothesis 1 (`hyp:d1-cutoffshift` l.900–910) feeding conditional Prop 5 (l.912–925); channel decomposition l.730–736; (C*) + Lemma 6 l.834–855; `app:proof-d1-GE` (l.2342–98) already has the C¹ cutoff map + computable residual bound. **Known: hump holds in 16/20 sensitivity cells, trough in 4/20 (all σ_ξ=0.60, driven by channel B)** — so the theorem must be region-sufficient-conditions + formalized counterexample, and the counterexample candidates already exist numerically. Records: `D1_prop6_GE_cutoffshift.tex`, `D1_prop6_condition_Cstarstar.tex`, IFT machinery in `D3_prop8_IFT.tex` (exact chain rule — reuse), `phase0_robustness_driver.py` (14-cell harness).
- Numerics: `m0=0.10, m1=0.30` exogenous (`numerical/params.py:123-124`); bidder primitives in place (`model.py:236-314`: ξ~N, entry threshold, surplus); generic 2D sweep template `_export_sensitivity()` (`export_data.py:249`).
- Missing entirely: gating literature in `lit/`+`bibliography.bib` (Celentano–Levine, Johnson–Swem, AFS 2022, Gantchev, CDF 2015, Bagnoli–Lipman, BGP, Milgrom–Shannon, Quah–Strulovici, Verrecchia, Dye, Kamenica–Gentzkow; Kahn–Winton PDF present but no bib entry) and any data code.

---

## Workstream A — Theorem A: microfound the wedge (GH free-rider tender game)

Goal: Condition BG's λ becomes a derived object; A3 (l.282) becomes a corollary; sign condition engages AFS's −13.7% finding.

| # | Task | Output |
|---|------|--------|
| A1 | **Game specification note**: bidder (synergy ξ over v + aρΔ), bloc (stake/toehold α, threat point = continued engagement value), atomistic dispersed shareholders (free-ride: tender iff offer ≥ expected post-takeover per-share value), dilution/exclusion device φ (GH 1980) or toehold profits. Timing aligned with model's t=0,1,2. | `quality_reports/fixes/D7_takeover_game_spec.md` |
| A2 | **Solve the tender game**: equilibrium acceptance + offer; derive required premium m(a) over P; λ = f(α, φ, θ, pivotality) closed form; **wedge sign condition** — m1−m0 > 0 iff engagement improvement is appropriable at the table rather than fully embedded in the free-rider floor (complements/substitutes vs bidder synergy). | `quality_reports/fixes/D7_takeover_game_microfound.tex` (derivation record, D-series pattern) |
| A3 | **Verification script**: every closed form checked numerically; calibration-consistency check that baseline (m0, m1) = (0.10, 0.30) is attainable from sensible primitives. | `quality_reports/fixes/d7_takeover_game_check.py` + JSON output |
| A4 | **AFS engagement proposition**: decompose the *measured* average premium effect of activism into conditional wedge (+) and deterrence/selection composition (−, via existing ∂p/∂π<0) + substitutes case ⇒ conditions under which average realized premia fall while the conditional wedge is positive. Numerical illustration (qualitative match to AFS −13.7%). | Section in D7 record + check in d7 script |
| A5 | **Numerics module**: `numerical/takeover_game.py` mapping game primitives → (m0, m1); endogenous-wedge mode alongside backward-compatible exogenous mode; new export `export_wedge_primitives()` + sensitivity-in-primitives figure (replaces "sensitivity to wedge" interpretation, l.1017). | `numerical/takeover_game.py`, export fn, `pyfig` fig15 |
| A6 | **Draft splice**: rewrite §Bidder Entry premium paragraphs (l.275–286) stating the game + result; A3 restated as corollary; App. B expanded from conditional theorem to full derivation; A4 synergy bounds restated in primitives. | `draft_v2.tex` edits |

**Gate G1 (end Sep 2026):** D7 has a closed-form wedge with sign condition, numerically verified. Fallback if stalled: (i) BGP toehold variant, or (ii) ship sharpened Condition-BG version — partial result "wedge sign = appropriability condition" with GH game as bounding case. Decision documented in a session log.

## Workstream B — Theorem B: sign the GE cutoff-shift channel (MCS + counterexample)

Goal: Hypothesis 1 → theorem with primitive sufficient conditions on a characterized region **plus** a formalized counterexample (σ_ξ=0.60 trough) proving tightness. Both outcomes are milestone-valid per the decision report ("MCS proof or a clean counterexample") — we deliver both halves.

| # | Task | Output |
|---|------|--------|
| B1 | **IFT cutoff derivatives**: differentiate the three indifference conditions F(k;κ)=0 → dk/dκ = −J⁻¹∂F/∂κ; J invertibility from A6 contraction (slack already verified numerically). Reuse exact-chain-rule machinery from `D3_prop8_IFT.tex`. | Part 1 of `quality_reports/fixes/D8_GE_dominance_MCS.tex` |
| B2 | **Sign ∂Δmin/∂k_i** explicitly (boundary terms of the region integrals — analytically tractable). | Part 2 of D8 |
| B3 | **Sufficient-condition theorem**: bound ‖dk/dκ‖ via the contraction modulus ⇒ computable bound on \|B(κ)\|; lower-bound channel-(A) amplitude under (C*); primitive inequality defining region R where the hump is a theorem. MCS toolkit (Milgrom–Shannon single-crossing; Quah–Strulovici interval dominance) to sign dk_i/dκ componentwise where obtainable. | Part 3 of D8 |
| B4 | **Counterexample formalized**: the σ_ξ=0.60 trough cells (draft l.2794, 2804) elevated to a verified counterexample — high-precision independent recomputation + interval bounds showing channel B overturns A there. | Part 4 of D8 + `d8_ge_dominance_check.py` |
| B5 | **GE-decomposition numerics**: `export_ge_decomposition()` computing channels A and B separately along κ across the (σ_ξ, S̄) grid (reuse `_export_sensitivity()` pattern + warm-start); hump/trough boundary map figure. | export fn + `pyfig` fig14 + Makefile updates |
| B6 | **Draft splice**: Hyp 1 → Theorem + counterexample subsection; update `app:proof-d1-GE`; tighten conditionality language in Props 7/8/10 *only where the new bound directly applies* (no full welfare rewrite — scope guard). | `draft_v2.tex` edits |

**Gate G2 (end Dec 2026):** region-theorem + formalized counterexample both stand. Degraded-but-shippable: counterexample + tightened computable bound only (still upgrades Prop 5's honesty and is presentable).

## Workstream C — De-risk leg (parallel, low intensity)

| # | Task | Output |
|---|------|--------|
| C1 | **Lit acquisition + bib**: download to `lit/`: Celentano–Levine (SSRN/SFI RP 25-81), Johnson–Swem, AFS (JFE 2022), Gantchev (2013), CDF (JF 2015), Bagnoli–Lipman, Burkart–Gromb–Panunzi, Milgrom–Shannon, Quah–Strulovici, Verrecchia, Dye, Kamenica–Gentzkow. Add ~12 entries to `bibliography.bib` + `pres/slides.bib` (incl. missing Kahn–Winton). | PDFs + bib entries |
| C2 | **Competitor scope tables** (Claude prepares; author does the full reads — they gate framing and the month-9+ structural commitment): claims, model objects, estimation scope, what each does NOT do, overlap matrix vs this paper. | `lit/competitor_scope_tables.md` |
| C3 | **Empirics scaffold**: `empirics/` package — `edgar_fetch.py` (EDGAR full-text/daily index pull of SC 13D/13D-A/13G; structured XML for filings ≥ Dec 18 2024; header/cover-page parse for older), `parse_13d.py` (→ tidy CSV/parquet: accession, filer, subject CIK, event date, filing date, %ownership, item-4 flag, cash-settled-derivatives flag), `facts.py`. `empirics/data/` gitignored; small derived summaries in `empirics/output/` committed. Deps: requests + lxml (+pandas already pinned). | `empirics/` package + README |
| C4 | **Fact 1 (descriptive)**: filing-delay distribution (filing date − event date) pre/post the Feb-5-2024 five-business-day rule; compression magnitude; 13D vs 13G composition. | summary CSV + 1 figure + memo paragraph |
| C5 | **Fact 2 (event study)**: 13D announcement-window CARs before vs after the acceleration (model prediction: shorter window → lower liquidity sensitivity of premia). Needs daily returns: **author confirms WRDS/CRSP access** (UCL); Bloomberg fallback; if neither lands by Dec, ship Fact 1 + design note only. | analysis script + memo section |
| C6 | **Open item from decision report (2d)**: Bloomberg function inventory — Claude prepares a terminal checklist (13D/G filing history, ownership history HDS/OWN, MA<GO> deals/premia, CACS, tick-history export caps); author runs it at the terminal. | checklist in `lit/` + author's notes |
| C7 | **Positioning memo**: one document framing this paper against the three competitors (AFS sign as explained quantity; Johnson–Swem anchor differentiation; Celentano–Levine scope split). Feeds intro rewrite + talk. | `quality_reports/plans/2026-MM-DD_positioning-memo.md` |

## Workstream D — Integration & milestone talk

| # | Task | Output |
|---|------|--------|
| D1 | **Manuscript integration** (after G1+G2): splice A6+B6; rewrite intro + related-lit around the three competitors; abstract; full rebuild `make clean && make all`; XeLaTeX×2+biber zero-undefined gate. | updated `draft_v2.tex` + figures |
| D2 | **Presentation update**: slides 11–13 (main result/decomposition/disclosure) reflect theorem status upgrades; +1 positioning slide; +2 theorem slides; refresh affected backups (hump-strictness backup l.905 etc.). | `pres/presentation.tex` |
| D3 | **Milestone talk**: adapt to required format (40-min seminar deck exists as `pres/blockholder_seminar_40min.pptx`); rehearsal pass. | talk deck |
| D4 | **Housekeeping**: keep D-series records + session logs current; quality report at merge time per project rules. | per templates |

---

## Timeline (Jun 2026 → Mar 2027)

| Month | Theory (primary thread) | Parallel (low intensity) |
|---|---|---|
| **M0** Jun 15–Jul 15 | A1 game-spec note; MCS toolkit notes | C1 lit+bib; C2 scope tables; **author starts competitor full reads**; C3 scaffold + parser v0 |
| **M1–M3** Jul–Sep | A2 derivation → D7; A3 verify; A4 AFS prop; A5 numerics | C4 Fact 1; C6 Bloomberg checklist; author confirms WRDS |
| **Gate G1** end-Sep | closed-form wedge + sign condition verified, else fallback | |
| **M4–M6** Oct–Dec | B1–B4 → D8; B5 numerics | C5 Fact 2; C7 positioning memo draft |
| **Gate G2** end-Dec | region-theorem + counterexample stand | |
| **M7** Jan | D1 manuscript integration; A6+B6 splices; full pipeline green | |
| **M8** Feb | D2 presentation; polish; one bounded review pass | C7 finalized after full reads |
| **M9** early-Mar | D3 rehearsal + **milestone talk** | |

## Division of labour

- **Author**: owns/reviews all proofs (Claude drafts, author validates — D-series pattern); full reads of Celentano–Levine + Johnson–Swem; WRDS/Bloomberg access + terminal inventory; route decisions at gates; talk delivery.
- **Claude (sessions)**: derivation drafts D7/D8 + verification scripts; all code (`takeover_game.py`, exports, figures, `empirics/`); bib/lit infrastructure; scope tables + memo drafts; draft/slide edits; compile/pipeline verification.

## Verification (every phase)

1. Every closed form in D7/D8 gets a numerical check in its paired `.py` script (established D-series pattern), outputs committed as JSON/TXT.
2. `make clean && make all` green; CSV row counts sane; NA-row handling intact.
3. Manuscript + presentation: XeLaTeX×2 + biber, **zero** undefined references/citations.
4. Counterexample (B4) independently recomputed at tightened tolerances (pure-Python path, no Numba) before being called a theorem-grade object.
5. `empirics/` parser validated against ~10 hand-checked filings spanning pre/post rule change and pre/post XML mandate; dedupe + amendment-chain logic spot-checked.
6. accel.py: while model equations are in flux, force pure-Python reference path; mirror into Numba only after G1/G2 stabilize (or document fallback).
7. Proofreading protocol (propose-only) before any commit touching `draft_v2.tex`/`presentation.tex`; quality gate ≥80 per project rules; review loops bounded (≤1 pass per integration milestone — budget guardrail).

## Risk register

- **Scooping (binding risk)**: Fos sits on both BCDFLL and AFS; Celentano–Levine at RFS. Mitigation: theory-first plan has zero data dependency; consider SSRN posting after M7 integration (author decision at G2).
- **A stalls** → G1 fallback (BGP variant / sharpened Condition BG). **B lands partial** → counterexample + computable bound is still shippable and honest.
- **Data access**: WRDS unconfirmed; Fact 2 degrades gracefully to Fact 1 + design note. Bloomberg inventory is an explicit open item (C6).
- **Re-check before month 9+**: "BCDFLL two-channel never estimated" and competitor scope (structural-leg commitment is *not* part of this plan).

## First executable chunk (next session)

M0: C1 (lit downloads + bib entries) → C2 (scope-table skeletons) → A1 (game-spec note) → C3 (empirics scaffold + parser v0 on a small EDGAR sample).
