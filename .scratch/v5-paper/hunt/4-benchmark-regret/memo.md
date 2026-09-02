# Certified benchmark-policy regret

## 1. Statement

### Hypotheses

The claim uses the standing-condition numbering of `proofs/04_inherited.tex`.

1. **(S1), one probability space.** The primitive vector, value $v$, signal noise
   $\varepsilon$, bidder draw $\xi$, and noise marks $z_{0:H}$ have a joint law on a finite
   product of Polish spaces. The noise marks lie in $\{-\bar z,0,+\bar z\}$, and
   $s=v+\varepsilon$.
2. **(S2), a finite menu and calendar.** The plan menu $\mathcal J$ is finite, $H$ is
   finite, and $T\in\{1,\ldots,H\}$.
3. **(S3), a cutoff selection map.** A step function with two ordered breakpoints carries the
   signal into Exit, Hold, or Voice.
4. **(S4), monotone Voice paths and a clean start.** Every plan has a stake path
   $B_j(s,\cdot)$ with $B_j(s,-1)=b_0<\tau$. The Voice path is weakly increasing in the signal
   and the date.
5. **(S5), legal-clock discipline.** Only Voice crosses the threshold. Its crossing date is the
   first date at which the path reaches $\tau$, or infinity if it never does. A truthful filing
   lands exactly $T$ dates later and only through the disclosure node.
6. **(S6), a public flag.** Every pooled history records whether the filing has landed by date
   $d$, and the control-node information contains the public history through that node.
7. **(S7), no-feedback timing.** The plan and signal determine the executed path, order marks,
   target, crossing date, filing date, filing stake, and flagged order. Realised flow and prices
   do not change them.
8. **(S8), a bounded pinned kernel.** The engagement-premium kernel is $h=\pi p$. The posterior
   $\pi$ lies in $[0,1]$. The bidder-entry probability $p$ lies in $(0,1)$ and is continuous in
   the posterior and price. The pricing rule pins one conditional-expectation version.
9. **(S9), a finite wedge.** $\Delta_m$ is finite and strictly positive, and
   $\Delta_{act}=\Delta_m\mathbb E[h(\mathcal I_H)]$.
10. **(S10), liquidity enters in one place.** $\kappa$ changes only the ternary noise-mark law.
    The laws of $v$, $\varepsilon$, and $\xi$ and all remaining constants do not change with
    $\kappa$.
11. **(S11), fixed policies.** The plan menu, execution policies, and benchmark cutoff vector
    remain fixed across all ten nodes.
12. **(S12), calibration.** The cutoffs are
    $k=(0.9425017266871091,1.8484512098302512)$. Also, $\kappa=0.5$, the order size is two noise
    lumps, and $H=10$. The rule has $T\in\{5,10\}$ and
    $\tau\in\{0.09239820387429526,0.09346755804663053,$
    $0.09453534811956685,0.09565657882778708,0.09703177146201895\}$.
    The remaining primitives equal `ParamsV4.baseline()`. The source parameter hash is
    `fbacc963f39422c3`, and `regret.json` gives the hash after each node's $T$ and $\tau$ are set.
13. **(S13), signal support.** The signal law is the calibrated Gaussian law restricted to
    $[s_{lo},s_{hi}]$, with $s_{lo}=1-6/\sqrt{2}$ and
    $s_{hi}=1+6/\sqrt{2}$. It has a continuous density. Finite breakpoint sets are null.
14. **(S14), fixed pooled pass.** At each node, `res` is the pooled pass at
    `atoms(frozen_k, p)` with the run-up path present. A deviation changes only the deviating
    signal and plan. It does not recompute `res`.

### Claim

Let $U_j(s)$ be `numerical_v4.policy.plan_payoff(j, s, res, p)`, let $j(s)$ be the benchmark
plan, and set
\[
 R(s)=\max_{j\in\{E,H,V\}} U_j(s)-U_{j(s)}(s).
\]
At every calibration node, the essential supremum of $R$ is no larger than the bound in the
last column. The certificate uses the full breakpoint partition, mesh width at most $10^{-5}$,
an analytic payoff-gap Lipschitz bound on each piece, and a $5\times10^{-12}$ arithmetic
allowance.

| Node | $T$ | $\tau$ | Certified upper bound |
|---:|---:|---:|---:|
| 1 | 5 | 0.092398203874295259 | `9.623219552034791e-05` |
| 2 | 5 | 0.093467558046630525 | `0.0001592462568311867` |
| 3 | 5 | 0.094535348119566848 | `0.00018783235544278404` |
| 4 | 5 | 0.095656578827787081 | `0.00020784219766716692` |
| 5 | 5 | 0.097031771462018954 | `0.0002248763859580155` |
| 6 | 10 | 0.092398203874295259 | `0.00024250934252785308` |
| 7 | 10 | 0.093467558046630525 | `0.00024250936609786458` |
| 8 | 10 | 0.094535348119566848 | `0.0002425093647088392` |
| 9 | 10 | 0.095656578827787081 | `0.00024250936470879758` |
| 10 | 10 | 0.097031771462018954 | `0.00024250936470879758` |

`regret.json` reports the attaining piece and its prior mass. It also reports every piece whose
certified upper bound is positive, all possible profitable alternatives on that piece, and a
sample witness when one exists. This conservative rule retains a piece even when only its
upper bound, rather than a computed payoff gap, is positive.

## 2. Proof of the bound

Fix one node. The pooled pass is fixed throughout.

### Smooth pieces

Take the two policy cutoffs, every jump of $n(s)$, and every pull-back of a threshold-crossing
date. Add the support endpoints and sort them. The script reconstructs the candidates below the
$10^{-9}$ merge used by `menu.breakpoints`, then removes exact duplicates only. Thus no
positive-width interval disappears. It checks the assigned plan and the Voice clock signature at
two interior points of every resulting interval.

On an open interval $I=(l,r)$, the assigned plan, Voice type $n$, filing status, crossing date,
and filing date are constant. The corresponding formula extends continuously to the closure of
that one-sided branch. Since the breakpoint set is finite and null under (S13), bounding every
branch closure bounds the essential supremum.

Write
\[
 b=b^*(s),\quad v_h=\mu_v+\beta(s-\mu_v),\quad
 C=C_0\exp[-\chi(s-\mu_v)/\sigma_s].
\]
For type $n$, let $e_n=\texttt{res.Ep\_bid}[n]$,
$q_n=\texttt{res.EpP}[n]$, and
\[
 A_n=\frac1n\sum_{d=0}^{n-1}\texttt{res.EP}[d][n].
\]
Direct substitution into `plan_payoff` gives
\[
 U_E=b_0\texttt{res.EP}[0][0],
\]
\[
 U_H=b_0\{(1-e_0)v_h+q_0+e_0m_0\},
\]
and, on a pooled Voice branch,
\[
 Y_n=(1-e_n)(v_h+\Delta_V)+q_n+e_nm_1,
 \qquad U_V=bY_n-A_n(b-b_0)-C.                 \tag{1}
\]
The Exit payoff is constant because the day-zero sale enters trade cost with a negative
increment. The Hold payoff is linear.

Now take a flagged Voice branch with filing date $f$. Put
\[
 r_f=\min\{1,(f+1)/n\},\quad B^F=b_0+r_f(b-b_0),
\]
and
\[
 A_{nf}=\frac1n\sum_{d=0}^{\min\{f,n-1\}}\texttt{res.EP}[d][n].
\]
At engagement posterior one, the flagged fixed point satisfies
\[
 P_F=(1-p_F)(v_h+\Delta_V)+p_F(P_F+m_1).
\]
The Voice payoff therefore reduces to
\[
 U_V=B^F P_F-A_{nf}(b-b_0)-C.                 \tag{2}
\]
For the numerical root returned by `inner_price`, the difference between the two sides of the
fixed point is the reported price residual. Its contribution to the unsimplified payoff is at
most $\bar b$ times that residual.

### Derivative bounds

The target stake obeys
\[
 b'(s)=\frac{\bar b-b_0}{2\sigma_s}(1+x^2)^{-3/2},
 \qquad x=(s-\mu_v)/\sigma_s.
\]
Its maximum on a closed piece occurs at the point nearest $\mu_v$. Also,
$C'(s)=-(\chi/\sigma_s)C(s)$, so $C$ is largest at the left endpoint.
Differentiating (1) gives
\[
 U_V'=b'(Y_n-A_n)+b(1-e_n)\beta+(\chi/\sigma_s)C.       \tag{3}
\]
Hence the script uses the valid bound
\[
 L_V^P=b'_{\max,I}\max_{s\in\{l,r\}}|Y_n(s)-A_n|
       +\bar b(1-e_n)\beta+(\chi/\sigma_s)C(l).          \tag{4}
\]
It uses $L_E=0$ and $L_H=b_0(1-e_0)\beta$.

It remains to bound the derivative of the flagged price. Set $V=v_h+\Delta_V$,
$a=1-p_F=\Phi(u)$, and
$u=(P_F+K+m_1-\bar S)/\sigma_\xi$. The price equation is
\[
 a(P_F-V)-(1-a)m_1=0.
\]
Implicit differentiation yields
\[
 \frac{dP_F}{ds}
 =\beta\frac{a^2}{a^2+(m_1/\sigma_\xi)\phi(u)},
 \qquad 0<\frac{dP_F}{ds}\le\beta.             \tag{5}
\]
The unique price root also lies in
\[
 [V,\ V+m_1\{1-a(V)\}/a(V)].                    \tag{6}
\]
The code applies (6) at the interval endpoints to obtain a bound $P_{abs}$ on $|P_F|$.
Differentiating (2), then using (5), gives
\[
 L_V^F=b'_{\max,I}(r_fP_{abs}+|A_{nf}|)
       +\bar b\beta+(\chi/\sigma_s)C(l).         \tag{7}
\]
These bounds are deliberately loose. Their role is to cover the space between sample points,
not to estimate the maximum from derivatives alone.

### Covering each piece

For an alternative $j$ and assigned plan $a$, define $G_{ja}=U_j-U_a$. Equations (4) and (7)
give a Lipschitz constant $L_{ja}=L_j+L_a$ on the closure of each branch. Divide the piece into
$n_I=\lceil(r-l)/10^{-5}\rceil$ equal segments and evaluate both alternative gaps at all
$n_I+1$ endpoints using the one-sided branch formula. Every point of the piece lies within
\[
 \delta_I=(r-l)/(2n_I)
\]
of a sample point. Therefore
\[
 \sup_{s\in I}G_{ja}(s)
 \le \max_{s\in\mathcal G_I}G_{ja}(s)+L_{ja}\delta_I.    \tag{8}
\]
The record adds $5\times10^{-12}$ for floating-point evaluation and the flagged fixed-point
residual. The largest pooled price residual was
$1.5482407023093003\times10^{-16}$, and the largest flagged root residual in the certifier was
$2.533780477098624\times10^{-16}$. The largest cover radius among reported positive pieces was
$4.999990936772152\times10^{-6}$. The allowance dominates the root residual contribution.

Taking the maximum of zero and the two bounds in (8) bounds $R$ on a piece. Taking the maximum
over all pieces proves the table. This step compares all plans, not only adjacent plans, so an
alternative-plan switch inside a piece cannot escape the bound.

### Relation to the node-1 candidate

The quoted node-1 island at
$\hat k=(0.9425042193,1.8472640726)$ belongs to that node's own solved candidate and its own
pooled pass. It is not the benchmark-policy object in this memo. Both calculations locate the
largest Hold gain immediately to the right of the same $n(s)$ jump at
$s=1.8608284620$. At $\hat k$, the reported island ends near $1.8625$ and peaks near
$7.0\times10^{-5}$. At the benchmark cutoffs, the sample peak is
$9.5932662747\times10^{-5}$ and the certified bound is
$9.6232195520\times10^{-5}$. The benchmark node also has smaller profitable deviations on two
other breakpoint pieces. `regret.json` reports them. The two peak numbers need not agree because
both the cutoffs and pooled pass differ.

## 3. Computation at a calibration node

Run:

```bash
PYTHONPATH=. .venv/bin/python .scratch/v5-paper/hunt/4-benchmark-regret/regret.py
```

The script does the following at each node.

1. It reads the full-precision ladder, benchmark cutoffs, and source hash from
   `numerical_v4/checks/t2_threshold_revelation_check.json`.
2. It constructs `atoms(frozen_k, p)` and runs one sequential pooled pass with
   `with_runup=True`. It does not solve a policy.
3. It constructs the unmerged breakpoint partition and checks each piece's signature.
4. It evaluates the three closed-form payoff branches on a mesh with width at most $10^{-5}$.
5. It applies (8) with the analytic derivative bounds and a $5\times10^{-12}$ arithmetic
   allowance.
6. It computes each piece's prior mass by the closed-form normal CDF difference, divided by the mass
   of the six-standard-deviation support.
7. It writes `regret.json` only after all ten nodes finish.

The script takes `COMPUTE_LOCK` once with `what` equal to
`hunt 4 regret record, ten pooled passes`, runs the passes in sequence, and releases the lock in
a `finally` block. This run took `61.488806375069544` seconds. The record gives pooled time,
certification time, both price residuals, the actual cover radius, and the number of mesh
segments for every reported piece.

## 4. Cost of carrying the result into the paper

No theorem or proof changes. The fixed-policy results retain their current labels. The
calibration section would gain one sentence that defines maximal interim regret and one compact
table row or range summary. That sentence would carry the label NUMERICAL and cite this record's
node grid, mesh tolerance, and parameter hash. A detailed ten-row table can remain in the
appendix or record. The calibration text should state that the benchmark is a fixed policy and
should not call it an equilibrium.

```json
{"status":"PASS","summary":"Certified maximal interim-regret upper bounds exist at all ten benchmark-policy nodes. The bounds range from 9.623219552034791e-05 to 0.00024250936609786458.","files_changed":[".scratch/v5-paper/hunt/4-benchmark-regret/regret.py",".scratch/v5-paper/hunt/4-benchmark-regret/regret.json",".scratch/v5-paper/hunt/4-benchmark-regret/memo.md"],"evidence":"regret.json applies a proved piecewise Lipschitz cover with mesh width at most 1e-5 and a 5e-12 arithmetic allowance. Ten sequential pooled passes completed in 61.49 seconds. The largest pooled and flagged price residuals were 1.55e-16 and 2.54e-16."}
```
