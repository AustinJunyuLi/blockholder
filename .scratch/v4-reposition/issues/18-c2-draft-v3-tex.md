# 18 — C2 · draft_v3.tex

**Lane:** convergence (`v4`, this machine)

**Routing:** per ADR-0005 — Opus writer for the introduction and the literature paragraph; Sonnet for LaTeX assembly and bibliography; a separate Opus checker reads section by section against the memo and the cards.

**What to build:** A compiling draft_v3 started as a copy of draft_v2: repositioned introduction and literature paragraph, the theory lane's model, theorem and proofs sections pulled in, the empirics lane's section pulled in, appendices trimmed to what the position needs. **Merge `v4-theory` into `v4` at the start of this ticket** — this is the point where the two lanes become one draft.

**Blocked by:** 17 (C1); section files from 08 (T4) and 16 (E8).

**Status:** ready-for-agent

- [ ] `v4-theory` merged into `v4` before any writing, with neither lane's work dropped in the merge
- [ ] Compiles with xelatex and biber, no undefined references
- [ ] Section-by-section check against the memo and the cards by an agent who did not write the draft
- [ ] draft_v2 untouched, and nothing on the `proposal` branch touched
- [ ] Session log entry and commit on `v4`

## Comments
