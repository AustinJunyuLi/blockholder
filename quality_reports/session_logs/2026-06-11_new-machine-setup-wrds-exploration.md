# Session Log: New-Machine Setup, Handoff Execution, WRDS Access Exploration

**Date:** 2026-06-11 (session started late 2026-06-10)
**Branch:** jmp-upgrade-2026-05
**Machine:** macOS (Austins-MacBook-Air) — the "new machine" of HANDOFF.md
**Status:** Machine-actionable handoff items COMPLETE; Fact 2 unblocked

## What was done

### Repo sync + staleness cleanup
- Pulled `0ce5741 → 2a9014b` (fast-forward; all milestone work landed locally). Cleared a stale `.git/index.lock` and three untracked-file collisions (two plan files byte-identical to incoming; one outdated R-pipeline `AGENTS.md`).
- Removed stale scratch (user-authorized, moved to Trash): `presentation_bones.html`, `presentation_guide.html`, `draft_v2.docx` (re-exportable). Kept: `pres/blockholder_seminar_40min.pptx`, `lit/*.pdf`.

### Fresh-machine verification (HANDOFF §3) — all gates pass
- `make venv` + `make all`: **16 CSVs + 15/15 figures** regenerated.
- `d7_takeover_game_check.py`: **ALL CHECKS PASS** (λ≈0.8614, wedge 0.20, λ_crit≈0.07 — matches origin).
- `d8_ge_dominance_check.py`: **ALL CHECKS PASS** (certified region [0.30,0.85] exact / [0.35,0.825] inversion-free; troughs at σ_ξ=0.60 — matches origin).
- LaTeX with **working biber** (broken on origin RHEL10): `draft_v2.pdf` 90 pp, 0 errors / 0 undefined refs / 0 undefined citations / 0 biber warnings; `pres/presentation.pdf` 50 pp, 0/0/0. Page counts grew 88→90, 48→50 vs origin because citations now resolve.
- Per-machine font fix (macOS variant of HANDOFF note): copied TeX Gyre Heros otf (regular/bold/italic/bolditalic) from TeXLive 2026 → `~/Library/Fonts/` (XeTeX on macOS resolves family names via Core Text, not fontconfig).

### Lit downloads (handoff item 2, download part) — complete
- `lit/johnson-swem-2021-jfe.pdf` (author site, 2.2 MB, 42 pp).
- `lit/albuquerque-fos-schroth-2022-wp.pdf` (ECGI, 1.05 MB).
- `lit/celentano-levine-2025-ssrn.pdf` (SSRN 5506659 via browser session; SFI RP 25-81 rev. 17 Nov 2025, 62 pp, 4.1 MB). Scope-tables header updated accordingly.

### WRDS/CRSP access exploration (handoff item 3) — CONFIRMED, Fact 2 unblocked
User logged into WRDS (UCL account) in a Claude-driven Chrome session. Findings:
- **CRSP Annual Update, Daily Stock File (CIZ v2): accessible**, coverage through 2025-12-31 → fully covers Fact 2 sample (2022-01-01→2025-12-31). Quarterly product `crsp_q_stock` NOT subscribed (view-only form) — not needed.
- **Compustat–Capital IQ (276 items) + CRSP/Compustat Merged: subscribed** → CIK→GVKEY→PERMNO path available.
- **SEC Analytics Suite: NOT subscribed** (no CIK–CUSIP link table). Mitigation: Compustat path, or (preferred) extend `empirics/parse_13d.py` to extract subject CUSIP from 13D cover pages — `fact1_filings.csv` currently has `subject_cik` but no CUSIP.
- **Event Study by WRDS, "U.S. Daily Event Study: Upload your own events": accessible** (requires only CRSP daily, any frequency; accepts PERMNO/CUSIP/TICKER + date upload; custom estimation/event windows) → can produce market-model CARs for the 13D sample directly.
- Bonus: subscriptions include a "Blockholders" dataset (1 item), Thomson/Refinitiv 13F, TRACE, FactSet, Preqin. No TAQ (Amihud from CRSP daily, as designed).
- Design note updated in place: `quality_reports/plans/2026-06-10_fact2-event-study-design.md` (status + data-requirements section).

## Remaining author-only items (unchanged from HANDOFF §6)
1. Full reads of C–L / J–S / AFS against the checklists; validate ◑ cells; finalize positioning memo (PDFs now all in `lit/`).
2. Bloomberg checklist at a terminal (item 2d).
3. D7/D8 mathematical-owner review + G1/G2 sign-off in a session log.
4. Milestone talk rehearsal (~Mar 2027).
5. (Origin machine only) `libxcrypt-compat` fix — irrelevant on this Mac; both docs compile clean here.

## Fact 2 execution (authorized by author this session; in progress)

**EDGAR leg.** `parse_13d.py` extended (CUSIP with check-digit voting, subject/filer names, `<ACCEPTANCE-DATETIME>` with after-16:00-ET next-business-day shift); new `empirics/fact2_events.py` (full 2022Q1–2025Q4 SC 13D universe, ~9.2k originals, resume-safe). **Two parser-layer discoveries:**
1. EDGAR renamed the form type to `SCHEDULE 13D` from Dec 2024 (voluntary XML era starts mid-2024) — and the new names overflow the legacy 12-char form.idx column, so fixed-width reads conflate amendments with originals. `list_filings` rewritten boundary-aware. **2025 would have been silently empty otherwise.**
2. New-era rendered cover pages defeat the event-date label regex (Fact-1 delay stats sparse for 2025 — future fix), but CUSIP parses at ~90% there (XML tag + cover voting).

**WRDS leg (dry-run validated end-to-end on the 39-event smoke sample).**
- U.S. Daily Event Study "upload your own events": query 11385273, Success in 6s. Output echoes CUSIP (`Model,cusip,uid,evtdate,date,evttime,ret,abret`; uid = `<permno>-<DDMONYYYY>`, "." for unmatched) → direct merge back to filings; 22/39 matched (misses ≈ foreign CINS G/M/U-prefix codes, expected). Parameters: CUSIP ids, DD-MMM-YYYY, Market Model, est 220 / min 100 / gap 20, window [−10,+10].
- CRSP annual Daily Stock File by PERMNO file upload: query 11385294 (28 dry-run permnos, 2021-01-01→2025-12-31, 14 vars incl. CIZ share-class fields for the shrcd-10/11 filter).
- Browser-automation notes (these forms fight visual clicks): drive `#wrds-query-form` via JS; the method-3 file input is `disabled` until enabled; method-2 text codes sync through a tom-select control that eats tokens; check variable checkboxes by `value` across the per-category group names; submit via the "Submit Form" button's `.click()`.

`empirics/fact2_analysis.py` written (CARs from per-day ABRET; Amihud [−250,−30] ×1e6, run-up [−60,−11], ln cap at −30; CIZ common-stock filter; CGM two-way clustered OLS by subject permno × calendar month; house-style CAR-path figure). Loader validated against the dry-run output.

---

## Continuation (overnight): goal = milestone e2e + paper validation + math + slidepack

### Fact 2 executed end-to-end (real data)
- CRSP full-universe panel (11.9M rows, 1.13 GiB; query 11385294, document **27466021** — the first download attempt used 27465938, which is the uploaded-permno echo) → `empirics/data/crsp_daily.csv`; `load_crsp()` rewritten to chunk-filter by matched PERMNOs (11.9M rows → 23K in 5.6s via `usecols` + 2M-row chunks).
- EDGAR universe complete: 9,234 originals, 86% CUSIP, 5,058 pre / 4,176 post, 3,518 unique upload pairs.
- **WRDS upload battle (event-study form, query 11385426, Success, 4.2 MiB):** Chrome PNA blocks page→localhost fetch even with `Access-Control-Allow-Private-Network` (request reaches the server; response withheld; renderer wedges) — do NOT use localhost bridges from WRDS pages. `file_upload` MCP tool rejects host paths (schema drift). What WORKS: gzip+base64 the file, ship it into `window.__chunks` in ≤5KB JS string chunks with **per-chunk SHA-256 verification in-page** (22KB single-shot transcription drifted; 5KB chunks were byte-perfect), then `atob → DecompressionStream('gzip') → File → DataTransfer → input.files + change event`, gzip CRC + full-file SHA-256 as gates. Field recipe re-confirmed: identifier=cusip, DATE11, model=m, est 220/min 100/gap 20, window −10..+10, variable groups `0165166b…_0/_1` (13 boxes), submit via button `.click()`.
- **Results (1,513 events; 843 pre / 670 post):** mean CAR[−1,+1] 0.85%→1.71% (β>0, t≈1.1 n.s.); CAR[−10,+1] 4.6%→12.6%; **ln Amihud −1.4pp, t=−3.7** (robust across specs/windows — surprises concentrate in liquid names); Post×ln Amihud **precise null** (δ̂≈+0.2pp, t=0.48 — the δ<0 prediction not supported; reported honestly in both decks).

### Paper validation (3 background deep-readers; reports in `lit/reads/`)
- **Two load-bearing misattributions found and fixed everywhere** (scope tables, slides 2b/Theorem A/summary, draft §lit ×3, D7 appendix): (1) the −13.7%/5.2pp premium effect is **Celentano–Levine (2025) p. 22/Table 4**, not AFS — AFS contains no takeover/premium analysis at all; (2) the "13D-window ↔ σ²T isomorphism" does **not exist** in Johnson–Swem — the framing is unowned. The 2026-06-10 "verified-claim journal" (3-vote, '0 refuted') passed both errors → treat adversarially-verified secondary-source claims as unverified until full-read.
- All ◑ cells resolved; threat levels: C–L MEDIUM (rival mechanism for the negative-premium fact; differentiate via (q,γ,ψ,κ) cross-sections + the selection/treatment-split endogeneity point), J–S LOW, AFS LOW (their conclusion literally names our agenda as future research). Validated positioning memo appended to `lit/competitor_scope_tables.md`.

### Math validation ("work over the math"; reports in `quality_reports/reviews/`)
- **D7 review (SOUND-WITH-ISSUES, 1C/3M/6m):** top-up deviation falsified Lemmas d7:floor/entry/bloc as stated (raider can buy out a blocking bloc at its reservation) — λ formula SURVIVES via the outside-option principle. Fixed: lemmas restated with the corrected raid set; α<τ_c made a stated primitive (+ code guard in `takeover_game.py`); Prop d7:afs's P′>0 clause restricted to the λ→0 limit; A5a citation fixed; discriminatory-offers ledger sign corrected (discrimination ⇒ λ=1, equal treatment is the conservative case); ρ²-fold identification flagged as open (single-ρ alternative: Δ_eng 0.516→0.46, signs unchanged). Check script upgraded: top-up BR check + φ-two-edged check — **7/7 PASS**.
- **D8 review (SOUND-WITH-ISSUES, 0C/4M/12m):** certificates and counterexample fully reproduced (trough multistart spread 5.7e−9). Fixed: "sign changes exactly once" weakened to ε-localized single-peakedness (statement+proof+manuscript×3+fig caption); (R0) single-crossing made an explicit grid-verified hypothesis; eq:d8-weights missing (m̃−m₀) factor inserted; rem:d8-signs restated with true equilibrium-cell numbers (t>0 on 5/7 cells; e_D sign positive); grid-sample honesty + collapsed-Hold note + sub-interval R2 margin (3.28e−3 vs 3.75e−4) + grid-limited vs failure-limited asymmetry. Script upgraded — **ALL PASS**.
- **Manuscript sweep (51 results inventoried; 4C/10M/9m) — all CRITICALs fixed:** C1+C2 (the §6.4 reclassification block assumed bids only on D=1, contradicting eq:bid-prob and prices.csv): lem:reclass-jump re-derived with both bid lotteries — Σ_P−Σ_Q = (p₁*−p̄_Q)(S̄−K−E[v|k_D]−Δ̃) + σ_ξ(φ(T₁)−E_zφ(T_{X,0})) = **+0.064 at baseline** (screening +0.19 vs foregone selection −0.12), now *increasing* in s, restoring Cor 1(a) and keeping Prop 8's underdisclosure; economics reframed option-creation → **bid screening**; first-best rule corrected ((1−p̄_Q)Δ̃ ≥ C(s); −m̃ transfer dropped = M1). C3 (D5's Λ>0 premise false): Λ≡0 at fixed prices — A2 is *exactly* the persuasion-regime condition; flat cost ⇒ two-cutoff collapse face; body §2 + prop + taxonomy aligned. C4 (stale D6 numbers): disclosed p* is **0.0131** not 0.847 — lem:BP-BQ's condition holds *comfortably*; slope ordering restated via eq:U-affine (η conditional, M5); rem:A5margins recomputed (binding cell = Exit (−2,0): 0.766+0.27≈1.04>1, so A5a stays maintained-not-derived; disclosed branch ≈0.18). MAJORs M2/M4/M6/M8/M9/M10 + minors m1–m4 all fixed; stale `D2_welfare_numerics.md` marked SUPERSEDED; D4 ledger's "λ open" line updated (resolved by D7).
- Decks' hardcoded baseline table was stale (old calibration) — refreshed from prices.csv in both decks (disclosed p = 0.01!).

### Slidepack (40-min, two formats; design: `quality_reports/plans/2026-06-11_slidepack-40min-design.md`)
- **Beamer** (`pres/presentation.pdf`, 56pp, 0 errors/0 undefined): de-milestone-ified; 13D window fact updated (10cd→5bd); Evidence act added (E1 Fact 1 + E2 Fact 2, real numbers, honest about the null); positioning slide rewritten post-validation; 3 new backups (tender game w/ corrected equilibrium, certified-region method, facts data&methods) + new category divider; backup links from Theorems A/B; overflow QA'd page-by-page.
- **PPTX** (`pres/blockholder_seminar_40min.pptx`, 35 slides, rebuilt from scratch by new `pres/make_pptx.py`): business idiom, 23 main + 11 backups + divider, Tol-palette chips/panels, 13 figures rasterized at 300dpi via pdftocairo into `pres/pptx_assets/`; **reads Fact 1/2 numbers from empirics outputs at build time** (rerun after any data refresh); original user pptx backed up at `/tmp/blockholder_seminar_40min_ORIGINAL_2026-06-11.pptx`.
- Manuscript recompiled clean: **93pp, 0 undefined** (was 90; growth = corrected derivations + ε-localization text).

### Open / follow-ups
- D7 ρ²-vs-single-ρ fold: author decision (flagged in D7 ledger + review).
- D8 reviewer's optional hardening: multistart at trough cells in-script, `_root()` loud-fail, Lipschitz bridging near loose-bound edges.
- Manuscript m5 notation renames (T(π) D1-vs-D5, W(s), three g's) — flagged, not executed (invasive).
- Fact 2: prediction 3's interaction is a null — consider model-side discussion (composition shift post-rule: smaller, slightly more illiquid names) and a robustness pass (winsorized CARs, placebo dates) before using in the paper text.
- Fact 1 full-universe recompute (currently sampled windows) is a flag change away.
