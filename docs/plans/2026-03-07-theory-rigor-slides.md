# Theory Rigor Slides Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a theory-facing equilibrium-definition slide and a standing-assumptions slide to the main deck without letting the close-out become bloated.

**Architecture:** Insert two compact slides after the timeline so the equilibrium object and A5 are defined before the cutoff and mechanism slides. Recover time and visual space by merging the current two closing slides into one lean summary slide and then update appendix return-link labels to the new main-slide numbering.

**Tech Stack:** Beamer LaTeX, `latexmk`, PDF visual QA

---

### Task 1: Add main-path rigor slides

**Files:**
- Modify: `pres/presentation.tex`

**Step 1: Insert `Equilibrium Definition` after `Timeline and Actions`**

State the monotone-cutoff PBE object, Bayes consistency on reached histories, competitive pricing, and the cutoff fixed-point characterization.

**Step 2: Insert `Standing Assumptions` after `Equilibrium Definition`**

Keep A1--A7 concise, visually emphasize A5 and A6, and link to the fuller backup slide.

### Task 2: Refit the close-out slide

**Files:**
- Modify: `pres/presentation.tex`

**Step 1: Merge the two current ending slides into one**

Keep takeaways, testable implications, theory status, and welfare caveat, but remove redundancy and avoid the previous cramped layout.

### Task 3: Repair navigation and rebuild

**Files:**
- Modify: `pres/presentation.tex`
- Verify: `pres/presentation.pdf`

**Step 1: Update backup `returnlink` labels to the new main-slide numbers**

**Step 2: Rebuild**

Run: `latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error presentation.tex`

**Step 3: Visual QA**

Render and inspect the new main-path slides around the inserted rigor material and the merged closing slide.
