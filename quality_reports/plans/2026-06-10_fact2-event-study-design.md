---
date: 2026-06-10
type: design-note
status: DESIGN-READY — WRDS/CRSP access CONFIRMED 2026-06-11 (see Data requirements)
branch: jmp-upgrade-2026-05
title: "Fact 2 — 13D announcement event study around the 2024 acceleration (design)"
---

# Fact 2 — Event-Study Design Note

**Question.** Did the information content of 13D announcements — announcement-window abnormal returns — change when the SEC cut the filing deadline from 10 calendar days to 5 business days (compliance 2024-02-05)?

**Model mapping.** In the model, a shorter pre-disclosure window is less cumulative noise-trading cover for the activist's accumulation (the σ²T reading Johnson–Swem formalize); the model's disclosure-attenuation result (Prop 6) predicts the *liquidity sensitivity* of activism-driven premia falls as more of the activism information arrives by disclosure rather than inference. Two testable contrasts:
1. **Announcement CAR level**: shorter window ⇒ less pre-disclosure price discovery ⇒ *larger* jump at filing (more information released at the event).
2. **Cross-sectional liquidity interaction**: the CAR–liquidity slope (e.g., CAR on pre-event Amihud) should *flatten* post-rule (attenuation).

**Spec (primary).**
- Sample: SC 13D originals, 2022-01-01 → 2025-12-31, US common stocks (CRSP share codes 10/11), match filer/subject via EDGAR CIK → CRSP PERMNO (CIK–CUSIP link via WRDS SEC Analytics or the `cik_map` from Compustat).
- Event window: CAR[−1, +1] and CAR[−10, +1] around the *filing* date, market-model abnormal returns (estimation window [−250, −30]).
- Design: `CAR_i = α + β·Post_i + γ·Amihud_i + δ·(Post_i × Amihud_i) + controls + ε_i` with Post = filed ≥ 2024-02-05; controls: size, book-to-market, pre-event run-up, activist-type FE (hedge fund vs other, from filer SIC/name matching), year-quarter FE. Inference: cluster by subject firm and by month.
- Predictions: β > 0 (contrast 1); δ < 0 relative to pre-period γ > 0 (contrast 2).
- Threats: (i) composition shifts in who files post-rule (selection — the model itself predicts marginal filers change; report filer-mix diagnostics); (ii) contemporaneous market-structure changes (tick-size, T+1 settlement May 2024 — add a May-2024 dummy robustness); (iii) the rule also expanded cash-settled-derivative inclusion — flag filings with derivative language (parser field exists).

**Data requirements.** CRSP daily (returns, volume, price) — **CONFIRMED 2026-06-11** (UCL WRDS login verified in-browser): CRSP **Annual Update** Daily Stock File (CIZ v2) query form accessible with coverage through 2025-12-31 — fully covers the sample window; the *quarterly* product (`crsp_q_stock`) is NOT subscribed but is not needed. Compustat–Capital IQ (276 items) and CRSP/Compustat Merged are subscribed → CIK→GVKEY→PERMNO linking path available. **SEC Analytics Suite NOT subscribed** (no CIK–CUSIP link table) — use the Compustat path, or extend `empirics/parse_13d.py` to extract the subject CUSIP from the 13D cover page (preferred; the WRDS U.S. Daily Event Study upload accepts CUSIP directly). **Event Study by WRDS "Upload your own events" is accessible** (requires only CRSP daily, any update frequency) — can compute market-model CARs with custom estimation/event windows directly from an uploaded (identifier, date) file. EDGAR side already in `empirics/` (Fact 1 parser provides event/filed dates + CIKs; no CUSIP field yet). Fallback: Bloomberg terminal pulls per `lit/bloomberg_checklist.md` (manageable for a few hundred events); degraded fallback: ship Fact 1 + this design note only.

**Estimated effort once data access lands:** 1–2 sessions (link table + event-study harness in `empirics/`, reusing the Fact-1 sample frame).

---

## RESULTS (full run, 2026-06-11) — design executed end-to-end

Sample: 9,234 EDGAR originals -> 3,518 (CUSIP8, trade-date) events -> 2,280
WRDS-matched -> 1,513 after filters (843 pre / 670 post). WRDS event-study
query 11385426 (market model, est 220/min 100/gap 20, window [-10,+10]);
CRSP covariates from the full 2021-2025 daily panel, chunk-filtered locally.

| Prediction | Estimate | Verdict |
|---|---|---|
| beta > 0 (Post level shift) | +0.9pp (t=1.12); mean CAR[-1,+1] 0.85%->1.71% | sign right, n.s. |
| delta < 0 (Post x lnAmihud) | +0.17pp (t=0.48) | precise null |
| (unconditional liquidity gradient) | lnAmihud -1.4pp (t=-3.73), all specs | strong; camouflage margin first-order |

Reading: the level doubling is economically large but noisy under firm x month
two-way clustering; the cross-sectional liquidity gradient is the robust fact;
the differential-compression interaction does not show up (note the post-rule
composition shift toward smaller/more illiquid targets). Slides report all
three honestly (Beamer E2; PPTX Evidence-2). Robustness backlog: winsorized
CARs, placebo rule dates, FF3 abnormal returns, matched pre/post samples.
