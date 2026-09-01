# C1 — independent statements-only re-derivation

**Inputs seen:** `rederive/C1_statement_sheet.md` (CLAIM + H1–H8) and `MODEL_CARD.md`
(stamp 2026-08-21). Nothing else. No proof file, no thread file, no other file in
`rederive/`. The route below is my own; it was not read off anything.

**VERDICT: PROVED-WITH-CHANGES.**

Parts (A), (B), (C), (D) all go through. Two hypotheses must be **added** (a norm
convention; two-sided openness of $\mathcal R_r$ in *both* coordinates), two clauses of
the stated set are **redundant** (H2's sign-constancy clause, for reaching (C); and H5,
under one reading of $\operatorname{sgn}$), two hypotheses are consumed in a **sharper
reading** than the sheet's wording (H3's "one branch" as continuity of the selection; the
$\Delta$- and $\mathcal T$-derivatives as partials *evaluated at the equilibrium point*),
one is **confirmed unused** for the boxed conclusion (H8, exactly as the sheet says), and
one symbol **collides with the card** ($\mathcal S$). The norm question bit hard: at
$J-1\ge2$ the card's bare $\lvert\cdot\rvert$ in $\mathcal B_r^{GE}$ is not well defined,
and a mismatched reading makes part (B) **false** — a two-line counterexample is at
WHERE IT FAILS 5.

---

## CLAIM

Throughout, $\vartheta=(\kappa,r)$ with $r$ the **threshold** strictness coordinate
$r_\tau=-\tau$ (card §4.5); the $r_T$ instance is discussed at WHERE IT FAILS 6 and is not
part of what I claim. $k\in\mathbb R^{J-1}$ is the cutoff vector, $\Theta$ the compact
ordered polytope, $\mathcal T$ the outer best-response map (card §4.5). Write

$$
\mathcal D(\kappa,r)\;:=\;\Delta^{\mathrm{act}}\!\bigl(k(\kappa,r),\kappa,r\bigr),
\qquad
\mathcal S^{GE}\;:=\;\Bigl\lvert \frac{d\mathcal D}{d\kappa}\Bigr\rvert .
$$

$\mathcal S^{GE}$ is the **equilibrium** liquidity-sensitivity. It is *not* card §4.4's
$\mathcal S=\lvert\partial_\kappa\Delta^{\mathrm{act}}\rvert$, which is the fixed-policy
object; see NOTATION DELTA 1, and WHERE IT FAILS 4 for why the distinction is
load-bearing rather than cosmetic.

**(A) Inversion-free derivative bounds.** On $\mathcal R_r$ the branch $\vartheta\mapsto
k(\vartheta)$ is twice continuously differentiable, and at every $\vartheta\in\mathcal R_r$

$$
\lVert\partial_\kappa k\rVert\le\bar k_\kappa=\frac{\lVert\partial_\kappa\mathcal T\rVert}{1-L_{\mathcal R}},
\qquad
\lVert\partial_r k\rVert\le\bar k_r=\frac{\lVert\partial_r\mathcal T\rVert}{1-L_{\mathcal R}},
$$
$$
\lVert\partial^2_{\kappa r}k\rVert\le\bar k_{\kappa r}
=\frac{\lVert\mathcal T_{\kappa r}\rVert+\lVert\mathcal T_{\kappa k}\rVert\bar k_r
+\lVert\mathcal T_{rk}\rVert\bar k_\kappa+\lVert\mathcal T_{kk}\rVert\bar k_\kappa\bar k_r}
{1-L_{\mathcal R}},
$$

every $\mathcal T$-derivative being the partial evaluated at $(k(\vartheta),\vartheta)$ and
every norm the one fixed by N1. No inverse of $I-D_k\mathcal T$ is formed: each bound is
the geometric sum $\sum_{n\ge0}L_{\mathcal R}^n$.

**(B) The GE remainder bound is exactly $\mathcal B_r^{GE}$.**

$$
\Bigl\lvert\frac{d^2\mathcal D}{d\kappa\,dr}-\partial_{\kappa r}\Delta^{\mathrm{act}}\Bigr\rvert
\;\le\;\mathcal B_r^{GE}
=\lvert\Delta_{\kappa k}\rvert\bar k_r
+\bigl(\lvert\Delta_{kr}\rvert+\lvert\Delta_{kk}\rvert\bar k_r\bigr)\bar k_\kappa
+\lvert\Delta_k\rvert\bar k_{\kappa r},
$$

with $\partial_{\kappa r}\Delta^{\mathrm{act}}$ and every other $\Delta$-derivative the
fixed-policy partial evaluated at $(k(\vartheta),\vartheta)$.

**(C) Dominance.** If in addition $g_r^{PE}>\mathcal B_r^{GE}$ on $\mathcal R_r$, then

$$
\boxed{\;\partial_r\mathcal S^{GE}\;\le\;-\eta_r\;<\;0
\qquad\text{at every }\vartheta\in\mathcal R_r,\qquad \eta_r=g_r^{PE}-\mathcal B_r^{GE}.\;}
$$

**(D) Finite scale.** If $\mathcal R_r\supseteq\{\kappa\}\times[r_0,r_1]$ with $r_0<r_1$,
then $\mathcal S^{GE}(\kappa,r_1)-\mathcal S^{GE}(\kappa,r_0)\le-\int_{r_0}^{r_1}\eta_r\,dr<0$.

Nonemptiness of $\mathcal R_r$ is not claimed and is not derivable here (NOT CLAIMED 1).

---

## HYPOTHESES

Each is marked **[as stated]**, **[ADDED]**, **[READING]**, **[REDUNDANT]** or
**[UNUSED for (C)]**, and the step that consumes it is named.

**H1 — Card and stamp.** MODEL_CARD.md, stamp 2026-08-21. Every symbol carries its card §4
meaning; upright $T$ is the window, $\mathcal T$ the outer map. **[as stated]** [all steps]

**H2a — AGE, along-the-path reading.** On $\mathcal R_r$ the outer map $(k,\vartheta)\mapsto
\mathcal T(k;\vartheta)$ is twice continuously differentiable **jointly** in its arguments,
and $L_{\mathcal R}=\sup_{\vartheta\in\mathcal R_r}\lVert D_k\mathcal T(k(\vartheta);\vartheta)\rVert<1$.
**[as stated, with the joint-differentiability reading]** [Steps 1–7]

**H2c — AGE, sign-constancy clause.** The sign of the equilibrium liquidity derivative is
constant on $\mathcal R$. **[REDUNDANT for (C)]** — Step 12 derives local constancy from
H5 plus continuity, which is all the boxed conclusion consumes. The clause retains a role
only when $\mathcal R_r$ is disconnected and one wants a single region-wide sign inside the
definition of $g_r^{PE}$. [Step 12, remark only]

**H2b — over-$\Theta$ reading.** Not used. Step 15 records what it would buy.
**[UNUSED, as the sheet says]**

**H3 — Interior equilibrium on a single branch.** At every $\vartheta\in\mathcal R_r$ there is
$k(\vartheta)\in\operatorname{int}\Theta$ with $k(\vartheta)=\mathcal T(k(\vartheta);\vartheta)$,
and $\vartheta\mapsto k(\vartheta)$ is one branch. **[READING]** — interiority is consumed as
"$\mathcal T(\cdot;\vartheta)$ is defined and two-sidedly differentiable on a full ball around
$k(\vartheta)$" (Step 2); "one branch, no switch" is consumed as **continuity of the selection**
(Step 4). Local uniqueness is *not* assumed — Step 3 derives it. [Steps 2, 3, 4]

**H4 — $C^2$ and finiteness of the premium's derivatives.** $(k,\kappa,r)\mapsto
\Delta^{\mathrm{act}}$ is twice continuously differentiable on a neighbourhood of the graph
$\{(k(\vartheta),\vartheta):\vartheta\in\mathcal R_r\}$, and $\Delta_k,\Delta_{kk},
\Delta_{\kappa k},\Delta_{kr},\Delta_{\kappa r}$, together with $\mathcal T_{\kappa r},
\mathcal T_{\kappa k},\mathcal T_{rk},\mathcal T_{kk}$, are finite there. **[as stated]**
[Steps 5, 8, 9, 13]

**H5 — Non-vanishing equilibrium liquidity derivative.** $d\mathcal D/d\kappa\neq0$ at every
$\vartheta\in\mathcal R_r$. **[as stated; REDUNDANT under one convention]** — under
$\operatorname{sgn}(0)=0$, H6 already forces it, because $g_r^{PE}$ would be $0$ and
$0>\mathcal B_r^{GE}\ge0$ is impossible. The card fixes no $\operatorname{sgn}(0)$
convention, so I keep H5 explicit. It is not a technical convenience: WHERE IT FAILS 3
exhibits a $\mathcal D$ violating (C) at a zero of $d\mathcal D/d\kappa$. [Step 12]

**H6 — Strict dominance.** $g_r^{PE}>\mathcal B_r^{GE}$, i.e. $\eta_r>0$, at every
$\vartheta\in\mathcal R_r$, with $g_r^{PE}=
-\operatorname{sgn}(d\Delta^{\mathrm{act}}/d\kappa)\,\partial_{\kappa r}\Delta^{\mathrm{act}}$,
the sign being the **equilibrium** one (card §4.5). **[as stated]** [Steps 13, 14]

**H7 — A smooth strictness domain.** $r$ ranges over an open interval on which the objects of
H2a and H4 are defined. **[as stated]** [Steps 2, 4, 5]

**H8 — Sign coherence.** $\operatorname{sgn}(\partial_\kappa\Delta^{\mathrm{act}}(k(\vartheta),
\vartheta))=\operatorname{sgn}(d\mathcal D/d\kappa)$ on $\mathcal R_r$.
**[UNUSED for (C) — confirmed]** — no step before Step 16 mentions it; Step 16 is where it is
consumed, and Step 16 is a statement about what $g_r^{PE}$ may be *called*. [Step 16]

**N1 — Norm convention. [ADDED]** Fix one norm $\lVert\cdot\rVert$ on $\mathbb R^{J-1}$. Every
$\lvert\cdot\rvert$ in the card §4.5 rows for $L_{\mathcal R}$, $\bar k_x$, $\bar k_{\kappa r}$
and $\mathcal B_r^{GE}$ is read as the member of the family that $\lVert\cdot\rVert$ induces:

| object | type | magnitude used |
|---|---|---|
| $\partial_\kappa\mathcal T,\ \partial_r\mathcal T,\ \mathcal T_{\kappa r}$ | vectors in $\mathbb R^{J-1}$ | $\lVert\cdot\rVert$ |
| $D_k\mathcal T,\ \mathcal T_{\kappa k},\ \mathcal T_{rk}$ | matrices | induced operator norm $\sup_{\lVert u\rVert\le1}\lVert Au\rVert$ |
| $\mathcal T_{kk}$ | $\mathbb R^{J-1}$-valued bilinear form | $\sup_{\lVert u\rVert,\lVert v\rVert\le1}\lVert\mathcal T_{kk}[u,v]\rVert$ |
| $\Delta_k,\ \Delta_{\kappa k},\ \Delta_{kr}$ | covectors | **dual** norm $\lVert\phi\rVert_*=\sup_{\lVert u\rVert\le1}\lvert\phi(u)\rvert$ |
| $\Delta_{kk}$ | scalar bilinear form | $\sup_{\lVert u\rVert,\lVert v\rVert\le1}\lvert\Delta_{kk}[u,v]\rvert$ |

Consumed in Steps 1, 6, 8, 9. Three consequences, all recorded rather than hidden:
(i) the operator norm must be **induced** (hence submultiplicative), because Step 1 uses
$\lVert A^n\rVert\le\lVert A\rVert^n$; (ii) $L_{\mathcal R}<1$ is a statement about the chosen
norm, so the certificate reads "**there exists** a norm at which …" and a rescaling of the
cutoff coordinates can move a node across the certification boundary (Step 17); (iii) at
$J-1=1$ — the single-cutoff case — the whole family collapses to the absolute value and N1
is vacuous, which is presumably why the card could write $\lvert\cdot\rvert$ throughout.

**N2 — Two-sided parameter domain. [ADDED]** $\mathcal R_r$ is relatively open in the
$(\kappa,r)$ plane; in particular $\kappa\in(0,1)$, the card §4.1 endpoints $\kappa\in\{0,1\}$
being excluded. H7 supplies openness in the $r$ coordinate only, and the implicit function
theorem of Step 4, the mixed partial of Step 5 and the mixed partial of Step 9 all need a
full two-dimensional neighbourhood. [Steps 2, 4, 5, 9]

---

## PROOF

### Part 0 — objects

**Step 0.** Fix $\vartheta\in\mathcal R_r$ and write $k^0=k(\vartheta)$ (H3). All
$\mathcal T$-derivatives below are partials of $(k,\kappa,r)\mapsto\mathcal T(k;\kappa,r)$
evaluated at $(k^0,\vartheta)$, and all $\Delta$-derivatives are partials of the
**fixed-policy** map $(k,\kappa,r)\mapsto\Delta^{\mathrm{act}}(k,\kappa,r)$ of card §4.4,
also evaluated at $(k^0,\vartheta)$. Subscripts denote partials: $\Delta_k\in(\mathbb
R^{J-1})^*$, $\Delta_{kk}$ the $k$-Hessian, $\Delta_{\kappa k}=\partial_k\partial_\kappa
\Delta^{\mathrm{act}}$, and likewise for $\mathcal T$, whose values are vectors, so
$\mathcal T_{kk}$ is an $\mathbb R^{J-1}$-valued bilinear form. Card §4.5's $\mathcal T_{rk}$
is $\partial_r\partial_k\mathcal T$; by H2a's $C^2$ clause and the symmetry of second
derivatives of a $C^2$ map, $\mathcal T_{rk}=\mathcal T_{kr}$, and I use whichever ordering
the display needs. $I$ is the identity on $\mathbb R^{J-1}$.

### Part I — (A): the inversion-free bounds

**Step 1 (Neumann).** Let $A$ be a matrix with $\lVert A\rVert\le L<1$ in the induced
operator norm of N1. The partial sums $S_N=\sum_{n=0}^NA^n$ satisfy $\lVert A^n\rVert\le
L^n$ by submultiplicativity (N1(i)), so $\sum_n\lVert A^n\rVert\le(1-L)^{-1}<\infty$ and,
the space of $(J-1)\times(J-1)$ matrices being finite-dimensional and complete, $S_N$
converges to some $S$ with $\lVert S\rVert\le(1-L)^{-1}$. From $(I-A)S_N=S_N(I-A)=
I-A^{N+1}$ and $\lVert A^{N+1}\rVert\le L^{N+1}\to0$, passing to the limit gives
$(I-A)S=S(I-A)=I$. Hence $I-A$ is invertible with
$$\lVert(I-A)^{-1}\rVert\le\frac1{1-L}=\sum_{n\ge0}L^n. \tag{1}$$
Applied at $A=D_k\mathcal T(k^0;\vartheta)$, whose norm is $\le L_{\mathcal R}<1$ by H2a,
$I-D_k\mathcal T$ is invertible at every point of the equilibrium graph.

**Step 2 (a ball on which $\mathcal T$ contracts).** By H2a the map $(k,\vartheta)\mapsto
D_k\mathcal T(k;\vartheta)$ is continuous. Pick $L'$ with $L_{\mathcal R}<L'<1$. By H3's
interiority and N2 there are $\delta,\rho>0$ with $\bar B(k^0,\delta)\subset
\operatorname{int}\Theta$, $\bar B(\vartheta,\rho)$ inside the domain of H2a and H4, and
$\lVert D_k\mathcal T(k';\vartheta')\rVert\le L'$ for all $(k',\vartheta')\in\bar
B(k^0,\delta)\times\bar B(\vartheta,\rho)$. The ball being convex, the mean-value
inequality along the segment gives $\lVert\mathcal T(k_1;\vartheta')-\mathcal
T(k_2;\vartheta')\rVert\le L'\lVert k_1-k_2\rVert$ there. Shrinking $\rho$ so that
$\lVert\mathcal T(k^0;\vartheta')-\mathcal T(k^0;\vartheta)\rVert\le(1-L')\delta$
(continuity of $\mathcal T$ in $\vartheta$, H2a), and using $\mathcal T(k^0;\vartheta)=k^0$
(H3),
$$\lVert\mathcal T(k_1;\vartheta')-k^0\rVert\le L'\delta+(1-L')\delta=\delta
\qquad\text{for all }k_1\in\bar B(k^0,\delta),\ \vartheta'\in\bar B(\vartheta,\rho). \tag{2}$$
So $\mathcal T(\cdot;\vartheta')$ maps the closed ball into itself and contracts it.

**Step 3 (local uniqueness and continuity, derived).** $\bar B(k^0,\delta)$ with
$\lVert\cdot\rVert$ is a complete metric space, so by Step 2 and the contraction mapping
theorem each $\vartheta'\in\bar B(\vartheta,\rho)$ admits **exactly one** fixed point
$\hat k(\vartheta')$ of $\mathcal T(\cdot;\vartheta')$ inside the ball, and $\hat
k(\vartheta)=k^0$. For $\vartheta',\vartheta''\in\bar B(\vartheta,\rho)$,
$$\lVert\hat k(\vartheta')-\hat k(\vartheta'')\rVert\le
L'\lVert\hat k(\vartheta')-\hat k(\vartheta'')\rVert
+\lVert\mathcal T(\hat k(\vartheta'');\vartheta')-\mathcal T(\hat k(\vartheta'');\vartheta'')\rVert,$$
so $\lVert\hat k(\vartheta')-\hat k(\vartheta'')\rVert\le(1-L')^{-1}\lVert\mathcal T(\hat
k(\vartheta'');\vartheta')-\mathcal T(\hat k(\vartheta'');\vartheta'')\rVert$, which tends to
$0$ as $\vartheta'\to\vartheta''$ by continuity of $\mathcal T$ in $\vartheta$. Hence $\hat
k$ is continuous. Nothing here is assumed: local uniqueness and local continuity are
consequences of H2a and H3.

**Step 4 (the branch is $C^2$).** Put $\Phi(k',\vartheta'):=k'-\mathcal T(k';\vartheta')$ on
$\bar B(k^0,\delta)\times\bar B(\vartheta,\rho)$. By H2a, $\Phi$ is $C^2$; $\Phi(k^0,
\vartheta)=0$ by H3; $D_k\Phi=I-D_k\mathcal T$ is invertible at $(k^0,\vartheta)$ by Step 1.
The implicit function theorem in its $C^2$ form therefore yields neighbourhoods and a
$C^2$ map $\vartheta'\mapsto\tilde k(\vartheta')$ with $\Phi(\tilde k(\vartheta'),
\vartheta')=0$ and $\tilde k(\vartheta)=k^0$, unique among solutions in those
neighbourhoods. Every such $\tilde k(\vartheta')$ is a fixed point of $\mathcal
T(\cdot;\vartheta')$ lying in $\bar B(k^0,\delta)$, so $\tilde k=\hat k$ where both are
defined, by Step 3's uniqueness. Finally, H3's clause "no switch of selected equilibrium
occurs inside $\mathcal R_r$" is consumed here in the form: $\vartheta'\mapsto
k(\vartheta')$ is continuous, so it stays in $\bar B(k^0,\delta)$ near $\vartheta$ and
coincides there with $\hat k=\tilde k$. (A selection that jumped to a different fixed point
at nearby parameters would be exactly the switch H3 excludes.) Since $\vartheta$ was
arbitrary in the relatively open $\mathcal R_r$ (N2), $k(\cdot)$ is $C^2$ on $\mathcal R_r$.
This is the first assertion of (A).

**Step 5 (first-order relations).** Differentiating the identity $k(\vartheta')=\mathcal
T(k(\vartheta');\vartheta')$ — legitimate by Step 4 and H2a, both sides being $C^2$ in
$\vartheta'$ on a two-sided neighbourhood (N2) — and evaluating at $\vartheta$:
$$k_\kappa=D_k\mathcal T\,k_\kappa+\mathcal T_\kappa,\qquad
k_r=D_k\mathcal T\,k_r+\mathcal T_r, \tag{3}$$
with $k_\kappa=\partial_\kappa k(\vartheta)$, $k_r=\partial_rk(\vartheta)$. H7 is what makes
the second relation meaningful, $r$ being a coordinate on an open interval.

**Step 6 (the $\bar k_x$ bounds).** Both $k_\kappa$ and $k_r$ are finite vectors by Step 4.
Take norms in (3) and use N1's operator-norm compatibility and H2a:
$$\lVert k_\kappa\rVert\le L_{\mathcal R}\lVert k_\kappa\rVert+\lVert\mathcal T_\kappa\rVert
\;\Longrightarrow\;
\lVert k_\kappa\rVert\le\frac{\lVert\mathcal T_\kappa\rVert}{1-L_{\mathcal R}}=\bar k_\kappa,
\qquad\text{and likewise }\lVert k_r\rVert\le\bar k_r. \tag{4}$$
The rearrangement is licensed because $\lVert k_\kappa\rVert<\infty$ and
$1-L_{\mathcal R}>0$. Equivalently, solving (3) as $k_\kappa=(I-D_k\mathcal
T)^{-1}\mathcal T_\kappa$ and applying (1) gives the same number; the displayed route never
writes the inverse down, which is the sense in which the bound is inversion-free. Note what
is and is not inversion-free: the *bound* needs only norms; the *object* $k_\kappa$ is still
the solution of a linear system.

**Step 7 (the $\bar k_{\kappa r}$ bound).** Differentiate the first relation of (3) with
respect to $r$, remembering that $D_k\mathcal T$ and $\mathcal T_\kappa$ are evaluated at
$(k(\vartheta'),\vartheta')$, so each carries a chain term through $k_r$:
$$\partial_r\bigl[D_k\mathcal T\bigr]=\mathcal T_{kk}[\,\cdot\,,k_r]+\mathcal T_{kr},
\qquad
\partial_r\bigl[\mathcal T_\kappa\bigr]=\mathcal T_{\kappa k}k_r+\mathcal T_{\kappa r},$$
so that
$$k_{\kappa r}=D_k\mathcal T\,k_{\kappa r}
+\underbrace{\mathcal T_{kk}[k_\kappa,k_r]}_{\text{(t1)}}
+\underbrace{\mathcal T_{kr}k_\kappa}_{\text{(t2)}}
+\underbrace{\mathcal T_{\kappa k}k_r}_{\text{(t3)}}
+\underbrace{\mathcal T_{\kappa r}}_{\text{(t4)}}. \tag{5}$$
Taking norms with N1 and using $\lVert\mathcal T_{kk}[u,v]\rVert\le\lVert\mathcal
T_{kk}\rVert\lVert u\rVert\lVert v\rVert$, then (4):
$$\lVert k_{\kappa r}\rVert\le L_{\mathcal R}\lVert k_{\kappa r}\rVert
+\lVert\mathcal T_{\kappa r}\rVert+\lVert\mathcal T_{\kappa k}\rVert\bar k_r
+\lVert\mathcal T_{rk}\rVert\bar k_\kappa+\lVert\mathcal T_{kk}\rVert\bar k_\kappa\bar k_r,$$
using $\mathcal T_{kr}=\mathcal T_{rk}$ (Step 0). Rearranging as in Step 6,
$\lVert k_{\kappa r}\rVert\le\bar k_{\kappa r}$, the card §4.5 expression term for term:
(t4) supplies $\lVert\mathcal T_{\kappa r}\rVert$, (t3) supplies $\lVert\mathcal T_{\kappa
k}\rVert\bar k_r$, (t2) supplies $\lVert\mathcal T_{rk}\rVert\bar k_\kappa$, (t1) supplies
$\lVert\mathcal T_{kk}\rVert\bar k_\kappa\bar k_r$. Four terms in, four terms out; none is
dropped and none is counted twice. **(A) is proved.**

### Part II — (B): the GE remainder

**Step 8 (the equilibrium premium is $C^2$).** $\mathcal D=\Delta^{\mathrm{act}}\circ
(k(\cdot),\mathrm{id})$ is a composition of the $C^2$ map of Step 4 with the $C^2$ map of
H4, whose domain contains the equilibrium graph, so $\mathcal D$ is $C^2$ on $\mathcal R_r$.
In particular its mixed second derivatives exist, are continuous, and are order-independent.

**Step 9 (the cross-derivative ledger).** By the chain rule,
$$\frac{d\mathcal D}{d\kappa}=\Delta_k\,k_\kappa+\Delta_\kappa. \tag{6}$$
Differentiating (6) in $r$, again with every $\Delta$-derivative evaluated at
$(k(\vartheta'),\vartheta')$ and therefore carrying a chain term through $k_r$:
$$\frac{d^2\mathcal D}{d\kappa\,dr}
=\underbrace{\Delta_{\kappa r}}_{\text{(u0)}}
+\underbrace{\Delta_{\kappa k}k_r}_{\text{(u1)}}
+\underbrace{\Delta_{kr}k_\kappa}_{\text{(u2)}}
+\underbrace{\Delta_{kk}[k_\kappa,k_r]}_{\text{(u3)}}
+\underbrace{\Delta_k\,k_{\kappa r}}_{\text{(u4)}}. \tag{7}$$
Derivation of (7) in full: $\partial_r[\Delta_\kappa]=\Delta_{\kappa k}k_r+\Delta_{\kappa
r}$ gives (u1) and (u0); $\partial_r[\Delta_k\,k_\kappa]=(\partial_r\Delta_k)k_\kappa+
\Delta_k\,k_{\kappa r}$ with $\partial_r\Delta_k=\Delta_{kk}[\,\cdot\,,k_r]+\Delta_{kr}$
gives (u3), (u2) and (u4). Five terms exactly; (u0) is the fixed-policy cross-derivative
$\partial_{\kappa r}\Delta^{\mathrm{act}}$ of the statement, so the remainder
$$\mathcal E:=\frac{d^2\mathcal D}{d\kappa\,dr}-\partial_{\kappa r}\Delta^{\mathrm{act}}
=\text{(u1)}+\text{(u2)}+\text{(u3)}+\text{(u4)} \tag{8}$$
has exactly four terms. Two facts about (7) are worth naming because they are where a
miscount would hide. First, no term $\Delta_{\kappa\kappa}$ or $\Delta_{rr}$ can appear: the
derivative is mixed, and $\kappa$ and $r$ are each differentiated once. Second, (u4) is the
only place where a **second** derivative of the equilibrium map enters, which is why part
(A) needs its third bound at all; if $\Delta_k=0$ on the region, $\bar k_{\kappa r}$ is not
consumed.

**Step 10 (triangle inequality and the three groups).** Apply the triangle inequality to (8)
and bound each term with the N1 pairings — covector against vector through the dual norm,
bilinear form against two vectors — then insert the Step 6 and Step 7 bounds:
$$
\lvert\mathcal E\rvert
\le\underbrace{\lvert\Delta_{\kappa k}\rvert\,\bar k_r}_{\text{(u1)}\;\to\;G_1}
+\underbrace{\lvert\Delta_{kr}\rvert\,\bar k_\kappa}_{\text{(u2)}\;\to\;G_2}
+\underbrace{\lvert\Delta_{kk}\rvert\,\bar k_r\,\bar k_\kappa}_{\text{(u3)}\;\to\;G_2}
+\underbrace{\lvert\Delta_k\rvert\,\bar k_{\kappa r}}_{\text{(u4)}\;\to\;G_3}.
$$
Collecting the two middle summands over the common factor $\bar k_\kappa$ gives exactly
$$\lvert\mathcal E\rvert\le
\lvert\Delta_{\kappa k}\rvert\bar k_r
+\bigl(\lvert\Delta_{kr}\rvert+\lvert\Delta_{kk}\rvert\bar k_r\bigr)\bar k_\kappa
+\lvert\Delta_k\rvert\bar k_{\kappa r}=\mathcal B_r^{GE}. \tag{9}$$
**Term audit, which is the check this part turns on.** $\mathcal B_r^{GE}$ has three
groups; (8) has four terms; the map is $G_1\leftarrow$(u1), $G_2\leftarrow$(u2)+(u3),
$G_3\leftarrow$(u4). Every cross-term of the second mixed derivative lands in exactly one
group, no group is fed by a term that is not in (8), and the only term of (7) outside the
groups is (u0), which is the object subtracted off. **(B) is proved**, and it is proved as
an equality of bookkeeping, not as an inequality with slack hidden in it: the only
inequalities used are the triangle inequality and the N1 norm pairings.

### Part III — (C): the sign

**Step 11 (what the absolute value is taken of).** $\mathcal S^{GE}=\lvert d\mathcal
D/d\kappa\rvert=\lvert\Delta_k k_\kappa+\Delta_\kappa\rvert$ by (6). This is the equilibrium
object. Card §4.4's $\mathcal S$ is $\lvert\Delta_\kappa\rvert$ — the second summand alone.
The two agree only where $\Delta_kk_\kappa=0$; the whole content of (C) sits in the
difference, so the symbol has to be the equilibrium one (NOTATION DELTA 1, WHERE IT FAILS 4).

**Step 12 (differentiating the absolute value — the licensing step).** Write
$f(\vartheta'):=d\mathcal D/d\kappa$ at $\vartheta'$, and $\mathfrak s(\vartheta'):=
\operatorname{sgn}f(\vartheta')$. By Step 8, $f$ is $C^1$ on $\mathcal R_r$. By H5,
$f\neq0$ on $\mathcal R_r$. Take a connected relatively open neighbourhood $\mathcal
N\subseteq\mathcal R_r$ of $\vartheta$ (N2). A continuous nowhere-zero real function on a
connected set takes values of one sign — otherwise the intermediate value theorem, applied
along a path in $\mathcal N$ joining a point where $f>0$ to one where $f<0$, would produce a
zero of $f$ inside $\mathcal N$, contradicting H5. Hence $\mathfrak s$ is constant on
$\mathcal N$, equal to $\mathfrak s(\vartheta)\in\{-1,+1\}$, and on $\mathcal N$
$$\mathcal S^{GE}=\lvert f\rvert=\mathfrak s(\vartheta)\,f .$$
The right-hand side is $C^1$ on $\mathcal N$ as a constant multiple of a $C^1$ function,
so $\mathcal S^{GE}$ is differentiable at $\vartheta$ with
$$\partial_r\mathcal S^{GE}=\mathfrak s(\vartheta)\,\frac{d^2\mathcal D}{d\kappa\,dr}. \tag{10}$$
Two hypotheses are consumed and neither is dispensable in the same way. H5 removes the one
point at which $x\mapsto\lvert x\rvert$ is not differentiable, and WHERE IT FAILS 3 shows
the conclusion is false without it. H2c's constancy clause is **not** consumed: constancy on
$\mathcal N$ was derived, and (10) is a pointwise statement. H2c would matter only for
naming a single sign across a disconnected $\mathcal R_r$.

**Step 13 (splitting off the direct margin).** Substitute (8) into (10) and use
$\mathfrak s^2=1$:
$$\partial_r\mathcal S^{GE}
=\mathfrak s\,\partial_{\kappa r}\Delta^{\mathrm{act}}+\mathfrak s\,\mathcal E
=-g_r^{PE}+\mathfrak s\,\mathcal E, \tag{11}$$
the last equality being the card §4.5 definition $g_r^{PE}=-\operatorname{sgn}(d
\Delta^{\mathrm{act}}/d\kappa)\,\partial_{\kappa r}\Delta^{\mathrm{act}}$ with the
**equilibrium** sign, which is $\mathfrak s$ by construction (H6's row). All the objects in
(11) are finite by H4.

**Step 14 (dominance closes it).** $\lvert\mathfrak s\,\mathcal E\rvert=\lvert\mathcal
E\rvert\le\mathcal B_r^{GE}$ by (9), so in particular $\mathfrak s\,\mathcal E\le\mathcal
B_r^{GE}$ — only this one-sided half of (B) is consumed. With (11),
$$\partial_r\mathcal S^{GE}\le-g_r^{PE}+\mathcal B_r^{GE}=-\bigl(g_r^{PE}-\mathcal
B_r^{GE}\bigr)=-\eta_r,$$
and $\eta_r>0$ by H6. **(C) is proved**, at every $\vartheta\in\mathcal R_r$, with
$\eta_r$ the card's slack.

**Step 15 (what H2b would have bought).** Nothing above evaluates $D_k\mathcal T$ anywhere
except at points $(k(\vartheta'),\vartheta')$ of the equilibrium graph — Steps 2 and 3
enlarge that to a ball, but the enlargement is obtained by continuity from the graph value,
not by assumption. So H2a suffices throughout and H2b is not consumed. Under H2b, Step 3's
uniqueness would hold on all of $\Theta$ rather than on $\bar B(k^0,\delta)$, and H3's
single-branch clause would become a conclusion instead of a hypothesis. That upgrade is not
claimed here.

**Step 16 (what H8 buys).** At fixed policies, the same argument as Step 12 applied to
$\lvert\partial_\kappa\Delta^{\mathrm{act}}(k^0,\vartheta')\rvert$ — with $k^0$ held fixed
and $\operatorname{sgn}(\partial_\kappa\Delta^{\mathrm{act}})$ in place of $\mathfrak s$ —
gives $\partial_r$ of the fixed-policy sensitivity $=\operatorname{sgn}(\partial_\kappa
\Delta^{\mathrm{act}})\,\partial_{\kappa r}\Delta^{\mathrm{act}}$. Under H8 that sign is
$\mathfrak s$, so the fixed-policy attenuation rate equals $-g_r^{PE}$ and the name "direct
fixed-policy attenuation margin" is accurate. Without H8 the two signs may differ, $g_r^{PE}$
is still the right quantity to compare against $\mathcal B_r^{GE}$ — (11) pulls out
$\mathfrak s$, never the fixed-policy sign — and Steps 13–14 are untouched, but the
sentence "T1's fixed-policy attenuation sign survives in equilibrium" is then a misnomer:
what survives is a sign the fixed-policy object does not have. H8 is consumed here and
nowhere else, exactly as the sheet asserts.

**Step 17 (norm-relativity, recorded not claimed).** Every quantity in (A)–(C) other than
$\partial_{\kappa r}\Delta^{\mathrm{act}}$ and $\mathfrak s$ depends on the N1 norm:
$L_{\mathcal R}$, the $\bar k$'s, $\mathcal B_r^{GE}$ and hence $\eta_r$. Since a matrix with
spectral radius below $1$ has induced operator norm below $1$ in some norm but not
necessarily in a given one, the hypothesis "$L_{\mathcal R}<1$" and the conclusion's slack
are both properties of the pair (region, norm). Concretely, with $D_k\mathcal
T=\bigl(\begin{smallmatrix}0&1.2\\0.5&0\end{smallmatrix}\bigr)$ the $\lVert\cdot\rVert_\infty$
operator norm is $1.2>1$, while the weighted norm $\lVert x\rVert_w=\max\{\lvert
x_1\rvert/1.5,\lvert x_2\rvert\}$ induces $\max\{1.2/1.5,\;0.5\cdot1.5\}=0.8<1$ — the same
node fails to certify in one norm and certifies in the other. This is not a free lunch: the
change of norm also moves $\lVert\mathcal T_x\rVert$ and the dual norms of $\Delta_k$,
$\Delta_{\kappa k}$, $\Delta_{kr}$ inside $\mathcal B_r^{GE}$. The honest reading of the
certificate is therefore existential in the norm, and a numerical implementation is entitled
to search over a family (diagonal weightings, say) rather than fixing $\lVert\cdot\rVert_2$
by default.

### Part IV — (D): the finite-scale statement

**Step 18.** Let $\{\kappa\}\times[r_0,r_1]\subseteq\mathcal R_r$ with $r_0<r_1$. By Step 12
applied at each point of the segment, $r\mapsto\mathcal S^{GE}(\kappa,r)$ is differentiable
there, and by Steps 8 and 12 its derivative $\mathfrak s\,d^2\mathcal D/d\kappa\,dr$ is
continuous in $r$ ($\mathfrak s$ is locally constant along the connected segment by Step 12,
so it is constant on it). The fundamental theorem of calculus therefore gives
$$\mathcal S^{GE}(\kappa,r_1)-\mathcal S^{GE}(\kappa,r_0)=\int_{r_0}^{r_1}\partial_r\mathcal
S^{GE}\,dr\;\le\;-\int_{r_0}^{r_1}\eta_r\,dr,$$
the inequality being Step 14 applied pointwise under the integral. $\eta_r$ is continuous in
$r$ on $[r_0,r_1]$: $g_r^{PE}$ is, because $\partial_{\kappa r}\Delta^{\mathrm{act}}$ is
continuous (H4) and $\mathfrak s$ is constant on the segment; and $\mathcal B_r^{GE}$ is,
because each of its ingredients is a continuous function of $\vartheta$ (H2a, H4, Step 4)
and $L_{\mathcal R}<1$ is a constant. A continuous strictly positive function (H6) on the
compact $[r_0,r_1]$ has a positive minimum, so $\int_{r_0}^{r_1}\eta_r\,dr\ge(r_1-r_0)\min
\eta>0$. **(D) is proved.**

---

## WHERE IT FAILS

1. **Collapsed action region (H3's interiority).** Card §3 permits $k_i=k_{i+1}$, which puts
$k(\vartheta)$ on $\partial\Theta$. There Step 2's ball is not contained in $\Theta$,
$D_k\mathcal T$ is a one-sided object in the collapsing direction, and the fixed-point
condition may hold only as a variational inequality. A cutoff pinned at a face has $k_r=0$
on one side of the pin and $k_r\neq0$ on the other, so $\partial_r\mathcal S^{GE}$ has two
different one-sided values and (C) does not even have a left-hand side. Concretely: any
$\kappa$ at which Hold collapses is outside $\mathcal R_r$ by construction, so a certified
region cannot be reported as an interval straddling such a $\kappa$ without checking
interiority at every node between.

2. **Approach to the contraction boundary.** As $L_{\mathcal R}\uparrow1$ the bounds diverge
at different rates: $\bar k_\kappa,\bar k_r=O\bigl((1-L_{\mathcal R})^{-1}\bigr)$ and,
through the $\lVert\mathcal T_{kk}\rVert\bar k_\kappa\bar k_r$ term of Step 7,
$\bar k_{\kappa r}=O\bigl((1-L_{\mathcal R})^{-3}\bigr)$. So whenever $\Delta_k\neq0$ and
$\mathcal T_{kk}\neq0$, $\mathcal B_r^{GE}=O\bigl((1-L_{\mathcal R})^{-3}\bigr)$ while
$g_r^{PE}$ is unaffected by $L_{\mathcal R}$, and H6 must fail at all $L_{\mathcal R}$ close
enough to $1$. The certified region is therefore bounded away from the contraction boundary
by a *cubic* margin, not a linear one — the single sharpest practical restriction the
certificate carries.

3. **A zero of the equilibrium liquidity derivative (H5).** Take $d\mathcal D/d\kappa=
c\,(r-r_\star)$ with $c>0$ near $r_\star$. Then $\mathcal S^{GE}=\lvert c\rvert\lvert
r-r_\star\rvert$, whose right derivative at $r_\star$ is $+\lvert c\rvert>0$. The conclusion
$\partial_r\mathcal S^{GE}\le-\eta_r<0$ is false there, for any $\eta_r>0$. H5 is thus not
a smoothness convenience: it excises a set on which (C) is refuted. This is the point of
contact with card §9's hump language — an interior extremum of the equilibrium premium in
$\kappa$ is precisely a zero of $d\mathcal D/d\kappa$, and $\mathcal R_r$ must avoid its
neighbourhood.

4. **Reading $\mathcal S$ as card §4.4's fixed-policy object.** If $\mathcal S$ in (C) is
taken to be $\lvert\partial_\kappa\Delta^{\mathrm{act}}\rvert$ with $k$ held fixed, then by
Step 16 $\partial_r\mathcal S=-g_r^{PE}$ exactly, $\mathcal B_r^{GE}$ never enters, part (B)
is unused and H6 reduces to $g_r^{PE}>0$. The theorem would then be a restatement of the
definition of $g_r^{PE}$ and would carry no general-equilibrium content whatsoever. The
symbol collision is therefore not cosmetic; it is the difference between the theorem and a
tautology.

5. **Norm mismatch (N1) — where the norm question bit.** Let $J-1=2$ and certify in
$\lVert\cdot\rVert_\infty$, so that $\bar k_{\kappa r}$ bounds $\lVert
k_{\kappa r}\rVert_\infty$. Suppose $k_{\kappa r}=(1,1)^\top$, giving $\lVert k_{\kappa
r}\rVert_\infty=1$, and suppose $\bar k_{\kappa r}=1$. Let $\Delta_k=(1,1)$. The true term
(u4) is $\Delta_k\,k_{\kappa r}=2$. If $\lvert\Delta_k\rvert$ is read as the Euclidean
length $\sqrt2\approx1.41421$, the group $G_3$ contributes $1.41421<2$, so $\mathcal
B_r^{GE}$ **understates** the remainder and the certificate is void even though every
number in it was computed correctly. The correct pairing is the dual norm of
$\lVert\cdot\rVert_\infty$, namely $\lVert\Delta_k\rVert_1=2$, which restores $G_3=2\ge2$.
Any implementation that mixes $\lVert\cdot\rVert_2$ magnitudes for the $\Delta$-derivatives
with an $\infty$-norm contraction measurement is producing invalid certificates, and the
error is silent — it makes $\eta_r$ look larger, never smaller.

6. **The $r_T$ instance (H7).** Card §4.1 puts $T\in\{1,\dots,H\}$, so $r_T=-T$ is a lattice
coordinate and $\partial_r$, $\mathcal T_{\kappa r}$, $\Delta_{\kappa r}$, $\partial_r
\mathcal S^{GE}$ and the integral of (D) have no meaning without an interpolation of the
model in $T$. H7 imports T1's window-interpolation clause for this instance. Two things go
wrong without it: the derivative-based certificate must be replaced by divided differences
over unit window steps, at which point the Step 10 bookkeeping bounds a *finite difference*
of a *product*, and the Step 7 bound loses its Neumann derivation, whose whole content is
about derivatives. Card §9's item 3 — the O-1 window-margin refutation with $W_TC_T>1$ at
three of four nodes — is independent evidence that the window instance should not be assumed
to inherit the threshold instance's behaviour.

---

## LABEL CLAIMED

**PROVED-WITH-CHANGES**, as a conditional statement on $\mathcal R_r$: under H1, H2a, H3
(with Step 4's reading), H4, H5, H6, H7, N1 and N2, parts (A)–(D) hold as displayed above.
The changes are the two additions N1 and N2, the two readings inside H3 and Step 0, the two
redundancies (H2c for (C); H5 under $\operatorname{sgn}(0)=0$), the confirmation that H8 is
unused for (C), and the $\mathcal S$ symbol collision.

For the card's ledger this is not yet a label move on C1. Two reasons, both external to the
derivation. First, every part is conditional on $\mathcal R_r$ being nonempty, which is a
property of the calibration and is not derivable here. Second, "region-certified" is not a
label (card §7): the honest row is PROVED with the region named in the hypothesis, and the
region is named only by the companion script's nodes, which is a set of nodes and not a
region (the sheet's Step 11 caveat, restated here as NOT CLAIMED 2).

---

## NUMERICAL CHECK REQUEST

**Object.** At each grid node $\vartheta=(\kappa,r_\tau)$, with the equilibrium solved to
fixed-point residual $\le10^{-10}$:

1. $L(\vartheta)=\lVert D_k\mathcal T(k(\vartheta);\vartheta)\rVert$, in **both**
$\lVert\cdot\rVert_\infty$ (max abs row sum) and the best diagonal weighting $w$ found by a
small search; report both, and report which one is used downstream. N1 forbids mixing.
2. $\bar k_\kappa,\bar k_r,\bar k_{\kappa r}$ by the Step 6 and Step 7 formulas, with all
$\mathcal T$-derivatives by central differences at step $h$, $h$ halved until the Richardson
estimate moves by $<1\%$; expect $h\approx10^{-3}$ in $\kappa$ and in $\tau$.
3. $\mathcal B_r^{GE}$ by (9), with the $\Delta$-derivatives in the **dual** norm of the one
chosen at 1.
4. $g_r^{PE}=-\operatorname{sgn}(d\mathcal D/d\kappa)\,\partial_{\kappa r}
\Delta^{\mathrm{act}}$ and $\eta_r=g_r^{PE}-\mathcal B_r^{GE}$.
5. **The independent measurement** the certificate is checked against:
$\widehat{\partial_r\mathcal S^{GE}}=\bigl[\mathcal S^{GE}(\kappa,r+\delta)-\mathcal
S^{GE}(\kappa,r-\delta)\bigr]/(2\delta)$, each $\mathcal S^{GE}$ obtained by **re-solving the
equilibrium** at the shifted parameter — this is what makes it a GE quantity and not a
recomputation of the bound.

**Grid.** $\kappa\in\{0.05,0.10,\dots,0.95\}$ (N2 excludes the endpoints), $\tau$ over the
maintained range at $8$–$10$ points, at the O-1 calibration. This reproduces the 80-node
shape of the 2026-08-21 run.

**Predicted sign.** At every node with $\eta_r>0$: $\widehat{\partial_r\mathcal
S^{GE}}<0$, strictly. At nodes with $\eta_r\le0$: **no prediction** — the certificate is
one-sided.

**Predicted magnitude, three falsifiable numbers.**
(i) $\widehat{\partial_r\mathcal S^{GE}}\le-\eta_r$ at every certifying node, with slack: the
triangle inequality of Step 10 is not generically tight, so expect
$-\widehat{\partial_r\mathcal S^{GE}}$ to sit in $[\eta_r,\;g_r^{PE}+\mathcal B_r^{GE}]$
and, at most nodes, within $10\%$ of $g_r^{PE}$ rather than near $\eta_r$.
(ii) Regressing $\log\mathcal B_r^{GE}$ on $\log\bigl(1/(1-L)\bigr)$ across nodes ordered by
$L$ gives a slope tending to $3$ as $L\uparrow1$ (WHERE IT FAILS 2), and a slope near $1$
only where $\lVert\mathcal T_{kk}\rVert\lvert\Delta_k\rvert$ is negligible. A measured slope
near $2$ at large $L$ indicates a mis-implemented $\bar k_{\kappa r}$.
(iii) Strictly more than $18$ of $80$ nodes should show $\widehat{\partial_r\mathcal
S^{GE}}<0$, the bound being conservative; if exactly the certifying nodes are the negative
ones, the numerics are suspect.

**Falsifiers.** Any node with $\eta_r>0$ and $\widehat{\partial_r\mathcal S^{GE}}>-\eta_r$
refutes either the theorem or the implementation, and the two are separated by re-running
that node in the other norm of item 1 and by halving $\delta$. Any node where the
$\lVert\cdot\rVert_\infty$ and weighted-norm runs disagree on certification is a live
instance of Step 17 and should be reported rather than resolved by fiat.

---

## NOTATION DELTA

Symbols used above that are not in card §4, and one that is:

1. **$\mathcal S^{GE}:=\lvert d\Delta^{\mathrm{act}}(k(\kappa,r),\kappa,r)/d\kappa\rvert$** —
the **equilibrium** liquidity-sensitivity. Introduced because card §4.4 already binds
$\mathcal S=\lvert\partial_\kappa\Delta^{\mathrm{act}}\rvert$ to the **fixed-policy** object
(the same row that carries $\mathcal S=(1-\Omega)\mathcal S_P$, which is T1's fixed-policy
factorisation). The C1 statement sheet uses the bare $\mathcal S$ for the equilibrium
object. Card §4 is not re-keyed here; a new symbol is added instead, and the card row for
C1 should say which object it means (WHERE IT FAILS 4).
2. **$\mathcal D(\kappa,r):=\Delta^{\mathrm{act}}(k(\kappa,r),\kappa,r)$** — the equilibrium
premium, proof-local shorthand for the composed map.
3. **$\mathfrak s(\vartheta):=\operatorname{sgn}(d\Delta^{\mathrm{act}}/d\kappa)$** —
proof-local abbreviation for the equilibrium sign. This is **not** the symbol $\sigma_\kappa$
that card §4.5 forbids: every displayed result above writes the sign inline as
$\operatorname{sgn}(\cdot)$, and $\mathfrak s$ appears only inside proof steps.
4. **$\mathcal E$** — the GE remainder $d^2\mathcal D/d\kappa\,dr-\partial_{\kappa
r}\Delta^{\mathrm{act}}$, the object $\mathcal B_r^{GE}$ bounds.
5. **$\lVert\cdot\rVert$, $\lVert\cdot\rVert_*$** — the N1 norm on $\mathbb R^{J-1}$ and its
dual; also the induced operator and bilinear norms. Card §4.5 writes $\lvert\cdot\rvert$ for
all of these.
6. **$\mathcal T_\kappa,\mathcal T_r,\mathcal T_{kr},D_k\mathcal T$; $\Delta_\kappa,\Delta_k,
\Delta_{kk},\Delta_{\kappa k},\Delta_{kr},\Delta_{\kappa r}$; $k_\kappa,k_r,k_{\kappa r}$** —
subscript shorthand for partials. $\mathcal T_{\kappa r},\mathcal T_{\kappa k},\mathcal
T_{rk},\mathcal T_{kk}$ and the five $\Delta$-derivatives are card §4.5 objects; the rest are
the same convention extended to the derivatives the card does not name.
7. **$\Phi,\hat k,\tilde k,L',\delta,\rho,\bar B(\cdot,\cdot),I,S_N,G_1,G_2,G_3$,
(t1)–(t4), (u0)–(u4)** — proof-local: the zero map of Step 4, the contraction and implicit
solutions, the local contraction modulus, ball radii, closed balls, the identity matrix,
Neumann partial sums, the three groups of $\mathcal B_r^{GE}$, and the term tags of (5) and
(7).
8. **N1, N2** — the two added hypotheses; not card labels.

---

## NOT CLAIMED

1. **Nonemptiness of $\mathcal R_r$.** Nothing above produces a single parameter vector
satisfying H2a–H7. The theorem is an implication and is empty of content until the region is
exhibited by a calibration.
2. **That a set of certifying nodes is a region.** The 2026-08-21 run's 18-of-80 is a finite
sample of a continuum; H2a's supremum and H6's "at every $\vartheta$" are region-wide
statements that node evaluations do not establish. Interpolating between certifying nodes
requires a modulus of continuity for $\eta_r$, which is not derived here.
3. **Norm-independence.** The certificate is existential in the N1 norm (Step 17). No claim
that a node failing in $\lVert\cdot\rVert_2$ fails in every norm, nor that $\eta_r$ has a
norm-free meaning.
4. **Sharpness.** $\mathcal B_r^{GE}$ is an upper bound built from a triangle inequality and
two Neumann bounds; it is generically strict, so $\eta_r>0$ is sufficient for the boxed
conclusion and never necessary. A node with $\eta_r\le0$ is uncertified, not refuted.
5. **Global uniqueness of equilibrium.** Step 3 gives uniqueness in a ball. H2b is not
assumed and no statement about $\Theta$ as a whole is made (card §3 does not claim
uniqueness either).
6. **Anything about the boundary of $\Theta$.** Collapsed action regions are excluded by
H3, not handled (WHERE IT FAILS 1).
7. **The $r_T$ instance.** Proved for $r_\tau=-\tau$ only. For $r_T=-T$ the statement is
conditional on a smooth window interpolation that the card does not supply (H7, WHERE IT
FAILS 6), and card §9's item 3 records that the window margin behaves differently at the O-1
calibration.
8. **That the fixed-policy sensitivity attenuates.** (C) is about $\mathcal S^{GE}$. Whether
the fixed-policy object attenuates in the same direction is H8's content, and H8 is a
hypothesis here, not a conclusion (Step 16).
9. **Any statement about $\Delta^{\mathrm{act}}$ itself.** (C) and (D) bound the $r$-motion
of a *sensitivity*. Nothing above signs $\partial_r\Delta^{\mathrm{act}}$,
$\partial_\kappa\Delta^{\mathrm{act}}$, or the level of the premium.
10. **That T1's PE-$\Omega$ clause is restored.** The card's C1 row notes that
$\partial_\kappa\Omega=0$ fails in GE. Nothing here derives a GE analogue of the
$(1-\Omega)\mathcal S_P$ factorisation; the GE failure is absorbed wholesale into
$\mathcal E$ and bounded, not decomposed.
