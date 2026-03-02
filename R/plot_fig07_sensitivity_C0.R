# ============================================================================
# Figure 7: Sensitivity to Engagement Cost C0
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))

plot_fig07 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "sensitivity_C0.csv"),
                 show_col_types = FALSE)

  plot_sensitivity(
    df, param_col = "C0",
    param_label = "$C_0$",
    title = "Sensitivity to Engagement Cost $C_0$",
    legend_fmt = function(v) sprintf("$C_0 = %.2f$", v),
    output_path = file.path(output_dir, "fig_sensitivity_C0.pdf")
  )
}

if (sys.nframe() == 0) plot_fig07()
