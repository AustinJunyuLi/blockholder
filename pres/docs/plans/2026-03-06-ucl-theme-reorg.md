# UCL Theme Reorganization Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Move the vendored UCL Beamer support files into a dedicated `theme/ucl/` folder without breaking local builds.

**Architecture:** Reorganize the theme assets on disk, then patch `presentation.tex` so TeX searches the new folder for theme files and banner graphics. Finish by rebuilding the deck and removing regenerated aux files.

**Tech Stack:** LaTeX Beamer, vendored UCL theme files, XeLaTeX via `latexmk`

---

### Task 1: Create the theme asset folder and move files

**Files:**
- Create: `theme/ucl/`
- Move: `beamerthemeucl.sty`
- Move: `beamercolorthemeucl.sty`
- Move: `beamerouterthemeucltitlebanner.sty`
- Move: `uclcolors.sty`
- Move: `banners/`

**Step 1: Create the folder**

Create `theme/ucl/`.

**Step 2: Move the theme files**

Move all vendored UCL `.sty` files and the banner asset directory into `theme/ucl/`.

**Step 3: Verify the new tree**

Confirm the root is cleaner and the theme assets exist under `theme/ucl/`.

### Task 2: Patch the document to load the moved assets

**Files:**
- Modify: `presentation.tex`

**Step 1: Add TeX input path setup**

Set `\input@path` so `\usetheme{ucl}` and related theme lookups resolve from `theme/ucl/`.

**Step 2: Add theme asset graphics path**

Extend `\graphicspath` so banner graphics continue to resolve after the move.

**Step 3: Keep the deck API unchanged**

Do not rewrite the document to use custom package names or absolute paths.

### Task 3: Rebuild and clean

**Files:**
- Modify if needed: `presentation.tex`

**Step 1: Build the deck**

Run: `latexmk -xelatex -interaction=nonstopmode -file-line-error presentation.tex`
Expected: successful PDF build

**Step 2: Verify no missing-theme failures**

Check that the banner and theme load correctly and that the PDF is produced.

**Step 3: Remove generated aux files**

Delete the LaTeX build byproducts after verification.
