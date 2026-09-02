let meta = #{
    name: "v5-batch-1",
    description: "Run v5 paper batch 1 in order: checkpoint-0 nits, who-gets-caught grid, existence, E2 run, E2 audit",
    when_to_use: "Implement remaining v5 paper tickets in batch 1 on branch v5",
    phases: [
        #{ title: "Step 0 nits", detail: "04-fix, 02-nits, 03-nits in parallel" },
        #{ title: "Who gets caught grid", detail: "finish t5_who_gets_caught.py and run --nodes 1" },
        #{ title: "Existence write", detail: "proofs/05_existence.tex and condition script" },
        #{ title: "Existence self-attack", detail: "fresh attacker; fix once only on FAIL" },
        #{ title: "E2 run", detail: "fingerprints run e2" },
        #{ title: "E2 audit", detail: "fresh auditor for E2-G2" },
        #{ title: "Batch result", detail: "write runs/batch-1/result.txt and stop" },
    ],
};

let result_schema = #{
    "type": "object",
    "properties": #{
        "status": #{ "type": "string" },
        "summary": #{ "type": "string" },
        "files_changed": #{ "type": "array", "items": #{ "type": "string" } },
        "evidence": #{ "type": "string" },
        "named_condition": #{ "type": "string" },
    },
};

let verdict_schema = #{
    "type": "object",
    "properties": #{
        "verdict": #{ "type": "string" },
        "reasons": #{ "type": "string" },
    },
};

fn rules() {
    let s = "Workspace: /Users/austinli/Projects/blockholder_v5 on branch v5. ";
    s += "Read CLAUDE.md, CONTEXT.md, and .scratch/v5-paper/spec.md with read_file before any edit. ";
    s += "Run no git command of any kind, including status, log, and stash. ";
    s += "Use PYTHONPATH=. .venv/bin/python, never system python. ";
    s += "Do not lower H. Do not run numerical_v4.smoke at mark 2. Do not run a full grid. ";
    s += "A check script is only ever run with --nodes 1. One evaluation at order size two takes about ten seconds and six gigabytes; run at most one at a time. ";
    s += "Do not kill any background process. T1 and L4 reruns may be running; leave them. ";
    s += "Do not edit empirics/spec.md. Do not change an honesty label. ";
    s += "Proof prose: positive results only, no em dashes, never mention earlier versions or the inherited draft, never promote a label. ";
    s += "If this step's result.txt already exists and its status field is PASS or ABSENT, do not redo the work. Read that file, confirm the named edits are actually present in the target files, and return those fields. If the result says PASS but the named edits are missing, do the edits. ";
    s += "A run directory that already exists holds debris from killed runs: write result.txt there and touch nothing else in that directory. ";
    s += "Write the step result JSON to the path named in this prompt. Report every file you changed in files_changed. ";
    s += "Do not use worktree isolation. Do not start the next batch. ";
    s
}

fn status_of(r) {
    if r == () { return "FAIL"; }
    if r.success != true { return "FAIL"; }
    let out = r.output;
    if out == () { return "PASS"; }
    if type_of(out) != "map" { return "PASS"; }
    if out.status == () { return "PASS"; }
    out.status
}

fn verdict_of(r) {
    if r == () { return "FAIL"; }
    if r.success != true { return "FAIL"; }
    let out = r.output;
    if out == () { return "PASS"; }
    if type_of(out) != "map" { return "PASS"; }
    if out.verdict == () { return "PASS"; }
    out.verdict
}

fn mark_stop(cur, nxt) {
    if cur == "STOP" { return "STOP"; }
    if nxt == "STOP" { return "STOP"; }
    cur
}

// ---------------------------------------------------------------------------
phase("Step 0 nits");
log("Step 0: 04-fix, 02-nits, 03-nits in parallel on distinct files");

let p04 = rules();
p04 += "STEP 04-fix. Ticket context: .scratch/v5-paper/grok/checkpoint-0.md section Step 0 of batch 1, and .scratch/v5-paper/runs/04-attack/result.txt. ";
p04 += "Edit only proofs/04_inherited.tex and write .scratch/v5-paper/runs/04-fix/result.txt. ";
p04 += "Do exactly this. Theorem thm:clock: add to the hypothesis list that the hypotheses of prop:factorisation hold at both clocks and that kappa maps to M_P(kappa, tau, T') is differentiable, exactly as clause (iii) of lem:threshold-weight already gates on the proposition at both thresholds. Cite the proposition where the proof says By the factorisation. Do not change the proof's logic. ";
p04 += "In the same edit apply the 04 wording nits: (1) thm:clock and lem:threshold-weight must name b_0 < tau, Voice date-monotonicity (S4, ref p:paths) and only Voice plans cross (S5, ref p:clock); (2) lem:partition Step 6 currently says the history-to-cell map is onto {C_F, C_P} while Step 7 allows Omega in {0,1}; reconcile, it is not onto when one cell is empty; (3) note that M_P being defined rests on (S8) pinning a version of the price, since (S4) states Borel regularity for Voice paths only; (4) S = |d_kappa Delta_act| is the noise sensitivity of the expected engagement premium, not of a price; say so where both weight-leg proofs say price; (5) prop:factorisation Step 5 speaks of differentiability in a policy coordinate, but T is an integer; drop that phrase; (6) eq:flagged-MF cites the partition result stated later in the file; pin it to the elementary definition of conditioning on a positive-probability event so the appendix reads in order; (7) the closing sentence of lem:threshold-weight is circular; the intended reading is the ceiling C_tau <= 1/W_tau. ";
p04 += "Edit nothing else. Return status PASS, summary of what changed, files_changed, evidence.";

let p02 = rules();
p02 += "STEP 02-nits. Read .scratch/v5-paper/grok/checkpoint-0.md Step 0. Edit only proofs/02_garbling.tex and write .scratch/v5-paper/runs/02-nits/result.txt. Wording only, no new claims. ";
p02 += "(i) At eq:g-kernel, state that the map h(nu) = h(pi(nu), v-hat(nu)) carries no kappa, since Lemma g3(a) rests on it. ";
p02 += "(ii) The proof of Theorem (B) says it used b_0 < tau'; it did not (c(tau') <= c(tau) follows from the set inclusion for any tau' < tau). Drop that sentence. ";
p02 += "Edit nothing else. Return status PASS, summary, files_changed, evidence.";

let p03 = rules();
p03 += "STEP 03-nits. Read .scratch/v5-paper/grok/checkpoint-0.md Step 0. Edit only proofs/03_caught.tex and write .scratch/v5-paper/runs/03-nits/result.txt. Wording only. ";
p03 += "(1) Hypothesis list (C-1) to (C-3) must name or cross-reference the standing conditions it consumes: the single-place entry of kappa (S11) for part (ii) and the pinned kernel version (S8) for part (iii). ";
p03 += "(2) The gloss near s_B and part (iii)'s the sensitivity of what it takes out currently read as tilde s_B. Say that s_B is the derivative of Lambda_T minus Lambda_T', which carries the survivors' re-pricing. ";
p03 += "(3) In part (vi)(b) share a sign reads s_A s_B > 0, since (a) owns s_B = 0. ";
p03 += "(4) Part (vi)(c) does not need phi > 0 to force a common sign; rho >= 1 > 0 suffices. ";
p03 += "(5) Add a half-sentence that (C-3)'s clause 0 < Omega(tau,T) is there so that the clock theorem applies. ";
p03 += "(6) Qualify the Reading paragraph's a cut that takes a small share of the pool faces only the first two requirements by the condition (vi)(e) states. ";
p03 += "Edit nothing else. Return status PASS, summary, files_changed, evidence.";

let step0 = parallel([
    #{ prompt: p04, label: "04-fix", capability_mode: "all", output_schema: result_schema },
    #{ prompt: p02, label: "02-nits", capability_mode: "all", output_schema: result_schema },
    #{ prompt: p03, label: "03-nits", capability_mode: "all", output_schema: result_schema },
]);

let r04 = step0[0];
let r02n = step0[1];
let r03n = step0[2];
let s04 = status_of(r04);
let s02 = status_of(r02n);
let s03n = status_of(r03n);
log("Step 0 statuses: 04-fix=" + s04 + " 02-nits=" + s02 + " 03-nits=" + s03n);

// ---------------------------------------------------------------------------
phase("Who gets caught grid");

let p_grid = rules();
p_grid += "STEP 03-grid. Read .scratch/v5-paper/issues/03-who-gets-caught.md in full, the Grid check paragraph, proofs/03_caught.tex (the corollary as committed, including s_B with survivors' re-pricing), and numerical_v4/checks/t5_who_gets_caught.py. ";
p_grid += "Edit only numerical_v4/checks/t5_who_gets_caught.py. The file exists from a killed run. Finish it against the ticket. It needs: a --nodes argument that limits the run to the first n calibration nodes; a provenance block (mark, H, params hash) in its JSON record; per node the two booleans (the corollary's condition holds; C_T at most one) and the two sensitivities s_A and s_B. ";
p_grid += "Rebuild the per-history, per-type mass matrix at mark 2 from the likelihood table and the alive MEASURE weights (not the market weights). Split the T = 10 pooled cell by the types the T = 5 clock newly flags. Use the point-derivative convention for S_P (4th-order central difference, step 1e-3, same as numerical_v4.premium.d_dkappa). ";
p_grid += "s_A is the point derivative of E[h | A] under the T = 10 pricing map. s_B is the corollary's object: d_kappa(Lambda_T - Lambda_T') / P(B), which carries survivors' re-pricing, not tilde s_B. The corollary's condition holds when s_B lies weakly between s_A and ((2-phi)/phi) s_A. C_T at most one is S_P(5)/S_P(10) from each clock's own pooled pass under the point-derivative convention. ";
p_grid += "Then run only: PYTHONPATH=. .venv/bin/python numerical_v4/checks/t5_who_gets_caught.py --nodes 1 ";
p_grid += "Paste the record it writes (numerical_v4/checks/t5_who_gets_caught.json) into evidence, at least provenance plus the one node. The full grid and the T1 comparison are not yours. ";
p_grid += "Write .scratch/v5-paper/runs/03-grid/result.txt. Return status PASS if the script is finished and --nodes 1 ran and wrote the record; FAIL if the run failed. files_changed includes the py file and the json record.";

let r_grid = agent(p_grid, #{
    label: "03-grid",
    capability_mode: "all",
    output_schema: result_schema,
});
let s_grid = status_of(r_grid);
log("03-grid status=" + s_grid);

// ---------------------------------------------------------------------------
phase("Existence write");

let p_write = rules();
p_write += "STEP 05-write. Read .scratch/v5-paper/issues/05-existence-if-clean.md in full, numerical_v4/checks/t5_existence_conditions.py, numerical_v4/solver.py (outer_map, solve_policy), numerical_v4/menu.py (breakpoints, a7_certificate), and the statement style of proofs/02_garbling.tex and proofs/04_inherited.tex. ";
p_write += "proofs/05_existence.tex does not exist. The check script exists from a killed run: a certified-box argument (an interior ordered box around the solver's candidate, single down-crossing of each adjacent-plan gap, a breakpoint-free Voice coordinate, Miranda face signs). Read it. Use it if the proof you write is the one it checks; rewrite it if not. The script must take --nodes and write a provenance block (mark, H, params hash). ";
p_write += "State and prove existence of an equilibrium of the two-round model at order size two under conditions a script can check at every calibration node. Statement first, in the paper's notation, into proofs/05_existence.tex. The model: two rounds, order size two (ADR 0003, docs/adr/0003-doubled-order-size-and-existence.md), menu Exit/Hold/Voice, ordered cutoff polytope Theta = {s_lo <= k1 <= k2 <= s_hi}, outer map T(k) the unique zeros of the two adjacent-plan payoff gaps at the prices k induces. ";
p_write += "A clean route matching the existing script: if a box B inside Theta is strictly interior and ordered (B1), its Voice coordinate contains no k-free breakpoint (B2), each adjacent-plan gap has a unique down-crossing at every k in B with ordered zeros (B3), and Miranda face signs hold for F(k) = T(k) - k (B4), and the inner pricing fixed point is unique on B, then T is a well-defined continuous self-map of B and Miranda's theorem supplies a zero, which is an equilibrium. State (B1)-(B4) as named conditions. The script verifies them on a stated 3x3 probe grid on B; say so. Do not claim the probe grid is a proof of (B3) at every point of B; the theorem is conditional on (B1)-(B4). ";
p_write += "If no proof under grid-checkable conditions is available, return ABSENT: write a one-paragraph note under Comments in ticket 05 (the only ticket edit allowed), write no proof file, skip running a long script. ";
p_write += "If you write the proof, run only: PYTHONPATH=. .venv/bin/python numerical_v4/checks/t5_existence_conditions.py --nodes 1 ";
p_write += "and paste the record into evidence. Allowed paths: proofs/05_existence.tex, numerical_v4/checks/t5_existence_conditions.py, numerical_v4/checks/t5_existence_conditions.json, the ticket Comments only if ABSENT, and .scratch/v5-paper/runs/05-write/result.txt. ";
p_write += "Return PASS if the proof is complete under its stated conditions and the script is written (the --nodes 1 run may FAIL the conditions; that is evidence, not a reason to drop the proof). Return ABSENT if no such proof is available. Return STOP only on a second failed attempt.";

let r_write = agent(p_write, #{
    label: "05-write",
    capability_mode: "all",
    output_schema: result_schema,
});
let s_write = status_of(r_write);
log("05-write status=" + s_write);

// ---------------------------------------------------------------------------
phase("Existence self-attack");

let s_attack = "SKIP";
let s_fix = "SKIP";

if s_write == "ABSENT" {
    log("05-write ABSENT: skip self-attack and fix");
} else if s_write == "STOP" {
    log("05-write STOP: skip self-attack and fix");
} else {
    let p_atk = "You are the self-attacker for ticket 05. You did not write the proof. You have no prior transcript. ";
    p_atk += "Workspace: /Users/austinli/Projects/blockholder_v5. Run no git. ";
    p_atk += "Read only these sources, with read_file, before judging: ";
    p_atk += "(1) the statement at the top of proofs/05_existence.tex and the whole proof; ";
    p_atk += "(2) CONTEXT.md; ";
    p_atk += "(3) .scratch/v5-paper/spec.md section 3 (The model, as the paper states it); ";
    p_atk += "(4) docs/adr/0003-doubled-order-size-and-existence.md; ";
    p_atk += "(5) the model section of inherited/draft_v3/draft_v3.tex, from Object and partition through Equilibrium notion and The cutoff polytope (around lines 308 to 530). ";
    p_atk += "Also read numerical_v4/solver.py outer_map and numerical_v4/checks/t5_existence_conditions.py so you know what the named conditions mean. ";
    p_atk += "Try to break the statement. Look for a missing hypothesis, a step that does not follow, a counterexample, a gap between a probe grid and a condition quantified over a whole box, an appeal to uniqueness or continuity that the model does not give. ";
    p_atk += "Where an inequality is doubted, recompute it at one calibration node with a short script using PYTHONPATH=. .venv/bin/python; do not lower H; run at most one evaluation. ";
    p_atk += "Write .scratch/v5-paper/runs/05-self-attack/result.txt as JSON {verdict, reasons}. verdict is PASS or FAIL. Do not edit the proof. Do not change any label. Your verdict is not the gate; Opus at checkpoint 1 is. ";
    p_atk += "Return verdict and reasons.";

    let r_atk = agent(p_atk, #{
        label: "05-self-attack",
        capability_mode: "all",
        output_schema: verdict_schema,
    });
    s_attack = verdict_of(r_atk);
    log("05-self-attack verdict=" + s_attack);

    if s_attack == "FAIL" {
        let p_fix = rules();
        p_fix += "STEP 05-fix. The self-attack returned FAIL. Read .scratch/v5-paper/runs/05-self-attack/result.txt and proofs/05_existence.tex. Fix once. One assumption may be replaced by a cleaner one; say so in the summary. ";
        p_fix += "Edit only proofs/05_existence.tex and, if the named conditions changed, numerical_v4/checks/t5_existence_conditions.py. If you change the script, run PYTHONPATH=. .venv/bin/python numerical_v4/checks/t5_existence_conditions.py --nodes 1 and no longer. ";
        p_fix += "Write .scratch/v5-paper/runs/05-fix/result.txt. Whatever you return, this step ends; no second self-attack. Return PASS, FAIL, ABSENT, or STOP.";
        let r_fix = agent(p_fix, #{
            label: "05-fix",
            capability_mode: "all",
            output_schema: result_schema,
        });
        s_fix = status_of(r_fix);
        log("05-fix status=" + s_fix);
    } else {
        log("05-self-attack did not FAIL: skip 05-fix");
    }
}

// ---------------------------------------------------------------------------
phase("E2 run");

let p_e2 = rules();
p_e2 += "STEP 08, the run. Read .scratch/v5-paper/issues/08-e2-run-and-link-audit.md and empirics/spec.md. ";
p_e2 += "Confirm the model direction note dated 2026-09-02 is present in empirics/spec.md. Do not use git to confirm it. Read the file. If that dated note is absent, write FAIL to .scratch/v5-paper/runs/08/result.txt and stop this step; do not run E2. ";
p_e2 += "If the note is present, run exactly: PYTHONPATH=. .venv/bin/python -m empirics.fingerprints run e2 ";
p_e2 += "It writes empirics/output/e2_estimate.json, e2_campaigns.csv, e2_runup_jump.pdf. ";
p_e2 += "Edit nothing outside empirics/output/ except .scratch/v5-paper/runs/08/result.txt. Do not edit empirics/spec.md. Do not repair a NO-GO. ";
p_e2 += "Report every gate value (E2-G1, E2-G3, E2-G4) exactly as the result file holds them, including the JSON key names and the verdict strings. A NO-GO is reported, not repaired. Status PASS if the command wrote the result file; FAIL if the command failed or the direction note was absent. ";
p_e2 += "Do not run the E2-G2 audit. That is the next step, a different agent.";

let r_e2 = agent(p_e2, #{
    label: "08",
    capability_mode: "all",
    output_schema: result_schema,
});
let s_e2 = status_of(r_e2);
log("08 E2 run status=" + s_e2);

// ---------------------------------------------------------------------------
phase("E2 audit");

let s_audit = "SKIP";
if s_e2 == "FAIL" {
    log("E2 run FAIL: skip 08-audit");
} else if s_e2 == "STOP" {
    log("E2 run STOP: skip 08-audit");
} else {
    let p_aud = "You are the E2 link auditor. You did not run E2. You have no prior transcript. ";
    p_aud += "Workspace: /Users/austinli/Projects/blockholder_v5. Run no git. Use PYTHONPATH=. .venv/bin/python. ";
    p_aud += "Read with read_file: empirics/spec.md gate E2-G2, empirics/output/e1_audit.csv (column names to mirror where they apply), empirics/output/e2_campaigns.csv, empirics/output/e2_estimate.json, empirics/fingerprints.py (link_campaign, CRSP_COLUMNS, e2_gates), and empirics/edgar_fetch.py fetch_filing_text. ";
    p_aud += "TASK. Draw sixty matched campaigns from empirics/output/e2_campaigns.csv (seed 5, stratified by year). Matched means the campaign has a CRSP PERMNO and valid R and J. Stratify by the calendar year of date_filed (or year column). Use random.Random(5).sample within each stratum after sorting by accession; allocate sixty rows across non-empty year strata as evenly as possible, leftover to earlier years in sorted order. ";
    p_aud += "For each drawn campaign compare the CRSP security identity with the filing's subject name. crsp_daily.csv has no issuer-name column; identify the CRSP security by PERMNO, Ticker, CUSIP, HdrCUSIP from empirics/data/crsp_daily.csv, and the SEC title from empirics/data/company_tickers.json via ticker or subject_cik. Read the filing from empirics/data/filings/<accession>.txt (or fetch_filing_text) and take the subject issuer name from the cover (NAME OF ISSUER) or XML issuerName / issuerTradingSymbol. A wrong match is when the filing's subject issuer is a different company than that CRSP ticker/CUSIP. ";
    p_aud += "Write empirics/output/e2_audit.csv with one row per campaign and the excerpt that supports each reading. Mirror e1_audit.csv columns where they apply, and add columns needed for this gate: accession, year, permno, ticker, crsp_cusip, crsp_title, filing_subject_name, match_ok, excerpt. ";
    p_aud += "Write gate E2-G2 into empirics/output/e2_estimate.json under gates.E2-G2_link_audit with PASS or NO-GO and the error count. Threshold: at most three wrong matches among the sixty. Keep every other key in e2_estimate.json unchanged. ";
    p_aud += "Edit only empirics/output/e2_audit.csv, empirics/output/e2_estimate.json, and .scratch/v5-paper/runs/08-audit/result.txt. ";
    p_aud += "Return status PASS if the audit file and the gate were written; FAIL otherwise. Put the error count and verdict in evidence.";

    let r_aud = agent(p_aud, #{
        label: "08-audit",
        capability_mode: "all",
        output_schema: result_schema,
    });
    s_audit = status_of(r_aud);
    log("08-audit status=" + s_audit);
}

// ---------------------------------------------------------------------------
phase("Batch result");

let batch_status = "PASS";
batch_status = mark_stop(batch_status, s04);
batch_status = mark_stop(batch_status, s02);
batch_status = mark_stop(batch_status, s03n);
batch_status = mark_stop(batch_status, s_grid);
batch_status = mark_stop(batch_status, s_write);
batch_status = mark_stop(batch_status, s_attack);
batch_status = mark_stop(batch_status, s_fix);
batch_status = mark_stop(batch_status, s_e2);
batch_status = mark_stop(batch_status, s_audit);

let steps_map = #{
    "04-fix": s04,
    "02-nits": s02,
    "03-nits": s03n,
    "03-grid": s_grid,
    "05-write": s_write,
    "05-self-attack": s_attack,
    "05-fix": s_fix,
    "08": s_e2,
    "08-audit": s_audit,
};

let p_close = rules();
p_close += "END OF BATCH 1. Write .scratch/v5-paper/runs/batch-1/result.txt as a single JSON object with keys status, steps, files_changed, summary. ";
p_close += "Use this status and these step statuses exactly, unless a result.txt on disk disagrees, in which case prefer the on-disk result.txt: ";
p_close += json_encode(#{ status: batch_status, steps: steps_map });
p_close += " Read every step result.txt under .scratch/v5-paper/runs/{04-fix,02-nits,03-nits,03-grid,05-write,05-self-attack,05-fix,08,08-audit}/result.txt that exists. Union their files_changed arrays, plus any numerical_v4/checks json the scripts wrote and empirics/output files. ";
p_close += "If 05-self-attack or 05-fix was skipped, write a result.txt for that label with status PASS and summary that the step was not required, so every listed step has a result file. Do not start batch 2. Do not run git. ";
p_close += "Return status equal to the batch status, files_changed the union, summary one paragraph.";

let r_close = agent(p_close, #{
    label: "batch-1-close",
    capability_mode: "all",
    output_schema: result_schema,
});
let s_close = status_of(r_close);
log("batch-1 close status=" + s_close);

let report = #{
    status: batch_status,
    steps: steps_map,
    close: s_close,
};
let path = write_scratch_file("batch-1-summary.json", json_encode(report));
complete(#{
    path: path,
    status: batch_status,
    steps: steps_map,
    summary: "Batch 1 finished with status " + batch_status,
});
