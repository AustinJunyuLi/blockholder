---
date: 2026-06-10
type: design-note
status: DESIGN-READY (execution gated on WRDS/CRSP access)
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

**Data requirements.** CRSP daily (returns, volume, price) — **author to confirm UCL WRDS access**; EDGAR side already in `empirics/` (Fact 1 parser provides event/filed dates + CIKs). Fallback: Bloomberg terminal pulls per `lit/bloomberg_checklist.md` (manageable for a few hundred events); degraded fallback: ship Fact 1 + this design note only.

**Estimated effort once data access lands:** 1–2 sessions (link table + event-study harness in `empirics/`, reusing the Fact-1 sample frame).
