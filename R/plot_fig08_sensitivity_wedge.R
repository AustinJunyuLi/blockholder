# ============================================================================
# Figure 8: Sensitivity to Premium Wedge (m1 - m0)
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))

plot_fig08 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "sensitivity_wedge.csv"),
                 show_col_types = FALSE)

  plot_sensitivity(
    df, param_col = "wedge",
    param_label = "$m_1 - m_0$",
    title = "Sensitivity to Premium Wedge $(m_1 - m_0)$",
    legend_fmt = function(v) sprintf("$m_1 - m_0 = %.2f$", v),
    output_path = file.path(output_dir, "fig_sensitivity_wedge.pdf")
  )
}

if (sys.nframe() == 0) plot_fig08()
