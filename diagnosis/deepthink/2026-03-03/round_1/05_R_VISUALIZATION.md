# R Visualization Layer

All R source files for the ggplot2 figure pipeline.

## R/theme_evtmodel.R

```r
# ============================================================================
# theme_evtmodel.R -- Shared ggplot2 theme, palettes, and helpers
#
# Replicates the matplotlib style from figures.py for publication-quality
# figures using the Paul Tol colourblind-friendly muted palette.
# ============================================================================

library(ggplot2)
library(latex2exp)
library(scales)
library(dplyr)
library(readr)

# -- Robust TeX wrapper ------------------------------------------------------

# latex2exp sometimes renders \mathrm{...} literally ("mathrmin") when labels
# mix text and math. Sanitize common commands before parsing.
sanitize_tex <- function(label) {
  label <- gsub("\\\\mathrm\\{([^}]*)\\}", "\\1", label, perl = TRUE)
  label <- gsub("\\\\operatorname\\{([^}]*)\\}", "\\1", label, perl = TRUE)
  label
}

TeX <- function(x, output = "expression", ...) {
  latex2exp::TeX(sanitize_tex(x), output = output, ...)
}

# -- Colour palettes ---------------------------------------------------------

# Action colours (Paul Tol muted)
COL_EXIT   <- "#cc6677"   # muted rose
COL_HOLD   <- "#ddcc77"   # muted sand
COL_QUIET  <- "#88ccee"   # muted cyan
COL_PUBLIC <- "#44aa99"   # muted teal

ACTION_COLORS <- c(
  "Exit"         = COL_EXIT,
  "Hold"         = COL_HOLD,
  "Quiet Voice"  = COL_QUIET,
  "Public Voice" = COL_PUBLIC
)

# Sensitivity analysis palette
SENS_COLORS <- c("#4477aa", "#ee6677", "#228833", "#ccbb44")

# Named line types and shapes for sensitivity
SENS_LINETYPES <- c("solid", "dashed", "dotdash", "dotted")
SENS_SHAPES    <- c(16, 15, 17, 18)  # circle, square, triangle, diamond

# -- Custom ggplot2 theme ----------------------------------------------------

theme_evt <- function(base_size = 11) {
  theme_bw(base_size = base_size, base_family = "serif") %+replace%
    theme(
      # Clean white canvas for publication export.
      panel.background = element_rect(fill = "white", colour = NA),
      plot.background = element_rect(fill = "white", colour = NA),

      # Remove top and right spines (matching matplotlib)
      panel.border     = element_blank(),
      axis.line        = element_line(colour = "black", linewidth = 0.4),
      axis.line.x      = element_line(colour = "black", linewidth = 0.4),
      axis.line.y      = element_line(colour = "black", linewidth = 0.4),

      # Grid tuned for readability without dominating lines.
      panel.grid.major = element_line(colour = "grey88", linewidth = 0.25),
      panel.grid.minor = element_blank(),

      # Font sizes matching matplotlib rcParams
      axis.title       = element_text(size = rel(1.09)),   # 12/11
      axis.text        = element_text(size = rel(0.91)),   # 10/11
      plot.title       = element_text(size = rel(1.09), hjust = 0.5, face = "plain"),
      legend.text      = element_text(size = rel(0.91)),
      legend.title     = element_blank(),
      legend.background = element_rect(fill = alpha("white", 0.95),
                                       colour = "grey80", linewidth = 0.3),
      legend.key       = element_rect(fill = "white", colour = NA),

      # Tight layout
      plot.margin      = margin(5, 10, 5, 5)
    )
}

# -- Default figure dimensions ------------------------------------------------

FIG_WIDTH  <- 5.5
FIG_HEIGHT <- 3.8
FIG_DPI    <- 300

# -- Save helper --------------------------------------------------------------

save_figure <- function(plot, filename, width = FIG_WIDTH, height = FIG_HEIGHT,
                        dpi = FIG_DPI, device = cairo_pdf) {
  ggsave(filename, plot = plot, width = width, height = height,
         dpi = dpi, device = device, bg = "white")
  message("  Saved: ", filename)
}

# -- Sensitivity plot helper --------------------------------------------------

#' Plot sensitivity analysis: Delta_min vs kappa for multiple parameter values.
#'
#' @param df         Data frame with columns: kappa, <param_col>, Delta_min
#' @param param_col  Name of the parameter column (string)
#' @param param_label LaTeX label for the parameter (passed to TeX())
#' @param y_label    LaTeX label for the y-axis
#' @param title      Plot title (LaTeX or plain text)
#' @param legend_fmt Format function for legend labels (e.g., function(x) sprintf("$C_0 = %.2f$", x))
#' @param output_path File path for saving (optional)
#' @return ggplot object
plot_sensitivity <- function(df, param_col, param_label,
                             y_label = "Expected Minority Takeover Gains $\\Delta^{\\mathrm{min}}$",
                             title = NULL,
                             legend_fmt = NULL,
                             output_path = NULL) {

  # Ensure param_col is a factor for consistent styling
  param_vals <- sort(unique(df[[param_col]]))
  n_vals <- length(param_vals)
  df[[param_col]] <- factor(df[[param_col]], levels = param_vals)

  # Build legend labels
  if (is.null(legend_fmt)) {
    legend_labels <- setNames(
      sapply(param_vals, function(v) TeX(sprintf("%s = %s", param_label, v))),
      param_vals
    )
  } else {
    legend_labels <- setNames(
      sapply(param_vals, function(v) TeX(legend_fmt(v))),
      param_vals
    )
  }

  # Assign colours/linetypes/shapes
  colors <- setNames(SENS_COLORS[seq_len(n_vals)], param_vals)
  ltypes <- setNames(SENS_LINETYPES[seq_len(n_vals)], param_vals)
  shapes <- setNames(SENS_SHAPES[seq_len(n_vals)], param_vals)

  p <- ggplot(df, aes(x = kappa, y = Delta_min,
                       colour = .data[[param_col]],
                       linetype = .data[[param_col]],
                       shape = .data[[param_col]])) +
    geom_line(linewidth = 0.9) +
    geom_point(size = 1.8) +
    scale_colour_manual(values = colors, labels = legend_labels) +
    scale_linetype_manual(values = ltypes, labels = legend_labels) +
    scale_shape_manual(values = shapes, labels = legend_labels) +
    labs(
      x = TeX("Liquidity $\\kappa$"),
      y = TeX(y_label),
      title = if (!is.null(title)) TeX(title) else NULL
    ) +
    theme_evt() +
    theme(legend.position = "right")

  if (!is.null(output_path)) {
    save_figure(p, output_path)
  }

  p
}
```

## R/render_all.R

```r
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
```

## R/plot_fig01_cutoff_structure.R

```r
# ============================================================================
# Figure 1: Equilibrium Cutoff Structure on Number Line
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))
library(patchwork)

plot_fig01 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  # Read data
  cutoffs <- read_csv(file.path(data_dir, "baseline_cutoffs.csv"),
                      show_col_types = FALSE)
  regions <- read_csv(file.path(data_dir, "cutoff_regions.csv"),
                      show_col_types = FALSE)

  k1 <- cutoffs$k1
  k0 <- cutoffs$k0
  kD <- cutoffs$kD
  mu <- cutoffs$mu
  sigma_s <- cutoffs$sigma_s

  has_hold <- abs(k0 - k1) > 1e-4
  tol <- 1e-4

  # Main number-line plot
  p_main <- ggplot() +
    # Coloured regions
    geom_rect(data = regions,
              aes(xmin = xmin, xmax = xmax, ymin = -0.2, ymax = 0.2,
                  fill = region),
              alpha = 0.7) +
    scale_fill_manual(
      values = ACTION_COLORS,
      limits = c("Exit", "Hold", "Quiet Voice", "Public Voice"),
      breaks = regions$region
    ) +
    # Region labels (only for wide-enough regions)
    geom_text(data = regions %>% filter((xmax - xmin) >= 0.8),
              aes(x = (xmin + xmax) / 2, y = 0, label = region),
              size = 3, fontface = "bold", family = "serif") +
    # Cutoff lines
    geom_vline(xintercept = k1, linetype = "dashed", linewidth = 0.5, alpha = 0.9) +
    {if (has_hold) geom_vline(xintercept = k0, linetype = "dashed",
                               linewidth = 0.5, alpha = 0.9)} +
    geom_vline(xintercept = kD, linetype = "dashed", linewidth = 0.5, alpha = 0.9) +
    # Number line
    geom_hline(yintercept = -0.32, linewidth = 0.5, alpha = 0.8) +
    # Cutoff points on number line
    annotate("point", x = k1, y = -0.32, size = 2) +
    {if (has_hold) annotate("point", x = k0, y = -0.32, size = 2)} +
    annotate("point", x = kD, y = -0.32, size = 2) +
    # Cutoff labels
    annotate("text", x = k1, y = -0.42,
             label = TeX("$k_1$"), size = 4, family = "serif", vjust = 1) +
    {if (has_hold) {
      annotate("text", x = k0, y = -0.50,
               label = TeX("$k_0$"), size = 4, family = "serif", vjust = 1)
    } else {
      annotate("text", x = k1 + 0.05, y = -0.50,
               label = TeX("$k_1 = k_0$"), size = 3.5, family = "serif", vjust = 1)
    }} +
    annotate("text", x = kD, y = -0.42,
             label = TeX("$k_D$"), size = 4, family = "serif", vjust = 1) +
    # Mu marker
    geom_vline(xintercept = mu, colour = "gray", linetype = "dotted",
               linewidth = 0.5) +
    annotate("text", x = mu, y = 0.35,
             label = TeX("$\\mu$"), size = 4, colour = "gray",
             family = "serif", vjust = 0) +
    # Axes and theme
    labs(x = TeX("Signal $s$")) +
    coord_cartesian(ylim = c(-0.6, 0.5)) +
    theme_evt() +
    theme(
      axis.text.y  = element_blank(),
      axis.ticks.y = element_blank(),
      axis.title.y = element_blank(),
      axis.line.y  = element_blank(),
      legend.position = "top",
      legend.direction = "horizontal",
      legend.justification = "center"
    ) +
    guides(fill = guide_legend(nrow = 1, override.aes = list(alpha = 0.7)))

  # If k1 and k0 are very close but distinct, add a zoom inset
  if (has_hold && abs(k0 - k1) < 0.15) {
    pad <- max(0.08, 8 * abs(k0 - k1))
    zoom_xmin <- k1 - pad
    zoom_xmax <- k0 + pad

    p_zoom <- ggplot() +
      geom_rect(data = regions,
                aes(xmin = xmin, xmax = xmax, ymin = -0.2, ymax = 0.2,
                    fill = region),
                alpha = 0.7) +
      scale_fill_manual(values = ACTION_COLORS, guide = "none") +
      geom_vline(xintercept = k1, linetype = "dashed", linewidth = 0.5) +
      geom_vline(xintercept = k0, linetype = "dashed", linewidth = 0.5) +
      coord_cartesian(xlim = c(zoom_xmin, zoom_xmax),
                      ylim = c(-0.25, 0.25)) +
      theme_evt() +
      theme(
        axis.text  = element_blank(),
        axis.ticks = element_blank(),
        axis.title = element_blank(),
        axis.line  = element_blank(),
        panel.border = element_rect(fill = NA, colour = "grey40", linewidth = 0.5)
      )

    p_final <- p_main + inset_element(p_zoom, left = 0.02, bottom = 0.02,
                                       right = 0.35, top = 0.45)
  } else {
    p_final <- p_main
  }

  save_figure(p_final, file.path(output_dir, "fig_cutoff_structure.pdf"),
              width = 8, height = 2.5)

  p_final
}

# Run if sourced directly
if (sys.nframe() == 0) plot_fig01()
```

## R/plot_fig02_nonmonotonicity.R

```r
# ============================================================================
# Figure 2: Non-Monotonic Effect of Liquidity on Takeover Gains
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))

plot_fig02 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "baseline_series.csv"),
                 show_col_types = FALSE)

  # Find the peak (kappa-dagger)
  peak_idx <- which.max(df$Delta_min)
  kappa_peak <- df$kappa[peak_idx]

  p <- ggplot(df, aes(x = kappa, y = Delta_min)) +
    geom_line(colour = "#4477aa", linewidth = 1.0) +
    # Peak marker
    geom_vline(xintercept = kappa_peak, colour = "gray",
               linetype = "dashed", linewidth = 0.5, alpha = 0.7) +
    annotate("text", x = kappa_peak + 0.015,
             y = max(df$Delta_min, na.rm = TRUE) * 0.98,
             label = TeX("$\\kappa^{\\dagger}$"),
             size = 4, colour = "gray", family = "serif") +
    labs(
      x = TeX("Liquidity $\\kappa$"),
      y = TeX("Expected Minority Takeover Gains $\\Delta^{\\mathrm{min}}$"),
      title = "Non-Monotonic Effect of Liquidity on Takeover Gains"
    ) +
    theme_evt()

  save_figure(p, file.path(output_dir, "fig_nonmonotone.pdf"))
  p
}

if (sys.nframe() == 0) plot_fig02()
```

## R/plot_fig03_decomposition.R

```r
# ============================================================================
# Figure 3: Decomposition of Minority Takeover Gains
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))

plot_fig03 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "baseline_series.csv"),
                 show_col_types = FALSE)

  df$total <- df$base + df$act

  # Find the peak
  peak_idx <- which.max(df$total)
  kappa_peak <- df$kappa[peak_idx]

  p <- ggplot(df, aes(x = kappa)) +
    # Base component: cyan fill from 0
    geom_ribbon(aes(ymin = 0, ymax = base),
                fill = COL_QUIET, alpha = 0.5) +
    # Activism component: rose fill stacked
    geom_ribbon(aes(ymin = base, ymax = total),
                fill = COL_EXIT, alpha = 0.5) +
    # Total line on top
    geom_line(aes(y = total), colour = "black", linewidth = 0.7) +
    # Peak marker
    geom_vline(xintercept = kappa_peak, colour = "gray",
               linetype = "dashed", linewidth = 0.5, alpha = 0.7) +
    annotate("text", x = kappa_peak + 0.015,
             y = max(df$total, na.rm = TRUE) * 0.98,
             label = TeX("$\\kappa^{\\dagger}$"),
             size = 4, colour = "gray", family = "serif") +
    # Manual legend via annotate (matching stacked area style)
    annotate("rect", xmin = 0.17, xmax = 0.20, ymin = max(df$total) * 0.88,
             ymax = max(df$total) * 0.92,
             fill = COL_QUIET, alpha = 0.5) +
    annotate("text", x = 0.21, y = max(df$total) * 0.90,
             label = TeX("Base: $m_0 \\cdot P(\\mathrm{bid})$"),
             size = 3, hjust = 0, family = "serif") +
    annotate("rect", xmin = 0.17, xmax = 0.20, ymin = max(df$total) * 0.80,
             ymax = max(df$total) * 0.84,
             fill = COL_EXIT, alpha = 0.5) +
    annotate("text", x = 0.21, y = max(df$total) * 0.82,
             label = TeX("Activism: $\\Delta^{\\mathrm{act}}(\\kappa)$"),
             size = 3, hjust = 0, family = "serif") +
    annotate("segment", x = 0.17, xend = 0.20, y = max(df$total) * 0.74,
             yend = max(df$total) * 0.74, linewidth = 0.5) +
    annotate("text", x = 0.21, y = max(df$total) * 0.74,
             label = TeX("Total $\\Delta^{\\mathrm{min}}$"),
             size = 3, hjust = 0, family = "serif") +
    labs(
      x = TeX("Liquidity $\\kappa$"),
      y = TeX("Expected Minority Takeover Gains"),
      title = "Decomposition of Minority Takeover Gains"
    ) +
    theme_evt()

  save_figure(p, file.path(output_dir, "fig_decomposition.pdf"))
  p
}

if (sys.nframe() == 0) plot_fig03()
```

## R/plot_fig04_prices.R

```r
# ============================================================================
# Figure 4: Equilibrium Prices by State
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))
library(patchwork)

plot_fig04 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "prices.csv"), show_col_types = FALSE)

  # Separate D=0 and D=1

  df_D0 <- df %>% filter(D == 0, on_path == TRUE)
  df_D1 <- df %>% filter(D == 1)

  # Create X labels
  df_D0$x_label <- paste0("X=", df_D0$X)
  df_D1$x_label <- paste0("X=", df_D1$X)

  # Match y-axis limits
  all_prices <- c(df_D0$price, df_D1$price)
  all_prices <- all_prices[is.finite(all_prices)]
  y_max <- max(all_prices) * 1.15

  # D=0 panel
  p1 <- ggplot(df_D0, aes(x = factor(X), y = price)) +
    geom_col(fill = COL_QUIET, colour = "black", alpha = 0.7, width = 0.6) +
    geom_text(aes(label = sprintf("pi=%.2f", pi)), vjust = -0.5, size = 3,
              family = "serif") +
    scale_y_continuous(limits = c(0, y_max)) +
    labs(
      x = NULL,
      y = TeX("Price $P(X, D=0)$"),
      title = TeX("Non-Disclosed States ($D=0$)")
    ) +
    scale_x_discrete(labels = function(x) TeX(paste0("$X=", x, "$"))) +
    theme_evt()

  # D=1 panel
  p2 <- ggplot(df_D1, aes(x = factor(X), y = price)) +
    geom_col(fill = COL_EXIT, colour = "black", alpha = 0.7, width = 0.6) +
    geom_text(aes(label = "pi=1.00"), vjust = -0.5, size = 3,
              family = "serif") +
    scale_y_continuous(limits = c(0, y_max)) +
    labs(
      x = NULL,
      y = TeX("Price $P(X, D=1)$"),
      title = TeX("Disclosed States ($D=1$)")
    ) +
    scale_x_discrete(labels = function(x) TeX(paste0("$X=", x, "$"))) +
    theme_evt()

  p_combined <- p1 + p2 + plot_layout(ncol = 2)

  save_figure(p_combined, file.path(output_dir, "fig_prices.pdf"),
              width = 10, height = 4)
  p_combined
}

if (sys.nframe() == 0) plot_fig04()
```

## R/plot_fig05_cutoffs_kappa.R

```r
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
```

## R/plot_fig06_disclosure.R

```r
# ============================================================================
# Figure 6: Disclosure Attenuation through the Inference Channel
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))

plot_fig06 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "disclosure_attenuation.csv"),
                 show_col_types = FALSE)

  plot_df <- bind_rows(
    df %>%
      transmute(kappa, value = act_disclosure, specification = "Baseline disclosure"),
    df %>%
      transmute(kappa, value = act_no_disclosure, specification = "No disclosure")
  )

  plot_df$specification <- factor(
    plot_df$specification,
    levels = c("Baseline disclosure", "No disclosure")
  )

  p <- ggplot(plot_df, aes(x = kappa, y = value,
                           colour = specification, linetype = specification,
                           shape = specification)) +
    geom_line(linewidth = 0.95) +
    geom_point(size = 1.6) +
    scale_colour_manual(values = c(
      "Baseline disclosure" = "#4477aa",
      "No disclosure" = "#ee6677"
    )) +
    scale_linetype_manual(values = c(
      "Baseline disclosure" = "solid",
      "No disclosure" = "dashed"
    )) +
    scale_shape_manual(values = c(
      "Baseline disclosure" = 16,
      "No disclosure" = 15
    )) +
    labs(
      x = TeX("Liquidity $\\kappa$"),
      y = TeX("Activism-Driven Minority Gains $\\Delta^{\\mathrm{act}}$"),
      title = "Disclosure Attenuation of Liquidity Sensitivity"
    ) +
    theme_evt() +
    theme(legend.position = "bottom", legend.title = element_blank())

  save_figure(p, file.path(output_dir, "fig_disclosure.pdf"))
  p
}

if (sys.nframe() == 0) plot_fig06()
```

## R/plot_fig07_sensitivity_C0.R

```r
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
```

## R/plot_fig08_sensitivity_wedge.R

```r
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
```

## R/plot_fig09_sensitivity_rho.R

```r
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
```

## R/plot_fig10_sensitivity_sigma_xi.R

```r
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
```

## R/plot_fig11_sensitivity_delta.R

```r
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
```

## R/plot_fig12_noisy_rumor.R

```r
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
```

## R/plot_fig13_welfare.R

```r
# ============================================================================
# Figure 13: Welfare Decomposition and Optimal Liquidity
# ============================================================================

source(here::here("R", "theme_evtmodel.R"))

plot_fig13 <- function(data_dir = here::here("numerical_output", "data"),
                       output_dir = here::here("numerical_output")) {

  df <- read_csv(file.path(data_dir, "welfare.csv"), show_col_types = FALSE)

  # Find optima
  idx_min <- which.max(df$W_min)
  idx_tot <- which.max(df$W_tot)
  kappa_dagger <- df$kappa[idx_min]
  kappa_star   <- df$kappa[idx_tot]

  p <- ggplot(df, aes(x = kappa)) +
    geom_line(aes(y = W_tot), colour = "#4477aa",
              linewidth = 0.9, linetype = "solid") +
    geom_line(aes(y = W_bid), colour = "#ee6677",
              linewidth = 0.9, linetype = "dashed") +
    geom_line(aes(y = W_min), colour = "#228833",
              linewidth = 0.9, linetype = "dotdash") +
    # Optimal kappa for minority gains
    geom_vline(xintercept = kappa_dagger, colour = "#228833",
               linetype = "dotted", linewidth = 0.5, alpha = 0.7) +
    annotate("text", x = kappa_dagger + 0.015,
             y = min(df$W_min, na.rm = TRUE),
             label = TeX("$\\kappa^{\\dagger}$"),
             colour = "#228833", size = 4, family = "serif") +
    # Optimal kappa for total surplus
    geom_vline(xintercept = kappa_star, colour = "#4477aa",
               linetype = "dotted", linewidth = 0.5, alpha = 0.7) +
    annotate("text", x = kappa_star - 0.015,
             y = max(df$W_tot, na.rm = TRUE) * 0.95,
             label = TeX("$\\kappa^{*}$"),
             colour = "#4477aa", size = 4, family = "serif", hjust = 1) +
    # Manual legend
    annotate("segment", x = 0.68, xend = 0.72,
             y = max(df$W_tot) * 0.35,
             yend = max(df$W_tot) * 0.35,
             colour = "#4477aa", linewidth = 0.7) +
    annotate("text", x = 0.73, y = max(df$W_tot) * 0.35,
             label = TeX("Total Surplus $W$"),
             hjust = 0, size = 3, family = "serif") +
    annotate("segment", x = 0.68, xend = 0.72,
             y = max(df$W_tot) * 0.30,
             yend = max(df$W_tot) * 0.30,
             colour = "#ee6677", linewidth = 0.7, linetype = "dashed") +
    annotate("text", x = 0.73, y = max(df$W_tot) * 0.30,
             label = TeX("Bidder Surplus $W_{\\mathrm{bid}}$"),
             hjust = 0, size = 3, family = "serif") +
    annotate("segment", x = 0.68, xend = 0.72,
             y = max(df$W_tot) * 0.25,
             yend = max(df$W_tot) * 0.25,
             colour = "#228833", linewidth = 0.7, linetype = "dotdash") +
    annotate("text", x = 0.73, y = max(df$W_tot) * 0.25,
             label = TeX("Minority Gains $W_{\\mathrm{min}}$"),
             hjust = 0, size = 3, family = "serif") +
    labs(
      x = TeX("Liquidity $\\kappa$"),
      y = "Expected Welfare / Surplus",
      title = "Welfare Decomposition"
    ) +
    theme_evt()

  save_figure(p, file.path(output_dir, "fig_welfare.pdf"))
  p
}

if (sys.nframe() == 0) plot_fig13()
```
