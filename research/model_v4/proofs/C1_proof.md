# C1 — GE region certificate

**Ticket 29 (T2i). Written against `research/model_v4/MODEL_CARD.md`, version stamp
2026-08-21 · commit `a175202`+.** Card §4 notation is binding; the answer template is card §8
rule 6. Upstream results are cited by their card-ledger IDs (L1, L2, T1) and by the card's
hypothesis labels (A8, A($\tau$), AGE). The companion executed check is
`quality_reports/fixes/t2_c1_region_check.py` with output
`quality_reports/fixes/t2_c1_region_check.json`.

---

## CLAIM

Fix a window $T$, a plan menu and a strictness coordinate $r$ (card §4.5:
$r_\tau=-\tau$ or $r_T=-T$; higher $r$ = tighter). Let $\mathcal R_r$ be a named set of
parameter vectors $\vartheta=(\kappa,r)$ on which H2–H8 below hold. Then:

**(A) Inversion-free derivative bounds.** The equilibrium cutoff vector $k$ solving
$k=\mathcal T(k;\vartheta)$ is a twice continuously differentiable function of $\vartheta$ on
$\mathcal R_r$, and its derivatives obey the card §4.5 bounds
$$
\lVert\partial_\kappa k\rVert\le\bar k_\kappa=\frac{\lvert\partial_\kappa\mathcal T\rvert}{1-L_{\mathcal R}},
\qquad
\lVert\partial_r k\rVert\le\bar k_r=\frac{\lvert\partial_r\mathcal T\rvert}{1-L_{\mathcal R}},
$$
$$
\lVert\partial^2_{\kappa r}k\rVert\le\bar k_{\kappa r}
=\frac{\lvert\mathcal T_{\kappa r}\rvert+\lvert\mathcal T_{\kappa k}\rvert\bar k_r
+\lvert\mathcal T_{rk}\rvert\bar k_\kappa+\lvert\mathcal T_{kk}\rvert\bar k_\kappa\bar k_r}
{1-L_{\mathcal R}} .
$$
No inverse of $I-D_k\mathcal T$ is formed; each bound is a Neumann geometric sum.

**(B) The GE remainder bound is exactly $\mathcal B_r^{GE}$.** Writing
$\Delta^{\mathrm{act}}(k,\kappa,r)$ for the **fixed-policy** premium of card §4.4 and
$\Delta^{\mathrm{act}}\!\left(k(\kappa,r),\kappa,r\right)$ for its **equilibrium** value, the
equilibrium cross-derivative differs from the fixed-policy one by at most the card §4.5 bound:
$$
\Bigl\lvert
\frac{d^2\Delta^{\mathrm{act}}\!\left(k(\kappa,r),\kappa,r\right)}{d\kappa\,dr}
-\partial_{\kappa r}\Delta^{\mathrm{act}}
\Bigr\rvert
\;\le\;
\mathcal B_r^{GE}
=\lvert\Delta_{\kappa k}\rvert\bar k_r
+\bigl(\lvert\Delta_{kr}\rvert+\lvert\Delta_{kk}\rvert\bar k_r\bigr)\bar k_\kappa
+\lvert\Delta_k\rvert\bar k_{\kappa r}.
$$

**(C) Dominance: the fixed-policy attenuation sign survives in equilibrium.** If in addition
$g_r^{PE}>\mathcal B_r^{GE}$ on $\mathcal R_r$, then writing $\mathcal S$ for the equilibrium
liquidity-sensitivity $\lvert d\Delta^{\mathrm{act}}/d\kappa\rvert$ evaluated along
$k(\kappa,r)$,
$$
\boxed{\;\partial_r\mathcal S\;\le\;-\eta_r\;<\;0
\qquad\text{at every }\vartheta\in\mathcal R_r,\quad \eta_r=g_r^{PE}-\mathcal B_r^{GE}.\;}
$$
Equivalently: tightening the margin strictly attenuates the premium's liquidity-sensitivity in
equilibrium, by at least $\eta_r$ per unit of strictness. Under H8 the same statement reads
"T1's fixed-policy attenuation sign survives in equilibrium on $\mathcal R_r$", which is the
ledger's wording.

**(D) Finite scale.** If $\mathcal R_r$ contains a segment $[r_0,r_1]$ at fixed $\kappa$, then
$\mathcal S(\kappa,r_1)-\mathcal S(\kappa,r_0)\le-\int_{r_0}^{r_1}\eta_r\,dr<0$.

**Nonemptiness of $\mathcal R_r$ is not claimed here and is not provable here** — it is a
property of the calibration, and the companion script is what decides it. See NOT CLAIMED 1. The
run of 2026-08-21 found 18 certifying nodes of 80 and is reported under NUMERICAL CHECK REQUEST;
a set of certified nodes is still not a certified region (Step 11).

---

## HYPOTHESES

Every hypothesis is used; the step that consumes it is named in brackets.

**H1 — Card and stamp.** MODEL_CARD.md, stamp 2026-08-21 · `a175202`+. All symbols carry their
card §4 meanings: $\kappa$ is noise-trading intensity; upright $T$ is the filing window and
$\mathcal T$ is the outer best-response map; $k=(k_1,\dots,k_{J-1})$ is the cutoff vector and
$\Theta$ the compact ordered polytope; $r_\tau=-\tau$, $r_T=-T$. No card symbol is renumbered.
[all steps]

**H2 — AGE (card §5, verbatim).** *"On a candidate region $\mathcal R$ the outer map is twice
continuously differentiable, $L_{\mathcal R}<1$, and the sign of the equilibrium liquidity
derivative is constant on $\mathcal R$."* Two readings of $L_{\mathcal R}=\sup_{\mathcal R}\lVert
D_k\mathcal T\rVert$ (card §4.5) must be kept apart, because different steps need different
ones:

- **(H2a) along-the-path reading.** $L_{\mathcal R}=\sup_{\vartheta\in\mathcal R}\lVert
  D_k\mathcal T(k(\vartheta);\vartheta)\rVert$ — the supremum over parameters of the norm **at
  the equilibrium cutoff vector**. This is what Steps 1–4 need, and it is what the companion
  script measures.
- **(H2b) over-$\Theta$ reading.** $L_{\mathcal R}=\sup_{\vartheta\in\mathcal R}\sup_{k\in\Theta}
  \lVert D_k\mathcal T(k;\vartheta)\rVert$. Strictly stronger, and **not** measured. **No step in
  the proof of (A)–(D) uses it**; Step 12 discusses what it would add, namely the upgrade of
  Step 1's *local* uniqueness to a global one on $\Theta$.

Where "$L_{\mathcal R}<1$" appears below without qualification, H2a is meant. [Steps 1–4, 7, 12]

**H3 — Interior equilibrium on a single branch.** At every $\vartheta\in\mathcal R_r$ there is a
cutoff vector $k(\vartheta)$ in the **interior** of $\Theta$ with $k(\vartheta)=\mathcal
T(k(\vartheta);\vartheta)$, and $\vartheta\mapsto k(\vartheta)$ is one branch — no switch of
selected equilibrium occurs inside $\mathcal R_r$. Interiority is a genuine restriction: card §3
permits collapsed action regions (weak inequalities $k_1\le\dots\le k_{J-1}$), and a collapsed
region puts $k$ on $\partial\Theta$, where the fixed-point equation may hold only as a
variational inequality and $k(\cdot)$ need not be differentiable. [Steps 1, 5, 12]

**H4 — Twice continuous differentiability and boundedness of the premium in
$(k,\kappa,r)$.** The fixed-policy map $(k,\kappa,r)\mapsto\Delta^{\mathrm{act}}(k,\kappa,r)$ of
card §4.4 is twice continuously differentiable on a neighbourhood of
$\{(k(\vartheta),\vartheta):\vartheta\in\mathcal R_r\}$, and the derivatives named in
$\mathcal B_r^{GE}$ — $\Delta_k$, $\Delta_{kk}$, $\Delta_{\kappa k}$, $\Delta_{kr}$,
$\Delta_{\kappa r}$ — together with those named in $\bar k_{\kappa r}$ —
$\mathcal T_{\kappa r},\mathcal T_{\kappa k},\mathcal T_{rk},\mathcal T_{kk}$ — are finite there.
This is the turn-1 C1 hypothesis 4 ("all required first and second derivatives of
$\Delta^{\mathrm{act}}$ and $\mathcal T$ are bounded on the region"), stated with the
differentiability it presupposes. Card §5's **A2′** — local boundedness of prices and payoffs
together with $\mathbb E[\max_j\lvert U_j\rvert]<\infty$, the clause that replaced A2's flat
boundedness when the latter was found false — is **not** cited for it: boundedness is not
differentiability, and A2′ is further from supplying it than A2 was. [Steps 5, 6, 9]

**H5 — Non-vanishing equilibrium liquidity derivative.**
$d\Delta^{\mathrm{act}}\!\left(k(\kappa,r),\kappa,r\right)/d\kappa\neq0$ at every
$\vartheta\in\mathcal R_r$. H2's constancy clause fixes a common sign; H5 is what keeps the
argument of $\lvert\cdot\rvert$ away from the one point where $\lvert\cdot\rvert$ is not
differentiable. The two are separate assertions and both are needed. [Step 7]

**H6 — Strict dominance (card §4.5).** $g_r^{PE}>\mathcal B_r^{GE}$, i.e. $\eta_r>0$, at every
$\vartheta\in\mathcal R_r$, with
$g_r^{PE}=-\operatorname{sgn}\!\left(d\Delta^{\mathrm{act}}/d\kappa\right)
\partial_{\kappa r}\Delta^{\mathrm{act}}$ where the sign is the **equilibrium** liquidity
derivative's, per the card §4.5 row. [Steps 8, 10]

**H7 — A smooth strictness domain.** The coordinate $r$ ranges over an open interval on which
the objects of H2 and H4 are defined. For $r_\tau=-\tau$ card §4.1 places no discreteness on
$\tau$, so only smoothness is being assumed, not a domain. For $r_T=-T$ the card's $T$ ranges
over $\{1,\dots,H\}$, so the $r_T$ instance additionally needs a smooth window interpolation —
the same added hypothesis T1 carries as its H15, imported here unchanged and named where it
bites (WHERE IT FAILS 6). [Steps 3, 4, 5]

**H8 — Sign coherence (used only to name $g_r^{PE}$, never to reach the conclusion).**
$\operatorname{sgn}\bigl(\partial_\kappa\Delta^{\mathrm{act}}(k(\vartheta),\vartheta)\bigr)
=\operatorname{sgn}\bigl(d\Delta^{\mathrm{act}}\!\left(k(\kappa,r),\kappa,r\right)/d\kappa\bigr)$
on $\mathcal R_r$: the fixed-policy and equilibrium liquidity derivatives point the same way.
Card §4.5 defines $g_r^{PE}$ with the **equilibrium** sign but calls it the *fixed-policy*
attenuation margin; H8 is exactly the clause that makes both halves of that name true at once.
The boxed conclusion (C) does **not** use H8 — Step 9 is where it is consumed, and Step 9 is a
statement about what (C) may be called. [Step 9]

---

## PROOF

Throughout, $\lVert\cdot\rVert$ on the cutoff space $\mathbb R^{J-1}$ is $\lVert\cdot\rVert_\infty$
and $\lVert D_k\mathcal T\rVert$ is the induced operator norm (maximum absolute row sum). For the
multilinear objects the card §4.5 bars mean the smallest constants making the displayed products
valid, namely
$$
\lvert\mathcal T_{\kappa k}\rvert=\max_i\sum_l\lvert\mathcal T^i_{\kappa k_l}\rvert,\quad
\lvert\mathcal T_{rk}\rvert=\max_i\sum_l\lvert\mathcal T^i_{r k_l}\rvert,\quad
\lvert\mathcal T_{kk}\rvert=\max_i\sum_{j,l}\lvert\mathcal T^i_{k_jk_l}\rvert,\quad
\lvert\mathcal T_{\kappa r}\rvert=\max_i\lvert\mathcal T^i_{\kappa r}\rvert,
$$
$$
\lvert\Delta_k\rvert=\sum_j\lvert\Delta_{k_j}\rvert,\quad
\lvert\Delta_{\kappa k}\rvert=\sum_j\lvert\Delta_{\kappa k_j}\rvert,\quad
\lvert\Delta_{kr}\rvert=\sum_j\lvert\Delta_{k_jr}\rvert,\quad
\lvert\Delta_{kk}\rvert=\sum_{j,l}\lvert\Delta_{k_jk_l}\rvert .
$$
These are the dual pairings that make the displayed products valid: for the bilinear objects,
$\lvert\mathcal T_{kk}[w_1,w_2]\rvert\le\lvert\mathcal T_{kk}\rvert\lVert w_1\rVert\lVert
w_2\rVert$ and likewise for $\Delta_{kk}$; for the linear ones,
$\lvert\Delta_{\kappa k}[w]\rvert\le\lvert\Delta_{\kappa k}\rvert\lVert w\rVert$ and likewise
for $\mathcal T_{\kappa k},\mathcal T_{rk},\Delta_{kr},\Delta_k$. (Card §4.6 rules $u_1,u_2$
proof-local and forbids a bare $u$, so the arguments here are written $w,w_1,w_2$; $w$ carries no
card meaning.) Card §4.5 writes the bars without fixing a norm, and NOTATION DELTA flags the
choice for the card owner. Any other consistent pairing changes the numerical value of
$\mathcal B_r^{GE}$ but not one line of the argument.

### Part A — the implicit-function step

**Step 1 (the equilibrium is a twice continuously differentiable function of the parameters).**
Define $\Psi(k;\vartheta)=k-\mathcal T(k;\vartheta)$ on a neighbourhood $\mathcal N\subseteq
\operatorname{int}\Theta\times\mathcal R_r$ of the equilibrium graph
$\{(k(\vartheta),\vartheta):\vartheta\in\mathcal R_r\}$ — **the same domain H4 chooses for
$\Delta^{\mathrm{act}}$, and the weakest one Steps 1–4 use**; every $\mathcal T$ derivative below
is evaluated at $(k(\vartheta);\vartheta)$, so smoothness away from the graph is never called on.
(Card §5's AGE says the outer map is twice continuously differentiable "on a candidate region
$\mathcal R$" without saying over which $k$ — the same ambiguity H2a/H2b flags for the norm.
NOTATION DELTA carries it as a card-owner flag; taking the weaker reading here means no step
depends on how it is resolved.) By H2 $\mathcal T$ is twice continuously differentiable on
$\mathcal N$, so $\Psi$ is, and $D_k\Psi=I-D_k\mathcal T$. Fix $\vartheta\in\mathcal R_r$ and let
$w$ satisfy $\lVert w\rVert=1$. By the reverse triangle inequality and H2a,
$$
\lVert(I-D_k\mathcal T)w\rVert\ \ge\ \lVert w\rVert-\lVert D_k\mathcal T\,w\rVert
\ \ge\ 1-L_{\mathcal R}\ >\ 0 .
$$
A linear map on a finite-dimensional space that is bounded below is injective, hence invertible.
By H3, $k(\vartheta)$ is an interior zero of $\Psi(\cdot;\vartheta)$; the implicit function
theorem then supplies a neighbourhood of $\vartheta$ on which the zero is unique and the map
$\vartheta\mapsto k(\vartheta)$ is as smooth as $\Psi$, i.e. twice continuously differentiable.
H3's single-branch clause is what lets these local objects be patched into one function on
$\mathcal R_r$.

**Step 2 (Neumann bound — no inverse is formed).** By H2a, $\lVert D_k\mathcal T\rVert\le
L_{\mathcal R}<1$, so $\sum_{n\ge0}\lVert(D_k\mathcal T)^n\rVert\le\sum_{n\ge0}L_{\mathcal
R}^{\,n}=(1-L_{\mathcal R})^{-1}<\infty$, the series $\sum_{n\ge0}(D_k\mathcal T)^n$ converges
absolutely in operator norm, and multiplying it by $(I-D_k\mathcal T)$ telescopes to $I$. Hence
$$
\bigl\lVert(I-D_k\mathcal T)^{-1}\bigr\rVert\ \le\ \frac{1}{1-L_{\mathcal R}} .
$$
This is the step the word "inversion-free" names: the bound is a geometric sum of norms, so
every derivative bound below is available from $\lVert D_k\mathcal T\rVert$ and one directional
derivative of $\mathcal T$, without solving a linear system.

**Step 3 (first-derivative bounds — the $\bar k_x$ row of card §4.5).** Let $x\in\{\kappa,r\}$;
H7 makes $x$ a coordinate on an open interval. Differentiate the identity
$k(\vartheta)=\mathcal T(k(\vartheta);\vartheta)$ in $x$, which Step 1 licenses, using the chain
rule on the first argument:
$$
\partial_xk=D_k\mathcal T\,\partial_xk+\partial_x\mathcal T
\qquad\Longleftrightarrow\qquad
(I-D_k\mathcal T)\,\partial_xk=\partial_x\mathcal T .
$$
Apply Step 2's operator bound to the right-hand side:
$$
\lVert\partial_xk\rVert\ \le\ \frac{\lVert\partial_x\mathcal T\rVert}{1-L_{\mathcal R}}
\ =\ \bar k_x ,
$$
which is card §4.5's row verbatim. Note which derivative appears on the right: $\partial_x\mathcal
T$ is the **partial** derivative of the best-response map in the parameter, holding $k$ fixed —
the belief-and-price response at frozen cutoffs — not a total derivative.

**Step 4 (the cross-derivative bound — the $\bar k_{\kappa r}$ row).** Differentiate the
$x=\kappa$ instance of Step 3 once more, in $r$. Written in components, with every $\mathcal T$
derivative evaluated at $(k(\vartheta);\vartheta)$ and the chain rule applied through
$k(\vartheta)$ in each slot,
$$
\partial^2_{\kappa r}k^i
=\sum_j\Bigl[\Bigl(\sum_l\mathcal T^i_{k_jk_l}\,\partial_rk^l+\mathcal T^i_{k_jr}\Bigr)\partial_\kappa k^j
+\mathcal T^i_{k_j}\,\partial^2_{\kappa r}k^j\Bigr]
+\sum_l\mathcal T^i_{\kappa k_l}\,\partial_rk^l+\mathcal T^i_{\kappa r},
$$
that is,
$$
(I-D_k\mathcal T)\,\partial^2_{\kappa r}k
=\mathcal T_{\kappa r}
+\mathcal T_{\kappa k}[\partial_rk]
+\mathcal T_{rk}[\partial_\kappa k]
+\mathcal T_{kk}[\partial_rk,\partial_\kappa k].
$$
Take norms on the right using the pairings fixed above and Step 3's bounds
$\lVert\partial_\kappa k\rVert\le\bar k_\kappa$, $\lVert\partial_rk\rVert\le\bar k_r$; then apply
Step 2 once more:
$$
\lVert\partial^2_{\kappa r}k\rVert
\le\frac{\lvert\mathcal T_{\kappa r}\rvert+\lvert\mathcal T_{\kappa k}\rvert\bar k_r
+\lvert\mathcal T_{rk}\rvert\bar k_\kappa+\lvert\mathcal T_{kk}\rvert\bar k_\kappa\bar k_r}
{1-L_{\mathcal R}}=\bar k_{\kappa r},
$$
which is card §4.5's row verbatim. Part (A) of the CLAIM is Steps 1, 3 and 4.

### Part B — the GE remainder

**Step 5 (the exact cross-derivative decomposition).** Write
$\Delta^*(\kappa,r):=\Delta^{\mathrm{act}}\!\left(k(\kappa,r),\kappa,r\right)$. By H4 and Step 1
the composition is twice continuously differentiable on $\mathcal R_r$ (H7 supplies the open
domain in $r$). The chain rule in $\kappa$ gives
$$
\partial_\kappa\Delta^*=\Delta_k\!\cdot\!\partial_\kappa k+\Delta_\kappa ,
$$
and differentiating that in $r$, term by term —
$\partial_r(\Delta_k)=\Delta_{kk}[\partial_rk]+\Delta_{kr}$ and
$\partial_r(\Delta_\kappa)=\Delta_{\kappa k}[\partial_rk]+\Delta_{\kappa r}$ — gives the exact
identity
$$
\partial^2_{r\kappa}\Delta^*
=\underbrace{\Delta_{\kappa r}}_{\text{fixed policy}}
+\underbrace{\Delta_{\kappa k}[\partial_rk]
+\bigl(\Delta_{kr}+\Delta_{kk}[\partial_rk]\bigr)\!\cdot\!\partial_\kappa k
+\Delta_k\!\cdot\!\partial^2_{\kappa r}k}_{\text{GE remainder}} .
$$
Nothing is dropped and no inequality has been used: this is one identity in four groups. The
four groups are the four ways a cutoff response can enter — the pooled-cell composition moving
with the cutoffs as $\kappa$ moves, the cutoffs' own response to the rule, that response's
interaction with the liquidity response, and the premium's first-order exposure to a
second-order cutoff response. The third term of T1's Step 2 display,
$(\partial_\kappa\Omega)(M_F-M_P)$, is the piece of $\Delta_k\!\cdot\!\partial_\kappa k$ that
T1's fixed-policy hypothesis set the equilibrium free of; it reappears here inside the remainder,
which is what T1's NOT CLAIMED 2 said C1 would have to bound.

**Step 6 (the remainder is bounded by $\mathcal B_r^{GE}$).** Apply the triangle inequality to
the three remainder groups of Step 5, then the pairings fixed above, then Step 3 for
$\lVert\partial_\kappa k\rVert$ and $\lVert\partial_rk\rVert$ and Step 4 for
$\lVert\partial^2_{\kappa r}k\rVert$. H4 makes every factor finite. Group by group:
$$
\bigl\lvert\Delta_{\kappa k}[\partial_rk]\bigr\rvert\le\lvert\Delta_{\kappa k}\rvert\bar k_r,\quad
\bigl\lvert\bigl(\Delta_{kr}+\Delta_{kk}[\partial_rk]\bigr)\!\cdot\!\partial_\kappa k\bigr\rvert
\le\bigl(\lvert\Delta_{kr}\rvert+\lvert\Delta_{kk}\rvert\bar k_r\bigr)\bar k_\kappa,\quad
\bigl\lvert\Delta_k\!\cdot\!\partial^2_{\kappa r}k\bigr\rvert\le\lvert\Delta_k\rvert\bar k_{\kappa r} .
$$
Summing the three,
$$
\bigl\lvert\partial^2_{r\kappa}\Delta^*-\Delta_{\kappa r}\bigr\rvert
\ \le\ \lvert\Delta_{\kappa k}\rvert\bar k_r
+\bigl(\lvert\Delta_{kr}\rvert+\lvert\Delta_{kk}\rvert\bar k_r\bigr)\bar k_\kappa
+\lvert\Delta_k\rvert\bar k_{\kappa r}
\ =\ \mathcal B_r^{GE},
$$
card §4.5's row verbatim. This is Part (B) of the CLAIM. Card §4.5 calls this *one admissible*
bound; the wording is exact, and NOT CLAIMED 5 keeps it.

### Part C — dominance

**Step 7 (the equilibrium sensitivity is differentiable, and its $r$-derivative).** By H2's
constancy clause the sign of $d\Delta^*/d\kappa$ is one and the same on $\mathcal R_r$, and by H5
that derivative never vanishes there. Hence on $\mathcal R_r$
$$
\mathcal S\ :=\ \bigl\lvert\partial_\kappa\Delta^*\bigr\rvert
\ =\ \operatorname{sgn}\!\left(\frac{d\Delta^{\mathrm{act}}}{d\kappa}\right)\,\partial_\kappa\Delta^*
$$
is an identity **of functions on $\mathcal R_r$**, not merely of values at one point: the factor
on the right is a constant $\pm1$. Constancy is what permits differentiating it, and H5 is what
keeps $\partial_\kappa\Delta^*$ off the kink of $\lvert\cdot\rvert$. Differentiating in $r$ —
permitted by Step 5's twice continuous differentiability —
$$
\partial_r\mathcal S
=\operatorname{sgn}\!\left(\frac{d\Delta^{\mathrm{act}}}{d\kappa}\right)\,\partial^2_{r\kappa}\Delta^* .
$$

**Step 8 (dominance).** Multiply Step 5's identity by the constant
$\operatorname{sgn}(d\Delta^{\mathrm{act}}/d\kappa)$ and read the first group through card
§4.5's definition of $g_r^{PE}$, which uses that same sign:
$$
\operatorname{sgn}\!\left(\frac{d\Delta^{\mathrm{act}}}{d\kappa}\right)\Delta_{\kappa r}
=-\left[-\operatorname{sgn}\!\left(\frac{d\Delta^{\mathrm{act}}}{d\kappa}\right)\partial_{\kappa r}\Delta^{\mathrm{act}}\right]
=-\,g_r^{PE} .
$$
For the remaining groups, multiplying by a factor of modulus one leaves the modulus alone, so
Step 6 bounds them by $\mathcal B_r^{GE}$. Combining with Step 7,
$$
\partial_r\mathcal S\ =\ -g_r^{PE}
+\operatorname{sgn}\!\left(\frac{d\Delta^{\mathrm{act}}}{d\kappa}\right)\bigl[\text{GE remainder}\bigr]
\ \le\ -g_r^{PE}+\mathcal B_r^{GE}\ =\ -\eta_r .
$$
By H6, $\eta_r>0$, so $\partial_r\mathcal S\le-\eta_r<0$: the boxed conclusion (C). Observe that
the argument never needs the remainder's sign, only its size — which is the whole point of
bounding rather than signing the GE channel.

**Step 9 (what "the fixed-policy attenuation sign survives" means, and where H8 bites).** At
fixed policies T1's object is $\mathcal S(\kappa,\tau,T)=\lvert\partial_\kappa\Delta^{\mathrm{
act}}\rvert$ at a **frozen** $k$, whose $r$-derivative is
$\operatorname{sgn}(\partial_\kappa\Delta^{\mathrm{act}})\,\partial_{\kappa r}\Delta^{\mathrm{
act}}$. Under H8 that leading sign is the same $\pm1$ as the one in $g_r^{PE}$, so the
fixed-policy $r$-derivative equals $-g_r^{PE}$ exactly, and
$$
g_r^{PE}>0\iff\text{strict fixed-policy attenuation at that node.}
$$
Step 8 then reads: fixed-policy attenuation, by a margin exceeding $\mathcal B_r^{GE}$, implies
equilibrium attenuation. Without H8 nothing in Steps 1–8 changes — none of them cites H8 — but
$g_r^{PE}$ would then be an orientation of the cross-derivative by the *equilibrium* sign while
the fixed-policy comparative static ran the other way, and the ledger's phrase "the fixed-policy
attenuation sign" would not describe it. The companion script therefore reports both signs and
the count of nodes where they disagree, rather than assuming coherence.

**Step 10 (finite scale).** Suppose $\mathcal R_r$ contains the segment
$\{(\kappa,r):r\in[r_0,r_1]\}$. By Step 5, $r\mapsto\mathcal S(\kappa,r)$ is continuously
differentiable there, so the fundamental theorem of calculus and Step 8 give
$$
\mathcal S(\kappa,r_1)-\mathcal S(\kappa,r_0)=\int_{r_0}^{r_1}\partial_r\mathcal S\,dr
\ \le\ -\int_{r_0}^{r_1}\eta_r\,dr\ <\ 0 ,
$$
the last inequality because $\eta_r>0$ (H6) and continuous on a segment of positive length.
Continuity of $\eta_r$ is not an extra assumption; it is already on the table. $g_r^{PE}$ is
continuous because $\partial_{\kappa r}\Delta^{\mathrm{act}}$ is (H4's $C^2$ clause, along the
$C^2$ path $k(\cdot)$ of Step 1) and its $\pm1$ prefactor is constant on $\mathcal R_r$ (Step 7);
$\mathcal B_r^{GE}$ is continuous because each factor in it is a continuous derivative of
$\mathcal T$ or $\Delta^{\mathrm{act}}$ (H2, H4) composed with the continuous $\bar k_x$, all
divided by the **region-constant** $1-L_{\mathcal R}$. A positive continuous function on a
segment of positive length has a positive integral. (Measurability plus positivity would suffice
just as well, and is the cheaper route if one prefers not to invoke H4 here.) This
is Part (D), and it is the form an empirical comparison of two rules can use: a bound on the
level change, not merely a sign at a point.

**Step 11 (a grid of certified nodes is not yet a certified region).** Steps 1–10 are
statements at each $\vartheta\in\mathcal R_r$; a numerical run evaluates them at finitely many
nodes. Certified nodes promote to a certified region only with a modulus of continuity: if
$\vartheta\mapsto\eta_r(\vartheta)$ is Lipschitz with constant $M$ on the convex hull of two
adjacent nodes at distance $\delta$, and $\eta_r\ge\eta_{\min}$ at both, then
$\eta_r\ge\eta_{\min}-M\delta/2$ on the hull, which is positive exactly when
$\eta_{\min}>M\delta/2$. **The companion script does not estimate $M$**, so what it reports is a
set of certified nodes, and the promotion to a region is an explicit open item rather than a
silent interpolation. The same gap applies to $L_{\mathcal R}$: a supremum over $\mathcal R$
cannot be read off finitely many nodes.

**Step 12 (what H2b would add, and why no step needs it).** Under H2b, $\mathcal
T(\cdot;\vartheta)$ is a contraction on the convex compact $\Theta$ (card §4.5), so Banach's
theorem gives a **unique** fixed point in $\Theta$ at that $\vartheta$, H3's single-branch clause
becomes automatic, and the equilibrium selection cannot jump. Under H2a alone, Step 1 gives only
local uniqueness near $k(\vartheta)$, and H3 carries the branch. The distinction is recorded
because the companion script measures the along-the-path norm and therefore certifies under H2a;
claiming uniqueness from it would be an over-read. Card §3's "Uniqueness is **not** claimed"
stands.

---

## WHERE IT FAILS

1. **$L_{\mathcal R}\ge1$ anywhere on $\mathcal R_r$.** $L_{\mathcal R}$ is a supremum, so a
   single parameter vector at which $\lVert D_k\mathcal T\rVert\ge1$ voids the certificate on the
   **whole** region, not only at that vector. Three things break at once: Step 2's Neumann series
   diverges; $1-L_{\mathcal R}\le0$ makes every $\bar k$ meaningless (negative or infinite); and
   if $1$ is an eigenvalue of $D_k\mathcal T$ then $I-D_k\mathcal T$ is singular, Step 1's
   implicit function theorem does not apply, and the equilibrium cutoff vector need not be a
   function of $\vartheta$ at all — a continuum of equilibrium cutoffs at one parameter is exactly
   the configuration $L_{\mathcal R}=1$ permits. Nothing in the certificate can be salvaged
   node-by-node in that case, because the objects $\bar k_x$ are region-level.

2. **A sign change of the equilibrium liquidity derivative inside $\mathcal R_r$** — AGE's
   constancy clause failing. At a parameter where $d\Delta^{\mathrm{act}}/d\kappa=0$ the function
   $\mathcal S=\lvert\partial_\kappa\Delta^*\rvert$ has a kink, $\partial_r\mathcal S$ does not
   exist, and Step 7's identity of functions is false on any set straddling the crossing (the
   $\pm1$ factor is not constant there). This is a live configuration, not a hypothetical: the
   committed smoke run (`numerical_v4/smoke_output.txt`) shows $M_P$ hump-shaped in $\kappa$ at
   the baseline calibration with $dM_P/d\kappa$ changing sign near $\kappa\approx0.55$, so any
   candidate region containing that peak violates the clause. A region must be carved to one side
   of the turning point, and doing so is what makes the certificate regional rather than global.

3. **The equilibrium leaves the interior of $\Theta$** — H3 failing. Card §3's weak inequalities
   permit a collapsed action region (draft_v2's baseline collapses Hold, $k_1=k_0$). On
   $\partial\Theta$ the equilibrium is characterised by a one-sided condition rather than
   $k=\mathcal T(k;\vartheta)$ as an interior equation, the implicit function theorem of Step 1
   does not apply, and $k(\cdot)$ can be non-differentiable — typically with a kink exactly where
   a region collapses, which is where comparative statics are most interesting.

4. **Multiple equilibria with a discontinuous selection.** Even where the local implicit function
   theorem applies to each branch, a switch of selected branch inside $\mathcal R_r$ makes
   $k(\cdot)$ jump, so $\partial_\kappa k$, $\partial_rk$ and $\partial^2_{\kappa r}k$ do not
   exist at the switch and Steps 3–5 are void. Under H2a this cannot be excluded; under H2b it
   can (Step 12).

5. **$\eta_r\le0$: no certificate, and no counter-claim either.** If $g_r^{PE}\le\mathcal
   B_r^{GE}$ the argument stops at Step 6 and says nothing about the sign of
   $\partial_r\mathcal S$. Because $\mathcal B_r^{GE}$ is a triangle-inequality bound, a failure
   of dominance is compatible with equilibrium attenuation, with equilibrium amplification, and
   with equality. Reading $\eta_r\le0$ as evidence against attenuation is a misuse of the
   certificate.

6. **The window instance without a smooth interpolation.** For $r_T=-T$ the card's window is an
   integer, $T\in\{1,\dots,H\}$ (card §4.1). Every derivative in Steps 3–8 taken with $x=r_T$
   then fails to exist, and $\partial_{\kappa r_T}\Delta^{\mathrm{act}}$ — hence $g_{r_T}^{PE}$
   itself — is undefined. H7 imports T1's H15 to supply an interpolation; without it the window
   instance of C1 has no content, and only the threshold instance $r_\tau=-\tau$ is available from
   the card alone. The companion script computes no $r_T$ certificate for this reason.

7. **A quantised threshold map: $\Delta^{\mathrm{act}}$ not differentiable in $\tau$, or locally
   constant in it.** H4 asks for a twice continuously differentiable
   $(k,\kappa,r)\mapsto\Delta^{\mathrm{act}}$. Two distinct failures live here and the second is
   easy to miss. (i) If the flagged set moves in jumps as $\tau$ falls — which happens whenever
   the crossing date is an integer-valued function of $\tau$, as card §4.2's
   $c_j=\inf\{d:B_j(s,d)\ge\tau\}$ makes it on a discrete calendar — then $\Omega(\cdot,T)$ is a
   step function of $\tau$, $\Delta^{\mathrm{act}}$ inherits the jumps, and
   $\partial_{\kappa r}\Delta^{\mathrm{act}}$ does not exist at them. This is T1's H18 failure
   mode, seen from the other side. (ii) **Between** the jumps the same discreteness makes
   $\Delta^{\mathrm{act}}$ locally *constant* in $\tau$, so $\partial_{\kappa r}\Delta^{\mathrm{
   act}}=0$ exactly and $g_r^{PE}=0$: H6 fails not because the GE remainder is large but because
   the direct margin is null. A node in that situation reports $\eta_r=-\mathcal B_r^{GE}\le0$ and
   is uncertifiable for a reason that has nothing to do with general equilibrium. The companion
   script separates the two attributions and reports the counts.

8. **$\mathcal T$ or $\Delta^{\mathrm{act}}$ not twice differentiable for a pricing reason** —
   H4 or H2's smoothness clause failing where card §5's A5 (unique, continuous inner price fixed
   point) holds but is not $C^2$ in beliefs, or where an off-path type's weight crosses zero and
   the belief map is only continuous. Continuity of $\mathcal T$ is what card §5's A6 supplies;
   AGE asks for more, and asks for it only on $\mathcal R$.

---

## LABEL CLAIMED

**CONJECTURE**, and two reasons carry it independently:

1. **Protocol.** Card §6: a result becomes PROVED only after an independent statements-only
   re-derivation PASS *and* an adversarial proof-read PASS, by different agents. The proof-read
   passed on 2026-08-21; the re-derivation is outstanding. This file is one half of the gate.
2. **No named region.** Card §6's intended-label row reads "C1 PROVED on a named **nonempty**
   region, NUMERICAL off-region, dropped if the region is empty." Parts (A)–(D) are implications;
   whether their antecedent is ever satisfied at the maintained calibration is decided by the
   companion script, not by this file. **The run did not come back empty** — 18 of 80 nodes
   certify, nine of them in one contiguous sign-homogeneous block — but that is a set of *nodes*.
   Naming a *region* needs Step 11's modulus of continuity, which no run in hand supplies, so the
   row's antecedent is not met either.

### The three objects, and the label each can carry

Passing both halves of the gate would not license one label but three, on three different
objects. Only the second has ever been in doubt.

1. **The certificate implication — (A), (B), (C), (D) read as conditionals** ("on a region where
   H2–H8 hold, …"). This is a pure implication. Its truth does not depend on any region being
   nonempty, and it is the object this file actually proves. **PROVED-eligible**, pending the
   re-derivation, with $\mathcal R_r$ carried as a **named hypothesis** — which is exactly what
   card §7 means by "Region-certified is not a fifth label: it is PROVED with the region named in
   the hypothesis." Card §6's C1 row must absorb the full hypothesis set before any label
   attaches: the row names only $L_{\mathcal R}<1$ and $g_r^{PE}>\mathcal B_r^{GE}$, omitting H3
   (interior equilibrium on a single branch), H4 ($C^2$ premium), H5 (non-vanishing equilibrium
   liquidity derivative) and H7 (a smooth strictness domain), and it does not separate H8's
   naming role from H6's use. Labelled against the row as written, C1 would be labelled against a
   statement this file does not prove.
2. **The 18 certified nodes — NUMERICAL, and nothing more.** Card §7's definition — "verified on
   a grid by an executed, committed check script with committed output" — fits them exactly. They
   are evidence that H2–H8 are jointly satisfiable at the maintained calibration. They are not a
   region.
3. **"C1 PROVED on a named nonempty region $\mathcal R_r$" — not available, and not obtainable
   from any run of this script.** That phrasing asserts the antecedent, and asserting it needs a
   set with interior plus a genuine supremum over that set. Step 11's Lipschitz constant $M$ is
   not estimated, and $L_{\mathcal R}$ is measured *pointwise along the equilibrium path*, node
   by node — a supremum over $\mathcal R$ cannot be read off finitely many evaluations. **No
   amount of grid refinement fixes this**: it needs a modulus of continuity for $\eta_r$ and a
   genuine supremum for $L_{\mathcal R}$, not more nodes. A live in-repo template for the
   promotion already exists — `quality_reports/fixes/d8_ge_dominance_check.py` certifies a
   *region* rather than a node set, by "(R1) pointwise dominance off an $\varepsilon$-ball around
   the channel-A peak and (R2) integral control inside it", and Part (D)'s integral form is the
   natural (R2) analogue here. A follow-on ticket should start from that construction rather than
   from a bare Lipschitz estimate.

The ledger row this file supports, once the re-derivation passes, is therefore: *C1 — the
certificate implication — **PROVED**, with $\mathcal R_r$ a hypothesis and H2–H8 named in full;
**NUMERICAL**: 18 of 80 nodes satisfy the hypothesis set at the maintained calibration, 9 of them
contiguous and sign-homogeneous; the promotion of certified nodes to a certified region
**OPEN**.* Until then the label is CONJECTURE and this file does not edit the ledger
(NOT CLAIMED 11).

### What C1 inherits from upstream, and what it does not

The economic content of the word "attenuation" is T1's, and C1 inherits T1's **conditionality**,
not its label. Card §6 now carries **T1 = PROVED at fixed policies** (proof-read, fix round
closed, re-derivation PASS, 2026-08-21). What propagates is the openness underneath it:
A($\tau$)'s applicability to the two-round pooled cell (card §9 item 1, **OPEN**); A(br) with its
clause (br-v) **assumed**; and A7′, whose *satisfiability* is resolved (card §5's ticket-24 note,
card §9) while its equilibrium selection — whether an equilibrium in which the separating plan is
actually *chosen* exists — remains card §9 item 2, **OPEN**. None of this moves C1's label in
either direction: reasons 1 and 2 above each hold it at CONJECTURE on their own.

The certificate's own hypotheses AGE, H3 and H4 are additionally not verified anywhere: the
companion script *measures* $L_{\mathcal R}$ along the equilibrium path but does not establish
AGE's differentiability clause, and no run can (WHERE IT FAILS 8). H3 is tested only as
$k_1<k_2$, which rules out the collapse faces of $\Theta$ but not its outer box faces, and H4 is
probed only by the curvature-to-slope diagnostic reported in the OUTCOME.

---

## NUMERICAL CHECK REQUEST

Executed as `quality_reports/fixes/t2_c1_region_check.py`; raw output
`quality_reports/fixes/t2_c1_region_check.json`.

**Formulas.** At each node $(\kappa,\tau,T)$: solve $k=\mathcal T(k;\vartheta)$; take a 33-point
second-order central stencil in $(k_1,k_2,\kappa,\tau)$ of both $\mathcal T$ and the
fixed-policy $\Delta^{\mathrm{act}}$; assemble
$L_{\mathcal R}=\lVert D_k\mathcal T\rVert_\infty$, then $\bar k_\kappa,\bar k_r$ (Step 3),
$\bar k_{\kappa r}$ (Step 4), $\mathcal B_r^{GE}$ (Step 6), and
$g_r^{PE}=-\operatorname{sgn}(d\Delta^{\mathrm{act}}/d\kappa)\,\partial_{\kappa r}\Delta^{\mathrm{
act}}$ with $r=r_\tau=-\tau$ and the sign taken from a re-solved equilibrium sweep in $\kappa$.
Report $\eta_r=g_r^{PE}-\mathcal B_r^{GE}$ and certify when $L_{\mathcal R}<1$ and $\eta_r>0$.

**Grid.** $\kappa\in[0.15,0.85]$, $T\in\{5,10\}$, $\tau$ at the 10th, 30th, 50th, 70th and 90th
percentiles of the baseline equilibrium's Voice $b^*(s)$, frozen once and reused (the 50th is the
committed $0.09076406$). **The $\kappa$ step is sized to the solver, not to the request.**
Measured: a 33-point stencil is about 40 s (each point is one pooled pass with run-up, one outer
map and one premium); a warm-started equilibrium re-solve at a *perturbed* parameter is about
43 s, because the solver drives $\lVert k-\mathcal T(k)\rVert$ to $10^{-10}$ and each damped
iteration costs a full pooled pass. A node without validation re-solves runs in 70–110 s; with
them, about 300 s. The requested $0.01$ grid is $71\times5\times2=710$ nodes, i.e. more than
eight hours before any validation, and **was not run**. The grid run is $\kappa$ step $0.10$,
i.e. $8\times5\times2=80$ nodes, with the six-re-solve validation on eight nodes spanning both
windows, the 10th/50th/90th thresholds and three liquidity levels. The JSON records the grid used
**and** the grid declined. A coarser certified grid honestly reported is the deliverable.

**Two readings of the equilibrium cross-derivative, and which nodes get which.** At every node
the equilibrium liquidity derivative and the equilibrium cross-derivative are read off the
implicit-function formula of Steps 3–5 — free, because the stencil already carries every
ingredient. At the eight validation nodes they are additionally read off re-solved equilibria,
which shares no arithmetic with the bound. The agreement of the two on the first derivative is
what licenses using the free reading elsewhere, and it is reported as a gating check.

**Predicted signs and magnitudes.**

*Block 1 — contraction.* $L_{\mathcal R}<1$ at every node, with the along-the-path reading (H2a)
named in the output. Any node with $L_{\mathcal R}\ge1$ is to be listed, not averaged away.

*Block 2 — the bound must contain the truth (the only verdict that can fail on substance).*
Compute $\partial^2_{r\kappa}\Delta^*$ twice by routes that do not share the bound's arithmetic:
by re-solving the equilibrium at the four corners $(\kappa\pm\varepsilon_\kappa,
\tau\pm\varepsilon_\tau)$ and cross-differencing, and by the implicit-function assembly of Steps 3–5. Then require
$$
\bigl\lvert\partial^2_{r\kappa}\Delta^*-\Delta_{\kappa r}\bigr\rvert\ \le\ \mathcal B_r^{GE}
$$
at every node with $L_{\mathcal R}<1$. *Predicted sign:* no violations. *Predicted magnitude:* the
ratio $\lvert\text{remainder}\rvert/\mathcal B_r^{GE}$ strictly below one and reported; a ratio
above one means Step 6's inequality is mis-assembled or the stencil straddles a kink, and is a
bug in one of the two, never evidence against the theorem. Separately, the two readings of
$d\Delta^*/d\kappa$ — re-solved and implicit-function — must agree to $5\times10^{-3}$ relative,
which is the executed test of Step 3's linear system.

*Block 3 — the certificate.* Report the count of certifying nodes, where they sit, and
$\min$/median/$\max$ of $\eta_r$ over them. **If no node certifies, the script must print
"EMPTY REGION" explicitly**; card §6 makes that a result, and no tolerance may be loosened to
avoid it. *No positive region size is predicted before the run.*

*Block 4 — failure attribution.* For every uncertified node say which hypothesis failed:
$L_{\mathcal R}\ge1$; $g_r^{PE}=0$ to machine precision (WHERE IT FAILS 7(ii) — the threshold map
is locally constant, so the direct margin is null and general equilibrium is not the reason);
$g_r^{PE}>0$ but dominated by $\mathcal B_r^{GE}$ (the genuine GE failure); or $g_r^{PE}<0$
(fixed-policy amplification at that node, under H8). *Predicted:* the three attributions are
mutually exclusive and their counts sum to the uncertified total.

*Block 5 — AGE's constancy clause, tested rather than assumed.* On each $(\tau,T)$ slice report
the sign of $d\Delta^{\mathrm{act}}/d\kappa$ at every $\kappa$ and the number of sign changes.
*Predicted sign:* at least one slice shows a change, because the committed smoke run has $M_P$
hump-shaped in $\kappa$ near $\kappa\approx0.55$. A slice with a change may not be taken whole as
$\mathcal R_r$ (WHERE IT FAILS 2). Also report the count of nodes where the fixed-policy and
equilibrium signs disagree, which is H8's diagnostic.

*Block 6 — A8 and A5 hygiene.* Report $\Omega$ at every node, flagging nodes with flagged-cell
mass below $0.01$ (A8 failing), the count of multiple-root pricing nodes (A5 failing), the count
of nodes with $k_1\ge k_2$ (H3's interiority failing), and the worst equilibrium solve residual.
*Predicted:* $\Omega$ collapses at $T=H$, because $T=H$ forces $c=0$ on every flagged history
(card §4.3's $P_{-1}^P$ row, turn-2 audit D1-R3), and $H=10$ in this calibration makes $T=10$
that corner. Such nodes are recorded as degenerate rather than dropped.

*Block 7 — the finite-scale secant, as a NUMERICAL side-record.* The five frozen $\tau$
percentiles are a finite tightening ladder, so across each adjacent pair report the secant
analogues of the fixed-policy and equilibrium margins, oriented by the equilibrium sign, and
whether they agree in orientation. *This is not the certificate*, which is a derivative
statement; it is the finite-difference reading of the same question, available at no extra cost,
and it is labelled NUMERICAL wherever it is quoted.

*Block 8 — the window margin, discretely.* Report $\mathcal S$ in equilibrium at $T=5$ against
$T=10$ at each $(\kappa,\tau)$, with $\Omega$ at both. *Predicted sign:* none. No $r_T$
certificate is computed (WHERE IT FAILS 6) and this block is a record.

*Block 9 — the price of the inversion-free step, as a RECORD.* Alongside $\mathcal B_r^{GE}$
report the same three groups of Step 6 with the **exactly solved** norms
$\lVert\partial_rk\rVert$, $\lVert\partial_\kappa k\rVert$, $\lVert\partial^2_{\kappa r}k\rVert$
in place of $\bar k_r$, $\bar k_\kappa$, $\bar k_{\kappa r}$, and the count of nodes that would
certify under it. **That object is not card §4.5's $\mathcal B_r^{GE}$ and certifies nothing** —
it needs $(I-D_k\mathcal T)^{-1}$, which is exactly what the card's rows avoid. Its only purpose
is to separate two very different reasons a node can fail: the GE channel is genuinely large, or
the Neumann step threw away too much. *Predicted magnitude:* the ratio
$\mathcal B_r^{GE}/\mathcal B_r^{GE,\text{sharp}}$ strictly above one at every node, and the
realised remainder well below both. A large gap is a **card-owner finding** (NOT CLAIMED 5), not
a result of this file.

### OUTCOME OF THE RUN (executed 2026-08-21, 10 339 s wall, exit code 0)

Recorded here because the request and its answer belong together; the card §8 rule 6 headings are
unchanged. Every number below is in the JSON, and none of it moves the ledger (NOT CLAIMED 11).

**The region is NOT empty.** 80 nodes, 0 errors, **18 certified** ($L_{\mathcal R}<1$ and
$\eta_r>0$), all at $T=5$ and at the 50th, 70th and 90th $\tau$ percentiles. Slack on the
certified nodes: $\eta_r$ minimum $0.0595$, median $0.3467$, maximum $1.7227$.

**Live margin against null margin — every ratio in this section is reported on the live subset.**
Of the 80 nodes, **24 carry a live threshold margin** ($\lvert g_r^{PE}\rvert$ above rounding
scale) and **56 do not**: at those 56 the flagged set does not move with $\tau$, so $g_r^{PE}$
and $\mathcal B_r^{GE}$ are both at $10^{-13}$ and every ratio built from them is a ratio of
rounding noise (WHERE IT FAILS 7(ii)). Pooling the two populations moves every aggregate
magnitude below, and not in one direction, so each is given three ways:

| Statistic | Pooled (80 nodes) | **Live margin (24)** | Null margin (48 with $\mathcal B_r^{GE}>0$) |
|---|---|---|---|
| realised remainder $/\ \mathcal B_r^{GE}$, median | 0.219 | **0.094** | 0.314 |
| realised remainder $/\ \mathcal B_r^{GE}$, maximum | 1.00 | **0.306** | 1.00 |
| $\mathcal B_r^{GE}/\mathcal B_r^{GE,\text{sharp}}$, median | 2.09 | **2.41** | 1.92 |
| $\mathcal B_r^{GE}/\mathcal B_r^{GE,\text{sharp}}$, maximum | 10.3 | **8.29** | 10.3 |

On the nodes that carry content the bound is *tighter* than the pooled figure suggests ($0.094$,
not $0.22$) and the Neumann step is *costlier* ($2.41$, not $2.09$). All 18 certified nodes are
live-margin nodes.

**One contiguous, sign-homogeneous block.** AGE's constancy clause is what carves the certified
nodes into candidate regions, and it bites: **all ten** $(\tau,T)$ slices show exactly one sign
change of the equilibrium liquidity derivative, between $\kappa=0.45$ and $\kappa=0.55$ — the
smoke run's $M_P$ hump, as WHERE IT FAILS 2 predicted. Splitting there, the largest set of nodes
that is contiguous in $\kappa$, certified throughout, and carries one sign is
$$
T=5,\qquad \tau\in\{\text{50th},\text{70th},\text{90th percentile}\},\qquad
\kappa\in\{0.65,0.75,0.85\},
$$
nine nodes, every one certified, the equilibrium liquidity derivative negative throughout,
$\eta_r$ minimum $0.2282$, median $0.3739$. On the low-$\kappa$ side ($\kappa\le0.45$, sign
positive) 9 of 12 nodes certify but not contiguously. **Nine certified nodes are still nine
nodes and not a region** — Step 11 stands, and promoting them needs the modulus of continuity the
script does not estimate.

**Checks.** All four PASS/FAIL verdicts pass, no FAILs, eight RECORDs.
$\lvert\partial^2_{r\kappa}\Delta^*-\Delta_{\kappa r}\rvert\le\mathcal B_r^{GE}$ holds at every
node under both readings, and the two readings differ in how much they are worth:

- *Implicit-function reading, all 80 nodes.* No violation. Maximum ratio $1.00$ pooled and
  **$0.306$ on the live-margin subset**. The ratio reaches $1.00$ only at
  $(T{=}10,\text{q}50,\kappa{=}0.35)$ and $(T{=}10,\text{q}50,\kappa{=}0.45)$, where bound and
  remainder are both at rounding scale ($\mathcal B_r^{GE}=1.6$ and $2.6\times10^{-13}$) —
  tightness in a trivial sense only. The containment test carries an **absolute** slack of
  $10^{-6}$, which at the 56 null-margin nodes exceeds both quantities on its own, so the check's
  headline "80 nodes checked, 0 violations" has an effective coverage of **24**. (Containment
  does hold at all 80 with the slack removed — maximum ratio $1.00$ — so nothing is being
  concealed; the count is simply broader than the evidence behind it.)
- *Four-corner re-solve — the only route that shares no arithmetic with the bound.* It runs at 8
  validation nodes, **four of which are null-margin**, and it touches **2 of the 18 certified
  nodes**, $(T{=}5,\text{q}50,\kappa{=}0.25)$ and $(T{=}5,\text{q}50,\kappa{=}0.85)$. On the four
  live-margin validation nodes the realised remainder is at most **$0.310$** of the bound. The
  pooled maximum $0.511$ comes from $(T{=}10,\text{q}10,\kappa{=}0.55)$, where
  $\mathcal B_r^{GE}=7.6\times10^{-13}$ against a remainder of $3.9\times10^{-13}$ — noise over
  noise, and not a statement about tightness. The independent cross-validation of this
  certificate is therefore narrower than "eight validation nodes" sounds.
- *The two independent readings of the equilibrium derivatives, and the run's strongest evidence.*
  On the **first** derivative they agree to $1.8\times10^{-3}$ relative, inside the
  $5\times10^{-3}$ gate; this is the executed test of Step 3's linear system. On the **cross**
  derivative the check records a pooled `max_rel_diff_cross` of $0.535$, which is a null-margin
  artefact: node by node the large disagreements are $0.78$, $1.23$ and $1.00$ at three
  null-margin nodes (a fourth is $0/0$), while **on every live-margin validation node the two
  readings of the equilibrium cross-derivative agree to better than $0.4\,\%$** — $3.8\times
  10^{-3}$, $2.8\times10^{-3}$, $1.6\times10^{-3}$ and $2.2\times10^{-4}$. Two routes that share
  no arithmetic — a four-corner equilibrium re-solve and the implicit-function assembly of
  Steps 3–5 — land within four parts in a thousand of each other wherever the margin is live.
  That is what licenses reading the equilibrium cross-derivative off the free implicit-function
  formula at the 72 unvalidated nodes, and it is the single strongest thing the run establishes.

$L_{\mathcal R}\in[0.264,0.501]$ at every node, none at or above one. Fixed-policy and
equilibrium liquidity-derivative signs agree at every one of the 80 nodes, so H8 holds throughout
and $g_r^{PE}$ deserves its name here.

**Why the other 62 nodes do not certify — three attributions, mutually exclusive.**

- **56 nodes: $g_r^{PE}=0$ to machine precision.** WHERE IT FAILS 7(ii), confirmed. These are the
  10th and 30th $\tau$ percentiles at $T=5$ and **all** of $T=10$: the flagged set does not move
  with $\tau$ there, so $\Omega$, $\Delta^{\mathrm{act}}$, and $\mathcal T$ are all locally
  constant in $\tau$, and $\mathcal B_r^{GE}$ collapses with $g_r^{PE}$ (both at $10^{-13}$).
  Nothing about general equilibrium is being reported at those nodes; the threshold margin has no
  local content there.
- **4 nodes: $g_r^{PE}>0$ but dominated** — the genuine GE failure (WHERE IT FAILS 5), at
  $(T{=}5,\text{q}50,\kappa{=}0.35)$, $(T{=}5,\text{q}50,\kappa{=}0.55)$,
  $(T{=}5,\text{q}70,\kappa{=}0.35)$ and $(T{=}5,\text{q}90,\kappa{=}0.25)$.
- **2 nodes: $g_r^{PE}<0$** — fixed-policy amplification, both at $\kappa=0.55$, i.e. adjacent to
  the sign change, where the region would be void anyway.

**H4's $\tau$-smoothness was measured at every node, and it did not bite where it would matter.**
WHERE IT FAILS 7(i) is the hazard that the quantised legal clock — the implementation takes
$c=\lceil\cdot\rceil$ — puts a jump of $\Delta^{\mathrm{act}}$ *inside* a $\tau$-stencil, which
would void H4 exactly where the certificate needs it. The obvious adversarial reading of
WHERE IT FAILS 7 is that (i) and (ii) exhaust the possibilities, so that any node with
$g_r^{PE}\neq0$ must be one whose stencil straddles a jump — that is, that the certified nodes
would be precisely the nodes where H4 fails. The script carries a diagnostic that settles this,
$$
\text{(kink ratio)}\;=\;
\frac{\bigl\lvert\partial^2_{\tau\tau}\Delta^{\mathrm{act}}\bigr\rvert\,\varepsilon_\tau}
{\bigl\lvert\partial_\tau\Delta^{\mathrm{act}}\bigr\rvert},
$$
the curvature-to-slope ratio over one stencil half-width, which blows up when a jump sits inside
the stencil. **At all 18 certified nodes it is finite and below $0.68$** — minimum $0.047$,
median $0.317$, maximum $0.673$ — so the second-order term is a fraction of the first over one
stencil width and the certified nodes sit in smooth $\tau$-patches. Nineteen nodes have a ratio
above one, and **every one of them is a null-margin node** (cells $(T{=}5,\text{q}10)$,
$(T{=}5,\text{q}30)$ and all of $T=10$), where $\lvert\partial_\tau\Delta^{\mathrm{act}}\rvert$
is at rounding scale and the ratio is noise in its denominator. This does not *verify* H4, which
no run can (NOT CLAIMED 7); it converts WHERE IT FAILS 7(i) from an unmeasured hazard into a
measured one that did not fire on any node that certifies. It is the only executed evidence in
the run that bears on H4.

**Block 7 — the finite-scale secant, answered.** Across the four adjacent pairs of the five
frozen $\tau$ percentiles at each $(\kappa,T)$ — 64 pairs — the fixed-policy and equilibrium
secant margins, oriented by the equilibrium sign, agree in orientation at **45**. The 19 that
disagree are not live disagreements: in every one of them the fixed-policy secant is at rounding
scale ($\lvert\cdot\rvert\le4.9\times10^{-14}$), so what is being compared is the orientation of
noise. **All 24 pairs whose fixed-policy secant is above rounding scale agree in orientation.**
Block 7 is explicitly not the certificate — the certificate is a derivative statement and this is
the finite-difference reading of the same question — and it is labelled NUMERICAL wherever
quoted; but Part (D)'s finite-scale claim is the place a reader will want this number, so it is
recorded beside it rather than left in the JSON.

**$T=10$ is the corner, and it is degenerate.** All 40 $T=10$ nodes report flagged-cell mass
$\Omega=0.00068$, far below the $0.01$ floor, so A8 fails there: with $H=10$, $T=H$ forces
$c=0$ on every flagged history and only the very top of the Voice region can file in time. The
window certificate was not attempted (WHERE IT FAILS 6), and the $T=5$ against $T=10$ record is
a finite-difference record only — 34 of 40 pairs attenuate, the six that do not sitting at
$\kappa=0.55$.

**A5, A3 and solver hygiene.** Zero multiple-root pricing nodes over all 80 nodes and all 33
stencil points each; zero nodes with $k_1\ge k_2$ (H3's interiority held everywhere it was
looked at); worst equilibrium residual $4.2\times10^{-11}$, inside the $10^{-8}$ gate.

**The inversion-free step is what is binding, and that is a card-owner finding.** Block 9's
companion bound — the same three groups with the exactly solved
$\lVert\partial_rk\rVert,\lVert\partial_\kappa k\rVert,\lVert\partial^2_{\kappa r}k\rVert$ in
place of $\bar k_r,\bar k_\kappa,\bar k_{\kappa r}$ — is, **on the live-margin nodes**, a median
factor $2.41$ smaller than $\mathcal B_r^{GE}$ with a maximum factor $8.29$ (the pooled figures
$2.09$ and $10.3$ mix in 48 rounding-scale nodes), and it certifies **22** nodes against the card
bound's 18. The realised remainder is a median $0.094$ of $\mathcal B_r^{GE}$ on those nodes
($0.22$ pooled). The four extra nodes the sharp companion certifies are **exactly** the four
genuine-GE-failure nodes $(T{=}5,\text{q}50,0.35)$, $(T{=}5,\text{q}50,0.55)$,
$(T{=}5,\text{q}70,0.35)$, $(T{=}5,\text{q}90,0.25)$; the only other uncertified live-margin
nodes are the two with $g_r^{PE}<0$, which no bound of any size could rescue. So at this
calibration **every uncertified live-margin node that any bound could rescue is rescued by
dropping the Neumann step** — it, and not the GE channel, is what binds.
**This does not certify anything** (NOT CLAIMED 5): the sharp companion needs
$(I-D_k\mathcal T)^{-1}$, which is exactly what card §4.5's rows are written to avoid. It is
offered to the card owner as evidence that a second, inversion-using bound would be worth adding
alongside the inversion-free one, not as a result of this file.

---

## NOTATION DELTA

Symbols used here that are not in card §4, each defined at first use above:

| Symbol | Meaning | Status |
|---|---|---|
| $\Delta^*(\kappa,r)=\Delta^{\mathrm{act}}\!\left(k(\kappa,r),\kappa,r\right)$ | the **equilibrium** premium: the card §4.4 object composed with the equilibrium cutoff vector | proof-local (Step 5), introduced because the card's $\Delta^{\mathrm{act}}$ is used at *both* a frozen $k$ and the equilibrium $k$, and every step here turns on the difference. Proposed for card §4.5 if C1 is re-derived |
| $\mathcal S$ used at the equilibrium $k$ | card §4.4 defines $\mathcal S=\lvert\partial_\kappa\Delta^{\mathrm{act}}\rvert$; Parts (C)–(D) evaluate it along $k(\kappa,r)$, i.e. $\lvert d\Delta^{\mathrm{act}}/d\kappa\rvert$ | **no new symbol**: the card's letter with an argument stated in words at each use. T1's $\mathcal S$ is the frozen-$k$ reading and Step 9 keeps the two apart |
| $\Psi(k;\vartheta)=k-\mathcal T(k;\vartheta)$ | the implicit-function residual map | proof-local (Step 1) |
| $\partial_\kappa k,\ \partial_rk,\ \partial^2_{\kappa r}k$ | the equilibrium cutoff vector's derivatives | card §4.5 names only their **bounds** $\bar k_x,\bar k_{\kappa r}$; the derivatives themselves are unnamed there. Written in $\partial$ form rather than as new letters |
| $\lVert\cdot\rVert=\lVert\cdot\rVert_\infty$ and the pairings $\lvert\mathcal T_{kk}\rvert=\max_i\sum_{j,l}\lvert\cdot\rvert$, $\lvert\Delta_{kk}\rvert=\sum_{j,l}\lvert\cdot\rvert$, etc. | the norms that make card §4.5's bars into valid multilinear bounds | **card-owner flag.** Card §4.5 writes $\lvert\partial_x\mathcal T\rvert$, $\lvert\Delta_{kk}\rvert$ and the rest without fixing a norm. With $J-1>1$ the numerical value of $\mathcal B_r^{GE}$ depends on the choice; the argument does not. Proposed as a parenthesis in the §4.5 rows |
| $\eta_{\min}$, $M$, $\delta$ | the smallest slack over a node set, a Lipschitz constant for $\eta_r$, and the node spacing | proof-local (Step 11), used only to state what a grid does **not** deliver |
| $\mathcal T_{\kappa r},\ \mathcal T_{\kappa k},\ \mathcal T_{rk},\ \mathcal T_{kk}$ | subscript shorthand for the second partials of the outer map at $(k(\vartheta);\vartheta)$ | proof-local (CLAIM (A), Step 4). Card §4.5 *names* $\bar k_{\kappa r}$ but never displays its formula, so these four shorthands appear nowhere on the card |
| $\Delta_\kappa,\ \Delta_{\kappa r}$ | $\partial_\kappa\Delta^{\mathrm{act}}$ and $\partial_{\kappa r}\Delta^{\mathrm{act}}$ at frozen $k$ | proof-local (Step 5). The card's $\mathcal B_r^{GE}$ row carries $\Delta_{\kappa k},\Delta_{kr},\Delta_{kk},\Delta_k$, but its $g_r^{PE}$ row writes the cross-derivative out as $\partial_{\kappa r}\Delta^{\mathrm{act}}$ and never as $\Delta_{\kappa r}$. Same object, shorter subscript |
| $\lvert\partial_\kappa\mathcal T\rvert,\ \lvert\partial_r\mathcal T\rvert$ (bars, in the CLAIM) | $\lVert\partial_x\mathcal T\rVert_\infty$ — the one pairing the preamble list does not fix, and the CLAIM writes it with bars where Step 3 writes it with a norm | **no new object**: for a vector the two coincide under $\lVert\cdot\rVert_\infty$. Written with bars in the CLAIM to match card §4.5's $\bar k_x$ row verbatim |
| $\mathcal B_r^{GE,\text{sharp}}$ | the same three groups of Step 6 with the exactly solved $\lVert\partial_xk\rVert,\lVert\partial^2_{\kappa r}k\rVert$ in place of $\bar k_x,\bar k_{\kappa r}$ | proof-local (Block 9, NUMERICAL CHECK REQUEST). **Not a card object and it certifies nothing** — it needs $(I-D_k\mathcal T)^{-1}$, which card §4.5's rows are written to avoid |
| $\varepsilon_\kappa,\ \varepsilon_\tau$ | the stencil half-widths in $\kappa$ and $\tau$ | proof-local (Block 2 and the kink-ratio diagnostic). Written $\varepsilon$ and **not** $h$: $h$ is card §4.4's engagement-premium kernel $h=\pi p$ and is not available |
| $r_0,\ r_1$ | the endpoints of the strictness segment in Part (D) | proof-local (CLAIM (D), Step 10), with $r_1>r_0$ (higher $r$ = tighter) |
| $w,\ w_1,\ w_2$ | the unit vector of Step 1 and the arguments of the multilinear bounds | proof-local. Card §4.6 rules $u_1,u_2$ proof-local and forbids a **bare $u$**; $w$ carries no card meaning, where $\Xi$, $\Upsilon$ and $\iota_F$ are already spoken for |
| $\mathcal N$ | a neighbourhood of the equilibrium graph $\{(k(\vartheta),\vartheta):\vartheta\in\mathcal R_r\}$ inside $\operatorname{int}\Theta\times\mathcal R_r$ | proof-local (Step 1), the weakest domain on which Steps 1–4 need $\mathcal T$ smooth |
| (H2a), (H2b) | the along-the-path and over-$\Theta$ readings of $L_{\mathcal R}=\sup_{\mathcal R}\lVert D_k\mathcal T\rVert$ | **card-owner flag 1.** Card §4.5's row and card §5's AGE do not say whether the supremum runs over $k\in\Theta$ as well as over $\vartheta\in\mathcal R$. Steps 1–4 need only (H2a); only Step 12's uniqueness remark needs (H2b) |
| the $k$ at which card §4.5's $\Delta$-derivatives are read | $\partial_{\kappa r}\Delta^{\mathrm{act}}$ inside $g_r^{PE}$, and $\Delta_k,\Delta_{kk},\Delta_{\kappa k},\Delta_{kr}$ inside $\mathcal B_r^{GE}$ | **card-owner flag 2.** Card §4.5 does not say **at which cutoff vector** these are evaluated. Step 8 needs all of them at $k(\vartheta)$ — the equilibrium cutoff vector at the *same* $\vartheta$ — because that is where Step 5's identity puts them; read at any other frozen policy, Step 8's cancellation of the first group against $-g_r^{PE}$ fails and the certificate compares unlike objects. The proof and the companion script are consistent throughout on the $k(\vartheta)$ reading (the script's stencil sits at $x_0=(k_1^*,k_2^*,\kappa,\tau)$); the card should say so |
| the $k$ over which AGE's $C^2$ clause runs | card §5's "on a candidate region $\mathcal R$ the outer map is twice continuously differentiable" | **card-owner flag 3.** The clause does not say over which $k$ — the identical ambiguity flag 1 raises for the norm. Step 1 takes the *weaker* reading, smoothness on $\mathcal N$ only, so no step here depends on the resolution |

The card's $\sigma_\kappa$ is **not** used: card §4.5 rules that the sign is written inline and
that no symbol is available for it, and every occurrence above is written
$\operatorname{sgn}(d\Delta^{\mathrm{act}}/d\kappa)$ in full. No card symbol is renumbered or
re-keyed: $\kappa$ is noise-trading intensity, bare $\lambda$ and $\psi$ (D7's appropriability
coefficient and pivotality) appear nowhere, upright $T$ is the window and $\mathcal T$ is the
outer map, $h$ is left to card §4.4's engagement-premium kernel $h=\pi p$, no bare $u$ appears
(card §4.6), and $\Omega=\Pr(D=1)$ wherever it is mentioned.

---

## NOT CLAIMED

1. **Region nonemptiness.** Nothing here asserts that any parameter vector satisfies H2–H6
   simultaneously. **An empty region is a reportable outcome, not a failed run**: card §6's
   intended-label row says C1 is then dropped and the paper ships the fixed-policy theorem (T1)
   only. No tolerance is to be weakened to manufacture a nonempty region, and a run that returns
   one after a tolerance change is to be treated as void.
2. **No uniqueness of equilibrium.** Step 1 gives local uniqueness near one branch; Step 12 says
   what global uniqueness would additionally require (H2b) and that it is not measured. Card §3's
   "Uniqueness is **not** claimed" is respected.
3. **Nothing off-region.** No sign, bound or magnitude is claimed at any parameter vector outside
   $\mathcal R_r$. Off-region numbers carry at most the label NUMERICAL (card §7).
4. **A grid of certified nodes is not a certified region** (Step 11). No interpolation between
   certified nodes is claimed, and no supremum over $\mathcal R$ is inferred from finitely many
   evaluations.
5. **$\mathcal B_r^{GE}$ is not claimed tight.** It is a triangle-inequality bound and card §4.5
   calls it "one admissible" bound. $\eta_r\le0$ therefore carries no information about the sign
   of $\partial_r\mathcal S$ (WHERE IT FAILS 5), and a sharper bound — for instance solving
   $(I-D_k\mathcal T)x=\partial_x\mathcal T$ instead of bounding it — could certify strictly more
   nodes. That sharper route is not taken here because the card's rows are the inversion-free
   ones.
6. **No window-margin sign, and no window certificate.** C1 propagates whatever sign the
   fixed-policy theorem delivers; T1 delivers an iff and no unconditional sign at the window
   margin, so C1 delivers none either. The $r_T$ instance is additionally unavailable without an
   interpolation hypothesis (WHERE IT FAILS 6). Card §9's first boundary is respected.
7. **AGE is not verified.** Its differentiability clause is assumed, not tested; its contraction
   clause is *measured* along the equilibrium path only; its constancy clause is reported per
   slice and is expected to fail on some of them.
8. **No claim about $J$, $R$ or $R_d$**, and none that $J$ is $\kappa$-invariant (card §9).
   Neither appears in any step.
9. **No claim that the model's plan menu satisfies A7′** (card §4.2), on which L2 — and hence
   T1's factorisation, and hence the meaning of "attenuation" here — depends. C1 inherits that
   openness in full.
10. **No welfare, no optimal rule, no empirical value for $\omega_a$**, and no claim about where
    $\Omega$ sits in the data. Card §9's boundaries are respected.
11. **No label move.** C1 stays CONJECTURE and the card's ledger is not edited by this file.

---

## Repairs applied (2026-08-21, C1 audit)

Source: `research/model_v4/threads/2026-08-21_C1_proofread_audit.md` (adversarial proof-read,
verdict PASS, FAIL 0 · REPAIR 13). **No step, hypothesis, bound or conclusion changed** — every
repair is at the reporting or citation level, and every number below was recomputed from
`quality_reports/fixes/t2_c1_region_check.json` before it was written in.

| ID | Change |
|---|---|
| **C1-R1** | OUTCOME: added the live-margin (24) against null-margin (56) split with a three-way table, and reported every ratio on the live subset — realised remainder / $\mathcal B_r^{GE}$ median **0.094** (0.22 pooled), $\mathcal B_r^{GE}/\mathcal B_r^{GE,\text{sharp}}$ median **2.41** (2.09 pooled). Recorded that the containment test's $10^{-6}$ **absolute** slack gives its "80 nodes" headline an effective coverage of 24 |
| **C1-R2** | Corrected "at most $0.51$ of the bound": that maximum is the dead node $(T{=}10,\text{q}10,0.55)$ ($\mathcal B_r^{GE}=7.6\times10^{-13}$); the live-node figure is **0.310**. Stated that the independent four-corner route touches **2 of the 18** certified nodes. Added the omitted strongest evidence: the two independent readings of the equilibrium **cross**-derivative agree to better than **0.4 %** at every live-margin validation node (the pooled `max_rel_diff_cross` 0.535 is a null-margin artefact) |
| **C1-R3** | OUTCOME: surfaced the script's `tau_kink_ratio` diagnostic — the only executed evidence bearing on H4. Finite and $\le0.673$ at all 18 certified nodes (min 0.047, median 0.317); all 19 ratios above one are null-margin nodes. Converts WHERE IT FAILS 7(i) from an unmeasured hazard into a measured one that did not fire |
| **C1-R4** | Answered Block 7, which the request made and the OUTCOME never returned: 64 pairs, 45 same orientation; all 19 disagreements have a fixed-policy secant at rounding scale ($\le4.9\times10^{-14}$), and all 24 pairs with a live fixed-policy secant agree |
| **C1-R5** | NOTATION DELTA: added card-owner flag 2 — card §4.5 does not say **at which $k$** its $\Delta$-derivatives are evaluated, and Step 8 needs them at $k(\vartheta)$ |
| **C1-R6** | LABEL CLAIMED: replaced the stale reason 3. T1 is **PROVED at fixed policies** on the current card and A7′ satisfiability is resolved; what C1 inherits is conditionality (A($\tau$) OPEN for the two-round pooled cell, A(br)(br-v) assumed, A7′'s equilibrium selection OPEN), not a label. Stated that reasons 1–2 each carry CONJECTURE on their own |
| **C1-R7** | H4: A2 → **A2′**, with its replaced clause (local boundedness plus $\mathbb E[\max_j\lvert U_j\rvert]<\infty$) named; the point that boundedness is not differentiability strengthens |
| **C1-R8** | Card §4.6 ruling honoured: the bare $u,v,A$ of the norm preamble and Step 1 are now $w,w_1,w_2$, with the multilinear bound written on the actual objects instead of a generic form |
| **C1-R9** | NOTATION DELTA: added the ten missing symbols — $\mathcal T_{\kappa r},\mathcal T_{\kappa k},\mathcal T_{rk},\mathcal T_{kk}$; $\Delta_\kappa,\Delta_{\kappa r}$; the CLAIM's $\lvert\partial_x\mathcal T\rvert$ bars; $\mathcal B_r^{GE,\text{sharp}}$; the stencil half-widths (renamed $h_\kappa,h_\tau\to\varepsilon_\kappa,\varepsilon_\tau$, since $h$ is card §4.4's kernel $h=\pi p$); $r_0,r_1$ — plus $w,w_1,w_2$ and $\mathcal N$ |
| **C1-R10** | Step 1: $\Psi$'s domain restricted from $\operatorname{int}\Theta\times\mathcal R_r$ to a neighbourhood $\mathcal N$ of the equilibrium graph — the domain H4 already chooses — and the unflagged strengthening turned into card-owner flag 3 (AGE does not say over which $k$ its $C^2$ clause runs) |
| **C1-R11** | Step 10: continuity of $\eta_r$ argued rather than asserted, from H4's $C^2$ clause, Step 7's constant sign and the region-constant $1-L_{\mathcal R}$; the measurability route noted as the cheaper alternative |
| **C1-R12** | Block 9: "what **most** uncertified $T=5$ nodes with a live margin fail on" → **"every uncertified live-margin node that any bound could rescue"** — the sharp companion's four extra nodes are exactly the four genuine-GE-failure nodes, and the other two live failures have $g_r^{PE}<0$ |
| **C1-R13** | H2b: "not used by any step below" → "no step in the proof of (A)–(D) uses it; Step 12 discusses what it would add", which is what the H2 bracket `[Steps 1–4, 7, 12]` already implied |
| **C1-O2** | (observation, applied where the audit directed it) LABEL CLAIMED object 3 now cites `quality_reports/fixes/d8_ge_dominance_check.py`'s $\varepsilon$-ball plus integral-control construction as the live in-repo template for a future node-to-region promotion, with Part (D) as its (R2) analogue |

**Also recut, per the auditor's three-object split (orchestrator adjudication, binding):**
LABEL CLAIMED now separates (1) the certificate implication — PROVED-eligible pending the
re-derivation, with $\mathcal R_r$ a named hypothesis and card §6's C1 row required to absorb
H2–H8 first; (2) the 18 certified nodes — NUMERICAL via the executed committed check; (3) "PROVED
on a named nonempty region" — declared **not obtainable from any run of this script**, since it
needs a modulus of continuity for $\eta_r$ and a genuine supremum for $L_{\mathcal R}$, neither of
which more grid nodes can supply.

**Not applied.** C1-O1 (the stamp-hash gap: git was out of scope for the audit and is out of scope
here), C1-O3 (H3's $k_1<k_2$ test is weaker than interiority — the OUTCOME's existing hedge
"everywhere it was looked at" already carries it, and the point is now also stated in LABEL
CLAIMED), C1-O4 (three cross-file attributions to `proofs/T1_proof.md`, left for the
re-derivation to confirm against T1 directly), C1-O6 and C1-O5 (card-owner items, recorded in
LABEL CLAIMED object 1 but not actionable in this file), C1-O7 (the $M_P$-hump attribution wants
one hedging word; an observation, not a repair, and left for the writer).
