# Audit — batch 1 proof-read (L3, L4, P1)

Sources under audit, all committed and read verbatim:
`research/model_v4/proofs/L3_proof.md`, `research/model_v4/proofs/L4_proof.md`,
`research/model_v4/proofs/P1_proof.md`.
`A7_construction.md` and `A7_attack_verdict.md` were **not** read (separate pipeline).

Context read first: `MODEL_CARD.md` in full (stamp 2026-08-20 · `0c9185b`);
`threads/thread1_msg3.md` §3 (the L3/L4 spec); `threads/thread1_turn1_answer.md` §§P1, L3, L4
(original statements) and §§2.10, 3, A(τ); `threads/thread1_turn2_audit.md` (binding notation
rulings and the D1 repairs P1 consumes).

Auditor: fresh Opus proof-reader, ticket 27 batch 1, 2026-08-21, worktree `blockholder_v4_theory`
(branch `v4-theory`). Wrote none of the proofs under audit. Stance: adversarial — every numbered
step was attacked before it was passed.

Role: this is the **Opus proof-read half** only. Per the handoff protocol a PROVED label needs
**independent re-derivation PASS *plus* proof-read PASS**. This audit supplies the second.
**All three results stay CONJECTURE.** The writers' own LABEL CLAIMED blocks (L3 claims PROVED for
parts (i)–(iv); L4 and P1 both claim CONJECTURE) move nothing. **No label moves in this file** —
that is the orchestrator's ledger job.

Finding classes: **FAIL** (a step's cited hypotheses/earlier steps do not deliver it, or the math is
wrong — blocks) · **REPAIR** (the claim stands; a step uses something true but uncited, or asserts
where it should argue — never blocks) · **OBSERVATION** (a card gap or a note for later turns).

---

## 0. Verdicts

| Result | Verdict | Failing steps | Repairs | Observations | Claim vs card |
|---|---|---|---|---|---|
| L3 | **PASS** | none | L3-R1 … L3-R5 | L3-O1 … L3-O4 | **refinement** |
| L4 | **PASS** | none | L4-R1 … L4-R5 | L4-O1 … L4-O3 | **refinement** (adds A(br)) |
| P1 | **PASS** | none | P1-R1 … P1-R8 | P1-O1 … P1-O5 | **refinement** (adds h.11, h.12, h.13) |

**Nothing blocks.** No numbered step reaches a false conclusion, so the one-retry rule does not fire
and no proof is bounced. Two repairs are heavy enough to name at the top:

* **P1-R1** — h.11's primary form is **jointly unsatisfiable with h.2**, one line, demonstrable by
  cardinality. P1 survives only on h.11's second reading, which the writer supplies. This is the
  direct analogue of turn-2's L2-R1, but sharper: the contradiction is internal to P1's own
  hypothesis list.
* **L4-R1 / L3-R1** — the two proofs disagree, in substance, about what $\bar\pi$ is and about
  whether $h$ is a function of the posterior alone. L4 names the second as an assumption it cannot
  prove; L3 consumes it silently as "the card's own reading". L4's standard is the right one.

**Mechanical scans** (all three files, executed).

| Scan | L3 | L4 | P1 |
|---|---|---|---|
| Banned words (`clearly`/`it follows`/`standard`/`obviously`/`evidently`/`trivially`/`straightforward`/`well-known`/`of course`/`easily seen`/`routine`) | **0** | **0** | **0** |
| draft_v2 refs (`\ref`, `\cite`, `lem:`/`prop:`/`thm:`/`app:`/`eq:`, `et al`) | **0** | **0** | **0** |
| Unused hypotheses | **0** (7/7 used) | **0** (11/11 used; (br-i)–(br-iv) all used) | **0** (13/13 used) |
| Bare steps (no hypothesis or step citation) | **0** (19 steps + Step 8′) | **0** (21 steps) | **0** (20 steps) |
| Card-section citations resolve to `MODEL_CARD.md` | **yes** | **no** — `card §2.5` (L4-R3) | **no** — `card §2.10` ×3 (P1-R6) |
| NOTATION DELTA complete | **no** — Θ (L3-R3) | **no** — bare Δ, indexed $A'_\kappa$/$\bar\pi$, $X_{0:H}$, $s^\ast$ (L4-R4) | **no** — bare $g$, $\beta$ ×2 meanings, $\mathcal C_j^{\mathrm{trade}}$ (P1-R7) |

Turn-1's four renames (`ψ→Γ`, bare `ω→ω_a`, `a_κ→A'_κ`, delete `σ_κ`) and turn-2's two
(`W→Ξ`, `G→Υ`, drop `𝖹`) are obeyed in all three files. `λ` and `ψ` appear only inside
notation-compliance prose, never as live symbols. `κ` is noise-trading intensity throughout, with
no drift toward depth, volume or turnover. Upright `T` is the window and `𝒯` the best-response map
in every occurrence.

**Cross-proof citation discipline.** L4 cites D1 and L3 **by ledger statement only** and says so at
Steps 3 and 15; it re-derives L3's proportionality constant from the card's own A(τ) rather than
reading L3's Step 8, which is the correct discipline and is worth recording as a positive. L3 cites
L2 as a card ID at Step 9 and re-proves nothing. P1 cites D1 by statement (h.9) but reaches into
**L2's proof internals once** — WHERE-IT-FAILS 1's "L2's Step-9 analogue" (P1-O4). Not load-bearing;
it sits in a failure case, not a numbered step.

---

## 1. Executed checks — outputs verbatim

Two stdlib-only scripts, written and run for this audit:
`…/scratchpad/audit_checks.py` (L3, L4) and `…/scratchpad/p1_checks.py` (P1).
Kernel throughout the L3 blocks is the proof's own check convention:
$h(\pi)=\pi p(\pi)$, $p(\pi)=1-\Phi\big((P(\pi)+K+m_0+\pi\Delta_m-\bar S)/\sigma_\xi\big)$,
$P(\pi)=m_0+\Delta_m\pi$, at $m_0=0.10$, $\Delta_m=0.18$, $K=0.15$, $\bar S=1.44$, $\sigma_\xi=0.40$.

```
== CHECK 1: L3 Block 1 (Example A, pi_bar=1) ==
  h(0)=0.000000  h(1/2)=0.4942735175  h(1)=0.9659994853
  C_h(1)                       = -2.254755e-02   [proof: -2.2548e-2]
  A'_kappa * C_h(1)            = +5.636887e-03   [proof: +5.6369e-3]
  direct d/dk E_k[h] (kappa grid .05..0.95): min=+5.6368874318e-03 max=+5.6368874429e-03
  range across kappa grid      = 1.110e-11  (Step 8 predicts exactly constant)
  max |residual vs A'_k C_h|   = 6.601e-12
  weight sum at kappa=0.37     = 1.000000000000000
  moment A_1/2*(1/2)+A_1*1     = 0.500000000000000   (rho=1/2, kappa-free)

== CHECK 2: L3 Block 3 (quarter h''(0)) ==
  (1/4)h''(0) = (1/2)p'(0)     = -4.381962e-03   [proof: -4.3820e-3]
  C_h(1e-2)                    = -4.463231e-07   [proof: ~ -4.4e-7]
  C_h(pb)/pb^2 at pb=1e-3      = -4.390029e-03
  C_h(pb)/pb^2 at pb=1e-4      = -4.382768e-03

== CHECK 3: L3 Block 2 (mean-value point zeta/pi_bar -> 1/2) ==
  pi_bar=1        zeta/pi_bar=0.53899142  |C_h - .25 pb^2 h''(z)|=0.00e+00
  pi_bar=0.5      zeta/pi_bar=0.52433977  |C_h - .25 pb^2 h''(z)|=2.17e-18
  pi_bar=0.2      zeta/pi_bar=0.51095327  |C_h - .25 pb^2 h''(z)|=6.51e-19
  pi_bar=0.1      zeta/pi_bar=0.5056846   |C_h - .25 pb^2 h''(z)|=2.03e-20
  pi_bar=0.01     zeta/pi_bar=0.50058739  |C_h - .25 pb^2 h''(z)|=0.00e+00
  pi_bar=0.001    zeta/pi_bar=0.50005894  |C_h - .25 pb^2 h''(z)|=8.27e-25
  pi_bar=0.0001   zeta/pi_bar=0.50000527  |C_h - .25 pb^2 h''(z)|=6.46e-27

== CHECK 4: L3 WHERE-IT-FAILS 3, kernel pi^{3/2} ==
  pi_bar=1      C_h=+2.9289321881e-01   pb^1.5*(1-2^-0.5)=+2.9289321881e-01  (1-2^-1/2=0.292893)
  pi_bar=0.5    C_h=+1.0355339059e-01   pb^1.5*(1-2^-0.5)=+1.0355339059e-01  (1-2^-1/2=0.292893)
  pi_bar=0.1    C_h=+9.2620968267e-03   pb^1.5*(1-2^-0.5)=+9.2620968267e-03  (1-2^-1/2=0.292893)
  pi_bar=0.01   C_h=+2.9289321881e-04   pb^1.5*(1-2^-0.5)=+2.9289321881e-04  (1-2^-1/2=0.292893)

== CHECK 5: L3 Step 13(a)/Block 4, affine kernel C_h=0 ==
  C_h(affine,pb=1) = +0.0e+00
  range of E_k[h_affine] over kappa grid = 0.000e+00

== CHECK 6: L3 WHERE-IT-FAILS 2, tent kernel ==
  C_h(tent,1) = -1.0  [proof: -1];  h''=0 a.e. -> no admissible zeta

== CHECK 7: L3 Step 17, Example B four atoms, monotone interior posteriors ==
  pi_-(0.05)=0.025641 -> pi_-(0.95)=0.904762   strictly increasing: True
  pi_+(0.05)=0.974359 -> pi_+(0.95)=0.095238   strictly decreasing: True
  distinct atoms at kappa=0.5: [0.0, 0.333333333, 0.666666667, 1.0]

== CHECK 8: L3 Step 19, pi_bar-as-mean forces degeneracy ==
  A_1=0.2: A_1/2=+1.60  A_0=-0.80  (A_0>=0 only at A_1=1) mean=1.000 (x pi_bar)
  A_1=0.5: A_1/2=+1.00  A_0=-0.50  (A_0>=0 only at A_1=1) mean=1.000 (x pi_bar)
  A_1=0.9: A_1/2=+0.20  A_0=-0.10  (A_0>=0 only at A_1=1) mean=1.000 (x pi_bar)
  A_1=1.0: A_1/2=+0.00  A_0=+0.00  (A_0>=0 only at A_1=1) mean=1.000 (x pi_bar)

== CHECK 9: L4 Step 11/12 conditional-probability identity ==
  max |Step12 form - direct difference|      = 1.664e-16
  max |Step12 alt closed form - difference|  = 6.761e-14
  sign check pi_pr(tau) >= pi_pr(tau'): held on all 200000 draws

== CHECK 10: L4 (br-iv) factor-two reading vs L3 Step 19 ==
  A_0=A_1=0.1: mean = A_1/2*(pb/2)+A_1*pb = 0.500000 * pi_bar  (predicted 0.5)
  A_0=A_1=0.25: mean = A_1/2*(pb/2)+A_1*pb = 0.500000 * pi_bar  (predicted 0.5)
  A_0=A_1=0.4: mean = A_1/2*(pb/2)+A_1*pb = 0.500000 * pi_bar  (predicted 0.5)
  A_0=A_1=0.49: mean = A_1/2*(pb/2)+A_1*pb = 0.500000 * pi_bar  (predicted 0.5)
```

```
== P1 CHECK A: Step 4 conditional-expectation algebra (Monte Carlo) ==
  Monte-Carlo E[Y|I] = 1.091700   Step-4 closed form = 1.091383   diff = 3.17e-04

== P1 CHECK B: Step 7 bracket + unique strict down-crossing (grid sweep) ==
  draws=20000  bracket [A, max(Sbar-K-mbar+sx, A+0.19 mbar)] valid failures = 0
  root count != 1 (2001-pt grid, wide window)            = 0
  rho'(root) >= 0 failures                               = 0
  min |rho'| at root over all draws                      = 0.0204

== P1 CHECK C: Step 8 IFT slope in (0,1] ==
  slope outside (0,1] : 0;  max |numeric dP/dvhat - analytic| = 6.67e-10

== P1 CHECK D: h.11 primary form vs h.2 (finite menu) ==
  |J| = 12 finite (h.2)  =>  {Q_j'^F(s) : j' in J} has at most 12 values.
  h.11 primary demands that set cover [0, bbar - B_j^F(s)], an uncountable interval
  whenever B_j^F(s) < bbar.  Cardinality: 12 < continuum.  JOINTLY UNSATISFIABLE
  unless B_j^F(s) = bbar for every flagged (j,s), i.e. Q^F == 0 and round 2 is empty.
```

**Reading of the outputs.**

* Every number L3's writer said was verified **is** verified: $C_h(1)=-2.2548\times10^{-2}$,
  $\partial_\kappa\mathbb E=+5.6369\times10^{-3}$ (and exactly constant across the $\kappa$ grid to
  $1.1\times10^{-11}$, the finite-difference floor, as Step 8 predicts for weights affine in
  $\kappa$), $\tfrac14h''(0)=-4.3820\times10^{-3}$, $\zeta/\bar\pi\to\tfrac12$ (monotone
  $0.5390\to0.50001$), and the $\pi^{3/2}$ value $1-2^{-1/2}=0.292893$ exact at every $\bar\pi$.
  The mean-value identity closes to $\le 2\times10^{-18}$ at every grid point — it is an identity,
  not an approximation, exactly as CLAIM (i) says.
* L3's Block-3 acceptance criteria are met on the writer's own kernel: the two smallest $\bar\pi$
  points differ by $0.17\%$ (bar: $5\%$) and the ratio to $\tfrac14h''(0)$ is within $0.19\%$ at
  $\bar\pi\le10^{-3}$ (bar: $2\%$).
* Example A's weights sum to 1 and its engagement moment is $\rho=\tfrac12$, free of $\kappa$, at
  every $\kappa$ — the Step-14 conservation check the writer claims. Example B's four atoms are
  distinct at every interior $\kappa$ with $\pi_-$ strictly up and $\pi_+$ strictly down. Both
  examples re-derived independently from the card's primitives and both reproduce.
* L4's Step 11/12 arithmetic is an identity to machine precision over 200 000 random admissible
  $(\rho_P,\nu,\bar\pi_{\mathrm{pr}})$ triples, in **both** closed forms the proof gives, with the
  sign never violated.
* P1's Step 4 closed form matches Monte Carlo within MC noise. Step 7's explicit bracket
  $[A,\max\{\bar S-K-\bar m+\sigma_\xi,\ A+0.19\bar m\}]$ is valid at **all 20 000** random
  parameter draws, the root is unique at all of them on a wide 2001-point window, and
  $\varrho'<0$ strictly at every root. Step 8's analytic slope matches the numerical derivative to
  $6.7\times10^{-10}$ and never leaves $(0,1]$. **P1's calculus is right.**

---

## 2. L3 — chord-vanishing lemma

### 2.1 Claim vs the card's ledger row

Card row: *"Under A(τ) the pooled cell's interior κ-motion is proportional to $C_h(\bar\pi)$, and
$C_h=\tfrac14h''(0)\bar\pi^2+o(\bar\pi^2)$, so it vanishes as $\bar\pi\downarrow0$."*

The proof adds (i) the **exact** mean-value form $C_g=\tfrac14\bar\pi^2g''(\zeta)$ needing only
$C^2$ on the open interval; (iv) the $C_h=0$ case and an explicit refusal of "iff"; (v) the
reduction of A(τ)'s derivative restrictions to its support condition, with a satisfying and a
non-satisfying example inside the card's primitives; and it demotes the quadratic form to a
corollary with its extra regularity priced. **Classification: refinement**, and it is the strongest
of the three files. Every item msg3 §3 asked for — (a) exact mean-value form, (a)-corollary with
its cost, (b) the $C_h=0$ case as an "if", (c) A(τ)'s domain named with one witness on each side and
an honest OPEN — is delivered and is delivered where it says it is.

### 2.2 Part I — the double mean value theorem. **PASS, and the interior bookkeeping is exact.**

This was the step the audit was asked to stress hardest. It survives intact, checked inequality by
inequality:

| Step | What it needs | Verified |
|---|---|---|
| 1 | $g$ twice differentiable on $(0,\bar\pi)$ ⟹ $g'$ exists **and is continuous** there | ✓ differentiable ⟹ continuous, applied to $g'$ |
| 3 | $\Delta_g$ continuous on $[0,\bar\pi/2]$ | ✓ $t\in[0,\bar\pi/2]$ and $t+\bar\pi/2\in[\bar\pi/2,\bar\pi]$, both in $[0,\bar\pi]$ |
| 3 | $\Delta_g$ differentiable on $(0,\bar\pi/2)$ | ✓ $t\in(0,\bar\pi/2)$ and $t+\bar\pi/2\in(\bar\pi/2,\bar\pi)$, both in $(0,\bar\pi)$ — **the endpoints are excluded on both sides**, which is the whole trick |
| 4 | MVT hypotheses on $[0,\bar\pi/2]$ | ✓ supplied by Step 3 |
| 5 | $[t_1,\ t_1+\bar\pi/2]\subset(0,\bar\pi)$ | ✓ $t_1>0$ and $t_1+\bar\pi/2<\bar\pi/2+\bar\pi/2=\bar\pi$ — the strict inequality $t_1<\bar\pi/2$ from Step 4 is what keeps the right endpoint interior |
| 5 | MVT hypotheses for $g'$ on that closed interval | ✓ the interval sits inside $(0,\bar\pi)$ where $g'$ is differentiable, hence continuous |
| 6 | chaining | ✓ $\tfrac{\bar\pi}{2}\cdot\tfrac{\bar\pi}{2}=\tfrac14\bar\pi^2$, $\zeta\in(0,\bar\pi)$ |

Step 6's recorded observation — that no value of $g'$ or $g''$ at $0$ or $\bar\pi$ is ever invoked —
is **true and is the reason the form is stronger than a Taylor expansion**. The tent-kernel witness
(WHERE-IT-FAILS 2, executed check 6) confirms Hypothesis 4 is not decoration: $C_h(1)=-1$ while
$h''\equiv0$ wherever it exists, so no admissible $\zeta$ exists. Step 11's second route (Peano
second-order differentiability at $0$) is correctly derived — the constant terms cancel $1-2+1=0$,
the linear terms $-2\cdot\tfrac12+1=0$, the quadratic terms leave
$(-\tfrac14+\tfrac12)h''(0)\bar\pi^2=\tfrac14h''(0)\bar\pi^2$ — and correctly described as neither
implying nor implied by the Part-I route.

### 2.3 Part II and Part IV — the algebra, all of it re-derived

**Step 8 — PASS.** Term-by-term differentiation of a three-term sum, then one factorisation; the
$(+1,-2,+1)$ coefficient pattern is exactly the second difference. Correct.

**Step 14 — PASS, both directions re-derived by hand.** Forward: $\mathrm r'=0$ reads
$A_{1/2}'\tfrac{\bar\pi}{2}+A_1'\bar\pi=0$, divide by $\bar\pi/2>0$ to get $A_{1/2}'=-2A_1'$;
substitute into $\mathrm m'=0$ to get $A_0'=2A_1'-A_1'=A_1'$. Reverse: sum is
$A_1'-2A_1'+A_1'=0$ and $-2A_1'\tfrac{\bar\pi}{2}+A_1'\bar\pi=0$. Exact.

**Step 15 — PASS.** $\mathbb E[\pi(\mathcal I_H)\mathbf 1\{D=0\}]=\Pr(a=1,D=0)$ needs
$\{D=0\}\in\sigma(\mathcal I_H)$, which card §4.3 supplies (the flag is a coordinate of the public
history; the cells are exclusive and exhaustive) — and Step 15 cites §4.3 for exactly that. This is
the same public-flag bridge turn-2 flagged as uncited in D1 (D1-R1); **L3 cites it, D1 did not**.

**Step 19 — PASS, and it is the most useful paragraph in the file.** Re-derived: with support
$\{0,\bar\pi/2,\bar\pi\}$, conditional weights summing to $1$, and mean $=\bar\pi$, the moment
equation gives $A_{1/2}=2(1-A_1)$, hence $A_0=1-A_{1/2}-A_1=A_1-1\le0$, hence $A_0=0$, $A_1=1$,
$A_{1/2}=0$: a point mass, $A'_\kappa=0$, zero motion for every kernel. Executed check 8 reproduces
it at four values of $A_1$. A mean cannot equal the maximum of its own support unless the law is
degenerate, and the writer says so.

**Step 16 (Example A) — PASS, re-enumerated from the card's primitives.** The five order-flow
realisations, the three posteriors, the masses $(2-\kappa)/4$, $\kappa/2$, $(2-\kappa)/4$, the sum
to $1$, $A'_\kappa=-\tfrac14$ and the $\kappa$-free moment $\tfrac12$ all reproduce (executed check
1). The two load-bearing features the writer names are the right two: the informed mark must be
strictly outside the uninformed mark's noise reach ($2\bar z>0+\bar z$), and the pre-order share
must be exactly $\tfrac12$ to put the pooling cell at the chord midpoint. The second is what the
word "symmetric" in A(τ) is carrying, which the card never said.

**Step 17 (Example B) — PASS, re-enumerated.** The four-cell table, the two interior posteriors,
and their strict monotonicity in $\kappa$ (likelihood ratios $\tfrac{\kappa/2}{1-\kappa}$ up and
$\tfrac{1-\kappa}{\kappa/2}$ down) all reproduce; executed check 7 confirms strict monotonicity at
every grid point and four distinct atoms at $\kappa=0.5$. The consequence Step 17 draws is the
sharpest sentence in the batch: **Step 8′ transfers to the frozen manuscript's structure and Step
8's clean proportionality does not.** That is a limitation of A(τ) stated by the author rather than
found by a referee, which is what this lane is for.

**Step 18 — the OPEN declaration is honest and correctly scoped.** The argument that any one-round
ternary-noise market with a non-degenerate pooled law forces $\bar\pi=1$ (non-engaging marks weakly
negative or zero, Voice increments positive, so the top realisation is Voice-only) is correct, and
it is why Example A cannot carry the $\bar\pi\downarrow0$ limit. (S1)–(S2) are a genuine weakest
sufficient condition, not a restatement.

### 2.4 Findings

> **L3-R1 (REPAIR — the substantive one). Step 7 assumes $h$ is a function of the engagement
> posterior alone, and that is not a reading, it is a restriction.**
>
> Step 7's reason for treating $h(0),h(\bar\pi/2),h(\bar\pi)$ as $\kappa$-free numbers is that
> "$h$ itself is a function of the posterior value only". In the model it is not. Card §4.4 gives
> $h(\mathcal I)=\pi(\mathcal I)p(\mathcal I)$ and card §4.3's entry row makes $p$ depend on the
> **price** $P(\mathcal I)$ as well as on $\pi$; P1's own Step 4 proves the control-node price
> depends on $\mathcal I$ through the **pair** $(\hat v(\mathcal I),\pi(\mathcal I))$. So
> $h(\mathcal I)=\pi\,p(\hat v,\pi)$ is a function of two scalars, and "$h$ evaluated at a fixed
> posterior is $\kappa$-free" is a substantive restriction on how the standalone-value channel and
> the engagement channel co-move inside the pooled cell.
>
> Two things stop this from blocking. Hypothesis 1's display already writes $h$ with no $\kappa$
> argument, so the claim as stated stands; and the card's own A(τ) and $C_h$ rows commit the same
> elision, so it is card-backed. But it is **load-bearing** — without it Step 7's differentiation
> carries an extra $\sum_iA_i\,\partial_\kappa h(\pi_i)$ term and CLAIM (ii) is false — and the
> writer knows it: the NUMERICAL CHECK REQUEST adopts $P(\pi)=m_0+\Delta_m\pi$ and calls it
> "a convention of the check, not a model claim". **Lift it into a numbered hypothesis and cite it
> at Step 7.** Note that L4 names this same object as an assumption it cannot prove — the second
> half of (br-ii), with "I do not prove that and I do not claim it" attached. **L4's treatment is
> the correct standard and L3 should match it, not the other way round.**

> **L3-R2 (REPAIR). The "two derivations that do not share a step" are not independent; L3's own
> Step 14 proves their hypothesis sets are equivalent.**
>
> LABEL CLAIMED defends PROVED for (ii) partly on the ground that it "is derived twice by routes
> that do not share a step — Step 8 from the weight derivatives, Step 8′ from the chord-gap
> decomposition plus the conservation laws — which agree." Checked: Step 8 consumes Hypothesis 2's
> three restrictions; Step 8′ consumes $A_{1/2}'=-2A'_\kappa$ plus Hypothesis 6's conservation of
> pooled mass and pooled engagement moment. **Step 14 then proves
> $[\mathrm m'=0\text{ and }\mathrm r'=0]\iff[A_0'=A_1'\text{ and }A_{1/2}'=-2A_1']$** — the two
> input sets are logically equivalent, and Step 15 says so in as many words. So Step 8′ is the same
> hypothesis in different coordinates, not an independent check on Step 8. The routes share no
> *step*; they share their *content*.
>
> This is not a defect in the mathematics — both routes are correct — but it weakens one of the four
> reasons offered for PROVED, and the second pass should not count it as a second voter. What Step
> 8′ genuinely adds, and what should be claimed instead: it displays the mechanism (all interior
> motion is carried by the mass of the single middle atom, the affine part contributing nothing), it
> is the form that generalises to $\partial_\kappa\mathbb E_\kappa[h]=\sum_iA_i'(h-\ell_h)(\pi_i)$,
> and it is therefore the part that transfers to Example B. That is worth more than a redundant
> second derivation, and it should be sold as that.

> **L3-R3 (REPAIR — notation, and it is a card-symbol collision).** WHERE-IT-FAILS 3 writes
> "$\Theta(\bar\pi^{3/2})$", using $\Theta$ as Landau big-Theta. Card §4.5 makes $\Theta$ the
> compact ordered cutoff polytope and card §8 rule 4 forbids re-keying a card symbol; the NOTATION
> DELTA does not declare it. This is worse than an undeclared new symbol — it is a card symbol used
> with a second meaning. Write "of exact order $\bar\pi^{3/2}$" instead. (Cross-check: P1 uses
> $\Theta$ correctly as the polytope in all 16 occurrences.)

> **L3-R4 (REPAIR — cosmetic, but it is the exact repair turn-2 made to L2).** Two items.
> (a) The hypothesis-use table is off in both directions: Hypothesis 1 is listed "Used at Steps 7,
> 12, 14" but Step 12 consumes it only through Step 8; Hypothesis 6 is listed "Used at Steps 9, 15"
> but Step 8′ consumes it explicitly and is not listed. (b) **D1 is cited inside Hypothesis 6's
> parenthetical rather than being a numbered hypothesis.** Turn-2's L2-R4 made precisely this repair
> to L2 ("Step 3's '$D$ is a function of $W$' *is* D1's Step-7 product formula; add D1 to L2's
> hypothesis list"). L3 inherits the same structure and should inherit the same repair, so that
> D1's CONJECTURE status is visibly propagated into L3.

> **L3-R5 (REPAIR — minor).** Step 12's second route — vanishing under continuity of $h$ at $0$
> alone — still needs one and the same $h$ across the shrinking family, which is Hypothesis 5's
> first clause. Step 12 names Hypothesis 5 only for the bounded-$h''$ route. Cite it in both places,
> or the "under continuity alone" sentence reads as needing less than it does.

> **L3-O1 (OBSERVATION).** Step 15's headline — "A(τ)'s derivative restrictions are implied by the
> model at fixed policies and are not a separate assumption" — drops the differentiability-in-$\kappa$
> of the weights, which is *not* implied by the model; the proof's own WHERE-IT-FAILS 4 shows a
> plan entering or leaving the pooled class at a $\kappa_0$ kills it. CLAIM (v) carries the caveat
> ("weights differentiable in $\kappa$"); Step 15's summary sentence does not. Wording only.

> **L3-O2 (OBSERVATION).** The WHERE-IT-FAILS 3 witness $h(\pi)=\pi^{3/2}$ has
> $C_h(\bar\pi)=+0.29289\,\bar\pi^{3/2}>0$ (executed check 4), i.e. it sits **outside** the card's
> maintained orientation $C_h\le0$. It is a legitimate witness for the regularity point — NOT
> CLAIMED 2 correctly says the proof uses no sign for $C_h$ anywhere — but a reader should know the
> separating example is a kernel A(τ)'s own orientation excludes. A concave witness with unbounded
> $h''$ at $0$ (e.g. $-\pi^{3/2}$ shifted to keep $h\ge0$) would make the same point inside the
> orientation.

> **L3-O3 (OBSERVATION).** Example A's informed mark $2\bar z$ is the same for every Voice signal,
> i.e. the stake path is flat in $s$ across the Voice region. That is exactly the configuration
> turn-2's L2-R1 shows destroys A7-injectivity. Example A has no flagged set, so nothing breaks —
> but it records why Example A cannot be promoted into a two-round witness, which is the same
> conclusion Step 18 reaches from the $\bar\pi=1$ side.

> **L3-O4 (OBSERVATION — a card gap Step 9 exposes, and it propagates into L4).** Step 9 correctly
> notes that A(τ) can be read with conditional weights (summing to $1$) or unnormalised ones
> (summing to $1-\Omega$), and that Step 8's identity holds verbatim in both. What it does not say
> is that **$A'_\kappa$ then means two different numbers**, differing by the factor $1-\Omega$. The
> card's §4.4 $A'_\kappa$ row does not fix the normalisation. This matters downstream: $\mathcal S_P
> =\lvert\partial_\kappa M_P\rvert$ with $M_P=\Delta_m\mathbb E[h\mid D=0]$ is unambiguously a
> **conditional** object, so L4's (br-iii) — $\lvert A'_\kappa(\tau')\rvert\le\lvert A'_\kappa(\tau)
> \rvert$ — must be about the conditional coefficient. Under the unnormalised reading (br-iii) would
> be a materially weaker assumption, because $\Omega(\tau')\ge\Omega(\tau)$ already supplies a factor
> $\tfrac{1-\Omega(\tau')}{1-\Omega(\tau)}\le1$. Recommend the card pin $A'_\kappa$ to the
> conditional normalisation.

---

## 3. L4 — threshold composition lemma

### 3.1 Claim vs the card's ledger row

Card row: *"At fixed policies a lower τ weakly raises Ω, weakly lowers $\bar\pi$ in the pooled
class, and — under L3 and monotone $\lvert C_h\rvert$ — weakly lowers $\mathcal S_P$."*
Intended final label in card §6: *"L4 PROVED under nested reclassification."*

The file's VERDICT UP FRONT rejects the card's own framing: nested reclassification is a
**conclusion** (Step 5), not a hypothesis, and the real burden is a bridge from L3's *interior*
motion to the card's *total* derivative $\mathcal S_P$. It names A(br) with four clauses, adds
$b_0<\tau'<\tau$ and $\Omega(\tau')<1$, deletes three turn-1 hypotheses with reasons recorded
in-file, and supplies an exact identity for leg 2 the card did not have.
**Classification: refinement, with the strongest hypothesis-honesty in the batch.** msg3 §3's three
explicit asks are each answered by number: the step that consumes "every newly flagged history is
Voice" is Step 9 (consumed at Step 11, force analysed at Step 13); the dependence on L3 is an
explicit statement-only citation at Step 15; and the status of $\lvert C_h\rvert$ monotonicity is
declared **maintained, not derived**, at Hypothesis 10 and Step 17.

### 3.2 The steps the audit was asked to stress

**Step 3 (product form from D1's clock equivalence) — PASS.** Both cases written out. The
$a_j=0$ case is immediate. The $a_j=1$ case turns on removing $\{c_j<\infty\}$ as redundant, and
the argument is right in both directions: $f_j\le H$ forces $f_j$ finite, hence
$c_j=f_j-T\le H-T<\infty$ (and if $c_j=+\infty$ then $f_j=\infty$ and $f_j\le H$ is false);
conversely the conjunction is contained in $\{f_j\le H\}$ by set inclusion. Only then is D1's
equivalence invoked, and only as its **ledger statement**. Hypothesis 4 puts both thresholds inside
D1's stated domain and Hypothesis 6 (A4) is what makes $c_j$ a first passage with the filing pinned
at $c_j+T$ — the two things the equivalence is an equivalence *about*. Correct.

The Step-5 remark is worth keeping: if the card's $\partial_dB_j\ge0$ were dropped, D1's equivalence
would have to read $f_j\le H\iff\max_{d\le H-T}B_j(s,d)\ge\tau$, and Step 5's inclusion would still
go through verbatim, because it uses only that **one $s$-measurable number is compared to two
thresholds**. The nestedness conclusion is more robust than the cited form of D1. Correct, and it is
a genuine strengthening the writer flags as not part of the proof.

**Steps 9, 11, 13 (the newly-flagged-is-Voice arithmetic) — PASS, recomputed.**
Step 11's identity re-derived: $\Pr(\{a=1\}\cap\mathcal C_P(\tau))
=\bar\pi_{\mathrm{pr}}(\tau')(\rho_P-\nu)+\nu\cdot1$, divide by $\rho_P>0$, giving
$\bar\pi_{\mathrm{pr}}(\tau)=(1-\tfrac{\nu}{\rho_P})\bar\pi_{\mathrm{pr}}(\tau')+\tfrac{\nu}{\rho_P}$.
Step 12's difference $\tfrac{\nu}{\rho_P}(1-\bar\pi_{\mathrm{pr}}(\tau'))$ and its alternative
closed form $\nu(1-\bar\pi_{\mathrm{pr}}(\tau))/(\rho_P-\nu)$ are algebraically the same number —
executed check 9 confirms both to $1.7\times10^{-16}$ and $6.8\times10^{-14}$ over 200 000 random
admissible triples, with the sign never violated. $\nu/\rho_P\in[0,1]$ from
$\mathcal N\subseteq\mathcal C_P(\tau)$ ✓; $\rho_P>0$ from Step 10 ✓.

**Step 13 is the best step in the file and the audit could not weaken it.** It answers a question
the turn-1 statement did not know it had: why does "newly flagged ⟹ Voice" deliver leg 2
*unconditionally* rather than conditionally? Because the general version's sign is the sign of
$\Pr(a=1\mid\mathcal N)-\bar\pi_{\mathrm{pr}}(\tau')$, and $1$ is the **maximum** value a conditional
probability can take, so the inequality holds for every admissible $\bar\pi_{\mathrm{pr}}(\tau')\in
[0,1]$ with no restriction on *which* histories move. The two corollaries (equality iff $\nu=0$ or
$\bar\pi_{\mathrm{pr}}(\tau')=1$; no strictness available without assuming $\nu>0$, which the card
does not supply) are both correct and both are correctly disclaimed in NOT CLAIMED 2.

**Step 21 (exact $\kappa$-invariance) — PASS.** $D$ is a function of $s$ alone (Step 4);
$a_{j(s)}$ likewise (Hypothesis 1); the marginal law of $s$ carries no $\kappa$ because card §4.1
puts $\kappa$ in the $z_d$ row and nowhere else and A1 gives $z_{0:H}\perp(v,\varepsilon)$. Hence
$\Omega$, $\nu$, $\bar\pi_{\mathrm{pr}}$ and Step 5's inclusion are $\kappa$-free, and legs 1 and 2
hold at every $\kappa$ pointwise rather than on average. Correct, and it is the same argument L3's
Hypothesis 6 runs — the two files agree.

**$b_0<\tau'<\tau$ (Hypothesis 4) — a correct and necessary addition.** Turn-1 did not have it.
The comparison moves the threshold, so the core restriction has to be imposed at the **tighter**
threshold too or D1's equivalence is cited off its domain at $\tau'$. WHERE-IT-FAILS 2 makes the
concrete case, and it is a realistic policy experiment rather than a corner: the point of a tighter
rule is to catch smaller positions. This is exactly the hazard turn-2's D1-O1 opened and the card
closed at §4.1; L4 is the first file to consume it.

**The three deletions — checked, and two are genuine.** Turn-1 H1 (nestedness) is Step 5's
conclusion from D1's equivalence plus path-fixity; carrying it would assume the first leg. Turn-1 H3
is H2's contrapositive on $\{a=0\}$ and is redundant twice over. Both deletions are right. Turn-1 H2
is discussed at L4-O2.

**A(br)'s four clauses — each is used** ((br-i), (br-ii) at Step 16; (br-iii) at Step 18; (br-iv) at
Steps 14 and 16). **Is (br-iii) derivable? Attacked, and no.** Under the conditional normalisation
Hypothesis 6 and Step 14 leave the pooled law a **one-parameter** family — $\mathrm m\equiv1$ and
$\mathrm r\equiv\bar\pi_{\mathrm{pr}}$ pin $A_0$ and $A_1$ once $A_{1/2}$ is chosen, so
$A'_\kappa=-A_{1/2}'/2$, the rate at which mass flows into the single pooling atom. Nothing in the
card ties that rate across two *different* pooled populations. Step 18's refusal and
WHERE-IT-FAILS 4's counter-story (the reclassification strips the low-end anchors and leaves a pool
whose weights swing more) are both correct. **(br-iii) is a genuine assumption and NOT CLAIMED 3's
"I have no argument for it" is the honest report.**

### 3.3 Findings

> **L4-R1 (REPAIR — the $\bar\pi$-reading inconsistency, and it is a live disagreement between two
> files in this batch).**
>
> L4's top-of-file remark and Step 14 say the map $\bar\pi_{\mathrm{pr}}\mapsto\bar\pi$ is "the
> identity" under the card §4.4 gloss and $\bar\pi=2\bar\pi_{\mathrm{pr}}$ under the level-symmetric
> reading $A_0=A_1$, and conclude: *"(br-iv) covers both and nothing below depends on which."*
>
> **L3's Step 19 proves the identity branch is degenerate.** With support
> $\{0,\bar\pi/2,\bar\pi\}$, conditional weights summing to $1$ and mean $=\bar\pi$, one gets
> $A_0=A_1-1\le0$, hence $A_0=0$, $A_1=1$, $A_{1/2}=0$: a point mass at $\bar\pi$, $A'_\kappa=0$,
> and zero interior motion for **every** kernel. Executed check 8 reproduces it. So under the
> identity branch, $\mathcal S_P(\tau)=\mathcal S_P(\tau')=0$ identically and leg 3's inequality
> holds only because both sides are zero. *"Nothing below depends on which"* is true of the
> inequality and false of its content.
>
> The factor-two branch is fine and is confirmed: executed check 10 verifies that $A_0=A_1$ gives
> $\mathbb E[\Pi_\kappa]=\bar\pi/2$ at every admissible level, and L3's Example A instantiates it
> ($\bar\pi=1$, $\rho=\tfrac12$). Note also that the two files reach the *same* non-degenerate
> reading by different routes — L3's Hypothesis 3 calls $\bar\pi$ the top of the pooled support, L4
> calls it twice the pooled prior share under level symmetry, and in the frozen manuscript's
> structure these coincide.
>
> **Repair:** adopt L3's Hypothesis-3 reading, drop the identity branch from (br-iv), and record
> that the card §4.4 gloss ("pre-order pooled engagement share in the chord") is the wording that
> generated the confusion and needs adjudicating. Non-blocking: no step delivers a false conclusion.
> But this and L3's Step 19 together are a **card-reading finding the orchestrator must settle
> before T1**, because T1's $W_\tau,C_\tau$ inherit both.

> **L4-R2 (REPAIR). (br-ii) is not independent of (br-i) under the card's literal A(τ), and the
> hypothesis list should say what it is actually buying.**
>
> The card's A(τ) displays $\mathbb E[h]=A_0(\kappa)h(0)+A_{1/2}(\kappa)h(\bar\pi/2)+A_1(\kappa)h
> (\bar\pi)$ with $\bar\pi$ and $h$ carrying no $\kappa$ argument. Read literally, (br-i) — "the
> representation holds at both thresholds" — **already** localises all $\kappa$-dependence in the
> weights, and (br-ii) restates it; Step 16's framing ("(br-i) makes the representation available,
> (br-ii) localises") treats them as two.
>
> Where (br-ii) genuinely earns its place is against the honest reading, not the literal one: by
> L3-R1, $h(\mathcal I)=\pi\,p(\hat v,\pi)$ is a function of two scalars, so "$h$ as a function of
> the posterior is $\kappa$-free" is real content that A(τ)'s notation hides. **Say that.** As
> written the hypothesis block advertises four independent clauses and delivers three and a half;
> restated, (br-ii) becomes the clause that repairs a card ambiguity, which is a better result than
> a redundant clause. L4's honesty here — "I do not prove that and I do not claim it" — is the
> standard the batch should converge on, and L3 should be brought up to it rather than L4 down.

> **L4-R3 (REPAIR — miscitation).** Step 5 cites *"card §2.5"* for
> $\mathcal C_F(\tau,T)=\{(j,s,z_{0:H}):D_j(s;\tau,T)=1\}$. `MODEL_CARD.md` has **no §2.5** — §2 is
> "Timing (the two rounds)", four unnumbered bullets. §2.5 is a section of
> `threads/thread1_turn1_answer.md` ("The disclosure flag and the partition"). The content is
> card-backed elsewhere (§4.3's cell row plus §4.2's $D_j$ row), so the claim stands and the pointer
> does not. Re-point it.

> **L4-R4 (REPAIR — NOTATION DELTA incomplete).** Undeclared: (a) a **bare $\Delta$** used as a
> window increment in WHERE-IT-FAILS 3 ($T+\Delta$, $\Delta>c(\tau)-c(\tau')$) and as a difference
> operator in the check block ($\Delta\Omega$, $\Delta\bar\pi_{\mathrm{pr}}$,
> $\Delta\mathcal S_P$) — the card's $\Delta$ family ($\Delta_m,\Delta_V,\Delta^{\mathrm{act}},
> \Delta_{\kappa k},\Delta_{kr},\Delta_{kk},\Delta_k$) is uniformly decorated, and L3's own delta
> declares "no bare $\Delta$ appears" as a standard it observes, so the batch is internally
> inconsistent; (b) the threshold-indexed $A'_\kappa(\tau)$, $A'_\kappa(\tau')$, $\bar\pi(\tau)$,
> $\bar\pi(\tau')$ — seven occurrences, a card symbol given a new argument; (c) $X_{0:H}$ (card has
> $X_d$; §4.6 blesses $z_{0:H}$ only); (d) $s^\ast$. All cosmetic; only the bare $\Delta$ risks a
> misread.

> **L4-R5 (REPAIR — cosmetic, but it will confuse a referee).** The file runs **two incompatible
> leg-numbering schemes.** The VERDICT calls the $\Omega$ result "Leg 1", the $\bar\pi$ result
> "Leg 2" and the $\mathcal S_P$ result "Leg 3"; the CLAIM lists four numbered items in which the
> $\Omega$ result is item 2, $\bar\pi$ is item 3 and $\mathcal S_P$ is item 4, and then says
> "Legs 1–3 are unconditional …; leg 4 is conditional on A(br)". Hypothesis 8's parenthetical
> "(which by leg 2 also gives $\Omega(\tau,T)<1$)" is right under the CLAIM numbering and wrong
> under the VERDICT numbering; Step 10 gets it right by citing Step 7 directly. Pick one scheme.

> **L4-O1 (OBSERVATION).** Step 16 cites Step 21 forward ("Partial support for (br-ii) … comes from
> Steps 4 and 21"). Step 21 does not depend on Step 16, so there is no circularity, but a forward
> citation in a numbered proof invites the reader to check for one. Reorder.

> **L4-O2 (OBSERVATION). The deletion of turn-1 H2 is a relabelling, not a derivation, and the
> difference matters for T1.** Step 9 derives $\Pr(a=1\mid\mathcal N)=1$ from Hypothesis 7, the
> card's $D=1\Rightarrow a=1$ — which is **definitional**: the disclosure indicator carries $a_j=1$
> as a conjunct. So the assumption did not disappear; it moved from L4's hypothesis list into the
> card's definition of $D$ and A4's "only Voice plans cross in the core". The substantive economic
> question turn-1's H2 was guarding against — a passive blockholder who crosses $\tau$ and must file
> — is **excluded by construction, not proved away**. L4 is entirely straight about this (it lists
> Hypothesis 7 and cites the card), and turn-1 H1 and H3 really are conclusions. Logged because T1
> inherits the composition effect and a referee will ask this question of the *model*, not of L4.

> **L4-O3 (OBSERVATION).** (br-iii) attacked and confirmed underivable (§3.2 above). The one thing
> worth adding to Step 18: under the conditional normalisation A(τ) leaves exactly one free function
> of $\kappa$, so $\lvert A'_\kappa\rvert=\lvert A_{1/2}'\rvert/2$ is a single scalar — "the rate at
> which noise pushes mass into the pooling atom". Saying it that way makes (br-iii) an economically
> interpretable assumption rather than an opaque one, and makes NUMERICAL CHECK item 5 (which
> measures exactly this residual) legible.

---

## 4. P1 — cutoff PBE existence

### 4.1 Claim vs the card's ledger row

Card row: *"Under A1–A7 a cutoff PBE over complete contingent plans exists; under A8 both cells are
on path."*

The proof states plainly that **the card's row overstates what A1–A7 deliver**: sequential
optimality of the flagged component (item (ii) of card §3) is not among their consequences, and it
adds h.11 (flagged closure), h.12 ($m_0\ge0$) and h.13 (Voice stake monotonicity across plans,
Step 20 only). It also *removes* burden in two places — Step 7 derives the existence-and-uniqueness
half of A5 rather than assuming it, and Step 13 derives the "weakly ordered / maps $\Theta$ into
itself" halves of A6 from A3. **Classification: refinement, and an unusually candid one** — Step 15
names itself "the single largest assuming-rather-than-deriving step in this proof".

### 4.2 The steps the audit was asked to stress

**Step 4 (reduction to $(\hat v,\pi)$) — PASS, re-derived and Monte-Carlo checked.**
Conditionally on $\mathcal I$, $\mathsf B$ is a function of $\xi$ alone, and A1 gives
$\xi\perp(v,\varepsilon,z_{0:H})$, hence $\mathsf B\perp(v,a)\mid\mathcal I$. Term by term:
$\mathbb E[(1-\mathsf B)(v+a\Delta_V)\mid\mathcal I]=(1-p)(\hat v+\pi\Delta_V)$ and
$\mathbb E[\mathsf B(P+m_0+a\Delta_m)\mid\mathcal I]=p(P+m_0)+\Delta_m p\pi$, summing to
$(1-p)(\hat v+\pi\Delta_V)+p(P+\bar m)$. Exactly Step 4's display. Executed check A matches Monte
Carlo within MC noise. **The two-scalar reduction is the load-bearing structural fact of the whole
file and it is correct.** (It is also the fact that refutes L3's Step 7 — see L3-R1.)

**Step 7 (h.12 bracket and strict-down-crossing uniqueness) — PASS, calculus verified line by line
and by executed sweep.**
(i) For $P<A$ both terms of $\varrho$ are nonnegative and the first is strictly positive since
$p<1$ ✓. (ii) $\varrho(A)=p(A)\bar m\ge0$ ✓; the explicit bracket is arithmetically exact — at
$P=\bar S-K-\bar m+\sigma_\xi$ the $\Phi$-argument is exactly $1$, so $p\le1-\Phi(1)=0.1587<0.159$,
whence $\varrho\le-0.841(P-A)+0.159\bar m\le0$ once $P-A\ge(0.159/0.841)\bar m=0.1891\bar m$, and
$0.19>0.1891$ ✓; taking the max of the two lower bounds secures both conditions and the left
endpoint $A$ satisfies $\varrho\ge0$ ✓. (iii)
$\varrho'(P)=p'(P)(P+\bar m-A)+p(P)-1$; at a root $P\ge A$ by (i), so $P+\bar m-A\ge\bar m\ge0$ by
h.12 and $p'<0$ makes the first term $\le0$, the second $<0$ ✓. **Executed check B: 0 bracket
failures, 0 multiplicity failures and 0 sign failures across 20 000 random parameter draws.**

**Step 8 — PASS.** $\partial\varrho/\partial\hat v=1-p$ (no $\hat v$ inside $p$),
$\partial\varrho/\partial P=-[(1-p)+\lvert p'\rvert(P+\bar m-A)]$, so
$\partial P/\partial\hat v=(1-p)/[(1-p)+\lvert p'\rvert(P+\bar m-A)]\in(0,1]$, equal to $1$ exactly
when $\bar m=0$. Executed check C: never outside $(0,1]$, analytic vs numerical agreement
$6.7\times10^{-10}$.

**Step 6, the Lusin–Souslin step — PASS, and it is stronger than needed** (see P1-O1). Both
$\mathcal J\times\mathbb R$ and $[0,\bar b]^2\times\{1\}$ are standard Borel; the flagged set is a
Borel subset by Step 2; h.7 gives injectivity; so Lusin–Souslin does deliver a Borel image and a
Borel inverse. The step is right. Turn-2's L2-O1 recorded the same theorem for L2 and P1 states it
correctly ("Injectivity plus measurability already delivers the measurable inverse; no separate
assumption is introduced").

**Step 13 (A3 ⟹ ordered best response) — PASS.** $\{s:j^\star\ge i+2\}\subseteq\{s:j^\star\ge i+1\}$
gives $\mathcal T_{i+1}\ge\mathcal T_i$ (an infimum over a subset is weakly larger), and
$\inf\emptyset:=\overline s$ keeps the ordering and the range at the empty end ✓. The honest framing
is right: A6's ordering content is derived **from A3's monotone-preferred-plan clause**, which is
itself an assumption — so the burden moves from A6 to A3 rather than vanishing, and Step 13 says so.

**Step 20 (A8 / h.13 reformulation) — PASS on the mathematics.** The composite
$s\mapsto B_{j_{k^\star}(s)}(s,H-T)$ is weakly increasing because it increases in $s$ at fixed plan
(card §4.2) and across plans (h.13); intersecting the up-set $\{a=1\}$ with an up-set gives an upper
interval; $\Omega=1-\Phi_s(s_F)$ since $s$ is continuous ✓. Step 20's candour — "Read literally,
Step 19 is close to a restatement of h.8" — is correct and welcome.

### 4.3 Findings

> **P1-R1 (REPAIR — the important one). h.11's primary form is jointly unsatisfiable with h.2, and
> P1 survives only on h.11's second reading.**
>
> h.11 asks: for every $j\in\mathcal J$, every flagged $s$, and **every** feasible
> $Q'\in[0,\bar b-B_j^F(s)]$, there exists $j'\in\mathcal J$ with the same pooled path up to $f_j$,
> the same flag, and $Q_{j'}^F(s)=Q'$. h.2 (A2) makes $\mathcal J$ finite, so
> $\{Q_{j'}^F(s):j'\in\mathcal J\}$ has at most $\lvert\mathcal J\rvert$ elements and **cannot
> cover an interval of positive length**. h.11-primary therefore forces $B_j^F(s)=\bar b$ at every
> flagged $(j,s)$ — i.e. $Q^F\equiv0$ and round 2 is empty — which contradicts the card's §4.2
> $Q^F$ row (Voice plans have $Q^F\ge0$ with $T'<T\Rightarrow Q^F(T')\ge Q^F(T)$, so $Q^F$ genuinely
> varies). Executed check D states the cardinality argument.
>
> The proof's own second reading rescues it: *"the round-2 action set is **defined** to be
> $\{Q_{j'}^F(s):j'\in\mathcal J\text{ shares }j\text{'s pooled path up to }f_j\}$ rather than the
> full interval."* That is consistent with h.2 and is all Step 12's argument needs — Step 12 runs
> verbatim on it. **Repair: strike the primary form and keep only the action-set reading**, and stop
> calling it a *closure* condition: it is not closure, it is a modelling stipulation that the
> round-2 action set is the plan-generated one, which is a different and much weaker thing.
>
> This is the direct analogue of turn-2's L2-R1 (a hypothesis stated in a form the model cannot
> satisfy, making a correct proof vacuous) but sharper in two ways: the contradiction is with
> **another of P1's own numbered hypotheses**, and it takes one line to see. It does not block,
> because the proof supplies the consistent reading itself — but if a later turn keeps h.11-primary,
> P1's CLAIM is vacuous.

> **P1-R2 (REPAIR). "h.11 is the weakest condition that delivers it" is asserted, not established;
> the standard PBE route is never considered.**
>
> Step 12's converse paragraph correctly shows date-0 optimality over a finite menu does not
> constrain off-menu round-2 orders. It then concludes h.11 is needed and is weakest. But the
> textbook route to sequential rationality at an unreached node is not a closure condition — it is
> **off-path beliefs**. Card §3(vi) requires off-path beliefs to be limits of full-support
> perturbations, and P1's own Step 9 perturbs **only the plan menu** (each type plays each
> $j\in\mathcal J$ with weight $\ge1/n$). Round-2 orders outside the menu image are then reached at
> no $n$, their limit beliefs are unconstrained by the perturbation, and the modeller is free to
> choose them. Whether some admissible choice deters every off-menu deviation is a genuine question
> — and not an obvious one, since a punishing (high) off-path $P^F$ makes the deviation purchase
> dearer but also raises the takeover-branch value of $Y$ — and **no step addresses it**.
>
> **Repair:** either argue that no admissible off-path belief system deters the deviation (which
> would be a real result and would justify "weakest"), or downgrade to "h.11 is *a* sufficient
> condition; whether an off-path-belief route also delivers item (ii) is open". Non-blocking: h.11
> does deliver Step 12.

> **P1-R3 (REPAIR). Step 10's "on path and off" does not mean what a reader will take it to mean.**
> Step 10 says the flagged belief is pinned "at every flagged tuple, on path and off". "Off path"
> there covers tuples generated by $(j,s)$ pairs the conjecture $k$ does not select. It does **not**
> cover tuples outside the **image** of $(j,s)\mapsto\sigma_F$ — exactly the tuples a round-2
> deviation to an off-menu $Q'$ produces — and no step assigns those a belief. Under h.11's
> action-set reading no such tuples exist and the gap closes. Say which reading Step 10 stands on
> and cite it; as written, Step 17(vi) inherits a hole that Step 12 has already silently filled.

> **P1-R4 (REPAIR). Step 15's named weakest replacement is close but two of its ingredients are
> misstated.**
> (a) **Separate continuity is not joint continuity.** The paragraph before (i)–(ii) establishes
> continuity of $U_j(s;k)$ **in $k$** at fixed $(j,s)$; condition (i) supplies continuity **in $s$**
> at fixed $k$. The boxed conclusion then invokes "continuity of $U$ in $(s,k)$", which is strictly
> stronger than the conjunction of the two and is nowhere argued. Step 18's Kakutani remark repeats
> the overstatement ("$U_j(s;k)$ is jointly continuous in $(s,k)$ under Step 15(i) alone"). Joint
> continuity is plausible from the structure — finitely many $j$, prices continuous in $k$, $(\hat
> v,\pi)$ ratios of integrals over intervals with endpoints $k$ — but it must be stated as the
> condition, because it is what the crossing-point argument consumes.
> (b) **The implicit function theorem is the wrong tool.** It needs $U$ differentiable in $(s,k)$,
> which no hypothesis supplies. What actually locates the crossing and moves it continuously is
> joint continuity plus the strict sign change — a topological argument, not a calculus one. Name it
> that way.
> The conclusion is right and (i)+(ii) is close to the right pair; only the derivation of the
> implication is loose. Note in (i)'s favour that Step 15's closing remark — a stake path flat on a
> signal interval destroys h.7's injectivity there, so the card cannot buy continuity by weakening
> monotonicity — is correct and is turn-2's L2-R1 seen from the other side.

> **P1-R5 (REPAIR). Step 20 rests on three conditions and numbers only one of them.** The
> reformulation supposes (a) the engagement flags $a_j$ are $1$ **exactly on an upper set** of the
> ordered menu, (b) $\partial_sB_j\ge0$ on Voice plans, (c) h.13. (b) is card §4.2 ✓ and (c) is
> correctly flagged as not in the card. **(a) is neither.** Card §4.2 says $a_j=1$ for Voice and $0$
> for Exit/Hold and orders the menu "least to most aggressive", but never ties the two; card §4.5's
> four-action gloss happens to satisfy it, a general finite menu need not. Number (a) as an
> [ADDITION] or fold it into h.13 — otherwise the file's own rule ("Each is cited by number at the
> step that consumes it") is broken at the one step that consumes it.

> **P1-R6 (REPAIR — miscitation, and it is load-bearing).** Step 11 writes *"Card §2.10's payoff
> $U_j(s)=\mathbb E[b_j^*(s)Y-\mathcal C_j^{\mathrm{trade}}-C_j(s)\mid s,j]$"*, and Step 14 cites
> §2.10 again. **`MODEL_CARD.md` has no §2.10, no blockholder payoff row at all, no
> $\mathcal C_j^{\mathrm{trade}}$**, and mentions $C_j(s)$ only inside §4.4's overload note. The
> object lives in `threads/thread1_turn1_answer.md` §2.10, which P1's own source list declares only
> at *§P1*. I checked the source: the quoted form is faithful to it. But **$U_j$ is the objective
> Steps 11–13 maximise and Step 15 asks to be continuous** — so P1's central optimand is imported
> from outside the card while the file claims to work from the card. Card §8 rule 2 says cite only
> what the card carries.
>
> **This is the one repair with a recommendation beyond re-pointing a citation:** the card is
> missing the blockholder payoff row. P1, L2 and every future best-response argument need it.
> Recommend the orchestrator add §2.10's $U_j$, $\mathcal C_j^{\mathrm{trade}}$ and $C_j(s)$ to the
> card as a §4.2 or §2 addition, the same way turn-2's four card facts were absorbed.

> **P1-R7 (REPAIR — NOTATION DELTA incomplete, and one item breaks a binding ruling).**
> (a) **A bare $g$.** Step 6(b): *"Write $g(\cdot)$ for the map sending a belief $\hat v$ to the
> unique root"*, used again at Step 6(d) as $P^F=g(\hat v)$. $g$ is **not** in P1's NOTATION DELTA;
> it collides with card §4.5's $g_r^{PE}$; and msg3 §2 item 2's binding ruling reserved $g$ for
> **L3's mean-value form** ("`g` is reserved for the L3 mean-value form below"), which L3 duly uses.
> Two files in one batch using the same reserved letter for different objects is exactly what the
> notation lane exists to stop. Rename (e.g. $G_P$, or fold it into $\mathcal P$).
> (b) **$\beta$ carries two meanings inside P1.** Steps 6 and 10 use card §4.1's Gaussian projection
> coefficient $\beta$ correctly; WHERE-IT-FAILS 3 uses $[\alpha,\beta]$ for a signal interval.
> Undeclared. Rename the interval endpoints.
> (c) $\mathcal C_j^{\mathrm{trade}}$ (Step 11) is undeclared — a consequence of P1-R6.
> Everything else checked line by line against card §4 and the declared table: $j_k$, $U_j(s;k)$,
> $\mathcal P_{\mathcal I}$, $\varrho$, $\phi$, $\bar m$, $\hat v$, $A$, $[\underline s,\overline
> s]$, $\sigma_F$, $\iota_F$, $\mathfrak T$, $s_F$, $\Phi_s$, $1/n$ are all declared and all the
> collision checks in the table are accurate. $\varrho$-because-$\psi$-is-reserved is a correct and
> well-documented choice. $\Theta$ is the polytope in all 16 occurrences (contrast L3-R3).

> **P1-R8 (REPAIR). Step 5 applies the control-node fixed-point map to intermediate pooled dates,
> where it is not a fixed point.**
>
> Step 4 is derived at *"a control-node information set $\mathcal I$"* — that is where $\mathsf B$
> is $\xi$-measurable given the conditioning. Step 5 then applies it to the whole pooled family:
> *"By Step 3 there are finitely many pooled public histories. For each of them, h.5 supplies a
> unique fixed point of $\mathcal P_{\mathcal I}$."*
>
> But $\mathcal H_d^P$ for $d<H$ is not a control node. Card §4.3's $Y$ row has the takeover branch
> $\mathsf B(P+m_0+a\Delta_m)$ with $P$ unqualified. Under the natural economic reading — and it is
> the reading Step 4 itself adopts — that $P$ is the **control-node** price $P(\mathcal I_H)$, in
> which case $P_d^P=\mathbb E[Y\mid\mathcal H_d^P]=\mathbb E[P(\mathcal I_H)\mid\mathcal H_d^P]$ by
> the tower property: a plain conditional expectation of already-solved control-node prices, with
> **no self-reference and no fixed point**. Under the other reading (the $P$ inside $Y$ is the price
> at whichever information set is conditioning) Step 5 is right as written.
>
> Step 5's conclusion — the pooled price family is a finite vector of functions continuous in $k$ —
> **survives either way**: at the control node by Step 7 plus h.5, and at intermediate dates as a
> finite-sum conditional expectation of continuous functions. So nothing downstream breaks
> (Step 11's pooled-execution bracket and Step 15's continuity both still go through). But the
> argument as written cites the fixed-point clause of h.5 for an object that, on the natural
> reading, has no fixed point. **Repair: split Step 5 in two — the pooled control-node cell
> ($D=0$ at date $H$), a genuine fixed point of Step 4's map; and dates $d<H$, a tower-property
> expectation — and record the card ambiguity in §4.3's $Y$ row as something the orchestrator should
> pin.**

> **P1-O1 (OBSERVATION). Lusin–Souslin is not load-bearing at Step 6, and saying so is worth a
> line.** Step 6(c) offers two routes. Route 1 alone suffices: $\hat v(\sigma_F;k)=\mathbb E[v\mid
> \sigma_F,D=1]$ is $\sigma(\sigma_F)$-measurable by construction, hence a Borel **function** of
> $\sigma_F$ by Doob–Dynkin, which is exactly what Step 6(d)'s composition needs. Route 2
> (Lusin–Souslin) buys the *explicit* form $\hat v=\mu_v+\beta(\iota_F(\sigma_F)_s-\mu_v)$ and the
> Borel image, which are convenient and are what Step 10 quotes, but are not required for the
> family to exist. The hypotheses do support route 2 as written. Recording it so a referee does not
> read P1's existence proof as resting on a descriptive-set-theory theorem — it does not.

> **P1-O2 (OBSERVATION).** Step 7(iii)'s uniqueness argument opens "Suppose two roots $P_1<P_2$
> **with no root between them**" without saying why such a pair exists. It does, in one line: $\varrho'<0$
> at every root makes every root isolated, the root set is closed because $\varrho$ is continuous, and a
> closed discrete subset of a compact interval is finite, so between any two roots there is a
> consecutive pair. Write the line.

> **P1-O3 (OBSERVATION).** Step 17(ii)'s "at the cutoff points the two adjacent plans are
> indifferent (Step 13's construction)" needs continuity of $U_j(\cdot;k)$ in $s$ — that is Step
> 15(i), which Step 15 declares the card does **not** supply. Under h.6 alone (continuity of
> $\mathcal T$ asserted) the indifference at the cutoff is not delivered. NOT CLAIMED 8 disclaims
> the cutoff-point indeterminacy, so nothing is over-claimed; the step should cite Step 15(i)
> rather than assert.

> **P1-O4 (OBSERVATION — cross-proof discipline).** WHERE-IT-FAILS 1 argues from *"L2's Step-9
> analogue"*. That is L2's **proof internals**, not its ledger statement. It sits in a failure case
> rather than a numbered step, so nothing load-bearing rides on it, and the point it makes (a
> $\kappa$-varying fixed-point **selection** would destroy flagged invariance) is correct and is the
> same point turn-2 confirmed at L2's Step 9. Restate it against L2's ledger row.

> **P1-O5 (OBSERVATION).** Hypothesis-use table overstates twice: h.2 is listed as used at Step 16,
> which cites only Step 1, Step 13 and h.6; h.1 is listed at Step 7, which consumes it only through
> Step 4. Same class as L3-R4(a). Every hypothesis **is** used somewhere, so the scan passes; the
> table just points at the wrong steps.

---

## 5. Cross-proof consistency

1. **$\bar\pi$.** L3 Step 19 and L4 (br-iv)/Step 14 disagree in substance about the admissible
   readings. **L4-R1** carries it. The orchestrator must adjudicate before T1, because T1's
   $W_\tau$, $C_\tau$, $W_T$, $C_T$ all inherit whichever reading wins. Recommended resolution:
   L3's Hypothesis 3 ($\bar\pi$ = top of the pooled support), with the card §4.4 gloss rewritten,
   since it is the only reading under which L3 and L4 both have content and it is the frozen
   manuscript's own.
2. **Is $h$ a function of the posterior alone?** L3 Step 7 assumes it silently (L3-R1); L4 (br-ii)
   assumes it explicitly and disclaims it (NOT CLAIMED, Step 16); **P1 Step 4 proves it is false as
   stated**, since the control-node price depends on $(\hat v,\pi)$ and $h=\pi p(\hat v,\pi)$. All
   three files touch the same object and only one of them says so. L4's treatment is the standard.
3. **Ledger-statement discipline.** L4 cites D1 and L3 by ledger statement only and re-derives L3's
   proportionality constant from the card's A(τ) rather than reading L3's Step 8 — clean, and it
   makes L4's Step 15 an incidental **independent re-derivation of L3 CLAIM (ii)** worth recording.
   L3 cites L2 as a card ID only. P1 cites D1 by statement but reaches into L2's Step 9 once, in a
   failure case (P1-O4). No proof relies on another's internals in a numbered step.
4. **$\kappa$-invariance of the composition objects.** L3 Hypothesis 6 and L4 Step 21 run the same
   argument to the same conclusion, independently and consistently. Both are correct.
5. **Card §-citations.** Two of three files point at sections of `thread1_turn1_answer.md` while
   naming the card (L4-R3, P1-R6). The batch should agree on one convention: cite the card for card
   rows and the turn-1 answer by filename for anything the card has not absorbed — and absorb the
   blockholder payoff, which is the item P1 actually needs.

---

## 6. Counts and what moves

**FAIL 0 · REPAIR 18 · OBSERVATION 12.**

* L3 — REPAIR 5 (L3-R1…R5) · OBSERVATION 4 (L3-O1…O4)
* L4 — REPAIR 5 (L4-R1…R5) · OBSERVATION 3 (L4-O1…O3)
* P1 — REPAIR 8 (P1-R1…R8) · OBSERVATION 5 (P1-O1…O5)

Banned-word hits **0**. draft_v2/external citation hits **0**. Unused hypotheses **0**. Bare steps
**0**. Card-section citations that do not resolve: **2 files, 4 hits** (L4-R3, P1-R6).
NOTATION DELTA incomplete in **3 of 3** files, with one binding-ruling breach (P1-R7a, the reserved
`g`) and one card-symbol re-key (L3-R3, `Θ`). Claim-vs-card: **three refinements, zero drift** — no
file weakened a hypothesis or quietly widened a claim, and all three named their additions.

**Nothing blocks.** No numbered step failed, so the one-retry rule does not fire and no proof is
bounced. Every repair is a card fact that exists but is uncited, a hypothesis that needs restating
in a satisfiable form, a citation that needs re-pointing, or an argument that is right but written
as an assertion.

**No label moves.** Per the protocol, PROVED needs independent re-derivation PASS **plus** Opus
proof-read PASS; this audit is the second half only. **L3, L4 and P1 all remain CONJECTURE**, each
now carrying "proof on file; Opus proof-read PASS 2026-08-21; awaiting Thread 2 re-derivation".
L3's own LABEL CLAIMED (PROVED for parts (i)–(iv)) is noted and moves nothing.

**Risks carried forward, ranked.**

1. **P1-R1** — h.11 must be restated in its action-set form or P1's claim is vacuous. Sharper than
   turn-2's L2-R1 because the contradiction is internal to P1's own hypothesis list.
2. **L4-R1 + L3 Step 19** — the $\bar\pi$ reading must be adjudicated at the card level before T1
   consumes it; one of the two readings L4 declares harmless makes leg 3 identically zero.
3. **L3-R1 / L4-R2** — whether $h$ is a function of the engagement posterior alone is an unpriced
   assumption in L3, a priced one in L4, and false as stated by P1's Step 4. It sits under A(τ)
   itself and therefore under L3, L4 and T1 jointly.
4. **L3 Step 18's OPEN** — whether the two-round pooled cell satisfies A(τ)'s support condition
   (S1)–(S2). Correctly declared open; it now sits alongside A7-satisfiability as the second
   maintained hypothesis in this model with an unverified domain.
5. **P1-R6** — the card has no blockholder payoff row and P1's optimand is imported from the turn-1
   answer. The cheapest of the five to fix and the one that unblocks the most later work.
