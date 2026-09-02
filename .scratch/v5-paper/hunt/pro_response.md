# A. Verdict on the headline and order of presentation

## Verdict

**The contrast is the right headline, but the session-spec wording is currently broader than the paper can defend.** The strongest defensible headline is:

> **At fixed policies, tightening either disclosure dial makes the public control-node experiment weakly more informative in Blackwell’s sense, because the model’s filing tuple identifies the blockholder’s signal. Yet it need not reduce the liquidity sensitivity of the engagement-related expected premium: tightening changes what silence means by changing the composition and the repricing of the unfiled pool.**

That is a materially stronger paper than the delivered version. It converts the existing results from “conditions under which more disclosure makes the premium less noise-sensitive” into a contrast between:

1. a genuine information-ordering result at a fixed \(\kappa\); and  
2. a separate comparative static in \(\kappa\) that the information ordering does not sign.

The delivered paper already contains the elements needed for that contrast: the control-node partition, the exact filing tuple \(S_F=(B^F,Q^F,a=1)\), the fixed-policy restriction, the factorisation, and the clock cut identity. In particular, the printed model states \(Q^F=b^*(s)-B^F\), while \(b^*(s)\) is strictly increasing, so \(B^F+Q^F=b^*(s)\) identifies \(s\). It also expressly acknowledges that this is a stronger information set than a filing necessarily supplies.  The appendix uses precisely that decoder as the load-bearing step in flagged-cell invariance. 

The session headline nevertheless overreaches in four places:

- “the market knows” must become “the model’s flagged tuple identifies \(s\)”; the market does not learn \(v\) or \(\xi\);
- “liquidity enters prices only through the pooled cell” must be restricted to the **control-node contribution to \(\Delta^{act}\)**; the appendix explicitly says pre-filing pooled prices can move with \(\kappa\), including on paths eventually flagged;
- “less noise-driven if and only if the removed histories carried more than their share of the noise” is not the exact criterion for the overall sensitivity \(S\); the upper overshoot bound matters, and the weight effect can produce overall attenuation even when the net removed leg is less sensitive than the original pool;
- the dominance of survivor repricing over the caught-only term is a **NUMERICAL benchmark finding**, not the general mechanism theorem. The general mechanism is inference from silence; numerical dominance of one term is its calibrated manifestation. 

## Order a referee wants

The conceptual order in the spec—Blackwell, factorisation, cut identity—is right. The formal order needs one preliminary step:

1. **Define the control-node experiment and establish the partition/nesting.** A theorem cannot compare experiments before their outputs and the two cells have been defined.
2. **Blackwell theorem.** This should be the first economic result.
3. **Immediate non-implication sentence:** Blackwell compares two rules at one fixed \(\kappa\); \(S\) compares derivatives in \(\kappa\) within each rule. One does not sign the other.
4. **Flagged-cell invariance and factorisation.** These identify where the \(\kappa\)-sensitivity comes from.
5. **Nested-cut identity.** State the clock result and its threshold analogue together in exposition, while leaving the existing clock corollary structurally intact.
6. **Polynomial certificate and calibrated reversal.** This is where “noise robustness is not monotone” becomes an actual result rather than merely a logical possibility.
7. **Order-size trichotomy and regret are supporting defenses, not steps in the central theorem chain.** The order-size result belongs in the model’s order-size subsection and the appendix’s garbling section. Regret belongs in the calibration and fixed-policy limitation discussion.

Thus, the Blackwell theorem may open the introduction’s results summary, but in Section 4 the partition or experiment definition must still appear first. The batch spec’s literal decision that Blackwell “opens the results section, before the partition” should be changed accordingly. 

## Referee’s first objection

> **The claimed Blackwell result appears to come from assuming that every filing exactly reveals a continuous private signal through \(Q^F\), rather than from disclosure regulation itself. Why is this not an assumption restated as a theorem?**

**One-line answer:** In the model \(B^F+Q^F=b^*(s)\) and strictly increasing \(b^*\) make the flagged tuple an exact signal decoder; conditional on that explicit modeling assumption, tightening the rule reveals that signal on a weakly larger set, and the theorem claims nothing beyond this model-specific experiment order.

That answer is adequate, but only if the decoder is displayed in the theorem’s hypotheses and discussed in the main text rather than buried in the invariance proof.

---

# B. The four results

## 1. Tightening either dial is a Blackwell improvement

### Verdict on the spec’s strength

**Defensible as a weak Blackwell dominance theorem under the printed model, but not “always” without an explicit decoder and exogenous-noise hypothesis.** The theorem does not require order size two, the pricing root, the premium kernel, normality, or an interior partition.

The strictness and equality statements at the calibration are not themselves purely analytic:

- the implication “positive newly flagged mass plus the decoder implies strictness” can be **PROVED**;
- the facts that the adjacent threshold cuts at \(T=5\) have positive mass and that the \(T=10\) threshold cuts are null are **NUMERICAL** calibration applications;
- the clock change \(T=10\) to \(T=5\) is not the equality case. It is a corner-to-interior comparison with a positive cut in the delivered tables. The phrase “strict at \(T=5\), equality at the \(T=10\) corner” is therefore meaningful only for the **threshold ladder**, not for the clock comparison.

### Statement I would print

**Theorem — Rule tightening Blackwell-dominates at the control node.**  
Fix a liquidity \(\kappa\in(0,1)\), the plan menu, cutoff vector, and execution paths. Let \(r=(\tau,T)\) be a disclosure rule and let \(r^{+}\) be tighter in one coordinate: either \(r^{+}=(\tau',T)\) with \(b_0<\tau'<\tau\), or \(r^{+}=(\tau,T')\) with \(T'<T\). Let the latent state be
\[
\Theta=(v,s,\xi),
\]
excluding the noise-trader marks. For a rule \(r\), define the public control-node experiment by
\[
I_H^{r}=
\begin{cases}
(0,H_H^P), & D_r=0,\\
(1,S_F^{r}), & D_r=1,
\end{cases}
\qquad
S_F^{r}=(B_F^{r},Q_F^{r},a=1).
\]

Assume:

1. the amended conditions (S1), (S3)–(S7), (S10), and (S11);
2. the noise vector is independent of \(\Theta\), and at the common \(\kappa\) has the same law under the two rules;
3. the control-node observation maps are Borel;
4. on the flagged set of either compared rule, \(S_F^{r}\) has a Borel decoder for \(s\).

Then there exists a Markov kernel \(K\), independent of \(\Theta\), such that
\[
\mathcal L(I_H^{r}\mid\Theta)
=
K\,\mathcal L(I_H^{r^{+}}\mid\Theta).
\]
Hence the tighter rule weakly Blackwell-dominates the looser rule at the control node.

If, in addition,
\[
\Pr(D_{r^{+}}=1,D_r=0)>0,
\]
the conditional law of \(s\) on that newly flagged set is nonatomic, and the pooled observation has finite range, then the dominance is strict. If the two flagged cells agree almost surely, the two experiments are Blackwell-equivalent.

### Hypotheses consumed

The standing-condition block does not currently carry all the theorem needs.

- **(S1) must be amended.** It presently states only that the primitives have a joint law on Polish spaces. It should also state
  \[
  z_{0:H}\perp(v,\varepsilon,\xi)
  \]
  and, where used, that the marks are independent across dates. The main model says this, but the numbered condition does not.
- **(S3)** supplies the measurable plan selector.
- **(S4) should be amended** to say that every \(s\mapsto B_j(s,d)\) is Borel. Voice monotonicity gives Borel regularity for Voice, and Exit and Hold are constant in the printed model, but the standing condition should say it directly.
- **(S5)** supplies the legal clock and nested flagged cells.
- **(S6)** makes the flag public.
- **(S7) should be amended** to say that the listed policy objects are **Borel** functions of the plan and signal.
- **(S10)** supplies the single \(\kappa\)-channel.
- **(S11)** fixes the policies across rules.
- Add **(S12), Flagged-tuple decoder**:

  > For every rule comparison to which it is applied, the map \(s\mapsto S_F^r(s)\) is injective almost surely on the relevant flagged set and has a Borel inverse. In the printed model this follows from
  > \[
  > B_F^r(s)+Q_F^r(s)=b^*(s)
  > \]
  > and strict monotonicity of \(b^*\).

No part of (S8) or (S9), and no pricing-root assumption, is needed for this information-order theorem.

### Weakest step

The weak step is the simulation of the looser **pooled** observation from a newly flagged tighter observation.

On the newly flagged set, the tighter rule has discarded the realised pooled flow history and reports \(S_F^{r^+}\). To reproduce the looser experiment, the garbling kernel must:

1. decode \(s\) from \(S_F^{r^+}\);
2. reconstruct the looser strategic mark path from the fixed policy;
3. draw a fresh noise vector from its common law at \(\kappa\);
4. construct the looser pooled history.

That is a legitimate Blackwell garbling only because realised noise is excluded from the state and is independent of the state. If the state included realised noise or trading-cost histories, or if the flagged tuple did not decode \(s\), the proof would fail.

### Spec lines to change

Change:

> “It holds always.”

to:

> “It holds under the model’s exact flagged-tuple decoder, exogenous noise, and fixed no-feedback policies.”

Change:

> “the market knows”

to:

> “the market observes a tuple that, in the model, identifies the blockholder’s signal.”

Change:

> “strict at \(T=5\), an equality at the \(T=10\) corner”

to:

> “For the adjacent threshold comparisons, the conditional strictness result applies where the cut has positive mass at \(T=5\); at \(T=10\) those threshold comparisons are Blackwell-equivalent because the cut is null. The clock comparison \(T=10\to5\) is a separate, non-null comparison.”

The paper should never infer strictness from an increase in the flagged share alone. Strictness uses positive cut mass **plus** the decoder, nonatomic signal variation, and the inability of the finite pooled signal to reconstruct the continuous flagged tuple.

---

## 2. Order size two is the unique integral exact-erasure order size

### Verdict on the spec’s strength

**The central trichotomy is defensible, but it must be stated as a property of the binary order-mark channel, not unconditionally as a property of every induced pooled type experiment.**

The paper fixes order size two. To compare integer order sizes, the proposition must introduce a local auxiliary integer \(r\) by changing only
\[
q_d=2\bar z g_d
\quad\text{to}\quad
q_d=r\bar z g_d,
\qquad r\in\mathbb N_+.
\]
That comparison is not currently a primitive of the printed model.

The phrases “one is not monotone” and “three and above decodes” also need objects:

- \(r\ge3\) decodes the **binary order mark**, not generally the continuous type or signal;
- \(r=1\) is not globally Blackwell-monotone over the entire \(\kappa\)-family. This does not establish that every pair of \(r=1\) experiments is incomparable, nor that every restricted prior over the paper’s actual mark paths generates nonmonotonicity.

### Statement I would print

**Proposition — Integer order-size trichotomy for the binary order-mark channel.**  
For an auxiliary positive integer \(r\), let
\[
X_d=r\bar z\,g_d+z_d,\qquad g_d\in\{0,1\},
\]
where \(\bar z>0\) and
\[
z_d\in\{-\bar z,0,+\bar z\}
\]
with probabilities \(\kappa/2,1-\kappa,\kappa/2\). Assume the noise marks are independent across rounds and independent of the mark path. At any finite depth \(d\):

1. **Order size two.** For \(r=2\), the channel is Blackwell-equivalent to independent erasure of each coordinate \(g_e\), with erasure probability
   \[
   \varepsilon=\kappa/2,
   \]
   followed by ancillary randomisation whose conditional law does not depend on the mark path. Consequently, for \(0<\kappa<\kappa'<1\), the experiment at \(\kappa'\) is obtained from that at \(\kappa\) by independently deleting each previously revealed coordinate with probability
   \[
   \frac{\kappa'-\kappa}{2-\kappa}.
   \]

2. **Larger integral orders.** For every \(r\ge3\), the idle support
   \[
   \{-\bar z,0,\bar z\}
   \]
   and active support
   \[
   \{(r-1)\bar z,r\bar z,(r+1)\bar z\}
   \]
   are disjoint. The order mark is therefore decoded in every round, and the experiments at different \(\kappa\) are Blackwell-equivalent as experiments about the mark path.

3. **Order size one.** For \(r=1\), there is no global Blackwell-monotone ordering of the channel over \(\kappa\). In the one-coordinate equal-prior decision problem of guessing \(g\), the optimal success probability is
   \[
   V_1(\kappa)=
   \begin{cases}
   1-\kappa/2, & \kappa\le 2/3,\\
   \kappa, & \kappa\ge 2/3,
   \end{cases}
   \]
   which first falls and then rises.

Thus \(r=2\) is the unique positive integer order size for which the entire interior \(\kappa\)-family is an exact, nontrivial erasure family: \(r\ge3\) fully reveals the marks, while \(r=1\) has no single global information direction.

The existing order-size-two erasure lemma already proves the first part through the common ambiguous value \(+\bar z\) and the deletion kernel. 

### Hypotheses consumed

- Amended **(S1)**: independent, date-independent ternary noise.
- **(S2)**: finite depth.
- **(S7)**: the binary mark path is a deterministic measurable function of type.
- **(S10)** and **(S11)** where the proposition is transferred from the mark channel to a pooled cell whose type law must remain \(\kappa\)-free.
- A new local definition:
  \[
  r\in\mathbb N_+,\qquad q_d=r\bar z g_d.
  \]
- For “nontrivial” and strict erasure effects, both mark values must occur with positive probability in at least one coordinate. The standing conditions do not currently guarantee this for every pooled cell.

Normality, pricing, and the disclosure decoder are unnecessary.

### Weakest step

The vulnerable step is not \(r=2\); that channel calculation is exact. It is the passage from the channel trichotomy to a claim about the paper’s **actual pooled experiment** at \(r=1\).

The equal-prior calculation proves that no universal monotonicity theorem can hold for the binary \(r=1\) channel. It does not prove nonmonotonicity for a degenerate pooled cell in which every admissible type has the same mark path. The main text should therefore state the result at the channel level, and only transfer it to an induced type experiment when the mark-path support is nondegenerate.

### Spec lines to change

Change:

> “Order size two is the unique integral order size at which more liquidity is an exact, non-trivial erasure of the pooled experiment.”

to:

> “Among positive integer multiples of one noise lump, order size two is the unique order size whose binary order-mark channel forms an exact, nontrivial erasure family over all \(\kappa\in(0,1)\).”

Change:

> “one is not monotone”

to:

> “the order-size-one channel is not globally Blackwell-monotone over the full \(\kappa\)-family.”

Change:

> “three and above decodes”

to:

> “three and above decode each binary strategic-order mark; they need not identify the underlying continuous type.”

Also correct the session spec’s phrase “two rounds of the inherited two-round structure.” The delivered paper has trading dates \(d=0,\ldots,H\) and calibrates \(H=10\), not a two-round model. 

---

## 3. Threshold cut identity and polynomial certificate

### Verdict on the spec’s strength

There are two analytically distinct claims:

1. **The threshold cut identity** is fully defensible and does not require order size two. It is the same accounting algebra as the clock corollary after rule-specific objects are relabelled.
2. **The polynomial certificate** is fully defensible as an analytic implication at order size two. Its application to numerically computed coefficients and its low-liquidity failure interval remain **NUMERICAL**, unless coefficient and root errors are enclosed rather than merely approximated.

The spec overstates both the economic interpretation and what is being certified. In particular, failure of the composition condition \(C_\tau\le1\) does **not** by itself establish that total sensitivity rises. The weight-adjusted inequality \(S_{\tau'}>S_\tau\) requires a second polynomial.

### Statement I would print

#### Threshold-margin cut identity

Fix \(b_0<\tau'<\tau\), a common window \(T\), common \(\kappa\), and fixed plan, cutoff, and execution policies. Let the looser and tighter rules be
\[
r=(\tau,T),\qquad r^+=(\tau',T).
\]
Define
\[
A=C_P(r),\qquad
B=C_F(r^+)\setminus C_F(r),\qquad
\phi=\frac{\Pr(B)}{\Pr(A)}.
\]
Let \(h^r\) and \(h^{r^+}\) denote the rule-specific pinned kernels. Define
\[
s_A=\partial_\kappa E[h^r\mid A],
\qquad
s_{A\setminus B}=\partial_\kappa E[h^{r^+}\mid A\setminus B],
\]
and define the **net cut leg**
\[
s_B^{\mathrm{net}}
=
\frac{1}{\Pr(B)}
\partial_\kappa
\left\{
E[h^r1_A]-E[h^{r^+}1_{A\setminus B}]
\right\}.
\]

Assume the relevant cells have positive mass and the displayed expectations are differentiable. Then:

\[
C_F(r)\subseteq C_F(r^+),\qquad
A\setminus B=C_P(r^+),\qquad
W_\tau=1-\phi,
\]
and the cell masses and \(\phi\) are independent of \(\kappa\). Moreover,
\[
s_A=(1-\phi)s_{A\setminus B}+\phi s_B^{\mathrm{net}}.
\]

Whenever \(s_A\ne0\),
\[
C_\tau\le1
\iff
\bigl(s_B^{\mathrm{net}}-s_A\bigr)
\bigl(\phi s_B^{\mathrm{net}}-(2-\phi)s_A\bigr)
\le0,
\]
and
\[
W_\tau C_\tau\le1
\iff
s_B^{\mathrm{net}}
\bigl(2s_A-\phi s_B^{\mathrm{net}}\bigr)
\ge0.
\]

Finally, if
\[
\widetilde s_B=\partial_\kappa E[h^r\mid B],
\qquad
\delta=\partial_\kappa E[h^{r^+}-h^r\mid A\setminus B],
\]
then
\[
s_B^{\mathrm{net}}
=
\widetilde s_B-\frac{1-\phi}{\phi}\delta.
\]

The existing clock corollary already shows why \(s_B\) is not a caught-only sensitivity: it includes the repricing of survivors. 

#### Polynomial certificate

At order size two, for a rule \(r\), write
\[
L_r(x)
=
\sum_{k=0}^{H}c_k(r)(1-x)^k x^{H-k},
\qquad x=\kappa/2.
\]
The appendix’s exact representation gives
\[
\partial_\kappa M_P(r;\kappa)
=
-\frac{\Delta m}{2}L_r(\kappa/2).
\]

For a tight rule \(r^+\) and loose rule \(r\), define
\[
\Psi_C(x)=L_{r^+}(x)^2-L_r(x)^2
\]
and
\[
\Psi_S(x)
=
(1-\Omega_{r^+})^2L_{r^+}(x)^2
-
(1-\Omega_r)^2L_r(x)^2.
\]

Then:

- where \(S_P(r;\kappa)>0\),
  \[
  C\le1 \iff \Psi_C(\kappa/2)\le0;
  \]
- without taking a ratio,
  \[
  S(r^+;\kappa)\le S(r;\kappa)
  \iff
  \Psi_S(\kappa/2)\le0.
  \]

For a compact interval
\[
K=[\underline\kappa,\overline\kappa]\subset(0,1),
\]
either inequality holds throughout \(K\) if and only if the corresponding polynomial is nonpositive at:

1. the two endpoints of \(K/2\); and
2. every real critical point in the interior of \(K/2\).

If the polynomial is constant, one evaluation suffices.

This is an exact finite certificate **conditional on the exact coefficients**. The coefficients in the calibration are themselves numerical objects, so the calibrated sign and interval retain the NUMERICAL label.

### Hypotheses consumed

For the threshold identity:

- **(S1)** for a common probability space;
- **(S3)** for the fixed selector;
- **(S5)** for threshold crossing and nestedness;
- **(S7)** for fixed, no-feedback paths;
- **(S8)** for pinned rule-specific kernels;
- **(S10)** for \(\kappa\)-free cell masses;
- **(S11)** for fixed policies across rules;
- \(b_0<\tau'<\tau\), common \(T\);
- \(\Pr(B)>0\), \(\Pr(A\setminus B)>0\);
- differentiability of the relevant conditional expectations.

The pure cut identity does **not** require the flagged-tuple decoder. The decoder and flagged-cell invariance are needed when the identity is combined with Proposition 1 to make a statement about total \(S\).

For the certificate:

- all assumptions of the exact order-size-two representation in Appendix Lemmas 5–7;
- positive pooled-cell mass for the coefficients being constructed;
- exact symmetric ternary noise and binary marks;
- \(\kappa\)-independent coefficients;
- a compact interval inside \((0,1)\);
- a nonzero baseline sensitivity only if the ratio \(C\) is reported.

The current appendix’s (C-1) also contains a numbering error: “liquidity enters the primitives in one place” is **(S10)**, not (S11). The latter is fixed policies.

### Weakest step

For the identity, the algebra is not weak; it follows directly from the definition of the net cut leg. The weakest substantive step is interpreting \(s_B^{\mathrm{net}}\) as “who gets caught.” It is not the caught-only sensitivity. It is a net quantity that combines:

- the old-rule sensitivity of the histories removed; and
- the change in how the surviving histories are priced under the tighter pool.

For the certificate, the weakest step is numerical rather than analytic: obtaining complete and correctly signed coefficients and critical points in the presence of numerical integration, pricing-root approximation, nearly zero sensitivities, and the code’s off-path belief floor.

### Spec lines to change

Change:

> “Liquidity enters prices only through the pooled cell.”

to:

> “At the control node, the \(\kappa\)-sensitivity of \(\Delta^{act}\) factorises through the pooled-cell contribution; completed-filing contributions are \(\kappa\)-invariant. Earlier pooled prices and the filing-day jump are not covered.”

Change:

> “Prices become less noise-driven if and only if the removed histories carried more than their share of the noise.”

to:

> “The cut identity gives the exact criterion. For the composition leg, the net cut leg must lie between \(s_A\) and \(((2-\phi)/\phi)s_A\); for overall sensitivity, it must lie between \(0\) and \((2/\phi)s_A\). Thus sharing the pool’s sign is necessary, while both an upper overshoot bound and the weight effect matter.”

The appendix itself already emphasizes that the overall criterion may accept a net cut leg less sensitive than the original pool, directly contradicting the current headline sentence. 

Change:

> “the who-gets-caught corollary holds verbatim at the threshold margin”

to:

> “the same algebra holds at the threshold margin after replacing the clock-specific sets and rule-indexed kernels by their threshold counterparts.”

“Verbatim” is false because the rule superscripts, common margin, and newly flagged set must all be relabelled.

Change:

> “a polynomial certificate decides it exactly on any liquidity interval”

to:

> “at order size two, a polynomial certificate decides the composition and overall-sensitivity inequalities on any stated compact interval contained in \((0,1)\), conditional on exact coefficients; its calibration application is NUMERICAL.”

Do not rename the existing condition “Condition D” unless every main-text and appendix reference is changed. The delivered paper calls it **Condition 1**.

Finally, the low-liquidity sentence must name:

- the specific adjacent threshold pair;
- \(T\);
- the fixed benchmark policy;
- order size two and \(H=10\);
- the exact certified interval;
- whether the reversal concerns \(C_\tau\) or total \(S\).

No such interval or pair is contained in the supplied files, so it cannot yet be inserted by prose.

---

## 4. Benchmark-policy maximal regret

### Verdict on the spec’s strength

**The paper can defend a numerical deviation diagnostic, but the phrase “maximal regret” is not defined by the printed model or the spec.**

The model defines plan utilities \(U_j(s)\), but it does not define what prices or beliefs apply when a type deviates from the frozen selector. That is particularly consequential because the public history and the market’s posterior depend on the policy mapping. The existing full-support reference belief for empty mark histories is not, by itself, a complete deviation convention. 

There are also two different objects the record might mean:

- a maximum adjacent-plan indifference residual at the two frozen cutoffs; or
- a maximum deviation gain over all signals and all three plans.

The first is not “maximal regret.” The second is maximal only over the computational grid unless a continuous-domain bound is supplied.

### Statement I would print

I would not print an unqualified “maximal regret” result. I would print the following once the record fixes the deviation convention:

**NUMERICAL — Frozen-policy one-step deviation diagnostic.**  
At calibration node \(n\), let \(j^b(s)\) be the plan selected by the frozen benchmark cutoffs. Under the registered frozen-belief and pricing convention \(\mathcal B_n\), define
\[
R_n^{\mathrm{grid}}
=
\max_{s\in\mathcal G_s}
\left[
\max_{j\in\{E,H,V\}}
U_{j,n}^{\mathcal B_n}(s)
-
U_{j^b(s),n}^{\mathcal B_n}(s)
\right]_+,
\]
where \(\mathcal G_s\) is the stated computational signal grid. The record reports \(R_n^{\mathrm{grid}}\), the maximizing signal, the benchmark plan, the best alternative, both utility levels, and the normalization used for the reported ratio.

> “Across the registered calibration nodes, the largest recorded one-step deviation gain under the frozen-belief convention is [record-generated value], equal to [record-generated ratio] of the stated payoff scale. This is a fixed-policy diagnostic, not an equilibrium or existence result.”

If only the two cutoff points are evaluated, use instead:

> “The maximum adjacent-plan cutoff residual is …”

and do not use the word “regret.”

### Hypotheses and definitions the paper does not carry

The new result needs, at minimum:

- **(R-1) Deviation pricing convention:** whether prices and beliefs are held at the benchmark-policy values or recomputed after changing the strategy mapping.
- **(R-2) Off-path convention:** the belief applied to every history reached by a deviation but not by the frozen policy.
- **(R-3) Maximization domain:** the exact signal grid, computational support, and treatment of the Gaussian tails outside \(\pm6\sigma_s\).
- **(R-4) Action domain:** Exit, Hold, and Voice, including tie-breaking.
- **(R-5) Scale:** utility units, denominator for the ratio, and treatment of a zero or near-zero denominator.
- **(R-6) Node set:** every \((\tau,T,\kappa)\) node over which the outer maximum is claimed.

The standing conditions support finiteness and measurability once these objects are defined, but do not determine them.

### Weakest step

The weakest step is the counterfactual payoff itself. A deviation changes the strategic order path and may reach observations that had zero probability under the frozen policy. Calling the resulting gain “regret” is meaningful only after specifying whether the deviator takes the benchmark price system and beliefs as fixed.

The second weakest step is the word “maximal.” The analytic model uses the full signal line; the computation uses a truncated, renormalized interval. A grid maximum is not a maximum over the analytic signal space without a global-optimization or tail argument.

### Spec lines to change

Change:

> “The benchmark policy’s maximal regret is reported at every node.”

to:

> “The paper reports the maximum recorded one-step menu deviation gain on the stated computational grid under a registered frozen-belief convention.”

Change:

> “The order size and the benchmark are defended by results.”

to:

> “The order-size normalization is characterized analytically, and the distance of the frozen benchmark selector from one-step optimality is reported as a numerical diagnostic.”

Change:

> “The regret record is the paper’s whole answer on this.”

to:

> “The regret record quantifies the fixed-policy approximation under its stated convention; it does not establish existence, equilibrium, or robustness to a reacting blockholder.”

The conditional existence row in the session spec should also be removed because existence is expressly out of scope for this version.

---

# C. Passages that must change

The replacements below use brackets only where the new certificate or regret records must supply numbers that are not in the attached files. Page references are to the delivered PDFs. The delivered paper’s present front matter, formal object, order-size discussion, results order, calibration claims, and conclusion are all organized around the old attenuation-first framing. 

## Main paper

### 1. Abstract, page 1

**Replace the theoretical block beginning “At fixed trading policies…” through the common-sign description of \(C_T\).**

Replacement:

> “At fixed policies and a common liquidity, tightening either disclosure dial weakly Blackwell-dominates the looser public experiment at the control node, under the model’s exact signal-decoding filing tuple. This information order does not sign the liquidity sensitivity \(S=|\partial_\kappa\Delta^{act}|\) of the engagement-related expected premium. That sensitivity factorises through the pooled cell and, for either dial, obeys a nested-cut identity in which the net cut leg includes the repricing of histories that remain unfiled. At order size two, a polynomial certificate signs both the composition and overall-sensitivity comparisons on a stated compact liquidity interval. For [named threshold pair] the benchmark certificate finds that tightening raises \(S\) on [record-generated interval] (NUMERICAL), while [record-generated repricing comparison] shows that survivor repricing dominates the caught-only contribution at the stated nodes (NUMERICAL).”

Add after it:

> “Order size two is the unique positive integer multiple of a noise lump whose binary mark channel forms a nontrivial erasure family over the full interior liquidity range. The frozen benchmark policy’s one-step deviation diagnostic is [record-generated statement] on the stated computational grid.”

The empirical sentences can remain unchanged.

### 2. Introduction, page 2, first paragraph

Replace the old central-thesis ending with:

> “The central thesis is a contrast. Tightening the rule reveals weakly more at a fixed liquidity, but it need not make the engagement-related expected premium less sensitive to liquidity noise, because removing histories from the unfiled pool changes what the absence of a filing tells the market.”

### 3. Introduction, page 2, second paragraph

Replace the sentence that moves directly from filed/unfiled cells to the sensitivity object with:

> “The paper therefore studies two distinct objects: the Blackwell order of the public control-node experiment at a fixed \(\kappa\), and the derivative in \(\kappa\) of the engagement-related premium component \(\Delta^{act}=\Delta mE[\pi p]\).”

Replace “Liquidity changes inference in the pooled cell but not what the market learns from a completed filing” with:

> “At the control node, the completed-filing contribution to \(\Delta^{act}\) is \(\kappa\)-invariant, while its pooled contribution can move with \(\kappa\). This claim does not cover earlier pooled prices or the filing-day jump.”

### 4. Introduction, page 2, paragraph beginning “The first result…”

Replace its opening with:

> “After defining the disclosure partition, the first substantive result is that a tighter threshold or shorter clock weakly Blackwell-dominates the looser control-node experiment. The result is driven by the model’s exact filing tuple: \(B^F+Q^F=b^*(s)\), and strict monotonicity of \(b^*\) identifies \(s\). A Blackwell comparison holds \(\kappa\) fixed; it therefore does not sign the derivative of \(\Delta^{act}\) with respect to \(\kappa\).”

Continue with the factorisation, cut identity, and certificate rather than presenting the factorisation as the first result.

### 5. Introduction, page 2, order-size paragraph

Replace the “At order size two…” paragraph with:

> “The choice of order size two has an information-theoretic characterization. Among positive integer multiples of one noise lump, two is the unique size for which the binary order-mark channel forms an exact, nontrivial erasure family as liquidity changes. At size one the channel is not globally ordered over \(\kappa\), while at sizes three and above each binary order mark is decoded. The proposition concerns the mark channel; decoding a mark path need not identify the continuous type.”

### 6. Introduction, page 3, contribution/road-map paragraph

Replace:

> “This paper analyses the clock dial result and the who-gets-caught characterisation.”

with:

> “The paper’s central contribution is the contrast between monotone informativeness of the disclosure rule and potentially nonmonotone robustness of the engagement-premium component, with inference from silence represented by a common nested-cut identity for the two legal dials.”

Update the roadmap so that Section 4 begins with the control-node experiment and Blackwell theorem.

### 7. Section 2.2, page 4

Replace the scope paragraph’s last two sentences with:

> “The paper separately studies the Blackwell order of the public control-node signal at a fixed liquidity and the liquidity sensitivity of \(\Delta^{act}\). Neither result is a statement about all prices, total takeover premia, or shareholder welfare; the baseline term \(m_0E[p]\) remains outside the formal comparative static.”

### 8. Section 3.1, page 5

Replace “The outcome of interest is…” with:

> “The model has two formal objects. The first is the public control-node experiment induced by \((\kappa,\tau,T)\). The second is the engagement-related expected premium \(\Delta^{act}(\kappa,\tau,T)\), its cell averages, and their liquidity sensitivities.”

### 9. Section 3.3, pages 6–7, flagged-tuple paragraph

After defining \(S_F\), insert:

> “The tuple is a signal decoder in the model:
> \[
> B^F+Q^F=b^*(s).
> \]
> Because \(b^*\) is strictly increasing, \(S_F\) identifies \(s\) on every flagged path. This exact-decoding assumption is load-bearing for the Blackwell theorem; filing status or the disclosed stake alone would not generally suffice.”

Retain the existing caveat that the exact residual order is stronger than what a filing guarantees.

### 10. Section 3.3, page 7, standing-condition sentence

Replace “(S1) to (S11)” with:

> “the amended conditions (S1) to (S12), including exogenous noise, Borel policy maps, and the flagged-tuple decoder.”

### 11. Section 3.4, page 7

Replace “Two noise lumps are a simple middle scale” with:

> “Two noise lumps are the unique positive integral order size that preserves exact, nontrivial erasure as \(\kappa\) varies: one lump has no global information direction, while three or more reveal the binary order mark.”

The existing five-support explanation can follow.

### 12. Section 3.5, pages 7–8

After “Each comparison holds \(\kappa\) fixed across the two rules,” insert:

> “This fixed-\(\kappa\) comparison is the domain of the Blackwell theorem. By contrast, \(S\) differentiates \(\Delta^{act}\) with respect to \(\kappa\) within each rule, so Blackwell dominance does not imply \(S(r^+)\le S(r)\).”

Replace “The formal outcome is…” with “The robustness outcome is…” because the experiment is now a separate formal object.

### 13. Section 4 opening and Section 4.1, pages 8–9

Change the title from “The partition and the factorisation” to:

> **“The control-node experiment and the information order.”**

Keep the disclosure-partition lemma first. Insert the Blackwell theorem immediately afterward. Move the two-cell decomposition, flagged-cell invariance, and factorisation into a following subsection titled:

> **“The pooled-cell factorisation.”**

Update the opening sentence to refer to (S1)–(S12).

### 14. Section 4.2, pages 9–10

Retain the order-size-two erasure lemma, but precede it with the integer order-size trichotomy.

After Condition 1, add:

> “At order size two, Condition 1 on a compact liquidity interval is equivalent to nonpositivity of the polynomial \(\Psi_C\) at the interval endpoints and every interior real critical point. The corresponding total-sensitivity comparison is decided by the separate weight-adjusted polynomial \(\Psi_S\).”

Do not silently rename Condition 1 as Condition D.

### 15. Section 4.3, pages 10–11

Replace the paragraph beginning “The two dials enter with different force” with:

> “The two dials have the same information direction and the same nested-cut accounting structure, but neither fact alone signs their robustness effect. Both tighten the control-node experiment in Blackwell’s order. For each dial, the looser pool’s sensitivity is a mass-weighted average of the tighter surviving pool and a net cut leg. The threshold comparison is signed on stated intervals by the order-size-two certificate; the clock theorem supplies the exact criterion \(W_TC_T\le1\).”

### 16. Section 4.4, pages 11–12

Every occurrence of “caught leg” referring to \(s_B\) must become **“net cut leg.”**

Replace the first definition with:

> “Write \(s_B^{\mathrm{net}}\) for the derivative of the pooled premium mass removed by the shorter clock per unit of removed mass. It includes the repricing of survivors and is therefore not the caught-only sensitivity \(\widetilde s_B\).”

Replace:

> “The caught leg turns \(C_T\) into…”

with:

> “The net cut leg turns \(C_T\) into…”

Add at the end:

> “The same identity and band criteria apply to a tighter threshold after replacing the two clock-indexed information sets by the two threshold-indexed information sets. This is an algebraic relabelling under the threshold’s nested cut, not a claim that the rule-specific kernels are literally the same.”

### 17. Section 5, page 12, calibration opening

After the benchmark cutoff paragraph, add:

> “For each registered calibration node, the numerical record also reports the maximum one-step menu deviation gain of the frozen selector on the stated signal grid under the registered frozen-belief convention. The largest recorded value is [value], attained at [node/signal], and equals [ratio] of [normalizer]. This is a fixed-policy diagnostic, not an equilibrium claim.”

### 18. Section 5, page 13, threshold paragraph and Table 1 caption

Replace the ending “The claim covers only the named grid” with:

> “On the delivered grid \(\kappa\in[0.15,0.85]\), the existing attenuation result remains NUMERICAL. The polynomial certificate additionally finds that for [named adjacent threshold pair] the overall sensitivity comparison reverses on \(\kappa\in[\underline\kappa,\overline\kappa]\) below that range [or other exact relationship supplied by the record]. This interval statement is NUMERICAL from certified coefficient and root enclosures.”

Replace:

> “At \(T=10\) the ladder reclassifies no mass, so both legs equal one.”

with:

> “At \(T=10\) the adjacent threshold cuts are null; these rows are Blackwell-equivalence and sensitivity-equality boundary checks, not substantive threshold findings.”

### 19. Section 5, page 14, “Who gets caught on the record” and Figure 2

Rename \(s_B\) in the prose, legend, and caption as **“net cut leg.”**

Add a record-generated sentence:

> “At each reported node,
> \[
> s_B^{\mathrm{net}}
> =
> \widetilde s_B-\frac{1-\phi}{\phi}\delta.
> \]
> The caught-only contribution is [range], the survivor-repricing contribution is [range], and the latter is [record-generated comparison] at [named nodes] (NUMERICAL).”

A statement such as “near forty” must identify whether forty is the multiplier \((1-\phi)/\phi\), a ratio of absolute contributions, or another statistic.

### 20. Section 7, page 17

Replace the first two conclusion paragraphs with:

> “At fixed plan, cutoff, and execution policies, tightening either legal dial weakly Blackwell-dominates the looser public experiment at the control node. The result rests on the model’s exact signal-decoding filing tuple and does not imply that a tighter rule makes the engagement-related expected premium less sensitive to liquidity noise.
>
> That robustness comparison runs through the unfiled pool. The flagged contribution is \(\kappa\)-invariant, the expected-premium sensitivity factorises through the pooled cell, and both dials obey the same nested-cut identity. At order size two, polynomial certificates sign the composition and total-sensitivity comparisons on stated intervals; the benchmark exhibits [record-generated low-liquidity reversal] and [record-generated survivor-repricing finding], both NUMERICAL. Order size two is uniquely a nontrivial integral erasure channel. The frozen-policy deviation record reports [record-generated regret statement], which quantifies but does not remove the fixed-policy limitation.”

The empirical conclusion can remain.

## Appendix

The appendix presently starts with flagged invariance and factorisation, specializes directly to order size two, and gives a clock-only cut section. Those structures must be minimally amended. 

### 21. Appendix preface, page 1

Replace the roadmap with:

> “The appendix first defines the disclosure partition and proves the Blackwell ordering of tighter rules, then gives flagged-cell invariance and the pooled-cell factorisation. It next characterizes integer order sizes, specializes to the order-size-two erasure representation, and proves the polynomial certificate. The final theory section gives the clock cut identity and its threshold-margin analogue.”

Change “(S1) to (S11)” to “(S1) to (S12).”

### 22. Standing condition (S1), page 5

Replace with:

> **(S1) One probability space and exogenous noise.** The primitive vector \((v,\varepsilon,\xi,z_{0:H})\) has a joint law on a finite product of Polish spaces; \(s=v+\varepsilon\); and \(z_{0:H}\) is independent of \((v,\varepsilon,\xi)\). Where the product erasure representation is invoked, the noise marks are independent across dates.

### 23. Standing condition (S4), page 5

Replace with:

> **(S4) Borel stake paths, Voice monotonicity, and a clean start.** For every plan and date, \(s\mapsto B_j(s,d)\) is Borel. Each path begins at \(B_j(s,-1)=b_0<\tau\); a Voice path is weakly increasing in \(s\) and in the calendar date.

### 24. Standing condition (S7), page 6

Replace with:

> **(S7) Borel no-feedback timing.** The executed path, order marks, terminal target, crossing date, filing date, filing stake, and flagged order are Borel functions of the plan and signal alone. Neither realised order flow nor a realised price enters them.

### 25. New standing condition (S12), page 6

Insert:

> **(S12) Flagged-tuple decoder.** On the flagged set of every compared rule, the public tuple \(S_F=(B^F,Q^F,a=1)\) identifies \(s\) through a Borel inverse. In the printed model,
> \[
> B^F+Q^F=b^*(s),
> \]
> and the strict monotonicity of \(b^*\) supplies the inverse.

### 26. After the partition lemma, pages 6–7

Insert the Blackwell theorem here, before the premium decomposition and factorisation.

The theorem’s proof should construct the garbling kernel in three cases: common pooled histories, common flagged histories, and newly flagged histories. State explicitly that realised noise is not part of the Blackwell state.

### 27. Appendix Section 2 title and setting, page 13

Change the title to:

> **“The integer order-size channel, order-size-two erasure, and the threshold dial.”**

Introduce \(r\in\mathbb N_+\) locally and state the trichotomy before specializing back to \(r=2\). The existing Lemmas 5–7 can then remain substantively unchanged.

### 28. Exact representation, pages 14–15

Add a reconciliation sentence after defining the posterior representation:

> “The analytic identity uses Bayes’ rule on positive-probability histories and does not assign mass to empty histories. The numerical off-path belief floor perturbs this identity only by the bound stated in the certificate record; every interval sign claim requires that bound to be smaller than the certified sign margin.”

A numerical floor cannot simply be described as agreeing with an exact polynomial without such a bound.

### 29. After Lemma 7 and Condition 1, pages 15–16

Insert the two-polynomial certificate lemma. One polynomial must certify \(C\le1\); a second must certify the total comparison \(S_{\mathrm{tight}}\le S_{\mathrm{loose}}\).

### 30. Appendix Section 3 title, page 20

Change:

> “The who-gets-caught corollary of the clock dial”

to:

> **“Nested cuts: the clock corollary and the threshold analogue.”**

### 31. Appendix pages 20–25, terminology

Rename \(s_B\) the **net cut leg** throughout. Rename \(\widetilde s_B\) the **caught-only leg**. This is necessary in the statement, proof, and reading paragraphs.

### 32. Hypothesis (C-1), page 21

Correct:

> “which is standing condition (S11)”

to:

> “which is standing condition (S10).”

Then cite (S11) separately for fixed policies.

### 33. Appendix reading, page 25

Replace:

> “shortening the clock pulls the pooled sensitivity down only if what it takes out sat above the average”

with:

> “For the composition ratio, the net cut leg must lie between \(s_A\) and \(((2-\phi)/\phi)s_A\); for overall attenuation, it need only lie between \(0\) and \((2/\phi)s_A\). Thus the weight leg can permit overall attenuation even when the net cut leg is less sensitive than the original pool.”

This is the exact correction to the session headline’s “more than their share” claim.

### 34. End of the cut section, page 25

Insert the threshold analogue with rule-specific \(h^{(\tau)}\) and \(h^{(\tau')}\), followed by the certificate lemma reference. Do not claim that the clock corollary applies “verbatim.”

### 35. Cross-references throughout both PDFs

Inserting the Blackwell theorem and order-size proposition will change theorem numbering. Every hard-coded reference on main-paper pages 8–11 and appendix pages 1, 9, 13, and 20 must be regenerated from labels rather than manually renumbered.

No headline-driven changes are required in main-paper Section 6 or Appendix Lemmas 8–9.

---

# D. Testing decisions that are insufficient

The spec’s proof attack structure is sound in principle, but the proposed numerical checks are below the standard required for the claims “at every node,” “on an interval,” and “maximal.” In particular, it proposes a one-node independent recomputation for each new record and a certificate verdict recomputed from the stored coefficients. 

## 1. One-node recomputation does not support an every-node record

For both the certificate and regret records, independently checking one node cannot support:

- “reported at every node”;
- a maximum over nodes;
- a failure interval;
- a statement that survivor repricing dominates at every node.

At minimum, the independent checker must recompute:

- all claimed extrema;
- every node adjacent to a sign change;
- each interval endpoint;
- each node where a denominator or sensitivity is smallest;
- every node appearing in the paper.

For a modest grid, recomputing all nodes is preferable.

## 2. The polynomial certificate needs certified coefficients

Recomputing a polynomial verdict from the same floating-point coefficient vector only verifies evaluation code, not the underlying coefficients.

The record must carry, for every \(c_k\):

- a reproducible high-precision value;
- an absolute error enclosure;
- its source integrals or finite sums;
- the pricing-root and quadrature tolerances used;
- an independently computed enclosure or comparison.

Without coefficient enclosures, the result is a dense numerical check, not an interval certificate.

## 3. Critical-point completeness must be proved computationally

A generic floating-point root routine is not enough. The checker must establish that it found **all** real roots of \(\Psi'\) in the interval, including:

- repeated roots;
- roots close to endpoints;
- clustered roots;
- the case \(\Psi'\equiv0\);
- roots whose numerical enclosure overlaps the interval boundary.

A Sturm-sequence, interval-arithmetic, or equivalent certified root-isolation procedure is appropriate. Each endpoint and critical-point evaluation must carry an interval sign enclosure. If an enclosure contains zero, the verdict must be “undecided,” not PASS.

## 4. Composition and total sensitivity need separate certificates

The spec discusses “the composition condition” and then a low-liquidity interval where tightening raises noise sensitivity. Those are not the same claim.

The record must separately compute and certify:

\[
\Psi_C=L_{\mathrm{tight}}^2-L_{\mathrm{loose}}^2
\]
and
\[
\Psi_S=(1-\Omega_{\mathrm{tight}})^2L_{\mathrm{tight}}^2
-(1-\Omega_{\mathrm{loose}})^2L_{\mathrm{loose}}^2.
\]

A failure of \(\Psi_C\le0\) does not imply \(\Psi_S>0\).

## 5. The failure interval needs endpoint error bars

The reported low-liquidity interval must include:

- the defining polynomial;
- an isolating interval for every boundary root;
- the sign on every connected component;
- the rounding rule used in the paper;
- a guarantee that rounded endpoints do not extend the claim beyond the certified interval.

The paper should report something like “for every \(\kappa\in[\underline\kappa^+,\overline\kappa^-]\)” using inward-rounded certified endpoints.

## 6. The off-path belief floor must be propagated into the sign margin

The paper’s analytic representation uses exact positive-probability conditioning, while the computation assigns a reference belief to empty mark-path histories. The check must report:

- which histories receive the floor;
- their exact or bounded probability mass;
- the induced perturbation of every \(G(S)\) and \(c_k\);
- the resulting uniform perturbation bound for \(\Psi_C\) and \(\Psi_S\);
- the minimum certified sign margin.

A sentence saying the floor is “small” is insufficient. The perturbation bound must be strictly smaller than the sign margin on every claimed interval.

## 7. The cut identity should be checked in all three forms

At every reported node, independently verify:

\[
s_A-(1-\phi)s_{A\setminus B}-\phi s_B^{\mathrm{net}}=0,
\]
\[
s_B^{\mathrm{net}}
-\widetilde s_B
+\frac{1-\phi}{\phi}\delta=0,
\]
and the direct difference in weighted pooled contributions.

Report absolute and scale-adjusted residuals. Because \((1-\phi)/\phi\) can be large, also report a cancellation or condition measure. A tiny final residual can otherwise conceal two large, inaccurate components.

## 8. The derivative check needs an independent route

The stored certificate and cut legs should not be checked only by re-evaluating the same coefficient formula. At selected nodes, compare the polynomial derivative with an independent route, such as:

- high-precision symmetric finite differences with step-size stability;
- automatic differentiation through an independently coded expectation;
- direct differentiation of the finite history sum.

The tolerance must be stated relative to both the derivative scale and the claimed sign margin.

## 9. Calibration strictness and equivalence need their own record

The Blackwell proof can establish conditional strictness analytically, but the calibration claims require numerical evidence that:

- each stated \(T=5\) threshold cut has positive mass;
- the \(T=10\) threshold cuts are null up to a stated tolerance;
- the \(T=10\to5\) clock cut is positive rather than an equality case;
- the decoder condition holds on all newly flagged computational paths.

These applications should be labelled NUMERICAL even though the conditional theorem is PROVED.

## 10. The regret record is under-specified

Before computing regret, register:

- the frozen or recomputed belief convention;
- the price system used under each deviation;
- all off-path beliefs;
- the signal and node grids;
- whether the maximum is over all signals or only cutoff points;
- the utility normalization.

The independent check must recompute all three plan utilities at the reported maximizer and at every cutoff. It should also search between signal nodes. If no continuous-domain bound is supplied, the output field and paper must say `max_grid_regret`, not `maximal_regret`.

Because the analytic model uses the full signal line while the computation truncates at \(\pm6\sigma_s\), a global regret claim additionally needs a tail argument. Otherwise the maximization domain is the renormalized computational support.

## 11. The number guard is only a formatting guard

Testing whether every rendered string appears in the paper does not establish that:

- the number came from the correct field;
- the correct threshold pair or clock pair was attached to it;
- rounding was conservative;
- a stale number from another table happens to match.

The paper should render numbers through keyed TeX macros generated from the records. The test should assert the mapping
\[
\text{record key}\longrightarrow\text{TeX macro}\longrightarrow\text{specific claim location},
\]
not merely string presence.

## 12. Any post-attack proof edit must reopen the gate

The planned sequence attacks the proofs before the paper rewrite, then allows a referee pass and author fix. Any author fix that changes:

- a theorem’s state space;
- a hypothesis;
- strictness;
- a kernel;
- a polynomial definition;
- a proof step;

must trigger a new independent attack. Otherwise the final statement carrying PROVED is not the statement that passed the gate.

## 13. Hypothesis-number auditing must be substantive

The final label-and-compile check should verify more than the existence of labels. It must catch:

- the current S10/S11 error in (C-1);
- references to (S1)–(S11) after adding (S12);
- use of independence where only the old S1 is cited;
- claims of differentiability where a pooled cell is null;
- ratio statements where the denominator sensitivity is zero;
- accidental use of “prices” where only \(\Delta^{act}\) is proved;
- accidental use of “caught leg” for a net quantity.

With those changes, the new version can carry a clean three-tier message: **PROVED information dominance, PROVED accounting and certificate implications, and NUMERICAL reversal, repricing, strictness, and regret applications.**