# ============================================================================
# Figure 12: Disclosure Attenuation via Noisy Rumors
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))

plot_fig12 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "noisy_rumor.csv"),
                 show_col_types = FALSE)

  # Build display labels: "Uninformative (eta_1=0.50, eta_0=0.50)"
  label_order <- c("Uninformative", "Moderate", "Precise")
  df$label <- factor(df$label, levels = label_order)

  # Build legend labels with TeX
  legend_labels <- setNames(
    sapply(label_order, function(lab) {
      row <- df[df$label == lab, ][1, ]
      TeX(sprintf("%s ($\\eta_1=%.2f, \\eta_0=%.2f$)",
                  lab, row$eta_1, row$eta_0))
    }),
    label_order
  )

  n_vals <- length(label_order)
  colors <- setNames(SENS_COLORS[seq_len(n_vals)], label_order)
  ltypes <- setNames(SENS_LINETYPES[seq_len(n_vals)], label_order)
  shapes <- setNames(SENS_SHAPES[seq_len(n_vals)], label_order)

  p <- ggplot(df, aes(x = kappa, y = Delta_min,
                       colour = label, linetype = label,
                       shape = label)) +
    geom_line(linewidth = 0.9) +
    geom_point(size = 1.8) +
    scale_colour_manual(values = colors, labels = legend_labels) +
    scale_linetype_manual(values = ltypes, labels = legend_labels) +
    scale_shape_manual(values = shapes, labels = legend_labels) +
    labs(
      x = TeX("Liquidity $\\kappa$"),
      y = TeX("Expected Minority Takeover Gains $\\Delta^{\\mathrm{min}}$"),
      title = "Disclosure Attenuation via Noisy Rumors"
    ) +
    theme_evt() +
    theme(legend.position = "right")

  save_figure(p, file.path(output_dir, "fig_noisy_rumor_precision.pdf"))
  p
}

if (sys.nframe() == 0) plot_fig12()
