# Presentation Editorial Cleanup Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Remove the rule-based callout styling and bright-red palette from the full deck, replacing it with a cleaner typography-first UCL presentation style.

**Architecture:** Update the global Beamer styling in `presentation.tex` so existing `block` and `alertblock` environments render as lightweight titled sections instead of ruled callouts, then rebuild the PDF and check for layout regressions. This minimizes slide-by-slide churn while changing the look across the whole deck consistently.

**Tech Stack:** LaTeX Beamer, local UCL theme assets, XeLaTeX via `latexmk`

---

### Task 1: Revise the global style system

**Files:**
- Modify: `presentation.tex`

**Step 1: Remove bright-red accents**

Change the color assignments for alert text, alert block titles, links, and observable-variable highlighting to a muted blue/grey palette.

**Step 2: Remove horizontal block-title rules**

Edit the `block` / `alertblock` / `exampleblock` templates so they no longer draw colored rules after the title.

**Step 3: Flatten box styling**

Make the block templates render as title-plus-body sections with tighter spacing and without decorative containers.

### Task 2: Verify whole-deck rendering

**Files:**
- Modify if needed: `presentation.tex`

**Step 1: Build the PDF**

Run: `latexmk -xelatex -interaction=nonstopmode -file-line-error presentation.tex`
Expected: successful PDF build

**Step 2: Check warnings and visual samples**

Inspect the log for serious build failures and spot-check sampled pages from the main deck and appendix.

**Step 3: Apply any final refinements**

If the new typography-first styling exposes obvious spacing issues, make a final targeted edit and rebuild.
