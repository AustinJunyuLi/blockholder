# UCL Theme Reorganization Design

**Date:** 2026-03-06

**Scope:** Local cleanup of the `pres/` directory so the UCL Beamer support files do not clutter the project root.

## Goal

Move the vendored UCL Beamer theme assets into a dedicated folder while keeping `presentation.tex` self-contained and directly buildable from `pres/`.

## Approved Structure

Create a single folder:

- `theme/ucl/`

Move the following into it:

- `beamerthemeucl.sty`
- `beamercolorthemeucl.sty`
- `beamerouterthemeucltitlebanner.sty`
- `uclcolors.sty`
- `banners/`

## Loading Strategy

Patch `presentation.tex` so LaTeX searches `theme/ucl/` when resolving the Beamer theme files. Keep the public document API unchanged:

- still use `\usetheme{ucl}`
- still use `\useoutertheme[small]{ucltitlebanner}`

Also extend the graphics path so the theme can resolve its banner asset from the new folder layout.

## Verification

- Rebuild `presentation.pdf`
- Confirm the theme still loads and the banner still renders
- Remove regenerated LaTeX aux files afterwards
