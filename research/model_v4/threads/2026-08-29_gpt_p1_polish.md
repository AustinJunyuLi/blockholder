# GPT Pro P1 polish pass — 2026-08-29 — filed verbatim

**Courier record.** Austin pasted `threads/gpt_p1_polish_prompt_2026-08-29.md` (self-contained:
ask + history + statement of record + card §§3–5 + the complete `proofs/P1_proof.md`, built
against card stamp 2026-08-28 · re-review audit repairs · `59c0dfc`) into a fresh GPT Pro
thread. The response is filed byte-for-byte below the separator — no edits, no reflow. Per the
standing rule its findings can support demotion but never promote; every proposal is
CONJECTURE-grade edit text until the lane's own gate applies it; the in-house audit is a
separate file and nothing below lands without it.

---
The audit below is against the required stamp, **2026-08-28 · re-review audit repairs · commit `59c0dfc`**, using the P1 row and complete proof supplied in the bundle. 

# FINDINGS — WRONG

## F1 — The filing-stake measurability display evaluates the stake at the wrong date

**Step anchor:** Step 2.

**Current text, quoted**

> “\(B_j^F(s)=\sum_{d=0}^{H-T}\mathbf 1\{f_j(s)=d+T\}\cdot B_j(s,d)\)
> is a finite sum of products of Borel functions, hence Borel…”

**Exact failure**

If \(c_j(s)=d\), then \(f_j(s)=d+T\), but the displayed sum returns \(B_j(s,d)\), the stake at the **crossing date**, whereas the definition requires

$$
B_j^F(s)=B_j(s,f_j(s))=B_j(s,d+T),
$$

the stake at the **filing date**. For example, \(c_j=2\) and \(T=3\) make the display return \(B_j(s,2)\) instead of \(B_j(s,5)\).

The display also silently assigns a value to \(B_j^F\) when no filing lands, although the card defines \(B_j^F\) on the flagged set.

**Proposed text**

> For the measurability argument, extend the filing objects off the flagged set by
>
> $$
> \widetilde B_j^F(s)
> :=\sum_{\ell=T}^{H}\mathbf 1\{f_j(s)=\ell\}\,B_j(s,\ell),
> \qquad
> \widetilde Q_j^F(s):=b_j^*(s)-\widetilde B_j^F(s).
> $$
>
> This is a finite sum of products of Borel functions. On \(\{D_j=1\}\), one has
> \(f_j(s)\in\{T,\dots,H\}\), so
> \(\widetilde B_j^F(s)=B_j(s,f_j(s))=B_j^F(s)\) and
> \(\widetilde Q_j^F(s)=Q_j^F(s)\). Off \(\{D_j=1\}\), the extension is conventional and is never
> used as a flagged object. Suppressing the tildes on the flagged set, \(B_j^F\) and \(Q_j^F\) are
> Borel there.

**Statement preservation:** This establishes exactly the measurability Step 2 needs, without changing the filing-date definition or the theorem’s antecedent.

---

## F2 — The flagged family need not exist, so it is not categorically continuum-indexed

**Step anchors:** Step 3; Step 6 opening.

**Current text, quoted**

> “**Step 3 (the pooled public-history family is finite; the flagged family is not).**”

and

> “By Step 3 the flagged information sets are indexed by the continuum
> \(\sigma_F\in[0,\bar b]^2\times\{1\}\).”

**Exact failure**

A8 is not assumed for the existence half. An admissible case is therefore that no plan ever flags—for example, the proof’s own WHERE IT FAILS 6 uses \(\tau>\bar b\). Then the flagged-pair set and its image are empty, hence finite.

The fact that the **codomain**
\([0,\bar b]^2\times\{1\}\) is a continuum does not establish that the actual flagged image is a continuum.

When the flagged-pair set is nonempty, the intended conclusion can be recovered: a Voice plan’s flagged signal set is an upper ray because \(s\mapsto B_j(s,H-T)\) is weakly increasing, and A7-J maps that uncountable ray injectively. Thus the flagged image is either empty or continuum-sized.

**Proposed text**

> **Step 3 (the pooled public-history family is finite; the flagged image is either empty or
> continuum-sized).**
> The pooled public-history family is finite by the argument below. Let the flagged image be the
> image of
>
> $$
> \{(j,s):D_j(s;\tau,T)=1\}
> \quad\text{under}\quad
> (j,s)\mapsto(B_j^F(s),Q_j^F(s),1).
> $$
>
> If no plan flags, this image is empty and the flagged-price construction in Step 6 is vacuous. If
> some Voice plan flags at one signal, Voice monotonicity implies that it flags on an upper ray of
> signals; that ray is uncountable, and h.7 maps it injectively, so the flagged image is uncountable.
> Thus the flagged layer cannot in general be treated as a finite indexed family, although it may be
> empty.
>
> **Step 6 opening:** Work on the Borel image of the flagged-pair map. If that image is empty, parts
> (a)–(d) are vacuous; otherwise it is continuum-sized by Step 3.

**Statement preservation:** The measurable-family construction remains unchanged where flags exist, while the no-flag equilibria already admitted by P1 are handled correctly.

---

## F3 — The perturbation limit is not plan-uniform at an on-path history

**Step anchor:** Step 9(b).

**Current text, quoted**

> “A ratio of polynomials in \(1/n\) with a denominator that is nonzero for all large \(n\)
> converges as \(n\to\infty\), pointwise in \((j,s)\), and the limit is the
> plan-uniform-weighted joint law restricted to the history.”

**Exact failure**

That characterization is false whenever \(\Lambda_k>0\). At an on-path history, the uniform tremble vanishes and the limiting posterior is the ordinary posterior generated by the conjectured strategy \(j_k\), not the posterior generated by uniform plan weights.

The later denominator case split implicitly recognizes the distinction, so the step currently contains two incompatible descriptions of the same limit.

**Proposed text**

> Expanding \(w_n\), the limit has two cases. If
>
> $$
> \Lambda_k
> =\int L_{j_k(s')}(\mathcal H_d^P\mid s')\varphi_s(s')\,ds'>0,
> $$
>
> then
>
> $$
> \mu_\infty(j,s)
> =\frac{\mathbf 1\{j=j_k(s)\}
> L_j(\mathcal H_d^P\mid s)\varphi_s(s)}
> {\Lambda_k},
> $$
>
> the ordinary Bayes posterior generated by \(j_k\). If \(\Lambda_k=0\), then the unperturbed term
> vanishes almost everywhere and
>
> $$
> \mu_\infty(j,s)
> =\frac{L_j(\mathcal H_d^P\mid s)\varphi_s(s)}
> {\Lambda_u},
> \qquad
> \Lambda_u
> =\sum_{j'}\int L_{j'}(\mathcal H_d^P\mid s')\varphi_s(s')\,ds',
> $$
>
> the plan-uniform posterior restricted to the history. In both cases the displayed density
> integrates to one and is the pointwise limit of \(\mu_n\).

**Statement preservation:** The replacement still proves existence of the limit at every reachable history and now correctly distinguishes Bayes-on-path from the selected off-path limit.

---

## F4 — The supposedly fixed unreachable-history convention uses an endogenous probability

**Step anchor:** Step 9(c).

**Current text, quoted**

> “fix once and for all a reference belief \((\hat v_\circ,\pi_\circ)\) — for definiteness the
> prior pair \(\bigl(\mu_v,\Pr(a=1)\bigr)\)…”

**Exact failure**

\(\Pr(a=1)\) is not a fixed primitive. Engagement is attached to the selected plan, so under the conjecture \(k\),

$$
\Pr(a=1)
=\Pr\!\bigl(a_{j_k(s)}=1\bigr),
$$

which generally varies with \(k\). The displayed choice therefore does not define a convention “fixed once and for all” across the price systems used to construct \(\mathcal T(k)\).

This matters because the proof expressly acknowledges that the unreachable-history convention can move the pointwise best-response cutoff.

**Proposed text**

> Fix once and for all a \(k\)-independent reference belief. For definiteness, take
>
> $$
> (\hat v_\circ,\pi_\circ):=(\mu_v,1),
> $$
>
> equivalently the reference law under which \(v\) has its prior distribution and \(a=1\) almost
> surely. Assign to every unreachable pooled history the unique root
> \(P_\circ\) of
>
> $$
> \mathcal P_{(\hat v_\circ,\pi_\circ)}(P_\circ)=P_\circ.
> $$
>
> The choice of \(1\) is not substantive; any admissible scalar
> \(\pi_\circ\in[0,1]\) fixed independently of \(k\) would serve. What is essential is that the
> reference belief not be computed from the conjectured plan distribution.

**Statement preservation:** This supplies the fixed convention the theorem claims to use at every \(k\), with no change to equilibrium requirements at reachable histories.

---

## F5 — The finite corner convention does not represent an empty action region on the Gaussian tails

**Step anchors:** Step 13; Step 17(i); Step 19.

**Current text, quoted**

> “The corner convention is the display’s
> \(\inf\emptyset:=\overline s\): a plan that is optimal nowhere contributes an empty up-set and its
> cutoff sits at the top of the bracket, so it simply never appears in the range of \(j^\star\).”

and

> “\(j^\star(\cdot;k)\) agrees with Step 1’s \(j_{\mathcal T(k)}\) at every \(s\) except possibly the
> finitely many \(\mathcal T_i(k)\)…”

and

> “that map and \(j^\star(\cdot;k^\star)\) agree off the finitely many cutoff points, hence
> \(\Phi_s\)-almost surely…”

**Exact failure**

Under Step 1,

$$
j_k(s)=1+\#\{i:k_i\le s\}.
$$

Setting \(k_i=\overline s\) does **not** encode “never.” It activates the upper plan at every
\(s\ge\overline s\).

A direct witness is \(J=2\) and

$$
j^\star(s;k)\equiv1.
$$

Its upper level set is empty, so Step 13 sets
\(\mathcal T_1(k)=\overline s\). But Step 1 then gives

$$
j_{\mathcal T(k)}(s)=2
\quad\text{for every }s\ge\overline s.
$$

Because \(s\) is Gaussian and \(\overline s\) is finite,
\(\Pr(s\ge\overline s)>0\). The two maps therefore disagree on a positive-probability tail, not merely at one cutoff point.

Consequently:

* the statement that the vector represents \(j^\star\) is false;
* the conjectured population used to construct prices need not agree almost surely with the proposed equilibrium strategy;
* Step 17(i) does not establish card §3(i);
* Step 19’s “\(\Omega\) is unaffected” parenthetical need not hold.

The same issue occurs at \(\underline s\) if that finite boundary is intended to encode an action that is chosen for all signals.

**Corrected claim actually reached**

Step 13 constructs a finite vector representing the upper sets **inside the artificial bracket**. It does not, under the printed coding rule, represent the strategy on all of \(\mathbb R\).

**Repair status**

There is no statement-preserving prose-only repair. One of the following must be made explicit and then gate-checked:

1. strengthen h.6 and the P1 row with tail conditions ensuring
   \(j^\star(s;k)=1\) below \(\underline s\) and
   \(j^\star(s;k)=J\) above \(\overline s\), so empty and full upper sets never occur; or
2. redefine the cutoff parameterization so boundary values are genuine “always/never” sentinels, and use that same coding in Step 1, the price system, \(\mathcal T\), and card §3.

**Statement effect:** This is a theorem-level defect under the printed cutoff coding. Fixing it changes either the antecedent or the equilibrium parameterization, so it is not a polish edit.

---

## F6 — Step 15 asserts the very cutoff continuity that the proof and current card do not derive

**Step anchor:** Step 15 opening.

**Current text, quoted**

> “\(U_j(s;k)\) is continuous in \(k\) for each fixed \((j,s)\): the pooled and flagged inner prices
> are continuous in the cutoffs…”

and

> “at histories of vanishing probability the Step 9 perturbation limit supplies the value.
> **That is continuity in \(k\) at fixed \((j,s)\)**…”

**Exact failure**

Supplying a value at a zero-probability history does not show that the value equals the limit from nearby conjectures under which that history has positive probability.

Indeed, Step 9 deliberately uses two different posterior formulas:

* Bayes conditioning when \(\Lambda_k>0\);
* the plan-uniform limit when \(\Lambda_k=0\).

Nothing in Step 9 shows that these formulas agree as \(\Lambda_k\downarrow0\). The current card’s A5/A6 record identifies precisely this composition-through-conditioning as the discontinuous object.

Step 8 establishes continuity of the scalar root **given** \((\hat v,\pi)\); it does not establish continuity of

$$
k\longmapsto(\hat v,\pi)\longmapsto P.
$$

**Proposed text**

> Nothing in Steps 4–10 proves that \(k\mapsto U_j(s;k)\), or even the composed pooled price
> system, is continuous at fixed \((j,s)\). Step 8 gives continuity of the inner root in its belief
> summaries. The dependence of those summaries on \(k\) runs through conditioning events whose
> probability can vanish, and Step 9’s selected value at a \(k\)-null history need not agree with
> the one-sided Bayes limit from conjectures at which that history has positive probability.
> P1 therefore uses h.6 exactly as an assumption: for the named tie-break, corner convention and
> off-path convention, \(\mathcal T\) is a continuous self-map of \(\Theta\). The conditions in
> (i)–(ii) below are only candidate primitive sufficient conditions for that assumption; they are
> not consequences of the preceding steps.

**Statement preservation:** P1 already assumes continuity of \(\mathcal T\) through h.6, so deleting the unsupported intermediate continuity claim leaves the conditional Brouwer proof unchanged.

# FINDINGS — GAP

## F7 — The proof silently replaces the card’s general ordered polytope by the full ordered box

**Step anchor:** Step 1.

**Current text, quoted**

> “\(\Theta=\{k\in[\underline s,\overline s]^{J-1}:
> \underline s\le k_1\le\cdots\le k_{J-1}\le\overline s\}\)
> is card §4.5’s compact ordered polytope…”

**Missing argument**

Card §4.5 says that \(\Theta\) is a nonempty compact convex ordered cutoff polytope. It does not identify it with the entire intersection of a cube and the ordering half-spaces.

For a proper ordered polytope, Step 13’s inequalities

$$
\underline s\le\mathcal T_1\le\cdots\le\mathcal T_{J-1}\le\overline s
$$

do not by themselves imply \(\mathcal T(k)\in\Theta\).

**Proposed text**

> Fix the nonempty compact convex ordered cutoff polytope \(\Theta\) supplied by h.6. Compactness
> gives finite numbers \(\underline s<\overline s\) such that
>
> $$
> \Theta\subseteq
> \{k\in[\underline s,\overline s]^{J-1}:k_1\le\cdots\le k_{J-1}\}.
> $$
>
> For \(k\in\Theta\), define
>
> $$
> j_k(s)=1+\#\{i:k_i\le s\}.
> $$
>
> This map is Borel and weakly increasing. The conclusion
> \(\mathcal T(k)\in\Theta\) is supplied by h.6’s self-map clause; ordering and coordinate bounds
> alone establish membership only in the containing ordered box.

Step 13’s closing sentence should correspondingly read:

> Thus the constructed components are weakly ordered and lie in the common coordinate bracket.
> Membership in the possibly proper polytope \(\Theta\) is the self-map content of h.6.

**Statement preservation:** This uses A6 exactly as the P1 row states it and removes an unnecessary specialization of \(\Theta\).

---

## F8 — Continuity of the inner root in \(\pi\) is missing

**Step anchors:** Step 5(a); Step 8.

**Current text, quoted**

> “Step 7 supplies a unique fixed point … with continuity in the belief from Step 8.”

But Step 8 proves only

> “\(\frac{\partial P}{\partial\hat v}
> =\frac{1-p}{1-p+|p'(P)|(P+\bar m-A)}\in(0,1].\)”

**Missing argument**

The pooled belief varies in both

$$
(\hat v,\pi).
$$

Step 8 varies \(\hat v\) with \(\pi\) held fixed. It neither differentiates with respect to \(\pi\) nor otherwise proves joint continuity of the root in the two summaries.

That missing continuity is subsequently used in Step 5(a) and Step 9(b).

**Proposed text**

Append to Step 8:

> The same argument gives continuity in the full belief pair. The residual
>
> $$
> \varrho(P;\hat v,\pi)
> $$
>
> is \(C^1\) jointly in \((P,\hat v,\pi)\), because
> \(A=\hat v+\pi\Delta_V\), \(\bar m=m_0+\pi\Delta_m\), and \(p\) are \(C^1\) in those variables.
> Step 7(iii) gives
> \(\partial_P\varrho<0\) at every root. The implicit function theorem therefore gives a locally
> \(C^1\) root \(P=P(\hat v,\pi)\) around every belief pair. Step 7’s global uniqueness makes these
> local root functions agree on overlaps, so the unique root is continuous jointly in
> \((\hat v,\pi)\) on \(\mathbb R\times[0,1]\). The displayed derivative with respect to
> \(\hat v\) supplies the additional non-expansiveness bound used below.

Then replace Step 5(a)’s phrase with:

> “…with joint continuity in \((\hat v,\pi)\) from Step 8.”

**Statement preservation:** This proves the exact belief-summary continuity the pooled-price and perturbation arguments already claim to use.

---

## F9 — Price convergence in Step 9 omits convergence of the engagement posterior

**Step anchor:** Step 9(b).

**Current text, quoted**

> “Either way \(\hat v_n\to\hat v_\infty\) and, by Step 8’s 1-Lipschitz bound, the prices converge
> with them.”

**Missing argument**

The price is a function of both \(\hat v_n\) and \(\pi_n\). The 1-Lipschitz bound in Step 8 controls only changes in \(\hat v\) at fixed \(\pi\).

The step never defines \(\pi_n\), proves \(\pi_n\to\pi_\infty\), or invokes joint continuity in \((\hat v,\pi)\).

**Proposed text**

> Define
>
> $$
> \pi_n
> :=\sum_{j\in\mathcal J}a_j\int\mu_n(j,s)\,ds.
> $$
>
> If \(\Lambda_k>0\), the same denominator bound used for \(\hat v_n\) supplies an integrable
> envelope for \(a_j\mu_n(j,s)\), since \(a_j\in\{0,1\}\); dominated convergence therefore gives
> \(\pi_n\to\pi_\infty\). If \(\Lambda_k=0\), the posterior is \(n\)-independent almost everywhere,
> so the convergence is immediate. Hence
>
> $$
> (\hat v_n,\pi_n)\longrightarrow(\hat v_\infty,\pi_\infty).
> $$
>
> By Step 8’s joint continuity of the unique inner root in \((\hat v,\pi)\),
> \(P_n\to P_\infty\). The derivative bound
> \(\partial P/\partial\hat v\in(0,1]\) remains available for comparisons in which \(\pi\) is fixed.

**Statement preservation:** This completes the claimed limiting-price construction at reachable pooled histories without strengthening P1’s hypotheses.

---

## F10 — Empty interior of the tie set does not supply the strict sign pattern used next

**Step anchor:** Step 15(ii) and the paragraph immediately following it.

**Current text, quoted**

> “the indifference set
> \(\{s:U_{i+1}(s;k)=U_i(s;k)\}\) has empty interior.”

followed by

> “Under (i) and (ii), continuity of \(\mathcal T\) follows from … the strict sign change of
> \(U_{i+1}-U_i\) at each crossing…”

**Missing argument**

“Empty interior” excludes a tie interval. It does not itself establish:

* a unique threshold;
* a strict negative sign below it and strict positive sign above it;
* appropriate corner behavior when one plan is absent;
* continuity of the selected threshold under the named largest-monotone-selection rule.

The proof invokes a strict-sign conclusion that is not part of (ii) and is not derived from h.3 plus empty interior.

**Proposed text**

> (ii) *Robust threshold identification.* For each adjacent pair define
>
> $$
> d_i(s,k):=U_{i+1}(s;k)-U_i(s;k).
> $$
>
> For every \(k\in\Theta\), there is a unique
> \(c_i(k)\in[\underline s,\overline s]\) such that
>
> $$
> d_i(s,k)<0\quad\text{for }s<c_i(k),
> \qquad
> d_i(s,k)>0\quad\text{for }s>c_i(k),
> $$
>
> with either inequality vacuous at the corresponding endpoint. Thus
> \(c_i(k)=\overline s\) may encode an upper plan that is never preferred within the bracket, and
> \(c_i(k)=\underline s\) may encode a lower plan that is never preferred within the bracket, but
> neither an interval of ties nor an isolated tangency is permitted.
>
> Under (i) and this condition, \(c_i(k)\) is continuous. To see this, let
> \(k_n\to k\) and take any convergent subsequence
> \(c_i(k_n)\to c\), which exists by compactness of the bracket. For every \(s<c\), eventually
> \(s<c_i(k_n)\), so joint continuity gives \(d_i(s,k)\le0\); similarly,
> \(d_i(s,k)\ge0\) for every \(s>c\). The unique sign-threshold property at \(k\) forces
> \(c=c_i(k)\). Every convergent subsequence has the same limit, hence
> \(c_i(k_n)\to c_i(k)\). Therefore each component of \(\mathcal T\) is continuous.
>
> These conditions are sufficient, not claimed to be weakest. P1 itself continues to assume their
> conclusion through h.6.

**Statement preservation:** This repairs only the optional primitive route to A6; Brouwer continues to rest directly on h.6.

---

## F11 — The Kakutani remark does not establish convex values or a closed graph

**Step anchor:** Step 18.

**Current text, quoted**

> “Its values are convex, because at an indifference plateau the admissible values of a component
> form an interval and the ordering constraints cut the product of those intervals by half-spaces;
> its values are compact … and its graph is closed by the maximum theorem…”

**Missing argument**

The correspondence is a set of **cutoff vectors representing globally weakly increasing selections** from a continuum of typewise argmax sets. The paragraph does not establish that:

1. every admissible cutoff vector is obtained by independently choosing one component from an interval;
2. interactions among skipped plans, non-adjacent ties and ordering constraints cannot make the value a nonconvex union of faces;
3. limits of represented monotone selections remain represented under the proof’s corner convention;
4. the ordinary maximum theorem, which is about finite-dimensional choice at a parameter, directly supplies closed graph for this function-valued selection problem.

The corner-representation problem in F5 also propagates to the definition of \(\mathfrak T\).

**Proposed text**

> **Step 18 (possible Kakutani route; not established here).**
> One could try to replace the selected map by
>
> $$
> \mathfrak T(k)
> =\{k'\in\Theta:k'\text{ represents an optimal weakly increasing plan selection at }k\}.
> $$
>
> A Kakutani proof would require a separate lemma establishing that, under the chosen cutoff
> encoding, \(\mathfrak T\) has nonempty compact convex values and a closed graph. Joint continuity
> of \(U_j(s;k)\) would be one input to that lemma, but it does not by itself prove convexity of the
> cutoff-vector values or closedness under the corner conventions. No such lemma is proved here, so
> no Kakutani conclusion is drawn. This possible route is not part of P1.

**Statement preservation:** Deleting the unsupported strengthening leaves the Brouwer proof and the P1 statement untouched.

# FINDINGS — POLISH

## F12 — h.12 is stale against the current card

**Step anchor:** HYPOTHESES h.12.

**Current text, quoted**

> “**h.12 [ADDITION] — nonnegative premia.** \(m_0\ge0\). Card §4.1 restricts only
> \(m_1>m_0\) and \(\Delta_m>0\); it does not sign \(m_0\).”

**Proposed text**

> **h.12 = card §4.1’s nonnegative-premium restriction.**
> \(m_0\ge0\). Together with \(\Delta_m>0\) and \(\pi\in[0,1]\), this gives
>
> $$
> \bar m(\mathcal I)
> =m_0+\pi(\mathcal I)\Delta_m\ge0.
> $$
>
> The restriction originated in this proof and has since been absorbed into card §4.1; it is no
> longer an addition outside the card. *Used: Steps 7, 8.*

**Statement preservation:** The mathematical hypothesis is unchanged; only its current card status is corrected.

---

## F13 — The Gaussian-law citation in Step 4 points to the independence hypothesis

**Step anchor:** Step 4.

**Current text, quoted**

> “With \(\xi\sim N(0,\sigma_\xi^2)\) (h.1)…”

**Proposed text**

> With \(\xi\sim N(0,\sigma_\xi^2)\) by h.17-d, and with its independence from
> \((v,\varepsilon,z_{0:H})\) supplied by h.1,
>
> $$
> p=1-\Phi\!\left(\frac{P+K+\bar m-\bar S}{\sigma_\xi}\right).
> $$

**Statement preservation:** The calculation is unchanged and is now keyed to the hypothesis that actually supplies each fact.

---

## F14 — Step 5(b) retains an ambiguity the current card has already resolved

**Step anchors:** Step 5(b); NOT CLAIMED 12.

**Current text, quoted**

> “Under the other reading of §4.3’s \(Y\) row … part (a)’s fixed-point argument applies at these
> dates too. **Card ambiguity, regeneration item…**”

and

> “at \(d<H\) by (b) as a finite-sum conditional expectation of continuous functions…”

**Proposed text**

> (b) *Intermediate pooled dates \(d<H\).*
> Card §4.3 fixes the interpretation: the genuine fixed point is solved at the control node, and an
> earlier pooled price is the tower expectation
>
> $$
> P_d^P
> =\mathbb E[Y\mid\mathcal H_d^P]
> $$
>
> of the already-defined terminal/control-node payoff. There is no self-reference and no inner
> fixed-point problem at \(d<H\). Because the pooled public-history alphabet is finite, these dates
> produce a finite indexed family of conditional expectations. The conditional expectation may
> still integrate over the continuous signal and flagged-tuple distribution; it is not asserted to
> be a finite sum over all terminal states.
>
> No continuity in the conjecture \(k\) is claimed in this step. Continuity of the selected outer
> map is the h.6 assumption used in Step 16, and Step 15 records why continuity of the composed
> pooled-price system is not derived automatically.

Delete NOT CLAIMED 12, or replace it with:

> 12. That intermediate pooled prices solve additional inner fixed-point equations. Card §4.3
>     instead defines them as tower expectations of the solved control-node payoff.

**Statement preservation:** The current card’s timing convention directly yields the same finite pooled-price family needed later.

---

## F15 — Step 7(iii) can prove uniqueness globally instead of arguing between adjacent roots

**Step anchor:** Step 7(iii).

**Current text, quoted**

> “At any root, (i) gives \(P\ge A\)… Suppose two roots \(P_1<P_2\) with no root between them…”

**Proposed text**

> (iii) *The root is unique.* For every \(P\ge A\),
>
> $$
> \varrho'(P)
> =p'(P)\bigl(P+\bar m-A\bigr)+p(P)-1.
> $$
>
> Here \(p'(P)<0\), \(P+\bar m-A\ge\bar m\ge0\), and \(p(P)-1<0\). Therefore
>
> $$
> \varrho'(P)<0
> \qquad\text{for every }P\ge A.
> $$
>
> By part (i), every root lies in \([A,\infty)\). The residual is strictly decreasing on that entire
> interval and therefore has at most one root. Part (ii) gives existence, so the root is unique.

**Statement preservation:** This establishes the same uniqueness conclusion more directly and with a stronger derivative statement.

---

## F16 — Step 9’s perturbation sequence needs a valid starting index, and \(\varphi_s\) is missing from the proof’s notation table

**Step anchor:** Step 9(b) and the proof’s NOTATION DELTA.

**Current text, quoted**

> “\(w_n(j\mid s)=(1-t_n)\mathbf1\{j=j_k(s)\}+\frac{t_n}{J},
> \qquad t_n:=\frac Jn\downarrow0\)”

and

> “with \(\varphi_s\) the signal density…”

**Proposed text**

> For integers \(n\ge J+1\), set
>
> $$
> t_n:=\frac Jn\in(0,1),
> \qquad
> w_n(j\mid s)
> =(1-t_n)\mathbf1\{j=j_k(s)\}+\frac{t_n}{J}.
> $$
>
> Then every plan receives probability at least \(t_n/J=1/n\), the weights are nonnegative and sum
> to one, and \(t_n\downarrow0\).

Add this row to the proof’s NOTATION DELTA:

| Symbol        | Meaning                              | Collision check                                                                                           |
| ------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| \(\varphi_s\) | density of the Gaussian signal \(s\) | Distinct from \(\phi\), the unit-normal density used in \(p'(P)\), and from \(\Phi_s\), the signal c.d.f. |

**Statement preservation:** This leaves the limiting perturbation unchanged while making every finite-stage strategy a valid probability distribution and completing the notation record.

---

## F17 — Step 12 should begin with the mathematical issue, not the repair history

**Step anchor:** Step 12 opening.

**Current text, quoted**

> “*Restructured 2026-08-25 (round 2) on pass-1 finding 1 and pass-2 R16–R17. The pre-round-2
> argument ran the deviation back to date-0 optimality…*”

**Proposed text**

> The argument must cover every flagged pair, including pairs that the date-0 cutoff policy does not
> select. It therefore cannot rely on date-0 optimality. Fix an arbitrary flagged pair \((j,s)\),
> without assuming \(j=j_k(s)\), and let \(j'\) range over the menu elements generating h.11’s
> round-2 action set.

The repair provenance can remain in the repair tables at the foot of the file.

**Statement preservation:** The replacement states the exact quantifier and proof strategy of Step 12; parts (a)–(d) are unchanged.

---

## F18 — Step 20 should state the threshold equivalence in the extended real line

**Step anchor:** Step 20 closing calculation.

**Current text, quoted**

> “h.8 is equivalent to \(s_F(k^\star)\) being finite and strictly above \(-\infty\).”

**Proposed text**

> Adopt the conventions
>
> $$
> \inf\emptyset:=+\infty,
> \qquad
> \inf\mathbb R:=-\infty.
> $$
>
> Since the flagged set is an upper interval,
>
> $$
> \Omega
> =1-\Phi_s\!\bigl(s_F(k^\star)\bigr),
> $$
>
> with the natural endpoint values at \(\pm\infty\). Hence
>
> $$
> 0<\Omega<1
> \quad\Longleftrightarrow\quad
> s_F(k^\star)\in\mathbb R.
> $$

**Statement preservation:** This is exactly the same A8 restatement, with the empty and full flagged sets handled explicitly.

# FINDINGS — UNCLEAR

## F19 — The claimed four-action derivation of the common bracket cannot be checked from this paste

**Step anchor:** Step 14.

**Current text, quoted**

> “In the four-action version of this model that the frozen manuscript works with, the bracket is
> proved rather than assumed: there the blockholder’s payoff to each action is affine in the
> posterior mean … with totally ordered slopes …; the engagement cost is continuous, strictly
> positive and strictly decreasing with full range on the half-line.”

**What is missing**

The paste does not supply:

* the four action-specific payoff formulas;
* the claimed slope coefficients;
* the uniform intercept bounds;
* the engagement-cost function or its domain;
* the argument that every adjacent indifference equation has a solution rather than merely at most one;
* the source passage in the frozen manuscript on which these claims rest.

The card’s general \(U_j\) row supplies plan-locality and integrability, not these special functional forms. I therefore cannot verify the first paragraph of Step 14 from the stipulated record.

The load-bearing general conclusion—“the common bracket is assumed through h.6”—does not depend on this unverified special-case paragraph.

# PER-STEP VERDICT TABLE

| Step         | Verdict          | Finding         | One line                                                                                                                                                   |
| ------------ | ---------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Step 1       | GAP              | F7              | The conjecture map is measurable, but the proof silently identifies the card’s general ordered polytope with the full bracket polytope.                    |
| Step 2       | WRONG            | F1              | The measurability conclusion is repairable, but the displayed formula evaluates the stake at the crossing date rather than the filing date.                |
| Step 3       | WRONG            | F2              | Pooled histories are finite; the flagged image is empty when no plan flags and otherwise is continuum-sized, not categorically nonfinite.                  |
| Step 4       | POLISH           | F13             | The scalar reduction is sound; the Gaussian-law citation must be h.17-d rather than h.1.                                                                   |
| Step 5       | GAP              | F8, F14         | The control/intermediate split is right, but full belief continuity is not yet proved and the intermediate-date discussion is stale.                       |
| Step 5(a)    | GAP              | F8              | Existence and uniqueness follow from Step 7, but Step 8 as written does not prove continuity in \(\pi\).                                                   |
| Step 5(b)    | POLISH           | F14             | The tower-expectation reading is correct; remove the obsolete alternative reading and the unnecessary cutoff-continuity claim.                             |
| Step 6       | WRONG            | F2              | The measurable-family construction is sound on the flagged image, but the opening wrongly assumes that image is always continuum-sized.                    |
| Step 6(a)    | SOUND AS WRITTEN | —               | On a flagged node, \(D=1\) implies \(a=1\) and hence \(\pi=1\).                                                                                            |
| Step 6(b)    | SOUND AS WRITTEN | —               | At \(\pi=1\), the unique root is a single-valued continuous function of the one remaining belief scalar.                                                   |
| Step 6(c)    | SOUND AS WRITTEN | —               | A7-J plus Borel measurability gives a Borel inverse on the image and hence a Borel posterior mean.                                                         |
| Step 6(d)    | SOUND AS WRITTEN | —               | Composition with the continuous inner-root map gives a Borel flagged-price family on the image.                                                            |
| Step 7       | POLISH           | F15             | Existence and uniqueness are correct; the uniqueness proof can be replaced by a direct monotonicity calculation.                                           |
| Step 7(i)    | SOUND AS WRITTEN | —               | Every root must lie at or above \(A\).                                                                                                                     |
| Step 7(ii)   | SOUND AS WRITTEN | —               | The residual is nonnegative at \(A\) and negative at an explicit finite upper bracket.                                                                     |
| Step 7(iii)  | POLISH           | F15             | Uniqueness is valid, but global negativity of the derivative on \([A,\infty)\) is shorter and stronger.                                                    |
| Step 8       | GAP              | F8              | The derivative in \(\hat v\) is correct, but the step does not establish continuity of the root in the full pair \((\hat v,\pi)\).                         |
| Step 9       | WRONG            | F3, F4, F9, F16 | Reachability and endpoint treatment are sound, but the posterior-limit characterization, reference convention and price-convergence inference need repair. |
| Step 9(a)    | SOUND AS WRITTEN | —               | The realized noise support and whole-history reachability definition correctly cover \(\kappa=0\) and \(\kappa=1\).                                        |
| Step 9(b)    | WRONG            | F3, F9, F16     | The limit is not plan-uniform on path, and price convergence omits convergence of \(\pi\); notation also needs cleanup.                                    |
| Step 9(c)    | WRONG            | F4              | The proposed “fixed” prior engagement probability is endogenous to \(k\), so the convention is not fixed across the outer map.                             |
| Step 9(d)    | SOUND AS WRITTEN | —               | The support-based treatment correctly extends the argument to both boundary values of \(\kappa\).                                                          |
| Step 10      | SOUND AS WRITTEN | —               | A7-J supplies a Borel inverse, and the point-mass kernel is a valid selected version on every image tuple.                                                 |
| Step 11      | SOUND AS WRITTEN | —               | The timing and payoff definition yield the stated pooled/flagged decomposition.                                                                            |
| Step 12      | POLISH           | F17             | The four-part sequential-optimality lemma is sound; its opening should state the mathematical purpose rather than repair history.                          |
| Step 12(a)   | SOUND AS WRITTEN | —               | All class members reveal the same \(s\) and \(\pi=1\), so the unique flagged price is invariant.                                                           |
| Step 12(b)   | SOUND AS WRITTEN | —               | Full separation makes the blockholder’s conditional value equal the competitive fixed-point price.                                                         |
| Step 12(c)   | SOUND AS WRITTEN | —               | The flagged order cancels from terminal value minus purchase cost, leaving only the common initial stake and engagement cost.                              |
| Step 12(d)   | SOUND AS WRITTEN | —               | Under either cost timing, h.16 makes every plan-generated order a maximizer.                                                                               |
| Step 13      | WRONG            | F5, F7          | The largest monotone selection exists, but the finite-boundary corner code does not represent empty upper sets on the Gaussian tails.                      |
| Step 14      | UNCLEAR          | F19             | The general theorem assumes the bracket; the claimed four-action derivation cannot be checked from the pasted materials.                                   |
| Step 15      | WRONG            | F6, F10         | The step first asserts cutoff continuity that the proof does not derive, then invokes a strict sign change not supplied by its stated condition.           |
| Step 15(i)   | SOUND AS WRITTEN | —               | Joint continuity is correctly identified as an additional sufficient-condition candidate, not as a derived fact.                                           |
| Step 15(ii)  | GAP              | F10             | Empty interior of the tie set does not itself supply the robust sign pattern used in the following continuity argument.                                    |
| Step 16      | SOUND AS WRITTEN | —               | Given the named single-valued continuous self-map in h.6, Brouwer yields a fixed point.                                                                    |
| Step 17      | WRONG            | F5              | Items (ii)–(vi) are largely assembled correctly, but item (i) and the claimed almost-sure consistency fail under the printed corner code.                  |
| Step 17(i)   | WRONG            | F5              | A weakly increasing map with an empty upper level set is not represented almost surely by the finite cutoff vector defined in Step 13.                     |
| Step 17(ii)  | SOUND AS WRITTEN | —               | The selected plan is pointwise optimal and the flagged continuation is sequentially optimal under h.11 and h.16.                                           |
| Step 17(iii) | SOUND AS WRITTEN | —               | On-path pooled beliefs are Bayes posteriors and flagged beliefs use the selected point-mass version.                                                       |
| Step 17(iv)  | GAP              | F8, F9          | The fixed-point pricing claim at reachable off-path pooled histories needs the missing \(\pi\) convergence and joint root continuity.                      |
| Step 17(v)   | SOUND AS WRITTEN | —               | The bidder-entry probability follows from the same public price and engagement posterior.                                                                  |
| Step 17(vi)  | SOUND AS WRITTEN | —               | The perturbation construction supplies limits on required reachable histories and selected versions on flagged image tuples.                               |
| Step 18      | GAP              | F11             | Convex values and a closed graph for the cutoff correspondence are asserted but not proved by the one-line plateau argument.                               |
| Step 19      | WRONG            | F5              | The positivity implication from A8 is sound, but the claimed almost-sure equivalence of \(j^\star\) and \(j_k\) can fail on a positive Gaussian tail.      |
| Step 20      | POLISH           | F18             | The upper-set reduction is sound under its three extra conditions; the endpoint equivalence should be stated with extended-real conventions.               |
| Step 20(a)   | SOUND AS WRITTEN | —               | Upper-set engagement flags make engagement monotone in the selected plan index.                                                                            |
| Step 20(b)   | SOUND AS WRITTEN | —               | Within-plan Voice stake monotonicity makes the threshold test weakly increasing in \(s\).                                                                  |
| Step 20(c)   | SOUND AS WRITTEN | —               | Across-plan stake monotonicity preserves the threshold test at upward plan switches.                                                                       |

# OVERALL JUDGMENT

No: as written, this is not yet at the standard of the best published existence proofs in the literature, although substantial parts—especially the scalar pricing reduction, the measurable flagged-price construction and the four-part Step 12 continuation lemma—are unusually careful and close to that standard. The decisive problem is not the measured failure of A3 or A6 at the implemented calibration, which remains an applicability matter; it is that the proof does not currently establish its own conditional theorem under the printed cutoff coding. The three changes that close most of the distance are, ranked: **(1)** repair Steps 1, 13, 17(i) and 19 so that finite corner values genuinely represent empty/full action regions on the entire Gaussian signal line, or add explicit tail hypotheses to the statement; **(2)** repair the inner-belief chain in Steps 2 and 8–9—the filing-date formula, the two-case posterior limit, the \(k\)-independent unreachable-history convention, convergence of \(\pi_n\), and joint root continuity—so every off-path price used by \(\mathcal T\) is actually obtained as claimed; **(3)** rewrite Steps 15 and 18 as a clean separation between what h.6 assumes and what optional primitive lemmas would be needed to derive it, while moving the inline repair chronology to the audit tables. With those changes, the proof would have a defensible theorem-to-argument match; without the first one, the P1 row should not remain PROVED on the strength of this proof.

# NOTATION DELTA

All proof-local symbols quoted above retain the meanings assigned in the proof’s own NOTATION DELTA. The following additions or clarifications occur in this review:

| Symbol                                                                                                                                                                          | Meaning                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| \(\widetilde B_j^F,\widetilde Q_j^F\)                                                                                                                                           | Borel extensions of the filing stake and residual order off the flagged set; they equal \(B_j^F,Q_j^F\) on \(\{D_j=1\}\). |
| \(\mu_\infty(j,s)\)                                                                                                                                                             | Pointwise limiting joint posterior density in Step 9(b), with separate formulas for \(\Lambda_k>0\) and \(\Lambda_k=0\).  |
| \(\pi_n\)                                                                                                                                                                       | Stage-\(n\) engagement posterior \(\sum_j a_j\int\mu_n(j,s)\,ds\).                                                        |
| \(d_i(s,k)\)                                                                                                                                                                    | Adjacent payoff difference \(U_{i+1}(s;k)-U_i(s;k)\) used in the proposed Step 15 repair.                                 |
| \(c_i(k)\)                                                                                                                                                                      | Unique robust sign threshold for \(d_i(\cdot,k)\) in the proposed Step 15 repair.                                         |
| \(\varphi_s\)                                                                                                                                                                   | Density of the Gaussian signal \(s\); already used in the proof but missing from its NOTATION DELTA.                      |
| \(j_k,j^\star,\mathcal S(k),\mathfrak T,\mu_n,L_j,w_n,t_n,Z_n,\Lambda_k,\Lambda_u,\mathcal P_{\mathcal I},\varrho,(\hat v_\circ,\pi_\circ),P_\circ,[\underline s,\overline s]\) | Inherited without alteration from the proof’s declared proof-local notation.                                              |

# NOT CLAIMED

* This pass does not audit D1, A7’s construction proof, L2 or any of the other seven proofs; P1 consumes those results by statement with their hypotheses travelling.
* It does not rerun or reassess the numerical implementation, ticket-34 nodes, or the settled applicability findings for A3, A6 and A\((\tau)\).
* It does not verify Step 14’s four-action specialisation because the required action-level payoff formulas are absent from the stipulated paste.
* It does not formally move the P1 label. Under the lane’s rules, the findings above are demotion-capable review findings, and every proposed repair remains CONJECTURE-grade edit text until the amended proof passes the required independent gates.
