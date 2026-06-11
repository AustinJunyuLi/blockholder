# ============================================================================
# Makefile for Exit-Voice-Takeover model figures
#
# Pipeline (Python end-to-end): Python (model) -> CSV data -> matplotlib -> PDF
#
# Usage:
#   make venv      -- create .venv and install Python dependencies
#   make all       -- run full pipeline (data + figures)
#   make data      -- export model computations to CSV
#   make figures   -- generate matplotlib figures from CSV
#   make clean     -- remove generated CSVs, PDFs, and LaTeX tables
#
# Override the interpreter with e.g.  make PYTHON=python3 all
# ============================================================================

PYTHON     ?= .venv/bin/python
DATA_DIR   := numerical_output/data
OUTPUT_DIR := numerical_output

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
        $(DATA_DIR)/welfare.csv \
        $(DATA_DIR)/ge_decomposition.csv \
        $(DATA_DIR)/ge_cellmap.csv \
        $(DATA_DIR)/wedge_primitives.csv

# PDF figures produced by pyfig (matplotlib)
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
        $(OUTPUT_DIR)/fig_welfare.pdf \
        $(OUTPUT_DIR)/fig_ge_decomposition.pdf \
        $(OUTPUT_DIR)/fig_wedge_primitives.pdf

# Slide-only figure variants (Beamer deck + PPTX build)
SLIDE_DIR  := pres/figures
SLIDE_PDFS := $(SLIDE_DIR)/fig_disclosure_slopes.pdf \
              $(SLIDE_DIR)/fig_sensitivity_panel1.pdf \
              $(SLIDE_DIR)/fig_sensitivity_panel2.pdf \
              $(SLIDE_DIR)/fig_noisy_rumor.pdf

.PHONY: all data figures venv clean

all: data figures

# Create the project virtual environment with all scientific dependencies
venv:
	python3 -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/python -m pip install -r requirements.txt

# Step 1: Python computation -> CSV
data: $(CSVS)

$(CSVS): numerical/export_data.py numerical/model.py numerical/solver.py numerical/params.py numerical/takeover_game.py
	$(PYTHON) -m numerical.export_data --output-dir $(OUTPUT_DIR)

# Step 2: matplotlib visualization -> PDF
figures: $(PDFS) $(SLIDE_PDFS)

$(PDFS): $(CSVS) pyfig/style.py pyfig/figures.py pyfig/render_all.py
	$(PYTHON) -m pyfig.render_all --data-dir $(DATA_DIR) --output-dir $(OUTPUT_DIR)

$(SLIDE_PDFS): $(CSVS) pyfig/style.py pyfig/slide_figures.py
	$(PYTHON) -m pyfig.slide_figures --data-dir $(DATA_DIR) --output-dir $(SLIDE_DIR)

clean:
	rm -f $(CSVS)
	rm -f $(PDFS)
	rm -f $(SLIDE_PDFS)
	rm -f $(OUTPUT_DIR)/table_example.tex $(OUTPUT_DIR)/table_disclosure_extensions.tex
