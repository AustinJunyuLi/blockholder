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
  \lVert D_k\mathcal T(k;\vartheta)\rVert$. Strictly stronger. It is **not** used by any step
  below and is **not** measured; it is recorded here only because it is what would upgrade
  Step 1's *local* uniqueness to a global one on $\Theta$ (Step 12).

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
differentiability it presupposes. Card §5's A2 (bounded prices and payoffs) is **not** cited for
it: boundedness is not differentiability. [Steps 5, 6, 9]

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

