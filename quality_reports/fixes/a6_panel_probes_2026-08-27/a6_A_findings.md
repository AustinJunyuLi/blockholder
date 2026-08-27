# ANALYST A — raw findings (scratch)

## Mechanism (analytic)

Only k-dependence in U_j is via the finite pooled price vector {P^P_d(h;k)}.
Flagged layer is k-FREE (A7-J pins the belief to the point mass at iota_F(sigma_F);
proof Step 10, Step 11 display).  So A6's continuity clause reduces to:
k -> (P^P_d(h;k))_h continuous on Theta.

P^P_d(h;k) is the inner root at (vhat(h;k), pi(h;k)).
- Lambda_k(h) > 0 : Bayes under k         (Step 9(b) case 1)
- Lambda_k(h) = 0 < Lambda_u(h) : plan-uniform posterior, k-FREE (Step 9(b) case 2)
- Lambda_u(h) = 0 : reference-belief root, k-free (Step 9(c))

Discontinuity set = U_h boundary{k : Lambda_k(h) > 0}.

CONTINUUM-FACE LEMMA.  On a collapse face {k_i = k_{i+1} = c}, for a history h
exclusive to plan i+1 with L>0 near c:
  interior limit  vhat -> mu_v + beta(c - mu_v)      (posterior concentrates at c)
  value AT face   vhat  = k-free family value
A k-INDEPENDENT family gives ONE number; the interior limit varies affinely in c
with slope beta > 0.  They agree for at most ONE c on the face.
=> the price system is discontinuous at every face point but at most one.
Requires J >= 3 (plan 1 and plan J always keep positive mass under a Gaussian s).

TOY: J=3, H=1, Gamma image {-1,0,+4}, z_bar=1, plan2 = Hold (q=0), plan1 Exit
(q=-1), plan3 Voice (q=+4).  h* = (X_0,X_1)=(1,1), flag 0, is plan-2-exclusive
(needs z=+1 twice), Pr = (kappa/2)^2 > 0.  L_2(h*|s) const in s
=> face belief = PRIOR, vhat = mu_v ; interior limit = mu_v + beta(c-mu_v).
JUMP = beta(c - mu_v), exact, nonzero for c != mu_v.  pi = 0 on both sides.
Into U_2 with weight b_0 (kappa/2)^2 [p'(P)(P+m_0-E[v|s]) + p(P)] via the
terminal-value channel (Hold trades nothing, so the execution channel is 0).

## Implemented menu (numerical_v4, J=3 Exit/Hold/Voice, H=10, M=2)

t2_p1_check.json p1_multistart_existence_sweep, 27 nodes:
  COLLAPSE IS LIVE: node (kappa,tau,T) = (0.5, 0.05, 1) solved to
  k = (1.35358624390523, 1.35358624390523), k2-k1 = 0.000e+00 EXACT, Hold mass 0.
  near-collapse (0.5,0.075,1): k2-k1 = 5.274e-02.
  All other 25 nodes: k2-k1 in [1.06e-1, 7.06e-1].
  params.py C0=0.014 comment: "smallest value at which the Hold region stays
  interior at the frozen tau; below it Voice and Exit meet and Hold collapses."

PROBE 5(a): the collapse face is BELIEF-INERT on this menu.
  k1 = k2 vs k1 = k2 - {1e-9, 1e-4, 1e-2}: E[P_0|theta=0] = 1.1383084485 to 10 dp
  on all four; impl T and card T2 identical.  Exit and Hold share theta = 0
  (menu.py: "Exit's day-0 increment is negative and marks 0, so Exit and Hold
  pool perfectly in order flow").  N11's LITERAL mechanism does not fire here.

PROBE 4: the SAME mechanism fires through the mark-type channel, on INTERIOR
hypersurfaces of Theta (k2 = an n(s) cell edge, where a Voice mark-type's mass
crosses zero).  k2 = edge -/+ 1e-9, node (0.5, tau_50, 5):

 dying t | vhat below | vhat above | JUMP     | pred (ref - conc) | card |T2 jump|
   11    | 1.23008952 | 0.84627187 | -3.84e-1 | -3.8382e-01       | 6.9e-10
   10    | 1.25896614 | 1.24439195 | -1.46e-2 | -1.4574e-02       | 6.8e-10
    9    | 1.29166663 | 1.27512024 | -1.65e-2 | -1.6546e-02       | 6.33e-03
    8    | 1.32953120 | 1.31030216 | -1.92e-2 | -1.9229e-02       | 1.09e-02
    7    | 1.37463449 | 1.35160560 | -2.30e-2 | -2.3029e-02       | 2.83e-02
    6    | 1.43041441 | 1.40169048 | -2.87e-2 | -2.8724e-02       | 1.91e-02
 "below" reproduces mu_v + beta(edge - mu_v) to 7-8 dp; "above" reproduces the
 k-free type_reference to full precision.  Predicted = measured to ~1e-8.
 At t=7 the number of sign changes of U_V - U_H goes 1 -> 3.
 Implementation's outer_map shows the same jumps (nearest-bracket does not save it).

PROBE 6: the channel.  Dying type t's own aggregates jump; the surviving
neighbour's move by ~3e-9 (control).
   t=10: sum_d |E[P_d|theta] jump| = 7.37e-2 ; E[p_bid|theta] +1.63e-2 ; E[p P] +1.91e-2
   t= 9: 8.02e-2 ; +8.99e-3 ; +1.11e-2
   t= 8: 9.45e-2 ; +6.49e-3 ; +8.37e-3
   t= 7: 1.19e-1 ; +5.55e-3 ; +7.47e-3
 U_VOICE(s) on the dying cell jumps +2.24e-4 .. +4.39e-4 (Voice looks BETTER once
 its own type is off path -- self-undermining direction).

PROBE 5(b): distance from each solved k2* to the nearest death surface:
 3e-3 .. 5.5e-2 in s (0.004 .. 0.054 sigma_s).  Edge spacing in the equilibrium
 region is 0.052-0.112, so half-spacing is 0.026-0.056: the equilibria are NOT
 systematically close -- the surfaces are simply dense there.  The four
 payoff-unresolved nodes sit at 0.031/0.026/0.044/0.030 sigma_s, no closer than
 the converged ones.  NO CORRELATION -- do not claim one.

type_reference IS the card's Step 9(b) plan-uniform limit for this menu:
for a t-exclusive h, L is constant on {n(s)=t}, so the limit posterior is the
prior truncated to that cell, i.e. E[v | n(s)=t] = ref.Ev[t].  Verified to 1e-8.
So the measured discontinuity is the CARD's construction, not an implementation
artifact.  OFF_PATH_EPS cancels in the ratio at an exclusive history.

Type-exclusive histories exist by construction: Gamma binary, X in {-1,0,1,2};
X_d = 2 forces q_d = 1 and X_d = -1 forces q_d = 0 (pooled.mark_stats `ok`),
so (2,...,2,-1,...,-1) with t twos identifies type t.  Pr = (kappa/2)^{H+1}.

## Other structural finds
- solver.py N_GRID=241 comment: "U_Voice(s) steps down at every n(s) decrement
  ... a bracket wider than an n-plateau lets brentq converge on the jump instead
  of the root."  => Step 15(i) continuity of s -> U_j FAILS on this menu too,
  independently.  WHERE IT FAILS 4's card-legal counterexample is instantiated.
- menu.py:304-316 docstring: "Without this the pricing map has holes, and the
  outer map T(k) jumps by ~0.1 in the cutoff whenever a type's mass crosses zero
  -- which is exactly where the equilibrium sits."
- solver.outer_map fallback `k2 = k1 if gap_HV(...) <= 0` returns a collapsed
  vector; and its `target=` nearest-bracket rule is a DIFFERENT tie-break from
  the proof's inf-selection (Step 13).

## PROBE 7-8 (verifications)

(A) A3 FAILS at the implemented calibration, on an OPEN set of k.
 k2 = edge(6)+1e-9: U_V - U_H has 3 strict sign changes at
 s = 1.5754434, 1.5833333, 1.5902426.  Middle excursions max|gap| = 2.80e-4 and
 2.40e-4, vs TOL_PAYOFF = 1e-9 -- five orders above solver noise, and equal to
 the measured U_VOICE off-path bump.  argmax = H,V,H,V: not weakly increasing,
 and the argmax is single-valued on each interval, so NO weakly increasing
 selection exists: Step 13's S(k) = EMPTY and the card's T is UNDEFINED there.
 Below the edge: 1 sign change (fine).
 OPEN SET: 3 sign changes at k2 = edge(6) + {1e-9, 1e-4, 1e-3, 5e-3, 2e-2};
 back to 1 at +5e-2 and +1e-1.  Width >= 2e-2 in s (>= 0.028 sigma_s).
 The middle excursion sits at s = 1.5833333 = edge(8), an n(s) step -- the
 interaction of the off-path bump with the s-discontinuity of U_VOICE.

(B) EPS robustness: same surface at +/-1e-6 (1000x the breakpoints merge
 tolerance 1e-9) reproduces every number:
   t=9 : vhat jump -1.6546e-02, card |T2 jump| 6.3331e-03  (vs 6.3333e-03 at 1e-9)
   t=8 : vhat jump -1.9229e-02, card |T2 jump| 1.0860e-02  (vs 1.0859e-02)
   t=7 : vhat jump -2.3028e-02, card |T2 jump| 2.8281e-02  (vs 2.8279e-02)
 Not a merged-sliver artifact.

## Reconciliation note (why measured jumps are percent-scale)
Globally-exclusive histories have mass (kappa/2)^(H+1) = 2.4e-7 at kappa=0.5.
The relevant notion is exclusive among ALIVE types: a history carrying X_d = 2
at a date only the dying type marks is alive-exclusive, and those carry mass
~kappa/2 per relevant date.  That is why E[P_d | theta] moves by 4e-2, not 1e-7.
