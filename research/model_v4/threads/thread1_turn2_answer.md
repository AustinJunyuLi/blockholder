D1 — Rule-keyed partition and timing-split representation
CLAIM
Under the model-card plan, calendar, legal-clock, and pricing definitions, (D_j(s;\tau,T)) is a measurable binary function of the realised complete history whose observed value assigns every control-node public history to exactly one of (\mathcal C_F) and (\mathcal C_P); for every Voice plan, (f_j(s;\tau,T)\le H) if and only if (B_j(s,H-T)\ge\tau); and every flagged history yields well-defined (B^F,R_d,R,J) satisfying (P^F-P_{c^-}^P=R+J).
HYPOTHESES

1. Finite plan and public-history structure. A2 holds; (T\in{1,\ldots,H}); (\Gamma) has finite image; and the model-card plan restrictions hold, including that (s\mapsto B_j(s,d)) and (d\mapsto B_j(s,d)) are weakly increasing for every Voice plan.
2. Legal-clock discipline. A4 holds: (c_j(s;\tau)) is the first date in ({0,\ldots,H}) at which (B_j(s,d)\ge\tau), with (c_j=+\infty) if the set is empty; (f_j=c_j+T), with (+\infty+T=+\infty); only Voice plans cross in the core; and the filing lands exactly at (f_j).
3. Well-defined prices. A5 holds, so every pooled or flagged public history used below has a unique competitive price.
4. Price-path definitions. On a flagged history, (P_{\mathrm{ND}}(\mathcal H_{f^-}^P)) is defined as the pooled price at the same realised order-flow history under no flag and therefore equals (P_{f^-}^P); (R_d=P_d^P-P_{c^-}^P), (R=P_{f^-}^P-P_{c^-}^P), and (J=P^F-P_{\mathrm{ND}}(\mathcal H_{f^-}^P)).

PROOF

1. Fix a Voice plan (j) and a date (d). Hypothesis 1 makes (s\mapsto B_j(s,d)) weakly increasing, so the set ({s:B_j(s,d)\ge\tau}) is an upper interval, possibly empty or all of the signal line, and is therefore Borel measurable. (Hypothesis 1.)
2. The event ({c_j(s;\tau)\le H-T}) equals the finite union
[
\bigcup_{d=0}^{H-T}{B_j(s,d)\ge\tau}.
]
Step 1 makes each member measurable, and Hypothesis 1 makes the union finite. (Hypotheses 1–2; Step 1.)
3. Because (f_j=c_j+T) and (T\le H), (f_j\le H) is equivalent to (c_j\le H-T), including the case (c_j=+\infty), for which both inequalities are false. (Hypothesis 2.)
4. Suppose (c_j\le H-T). The date set is finite, so the infimum in Hypothesis 2 is a minimum and (B_j(s,c_j)\ge\tau); weak increase in the calendar date gives
[
B_j(s,H-T)\ge B_j(s,c_j)\ge\tau.
]
(Hypotheses 1–2; Step 3.)
5. Suppose (B_j(s,H-T)\ge\tau). Then (H-T) belongs to the nonempty set whose first element defines (c_j), so (c_j\le H-T), and Step 3 gives (f_j\le H). (Hypothesis 2; Step 3.)
6. Steps 4–5 do not require a strict crossing: when (B_j(s,c_j)=\tau) and the path is flat at (\tau) through date (H-T), (c_j) remains the first hitting date and (B_j(s,H-T)=\tau), so both sides of the equivalence remain true. (Steps 4–5.)
7. By Hypothesis 2, non-Voice plans do not cross and have (D_j=0); for Voice plans, Steps 3–5 give
[
D_j(s;\tau,T)
\mathbf 1{a_j=1},
\mathbf 1{B_j(s,H-T)\ge\tau}.
]
Step 1 makes the second indicator measurable, while (a_j) is fixed by the finite plan index. Hence (D_j) is a well-defined measurable map from every realised history to ({0,1}). (Hypotheses 1–2; Steps 1 and 3–5.)
8. Hypothesis 1 makes every pre-filing pooled-history alphabet finite: each (q_{jd}(s)) lies in the finite image of (\Gamma), each (z_d) has three values, the flag coordinate has two values, and the calendar has finitely many dates. Steps 1–5 make (f_j) a measurable finite-valued function on the flagged set; hence (B_j^F=B_j(s,f_j)) and (Q_j^F=b_j^*(s)-B_j^F) are measurable there. A flagged control-node history augments one finite pooled history by the measurable tuple ((B^F,Q^F,a=1)), so the full control-node history space is a finite union of measurable pooled and flagged components and its observed flag coordinate is measurable. (Hypothesis 1; Steps 1–7.)
9. Define
[
\mathcal C_F
{\text{control-node histories}:D=1},
\qquad
\mathcal C_P
{\text{control-node histories}:D=0}.
]
A history cannot satisfy (D=1) and (D=0) simultaneously, so
[
\mathcal C_F\cap\mathcal C_P=\varnothing.
]
Every binary value is either zero or one, so
[
\mathcal C_F\cup\mathcal C_P
]
is the entire control-node history set. Measurability follows because both cells are preimages of singleton subsets of ({0,1}) under the measurable map in Step 7. (Steps 7–8.)
10. No probability restriction entered Steps 7–9. The partition therefore exists even when (\Pr(D=1)=0) or (\Pr(D=1)=1); A8 is needed only when both cells must have positive mass. (Step 9.)
11. On a flagged history, Step 7 and Hypothesis 2 give (c_j<\infty) and (f_j\le H). Thus (B_j^F=B_j(s,f_j)) is evaluated at a date in the model calendar, the pooled dates from (c_j) through (f_j^-) are finite, and Hypothesis 3 supplies the prices entering (R_d,R,J). (Hypotheses 2–3; Step 7.)
12. Add and subtract the same-order-flow counterfactual from Hypothesis 4:
[
\begin{aligned}
P^F-P_{c^-}^P
&=
\bigl[
P^F-P_{\mathrm{ND}}(\mathcal H_{f^-}^P)
\bigr]

* 

\bigl[
P_{\mathrm{ND}}(\mathcal H_{f^-}^P)-P_{c^-}^P
\bigr]
\
&=
J+\bigl[P_{f^-}^P-P_{c^-}^P\bigr]
\
&=
J+R.
\end{aligned}
]
(Hypothesis 4; Step 11.)

13. The measurable binary map, cell exclusivity and exhaustion, and legal-clock equivalence in Steps 1–10 carry representational content. The existence of the named price-path objects in Step 11 uses the model’s timing and unique pricing. The equality in Step 12 is definitional bookkeeping—an exact accounting identity produced by the same-order-flow definition of (P_{\mathrm{ND}}), not an economic sign theorem. (Steps 1–12.)

WHERE IT FAILS

1. If a Voice stake path may fall after first reaching (\tau), then (c_j\le H-T) need not imply (B_j(s,H-T)\ge\tau); for example, the path can hit (\tau) at date zero and fall below it before (H-T).
2. If filing occurs at a discretionary date unrelated to (c_j+T), then (f_j\le H\iff c_j\le H-T) is unavailable, so the window cannot be represented by (B_j(s,H-T)\ge\tau).
3. If (P_{\mathrm{ND}}) is evaluated at a different order-flow history rather than the same realised one, then the second bracket in Step 12 is not (R) and the stated timing split does not hold.
4. If A5 fails and a public history supports multiple selected prices, the cells still partition histories, but (R_d,R,J) are not single-valued without an additional price-selection rule.

LABEL CLAIMED
PROVED — CONJECTURE (\rightarrow) PROVED. Steps 1–13 independently derive the measurable partition, the Voice-path clock equivalence including a flat-at-(\tau) path, and the exact timing split. The label does not rely on a numerical run; the pending script is a separate implementation check. The structural partition does not require A8.
NUMERICAL CHECK REQUEST
Run one history-enumeration script over
[
\kappa\in{0.15,0.35,0.55,0.75,0.85},
\qquad
T\in{5,10},
]
and thresholds equal to the 10th, 30th, 50th, 70th, and 90th percentiles of the equilibrium Voice stake paths. For every grid node, compute
[
\max_{j,s:a_j=1}
\left|
\mathbf 1{f_j(s;\tau,T)\le H}
\mathbf 1{B_j(s,H-T)\ge\tau}
\right|,
]
the number of histories with (D\notin{0,1}), the overlap mass
[
\Pr(\mathcal C_F\cap\mathcal C_P),
]
the exhaustion residual
[
\left|
\Pr(\mathcal C_F)+\Pr(\mathcal C_P)-1
\right|,
]
and
[
\max_{D=1}
\left|
P^F-P_{c^-}^P-R-J
\right|.
]
The predicted signed discrepancies are all zero. The required numerical magnitudes are zero binary/equivalence violations and residuals below (10^{-12}). Under the interiority calibration, the predicted minimum mass of each cell is at least the chosen grid floor (0.01); outside that calibration, only the zero partition and timing-split residuals are predicted.
NOTATION DELTA
None.
NOT CLAIMED
Positive mass in both cells without A8; a sign for (R), (J), or any (R_d); (\kappa)-invariance of (J); endogenous filing before the deadline; or a causal interpretation of the accounting timing split.
L1 — Premium cell decomposition
CLAIM
For every integrable engagement-premium kernel, (0<\Omega<1) implies
[
\Delta^{\mathrm{act}}
\Omega M_F+(1-\Omega)M_P;
]
at (\Omega=1) the identity degenerates to (\Delta^{\mathrm{act}}=M_F), and at (\Omega=0) it degenerates to (\Delta^{\mathrm{act}}=M_P).
HYPOTHESES

1. Binary measurable partition. D1 holds, so (D\in{0,1}) is measurable and ({D=1},{D=0}) are disjoint and exhaustive.
2. Integrability. (\Delta_m h(\mathcal I_H)) is measurable and integrable:
[
\mathbb E!\left[
\left|
\Delta_m h(\mathcal I_H)
\right|
\right]<\infty.
]
In the model card this condition is automatic because (0\le\pi\le1), (0<p<1), (h=\pi p\in[0,1]), and (\Delta_m) is finite.

PROOF

1. Because (D) is binary,
[
\mathbf 1{D=1}
+
\mathbf 1{D=0}
1
]
on every history. (Hypothesis 1.)
2. Multiply Step 1 by the integrable variable (\Delta_m h(\mathcal I_H)) and take expectations:
[
\Delta^{\mathrm{act}}
\mathbb E!\left[
\Delta_m h(\mathcal I_H)\mathbf 1{D=1}
\right]
+
\mathbb E!\left[
\Delta_m h(\mathcal I_H)\mathbf 1{D=0}
\right].
]
Both expectations are finite. (Hypothesis 2; Step 1.)
3. If (0<\Omega<1), the defining property of conditioning on an event with positive probability gives
[
\begin{aligned}
\mathbb E!\left[
\Delta_m h(\mathcal I_H)\mathbf 1{D=1}
\right]
&=
\Pr(D=1),
\Delta_m
\mathbb E[h(\mathcal I_H)\mid D=1]
\
&=
\Omega M_F,
\end{aligned}
]
and
[
\mathbb E!\left[
\Delta_m h(\mathcal I_H)\mathbf 1{D=0}
\right]
(1-\Omega)M_P.
]
(Hypotheses 1–2; Step 2.)
4. Substituting the two equalities from Step 3 into Step 2 yields
[
\Delta^{\mathrm{act}}
\Omega M_F+(1-\Omega)M_P.
]
(Steps 2–3.)
5. If (\Omega=1), then (D=1) almost surely, the second expectation in Step 2 is zero, and the positive-mass conditional average (M_F) satisfies
[
\Delta^{\mathrm{act}}=M_F.
]
The ordinary conditional average (M_P) is not defined because (\Pr(D=0)=0). (Hypotheses 1–2; Step 2.)
6. If (\Omega=0), then (D=0) almost surely, the first expectation in Step 2 is zero, and the positive-mass conditional average (M_P) satisfies
[
\Delta^{\mathrm{act}}=M_P.
]
The ordinary conditional average (M_F) is not defined because (\Pr(D=1)=0). (Hypotheses 1–2; Step 2.)
7. At either boundary, no convention is needed for the degenerate identity in Steps 5–6. If the equilibrium’s full-support perturbations assign a finite off-path cell average, that value may be inserted into the zero-weight term, but it is a convention rather than an identified conditional expectation. (Steps 5–6.)

WHERE IT FAILS

1. If the purported cells overlap or omit histories, Step 1 is false and the two-term decomposition double-counts or loses probability mass.
2. If (\Delta_m h(\mathcal I_H)) is not integrable, the expectations in Step 2 need not be finite and the decomposition may be undefined as an equality of real numbers.
3. At (\Omega\in{0,1}), treating the null-cell average as uniquely identified is invalid; only the positive-mass degenerate identity is intrinsic.

LABEL CLAIMED
PROVED — CONJECTURE (\rightarrow) PROVED. Steps 1–7 give a complete independent derivation, including the two boundary cases and the status of null-cell conditional averages. The result is an accounting identity, not a comparative-static theorem.
NUMERICAL CHECK REQUEST
Using the D1 grid
[
\kappa\in{0.15,0.35,0.55,0.75,0.85},
\qquad
T\in{5,10},
]
with (\tau) at the 10th, 30th, 50th, 70th, and 90th percentiles of equilibrium Voice stake paths, compute (\Delta^{\mathrm{act}}) once by direct summation over all histories and once as
[
\Omega M_F+(1-\Omega)M_P
]
at every interior node.
Also run one all-pooled policy with (\Omega=0) and one all-flagged policy with (\Omega=1) and verify the degenerate identities, recording the zero-mass cell average as undefined rather than imputing it.
The predicted signed residual is zero in every case; the required absolute residual is below (10^{-12}). Report (\Delta^{\mathrm{act}},M_F,M_P) in premium percentage points, not normalized indices.
NOTATION DELTA
None.
NOT CLAIMED
A sign for (M_F-M_P); positive mass in both cells without A8; a causal interpretation of the cell decomposition; or a uniquely identified conditional average for a zero-mass cell.
L2 — Flagged-cell direct liquidity-invariance
CLAIM
At fixed cutoff and execution policies, under A1, A4, A5, A7 in its injective-recoverability form, and (\Omega>0), ((B^F,Q^F,a=1)) makes the pre-filing pooled history conditionally independent of ((v,s,\xi)) on the flagged set, so the flagged posterior, unique price (P^F), bidder-entry probability, and (M_F) are constant in noise-trading intensity (\kappa).
HYPOTHESES

1. Independent primitives. A1 holds: the full noise vector is independent of ((v,\varepsilon,\xi)), and hence of ((v,s,\xi)) because (s=v+\varepsilon).
2. Finite histories. A2 holds, so the calendar and pooled public-history support are finite and every pre-filing history is a measurable function of finitely many order-flow observations.
3. Truthful flagged purpose. A4 holds, so (D=1) implies (a=1), the filing truthfully reports (F=(B^F,a=1)), and (f) is determined by the selected plan and signal.
4. Unique flagged price. A5 holds, so the flagged competitive-pricing map has one fixed point at every on-path flagged information set.
5. Injective filing sufficiency. A7 is used in its recoverability form: on the flagged set the measurable map
[
(j,s)
\mapsto
\bigl(
B_j(s,f_j(s;\tau,T)),
Q_j^F(s;\tau,T),
a_j
\bigr)
]
is injective and the plan-and-signal pair ((j,s)) is measurable with respect to the observed tuple; equivalently, the map has a measurable inverse on its image.
6. Fixed-policy direct comparison. As (\kappa) varies, the cutoff mapping from (s) to (j), every (B_j(s,d)), every (Q_j^F(s;\tau,T)), (\tau), (T), and all non-noise primitives are held fixed; the flagged-round order is observed without an additional (\kappa)-dependent noise term; (\kappa) parameterizes only the law of the pooled (z_d) draws.
7. Positive flagged mass. (\Omega=\Pr(D=1)>0), so conditioning on the flagged cell and the cell average (M_F) are defined under the ordinary equilibrium probability law.

PROOF

1. On the flagged set define
[
\mathsf S_F:=(B^F,Q^F,a=1)
]
and write
[
\mathcal H^P:=\mathcal H_{f^-}^P.
]
Hypothesis 5 supplies a measurable inverse (\iota_F) on the image of (\mathsf S_F), so
[
(j,s)=\iota_F(\mathsf S_F)
]
on every flagged history. Thus (\mathsf S_F) identifies the plan and signal, not merely the broad action class. (Hypothesis 5.)
2. Conditional on a fixed pair ((j,s)), Hypotheses 2–3 and 6 determine (f), each informed order mark (q_{jd}(s)), and every pre-filing flag coordinate. Since
[
X_d=q_{jd}(s)+z_d,
]
there is a deterministic measurable map (G_{j,s}) such that
[
\mathcal H^P
G_{j,s}(z_0,\ldots,z_{f-1}).
]
(Hypotheses 2–3 and 6.)
3. Let
[
W:=(v,s,\xi),
\qquad
\mathbf z^H:=(z_0,\ldots,z_H).
]
Hypothesis 1 makes (\mathbf z^H) independent of (W). Under Hypothesis 6, the selected (j), the event (D=1), and (\mathsf S_F) are functions of (W) and fixed policy objects, not of (\mathbf z^H). Therefore, at each fixed (\kappa) and for every measurable set of noise vectors, almost surely on (D=1),
[
\begin{aligned}
&\mathbb E!\left[
\mathbf 1{\mathbf z^H\text{ is in that set}}
\mid W,\mathsf S_F,D=1
\right]
\
&\qquad=
\Pr(\mathbf z^H\text{ is in that set})
\
&\qquad=
\mathbb E!\left[
\mathbf 1{\mathbf z^H\text{ is in that set}}
\mid\mathsf S_F,D=1
\right].
\end{aligned}
]
The middle probability may vary with (\kappa); the equality shows that pooled noise remains independent of (W) after conditioning on the flagged event and tuple. (Hypotheses 1 and 6; Step 1.)
4. Let (u_1) and (u_2) be bounded measurable test functions. Using Steps 1–3 and iterated conditioning,
[
\begin{aligned}
&\mathbb E[
u_1(W)u_2(\mathcal H^P)
\mid\mathsf S_F,D=1
]
\
&=
\mathbb E!\left[
u_1(W)
\mathbb E!\left[
u_2!\left(
G_{\iota_F(\mathsf S_F)}(\mathbf z^H)
\right)
\mid W,\mathsf S_F,D=1
\right]
\middle|
\mathsf S_F,D=1
\right]
\
&=
\mathbb E!\left[
u_1(W)
\mathbb E[
u_2(\mathcal H^P)
\mid\mathsf S_F,D=1
]
\middle|
\mathsf S_F,D=1
\right]
\
&=
\mathbb E[
u_1(W)\mid\mathsf S_F,D=1
]
,
\mathbb E[
u_2(\mathcal H^P)\mid\mathsf S_F,D=1
].
\end{aligned}
]
The second equality uses the independence in Step 3; the final equality uses that the second conditional expectation is measurable with respect to (\mathsf S_F). This factorization proves the required conditional-independence statement
[
(v,s,\xi)
\ \perp!!!\perp
\mathcal H^P
\ \big|
(B^F,Q^F,a=1)
\qquad
\text{under the conditional law given }D=1.
]
(Steps 1–3.)
5. The conditional independence in Step 4 implies, for every measurable event concerning ((v,s,\xi)),
[
\Pr!\left(
(v,s,\xi)\in\cdot
\mid
\mathsf S_F,\mathcal H^P,D=1
\right)
\Pr!\left(
(v,s,\xi)\in\cdot
\mid
\mathsf S_F,D=1
\right).
]
The pooled history therefore supplies no posterior refinement once (\mathsf S_F) is observed. (Step 4.)
6. Hypothesis 6 makes (\mathsf S_F) and (D) functions of the fixed policy and ((j,s)), while Hypotheses 1 and 6 place (\kappa) only in the law of (\mathbf z^H). The joint law of
[
(W,\mathsf S_F,D)
]
is therefore the same for every (\kappa), so the right-hand conditional law in Step 5 can be chosen identically across (\kappa), up to conditional null sets. The distribution of (\mathcal H^P) conditional on (\mathsf S_F) generally does vary with (\kappa), but Step 5 removes that distribution from the flagged posterior. (Hypotheses 1 and 6; Steps 1 and 5.)
7. Step 5 gives the full flagged posterior of ((v,s,\xi)), including
[
\mathbb E[
v\mid
\mathsf S_F,\mathcal H^P,D=1
],
]
as a function of (\mathsf S_F) alone; Step 6 makes that posterior independent of (\kappa). Hypothesis 3 also makes (a=1) part of the truthful flagged information, so
[
\pi(\mathsf S_F,\mathcal H^P)
\Pr(
a=1
\mid
\mathsf S_F,\mathcal H^P,D=1
)
   1. 
]
(Hypothesis 3; Steps 5–6.)
8. At a fixed flagged tuple, the competitive price solves
[
P
\mathbb E!\left[
(1-\mathsf B)(v+\Delta_V)
+
\mathsf B(P+m_1)
\mid
\mathsf S_F,\mathcal H^P,D=1
\right],
]
where, because Step 7 gives (\pi=1),
[
\mathsf B
\mathbf 1
{
\bar S+\xi-K-P-m_1\ge0
}.
]
Steps 5–7 make the conditional law entering the right-hand side independent of (\mathcal H^P) and (\kappa); Hypothesis 6 excludes a second (\kappa)-dependent noise source in (Q^F). Thus the flagged pricing map is the same for every (\kappa). (Hypothesis 6; Steps 5–7.)
9. Hypothesis 4 gives that the (\kappa)-independent pricing map in Step 8 has one fixed point, so its selected solution
[
P^F=P(F,Q^F)
]
is constant in (\kappa). Without uniqueness, an extraneous fixed-point selection could vary with (\kappa) even when the map itself does not. (Hypothesis 4; Step 8.)
10. Substituting Step 7 and the (\kappa)-invariant price from Step 9 into the bidder rule gives the flagged entry probability
[
p
1-\Phi!\left(
\frac{
P^F+K+m_1-\bar S
}{
\sigma_\xi
}
\right),
]
which is constant in (\kappa). (Steps 7 and 9.)
11. Under Hypotheses 1 and 6, the joint law of ((\mathsf S_F,D)) is independent of (\kappa), because both are functions of the (\kappa)-invariant signal/plan policy rather than of (z_d). Hypothesis 7 makes the flagged conditional law well defined; Step 7 gives (h=\pi p=p) on (D=1); and Step 10 makes that integrand (\kappa)-invariant. Hence
[
M_F
\Delta_m,
\mathbb E[p\mid D=1]
]
is constant in (\kappa). (Hypotheses 1, 6–7; Steps 7 and 10.)
12. The only direct entry point for (\kappa) is the probability law of the pooled noise draws in Hypothesis 6. Step 4 removes the resulting pooled-history variation from the flagged posterior; Steps 8–11 then remove it from price, entry, and (M_F). If equilibrium cutoffs or execution paths move with (\kappa), Hypothesis 6 no longer applies and those policy and composition responses are GE channels outside this result. (Hypothesis 6; Steps 4 and 8–11.)

WHERE IT FAILS

1. If two distinct pairs ((j,s)) produce the same ((B^F,Q^F,a=1)) but different pooled informed-order paths, then (\mathcal H^P) can distinguish those pairs; its likelihood depends on the (z_d) law and the flagged posterior can depend on (\kappa).
2. If the flagged-round order is mixed with an unobserved noise order whose distribution is indexed by (\kappa), then the flagged information itself retains a direct (\kappa) channel.
3. If A5 permits multiple flagged price fixed points and the selection rule varies with (\kappa), the posterior can be invariant while the selected (P^F) is not.
4. If cutoffs, plan choice, stake paths, or (Q^F) respond to (\kappa), then the theorem’s fixed-policy hypothesis fails; (M_F) can move through flagged-cell composition even when each fixed-tuple posterior remains directly invariant.
5. If purpose is not truthful or passive plans can be flagged without being distinguished, then (\pi) need not equal one on (\mathcal C_F).
6. If (\Omega=0) and no full-support limiting belief is specified, the flagged conditional law and (M_F) are not identified by the equilibrium probability law.

LABEL CLAIMED
PROVED under A7’s injective-recoverability form — CONJECTURE (\rightarrow) PROVED. Step 4 proves the required conditional-independence statement rather than assuming it; Steps 5–11 transmit that result through the posterior, unique pricing fixed point, bidder rule, and flagged-cell average. The weaker verbal phrase “identifies the informed component” is not sufficient if it permits multiple ((j,s)) pairs with different pooled paths; the proof uses the card’s injective A7 in its measurable-recoverability meaning. The ordinary conditional-independence and (M_F) statements require (\Omega>0); a zero-mass flagged cell would need a separately specified off-path limiting belief. No numerical output is used for this label.
NUMERICAL CHECK REQUEST
Freeze one equilibrium cutoff and execution policy at each
[
T\in{5,10}
]
and at thresholds equal to the 10th, 30th, 50th, 70th, and 90th percentiles of equilibrium Voice stake paths. Vary
[
\kappa\in{0.05,0.10,\ldots,0.95}.
]
For every on-path flagged tuple and for (M_F), compute
[
\operatorname{range}_{\kappa}\mathsf Z
\max_{\kappa}\mathsf Z
\min_{\kappa}\mathsf Z
]
for each flagged engagement posterior, each conditional-value posterior used by pricing, (P^F), bidder-entry probability (p), and (M_F), and compute central finite-difference derivatives in (\kappa).
The predicted sign is zero and the predicted economic magnitude is exactly zero for every object. Numerical acceptance requires every range below (10^{-10}) and every finite-difference derivative below (10^{-8}) in absolute value.
NOTATION DELTA
(\mathsf S_F=(B^F,Q^F,a=1)) is the full observed flagged tuple; (\mathcal H^P=\mathcal H_{f^-}^P) is shorthand for the pre-filing pooled history on a flagged path; (W=(v,s,\xi)); (\mathbf z^H=(z_0,\ldots,z_H)); (\iota_F) is the measurable inverse supplied by injective A7; (G_{j,s}) is the deterministic map from pooled noise draws to the pre-filing public history; (u_1,u_2) are bounded measurable test functions used only to establish conditional independence; and (\mathsf Z) is a generic scalar object in the numerical range check.
NOT CLAIMED
GE invariance when cutoffs or execution policies move with (\kappa); (\kappa)-invariance of the filing-day jump (J); invariance under noisy or partially revealing flagged-round trading; any off-path flagged posterior or cell average when (\Omega=0) without a specified limiting belief; or equilibrium uniqueness beyond the unique inner price imposed by A5.
