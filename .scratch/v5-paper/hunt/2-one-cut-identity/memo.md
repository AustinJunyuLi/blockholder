# One cut identity for both dials

## 1. Statement

### Standing hypotheses

Both parts use the standing conditions from the partition subsection.

1. **(S1) One probability space.** The primitive vector has a joint law on a finite product of Polish spaces. The signal is $s=v+\varepsilon$, and each noise mark lies in $\{-\bar z,0,+\bar z\}$.
2. **(S2) A finite menu and calendar.** The plan menu is finite, $H<\infty$, and $T\in\{1,\ldots,H\}$.
3. **(S3) A cutoff selection map.** A step function with finitely many breakpoints maps the signal into a plan.
4. **(S4) Monotone Voice paths and a clean start.** Each plan has $B_j(s,-1)=b_0$. Voice paths are weakly increasing in the signal and in the date. The clean-start inequality for the pair appears in (C$\tau$-1).
5. **(S5) Legal-clock discipline.** Only Voice plans cross. The crossing date is the first date at which the stake reaches the threshold. A filing lands at $c_j+T$ through the disclosure node and reports the stake truthfully.
6. **(S6) The flag is public.** A pooled history records whether the filing has landed by each date, and the control-node information set contains the pooled history.
7. **(S7) No-feedback timing.** The executed path, order marks, terminal target, crossing date, filing date, filing stake, and flagged order depend only on the plan and signal. They do not depend on realised order flow or prices.
8. **(S8) A bounded, pinned kernel.** The kernel is $h(\mathcal I)=\pi(\mathcal I)p(\mathcal I)$. The pricing rule pins a version at every information set. The entry probability is continuous in the posterior and price.
9. **(S9) A finite positive wedge.** $0<\Delta_m<\infty$ and $\Delta^{\rm act}=\Delta_m\mathbb E[h(\mathcal I_H)]$.
10. **(S10) Liquidity enters once.** $\kappa$ enters the primitives only through the ternary noise law. The laws of $v$, the signal noise, and the bidder draw do not depend on $\kappa$.
11. **(S11) Fixed policies.** The menu, execution policies, and cutoff vector are held fixed in $\kappa$ and across the two rules.

The following hypotheses are the threshold analogues of (C-1) to (C-3).

1. **(C$\tau$-1) A fixed threshold cut.** Fix a common $T$ and $\kappa$ and compare $b_0<\tau'<\tau$. The tighter rule is $(\tau',T)$. Conditions (S4), (S5), and (S7) make both disclosure indicators functions of the same plan and signal. Conditions (S10) and (S11) hold throughout the liquidity comparison.
2. **(C$\tau$-2) Differentiability and pinned versions.** The maps
   
   $$
   \kappa\longmapsto \mathbb E[h^{(\tau)}\mid A]
   \quad\text{and}\quad
   \kappa\longmapsto \mathbb E[h^{(\tau')}\mid A\setminus B]
   $$
   
   are differentiable at the compared $\kappa$. The superscript identifies the information set supplied by that rule. Condition (S8) pins both kernels. For the optional split of the caught leg, $\mathbb E[h^{(\tau)}\mid B]$ is also differentiable.
3. **(C$\tau$-3) Non-degeneracy and factorisation.** $0<\Pr(B)<\Pr(A)$, $0<\Omega(\tau,T)$, $\Omega(\tau',T)<1$, and
   
   $$
   s_A:=\partial_\kappa\mathbb E[h^{(\tau)}\mid A]\ne0.
   $$
   
   The hypotheses of Proposition `prop:factorisation`, including flagged-endpoint invariance, hold at both thresholds whenever the aggregate criterion is invoked.
4. **(C$\tau$-4) Erasure representation.** Only the identification with Condition D and Part 2 require order size two and $\kappa\in(0,1)$, so that Lemmas g1 to g3 apply. Parts (i) to (vi) of the cut result do not require this clause.

Set

$$
A=\mathcal C_P(\tau,T),\qquad
B=\mathcal C_F(\tau',T)\setminus\mathcal C_F(\tau,T),\qquad
\varphi=\frac{\Pr(B)}{\Pr(A)}.
$$

Define

$$
\begin{aligned}
s_{A\setminus B}
  &=\partial_\kappa\mathbb E[h^{(\tau')}\mid A\setminus B],\\
\widetilde s_B
  &=\partial_\kappa\mathbb E[h^{(\tau)}\mid B],\\
\delta
  &=\partial_\kappa\mathbb E[h^{(\tau')}-h^{(\tau)}\mid A\setminus B],
\end{aligned}
$$

and define the caught leg by

$$
 s_B:=\frac{1}{\Pr(B)}\partial_\kappa\left(
 \mathbb E[h^{(\tau)}\mathbf 1_A]
 -\mathbb E[h^{(\tau')}\mathbf 1_{A\setminus B}]
 \right). \tag{1}
$$

This $s_B$ includes the re-pricing of the histories that remain pooled.

### Part 1: threshold cut corollary

**Status: PASS.** Under (S1) to (S11) and (C$\tau$-1) to (C$\tau$-3), the who-gets-caught corollary holds at the threshold margin as follows.

1. **Nestedness.**
   
   $$
   \mathcal C_F(\tau,T)\subseteq\mathcal C_F(\tau',T),\qquad
   B\subseteq A,\qquad
   A\setminus B=\mathcal C_P(\tau',T).
   $$
   
   Also $\varphi\in(0,1)$ and
   
   $$
   W_\tau=\frac{1-\Omega(\tau',T)}{1-\Omega(\tau,T)}=1-\varphi\le1. \tag{2}
   $$
2. **Kappa-free masses.** $\partial_\kappa\Pr(A)=\partial_\kappa\Pr(B)=0$, so $\varphi$ does not depend on $\kappa$.
3. **Cut identity.**
   
   $$
   \begin{aligned}
   s_{A\setminus B}
   &=\frac{\Pr(A)s_A-\Pr(B)s_B}{\Pr(A)-\Pr(B)}\\
   &=\frac{s_A-\varphi s_B}{1-\varphi}\\
   &=\frac{s_A-\varphi\widetilde s_B}{1-\varphi}+\delta, \tag{3}
   \end{aligned}
   $$
   
   where the last line uses the extra differentiability in (C$\tau$-2). Equivalently,
   
   $$
   s_A=(1-\varphi)s_{A\setminus B}+\varphi s_B,
   \qquad
   s_B=\widetilde s_B-\frac{1-\varphi}{\varphi}\delta. \tag{4}
   $$
4. **Composition ratio.**
   
   $$
   C_\tau=\frac{|s_A-\varphi s_B|}{(1-\varphi)|s_A|}, \tag{5}
   $$
   
   and
   
   $$
   C_\tau\le1
   \quad\Longleftrightarrow\quad
   (s_B-s_A)\bigl(\varphi s_B-(2-\varphi)s_A\bigr)\le0. \tag{6}
   $$
   
   Thus $C_\tau\le1$ exactly when $s_B$ lies weakly between $s_A$ and $((2-\varphi)/\varphi)s_A$. Under (C$\tau$-4), Lemma g3 gives $\mathcal S_P=(\Delta_m/2)|\mathcal W|$, so Condition D is equivalent to (6).
5. **Aggregate criterion.**
   
   $$
   W_\tau C_\tau=\frac{|s_A-\varphi s_B|}{|s_A|}, \tag{7}
   $$
   
   and
   
   $$
   W_\tau C_\tau\le1
   \quad\Longleftrightarrow\quad
   s_B(2s_A-\varphi s_B)\ge0. \tag{8}
   $$
   
   This is equivalent to $s_B$ lying weakly between $0$ and $(2/\varphi)s_A$. With the factorisation hypotheses in (C$\tau$-3), (8) is also equivalent to the tighter threshold weakly lowering the aggregate liquidity sensitivity.
6. **Readings.** Let $\rho=s_B/s_A$.
   
   a. If $s_As_B\le0$, including $s_B=0$, then $C_\tau>1$.
   
   b. If $s_As_B>0$, then $C_\tau\le1$ if and only if
   
   $$
   |s_A|\le|s_B|\le\frac{2-\varphi}{\varphi}|s_A|.
   $$
   
   c. If $s_{A\setminus B}s_A\ge0$, then $C_\tau\le1$ if and only if $\rho\ge1$. Under the common sign this says $|s_B|\ge|s_A|$. Under that same sign, the proviso itself is $|s_B|\le|s_A|/\varphi$.
   
   d. $W_\tau C_\tau\le1$ if and only if $s_B$ has the sign of $s_A$ or is zero, and $|s_B|\le(2/\varphi)|s_A|$.
   
   e. The upper limits $(2-\varphi)/\varphi$ and $2/\varphi$ fall as $\varphi$ rises and diverge as $\varphi\downarrow0$. If $M\ge1$, $\varphi\le2/(1+M)$, and $|s_B|\le M|s_A|$, the upper limits are slack. The composition condition then asks for a common sign and $|s_B|\ge|s_A|$. The aggregate condition asks only for a common sign or $s_B=0$.

The threshold version needs one clean-start clause that the clock comparison does not: $b_0<\tau'$. It puts the first-passage and clock equivalence in force at the tighter threshold as well as at $\tau$. Order size two is not needed for the cut algebra. It is needed only to call the resulting band Condition D through Lemma g3.

### Part 2: a single-crossing revelation certificate

**Status: PASS for the implication, with a numerical calibration check.** Inherit Part 1 and (C$\tau$-4). Write

$$
c^A_k=c_k(\tau,T),\qquad
c^R_k=c_k(\tau',T),\qquad
d_k=c^R_k-c^A_k,
$$

where $R=A\setminus B$ is the pool that remains under the tighter threshold. These are the kappa-free coefficients of Lemma g3. For any vector $v=(v_0,\ldots,v_H)$ define its reversed polynomial

$$
P_v(x)=\sum_{k=0}^H v_kx^{H-k},
\qquad
x=x(\kappa):=\frac{\kappa}{2-\kappa}. \tag{9}
$$

Add the following hypotheses.

1. **(R1) One crossing for each pooled cell.** After coefficients with value zero are deleted, both sequences $(c^A_0,\ldots,c^A_H)$ and $(c^R_0,\ldots,c^R_H)$ change sign exactly once, from negative to positive. Their first and last coefficients are strictly negative and strictly positive, respectively.
2. **(R2) One crossing for the survivor difference.** After zeros are deleted, $(d_0,\ldots,d_H)$ changes sign exactly once, from positive to negative. Its first and last coefficients are strictly positive and strictly negative, respectively.
3. **(R3) Liquidity is above the three revelation roots.** Let $r_A,r_R,r_D$ be the unique positive roots of $P_{c^A}$, $P_{c^R}$, and $P_d$. Then
   
   $$
   x(\kappa)\ge r_*:=\max\{r_A,r_R,r_D\}. \tag{10}
   $$

Under (R1) to (R3),

$$
0\le s_{A\setminus B}\le s_A,
$$

and the caught leg satisfies the stronger bounds

$$
s_A\le s_B\le\frac{s_A}{\varphi}
<\frac{2-\varphi}{\varphi}s_A. \tag{11}
$$

The strict last inequality uses $s_A>0$, which follows from (C$\tau$-3) and the displayed slope order. Hence the band condition and $C_\tau\le1$ hold. This condition says that more erasure raises the pooled premium in both pools, while the pool that survives the tighter rule is weakly less sensitive to that erasure. The cut identity assigns the missing sensitivity to the premium mass removed by the tighter threshold. That caught leg includes survivor re-pricing. It is more noise-sensitive than the original pool, but not enough to reverse the survivor sensitivity.

Once the common slope direction is known, the difference-root clause is algebraically the same order that Condition D tests. The certificate is therefore an interval certificate on kappa-free objects, not a deeper shape restriction on the kernel. Its gain is that three one-crossing sign lists reduce a continuum of liquidity comparisons to one root cutoff. The roots also locate why the below-grid pair fails.

At the frozen calibration, the certificate holds on the full continuous interval $\kappa\in[0.15,0.85]$ for each of the four non-null $T=5$ pairs. The table reports each root after conversion to the $\kappa$ scale:

| threshold quantiles $q\to q'$ | $\kappa(r_A)$ | $\kappa(r_R)$ | $\kappa(r_D)$ | $\kappa_*$ |
|---|---:|---:|---:|---:|
| $0.9\to0.7$ | 0.048670563 | 0.108569232 | 0.028758461 | 0.108569232 |
| $0.7\to0.5$ | 0.108569232 | 0.145962695 | 0.094456809 | 0.145962695 |
| $0.5\to0.3$ | 0.145962695 | 0.126033933 | 0.149012173 | 0.149012173 |
| $0.3\to0.1$ | 0.126033933 | 0.091805343 | 0.133523094 | 0.133523094 |

The smallest gap between a cutoff and the grid's lower endpoint is $0.15-0.149012173=0.000987827$. The $0.5\to0.3$ cutoff also separates the reported failure interval. On $[0.1440,0.145962695)$ the two pooled slopes do not have the required common direction. At $0.145962695$ the original-pool slope is zero, so the ratio is undefined. On $(0.145962695,0.149012173)$ both slopes have the same direction, but the survivor is more sensitive than the original pool. The reported failure endpoint $0.1485$ is below the certificate cutoff. At $T=10$ all four cuts are null: the reclassified mass is zero and the paired coefficient vectors are identical. Thus $C_\tau=1$ wherever their common sensitivity is nonzero, including every recorded grid node. The ratio is undefined at a zero of that common sensitivity. The caught share and caught leg are not defined for these null cuts.

## 2. Proof

### Part 1

For each threshold, the clock equivalence from (S4), (S5), and the clean start gives

$$
D(\tau,T)=\mathbf 1\{a=1\}\mathbf 1\{B(s,H-T)\ge\tau\}.
$$

If $D(\tau,T)=1$, then the same path satisfies $B(s,H-T)\ge\tau>\tau'$, so $D(\tau',T)=1$. This proves the flagged-set inclusion. Taking complements gives $A\setminus B=\mathcal C_P(\tau',T)$. The mass identities then give (2). The strict inequalities in (C$\tau$-3) give $0<\varphi<1$.

By (S7), both disclosure indicators are functions of the plan and signal. By (S10), $\kappa$ moves only the order-flow noise. By (S11), neither the cutoff selection nor the executed paths move with it. Thus $A$, $B$, and their probabilities do not move with $\kappa$. This proves part 1(ii).

Let

$$
\Lambda_\tau=\mathbb E[h^{(\tau)}\mathbf1_A],
\qquad
\Lambda_{\tau'}=\mathbb E[h^{(\tau')}\mathbf1_{A\setminus B}].
$$

The kappa-free masses and (C$\tau$-2) imply

$$
\partial_\kappa\Lambda_\tau=\Pr(A)s_A,
\qquad
\partial_\kappa\Lambda_{\tau'}=
(\Pr(A)-\Pr(B))s_{A\setminus B}.
$$

Definition (1) therefore gives

$$
\Pr(B)s_B=\Pr(A)s_A-(\Pr(A)-\Pr(B))s_{A\setminus B}.
$$

Solving and dividing by $\Pr(A)>0$ proves the first two lines of (3) and the average identity in (4).

For the split, use $\mathbf1_A=\mathbf1_B+\mathbf1_{A\setminus B}$:

$$
\begin{aligned}
\Lambda_\tau-\Lambda_{\tau'}
&=\Pr(B)\mathbb E[h^{(\tau)}\mid B]\\
&\quad-\Pr(A\setminus B)
\mathbb E[h^{(\tau')}-h^{(\tau)}\mid A\setminus B].
\end{aligned}
$$

Differentiate and divide by $\Pr(B)$. This gives the second identity in (4), and substitution gives the last line of (3). Notice that the second term uses the two rules' own kernels. It is the survivor re-pricing term.

By (S9),

$$
\mathcal S_P(\kappa,\tau,T)=\Delta_m|s_A|,
\qquad
\mathcal S_P(\kappa,\tau',T)=\Delta_m|s_{A\setminus B}|.
$$

Use (3) and $1-\varphi>0$ to obtain (5). To test $C_\tau\le1$, square its two nonnegative sides. Put $u=s_A-\varphi s_B$ and $w=(1-\varphi)s_A$. Then

$$
u^2-w^2
=\varphi(s_A-s_B)((2-\varphi)s_A-\varphi s_B).
$$

Since $\varphi>0$, this is nonpositive exactly when $s_B$ lies between the two roots $s_A$ and $((2-\varphi)/\varphi)s_A$. This proves (6). Under (C$\tau$-4), Lemma g3 gives the exact derivative formula at both thresholds. Condition D compares the corresponding absolute revelation values, so it is equivalent to $C_\tau\le1$.

Multiplying (5) by (2) gives (7). Squaring the two sides of (7) yields

$$
(s_A-\varphi s_B)^2-s_A^2
=-\varphi s_B(2s_A-\varphi s_B).
$$

This proves (8). Proposition `prop:factorisation` at both thresholds turns the left side of (7) into the aggregate sensitivity ratio, as claimed.

For the readings, the two roots in (6) are nonzero and have the sign of $s_A$. A value with the opposite sign, or zero, lies strictly outside their interval. Under a common sign, divide the two endpoints and $s_B$ by $s_A$. If $s_A<0$, their order reverses. In either case the image interval is $1\le\rho\le(2-\varphi)/\varphi$. If $s_{A\setminus B}s_A\ge0$, then

$$
\frac{s_{A\setminus B}}{s_A}
=\frac{1-\varphi\rho}{1-\varphi}\ge0,
$$

so $C_\tau\le1$ is equivalent to $\rho\ge1$. The proviso is $\varphi\rho\le1$. Dividing the interval in (8) by $s_A$ gives $0\le\rho\le2/\varphi$. Finally, both upper limits fall in $\varphi$ and diverge at zero. If $\varphi\le2/(1+M)$, then $(2-\varphi)/\varphi\ge M$ and $2/\varphi\ge M$. This proves all five readings.

### Part 2

Let $\epsilon=\kappa/2$. Lemma g3 gives, in kernel units,

$$
 s_A=-\frac12\sum_{k=0}^H(1-\epsilon)^k\epsilon^{H-k}c^A_k,
 \qquad
 s_{A\setminus B}=-\frac12\sum_{k=0}^H(1-\epsilon)^k\epsilon^{H-k}c^R_k. \tag{12}
$$

Since $x=\epsilon/(1-\epsilon)=\kappa/(2-\kappa)$,

$$
\sum_{k=0}^H(1-\epsilon)^k\epsilon^{H-k}v_k
=(1-\epsilon)^H P_v(x). \tag{13}
$$

Under (R1), the coefficient list of each pooled-cell polynomial has one sign change. Descartes' rule of signs gives exactly one positive root. The strict endpoint signs give $P_{c^A}(0)>0$ and $P_{c^R}(0)>0$, while both polynomials tend to $-\infty$ as $x\to\infty$. Each is therefore nonpositive at and above its positive root. Under (R2), $P_d(0)<0$, its leading coefficient is positive, and Descartes' rule again gives one positive root. Thus $P_d$ is nonnegative at and above that root.

Condition (R3), (13), and the positive factor $(1-\epsilon)^H$ give

$$
\mathcal W_A\le0,\qquad
\mathcal W_R\le0,\qquad
\mathcal W_R-\mathcal W_A\ge0.
$$

Hence $\mathcal W_A\le\mathcal W_R\le0$. Equation (12) gives

$$
0\le s_{A\setminus B}\le s_A.
$$

Condition (C$\tau$-3) rules out $s_A=0$, so $s_A>0$. Solve the cut identity for $s_B$:

$$
s_B=\frac{s_A-(1-\varphi)s_{A\setminus B}}{\varphi}.
$$

The lower band margin is

$$
s_B-s_A=\frac{1-\varphi}{\varphi}
(s_A-s_{A\setminus B})\ge0.
$$

The stronger upper margin is

$$
\frac{s_A}{\varphi}-s_B
=\frac{1-\varphi}{\varphi}s_{A\setminus B}\ge0.
$$

Since $0<\varphi<1$ and $s_A>0$, $s_A/\varphi<((2-\varphi)/\varphi)s_A$. This proves (11), and Part 1 gives $C_\tau\le1$.

## 3. Calibration computation

A calibration check needs no finite difference in $\kappa$.

1. For each $(\tau,T)$, compute the pooled measure type weights and the separate market weights used for beliefs. The existing route is `_alive_weights`. Measure weights set cell masses. Market weights include the off-path floor and set the posteriors.
2. For each revealed-round set $S$, partition the pooled type law by its restricted mark path. Compute each cell posterior $(\pi,\widehat v)$ as in Lemma g1, price it with `inner_price`, and integrate $h=\pi p$ using the measure weights. This gives the kappa-free $\mathcal G_{\tau,T}(S)$.
3. Form $c_k(\tau,T)$ from the finite sums in Lemma g3. For a pair, form $d_k=c_k(\tau',T)-c_k(\tau,T)$.
4. Classify a coefficient as zero when its absolute value is at most $10^{-12}$. Reject the certificate if any nonzero sign list lacks the orientation in (R1) or (R2). At the calibration, the smallest absolute $c_k$ used in a sign decision is $1.07\times10^{-7}$ and the smallest absolute $d_k$ is $1.34\times10^{-6}$.
5. Bisect each unique positive polynomial root to absolute tolerance $10^{-13}$ in $x$. Convert it by $\kappa=2x/(1+x)$. Certify an interval beginning at $\underline\kappa$ only if $\underline\kappa-\kappa_*\ge10^{-8}$.
6. As a check, evaluate (12) at each reported node and require both band margins to be at least $-10^{-12}$. For a null cut, require reclassified mass at most $10^{-12}$, paired coefficient differences at most $10^{-12}$, and $|C_\tau-1|\le10^{-12}$.

`single_crossing_certificate.py` performs steps 4 to 6 from the frozen c-coefficient record. Its record is `single_crossing_certificate.json`. All six checks pass. The largest residual against the source record's revelation values and $C_\tau$ is $3.89\times10^{-15}$. The source record already performs steps 1 to 3 and matches the pooled pass within $4.99\times10^{-18}$.

The computation is finite. It uses the pooled type law, the Lemma g1 cell posteriors, the Lemma g3 coefficients, and the two rules' own kernels. The tolerances separate the recorded float values, but they are not certified error bounds for those inputs. Because the coefficients come from numerical pricing rather than interval arithmetic, the calibration conclusion remains a numerical check. The implication from (R1) to (R3) is the proved part.

## 4. Cost of carrying the result into the paper

The result can replace two composition narratives with one nested-cut statement.

- `proofs/03_caught.tex` can state the cut identity for either dial, then specialise $B$ to a shorter clock or a tighter threshold. The threshold specialisation adds $b_0<\tau'$ and the mark-two clause for Condition D.
- `proofs/02_garbling.tex` can cite the threshold specialisation after Condition D and add the single-crossing revelation certificate. Remark `rem:g-Dstar` can remain as a global sufficient condition. The new certificate is local to an interval and holds where that remark fails.
- `proofs/04_inherited.tex` needs no changed argument. `lem:threshold-weight`, `thm:clock`, and `prop:factorisation` supply the two weight legs and the aggregate ratios.
- The theory section can ask one question for both dials: whether the tighter rule removes premium mass that is more noise-sensitive than what stays pooled. The numerical section would report the four $T=5$ cutoffs and treat the $T=10$ pairs as null cuts.

Part 1 would support a PROVED label only after the independent attack gate. The implication in Part 2 would support the same label after attack. The coefficient signs, roots, and calibration interval support a NUMERICAL statement tied to `t2_threshold_revelation_check.json` and the certificate record. They do not change the threshold composition leg's current label by themselves. No prose should call the $T=10$ null cuts evidence about who is caught.

## 5. Result

```json
{"status":"PASS","summary":"The nested-cut identity transfers to the threshold margin. A one-crossing certificate on the kappa-free c_k vectors proves the two-sided caught-leg band above a computable liquidity cutoff and holds on every non-null calibration pair over kappa in [0.15, 0.85].","files_changed":[".scratch/v5-paper/hunt/2-one-cut-identity/memo.md",".scratch/v5-paper/hunt/2-one-cut-identity/single_crossing_certificate.py",".scratch/v5-paper/hunt/2-one-cut-identity/single_crossing_certificate.json"],"evidence":"The cut proof uses nested type events and kappa-free masses. Descartes' rule turns three one-sign-change coefficient lists into unique root cutoffs. The largest cutoff is 0.149012173, below the grid at 0.15 and above the reported failure endpoint 0.1485. All script checks pass; source-record wiring residual is 3.89e-15."}
```
