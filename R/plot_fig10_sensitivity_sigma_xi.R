# ============================================================================
# Figure 10: Sensitivity to Bidder Synergy Volatility sigma_xi
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))

plot_fig10 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "sensitivity_sigma_xi.csv"),
                 show_col_types = FALSE)

  plot_sensitivity(
    df, param_col = "sigma_xi",
    param_label = "$\\sigma_\\xi$",
    title = "Sensitivity to Bidder Heterogeneity $\\sigma_\\xi$",
    legend_fmt = function(v) sprintf("$\\sigma_\\xi = %.2f$", v),
    output_path = file.path(output_dir, "fig_sensitivity_sigma_xi.pdf")
  )
}

if (sys.nframe() == 0) plot_fig10()
