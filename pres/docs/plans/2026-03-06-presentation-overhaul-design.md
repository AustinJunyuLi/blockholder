# Presentation Overhaul Design

**Date:** 2026-03-06

**Scope:** Full-deck redesign of `presentation.tex`, including the 16-slide main talk and the appendix backup slides.

## Goal

Convert the current seminar deck from the `metropolis` theme to the UCL Beamer banner style, while also reworking slide structure so the talk reads as a cleaner, more deliberate research presentation rather than a dense draft deck.

## Design Choice

The approved direction is an aggressive overhaul rather than a theme-only port. The redesign will preserve the economics, figures, citations, and overall paper logic, but it will rewrite slide composition where necessary:

- move to the UCL banner theme with the local customizations required by this workspace;
- replace filled theorem/result boxes with lighter underline callouts;
- give figures and equations more space by reducing over-compressed columns and tiny body text;
- standardize title treatment, spacing, and footer behavior across the main deck and appendix;
- tighten slide narratives where the current layout feels like notes pasted onto a page.

## Visual System

- Use the UCL black banner header with white bold frame titles.
- Remove the black title box on the title slide so the opening slide feels cleaner.
- Keep slide-body variable color coding, but neutralize those colors inside frame titles so the banner remains legible.
- Use a restrained palette: UCL black/white plus bright blue for structural emphasis and rich red only for warning-style callouts.
- Favor white space and aligned text blocks over dense `alertblock` stacks.

## Layout Strategy

### Main deck

- Rebuild the title slide around the UCL title-page treatment.
- Rebalance the early literature and notation slides, which currently rely on narrow columns and small text.
- Simplify the proposition/result slides so each frame has one dominant visual anchor: a table, a figure, or a single callout.
- Reduce the number of places where text competes with a full-width figure on the same frame.

### Appendix

- Keep the appendix comprehensive, but make it visually consistent with the main talk.
- Convert repeated proof/result `alertblock`s into cleaner theorem-style callouts with better spacing.
- Reflow the densest backup slides so tables, equations, and proof sketches are easier to scan in Q&A.

## Theme Asset Plan

Vendor the UCL Beamer theme files directly into `pres/` so the deck is reproducible from this directory:

- `beamerthemeucl.sty`
- `beamercolorthemeucl.sty`
- `beamerouterthemeucltitlebanner.sty`
- `uclcolors.sty`
- `banners/uclbannerblack.pdf`

## Verification Plan

- Compile the deck locally after the refactor.
- Inspect the resulting PDF for obvious theme regressions, overflow, broken links, or banner/title issues.
- Iterate on any visibly awkward frames that remain after the first pass.
