# 11 · Write the paper

**Lane:** paper. **Routing:** Grok writer in batch 2 (effort xhigh); Opus checker for the number
guard and compile at checkpoint 2. **Blocked by:** 02, 03, 04, 05, 06, 07, 08, 09, 10. **Blocks:** 12.

**What to write.** `paper.tex`, `appendix.tex`, `paper.bib` (copy the inherited bib and prune
to what is cited). `appendix.tex` assembles the `proofs/` files by `\input` and adds the
hypothesis lists. The headline wording in the abstract and introduction follows ticket 02's
outcome: if the threshold theorem carries a named condition, the wording names it. Structure: abstract; introduction leading with the partition and the two dials;
the institutional setting in one section; the model; the results (factorisation, garbling lemma,
threshold dial, clock dial, who gets caught, existence if present), each with its label and a
route map of at most six lines; the calibration and figures; the empirics (E1, E2, the clock
paragraph) with the registered design stated and the descriptive register stated; conclusion
without a list of non-claims. Hypothesis lists go to the appendix. The inherited draft's prose may
be reused sentence by sentence where it still holds, never cited. The order-size choice gets one
defending paragraph in the model section. Title from CLAUDE.md. Every number from a result file.
Unslop rules apply to the paper's prose.

**Acceptance.**
- [ ] Number guard green against `paper.tex`.
- [ ] Both files compile with zero errors, undefined references, or citations, in the order
      given in `CLAUDE.md`.
- [ ] Every theorem in `paper.tex` has a proof in `appendix.tex` that passed ticket 02, 03, 04
      or 05, and carries that label.
- [ ] No sentence refers to earlier versions, dropped results, or failed attempts.

**Status:** open

## Comments
