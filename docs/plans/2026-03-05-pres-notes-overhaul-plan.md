# Presentation Notes Overhaul Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Rewrite the presentation support documents so they match the revised paper and slide deck and are genuinely useful for seminar preparation.

**Architecture:** One document will serve as a technical derivation note and the other as a live-defense memo. The rewrite should favor coherence over patching; stale sections are replaced rather than incrementally edited.

**Tech Stack:** XeLaTeX, plain LaTeX article documents, existing slide notation and model objects.

---

### Task 1: Rewrite the technical note structure

**Files:**
- Modify: `pres/lecture_notes.tex`

**Step 1: Replace the current front matter**
- Rewrite the title and opening paragraphs so the file is explicitly a technical appendix note for self-study and hand derivation.

**Step 2: Rebuild the section structure**
- Organize the file into:
  - orientation and theory-status guide,
  - model primitives and timing,
  - action payoffs,
  - cutoff characterization,
  - posterior derivations,
  - pricing and bidder problem,
  - minority-gains decomposition,
  - numerical/heuristic sections,
  - derivation checklist.

**Step 3: Remove stale or overclaiming sections**
- Eliminate or rewrite:
  - old QA-domination centrality,
  - old Weierstrass interior-peak language,
  - strong uniqueness claims,
  - welfare/policy phrasing that sounds theorem-level.

### Task 2: Rewrite the companion as a defense memo

**Files:**
- Modify: `pres/presenter_companion.tex`

**Step 1: Rebuild the opening talk map**
- Keep a concise slide-by-slide path aligned to the current 16-slide deck.

**Step 2: Add dual-use structure**
- Include:
  - podium script / transitions,
  - interruption recovery,
  - objection bank,
  - hardball theory challenges with disciplined answers,
  - backup slide map.

**Step 3: Align all answers with current theory status**
- Ensure every answer reflects the narrowed claims in the deck/manuscript.

### Task 3: Compile and verify

**Files:**
- Build: `pres/lecture_notes.tex`
- Build: `pres/presenter_companion.tex`

**Step 1: Compile lecture notes**
- Run: `latexmk -pdfxe -interaction=nonstopmode -halt-on-error lecture_notes.tex`

**Step 2: Compile presenter companion**
- Run: `latexmk -pdfxe -interaction=nonstopmode -halt-on-error presenter_companion.tex`

**Step 3: Verify PDFs exist**
- Confirm:
  - `pres/lecture_notes.pdf`
  - `pres/presenter_companion.pdf`

### Task 4: Clean build artifacts

**Files:**
- Clean intermediates in `pres/`

**Step 1: Run LaTeX cleanup**
- Run `latexmk -c` on both files.

**Step 2: Remove leftover `.bbl`, `.nav`, `.snm` if needed**
- Verify no auxiliary build files remain in `pres/`.
