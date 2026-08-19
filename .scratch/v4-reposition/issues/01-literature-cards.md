# 01 — Read the literature in full and write verified cards

**What to build:** Every paper on the reading list read cover to cover (never abstract-only) and summarized as one structured card: question; model/architecture and method; results with what is PROVED vs NUMERICAL vs ESTIMATED; institutional facts used; referee-facing strengths and weaknesses; implications for our position; page-cited quotes for every result we may lean on. A separate checker opens each source and confirms every quote and page. Cards live under `research/cards/`, one file per paper, plus an index. Reading list = the 14 papers in `lit/`, the competitor set (CONTEXT.md), and the classics/empirics the orchestrator names.

**Blocked by:** None — can start immediately.

**Status:** ready-for-human (done 2026-08-19; awaiting author read of research/cards/INDEX.md)

- [x] ≥ 28 cards written from full text; each states where the full text came from (local PDF/txt, Wiley/OUP/NBER page, SSRN)
- [x] Every card's quotes verified by a second agent (WRONG / MISCITED / UNCHECKED); WRONG items fixed, MISCITED swapped, UNCHECKED listed in the index
- [x] Index `research/cards/INDEX.md` with one line per paper (venue/status, object, margin, identification, one-line "so what")
- [x] Papers that could not be obtained listed by name with the reason
- [x] Session log entry + commit on `v4`

## Comments
- 2026-08-19 (ticket-01 session): 39 cards written (11 competitor set, 13 theory antecedents, 13 empirics/measurement, 2 surveys) + `_institutional_sec_33_11253.md` fact sheet; every card read in full by an Opus reader and re-read by a separate Opus verifier (finder ≠ verifier, refute-framed); WRONG fixed / MISCITED swapped in place, UNCHECKED listed in INDEX §3 (19 cards still carry some, mostly appendix-only proofs). Fetch: 3 Sonnet ego-browser agents via UCL (Wiley/OUP/NBER/Cambridge/Emerald open; SSRN Cloudflare-walled → author dropped Trivedi, Corum 2025, Bishop et al., Corum–Levit published manually). Still not obtained: Kyle–Vila 1991 (JSTOR), Fos 2017 MS published (INFORMS), Ben-David JF IA, Edmans 2009 IA, Edmans–Manso appendices, CCKV IA, Corum–Levit OA, CDF random-horizon WP, HMN JCF, BLV Dec-2025 revision (INDEX §2). Sonnet readers were started then hard-stopped on the author's rule (Opus reads everything; Sonnet mechanical only) — ADR-0005 updated. Log: quality_reports/session_logs/2026-08-19_v4-kickoff.md.

