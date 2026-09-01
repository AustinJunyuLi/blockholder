# 0007: pricing a mixed order

Austin completed Lesson 3 on how a market maker prices pooled order flow when the
bidder's entry depends on the price being computed.

## Demonstrated

- Austin restated the bidder-entry condition in its rearranged form,
  xi > P + K + m_bar - S_bar, and read the entry probability as a normal tail,
  p(P) = 1 - Phi((P + K + m_bar - S_bar) / sigma_xi). Direction: p falls as P rises.
- Austin explained why the price appears inside its own definition: the takeover
  branch pays the prevailing price plus premium, so P shows up on both sides of
  the pricing equation. The pricing problem is a fixed point, not a sum.
- Austin derived the odds formula: collecting the pP term gives
  (1 - p)P = (1 - p)y_bar + p m_bar, and dividing by 1 - p turns the probability
  of entry into the odds of entry. Correctly identified 1 - p as the weight of the
  branch that carries no P.
- Austin rebuilt the fixed-point price 113 from y_bar = 102 and m_bar = 11 at
  p = 0.5 and verified it against the branches (102 without a bidder, 124 with,
  averaging to 113).
- Austin traced the one-half entry chance at P = 113 to the symmetry of
  xi ~ N(0, sigma_xi^2): the threshold xi > 0 splits the distribution in half.
- Austin argued uniqueness correctly after one correction: the map is decreasing
  everywhere (feed 100, get 133.66; feed 120, get 108.27), not "increasing below
  the crossing"; below 113 the map lies above the 45-degree line, above 113 it
  lies below, so the falling curve and rising line meet once.
- Austin gave the three pipes through which a higher engagement posterior moves
  the price: y_bar up via Delta_V, premium up via Delta_m times odds, entry
  probability down via the higher bill. Initial answer attributed pipe 3 to the
  price rising; corrected to the direct channel through m_bar = m0 + pi Delta_m.
- Austin explained the liquidity experiment: doubling kappa from 0.30 to 0.60 cut
  the +1 order's price impact from 0.6932 to 0.1871 because more noise makes the
  order easier to explain without Northstar, so the posterior moves less.
- Austin stated that kappa is not turnover. Both definitions needed a precision
  pass in session: kappa is noise-trading intensity, Pr(z = +-1) = kappa/2,
  Pr(z = 0) = 1 - kappa; turnover is a volume measure, shares traded per period.

## Evidence

Chat retrieval on 2026-09-01. Austin supplied the fixed-point algebra, the odds
derivation, the uniqueness argument, the three-pipe decomposition, and the kappa
comparative static, with two corrections made in session (pipe-3 attribution,
kappa/turnover definitions). No quiz score was used.

## Handoff

Lesson 4 is in progress, taught in chat (teach/lessons/ has no 0004 HTML file;
continue in chat unless one is created). The first topic was delivered on
2026-09-01: the two-round timeline. Austin was given the four nodes (Nature draws
v and s, Northstar commits to one complete contingent plan; round 1 pooled
trading over days 0..H with P_d = E[Y | H_d]; the disclosure node where the flag
reveals (B^F, a=1) and terminates the pooled round; round 2 flagged trading then
the bidder, or bidder on pooled history if no flag), the sequence line, and the
no-feedback assumption as a numbered hypothesis.

Three retrieval questions were posed and are unanswered. Resume lesson 4 by
collecting them: (1) recite the sequence and name the two things the filing
reveals; (2) at which node is the market still inferring engagement and at which
is it settled for good; (3) why does "the flag terminates the pooled round"
matter, i.e. what breaks if pooled trading could continue after the filing.

After those pass, the remaining lesson 4 topic is the clock equivalence
(model note section 3-4): for every Voice plan, the flag lands iff
B_j(s, H - T) >= tau, and a tighter threshold or shorter window moves histories
from the pooled cell to the flagged cell and nowhere else.
