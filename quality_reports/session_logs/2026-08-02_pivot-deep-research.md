# Session log — 2026-08-02 — pivot deep-research (ringer)

**Goal:** validate pivot.md (GPT-5.6 Sol Pro's recommendation to abandon the liquidity-hump
paper and pivot to "Disclosure Before the Bid") on positioning, soundness, and
best-in-timeframe, via a ringer swarm with UCL full-text literature access.
Plan: `quality_reports/plans/2026-08-02_pivot-deep-research.md`.

## Incremental notes
- Boss read pivot.md (full) + draft_v2.pdf pp.1–20 + June-10 two-path decision report +
  competitor scope tables + HANDOFF.md.
- **Found:** `draft_v2.tex`, `HANDOFF.md`, `requirements.txt` were locally deleted (tracked in
  git, missing from working tree). Restored draft_v2.tex + HANDOFF.md via `git checkout --`
  (committed content; needed as worker source material). Left requirements.txt as-is.
- **Discrepancy logged:** −13.7% (5.2pp) premia finding attributed to AFS 2022 (June verified
  journal + scope tables) vs Celentano–Levine 2025 (draft §2.3, pivot). Must resolve from full
  texts — load-bearing for pivot's Prop 1 motivation.
- **Tension logged:** June-10 strategy = "J–S owns the σ²T/2024-acceleration framing, keep it a
  de-risk fact"; pivot = put the 2024 reform at the paper's center. Adjudication is the heart
  of Q1/Q3.
- HANDOFF open items relevant to pivot feasibility: WRDS/CRSP access unconfirmed; Bloomberg
  M&A inventory unrun; C–L full read was still on the author to-do list.
- **Corpus assembled** (boss, browser UCL SSO + curl): celentano-levine-2025 (SSRN 5506659),
  polk-etal-13d-acceleration (SSRN 4596959 = Polk, Buchheit, Riley & Stone projection paper),
  ordonez-calafi-bernhardt-2022-jfqa (open access), bonetti-duro-ormazabal-jar2020 (ECGI; note:
  PUBLISHED JAR 58(1) 2020, pivot undersold it as a WP), sec-33-11253-final-rule,
  sec-13dg-cdi-2025.txt (C&DI page, last update 2026-07-09 — newer than pivot's Feb-2025 ref).
  All converted to lit/txt/. hhab039.pdf confirmed = Burkart & Lee RFS 2022. ScienceDirect
  CAPTCHA'd (won't bypass) → Schwert/Greenwood-Schor/Gantchev delegated to web workers via
  author copies.
- **−13.7% attribution RESOLVED pre-swarm:** C–L 2025's own text: "Bid premia are 13.7 percent
  (5.2 percentage…" → the number is Celentano–Levine's; June scope-table attribution to AFS was
  wrong; draft §2.3 and pivot.md are right. (Detail check still delegated to L3a.)
- **Ringer run FIRED:** run_name pivot-deep-research, 13 tasks, max_parallel 6, identity
  fable-boss. Lanes: sonnet×5 (L1/L3a/L3b/L4/L6-web), opus×3 (T1 attacks w/ executable proofs,
  T2 max-effort model referee, E1 identification), deepseek×4 (L2/L5/L7/E2), k3×1 (T3 second
  opinion). ZERO codex lanes (GPT-correlation guard). Checks: quote-grep validators + executed
  proof scripts. Manifest: C:/Users/ALi/.ringer/work/pivot-deep-research/manifest.json.
- Restored requirement: system python needed numpy/scipy for T1 proofs (venv was deleted with
  requirements.txt); numpy in, scipy installing in background at launch.
- Next: monitor run → boss synthesis → ONE Fable-max red-team via ringer claude lane → final
  report at quality_reports/research/2026-08-02_pivot-deep-research-report.md.

## Run results (13 tasks: 11 pass, 2 check-root-cause fails both recovered boss-side)
- L4 "fail" = my validator only whitelisted repo paths while the spec told the worker to save
  fetched texts to ./fetched/ → re-validated with taskdir allowed: PASS (8 claims, 7 verified).
- T1 "fail" = proof suite needs ~45min; check subprocess cap 2400s → boss rerun exit 0, all
  9 verdicts proof-consistent. Both annotated in ~/fleet/swarm/docs/MODEL-NOTES.md.
- **Headline findings** (full synthesis: quality_reports/research/2026-08-02_pivot-deep-research-synthesis.md):
  1. Novelty gate OPEN — no realized-outcome 2024-reform paper exists (L6 null, ~40 searches).
  2. June's "J-S owns σ²T" blocker was a PHANTOM — not in the J-S text at all (L3b); traced to
     the draft's own line-130 gloss (L5). The 2026-06-10 decision report's key constraint dissolves.
  3. The pivot's page-1 headline (capitalization) is OCCUPIED — C-L 2025's own text asserts the
     capitalization reading of their −13.7%/5.2pp; "completion up, premium down" already in
     Corum-Levit 2019 fn.29; "activist as broker" is Burkart-Lee's verbatim headline.
  4. T1 executed proofs: pivot's attacks A3/A4/A5 CONFIRMED (A4/A5 stronger than pivot argued),
     A1/A2/A6* PARTLY (facts right, severity overstated; several draft defects found that the
     pivot missed: line-971 contradiction; near-flat σξ=0.60 "counterexample"; rem:A5margins
     arithmetic slip).
  5. T2 (opus-max) + T3 (kimi) convergent: mini-model as specified = identity + assumed
     cross-partial + assumed sign + signaling problem unmentioned; FIXABLE via dealer/deadline
     microfoundation; "the window is the paper".
  6. E1: exposure design infeasible as written (1.65 filings/entity; MDE 17-31pp on 17pp base);
     treatment intensity ~0.1pp of shares outstanding on population average; mechanical
     decomposition artifact runs OPPOSITE to the prediction; fix = target-level required-
     trading-days exposure + activist×quarter FE + measurement-first outcomes.
  7. E2: CRSP/WRDS unconfirmed = kill gate; chronology "comparative advantage" not in this repo;
     26-week schedule not executable as written.
  8. Draft's own referee exposure (L5): Corum-Levit mischaracterization contradicts the
     contribution sentence (kill unless narrowed); AFS premium misattribution at lines 101/130.
- Boss recommendation (pre-red-team): adopt pivot DIRECTION, reject CONFIGURATION; window-
  deadline paper + measurement-first reform empirics; current draft frozen as standalone WP.
- Fable red-team fired (one-task manifest, claude:fable, --effort max) — the single budgeted
  Fable call; awaiting adjudication.

## End of session
- Fable red-team PASSED attempt 1 (9.6 min). It confirmed the direction and overturned my
  framing with the swarm's own evidence: (1) "the window is the paper" inverted → **the reform
  is the paper; the window is the model**; (2) sequencing inverted → pre-registered EDGAR-only
  first-stage pass BEFORE model writing (highest-regret error identified: theory-before-first-
  stage for a solo part-time author when null-on-behavioral-margins is the modal world);
  (3) named the JMP headline: chilling/substitution dose-response + Item 6 derivative
  substitution, adjudicating DERA's $810M/yr projection; (4) two process gaps: advisor
  ratification = gate zero (kill-severity), and a bounded hygiene pass on draft_v2.tex before
  freezing (T1-confirmed false statements live in a public repo); (5) re-baselined clock:
  9 months to draft, Mar 2027 = milestone talk.
- FINAL REPORT: quality_reports/research/2026-08-02_pivot-deep-research-report.md
  (supersedes the synthesis file, which is kept as the pre-red-team record).
- MODEL-NOTES annotated (L4/T1 recorded fails = check-root-cause; sonnet/opus/deepseek/k3 lane
  observations). Second Fable call NOT used — no impasse arose.
- Open item for the author: confirm whether merger-chronology tooling exists in other repos
  (Gorbenko/M&A projects); E2 verified it does not exist in this one despite pivot §6.3's claim.

## Outline build (same day, second job)
- Deliverable: proposal/outline.tex + outline.pdf. Rounds: A (5 workers), B (qwen+deepseek),
  B2 swap (sonnet), C (Sol review), Fable gate pending.
- Luna: categorically unavailable on this ChatGPT plan (codex exec 400s on model 'luna') →
  bib swapped to deepseek (passed: 32 keys resolve under biber). MODEL-NOTES annotated.
- Qwen: double 3600s timeout on the lit synthesis (19KB partial, no grounding record) →
  swapped to sonnet per user rule (passed: 2,592 words, 14/15 quotes verified). MODEL-NOTES:
  task-shape mismatch, lane narrowed not cut.
- Boss catches during integration: framing.tex garbled Schwert-additivity vs BETT14-
  substitution into one sentence (fixed); lit.tex EFZ-2013 mischaracterization (fixed);
  master needed xcolor for hyperref blends (fixed). "Since 1968" claim verified in SEC txt.
- Full compile: 25pp, 0 errors, 0 undefined refs. W2 model sanity script executed (40% cost
  factor for 7->5 BD). Sol (GPT) adversarial review running; then ONE Fable-max gate.

## GPT-lane probe + Sol review integration (same day, cont.)
- User: "probe the problem of gpt". ROOT CAUSE of the sol/luna 400s: manifests wrote bare tier
  aliases (-m sol / -m luna); codex 0.145.0 requires full slugs gpt-5.6-sol / gpt-5.6-luna
  (registry canonical keys). The "not supported when using Codex with a ChatGPT account" error
  text was misleading --- the account is fine (the desktop config's own default IS gpt-5.6-sol).
  Earlier MODEL-NOTES "account-blocked / named-tier DOWN" entries were wrong; corrected in place.
- Guards landed: registry marks codex:sol/luna/terra as noncanonical routes (lint-negative
  fixture proves lint now rejects bare aliases, naming the canonical route); ringer config sets
  codex model_default=gpt-5.6-sol (an omitted model now emits an explicit -m instead of riding
  the desktop's Sol-at-MAX default). New Windows check rule: cmd.exe parses && || { } inside
  bash -c single quotes --- checks must be single commands (python validators); documented in
  the config header. First probe attempt's 2 FAILs were exactly this check bug (annotated
  CHECK-ROOT-CAUSE in MODEL-NOTES).
- Validation: codex-lane-probe rerun 2/2 PASS first-try with served-model identity assertion
  (sol 27.8s, luna 32.8s). W5b adversarial review PASSED on Sol (336K tokens, 8 findings, 14
  checks) --- the "let GPT contribute" requirement is satisfied by Sol itself.
- Sol findings adjudicated: F1 CONFIRMED kill (statutory clock starts at the 5% crossing;
  re-timed model+framing+empirics+abstract; RTD formula and design unchanged); F4 confirmed
  (Amihud sign prose); F5/F6/F7/F8 accepted (equal-billing, C-L table cell, RTD notation,
  workplan critical-path re-scope); F2 REFUTED (abstract is not empty); F3 REFUTED as stated
  (SEC 7742-44 supports 29%-within-5BD; denominator parenthetical added; W3 grounding record
  was already correct).
- Repo edits isolated in worktree outline-sol-fixes per the background-session guard; delivery
  via branch + draft PR.
- Fable gate on the worktree revision: SHIP-WITH-EDITS (891s, high confidence). G1-G11 applied
  boss-side: P0-anchor contamination diagnostic + 120-day robustness; ADV window lagged to six
  months ending 60 trading days pre-trigger (extends CDF-2015 caution to the exposure measure);
  Myth-1 residual phrasing; R2(ii) benchmark-increment clause; Gate-2 vs workplan wording;
  CRSP cell de-killed to cut-order fallback; bett2014 cite removed from Item-6 battery;
  conclusion 29%-vs-80% disambiguated; nested abstract env removed (doubled page-1 heading);
  R1 gloss + R6 envelope corner-case caveat. Final compile 0 errors / 0 undefined refs.
- NOTE: a parallel fix set (different notation) was applied to the MAIN checkout outside this
  session while the gate ran; this branch is the Fable-gated version; reconcile by diff before
  merging.
