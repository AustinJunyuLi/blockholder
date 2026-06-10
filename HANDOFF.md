# HANDOFF — continuing this project on another machine

**Written:** 2026-06-10 · **Branch to use:** `jmp-upgrade-2026-05` (commit `4d323c0`+)
**Repo:** https://github.com/AustinJunyuLi/blockholder

---

## 1. Project state in one paragraph

The nine-month milestone (due ~Mar 2027) has been executed end-to-end on this branch: **Theorem A** (premium wedge microfounded via the disagreement-node Grossman–Hart tender game; λ = 1−q(1−γ)ψ; Appendix D7, `\input` from `quality_reports/fixes/`), **Theorem B** (GE cutoff-shift channel: inversion-free bound, hump certified as a theorem on κ∈[0.35,0.825], certified counterexample at σ_ξ=0.60; Appendix D8), **Fact 1** (13D delay compression: median 7→5.0 business days, within-5bd share 35.7%→75.6%; `empirics/output/`), plus competitor positioning, presentation updates, and full verification artifacts. Strategy and execution records: `quality_reports/plans/2026-06-10_two-path-feasibility-decision.md` (why), `…_nine-month-milestone-implementation.md` (what), `quality_reports/session_logs/2026-06-10_milestone-execution.md` (done + **author to-do list**).

## 2. Branch map

| Branch | State |
|---|---|
| `jmp-upgrade-2026-05` | **Active.** All milestone work. Work here. |
| `main` | Behind (at the pres-refactor commit). Merge when the milestone round is reviewed; quality report at merge time per `templates/quality-report.md` convention. |
| `pres-overhaul-20260305`, `theory-fixes`, `snapshot/v3-pre-v2-20260308`, `worktree-agent-*` | Historical; ignore. |

## 3. Fresh-machine setup (in order)

```bash
# 1. Clone and switch to the working branch
git clone https://github.com/AustinJunyuLi/blockholder.git && cd blockholder
git checkout jmp-upgrade-2026-05
git config user.name "Junyu Li"
git config user.email "106483677+AustinJunyuLi@users.noreply.github.com"

# 2. GitHub auth (per-machine; device flow)
gh auth login --hostname github.com --git-protocol https --web
gh auth setup-git

# 3. Python pipeline (Python >= 3.12)
make venv          # creates .venv from requirements.txt
make all           # regenerates 16 CSVs + 15 figure PDFs
                   #   (data step is pure-Python, ~10 min; CSVs are gitignored by design)

# 4. Verify the theory numerics reproduce
.venv/bin/python quality_reports/fixes/d7_takeover_game_check.py   # expect ALL CHECKS PASS
.venv/bin/python quality_reports/fixes/d8_ge_dominance_check.py    # expect ALL CHECKS PASS (~10 min)

# 5. LaTeX (TeXLive with XeLaTeX + biber + tex-gyre fonts)
xelatex draft_v2.tex && biber draft_v2 && xelatex draft_v2.tex && xelatex draft_v2.tex
cd pres && xelatex presentation.tex && biber presentation && xelatex presentation.tex && cd ..
# Gate: 0 errors, 0 undefined references, 0 undefined citations.
```

**LaTeX notes.** On a healthy TeXLive, biber just works — the citation warnings in the committed PDFs exist only because the *origin* machine (RHEL10) lacks `libxcrypt-compat` (fix there: `sudo dnf install libxcrypt-compat`). If `fontspec` cannot find "TeX Gyre Heros" (presentation theme), expose TeXLive's font dirs to fontconfig:
`~/.config/fontconfig/fonts.conf` with `<dir>/path/to/texlive/20XX/texmf-dist/fonts/opentype</dir>` then `fc-cache -f`.

## 4. What does NOT travel via git (carry manually or regenerate)

| Item | Status | Action on new machine |
|---|---|---|
| `lit/*.pdf` (papers) | Deliberately untracked (third-party copyright) | Re-download: Johnson–Swem (author site, link in scope tables), AFS (ECGI: `albuquerquefosschrothfinal.pdf`), Maug/Kahn–Winton/etc. via library. **Celentano–Levine: SSRN 5506659 (browser; anti-bot).** |
| `empirics/data/` | Gitignored, regenerable | `.venv/bin/python -m empirics.facts --per-window 150` re-downloads from EDGAR (~5 min, throttled) |
| `numerical_output/data/*.csv` | Gitignored, regenerable | `make data` |
| `.venv/` | Gitignored | `make venv` |
| `draft_v2.docx` | Untracked Word export | Carry manually if needed, or re-export |
| `pres/blockholder_seminar_40min.pptx` | Untracked binary deck | Carry manually if you want it; the Beamer deck is the source of truth |
| `presentation_bones.html`, `presentation_guide.html` | Untracked design scratch | Carry manually or drop |
| `quality_reports/workflow_backups/` | Local agent-workflow state | Leave behind |
| gh/git credentials, fontconfig fix | Per-machine | Redo step 2 (and font note) above |
| Claude Code project memory (`~/.claude/projects/...`) | Per-machine | Fresh sessions re-learn from this file + CLAUDE.md |

## 5. Where everything lives

- **Theory records:** `quality_reports/fixes/D7_takeover_game_microfound.tex` + `D8_GE_dominance_MCS.tex` (both `\input` into `draft_v2.tex`), spec note `D7_takeover_game_spec.md`, paired verification scripts + JSON artifacts (`d7_…check.py/json`, `d8_…check.py/json`).
- **Numerics:** `numerical/takeover_game.py` (endogenous wedge, opt-in via `params_with_endogenous_wedge`); new exports `export_ge_decomposition`/`export_wedge_primitives` in `numerical/export_data.py`; figures 14–15 in `pyfig/figures.py`.
- **Empirics:** `empirics/` (README inside; stdlib-only EDGAR; Fact-1 outputs committed under `empirics/output/`).
- **Positioning:** `lit/competitor_scope_tables.md` (◑ cells await your full reads), `quality_reports/plans/2026-06-10_positioning-memo.md`, Fact-2 design `…_fact2-event-study-design.md`, `lit/bloomberg_checklist.md`.
- **Presentation:** `pres/presentation.tex` (+3 new slides: positioning, Theorem A, Theorem B); `pres/slides.bib` is now a **real file** — never restore the old symlink.

## 6. Your open to-dos (the author-only list)

Full detail in `quality_reports/session_logs/2026-06-10_milestone-execution.md` §Author handoff:

1. (Old machine only) `sudo dnf install libxcrypt-compat`, then rerun biber + XeLaTeX there. On the new machine, just compile normally.
2. Download Celentano–Levine (SSRN 5506659) → `lit/`; **full reads** of C–L, Johnson–Swem, AFS against the checklists in the scope tables; validate the ◑ cells; finalize the positioning memo.
3. Confirm UCL **WRDS/CRSP** access → unlocks Fact 2 (design note is ready).
4. Run `lit/bloomberg_checklist.md` at a terminal (decision-report open item 2d).
5. Review D7/D8 as the mathematical owner (institutional primitives of the tender game; the region-theorem proof) and record sign-off in a session log.
6. Milestone talk rehearsal (~Mar 2027); deck compiles clean.

## 7. Working conventions (so any machine behaves the same)

Plan-first workflow with plans in `quality_reports/plans/`, session logs in `quality_reports/session_logs/`; D-series derivation records pattern (`DN_*.tex` + `dN_*_check.py` + JSON); never weaken the proved/conditional/numerically-verified honesty labels; verification = `make clean && make all` + check scripts + compile gates (no formal test suite). See `CLAUDE.md` (canonical) and `AGENTS.md`.
