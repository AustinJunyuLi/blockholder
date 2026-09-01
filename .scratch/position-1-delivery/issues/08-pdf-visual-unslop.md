# P1-08: Build, inspect, and unslop the paper

Status: ready-for-agent
Blocked by: P1-07

## What to build

Deliver polished main and online-appendix PDFs from the integrated sources.

## Acceptance

- [ ] Build the main draft with XeLaTeX, Biber, and two final XeLaTeX passes; build the online appendix after the main draft so external references resolve
- [ ] Logs contain zero TeX errors, undefined references, undefined citations, or missing files
- [ ] Render every PDF page to images and inspect every page at readable scale; fix clipped text, bad breaks, overlaps, empty pages, broken glyphs, unreadable tables, and inconsistent figure or caption placement
- [ ] Compare every reported number, table cell, caption, sample count, and E1 figure with the reproduced source artifact
- [ ] Apply the `unslop` skill to the full manuscript and appendix. Remove stock AI phrasing, inflated claims, repetitive signposting, and dense prose while preserving economics, citations, conditions, and honesty labels
- [ ] A final claim search finds no causal wording for E1, no L2-to-filing-CAR equivalence, and no unconditional window sign
- [ ] Write the checked PDFs to `deliverable/draft_v3.pdf` and `deliverable/draft_v3_onlineappendix.pdf`; record hashes and the visual inspection log

## Comments
