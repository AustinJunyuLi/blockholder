# 06 — T2 · Two-round core model and the partition theorem

**Lane:** theory (`v4-theory`, other machine)

**Routing:** per ADR-0005 — Opus model writer; an independent Opus re-deriver who never saw the writer's reasoning; Sonnet for formatting and file plumbing. The lane may use GPT Pro as its theorist (chatbot, author-pasted); every claim it returns is re-derived by the Opus checker before it enters a file.

**What to build:** The core model of the paper, rebuilt in two rounds — one pooled trading round, then the flag lands or it does not, then one flagged round plus the bidder's decision — written out under `research/model_v4/` as LaTeX with a markdown mirror. Primitives, timing, the partition, the equilibrium notion, and the theorem with its proof route: the decomposition identity, the flagged cell's liquidity-invariance, threshold-margin attenuation with its second lemma, the window-margin sign with the weight and composition condition, and the general-equilibrium region certificate. Plus a short map of which draft_v2 machinery is reused, which is simplified, and which is dropped.

**Blocked by:** None — this is the lane's long pole and starts immediately. 05 (T1) re-runs against it once it exists.

**Status:** ready-for-agent

- [ ] Model note with primitives, timing, partition, equilibrium notion, the theorem and its proof route
- [ ] Every theory claim carries an honesty label; a region-certified claim names its region in the hypothesis, and no claim is labelled more strongly than its proof supports
- [ ] Independent re-derivation by a checker who did not write the model, reported as WRONG / MISCITED / UNCHECKED; WRONG items fixed and re-checked by a fresh checker, not by the one who found them
- [ ] Every numerical claim produced by a committed check script under `quality_reports/fixes/`, run with the project virtualenv, with its output committed
- [ ] The window-margin sign stated consistently with what 05 found, or the disagreement named
- [ ] Map of draft_v2 machinery reused / simplified / dropped
- [ ] Any new glossary term proposed in the theory lane's session log, never by editing the shared glossary
- [ ] Session log entry and commit on `v4-theory`

## Comments

2026-08-20: decomposed into tickets 21-30 under the agentic lane-v2 protocol (see quality_reports/plans/2026-08-20_theory-lane-agentic.md and ADR-0008). D1/L1/L2 proofs already on file with Opus proof-read PASS (v4-theory d40f113); Thread 1 retired, msg3 never pasted. This ticket stays as the umbrella; done when 21-30 are done.
