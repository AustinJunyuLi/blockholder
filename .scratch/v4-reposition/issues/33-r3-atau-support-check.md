# 33 — R3 · A(τ) support enumeration: the decisive check

**Lane:** theory (`v4-theory` worktree at `~/Projects/blockholder_v4_theory`)

**Routing (lane v2, agentic):** Opus writer, effort medium (the enumerated object must be exactly
the card's pooled posterior law — a wrong object silently passes; a Sonnet mistake here forces a
full redo). Deterministic script; no separate re-runner (the execution is the verdict).
Orchestrator commits.

**Premise:** Audit finding 3 + GPT review finding 3's NUMERICAL CHECK REQUEST. A(τ) says the
pooled cell's posterior law is a three-point family on $\{0,\bar\pi/2,\bar\pi\}$ with κ-free
support and $\bar\pi$ (card §5, clauses (τ-i)/(τ-ii)) and the derivative pattern
$A_0'=A_1'=A'_\kappa$, $A_{1/2}'=-2A'_\kappa$. Both prior "failure" tests were misformulated;
applicability is OPEN. `numerical_v4/` enumerates the pooled law exactly. The card's $\bar\pi$
ruling: $\bar\pi$ = the **upper support point** (never assume $\bar\pi = 2\times$ the pooled
share — that level-symmetry assumption was the block-3 error).

**What to build:**

- [ ] `quality_reports/fixes/t2_atau_support_check.py` → `t2_atau_support_check.json`, standard
      header/tolerances/OUT-beside-script pattern (copy the t2_* house style). Grid: the standard
      sweep (κ ∈ {0.05,…,0.95} or the established t2 grid, τ at the established percentiles,
      T ∈ {1,2,5,10,H}); frozen policies per design §6.2.
- [ ] Per node, from the exact enumeration of the pooled cell's engagement-posterior law:
      1. **support**: distinct posterior values (cluster at tol 1e-12) + their masses; the count;
      2. **support movement**: max |support-point shift| across adjacent κ at fixed (τ,T) —
         A(τ) predicts < 1e-12, and $\bar\pi$ κ-free;
      3. **shape test**: is the support exactly $\{0,\bar\pi/2,\bar\pi\}$ (three points, midpoint
         relation to tol)?;
      4. **weights**: recover $A_0, A_{1/2}, A_1$ where 3-point holds; central finite differences
         in κ; residuals of $A_0'=A_1'$ and $A_{1/2}'=-2A_0'$ (predict < 1e-10 under A(τ));
      5. **identity**: $|\,\mathcal S_P - \Delta_m|A'_\kappa||C_h(\bar\pi)|\,|$ with the
         **recovered** $A'_\kappa$ and the **actual upper support point** as $\bar\pi$
         (predict < 1e-10 if the representation holds). Report the recovered $|A'_\kappa|$ per
         node (prior implied range from block 3: ≈[0.997, 1.158]).
- [ ] Verdict logic, reported honestly: **HOLDS at calibration** (three fixed points + pattern +
      identity everywhere), **FAILS at calibration** (support ≠ 3 points, or moving support, or
      pattern residual — say which, where, by how much), or **MIXED** (node counts per regime).
      A support failure and a derivative-pattern failure are different findings — separate them.
- [ ] Run it; commit script + JSON. Then append a **dated evidence note** to the card §5 A(τ)
      block ("Whether the two-round pooled cell satisfies the support condition" paragraph):
      the verdict + node counts + JSON pointer. **No label moves** — A(τ) is an assumption;
      this is applicability evidence, NUMERICAL-class.

**Do NOT:** impose Example A's 0.25 anywhere; impose level symmetry; touch L3/T1 rows or labels.

**Stopping condition:** JSON on file with a three-way verdict; card note appended; pushed.
