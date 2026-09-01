# Notes

Working preferences for this teaching workspace.

- Unslop rules are active for all course prose: no em dashes, sentence-case
  headings, straight quotes, plain words, no bold-label-colon list tells.
- User's chosen depth (updated 2026-08-30): rigorous end-to-end understanding for
  a presentation. Derive equations line by line, then give the proof route and
  the exact hypothesis boundary. Do not hide difficult steps behind "it follows".
- User's footing: zero, including Kyle-style microstructure basics. Teach the
  inference machinery when the course reaches the pooled cell; do not assume it.
- Quiz answers must be equal in word count so length gives no clue.
- Open each new lesson in the browser when it is created (`open <file>`).
- The course lives in `teach/` to stay out of the manuscript pipeline's way. It is
  tracked in git as of `cfdb88a`, not untracked as this note previously said.
- Use a fast pace. Skip facts already demonstrated, bundle adjacent ideas into
  one whiteboard prompt, and correct minor wording, notation, or arithmetic slips
  inline. Pause only when an error would break later model logic.
- Do not treat a quiz score or one-word confirmation as mastery. Write a learning
  record only after Austin explains the idea in his own words.
- 2026-08-29: `report.html` is the grand tour (background from zero, the idea,
  the math on-ramp). It is an optional reference companion to the lesson sequence,
  not a numbered lesson. Five interactive widgets, all vanilla JS on the shared
  stylesheet. Numbers in it come only from model_v4.md, MODEL_CARD.md via the
  note, CONTEXT.md, the empirics README, legal_regime_portability.md, and the
  draft_v2 abstract and introduction.

## Live session state on 2026-08-31

- Lessons 1 and 2 are complete. Records 0003, 0004 and 0005 cover Lesson 1: the
  free-rider arithmetic, exit and voice with price discipline, and the disclosure
  clock with the takeover-premium caveat. Record 0006 covers Lesson 2: private
  signal inference, trading noise, Bayes' rule in the pooled cell, and what the
  filing does and does not reveal.
- Austin demonstrated the Lesson 2 comparative logic directly. He identified
  that accurate research keeps the estimate near an extreme signal, noisy
  research shrinks it toward the prior mean, and a +1 order can come from noise
  traders rather than Northstar. At kappa = 0.60 he reconstructed the Bayes masses
  0.20 and 0.15 and the posterior 0.5714. He also stated that the filing makes the
  engagement posterior one while other uncertainty remains.

## Live session state on 2026-09-01

- Lesson 3 is written and opened: `lessons/0003-pricing-a-mixed-order.html`, with a
  new `assets/pricing-widget.js`. It covers module 3: competitive pricing as
  P = E[Y | public information], the payoff branches, the bidder-entry rule, the
  scalar price fixed point in its odds form, price impact running through the
  posterior, and why kappa is liquidity rather than depth, volume or turnover.
- Worked calibration, arranged so the numbers close exactly: E[v] = 100,
  Delta_V = 4, m0 = 6, Delta_m = 10, K = 5, S-bar = 129, sigma_xi = 20. At the
  prior pi = 0.5 the fixed point is exactly P = 113 with entry chance exactly 0.5.
  The +1 order gives impact +0.6932 at kappa = 0.30 and +0.1871 at kappa = 0.60.
  These are asserted in the widget's console self-checks.
- Two deliberate scope decisions. The m0 >= 0 uniqueness derivation stays in
  module 5, so Lesson 3 gives only the one-crossing picture and a forward pointer.
  The run-up and jump identity stays in module 6 and is not previewed.
- The sensitivity of price to the posterior is taught as three channels with a
  net computed at this calibration only. It is not a signed general result: the
  entry-deterrence channel is negative and the net sign is not guaranteed.
- Record 0007 covers Lesson 3: written 2026-09-01 after Austin explained the pricing
  logic back, per the rule above.
