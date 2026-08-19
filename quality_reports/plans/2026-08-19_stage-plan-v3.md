# Plan — Repositioning draft_v2 for a top finance journal

## Goal (user)
Turn "Liquidity, Activism Disclosure, and Takeover Premia" (draft_v2.tex, pure theory, key result only
numerically verified) into a paper strong enough for JF/RFS/JFE or just below:
- Simplify the theoretical core (simpler, elegant, coherent).
- Move part of the results to empirics → stronger institutional anchor.
- Deep literature research = actually OPEN and READ papers (full text), not abstracts.
- Prefer angles/setups tied robustly to institutional facts.
- Deliverable: best angle + modelling setup + empirical spec. Ignore proposal/ (treat as new project).

## Current paper state (read by orchestrator)
- Static 4-stage model (EGJ-2015-style discrete order flow): blockholder chooses
  Exit / Hold / Quiet Voice / Public Voice; disclosure D=1{q=+1} stake-triggered; bidder entry
  conditioned on price; competitive market maker.
- Results: (R1) hump-shaped minority takeover gains in liquidity κ — only CONDITIONAL/numerical
  (endpoint symmetry Δ^min(0)=Δ^min(1)); (R2) disclosure-attenuation: stricter 13D-type threshold
  lowers liquidity-sensitivity of premia. Existence via Brouwer; uniqueness = "numerical regularity".
- Heavy appendix scaffolding (D1–D7 derivation records) defending assumptions; welfare section.
- Assets: lit/ has 10 key PDFs; empirics/ has a working EDGAR 13D/G pipeline (stdlib, throttled).

## Stage 1 — Deep literature research (swarm, 9 agents, parallel) — **COMPLETE (9/9; strand E finished 2026-08-19 → research/lit_liquidity-premia-empirics.md)**
Each agent READS full texts (local lit/ PDFs via pypdf; open-access PDFs via FetchURL; paywalled
journal pages via Kimi WebBridge daemon through the user's logged-in browser) and writes
research/lit_<strand>.md. Structure per paper: question / architecture & method / key results
(what is proved vs numerical vs estimated) / institutional facts used / referee-facing strengths
& weaknesses / implications for repositioning our paper.

- A1 classic-exit-voice — Maug 1998, Kahn-Winton 1998, Faure-Grimaud-Gromb 2004, Admati-Pfleiderer 2009
- A2 modern-blockholder-trading — Edmans 2009, Edmans-Manso 2011, Back et al 2018 (lit/), Levit-Malenko-Maug 2024
- B feedback-takeover-theory — EGJ 2012 (lit/ hhab039), EGJ 2015, Bond-Edmans-Goldstein 2012,
  Dow-Goldstein-Guembel 2017, Corum-Levit 2019 (lit/), Goldstein 2023 survey
- C disclosure-structural-activism — Ordonez-Calafi-Bernhardt 2022, Albuquerque-Fos-Schroth 2022 (lit/),
  Johnson-Swem 2021 (lit/), Celentano-Levine 2025 (lit/), Cetemen-Cisternas-Kolb-Viswanathan 2026
- D activism-empirics — Brav-Jiang-Partnoy-Thomas 2008, Greenwood-Schor 2009, Gantchev 2013,
  Clifford 2008, Klein-Zur 2009, Becht-Franks-Grant-Wagner 2017
- E liquidity-activism-premia-empirics — Edmans-Fang-Zur 2013 (lit/), Norli-Ostergaard-Schindele 2015,
  Collin-Dufresne-Fos 2015, Fos 2017, + target-liquidity→takeover-premium empirical literature (agent finds)
- F institutional-facts — 13D/G regime (5% threshold, filing windows, 2024 SEC amendments, Item 4),
  HSR, poison pills, UK Takeover Panel 3%, EU Transparency Directive thresholds, state antitakeover
  statutes, data sources (SDC/LSEG, SharkRepellent, EDGAR, Activist Insight)
- G frontier-scan — 2022–2026 JF/RFS/JFE/RAPS/JFQA: activism, blockholders, takeovers, disclosure
  thresholds; what gets published now; direct competitors to a repositioned version
- H theory-to-empirics-templates — recent theory papers that successfully added a reduced-form or
  structural empirical section (finance top-3 + JFQA/RAPS); extract the template (how much empirics,
  what identification, how theory sections were compressed)

## Stage 2 — Synthesis (orchestrator, no delegation) — **COMPLETE 2026-08-19 → framework_v3.md**
Produced framework_v3.md: angle = "the 13D disclosure rule as the revelation technology of the
market for corporate control"; R2 promoted to headline theorem (proof route mapped), R1 demoted
to endpoint theorem + certified region + falsifiable prediction; empirical section = facts + the
Feb-2024 13D-acceleration DiD on liquidity-sensitivity (data largely on disk per
research/empirical_feasibility.md); edit map draft_v2 → draft_v3; targets JF/RFS (JFE alt).
Supporting swarm outputs: research/draft_v2_digest.md, research/empirical_feasibility.md.

## Stage 3 — Deliver
Summary in chat + [framework_v3.md] link. Editing draft_v2 itself waits for user approval of the angle.
