# 02 — Competitor map and whitespace table

**What to build:** One table over the competitor set (and any 2024–26 paper a fresh sweep of SSRN/NBER/JF-RFS-JFE forthcoming pages turns up): venue and stage, object studied, margin of the disclosure rule (threshold / window / none), identification (theory / structural / reduced-form + shock), and what the paper explicitly does NOT do (quoted). A "whitespace" section listing objects/margins/identifications no row occupies, each with the card that would refute it and why it does not.

**Blocked by:** 01 — Literature cards.

**Status:** done (2026-08-19)

- [x] Every row sourced to a card or a page-cited quote; verified by a second agent
- [x] Sweep of new 2024–26 work done (SSRN + Scholar + journal forthcoming pages), hits added or "none found" stated with the queries used
- [x] Whitespace list with refutation check per item
- [x] Commit on `v4`

## Comments

- 2026-08-19 (Fable head + Agent team; ADR-0005). Deliverable: `research/competitor_map.md` — Part 1: 11 competitor rows + 2 sweep-addition rows (Zeng RAS 2026; Gryglewicz–Mayer–Morellec Dec-2025 WP), every cell sourced to a card §/page, "does NOT do" cells verbatim quotes; Part 2: occupied cells (hazards); Part 3: whitespace W1–W14 with refuter card + rating (CLEAR: W1 window length→premium theory, W2 control outcome × Feb-2024 DiD w/ control, W3 rule-keyed partition, W5 legal deadline + partition in a Kyle model, W6 rule moves the κ-slope, W8b bidder entry × window, W13 campaign success × window change (power-limited); NARROW: W4, W7 (provisional — Payne-Mann walled), W8a, W9, W10, W11, W12-existence; W14 = looks open, really occupied).
- Sweep: `research/sweep_2024_26_A.md` (20 queries: Scholar/SSRN/NBER) + `research/sweep_2024_26_B.md` (47 visits: JF/RFS/RoF/RAPS/JFE/JCF/Ecta/MS/JFQA, ECGI, CEPR, arXiv, SFI, NY Fed/FEDS, AFA 25/26, WFA 25, Cavalcade 25/26, EFA 25). **No 2024–26 paper combines liquidity × the 13D rule × a control outcome.** DIRECT hits: Zeng (carded, verified); Payne-Mann–Stice-Lawrence–Wong SSRN 5076900 (WALL — author to drop manually; only W7 depends on it). ADJACENT (not read): Duong–Pi–Sapp JCF 2025, Gryglewicz et al. (carded), Lee–Kim–Kim ECGI 2024, Eckbo–Malenko–Thorburn ECGI 2025, Israelsen et al. RCFS 2025, Bogousslavsky–Fos–Muravyev JF 2024, Choi et al. SSRN 2025, Freund et al. FR 2025, Meles et al. EJF 2026; plus Chabakauri et al. (2022, outside window, named by Zeng) as a candidate for a later reader.
- Verification: mapverifier (opus) — Part 1 76 OK/0 W/1 M; Part 2 17/1/1; Part 3 11/2/1 (fabricated Polk quote in W2 replaced; W9 CLEAR→NARROW; 9 omissions added). Card verifiers: Zeng 30/3/2/5, GMM 40/0/4/1. rowsverifier — map additions 32/2/4/0, INDEX 3/0/3 — all fixed in place. Team: 2 sonnet sweepers, 1 opus builder (2 passes), 2 opus readers, 4 opus verifiers.
- Open: Payne-Mann PDF (author); Zeng Springer IA (Table IA.2 size split, decision-critical for the κ opening); BLV Dec-2025 revision; CCKV IA/pagination — all listed in INDEX §2/§3 and the map's verification log.
