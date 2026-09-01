---
status: accepted
date: 2026-09-01
---
# The paper is the only record, built on a fresh branch from the inherited draft alone

Earlier work on this paper accumulated a frozen theory record, a closed result numbering, a
registered empirical specification, eight decision records, and several hundred files of
provenance. By September 2026 those records did more to constrain the next step than to support
it: the paper's most visible results rested on assumptions that its own calibration violated, and
the rules forbade changing the model that produced them. Austin chose to start branch `v5` with
only the inherited draft (`inherited/draft_v3/`), the model code, the empirics code and data, and
one referee brief, and to delete everything else from the tree. The deleted material stays in the
`v4` history and is never consulted.

Under this doctrine the paper and its appendix are the theory record. Every result that appears
in `paper.tex` passes the two-pass gate on `v5`, inherited or new. The paper states positive
results only. It never refers to earlier versions, attempts, dropped results, or fallbacks.
An exercise or result that fails is absent. This trades provenance for freedom to change the
model, and it makes the paper read as an academic paper rather than a development log.
