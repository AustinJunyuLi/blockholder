# Blackwell order under a tighter disclosure rule

## 1. Statement

For a rule \(r=(\tau,T)\), let \(D_r^d\) indicate that the filing has landed by date
\(d\leq H\). Let \(r_+\) denote the tighter rule and \(r_-\) the looser rule. At date \(d\),
the tagged output is
\[
 Y_r^d=
 \begin{cases}
  (F,\mathsf S_{F,r}),&D_r^d=1,\\
  (P,\mathcal H_{r,d}^P),&D_r^d=0,
 \end{cases}
 \qquad
 \mathsf S_{F,r}=(B_r^F,Q_r^F,a=1).
\]
The pooled history is
\[
 \mathcal H_{r,d}^P=
 \bigl(X_0,\ldots,X_d;L_{r,0},\ldots,L_{r,d}\bigr),
 \qquad
 L_{r,e}=\mathbf 1\{\text{the filing has landed by }e\}.
\]
On a pooled path every \(L_{r,e}\) through date \(d\) is zero. Prices can be appended to either
output. They are pinned measurable functions of the displayed information and do not enlarge the
experiment.

The hypotheses are the standing conditions, stated here in full, and three added conditions.

1. **(S1) One probability space.** The primitive vector \((v,\varepsilon,\xi,z_{0:H})\)
   has a joint law on a finite product of Polish spaces, the noise marks take values in
   \(\{-\bar z,0,+\bar z\}\), and \(s=v+\varepsilon\).
2. **(S2) A finite menu and calendar.** The plan menu is finite, \(H<\infty\), and each
   compared window belongs to \(\{1,\ldots,H\}\).
3. **(S3) A cutoff selection map.** A Borel step function \(j(s)\) selects the plan.
4. **(S4) Monotone Voice paths and a clean start.** Voice stake paths are weakly increasing
   in the signal and the date. Also \(B_j(s,-1)=b_0\), with \(b_0<\tau\) at every compared
   threshold. Thus the threshold comparison has \(b_0<\tau'<\tau\).
5. **(S5) Legal-clock discipline.** Only Voice plans cross. The crossing date is the first
   date the stake reaches the threshold. A truthful filing lands at \(f=c+T\), and only at the
   disclosure node.
6. **(S6) The flag is public.** Every pooled history contains \(L_{r,e}\), and the date-\(d\)
   information set contains the pooled history through \(d\).
7. **(S7) No-feedback timing.** The executed path, order marks, terminal target, crossing and
   filing dates, filing stake, and flagged order are Borel functions of the plan and signal alone.
   Realised flow and prices do not enter them. Write \(m_d(\theta)\) for the common strategic
   order mark at date \(d\).
8. **(S8) A bounded, pinned kernel.** The premium kernel is \(h=\pi p\), with
   \(\pi=\Pr(a=1\mid\mathcal I)\), \(p\in(0,1)\) continuous in the posterior and price, and
   the pricing rule pins a version of each conditional expectation.
9. **(S9) A finite wedge.** \(0<\Delta_m<\infty\) and
   \(\Delta_{\rm act}=\Delta_m\mathbb E[h(\mathcal I_H)]\).
10. **(S10) Liquidity enters in one place.** The value of \(\kappa\) changes only the law of
    the ternary noise mark.
11. **(S11) Fixed policies.** The menu, cutoff vector, and execution policies are common to
    the two rules and are not re-optimised with \(\kappa\).
12. **(S12) A common noise channel.** The vector \(z_{0:H}\) is independent of
    \((v,\varepsilon,\xi)\) and has the common rule-invariant law \(Q_\kappa\). Pooled flow is
    \(X_d=m_d(\theta)+z_d\). In the order-size-two model the noise marks are independent across
    dates and have probabilities \((\kappa/2,1-\kappa,\kappa/2)\).
13. **(S13) The control-node convention.** On the flagged cell the information set is exactly
    \(\sigma(\mathsf S_{F,r})\), up to pinned price coordinates. On the pooled cell it is
    exactly the displayed public pooled history, again up to pinned prices. The same convention
    applies at each depth \(d\).
14. **(S14) Identified flagged types.** On the tighter rule's flagged signal region, the
    composed terminal target
    \[
       g(s)=b^*_{j(s)}(s)
    \]
    is strictly increasing and
    \(B_{r_+}^F+Q_{r_+}^F=g(s)\). Pointwise strict increase gives a pointwise experiment
    comparison. Strict increase outside a prior-null set gives the same comparison modulo that
    null set and is enough for all posterior conclusions below.

**Theorem.** Fix a common \(\kappa\in[0,1]\). Suppose (S1) to (S14) hold. Compare either
\[
 \tau'<\tau\quad\text{at a common }T,
 \qquad r_+=(\tau',T),\quad r_-=(\tau,T),
\]
with \(b_0<\tau'<\tau\), or
\[
 T'<T\quad\text{at a common }\tau,
 \qquad r_+=(\tau,T'),\quad r_-=(\tau,T).
\]
For every \(d\leq H\), the tighter experiment is Blackwell more informative about
\(\theta=(j(s),s)\). In particular, there is a Markov kernel \(K_d\), independent of the type,
such that
\[
 \mathcal L(Y_{r_-}^d\mid\theta)
 =\int K_d(y,\mathord\cdot)\,
       \mathcal L(Y_{r_+}^d\in \mathrm dy\mid\theta).
\]
No positive-mass condition on either cell is needed. The result includes \(\kappa=0\),
\(\kappa=1\), and the corner \(T=H\). The noise law remains a probability law at both liquidity
endpoints, and nestedness of the filing events does not use an interior window or an interior cell
mass.


Condition (S14) is a transparent sufficient condition, not the logically weakest one. The minimal
replacement is a measurable fiber condition: on each tighter flagged-tuple fiber, the looser-output
channel must factor through that tuple by one type-independent kernel. A measurable decoder supplies
such a factorisation because every fiber is a singleton. Strict monotonicity supplies the decoder in
the paper's model.

The theorem is formally about \(\theta\). It gives the same Blackwell order for the price-relevant
state \((v,a)\). The reason is specific to this model. The engagement flag is a function of
\(\theta\), the conditional law of \(v\) given \(\theta\) is rule-invariant, and, by (S7) and
(S12), both rule outputs are conditionally independent of \(v\) given \(\theta\). Thus the same
kernel also maps the tighter conditional channel given \((v,a)\) into the looser one. Equivalently,
for any posterior \(\nu\) over types,
\[
 \pi(\nu)=\mathbb E_\nu[a(\theta)],
 \qquad
 \widehat v(\nu)=\mathbb E_\nu[\mathbb E(v\mid\theta)],
\]
so the pair used by the price is a linear image of the type posterior. The two state spaces are not
literally identical. Their information ordering agrees here.

The conditions carry the argument as follows.

| Condition | Use |
|---|---|
| (S1) | Gives standard Borel output spaces, measurable conditional laws, and a measurable garbling kernel. |
| (S2) | Makes dates and tagged histories finite and permits the same construction at every \(d\leq H\). |
| (S3) | Makes the plan a measurable function of the recovered signal. |
| (S4), (S5) | Give first-crossing dates and the nesting of filing events at both margins. |
| (S6) | Makes the cell tag observable and makes the public flag coordinates agree on common pooled paths. |
| (S7) | Makes the path and marks common across rules and functions of \(\theta\), so common pooled histories agree. |
| (S8) | Makes appended prices functions of the output. Its kernel content is used in the premium corollary, not in the Blackwell order itself. |
| (S9) | Fixes the sign and scale in the premium corollary. It is not used in the Blackwell order itself. |
| (S10), (S12) | Supply the same type-independent noise channel at the common \(\kappa\), which the kernel redraws. |
| (S11) | Keeps the type-to-path map common when the rule changes. |
| (S13) | States the exact experiment being compared. |
| (S14) | Recovers \(s\), hence \(j(s)\) and \(\theta\), from every tighter flagged output. |

Three corollaries follow.

1. **Posterior variance of engagement.** Under (S1) to (S7) and (S10) to (S14),
   \[
      \mathbb E\!\left[\operatorname{Var}(a\mid\mathcal I_{H,r_+})\right]
      \leq
      \mathbb E\!\left[\operatorname{Var}(a\mid\mathcal I_{H,r_-})\right].
   \]
   More generally, the same inequality holds for every square-integrable function of the type.
2. **Expected premium under curvature.** Assume in addition (S8), (S9),
   \(\mathbb E|v|<\infty\), and equation (g-kernel),
   \(h(\nu)=\mathsf h(\pi(\nu),\widehat v(\nu))\). For \(r\in\{r_+,r_-\}\), define
   \[
      Z_r=\bigl(\Pr(a=1\mid\mathcal I_{H,r}),
                 \mathbb E[v\mid\mathcal I_{H,r}]\bigr)
   \]
   and define the exact curvature set by
   \[
      \mathcal K=
      \overline{\operatorname{co}}\!\left(
        \operatorname{essran} Z_{r_+}\ \cup\
        \operatorname{essran} Z_{r_-}
      \right).
   \]
   Here the closure is part of the definition, so conditional barycentres remain in the set.
   If \(\mathsf h\) is convex on \(\mathcal K\), then
   \[
       \Delta_{\rm act}(r_+)\geq\Delta_{\rm act}(r_-).
   \]
   If it is concave there, the inequality reverses. Every flagged posterior point that occurs with positive probability is in the curvature set.
   More precisely, for prior-almost every signal flagged by rule \(r\),
   \[
      Z_r=\bigl(1,\mathbb E[v\mid s]\bigr).
   \]
   When the flagged cell has positive mass, these \(\pi=1\) points belong to
   \(\operatorname{essran}Z_r\) or its closure and hence to \(\mathcal K\). When its mass is zero,
   no flagged point enters the expected premium. A curvature check that covers only pooled posterior
   pairs is not enough when a flagged cell has positive mass.
3. **Depth and liquidity composition.** Under the date-\(d\) form of (S13), the same Blackwell
   order holds at every \(d\leq H\). If Lemma g2 is also applied to the full tagged experiment,
   using its pooled garbling and the identity map on the flagged cell, then for
   \(0<\kappa_L<\kappa_H<1\),
   \[
      \mathcal E_{r_+}(\kappa_L)
      \succeq_B \mathcal E_{r_+}(\kappa_H)
      \succeq_B \mathcal E_{r_-}(\kappa_H),
   \]
   and also
   \[
      \mathcal E_{r_+}(\kappa_L)
      \succeq_B \mathcal E_{r_-}(\kappa_L)
      \succeq_B \mathcal E_{r_-}(\kappa_H).
   \]
   Thus a tighter rule at lower liquidity intensity dominates a looser rule at higher intensity.
   A tighter rule at higher \(\kappa\) and a looser rule at lower \(\kappa\) have no general
   order. A three-type example below makes the non-order explicit.

## 2. Proof and boundaries

### Nested cells

For either margin, a filing event is a type event by (S7). At the threshold margin, the first
crossing of \(\tau'<\tau\) occurs no later than the first crossing of \(\tau\). Hence
\[
 D_{(\tau,T)}^d(\theta)=1\quad\Longrightarrow\quad
 D_{(\tau',T)}^d(\theta)=1.
\]
At the clock margin, \(c(\theta;\tau)+T\leq d\) implies
\(c(\theta;\tau)+T'\leq d\) when \(T'<T\). Therefore, at either margin,
\[
 \mathcal C_{F,r_-}^d\subseteq\mathcal C_{F,r_+}^d,
 \qquad
 \mathcal C_{P,r_+}^d\subseteq\mathcal C_{P,r_-}^d.
\]
This is the nesting used in `lem:threshold-weight` and the weight leg of `thm:clock`, now read at
an arbitrary depth.

### Recovery on the tighter flagged cell

On \(\mathcal C_{F,r_+}^d\), the observed first two coordinates satisfy
\[
 B_{r_+}^F+Q_{r_+}^F=g(s).
\]
By (S14), this sum has a measurable inverse \(\iota_+\) on its image. Thus
\[
 s=\iota_+(B_{r_+}^F+Q_{r_+}^F),
 \qquad
 \theta=\bigl(j(s),s\bigr).
\]
This is the strictly increasing composed-terminal-target hypothesis carried by
`lem:flagged-kappa-free`. It does the main work. Truthful revelation of \(B^F\) alone would not
suffice. The flagged order \(Q^F\) and the accounting identity for their sum are needed.

### The garbling kernel

The output space is a disjoint union of the flagged-tuple space and the pooled-history space.
Define \(K_d\) on a tighter output \(y\) as follows.

* If \(y=(P,\mathfrak h)\), retain the core history and set \(K_d(y,\cdot)=\delta_{(P,\mathfrak h)}\). If prices are recorded, discard the tighter price coordinates and append the pinned looser price functions of \(\mathfrak h\).
* If \(y=(F,\mathsf s_F)\), recover \(\widehat\theta\) with \(\iota_+\). If
  \(D_{r_-}^d(\widehat\theta)=1\), emit the deterministic looser flagged tuple
  \((F,\mathsf S_{F,r_-}(\widehat\theta))\).
* If \(y=(F,\mathsf s_F)\) and \(D_{r_-}^d(\widehat\theta)=0\), draw a fresh
  \(z'_{0:d}\sim Q_\kappa\) and emit the looser pooled history
  \[
    \left(P,
      \bigl(m_0(\widehat\theta)+z'_0,\ldots,
            m_d(\widehat\theta)+z'_d;0,\ldots,0\bigr)
    \right).
  \]
  Append the pinned looser prices if the output convention records them.

Every branch reads only \(y\). It never reads the true type. The inverse is measurable by strict
monotonicity. The disclosure test, flagged tuple, and order marks are measurable functions of the
recovered type. The last branch uses a fixed probability law. Define the kernel arbitrarily at
flagged tuples outside the actual tighter image. Thus \(K_d\) is a Markov kernel on the whole
output space.

Fix a type. If it is pooled under the tighter rule, nestedness says it is pooled under the looser
rule. By (S6), (S7), and (S11), the two histories then have the same order flows and the same
all-zero flag coordinates. The first branch is exact for the core history. Recomputing any recorded prices with the looser rule preserves exactness. If the type is flagged under both rules,
the second branch returns its looser tuple. If the tighter rule newly flags it, the third branch
uses its recovered mark path and an independent draw from the same \(Q_\kappa\) that generates the
looser pooled experiment. Its output therefore has exactly the looser conditional law. These cases
prove the displayed Blackwell identity.

The actual control-node information set on a flagged path contains the flagged tuple, not the
pre-filing pooled history. That omitted history does not weaken the claim. Steps 3 to 9 of
`lem:flagged-kappa-free` show that the tuple pins the signal and that the pre-filing history is
conditionally independent of \((v,s,\xi)\) given the tuple. The kernel can redraw all noise needed
for the looser path. If an alternative convention retained the pre-filing history on flagged paths, the order still
follows, but the kernel needs one extra step. On a tighter flagged output it recovers the type,
discards the observed pre-filing noise, redraws \(Q_\kappa\), and appends the lower rule's simulated
pre-filing history whether the lower output is flagged or pooled. Merely projecting and emitting a
bare lower flagged tuple would not reproduce that richer output convention.

### Posterior corollaries

Use \(K_H\) to couple the two outputs so that
\((v,a,\theta)\), \(Y_{r_+}^H\), and \(Y_{r_-}^H\) form a Markov chain in that order. Put
\(M_r=\mathbb E[a\mid Y_r^H]\). Then
\[
 M_{r_-}=\mathbb E[M_{r_+}\mid Y_{r_-}^H].
\]
The conditional variance identity gives
\[
 \mathbb E\operatorname{Var}(a\mid Y_{r_-}^H)
 -\mathbb E\operatorname{Var}(a\mid Y_{r_+}^H)
 =\mathbb E\operatorname{Var}(M_{r_+}\mid Y_{r_-}^H)\geq0.
\]
Replacing \(a\) by any square-integrable function of \(\theta\) proves the stated extension.

For the premium corollary, the same tower property gives
\[
 Z_{r_-}=\mathbb E[Z_{r_+}\mid Y_{r_-}^H].
\]
Conditional Jensen on \(\mathcal K\) yields
\(\mathbb E\mathsf h(Z_{r_-})\leq\mathbb E\mathsf h(Z_{r_+})\) under convexity. Multiplication by
\(\Delta_m>0\) preserves the inequality. Concavity reverses the Jensen step. This is the same
posterior-martingale step used in Lemma g3(c), but the hull here contains the cells of both full
experiments, including their flagged points.

### Why the opposite cross-comparison has no order

A three-type experiment gives a direct check. Let types \(A\), \(B\), and \(C\) have positive
prior mass. The looser rule pools all three. The tighter rule newly flags \(A\) and continues to
pool \(B\) and \(C\). Choose \(A\) and \(B\) to have the same coarsened mark path, and choose
\(C\) to differ from them in one round. Such paths are allowed because the order coarsening need
not reveal the size of every stake increment. At \(\kappa_L=0\), the looser flow reveals the mark
path exactly. It separates \(C\) from \(\{A,B\}\), but it cannot separate \(A\) from \(B\). At
\(\kappa_H=1\), the tighter rule separates \(A\) from \(B\) by the cell tag. It does not perfectly
separate \(B\) from \(C\), because an active and an idle round both produce flow \(+\bar z\) with
positive probability. The looser experiment cannot simulate the tighter rule's \(A\)-versus-\(B\)
separation, and the tighter experiment cannot simulate the looser rule's exact \(B\)-versus-\(C\)
separation. The two cross-experiments are Blackwell incomparable.

### Why identification cannot be dropped without a fiber condition

The conclusion is not guaranteed when the flagged tuple fails to identify the type, even when
no-feedback timing holds. Here is a two-type clock example. Let \(H=2\), \(b_0=0\), \(\tau=1\), \(T'=1\), and \(T=2\). Both types choose Voice and
have signals \(s_L<s_U\), each with prior probability one half. Their stake paths at dates
\((-1,0,1,2)\) are
\[
 B_L=(0,0,1,2),
 \qquad
 B_U=(0,1/2,1,2).
\]
They are weakly increasing in the date and in the signal. Both cross at date 1. Under the shorter
clock both file at date 2 and produce the same flagged tuple
\[
 (B^F,Q^F,a)=(2,0,1).
\]
The terminal target is constant at 2, so (S14) fails.

Let the binary order coarsening be
\(m_d=2\bar z\,\mathbf 1\{B(d)-B(d-1)\geq3/4\}\). The two mark paths are
\[
 m_L=(0,2\bar z,2\bar z),
 \qquad
 m_U=(0,0,2\bar z).
\]
Under the longer clock both types remain pooled because their filing date would be 3. Its date-1
flow has different conditional laws for the two types. At any \(\kappa\in[0,1]\), an active mark
and an idle mark have different flow distributions. The tighter output is the same constant tuple
under both types. A type-independent kernel applied to that constant must have the same output law
under both types, so it cannot reproduce the looser experiment. This example satisfies the nested
clock and monotone-path conditions. The flagged fiber contains two types with different looser-output laws, so neither a decoder nor the weaker fiberwise kernel exists.

No-feedback timing has a separate role. Without (S7), the disclosure rule can change prices, those
prices can change later orders, and the type-to-path map need not be common across rules. The
identity branch on the common pooled set then fails. The filing event and terminal target may also
depend on realised flow rather than on \(\theta\). Nothing in the remaining conditions rules out a
feedback system whose tighter pooled channel is constant while its looser pooled channel separates
two types. The Blackwell order therefore needs either no feedback or a direct replacement
hypothesis that supplies nested cell events and a garbling on the common pooled region.

### What the theorem does not give

The theorem does not sign the noise sensitivity \(\mathcal S\) or the pooled sensitivity
\(\mathcal S_P\). It orders two level experiments at one common \(\kappa\). Even under convexity,
a pointwise order of expected premiums does not order the absolute derivatives of those premiums
with respect to \(\kappa\). The pooled experiments also use different conditional type laws because
tightening changes who remains in the pool. Their sensitivities still require the weight and
composition analysis.

Once nestedness and (S14) are in hand, the kernel is short. Those inputs are not automatic. The two
information sets are not nested as sigma-algebras because a newly flagged path replaces a pooled
history with a different tuple. The strict target turns that replacement into full type revelation,
which makes simulation possible. The public flag and no-feedback timing make the common pooled
branch identical. This is the content. The theorem fits as the structural link in the two-dial
framing, not as a quantitative headline.

## 3. Calibration computation

No script or model evaluation is needed. The calibration supplies an exact analytic certificate:
`numerical_v4/menu.py` defines
\[
 b^{*\prime}(s)=
 \frac{\bar b-b_0}{2\sigma_s}
 \left(1+\left(\frac{s-\mu_v}{\sigma_s}\right)^2\right)^{-3/2}>0
\]
when \(\bar b>b_0\) and \(\sigma_s>0\). The same file defines
\(Q^F=b^*(s)-B^F\), so \(B^F+Q^F=b^*(s)\) exactly. `legal_clock` computes the first crossing and
\(f=c+T\). These are algebraic facts, so there is no numerical tolerance to set. A floating-point
check would be weaker than the source formula.

## 4. Cost of carrying the result into the paper

The result would add one theorem and its three corollaries after the partition and flagged-cell
information result. Its proof uses `lem:partition`, the information recovery in
`lem:flagged-kappa-free`, clause (i) of `lem:threshold-weight`, and the nested-cell step in
`thm:clock`. The curvature corollary cites equation (g-kernel) and the Jensen method of Lemma g3(c).
No numerical record or figure changes.

The main text could use one paragraph to state the rule-level information order before it turns to
\(\kappa\)-sensitivity. The appendix would carry the kernel and the necessity example. The threshold
and clock sensitivity theorems do not move and their labels do not change. After an independent
attack gate, the new theorem would support a PROVED label. This memo does not award that label.

## 5. Result

```json
{"status":"PASS","summary":"Under nested filing events, no-feedback timing, the exact tagged information convention, and a strictly increasing composed terminal target on the tighter flagged region, an explicit type-independent kernel maps every tighter output into the looser output. The result extends to every depth, both liquidity endpoints, and T = H.","files_changed":[".scratch/v5-paper/hunt/3-blackwell-tightening/memo.md"],"evidence":"The kernel is the identity on common pooled core histories. On a tighter flagged output it recovers the type from B^F+Q^F, then emits the looser flagged tuple or redraws the looser pooled noise channel. A two-type clock example shows the order can fail when the target is not injective."}
```
