# Presentation Editorial Cleanup Design

**Date:** 2026-03-06

**Scope:** Full-deck visual cleanup of `presentation.tex` after the first UCL conversion.

## Goal

Reduce visual clutter and make the deck feel less cramped by removing decorative rule-based callouts, eliminating bright red accents, and shifting from box-heavy composition to a typography-first layout.

## Approved Direction

The approved approach is an editorial cleanup:

- remove the colored horizontal rules drawn under block and alert titles;
- remove bright red from the visual system;
- keep the UCL banner/header structure;
- preserve the economics and slide ordering, but restyle the deck so titles, equations, figures, and bullets carry more of the visual hierarchy than boxes do.

## Visual Changes

- Use black/white UCL framing with muted blue accents.
- Reassign alert styling from red to neutral dark grey.
- Recolor observables away from red so the body palette stays restrained.
- Make block environments render as simple titled text sections rather than ruled callouts.

## Layout Changes

- Let existing `block` and `alertblock` content render as plain titled sections with tighter spacing.
- Keep only the minimum structural emphasis needed for backup proposition/proof slides.
- Preserve final PDF output and rebuild after the cleanup.
