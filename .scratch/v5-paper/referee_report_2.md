# Second referee read

I checked the 20 marked fixes against `deliverable/paper.pdf`, `deliverable/appendix.pdf`, `paper.tex`, `appendix.tex`, and `proofs/`. I did not compile. I used PDF text extraction, `pdffonts`, and rendered page images for the production checks.

## Assessment of the 20 marked fixes

### Blocking items

1. **RESOLVED.** The statutory trigger now says more than 5 percent and accounts for Schedule 13G eligibility or election. Location: `paper.tex:83-88,163-167`; `paper.pdf` pp. 2-3.

2. **RESOLVED.** The paper now separates calendar and business days in the statute from discrete trading rounds in the model. It also identifies `T=10=H` as a corner comparison rather than a calibrated copy of the reform. Location: `paper.tex:118-120,171-175,284-289,727-733`; `paper.pdf` pp. 2-3, 5, 13.

3. **RESOLVED.** The formal outcome is now consistently defined as the engagement-related component `Delta_m E[pi p]`, with the baseline term `m_0 E[p]` excluded. Location: `paper.tex:99-101,194-201,412-430`; `paper.pdf` pp. 2, 4, 7.

4. **PARTIAL.** The unsupported sentence about selected Voice paths was deleted, and the pricing-root and filing-stake claims now point to stated proofs. The two new lemmas still have no honesty label and have not passed an attack gate. The appendix says this directly. Location: `paper.tex:308,432-436,863-868`; `proofs/06_lemmas.tex:5-12,59-72`; `appendix.tex:73-75`; `appendix.pdf` pp. 25-27. The filing-stake lemma is also false on some paths, as new defect 2 explains.

5. **RESOLVED.** The pooled-experiment setup, statements, and proofs now assume noise is i.i.d. across rounds and independent of type. Location: `proofs/02_garbling.tex:28-58,93-146,237-310`; `appendix.pdf` pp. 9-11.

6. **RESOLVED.** The pooled type law and pooled-premium representation now require positive pooled mass, and the flagged result requires positive flagged mass. The endpoint decomposition also states that an average over a null cell is undefined. Location: `proofs/02_garbling.tex:53-58,85-88,93-146`; `proofs/04_inherited.tex:11-33,377-450`; `paper.tex:451-470,510-536`; `paper.pdf` pp. 8-9.

7. **PARTIAL.** The hooks in `appendix.tex` now print `Label: PROVED` before the attacked theorem, proposition, corollary, and lemma environments. The appendix still contains two unlabelled lemma environments because `\unlabelledtrue` wraps `proofs/06_lemmas.tex`. Thus the proved block is consistent, but the appendix as delivered is not fully labelled. Location: `appendix.tex:33-40,73-75`; `proofs/06_lemmas.tex:8-12,59-72`; `appendix.pdf` pp. 25-27.

8. **NOT RESOLVED.** The formal corollary states the two bands correctly, but the appendix's final reading still assigns the attenuation band `[0,(2/varphi)s_A]` to the composition condition `C_T <= 1`. That condition instead requires the band with endpoints `s_A` and `((2-varphi)/varphi)s_A`. Location: `proofs/03_caught.tex:162-182,355-359`; `appendix.pdf` pp. 22, 25. The same error was added to the introduction at `paper.tex:122-123` and `paper.pdf` p. 2.

9. **PARTIAL.** A local `ESTIMATED` label now sits immediately before the two post-minus-pre bootstrap differences. However, a second `ESTIMATED` label remains at the start of Section 6 and visually scopes the entire empirical section, including descriptive tables without uncertainty. Location: `paper.tex:780-812,817-832`; `paper.pdf` pp. 14-15.

10. **RESOLVED.** Figure 1 now uses consecutive-grid finite-difference notation in the axes and caption. The plot code evaluates those slopes at interval midpoints. Location: `numerical_v4/checks/figures.py:70-130`; `paper.tex:675-693`; `paper.pdf` p. 12.

### Minor items

1. **RESOLVED.** The text now says the policy profile is imposed and frozen, and disclaims an endogenous policy response or equilibrium-existence result. Location: `paper.tex:107-112,377-387,409-412`; `paper.pdf` pp. 2, 7.

2. **PARTIAL.** The paper now gives Item 4 as the institutional reason for disclosing purpose and future-purchase plans. It still treats the filing as revealing the exact residual target order `Q^F` and a certain engagement commitment `a=1`. Item 4 does not by itself guarantee either exact object. The stronger information set is explained as a model representation, but not acknowledged as stronger than the filing. Location: `paper.tex:95-98,351-357`; `paper.pdf` pp. 2, 6.

3. **RESOLVED.** The introduction and calibration identify the narrow five-node threshold ladder, the fixed benchmark policy, and the named liquidity grid before stating the numerical composition result. Location: `paper.tex:112-117,665-704`; `paper.pdf` pp. 2, 12-13.

4. **RESOLVED.** The empirical population is now described as all initial Schedule 13D campaigns without an Item 4 screen, with the maximum stake across reporting persons in joint filings. Location: `paper.tex:133-137,798-804`; `paper.pdf` pp. 2, 14.

5. **RESOLVED.** The paper now says the empirical section supplies descriptive context for `B^F` and filing delays and does not measure market inference. Location: `paper.tex:133-141,240-244,792-796`; `paper.pdf` pp. 2, 4, 14.

6. **RESOLVED.** The delay section reports the two negative delays, the 138 pre-2021 triggers, the oldest trigger, and the reason the registered median and within-five-day summaries are not driven by the tails. Location: `paper.tex:885-891`; `paper.pdf` p. 16.

7. **RESOLVED.** Main-text theorem titles now point to the matching appendix sections and statement numbers through the `app:` external-document prefix. The delivered PDF resolves those references. Location: `paper.tex:22-24,452-627`; `paper.pdf` pp. 8-11.

8. **RESOLVED.** Equal-mass and no-reclassification readings now use almost-sure or null-set language. Location: `paper.tex:570-572`; `proofs/02_garbling.tex:198-209,387-398`; `appendix.pdf` pp. 10, 16.

9. **RESOLVED.** The literature positioning no longer claims categorical priority. It states the narrower comparison to the cited disclosure and trading models. Location: `paper.tex:143-148,203-244`; `paper.pdf` pp. 2-4.

10. **RESOLVED.** `pdffonts` reports no Type 3 font in either delivered PDF. The rendered Figure 2 labels do not collide, appendix p. 12 starts with a full paragraph, and paper p. 19 has no orphaned bibliography line or clipping. Location: `paper.pdf` pp. 12-14, 19; `appendix.pdf` p. 12.

## New defects introduced by the fixes

1. **Blocking, false theorem summary.** The introduction now says `C_T <= 1` holds when `s_B` lies between `0` and `((2-varphi)/varphi)s_A`. The correct lower endpoint is `s_A`. The `0` lower endpoint belongs to the overall attenuation condition, whose upper endpoint is `(2/varphi)s_A`. Location: `paper.tex:118-123`; `paper.pdf` p. 2. The appendix repeats the conflation at `proofs/03_caught.tex:355-359`; `appendix.pdf` p. 25.

2. **Blocking, false and undefined filing-stake lemma.** The new lemma sets `f(s;T_0)=min{c(s;tau)+T_0,H}` for every Voice path that crosses by `H`. The model instead says a filing lands at `c+T_0` only when `c+T_0 <= H`; otherwise no filing lands and `B^F` is not defined as a stake at filing. For example, a path with `c+T>H` is pooled under the long clock, but the lemma creates a filing at `H` and compares a fictitious `B^F`. The conclusion "on every executed path" is therefore false. Location: `proofs/06_lemmas.tex:59-80`, against `proofs/04_inherited.tex:274-277` and `paper.tex:284-289`; the claim is used at `paper.tex:432-436,863-868`; `appendix.pdf` pp. 26-27 and `paper.pdf` pp. 7, 16.

## Verdict

**FAIL.** Blocking items 4, 7, and 9 remain partial, blocking item 8 is not resolved, and the fix pass introduced two blocking false claims.


# Third read

I checked the seven requested findings against the current sources and the freshly compiled `paper.pdf` and `appendix.pdf` in the repository root. I also read `.scratch/v5-paper/runs/13-attack/result.txt` and `.scratch/v5-paper/runs/13-attack-2/result.txt`. I did not compile.

## Reassessment of the requested findings

1. **Item 4: RESOLVED.** The pricing-root lemma passed the first attack. The repaired filing-stake lemma passed the second attack, which also rechecked the pricing-root lemma. Both supporting claims now cite labelled lemmas, and the pending-gate process sentence is gone. Location: `paper.tex:305,430-435,855-861`; `proofs/06_lemmas.tex:5-12,64-85`; `appendix.pdf` pp. 25-27; `.scratch/v5-paper/runs/13-attack/result.txt`; `.scratch/v5-paper/runs/13-attack-2/result.txt`.

2. **Item 7: RESOLVED.** `appendix.tex` no longer disables the automatic label hook around `proofs/06_lemmas.tex`. The fresh appendix prints `Label: PROVED` before both Lemma 8 and Lemma 9. Location: `appendix.tex:33-39,71-73`; `appendix.pdf` pp. 25-26.

3. **Item 8: RESOLVED.** The appendix closing paragraph now gives the composition band with endpoints `s_A` and `((2-varphi)/varphi)s_A`, and the overall attenuation band with endpoints `0` and `(2/varphi)s_A`. It states the common-sign condition as `s_A s_B > 0`. Location: `proofs/03_caught.tex:355-362`; `appendix.pdf` p. 25.

4. **Item 9: RESOLVED.** The section-level `ESTIMATED` label is gone. The only such label in the fresh paper sits immediately before the two post-minus-pre bootstrap differences. Location: `paper.tex:780-817`; `paper.pdf` pp. 14-15.

5. **Minor item 2: RESOLVED.** The model now says that exact disclosure of `Q^F` and `a=1` is stronger than a Schedule 13D filing and is an explicit model choice. Location: `paper.tex:348-356`; `paper.pdf` pp. 6-7.

6. **New defect 1: RESOLVED.** The introduction now assigns each clock criterion its correct band under `s_A s_B > 0`, matching the formal corollary and corrected appendix reading. Location: `paper.tex:117-124`; `paper.pdf` p. 2.

7. **New defect 2: RESOLVED.** Lemma 9 now uses the model filing date `f=c+T`, defines `B^F` only when `f<=H`, proves nesting of the filing sets, and compares filing stakes only on paths flagged under both windows. Both main-text citations preserve that domain and distinguish the pathwise result from the changing filer population. Location: `proofs/06_lemmas.tex:64-85`; `paper.tex:430-435,855-861`; `appendix.pdf` pp. 26-27; `paper.pdf` pp. 7, 16.

## New defects from the third-read changes

None. The changed passages introduce no false sentence, stronger claim, broken cross-reference, or visible production defect. The fresh PDFs contain no unresolved `??` reference and no Type 3 font.

## Third-read verdict

**PASS.** Every blocking item from the second read is resolved, and no new blocking defect exists.
