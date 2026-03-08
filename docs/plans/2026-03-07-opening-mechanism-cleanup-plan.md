# Opening Mechanism Cleanup Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Remove duplicate mechanism framing from the opening of the talk and keep the early mechanism slide purely verbal.

**Architecture:** Delete the `Key mechanism` block from the motivation slide so the mechanism is introduced only once. Replace the symbolic arrow chain on the new `Main Mechanism` slide with one plain-English summary sentence.

**Tech Stack:** Beamer LaTeX, `latexmk`, `pdftoppm`

---

### Task 1: Clean the opening slides

**Files:**
- Modify: `pres/presentation.tex`

**Step 1:** Remove the `Key mechanism` block from the `Motivation and Gap` slide.

**Step 2:** Replace the symbolic chain on `Main Mechanism` with a plain-English summary sentence.

### Task 2: Rebuild and verify

**Files:**
- Verify: `pres/presentation.pdf`

**Step 1:** Build with `latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error presentation.tex`.

**Step 2:** Render pages 2 to 4 to PNG and visually verify that the opening sequence reads cleanly.
