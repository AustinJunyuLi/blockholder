# Presentation Overhaul Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Convert the full presentation to the UCL Beamer style and rework awkward slide layouts across the main deck and appendix.

**Architecture:** Vendor the UCL Beamer theme assets into the presentation directory, then refactor `presentation.tex` so the preamble, title treatment, block styling, frame layouts, and appendix all align with the new visual system. Finish by compiling the deck and fixing any layout regressions exposed by the build.

**Tech Stack:** LaTeX Beamer, local UCL theme `.sty` assets, existing PDF figures and tables, `latexmk`

---

### Task 1: Add local UCL theme assets

**Files:**
- Create: `banners/uclbannerblack.pdf`
- Create: `beamerthemeucl.sty`
- Create: `beamercolorthemeucl.sty`
- Create: `beamerouterthemeucltitlebanner.sty`
- Create: `uclcolors.sty`

**Step 1: Create the local banner asset directory**

Run: `mkdir -p banners`
Expected: directory exists with no errors

**Step 2: Copy the reference UCL theme files into this repo**

Run: `cp ...`
Expected: the four `.sty` files and banner PDF appear under `pres/`

**Step 3: Verify the copied files are present**

Run: `ls beamerthemeucl.sty beamercolorthemeucl.sty beamerouterthemeucltitlebanner.sty uclcolors.sty banners/uclbannerblack.pdf`
Expected: all files listed successfully

### Task 2: Refactor the presentation preamble and global style

**Files:**
- Modify: `presentation.tex`

**Step 1: Replace the theme selection**

Change the preamble from `metropolis` to the UCL theme and outer theme.

**Step 2: Apply the workspace UCL customizations**

Add the title-color, frame-title, block-template, and footer adjustments required by the UCL workflow.

**Step 3: Keep the existing content macros compatible**

Retain notation macros, bibliography setup, figures, and hyperlinks while adapting colors to the new theme.

### Task 3: Rebuild the main-talk frames for the new layout

**Files:**
- Modify: `presentation.tex`

**Step 1: Rework the title slide**

Move from the custom Metropolis-style title frame to a cleaner UCL title page.

**Step 2: Refactor dense content frames**

Rewrite crowded main-talk frames so each slide has a clearer visual center and better spacing.

**Step 3: Normalize spacing and text sizes**

Reduce reliance on `scriptsize`/`footnotesize` where possible and rebalance columns around figures and tables.

### Task 4: Restyle and reflow the appendix

**Files:**
- Modify: `presentation.tex`

**Step 1: Bring appendix slides into the same visual system**

Make the backup slides look consistent with the main talk under the UCL theme.

**Step 2: Simplify repeated proof/result boxes**

Use cleaner callout patterns and spacing for backup theorem/proof slides.

**Step 3: Fix obvious awkward layouts**

Adjust tables, figures, and paragraph blocks where the current appendix frames are too compressed.

### Task 5: Compile and verify the deck

**Files:**
- Modify if needed: `presentation.tex`

**Step 1: Build the PDF**

Run: `latexmk -pdf -interaction=nonstopmode -file-line-error presentation.tex`
Expected: successful PDF build

**Step 2: Inspect for regressions**

Check the generated PDF for banner issues, title rendering, overfull content, and broken appendix layouts.

**Step 3: Apply final fixes and rebuild**

Repeat small layout edits until the deck compiles cleanly and the obvious styling issues are resolved.
