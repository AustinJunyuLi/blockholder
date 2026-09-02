# Order size two is the erasure regime

## 1. Statement

### Hypotheses

The proposition uses the paper's standing conditions with the following names.

1. (S1) One probability space. The primitive vector and the noise marks have a joint law on a
   finite product of Polish spaces.
2. (S2) A finite menu and a finite calendar. The plan menu is finite and the depth satisfies
   $d\leq H<\infty$.
3. (S3) A cutoff selection map. A step function maps the signal into a plan.
4. (S4) Monotone Voice paths and a clean start. The stake paths satisfy the paper's monotonicity
   and initial-stake conditions.
5. (S5) Legal-clock discipline. Only Voice plans cross the threshold, and a filing lands through
   the disclosure node after the window margin.
6. (S6) The flag is public. The history records whether a filing has landed.
7. (S7) No-feedback timing. At fixed policies, the type determines the mark path. Realised flow
   and price do not change it.
8. (S8) A bounded, pinned kernel. The paper uses one pinned version of the engagement-premium
   kernel.
9. (S9) A finite wedge. The premium wedge is finite and strictly positive.
10. (S10) Liquidity enters in one place. The intensity $\kappa$ changes only the noise law.
11. (S11) Fixed policies. The plan menu, execution policies, and cutoff vector stay fixed in
    $\kappa$ and across the experiments compared.
12. (E1) Exact independent ternary noise. For a fixed $\bar z>0$, the variables $z_e$ are
    independent across rounds and independent of the type, with
    \[
    \Pr_\kappa(z_e=-\bar z)=\Pr_\kappa(z_e=+\bar z)=\kappa/2,
    \qquad
    \Pr_\kappa(z_e=0)=1-\kappa.
    \]
13. (E2) Integral order size. For one positive integer $b$, every mark is
    $m_e\in\{0,b\bar z\}$ and $X_e=m_e+z_e$.
14. (E3) Nondegenerate mark experiment. The state set $\mathcal M$ is any subset of
    $\{0,b\bar z\}^{d+1}$ that contains at least two distinct mark paths. In a pooled cell,
    $\mathcal M$ is the set of paths with positive conditional probability. The cell event is a
    type event of positive mass, so it does not change the conditional noise law.

Conditions (S3) to (S6), (S8), and (S9) place the experiment inside the paper's model. The
information comparison itself uses (S1), (S2), (S7), (S10), (S11), and (E1) to (E3).

For $m=(m_0,\ldots,m_d)\in\mathcal M$, let $P^b_\kappa(\cdot\mid m)$ be the law of
$X_{0:d}$. Say that $E^b_{\kappa'}$ is a garbling of $E^b_\kappa$ if there is a Markov kernel
$\Lambda$ on flow histories, independent of $m$, such that
\[
P^b_{\kappa'}(y\mid m)
 =\sum_x P^b_\kappa(x\mid m)\Lambda(y\mid x)
\quad\text{for every }m\in\mathcal M\text{ and every }y.
\]
The experiment fully reveals the mark path if a decoder $g$ satisfies
$g(X_{0:d})=m$ with $P^b_\kappa(\cdot\mid m)$ probability one for every $m\in\mathcal M$.
Equivalently, distinct rows of the finite experiment have disjoint supports. Under any
full-support prior, this is equivalent to a degenerate posterior over the mark path almost
surely.

### Proposition

Under (S1) to (S11) and (E1) to (E3), the following two properties hold together if and only if
$b=2$:

1. for every $0<\kappa<\kappa'<1$, $E^b_{\kappa'}$ is a garbling of
   $E^b_\kappa$;
2. for every $\kappa\in(0,1)$, $E^b_\kappa$ does not fully reveal the mark path.

The three regimes are exact.

1. If $b=2$, the garbling result holds more widely for
   $0\leq\kappa<\kappa'\leq1$. The experiment fails to reveal any nondegenerate mark-path state
   set for every $\kappa\in(0,1]$, while $\kappa=0$ fully reveals it.
2. If $b=1$, the experiment is not fully revealing for $\kappa\in(0,1)$, but
   $E^1_{\kappa'}$ is not a garbling of $E^1_\kappa$ for any
   $0<\kappa<\kappa'<1$. Both endpoint experiments, at $\kappa=0$ and $\kappa=1$, fully reveal
   the one-round mark.
3. If $b\geq3$, every experiment fully reveals the mark path for every
   $\kappa\in[0,1]$. All liquidity nodes are Blackwell equivalent because each one reveals the
   state and can simulate every other node.

For $b=1$, one round also gives the exact Blackwell turn. Write $E_t=E^1_t$ on the two-state
space $\{0,\bar z\}$. For $0<\kappa<\kappa'<1$,
\[
E_\kappa\text{ is a garbling of }E_{\kappa'}
\quad\Longleftrightarrow\quad
2\kappa'+\kappa\geq2.
\]
The reverse relation never holds. Thus experiments with
$0<\kappa<\kappa'<2/3$ are incomparable. On $[2/3,1)$, higher $\kappa$ is strictly more
informative, which is the reverse of the proposed liquidity ordering. Across $2/3$, higher
$\kappa'$ dominates lower $\kappa$ exactly when $\kappa'\geq1-\kappa/2$; otherwise they are
incomparable. The value of the symmetric correct-guess problem falls up to $\kappa=2/3$ and
rises after it. The overlapping signals exchange their likelihood ranking at that same point.

This is a statement about the mark path. At fixed policies, type maps deterministically into
mark path and then into flow. The $b=2$ kernel therefore also garbles the experiment about the
paper's type, including after conditioning on a pooled cell event. Full revelation of the mark
path need not reveal the type when two types have the same path, so the uniqueness claim is not
stated for type revelation. One round settles both only-if regimes. The full-history statement
is needed for the positive $b=2$ result and is already supplied by Lemma g2.

## 2. Proof

Scale flows by $\bar z$ and write
\[
a_t=t/2,\qquad c_t=1-t.
\]
This loses no information because $\bar z>0$.

### The regime $b=2$

The garbling claim for interior liquidity nodes is exactly Lemma g2 in
`proofs/02_garbling.tex`. Its kernel reads the revealed set
\[
R_d=\{e\leq d:X_e\neq1\},
\]
deletes each member independently with probability
\[
\delta=\frac{\kappa'-\kappa}{2-\kappa},
\]
emits $1$ on deleted and already erased rounds, and redraws a surviving flow from the
$\kappa'$ conditional law given the mark. Lemma g1 shows that the input history identifies the
mark on every member of $R_d$. Lemma g2 then verifies the kernel identity for every type and
hence for every mark path. This memo does not re-prove that lemma.

The same formula covers $\kappa=0$ and $\kappa'=1$. For
$0\leq\kappa<\kappa'\leq1$, its deletion probability lies in $[0,1]$. At $\kappa=0$ every round
starts in $R_d$, and at $\kappa'=1$ the conditional redraw puts all surviving mass on the
nonzero-noise revealing value. Thus no limiting argument is needed.

It remains to settle revelation. Take two distinct paths $m,m'$. At a coordinate where they
differ, flow $1$ has probability $\kappa/2$ under either mark. At a coordinate where both marks
are zero, flow $-1$ has probability $\kappa/2$ under both paths. At a coordinate where both
marks are two, flow $3$ has probability $\kappa/2$ under both paths. These choices give one
common flow history with positive probability under both paths whenever $\kappa>0$. Their row
supports overlap, so no decoder can fully reveal the path. At $\kappa=0$, flow equals the mark
coordinate by coordinate and does reveal it.

### The regime $b=1$

For one round, with rows indexed by marks $0,1$ and columns indexed by flows $-1,0,1,2$, the
experiment is
\[
A_t=
\begin{pmatrix}
a_t&c_t&a_t&0\\
0&a_t&c_t&a_t
\end{pmatrix}.
\tag{1}
\]
For interior $t$, the rows overlap at flows $0$ and $1$. Products of these common-support
values give a common history for any two mark paths, so the path is not fully revealed.
At $t=0$, the flow equals the mark. At $t=1$, the row supports are $\{-1,1\}$ and $\{0,2\}$.
Both endpoints are fully revealing.

Now fix $0<\kappa<\kappa'<1$. Give the two one-round marks equal prior probability. There are
two actions, abstain and claim that the mark is zero. Abstention pays zero. A correct claim pays
one and a false claim pays $-C$, where
\[
C>
\max_{t\in\{\kappa,\kappa'\}}
\left\{\frac{a_t}{c_t},\frac{c_t}{a_t}\right\}.
\]
All displayed ratios are finite. Under either experiment, the unique flow at which a claim has
positive conditional value is $-1$. The value of the decision problem at node $t$ is therefore
$a_t/2=t/4$. It is strictly larger at $\kappa'$ than at $\kappa$. A garbling cannot raise the
value of any decision problem. Hence $E_{\kappa'}$ is not a garbling of $E_\kappa$. This
one-round counterexample also applies to a longer nondegenerate path experiment. Put prior mass
on two distinct paths and let $q$ be the number of coordinates at which they differ. Choose the
false-claim loss above every finite likelihood ratio at both nodes. A claim then pays only on
histories that have zero likelihood under the other path. Under the claimed path, their total
probability is $1-(1-a_t)^q$. It rises strictly with $t$, so the decision value is again larger
at $\kappa'$.

For completeness, the reverse Blackwell relation has a closed form. Suppose
$2\kappa'+\kappa\geq2$, put
\[
r=\frac{\kappa'-\kappa}{3\kappa'-2},
\]
and index both the rows and columns of the following kernel by $-1,0,1,2$:
\[
K_{\kappa'\to\kappa}=
\begin{pmatrix}
\kappa/\kappa'&1-\kappa/\kappa'&0&0\\
0&1-r&r&0\\
0&r&1-r&0\\
0&0&1-\kappa/\kappa'&\kappa/\kappa'
\end{pmatrix}.
\tag{2}
\]
The inequality implies $\kappa'>2/3$ and $0\leq r\leq1$, so (2) is a Markov kernel. Direct
multiplication gives
\[
A_{\kappa'}K_{\kappa'\to\kappa}=A_\kappa.
\]
Thus $E_\kappa$ is a garbling of $E_{\kappa'}$. Applying the kernel independently across rounds
proves the same relation for every mark-path state set.

If $2\kappa'+\kappa<2$, consider instead the two-action problem that pays one for a correct
mark guess and zero for a wrong guess, under the uniform prior. Its value at node $t$ is
\[
V(t)=\frac{1+\operatorname{TV}(A_t(\cdot\mid0),A_t(\cdot\mid1))}{2}
=
\begin{cases}
1-t/2,&0\leq t\leq2/3,\\
t,&2/3\leq t\leq1.
\end{cases}
\tag{3}
\]
The inequality $2\kappa'+\kappa<2$ gives $V(\kappa)>V(\kappa')$. Therefore
$E_\kappa$ cannot be a garbling of $E_{\kappa'}$. The false-claim problem already showed that
the relation in the other direction also fails. This proves incomparability and the exact
condition. Formula (3) has its unique minimum at $2/3$. At that node $a_t=c_t$, so flows $0$
and $1$ have likelihood ratio one. Their likelihood rankings reverse on the two sides of the
node.

### The regime $b\geq3$

The idle support is $\{-1,0,1\}$ and the building support is
$\{b-1,b,b+1\}$. They are disjoint when $b\geq3$. The decoder reads mark zero from a flow at
most one and mark $b$ from a flow at least two, coordinate by coordinate. It works at every
$\kappa\in[0,1]$.

There is also an explicit kernel between any two liquidity nodes. Read the mark from the input
flow, draw fresh ternary noise with the target node's law, and emit the decoded mark plus the
fresh noise. The kernel does not use the unknown state beyond what the input already reveals.
It maps every row at the source node to the corresponding row at the target node. Reversing the
nodes gives the reverse kernel, so all nodes are Blackwell equivalent.

The $b=2$ regime satisfies both properties in the proposition. The $b=1$ regime fails the first.
The $b\geq3$ regime fails the second. This proves the equivalence.

### Wider symmetric noise support

The same support argument gives a short extension. Suppose integer noise has support
$\{-L,\ldots,L\}$ and a symmetric law. The supports under marks zero and $b$ meet in exactly
one flow if $b=2L$. The common flow is $L$, and symmetry gives it the same probability under
both marks. Thus $b=2L$ is the erasure form guaranteed by symmetry alone. If a family of laws
raises the endpoint mass $\Pr(z=L)=\Pr(z=-L)$, the deletion and conditional-redraw kernel from
Lemma g2 applies. Orders $b>2L$ fully reveal the mark. Orders $b<2L$ have several common flows
and need extra equalities such as $p(z)=p(z-b)$ on the overlap to be an erasure experiment.
Those equalities can hold for special laws, including a uniform law, but symmetry alone does not
imply them.

## 3. Calibration computation

No calibration computation is needed. The result is an exact comparison of finite channel
matrices and does not depend on the policy cutoffs, threshold ladder, horizon calibration, or
premium kernel.

A regression test would only check algebra already displayed here. For selected interior pairs,
it could require nonnegative kernel entries and row sums within $10^{-12}$ of one, and require
$\lVert A_{\kappa'}K-A_\kappa\rVert_\infty\leq10^{-12}$ for (2). No pooled pass, policy solve,
or compute lock is needed.

## 4. Cost of carrying the result into the paper

The new proposition belongs immediately before or after Lemma g1 in
`proofs/02_garbling.tex`. Lemma g2 already proves its positive $b=2$ half, so its proof does not
change. The threshold theorem also does not change because it already fixes order size two and
uses Lemma g2. The main paper's model section can replace the present order-size defense with
one sentence that states the unique-erasure result and points to the proposition. The appendix
would add the short $b=1$ decision problem and the disjoint-support argument for $b\geq3$.

The result would support a PROVED label only after an independent attack gate. This memo awards
no label. It does not change the labels of Lemmas g1 to g3, the threshold theorem, the clock
theorem, or any numerical result. No figure, calibration record, empirical section, or result
file moves.

## 5. RESULT

```json
{"status":"PASS","summary":"Under a nondegenerate mark-path state set, order size two is exactly the only positive integer order size for which every higher interior liquidity node is a garbling and no interior node fully reveals the mark path. Lemma g2 is the full-history positive half. At order size one, higher liquidity is never a garbling of lower liquidity; the exact one-round Blackwell turn is at 2/3. At order sizes at least three, flow fully reveals every mark coordinate.","files_changed":[".scratch/v5-paper/hunt/1-erasure-regime/memo.md"],"evidence":"Lemma g2 supplies the explicit deletion kernel for b=2. A two-action false-claim problem has value kappa/4 at b=1 and strictly improves with kappa. The reverse b=1 kernel exists exactly when 2 kappa' + kappa >= 2, while the correct-guess value proves incomparability otherwise. For b>=3 the two conditional supports are disjoint and a decode-then-redraw kernel gives Blackwell equivalence across liquidity nodes."}
```
