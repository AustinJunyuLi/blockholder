# One-pager for Austin — 2026-08-30, draft_v3 prose rewrite

## Proved

The main text is now a prose economics paper with two formal statements, and nothing was lost
getting there.

- **Theorem 1** (disclosure attenuation at fixed policies) and **Proposition 2** (the
  general-equilibrium implication) are the only formal environments that print. Existence, the
  disclosure partition, the two-cell decomposition, the flagged-cell invariance, the pooled
  interior-motion result and the three-leg threshold result are prose.
- **Both documents build clean.** Main text: four passes, 0 errors, 0 undefined references, 0
  multiply-defined labels, 27 pages (31 before). Online appendix: three passes, 0 errors, 0
  undefined references, 56 pages, zero `??` in the extracted text. Abstract 146 words.
- **The appendix still reads correctly.** I rebuilt the previous commit's main text and compared
  the printed value of all 51 labels the appendix resolves into it. 50 of 51 identical. Every
  assumption clause number, definition, lemma anchor, Theorem 1 and Proposition 2 print as before.
  `draft_v3_onlineappendix.tex` was not edited.
- **Dropped clause tags recovered.** The earlier prose pass had removed (TR-i)--(TR-iv),
  ($\tau$-i)/($\tau$-ii), (br-i)--(br-v) and the (i)--(vi) equilibrium requirements from Section 3
  while the appendix kept citing them, about 130 sites. All reinstated inline from the pre-pass
  text. This was a live defect, not a cosmetic one.
- `deliverable/` PDFs refreshed; `draft_v3_trace.md` and the team-review brief carry dated fourth
  amendments.

## At risk

- **Section 4 still prints the thirteen existence hypotheses as a tagged list.** Not a theorem
  environment, but a list, and you asked for concise prose. The appendix cites (P-1)--(P-13) 67
  times as plain text and was out of scope, so the tags had to stay somewhere. Commentary
  compressed hard; conditions untouched.
- **There is a Proposition 2 and no visible Proposition 1.** Existence holds anchor 1 because the
  appendix titles its own section "Proof of Proposition 1 (existence)". Renumbering would give two
  objects the same name.
- **One printed pointer moved:** `sec:hypotheses` resolves to "Section 3" instead of "Section 3.5",
  since the subsection that held the label is gone. Three sentences read differently. Nothing else
  in the cross-reference surface changed.

## Needs me

- Whether to move the (P-1)--(P-13) list into the online appendix. That needs both files edited,
  which this session's scope forbade. One session's work on your word.
- Whether the Proposition 1 / Proposition 2 gap is acceptable, or whether the appendix should be
  reworded so the general-equilibrium result can be Proposition 1.

Nothing theorem-level surfaced. The frozen record and `sections_v3/` were not opened for writing,
no empirics work was done here, and your uncommitted changes are untouched. One environment note:
`biber` fails silently on this machine (exit 25, empty `.bbl`) until its stale PAR cache under
`$TMPDIR/par-*` is deleted.
