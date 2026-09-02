# Attack on the hunt 2 memo, one cut identity for both dials

I did not write the memo. I read `CLAUDE.md`, `CONTEXT.md`, section 3 of the session spec,
ADR 0003, the standing conditions (S1) to (S11) at lines 257 to 297 of `proofs/04_inherited.tex`,
`proofs/02_garbling.tex` (Lemmas g1 to g3, Condition D, Theorem `thm:g-threshold` and the two
remarks), the whole of `proofs/03_caught.tex`, then the brief and the memo. I then recomputed
every number the memo reports from the committed record
`numerical_v4/checks/t2_threshold_revelation_check.json`, and I tested the algebra the memo
transcribes. I ran no pooled pass, no policy solve, no script under `numerical_v4/checks/`, and
no git command. I did not overwrite `single_crossing_certificate.json`: I imported the memo's
script and pointed its output at a temporary file.

## What I tried to break

Six lines of attack: a missing hypothesis in the threshold transfer, a step in part 2 that does
not follow, a hidden use of a dropped assumption (the order size one pooled law, or a support
assumption on the pooled posterior), a claim about the record that the record does not carry,
the Descartes step and the orientation of the reversed polynomial, and the treatment of the
T = 10 pairs.

## Part 1, the cut identity at the threshold margin

The transfer is real and the proof is complete. The clock proof of `cor:caught` uses the clock
only in part (i), through `c(tau) + T' <= c(tau) + T <= H`. The threshold proof replaces that
step by first passage at a lower threshold. The memo's route is
`D(tau,T) = 1{a=1} 1{B(s,H-T) >= tau}`, which is legitimate under (S4) monotone Voice paths in
the date and (S5) legal clock discipline, and `tau' < tau` then gives the inclusion. The direct
route `c(tau') <= c(tau)` needs even less. Parts (ii) to (vi) never look at the dial: they use
only that the two cells are type events, that the masses are kappa free, and the definition of
the caught leg. So they transfer with the same words, as the memo says.

The added hypothesis the memo names, `b_0 < tau'`, is the right one and it is already the
hypothesis of Theorem `thm:g-threshold`. The claim that order size two is not needed for parts
(i) to (vi) is correct: differentiability is assumed in (C-tau-2), not derived, so Lemma g3 is
needed only to name the band Condition D. No support assumption on the pooled posterior appears
anywhere in part 1, and the order size one ternary law is not used.

I checked the algebra of (6), (8) and the five readings by brute force over 400000 random draws
of `(s_A, s_B, phi)` with `s_{A\B}` set by the identity. Zero counterexamples for the
equivalence in (6), the equivalence in (8), reading (a) with its strict conclusion, reading (b),
reading (c) with its proviso, and reading (d). The identity `W_tau = 1 - phi` reproduces the
record's `W_tau` at all four non-null pairs to the last bit.

One hypothesis deserves a sentence the memo does not give it. (S5) says only Voice plans cross
the threshold. The threshold comparison needs that reading at `tau'` as well as at `tau`, since
otherwise a plan with `a = 0` could reach `tau'` and the flagged set at the tighter rule would
not be `{a = 1, c(tau') + T <= H}`. The memo does invoke (S5) inside (C-tau-1) for both rules,
so this is a wording point, and the same reading is already implicit in Theorem
`thm:g-threshold` part (B). It is not a hole.

## Part 2, the single crossing certificate

The implication holds. I checked each step.

The representation (13) is exact: `(1-eps)^H P_v(x)` with `x = eps/(1-eps)` equals
`sum_k (1-eps)^k eps^(H-k) v_k`, and the memo's `P_v(x) = sum_k v_k x^(H-k)` puts `c_0` on the
leading power and `c_H` on the constant. The orientation in (R1) therefore gives `P(0) > 0` and
a negative leading coefficient, so `P` runs to minus infinity. With exactly one sign change,
Descartes' rule gives exactly one positive root counted with multiplicity, so the root is simple
and `P > 0` below it and `P < 0` above it. (R2) is the mirror image for the difference. Adding
`x(kappa) >= r_*` gives `W_A <= W_R <= 0`, hence `0 <= s_{A\B} <= s_A` after the factor
`-1/2`. The band then follows from the part 1 identity by two lines that I verified:
`s_B - s_A = ((1-phi)/phi)(s_A - s_{A\B})` and `s_A/phi - s_B = ((1-phi)/phi) s_{A\B}`. The
strict step `s_A/phi < ((2-phi)/phi) s_A` uses `s_A > 0` and `phi < 1`, both available.

The hypotheses are not vacuous and the implication is not accidental. I generated 7585 random
coefficient triples that satisfy (R1) and (R2) and evaluated them at random points above the
largest root. Every one gave `0 <= s_R <= s_A`, the two sided band, and `C_tau <= 1`.

The certificate uses Lemma g3(a) and g3(b) only. It does not use g3(c), whose curvature
hypothesis fails at every node, and it does not use the mean preserving contraction of Lemma g2.
That is the right choice, and it also means the certificate is unharmed by the fact that the code
prices cells with market weights and integrates them with measure weights (see the nits).

## The numbers, recomputed

I rebuilt the revelation values from the record's `c_k` alone, with my own code, and compared
against the record.

- `W_rev` at all 8 pairs and 71 kappa nodes: largest absolute difference 1.04e-17. `S_P` is
  `|W|/10` in the record: largest difference 1.30e-18. `C_tau`: 3.89e-15. `W_tau C_tau`:
  3.77e-15. The condition D flag agrees at every node. The memo's reported wiring residual of
  3.89e-15 is exactly the `C_tau` column, so its claim is right.
- Sign lists. Every T = 5 node has one crossing, first coefficient negative, last positive. Every
  non-null difference has one crossing, first positive, last negative. This survives raising the
  zero tolerance from 1e-12 to 1e-6 times the largest coefficient of the vector.
- Roots. My `numpy.roots` values agree with the memo's table at every digit it prints. The
  cutoffs in kappa are 0.108569232, 0.145962695, 0.149012173, 0.133523094 for the four T = 5
  pairs, and each pair's `r_A` equals the previous pair's `r_R`, as the ladder requires. The
  smallest gap to the grid is 0.15 - 0.149012173 = 0.000987827, as the memo states.
- Robustness of that gap. Writing the root's first order sensitivity to a relative perturbation
  of the coefficients, the worst pair tolerates a relative error of about 1.03e-2 in the `c_k`
  before its cutoff reaches 0.15. Float level error in the record cannot move the conclusion.
- The band at the grid. Over all four non-null pairs and all 71 nodes, the smallest lower margin
  `s_B - s_A` is 7.67e-6 and the smallest upper margin `((2-phi)/phi)s_A - s_B` is 4.12e-5. The
  smallest `s_A - s_{A\B}` is 1.93e-7 and both slopes stay positive.
- The reported minima the memo quotes are right: the smallest absolute `c_k` used in a sign
  decision is 1.070662e-07 and the smallest absolute difference coefficient is 1.341782e-06.

## The T = 10 pairs

The memo's treatment is correct and it is the honest one. In the record all four T = 10 pairs
carry `reclassified_mass` exactly 0.0, the five T = 10 coefficient vectors are bitwise identical,
and `C_tau_min = C_tau_max = 1.0`. So (C-tau-3) fails at those pairs, `phi` is zero, and the
caught leg is not defined. I also checked the point the memo leaves implicit: the common T = 10
polynomial has its only positive root at kappa = 0.019047, far below the grid, and the smallest
`|W|` on the grid is 1.34e-3, so the common sensitivity never vanishes on `[0.15, 0.85]` and the
ratio really is 1 there rather than 0 divided by 0. The memo's sentence that no prose should read
the T = 10 rows as evidence about who is caught is the correct reading, and it agrees with
checkpoint 0, which already said the threshold content rests on the four T = 5 pairs.

## The failure region below the grid

The memo says the reported failure endpoint 0.1485 is below the certificate cutoff 0.149012173.
That is true, but the record deserves a sharper statement, which I checked on a 1e-6 mesh from
the record's own coefficients for the pair q0.5 to q0.3:

- `C_tau > 1` on about [0.143673, 0.149012], so the certificate cutoff is, to six decimals, the
  exact upper endpoint of the region where Condition D fails.
- `W_tau C_tau > 1` on about [0.143723, 0.148924], which is what checkpoint 0's bracket
  [0.1440, 0.1485] is: the dial failure on a coarse mesh, not the Condition D failure.

Every sub-interval claim the memo makes about that pair checks out. Below 0.145962695 the two
pooled slopes have opposite signs. At 0.145962695 the pool's own slope is zero. Between
0.145962695 and 0.149012173 both slopes are positive and the survivor is the more sensitive of
the two.

## Nits

Nits: (1) The memo says the source record "matches the pooled pass within 4.99e-18". The record's
wiring check runs at one node, T = 5 and quantile 0.9, at three kappa values. The other nine
nodes inherit the same code path but are not checked against `pooled_premium`; the sentence
should say so. (2) Step 2 of the calibration section says the cell posteriors are computed "as in
Lemma g1". In the code the cell mass uses the measure weights and the cell belief uses the market
weights, which carry the off path floor `OFF_PATH_EPS = 1e-14` in `_alive_weights`. So the
record's `G(S)` is not literally `E_rho[h(rho(. | marks))]` of Lemma g3. Nothing in part 2 breaks,
because only g3(a) and g3(b) are used and they need only that `G` is kappa free, but the two
weight systems should be named where the identification is made, as step 1 does and step 2 does
not. (3) The script's check name `failure_region_is_below_certificate_cutoff` and the memo's
phrase "the reported failure endpoint" attach to the dial's coarse bracket, not to the Condition
D failure; the sharper statement above is available from the same coefficients. (4) (R1) says the
first and last coefficients are strictly signed after zeros are deleted. If a trailing
coefficient were classified as zero, `P(0) = 0` and the argument needs the factor `x^j` peeled
off before Descartes is applied. The conclusion survives either reading, but the clause should
pick one. (5) (R3) is stated with a weak inequality. At `x(kappa) = r_A` exactly, `s_A = 0` and
(C-tau-3) fails, so the conclusion is not available at that single point; the check should be
strict, which the script's 1e-8 gap already is. (6) The step from a cutoff in `x` to an interval
in kappa uses that `kappa/(2-kappa)` rises in kappa. True and trivial, but neither the memo nor
the script says it. (7) (C-tau-1) leans on (S5) at the tighter threshold as well as at the
looser one; say it, as the memo says the clean start clause. (8) The certificate's stronger upper
bound `s_B <= s_A/phi` is close to binding on the grid: the ratio `s_B/s_A` runs from 9.3 to 40.5
while `1/phi` is about 40 to 43. The memo could say that, and could also say that with
`(1-phi)/phi` near 40 the caught leg is dominated by the survivor re-pricing remainder, so the
"who gets caught" reading of the threshold dial is a statement about the sum and not about the
newly caught histories alone. The memo does flag that the caught leg carries re-pricing, and
reports no split, so this is a reading nit and not a claim I can falsify.

## Files I wrote

- `.scratch/v5-paper/hunt/2-one-cut-identity/attack.md`, this file.
- `.scratch/v5-paper/hunt/2-one-cut-identity/attack_recheck.py` and its record
  `attack_recheck.json`: the independent rebuild of the record's revelation values, the sign
  lists, the roots, the root sensitivity, the T = 10 check, the below grid scan, the brute force
  test of the part 1 algebra, and the band margins at every grid node.
- `.scratch/v5-paper/hunt/2-one-cut-identity/attack_implication_test.py`: the randomised test of
  the part 2 implication on synthetic coefficient vectors. It prints its result and writes
  nothing.

I changed no other file. I ran the memo's `single_crossing_certificate.py` through a temporary
output path; it returns PASS and its output is byte identical to the committed record.

```json
{"verdict": "PASS", "reasons": "Part 1 is a sound transfer: the clock is used only in the nesting step of cor:caught, first passage at a lower threshold replaces it under (S4) and (S5), the added clean start b_0 < tau' is named, and parts (ii) to (vi) never touch the dial. I found no missing hypothesis, no use of the order size one pooled law and no support assumption on the pooled posterior; 400000 random draws produced no counterexample to (6), (8) or the five readings. Part 2's implication is correct: the reversed polynomial is oriented as the memo says, one sign change gives exactly one positive root with the right sign either side, the three root cutoff gives W_A <= W_R <= 0 and so 0 <= s_{A-B} <= s_A, and the two band margins follow from the part 1 identity; 7585 random coefficient triples satisfying (R1) to (R3) gave no violation. Every reported number reproduces from the record's c_k with my own code: W_rev to 1.04e-17, C_tau to 3.89e-15, the four cutoffs to every printed digit, the 0.000987827 gap, and the quoted coefficient minima. The cutoff for the q0.5 to q0.3 pair is in fact the exact upper endpoint of the Condition D failure region, and the quoted 0.1485 is the coarse mesh endpoint of the dial failure. The T = 10 pairs are genuinely null: mass exactly zero, bitwise identical coefficient vectors, and a common sensitivity whose only positive root sits at kappa 0.019, so C_tau = 1 on the whole grid and the memo's refusal to read them as evidence is right. Eight nits, none of them a hole."}
```
