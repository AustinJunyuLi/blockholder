# JMP Fix — Handoff Report for the Next Agent (2026-05-31)

**Paper:** "Liquidity, Activism Disclosure, and Takeover Premia" — `draft_v2.tex` (1432 lines).
**Branch:** `jmp-upgrade-2026-05` (all work below is on this branch; `main` is untouched).
**Governing docs:** critique+roadmap `quality_reports/plans/2026-05-30_jmp-upgrade-critique-and-roadmap.md`; evidence `…_jmp-upgrade-evidence-appendix.md`; rigor memo `quality_reports/rewrites/prop6_rigor_memo.md`.

---

## 0. TL;DR — where things stand

A dynamic workflow produced and **numerically verified** the six hard mathematical fixes (Prop 6 correction, welfare planner, Prop 8 IFT, bargaining micro-foundation, A2 robustness, equilibrium foundations). They are **staged as standalone `.tex` files in `quality_reports/fixes/` but NOT yet integrated into `draft_v2.tex`.**

**What is NOT done:** (1) the four "safe" content pieces — dominance lemma, framing pivot, citations/bib, institutional box; (2) the assembly (splicing staged content into the manuscript); (3) the integrated compile + figure regeneration; (4) the final verification pass; (5) independent citation verification.

**`draft_v2.tex` (the manuscript body) is UNCHANGED** (`git diff --quiet draft_v2.tex` → no change). The integration/splice has not happened.

**BUT the workflow edited two TRACKED files directly (not just staging) — review these before trusting them:**
- `numerical/model.py` (+7/−1) — **BENIGN, KEEP IT.** It is only a numpy-2.0 compatibility shim (`np.trapz`→`np.trapezoid`) plus the one call site in `compute_welfare`. Not a model/economics change. (`.bak_trapz` is the pre-shim backup; no need to revert.)
- `bibliography.bib` (+10) — **one** new entry only: `@article{BinmoreRubinsteinWolinsky1986}` (the Nash-bargaining reference for D4). It is a legitimate classic; still verify its fields. **The major must-add citations (Ordóñez-Calafí & Bernhardt 2022, Corum-Levit 2019, Levit-Malenko-Maug 2024, Cetemen et al., Goldstein 2023) are NOT yet in the bib** — see §2.D.
- Backups present: `draft_v2.tex.bak_welfare` (a welfare-section edit was prepared but NOT applied — `draft_v2.tex` is unchanged), plus `_*` scratch wrappers.

Nothing of value is lost — the derivations are staged on disk, and the only tracked edits are the benign model.py shim and one bib entry.

**Do NOT re-run the workflow** — it is what consumed the tokens. The derivations are already on disk and verified. The remaining work is cheap, deterministic editing + a few targeted web lookups.

---

## 1. DONE — staged, verified mathematical fixes (in `quality_reports/fixes/`)

Each is a self-contained statement+proof in the draft's notation. "Verified" = an independent Python check (also staged) confirmed the quantitative claims against the repo solver.

| File | ~KB | Content | Status | Verification artifact |
|---|---|---|---|---|
| `phase0_robustness.md` | 11 | Phase-0 numerics fact sheet (the ground truth) | DONE | `phase0_robustness_driver.py` |
| `D1_prop6_endpoint_variance.tex` | 34 | Lemma A (endpoint symmetry Δ^min(0)=Δ^min(1)) + closed-form U-shaped Var[π|D=0] quartic | **CLOSED** | `D1_verify_RESULT.txt` (~25 checks PASS) |
| `D1_prop6_condition_Cstarstar.tex` | 35 | Condition (C\*\*) for h(π)=π·p concave on chord [0,π̄] → single-peak | **CLOSED** | `D1_verify_Cstarstar.py` |
| `D1_prop6_GE_cutoffshift.tex` | 21 | GE cutoff-shift channel: κ↦(k1,k0,kD) is C¹ via IFT; the cutoff-shift sum is treated as a numerically-verified regularity under a stated condition | **RELABELED** (honest numerical-regularity fallback — see §6) | `D1_GE_check_out.json`, `_relabel_FINAL.txt` |
| `D2_welfare_planner.tex` | 43 | Planner program, FOC via envelope, sign(κ\*−κ†); engages Levit-Malenko-Maug (2024) | **CLOSED** (compiles standalone, 8pp) | `D2_welfare_verify.py`, `_d2_status.txt` |
| `D3_prop8_IFT.tex` | 25 | Prop 8 as a genuine comparative static (`=` not `≈`); IFT on cutoff map, signed Jacobian | **CLOSED** | `_D3_check_result.json` (det≈0.075, signs OK) |
| `D4_bargaining_microfound.tex` | 30 | Nash bargaining → closed-form m0,m1; A3 becomes a theorem; hump survives state-dependent wedge | **CLOSED** | `d4_bargaining_driver_out.json` |
| `D5_A2_robustness.tex` | 30 | A2 robustness: hump survives flat cost (χ=0); persuasion-vs-entrenchment taxonomy | **CLOSED** | `_D5_verify_out.txt` |
| `D6_equilibrium_foundations.tex` | 54 | Self-map proof; B_P>B_Q lemma; global monotone-best-response lemma; drop A7; split A5; uniqueness | **CLOSED** — needs 1 label-collision fix | `D6_equilibrium_checks.py`, `_d6_state.txt` |

### Verified numerical facts (cite these; do not re-derive)
- **The hump is real, not solver noise.** At fixed-point tol 1e-9 the baseline Δ^min(κ) is single-peaked, peak **κ≈0.60**, amplitude **≈15.8% of level** (abs ≈1.06e-2), which exceeds 10× the max residual among kept points (4.47e-9). (`phase0_robustness.md §0`.)
- **Reproducibility resolved:** an independent reimplementation matches the repo solver **exactly** at κ=0.5 — cutoffs (0.8217, 0.8217, 2.2611), Δ^min=0.077015, resid ~3.7e-7. (`_recon_branches.txt`.)
- **Endpoint symmetry** Δ^min(0)=Δ^min(1) confirmed on valid equilibria (exact-endpoint solves coincide to 9e-8 but carry high residual — report as suggestive at the exact endpoints, verified on the valid interior). (`phase0_robustness.md §0`.)
- **The hump is conditional, as the memo predicted.** Over a (σ_ξ, S̄) grid it is a hump everywhere except **σ_ξ=0.60 with high S̄**, where the profile is near-flat and tips to a shallow trough (the takeover channel is washed out). The **corrected chord criterion (h=π·p) tracks the hump better than the memo's g=m̄·p criterion** — vindicating correction (a) of the memo. (`phase0_robustness.md §1` table.)
- **Hump survives flat cost χ=0** (peak κ≈0.60, amp 4.6%) and **survives a state-dependent premium wedge** (D4 case E, shape=HUMP) — neutralizing the two biggest "fragility" worries from the verification pass.
- Constant correction: π̄ = 0.45/0.70 = **9/14 ≈ 0.6429** (an earlier draft value 0.4545 used the wrong denominator; D1 already uses the correct one).

---

## 2. NOT DONE — remaining work (in priority order)

### A. Safe content not yet produced (was next in the workflow when stopped)
These are referenced by the roadmap (memo §3.4(iii), §5, §7 items R3/R4/R5) but **no `S*.tex` files exist** in `quality_reports/fixes/`:
1. **S2 — Dominance Lemma** for the excluded actions (−1,1) and (+1,0). The (−1,1) "engaged exit" case is a one-liner (selling sets h=0 ⇒ captures none of δhΔ̃ yet pays C(s)>0). For (+1,0): note honestly that D=1⟺q=+1 means a silent buy still discloses, so the exclusion is partly pinned by the disclosure technology (do not overclaim).
2. **S3 — Framing pivot:** new abstract, intro contribution paragraph, conclusion, and title — **lead with disclosure attenuation (Prop 7)**, demote the hump to a conditional supporting result around interior-optimal κ† (endpoint symmetry refutes "more liquidity hurts minorities"). Replace the over-claim "No existing framework combines these three forces." Use one consistent "central contribution" referent. Base on memo §8.1.
3. **S4 — Citations + positioning:** add bib entries (Ordóñez-Calafí & Bernhardt 2022 JFQA [closest competitor, currently uncited]; Corum-Levit 2019 JFE; Levit-Malenko-Maug 2024 JF; Cetemen-Cisternas-Kolb-Viswanathan; Goldstein 2023 RoF); correct EGJ2015 to published AER 105(12) title; write the related-lit positioning paragraph + scooping boundary vs Cetemen.
4. **S5 — Institutional-facts box:** dated US 13D 5% + the 2024 SEC acceleration (10 calendar → 5 business days); UK FCA DTR5 3% + deadline; EU Transparency Directive; name the UK City Code mandatory-bid-at-30% confounder.

### B. Assembly into `draft_v2.tex` — NOT started (the workflow never reached the assembly-plan step)
No `.tex` has been spliced. The 8 derivation files are standalone. See §4 for the recommended assembly map.

### C. Integrated compile + figures + verification — NOT done
- Compile recipe (known-good baseline = 50pp, 0 undefined): `xelatex → biber → xelatex → xelatex`.
- `make` to regenerate the affected figures (esp. Fig 1 with the true endpoints; add the hump→trough robustness table).
- Final proofread/verification pass.

### D. Independent citation verification — NOT done
The S4 web checks never ran. The next agent must web-verify exact venue/volume/pages before any new \cite enters the bib, especially: **OCB (2022 JFQA) exact pages; Cetemen et al. forthcoming-JF vs working-paper status + exact title; UK FCA DTR5 deadline.** (Flagged in memo §5 "could not confirm" list and the verification `citation_audit`.)

---

## 3. Known cleanups required during assembly (small but mandatory)
1. **`D1_prop6_GE_cutoffshift.tex` (relabeled): 2 stale hardcoded numbers remain** (`_d1_final_status.txt: STALE_COUNT=2`). It otherwise compiles clean (0 errors, 0 undefined, condition-guard present). Strip/refresh the 2 comment-only stale numbers before insertion.
5. **Standalone-compile `rc=1` on some staged files is a WRAPPER ARTIFACT, not a content error** (e.g. D2/D4 test wrappers report `! Command \1 undefined` because the scratch wrapper lacks the draft preamble macros `\1,\E,\PP,\Var`). These compile fine once spliced into `draft_v2.tex`, which defines them. Verify via the full draft compile, not the scratch wrappers.
2. **`D6_equilibrium_foundations.tex` has 1 label collision** (`_d6_state.txt` "label collision check"). Rename the duplicated `\label{}` before insertion.
3. **Theorem renumbering / cross-refs:** inserting Lemma A and the corrected Prop 6, dropping A7, and splitting A5 into A5a/A5b will shift numbering. After splicing, run the 3-pass compile and confirm **0 undefined references/citations** (baseline had 0 after 3 passes).
4. **Notation consistency:** the staged files use the draft's macros (`\E,\PP,\1,\Var`) and symbols (m̄, π̄, T(π), Δ^min, Δ^act). Confirm no clashes when merged.

---

## 4. Recommended assembly map (the next agent's main task)

Splice sequentially on the branch; the draft's relevant anchors (verbatim line numbers in the current `draft_v2.tex`):

| Order | Action | Draft location (current) | Source / note |
|---|---|---|---|
| 1 | **Delete** false Endpoints Lemma (statement) | lines ~546–560 (`\begin{lemma}[Endpoint Behavior…]`) and its proof ~1229–1244 (`app:proof-endpoints`) | replace with D1 Lemma A |
| 2 | **Delete** circular Prop 6 (statement ~552–562) + its proof (~1246–1253, `app:proof-nonmonotone`) | replace with corrected Prop 6 | from D1 (endpoint+variance, C\*\*, GE) |
| 3 | **Insert** Lemma A + Var quartic (main + appendix) | §"Nonmonotonic Minority Takeover Gains" (~525) + appendix | `D1_prop6_endpoint_variance.tex` |
| 4 | **Insert** condition (C\*\*) into Standing Assumptions + the corrected single-peak Prop 6 | ~525–562 + standing-assumptions footnote (~322) | `D1_prop6_condition_Cstarstar.tex` |
| 5 | **Insert** GE cutoff-shift lemma + proof (appendix) | appendix after Prop 6 proof | `D1_prop6_GE_cutoffshift.tex` (clean comments first) |
| 6 | **Replace** Prop 8 (~783–790) | §"General Equilibrium Disclosure Effects" | `D3_prop8_IFT.tex` |
| 7 | **Replace** welfare section (~717–730) | §"Welfare Analysis" | `D2_welfare_planner.tex` |
| 8 | **Insert** bargaining micro-foundation (new subsection in Model/Extensions + appendix) | after §"Engagement Technology" (~234) or as an extension | `D4_bargaining_microfound.tex`; turns A3 into a theorem |
| 9 | **Insert** A2 robustness proposition | §"Engagement Technology" (~214–234) or extensions | `D5_A2_robustness.tex` |
| 10 | **Replace** existence/uniqueness (~506–522 + appendix ~1217–1227) | §"Equilibrium Existence and Uniqueness" | `D6_equilibrium_foundations.tex` (fix label; drop A7 → recast bidder on price ~240) |
| 11 | **Insert** Dominance Lemma | §"Model"/equilibrium | **S2 (to be written)** |
| 12 | **Replace** abstract/intro-contribution/conclusion/title | ~57–59, ~67–77, ~794–802, ~47–48 | **S3 (to be written)** |
| 13 | **Add** bib entries + positioning paragraph; fix EGJ title | `bibliography.bib` + §"Related Literature" (~78–106) | **S4 (web-verify first)** |
| 14 | **Insert** institutional-facts box | §"Extensions" (~737–739) | **S5 (web-verify first)** |
| 15 | **Compile** (xelatex→biber→xelatex→xelatex); confirm 0 undefined; `make` figures | — | — |

---

## 5. Guidance for the next agent (token discipline)
- **Do not invoke the Workflow tool or spawn parallel agents.** The derivations are done; remaining work is single-threaded editing + ~5 web lookups.
- Read staged `.tex` files **one at a time with offset/limit**, not in bulk (a whole-file Read of the big ones is large).
- The staging dir has ~200 scratch files prefixed `_` (verification scratch). The **canonical deliverables are the non-underscore `D*.tex` / `phase0_robustness.md`** only. Ignore the `_*` files unless auditing a specific check.
- After assembly, the success gate is: clean 4-pass compile, **0 undefined refs/citations**, page count sane (~55–65pp expected), and `make` regenerates figures without new NA-row regressions.
- **Do not commit or push** until the human reviews the diff.

## 6. Honesty ledger (closed vs. relabeled)
**Five of six hard derivations CLOSED** (analytic proof + numerical confirmation): D1 endpoint/variance, D1 condition (C\*\*), D2 welfare, D3 Prop 8 IFT, D4 bargaining, D5 A2, D6 equilibrium.

**One was RELABELED, as designed: `D1_prop6_GE_cutoffshift.tex` (the GE cutoff-shift term).** Evidence: a `_relabel_FINAL.txt` verdict file appeared (~17:01) and the file shrank from ~48 KB to ~21 KB (405 lines). This is the **honest-fallback** outcome the user pre-authorized — the cutoff-shift sum could not be signed/bounded in fully closed analytic form, so it is presented as a **numerically-verified regularity under a stated condition** (the EGJ precedent), not as a completed proof. **The next agent should read this file and confirm the framing is honest** (it must say "verified numerically," not assert a proof). This is the single place where the top-journal bar is not fully met analytically — consistent with the verification pass's prediction that this term might be analytically intractable.

The headline result is now **conditional** (single-peak under (C\*\*); shallow near-flat trough only in the σ_ξ=0.60 corner) — this conditionality must be stated as a hypothesis, not hidden.

**Re-verification note:** because `numerical/model.py` was modified during the run, the next agent should re-run the Phase-0 numerics (`phase0_robustness_driver.py`) against the FINAL model.py (or the reverted one) to confirm the headline numbers (hump amplitude, endpoint symmetry) still hold under whatever model.py state is kept.
