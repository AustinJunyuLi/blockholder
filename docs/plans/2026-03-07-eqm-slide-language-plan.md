# Equilibrium Slide Language Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make the main-deck equilibrium explanation more seminar-friendly while keeping the backup equilibrium material fully formal.

**Architecture:** Keep the formal theorem content in backup slides and shift the main path to plain-language descriptions of what the market sees, how inference works, and what self-consistency means. Align the timeline wording with the same public-signal language so the main deck no longer overuses `h` or invites the literal `X` observability objection.

**Tech Stack:** Beamer LaTeX, generated PDF figure from `numerical/figures.py`, `latexmk`, `python -m numerical.figures`

---

### Task 1: Rewrite the main-deck wording

**Files:**
- Modify: `pres/presentation.tex`
- Modify: `numerical/figures.py`

**Step 1:** Replace the main timeline sentence with public-signal language that mentions `(X,D)` only as the baseline summary.

**Step 2:** Rewrite the main equilibrium slide bullets so they explain inference and consistency in plain English, while preserving cutoff notation and bidder private synergy `\xi`.

**Step 3:** Update the generated timeline figure text so it matches the revised main-slide wording.

### Task 2: Rebuild and verify the deck

**Files:**
- Verify: `pres/presentation.pdf`

**Step 1:** Regenerate the timeline figure with `python -m numerical.figures --output-dir /home/austinli/Dropbox/Projects/Blockholder/directory/numerical_output`.

**Step 2:** Rebuild the deck with `latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error presentation.tex`.

**Step 3:** Render the affected pages to PNG and visually verify that the timeline, equilibrium slide, and formal backup slides all read cleanly.
