# 29 — T2i · C1: the GE region certificate

**Lane:** theory (`v4-theory` worktree at `~/Projects/blockholder_v4_theory`)

**Routing (lane v2, agentic):** Opus writer for the bound derivations; Opus
script writer + separate re-runner for the certification run; Fable reviews if
the region comes back empty (that decision — ship fixed-policy only — is
already made in the card, but the empty-region call gets a second read).

**Premise:** card §4.5 (the inversion-free bounds k̄_x, k̄_κr, ℬ_r^GE and the
slack η_r); turn-1 C1 statement + check request; the D8 dominance-check
pattern (`quality_reports/fixes/d8_ge_dominance_check.py`) is the architectural
precedent; `numerical_v4/` equilibrium mode (ticket 25) supplies 𝒯 and its
derivatives.

**What to build:**

- [ ] `research/model_v4/proofs/C1_proof.md`: the certificate theorem —
      inversion-free bounds derived (implicit-function step under L_ℛ < 1),
      the dominance inequality g_r^PE > ℬ_r^GE ⟹ the fixed-policy sign
      survives in equilibrium; answer template
- [ ] `quality_reports/fixes/t2_c1_region_check.py` + JSON: κ∈[0.15,0.85] on
      0.01 grid, T∈{5,10}, threshold percentiles 10–90, perturbations; per
      node L_ℛ, g_r^PE, ℬ_r^GE, η_r; **"empty region" printed explicitly if no
      node certifies** — an empty region is a reportable outcome, and the
      paper then ships the fixed-policy theorem only (card §"not claimed")
- [ ] Proof-read + re-derivation via ticket 27's pipeline; label per evidence
      (PROVED on the named region only if nonempty; NUMERICAL off-region)
- [ ] Session log lines; commits on `v4-theory`

**Blocked by:** 25 (implementation), 26 (T1 — the sign being certified).

**Status:** ready-for-agent

## Comments
