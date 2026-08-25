# ADR-0007 corrigendum — for Austin to paste

Target: `docs/adr/0007-one-theorem-two-round-model-two-lanes.md` (v4 worktree).
Where: append at the end of the file as a new section. Nothing above it changes.

---

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
