# SNAPSHOT — draft_v2 repositioning project (handoff to next agent)

Date: 2026-08-19. Owner goal (verbatim intent): turn `draft_v2.tex` ("Liquidity, Activism
Disclosure, and Takeover Premia") into a paper strong enough for JF/RFS/JFE or just below by
(1) simplifying the theoretical core (simpler, elegant, coherent), (2) moving part of the results
to empirics for institutional anchoring, (3) repositioning the framing — a substantial move is
allowed. `proposal/` is out of scope (treat as a different project). Final deliverable owed to
owner: **best angle + modelling setup + empirical spec**.

## Where things stand

- `plan.md` — the 3-stage plan (research → synthesis → deliver).
- Stage 1 (deep literature research, 9-agent swarm) — **9 of 9 strands COMPLETE** (strand E liquidity–premia empirics finished 2026-08-19 → `research/lit_liquidity-premia-empirics.md`; key adds: Massa–Xu 2013 JFQA +10% premium per SD of target liquidity; Huang–Maharjan–Nanda 2024 JCF −4.5pp per SD acquirer−target liquidity difference, stock deals only; CDF 2015 run-up 7% vs jump 3% with λ/PIN *falling* during accumulation). Two synthesis inputs added: `research/draft_v2_digest.md` (full structural digest + cut-list) and `research/empirical_feasibility.md` (Fact-2 data already on disk: 9,234 parsed 13Ds 2022–25, CRSP snapshot 2021–25, WRDS CARs 2,285 events; 2025 parser bug found, fixable ~1 day).

  | File | Strand | Status |
  |---|---|---|
  | research/lit_classic-exit-voice.md | Maug 98, Kahn-Winton 98, Faure-Grimaud-Gromb 04, Admati-Pfleiderer 09 | done |
  | research/lit_modern-blockholder-trading.md | Edmans 09, Edmans-Manso 11, Back et al 18, Levit-Malenko-Maug 24 | done |
  | research/lit_feedback-takeover-theory.md | EGJ 12/15, BEG 12, DGG 17, Corum-Levit 19, Goldstein 23 | done |
  | research/lit_disclosure-structural-activism.md | OC-Bernhardt 22, AFS 22, Johnson-Swem 21, Celentano-Levine 25, CCKV 26 | done |
  | research/lit_activism-empirics.md | BJPT 08, Greenwood-Schor 09, Gantchev 13, Clifford 08 (partial), Klein-Zur 09, BFGW 17 | done |
  | research/lit_institutional-facts.md | 13D/G regime, 2024 SEC amendments, HSR, pills, UK/EU thresholds, state statutes, data sources | done |
  | research/lit_frontier-scan.md | 2022–26 top-journal taste + competitors | done |
  | research/lit_theory-to-empirics-templates.md | templates for theory+empirics papers | done |
  | — | liquidity-activism-premia empirics (EFZ 13, Norli et al 15, CDF 15, Fos 17, target-liquidity→premia) | **ABORTED (user interrupt); can rerun or fold into synthesis** |

- Stage 2 (synthesis) — **COMPLETE 2026-08-19 → `framework_v3.md`** (angle, simplified model
  setup + proof plan, empirical spec, edit map, journal targets). Awaiting owner approval of the
  angle.
- Stage 3 — deliver summary + link; editing draft_v2 waits for owner approval of the angle.

## Cross-cutting findings the synthesis must use

1. **The gap is real and quotable**: Back et al. 2018 and Burkart & Lee (RFS 2022) explicitly
   leave "endogenous disclosure horizon / pre-disclosure trading interacting with post-disclosure
   control" to future work. The trading–disclosure–takeover-premium nexus is unclaimed
   (OC&B do threshold design w/o bidder; CCKV stop at the crossing; structural papers AFS / J&S /
   C&L have no microstructure).
2. **R1 (hump-shaped minority premia in κ) is the exposed flank** — top-3 theory papers are
   100% analytical; no precedent for numerically-verified headline results. Recommended fixes:
   prove the hump in an exponential-noise special case (OC&B template) or via a primitive
   curvature/elasticity condition (Back et al. Thm 2 template), or convert it into a falsifiable
   non-monotonicity identification device (Corum-Levit Prop 4 template) and prove only the
   endpoint structure. Note: the hump has pedigree (Edmans 09 Prop 3 is hump-shaped in liquidity).
3. **R2 (disclosure attenuation) should headline**: the SEC 13D modernization (10 days → 5
   business days, compliance 2024-02-05) is a clean dated shock; cross-country threshold variation
   (UK/DE/ES/IT/NL 3% vs US/FR/JP/AU 5% vs CA 10%) is an unused out-of-sample test. The project's
   `empirics/` EDGAR 13D/G pipeline already works.
4. **Structure advice**: cut action menu to ≤3 branches; keep bidder entry as reduced-form
   price trigger (EGJ-style); Brouwer existence + labeled numerical uniqueness is acceptable if
   headline comparative statics are proven. Avoid the "70% theory + casual event study" middle —
   either pure-theory-with-anchoring (Burkart-Lee template) or committed empirics.
5. **Calibration/empirical anchors collected**: C&L estimate mean bid premium 36.6%, activism
   lowers premia 13.7% (5.2pp), raises deal prob 7.7%; Gantchev voice costs by escalation stage;
   BJPT 13D run-up 10 days pre-filing (market infers accumulation); Ben-David et al. (JF 2026)
   warns naïve CAR-based premia measures.

## Corrections to repo (found by the swarm, not yet applied)

- `lit/hhab039.pdf` is **Burkart & Lee 2022 RFS "Activism and Takeovers"**, NOT EGJ 2012.
- EGJ 2012 is **JF 67(3):933–971** (not RFS); Gantchev 2013 is **JFE 107:610–631** (not JF);
  DGG 2017 is JEEA (not JF); Goldstein 2023 survey is Review of Finance (not RFS).
- `lit/competitor_scope_tables.md` misattributes the −13.7% premium effect to AFS — it is
  Celentano & Levine's; J&S contain no σ²T/13D-window claim.
- Draft cites EGJ 2015 as precedent for *numerical* uniqueness — they prove region-wise
  uniqueness analytically; reframe that citation.

## Suggested next-agent sequence

1. Read this file, `plan.md`, the 8 briefs in `research/`, and draft_v2.tex sections
   Intro/Model/Equilibrium/ComparativeStatics/TestableImplications.
2. (Optional) rerun the aborted liquidity-premia strand (agent-5 scope, see swarm history).
3. Write `framework_v3.md`: best angle, simplified model setup (what to prove), which results
   move to empirics + full empirical spec (hypotheses, data, identification around the Feb-2024
   13D acceleration and cross-country thresholds), edit map draft_v2 → draft_v3, journal targets.
4. Only after owner approves the angle: edit `draft_v2.tex` into `draft_v3.tex`.

## Environment notes

- Managed Python has pypdf (extract lit PDFs); scanned JF PDFs may need OCR (macOS Vision worked).
- WebBridge daemon (127.0.0.1:10086) available for paywalled pages via the owner's browser;
  use a distinct `session` name; the browser is shared.
- `empirics/` EDGAR pipeline: stdlib-only, throttled, raw data gitignored; output in
  `empirics/output/`.
