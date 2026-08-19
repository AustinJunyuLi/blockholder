# Judge brief — Ticket 03 positioning tournament (2026-08-19)

You are ONE of several independent judges. You do not see the other judges' scores. Repo
root: /Users/austinli/Projects/blockholder_v4. You are adversarial: your default is that a
proposal overclaims until its citations check out.

## Read first (do not edit)
CONTEXT.md; docs/adr/0003, 0004; .scratch/v4-reposition/spec.md; research/competitor_map.md;
research/cards/INDEX.md; research/positions/_PROPOSER_BRIEF.md; then EVERY proposal file
research/positions/P*.md. For each proposal open the cards it cites where a claim is
decision-critical and check the claim against the card.

## Score each proposal 1–5 on each criterion, with a two-to-four-line reason per score:
A. Whitespace — does the position sit in a cell the map rates CLEAR (or NARROW with the
   named card disposed of)? Penalise any claim the map or a card refutes.
B. Fact anchoring — is the anchor a verified institutional fact (card/page), and is every
   competitor claim sourced?
C. Main result — is it stated precisely, is the proof route credible, is the honesty label
   realistic, is the technical risk named honestly?
D. Empirical design — does it pass the referee checklist (control group or bounded null,
   confounds, power, placebo, pre-trend, parser validation) on data in hand?
E. Deliverability by December — realistic weeks, no new tools/data/coauthors, credible fallback.
F. Supervisor continuity — a recognisable descendant of draft_v2 (liquidity × rule × control).
Also: one line on the proposal's single biggest flaw, and one line on what you would steal
from it for the winner.

## Output
Write research/positions/JUDGE_<k>.md: a score table (proposals × criteria, plus total and
rank), the reasons, the flaw/steal lines, and your ranking with a one-paragraph
justification of the top two. If two proposals are near-identical in position, say so.

## Rules
- Check, do not trust: at least three decision-critical citations per proposal opened in
  the card and confirmed or refuted (say which).
- Do not edit proposals or cards. No commit. ~30–40 turns.

## Return (≤ 12 lines)
Ranking with totals; the refuted claims you found (proposal · claim · card that refutes it);
your winner and runner-up in one sentence each.
