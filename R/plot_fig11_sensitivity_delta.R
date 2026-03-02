# ============================================================================
# Figure 11: Sensitivity to Discount Factor delta
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))

plot_fig11 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "sensitivity_delta.csv"),
                 show_col_types = FALSE)

  plot_sensitivity(
    df, param_col = "delta",
    param_label = "$\\delta$",
    title = "Sensitivity to Discount Factor $\\delta$",
    legend_fmt = function(v) sprintf("$\\delta = %.2f$", v),
    output_path = file.path(output_dir, "fig_sensitivity_delta.pdf")
  )
}

if (sys.nframe() == 0) plot_fig11()
