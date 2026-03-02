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
