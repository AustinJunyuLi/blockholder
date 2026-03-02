# ============================================================================
# Figure 6: Disclosure Attenuation through the Inference Channel
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))

plot_fig06 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "disclosure_attenuation.csv"),
                 show_col_types = FALSE)

  p <- ggplot(df, aes(x = kappa)) +
    geom_line(aes(y = act_disclosure), colour = "#4477aa",
              linewidth = 0.9, linetype = "solid") +
    geom_point(aes(y = act_disclosure), colour = "#4477aa",
               shape = 16, size = 1.5) +
    geom_line(aes(y = act_no_disclosure), colour = "#ee6677",
              linewidth = 0.9, linetype = "dashed") +
    geom_point(aes(y = act_no_disclosure), colour = "#ee6677",
               shape = 15, size = 1.5) +
    # Manual legend
    annotate("segment", x = 0.60, xend = 0.65, y = max(df$act_no_disclosure) * 0.98,
             yend = max(df$act_no_disclosure) * 0.98,
             colour = "#4477aa", linewidth = 0.7) +
    annotate("text", x = 0.66, y = max(df$act_no_disclosure) * 0.98,
             label = "Threshold disclosure (baseline)",
             hjust = 0, size = 3, family = "serif") +
    annotate("segment", x = 0.60, xend = 0.65, y = max(df$act_no_disclosure) * 0.92,
             yend = max(df$act_no_disclosure) * 0.92,
             colour = "#ee6677", linewidth = 0.7, linetype = "dashed") +
    annotate("text", x = 0.66, y = max(df$act_no_disclosure) * 0.92,
             label = "No disclosure (counterfactual)",
             hjust = 0, size = 3, family = "serif") +
    labs(
      x = TeX("Liquidity $\\kappa$"),
      y = TeX("Activism-Driven Minority Gains $\\Delta^{\\mathrm{act}}$"),
      title = "Disclosure Attenuation of Liquidity Sensitivity"
    ) +
    theme_evt()

  save_figure(p, file.path(output_dir, "fig_disclosure.pdf"))
  p
}

if (sys.nframe() == 0) plot_fig06()
