# 02 · Garbling lemma at order size two, and the threshold dial proved from it

**Lane:** theory. **Routing:** writer grok `high`; independent attacker opus `high`.
**Blocked by:** none for the proofs; 01 for the grid verification of any named condition.
**Blocks:** 11.

**What to prove.** With the blockholder's order equal to two noise lumps, the pooled-cell
experiment (the order-flow history observed by the market, as an experiment about the plan's
engagement flag and stake path) at noise intensity κ' > κ is a garbling of the experiment at κ:
the ambiguous outcome carries likelihood ratio one and its mass rises in κ, every other outcome is
revealing, and the revealing outcomes' relative masses do not depend on κ. Conclude that the
pooled expectation of h(π) = π p is monotone in κ with the sign of the chord the model already
carries, for every history depth up to H. Then prove the threshold dial: at fixed policies, a
tighter threshold weakly lowers S = (1 minus Ω) S_P through the weight leg (Ω rises) and the
composition leg (S_P does not rise). Where the inherited proof used bridge clauses, prove each
from the order-size-two structure; any clause that does not follow is stated as one named
condition in the theorem's hypothesis and verified on the grid (NUMERICAL, grid named). The proof
is written into `proofs/02_garbling.tex`, statement first, in the paper's notation. Ticket 11
assembles `appendix.tex` from the `proofs/` files.

**Attack gate.** The attacker reads the statement and the proof and tries to break it.
PASS or FAIL with the hole. On FAIL the writer fixes once; a second FAIL is STOP.

**Acceptance.**
- [ ] Lemma statement, proof, and the threshold theorem with at most one named condition.
- [ ] Attacker PASS on the written proof.
- [ ] If a named condition exists: a check script under `numerical_v4/checks/` verifies it at
      every calibration node at `mark=2` and the record is cited.
- [ ] No sentence refers to the inherited draft, prior assumptions, or what was replaced.

**Status:** write exists (Kimi, 2026-09-02); old blind re-derive PASS does not count under the attack gate; attack still due; Condition D grid check satisfied by numerical_v4/checks/t2_threshold_revelation_check.json (rev_condition_D pass at every node, hash fbacc963f39422c3, mark 2, H 10); commit pending

## Comments
