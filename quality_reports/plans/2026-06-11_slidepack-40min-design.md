# Slidepack Design: 40-Minute Talk, Two Formats

**Date:** 2026-06-11
**Status:** APPROVED (executing under session goal)
**Deliverables:**
1. `pres/presentation.tex` — academic Beamer deck (UCL theme), narrative main + technical backups
2. `pres/blockholder_seminar_40min.pptx` — business deck, same narrative, figure-led (rebuilt by `pres/make_pptx.py`)

**Constraints from the author:** no mention of the nine-month-milestone framing anywhere
(titles, headers, "status upgrade" phrasing); a coherent 40-minute research talk; all
technical material in backups; main slides carry the narrative seamlessly. The TeX deck
reads academic; the PPTX reads business. Both well-motivated and self-contained.

---

## The shared narrative spine (40 min)

| Act | Minutes | Beats |
|---|---|---|
| I. Motivation | 5 | Activist returns ride the takeover channel → the two levers nobody models together (liquidity, disclosure law) → 2024 SEC acceleration makes this live → central question |
| II. Model | 10 | Institutions→model translation (13D = action-triggered disclosure) → timeline & four actions → engagement + bidder entry feedback → cutoff equilibrium → where κ enters inference → prices embed an activism premium |
| III. Results | 14 | Hump-shaped Δ^min(κ) → two-force decomposition → Theorem A (premium wedge from tender mechanics; AFS sign reconciled) → Theorem B (certified GE region + counterexample) → disclosure attenuation → GE disclosure trade-off (policy paradox) |
| IV. Evidence | 6 | Fact 1: filing-delay compression after the 2024-02-05 rule (EDGAR universe) → Fact 2: 13D announcement CARs, post-rule shift × illiquidity interaction (CRSP/WRDS event study) |
| V. Close | 5 | Summary (mechanism, prediction, contribution) → where this goes (engagement-cost distribution on 13D XML; structural leg) |

Timing check: 18 content slides ≈ 2.2 min/slide = 40 min with a 13-min results act
absorbing the deepest questions.

## Academic deck (Beamer) — changes to `pres/presentation.tex`

Main sequence (18 slides): keep the existing 16-slide spine, with:
1. **De-milestone-ify**: drop "Status upgrade (new)" (slide 10); retitle "New Theorem A/B"
   → "Theorem A/B"; trim "New:" prefix in the summary slide.
2. **Fix stale institutional fact** (slide 3): 13D window is now **5 business days**
   (was 10 calendar days; compliance 2024-02-05) — the deck currently states only the
   10-day rule. Present old→new as the live policy experiment.
3. **Add Act IV — two evidence slides** after Prop 6/policy block:
   - Fact 1: delay-compression figure (`empirics/output/fact1_delay.pdf`), share within
     5 business days pre/post.
   - Fact 2: CAR event-study figure (`empirics/output/fact2_car.pdf`) + the
     Post / Post×ln(Amihud) coefficients vs the model's predictions (β>0, δ<0).
4. **Refresh positioning slide (2b)** with the validated full-read findings (C–L, J–S,
   AFS) — keep one slide, sharpened one-liners.
5. **Backups**: keep all 21; add (a) Fact 1/2 data+method backup (sample construction,
   event-study spec, full regression table), (b) tender-game extensive form (D7
   structure: λ = 1 − q(1−γ)ψ derivation sketch), (c) certified-region method note
   (how the inversion-free bound is computed). Bidirectional hyperlinks as existing.
6. Keep audience-calibration comment block; figures stay vector PDF.

## Business deck (PPTX) — rebuild via `pres/make_pptx.py`

Same spine, business idiom: decision-oriented headlines, one message per slide,
figures > equations (λ shown once, boxed; no posterior algebra in main), 16:9,
flat editorial style (near-black ink, one accent = UCL-ish blue #4477aa,
rose #ee6677 for warnings/counterexample), generous whitespace, 28–40pt headlines.

~22 main + ~11 backup:
1 Title (research talk title, no "upgrade")
2 The takeaway up front (three numbered claims)
3 Why care: activist returns ride takeovers (65% stat)
4 The two levers: liquidity & disclosure law (2×2 visual)
5 2024: the SEC halved the clock (timeline graphic; Fact-1 teaser)
6 The question
7 Framework in one picture (timeline)
8 The four plays (exit/hold/quiet/public — 2×2 action grid)
9 The feedback loop (order flow → inference → price → bid entry)
10 What the market can/can't see (two regimes)
11 Result 1: liquidity's sweet spot (hump figure)
12 Why: cover vs camouflage (decomposition)
13 Result 2: who captures the prize (λ wedge; AFS sign flip explained)
14 Result 3: when is it a theorem (certified region + the trough at σ_ξ=0.60)
15 Disclosure attenuates the dial (slopes figure)
16 The policy paradox (transparency vs deterrence)
17 Evidence 1: the clock bit (delay compression)
18 Evidence 2: the market noticed (CAR fig + interaction sign)
19 What this means for policy (liquidity regulation ≡ governance policy)
20 What this means for investors (cross-sectional predictions)
21 Where this goes (data roadmap)
22 Takeaways (mirror of slide 2)
Backups: calibration table, baseline equilibrium table, posteriors, existence/uniqueness,
sensitivity ×2, welfare, disclosure benchmarks, GE region method, tender game, Fact 2 table.

Figures: rasterize the needed PDFs to 300-dpi PNGs (matplotlib re-render via pyfig with
PNG output into `pres/pptx_assets/`); PPTX embeds PNGs.

## Verification gates

- Beamer: XeLaTeX + biber clean (0 errors / 0 undefined refs / 0 undefined citations);
  page count sanity; visual audit of new slides; no "milestone/upgrade" string anywhere
  in either deck (`grep -i "milestone\|upgrade"`).
- PPTX: opens in PowerPoint/Keynote (python-pptx round-trip), every image present,
  text within frames (manual size budget), 33±3 slides.
- Both: narrative table above maps 1:1 to slide order.

## Dependencies

- Fact 2 numbers/figure: blocked on EDGAR build (#6) → WRDS event study (#7) →
  analysis (#9). Evidence slides are last to land; rest of both decks build now.
- Positioning slide refresh: blocked on paper-read agents (#10–#12).
- Claim wording on Theorems A/B: blocked on math reviews (#13) — adopt corrections.
