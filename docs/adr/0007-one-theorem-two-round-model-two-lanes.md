---
status: accepted
date: 2026-08-19
---
# One new theorem, proved on a two-round model, built by a theory lane and an empirics lane running in parallel on two machines

Sharpening the existing model was rejected because the referee's O-1 check (executed, `research/review_v3/verify_theory.md`) shows the window-margin attenuation claim is *false* at baseline in the repo model — the κ-sensitivity ratios run 1.06/1.18/1.14 for flagged mass below ≈0.29 — so there is nothing sound to sharpen on that margin; continuous time before December was rejected on tractability and because it would put the paper head-on against Back et al., Cetemen–Cisternas–Kolb–Viswanathan and Collin-Dufresne–Fos rather than beside them (ADR-0003). The model is therefore rebuilt as **two rounds** — one pooled trading round, the flag lands or not, one flagged round plus the bidder's decision — which makes the window margin a genuine primitive instead of a reduced-form parameter and gives stake-at-filing as an object the empirics can measure. The first milestone of the theory lane is re-running O-1 in the rebuilt model and publishing the sign, magnitude and condition to `research/model_v4/HANDOFF_sign.md`; that file is the empirics lane's only dependency (the slope sign for the post-2024 prediction), and the empirics lane proceeds with a placeholder until it lands. Calibration is re-anchored so the flagged share is an empirically meaningful number — the share of engagements that get disclosed — and magnitudes are reported, not just signs; a separate research-only scoping note covers the endogenous-filing-date game and continuous-time tractability so those stay named extensions rather than December work.

Execution runs as **two lanes on two machines**: the theory lane on the author's other laptop in a worktree on branch `v4-theory` (pushed to GitHub), the empirics lane in this session on branch `v4`, with `v4-theory` merged into `v4` at the draft_v3 ticket. Convergence tickets and the shared files (`CONTEXT.md`, `docs/adr/`, `.scratch/`, `bibliography.bib`) are owned by the empirics-lane session; the theory lane proposes glossary terms through its session log instead of editing them. Routing follows ADR-0005 — Opus for the model writer, the independent re-deriver, judges and the final referee; Sonnet for mechanical stages — with one addition: the theory lane may use GPT Pro as its theorist, as a chatbot the author pastes into, with Claude Code agents as hands and every returned claim re-derived by an Opus checker before it enters a file.

**Corrigendum (2026-08-23).** The motivation above describes the referee's O-1 check as
showing "the window-margin attenuation claim is *false* at baseline in the repo model."
That reading was wrong and is withdrawn (theory-lane audit:
`research/model_v4/threads/2026-08-23_gpt_end_review_audit.md`, finding 4, branch
`v4-theory`). O-1 toggles the disclosure **regime** — flag observed vs hidden — at a fixed
window; the static model has no window primitive to vary, which is exactly why this ADR
rebuilds the model. O-1's ratios show that a regime-comparison composition factor can
exceed one; they measure nothing about $T$. The decision this ADR records is unaffected —
if anything reinforced: the rebuilt two-round model's own fixed-policy window comparison
(`t2_t1_check` block 4; `research/model_v4/HANDOFF_sign.md` §8) shows attenuation
($W_T C_T < 1$) at every checked node at the implemented calibration.
