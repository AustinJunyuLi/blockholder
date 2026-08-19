# Fetch Log B

| slug | status | source URL used | pages | txt bytes | note |
|---|---|---|---|---|---|
| ordonez_calafi_bernhardt_2022_jfqa | OK | https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/blockholder-disclosure-thresholds-and-hedge-fund-activism/3A56BF8A41948A79931DDE3920BFA71E (PDF: .../S0022109022000059a.pdf) | 26 | 99613 | Task-given DOI 10.1017/S0022109021000594 resolved to a *different* article ("Media Partisanship..."); found correct paper via Cambridge Core search instead. Actual DOI is S0022109022000059. |
| massa_xu_2013_jfqa | OK | https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/value-of-stock-liquidity-in-the-ma-market/8CF3F82E07AF0E9296F74D41AA1FBECC (PDF: .../S0022109013000604a.pdf) | 35 | 164297 | UCL-authenticated Cambridge Core access confirmed working. |
| bebchuk_brav_jackson_jiang_2013_clr | OK | https://business.columbia.edu/sites/default/files-efs/pubfiles/6038/prediclsoure_accumulation.pdf | 42 | 96815 | columbialawreview.org site search returned no hits for this 2013 archive item. Found via Bing search -> Columbia Business School faculty page. This is the "Working Draft, May 2013" (Forthcoming, J. Corporation Law) version, not a CLR-branded PDF, but same title/authors/content. |
| polk_et_al_2024_jfrc | OK | https://www.emerald.com/jfrc/article-pdf/32/4/516/9544340/jfrc-01-2024-0016.pdf | 23 | 118524 | UCL Emerald access confirmed (page showed "Authenticated by ... UCL" equivalent; had to click "Reject All" on cookie consent banner first, per privacy-preserving default, before PDF link appeared in DOM). |
| trivedi_2026_ssrn | WALL | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6866499 | - | - | Cloudflare "Just a moment..." bot-check, did not clear after ~13s wait. No fallback given for this target; not bypassed. |
| corum_2025_ssrn | WALL | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4319599 | - | - | Same Cloudflare wall. Fallback tried: author's Cornell page (https://business.cornell.edu/profiles/aac256/) — page lists only an SSRN link back to the same walled URL; dead link http://ewfs.org/wp-content/uploads/2024/01/Activist-Short-Termism-updated-2023.08.31.pdf found via search (404 "Page not found"). |
| bishop_fos_jiang_partnoy_2026_ssrn | WALL | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6061814 | - | - | Same Cloudflare wall. Fallback tried: co-author Vyacheslav Fos's Google Sites page (https://sites.google.com/a/bc.edu/vyacheslav-fos/home/research) — hit a browser cert error (ERR_CERT_COMMON_NAME_INVALID), not bypassed; Duke Scholars page (https://scholars.duke.edu/publication/1907820) links only to the same SSRN DOI. |
| huang_maharjan_nanda_2024_jcf | OK | https://www.bayes.citystgeorges.ac.uk/__data/assets/pdf_file/0009/437949/45.-maharjan_liquidity-ma.pdf | 52 | 173253 | SSRN 4730486 walled (not tried directly per instructions — ScienceDirect off-limits too). Found open working-paper PDF (Sept 2017 draft, co-authored by Nishant Dass + Huang/Maharjan/Nanda) hosted by Bayes Business School (Dass's prior institution page). Title/authors verified in extracted text. |
| corum_levit_2019_jfe_published | WALL (partial) | primary: ScienceDirect (not attempted, off-limits per instructions); SSRN 2586254/2600340 Cloudflare-walled | - | - | Could not obtain the final JFE (2019) published PDF or its Online Appendix from any open source. Found only earlier working-paper drafts, all pre-dating the repo's existing Aug-2016 copy: (1) https://www.law.nyu.edu/sites/default/files/Doron%20Levit.pdf — identical Aug 11, 2016 draft already held (not re-saved as duplicate); (2) https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/06-15.levit_.pdf — earlier "First draft: March 15, 2015 / This draft: October 14, 2015" version (60pp) — not saved, superseded by the Aug-2016 copy already in repo; (3) UPenn ScholarlyCommons repository.upenn.edu bitstream link resolves to a DSpace Angular app shell, not a direct PDF. No standalone Online Appendix file found anywhere open. |

## Wall URLs requiring manual access (author must open in own browser)

- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6866499 (Trivedi 2026)
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4319599 (Corum 2025)
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6061814 (Bishop, Fos, Jiang & Partnoy 2026)
- https://www.sciencedirect.com/science/article/pii/S0304405X19300236 (Corum & Levit 2019, JFE — final published version + Online Appendix; not attempted per instructions, ScienceDirect is bot-blocked)

## Author manual drop (2026-08-19)
| corum_levit_2019_jfe_published | OK (author) | ScienceDirect S0304405X19300236 | 17 | see txt | published JFE 133(1) 1–17; Online Appendix NOT included |
| corum_2025_ssrn | OK (author) | SSRN 4319599 | 77 | see txt | April 15, 2025 version |
| bishop_fos_jiang_partnoy_2026_ssrn | OK (author) | SSRN 6061814 | 46 | see txt | HKU paper series 2026/006 version |
| trivedi_2026_ssrn | OK (author) | SSRN 6866499 | 25 | see txt | dropped by author as ssrn-6866499.pdf |
