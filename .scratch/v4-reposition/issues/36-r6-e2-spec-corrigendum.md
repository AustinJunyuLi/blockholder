# 36 — R6 · E2 SPEC corrigendum (dated addendum)

**Lane:** empirics document, **v4 worktree** — file `research/empirics_v4/SPEC.md` in
`~/Projects/blockholder_v4`, commit on branch **`v4`** (NOT v4-theory). The executing session
works from the theory worktree; this one ticket's edit + commit happen in the other checkout.

**Routing (lane v2, agentic):** Sonnet, effort low — the text is given verbatim below; append
only. Orchestrator commits (on `v4`) and pushes.

**Status:** stale (2026-09-01) — targets `research/empirics_v4/SPEC.md` (the E2 spec) of the August
empirical record, deleted 2026-09-01 (history: 9b98089; record preserved in
draft_v3_onlineappendix.tex §app:honesty); the SPEC file no longer exists on disk. Do not execute.

**Premise:** Audit finding 4. The SPEC's "Note on the O-1 history" (≈ :366-371) repeats the
withdrawn mislabel ("the window-margin attenuation claim is false at baseline in the repo
model"). The SPEC is pre-registered: the original text is **never edited**; corrections are
dated addenda. Austin approved the addendum route (Q6).

**What to build:**

- [ ] Append at the very end of `research/empirics_v4/SPEC.md`, verbatim:

```markdown
## Corrigendum — 2026-08-23 (post-registration; no test changed)

The "Note on the O-1 history" above repeats a mislabel that the theory lane's end-review
audit has withdrawn (`research/model_v4/threads/2026-08-23_gpt_end_review_audit.md`,
finding 4, branch `v4-theory`). O-1 is a **disclosure-regime** experiment — it compares
"market sees the flag" with "market does not" at a **fixed** filing window — so it cannot
show that "the window-margin attenuation claim is false at baseline"; the static model has
no window to vary. That sentence is withdrawn. The genuine window-margin evidence on file
is the two-round model's fixed-policy comparison (`t2_t1_check` block 4;
`HANDOFF_sign.md` §8): attenuation ($W_T C_T < 1$) at every checked node at the implemented
calibration — directional support for Branch A at that calibration. This spec's design is
unchanged: the sign remains the estimand, both branches remain live, and no prediction,
test, sample rule, or variable defined above is modified by this note.
```

- [ ] Nothing else in the file changes — not a character above the appended heading.

**Do NOT:** edit the original "Note on the O-1 history" paragraph; touch any other empirics file;
commit this on v4-theory.

**Stopping condition:** addendum appended byte-for-byte, committed on `v4`, pushed.
