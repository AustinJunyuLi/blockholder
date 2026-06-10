# Session Log: Nine-Month Milestone — End-to-End Execution

**Date:** 2026-06-10
**Branch:** jmp-upgrade-2026-05
**Status:** COMPLETED (Claude-side deliverables); author handoffs listed below
**Plan:** `quality_reports/plans/2026-06-10_nine-month-milestone-implementation.md`

## What was executed (all four workstreams)

### Workstream A — Theorem A (wedge microfoundation) ✅
- `quality_reports/fixes/D7_takeover_game_spec.md` — game spec note.
- `quality_reports/fixes/D7_takeover_game_microfound.tex` — **the disagreement-node tender game, solved**: free-rider floor (Lemma), dilution-financed state-blind entry q = H(φ) (Lemma), blocking rule (Lemma), threat-point shift with **λ = 1 − q(1−γ)ψ** (Proposition), Condition BG's form derived (Corollary), **A3 iff-boundary** (Theorem: fails only if raids certain + superseding + unblockable), exact ρ-fold consistency (Remark), **AFS reconciliation** (Prop d7:afs: measured premium m̄/P falls in activism evidence for λ < λ_crit), comparative statics + testability remarks, honesty ledger.
- `d7_takeover_game_check.py` — **ALL PASS**: MC-vs-closed-form (err 5e-4), bounds/monotonicity, 48-cell iff-boundary exact, calibration consistency (wedge 0.20 from θ=0.5, q=0.5, γ=0.6, pivotal, λ≈0.861, Δ_eng≈0.516), AFS reversal region nonempty (λ_crit≈0.07 for full-range reversal at baseline).
- `numerical/takeover_game.py` + `export_wedge_primitives()` + fig15; spliced into draft (§Bidder Entry paragraph rewritten; App B honest-scope updated to point at solved game; `\input` after App B).

### Workstream B — Theorem B (GE channel) ✅
- `quality_reports/fixes/D8_GE_dominance_MCS.tex` — pricing-layer IFT under A5; cutoff-layer IFT with **inversion-free bound** |B| ≤ (ΣW)·‖∂_κT‖/(1−L); weight decomposition + conditional MCS signs; **region theorem** (R1 pointwise + R2 integral ⇒ strict single peak); **counterexample proposition** (σ_ξ=0.60 troughs with channel A single-peaked ⇒ Hypothesis 1 false globally); welfare-spillover note; ledger.
- `d8_ge_dominance_check.py` — **ALL PASS**: pricing IFT to 7e-11; **L_max = 0.836 < 1** (A6 quantified); B-residual ≡ B-IFT to 5e-6; **certified region [0.30,0.85] (exact) / [0.35,0.825] (inversion-free)** with R2 margin ~200×; **troughs certified at (0.60, {1.44,1.54,1.64})** with ∫|B| > A* in every cell.
- `export_ge_decomposition()` (+cellmap CSV) + fig14; spliced into draft (post-Prop-5 status paragraph; app:proof-d1-GE pointer; App C summary updated; `\input` after App C/d5).

### Workstream C — De-risk leg ✅ (one author-gated item)
- Lit: `johnson-swem-2021-jfe.pdf`, `albuquerque-fos-schroth-2022-wp.pdf` downloaded; **Celentano–Levine blocked by SSRN anti-bot** (author: one click, SSRN 5506659). 14 bib entries added to `bibliography.bib`; `pres/slides.bib` **recreated as a real file** (it had been a self-referential symlink, broken since the initial commit) with all 13 cited keys.
- `lit/competitor_scope_tables.md` (◑-marked cells await author full reads); `lit/bloomberg_checklist.md`; `quality_reports/plans/2026-06-10_fact2-event-study-design.md` (WRDS-gated); `quality_reports/plans/2026-06-10_positioning-memo.md`.
- `empirics/` package (stdlib-only EDGAR; throttled; raw data gitignored) + **Fact 1 produced** (150 sampled SC 13D originals per window; parse rates 0.68/0.64):
  - **Median delay: 7 → 5.0 business days** (snaps to the new deadline); mean 9.6 → 6.4;
  - **Share within 5 business days: 35.7% → 75.6%**; **p90: 23 → 11.1** (the long tail is what compresses);
  - Artifacts: `empirics/output/fact1_summary.csv`, `fact1_filings.csv`, `fact1_delay.pdf`. v0 caveats (sampled, regex parse rate reported) in `empirics/README.md`.
  - (First run had a form.idx fixed-width parsing bug — all fetches 404'd on malformed paths; fixed with a right-anchored regex and re-run.)

### Workstream D — Integration ✅
- Draft: abstract + intro + related-lit (structural-trio paragraph) updated; 2 new figure blocks; **compile gate: 0 errors, 0 undefined label refs, 88 pages** (XeLaTeX ×2).
- Presentation: +positioning slide, +2 theorem slides, Prop-5 status line, summary updated; figures copied; **compile gate: 0 errors, 0 undefined refs, 48 pages**.
- `CLAUDE.md` updated (takeover_game, empirics, 16 CSVs, D-series pattern). `make all` green: **15/15 figures**.

## Environment issues found & fixed/flagged
1. **biber broken on this host** (TeXLive packed binary needs `libcrypt.so.1`; RHEL10 ships only `.so.2`; sandbox correctly refused injecting an external RPM lib). Mitigation: all 35 draft + 13 slide cite keys verified present in the .bib files; **author fix: `sudo dnf install libxcrypt-compat`, then biber + 2 XeLaTeX passes clears the 82/15 citation warnings.**
2. **TeX Gyre Heros missing from fontconfig** — fixed user-locally (`~/.config/fontconfig/fonts.conf` → TeXLive font dirs + `fc-cache`).
3. **`pres/slides.bib` self-referential symlink** (broken since initial commit) — replaced with a real file.

## Author handoff list (cannot be done by Claude)
1. `sudo dnf install libxcrypt-compat` → rerun `biber draft_v2` + `xelatex` ×2 (and same in `pres/`).
2. Download Celentano–Levine PDF (SSRN 5506659) into `lit/`; **full reads** of it + Johnson–Swem + AFS against the checklists in `lit/competitor_scope_tables.md`; validate ◑ cells; confirm/adjust the positioning memo.
3. Confirm **UCL WRDS/CRSP access** (gates Fact 2 execution; design note ready).
4. Run `lit/bloomberg_checklist.md` at the terminal (decision-report open item 2d).
5. Review the two derivation records (D7/D8) as the mathematical owner — especially D7's institutional primitives (equal-treatment offers, GH selection) and D8's Theorem-region proof.
6. Gate decisions G1/G2 are effectively pre-met (both theorems landed); record formal sign-off in a session log when reviewed.
7. Milestone talk rehearsal (deck ready; `pres/blockholder_seminar_40min.pptx` adaptation optional).

## Verification artifacts
- `quality_reports/fixes/d7_takeover_game_check.json` — all_pass: true.
- `quality_reports/fixes/d8_ge_dominance_check.json` — all_pass: true (incl. baseline path rows).
- `numerical_output/data/ge_cellmap.csv` — troughs exactly at σ_ξ=0.60 ∩ S̄∈{1.44,1.64} on the 3×3 export grid.
- Compile logs: 0 LaTeX errors both documents; citation warnings = biber-blocked only.
