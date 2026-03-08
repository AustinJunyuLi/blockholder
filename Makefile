# ============================================================================
# Makefile for Exit-Voice-Takeover model figures
#
# Pipeline: Python (model) → CSV data → Python (matplotlib) → PDF figures
#
# Usage:
#   make all       -- run full pipeline (data + figures)
#   make data      -- export model computations to CSV
#   make figures   -- generate matplotlib figures from CSV
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

# PDF figures produced by Python/matplotlib
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
        $(OUTPUT_DIR)/fig_sensitivity_panel1.pdf \
        $(OUTPUT_DIR)/fig_sensitivity_panel2.pdf \
        $(OUTPUT_DIR)/fig_disclosure_slopes.pdf \
        $(OUTPUT_DIR)/fig_noisy_rumor_precision.pdf \
        $(OUTPUT_DIR)/fig_welfare.pdf \
        $(OUTPUT_DIR)/fig_timeline.pdf \
        $(OUTPUT_DIR)/fig_mechanism_chain.pdf

.PHONY: all data figures clean

all: data figures

# Step 1: Python computation → CSV
data: $(CSVS)

$(CSVS) &: numerical/export_data.py numerical/model.py numerical/solver.py numerical/params.py
	python -m numerical.export_data --output-dir $(OUTPUT_DIR)

# Step 2: Python/matplotlib visualization → PDF
figures: $(PDFS)
$(PDFS) &: $(CSVS) numerical/figures.py numerical/theme.py
	python -m numerical.figures --data-dir $(DATA_DIR) --output-dir $(OUTPUT_DIR)

clean:
	rm -f $(CSVS)
	rm -f $(PDFS)
	rm -f $(OUTPUT_DIR)/table_example.tex $(OUTPUT_DIR)/table_disclosure_extensions.tex
