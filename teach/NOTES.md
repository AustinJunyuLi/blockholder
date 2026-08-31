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
- The course lives in `teach/` to stay out of the manuscript pipeline's way.
  Untracked in git until the user decides otherwise.
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
- The next live move is Lesson 3, module 3 of the course plan: competitive pricing
  from public information, P = E[Y | public information], order-flow price impact,
  bidder entry, and why the paper calls kappa liquidity. Start Lesson 3 from the
  beginning in a fresh chat. Do not reteach Lesson 2 unless Austin asks for a
  review or a later retrieval check exposes a gap.
