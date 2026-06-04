---
date: 2026-05-30
session_type: adversarial critique + literature positioning + JMP roadmap
status: COMPLETED (diagnostic phase); execution phase pending author decision
---

# Session: Adversarial Critique & Top-10 JMP Roadmap — draft_v2.tex

## Goal
Meticulously understand the paper, then run a deep-research / multi-angle adversarial
critique + current-literature positioning, to upgrade "Liquidity, Activism Disclosure,
and Takeover Premia" toward a theory JMP for a top-10 financial-economics program.

## What was done
- Full verified read of `draft_v2.tex` (1432 lines — complete draft, NOT a stub; early
  tooling had fed a garbled/truncated view that briefly misled the read).
- Absorbed strategy docs: three-paths plan (Path A/B/C), 2026-05-02 structural-disclosure
  pivot, and `prop6_rigor_memo` (endpoint symmetry + Jensen/variance fix).
- Ran a 19-agent background workflow (`wf_ee57529c-acf`): 5 dossier readers, 4 web-verified
  literature themes, 8 adversarial referee lenses, 1 synthesis, 1 adversarial verifier.
  ~2.06M subagent tokens, 626 tool uses, ~38 min.

## Artifacts
- `quality_reports/plans/2026-05-30_jmp-upgrade-critique-and-roadmap.md` (258 lines) — the memo.
- `quality_reports/plans/2026-05-30_jmp-upgrade-evidence-appendix.md` (221 lines) — raw evidence.

## Key findings
- **Headline Prop 6 is petitio principii** (line 554 assumes the inequality it claims to prove);
  its supporting **Endpoints Lemma is factually false** (voice does NOT collapse at kappa->1;
  kappa=1 posteriors are the two-point law {0, pi_bar}, not the unconditional prior).
- The rigor memo's fix is substantially right at baseline but **incomplete**: (a) condition stated
  for g=m_bar*p, not the actual integrand h=pi*p; (b) GE cutoff-shift term is genuinely unsigned
  (envelope theorem does not apply — Delta^min is minority welfare); (c) hump is conditional (flips
  to a trough when the condition fails) so it must be a stated hypothesis.
- Uniqueness numerical-only (mislabeled a Proposition); existence self-map + B_P>B_Q step unproved;
  A7 circular. Welfare section rhetorical (no planner/FOC/envelope); Prop 8 has \approx inside a
  theorem env. m0/m1, A2, the action set, and the 1-share normalization are imposed by fiat.
- **Ordonez-Calafi & Bernhardt (2022 JFQA) not cited** = fastest desk-reject trigger; also missing
  Corum-Levit, Levit-Malenko-Maug (2024), Cetemen et al. (live competitor), Goldstein (2023).
- **Binding constraint is the novelty ceiling, not rigor**: static model caps ~top-20/25.
- Verifier caveats: placement tiers are unbenchmarked priors; Path B feasibility is asserted not
  demonstrated (needs a spike); the disclosure-attenuation reframe may itself be partly scoopable;
  no field-journal fallback / exit criterion stated.

## Recommendation
Sequenced hybrid: execute no-regret repairs (R1-R5) first; run a 1-2 wk Path-B feasibility spike
before any week-6 commitment gate; pre-commit numerical-regularity + field-journal fallbacks.

## Open decisions (author's call)
- Path B (continuous-time, top-10 ceiling, 10-12 mo) vs Fourth Option (one sharp theorem + 2024
  SEC 13D-acceleration DiD, top-15/20) — pending a feasibility spike.
- Whether to begin editing draft_v2.tex now (no-regret repairs) vs review the memo first.
