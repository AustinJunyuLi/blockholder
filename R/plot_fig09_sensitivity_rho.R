# ============================================================================
# Figure 9: Sensitivity to Engagement Success Probability rho
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))

plot_fig09 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "sensitivity_rho.csv"),
                 show_col_types = FALSE)

  plot_sensitivity(
    df, param_col = "rho",
    param_label = "$\\rho$",
    title = "Sensitivity to Engagement Success $\\rho$",
    legend_fmt = function(v) sprintf("$\\rho = %.1f$", v),
    output_path = file.path(output_dir, "fig_sensitivity_rho.pdf")
  )
}

if (sys.nframe() == 0) plot_fig09()
