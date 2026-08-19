# 08 — T4 · Draft-ready model, theorem and proofs sections

**Lane:** theory (`v4-theory`, other machine)

**Routing:** per ADR-0005 — Opus writer (paper prose, not note prose); Sonnet for LaTeX plumbing and bibliography entries; a separate Opus checker reads the sections against the model note.

**What to build:** The model, the theorem and the proofs written as standalone files under `sections_v3/` for inclusion in draft_v3, plus bibliography entries for every new citation. This is the theory lane's handover to the draft.

**Blocked by:** 06 (T2).

**Status:** ready-for-agent

- [ ] Section files compile on their own with xelatex, no undefined references
- [ ] Every statement matches the model note; every honesty label carries over unchanged
- [ ] Bibliography entries added for each new citation
- [ ] A checker who did not write the sections reads them against the model note and reports every difference
- [ ] Session log entry and commit on `v4-theory`; branch pushed for the convergence owner

## Comments
