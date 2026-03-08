# Mechanism Preview Slide Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a high-level mechanism review to the main path before the pricing building block and rewrite backup slide B5 so it explains the mechanism step by step rather than using the “no fixed point required” language.

**Architecture:** Insert a new main `Mechanism Preview` slide between `Equilibrium Cutoffs` and `Inference, Bid Entry, and Prices`. Rewrite B5 as a three-step mechanism-and-pricing slide, then update backup return labels and slide-number text to reflect the new main-slide ordering.

**Tech Stack:** Beamer LaTeX, `latexmk`, `pdftoppm`

---

### Task 1: Add the main-path mechanism preview

**Files:**
- Modify: `pres/presentation.tex`

**Step 1:** Insert a new main slide after `Equilibrium Cutoffs`.

**Step 2:** Use mechanism-first language: public signal, inferred activism, value/premium/bid incentives, and why liquidity matters.

**Step 3:** Add backup links from the preview into the rigorous mechanism material.

### Task 2: Rewrite B5

**Files:**
- Modify: `pres/presentation.tex`

**Step 1:** Retitle B5 to `Mechanism and pricing logic`.

**Step 2:** Replace the current feed-forward wording with three explicit steps: signal to beliefs, beliefs to bidder incentives, prices from those objects.

**Step 3:** Remove the “No fixed point required” phrase.

### Task 3: Keep slide references consistent

**Files:**
- Modify: `pres/presentation.tex`

**Step 1:** Update hard-coded backup return labels for the shifted main slide numbers.

**Step 2:** Update any `Pricing derivation` link text to match the new B5 title.

### Task 4: Rebuild and verify

**Files:**
- Verify: `pres/presentation.pdf`

**Step 1:** Build with `latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error presentation.tex`.

**Step 2:** Render the new preview slide, the revised main mechanism slide, and B5 to PNG.

**Step 3:** Visually confirm the new structure reads cleanly and that the slide references match the new order.
