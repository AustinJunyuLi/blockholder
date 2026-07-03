# Session Log — Framing Reframe (draft_v2.tex)

**Date:** 2026-07-03
**Trigger:** `/model-council` on `~/Downloads/framing_memo.md` — "evaluate the work and adjust the framing accordingly."

## Goal
Evaluate an external framing memo against the actual draft, then implement the framing changes it justified.

## Evaluation verdict (memo vs. draft)
Memo substantially correct, but fault narrowly located: **the body is already scrupulously honest** (Prop 6 titled "Disclosure Attenuation (Partial Equilibrium)" l.991; Prop 10 "net sign indeterminate and governed by primitives" l.1841; conclusion says "result" not "theorem"). The overselling lived **only in the abstract** ("disclosure-attenuation theorem," "certified single-peakedness region"). Intro already led with the hump narratively and already contained the puzzle-facts (l.101) + best sentence (l.99) — memo's asks were mostly resequencing + register alignment, not rewriting. Disagreed with memo point (b): kept disclosure-attenuation as marquee *contribution* (genuine novelty + policy hook), reordered only the *exposition*.

## User decisions
- Title → Hybrid: "Exit, Voice, and Disclosure: Liquidity and Takeover Premia under Stake-Triggered Ownership Rules"
- Billing → reorder exposition (hump first as engine), keep attenuation as marquee, PE/GE honesty in-abstract, drop "theorem"
- Empirics → no §6 change this pass

## Edits (draft_v2.tex)
1. Title (l.73–74) — three-noun list → finding-forward hybrid.
2. Abstract (l.84) — full rewrite, 150 words: opens on economic idea; hump first (conditioned "single-peakedness certified over a baseline region"); attenuation "sharply PE, conditionally GE"; wedge microfoundation; closes on 5%/3% policy hook. "theorem" removed.
3. Intro contribution sentence (l.93) — "this paper is the first to…" → relational framing vs. EGC 2015 / OCB 2022 / Corum–Levit 2019 / Cetemen 2026.
4. Intro results paragraph (l.97) — added PE-sharp / GE-conditional status label + credibility sentence, `\ref{prop:ge-disclosure}`.

## Review (codex, cross-family — Fable/Opus authored prose)
- PASS: attenuation framing faithful to Props 6/10; intro channel sentence faithful; all 4 `\citep` keys + `\ref` resolve; no LaTeX hazards; title consistent.
- **Major (fixed):** abstract asserted hump unconditionally; body treats it as conditional (Prop nonmonotone l.919; trough in 4/20 cells l.2871). Fixed by conditioning at assertion — "single-peakedness certified over a baseline region."
- **Minor (fixed):** "both primitives are microfounded" imprecise (single-peakedness is certified/numerical, not microfounded). Fixed — only the wedge now called microfounded.

## Verification
`xelatex` exit 0, no errors; abstract exactly 150 words (cap respected). Not committed (framing change to JMP — left for author review).

## Extend pass (memo §3.5) — subordinate §Welfare / §Extensions
Added two roadmap sentences so the reader keeps the thread to the two core results:
- Extensions (l.1763) — opening sentence framing all benchmarks as robustness bracketing the disclosure-attenuation mechanism; GE analysis marks where the sign turns indeterminate.
- Welfare (l.1139) — opening sentence carrying the hump + attenuation into a normative register.

**Codex cycle 1:** 3 Major + 1 Minor — my roadmap sentences themselves over-claimed:
(M1) "marks precisely where the attenuation sign turns" contradicted Prop 10's indeterminate net sign;
(M2) "None introduces a new channel" clashed with the named transparency/deterrence channels;
(M3) Welfare sentence over-subordinated + clashed with "genuine planner problem, not a corollary," understating the section's own planner results (κ*−κ† wedge l.1370, disclosure wedge l.1570, first-best l.1667);
(minor) "media or leaks rather than filings" too exclusive.
**Fix (cycle 2):** softened to "ceases to carry a determinate sign," "rather than introducing a mechanism of its own," "carries… into a normative register," "not only through filings." **Codex cycle 2: all 4 RESOLVED, no new issues.** `xelatex` exit 0.

Lesson: register-alignment edits can themselves drift into overclaim — the cross-family faithfulness check is what caught it. Not committed; staged for author review.
