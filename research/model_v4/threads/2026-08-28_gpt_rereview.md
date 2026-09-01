# GPT Pro re-review — 2026-08-28 — filed verbatim

**Courier record.** Austin pasted `threads/gpt_rereview_bundle_2026-08-28.md` (built against card
stamp 2026-08-28 · follow-up curation · commit `926f58c`) to GPT Pro and pasted the response back
the same day. The response is filed byte-for-byte below the separator — no edits, no reflow; the
doubled plain-text/LaTeX display lines are artifacts of copying from the GPT interface and are
preserved as received. The in-house audit is a separate file
(`threads/2026-08-28_gpt_rereview_audit.md`); per the standing rule, this review can demote
labels but never promote, and no repair below lands without the audit.

---

Reviewed against MODEL CARD stamp 2026-08-28 · follow-up curation · commit `926f58c`.
Verdict index
D1 — LABEL STANDS
L1 — LABEL STANDS
L2 — LABEL STANDS
L3 — LABEL STANDS
L4 — LABEL STANDS
P1 — LABEL STANDS
T1 — LABEL STANDS
C1 — LABEL STANDS
A($\tau$) — LABEL STANDS as an assumption block with adverse applicability evidence
A6 — LABEL STANDS as an assumption block with adverse applicability evidence
A3 — LABEL STANDS as an assumption block with adverse applicability evidence
No label is demoted. The repaired P1 implication survives. The draft_v3 paper text, however, is not clean against the 2026-08-28 stamp: I find five blocking WRONG statements or status descriptions, three material MISCITED items, and several decision-relevant UNCHECKED claims.
The three required answers
1. Is amended P1 the theorem the model needs?
The three ticket-35 repairs are not arbitrary retreats:

* A7-J repairs an actual proof/statement mismatch.
* Continuation-cost equivalence repairs an actual round-2 deviation gap.
* The $\kappa=1$ extension removes a false positivity statement without shrinking the domain.

Those changes produce a valid conditional existence theorem.
But P1 is not the implemented-model existence theorem the paper ultimately needs. Its decisive antecedents A3 and A6 are measured false at the implemented calibration, and the bundle contains no complete exhibited instance satisfying the entire P1 hypothesis set simultaneously. P1 therefore establishes:
If the completed model supplies an ordered cutoff structure and a continuous compact outer self-map, together with the strengthened flagged-information and continuation conditions, then a cutoff PBE exists.
It does not establish that the implemented menu and calibration possess such an equilibrium. The remaining gap is a constructive existence route replacing A3/A6—most plausibly the already identified correspondence-based route—or a verified parameter region on which all P1 antecedents jointly hold.
2. Is "PROVED as a conditional whose antecedent is false here" honest?
Yes as mathematical labelling; no as an applied result for this calibration.
A proved implication remains proved when its antecedent fails. The label becomes misleading only when the paper cites the implication as evidence about the implemented calibration. The draft generally handles this correctly: it says that L3, L4 leg 3, T1 Part B, and P1 say nothing about the implemented model where their antecedents fail.
The substantive problem is usability. At the only implemented calibration:

* A($\tau$) fails at all 180 non-degenerate nodes.
* A6 fails for the declared construction.
* A3 fails at two loci.

Thus the conditional conclusions are not model predictions at that calibration. They are benchmark implications and should be described that way in the abstract, introduction, conclusion, and any discussion of numerical results.
There is also a fourth applicability problem not fully acknowledged by the card: A5's claimed cutoff-continuity content conflicts with the A6 record of discontinuous pooled prices. That affects every row that literally carries full A5, even where its proof only needs a narrower fixed-point or version-pinning property.
3. Does §7.1 drop conditionality?
No material conditionality is dropped.

* Card L3: PROVED under A($\tau$). Paper: `PROVED under A($\tau$)` and expressly says the result says nothing at the implemented calibration.
* Card L4: legs 1–2 outright; leg 3 under A(br). Paper: the same split, including the implemented-calibration failure.
* Card P1: under A3, A6, A7-J and the remaining enumerated conditions. Paper: all are enumerated, and the adjacent remark says A3 and A6 fail at the implemented calibration.
* Card T1: fixed policies, with Part B importing A($\tau$) and A(br). Paper: T-9 and T-11 carry them, and the adjacent remark states that Part B is inapplicable at the calibration.
* Card C1: implication with the region as hypothesis; no named nonempty region. Paper: same status and same limitation.

The paper's defect is staleness, not dropped conditionality: its A6 and A3 evidence paragraphs remain at the 2026-08-27 state while the controlling card is dated 2026-08-28.
D1 — LABEL STANDS
CLAIM
D1 remains PROVED as the conditional measurable-partition, clock-equivalence, and exact price-path decomposition result.
HYPOTHESES

1. A1, A2′, A4, A5, the primitive table restrictions, and the cutoff selection map support the measurable cell construction.
2. Borel regularity for every plan, including Exit, and the filled control-node information set support the pricing objects.
3. The $P_{-1}^P$ and $P_{\mathrm{ND}}$ conventions support the boundary case and the exact identity.

PROOF

1. The paper statement carries every hypothesis and every conclusion in the card row.
2. The displayed Step 1 proves the cutoff selection map is Borel from its finite-breakpoint construction, which is the correct opening for the measurability argument.
3. The exact decomposition is algebraic once $P_{\mathrm{ND}}$ is the same-history not-yet-disclosed price.
4. UNCHECKED: §7.3 supplies only Step 1. I cannot independently inspect D1 Steps 2–13 from this bundle, so the complete proof remains supported by the recorded two-pass evidence rather than by my line-by-line reconstruction.
5. The A5 cutoff-continuity problem classified under P1 below limits D1's applicability under its literal full hypothesis set; it does not contradict the implication under A5.

WHERE IT FAILS

1. If an Exit path is not Borel in $s$, pooled pricing need not be measurable.
2. If $P_{\mathrm{ND}}$ is read as a never-disclosed counterfactual rather than the same-history pre-filing price, the decomposition acquires a residual term.
3. If $c=0$ and $P_{-1}^P$ is not defined, the run-up objects are incomplete.

LABEL CLAIMED + why
LABEL STANDS. No supplied record contradicts D1's conditional conclusion, and its evidence chain satisfies the gate.
NUMERICAL CHECK REQUEST
Enumerate all plan/date combinations over $\kappa\in{0,0.05,\ldots,1}$, all implemented $\tau$ values, and every $T\in{1,\ldots,H}$. Require:
fj≤H  ⟺  Bj(s,H−T)≥τf_j\le H \iff B_j(s,H-T)\ge\tau
with zero violations, and
∣PF−Pc−P−R−J∣<10−12\left|P^F-P_{c^-}^P-R-J\right|<10^{-12}
at every flagged history. Predicted sign: none; predicted magnitude: machine-zero residual.
NOTATION DELTA
None.
NOT CLAIMED
D1 does not prove equilibrium existence, a comparative-static sign, positive mass of either cell, or applicability when its full antecedent fails.
L1 — LABEL STANDS
CLAIM
L1 remains PROVED as the exact two-cell decomposition, including its null-cell non-identification statement.
HYPOTHESES

1. D1 supplies an exclusive and exhaustive measurable partition.
2. The premium definitions supply $\Delta^{\mathrm{act}}$, $M_F$, $M_P$, and $\Omega$.
3. A5 pins the conditional-expectation version; A1 places the objects on one probability space.
4. A2′ and the primitive restrictions make the relevant objects integrable.

PROOF

1. Conditioning on the flagged and pooled cells yields the decomposition whenever both cells have positive mass.
2. At $\Omega=0$ or $\Omega=1$, only the positive-mass cell average is identified.
3. The opening establishes $0\le h\le1$, sufficient for the basic integrability step.
4. UNCHECKED: the bundle omits L1 Steps 2–10, including the full non-identification construction.
5. L1 inherits the A5 applicability issue identified under P1: its implication under A5 stands, but the card has not established full A5 cutoff continuity at the implemented calibration.

WHERE IT FAILS

1. At a null cell, assigning an arbitrary value to its conditional average would turn a non-identified object into an imputed one.
2. If the two cells are not exclusive and exhaustive, the law-of-total-expectation decomposition gains missing or double-counted mass.
3. If different incompatible versions of the conditional expectation are used across terms, the identity need not describe one price system.

LABEL CLAIMED + why
LABEL STANDS. The result is a conditional probability identity with an explicit treatment of degenerate cells, and no contrary record is supplied.
NUMERICAL CHECK REQUEST
Over a grid containing interior values and deliberately constructed $\Omega=0$ and $\Omega=1$ cases, require
∣Δact−ΩMF−(1−Ω)MP∣<10−12\left|\Delta^{\mathrm{act}}-\Omega M_F-(1-\Omega)M_P\right|<10^{-12}
whenever both averages exist. At degenerate cases, verify that the null-cell average is not read or imputed. Predicted magnitude: machine-zero residual.
NOTATION DELTA
None.
NOT CLAIMED
L1 does not identify a null-cell average, determine the sign of either cell's premium, or establish the applicability of A5.
L2 — LABEL STANDS
CLAIM
L2 remains PROVED at fixed cutoff and execution policies under A7′ and its remaining named hypotheses.
HYPOTHESES

1. Fixed policies and no within-window feedback isolate $\kappa$ in the noise law.
2. A7′ pins the signal almost surely on the flagged set through the composed terminal target.
3. A1 supplies noise independence.
4. A2′, A4, A5, D1, $\Omega>0$, and the bidder-entry rule make the flagged posterior, price, entry probability, and cell average well defined.

PROOF

1. Under Hypothesis 1, changing $\kappa$ changes only the distribution of the pooled noise history.
2. Under A7′, the flagged tuple pins the selected on-path signal almost surely.
3. Conditional on that tuple, the residual pooled history is generated by noise independent of $(v,s,\xi)$, so it supplies no additional information about those primitives.
4. The flagged information and its induced price and entry objects therefore do not move with $\kappa$ at fixed policies.
5. MISCITED: §7.2 says the entire A7 failure boundary is "for the on-path form." The card does not scope the whole list that way; a binding stake cap and quantized stakes can also destroy A7-J. This does not weaken L2, which consumes A7′.
6. UNCHECKED: the bundle supplies only L2 Step 1, not the measurable-inverse and information-sandwich steps carrying the main weight.

WHERE IT FAILS

1. If realised order flow or prices feed back into the stake path, $\kappa$ enters policy objects and the freezing argument fails.
2. Under weak A7 alone, two $(j,s)$ pairs can produce the same flagged message while carrying different pooled paths.
3. If $\Omega=0$, $M_F$ is undefined.

LABEL CLAIMED + why
LABEL STANDS. The stated result is the on-path fixed-policy implication verified by the existing two-pass chain; the adverse numerical evidence concerns A($\tau$), not L2's flagged-cell invariance.
NUMERICAL CHECK REQUEST
Freeze one policy and evaluate $\kappa\in{0,0.05,\ldots,1}$. For each positive-mass flagged cell, require the ranges of the flagged posterior, $P^F$, entry probability, and $M_F$ to be below $10^{-12}$. Predicted sign: zero derivative; predicted magnitude: variation below numerical precision.
NOTATION DELTA
None.
NOT CLAIMED
L2 does not make $J$ invariant, make the pooled cell invariant, survive within-window re-optimisation, or establish A7′ at an equilibrium.
L3 — LABEL STANDS
CLAIM
L3 remains PROVED under A($\tau$). It is not applicable to the implemented pooled cell at the tested calibration.
HYPOTHESES

1. A($\tau$), including kernel-through-posterior and $\kappa$-free support with $\kappa$-free $\bar\pi$.
2. $h(0)=0$, fixed pooled mass and engagement moment, and D1.
3. Continuity of $h$ on the closed interval and twice differentiability on the open interval.
4. For the small-$\bar\pi$ conclusion, the Peano expansion, one common kernel, and a uniform bound on $\lvert A'_\kappa\rvert$ along the shrinking family.

PROOF

1. Differentiating a representation with fixed support leaves only the three weight derivatives.
2. The derivative restrictions reduce that derivative to $A'_\kappa C_h(\bar\pi)$.
3. Two mean-value applications produce the exact second-difference identity.
4. The Peano expansion gives the stated second-order asymptotic.
5. MISCITED: the card still cites the upper-support-point degeneracy argument as L3 Step 19, while the paper folds that material into Step 15. The claim is present, but that in-paper step citation does not resolve.
6. UNCHECKED: only Step 1 of the 18-step proof is inlined, so I cannot independently verify the derivative and mean-value steps from the proof text itself.

WHERE IT FAILS

1. If support atoms move with $\kappa$, differentiation adds support-motion terms.
2. If $h$ changes at a fixed posterior because the standalone-value channel changes, the three kernel values are not fixed.
3. If $\bar\pi$ moves with $\kappa$, a first-order endpoint term can dominate the claimed second-order motion.
4. At the implemented calibration the support has 23–767 atoms rather than three.

LABEL CLAIMED + why
LABEL STANDS. The implication under A($\tau$) remains supported. The executed check refutes its antecedent at this calibration, not its derivation.
NUMERICAL CHECK REQUEST
Use synthetic posterior laws that satisfy A($\tau$), quadratic and cubic kernels, $\bar\pi\in{10^{-1},10^{-2},10^{-3},10^{-4},10^{-5}}$, and both signs of $A'_\kappa$. Require
∣∂κEκ[h]−Aκ′Ch(πˉ)∣<10−12.\left|\partial_\kappa\mathbb E_\kappa[h]-A'_\kappa C_h(\bar\pi)\right|<10^{-12}.
For a quadratic kernel, require the motion divided by $\bar\pi^2$ to remain constant to $10^{-10}$. Predicted magnitude: proportional to $\bar\pi^2$ under the uniform bound.
NOTATION DELTA
None.
NOT CLAIMED
L3 does not claim A($\tau$) holds in the two-round model, does not give an "if and only if," and has no small-$\bar\pi$ application on the implemented grid where $\bar\pi$ is never interior.
L4 — LABEL STANDS
CLAIM
L4 remains PROVED, with legs 1–2 unconditional under their stated fixed-policy hypotheses and leg 3 conditional on A(br).
HYPOTHESES

1. Fixed policies, D1's clock equivalence, no-feedback timing, A1, A4, $b_0<\tau'<\tau$, and positive pooled mass at the tighter threshold.
2. $D=1\Rightarrow a=1$ ensures newly flagged histories remove engagement mass from the pool.
3. For leg 3 only: L3, the magnitude monotonicity of the chord, and A(br)(br-i)–(br-v).

PROOF

1. Lowering $\tau$ weakly advances each Voice crossing and can only enlarge the flagged cell.
2. Every newly removed pooled history is engaging, so removing it weakly lowers the pooled engagement share.
3. Under A(br), both the coefficient magnitude and chord magnitude weakly fall, giving leg 3.
4. UNCHECKED: §7.3 supplies only L4 Step 1, not Steps 2–16.
5. UNCHECKED: the bundle exhibits no two-round threshold pair satisfying all of A(br)(br-i)–(br-v). At the implemented calibration br-i already fails through A($\tau$).

WHERE IT FAILS

1. Re-optimising policies after the threshold change can destroy the pathwise nesting argument.
2. If br-iii fails, the coefficient response can increase enough to reverse leg 3.
3. If br-v fails, the two chord magnitudes are values of different functionals and are not comparable.
4. If the tighter threshold leaves no pooled mass, its pooled share is undefined.

LABEL CLAIMED + why
LABEL STANDS. Legs 1–2 are structurally supported; leg 3 is honestly stated as a conditional implication.
NUMERICAL CHECK REQUEST
For every frozen-policy threshold pair, require zero violations of
CF(τ,T)⊆CF(τ′,T)\mathcal C_F(\tau,T)\subseteq\mathcal C_F(\tau',T)
and require
πˉpr(τ′)−πˉpr(τ)≤10−12.\bar\pi_{\mathrm{pr}}(\tau')-\bar\pi_{\mathrm{pr}}(\tau)\le10^{-12}.
On synthetic A(br)-satisfying pairs, require
SP(τ′,T)−SP(τ,T)≤10−12.\mathcal S_P(\tau',T)-\mathcal S_P(\tau,T)\le10^{-12}.
Predicted signs: non-negative flagged-weight change, non-positive pooled-share and sensitivity changes.
NOTATION DELTA
None.
NOT CLAIMED
L4 does not give an unconditional sensitivity result for the implemented calibration, does not address the window margin, and does not survive policy re-optimisation without additional analysis.
P1 — LABEL STANDS
CLAIM
The repaired P1 implication remains PROVED, but it is not an existence result for the implemented calibration because A3 and A6 fail there.
HYPOTHESES

1. A1, A2′, A3, A4, and A6 provide the ordered compact fixed-point environment.
2. A7-J supplies pointwise flagged-tuple identification, including off-path image tuples.
3. The definitional round-2 action set and continuation-cost equivalence supply sequential optimality at every flagged pair.
4. D1, no feedback, flag termination, $m_0\ge0$, $U_j$, and the primitive table restrictions supply prices, payoffs, and measurability.
5. One full-support plan perturbation family supplies pooled off-path beliefs at every $k\in\Theta$; the boundary $\kappa$ values use the extension route.
6. A8 and the additional ordering hypotheses apply only to the positive-cell-mass addendum.

PROOF

1. The repaired statement now uses the same A7-J form as the proof.
2. The Step 12 reconstruction in the adversarial proof-read establishes flagged-price invariance, the conditional-expectation identity, cancellation of the flagged order, and the role of continuation-cost equivalence.
3. The $\kappa=1$ error is removed by restricting belief requirements to histories with positive probability under some profile.
4. Brouwer produces a fixed point once A6 supplies a single-valued continuous self-map.
5. WRONG: P1 says, "A5 is not assumed: … its continuity content [is derived] from the same scalar reduction." The scalar reduction establishes continuity of the unique inner root in its belief summaries. It does not establish continuity of the composed pooled price family in the cutoff vector. The A6 record and `t2_a6_edge_jump_check` exhibit cutoff-induced price and $\mathcal T$ jumps. What survives is: existence, uniqueness, and continuity of the scalar root in its belief inputs are derived; cutoff continuity is not. P1's label survives because A6 separately assumes the outer-map continuity used by Brouwer.
6. UNCHECKED: the full 20-step proof is not pasted; only its opening is available.
7. UNCHECKED: no complete witness in the bundle satisfies A3, A6, A7-J, continuation-cost equivalence, and the other P1 hypotheses jointly over the claimed $\kappa$ domain. The theorem's logical implication is non-refuted, but its economically relevant domain is not exhibited.

WHERE IT FAILS

1. At $(\kappa=0.5,\tau_{50},T=5)$, A3 fails on an open set and $\mathcal T$ is undefined.
2. At the same calibration, A6 fails at interior cell edges through reproduced jumps in $\mathcal T_2$.
3. At $(\kappa=0.15,0.05,5)$, a crossing is destroyed and a located fixed point lies on an edge.
4. Without A7-J, off-path flagged tuples can have multiple generating pairs.
5. Without continuation-cost equivalence on a multi-Voice shared-path class, a non-selected pair can prefer the lower-cost continuation.

LABEL CLAIMED + why
LABEL STANDS. The repaired conditional theorem has passed the two-pass gate, and the new adverse evidence shows failure of its antecedents rather than a contradiction of the implication.
The theorem is not merely a proof-driven retreat on A7-J, continuation cost, or the $\kappa$ boundary. Those repairs answer real holes. Its remaining inadequacy is model applicability: A3 and A6 assume the structure that the implementation fails to possess.
NUMERICAL CHECK REQUEST
Construct and commit at least one nontrivial menu/calibration satisfying the entire P1 hypothesis set, not only A7-J. Sweep
κ∈{0,0.05,…,1},\kappa\in\{0,0.05,\ldots,1\},
all implemented $\tau$ values, and every $T\in{1,2,5,10}$. At every node require
∥k−T(k;ϑ)∥<10−10\lVert k-\mathcal T(k;\vartheta)\rVert<10^{-10}
and no profitable adjacent-plan deviation above $10^{-9}$. Also require direct global checks of A3 and continuity of $\mathcal T$ on the chosen $\Theta$, not the existing local proxies. Predicted magnitude: cutoff residual below $10^{-10}$ and payoff residual below $10^{-9}$ at every node.
NOTATION DELTA
None.
NOT CLAIMED
P1 does not establish existence at the implemented calibration, non-vacuity of its full assumption set, uniqueness, an A8-satisfying equilibrium, or validity of the current numerical cutoff solver as an equilibrium certificate.
T1 — LABEL STANDS
CLAIM
T1 remains PROVED at fixed policies, with Part B conditional on A($\tau$) and A(br), and Part C an exact product criterion rather than an unconditional window sign.
HYPOTHESES

1. Fixed plan, execution, and cutoff policies; A8; positive pooled sensitivity; L1, L2, and D1.
2. Fixed-policy $\partial_\kappa\Omega=0$ and $\kappa$-differentiability of $M_P$.
3. For Part B: A($\tau$) at both policies, L3, A(br), and L4.
4. For the local form of Part C: a smooth window interpolation.
5. Threshold-side smoothness is carried but not used.

PROOF

1. L1 decomposes the premium into flagged and pooled terms.
2. L2 and fixed-policy $\Omega$ remove the $\kappa$ variation of the flagged term and the cell weight.
3. This yields Part A's exact factorisation.
4. L4 and A(br) yield Part B.
5. The window ratio decomposition yields Part C, and integration along the tightening path explains why its differential form is an average finite-path condition rather than a pointwise equivalence.
6. UNCHECKED: the bundle supplies only T1 Step 1, not Steps 2–17.
7. UNCHECKED: the card itself contains an unresolved O-1 numerical discrepancy: approximately $0.29$ in the §4.4 gloss versus approximately $0.343$ in §9 and the paper. The bundle does not establish whether these are distinct cuts or inconsistent descriptions.

WHERE IT FAILS

1. If $k$ re-solves with $\kappa$ or the policy rule, fixed-policy $\partial_\kappa\Omega=0$ fails.
2. At the implemented calibration, A($\tau$) and hence br-i fail, so Part B is inapplicable.
3. Reading the local window inequality pointwise at every point of a finite tightening path is false.
4. No local window derivative exists without an interpolation because $T$ is integer-valued.

LABEL CLAIMED + why
LABEL STANDS. The paper keeps the fixed-policy scope, the A($\tau$)/A(br) dependence, and the finite-path quantifier. No unconditional window sign is introduced.
NUMERICAL CHECK REQUEST
At fixed policies, evaluate adjacent $\kappa$ values and require
∣S−(1−Ω)SP∣<10−12.\left|\mathcal S-(1-\Omega)\mathcal S_P\right|<10^{-12}.
For synthetic threshold pairs satisfying A(br), require $W_\tau C_\tau\le1+10^{-12}$. For every window pair, verify that attenuation occurs exactly when $W_TC_T\le1$, with ratio-identity residual below $10^{-12}$. Predicted sign for Part B: non-positive change in $\mathcal S$; Part C: no unconditional sign.
NOTATION DELTA
None.
NOT CLAIMED
T1 does not describe general equilibrium, does not establish A($\tau$), does not give an unconditional window sign, and does not make the O-1 regime comparison a window comparison.
C1 — LABEL STANDS
CLAIM
C1 remains PROVED as a dominance-and-contraction implication with the region as a hypothesis, plus separate NUMERICAL point evidence.
HYPOTHESES

1. One induced norm convention and along-path $L_{\mathcal R}<1$.
2. Relative openness in both coordinates, interiority, and one selected equilibrium branch.
3. Twice continuous differentiability of $\Delta^{\mathrm{act}}$ and $\mathcal T$ near the branch.
4. A non-vanishing equilibrium liquidity derivative.
5. Strict dominance $g_r^{PE}>\mathcal B_r^{GE}$.
6. The threshold margin only.

PROOF

1. The displayed Step 1 correctly obtains invertibility of $I-D_k\mathcal T$ by the convergent geometric series under $L_{\mathcal R}<1$.
2. The norm and dual-pairing conventions are sufficient for the bound used later.
3. The statement distinguishes fixed-policy from equilibrium sensitivity and excludes the integer-valued window margin.
4. The numerical remark expressly limits the 18 nodes to two pointwise inequalities and diagnostics.
5. UNCHECKED: C1 Steps 2–9, including the exact derivative decomposition and remainder bound, are not pasted.

WHERE IT FAILS

1. If $L_{\mathcal R}\ge1$, the inverse bound used by the proof is unavailable.
2. At a collapsed or branch-switching equilibrium, the interior single-branch derivative argument fails.
3. If the equilibrium liquidity derivative vanishes, differentiating its absolute value requires a separate treatment.
4. Pointwise numerical inequalities alone do not establish relative openness, smoothness, or a named region.

LABEL CLAIMED + why
LABEL STANDS. The result is explicitly an implication with a region as hypothesis; the paper does not convert the 18 nodes into a region theorem.
NUMERICAL CHECK REQUEST
Around one of the existing pointwise nodes, build a compact neighbourhood and compute genuine bounds, not point samples:
sup⁡RrLR<1,inf⁡Rrηr>0.\sup_{\mathcal R_r}L_{\mathcal R}<1,\qquad \inf_{\mathcal R_r}\eta_r>0.
Require an independently calculated finite-difference estimate of the equilibrium derivative to satisfy
∂rSGE≤−inf⁡Rrηr.\partial_r\mathcal S^{GE}\le-\inf_{\mathcal R_r}\eta_r.
A useful target is a certified lower slack above $0.05$, given the current pointwise minimum $0.0595$. Predicted sign: strictly negative; predicted magnitude: at least the certified slack.
NOTATION DELTA
None.
NOT CLAIMED
C1 does not prove that a nonempty region exists, does not cover the window margin, and does not turn dominance-and-contraction nodes into a fifth label.
A($\tau$) — LABEL STANDS
CLAIM
A($\tau$) remains an assumption, and the NUMERICAL record that it fails at the implemented calibration stands.
HYPOTHESES

1. The pooled posterior law has the three fixed support points.
2. The kernel reaches the information set only through the posterior.
3. $\bar\pi$ and the support are $\kappa$-free.
4. Only the weights move, with the derivative pattern stated in A($\tau$).
5. The chord orientation and magnitude condition hold.

PROOF

1. The executed enumeration measures the pooled posterior law itself rather than imposing the representation.
2. The independent re-enumeration and mean-equals-share gates pass.
3. The support has 23–767 atoms and moves with $\kappa$, so the support condition fails at all 180 non-degenerate nodes.
4. WRONG: the card and paper introduce the record with "it fails on the support, not on the derivative pattern," but later state that the derivative pattern fails independently at 0 of 180 nodes. Both sentences cannot stand together. The surviving wording is: the decisive representation failure is already established by the support; the derivative pattern also fails.
5. UNCHECKED: §6 contains an extract rather than the complete JSON and per-node posterior laws, so I cannot independently reproduce the 180-node count from the bundle alone.

WHERE IT FAILS

1. The implemented support contains many interior atoms rather than three.
2. Interior atoms move with $\kappa$.
3. Entry probability and $h$ vary within a fixed-posterior cluster, violating the kernel-through-posterior clause.
4. The derivative pattern and chord identity also fail on the recorded grid.

LABEL CLAIMED + why
LABEL STANDS. No honesty label attaches to the assumption itself. Its adverse applicability evidence is NUMERICAL and does not demote the conditional results that assume it.
The conditional labels are honest only if the paper continues to say that they are unusable at the implemented calibration.
NUMERICAL CHECK REQUEST
Re-run the exact support enumeration for at least three alternative menus and $H\in{5,10,20}$, with the same gates. For the current calibration, predicted results are:

* 0 of 180 non-degenerate nodes with three-point support;
* support count at least 23;
* positive off-support mass;
* chord residual at least $0.0013$ at every non-degenerate node.

For any proposed satisfying design, require off-support mass below $10^{-12}$ and support Hausdorff motion below $10^{-12}$.
NOTATION DELTA
None.
NOT CLAIMED
The record does not prove that no two-round menu can satisfy A($\tau$), does not invalidate L3's implication, and does not supply a threshold comparative static for the implemented model.
A6 — LABEL STANDS
CLAIM
A6 remains an assumption, with reproduced evidence that its continuity clause fails for the declared construction at the implemented calibration.
HYPOTHESES

1. All best-response cutoffs lie in a common compact ordered polytope.
2. The named tie-break-and-corner choice makes $\mathcal T$ single-valued.
3. One plan perturbation family is fixed across every $k\in\Theta$.
4. $\mathcal T$ is continuous and maps $\Theta$ into itself.

PROOF

1. The opposed briefs agree that pooled prices can jump when a history changes between positive on-path mass and the fixed off-path belief.
2. The deviating plan evaluates those prices under its own noise law, so the effect does not vanish with the plan's equilibrium population mass.
3. The curated checks reproduce the three baseline jumps, the larger $\kappa=0.15$ jump, the destroyed crossing, and the clean Hold-collapse face.
4. WRONG: §7.2 still says $\mathcal T$ is "bit-identical" on the clean collapse face. The executed check says $U_j$ is bit-identical but $\mathcal T_2$ moves by $6.66\times10^{-16}$, or three ulps. The economically relevant invariance survives; the literal claim does not.
5. WRONG: §7.2 says the A6 probes are "analysis-grade and not curated executed checks." The 2026-08-28 card says the decisive probes are now executed `t2_a6_*` checks.
6. MISCITED: the draft headers still identify the 2026-08-27 card stamp, not the controlling 2026-08-28 stamp. Its "about $10^{-8}$" belief-snap sentence also needs the bracket qualifier: that accuracy holds at the $10^{-8}$ crossover bracket; at the probes' $10^{-9}$ bracket two residuals are of order $10^{-7}$.
7. UNCHECKED: the continuum-face lemma is expressly a single-pass panel derivation and has not passed the two-pass gate. It may be cited as an analytic observation, not as a proved extension of P1.

WHERE IT FAILS

1. At the three baseline interior cell edges, $\mathcal T_2$ jumps by approximately $0.00633$, $0.0109$, and $0.0283$.
2. At $(\kappa=0.15,0.05,5)$, the jump is approximately $0.1647$ and destroys a diagonal crossing.
3. On menus with a middle plan owning an exclusive reachable history, the proposed collapse-face mechanism can also operate.
4. The clean Hold-collapse face does not rescue A6 because the live failure occurs at different loci.

LABEL CLAIMED + why
LABEL STANDS. A6 is an antecedent, not a labelled theorem. The checks establish its failure at a calibration; they do not contradict P1's implication under A6.
NUMERICAL CHECK REQUEST
First, update the paper record and rerun the three curated checks. Predicted magnitudes are:

* baseline jumps: $0.00633$, $0.0109$, and $0.0283$ to three significant figures;
* surviving-type controls: below $4\times10^{-9}$;
* $\kappa=0.15$ jump: approximately $0.1647$;
* collapse-face pooled-price spread: at most $4.441\times10^{-16}$;
* collapse-face $\mathcal T_2$ spread: approximately $6.66\times10^{-16}$, not zero.

Second, implement the proposed replacement existence route and require its map or correspondence to have no edge discontinuity above $10^{-10}$ on the full constructed domain.
NOTATION DELTA
None.
NOT CLAIMED
The evidence does not prove nonexistence, does not show every menu violates A6, does not gate-check the continuum-face lemma, and does not make the clean collapse face a global continuity result.
A3 — LABEL STANDS
CLAIM
A3 remains an assumption, with evidence that it fails at two loci in the implemented calibration.
HYPOTHESES

1. Every adjacent-plan payoff difference crosses zero at most once in $s$.
2. The preferred plan is weakly increasing in $s$.
3. These properties hold at every belief and price system relevant to the outer map.

PROOF

1. Three strict sign changes in $U_V-U_H$ contradict Hypothesis 1.
2. The sequence Hold–Voice–Hold–Voice contradicts Hypothesis 2 and leaves no weakly increasing selection.
3. The Voice-to-Hold reversal at the second locus independently contradicts Hypothesis 2.
4. WRONG: §7.2 still says the candidate account is "UNCHECKED beyond the one node probed." The 2026-08-28 `t2_t34_account_sweep` reports that the preregistered account HOLDS at all three remaining nodes. The paper must replace the old status with the three-node diagnostic record, while retaining that existence remains unresolved.
5. UNCHECKED: the first open-set A3 failure is reported through the panel records, but no dedicated curated `t2` A3 check containing the complete payoff curves is inlined. The logical implication from the reported sign changes is valid; the raw measurement is not independently reconstructible from this paste.

WHERE IT FAILS

1. At $(\kappa=0.5,\tau_{50},T=5)$, $U_V-U_H$ has three strict sign changes and the argmax alternates.
2. At $(\kappa=0.15,0.05,5)$, the preferred plan moves from Voice to Hold as $s$ rises.
3. At two additional ticket-34 nodes, a located fixed point is pinned to an $n(s)$ edge where the payoff difference jumps through zero.
4. At the remaining swept node, the worst deviation lies immediately above such an edge even though no pin is found.

LABEL CLAIMED + why
LABEL STANDS. A3 carries no proof label. Its failure is applicability evidence showing that P1 cannot be invoked at those loci.
NUMERICAL CHECK REQUEST
Create a dedicated executed A3 check. At the first locus, evaluate $U_V-U_H$ on a dense $s$ grid for every $k_2$ offset from $10^{-9}$ through $2\times10^{-2}$. Predicted result:

* exactly three strict sign changes near $1.5754434$, $1.5833333$, and $1.5902426$;
* middle excursions between $2.4\times10^{-4}$ and $2.8\times10^{-4}$;
* Hold–Voice–Hold–Voice argmax order.

At the second locus, require a reproduced Voice-to-Hold reversal at both located fixed points. Predicted sign: decreasing plan choice in $s$, contrary to A3.
NOTATION DELTA
None.
NOT CLAIMED
The A3 evidence does not establish equilibrium nonexistence, does not turn an edge-pinned cutoff-map fixed point into an equilibrium, and does not resolve the four ticket-34 existence questions.
Final disposition
Labels: all stand.
P1: valid conditional implication, but not the implemented-model existence theorem.
Conditional labelling: formally honest and economically unusable at the tested calibration unless the caveat remains adjacent.
§7.1 conditionality: no material drop.
Blocking repairs before accepting draft_v3 against stamp `926f58c`:

1. Separate A5 root continuity in belief summaries from cutoff continuity of the composed price family.
2. Replace "fails on the support, not on the derivative pattern" with wording that records both failures.
3. Replace A6's literal "$\mathcal T$ bit-identical" statement.
4. Replace the stale "analysis-grade, not curated" A6 status and add the executed `t2_a6_*` records.
5. Replace A3's "UNCHECKED beyond one node" sentence with the 3/3 swept diagnostic result.
6. Update the draft section provenance from the 2026-08-27 stamp to the 2026-08-28 stamp.
