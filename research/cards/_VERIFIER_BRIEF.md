# Verifier brief — Ticket 01 literature cards (2026-08-19)

You are an adversarial verifier. A separate reader wrote the card(s) named in your prompt.
You never see the reader's reasoning — only the card and the source. Your job is to REFUTE.
Repo root: /Users/austinli/Projects/blockholder_v4. Read CONTEXT.md and research/cards/_TEMPLATE.md first.

## Checks (all executed against the source, not against opinion)
1. Quotes (§8 and any quote elsewhere): grep each quote in the source text file(s) named in
   the card header (`grep -nF` on a distinctive 6–10-word fragment; if the txt lacks page
   markers, re-extract from the PDF with `pdftotext -layout` or per page with
   `pdftotext -f N -l N -layout <pdf> -` and confirm the printed page). Verdict per quote:
   OK / WRONG (text not in source, or meaning altered) / MISCITED (text present, page or
   attribution off) / UNCHECKED (could not check — say why).
2. Results (§3): re-read the cited proposition/table/page and confirm the statement and the
   honesty label (PROVED / NUMERICAL / ESTIMATED / ASSERTED). A label that is too strong is WRONG.
   Numbers must match the print exactly (SEs, N, periods, windows).
3. Scope claims (§6): every "they do not do X" / "never mention Y" claim — grep the full text
   for the obvious terms (e.g. liquidity, noise, 13D, window, five business days, premium,
   bidder, disclosure, threshold) and confirm or refute.
4. Version/venue claims in the header: confirm from the PDF front matter.
5. Omissions: read the full paper (all pages) and list anything MATERIAL to a position on
   liquidity × disclosure-rule × control outcomes that the card neglects: a result, a
   proposition, a stated limitation, an institutional fact, a data detail. Be concrete
   (page + one line). This is the check the author cares about most.

## Output
- Append to the card a filled §9 "Verification log": one line per quote/result checked with
  the verdict and what was checked against; a list of omissions; a one-line overall verdict.
- Apply the fixes yourself, in the card: WRONG → correct the text (or delete the item if it
  cannot be sourced); MISCITED → fix the page/attribution; omissions → add the missing item
  in the right section, marked "(added by verifier)". Leave UNCHECKED items in place, marked.
- Do not touch any other file. Do not commit.
- Stop when every card in your prompt has a §9 log; ~30 turns per card.

## Return message (≤ 20 lines)
Per card: counts (OK / WRONG / MISCITED / UNCHECKED), the WRONG items in one line each,
the omissions added, and any claim you could not check that is decision-critical for
positioning (name it — never triage it away).
