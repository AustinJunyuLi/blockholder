# T1 — INDEPENDENT RE-DERIVATION (ticket 27)

**Inputs used, and only these:** `rederive/T1_statement_sheet.md` (CLAIM + H1–H18) and
`MODEL_CARD.md` (stamp 2026-08-21 · `a175202`+). No file in `proofs/` or `threads/` was opened.
No other file in `rederive/` was opened. Step numbers below are **mine**; they do not track the
statement sheet's bracketed step numbers, which I ignored as instructed.

---

## RE-DERIVATION VERDICT (summary; the reasoning is in PROOF)

| Part | Verdict | Note |
|---|---|---|
| **A — factorisation + total-variation form** | **PROVED-AS-STATED** | H6 is not only assumed but *derived* (S4) from H9 + H16 + H5 + the card's placement of $\kappa$. Differentiability of $\Delta^{\mathrm{act}}$ is a conclusion, not a hypothesis. |
| **B — threshold attenuation, $W_\tau C_\tau\le1$** | **PROVED-AS-STATED** | I confirm independently that H17 (br-v) is genuinely required and is **not** implied by (br-i)–(br-iv). Everything downstream of H11/H12 inherits the L3 writer's declared OPEN on A($\tau$). |
| **B — local form under H18** | **PROVED-AS-STATED** | Not load-bearing: Part B's conclusion (S19) is finite-difference throughout. |
| **C — exact iff $W_TC_T\le1$** | **PROVED-AS-STATED** | Both directions come from **one** reversible division by $\mathcal S(\kappa,\tau,T)>0$; there are not two independent arguments. See S24 and the report. |
| **C — $W_T\le1$** | **PROVED-AS-STATED** | Derived from D1's clock equivalence + $\partial_dB_j\ge0$ + $T$-freeness of the plan path under H5. |
| **C — no unconditional window sign** | **PROVED-AS-STATED**, and strengthened | S25 audits all eighteen hypotheses; S26 names exactly which A(br) clauses a window sign would need and records that the supplied O-1 numbers **refute their conjunction at the calibration**. |
| **C — local form, "equivalently"** | **PROVED-WITH-CHANGES** | Proved in the *integrated / average* sense, which is what the statement sheet's CLAIM says. It is **not** true in the pointwise sense, and the card's §6 T1 row writes "equivalently" without that qualification. One card-row wording repair requested (S28, WHERE IT FAILS 7). |

**Hypotheses added / dropped / strengthened:** none added, none dropped, none strengthened.
One premise made explicit that the sheet leaves inside the card rather than in H1–H18: the
**$\kappa$-placement reading** (card §4.1's $\kappa$/$\bar z$ row plus A1 put $\kappa$ *only* in the
law of $z_d$). It is card-internal, not new, and it is what S2–S4 run on. Two hypotheses were found
to be **partly unconsumed**: only the first clause of H12 is load-bearing (S16, S20), and H15's
monotonicity clause is not consumed by the equivalence itself (S30).

---

## CLAIM

At fixed plan and cutoff policies, with $0<\Omega<1$ and $\mathcal S_P>0$:

**(A) Factorisation.**
$$\mathcal S(\kappa,\tau,T)=\bigl(1-\Omega(\tau,T)\bigr)\,\mathcal S_P(\kappa,\tau,T),$$
and for every finite grid $\mathcal G=\{\kappa_0<\kappa_1<\dots<\kappa_N\}$,
$$\mathrm{TV}\bigl(\Delta^{\mathrm{act}};\mathcal G\bigr)=\bigl(1-\Omega(\tau,T)\bigr)\,\mathrm{TV}\bigl(M_P;\mathcal G\bigr),$$
with no differentiability required for the second.

**(B) Threshold margin — attenuation.** For $b_0<\tau'<\tau$ at a common window $T$,
$$\frac{\mathcal S(\kappa,\tau',T)}{\mathcal S(\kappa,\tau,T)}=W_\tau C_\tau\le1,\qquad
W_\tau=\frac{1-\Omega(\tau',T)}{1-\Omega(\tau,T)},\quad
C_\tau=\frac{\mathcal S_P(\kappa,\tau',T)}{\mathcal S_P(\kappa,\tau,T)},$$
because $W_\tau\in(0,1]$ and $C_\tau\in[0,1]$ separately. No dominance condition is needed at this
margin.

**(C) Window margin — an iff, and no sign.** For $T'<T$ at a common threshold $\tau$,
$$\mathcal S(\kappa,\tau,T')\le\mathcal S(\kappa,\tau,T)\iff W_TC_T\le1,$$
with $W_T\le1$ proved and $C_T$ **unsigned** by every hypothesis maintained here. Under H15 the
product criterion is the **integrated** form of
$$\frac{\partial_{r_T}\mathcal S_P}{\mathcal S_P}\le\frac{\Omega_{r_T}}{1-\Omega},\qquad r_T=-T,$$
and the two coincide exactly in the infinitesimal limit. **No unconditional window attenuation sign
is claimed anywhere in this file.**

---

## HYPOTHESES

H1–H18 are taken **exactly** as the statement sheet fixes them, and are not restated here at
length. Each step below names the ones it consumes. For reference, the short handles I use:

- **H1** card + stamp; $\Omega=\Pr(D=1)$ is draft_v2's $\omega_P$, distinct from $\omega_a$; upright $T$ is the window, $\mathcal T$ the outer map; $\Delta_m>0$.
- **H2** A8 interior crossing, $0<\Omega<1$, at $(\tau,T)$, $(\tau',T)$ and $(\tau,T')$.
- **H3** L1, verbatim. **H4** L2, verbatim, its own hypotheses travelling (A7 injective, no-feedback timing).
- **H5** fixed plan menu, execution policies and cutoff vector — frozen in $\kappa$ **and** across the two rules compared at each margin; no re-solving of $k=\mathcal T(k;\vartheta)$.
- **H6** PE-$\Omega$: $\Omega(\cdot,\tau,T)$ **constant** in $\kappa$ (the derivative form is its corollary).
- **H7** $\kappa\mapsto M_P$ differentiable. **H8** $\mathcal S_P>0$ at every denominator policy.
- **H9** D1, verbatim (measurability, clock equivalence $f_j\le H\iff B_j(s,H-T)\ge\tau$, $P^F-P^P_{c^-}=R+J$).
- **H10** $\partial_dB_j\ge0$ for Voice; A4's "only Voice plans cross in the core"; maintained $b_0<\tau'<\tau$.
- **H11** A($\tau$) at both compared policies, with the **binding ruling** that $\bar\pi$ is the *upper support point*, not the pooled engagement share.
- **H12** L3 as landed, with the exact identity $\partial_\kappa\mathbb E[h]=A'_\kappa C_h(\bar\pi)$ and the mean-value form; A($\tau$) for the two-round pooled cell is declared **OPEN**.
- **H13** A(br), clauses (br-i)–(br-iv), quantified **over the threshold pair only**.
- **H14** L4 as landed: leg 1 and leg 2 outright, leg 3 only under A(br), with equality when $C_h(\bar\pi(\tau))=0$.
- **H15** smooth window interpolation on $I$, including $r\mapsto\Omega(r)$ weakly increasing.
- **H16** no-feedback timing, carried as a numbered hypothesis: $B_j(s,d)$, $q_{jd}(s)$ functions of $(j,s,d)$ alone, $Q^F_j$ of $(j,s,\tau,T)$ alone.
- **H17** (br-v): $C_h(\cdot)$ is **the same functional** at $\tau$ and $\tau'$. T1-LOCAL addition, not carried by A(br).
- **H18** threshold-side smoothness on $I_\tau$, consumed by S21 alone.

**Card-internal premise made explicit (not a new hypothesis).**

- **(κ-PLACE)** By card §4.1 the parameter $\kappa$ is the noise-trading intensity and enters the
  model **only** through the law of the ternary noise mark, $\Pr(z_d=0)=1-\kappa$,
  $\Pr(z_d=\pm\bar z)=\kappa/2$; by A1 the $z_d$ are mutually independent of $v,\varepsilon,\xi$. No
  other card row carries a $\kappa$ argument in a primitive. This is a reading of the card, not an
  addition to H1–H18, and it is what S2–S4 consume.

---

## PROOF

### Part 0 — Preliminaries

**S1 (Objects and setting).** Fix a plan menu $\mathcal J$, execution policies
$B_j(\cdot,\cdot),b^*_j(\cdot),Q^F_j(\cdot)$ and a cutoff vector $k\in\Theta$, all frozen (H5).
Write $j(s)$ for the plan selected at signal $s$ by the frozen $k$. Card §4.4 fixes
$\Delta^{\mathrm{act}}=\Delta_m\mathbb E[h(\mathcal I_H)]$, $M_F=\Delta_m\mathbb E[h\mid D=1]$,
$M_P=\Delta_m\mathbb E[h\mid D=0]$, $\Omega=\Pr(D=1)$,
$\mathcal S=\lvert\partial_\kappa\Delta^{\mathrm{act}}\rvert$,
$\mathcal S_P=\lvert\partial_\kappa M_P\rvert$, and $\Delta_m>0$ (H1). All of Parts A–C are
statements at this fixed policy configuration.

**S2 ($\kappa$ sits only in the noise law).** By (κ-PLACE), the joint law of $(v,\varepsilon,\xi)$
carries no $\kappa$ argument, and therefore neither does the law of the signal $s=v+\varepsilon$.
The only object whose law $\kappa$ indexes is $(z_0,\dots,z_H)$.

**S3 (The cell indicator is a function of $s$ alone).** By H9, $D=\mathbf 1\{a=1,\ c(\tau)+T\le H\}$
and, for every Voice plan, $f_j\le H\iff B_j(s,H-T)\ge\tau$; hence
$$D=\mathbf 1\bigl\{a_{j(s)}=1\ \text{ and }\ B_{j(s)}(s,H-T)\ge\tau\bigr\}.$$
By H16 the executed path $B_j(s,d)$ is a function of $(j,s,d)$ alone, with no argument in realised
order flow or realised prices, hence no argument in any $z_d$. By H5 the selector $j(s)$ is frozen
and does not move with $\kappa$. Composing, $D$ is a fixed measurable function of $s$ alone, with no
$\kappa$ argument. (Measurability is H9's first clause.)

**S4 ($\Omega$ is constant in $\kappa$ — H6 derived).** By S3, $\Omega=\Pr(D=1)$ is the probability
that $s$ lands in a fixed measurable set determined by $(\mathcal J,k,\tau,T)$; by S2 the law of $s$
does not depend on $\kappa$. Hence $\Omega(\kappa,\tau,T)$ takes **the same value at every $\kappa$**
in the maintained set. This is H6 in its strong (constancy) form, so H6 is available rather than
merely assumed at this margin; its corollary $\partial_\kappa\Omega=0$ is immediate. The derivation
consumes H5 at exactly one place — the frozen selector $j(s)$ — which is why the general-equilibrium
version, where $k$ re-solves $k=\mathcal T(k;\vartheta)$ as $\kappa$ moves, breaks S4 and not merely
its conclusion (WHERE IT FAILS 1).

**S5 (Interiority transfers across $\kappa$).** H2 gives $0<\Omega<1$ at $(\tau,T)$. By S4 that one
number is $\Omega$ at *every* $\kappa$, so $0<\Omega(\kappa,\tau,T)<1$ for every $\kappa$ in the
maintained set, and both cells carry positive mass at every $\kappa$. The same argument runs at
$(\tau',T)$ and at $(\tau,T')$, where H2 is also assumed.

### Part A — Factorisation

**S6 (L1 at every $\kappa$).** By S5, $0<\Omega<1$ at each $\kappa$, so H3's first branch applies at
each $\kappa$:
$$\Delta^{\mathrm{act}}(\kappa)=\Omega\,M_F(\kappa)+(1-\Omega)\,M_P(\kappa),\tag{S6}$$
with **one and the same** $\Omega$ at every $\kappa$ by S4. Both conditional means are defined at
each $\kappa$ because both cells carry positive mass (S5); H3's degenerate branches, which leave the
null-cell average undefined rather than imputed, are not reached.

**S7 ($M_F$ does not move with $\kappa$).** H4 states L2's conclusion: at fixed cutoff and execution
policies, under A1, A4, A5, A7 in its injective form, the no-feedback timing (H16) and $\Omega>0$,
the flagged posterior, price, entry probability and $M_F$ are invariant to $\kappa$. H5 supplies the
fixed policies; H16 supplies the timing; S5 supplies $\Omega>0$. Hence $M_F(\kappa)=M_F(\kappa')$ for
any two $\kappa,\kappa'$ in the maintained set, and in particular $\partial_\kappa M_F=0$ wherever the
derivative is taken.

**S8 (Derivative form).** By H7, $\kappa\mapsto M_P(\kappa)$ is differentiable at the $\kappa$ of
interest. In (S6) the coefficients $\Omega$ and $1-\Omega$ are constants in $\kappa$ (S4) and
$M_F(\cdot)$ is constant in $\kappa$ (S7), so the right-hand side of (S6) is a constant plus a
constant multiple of a differentiable function. Differentiating,
$$\partial_\kappa\Delta^{\mathrm{act}}(\kappa)=\Omega\cdot 0+(1-\Omega)\,\partial_\kappa M_P(\kappa)
=(1-\Omega)\,\partial_\kappa M_P(\kappa).\tag{S8}$$
The term $(\partial_\kappa\Omega)(M_F-M_P)$ that a general product rule would carry is absent
because $\partial_\kappa\Omega=0$ (S4), not because $M_F=M_P$.

**S9 (Factorisation).** By S5, $1-\Omega>0$. Taking absolute values in (S8) and using
$\lvert(1-\Omega)x\rvert=(1-\Omega)\lvert x\rvert$ for $1-\Omega>0$:
$$\mathcal S(\kappa,\tau,T)=\lvert\partial_\kappa\Delta^{\mathrm{act}}\rvert
=(1-\Omega(\tau,T))\,\lvert\partial_\kappa M_P\rvert
=(1-\Omega(\tau,T))\,\mathcal S_P(\kappa,\tau,T).$$
This is Part A's first display. It is an **identity**, not an inequality or an approximation: no
remainder term is discarded anywhere in S6–S9.

**S10 (Total-variation form, no differentiability).** Let
$\mathcal G=\{\kappa_0<\kappa_1<\dots<\kappa_N\}$ be any finite grid inside the maintained set, and
write $\mathrm{TV}(X;\mathcal G)=\sum_{i=1}^N\lvert X(\kappa_i)-X(\kappa_{i-1})\rvert$. Apply (S6) at
$\kappa_i$ and at $\kappa_{i-1}$ and subtract. The coefficient $\Omega$ is the *same number* at both
nodes by S4 — this is exactly the place where a merely vanishing derivative at one point would not
suffice, and where H6's constancy form earns its keep — so the subtraction is term-by-term:
$$\Delta^{\mathrm{act}}(\kappa_i)-\Delta^{\mathrm{act}}(\kappa_{i-1})
=\Omega\bigl[M_F(\kappa_i)-M_F(\kappa_{i-1})\bigr]
+(1-\Omega)\bigl[M_P(\kappa_i)-M_P(\kappa_{i-1})\bigr].$$
By S7 the first bracket is zero. Taking absolute values and using $1-\Omega>0$ (S5),
$$\bigl\lvert\Delta^{\mathrm{act}}(\kappa_i)-\Delta^{\mathrm{act}}(\kappa_{i-1})\bigr\rvert
=(1-\Omega)\bigl\lvert M_P(\kappa_i)-M_P(\kappa_{i-1})\bigr\rvert .$$
Summing over $i=1,\dots,N$ and pulling the constant $(1-\Omega)$ out of the finite sum:
$$\mathrm{TV}(\Delta^{\mathrm{act}};\mathcal G)=(1-\Omega(\tau,T))\,\mathrm{TV}(M_P;\mathcal G).$$
H7 is not used: no derivative is taken and no limit is passed. The identity holds grid by grid, for
every $\mathcal G$, and therefore also for the supremum over grids whenever that supremum is finite.

**S11 (Remark — differentiability of $\Delta^{\mathrm{act}}$ is a conclusion).** S8 does not assume
$\kappa\mapsto\Delta^{\mathrm{act}}$ differentiable. Under S4, S7 and H7, (S6) exhibits
$\Delta^{\mathrm{act}}$ as an affine function of $M_P$ with $\kappa$-constant coefficients, so its
differentiability is *derived* from H7. Nothing in Part A requires differentiability of $\Omega$ or
of $M_F$ beyond what S4 and S7 already deliver.

### Part B — Threshold margin

**S12 (Ratio identity).** Apply S9 at $(\tau',T)$ and at $(\tau,T)$ — legitimate at both, since H2
holds at both (H2 names $(\tau',T)$ explicitly) and H5 freezes the policies **across** the two
thresholds, so S4 and S7 hold at each of the two rules separately. The denominator
$\mathcal S(\kappa,\tau,T)=(1-\Omega(\tau,T))\mathcal S_P(\kappa,\tau,T)$ is a product of two
strictly positive numbers: $1-\Omega(\tau,T)>0$ by H2, and $\mathcal S_P(\kappa,\tau,T)>0$ by H8.
Hence the ratio is well defined and
$$\frac{\mathcal S(\kappa,\tau',T)}{\mathcal S(\kappa,\tau,T)}
=\frac{1-\Omega(\tau',T)}{1-\Omega(\tau,T)}\cdot
\frac{\mathcal S_P(\kappa,\tau',T)}{\mathcal S_P(\kappa,\tau,T)}=W_\tau\,C_\tau.\tag{S12}$$

**S13 ($W_\tau\in(0,1]$ — L4 leg 1, derived).** By S3 the flagged event at threshold $t$ is
$$\{D(t)=1\}=\bigl\{s:\ a_{j(s)}=1\ \text{ and }\ B_{j(s)}(s,H-T)\ge t\bigr\}.$$
The policies $\mathcal J$, $B_j$, $k$ (hence $j(s)$) and the window $T$ are common to the two rules
by H5, so the only thing that moves between $t=\tau$ and $t=\tau'$ is the level $t$ in the last
inequality. For $\tau'<\tau$, $B\ge\tau\Rightarrow B\ge\tau'$, hence
$\{D(\tau)=1\}\subseteq\{D(\tau')=1\}$, and monotonicity of a probability measure gives
$$\Omega(\tau',T)\ \ge\ \Omega(\tau,T).$$
(H10's maintained $b_0<\tau'<\tau$ keeps both rules in the core, where by A4 only Voice plans cross;
without it a pre-existing crossing $b_0\ge\tau'$ makes the last inequality slack for every $s$ and
the comparison degenerate rather than false.) Subtracting from one,
$0<1-\Omega(\tau',T)\le1-\Omega(\tau,T)$, both strictly positive by H2 at each rule, hence
$W_\tau\in(0,1]$.

**S14 (The pooled engagement share falls).** Write $\bar\pi_{\mathrm{pr}}(t)=\Pr(a=1\mid D(t)=0)$,
the object H13's (br-iv) names. By card §4.2, $D=1\Rightarrow a=1$, so the set of histories that are
pooled at $\tau$ but flagged at $\tau'$,
$$N_\tau:=\{D(\tau)=0\}\setminus\{D(\tau')=0\}=\{D(\tau')=1\}\setminus\{D(\tau)=1\},$$
satisfies $N_\tau\subseteq\{a=1\}$; and $\{D(\tau')=0\}\subseteq\{D(\tau)=0\}$ by S13. Put
$x=\Pr(\{a=1\}\cap\{D(\tau')=0\})$, $y=\Pr(D(\tau')=0)$, $n=\Pr(N_\tau)$. Then $0\le x\le y$,
$n\ge0$, $y>0$ by H2 at $(\tau',T)$, and
$$\bar\pi_{\mathrm{pr}}(\tau)=\frac{x+n}{y+n},\qquad \bar\pi_{\mathrm{pr}}(\tau')=\frac{x}{y}.$$
Cross-multiplying, $(x+n)y-x(y+n)=n(y-x)\ge0$, and both denominators are positive, hence
$$\bar\pi_{\mathrm{pr}}(\tau')\ \le\ \bar\pi_{\mathrm{pr}}(\tau).$$
Adding a set of engaging histories to the flagged cell removes them from the pooled cell and can
only lower the pooled engagement share.

**S15 ($\bar\pi(\tau')\le\bar\pi(\tau)$ — L4 leg 2).** H11's binding ruling forbids identifying
$\bar\pi$ with the pooled engagement share, so S14 does not by itself move $\bar\pi$. The bridge is
H13's **(br-iv)**: $\bar\pi$ is a weakly increasing function of $\bar\pi_{\mathrm{pr}}$, *the same
function at $\tau$ and $\tau'$*. Applying that function to S14's inequality,
$\bar\pi(\tau')\le\bar\pi(\tau)$. (Consistency with H11's ruling: by H9 the cell $\{D=0\}$ is
$\mathcal I_H$-measurable, so the tower property gives
$\mathbb E[\Pi_\kappa]=\mathbb E[\pi(\mathcal I_H)\mid D=0]=\Pr(a=1\mid D=0)=\bar\pi_{\mathrm{pr}}$;
under the ternary representation $\mathbb E[\Pi_\kappa]=\bar\pi(A_{1/2}/2+A_1)$, which is strictly
below $\bar\pi$ unless $A_0=A_{1/2}=0$. The share and the upper support point are distinct objects,
exactly as the ruling requires, and (br-iv) is the only link between them that this file uses.)

**S16 (The exact $\kappa$-motion of the pooled cell).** By H11 / H13 (br-i), the pooled posterior law
at each compared policy has the symmetric ternary representation
$$\mathbb E[h\mid D=0]=A_0(\kappa)h(0)+A_{1/2}(\kappa)h(\bar\pi/2)+A_1(\kappa)h(\bar\pi),$$
with $A_0'=A_1'=A'_\kappa$ and $A_{1/2}'=-2A'_\kappa$. By H13 **(br-ii)**, at fixed policies the
three support points $\{0,\bar\pi/2,\bar\pi\}$ and the kernel $h$ as a function of the posterior do
not move with $\kappa$, so differentiating the representation in $\kappa$ acts on the weights alone,
with no composition remainder:
$$\partial_\kappa\mathbb E[h\mid D=0]=A'_\kappa h(0)-2A'_\kappa h(\bar\pi/2)+A'_\kappa h(\bar\pi)
=A'_\kappa\bigl[h(0)-2h(\bar\pi/2)+h(\bar\pi)\bigr]=A'_\kappa\,C_h(\bar\pi),$$
using card §4.4's definition of the chord. Multiplying by the $\kappa$-free constant $\Delta_m$
(H1) reproduces H12's exact identity in the $M_P$ scale:
$$\partial_\kappa M_P=\Delta_m\,A'_\kappa\,C_h(\bar\pi),\qquad
\mathcal S_P=\Delta_m\,\lvert A'_\kappa\rvert\,\lvert C_h(\bar\pi)\rvert,\tag{S16}$$
the second equality because $\Delta_m>0$ (H1) and $\lvert ab\rvert=\lvert a\rvert\lvert b\rvert$.
*Two internal checks.* (i) The weights sum to one at every $\kappa$, so their derivatives sum to
zero: $A'_\kappa-2A'_\kappa+A'_\kappa=0$, which the representation satisfies identically. (ii) The
perturbation moves mass $A'_\kappa\,d\kappa$ onto each of the two endpoints and $2A'_\kappa\,d\kappa$
off the midpoint, and $0+\bar\pi=2\cdot(\bar\pi/2)$, so it is **mean-preserving**:
$\partial_\kappa\mathbb E[\Pi_\kappa]=0$, matching H11's ruling that the share is $\kappa$-invariant
under A($\tau$). All of the pooled cell's $\kappa$-motion is therefore curvature of $h$ along the
chord and nothing else. With $h(0)=0$ (card §4.4) the chord reduces to
$C_h(\bar\pi)=h(\bar\pi)-2h(\bar\pi/2)$, so the maintained orientation $C_h\le0$ reads
$h(\bar\pi)\le2h(\bar\pi/2)$ and $\lvert C_h\rvert=2h(\bar\pi/2)-h(\bar\pi)$.

**S17 (Chord comparison across the threshold pair — where H17 is unavoidable).** H11's maintained
orientation supplies "$\lvert C_h\rvert$ weakly increasing in $\bar\pi$". That is a statement about
**one** functional evaluated at two arguments. At the threshold margin the two quantities to be
compared are $\lvert C_h(\bar\pi(\tau'))\rvert$ and $\lvert C_h(\bar\pi(\tau))\rvert$, which are two
values of one functional **only if** the univariate section of $h$ in its posterior argument is the
same at $\tau$ and at $\tau'$. I checked H13's four clauses one at a time against that requirement
and none delivers it: (br-i) fixes the *representation, endpoints and weight-coefficients* at the two
policies but says nothing about the kernel section; (br-ii) freezes the support points and the kernel
**along $\kappa$**, at fixed policies, not along $\tau$; (br-iii) compares the coefficients
$A'_\kappa$; (br-iv) asserts "the same function at $\tau$ and $\tau'$" of the **endpoint map**, with
no counterpart for $h$. The requirement is therefore exactly **H17 (br-v)**, and I confirm
independently of the statement sheet that it is used and is not implied. With H17 in hand, and
$\bar\pi(\tau')\le\bar\pi(\tau)$ from S15, the monotonicity clause of H11 applies to a single
functional and gives
$$\lvert C_h(\bar\pi(\tau'))\rvert\ \le\ \lvert C_h(\bar\pi(\tau))\rvert.\tag{S17}$$

**S18 ($C_\tau\in[0,1]$ — L4 leg 3).** By S16 at each of the two rules,
$\mathcal S_P(\kappa,t,T)=\Delta_m\lvert A'_\kappa(t)\rvert\lvert C_h(\bar\pi(t))\rvert$ for
$t\in\{\tau,\tau'\}$. H13 **(br-iii)** gives
$\lvert A'_\kappa(\tau')\rvert\le\lvert A'_\kappa(\tau)\rvert$, and S17 gives
$\lvert C_h(\bar\pi(\tau'))\rvert\le\lvert C_h(\bar\pi(\tau))\rvert$. All four quantities are
non-negative (they are absolute values), and for non-negative reals $0\le a\le A$ and $0\le b\le B$
imply $ab\le AB$ (because $ab\le Ab\le AB$, each step multiplying an inequality by a non-negative
number). Multiplying by $\Delta_m>0$,
$$\mathcal S_P(\kappa,\tau',T)\ \le\ \mathcal S_P(\kappa,\tau,T),$$
which is H14's leg 3. Both sides are non-negative and the right side is strictly positive by H8, so
$C_\tau\in[0,1]$.

**S19 (Part B — conclusion).** Combining (S12), S13 and S18: $W_\tau\in(0,1]$ and $C_\tau\in[0,1]$,
so the product of two numbers in $[0,1]$ satisfies $W_\tau C_\tau\le1$, hence
$$\frac{\mathcal S(\kappa,\tau',T)}{\mathcal S(\kappa,\tau,T)}=W_\tau C_\tau\le1
\quad\Longrightarrow\quad \mathcal S(\kappa,\tau',T)\le\mathcal S(\kappa,\tau,T).$$
Threshold tightening weakly attenuates the premium's liquidity sensitivity. **No dominance condition
is needed**, and this is the structural reason: at this margin the weight ratio and the composition
ratio point the *same* way, so their product is bounded without either having to outweigh the other.
Every step from S15 to S19 is a finite-difference statement between two policies; no derivative in
$\tau$ appears, so this conclusion does not touch H18.

**S20 (The $C_h=0$ case, and what H8 rules out).** H14 records that leg 3 holds *with equality*
whenever $C_h(\bar\pi(\tau))=0$, which A($\tau$)'s weak orientation permits. Two observations. (i)
At the *ratio* level that case is excluded by H8: by (S16), $\mathcal S_P(\kappa,\tau,T)>0$ forces
both $A'_\kappa(\tau)\ne0$ and $C_h(\bar\pi(\tau))\ne0$, so H8 at the denominator policy is exactly
the assumption that the denominator rule is not chord-degenerate. (ii) At the *unnormalised* level
the conclusion survives the degenerate case anyway: if $C_h(\bar\pi(\tau))=0$ then S17 forces
$\lvert C_h(\bar\pi(\tau'))\rvert\le0$, hence $\mathcal S_P=0$ at both rules, hence
$\mathcal S(\kappa,\tau',T)=0=\mathcal S(\kappa,\tau,T)$ and attenuation holds with equality — while
the ratio $W_\tau C_\tau$ is $0/0$ and undefined. So H8 protects the *displayed ratio form*, not the
economics. Only the first clause of H12 (the exact identity) is consumed above; H12's mean-value form
$C_h=\tfrac14\bar\pi^2g''(\zeta)$ is used **only** here, to say that the degenerate case is the
$\bar\pi\downarrow0$ boundary at which $\mathcal S_P$ vanishes and H8 fails.

**S21 (Part B, local form under H18).** Assume H18 on an interval $I_\tau\ni\tau',\tau$, and write
$r_\tau=-\tau$ (card §4.5), so higher $r_\tau$ is tighter. H18 clause 2 extends H2 and H8 to every
$t\in I_\tau$, so S9 applies at every point of the interval and
$\mathcal S(r_\tau)=(1-\Omega(r_\tau))\mathcal S_P(r_\tau)>0$ there. H18 clause 1 makes
$r_\tau\mapsto\Omega$ and $r_\tau\mapsto\partial_\kappa M_P$ continuously differentiable; by the same
non-vanishing-plus-continuity argument spelled out in S27a, $\mathcal S_P$ is then continuously
differentiable on the interval as well. Since $\mathcal S>0$ there, $\log\mathcal S$ is defined and
$C^1$, and
$$\frac{\partial_{r_\tau}\mathcal S}{\mathcal S}
=\frac{\partial_{r_\tau}\mathcal S_P}{\mathcal S_P}-\frac{\Omega_{r_\tau}}{1-\Omega}.\tag{S21}$$
H18 clause 3 makes H13 and H17 available for **every** pair $t'<t$ in $I_\tau$, so S13 and S18 can be
read along the interval rather than only at its ends: S13 gives $\Omega$ weakly increasing in
$r_\tau$, i.e. $\Omega_{r_\tau}\ge0$, and S18 gives $\mathcal S_P$ weakly decreasing in $r_\tau$,
i.e. $\partial_{r_\tau}\mathcal S_P\le0$. Both terms on the right of (S21) are then non-positive, so
$\partial_{r_\tau}\mathcal S\le0$: local attenuation at the threshold margin, with no dominance
condition, matching S19.

**S22 (H18 is not load-bearing).** Part B's conclusion is S19, which is finite-difference from S12
onward, and Parts A and C never mention $r_\tau$. If H18 fails — for instance through the atom that
H18's own commentary names, a flat stretch of $s\mapsto B_j(s,H-T)$ inside the Voice region at which
$t\mapsto\Omega(t,T)$ jumps — then S21 is void and no other step moves.

### Part C — Window margin

**S23 ($W_T\in(0,1]$ — window tightening weakly raises $\Omega$).** By S3 the flagged event at window
$t$ is $\{s:a_{j(s)}=1,\ B_{j(s)}(s,H-t)\ge\tau\}$. Under H5 the plan path $B_j(s,\cdot)$ and the
selector $j(s)$ are frozen across the two windows: the window enters the *date at which the path is
evaluated*, through H9's clock equivalence, not the path itself. (Card §4.2's rows
$T'<T\Rightarrow B^F(T')\le B^F(T)$ and $Q^F(T')\ge Q^F(T)$ are the same statement seen from the
execution side: the filing date $f_j=c_j+T$ moves earlier and the pooled/flagged split of one
unchanged path moves with it.) For $T'<T$ we have $H-T'>H-T$, and by H10 every Voice plan has
$\partial_dB_j\ge0$, so $B_{j(s)}(s,H-T')\ge B_{j(s)}(s,H-T)$ for every $s$ with $a_{j(s)}=1$.
Therefore
$$\{D(T)=1\}\subseteq\{D(T')=1\},\qquad \Omega(\tau,T')\ \ge\ \Omega(\tau,T),$$
and, subtracting from one and using H2 at both $(\tau,T)$ and $(\tau,T')$,
$0<1-\Omega(\tau,T')\le1-\Omega(\tau,T)$, hence $W_T\in(0,1]$. (H10's $b_0<\tau$ keeps the
comparison in the core; H9's clock equivalence is what licenses evaluating a single monotone path at
the two dates $H-T$ and $H-T'$, both of which lie in the plan's calendar $\{0,\dots,H\}$ because
$T,T'\in\{1,\dots,H\}$ by card §4.1.)

**S24 (The iff — and both of its directions).** By H2 and H5, S4 and S7 hold separately at
$(\tau,T)$ and at $(\tau,T')$, so S9 gives the factorisation at each:
$$\mathcal S(\kappa,\tau,T')=(1-\Omega(\tau,T'))\,\mathcal S_P(\kappa,\tau,T'),\qquad
\mathcal S(\kappa,\tau,T)=(1-\Omega(\tau,T))\,\mathcal S_P(\kappa,\tau,T).$$
By H2, $1-\Omega(\tau,T)>0$; by H8, $\mathcal S_P(\kappa,\tau,T)>0$; hence
$$\mathcal S(\kappa,\tau,T)>0.\tag{S24a}$$
For real $u$ and $w>0$, the equivalence $u\le w\iff u/w\le1$ holds and is **reversible**, because
dividing by a strictly positive number and multiplying by it are mutually inverse order-preserving
operations. Applying it with $u=\mathcal S(\kappa,\tau,T')$ and $w=\mathcal S(\kappa,\tau,T)$, and
substituting the two factorisations,
$$\mathcal S(\kappa,\tau,T')\le\mathcal S(\kappa,\tau,T)
\iff\frac{\mathcal S(\kappa,\tau,T')}{\mathcal S(\kappa,\tau,T)}\le1
\iff\underbrace{\frac{1-\Omega(\tau,T')}{1-\Omega(\tau,T)}}_{W_T}\cdot
\underbrace{\frac{\mathcal S_P(\kappa,\tau,T')}{\mathcal S_P(\kappa,\tau,T)}}_{C_T}\le1 .$$
**Both directions have the same source.** There are not two arguments here, one for "$\Rightarrow$"
and one for "$\Leftarrow$": there is one reversible division, and (S24a) — that is, H2 at $(\tau,T)$
together with H8 at $(\tau,T)$ — is what makes it reversible. This matters for the failure analysis:
if H8 is dropped at the denominator policy then $\mathcal S(\kappa,\tau,T)=0$, the "$\Leftarrow$"
direction has no content (the criterion $W_TC_T\le1$ is a ratio with a zero denominator) while the
"$\Rightarrow$" direction becomes the vacuous statement that $0\le0$. Neither direction survives the
loss of (S24a); they stand or fall together.

**S25 ($C_T$ is unsigned by every maintained hypothesis — audit).** I went through H1–H18 asking of
each whether it constrains $\mathcal S_P$ across two windows at a common threshold. H1 is notation.
H2 constrains $\Omega$, not $\mathcal S_P$. H3 and H4 are cell decomposition and $\kappa$-invariance
of $M_F$, with no window comparison. H5 freezes policies, which is what makes the comparison
well-posed but signs nothing. H6 and H7 are $\kappa$-side. **H8 constrains $\mathcal S_P$ only by
positivity**, at $(\tau,T)$ and $(\tau,T')$ — it makes $C_T$ a well-defined positive number and stops
there. H9, H10 and H16 are path and clock structure, consumed by S23 on the $\Omega$ side. H11 and
H12 supply the representation and the chord identity; H12's second clause is a boundary statement in
$\bar\pi$. **H13 is quantified over the threshold pair only** — its own text says so, and H17's
commentary confirms the quantification is deliberate rather than a drafting accident. H14's three
legs are all quantified over $b_0<\tau'<\tau$. **H15 supplies smoothness and $\Omega$ monotonicity in
the window, and positivity of $\mathcal S_P$ — it does not sign $\partial_{r_T}\mathcal S_P$.** H17
and H18 are threshold-side. No hypothesis signs $C_T$. (H11's header reads "at both compared
policies", which could be stretched to cover $(\tau,T')$ as well as $(\tau',T)$. Even on that
generous reading nothing changes: it would give
$C_T=\lvert A'_\kappa(T')\rvert\lvert C_h^{T'}(\bar\pi(T'))\rvert\big/\lvert A'_\kappa(T)\rvert\lvert C_h^{T}(\bar\pi(T))\rvert$
and leave both factors unbounded, for the reasons in S26.)

**S26 (What a window sign would require, and the live failure case).** The *set-inclusion* half of
the threshold argument does transfer. Running S14's algebra with $N_T=\{D(T')=1\}\setminus\{D(T)=1\}$
in place of $N_\tau$ — legitimate because S23 gives the same inclusion and card §4.2's
$D=1\Rightarrow a=1$ gives $N_T\subseteq\{a=1\}$ — yields
$\bar\pi_{\mathrm{pr}}(\tau,T')\le\bar\pi_{\mathrm{pr}}(\tau,T)$. What does **not** transfer is
everything that converts a share ranking into an $\mathcal S_P$ ranking. Reading S16–S18 back, a
window analogue of S18 would need, at the window pair, all four of:
(a) (br-i) — the ternary representation at $(\tau,T')$;
(b) a window (br-iii) — $\lvert A'_\kappa(T')\rvert\le\lvert A'_\kappa(T)\rvert$;
(c) a window (br-iv) — one weakly increasing endpoint map from $\bar\pi_{\mathrm{pr}}$ to $\bar\pi$,
the same at $T$ and $T'$;
(d) a window (br-v) — the same chord functional $C_h(\cdot)$ at $T$ and $T'$.
Three of the four are threshold-quantified in H13/H17 and the fourth, (b), is nowhere assumed. So
"no unconditional window sign" is not an omission that a sharper argument could repair from the
present hypothesis set: it is the exact statement that (a)–(d) are not available.

Moreover the conjunction (a)–(d) is not merely unavailable but, on the numbers this project's
orchestrator carries as binding, **false at the model's own calibration**. The O-1 evaluations of
$W_TC_T$ are
$$1.06397\ \text{at}\ \Omega=0.037252,\quad
1.18373\ \text{at}\ \Omega=0.128950,\quad
1.13631\ \text{at}\ \Omega=0.285804,\quad
0.37798\ \text{at}\ \Omega=0.50,$$
with the criterion boundary at $\Omega^*\approx0.343$. Two consequences, both derived here rather
than assumed. First, the iff's **negative branch is realised**: at the three low-$\Omega$ nodes
$W_TC_T>1$, so by S24 window tightening *raises* $\mathcal S$ there — amplification, not attenuation
— while at $\Omega=0.50$ the criterion holds with room to spare and window tightening attenuates.
Both branches occur inside the maintained parameter set, which is the sharpest possible content of
"no unconditional sign". Second, since S23 gives $W_T\le1$ unconditionally, $W_TC_T>1$ forces
$$C_T=\frac{\mathcal S_P(\kappa,\tau,T')}{\mathcal S_P(\kappa,\tau,T)}\ \ge\ W_TC_T\ >\ 1$$
at each of the three low-$\Omega$ nodes, i.e. window tightening **raises** pooled sensitivity there.
That is the direct contradiction of clause (b)+(d)'s conclusion, so the window analogue of L4's leg 3
is refuted at the calibration, not merely unproved. *These four numbers and $\Omega^*$ are carried as
a supplied NUMERICAL input under the orchestrator's binding ruling; they were not re-computed in this
file, and the conditional structure above is what I derive — if the numbers are right, the window
analogue of A(br) is false at the calibration.*

**S27a ($\mathcal S_P$ is $C^1$ on the interpolation).** Assume H15 on the open interval
$I\supseteq[T',T]$, with $r_T=-T$ and the objects extended to $\{-t:t\in I\}$. H15 makes
$r\mapsto\partial_\kappa M_P(r)$ continuously differentiable there and requires
$\mathcal S_P(r)=\lvert\partial_\kappa M_P(r)\rvert>0$ throughout, so $\partial_\kappa M_P$ is a
continuous function that never vanishes on a connected set. By the intermediate value theorem it
cannot change sign there: if it took both a positive and a negative value it would take the value
zero in between, contradicting $\mathcal S_P>0$. Let $\mathfrak e\in\{-1,+1\}$ be that constant sign.
Then $\mathcal S_P(r)=\mathfrak e\,\partial_\kappa M_P(r)$ on the whole set, so $\mathcal S_P$ is
continuously differentiable with $\partial_r\mathcal S_P=\mathfrak e\,\partial_r\partial_\kappa M_P$.
This step is not cosmetic: $\lvert\cdot\rvert$ is not differentiable at $0$, and H15's positivity
clause is precisely what removes that obstruction.

**S27 (Local criterion).** On the same set, H15 gives $\Omega(r)\in(0,1)$ and
$r\mapsto\Omega(r)$ continuously differentiable, so by S9 (applicable pointwise, since H2's
interiority is the content of $\Omega(r)\in(0,1)$ and H5's freezing is maintained along the
interpolation)
$$\mathcal S(r)=(1-\Omega(r))\,\mathcal S_P(r)>0 .$$
Both factors are $C^1$ (H15 and S27a) and strictly positive, so $\log\mathcal S$ is $C^1$ and
$$\frac{\partial_r\mathcal S(r)}{\mathcal S(r)}
=\frac{-\Omega_r(r)}{1-\Omega(r)}+\frac{\partial_r\mathcal S_P(r)}{\mathcal S_P(r)} .\tag{S27}$$
Since $\mathcal S(r)>0$, the sign of $\partial_r\mathcal S$ equals the sign of the right-hand side.
Tightening the window is *increasing* $r_T=-T$ (card §4.5: higher $r$ = tighter), so local
attenuation is $\partial_{r_T}\mathcal S\le0$, and by (S27) that holds exactly when
$$\frac{\partial_{r_T}\mathcal S_P}{\mathcal S_P}\ \le\ \frac{\Omega_{r_T}}{1-\Omega},$$
which is the CLAIM's local criterion. Note that (S27) is an identity for **any** sign of $\Omega_r$;
H15's monotonicity clause is not used to obtain it.

**S28 (In what exact sense the product criterion "is" the local criterion).** Let $r_1=-T$ (looser)
and $r_2=-T'$ (tighter), so $r_1<r_2$ and $[r_1,r_2]\subset\{-t:t\in I\}$. By S24's factorisations
and the definition of $W_T,C_T$,
$$W_TC_T=\frac{\mathcal S(r_2)}{\mathcal S(r_1)} .$$
Both are strictly positive (S27), so taking logarithms and applying the fundamental theorem of
calculus to the $C^1$ function $\log\mathcal S$, then substituting (S27),
$$\log\bigl(W_TC_T\bigr)=\int_{r_1}^{r_2}\frac{\partial_r\mathcal S(r)}{\mathcal S(r)}\,dr
=\int_{r_1}^{r_2}\Bigl[\frac{\partial_r\mathcal S_P(r)}{\mathcal S_P(r)}
-\frac{\Omega_r(r)}{1-\Omega(r)}\Bigr]dr .\tag{S28}$$
Write $\Lambda(r)$ for the bracket, the *local excess*. Because $\log$ is strictly increasing and
$\log1=0$,
$$W_TC_T\le1\iff\int_{r_1}^{r_2}\Lambda(r)\,dr\le0
\iff\frac{1}{r_2-r_1}\int_{r_1}^{r_2}\Lambda(r)\,dr\le0 .$$
So: **the product criterion is exactly the statement that the local excess is non-positive *on
average* over $[r_1,r_2]$.** This is the precise sense of "equivalently", and it is the sense the
CLAIM asserts ("the integrated form of the local criterion"). Two one-way remarks complete the
relation, and the second is the reason the qualification cannot be dropped:
(i) If $\Lambda(r)\le0$ at **every** $r\in[r_1,r_2]$ — the pointwise local criterion — then the
integral is non-positive and $W_TC_T\le1$. Pointwise $\Rightarrow$ product.
(ii) The converse fails. $\int\Lambda\le0$ is compatible with $\Lambda(r)>0$ on a subinterval, offset
by $\Lambda<0$ elsewhere; nothing in H15 excludes a sign change of $\Lambda$ in the interior.
Product $\not\Rightarrow$ pointwise. Hence "$W_TC_T\le1$, equivalently
$\partial_{r_T}\mathcal S_P/\mathcal S_P\le\Omega_{r_T}/(1-\Omega)$" is **true read as an average and
false read pointwise**, for any window pair separated by more than an infinitesimal.

**S29 (Infinitesimal limit).** Fix $r\in\{-t:t\in I\}$ interior and let $r_2=r+\delta$ with
$\delta>0$ small enough that $[r,r+\delta]$ stays in the set. $\Lambda$ is continuous there (S27a,
H15), so by the mean value theorem for integrals there is $\varrho_\delta\in(r,r+\delta)$ with
$\int_r^{r+\delta}\Lambda=\delta\,\Lambda(\varrho_\delta)$. Dividing by $\delta$ and using (S28),
$$\frac{1}{\delta}\log\bigl(W_TC_T\bigr)=\Lambda(\varrho_\delta)\ \xrightarrow[\ \delta\downarrow0\ ]{}\ \Lambda(r)
=\frac{\partial_{r_T}\mathcal S_P(r)}{\mathcal S_P(r)}-\frac{\Omega_{r_T}(r)}{1-\Omega(r)},$$
the limit by continuity of $\Lambda$ at $r$. Since $\delta>0$, the sign of $\log(W_TC_T)$ is the sign
of $\Lambda(\varrho_\delta)$; hence whenever $\Lambda(r)\ne0$, continuity gives $\Lambda$ of one sign
on a neighbourhood, and for all small enough $\delta$ the product criterion $W_TC_T\le1$ holds if and
only if $\Lambda(r)\le0$. **The two criteria coincide exactly in the infinitesimal limit**, which is
the CLAIM's last window assertion. The one case the limit leaves open is $\Lambda(r)=0$: there the
finite-$\delta$ direction of the inequality is decided by higher-order behaviour that (S28) does not
resolve, and the pointwise criterion is knife-edge.

**S30 (H15's monotonicity clause is not consumed by S27–S29).** The identity (S27), the integrated
form (S28) and the limit (S29) hold for any sign of $\Omega_r$: none of the three uses
$\Omega_{r_T}\ge0$. The clause is consumed only where the *interpretation* needs it — to say that the
weight term $-\Omega_{r_T}/(1-\Omega)$ is an attenuating force along the interpolation, and hence
that $W_T\le1$ persists between the integer endpoints rather than only at them. That is why S23,
which compares two **integer** windows, cannot be substituted for it: an extension agreeing with the
card's objects at $r=-T$ and $r=-T'$ is free to dip in between, so $\Omega_{r_T}\ge0$ on the
interpolation is a hypothesis (H15) and not a consequence of S23.

**S31 (Part C — conclusion).** S24 is the exact iff; S23 proves $W_T\le1$; S25–S26 establish that
$C_T$ is unsigned by H1–H18 and that its violating branch is live at the calibration; S27–S29 give
the local criterion, the integrated equivalence and the infinitesimal coincidence. **No
unconditional window attenuation sign is claimed.**

---

## WHERE IT FAILS

1. **General equilibrium (H5/H6 fail together).** If the cutoff vector re-solves
   $k=\mathcal T(k;\vartheta)$ as $\kappa$ moves, S3's selector $j(s)$ acquires a $\kappa$ argument,
   S4 collapses, and (S8) regains the term $(\partial_\kappa\Omega)(M_F-M_P)$. The factorisation
   becomes
   $\partial_\kappa\Delta^{\mathrm{act}}=(\partial_\kappa\Omega)(M_F-M_P)+(1-\Omega)\partial_\kappa M_P$,
   the omitted term is of the sign of $\partial_\kappa\Omega$ times the cell gap, and **all three
   parts** of T1 lose their common backbone. This is C1's business, not T1's; T1 is a fixed-policy
   result and this file claims it nowhere else.
2. **$\Omega\to1$ (H2 fails at the top).** The pooled cell becomes null, H3's degenerate branch makes
   $M_P$ undefined rather than imputed, $\mathcal S_P$ has no meaning, and every displayed ratio
   divides by $1-\Omega=0$. Both S12 and S24 are void. At the other end, $\Omega\to0$ leaves the
   factorisation intact in form ($\mathcal S\to\mathcal S_P$) but makes $M_F$ undefined and, per card
   §5's ticket-24 row, breaks L2's own $\Omega>0$ premise, so S7 is lost.
3. **Chord-degenerate denominator (H8 fails), $C_h(\bar\pi(\tau))=0$.** Inside A($\tau$)'s maintained
   *weak* orientation, so not an exotic case. Part B's ratio is $0/0$ (S20), and Part C is worse:
   with $\mathcal S(\kappa,\tau,T)=0$ the division in S24 is not reversible and **both directions of
   the iff fail together** (S24's closing paragraph) — the "$\Leftarrow$" for want of a defined
   criterion, the "$\Rightarrow$" for want of content.
4. **A7-injective fails for the running menu (H4's residual risk).** Card §5's ticket-24 note
   resolves *satisfiability* (the pro-rata single-Voice menu works) but not whether **this** model's
   menu satisfies A7′; the named boundary is a binding stake cap, quantized stakes, a composed target
   repeating values across Voice-plan switches, $\Omega=0$, and policy-dependence when the condition
   is stated at one equilibrium's cutoffs only. On any of those, L2 fails, $\partial_\kappa M_F\ne0$,
   and S7 — hence (S8), (S9) and the whole of Parts A–C — is lost. This is the largest single
   exposure in the file, because everything factors through S9.
5. **A($\tau$) fails for the two-round pooled cell (H12's declared OPEN).** Then (S16) is not
   available, $\partial_\kappa M_P$ has no $A'_\kappa C_h$ form, and S16–S21 collapse: **the whole of
   Part B falls**. Parts A and C are untouched, because neither uses A($\tau$) — a useful separation,
   since it localises the L3 writer's open question to one of the three parts.
6. **(br-v)/H17 fails.** At fixed policies a change in $\tau$ moves which histories are pooled, hence
   the pooled price $P$, which enters $h$ through the entry probability
   $p=1-\Phi((P+K+m_0+\pi\Delta_m-\bar S)/\sigma_\xi)$ (card §4.3). If the univariate section of $h$
   at $\tau'$ differs from the one at $\tau$, then (S17) compares two different functionals and H11's
   monotonicity clause does not apply; leg 3 and therefore S18, S19 fail. Note the direction of the
   damage: S15 (the *share* falls) survives untouched, so the failure is precisely at the
   share-to-sensitivity bridge.
7. **Reading "equivalently" pointwise (a card-row wording exposure, not a hypothesis failure).**
   Card §6's T1 row writes "$W_TC_T\le1$, equivalently
   $\partial_{r_T}\mathcal S_P/\mathcal S_P\le\Omega_{r_T}/(1-\Omega)$" with no qualifier. By S28(ii)
   that is false for any non-infinitesimal window pair: the product criterion is the *average* local
   criterion, and $\int\Lambda\le0$ does not give $\Lambda\le0$ pointwise. **Repair requested:** the
   card row should read "equivalently, in integrated form over $[-T,-T']$" or "equivalently in the
   infinitesimal limit". Left unqualified, the row over-states T1 in a way this re-derivation cannot
   support.
8. **H18 clause 1 fails (atom in the date-$(H-T)$ stake law).** Card §4.2 requires only *weak*
   $\partial_sB_j\ge0$ and the 2026-08-21 A7′ row constrains only the composed **terminal** target,
   not the interior date $B_j(s,H-T)$; a flat stretch there puts an atom in the law, at which
   $t\mapsto\Omega(t,T)$ jumps and $\Omega_{r_\tau}$ does not exist. S21 is void; S19 and everything
   in Parts A and C are unaffected (S22).

---

## LABEL CLAIMED

**CONJECTURE**, unchanged. Card §7 permits a label move only on an executed check or an independent
re-derivation, and §6 records that the protocol requires **independent re-derivation PASS *plus*
proof-read PASS** before PROVED. This file is one of those two inputs and is not authorised to move
anything by itself. Beyond the protocol, three substantive reasons keep T1 short of PROVED even as an
aspiration:

1. Part B inherits H12's **declared OPEN** on whether the two-round pooled cell satisfies A($\tau$).
2. Part B additionally rests on **H17 (br-v)**, which is a T1-local addition that A(br) does not
   carry; I confirm independently (S17) that it is used and unavoidable. Until the card owner adopts
   it as a fifth A(br) clause, the threshold leg rests on A($\tau$) + A(br) + (br-v).
3. Parts A–C all route through S7, i.e. L2, whose exposure is whether the running menu satisfies A7′
   (WHERE IT FAILS 4).

Parts A and C are the strongest of the three: A is an identity given S4 and S7, and C's iff is a
single reversible division. Part B carries both extra exposures.

---

## NUMERICAL CHECK REQUEST

All four checks are at fixed policies, on the baseline calibration, with the solver's own tolerances
(`TOL_CONVERGE = 1e-6`, `TOL_RESIDUAL = 5e-3`).

**N1 — Part A, identity form.** Grid $\kappa\in\{0.05,0.10,\dots,0.95\}$ at baseline $(\tau,T)$.
Compute $\Omega(\kappa)$, $M_F(\kappa)$, $M_P(\kappa)$, $\Delta^{\mathrm{act}}(\kappa)$. Predicted:
$\max_i\lvert\Omega(\kappa_i)-\Omega(\kappa_0)\rvert=0$ and
$\max_i\lvert M_F(\kappa_i)-M_F(\kappa_0)\rvert=0$, magnitudes below $10^{-8}$ (solver noise only —
S4 and S7 are exact, not approximate); and the residual
$\rho=\max_i\bigl\lvert[\Delta^{\mathrm{act}}(\kappa_i)-\Delta^{\mathrm{act}}(\kappa_{i-1})]
-(1-\Omega)[M_P(\kappa_i)-M_P(\kappa_{i-1})]\bigr\rvert$ predicted $=0$, magnitude below $10^{-10}$.
A residual at $10^{-3}$ or larger would indict S4 or S7, not floating point.

**N2 — Part A, total-variation form.** Same grid. Predicted
$\mathrm{TV}(\Delta^{\mathrm{act}};\mathcal G)/\mathrm{TV}(M_P;\mathcal G)=1-\Omega$ exactly; at the
calibration $\Omega=0.037252$ the predicted value is $0.962748$, to $10^{-9}$. Re-run on a
deliberately coarse grid (3 nodes) and a fine one (200 nodes): the ratio must be **grid-invariant**,
since S10 uses no limit.

**N3 — Part B.** Grid of adjacent threshold pairs $\tau'<\tau$ with $b_0<\tau'$, e.g. eight nodes
spanning the maintained range at the baseline $T$. At each pair report
$W_\tau,C_\tau,W_\tau C_\tau$ and $\mathcal S(\tau')-\mathcal S(\tau)$. Predicted signs:
$W_\tau\in(0,1]$, $C_\tau\in[0,1]$, $W_\tau C_\tau\le1$ at **every** pair, and
$\mathcal S(\tau')-\mathcal S(\tau)\le0$ at every pair. Predicted magnitude: the product should sit
strictly below $1$ wherever $\bar\pi(\tau')<\bar\pi(\tau)$ strictly, and approach $1$ only as the pair
closes up. A single node with $W_\tau C_\tau>1$ refutes S18 and, through it, (br-iii), H17 or H14
leg 3 — and the check should report which of $W_\tau$, $\lvert A'_\kappa\rvert$, $\lvert C_h\rvert$
moved the wrong way.

**N4 — Part C, both branches of the iff.** Reproduce the O-1 evaluations of $W_TC_T$ at
$\Omega\in\{0.037252,\,0.128950,\,0.285804,\,0.500000\}$. Predicted values
$\{1.06397,\,1.18373,\,1.13631,\,0.37798\}$ to five significant figures, and a single sign change with
boundary $\Omega^*\approx0.343$ (bisect to $10^{-3}$). Predicted joint pattern, which is the real
content of the check: $W_T\le1$ at every node (S23), therefore $C_T\ge W_TC_T>1$ at the three
low-$\Omega$ nodes — magnitude $C_T\ge1.06$ — and $\mathcal S(\kappa,\tau,T')>\mathcal S(\kappa,\tau,T)$
there, i.e. **window tightening amplifies at the calibration**. If instead $W_T>1$ is ever returned,
S23 is contradicted and D1's clock equivalence or $\partial_dB_j\ge0$ is the place to look.

**N5 — Part C, S28's average-versus-pointwise gap (optional but decisive for WHERE IT FAILS 7).** On
a smooth window interpolation, evaluate $\Lambda(r)$ on a fine $r$-grid across $[-T,-T']$. Predicted:
at least one calibration exists where $\int\Lambda\le0$ while $\max_r\Lambda(r)>0$. One such instance
settles that the card's unqualified "equivalently" must be repaired.

---

## NOTATION DELTA

Symbols used above that are **not** rows of card §4. None is a re-key of a card symbol; card §8
rule 4's reservations ($\lambda$, $\psi$, $\chi$, bare $W$, upright $T$ vs $\mathcal T$, $\kappa$)
are respected throughout, and $\Gamma$, $K$, $\varepsilon$, $\vartheta$, $\Theta$ are used only in
their card senses or not at all.

| Symbol | Meaning | Provenance |
|---|---|---|
| $j(s)$ | plan selector induced by the frozen cutoff vector $k$ | §4.5 carries $k$, not the induced map; proof-local |
| $\bar\pi_{\mathrm{pr}}(t)$ | pooled prior engagement share $\Pr(a=1\mid D(t)=0)$ | introduced by H13 (br-iv); no §4 row |
| $\Pi_\kappa$ | the pooled posterior as a random variable, $\pi(\mathcal I_H)$ on $\{D=0\}$ | named in H11's ruling; no §4 row |
| $D(t)$ | the disclosure indicator with its threshold (S13–S14) or window (S23) argument displayed | §4.2 writes $D_j(s;\tau,T)$; abbreviation only |
| $N_\tau$, $N_T$ | newly flagged sets at the threshold / window margin | proof-local (S14, S26) |
| $x,y,n$ | probabilities in S14's algebra | proof-local, S14 only |
| $\mathcal G$, $\mathrm{TV}(X;\mathcal G)$ | finite $\kappa$-grid; total variation of $X$ over it | proof-local (S10) |
| $g$ | univariate section of $h$ in its posterior argument | implicit in H12's mean-value form and in H17; no §4 row |
| $\zeta$ | mean-value point in $(0,\bar\pi)$ in H12's form | H12; no §4 row |
| $\mathfrak e$ | constant sign of $\partial_\kappa M_P$ on the interpolation, $\in\{-1,+1\}$ | proof-local (S27a) |
| $I$, $I_\tau$ | window / threshold interpolation intervals | H15, H18 |
| $r_1,r_2$ | interval endpoints in the $r_T=-T$ coordinate, $r_1=-T<r_2=-T'$ | proof-local (S28) |
| $\Lambda(r)$ | local excess $\partial_r\mathcal S_P/\mathcal S_P-\Omega_r/(1-\Omega)$ | proof-local (S28–S29) |
| $\delta$, $\varrho_\delta$ | window increment; mean-value point in $(r,r+\delta)$ | proof-local (S29) |
| $\Omega^*$ | O-1 criterion boundary, $\approx0.343$ | supplied by the orchestrator's binding ruling |
| (κ-PLACE) | the card-internal premise that $\kappa$ enters only the law of $z_d$ | reading of §4.1 + A1; named in HYPOTHESES |

---

## NOT CLAIMED

1. **No general-equilibrium claim.** Everything is at the frozen policies of H5. Nothing here says
   the attenuation sign survives $k=\mathcal T(k;\vartheta)$ re-solving; that is C1.
2. **No unconditional window sign**, in either direction. S26 in fact records the opposite at the
   calibration, and does so conditionally on supplied numbers.
3. **No claim that the O-1 numbers are correct.** They are a supplied NUMERICAL input carried under
   the orchestrator's binding ruling; I re-derived none of them and ran no code. What I derive is the
   conditional: *if* those numbers hold, the window analogue of L4 leg 3 is false at the calibration.
4. **No claim that A($\tau$) holds for the two-round pooled cell.** H12 declares it OPEN and Part B
   inherits the openness in full.
5. **No claim that (br-v)/H17 is implied by A(br).** S17 argues the contrary, clause by clause.
6. **No claim that the pointwise local criterion is necessary** for $W_TC_T\le1$ (S28(ii)), and no
   claim that the card's unqualified "equivalently" is defensible as written (WHERE IT FAILS 7).
7. **No claim that A7′ holds for this model's menu** — only that L2's conclusion is being used as
   H4 supplies it.
8. **No claim about $J$'s $\kappa$-invariance**, no equilibrium uniqueness, no nonempty GE-certified
   region, no welfare or optimal-rule statement — card §9's exclusions stand.
9. **No label move.** T1 remains CONJECTURE (LABEL CLAIMED), and this file is one of the two inputs
   the protocol requires, not the decision.
10. **No claim that the O-1 amplification result generalises off the calibration** beyond what the
    sign change at $\Omega^*\approx0.343$ states.
