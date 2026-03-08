# Supporting Files

## Makefile
Build pipeline: Python → CSV → R → PDF.

```makefile
# ============================================================================
# Makefile for Exit-Voice-Takeover model figures
#
# Pipeline: Python (model) → CSV data → R/ggplot2 → PDF figures
#
# Usage:
#   make all       -- run full pipeline (data + figures)
#   make data      -- export model computations to CSV
#   make figures   -- generate ggplot2 figures from CSV
#   make clean     -- remove generated CSVs and PDFs
# ============================================================================

DATA_DIR    := numerical_output/data
OUTPUT_DIR  := numerical_output

# CSV files produced by Python export
CSVS := $(DATA_DIR)/baseline_params.csv \
        $(DATA_DIR)/baseline_cutoffs.csv \
        $(DATA_DIR)/cutoff_regions.csv \
        $(DATA_DIR)/baseline_series.csv \
        $(DATA_DIR)/prices.csv \
        $(DATA_DIR)/disclosure_attenuation.csv \
        $(DATA_DIR)/sensitivity_C0.csv \
        $(DATA_DIR)/sensitivity_wedge.csv \
        $(DATA_DIR)/sensitivity_rho.csv \
        $(DATA_DIR)/sensitivity_sigma_xi.csv \
        $(DATA_DIR)/sensitivity_delta.csv \
        $(DATA_DIR)/noisy_rumor.csv \
        $(DATA_DIR)/welfare.csv

# PDF figures produced by R
PDFS := $(OUTPUT_DIR)/fig_cutoff_structure.pdf \
        $(OUTPUT_DIR)/fig_nonmonotone.pdf \
        $(OUTPUT_DIR)/fig_decomposition.pdf \
        $(OUTPUT_DIR)/fig_prices.pdf \
        $(OUTPUT_DIR)/fig_cutoffs_kappa.pdf \
        $(OUTPUT_DIR)/fig_disclosure.pdf \
        $(OUTPUT_DIR)/fig_sensitivity_C0.pdf \
        $(OUTPUT_DIR)/fig_sensitivity_wedge.pdf \
        $(OUTPUT_DIR)/fig_sensitivity_rho.pdf \
        $(OUTPUT_DIR)/fig_sensitivity_sigma_xi.pdf \
        $(OUTPUT_DIR)/fig_sensitivity_delta.pdf \
        $(OUTPUT_DIR)/fig_noisy_rumor_precision.pdf \
        $(OUTPUT_DIR)/fig_welfare.pdf

.PHONY: all data figures clean

all: data figures

# Step 1: Python computation → CSV
data: $(CSVS)

$(CSVS): numerical/export_data.py numerical/model.py numerical/solver.py numerical/params.py
	python -m numerical.export_data --output-dir $(OUTPUT_DIR)

# Step 2: R/ggplot2 visualization → PDF
figures: $(PDFS)

$(PDFS): $(CSVS) R/theme_evtmodel.R R/render_all.R $(wildcard R/plot_fig*.R)
	Rscript R/render_all.R --data-dir $(DATA_DIR) --output-dir $(OUTPUT_DIR)

clean:
	rm -f $(CSVS)
	rm -f $(PDFS)
	rm -f $(OUTPUT_DIR)/table_example.tex $(OUTPUT_DIR)/table_disclosure_extensions.tex
```

## numerical/export_data.py
Interface between Python model and R visualization. Sweeps parameter grids and writes CSVs.

```python
"""
Data export for the Exit-Voice-Takeover model.

Extracts computation logic from figures.py and writes CSV files
for downstream R/ggplot2 visualization. No matplotlib dependency.

Usage:
    python -m numerical.export_data [--output-dir DIR]
"""

from __future__ import annotations

import csv
import os
from typing import Dict, List, Optional, Tuple

import numpy as np

from numerical.params import (
    Cutoffs,
    ModelParams,
    TOL_PROB,
    TOL_REGION,
    TOL_RESIDUAL,
)
from numerical.model import (
    bid_probability,
    compute_action_probabilities,
    compute_conditional_means,
    compute_equilibrium_prices,
    compute_minority_gains,
    compute_minority_gains_no_disclosure_given_strategy,
    compute_minority_gains_noisy_rumor,
    compute_posteriors,
    compute_posteriors_full_information,
    compute_posteriors_no_disclosure,
    compute_posteriors_noisy_rumor,
    compute_welfare,
    noise_probs,
    compute_E_v_given_XD,
)
from numerical.solver import (
    compute_series_over_kappa,
    solve_equilibrium,
    solve_valid,
)

def _write_csv(path: str, header: List[str], rows: List[List]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

def _fmt(x: float, decimals: int = 10) -> str:
    if x is None or (isinstance(x, float) and (np.isnan(x) or not np.isfinite(x))):
        return "NA"
    return f"{x:.{decimals}f}"

def export_baseline_params(params: ModelParams, data_dir: str) -> None:
    rows = [
        ["mu", _fmt(params.mu)],
        ["sigma_v", _fmt(params.sigma_v)],
        ["sigma_eps", _fmt(params.sigma_eps)],
        ["sigma_s", _fmt(params.sigma_s)],
        ["kappa", _fmt(params.kappa)],
        ["C0", _fmt(params.C0)],
        ["chi", _fmt(params.chi)],
        ["rho", _fmt(params.rho)],
        ["Delta", _fmt(params.Delta)],
        ["m0", _fmt(params.m0)],
        ["m1", _fmt(params.m1)],
        ["m_tilde", _fmt(params.m_tilde)],
        ["S_bar", _fmt(params.S_bar)],
        ["Delta_S", _fmt(params.Delta_S)],
        ["K", _fmt(params.K)],
        ["s_xi", _fmt(params.s_xi)],
        ["lambda_B", _fmt(params.lambda_B)],
        ["delta", _fmt(params.delta)],
        ["beta", _fmt(params.beta)],
        ["Delta_tilde", _fmt(params.Delta_tilde)],
    ]
    _write_csv(os.path.join(data_dir, "baseline_params.csv"), ["param", "value"], rows)

def export_cutoff_structure(k1: float, k0: float, kD: float, params: ModelParams, data_dir: str) -> None:
    _write_csv(
        os.path.join(data_dir, "baseline_cutoffs.csv"),
        ["k1", "k0", "kD", "mu", "sigma_s"],
        [[_fmt(k1), _fmt(k0), _fmt(kD), _fmt(params.mu), _fmt(params.sigma_s)]],
    )
    x_min = params.mu - 3 * params.sigma_s
    x_max = max(params.mu + 4 * params.sigma_s, kD + 0.5 * params.sigma_s)
    has_hold = (k0 - k1) > TOL_REGION
    regions: List[List[str]] = [["Exit", _fmt(x_min), _fmt(k1)]]
    quiet_left = k0 if has_hold else k1
    if has_hold: regions.append(["Hold", _fmt(k1), _fmt(k0)])
    regions.append(["Quiet Voice", _fmt(quiet_left), _fmt(kD)])
    regions.append(["Public Voice", _fmt(kD), _fmt(x_max)])
    _write_csv(os.path.join(data_dir, "cutoff_regions.csv"), ["region", "xmin", "xmax"], regions)

def export_baseline_series(params: ModelParams, data_dir: str, n_points: int = 35) -> Dict[str, np.ndarray]:
    kappa_values = np.linspace(0.15, 0.85, n_points)
    series = compute_series_over_kappa(params, kappa_values, include_no_disclosure=False)
    rows = [[_fmt(float(series[k][i])) for k in ["kappa", "k1", "k0", "kD", "Delta_min", "base", "act"]] for i in range(len(kappa_values))]
    _write_csv(os.path.join(data_dir, "baseline_series.csv"), ["kappa", "k1", "k0", "kD", "Delta_min", "base", "act"], rows)
    return series

def export_prices(k1: float, k0: float, kD: float, params: ModelParams, data_dir: str) -> None:
    prices, prices_trade, E_v_dict = compute_equilibrium_prices(k1, k0, kD, params)
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    posteriors = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    p0, p1 = noise_probs(params.kappa)

    prob_XD: Dict[Tuple[int, int], float] = {}
    actions = [("E", -1, 0, omega_E), ("H", 0, 0, omega_H), ("Q", 0, 0, omega_Q), ("P", 1, 1, omega_P)]
    for _name, q, D, omega in actions:
        if omega < TOL_PROB: continue
        for z, pz in [(-1, p1), (0, p0), (1, p1)]:
            prob_XD[(q + z, D)] = prob_XD.get((q + z, D), 0.0) + float(omega) * float(pz)

    rows = []
    for X in [-2, -1, 0, 1]:
        on_path = prob_XD.get((X, 0), 0.0) > 1e-4
        P = prices.get((X, 0), float("nan"))
        P_tr = prices_trade.get(X, float("nan"))
        pi = posteriors.get((X, 0), 0.0)
        V_hat_XD = E_v_dict.get((X, 0), params.mu) + params.Delta_tilde * pi
        m_XD = params.m0 + (params.m_tilde - params.m0) * pi
        p_bid = params.lambda_B * bid_probability(V_hat_XD, m_XD, pi, params) if np.isfinite(P) else float("nan")
        rows.append([str(X), "0", _fmt(P), _fmt(P_tr), _fmt(pi), _fmt(p_bid), _fmt(m_XD), "TRUE" if on_path else "FALSE"])

    for X in [0, 1, 2]:
        on_path = prob_XD.get((X, 1), 0.0) > 1e-4
        P = prices.get((X, 1), float("nan"))
        P_tr = prices_trade.get(X, float("nan"))
        pi = 1.0
        V_hat_XD = E_v_dict.get((X, 1), params.mu) + params.Delta_tilde * pi
        m_XD = params.m_tilde
        p_bid = params.lambda_B * bid_probability(V_hat_XD, m_XD, pi, params) if np.isfinite(P) else float("nan")
        rows.append([str(X), "1", _fmt(P), _fmt(P_tr), _fmt(pi), _fmt(p_bid), _fmt(m_XD), "TRUE" if on_path else "FALSE"])

    _write_csv(os.path.join(data_dir, "prices.csv"), ["X", "D", "P_post", "P_trade", "pi", "p_bid", "m_XD", "on_path"], rows)

def export_disclosure_attenuation(base_params: ModelParams, k1_ref: float, k0_ref: float, kD_ref: float, data_dir: str, n_points: int = 35) -> None:
    kappa_values = np.linspace(0.15, 0.85, n_points)
    rows = []
    for kappa in kappa_values:
        params_k = base_params.replace(kappa=float(kappa))
        _, _, act_k = compute_minority_gains(k1_ref, k0_ref, kD_ref, params_k)
        _, _, act_nd_k = compute_minority_gains_no_disclosure_given_strategy(k1_ref, k0_ref, kD_ref, params_k)
        rows.append([_fmt(float(kappa)), _fmt(act_k), _fmt(act_nd_k)])
    _write_csv(os.path.join(data_dir, "disclosure_attenuation.csv"), ["kappa", "act_disclosure", "act_no_disclosure"], rows)

def _export_sensitivity(base_params, param_name, param_values, param_field, data_dir, csv_name, replace_fn=None):
    kappa_values = np.linspace(0.25, 0.85, 21)
    rows = []
    for pval in param_values:
        prev = None
        for kappa in kappa_values:
            try:
                p = replace_fn(base_params, float(kappa), pval) if replace_fn else base_params.replace(kappa=float(kappa), **{param_field: pval})
                cutoffs, res = solve_valid(p, prev)
                if cutoffs is None or not np.isfinite(res) or res > TOL_RESIDUAL:
                    rows.append([_fmt(float(kappa)), _fmt(pval), "NA"])
                    prev = None
                    continue
                prev = cutoffs
                total, _, _ = compute_minority_gains(cutoffs.k1, cutoffs.k0, cutoffs.kD, p)
                rows.append([_fmt(float(kappa)), _fmt(pval), _fmt(total)])
            except Exception:
                rows.append([_fmt(float(kappa)), _fmt(pval), "NA"])
    _write_csv(os.path.join(data_dir, csv_name), ["kappa", param_name, "Delta_min"], rows)

def export_sensitivity_C0(base_params: ModelParams, data_dir: str): _export_sensitivity(base_params, "C0", [0.06, 0.12, 0.21, 0.24], "C0", data_dir, "sensitivity_C0.csv")
def export_sensitivity_wedge(base_params: ModelParams, data_dir: str): _export_sensitivity(base_params, "wedge", [0.10, 0.20, 0.30], "m1", data_dir, "sensitivity_wedge.csv", replace_fn=lambda bp, k, w: bp.replace(kappa=k, m1=bp.m0 + w))
def export_sensitivity_rho(base_params: ModelParams, data_dir: str): _export_sensitivity(base_params, "rho", [0.5, 0.7, 0.9], "rho", data_dir, "sensitivity_rho.csv")
def export_sensitivity_s_xi(base_params: ModelParams, data_dir: str): _export_sensitivity(base_params, "s_xi", [0.10, 0.15, 0.25], "s_xi", data_dir, "sensitivity_s_xi.csv")
def export_sensitivity_delta(base_params: ModelParams, data_dir: str): _export_sensitivity(base_params, "delta", [0.85, 0.90, 0.95], "delta", data_dir, "sensitivity_delta.csv")

def export_noisy_rumor(base_params: ModelParams, data_dir: str) -> None:
    kappa_values = np.linspace(0.25, 0.85, 21)
    rumor_configs = [(0.50, 0.50, "Uninformative"), (0.75, 0.25, "Moderate"), (0.95, 0.05, "Precise")]
    rows = []
    for eta_1, eta_0, label in rumor_configs:
        prev = None
        for kappa in kappa_values:
            try:
                p = base_params.replace(kappa=float(kappa))
                cutoffs, res = solve_valid(p, prev)
                if cutoffs is None or not np.isfinite(res) or res > TOL_RESIDUAL:
                    rows.append([_fmt(float(kappa)), _fmt(eta_1), _fmt(eta_0), label, "NA"])
                    prev = None
                    continue
                prev = cutoffs
                gains = compute_minority_gains_noisy_rumor(cutoffs.k1, cutoffs.k0, cutoffs.kD, p, eta_1, eta_0)
                rows.append([_fmt(float(kappa)), _fmt(eta_1), _fmt(eta_0), label, _fmt(gains.total)])
            except Exception:
                rows.append([_fmt(float(kappa)), _fmt(eta_1), _fmt(eta_0), label, "NA"])
    _write_csv(os.path.join(data_dir, "noisy_rumor.csv"), ["kappa", "eta_1", "eta_0", "label", "Delta_min"], rows)

def export_welfare(base_params: ModelParams, data_dir: str) -> None:
    kappa_values = np.linspace(0.25, 0.85, 21)
    rows, prev = [], None
    for kappa in kappa_values:
        try:
            p = base_params.replace(kappa=float(kappa))
            cutoffs, res = solve_valid(p, prev)
            if cutoffs is None or not np.isfinite(res) or res > TOL_RESIDUAL:
                rows.append([_fmt(float(kappa)), "NA", "NA", "NA"])
                prev = None
                continue
            prev = cutoffs
            W_min, W_bid, _, W_tot = compute_welfare(cutoffs.k1, cutoffs.k0, cutoffs.kD, p)
            rows.append([_fmt(float(kappa)), _fmt(W_min), _fmt(W_bid), _fmt(W_tot)])
        except Exception:
            rows.append([_fmt(float(kappa)), "NA", "NA", "NA"])
    _write_csv(os.path.join(data_dir, "welfare.csv"), ["kappa", "W_min", "W_bid", "W_tot"], rows)


def write_baseline_table(k1: float, k0: float, kD: float, params: ModelParams, output_path: str) -> None:
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    posteriors = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    prices, _prices_trade, E_v_dict = compute_equilibrium_prices(k1, k0, kD, params)

    def row_for(X: int, D: int) -> str:
        P = prices.get((X, D), np.nan)
        pi = posteriors.get((X, D), 0.0)
        V_hat_XD = E_v_dict.get((X, D), params.mu) + params.Delta_tilde * pi
        m_XD = params.m0 + (params.m_tilde - params.m0) * pi
        p_bid = params.lambda_B * bid_probability(V_hat_XD, m_XD, pi, params) if np.isfinite(P) else np.nan
        return f"{D} & ${X}$ & {P:.2f} & {pi:.2f} & {p_bid:.2f} & {m_XD:.2f} \\\\"

    lines = ["\\begin{tabular}{llrrrr}", "\\toprule", "$D$ & Order flow $X$ & $P(X,D)$ & $\\pi(X,D)$ & $p(X,D)$ & $m(X,D)$ \\\\", "\\midrule"]
    for X in [-2, -1, 0, 1]: lines.append(row_for(X, 0))
    lines.append("\\midrule")
    for X in [0, 1, 2]: lines.append(row_for(X, 1))
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    with open(output_path, "w", encoding="utf-8") as f: f.write("\n".join(lines) + "\n")

def write_disclosure_extension_table(k1, k0, kD, params, output_path, rho1=0.75, rho0=0.25):
    omega_E, omega_H, omega_Q, omega_P = compute_action_probabilities(k1, k0, kD, params)
    post_baseline = compute_posteriors(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    post_nd = compute_posteriors_no_disclosure(omega_E, omega_H, omega_Q, omega_P, params.kappa)
    post_nr = compute_posteriors_noisy_rumor(omega_E, omega_H, omega_Q, omega_P, params.kappa, rho1, rho0)
    post_fi = compute_posteriors_full_information()
    fmt = lambda x: f"{x:.2f}"
    
    lines = ["\\begin{tabular}{lrrrr}", "\\toprule", "$X$ & $\\pi(X,0)$ & $\\pi_{\\textup{ND}}(X)$ & $\\pi_{\\textup{NR}}(X,0,R=0)$ & $\\pi_{\\textup{NR}}(X,0,R=1)$ \\\\", "\\midrule"]
    for X in [-1, 0, 1]:
        lines.append(f"${X}$ & {fmt(post_baseline.get((X, 0), 0.0))} & {fmt(post_nd.get(X, 0.0))} & {fmt(post_nr.get((X, 0, 0), 0.0))} & {fmt(post_nr.get((X, 0, 1), 0.0))} \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}", "\\vspace{0.6em}", "\\begin{tabular}{ll}", "\\toprule", "$(q,a)$ & $\\pi_{\\textup{FI}}$ \\\\", "\\midrule"])
    for key in [(-1, 0), (0, 0), (0, 1), (1, 1)]: lines.append(f"$({key[0]},{key[1]})$ & {fmt(post_fi.get(key, 0.0))} \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    with open(output_path, "w", encoding="utf-8") as f: f.write("\n".join(lines) + "\n")

def export_all(output_dir: str = "numerical_output") -> None:
    data_dir = os.path.join(output_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    params = ModelParams()
    print("Solving baseline equilibrium...")
    k1, k0, kD = solve_equilibrium(params)
    print(f"Equilibrium cutoffs: k1={k1:.3f}, k0={k0:.3f}, kD={kD:.3f}")
    print(f"Net deterrence holds: {params.net_deterrence_active}")
    
    export_baseline_params(params, data_dir)
    export_cutoff_structure(k1, k0, kD, params, data_dir)
    export_baseline_series(params, data_dir)
    export_prices(k1, k0, kD, params, data_dir)
    export_disclosure_attenuation(params, k1, k0, kD, data_dir)
    export_sensitivity_C0(params, data_dir)
    export_sensitivity_wedge(params, data_dir)
    export_sensitivity_rho(params, data_dir)
    export_sensitivity_s_xi(params, data_dir)
    export_sensitivity_delta(params, data_dir)
    export_noisy_rumor(params, data_dir)
    export_welfare(params, data_dir)

    write_baseline_table(k1, k0, kD, params, os.path.join(output_dir, "table_example.tex"))
    write_disclosure_extension_table(k1, k0, kD, params, os.path.join(output_dir, "table_disclosure_extensions.tex"))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Export model data to CSV")
    parser.add_argument("--output-dir", default="numerical_output", help="Output directory")
    args = parser.parse_args()
    export_all(output_dir=args.output_dir)
```

## bibliography.bib
Manuscript bibliography (24 entries). Key references for this round:
- EdmansGoldsteinJiang2015: Precedent for numerical uniqueness verification
- Kyle1985: Standard microstructure intuition (more noise → more informed trading rents)
- Maug1998: Liquidity helps governance
- Coffee1991, Bhide1993: Liquidity hurts governance

```bibtex
% =============================================================================
% bibliography.bib
% =============================================================================
% Bibliography for the unified exit-voice-takeover model
% =============================================================================

% =============================================================================
% FOUNDATIONAL EXIT-VOICE THEORY
% =============================================================================

@book{Hirschman1970,
  author    = {Hirschman, Albert O.},
  title     = {Exit, Voice, and Loyalty: Responses to Decline in Firms, Organizations, and States},
  publisher = {Harvard University Press},
  year      = {1970},
  address   = {Cambridge, MA}
}

@article{Coffee1991,
  author  = {Coffee, John C.},
  title   = {Liquidity Versus Control: The Institutional Investor as Corporate Monitor},
  journal = {Columbia Law Review},
  year    = {1991},
  volume  = {91},
  number  = {6},
  pages   = {1277--1368}
}

@article{Bhide1993,
  author  = {Bhide, Amar},
  title   = {The Hidden Costs of Stock Market Liquidity},
  journal = {Journal of Financial Economics},
  year    = {1993},
  volume  = {34},
  number  = {1},
  pages   = {31--51}
}

@article{Maug1998,
  author  = {Maug, Ernst},
  title   = {Large Shareholders as Monitors: Is There a Trade-Off Between Liquidity and Control?},
  journal = {Journal of Finance},
  year    = {1998},
  volume  = {53},
  number  = {1},
  pages   = {65--98}
}

@article{Edmans2009,
  author  = {Edmans, Alex},
  title   = {Blockholder Trading, Market Efficiency, and Managerial Myopia},
  journal = {Journal of Finance},
  year    = {2009},
  volume  = {64},
  number  = {6},
  pages   = {2481--2513}
}

@article{EdmansManso2011,
  author  = {Edmans, Alex and Manso, Gustavo},
  title   = {Governance Through Trading and Intervention: A Theory of Multiple Blockholders},
  journal = {Review of Financial Studies},
  year    = {2011},
  volume  = {24},
  number  = {7},
  pages   = {2395--2428}
}

@article{EdmansFangZur2013,
  author  = {Edmans, Alex and Fang, Vivian W. and Zur, Emanuel},
  title   = {The Effect of Liquidity on Governance},
  journal = {Review of Financial Studies},
  year    = {2013},
  volume  = {26},
  number  = {6},
  pages   = {1443--1482}
}

% =============================================================================
% MARKET MICROSTRUCTURE
% =============================================================================

@article{Kyle1985,
  author  = {Kyle, Albert S.},
  title   = {Continuous Auctions and Insider Trading},
  journal = {Econometrica},
  year    = {1985},
  volume  = {53},
  number  = {6},
  pages   = {1315--1335}
}

@article{GlostenMilgrom1985,
  author  = {Glosten, Lawrence R. and Milgrom, Paul R.},
  title   = {Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders},
  journal = {Journal of Financial Economics},
  year    = {1985},
  volume  = {14},
  number  = {1},
  pages   = {71--100}
}

@article{EdmansGoldsteinJiang2015,
  author  = {Edmans, Alex and Goldstein, Itay and Jiang, Wei},
  title   = {Feedback Effects, Asymmetric Trading, and the Limits to Arbitrage},
  journal = {American Economic Review},
  year    = {2015},
  volume  = {105},
  number  = {12},
  pages   = {3766--3797}
}

% =============================================================================
% SHAREHOLDER ACTIVISM AND INTERVENTION
% =============================================================================

@article{BravJiangPartnoyThomas2008,
  author  = {Brav, Alon and Jiang, Wei and Partnoy, Frank and Thomas, Randall},
  title   = {Hedge Fund Activism, Corporate Governance, and Firm Performance},
  journal = {Journal of Finance},
  year    = {2008},
  volume  = {63},
  number  = {4},
  pages   = {1729--1775}
}

@article{GreenwoodSchor2009,
  author  = {Greenwood, Robin and Schor, Michael},
  title   = {Investor Activism and Takeovers},
  journal = {Journal of Financial Economics},
  year    = {2009},
  volume  = {92},
  number  = {3},
  pages   = {362--375}
}

@article{BackEtAl2018,
  author  = {Back, Kerry and Collin-Dufresne, Pierre and Fos, Vyacheslav and Li, Tao and Ljungqvist, Alexander},
  title   = {Activism, Strategic Trading, and Liquidity},
  journal = {Econometrica},
  year    = {2018},
  volume  = {86},
  number  = {4},
  pages   = {1431--1463}
}

@article{BravDasguptaMathews2022,
  author  = {Brav, Alon and Dasgupta, Amil and Mathews, Richmond},
  title   = {Wolf Pack Activism},
  journal = {Management Science},
  year    = {2022},
  volume  = {68},
  number  = {8},
  pages   = {5557--5568}
}

% =============================================================================
% TAKEOVERS AND CORPORATE CONTROL
% =============================================================================

@article{GrossmanHart1980,
  author  = {Grossman, Sanford J. and Hart, Oliver D.},
  title   = {Takeover Bids, the Free-Rider Problem, and the Theory of the Corporation},
  journal = {Bell Journal of Economics},
  year    = {1980},
  volume  = {11},
  number  = {1},
  pages   = {42--64}
}

@article{Fishman1988,
  author  = {Fishman, Michael J.},
  title   = {A Theory of Preemptive Takeover Bidding},
  journal = {RAND Journal of Economics},
  year    = {1988},
  volume  = {19},
  number  = {1},
  pages   = {88--101}
}

@article{BulowHuangKlemperer1999,
  author  = {Bulow, Jeremy and Huang, Ming and Klemperer, Paul},
  title   = {Toeholds and Takeovers},
  journal = {Journal of Political Economy},
  year    = {1999},
  volume  = {107},
  number  = {3},
  pages   = {427--454}
}

@article{EdmansGoldsteinJiang2012,
  author  = {Edmans, Alex and Goldstein, Itay and Jiang, Wei},
  title   = {The Real Effects of Financial Markets: The Impact of Prices on Takeovers},
  journal = {Journal of Finance},
  year    = {2012},
  volume  = {67},
  number  = {3},
  pages   = {933--971}
}

% =============================================================================
% INFORMATION ACQUISITION AND FEEDBACK
% =============================================================================

@article{BondEdmansGoldstein2012,
  author  = {Bond, Philip and Edmans, Alex and Goldstein, Itay},
  title   = {The Real Effects of Financial Markets},
  journal = {Annual Review of Financial Economics},
  year    = {2012},
  volume  = {4},
  pages   = {339--360}
}

@article{DowGoldsteinGuembel2017,
  author  = {Dow, James and Goldstein, Itay and Guembel, Alexander},
  title   = {Incentives for Information Production in Markets where Prices Affect Real Investment},
  journal = {Journal of the European Economic Association},
  year    = {2017},
  volume  = {15},
  number  = {4},
  pages   = {877--909}
}

% =============================================================================
% MEDIA AND INFORMATION
% =============================================================================

@article{FangPeress2009,
  author  = {Fang, Lily and Peress, Joel},
  title   = {Media Coverage and the Cross-Section of Stock Returns},
  journal = {Journal of Finance},
  year    = {2009},
  volume  = {64},
  number  = {5},
  pages   = {2023--2052}
}

% =============================================================================
% ASSET PRICING AND DISCOUNTING
% =============================================================================

@book{Cochrane2005,
  author    = {Cochrane, John H.},
  title     = {Asset Pricing},
  publisher = {Princeton University Press},
  year      = {2005},
  edition   = {Revised},
  address   = {Princeton, NJ}
}

@book{Duffie2010,
  author    = {Duffie, Darrell},
  title     = {Dynamic Asset Pricing Theory},
  publisher = {Princeton University Press},
  year      = {2010},
  edition   = {3rd},
  address   = {Princeton, NJ}
}

% =============================================================================
% ECONOMETRIC METHODS
% =============================================================================

@article{LindMehlum2010,
  author  = {Lind, Jo Thori and Mehlum, Halvor},
  title   = {With or Without U? The Appropriate Test for a U-Shaped Relationship},
  journal = {Oxford Bulletin of Economics and Statistics},
  year    = {2010},
  volume  = {72},
  number  = {1},
  pages   = {109--118}
}
```
