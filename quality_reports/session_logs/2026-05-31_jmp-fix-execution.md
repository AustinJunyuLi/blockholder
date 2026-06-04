---
date: 2026-05-31
session_type: JMP fix execution (derive -> stage -> assemble)
status: IN_PROGRESS — derivations closed & staged; safe content + assembly pending
branch: jmp-upgrade-2026-05
---

# Session: Executing the JMP Upgrade Fixes — draft_v2.tex

## Goal
Implement the full fix roadmap from `quality_reports/plans/2026-05-30_jmp-upgrade-critique-and-roadmap.md`
on branch `jmp-upgrade-2026-05`: correct the headline Prop 6, repair equilibrium foundations,
welfare, Prop 8, micro-found m0/m1, A2 robustness, reframe, and add missing citations.
User decisions: FULL fix; edit on a git branch; iterate hard proofs until they close (honest relabel only as last resort).

## Key context / state
- Baseline `draft_v2.pdf` compiles clean on the branch (50pp; 0 undefined after xelatex->biber->xelatex->xelatex).
- Content-production workflow `wf_5c298ff4-cda` (task `wgh3yp0p7`) is RUNNING; staging dir `quality_reports/fixes/`.
- Phase 0 numerics: hump is REAL (amp ~15.8% rel at tol 1e-9, peak kappa~0.60, >> solver noise);
  independent reimplementation MATCHES repo solver exactly; endpoint symmetry holds on valid equilibria;
  hump->trough only at sigma_xi=0.60 (near-flat corner). Corrected chord criterion (h=pi*p) tracks the hump
  better than the memo's g=mbar*p.
- Hard derivations CLOSED + numerically verified and staged as D1..D6 .tex:
  D1 endpoint/variance (closed-form quartic; bar_pi=9/14, old 0.4545 was wrong);
  D2 welfare planner (compiles); D3 Prop 8 IFT (Jacobian signs verified, det~0.075);
  D4 bargaining (m0=.1,m1=.3 recovered; A3 a theorem; hump survives state-dependent wedge);
  D5 A2 (hump survives flat cost chi=0); D6 equilibrium foundations.
- Cleanups needed at assembly: D1-GE has stale hardcoded numbers in comments (lint FAIL); D6 has 1 label collision.

## Next steps
1. Let workflow finish DeriveSafe (S2 dominance, S3 framing, S4 web-verified citations, S5 institutional) + ReviewContent (assembly plan).
2. Splice staged content into draft_v2.tex sequentially per the assembly plan; fix the two cleanups.
3. Compile (xelatex->biber->xelatex->xelatex; expect 0 undefined) + `make` to regenerate figures.
4. Verification pass; report closed-vs-relabeled ledger + diff. Do NOT commit/push until user asks.

## Open questions / risks
- D1-GE cutoff-shift: confirm the analytic bound closed vs was relabeled as numerical regularity.
- S4 citations: double-check any %% UNVERIFIED flags (OCB JFQA pages, Cetemen forthcoming-JF status, UK DTR5 deadline) before they enter the bib.
