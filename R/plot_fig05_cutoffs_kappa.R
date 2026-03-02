# ============================================================================
# Figure 5: Equilibrium Cutoffs vs. Liquidity
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))

plot_fig05 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "baseline_series.csv"),
                 show_col_types = FALSE)

  # Detect if k0 == k1 throughout
  k0_equals_k1 <- max(abs(df$k0 - df$k1), na.rm = TRUE) < 1e-3

  # Read baseline mu for reference line
  params <- read_csv(file.path(data_dir, "baseline_params.csv"),
                     show_col_types = FALSE)
  mu <- as.numeric(params$value[params$param == "mu"])

  # Reshape for plotting
  if (k0_equals_k1) {
    df_long <- bind_rows(
      data.frame(kappa = df$kappa, cutoff = df$k1,
                 series = "k1=k0 (Exit/Quiet)"),
      data.frame(kappa = df$kappa, cutoff = df$kD,
                 series = "kD (Quiet/Public)")
    )
    series_order <- c("k1=k0 (Exit/Quiet)", "kD (Quiet/Public)")
    col_vals <- c(COL_EXIT, COL_QUIET)
    lt_vals  <- c("solid", "dotdash")
    sh_vals  <- c(16, 17)
  } else {
    df_long <- bind_rows(
      data.frame(kappa = df$kappa, cutoff = df$k1,
                 series = "k1 (Exit/Hold)"),
      data.frame(kappa = df$kappa, cutoff = df$k0,
                 series = "k0 (Hold/Quiet)"),
      data.frame(kappa = df$kappa, cutoff = df$kD,
                 series = "kD (Quiet/Public)")
    )
    series_order <- c("k1 (Exit/Hold)", "k0 (Hold/Quiet)", "kD (Quiet/Public)")
    col_vals <- c(COL_EXIT, COL_HOLD, COL_QUIET)
    lt_vals  <- c("solid", "dashed", "dotdash")
    sh_vals  <- c(16, 15, 17)
  }

  df_long$series <- factor(df_long$series, levels = series_order)

  # Build label expressions
  if (k0_equals_k1) {
    lab_vals <- c(
      TeX("$k_1 = k_0$ (Exit/Quiet)"),
      TeX("$k_D$ (Quiet/Public)")
    )
  } else {
    lab_vals <- c(
      TeX("$k_1$ (Exit/Hold)"),
      TeX("$k_0$ (Hold/Quiet)"),
      TeX("$k_D$ (Quiet/Public)")
    )
  }
  names(col_vals) <- series_order
  names(lt_vals)  <- series_order
  names(sh_vals)  <- series_order
  names(lab_vals) <- series_order

  p <- ggplot(df_long, aes(x = kappa, y = cutoff,
                            colour = series, linetype = series,
                            shape = series)) +
    geom_line(linewidth = 0.9) +
    geom_point(size = 1.8) +
    geom_hline(yintercept = mu, colour = "gray", linetype = "dotted",
               linewidth = 0.5) +
    annotate("text", x = max(df$kappa) - 0.02, y = mu + 0.03,
             label = TeX("$\\mu$"), colour = "gray", size = 4,
             family = "serif") +
    scale_colour_manual(values = col_vals, labels = lab_vals) +
    scale_linetype_manual(values = lt_vals, labels = lab_vals) +
    scale_shape_manual(values = sh_vals, labels = lab_vals) +
    labs(
      x = TeX("Liquidity $\\kappa$"),
      y = "Signal Cutoff",
      title = "Equilibrium Cutoffs vs. Liquidity"
    ) +
    theme_evt() +
    theme(legend.position = "right")

  save_figure(p, file.path(output_dir, "fig_cutoffs_kappa.pdf"))
  p
}

if (sys.nframe() == 0) plot_fig05()
