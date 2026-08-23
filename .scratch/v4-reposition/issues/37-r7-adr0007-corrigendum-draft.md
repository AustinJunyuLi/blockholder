# 37 — R7 · ADR-0007 corrigendum: draft for Austin to paste

**Lane:** theory (`v4-theory` worktree at `~/Projects/blockholder_v4_theory`) — the DRAFT file
lands there; **no agent touches `docs/adr/`** (standing rule). Austin pastes it himself (Q7).

**Routing (lane v2, agentic):** Sonnet, effort low — text given verbatim; file creation only.
Orchestrator commits.

**What to build:**

- [ ] Create `quality_reports/handoffs/2026-08-23_adr0007_corrigendum.md` (theory worktree)
      containing instructions + the paste text:

```markdown
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
```

**Do NOT:** edit `docs/adr/` in either worktree; rephrase the paste text (it was approved in
this form).

**Stopping condition:** the draft file exists, committed on v4-theory, pushed; the final report
to Austin names it as his paste item.
