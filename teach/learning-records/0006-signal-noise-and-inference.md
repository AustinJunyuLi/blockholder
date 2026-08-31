# 0006: signal, noise, and inference

Austin completed Lesson 2 on the blockholder's private signal and the market's
inference from pooled order flow.

## Demonstrated

- When Northstar's research is accurate, its posterior estimate of firm value
  should stay close to an extreme private signal. When the research is very
  noisy, the estimate should shrink back toward the prior mean.
- Austin correctly identified that an observed buy order need not come from
  Northstar because noise traders can generate the same order flow.
- With prior engagement probability 0.5 and kappa = 0.30, Austin understood why
  the +1 order raises the engagement posterior above 0.5: the engagement
  explanation has more prior-weighted probability mass than the noise-only
  explanation.
- When kappa rises to 0.60, Austin reconstructed the two masses directly:
  0.5 x 0.4 = 0.20 for engagement plus zero noise, and 0.5 x 0.3 = 0.15 for no
  engagement plus a noise buy. This gives Pr(E | X = +1) = 0.20 / 0.35 = 0.5714.
- Austin therefore has the key comparative-static intuition for this teaching
  case: more noise trading makes the same observed buy order less informative
  about engagement.
- Austin correctly stated that once the purpose-revealing filing lands,
  Pr(E | public information) = 1. The filing settles engagement status, while
  uncertainty about firm value and bidder synergy remains.
- Austin can distinguish the two inference layers: signal error epsilon makes
  Northstar uncertain about v in s = v + epsilon, while trading noise z makes the
  market uncertain about Northstar in X = q + z.

## Evidence

Chat retrieval on 2026-08-31. Austin supplied the key comparative answers and
reconstructed the kappa = 0.60 Bayes calculation without prompting for the
arithmetic. No quiz score was used.

## Handoff

Lesson 3 should start with competitive pricing from public information. The next
object is P = E[Y | public information]: how the market maker converts pooled
beliefs into price, how price impact arises from mixed order flow, and how bidder
entry enters the payoff being priced.
