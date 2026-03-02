# Backup Slides Design: Theory-Focused Reinforcement

**Status:** APPROVED
**Date:** 2026-03-02
**Audience:** Theory-focused (committee members probing proofs, equilibrium robustness)

## Goal

Add 7 new backup slides to `pres/presentation.tex` to cover mathematical proof gaps identified in the paper's appendices. Integrate into the existing 5-category structure (Approach 1).

## New Slides

### Mathematical Foundations & Equilibrium Robustness (3 new, after existing Backup 5)

| ID | Title (question format) | Hypertarget | Links from | Paper source |
|----|------------------------|-------------|------------|--------------|
| 6b | "How do you derive the Delta^min decomposition?" | `backup:decomposition_proof` | Slide 10b | Appendix A.9 |
| 6c | "What are the endpoint limits of minority gains?" | `backup:endpoint_behavior` | Slide 10 | Appendix A.11 (Lemma 1) |
| 6d | "How do you know the hump is strict?" | `backup:nonmonotonicity_proof` | Slide 10 | Appendix A.12 (Prop 5) |

**Backup 6b content:**
- 3-step proof: definition of Delta^min, conditional independence of bid indicator and (v,a) given (X,D), iterated expectations
- Key equation: E[m^R(a) * 1{bid} | X,D] = m_bar(X,D) * p(X,D)
- Emphasis: conditional independence is the heart -- xi independent of (v,a)

**Backup 6c content:**
- Lemma 1: two endpoint limits
- kappa -> 1: order flow uninformative, posteriors flatten, voice collapses, Delta^act -> 0
- kappa -> 0: order flow reveals q, engagement persists but bid deterrence suppresses
- Key equations: limit expressions for both endpoints

**Backup 6d content:**
- Prop 5 proof: Weierstrass on compact [0,1] + verifiable sufficient condition
- Note: guarantees at least one interior peak, doesn't rule out W-shape
- Baseline calibration confirms single-peaked hump

### Sensitivity & Comparative Statics (2 new, filling backups 8-9 gap)

| ID | Title | Hypertarget | Links from | Paper source |
|----|-------|-------------|------------|--------------|
| 8 | "Does engagement deter bids?" | `backup:bid_monotonicity` | Slide 6 | Appendix A.6 |
| 9 | "How do synergies and entry costs affect bid incidence?" | `backup:takeover_comps` | Slide 6 | Appendix A.8 |

**Backup 8 content:**
- dp/dP = -phi(T)/sigma_xi < 0 and dp/dpi = -(m_tilde - m_0)*phi(T)/sigma_xi < 0
- Policy implication: Disclosed activism (pi=1) deters more than inferred (pi<1)
- Connection to A5: sup|dp/dP| = phi(0)/sigma_xi is the regularity condition

**Backup 9 content:**
- dp/dS_bar > 0, dp/dK < 0 (same phi(T)/sigma_xi factor, different signs)
- All three derivatives share the same structure -- differences are purely in sign
- PE results (hold equilibrium prices fixed)

### Disclosure Extensions & Information Regimes (2 new)

| ID | Title | Hypertarget | Links from | Paper source |
|----|-------|-------------|------------|--------------|
| 10 | "Why are prices flat on the disclosed branch?" | `backup:disclosed_invariance` | Slides 8, 9 | Appendix A.2 |
| 12b | "How does PE vs GE change the disclosure story?" | `backup:PE_vs_GE` | Slides 11, 12 | Sections 8.4, Prop 6 & 7 |

**Backup 10 content:**
- 3-step proof: D=1 => Public Voice (a=1 a.s., X=1+z)
- z independent of (v,s,xi), so conditioning on X given D=1 only reveals z=x-1
- Fixed-point uniqueness (A5): same RHS => same P*
- Key result: pi(x,1)=1, P*(x,1)=P*(x',1) for all x,x'
- Why it matters: foundation of Prop 6 (disclosed component is kappa-invariant)

**Backup 12b content:**
- Side-by-side: Prop 6 (PE, fix cutoffs, vary kappa through inference) vs Prop 7 (GE, allow k_D(tau) to adjust)
- PE shows WHY disclosure attenuates; GE shows WHETHER stricter disclosure is welfare-improving
- Policy punchline: Low C_0 + moderate kappa => transparency dominates; High C_0 => deterrence dominates

## Formatting Conventions (match existing backups)

- Frame titles are questions (interrogative style)
- `\small` for body text, `\scriptsize` for heavy equations
- 2-4 bolded steps per proof sketch
- `\returnlink` back to relevant main slide
- `\hypertarget` labels follow `backup:snake_case_name`
- Add `\backuplink` from relevant main slides to new backups

## Bidirectional Links to Add

Main slides needing new `\backuplink` additions:
- Slide 6 -> `backup:bid_monotonicity`, `backup:takeover_comps`
- Slide 8 -> `backup:disclosed_invariance`
- Slide 9 -> `backup:disclosed_invariance`
- Slide 10 -> `backup:endpoint_behavior`, `backup:nonmonotonicity_proof`
- Slide 10b -> `backup:decomposition_proof`
- Slide 11 -> `backup:PE_vs_GE`
- Slide 12 -> `backup:PE_vs_GE`

## Verification

- `xelatex pres/presentation.tex` compiles without errors
- All hyperlinks resolve (no undefined hypertargets)
- All new backups have return links to their source main slides
- New backups match the formatting style of existing ones
- Total backup count: 20 existing + 7 new = 27 backup slides
