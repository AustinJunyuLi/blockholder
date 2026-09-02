Austin, I treat the handoff as the sole factual record and the worker/attacker texts as evidence rather than authority. 

# A. Ranking

## 1. Candidate 4.3 — Tightening is a Blackwell improvement

This is the most valuable candidate because it supplies the paper’s cleanest policy-level result: at a common \(\kappa\), tightening either legal dial produces a more informative control-node experiment. That lets the paper lead with an unconditional information statement—conditional only on the maintained flagged-type identification structure—and then explain that the later sensitivity results concern a different question: how the value of that experiment changes with \(\kappa\). The cost is modest: one theorem, one explicit three-branch kernel, and one genuinely substantive added hypothesis, namely that the tighter flagged output is sufficiently informative to simulate the looser experiment. The worker included several assumptions that are unnecessary for the Blackwell result itself: (S8), (S9), and the premium curvature machinery belong only in corollaries; the main theorem should also be stated at the control node \(H\), with the arbitrary-depth extension separated. The referee’s first objection will be that the result is driven by the convention that \((B^F,Q^F,a=1)\) identifies \(s\), especially because the legal filing itself reports \(F=(B^F,a=1)\), not \(Q^F\). The answer is that the theorem is explicitly conditional on the maintained control-node information convention, and that the paper should distinguish sharply between what the filing reports and what the market has observed by the control node.

## 2. Candidate 4.2 — One cut identity for both dials

I rank this second, but only after replacing the worker’s Part 2 with a sharper argument. Part 1 should become a generic **nested-cut identity**, not a second threshold-specific copy of `cor:caught`. It then lets the paper say that both legal dials obey exactly the same accounting law: the looser pool’s sensitivity is a mass-weighted average of the tighter pool’s sensitivity and the net sensitivity of the premium mass removed by the cut. More importantly, Lemma g3 already makes Condition D over a continuum of \(\kappa\) equivalent to the sign of one finite polynomial,
\[
Q(x)=P_R(x)^2-P_A(x)^2.
\]
Thus the three one-crossing assumptions (R1)–(R3) are unnecessary: the paper can give a necessary-and-sufficient finite certificate on any compact \(\kappa\)-interval. That is both stronger and more economical. The cost is about one generic proposition plus one short computational lemma; the algebraic statements are PROVED, while application to numerically constructed coefficients remains NUMERICAL. The referee’s first objection is interpretive rather than mathematical: \(s_B\) is not generally the sensitivity of the newly caught histories themselves; it includes the survivors’ re-pricing, and the handoff indicates that this re-pricing is quantitatively dominant for the threshold cuts. The paper should therefore call \(s_B\) the **net cut leg** and reserve the literal “who gets caught” interpretation for \(\widetilde s_B\), or for cases where \(\delta\) is zero or separately bounded.

## 3. Candidate 4.1 — Order size two is the erasure regime

This is worth keeping because it provides a short, exact defence of the otherwise conspicuous two-lump normalization. It establishes that, among positive integral order sizes under the maintained ternary noise law, \(b=2\) is the unique regime combining global downward Blackwell monotonicity in \(\kappa\) with nontrivial pooling. At \(b=1\), increasing \(\kappa\) is not uniformly a garbling; at \(b\ge3\), order flow identifies the mark path exactly. The cost is very low—roughly half a page for the statement and one appendix page for the proof—and there are no premium or posterior-support assumptions. The referee’s first objection is that the proposition confirms rather than dispels the knife-edge nature of the primitive: two lumps are exactly the one-point-overlap case. The correct answer is not to call it robust or generic. It is a transparent benchmark result that tells the reader precisely what is gained and lost at neighboring integral order sizes.

### Keep, merge, and manuscript order

I would keep all three, but not as three freestanding sections.

Candidate 4.2 Part 1 should **replace** the duplicated clock-versus-threshold algebra with one generic nested-cut proposition and two one-line applications. Its submitted Part 2 should be replaced by the exact polynomial certificate below. Candidate 4.1’s one-round \(2/3\) turn, its full-history “incomparability” language, and the wider-support extension should be dropped from the paper; they are peripheral and create avoidable qualifications. Candidate 4.3’s curvature corollary should be appendix-only because the handoff reports that the required curvature fails at every calibration node.

The best manuscript order is not the ranking order:

1. State the order-size-two erasure intuition briefly in the model section; put Candidate 4.1’s proof in the appendix.
2. Present Candidate 4.3 as the first comparative-static theorem: tightening either dial improves information.
3. State explicitly that Blackwell order is a level comparison at fixed \(\kappa\) and does not order \(\lvert\partial_\kappa\Dact\rvert\).
4. Present factorisation and the pooled sensitivity representation.
5. Present Candidate 4.2’s generic cut identity, followed by the threshold and clock applications.

That sequence gives the paper a coherent progression: **what tightening does to information; where liquidity sensitivity resides; and which part of the pool a legal cut removes.**

---

# B. Proof sketches

# 1. Candidate 4.3 — Blackwell improvement under tightening

## Statement I would print

### Theorem: Blackwell monotonicity of disclosure tightening

Fix a common \(\kappa\in[0,1]\) and the control date \(H\). Let
\[
\theta=(j(s),s)
\]
be the fixed-policy type. For a rule \(r=(\tau,T)\), define the tagged control-node output
\[
Y_r=
\begin{cases}
(F,\mathsf S_{F,r}), & D_r=1,\\[2mm]
(P,\mathcal H^P_{r,H}), & D_r=0,
\end{cases}
\qquad
\mathsf S_{F,r}=(B_r^F,Q_r^F,a=1).
\]
Pinned price coordinates may be appended to \(Y_r\); they are measurable functions of the displayed information and do not enlarge the experiment.

Compare either

\[
r_+=(\tau',T),\qquad r_-=(\tau,T),
\qquad b_0<\tau'<\tau,
\]

or

\[
r_+=(\tau,T'),\qquad r_-=(\tau,T),
\qquad T'<T.
\]

Assume:

1. **(S1)–(S3): measurable primitives and fixed-policy type.** The primitive and output spaces are standard Borel, the menu and calendar are finite, and \(j(s)\) is Borel.

2. **(S4)–(S5): legal nestedness.** The clean-start and first-crossing conventions hold at every compared threshold, only Voice crosses, and filing occurs at \(c+T\).

3. **(S6): public cell tag.** The market observes whether the filing has landed.

4. **(S7m): measurable no-feedback timing.** Strengthen (S7) only by making explicit what the proof needs: the executed path, mark path, terminal target, crossing and filing dates, filing stake, and flagged order are Borel functions of \(\theta\), and none responds to realised order flow or price.

5. **(S11): fixed policies.** The plan selection and complete execution path are common across the two rules.

6. **(B1) Common noise channel.** Conditional on \(\theta\), pooled flow is
   \[
   X_{0:H}=m_{0:H}(\theta)+z_{0:H},
   \]
   where \(z_{0:H}\sim Q_\kappa\) is independent of \(\theta\) and has the same law under both rules. Independence across dates is not needed for this theorem.

7. **(B2) Control-node output convention.** On the flagged cell, the public experiment is exactly \(\sigma(\mathsf S_{F,r})\), up to pinned prices. On the pooled cell, it is exactly the public pooled history and the all-zero filing coordinates, again up to pinned prices.

8. **(B3) Identified tighter flags.** There is a Borel decoder
   \[
   \iota_+:\operatorname{ran}(\mathsf S_{F,r_+})\longrightarrow \Theta_\theta
   \]
   such that
   \[
   \iota_+\!\left(\mathsf S_{F,r_+}(\theta)\right)=\theta
   \qquad\text{whenever }D_{r_+}(\theta)=1.
   \]
   In the calibration, this follows from
   \[
   B_{r}^F+Q_{r}^F=b^*_{j(s)}(s)
   \]
   at every rule and strict monotonicity of \(s\mapsto b^*_{j(s)}(s)\) on the tighter flagged region.

Then there exists a Markov kernel \(K_H\), independent of \(\theta\), such that
\[
\mathcal L(Y_{r_-}\mid\theta)
=
\int K_H(y,\cdot)\,
\mathcal L(Y_{r_+}\in dy\mid\theta)
\qquad\text{for every }\theta.
\]
Hence
\[
\mathcal E_{r_+}(\kappa)\succeq_B\mathcal E_{r_-}(\kappa).
\]

No positive-mass condition on either cell is required. The statement includes \(\kappa=0\), \(\kappa=1\), and \(T=H\).

### Corollary: posterior risk

For every square-integrable \(q(\theta)\),
\[
\Eop\!\left[\operatorname{Var}\!\left(q(\theta)\mid Y_{r_+}\right)\right]
\le
\Eop\!\left[\operatorname{Var}\!\left(q(\theta)\mid Y_{r_-}\right)\right].
\]
In particular, this holds for \(q(\theta)=a(\theta)\).

### Conditional premium-level corollary

Add (S8), (S9), \(\Eop|v|<\infty\), and
\[
h(\nu)=\mathsf h\bigl(\pi(\nu),\widehat v(\nu)\bigr).
\]
Let
\[
Z_r=
\left(
\Prb(a=1\mid Y_r),
\Eop[v\mid Y_r]
\right),
\qquad
\mathcal K=
\overline{\operatorname{co}}\!\left(
\operatorname{essran}Z_{r_+}\cup
\operatorname{essran}Z_{r_-}
\right).
\]
If \(\mathsf h\) is convex on \(\mathcal K\), then
\[
\Dact(r_+)\ge\Dact(r_-);
\]
if \(\mathsf h\) is concave, the inequality reverses.

This last corollary is formally valid but should not be sold as a calibration result: the handoff reports that the relevant curvature condition fails at every calibration node.

### What changed relative to the worker

The main theorem no longer assumes (S8), (S9), or the premium kernel. It is stated at \(H\), which is the object the paper needs. The arbitrary-depth result becomes an extension conditional on the corresponding date-\(d\) version of (B2). The decoder is stated directly; strict monotonicity is its model-specific verification. I also avoid claiming a separate Blackwell order over \((v,a)\): for the premium corollary it is enough that \(a(\theta)\) and \(\Eop[v\mid s]\) are functions of \(\theta\).

## Proof sketch

1. **Establish nested disclosure cells.**  
   For the threshold comparison, (S4), (S5), and \(b_0<\tau'<\tau\) imply
   \[
   c(\theta;\tau')\le c(\theta;\tau),
   \]
   hence \(D_{r_-}=1\Rightarrow D_{r_+}=1\). This is exactly the inclusion in Lemma \(\ref{lem:threshold-weight}\)(i).  
   For the clock comparison, \(T'<T\) gives
   \[
   c(\theta;\tau)+T\le H
   \Rightarrow
   c(\theta;\tau)+T'\le H,
   \]
   as in Corollary \(\ref{cor:caught}\)(i). Therefore
   \[
   \mathcal C_{F,r_-}\subseteq\mathcal C_{F,r_+},
   \qquad
   \mathcal C_{P,r_+}\subseteq\mathcal C_{P,r_-}.
   \]
   **Hypotheses consumed:** (S4), (S5).

2. **Identify the common pooled branch.**  
   If the tighter rule leaves \(\theta\) pooled, nestedness leaves it pooled under the looser rule. Under (S7m) and (S11), the full mark path \(m_{0:H}(\theta)\) is the same under both rules. Under (B1), the same pooled flow has the same conditional law. Under (S6) and (B2), both outputs carry the pooled tag and all-zero filing coordinates. Thus the core pooled output channels coincide.  
   **Hypotheses consumed:** (S6), (S7m), (S11), (B1), (B2).

3. **Recover the type on the tighter flagged branch.**  
   By (B3), a tighter flagged tuple \(u\) yields
   \[
   \widehat\theta=\iota_+(u).
   \]
   In the calibration, take
   \[
   s
   =
   (b^*)^{-1}(B^F+Q^F),
   \qquad
   \theta=(j(s),s).
   \]
   Measurability follows directly from the decoder hypothesis; under the primitive verification, it follows from the Borel injective-map theorem on standard Borel spaces.  
   **Hypotheses consumed:** (S1), (S3), (S7m), (B3).

4. **Construct the Markov kernel explicitly.**  
   On an input \(y\) from the tighter experiment, define \(K_H\) as follows.

   - If \(y=(P,\mathfrak h)\), output the same core pooled history. If prices are recorded, discard the tighter price and append the pinned looser-rule price computed from \(\mathfrak h\).

   - If \(y=(F,u)\), decode \(\widehat\theta=\iota_+(u)\).

     If \(D_{r_-}(\widehat\theta)=1\), output
     \[
     \bigl(F,\mathsf S_{F,r_-}(\widehat\theta)\bigr).
     \]

     If \(D_{r_-}(\widehat\theta)=0\), draw
     \[
     z'_{0:H}\sim Q_\kappa
     \]
     and output the looser pooled history
     \[
     \left(
     P,\,
     \bigl(m_0(\widehat\theta)+z'_0,\ldots,
           m_H(\widehat\theta)+z'_H;\,0,\ldots,0\bigr)
     \right).
     \]

   Define the kernel arbitrarily outside the realised tighter-output image.  
   **Hypotheses consumed:** (B1)–(B3), (S7m), (S11).

5. **Verify the channel identity type by type.**

   - A tighter-pooled type is pooled under both rules, and the identity branch returns exactly the common channel.
   - A type flagged under both rules is decoded and mapped to its deterministic looser flagged tuple.
   - A newly flagged type is decoded, and the fresh \(Q_\kappa\) draw reproduces exactly the looser pooled channel conditional on that type.

   These cases exhaust the type space by Step 1. Therefore
   \[
   P_{r_-}(\cdot\mid\theta)
   =
   P_{r_+}(\cdot\mid\theta)K_H.
   \]
   **Hypotheses consumed:** nestedness from Step 1; (B1)–(B3).

6. **Derive posterior-risk monotonicity.**  
   Couple \(Y_{r_-}\) to \(Y_{r_+}\) through \(K_H\). For \(q\in L^2\), let
   \[
   M_+=\Eop[q(\theta)\mid Y_{r_+}],
   \qquad
   M_-=\Eop[q(\theta)\mid Y_{r_-}].
   \]
   The Markov chain gives
   \[
   M_-=\Eop[M_+\mid Y_{r_-}].
   \]
   Therefore
   \[
   \Eop\operatorname{Var}(q\mid Y_{r_-})
   -
   \Eop\operatorname{Var}(q\mid Y_{r_+})
   =
   \Eop\operatorname{Var}(M_+\mid Y_{r_-})
   \ge0.
   \]
   **Hypotheses consumed:** Blackwell kernel; \(q\in L^2\).

7. **Derive the conditional premium corollary.**  
   Both coordinates of \(Z_r\) are posterior means of functions of \(\theta\):
   \[
   \pi_r=\Eop[a(\theta)\mid Y_r],
   \qquad
   \widehat v_r
   =
   \Eop[\Eop(v\mid s)\mid Y_r].
   \]
   Hence
   \[
   Z_{r_-}=\Eop[Z_{r_+}\mid Y_{r_-}].
   \]
   Jensen’s inequality on the closed convex hull \(\mathcal K\) gives the result. This is the full-experiment analogue of the posterior-martingale argument in Lemma \(\ref{lem:g3}\)(c), but its curvature set must contain both pooled and flagged posterior pairs.  
   **Hypotheses consumed:** (S8), (S9), integrability, `eq:g-kernel`, curvature.

8. **Optional two-parameter corollary.**  
   At order size two and \(0<\kappa_L<\kappa_H<1\), apply Lemma \(\ref{lem:g2}\) on the pooled cell and the identity kernel on the flagged cell. The latter is valid because Lemma \(\ref{lem:flagged-kappa-free}\) makes the entire flagged output, including a pinned flagged price, \(\kappa\)-free. Transitivity yields
   \[
   \mathcal E_{r_+}(\kappa_L)
   \succeq_B
   \mathcal E_{r_+}(\kappa_H)
   \succeq_B
   \mathcal E_{r_-}(\kappa_H).
   \]
   I would not add the opposite-cross-comparison non-order unless the appendix supplies explicit channel matrices and two explicit decision problems or a finite infeasibility certificate.

## Weakest step and attacker nits

The weakest step is (B3), both economically and mathematically. Mathematically, the theorem needs only the weaker measurable fiber condition: the conditional looser-output channel must be constant on each tighter flagged-tuple fiber. Economically, the maintained decoder relies on \(Q^F\) being in the control-node public information set. The paper must not describe this as a generic consequence of a legal filing.

I would act on the attacker’s nits as follows:

- **Act on nit 1:** write the kernel identity first and then say “therefore the tighter experiment Blackwell-dominates.”
- **Act on nit 2:** impose \(B_r^F+Q_r^F=b^*(s)\) at every rule, not only \(r_+\), wherever the flagged posterior is described as \((1,\E[v\mid s])\).
- **Act on nit 3:** either remove the necessity example or state expressly that it is under output convention (B2).
- **Act on nit 4:** cite Lemma \(\ref{lem:flagged-kappa-free}\) at the flagged identity branch in the liquidity corollary.
- **Act on nit 5:** say the endpoint claim concerns the primitive experiment; it is not a calibration-grid claim.
- **Act on nit 6:** attribute common mark paths jointly to no feedback and fixed execution policy, (S7m) plus (S11).
- **Act on nit 7:** state where the result is strict or an equality in the calibration.
- **Ignore nit 8:** it is repository bookkeeping, not paper content.

I would additionally restrict the main theorem to \(H\). The arbitrary-depth extension is correct only under an explicit date-\(d\) version of the flagged-output convention.

## Referee’s first attack and one-line answer

**Attack:** “Your information order is built into the assumption that the flagged tuple reveals the blockholder’s exact signal.”

**Answer:** “The result is explicitly conditional on a fiber-identification condition; in the maintained control-node information structure it is verified by \(B^F+Q^F=b^*(s)\) and strict monotonicity of \(b^*\), and without that condition the order need not hold.”

## What a script computes at a node

The weak Blackwell order needs no numerical computation.

The calibration verifies (B3) analytically:
\[
b^{*\prime}(s)
=
\frac{\bar b-b_0}{2\sigma_s}
\left[
1+\left(\frac{s-\mu_v}{\sigma_s}\right)^2
\right]^{-3/2}
>0,
\]
and
\[
Q^F=b^*(s)-B^F
\quad\Longrightarrow\quad
B^F+Q^F=b^*(s).
\]
There is no tolerance: these are symbolic identities.

For calibration-specific strictness or equality, compute
\[
\Delta\Omega
=
\Omega(r_+)-\Omega(r_-)
=
\Prb(D_{r_+}=1,D_{r_-}=0).
\]
Report a non-null cut when \(\Delta\Omega>10^{-12}\), and a null cut when \(\Delta\Omega\le10^{-12}\). Under the calibration’s continuous signal and finite pooled-history support, a positive-mass newly flagged region makes the Blackwell order strict for squared-error signal prediction. The handoff’s \(T=5\) threshold pairs have positive reclassified mass; the \(T=10\) threshold pairs are null and therefore exact equalities. 

---

# 2. Candidate 4.2 — A generic cut identity and exact interval certificate

## Part 1 statement I would print

### Proposition: Nested-cut identity

Let \(r_-\) be a looser rule and \(r_+\) a tighter rule, evaluated at a common \(\kappa\) and common fixed plan and cutoff policies. Let \(h^-\) and \(h^+\) denote the pinned kernels evaluated under the public information supplied by \(r_-\) and \(r_+\), respectively.

Assume:

1. **(S1), (S6), (S7m), (S8), (S10), (S11).** The cells and kernels are measurable; disclosure is public; disclosure and executed paths are type events under no feedback; the kernels are pinned; \(\kappa\) enters only the noise law; and policies are fixed.

2. **(N1) Nested cut.**
   \[
   \mathcal C_{F,r_-}\subseteq\mathcal C_{F,r_+}.
   \]
   For a threshold comparison, this follows from (S4), (S5), and
   \(b_0<\tau'<\tau\), by Lemma \(\ref{lem:threshold-weight}\)(i).  
   For a clock comparison, it follows from (S4), (S5), and \(T'<T\), by Corollary \(\ref{cor:caught}\)(i).

3. **(N2) Non-null cut.** With
   \[
   A=\mathcal C_{P,r_-},
   \qquad
   B=\mathcal C_{F,r_+}\setminus\mathcal C_{F,r_-},
   \qquad
   R=A\setminus B,
   \]
   assume
   \[
   0<\Prb(B)<\Prb(A).
   \]

4. **(N3) Differentiability.**
   \[
   \kappa\mapsto\Eop[h^-\mid A],
   \qquad
   \kappa\mapsto\Eop[h^+\mid R]
   \]
   are differentiable at the compared \(\kappa\).

5. **(N4) Nonzero looser-pool sensitivity.**
   \[
   s_A:=
   \partial_\kappa\Eop[h^-\mid A]\ne0.
   \]

Define
\[
\varphi=\frac{\Prb(B)}{\Prb(A)},
\qquad
s_R:=
\partial_\kappa\Eop[h^+\mid R],
\]
and
\[
s_B^{\mathrm{net}}
:=
\frac{1}{\Prb(B)}
\partial_\kappa
\left\{
\Eop[h^-\ind_A]
-
\Eop[h^+\ind_R]
\right\}.
\]
This is the submitted object \(s_B\); the superscript “net” is interpretive clarification rather than a change in the mathematics.

Then:

1. \(R=\mathcal C_{P,r_+}\), \(\varphi\in(0,1)\), and
   \[
   W_r
   =
   \frac{\Prb(R)}{\Prb(A)}
   =
   1-\varphi.
   \]

2. \(\Prb(A)\), \(\Prb(B)\), and \(\varphi\) are \(\kappa\)-free.

3. The cut identity is
   \[
   s_A
   =
   (1-\varphi)s_R+\varphi s_B^{\mathrm{net}},
   \]
   equivalently
   \[
   s_R
   =
   \frac{s_A-\varphi s_B^{\mathrm{net}}}{1-\varphi}.
   \]

4. If additionally
   \[
   \widetilde s_B
   =
   \partial_\kappa\Eop[h^-\mid B],
   \qquad
   \delta
   =
   \partial_\kappa\Eop[h^+-h^-\mid R]
   \]
   exist, then
   \[
   s_B^{\mathrm{net}}
   =
   \widetilde s_B
   -
   \frac{1-\varphi}{\varphi}\delta.
   \]

5. With
   \[
   C_r=\frac{|s_R|}{|s_A|},
   \]
   one has
   \[
   C_r
   =
   \frac{|s_A-\varphi s_B^{\mathrm{net}}|}
        {(1-\varphi)|s_A|},
   \]
   and
   \[
   C_r\le1
   \quad\Longleftrightarrow\quad
   s_B^{\mathrm{net}}
   \in
   \left[
   s_A,\frac{2-\varphi}{\varphi}s_A
   \right]_{\mathrm{btw}},
   \]
   where \([u,v]_{\mathrm{btw}}=[\min\{u,v\},\max\{u,v\}]\).

6. The aggregate-leg product satisfies
   \[
   W_rC_r
   =
   \frac{|s_A-\varphi s_B^{\mathrm{net}}|}{|s_A|},
   \]
   and
   \[
   W_rC_r\le1
   \quad\Longleftrightarrow\quad
   s_B^{\mathrm{net}}
   \in
   \left[
   0,\frac{2}{\varphi}s_A
   \right]_{\mathrm{btw}}.
   \]

7. If the hypotheses of Proposition \(\ref{prop:factorisation}\) hold at both rules, including flagged-endpoint invariance, then
   \[
   W_rC_r\le1
   \quad\Longleftrightarrow\quad
   \mathcal S(r_+)\le\mathcal S(r_-).
   \]

For the threshold margin, set \(r_-=(\tau,T)\) and \(r_+=(\tau',T)\); then \(C_r=C_\tau\). For the clock margin, set \(r_-=(\tau,T)\) and \(r_+=(\tau,T')\); then \(C_r=C_T\).

This proposition does not require order size two, Lemma g1, Lemma g2, a support restriction on the pooled posterior, or flagged \(\kappa\)-invariance unless the final aggregate comparison is invoked.

## Part 2 statement I would print

### Proposition: Exact polynomial certificate for Condition D

Consider the threshold application above, and add the order-size-two hypotheses of Lemmas \(\ref{lem:g1}\)–\(\ref{lem:g3}\). Define
\[
c_k^A=c_k(\tau,T),
\qquad
c_k^R=c_k(\tau',T),
\]
and
\[
P_A(x)=\sum_{k=0}^Hc_k^A x^{H-k},
\qquad
P_R(x)=\sum_{k=0}^Hc_k^R x^{H-k},
\qquad
x(\kappa)=\frac{\kappa}{2-\kappa}.
\]

Let \(I=[\underline\kappa,\overline\kappa]\subset(0,1)\) and
\[
J=[x(\underline\kappa),x(\overline\kappa)].
\]
Then
\[
\Wrev_{\tau,T}(\kappa)
=
\left(1-\frac{\kappa}{2}\right)^H P_A(x(\kappa)),
\]
and
\[
\Wrev_{\tau',T}(\kappa)
=
\left(1-\frac{\kappa}{2}\right)^H P_R(x(\kappa)).
\]

Consequently, Condition \(\ref{cond:D}\) holds at \(\kappa\) if and only if
\[
Q(x(\kappa))\le0,
\qquad
Q(x):=P_R(x)^2-P_A(x)^2.
\]

If \(P_A\) has no zero on \(J\), then
\[
C_\tau(\kappa)\le1
\quad\text{for every }\kappa\in I
\]
if and only if
\[
Q(x)\le0
\quad\text{for every }x\in J.
\]

Let
\[
\Xi
=
\{x(\underline\kappa),x(\overline\kappa)\}
\cup
\{x\in\operatorname{int}J:Q'(x)=0\}.
\]
If \(Q\) is nonconstant, \(\Xi\) is finite and
\[
Q\le0\text{ on }J
\quad\Longleftrightarrow\quad
\max_{x\in\Xi}Q(x)\le0.
\]
If \(Q\) is constant, one evaluation suffices.

This is a necessary-and-sufficient finite reduction. No one-crossing assumptions on \(c^A\), \(c^R\), or \(c^R-c^A\) are required.

### Why this is sharper than (R1)–(R3)

The worker’s sign-pattern hypotheses prove one sufficient upper interval. But the object to be signed is already a finite polynomial. Directly checking \(Q\) is weaker in hypotheses, exact in logic, and reveals both boundaries of any failure region. Indeed,
\[
Q(x)
=
\bigl(P_R(x)-P_A(x)\bigr)
\bigl(P_R(x)+P_A(x)\bigr).
\]
For the calibration pair \(q0.5\to q0.3\), the lower failure boundary is generated by \(P_R+P_A=0\), approximately \(\kappa=0.143673\), and the upper boundary by \(P_R-P_A=0\), approximately \(\kappa=0.149012\). Thus the handoff’s coarse failure bracket \([0.1440,0.1485]\) should be replaced by the sharper numerical interval. The worker’s largest root \(0.149012\) was only the upper endpoint. 

If the authors want to retain the worker’s economic sign reading, (R1)–(R3) can be a short sufficient corollary. It should not be the main certification theorem.

## Proof sketch

1. **Instantiate nestedness.**  
   At the threshold margin, Lemma \(\ref{lem:threshold-weight}\)(i) gives
   \[
   \mathcal C_F(\tau,T)
   \subseteq
   \mathcal C_F(\tau',T)
   \]
   under (S4), (S5), fixed policies, and \(b_0<\tau'<\tau\).  
   At the clock margin, Corollary \(\ref{cor:caught}\)(i) gives the corresponding inclusion under \(T'<T\). Therefore
   \[
   B\subseteq A,
   \qquad
   R=A\setminus B=\mathcal C_{P,r_+}.
   \]
   **Hypotheses consumed:** (N1), with the cited dial-specific standing conditions.

2. **Compute the weight leg.**  
   Since \(B\) and \(R\) partition \(A\),
   \[
   \Prb(R)=\Prb(A)-\Prb(B),
   \]
   so
   \[
   W_r
   =
   \frac{\Prb(R)}{\Prb(A)}
   =
   1-\varphi.
   \]
   Assumption (N2) gives \(0<\varphi<1\).  
   **Hypotheses consumed:** (N1), (N2).

3. **Show the masses are \(\kappa\)-free.**  
   Under (S7m), the two disclosure indicators are functions of \(\theta\), not realised noise. Under (S10), \(\kappa\) changes only the noise law. Under (S11), the type selection and paths do not change with \(\kappa\). Hence the probabilities of \(A\), \(B\), and \(R\) are constant in \(\kappa\).  
   **Hypotheses consumed:** (S7m), (S10), (S11).

4. **Differentiate the two pooled contributions.**  
   Define
   \[
   \Lambda_-=\Eop[h^-\ind_A],
   \qquad
   \Lambda_+=\Eop[h^+\ind_R].
   \]
   Step 3 and (N3) imply
   \[
   \partial_\kappa\Lambda_-
   =
   \Prb(A)s_A,
   \qquad
   \partial_\kappa\Lambda_+
   =
   \Prb(R)s_R.
   \]
   The definition of \(s_B^{\mathrm{net}}\) gives
   \[
   \Prb(B)s_B^{\mathrm{net}}
   =
   \Prb(A)s_A-\Prb(R)s_R.
   \]
   Divide by \(\Prb(A)\) and use
   \(\Prb(R)/\Prb(A)=1-\varphi\) to obtain
   \[
   s_A=(1-\varphi)s_R+\varphi s_B^{\mathrm{net}}.
   \]
   **Hypotheses consumed:** (N2), (N3), Step 3.

5. **Separate caught-type sensitivity from survivor re-pricing.**  
   Since \(\ind_A=\ind_B+\ind_R\),
   \[
   \Lambda_--\Lambda_+
   =
   \Prb(B)\Eop[h^-\mid B]
   -
   \Prb(R)\Eop[h^+-h^-\mid R].
   \]
   Differentiate and divide by \(\Prb(B)\):
   \[
   s_B^{\mathrm{net}}
   =
   \widetilde s_B
   -
   \frac{\Prb(R)}{\Prb(B)}\delta
   =
   \widetilde s_B
   -
   \frac{1-\varphi}{\varphi}\delta.
   \]
   **Hypotheses consumed:** the optional split differentiability; Step 3.

6. **Derive the composition band.**  
   By (S9),
   \[
   \mathcal S_P(r_-)=\Delta_m|s_A|,
   \qquad
   \mathcal S_P(r_+)=\Delta_m|s_R|.
   \]
   Hence
   \[
   C_r
   =
   \frac{|s_R|}{|s_A|}
   =
   \frac{|s_A-\varphi s_B^{\mathrm{net}}|}
        {(1-\varphi)|s_A|}.
   \]
   Because both sides are nonnegative, \(C_r\le1\) is equivalent to
   \[
   (s_A-\varphi s_B^{\mathrm{net}})^2
   \le
   (1-\varphi)^2s_A^2.
   \]
   The difference factors as
   \[
   \varphi
   (s_A-s_B^{\mathrm{net}})
   \bigl((2-\varphi)s_A-\varphi s_B^{\mathrm{net}}\bigr).
   \]
   Since \(\varphi>0\), the inequality holds exactly when \(s_B^{\mathrm{net}}\) lies between the two roots.  
   **Hypotheses consumed:** (S9), (N4), Step 4.

7. **Derive the aggregate band.**  
   Multiply the expression for \(C_r\) by \(W_r=1-\varphi\):
   \[
   W_rC_r
   =
   \frac{|s_A-\varphi s_B^{\mathrm{net}}|}{|s_A|}.
   \]
   Squaring gives
   \[
   (s_A-\varphi s_B^{\mathrm{net}})^2-s_A^2
   =
   -\varphi s_B^{\mathrm{net}}
   (2s_A-\varphi s_B^{\mathrm{net}}).
   \]
   This gives the second interval. Proposition \(\ref{prop:factorisation}\) at both rules then identifies \(W_rC_r\) with the aggregate sensitivity ratio.  
   **Hypotheses consumed:** Step 2, Step 6, and the hypotheses of Proposition \(\ref{prop:factorisation}\).

8. **Identify the threshold band with Condition D.**  
   At order size two, Lemma \(\ref{lem:g3}\)(b) gives
   \[
   s_A=-\frac12\Wrev_{\tau,T}(\kappa),
   \qquad
   s_R=-\frac12\Wrev_{\tau',T}(\kappa).
   \]
   Therefore
   \[
   C_\tau
   =
   \frac{|\Wrev_{\tau',T}|}{|\Wrev_{\tau,T}|},
   \]
   and \(C_\tau\le1\) is exactly Condition \(\ref{cond:D}\). Lemma \(\ref{lem:g2}\) is not used in this step.  
   **Hypotheses consumed:** order size two; Lemma \(\ref{lem:g3}\)(b).

9. **Derive the polynomial representation.**  
   Put \(\epsilon=\kappa/2\), \(q=1-\epsilon\), and \(x=\epsilon/q=\kappa/(2-\kappa)\). Then
   \[
   \sum_{k=0}^Hq^k\epsilon^{H-k}c_k
   =
   q^H\sum_{k=0}^Hc_kx^{H-k}
   =
   q^HP_c(x).
   \]
   Since \(q^H>0\),
   \[
   |\Wrev_R|\le|\Wrev_A|
   \Longleftrightarrow
   |P_R(x)|\le|P_A(x)|
   \Longleftrightarrow
   Q(x)\le0.
   \]
   Also
   \[
   x'(\kappa)=\frac{2}{(2-\kappa)^2}>0,
   \]
   so \(x\) maps the compact \(\kappa\)-interval monotonically onto \(J\).  
   **Hypotheses consumed:** Lemma \(\ref{lem:g3}\)(b); \(0<\kappa<1\).

10. **Reduce the continuum to finitely many checks.**  
    A continuous differentiable polynomial reaches its maximum on compact \(J\) at an endpoint or a critical point. Thus checking \(Q\le0\) at \(\Xi\) is necessary and sufficient. Separately isolate roots of \(P_A\) to verify that \(C_\tau\) is defined throughout \(I\).  
    **Hypotheses consumed:** finite \(H\); elementary polynomial calculus.

## Weakest step and attacker nits

The algebraic identity is not weak. Its vulnerable point is the interpretation of \(s_B^{\mathrm{net}}\). When
\[
\frac{1-\varphi}{\varphi}
\]
is about forty, even a moderate \(\delta\) can dominate \(\widetilde s_B\). The threshold result then says something about the **net premium mass removed by the rule**, not just the types newly required to file.

The most important technical issue is stronger than the attacker presented it. Lemma g3 defines \(\Grev(S)\) using the actual pooled type measure both to weight cells and to form on-path Bayes posteriors. The code record reportedly uses measure weights for integration but market weights containing `OFF_PATH_EPS` for beliefs. If that floor changes an on-path posterior, the computed coefficients are not literally the \(c_k\) of Lemma g3. The algebra remains valid for a perturbed \(\kappa\)-free experiment, but the paper must either:

- compute Bayes posteriors from the true measure weights at every positive-mass record cell, using the off-path convention only at zero-mass cells; or
- provide an explicit bound from the perturbed coefficients to the exact model coefficients.

I would act on all substantive attacker nits:

- Narrow the “matches the pooled pass” statement to the one node actually cross-checked.
- Resolve the measure-weight/market-weight mismatch.
- Report the exact numerical failure interval, not the coarse grid bracket.
- If (R1)–(R3) are retained as a corollary, require actual endpoint signs, not signs only after deleting zeros.
- Replace \(x\ge r_*\) by \(x>r_A\) and \(x\ge r_R,r_D\), or simply use the exact \(Q\)-certificate.
- State \(x'(\kappa)>0\).
- State the clean-start condition at the tighter threshold.
- Report \(\widetilde s_B\) and \(\delta\), or refrain from interpreting \(s_B^{\mathrm{net}}\) as caught-type sensitivity.

The direct \(Q\)-certificate makes the worker’s nits 4–6 largely moot.

## Referee’s first attack and one-line answer

**Attack:** “Your ‘who gets caught’ variable is a residual that includes re-pricing of everyone who remains silent.”

**Answer:** “Correct: the theorem calls it the net cut leg, separately reports \(\widetilde s_B\) and \(\delta\), and reserves the literal caught-type interpretation for cases in which the re-pricing term is zero or quantitatively controlled.”

## What a script computes at a node

### Exact objects

For each rule and each \(S\subseteq\{0,\ldots,H\}\), compute
\[
\Grev_r(S)
=
\sum_{\ell\in\mathcal L_r(S)}
\mu_{r,\ell}\,
\mathsf h(\pi_{r,\ell},\widehat v_{r,\ell}),
\]
where \(\mathcal L_r(S)\) is the finite partition induced by the restricted mark record, \(\mu_{r,\ell}\) is its **measure mass**, and \((\pi_{r,\ell},\widehat v_{r,\ell})\) is the Bayes posterior formed from those same measure weights whenever \(\mu_{r,\ell}>0\).

Then form
\[
c_k(r)
=
\sum_{d=0}^{H}
\sum_{\substack{S\subseteq\{0,\ldots,H\}\setminus\{d\}\\|S|=k}}
\left[
\Grev_r(S\cup\{d\})-\Grev_r(S)
\right].
\]

For a threshold pair:
\[
P_A(x)=\sum_{k=0}^Hc_k(\tau,T)x^{H-k},
\quad
P_R(x)=\sum_{k=0}^Hc_k(\tau',T)x^{H-k},
\]
\[
Q(x)=P_R(x)^2-P_A(x)^2.
\]

At a particular \(\kappa\),
\[
s_A
=
-\frac12
\left(1-\frac{\kappa}{2}\right)^H
P_A(x(\kappa)),
\]
\[
s_R
=
-\frac12
\left(1-\frac{\kappa}{2}\right)^H
P_R(x(\kappa)),
\]
\[
s_B^{\mathrm{net}}
=
\frac{s_A-(1-\varphi)s_R}{\varphi},
\qquad
\varphi
=
\frac{\Omega(r_+)-\Omega(r_-)}
     {1-\Omega(r_-)}.
\]

To make the interpretation honest, also compute \(\widetilde s_B\) by applying Lemma g3 to the cell event \(B\) under \(h^-\), and compute
\[
\delta
=
\partial_\kappa\Eop[h^+-h^-\mid R].
\]
Verify
\[
\left|
s_B^{\mathrm{net}}
-\widetilde s_B
+\frac{1-\varphi}{\varphi}\delta
\right|
\le10^{-12}.
\]

### Continuous-interval check

For \(I=[\underline\kappa,\overline\kappa]\):

1. Isolate every real root of \(Q'\) in \(J=x(I)\) to absolute width at most \(10^{-13}\) in \(x\).
2. Isolate every root of \(P_A\) in \(J\); the composition ratio is certified as defined only if none is present.
3. Evaluate \(Q\) with directed rounding or interval arithmetic at both endpoints and all isolated critical points.
4. For an interval-certified result, require every upper interval bound for \(Q\) to be \(\le0\). For the existing ordinary-floating-point record, use \(10^{-12}\) only as a regression tolerance and retain the NUMERICAL label.
5. Convert roots via
   \[
   \kappa=\frac{2x}{1+x}.
   \]
   Require any claimed lower endpoint to exceed the largest relevant root by at least \(10^{-8}\).
6. For a null cut, require
   \[
   \Prb(B)\le10^{-12},
   \qquad
   \max_k|c_k^R-c_k^A|\le10^{-12},
   \]
   and report \(C_\tau=1\) only where the common denominator is nonzero.
7. Verify the cut identity and both band formulas at each reported node with residual at most \(10^{-12}\).

The polynomial implication is PROVED. Unless the coefficient construction is enclosed with certified integration and pricing errors, the calibration application remains NUMERICAL.

---

# 3. Candidate 4.1 — Order size two as the unique nontrivial erasure regime

## Statement I would print

### Proposition: The integral-order erasure trichotomy

Fix a depth \(d\le H\) and a positive-mass cell event determined by the type. Assume (S1), (S2), (S7m), (S10), and (S11), and add:

1. **(E1) Exact independent ternary noise.**
   \[
   \Prb_\kappa(z_e=-\bar z)
   =
   \Prb_\kappa(z_e=+\bar z)
   =
   \frac{\kappa}{2},
   \qquad
   \Prb_\kappa(z_e=0)=1-\kappa,
   \]
   independently across dates and independently of the mark path.

2. **(E2) Integral order size.** For an integer \(b\ge1\),
   \[
   m_e\in\{0,b\bar z\},
   \qquad
   X_e=m_e+z_e.
   \]

3. **(E3) Nondegenerate mark-path state space.** The conditional mark-path set
   \[
   \mathcal M\subseteq\{0,b\bar z\}^{d+1}
   \]
   contains at least two distinct paths of positive conditional mass.

Let \(E_\kappa^{b,d}\) denote the finite experiment about \(m\in\mathcal M\) generated by \(X_{0:d}\).

Then the following two properties hold jointly if and only if \(b=2\):

1. For every \(0\le\kappa<\kappa'\le1\),
   \[
   E_\kappa^{b,d}\succeq_B E_{\kappa'}^{b,d};
   \]
   equivalently, the higher-\(\kappa\) experiment is a garbling of the lower-\(\kappa\) experiment.

2. For every \(\kappa\in(0,1)\), the experiment does not fully reveal the mark path.

More precisely:

- **\(b=2\).** The Blackwell ordering holds for all \(0\le\kappa<\kappa'\le1\). The path is not fully revealed for every \(\kappa\in(0,1]\), while \(\kappa=0\) reveals it.

- **\(b=1\).** For every \(0<\kappa<\kappa'<1\),
  \[
  E_{\kappa'}^{1,d}
  \text{ is not a garbling of }
  E_\kappa^{1,d}.
  \]
  No general claim about the reverse comparison is needed.

- **\(b\ge3\).** Every \(\kappa\)-experiment fully reveals the mark path, and all liquidity nodes are Blackwell equivalent.

At fixed policies, the \(b=2\) garbling also applies to the experiment about \(\theta\), because \(\theta\mapsto m(\theta)\mapsto X\) is a Markov chain. Full revelation of the mark path need not reveal \(\theta\) when several types have the same path.

### What changed relative to the worker

Only the assumptions actually used by the information comparison remain. The one-round \(2/3\) turn is omitted, as is any full-history incomparability claim. The wider-support extension is also omitted. These are not needed to justify the paper’s primitive and would materially lengthen the qualification.

## Proof sketch

Scale flows by \(\bar z>0\), so the two marks are \(0\) and \(b\).

1. **The \(b=2\) channel has a type-independent erasure symbol.**  
   The idle support is
   \[
   \{-1,0,1\},
   \]
   and the active support is
   \[
   \{1,2,3\}.
   \]
   They overlap only at \(1\), and
   \[
   \Prb_\kappa(X_e=1\mid m_e=0)
   =
   \Prb_\kappa(X_e=1\mid m_e=2)
   =
   \frac{\kappa}{2}.
   \]
   Hence the event \(X_e=1\) is a state-independent erasure. This is Lemma \(\ref{lem:g1}\)(a)–(b).  
   **Hypotheses consumed:** (E1), (E2) with \(b=2\).

2. **Construct the \(b=2\) garbling.**  
   For \(0\le\kappa<\kappa'\le1\), let
   \[
   \delta=\frac{\kappa'-\kappa}{2-\kappa}.
   \]
   Read the revealed set
   \[
   R_d=\{e:X_e\ne1\}.
   \]
   Delete each \(e\in R_d\) independently with probability \(\delta\), output \(1\) on deleted and already erased coordinates, and on surviving coordinates redraw from the \(\kappa'\) conditional law given the decoded mark. This is the explicit kernel of Lemma \(\ref{lem:g2}\); its proof is rowwise in the mark path and therefore applies to every \(m\in\mathcal M\), realised or not.  
   **Hypotheses consumed:** (E1), (E2), finite \(d\).

3. **Show non-revelation for \(b=2\).**  
   Take two distinct paths \(m,m'\). Construct a history in both row supports:

   - at every coordinate where they differ, choose \(X_e=1\);
   - where both marks are zero, choose \(X_e=-1\);
   - where both marks are two, choose \(X_e=3\).

   Every chosen coordinate has positive probability when \(\kappa>0\). Hence the two row supports overlap, and no decoder fully reveals the path. At \(\kappa=0\), \(X=m\) coordinate by coordinate.  
   **Hypotheses consumed:** (E1), (E3).

4. **At \(b=1\), give an explicit decision problem refuting upward garbling.**  
   Choose two distinct paths \(m,m'\in\mathcal M\), put prior probability \(1/2\) on each, and let \(q\ge1\) be the number of coordinates at which they differ. There are two actions: abstain, paying zero in both states, and claim \(m\), paying
   \[
   u(\text{claim }m,m)=1,
   \qquad
   u(\text{claim }m,m')=-C.
   \]
   Choose \(C\) larger than every finite likelihood ratio
   \[
   \frac{P_t(x\mid m)}{P_t(x\mid m')}
   \]
   on the common support at \(t=\kappa\) and \(t=\kappa'\). Such a finite \(C\) exists because the signal space is finite and both nodes are interior.

   The claim is then optimal exactly on histories that are possible under \(m\) and impossible under \(m'\). At each differing coordinate, the unique \(m\)-only extreme occurs with probability \(t/2\). Therefore the decision value is
   \[
   V_t
   =
   \frac12
   \left[
   1-\left(1-\frac t2\right)^q
   \right],
   \]
   which is strictly increasing in \(t\). Hence
   \[
   V_{\kappa'}>V_\kappa.
   \]
   If \(E_{\kappa'}^{1,d}\) were a garbling of \(E_\kappa^{1,d}\), no decision problem could have greater value under \(E_{\kappa'}^{1,d}\). Contradiction.  
   **Hypotheses consumed:** (E1)–(E3).

5. **At \(b\ge3\), decode the path.**  
   The idle and active supports are
   \[
   \{-1,0,1\},
   \qquad
   \{b-1,b,b+1\}.
   \]
   Since \(b-1\ge2\), they are disjoint. Decode \(m_e=0\) from \(X_e\le1\) and \(m_e=b\) from \(X_e\ge2\). Thus every node fully reveals the path.  
   **Hypotheses consumed:** (E2) with \(b\ge3\).

6. **Show equivalence across \(\kappa\) when \(b\ge3\).**  
   Decode \(m\) from the source history, draw fresh ternary noise from the target liquidity node, and output \(m+z'\). This gives a kernel in either direction between every pair of nodes.  
   **Hypotheses consumed:** Step 5; (E1).

7. **Conclude uniqueness.**  
   The \(b=2\) regime satisfies both properties. The \(b=1\) regime fails global downward Blackwell monotonicity. The \(b\ge3\) regime fails non-revelation.  
   **Hypotheses consumed:** Steps 1–6.

## Weakest step and attacker nits

The proof’s most delicate step is the \(b=1\) refutation for arbitrary multi-round path sets. A one-round counterexample alone would not suffice. The explicit \(q\)-coordinate decision problem above is what closes that gap.

I would act on every substantive attacker nit:

- Delete or rigorously confine the \(2/3\) comparison to a one-round two-state remark. My preference is to delete it.
- Say the Lemma g2 kernel is verified rowwise for every mark path, rather than inferring unrealised paths from a theorem stated over realised types.
- Correct any statement that the threshold theorem uses Lemma g2; it uses Lemma g3(b).
- Replace “one round settles both only-if regimes” with the full \(q\)-coordinate argument.
- Verify (E3) at every calibration node where the proposition is invoked.

The repository-file nit is irrelevant.

## Referee’s first attack and one-line answer

**Attack:** “The proposition merely proves that \(b=2\) is the knife-edge overlap chosen to manufacture the erasure theorem.”

**Answer:** “Yes—the proposition is a transparent benchmark classification, not a genericity claim: \(b=1\) confounds signals non-monotonically, \(b=2\) produces nontrivial erasure, and \(b\ge3\) eliminates pooling altogether.”

## What a script computes at a node

No pooled pricing pass or policy solution is required for the proposition.

An optional applicability check computes, in the pooled cell,
\[
\mu_m=\Prb\bigl(m(\theta)=m\mid D=0\bigr),
\qquad
N_{\mathcal M}
=
\#\{m:\mu_m>10^{-12}\}.
\]
Require
\[
N_{\mathcal M}\ge2.
\]
Where possible, these masses should be certified analytically from the normal CDF and the \(n(s)\) breakpoints rather than by quadrature. If \(N_{\mathcal M}=1\), order flow is independent of type inside the cell and \(\mathcal S_P=0\); the substantive sensitivity comparison is degenerate.

For regression tests of the explicit kernels, require:

\[
\min_{x,y}\Lambda(y\mid x)\ge-10^{-12},
\]
\[
\left|\sum_y\Lambda(y\mid x)-1\right|\le10^{-12}
\quad\text{for every }x,
\]
and
\[
\left\|P_\kappa\Lambda-P_{\kappa'}\right\|_\infty
\le10^{-12}.
\]

These are code checks, not proof ingredients.

---

# C. Holistic comments

## 1. Put the Blackwell order before the sensitivity results

The Blackwell theorem should come first. It gives a clean answer to the broad policy question:

> At a fixed noise environment and fixed blockholder policy, a tighter disclosure rule improves the market’s information.

The sensitivity results then answer the narrower and more difficult question:

> How does changing the noise environment move the premium under each rule, and why can the derivative magnitude behave differently even though the tighter experiment is more informative at every fixed \(\kappa\)?

The paper should place a conspicuous sentence immediately after the Blackwell theorem:

\[
\mathcal E_{r_+}(\kappa)\succeq_B\mathcal E_{r_-}(\kappa)
\quad\not\Rightarrow\quad
\left|\partial_\kappa\Dact(r_+)\right|
\le
\left|\partial_\kappa\Dact(r_-)\right|.
\]

That distinction prevents the most predictable reader confusion. The Blackwell result orders levels at a fixed \(\kappa\); the dial results compare slopes across two different experiment families.

## 2. The unified cut identity should replace, not sit beside, the two-corollary presentation

One generic nested-cut proposition is better than a complete clock corollary plus a nearly identical threshold corollary. The generic proposition should be followed by:

- **Threshold application:** nestedness from Lemma \(\ref{lem:threshold-weight}\); Condition D identification from Lemma \(\ref{lem:g3}\)(b).
- **Clock application:** nestedness and factorisation from Theorem \(\ref{thm:clock}\).

The main text can still give separate economic paragraphs because the legal interventions differ. The appendix should not repeat the algebra.

I would also rename the submitted \(s_B\) as \(s_B^{\mathrm{net}}\), or at least write “net cut leg” every time it is interpreted. The decomposition
\[
s_B^{\mathrm{net}}
=
\widetilde s_B
-
\frac{1-\varphi}{\varphi}\delta
\]
should appear immediately after its definition, not several paragraphs later. Otherwise “who gets caught” invites the reader to assume that \(s_B\) is a conditional sensitivity of the newly caught types.

## 3. Put the erasure proposition’s statement in the model section and its proof in the appendix

The model section should contain the three-regime intuition in four or five lines:

- \(b=1\): overlapping flows carry state-dependent likelihood ratios, so liquidity need not be a garbling.
- \(b=2\): the supports meet at one state-independent erasure symbol.
- \(b\ge3\): the supports are disjoint, so the mark is revealed.

The formal proposition can be stated there or in a short boxed remark. The full decision-problem proof belongs immediately before or after Lemmas g1 and g2 in the appendix.

Do not present Candidate 4.1 as a headline policy result. It is a model-design transparency result.

## 4. What the referee says first about the fixed-policy benchmark

The first objection will be:

> “The benchmark policy was selected by an equilibrium solver, but the solver’s candidate is not an equilibrium. Why should calculations at that policy be economically meaningful, and why should a small payoff regret imply robustness of the information and sensitivity conclusions?”

The best one-line response is:

> “The paper makes no equilibrium comparative-static claim: every theorem is exact for any fixed policy, and the calibration uses a pre-specified benchmark whose maximal interim regret is certified below \(2.4\times10^{-4}\); all numerical claims are labelled as benchmark-policy results rather than equilibrium outcomes.”

That answer is necessary but not sufficient. The regret record is strong evidence that the benchmark is close to sequentially optimal in payoff units, but it does not by itself establish that \(\Omega\), \(C_\tau\), the polynomial roots, or the signs of sensitivity comparisons are robust to nearby policies. Small utility regret need not imply small changes in posterior composition.

I would add one numerical robustness exercise:

1. Define a transparent neighborhood of cutoff policies around
   \[
   k=(0.9425017267,1.8484512098),
   \]
   including the node-specific solver candidates and policies that remove the \(s\in(1.8608,1.8625)\) Voice island.

2. Recompute \(\Omega\), the \(c_k\), the polynomial \(Q\), and the cut identities throughout that neighborhood.

3. Report the smallest margin by which each claimed sign survives.

That would answer the economically relevant objection much more directly than the regret percentage alone.

The statement that the maximum regret is roughly \(0.6\%\) of the payoff level \(0.038\) is useful scale information, but it should not be treated as a theorem that the policy is “approximately an equilibrium.” The natural metric is the absolute maximal profitable deviation, together with robustness of the paper’s outcome statistics.

## 5. Items in sections 5–9 that should be corrected or clarified

### First: remove dead inherited assumptions and equilibrium apparatus

The inherited model text still contains \(\Atau\), \(\Abr\), the general-equilibrium derivative machinery, and the cutoff-PBE existence architecture, even though the handoff says:

- the pooled-support assumption was dropped and is violated by the calibration;
- the general-equilibrium dominance result is absent;
- existence is absent;
- the paper is fixed-policy.

If that material remains in the actual draft, it will confuse the referee and make the paper look internally inconsistent. Remove \(\Atau\), \(\Abr\), \(\AGE\), \(g_r^{PE}\), and \(\mathcal B_r^{GE}\) unless they are clearly quarantined as discarded inherited material. The fixed-policy paper does not need a long equilibrium-definition subsection.

### Second: stop calling the benchmark or its distribution an equilibrium

Section 7 describes the threshold ladder as quantiles of the “baseline equilibrium’s stake-at-filing distribution,” while section 4.3 expressly says that the benchmark is not an equilibrium. Rename this everywhere as the:

- benchmark-policy stake-at-filing distribution;
- solver benchmark;
- frozen calibration policy.

This is not cosmetic. A referee will quote the inconsistent labels back at the authors.

### Third: clarify observability of \(Q^F\)

The model says the filing reports
\[
F=(B^F,a=1),
\]
but the flagged control-node tuple is
\[
\mathsf S_F=(B^F,Q^F,a=1).
\]
Candidate 4.3 relies on the latter. The paper must say where \(Q^F\) comes from:

- Is it legally disclosed?
- Is it inferred from an observed post-filing residual trade?
- Has the residual order already executed by the control node?
- Is it a modelling convention rather than an empirical feature?

The theorem should not describe \(Q^F\) as part of the filing if it is not.

### Fourth: strengthen the standing measurability condition

The inherited primitive restriction says every \(s\mapsto B_j(s,d)\) is Borel, but standing condition (S4) explicitly states regularity only for Voice paths, and original (S7) merely calls the remaining objects “functions.” The experiments, conditional laws, and decoder kernels require measurable mark and tuple maps for every selected plan, including Exit and Hold.

The clean fix is to amend (S7) to:

> All no-feedback path, mark, crossing, filing, and tuple maps are Borel functions of \((j,s)\).

This also makes Candidate 4.3’s measurable-kernel proof cleaner.

### Fifth: reconcile the off-path floor with Lemma g3

As noted above, the code’s distinction between measure weights and market weights is not innocuous if `OFF_PATH_EPS` changes beliefs at positive-mass histories. Lemma g3 is a statement about the actual posterior experiment. A tiny perturbation may be numerically harmless, but exact identification requires either exact on-path Bayes weights or a perturbation-error bound.

This is probably the most important implementation issue remaining in Candidate 4.2.

### Sixth: do not advertise the curvature corollary as an applied mechanism

The handoff says the curvature condition of Lemma g3(c) fails at every calibration node and that the garbling machinery contributes to neither threshold leg on the grid. The paper can retain the convex/concave expectation result as a general information-theoretic corollary, but it should not imply that it explains the numerical threshold result.

### Seventh: treat \(T=10\) threshold comparisons as a boundary check

At \(T=H=10\), the five thresholds induce the same flagged set and identical coefficient vectors. Thus:

\[
W_\tau=1,\qquad C_\tau=1,
\]
where the common sensitivity is nonzero.

That is a useful consistency check, but it is not substantive evidence for the threshold dial. The main calibration discussion should focus on the four non-null \(T=5\) cuts.

### Eighth: update the below-grid failure record

The coarse statement that Condition D fails over approximately \([0.1440,0.1485]\) should be replaced by the polynomially identified numerical interval
\[
[0.143673,\;0.149012]
\]
for the \(q0.5\to q0.3\) pair, subject to the precision of the underlying coefficients. The two boundaries have different meanings:
\[
P_R+P_A=0
\]
at the lower boundary and
\[
P_R-P_A=0
\]
at the upper boundary.

### Ninth: do not claim strict Blackwell order solely from a change in \(\Omega\)

Positive reclassified mass is not, in complete generality, sufficient for strict Blackwell dominance: the looser experiment might already reveal everything relevant on that set. In this calibration strictness follows because the tighter tuple identifies a continuously distributed \(s\), whereas the looser pooled history has finite support. That extra argument should be stated. At the \(T=10\) threshold pairs, zero reclassified mass gives equality immediately.

### Tenth: trim Candidate 4.1 aggressively

The one-round exact turn at \(2/3\) is mathematically interesting but distracts from the paper’s full-history experiment, and the attacker supplied explicit multi-round counterexamples to the corresponding incomparability language. The proposition needs only:

- the \(b=2\) kernel;
- the explicit \(b=1\) decision problem refuting downward monotonicity;
- the \(b\ge3\) decoder.

That is the version a referee is least likely to attack as ornamental.

---

## Recommended implementation decision

Adopt the three upgrades with the following labels and placement:

\[
\boxed{
\begin{array}{ll}
\text{Candidate 4.3:} &
\text{PROVED main theorem, before sensitivity results;}\\[2mm]
\text{Candidate 4.2 Part 1:} &
\text{PROVED generic nested-cut proposition;}\\[2mm]
\text{Candidate 4.2 interval equivalence:} &
\text{PROVED computational lemma;}\\[2mm]
\text{Candidate 4.2 calibration application:} &
\text{NUMERICAL, continuous interval rather than grid only;}\\[2mm]
\text{Candidate 4.1:} &
\text{PROVED model-design proposition, proof in appendix.}
\end{array}}
\]

The central editorial change is to separate three claims that the current presentation risks blending:

1. **Information:** tightening Blackwell-improves the experiment under identified flags.
2. **Liquidity sensitivity:** Blackwell order does not sign the derivative magnitude.
3. **Selection by the rule:** the nested-cut identity shows exactly which net component must be removed for sensitivity to fall.

That is the strongest and most referee-resistant version of the two-dial paper contained in the handoff.