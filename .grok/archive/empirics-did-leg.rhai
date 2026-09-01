let meta = #{
    name: "empirics-did-leg",
    description: "Finish BID12, option-2 recovery, matched DiD, and bidder-entry on branch v4",
    when_to_use: "Continue the v4 empirical DiD leg after the treated post-pass chain",
    phases: [
        #{ title: "Wait for treated chain", detail: "confirm chain complete without touching protected PIDs" },
        #{ title: "BID12 gates", detail: "run bid12_gates and stop on any failure" },
        #{ title: "Recall check", detail: "run and adjudicate the 20-firm recall sample" },
        #{ title: "Treated audit", detail: "fresh auditor, then adjudicate the treated half" },
        #{ title: "Option-2 recovery", detail: "13F CUSIP to CIK recovery with validation gate" },
        #{ title: "Match and estimate", detail: "matching, control lookup, DiD, then review" },
        #{ title: "Bidder entry and diagnostics", detail: "section 9, then 8.7 and 8.8" },
    ],
};

let status_schema = #{
    "type": "object",
    "required": ["ok", "summary", "blocker"],
    "properties": #{
        "ok": #{ "type": "boolean" },
        "summary": #{ "type": "string" },
        "blocker": #{ "type": "string" },
    },
};

let chain_schema = #{
    "type": "object",
    "required": ["complete", "failed", "summary"],
    "properties": #{
        "complete": #{ "type": "boolean" },
        "failed": #{ "type": "boolean" },
        "summary": #{ "type": "string" },
    },
};

let review_schema = #{
    "type": "object",
    "required": ["ok_to_commit", "findings", "worst"],
    "properties": #{
        "ok_to_commit": #{ "type": "boolean" },
        "findings": #{ "type": "string" },
        "worst": #{ "type": "string" },
    },
};

fn constraints() {
    let s = "Workspace: /Users/austinli/Projects/blockholder_v4 on branch v4. ";
    s += "Use .venv/bin/python for every Python command. ";
    s += "Do not kill or restart PIDs 29378, 79276, or 52774. ";
    s += "Keep at most two SEC-fetch lanes at once. ";
    s += "Never git push. Commits must name explicit paths; no git add -A. ";
    s += "Do not edit research/empirics_v4/bid12_coding_rules.md until empirics/output/bid12_run_meta.json exists from the chain lookup. ";
    s += "Do not edit the frozen SPEC. Realised numbers go in dated notes under research/empirics_v4/ and the session log. ";
    s += "Preserve ESTIMATED labels, standard errors, realised MDEs, and the SPEC section 6 three-rung ladder. ";
    s += "Keep and update in place the three documentation files: quality_reports/session_logs/2026-08-30_did-leg.md, research/empirics_v4/link_map_nan_ticker_2026-08-30.md, research/empirics_v4/bid12_status_2026-08-30.md. ";
    s += "Read treated progress only with the snippet that loads bid12.load_treated_universe and counts that universe's event caches. Never count events/*.json, because treated and control share that directory. ";
    s += "If both extractor CPU is zero and find empirics/data/bid12_cache -type f -mmin -1 is zero, inspect /tmp/sec_edgar_bulk.lock before anything else. rmdir an orphan only after confirming no live holder. ";
    s += "Prose in notes, session-log entries, and commit messages must be plain and specific: no em dashes, no AI filler, no puffery. ";
    s += "S2 corporate-action coding does not exist; S1 is primary; do not invent an S2 sample. ";
    s += "Ambiguous-only BID12 rows stay empty with ambiguous=1; correct any status-note sentence that still says they are coded 0. ";
    s
}

fn stop_if_bad(result, phase_name) {
    if result == () || result.success != true {
        complete(#{ summary: "agent failed", phase: phase_name, ok: false });
    }
    if result.output.ok != true {
        let blocker = result.output.blocker;
        if blocker == () { blocker = result.output.summary; }
        complete(#{
            summary: "stopped",
            phase: phase_name,
            ok: false,
            blocker: blocker,
            detail: result.output.summary,
        });
    }
}

let chain_already = false;
if args != () {
    if args.chain_complete == true { chain_already = true; }
}

phase("Wait for treated chain");
if !chain_already {
    let probe_p = constraints();
    probe_p += "Check whether the treated post-pass chain has finished. Read /tmp/bid12_postpass_chain.log and test whether /tmp/bid12_chain_failed.marker exists. ";
    probe_p += "Confirm PIDs 29378, 79276, and 52774 with ps; do not kill them. ";
    probe_p += "Set complete=true only if the log contains the exact line prefix == chain complete and the failure marker is absent. ";
    probe_p += "Set failed=true if the marker exists. Use tools; do not guess. ";
    let probe = agent(probe_p, #{
        label: "probe-chain",
        capability_mode: "read-only",
        output_schema: chain_schema,
    });
    if probe != () && probe.success && probe.output.complete == true && probe.output.failed != true {
        chain_already = true;
        log("treated chain already complete");
    }
}
if !chain_already {
    await_user("back_off", "Resume when /tmp/bid12_postpass_chain.log contains == chain complete == and /tmp/bid12_chain_failed.marker is absent. Do not kill PIDs 29378, 79276, or 52774.");
}

phase("BID12 gates");
let gates_p = constraints();
gates_p += "Run: .venv/bin/python -m empirics.bid12_gates --json empirics/output/bid12_gates.json ";
gates_p += "from the repo root. Every gate must pass. ";
gates_p += "If the treated BID12 base rate is at or below 18.1 percent, stop and investigate before any downstream step; do not note it and continue. ";
gates_p += "If bid12_run_meta.json is still missing, the chain has not actually finished; report that as a blocker. ";
gates_p += "Do not edit bid12_coding_rules.md. Append a short dated entry to quality_reports/session_logs/2026-08-30_did-leg.md with the gate counts. ";
gates_p += "Set ok=true only if the gates command exited 0 and the JSON all_passed field is true. ";
let gates = agent(gates_p, #{
    label: "bid12-gates",
    capability_mode: "all",
    output_schema: status_schema,
});
stop_if_bad(gates, "BID12 gates");

phase("Recall check");
let recall_p = constraints();
recall_p += "Confirm at most one other SEC-fetch lane is live (PID 79276 may still be extracting controls). ";
recall_p += "Then run: .venv/bin/python -m empirics.bid12_recall_check ";
recall_p += "Hand-adjudicate every potential miss into research/empirics_v4/bid12_status_2026-08-30.md section 7. ";
recall_p += "Fill PENDING treated-side numbers in that status note from bid12_run_meta.json and the treated CSVs. ";
recall_p += "Correct the section 6 sentence if it still says an ambiguous-only row is coded BID12=0; the rulebook leaves that value empty with ambiguous=1. Do not change the rulebook. ";
recall_p += "Commit the treated unit with explicit paths only, including the status note, session log, gate JSON if present, and the treated BID12 outputs that the chain wrote. Never push. ";
recall_p += "Set ok=true only after adjudication is written and the treated-unit commit has landed, or after you have written why a commit is blocked. ";
let recall = agent(recall_p, #{
    label: "recall-check",
    capability_mode: "all",
    output_schema: status_schema,
});
stop_if_bad(recall, "Recall check");

phase("Treated audit");
let sample_p = constraints();
sample_p += "Draw the treated half of the blind audit: .venv/bin/python -m empirics.bid12_audit_sample --side treated ";
sample_p += "Confirm empirics/output/bid12_audit_pairs.csv carries no coder verdicts and bid12_audit_key.csv exists separately. ";
sample_p += "Do not open the key for the auditor. Do not start the auditor yourself. Set ok=true only if the pairs file and manifest exist. ";
let sampled = agent(sample_p, #{
    label: "audit-sample-treated",
    capability_mode: "all",
    output_schema: status_schema,
});
stop_if_bad(sampled, "Treated audit sample");

let auditor_p = "";
auditor_p += "You are the BID12 blind auditor. You did not write the coder. ";
auditor_p += "Workspace: /Users/austinli/Projects/blockholder_v4. Use .venv/bin/python only if you must fetch a truncated document. ";
auditor_p += "Read ONLY: research/empirics_v4/bid12_audit_protocol.md, research/empirics_v4/bid12_coding_rules.md including section 5.1, and empirics/output/bid12_audit_pairs.csv. ";
auditor_p += "Verify the rulebook SHA-256 against empirics/output/bid12_audit_manifest.json. ";
auditor_p += "Do not read empirics/bid12.py, empirics/output/bid12_treated.csv, bid12_events_treated.csv, bid12_control.csv, bid12_ambiguous_cases.csv, bid12_run_meta.json, or empirics/data/bid12_cache/events/. ";
auditor_p += "Raw caches under submissions, texts, headers, fts, and fts_pages are allowed. If a cached text or header looks truncated at the deciding point, re-fetch from EDGAR rather than reading the truncation. ";
auditor_p += "Keep at most two SEC-fetch lanes; PID 79276 may still hold one. Do not kill PIDs 29378, 79276, or 52774. ";
auditor_p += "For every pair, re-derive BID12 from raw EDGAR under the rulebook: window [TD, TD+365] inclusive on filing date; originals only of the registered forms; 8-K Item 1.01/2.01 is a candidate, apply the section 5 table top to bottom; SC TO-T/C need header SUBJECT COMPANY CIK verification; a bid strictly before TD is excluded_prior_bid, a bid on TD is BID12=1; ambiguous is permitted and never forced to 0 or 1. ";
auditor_p += "Watch for loan/credit Item 1.01 8-Ks and acquirer-side 8-Ks. ";
auditor_p += "Write empirics/output/bid12_audit_readings.csv BEFORE anyone shows you the key, with columns cik, td, bid12 (1, 0, or ambiguous), first_event_accession, first_event_date, rulebook_row, reason. ";
auditor_p += "Set ok=true only after that readings file is on disk with one row per sampled pair. Do not open the key. ";
let auditor = agent(auditor_p, #{
    label: "blind-auditor-treated",
    capability_mode: "all",
    output_schema: status_schema,
});
stop_if_bad(auditor, "Treated audit readings");

let adj_p = constraints();
adj_p += "The treated-half readings are at empirics/output/bid12_audit_readings.csv. Only now open empirics/output/bid12_audit_key.csv. ";
adj_p += "Count disagreements per bid12_audit_protocol.md section 4. Three or more treated-half disagreements require immediate escalation; four of the full 30 blocks the leg. Do not rescale a 15-pair result into a new threshold. ";
adj_p += "Write every disagreement individually into research/empirics_v4/bid12_audit_result_2026-08-30.md. The coder is probably right is not an adjudication. ";
adj_p += "Do not commit the adjudication until the following review panel has run; leave the result note on disk. ";
adj_p += "Set ok=true if the treated half is below the 3-disagreement escalation, or ok=false with the count if it escalates. ";
let adjudicate = agent(adj_p, #{
    label: "audit-adjudicate-treated",
    capability_mode: "all",
    output_schema: status_schema,
});
if adjudicate == () || adjudicate.success != true || adjudicate.output.ok != true {
    let blocker = "treated-half audit blocked or escalated";
    if adjudicate != () && adjudicate.output.summary != () {
        blocker = adjudicate.output.summary;
    }
    complete(#{ summary: "audit stop", phase: "Treated audit", ok: false, blocker: blocker });
}

let audit_std = agent("Review the uncommitted audit result note and sampler/output changes in /Users/austinli/Projects/blockholder_v4 since HEAD. Use git diff and read the files. Standards axis: repo AGENTS.md, empirics stdlib-only pipeline, no SPEC edits, no rulebook edits before run_meta stamp, explicit git paths. Also apply the smell baseline: Mysterious Name, Duplicated Code, Feature Envy, Data Clumps, Primitive Obsession, Repeated Switches, Shotgun Surgery, Divergent Change, Speculative Generality, Message Chains, Middle Man, Refused Bequest; smells are judgement calls and repo standards win. Report ok_to_commit=false if a documented-standard breach would make the adjudication untrustworthy.", #{
    label: "review-audit-standards",
    capability_mode: "read-only",
    output_schema: review_schema,
});
let audit_spec = agent("Review the treated-half BID12 audit adjudication in /Users/austinli/Projects/blockholder_v4 against research/empirics_v4/bid12_audit_protocol.md and bid12_coding_rules.md section 10. Confirm readings were written before the key, forbidden files were not required for the writeup, disagreement counting follows the protocol, and the result note writes each disagreement individually. Set ok_to_commit=false if the procedure was violated.", #{
    label: "review-audit-spec",
    capability_mode: "read-only",
    output_schema: review_schema,
});
if audit_std == () || audit_std.success != true || audit_std.output.ok_to_commit != true {
    complete(#{ summary: "audit standards review blocked commit", ok: false });
}
if audit_spec == () || audit_spec.success != true || audit_spec.output.ok_to_commit != true {
    complete(#{ summary: "audit spec review blocked commit", ok: false });
}

let audit_commit_p = constraints();
audit_commit_p += "Commit the treated-half audit artefacts and research/empirics_v4/bid12_audit_result_2026-08-30.md with explicit paths. Never push. Update the session log. Set ok=true after the commit. ";
let audit_commit = agent(audit_commit_p, #{
    label: "commit-treated-audit",
    capability_mode: "all",
    output_schema: status_schema,
});
stop_if_bad(audit_commit, "Treated audit commit");

phase("Option-2 recovery");
let rec_p = constraints();
rec_p += "Austin selected option 2 as primary: Geode 13F CUSIP to nameOfIssuer to CIK, with a validation gate. Option 1 is the fallback. Option 3 is not selected. ";
rec_p += "Do not fetch while two SEC lanes are busy. Recovery fetches wait for a free lane; local parsing is safe. PID 79276 may still be the control extractor. ";
rec_p += "Code already exists: empirics/recover_delisted_controls.py and empirics/test_recover_delisted_controls.py. Keep it the smallest reproducible route. Run .venv/bin/python -m empirics.test_recover_delisted_controls first. ";
rec_p += "Then run .venv/bin/python -m empirics.recover_delisted_controls once a lane is free. Do not pass --fetch-bid12 until PID 79276 has exited, so the recovered-CIK extract does not make a third SEC lane. ";
rec_p += "No recovered CIK may enter matching until its validation result is in empirics/output/delisted_control_cik_recovery.csv. Hold ambiguous names and failed validation out of the map. ";
rec_p += "Write a dated recovery result/gate under research/empirics_v4/. If n_validated is 0 or the pass cannot complete, record option 1 explicitly, count unresolved delisted controls, and sign the survivorship bias: control bid rate down, gamma up. ";
rec_p += "Update the link note and session log. Set ok=true only after the recovery CSV, meta JSON, and dated note exist. ";
let recovery = agent(rec_p, #{
    label: "option2-recovery",
    capability_mode: "all",
    output_schema: status_schema,
});
stop_if_bad(recovery, "Option-2 recovery");

phase("Match and estimate");
let match_p = constraints();
match_p += "Do not match against a partial control pool. Wait until PID 79276 has exited before matching if that process is still filling the control event cache needed for lookup, and wait until recovery has updated permno_cik_map.csv or option 1 is recorded. ";
match_p += "If recovery validated CIKs, run .venv/bin/python -m empirics.recover_delisted_controls --fetch-bid12 only after a SEC lane is free (control extractor gone, or treated chain gone and only one other lane live). ";
match_p += "Then run in order: .venv/bin/python -m empirics.estimate_did --stage match ; .venv/bin/python -m empirics.bid12_control_lookup ; .venv/bin/python -m empirics.estimate_did --stage estimate ";
match_p += "Report cell-level 3:1 shortfalls and standardised differences. If balance stays above 0.10 after the predeclared 0.20 caliper, that is a design failure, not an estimate. ";
match_p += "The estimate may be computed before the control-half audit; it may not be quoted as a result. Keep the ESTIMATED label, SEs, realised MDE, and the section 6 ladder in the JSON. ";
match_p += "Do not commit estimate scripts or outputs until the review panel. Set ok=true when did_estimate.json exists or a recorded design failure exists. ";
let matched = agent(match_p, #{
    label: "match-lookup-estimate",
    capability_mode: "all",
    output_schema: status_schema,
});
stop_if_bad(matched, "Match and estimate");

let est_std = agent("Review uncommitted estimate_did, bid12_control_lookup, recovery, and related tests in /Users/austinli/Projects/blockholder_v4 against AGENTS.md and empirics conventions. Use git diff HEAD. Flag documented-standard breaches. Smell baseline is judgement-only. Set ok_to_commit=false on a hard standards breach in the estimate path.", #{
    label: "review-estimate-standards",
    capability_mode: "read-only",
    output_schema: review_schema,
});
let est_spec = agent("Review the matched DiD implementation and outputs in /Users/austinli/Projects/blockholder_v4 against research/empirics_v4/SPEC.md sections 6, 8, and 10. Confirm 3:1 Mahalanobis matching with 0.25 pooled-sd calipers, exact SIC2, per-quarter no-replacement, pseudo-TD inheritance, LPM with match FE, two-way cluster plus wild bootstrap, ESTIMATED label, realised MDE, three-rung ladder, S2 unestimated because coding is absent, and no quoting of the DiD as a result before the control-half audit. Set ok_to_commit=false if a registered requirement is missing or wrong.", #{
    label: "review-estimate-spec",
    capability_mode: "read-only",
    output_schema: review_schema,
});
if est_std == () || est_std.success != true || est_std.output.ok_to_commit != true {
    complete(#{ summary: "estimate standards review blocked commit", ok: false });
}
if est_spec == () || est_spec.success != true || est_spec.output.ok_to_commit != true {
    complete(#{ summary: "estimate spec review blocked commit", ok: false });
}

let est_commit_p = constraints();
est_commit_p += "Commit estimate scripts, tests, recovery route, dated notes, and estimate outputs with explicit paths. Never push. Do not quote the DiD as a result in the session log; record it as computed, pending the control-half audit. Set ok=true after the commit. ";
let est_commit = agent(est_commit_p, #{
    label: "commit-estimate",
    capability_mode: "all",
    output_schema: status_schema,
});
stop_if_bad(est_commit, "Estimate commit");

phase("Bidder entry and diagnostics");
let rest_p = constraints();
rest_p += "Run section 9 then 8.7 and 8.8 in that order. ";
rest_p += ".venv/bin/python -m empirics.estimate_bidder_entry ";
rest_p += "then .venv/bin/python -m empirics.estimate_did_diagnostics ";
rest_p += "Do not invent a 568-date placebo estimate if the diagnostic blocks; write the blockers. Pre-trends may still be ESTIMATED while placebo is BLOCKED. ";
rest_p += "Keep ESTIMATED labels and realised MDEs. Quote tau against the section 9 rule of thumb. S2 remains unestimated. ";
rest_p += "If the control lookup exists, you may draw the control-half audit sample with the same seed, but the control-half auditor must still be a later fresh agent; do not audit it yourself if you have now seen coder outputs. ";
rest_p += "Update the session log. Commit explicit paths for bidder-entry and diagnostic outputs after tests you already have are green. Never push. Set ok=true when those scripts have run and the log is updated. ";
let rest = agent(rest_p, #{
    label: "bidder-entry-diagnostics",
    capability_mode: "all",
    output_schema: status_schema,
});
stop_if_bad(rest, "Bidder entry and diagnostics");

let report = "DID leg workflow finished. ";
report += "Gates: " + gates.output.summary + ". ";
report += "Recall: " + recall.output.summary + ". ";
report += "Audit: " + adjudicate.output.summary + ". ";
report += "Recovery: " + recovery.output.summary + ". ";
report += "Estimate: " + matched.output.summary + ". ";
report += "Rest: " + rest.output.summary + ".";
let path = write_scratch_file("did-leg-result.md", report);
complete(#{
    summary: report,
    path: path,
    ok: true,
});
