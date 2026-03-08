I audited `PROPOSED_FIX.md` (Gemini) against (i) the exact logical/math failures in `ORIGINAL_AUDIT.md`, (ii) the current on-disk `draft_v3.tex` (1462 lines), and (iii) Claude’s flagged concerns in `CLAUDE_AUDIT_OF_FIX.md`.

Bottom line, before I go line-by-line:

* **D3 (premium interpretation) and D4 (formalizing A7: (\lambda_B\le 1/2)) are basically correct** and can be adopted with only tiny bookkeeping edits (line-range mismatch, and one stray environment token in D4c).
* **D6 (minor rigor leaks) is mostly correct**, but the narrative sentence “interior order flows (X\in{-1,0,1}) mix across disclosure states” is wrong for (X=-1) (since (D=1) is impossible there). The Bayes formula itself is fine.
* **D1 (Lemma 2) fixes the *original contradiction* (bounded support implies no fully-uninformative limit), but replaces it with an *unproved* claim ((\omega_Q\to 0) as (\kappa\to 1)) and therefore remains **not theorem-grade** as written.**
* **D2 (Proposition 5) is an improvement in structure (decomposition), but it still **overclaims analytic monotonicities** that are not established from primitives. It should be rewritten as “analytic decomposition + numerically verified monotonic components.”**
* **D5 (Lemma 1 / QA domination) has a real gap. Claude is right.** The step comparing (p(X,1)) and (p(X,0)) via the (k_0) indifference condition is invalid because the inner expectations differ (different (X) distributions and different disclosure regimes), and under A5 you typically have (p(\cdot,1)<p(\cdot,0)).

Below is the exhaustive audit, including the exact points of failure and **camera‑ready LaTeX** patches where needed.

---

# Part 1 — Validate D1–D7 Against P0–P4

I map your Round‑1 issues (P0–P4) to Gemini deliverables (D1–D7) as follows:

* **P0 (Lemma 2 endpoint failure + Prop 5 dependence on it)** → D1, D2, D7
* **P1 (Lemma 1 / QA elimination proof gap)** → D5
* **P2 (premium interpretation inconsistency)** → D3
* **P3 (implicit (\lambda_B<0.5) restriction in Prop 1 proof)** → D4
* **P4 (minor rigor leaks, Bayes objects and decomposition “by definition”)** → D6

I treat each in the format you requested.

---

## P0 — Lemma 2 endpoint behavior and Prop 5 proof dependence

### 1) Original issue (from `ORIGINAL_AUDIT.md`)

**Lemma 2 in `draft_v3.tex` claimed that as (\kappa\uparrow 1), order flow becomes uninformative and posteriors (\pi(X,0)) converge to an unconditional prior across all (X). That is false with the discrete bounded noise (z\in{-1,0,1}).** In particular, for (X=1,D=0),
[
\pi(1,0)=\frac{\omega_Q}{\omega_H+\omega_Q}
]
is **independent of (\kappa)** (because (X=1) under (D=0) pins down (q=0)). Therefore it cannot converge to the unconditional prior as (\kappa\to 1). The old Lemma 2 further claimed (\Delta^{\text{act}}\to 0); numerics falsify that too.

**Proposition 5 relied on that false endpoint**, so its existence/uniqueness-of-interior-max argument was built on sand.

### 2) Fix text that addresses it (Gemini D1 + D2)

The key parts of Gemini’s replacement are:

* **D1a** (new Lemma 2 statement): claims bounded support means some order flow remains informative, but then asserts **(\omega_Q\to 0)** and hence (\pi(X,0)\to 0) as (\kappa\uparrow 1).
* **D1b** (proof): provides microstructure intuition (“max noise homogenizes prices, eliminates stealth advantage, so Quiet Voice collapses”).
* **D2** (Prop 5): decomposes (\Delta^{\min}=\Delta^{\text{base}}+\Delta^{\text{act}}) and claims monotonicities of each component.

### 3) Mathematical evaluation

I break this into three layers:

1. **Does D1 remove the *original logical contradiction*?**
2. **Are D1’s *new* endpoint claims actually proved?**
3. **Does D2’s Proposition 5 become theorem‑correct?**

---

#### Layer 1: the core contradiction is fixed, but only partially

You already have in Appendix B.4 (`draft_v3.tex` lines 1157–1181) the correct posterior formulas (I will re-derive them here; no “see appendix” shortcuts):

Let (p_0(\kappa)\equiv \mathbb P(z=0)=1-\frac{2}{3}\kappa) and (p_1(\kappa)\equiv\mathbb P(z=1)=\mathbb P(z=-1)=\frac{\kappa}{3}).

Let (\omega_E,\omega_H,\omega_Q,\omega_P) denote the unconditional probabilities of Exit, Hold, Quiet Voice, Public Voice.

On the **nondisclosed** branch (D=0), the only actions are Exit (q=-1,a=0), Hold (q=0,a=0), Quiet Voice (q=0,a=1). Public Voice never yields (D=0).

* For (X=1, D=0):
  (X= q+z = 1) can arise under (q=0) with (z=1). It **cannot** arise under (q=-1) because that would require (z=2), which is impossible. Therefore ({X=1,D=0}) implies (q=0), which pools Hold and Quiet Voice only. So:
  [
  \pi(1,0)=\mathbb P(a=1\mid X=1,D=0)=\frac{\mathbb P(Q)}{\mathbb P(H)+\mathbb P(Q)}=\frac{\omega_Q}{\omega_H+\omega_Q},
  ]
  **independent of (\kappa)**.

* For (X=-1,D=0):
  (X=-1) can arise either from (q=0,z=-1) (Hold or Quiet Voice) or from (q=-1,z=0) (Exit). So:
  [
  \pi(-1,0)=
  \frac{\omega_Q\cdot \mathbb P(z=-1)}{(\omega_H+\omega_Q)\cdot \mathbb P(z=-1)+\omega_E\cdot \mathbb P(z=0)}
  =\frac{\omega_Q p_1}{(\omega_H+\omega_Q)p_1+\omega_E p_0}.
  ]

* For (X=0,D=0):
  (X=0) can arise from (q=0,z=0) (Hold/QV) or (q=-1,z=1) (Exit). So:
  [
  \pi(0,0)=
  \frac{\omega_Q\cdot \mathbb P(z=0)}{(\omega_H+\omega_Q)\cdot \mathbb P(z=0)+\omega_E\cdot \mathbb P(z=1)}
  =\frac{\omega_Q p_0}{(\omega_H+\omega_Q)p_0+\omega_E p_1}.
  ]

These are exactly the formulas already in your Appendix B.4.

Now take the limit (\kappa\uparrow 1). Then
[
p_0(1)=1-\frac{2}{3}=\frac{1}{3},\qquad p_1(1)=\frac{1}{3}.
]

So the limits are:

* (\pi(1,0)) stays (\frac{\omega_Q}{\omega_H+\omega_Q}) (no (\kappa)).
* (\pi(-1,0)\to \dfrac{\omega_Q\cdot (1/3)}{(\omega_H+\omega_Q)\cdot (1/3)+\omega_E\cdot(1/3)}
  =\dfrac{\omega_Q}{\omega_H+\omega_Q+\omega_E}.)
* (\pi(0,0)\to \dfrac{\omega_Q\cdot (1/3)}{(\omega_H+\omega_Q)\cdot (1/3)+\omega_E\cdot(1/3)}
  =\dfrac{\omega_Q}{\omega_H+\omega_Q+\omega_E}.)

So D1 is correct that **the “uninformative” claim is wrong**: the limit is not the unconditional prior (\omega_Q/(\omega_E+\omega_H+\omega_Q+\omega_P)), and even at (\kappa=1) you do **not** get state‑invariant posteriors because (\pi(1,0)\neq \pi(0,0)) unless (\omega_E=0).

So **D1 fixes the original contradiction** insofar as it no longer asserts “all posteriors converge to an unconditional prior” with bounded noise.

---

#### Layer 2: D1’s new claim (\omega_Q\to 0) as (\kappa\uparrow 1) is NOT proved

This is the critical issue.

Gemini’s D1 wants to replace the false “uninformative posterior limit kills voice” with “bounded support remains informative, but **equilibrium shifts so that Quiet Voice collapses ((\omega_Q\to 0))**.”

Mathematically, the statement “(\omega_Q\to 0)” is **a claim about the equilibrium correspondence** (\kappa\mapsto (k_1(\kappa),k_0(\kappa),k_D(\kappa))) (or (\omega(\kappa))). You cannot get it from Bayesian algebra alone; you need a comparative statics argument on the blockholder’s best response, with equilibrium feedback through prices and beliefs.

Gemini’s D1b proof does not do that. It appeals to a Kyle-style intuition (“more noise reduces adverse selection cost”) but never derives the sign of:
[
\frac{\partial}{\partial \kappa}\Big(U_Q(s;\kappa)-U_P(s;\kappa)\Big),
]
nor does it show that the indifference cutoffs satisfy (k_D(\kappa)-k_0(\kappa)\to 0).

Even worse: your own `NUMERICAL_VERIFICATION.md` table shows (\omega_Q) can hit zero at (\kappa=0.63), then become positive again at (\kappa=0.70), then return toward zero by (\kappa=0.99). That already warns that any monotonic comparative static (\omega_Q(\kappa)) is not stable unless you have extra structure.

So:

* **I am confident** D1’s *qualitative* endpoint (“quiet region shrinks again by (\kappa\approx 1) in baseline numerics”) is numerically true in your reported calibration.
* **I am also confident** D1’s *theorem claim* (“(\lim_{\kappa\to 1}\omega_Q(\kappa)=0) under Standing Assumptions”) is **not proved** and probably **false without additional parametric restrictions**.

If you keep D1, you must either:

* (i) **turn it into a numerical result** (“In the baseline calibration and across the parameter sweep, (\omega_Q\to 0)”), or
* (ii) add the missing comparative statics proof (which I suspect is a **separate paper** level task given the endogeneity), or
* (iii) change the noise process (Route B from Round 1) so that a clean uninformative limit exists and can be handled analytically.

---

#### Layer 3: D2’s Proposition 5 still overclaims

Gemini’s D2 proof says:

* (\Delta^{\text{base}}(\kappa)) is “monotonically increasing” in (\kappa).
* (\Delta^{\text{act}}(\kappa)) is “monotonically decreasing” in (\kappa).

But in the model, both objects are **general equilibrium outcomes**:

[
\Delta^{\text{base}}(\kappa)=m_0 \cdot \mathbb P(\text{bid};\kappa),
]
where
[
\mathbb P(\text{bid};\kappa) = \sum_{x,d}\mathbb P(X=x,D=d;\kappa),p(x,d;\kappa),
]
and both the distribution (\mathbb P(X,D;\kappa)) and the conditional bid probabilities (p(x,d;\kappa)) depend on (\kappa) through:

* the noise distribution (p_0(\kappa),p_1(\kappa));
* the equilibrium cutoffs (k_1(\kappa),k_0(\kappa),k_D(\kappa));
* the implied mixture weights in Bayes’ rule.

There is no analytic monotonicity theorem in D2. It is **intuition + numerics**. That is fine, but then you must **say that** and not label it “monotonically” in the proof.

### 4) Verdict for P0

* **D1:** **PARTIALLY RESOLVED**
  It fixes the original incorrect “uninformative limit” claim, but it replaces it with an unproved equilibrium limit claim ((\omega_Q\to 0)) that is not derived and is plausibly false in some parameter regions.

* **D2:** **PARTIALLY RESOLVED**
  Decomposition is correct, but the monotonicity statements are not proved from primitives and should be demoted to numerical verification.

* **D7:** **RESOLVED in direction, but depends on D1/D2 being correctly hedged**
  The narrative is better (bounded support ⇒ no full uninformative limit), but it inherits the same overclaim if you keep “(\omega_Q\to 0)” as a theorem.

### 5) How to fix P0 properly (what I recommend)

I recommend you **stop trying to prove general equilibrium endpoint limits analytically** under bounded noise. Instead, do this:

1. **Rewrite Lemma 2 as a purely Bayesian/pricing endpoint lemma** (what is actually provable).
2. **Rewrite Proposition 5 as an analytic decomposition + numerical comparative statics theorem** (explicitly labeled numerical).

I give camera-ready LaTeX for both in Part 5.

---

## P1 — Lemma 1 / QA Domination

### 1) Original issue

Your Round‑1 audit flagged that the Lemma 1 proof was too hand‑wavy about ruling out (QA=(+1,0)) for the types that would ever buy. The existing proof in `draft_v3.tex` Appendix B.7 only shows that for **sufficiently high** (s), (U_P-U_{QA}>0), and then claims refinements kill (QA). It did **not** directly prove the lemma’s stated “for all relevant signals” conclusion.

### 2) Fix text (Gemini D5)

Gemini’s D5 computes:
[
U_P(s)-U_{QA}(s)=
2\delta \mathbb E_z\left[p(X,1)(\tilde m-m_0)+(1-p(X,1))\tilde\Delta\right]-C(s)
\equiv G - C(s),
]
then tries to show (G>C(k_0)) by comparing to
[
C(k_0)=\delta \mathbb E_z\left[p(X,0)(\tilde m-m_0)+(1-p(X,0))\tilde\Delta\right].
]
Then it concludes (U_P-U_{QA}>0) for all (s\ge k_0).

### 3) Mathematical evaluation (this is the D5 “gap”)

Claude’s objection is exactly right:

* The inner terms differ: (p(X,1)) vs (p(X,0)).
* Under net deterrence (A5), you typically have (p(\cdot,1)<p(\cdot,0)) because disclosure pins down engagement and raises the bid threshold.
* Therefore the step “(2\delta[\cdots] > \delta[\cdots])” does **not** follow from “multiply by 2” because you are not multiplying the same expectation.

This is not a pedantic issue; it can reverse the inequality in principle.

So D5, as written, is not watertight.

### 4) Verdict for P1

**INTRODUCES NEW PROBLEM.** D5’s attempted strengthening introduces an invalid comparison step, so the proof is not correct as a theorem.

### 5) How to fix P1

You have two viable routes:

* **Route 1 (no new assumptions; honest statement):** keep the original “for sufficiently high (s)” proof, but **rewrite the lemma statement** to match what is proved and explicitly tie the refinement to a parameter check (or to empirical institutional restriction “activists that file are engaged”). This is the most defensible without knife-edge assumptions.

* **Route 2 (minimal extra assumption to recover “for all (s\ge k_0)”):** add a **simple primitive inequality** that guarantees the two-share engagement gross benefit dominates the cost at the bottom of the voice region. Then you can prove (U_P-U_{QA}>0) for all (s\ge k_0) (or (s\ge k_D)).

I do both: (i) I confirm the gap is real, (ii) I show exactly what assumption would fix it, and (iii) I provide a fully watertight proof and camera-ready text in Part 2 + Part 5.

---

## P2 — Premium interpretation inconsistency

### 1) Original issue

In main text (line 231), you wrote: offer satisfies (b=P+m) (“premium above market price”). But your bidder offer rule is:
[
b(X,D,a)=\hat V(X,D)+m^R(a),
]
so premium is above (\hat V), not above (P). This inconsistency triggers referee distrust.

### 2) Fix text (Gemini D3)

D3 changes the sentence to interpret (m_0,m_1) as premia above expected standalone fundamental value (\hat V).

### 3) Mathematical evaluation

This fix is purely definitional consistency. It matches:

* your definition (b(X,D,a)=\hat V(X,D)+m^R(a)) (line 268 in `draft_v3.tex`),
* your notation table (line 847 already says premia above (\hat V)).

### 4) Verdict

**RESOLVED.** (Only tweak: update line-range references; content is correct.)

---

## P3 — (\lambda_B\le 1/2) restriction hidden inside Proposition 1 proof

### 1) Original issue

In Proposition 1 proof (line 973), you used a bound (p(X,1)\le\lambda_B<0.5) to ensure (U_P-U_Q) is increasing in (s) (single-crossing) and hence there is a unique (k_D). But you did not state (\lambda_B<0.5) as an assumption.

### 2) Fix text (Gemini D4)

D4:

* Adds Assumption (A7): (\lambda_B\le 1/2),
* Updates the assumption table,
* Updates the proof to reference A7.

### 3) Mathematical evaluation (full algebra)

You define (in proof) the difference:
[
U_P(s)-U_Q(s) = A + \beta s (B_P-B_Q),
]
with
[
B_P-B_Q=\delta \beta \mathbb E_z\left[1-2p(X,1)+p(X,0)\right].
]

To show (B_P-B_Q>0), it is sufficient that the integrand be strictly positive:
[
1-2p(X,1)+p(X,0)>0.
]

Since (p(X,0)\ge 0), a sufficient condition is:
[
1-2p(X,1)>0 \quad\Longleftrightarrow\quad p(X,1)<\frac{1}{2}.
]

But (p(X,1)\le \lambda_B) because (p(X,D)=\lambda_B\tilde p(X,D)) and (\tilde p\in[0,1]). Therefore if (\lambda_B\le 1/2), then for all ((X,1)):
[
p(X,1)\le \lambda_B \le \frac{1}{2}
\quad\Rightarrow\quad
1-2p(X,1)\ge 0.
]

If you want strict positivity, you either take (\lambda_B<1/2) or add that (\tilde p) is not identically 1 at (D=1). In any realistic takeover calibration, (p(X,1)\ll 1/2), so strict inequality holds.

Thus D4 repairs the logical hole: the “single crossing” step is now properly assumed.

### 4) Verdict

**RESOLVED** (with the caveat that you should be explicit if you need strict “(<)” rather than “(\le)”).

---

## P4 — Minor rigor leaks (Bayes objects, decomposition “by definition”)

### 1) Original issue

Two leaks:

1. You reference (\mathbb P(D=1\mid X)) in pricing, but you do not give the explicit Bayes formula anywhere, even though it is a simple rational expression in (\omega) and (p_z). This matters because the paper’s “pre‑trade anonymity” is entirely inside that mixing probability.

2. Appendix B.11 starts “By definition (\Delta^{\min}(\kappa)=\mathbb E[\bar m(X,D)\mathbf 1{\text{bid}}]).” That is *not* the definition; the definition is (\mathbb E[m^R(a)\mathbf 1{\text{bid}}]). The step is salvageable via iterated expectations, but not “by definition.”

### 2) Fix text (Gemini D6)

* D6a provides:
  [
  \mathbb P(D=1\mid X)=\frac{\omega_P p_{X-1}}{\omega_Ep_{X+1}+(\omega_H+\omega_Q)p_X+\omega_Pp_{X-1}}.
  ]
* D6b rewrites the decomposition proof via conditioning.

### 3) Mathematical evaluation

#### D6a Bayes formula derivation (full)

Let (p_z(j)\equiv\mathbb P(z=j)) for (j\in{-1,0,1}).

Given an action (q\in{-1,0,1}), we have (X=q+z). Therefore:

* If (q=+1), then (z=X-1), so
  [
  \mathbb P(X\mid q=+1)=p_z(X-1).
  ]
* If (q=0), then (z=X), so
  [
  \mathbb P(X\mid q=0)=p_z(X).
  ]
* If (q=-1), then (z=X+1), so
  [
  \mathbb P(X\mid q=-1)=p_z(X+1).
  ]

Now (D=1) iff (q=+1). So by Bayes:
[
\mathbb P(D=1\mid X)
=\mathbb P(q=+1\mid X)
=\frac{\mathbb P(q=+1)\mathbb P(X\mid q=+1)}{\sum_{q'\in{-1,0,1}}\mathbb P(q')\mathbb P(X\mid q')}.
]

Substitute (\mathbb P(q=+1)=\omega_P), (\mathbb P(q=0)=\omega_H+\omega_Q), (\mathbb P(q=-1)=\omega_E). Then
[
\mathbb P(D=1\mid X)
=\frac{\omega_P,p_z(X-1)}{\omega_E,p_z(X+1)+(\omega_H+\omega_Q),p_z(X)+\omega_P,p_z(X-1)}.
]

That matches D6a, with the understanding that (p_z(k)=0) if (k\notin{-1,0,1}).

**Important correction to Gemini’s narrative:** for (X=-1), the numerator uses (p_z(-2)=0), so (\mathbb P(D=1\mid X=-1)=0). Thus (X=-1) is *not* a mixing state. The mixing states are (X\in{0,1}) (and trivially (X=2\Rightarrow D=1), (X\in{-2,-1}\Rightarrow D=0)).

So D6a is mathematically correct; just fix the sentence.

#### D6b decomposition proof

The correct definition is:
[
\Delta^{\min}(\kappa)=\mathbb E\left[m^R(a)\cdot \mathbf 1{\text{bid}}\right].
]

Condition on ((X,D)). Because the bidder’s bid decision is a function of ((X,D)) and the independent shock (\xi), the indicator (\mathbf 1{\text{bid}}) is independent of the realized (a) conditional on ((X,D)). Therefore:
[
\mathbb E[m^R(a)\mathbf 1{\text{bid}}\mid X,D]
==============================================

\mathbb E[m^R(a)\mid X,D]\cdot \mathbb E[\mathbf 1{\text{bid}}\mid X,D].
]

Now:

* (\mathbb E[m^R(a)\mid X,D]=m_0+(\tilde m-m_0)\pi(X,D)=\bar m(X,D)).
* (\mathbb E[\mathbf 1{\text{bid}}\mid X,D]=p(X,D)).

So:
[
\mathbb E[m^R(a)\mathbf 1{\text{bid}}\mid X,D]
=\bar m(X,D),p(X,D).
]

Take unconditional expectation:
[
\Delta^{\min}(\kappa)
=\mathbb E[\bar m(X,D)p(X,D)].
]

Equivalently, since (\bar m) is measurable w.r.t. ((X,D)),
[
\Delta^{\min}(\kappa)
=\mathbb E\left[\bar m(X,D)\mathbf 1{\text{bid}}\right],
]
but **this is a derived equality**, not a definition. So D6b’s approach is right.

### 4) Verdict

**RESOLVED (with a minor correction)**: D6a’s formula is correct but its “mixing at (X=-1)” sentence should be corrected.

---

# Part 2 — The D5 Gap (Lemma 1 / QA Domination)

You asked four sub-questions: (a) is the gap real, (b) fixable under current assumptions, (c) minimal new assumption if not, (d) provide watertight proof + evaluate old proof.

I answer in that order.

---

## (a) Is Claude’s D5 gap real?

**Yes. I am confident it is real.**

### Where Gemini’s proof breaks

Gemini defines:

[
U_P(s)-U_{QA}(s)=
2\delta,\mathbb E_z!\left[p(X,1)(\tilde m-m_0)+(1-p(X,1))\tilde\Delta\right]-C(s).
]

Then it defines (G) as that gross benefit term:
[
G \equiv 2\delta,\mathbb E_z!\left[p(X,1)(\tilde m-m_0)+(1-p(X,1))\tilde\Delta\right].
]

Then it tries to compare (G) to (C(k_0)) using:

[
C(k_0)=\delta,\mathbb E_z!\left[p(X,0)(\tilde m-m_0)+(1-p(X,0))\tilde\Delta\right].
]

The implicit step is “(G> C(k_0))” because “2 times something > 1 times something.”

But these are **not the same “something.”** Specifically:

* In (G), the expectation is over **(X=1+z)** (because (q=+1) under Public Voice / QA).
* In (C(k_0)), the expectation is over **(X=z)** (because (q=0) under Hold/Quiet Voice at the (k_0) boundary).
* Moreover, the conditional bid probability uses different disclosure regimes: (p(\cdot,1)) vs (p(\cdot,0)).
* Under net deterrence (A5), disclosure and higher inferred engagement weakly **reduce** (p): for comparable (X), (p(X,1)\le p(X,0)).

Thus the inequality (G>C(k_0)) is not implied.

So Claude’s critique is correct.

---

## (b) Is it fixable under the current assumptions?

**You can fix the lemma, but not with Gemini’s “compare to (k_0) indifference” argument unless you add an extra restriction.**

Under the *current* assumptions (A1–A6 + proposed A7), you can prove:

* There exists a threshold (\bar s) such that for all (s\ge \bar s), (U_P(s)>U_{QA}(s)), **uniformly over beliefs** (\pi(X,1)\in[0,1]).

This is exactly what your *original* proof in `draft_v3.tex` does. It is mathematically correct.

What you **cannot** prove from current assumptions alone is the stronger statement:

* For every (s) that would ever rationally choose to buy (i.e., every “relevant” (s)), (U_P(s)>U_{QA}(s)).

To bridge that, you need either:

* a condition ensuring the public-voice cutoff (k_D) is above (\bar s) (a parameter restriction checked numerically), or
* a primitive inequality guaranteeing that the gross two-share benefit dominates the cost already at the bottom of the engaging region.

---

## (c) Minimal additional assumption needed (if you insist on “for all (s\ge k_0)”)

A clean sufficient condition is:

### **Assumption (A8) (Two-share engagement dominates at the voice threshold).**

[
C(k_0);<;2\delta\min{\tilde m-m_0,\ \tilde\Delta}.
\tag{A8}
]

This is “minimal” in the sense that it directly targets the point you need: if cost at the bottom of engagement region is below the **worst-case** (belief-free) lower bound on the gross benefit, then Public Voice dominates Quiet Accumulation for all types that are ever in the voice region.

If you dislike assumptions involving equilibrium objects ((k_0)), you can replace (A8) by a stronger **primitive** sufficient condition:

[
\max{\tilde m-m_0,\tilde\Delta};<;2\min{\tilde m-m_0,\tilde\Delta}.
\tag{A8'}
]

Because at (k_0), (C(k_0)=\delta\mathbb E_z[\text{convex combination of }(\tilde m-m_0)\text{ and }\tilde\Delta]\le \delta\max{\tilde m-m_0,\tilde\Delta}), so if (\delta\max <2\delta\min), then (C(k_0)<2\delta\min) automatically.

That said, (A8′) is a bit “parameter‑ratio” looking; (A8) can be defended as “we focus on equilibria where filing is undertaken only when cost is low enough.”

---

## (d) Provide a complete, watertight proof of Lemma 1

I give two versions:

* **Version 1 (no new assumption; honest lemma statement)** — corresponds to your existing approach but rewritten to be fully internally consistent and not overclaim.
* **Version 2 (adds A8; delivers the stronger domination claim)** — if you want the lemma to say “for all (s\ge k_0)” without any refinement hand-waving.

### Version 1 (no new assumptions): “domination for sufficiently high signals”

**Lemma 1 (Domination of passive accumulation for sufficiently high signals).**
Fix any belief system (\pi(X,1)\in[0,1]) after (D=1). Define (P\equiv(+1,1)) and (QA\equiv(+1,0)). Then there exists a finite threshold (\bar s) such that for all (s\ge \bar s),
[
U_P(s)>U_{QA}(s).
]

**Proof (full algebra).**

**Step 1: write payoffs under (P) and (QA).**

Under both (P) and (QA), the blockholder chooses (q=+1), hence holds (h=2) shares at (t=2), and the order flow is:
[
X = q+z = 1+z,\qquad z\in{-1,0,1}.
]

Because the trade executes at (t=1) *before* (D) is revealed, and because both strategies have the same (q), the cash flow from the trade is identical:
[
\text{trading cash flow}=-P_{\text{trade}}(X).
]

The only difference is the engagement decision (a\in{0,1}), which affects:

* standalone payoff via (a\tilde\Delta),
* realized premium via (m^R(a)=m_0+a(\tilde m-m_0)).

Thus, conditional on a realized ((X,D=1)), the discounted expected terminal payoff under (P) is:
[
\delta\cdot 2\Big(p(X,1)\big(\hat V(X,1)+\tilde m\big)+(1-p(X,1))(\hat v(s)+\tilde\Delta)\Big),
]
and under (QA) it is:
[
\delta\cdot 2\Big(p(X,1)\big(\hat V(X,1)+m_0\big)+(1-p(X,1))\hat v(s)\Big).
]

Therefore (integrating over (z)):

[
U_P(s)
======

\mathbb E_z!\left[
-P_{\text{trade}}(1+z)
+
2\delta\Big(p(1+z,1)(\hat V(1+z,1)+\tilde m)+(1-p(1+z,1))(\hat v(s)+\tilde\Delta)\Big)
\right]
-C(s),
]
[
U_{QA}(s)
=========

\mathbb E_z!\left[
-P_{\text{trade}}(1+z)
+
2\delta\Big(p(1+z,1)(\hat V(1+z,1)+m_0)+(1-p(1+z,1))\hat v(s)\Big)
\right].
]

**Step 2: subtract (U_{QA}) from (U_P) and cancel common terms.**

The execution price term (-P_{\text{trade}}(1+z)) cancels because it is identical inside the expectation. The (\hat V(1+z,1)) term also cancels inside the bid component because it is multiplied by the same (p(1+z,1)). The (\hat v(s)) term cancels partially.

Compute the difference inside the expectation:

Bid part difference:
[
2\delta\cdot p(1+z,1)\Big[(\hat V+\tilde m)-(\hat V+m_0)\Big]
=============================================================

2\delta\cdot p(1+z,1)(\tilde m-m_0).
]

No-bid part difference:
[
2\delta\cdot (1-p(1+z,1))\Big[(\hat v(s)+\tilde\Delta)-\hat v(s)\Big]
=====================================================================

2\delta\cdot(1-p(1+z,1))\tilde\Delta.
]

So:
[
U_P(s)-U_{QA}(s)
================

2\delta,\mathbb E_z!\left[
p(1+z,1)(\tilde m-m_0)+(1-p(1+z,1))\tilde\Delta
\right]
-C(s).
]

Define (\alpha\equiv \tilde m-m_0>0) and (\beta\equiv\tilde\Delta>0). Then:

[
U_P(s)-U_{QA}(s)
================

2\delta,\mathbb E_z!\left[
p(1+z,1)\alpha+(1-p(1+z,1))\beta
\right]
-C(s).
\tag{1}
]

**Step 3: lower-bound the gross benefit uniformly over (p\in[0,1]).**

For any fixed (p\in[0,1]),
[
p\alpha+(1-p)\beta
==================

\beta+p(\alpha-\beta).
]

Now note that (\min{\alpha,\beta}\le \alpha) and (\min{\alpha,\beta}\le \beta). Therefore:
[
p\alpha+(1-p)\beta
==================

p\alpha+(1-p)\beta
\ge p\min{\alpha,\beta}+(1-p)\min{\alpha,\beta}
=\min{\alpha,\beta}.
]

This inequality holds **pointwise** for each realization of (z). Therefore:
[
\mathbb E_z!\left[
p(1+z,1)\alpha+(1-p(1+z,1))\beta
\right]
\ge
\min{\alpha,\beta}.
]

Plug into (1):
[
U_P(s)-U_{QA}(s)
\ge
2\delta\min{\alpha,\beta}-C(s).
\tag{2}
]

Crucially, this bound does **not** depend on the off-path belief (\pi(X,1)), because it did not use any property of (p) besides (p\in[0,1]).

**Step 4: use the cost tail condition.**

Assumption (A2) gives:

* (C(s)) strictly decreasing,
* (\lim_{s\to\infty} C(s)=0).

Let
[
\underline G \equiv 2\delta\min{\alpha,\beta}>0.
]

Since (C(s)\to 0), there exists (\bar s\in\mathbb R) such that for all (s\ge \bar s),
[
C(s)<\underline G.
]

Then for (s\ge \bar s), (2) implies:
[
U_P(s)-U_{QA}(s)
\ge
\underline G-C(s)

>

0.

]

So (U_P(s)>U_{QA}(s)) for all (s\ge\bar s).

That proves the lemma. (\blacksquare)

**What this DOES and DOES NOT prove:** it proves strict domination only for high signals (s\ge\bar s). It does **not** prove “for all (s\ge k_0)” unless you relate (k_0) to (\bar s) (numerically or via an extra assumption).

### Version 2 (with A8): “domination for all (s\ge k_0)” (what Gemini tried to do)

If you add (A8) (C(k_0)<2\delta\min{\alpha,\beta}), then:

Because (C(s)) is decreasing,
[
s\ge k_0\quad\Rightarrow\quad C(s)\le C(k_0).
]

Then from (2),
[
U_P(s)-U_{QA}(s)
\ge 2\delta\min{\alpha,\beta}-C(s)
\ge 2\delta\min{\alpha,\beta}-C(k_0)

> 0,
> ]
> for all (s\ge k_0).

That fully closes the logic without comparing (p(X,1)) to (p(X,0)). It uses only:

* the belief-free lower bound (\min{\alpha,\beta}),
* monotonicity of (C),
* the single inequality (A8).

---

## Evaluate “old proof” (draft_v3.tex lines 906–922) vs Gemini’s approach

* Your **existing proof** (lines 906–922) is **mathematically correct** as far as it goes, because it proves the **existence** of a high-s region where (P) dominates (QA) uniformly over beliefs. Its weakness is **only** that the lemma statement in the main text overclaims (“for all relevant signals”) and that the invocation of D1 is not fully formal.

* Gemini’s attempted strengthening is directionally right (you’d *like* “(P) dominates (QA) throughout the relevant region”), but the actual step they used is wrong.

My recommendation: **keep the structure of your existing proof, rewrite the lemma statement to match what is proved, and—if you need the strong claim—add a single extra assumption like (A8).**

That is the smallest repair.

---

# Part 3 — D2 Monotonicity Claims (Proposition 5)

You asked (a) can monotonicities be proved analytically, (b) is analytic+numeric defensible, (c) does the proposition overclaim.

I answer in that order.

---

## (a) Can (\Delta^{\text{base}}(\kappa)) increasing and (\Delta^{\text{act}}(\kappa)) decreasing be proved analytically from primitives?

**In full general equilibrium: almost certainly not, absent additional structure.**

Here is why, precisely.

### Step 1: write the objects explicitly

Your decomposition (once fixed correctly) is:

[
\Delta^{\min}(\kappa)
= m_0,\mathbb P(\text{bid};\kappa)
+(\tilde m-m_0),\mathbb E!\left[\pi(X,D;\kappa)\mathbf 1{\text{bid}}\right].
]

Define:

[
\Delta^{\text{base}}(\kappa)\equiv m_0,\mathbb P(\text{bid};\kappa),
]
[
\Delta^{\text{act}}(\kappa)\equiv (\tilde m-m_0),\mathbb E!\left[\pi(X,D;\kappa)\mathbf 1{\text{bid}}\right].
]

Now expand (\mathbb P(\text{bid};\kappa)) as a finite sum over discrete states:

[
\mathbb P(\text{bid};\kappa)=\sum_{x\in{-2,-1,0,1,2}}\sum_{d\in{0,1}}
\mathbb P(X=x,D=d;\kappa),p(x,d;\kappa).
]

Similarly,
[
\mathbb E[\pi(X,D)\mathbf 1{\text{bid}}]
=\sum_{x,d}
\pi(x,d;\kappa),\mathbb P(X=x,D=d;\kappa),p(x,d;\kappa).
]

### Step 2: note the sources of (\kappa)-dependence

Even if the strategy cutoffs were held fixed, each term still depends on (\kappa) through:

* the likelihoods (\mathbb P(X=x\mid q)) (via (p_0(\kappa),p_1(\kappa))),
* Bayes’ posteriors (\pi(x,d;\kappa)),
* conditional means (\mathbb E[v\mid X=x,D=d]) (also Bayes),
* hence the bid threshold (T(x,d;\kappa)),
* hence the bid probability (p(x,d;\kappa)).

In **general equilibrium**, you additionally have endogenous cutoffs ((k_1(\kappa),k_0(\kappa),k_D(\kappa))) affecting:

* the weights (\omega(\kappa)),
* and therefore everything above.

Without (i) a monotone comparative static theorem for the fixed point of the cutoff mapping in (\kappa), and (ii) a monotone likelihood ratio ordering that survives the endogenous mixing, you cannot sign the derivative of (\Delta^{\text{base}}) or (\Delta^{\text{act}}) in general.

### What you *can* prove analytically (and you already have)

You *can* prove monotonicity of certain posterior components holding ((\omega_E,\omega_H,\omega_Q)) fixed. This is exactly your Appendix B.4. Let me redo it fully (this is useful because it is the only analytic monotonicity you truly have, and you should leverage it honestly):

Fix ((\omega_E,\omega_H,\omega_Q)) and define (A\equiv\omega_Q), (B\equiv\omega_H+\omega_Q), (C\equiv\omega_E).

Recall:
[
\pi(-1,0)=\frac{A p_1}{B p_1 + C p_0},
\quad
p_1=\frac{\kappa}{3},
\quad
p_0=1-\frac{2}{3}\kappa.
]

Substitute:
[
\pi(-1,0)=\frac{A(\kappa/3)}{B(\kappa/3)+C(1-\frac{2}{3}\kappa)}.
]

Multiply numerator and denominator by 3:
[
\pi(-1,0)=\frac{A\kappa}{B\kappa + 3C -2C\kappa}
=\frac{A\kappa}{3C+\kappa(B-2C)}.
]

Differentiate w.r.t. (\kappa). Let (D(\kappa)\equiv 3C+\kappa(B-2C)). Then
[
\pi(-1,0)=\frac{A\kappa}{D(\kappa)}.
]

Use quotient rule:
[
\frac{d}{d\kappa}\pi(-1,0)
==========================

\frac{A\cdot D(\kappa)-A\kappa\cdot D'(\kappa)}{D(\kappa)^2}.
]

Compute (D'(\kappa)=B-2C). So:
[
\frac{d}{d\kappa}\pi(-1,0)
==========================

# \frac{A\big(3C+\kappa(B-2C)\big)-A\kappa(B-2C)}{D(\kappa)^2}

\frac{A\cdot 3C}{D(\kappa)^2}.
]

Since (A\ge 0), (C\ge 0), and (D(\kappa)^2>0) whenever denominators are nonzero, we have
[
\frac{d}{d\kappa}\pi(-1,0)\ge 0,
]
with strict inequality if (A>0) and (C>0).

Similarly:
[
\pi(0,0)=\frac{A p_0}{B p_0 + C p_1}
=\frac{A(1-\frac{2}{3}\kappa)}{B(1-\frac{2}{3}\kappa)+C(\kappa/3)}.
]

Write (p_0=(3-2\kappa)/3), (p_1=\kappa/3). Multiply numerator/denominator by 3:
[
\pi(0,0)=\frac{A(3-2\kappa)}{B(3-2\kappa)+C\kappa}.
]

Define (N(\kappa)=A(3-2\kappa)), (E(\kappa)=B(3-2\kappa)+C\kappa=3B+\kappa(C-2B)).

Then:
[
\frac{d}{d\kappa}\pi(0,0)
=========================

\frac{N'(\kappa)E(\kappa)-N(\kappa)E'(\kappa)}{E(\kappa)^2}.
]

Compute:
[
N'(\kappa)=-2A,
\quad
E'(\kappa)=C-2B.
]

So numerator:
[
-2A\cdot E(\kappa)-A(3-2\kappa)(C-2B)
=====================================

-A\Big(2E(\kappa)+(3-2\kappa)(C-2B)\Big).
]

Now expand:
[
2E(\kappa)=2(3B+\kappa(C-2B))=6B+2\kappa(C-2B).
]
[
(3-2\kappa)(C-2B)=3(C-2B)-2\kappa(C-2B).
]

Add them:
[
2E(\kappa)+(3-2\kappa)(C-2B)
============================

# 6B+2\kappa(C-2B)+3(C-2B)-2\kappa(C-2B)

# 6B+3(C-2B)

# 6B+3C-6B

3C.
]

So numerator is:
[
-A\cdot 3C.
]

Thus:
[
\frac{d}{d\kappa}\pi(0,0)
=========================

\frac{-3AC}{E(\kappa)^2}\le 0,
]
strict if (A,C>0).

This is the kind of analytic monotonicity you can credibly claim.

But that is **not** the same as monotonicity of (\Delta^{\text{act}}(\kappa)) in equilibrium.

So the correct answer to (a) is:

* **Analytically provable:** certain posterior components (\pi(x,0)) are monotone in (\kappa) holding strategy fixed (you already prove this).
* **Not analytically provable from primitives (without major extra structure):** the general equilibrium monotonicity of (\Delta^{\text{base}}(\kappa)) and (\Delta^{\text{act}}(\kappa)).

---

## (b) Is “analytic decomposition + numerical verification” defensible in a top finance journal?

**Yes, if you are explicit about what is proved and what is computed.** You cannot write “monotonically increasing” as if proved when it is not.

Two points of methodological standard:

1. **Finance theory papers routinely use equilibrium refinements (e.g., Intuitive Criterion) and numerical fixed point computations** when closed forms are impossible. For example, in Edmans–Goldstein–Jiang they explicitly define equilibrium as PBE + Cho–Kreps intuitive criterion, and state off‑path belief restrictions for extreme order flows. 
   That is a direct precedent for your own off‑path belief language.

2. For comparative statics that depend on endogenous mixtures, it is standard to provide:

   * a decomposition and intuition,
   * then numerically verify monotonicity and hump shape across robust parameter grids.

But you must phrase it as “Result (Numerical)” or “Proposition (Numerical comparative statics)” and include robustness.

---

## (c) Is Proposition 5 appropriately hedged in Gemini D2?

**No. It overclaims.**

D2 says the monotonicities are established, but it does not provide a proof. It should be rewritten as:

* “We prove the decomposition.”
* “We prove within-regime posterior monotonicities (Appendix B.4).”
* “We numerically verify that, in equilibrium, (\Delta^{\text{base}}) rises and (\Delta^{\text{act}}) falls, producing a unique interior maximizer.”

I give camera-ready text for this rewrite in Part 5.

---

# Part 4 — Overall Theory Robustness (assuming fixes implemented)

You asked four items.

---

## 4.1 Is the corrected theory rigorous enough for JF/JFE/RFS?

**If you implement the repairs I’m giving (D5 fix + D1/D2 hedging), it becomes “referee‑proofable” on the main mathematical failure points.**

What a hostile referee will still target:

1. **Claims labeled as theorems that are actually numerical.**
   If you keep any of these as “Lemma/Proposition” without clearly stating the numerical component, you invite a desk reject.

2. **Use of equilibrium refinements without formally specifying them.**
   You mention “D1” in the lemma proof. If you keep that, you need a one-paragraph formal definition (or switch to “Cho–Kreps intuitive criterion”) and explicitly state what it rules out in your setting. You have precedent in the literature using intuitive criterion language.

3. **Existence/uniqueness.**
   Your existence proof uses Brouwer and a compact rectangle argument (Appendix B.12). That is okay if:

   * you explicitly prove the cutoff mapping is continuous,
   * you justify the bounding box choice without hand-waving.
     Uniqueness is explicitly numerical (A6). That is acceptable but must be framed carefully.

4. **Knife-edge disclosure rule.**
   (D=1) iff (q=+1) is a stylized shortcut for “stake increase crosses filing threshold.” A referee may tolerate it as simplification, but you need to be explicit about what is abstracted.

5. **Bounded noise support.**
   With (z\in{-1,0,1}), the “uninformative limit” intuition does not literally hold. You already discovered this. A referee will nail you if any remaining text speaks as if “fully uninformative” is achieved. Make sure you never say “(\pi\to) unconditional” except where it is algebraically true for specific states.

---

## 4.2 Remaining logical gaps / unstated assumptions / knife edges

The big ones after you fix the six issues:

* **The “full support” sentence is false at (\kappa=0).**
  At `draft_v3.tex` line 321 you say “noise has full support on ({-1,0,1}), hence every (X\in{-2,-1,0,1,2}) occurs with positive probability.” But your distribution is (P(z=\pm1)=\kappa/3). If (\kappa=0), support collapses and (X=\pm2) never happens.
  Fix: state “for any (\kappa>0)” or treat (\kappa=0) as a limit case.

* **Lemma 1 statement vs proof mismatch** (the D5 problem).
  This is the most dangerous because it directly affects identification of the disclosed branch.

* **Any “monotonicity” claim about equilibrium objects** must be clearly numerical unless you actually prove it.

---

## 4.3 Is Assumption (A7) (\lambda_B \le 1/2) economically defensible?

Economically, (\lambda_B) is the probability a bidder arrives in the relevant short window between the blockholder’s action and takeover resolution. Interpreted as an annualized hazard, (\lambda_B\le 1/2) is extremely mild (most firm-year bid rates are far lower).

So:

* **Mathematically:** A7 is clean and does what you need (single crossing).
* **Economically:** a referee might call it “ad hoc” if you do not explain that realistic takeover arrival hazards are far below 50%.

Fix: add one sentence in the assumption table explanation: “We require (\lambda_B\le 1/2), which is trivially satisfied in U.S. M&A data (annual bid incidences are single-digit percentages).”

---

## 4.4 Is “analytic + numerical verification” hybrid standard practice?

Yes, provided you do it transparently:

* State the equilibrium concept and refinement (e.g., PBE + Cho–Kreps intuitive criterion is explicitly used in published work).
* Provide analytic decomposition and partial monotonicities where possible.
* Label computed results as numerical and show robustness.

---

# Part 5 — Camera‑Ready LaTeX Fixes for Remaining Problems

You requested: exact replacement text, boundary markers, what it replaces, and verification.

I provide **four** patches:

1. **Fix Lemma 1 statement + proof (D5 gap).**
2. **Fix Lemma 2 + Proposition 5 to avoid unproved endpoint and monotonicity claims (D1/D2 overclaim).**
3. **Apply D3 (premium interpretation).**
4. **Apply D4 (A7) + correct its minor LaTeX bookkeeping.**
5. **Apply D6 (Bayes (\mathbb P(D=1\mid X)) + decomposition proof) with one narrative correction.**

I will be explicit about line ranges in **your current `/mnt/data/draft_v3.tex`**.

---

## Patch 1 — Lemma 1 (QA domination): fix statement and proof

### What it replaces

**(A) Lemma statement in main text**: lines **333–336** in `draft_v3.tex`:

```tex
\begin{lemma}[Domination of Passive Accumulation]
\label{lem:qa-domination}
Because the fundamental value improvement $\tilde{\Delta}$ is realized on $h=2$ shares, the expected marginal return to active engagement strictly exceeds the private cost $C(s)$ for any signal $s$ high enough to justify the capital cost of acquiring the second share. Therefore, $U(+1,1 \mid s) > U(+1,0 \mid s)$ for all relevant signals. In equilibrium, threshold-crossing ($D=1$) perfectly reveals engagement ($a=1$).
\end{lemma}
```

**(B) Appendix proof**: lines **905–922** (Appendix `app:proof-qa-domination` currently begins line 904). The current proof includes the “sufficiently high” argument plus an informal D1 invocation.

### Replacement text (Version 1: no new assumption; honest statement)

If you do **not** want to add a new assumption, you must weaken the lemma statement to what is proved.

**BEGIN REPLACEMENT (lines 333–336):**

```tex
%==================== BEGIN REPLACEMENT: Lemma 1 statement ====================
\begin{lemma}[Domination of Passive Accumulation for High Signals]
\label{lem:qa-domination}
Fix an arbitrary market belief system $\pi(X,1)\in[0,1]$ following a regulatory filing $D=1$. 
There exists a finite threshold $\bar{s}\in\mathbb R$ such that, for all $s\ge \bar{s}$, 
Public Voice strictly dominates Quiet Accumulation:
\[
U(+1,1\mid s)\;>\;U(+1,0\mid s).
\]
In the baseline calibration and in the parameter sweeps reported in Section~\ref{sec:numerics}, the Public Voice cutoff satisfies $k_D\ge \bar{s}$, so that Quiet Accumulation is never played on the disclosed branch and $D=1$ reveals active engagement ($a=1$).
\end{lemma}
%==================== END REPLACEMENT: Lemma 1 statement ======================
```

**Why this is watertight:** it precisely matches what the proof can show (existence of (\bar s)), and then *separately* states the calibration check needed to conclude “(D=1\Rightarrow a=1)” on-path.

Now replace the appendix proof with a fully explicit version (no “sketch”).

**BEGIN REPLACEMENT (replace the entire proof environment at lines 905–922):**

```tex
%==================== BEGIN REPLACEMENT: Proof of Lemma 1 =====================
\begin{proof}
Let $QA\equiv(+1,0)$ denote Quiet Accumulation and let $P\equiv(+1,1)$ denote Public Voice.
Fix an arbitrary belief system $\pi(X,1)\in[0,1]$ upon observing $D=1$ and consider any signal realization $s$.

Because $q=+1$ under both $QA$ and $P$, the aggregate order flow is $X=1+z$ and the anonymous execution price $P_{\textup{trade}}(X)$ applies identically under both actions. Moreover, conditional on $(X,1)$, the bid probability $p(X,1)$ and the post-disclosure price $P_{\textup{post}}(X,1)$ are identical under $QA$ and $P$ because $a$ is not observed at the trading stage. Thus the only difference between $QA$ and $P$ is the realized engagement decision $a\in\{0,1\}$, which changes (i) the realized premium from $m_0$ to $\tilde m$ when a bid occurs and (ii) the standalone payoff from $v$ to $v+\tilde\Delta$ when no bid occurs, at private cost $C(s)$.

Write $\alpha\equiv\tilde m-m_0>0$ and $\beta\equiv\tilde\Delta>0$.
Using the payoff function~\eqref{eq:blockholder-payoff} and the fact that $h=2$ shares are held under both $QA$ and $P$, we have:
\begin{align*}
U_P(s)
&=\E_z\!\Big[-P_{\textup{trade}}(1+z) 
+2\delta\big(p(1+z,1)\,(\hat V(1+z,1)+\tilde m) +(1-p(1+z,1))(\hat v(s)+\tilde\Delta)\big)\Big]-C(s),\\
U_{QA}(s)
&=\E_z\!\Big[-P_{\textup{trade}}(1+z) 
+2\delta\big(p(1+z,1)\,(\hat V(1+z,1)+m_0) +(1-p(1+z,1))\hat v(s)\big)\Big].
\end{align*}
Subtracting and cancelling the common execution-price term and the common $\hat V(1+z,1)$ term yields:
\begin{align*}
U_P(s)-U_{QA}(s)
&=2\delta\,\E_z\!\Big[p(1+z,1)(\tilde m-m_0) +(1-p(1+z,1))\tilde\Delta\Big]-C(s)\\
&=2\delta\,\E_z\!\Big[p(1+z,1)\alpha +(1-p(1+z,1))\beta\Big]-C(s).
\end{align*}

For any $p\in[0,1]$, the expression $p\alpha+(1-p)\beta$ is a convex combination of $\alpha$ and $\beta$, hence satisfies
\[
p\alpha+(1-p)\beta\;\ge\;\min\{\alpha,\beta\}.
\]
Applying this pointwise inequality inside the expectation gives
\[
\E_z\!\Big[p(1+z,1)\alpha +(1-p(1+z,1))\beta\Big]\;\ge\;\min\{\alpha,\beta\}.
\]
Therefore,
\[
U_P(s)-U_{QA}(s)\;\ge\;2\delta\min\{\alpha,\beta\}-C(s).
\]

By Assumption~\textup{(A2)}, $C(s)$ is strictly decreasing and $\lim_{s\to\infty}C(s)=0$.
Define the positive constant $\underline G\equiv 2\delta\min\{\alpha,\beta\}>0$.
Since $C(s)\to 0$, there exists a finite $\bar s$ such that $C(s)<\underline G$ for all $s\ge \bar s$.
For such $s$,
\[
U_P(s)-U_{QA}(s)\;\ge\;\underline G-C(s)\;>\;0,
\]
so $U_P(s)>U_{QA}(s)$ for all $s\ge\bar s$.
\end{proof}
%==================== END REPLACEMENT: Proof of Lemma 1 =======================
```

**Verification checklist (no gaps):**

* I explicitly wrote both utilities using your own payoff structure.
* I cancelled only identical terms.
* I used only the inequality “convex combination ≥ min”.
* I used only Assumption A2 to produce (\bar s).
* No comparison between (p(X,1)) and (p(X,0)) occurs, so Claude’s gap is avoided.

### Optional strengthening (Version 2) if you want “for all (s\ge k_0)”

Add Assumption (A8) and change the lemma statement accordingly. If you want this, say so and I will provide the exact assumption-table insertion. For now, Version 1 is the cleanest “no new assumptions” patch.

---

## Patch 2 — Lemma 2 + Proposition 5: remove unproved (\omega_Q\to 0) and monotonicity overclaims

### What it replaces

Main text:

* Lemma 2 lines **552–555**
* Proposition 5 lines **558–564**
* The narrative paragraph lines **566–568** (Weierstrass + endpoint collapse story)

Appendix:

* Lemma 2 proof lines **1258–1270**
* Prop 5 proof lines **1272–1297**

These are currently the “broken” parts.

### Replacement approach

* Lemma 2 should state only what is provable from the bounded-noise Bayes structure: what happens to (\mathbb P(D=1\mid X)) and (\pi(X,0)) as (\kappa\to 0) and (\kappa\to 1) **holding strategy fixed**.
* Proposition 5 should:

  1. prove the decomposition analytically,
  2. label the hump and component monotonicities as numerical comparative statics, not analytic.

### Replacement text (main text Lemma 2 + Proposition 5 + narrative)

**BEGIN REPLACEMENT (replace lines 552–568 inclusive):**

```tex
%==================== BEGIN REPLACEMENT: Lemma 2 + Proposition 5 block ====================

\begin{lemma}[Endpoint Behavior of Beliefs and Execution Prices with Bounded Noise]
\label{lem:endpoints}
Fix any cutoff strategy (equivalently, fix the induced action probabilities $(\omega_E,\omega_H,\omega_Q,\omega_P)$). 

(i) As $\kappa\downarrow 0$, $\PP(z=0)\to 1$ and hence $X=q$ almost surely. Therefore, on all reached order-flow states, the disclosure indicator $D$ is (asymptotically) revealed by $X$ and the anonymous execution price converges to the corresponding post-disclosure price:
\[
P_{\textup{trade}}(X)\;\longrightarrow\;P_{\textup{post}}(X,D(X)).
\]

(ii) As $\kappa\uparrow 1$, the noise distribution converges to $\PP(z=-1)=\PP(z=0)=\PP(z=1)=1/3$. Because the support of $z$ is bounded, extreme order flows remain perfectly informative about disclosure ($\PP(D=1\mid X=2)=1$ and $\PP(D=1\mid X\in\{-2,-1\})=0$), while interior order flows ($X\in\{0,1\}$) continue to mix across latent disclosure states via Bayes' rule.
\end{lemma}

\begin{proposition}[Hump-Shaped Minority Takeover Gains: Decomposition and Numerical Comparative Statics]
\label{prop:nonmonotonic}
Minority takeover gains admit the decomposition
\[
\Delta^{\min}(\kappa)
=
\Delta^{\textup{base}}(\kappa)
+
\Delta^{\textup{act}}(\kappa),
\qquad
\Delta^{\textup{base}}(\kappa)\equiv m_0\cdot \PP(\textup{bid}),
\qquad
\Delta^{\textup{act}}(\kappa)\equiv (\tilde m-m_0)\cdot \E\!\left[\pi(X,D)\cdot \1\{\textup{bid}\}\right].
\]
In the baseline calibration and across the parameter sweeps reported in Section~\ref{sec:numerics}, $\Delta^{\textup{base}}(\kappa)$ increases in liquidity $\kappa$ while $\Delta^{\textup{act}}(\kappa)$ decreases, so that $\Delta^{\min}(\kappa)$ is hump-shaped with a unique interior maximizer.
\end{proposition}

The hump arises because higher liquidity increases the incidence of takeovers (raising the baseline component) but reduces the extent to which activism is inferred and priced without disclosure (lowering the activism-driven component). With bounded noise trading, the right-endpoint $\kappa\uparrow 1$ does not generate a fully uninformative order-flow limit; instead, the decline in $\Delta^{\textup{act}}(\kappa)$ is a general-equilibrium outcome driven by the endogenous reallocation of engagement across the quiet and public regimes, which we document numerically.

%==================== END REPLACEMENT: Lemma 2 + Proposition 5 block ======================
```

**Why this is watertight:**

* It removes any theorem claim that requires proving (\omega_Q\to 0) analytically.
* It still preserves the economic narrative and makes the hump a **numerical** comparative static, which is what you actually have.
* It aligns with your bounded-noise specification and avoids the old contradiction.

### Replacement text (appendix proofs for Lemma 2 + Proposition 5)

Now replace the broken proofs at lines **1258–1297**.

**BEGIN REPLACEMENT (replace the entire Lemma 2 and Proposition 5 proof blocks, lines 1258–1297):**

```tex
%==================== BEGIN REPLACEMENT: Proofs of Lemma 2 and Proposition 5 ====================

\subsection{Proof of Lemma~\ref{lem:endpoints}}
\label{app:proof-endpoints}

\begin{proof}
Fix a cutoff strategy and hence fix the induced action probabilities $(\omega_E,\omega_H,\omega_Q,\omega_P)$.

(i) As $\kappa\downarrow 0$, we have $\PP(z=0)=1-\frac{2}{3}\kappa\to 1$ and $\PP(z=\pm 1)=\frac{\kappa}{3}\to 0$. Therefore $z=0$ almost surely in the limit and $X=q+z\to q$. Since $D=1$ if and only if $q=+1$, the disclosure state becomes a deterministic function of $X$ on all reached order-flow states: $X=1$ implies $(q,D)=(+1,1)$, while $X\in\{-1,0\}$ implies $D=0$. Hence the conditional mixing weights in~\eqref{eq:pricing_trade} satisfy $\PP(D=d\mid X)\to 1\{d=D(X)\}$, and the anonymous execution price
\[
P_{\textup{trade}}(X)=\sum_{d\in\{0,1\}}\PP(D=d\mid X)\,P_{\textup{post}}(X,d)
\]
converges to $P_{\textup{post}}(X,D(X))$.

(ii) As $\kappa\uparrow 1$, $\PP(z=-1)=\PP(z=0)=\PP(z=1)=1/3$. Because $z$ has bounded support, the extreme order flows identify $q$ and hence $D$: if $X=2$, then necessarily $(q,z)=(+1,+1)$ and thus $D=1$, so $\PP(D=1\mid X=2)=1$; if $X=-2$, then necessarily $(q,z)=(-1,-1)$ and thus $D=0$; if $X=-1$, then $q=+1$ would require $z=-2$ which is impossible, so $\PP(D=1\mid X=-1)=0$. For $X\in\{0,1\}$ both $q=0$ and $q=+1$ are feasible with appropriate noise realizations, so $\PP(D=1\mid X)\in(0,1)$ is determined by Bayes' rule (see Appendix~\ref{app:proof-posteriors} for the explicit formula).
\end{proof}

\subsection{Proof of Proposition~\ref{prop:nonmonotonic}}
\label{app:proof-nonmonotonic}

\begin{proof}
By definition, minority takeover gains equal the expected realized premium paid in a consummated takeover:
\[
\Delta^{\min}(\kappa)=\E\!\left[m^{R}(a)\cdot \1\{\textup{bid}\}\right],
\qquad
m^{R}(a)=m_0+a(\tilde m-m_0).
\]
Substituting the affine form of $m^{R}(a)$ and using linearity of expectation yields:
\begin{align*}
\Delta^{\min}(\kappa)
&=\E\!\left[\big(m_0+a(\tilde m-m_0)\big)\cdot \1\{\textup{bid}\}\right]\\
&=m_0\,\E[\1\{\textup{bid}\}]+(\tilde m-m_0)\,\E\!\left[a\cdot \1\{\textup{bid}\}\right].
\end{align*}
Since $\PP(\textup{bid})=\E[\1\{\textup{bid}\}]$, this gives the baseline component $\Delta^{\textup{base}}(\kappa)=m_0\PP(\textup{bid})$.

To express the activism component in terms of $\pi(X,D)=\PP(a=1\mid X,D)$, apply the law of iterated expectations:
\[
\E\!\left[a\cdot \1\{\textup{bid}\}\right]
=\E\!\left[\E\!\left[a\cdot \1\{\textup{bid}\}\mid X,D\right]\right].
\]
Conditional on $(X,D)$, the bid indicator $\1\{\textup{bid}\}$ depends only on the bidder's independent synergy shock $\xi$ and the public state $(X,D)$, while $a$ is chosen by the blockholder prior to $\xi$ being realized. Thus, conditional on $(X,D)$, $a$ and $\1\{\textup{bid}\}$ are independent, so
\[
\E\!\left[a\cdot \1\{\textup{bid}\}\mid X,D\right]
=\E[a\mid X,D]\cdot \E[\1\{\textup{bid}\}\mid X,D]
=\pi(X,D)\cdot p(X,D).
\]
Because $\pi(X,D)$ is measurable with respect to $(X,D)$, we can equivalently write
\[
\E\!\left[a\cdot \1\{\textup{bid}\}\right]
=\E\!\left[\pi(X,D)\cdot \1\{\textup{bid}\}\right].
\]
Therefore,
\[
\Delta^{\min}(\kappa)
=
m_0\PP(\textup{bid})
+
(\tilde m-m_0)\E\!\left[\pi(X,D)\cdot \1\{\textup{bid}\}\right]
\equiv
\Delta^{\textup{base}}(\kappa)+\Delta^{\textup{act}}(\kappa),
\]
which is the claimed decomposition.

The monotonicity of $\Delta^{\textup{base}}(\kappa)$ and $\Delta^{\textup{act}}(\kappa)$ in $\kappa$ is a general-equilibrium comparative static that depends on the endogenous cutoff vector $(k_1,k_0,k_D)$ and the induced belief and pricing system. We therefore establish the hump shape and the monotonic component patterns numerically in Section~\ref{sec:numerics} and in the accompanying Monte Carlo evidence.
\end{proof}

%==================== END REPLACEMENT: Proofs of Lemma 2 and Proposition 5 ======================
```

**Verification:** This fixes the logical flaw in B.11 (“by definition”), removes reliance on false endpoint claims, and cleanly labels what is numerical.

---

## Patch 3 — Premium interpretation (D3)

### What it replaces

Line **231** (from the snippet at lines 230–231).

### Replacement text

**BEGIN REPLACEMENT (replace line 231 only):**

```tex
%==================== BEGIN REPLACEMENT: Premium interpretation ====================
I interpret $m_0$ and $m_1$ as \emph{per-share takeover premia} above the expected standalone fundamental value (so the consummated offer satisfies $b=\hat{V}(X,D)+m^{R}(a)$); they are distinct from $\hat{v}(s)$, the blockholder's posterior mean of fundamentals.
%==================== END REPLACEMENT: Premium interpretation ======================
```

This is essentially Gemini D3, but I used your own offer equation form.

---

## Patch 4 — Formalize A7 ((\lambda_B\le 1/2)) and fix Prop 1 proof line

### What it replaces

* Assumption table lines **892–898** currently lists A1–A6.
* Prop 1 proof lines **973–974** currently says “empirical calibrations ensure (\lambda_B<0.5)” without assumption.

### Replacement text for Assumption table insertion

Insert a new row after A6 (after line 898).

**BEGIN INSERTION (after line 898):**

```tex
\textup{(A7)} & $\lambda_B \leq 1/2$ (bid arrival rate is not too large). \\ 
```

(And update the prior row punctuation if needed.)

### Replacement text for Prop 1 proof sentence (lines 973–974)

Replace lines 973–974 with:

```tex
Because the unconditional bid probability is bounded by the bidder arrival rate ($p(X,D)\le \lambda_B$) and Assumption~\textup{(A7)} imposes $\lambda_B\le 1/2$, we have $2p(X,1)\le 1$. Consequently, the term inside the expectation is nonnegative, and it is strictly positive in any nondegenerate calibration where $p(X,1)<1/2$. This guarantees $\frac{\partial}{\partial s}(U_P-U_Q)=\beta(B_P-B_Q)>0$ and hence a unique cutoff $k_D$ solving $U_Q(k_D)=U_P(k_D)$.
```

This is the mathematically correct version.

---

## Patch 5 — Minor rigor leaks (D6) with correction

### (A) Add explicit (\mathbb P(D=1\mid X)) formula in Appendix B.3

Insert after the posterior derivations (after line ~1015, i.e., after the displayed formulas for (\pi(X,D))).

**BEGIN INSERTION (after line 1012, immediately after the (\pi) formulas):**

```tex
\medskip\noindent\textbf{Disclosure probability given order flow.}
Because $D=1$ if and only if $q=+1$, Bayes' rule implies for any $X\in\{-2,-1,0,1,2\}$,
\[
\PP(D=1\mid X)
=\frac{\omega_P\,\PP(X\mid q=+1)}{\omega_E\,\PP(X\mid q=-1)+(\omega_H+\omega_Q)\,\PP(X\mid q=0)+\omega_P\,\PP(X\mid q=+1)}.
\]
Since $X=q+z$, $\PP(X\mid q=+1)=\PP(z=X-1)$, $\PP(X\mid q=0)=\PP(z=X)$, and $\PP(X\mid q=-1)=\PP(z=X+1)$, hence
\[
\PP(D=1\mid X)
=\frac{\omega_P\,\PP(z=X-1)}{\omega_E\,\PP(z=X+1)+(\omega_H+\omega_Q)\,\PP(z=X)+\omega_P\,\PP(z=X-1)}.
\]
In particular, bounded support implies $\PP(D=1\mid X=2)=1$ and $\PP(D=1\mid X\in\{-2,-1\})=0$, while $X\in\{0,1\}$ mix across disclosure states.
```

This fixes the “mixing at (X=-1)” narrative error.

### (B) Fix Appendix B.11 definition error

If you implement Patch 2’s Proposition 5 proof replacement, you already fixed this. If you prefer minimal local edit, then replace lines 1219–1231 with the corrected conditioning derivation (Patch 2 already does so more cleanly).

---

# Final “verdict list” (as you requested)

* **P0 / D1:** PARTIALLY RESOLVED
  Removes the false “uninformative posterior” claim, but the new equilibrium limit claim (\omega_Q\to 0) is not proved. Fix by hedging to numerical.

* **P0 / D2:** PARTIALLY RESOLVED
  Decomposition is correct; monotonicities are not proved. Fix by stating they are numerically verified.

* **P1 / D5:** INTRODUCES NEW PROBLEM
  Claude’s gap is real. Fix by reverting to a belief-free lower bound proof and either (i) weaken lemma statement, or (ii) add a single extra assumption (A8) to get uniform domination over the relevant region.

* **P2 / D3:** RESOLVED.

* **P3 / D4:** RESOLVED (minor bookkeeping edits recommended).

* **P4 / D6:** RESOLVED with a minor narrative correction ((X=-1) is not a mixing state for disclosure).

---

If you want, I can also produce a **single consolidated patch file** (a “diff-style” block) that you can paste into `draft_v3.tex` with exact begin/end markers and updated line numbers after insertion (since insertions shift subsequent line numbers).

