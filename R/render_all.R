# ============================================================================
# render_all.R -- Master script: generate all ggplot2 figures from CSV data
#
# Usage:  Rscript R/render_all.R [--data-dir DIR] [--output-dir DIR]
# ============================================================================

# Ensure working directory is project root (for here::here to work)
if (!requireNamespace("here", quietly = TRUE)) {
  stop("Package 'here' is required. Install with: install.packages('here')")
}

cat("=== EVT Model: Generating all R/ggplot2 figures ===\n\n")

# Parse optional arguments
args <- commandArgs(trailingOnly = TRUE)
data_dir   <- here::here("numerical_output", "data")
output_dir <- here::here("numerical_output")

for (i in seq_along(args)) {
  if (args[i] == "--data-dir" && i < length(args)) {
    data_dir <- args[i + 1]
  }
  if (args[i] == "--output-dir" && i < length(args)) {
    output_dir <- args[i + 1]
  }
}

cat("  Data dir:   ", data_dir, "\n")
cat("  Output dir: ", output_dir, "\n\n")

# Source and run each figure script
scripts <- c(
  "plot_fig01_cutoff_structure.R",
  "plot_fig02_nonmonotonicity.R",
  "plot_fig03_decomposition.R",
  "plot_fig04_prices.R",
  "plot_fig05_cutoffs_kappa.R",
  "plot_fig06_disclosure.R",
  "plot_fig07_sensitivity_C0.R",
  "plot_fig08_sensitivity_wedge.R",
  "plot_fig09_sensitivity_rho.R",
  "plot_fig10_sensitivity_sigma_xi.R",
  "plot_fig11_sensitivity_delta.R",
  "plot_fig12_noisy_rumor.R",
  "plot_fig13_welfare.R"
)

for (script in scripts) {
  cat("Running ", script, "...\n")
  tryCatch({
    source(here::here("R", script), local = TRUE)
    # Call the plot function (naming convention: plot_figXX)
    # Extract "plot_fig01" from "plot_fig01_cutoff_structure.R"
    fn_name <- sub("^(plot_fig\\d+)_.*\\.R$", "\\1", script)
    fn <- get(fn_name, envir = environment())
    fn(data_dir = data_dir, output_dir = output_dir)
  }, error = function(e) {
    cat("  ERROR in ", script, ": ", conditionMessage(e), "\n")
  })
}

cat("\n=== All figures generated ===\n")
