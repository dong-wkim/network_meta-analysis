# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: R:percent
#     text_representation:
#       extension: .R
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: R
#     language: R
#     name: ir
# ---

# %%
packages <- c(
  "googledrive",
  "googlesheets4",
  "readxl",
  "Matrix",
  "metafor",
  "dplyr",
  "meta",
  "ggplot2",
  "ggpubr",
  "ggforestplot",
  "ggplotify",
  "ggplot2",
  "tidyverse",
  "svglite",
  "extrafont"
)

# Only install packages as needed
for (package in packages) {
  if (!requireNamespace(package, quietly = TRUE))
    install.packages(package, dependencies = TRUE)
}

lapply(packages, library, character.only = TRUE)
?extrafont()

# %%
setwd("./") # set working directory.
dir.create(file.path("../plots/forest/continuous/"))
dir.create(file.path("../plots/forest/dichotomous/"))

# %% [markdown]
# ① Custom function for meta-analysis of continuous data.

# %%
customfunction01 <- function(x) {
  xlsx_path <- paste0("data/xlsx/continuous/",x,".xlsx")
  csv_path <- paste0("data/csv/continuous/",x,".csv")
  svg_path <- paste0("plots/forest/continuous/",x,".svg")
  
  data <- read_excel(xlsx_path) %>%
    rename(ni = paste0(x, "_n"), mi = paste0(x, "_mean"), sdi = paste0(x, "_sd")) %>% 
    select(study, graft_type, ni, mi, sdi)
  data <- escalc(measure = "MN", ni = ni, mi = mi, sdi = sdi, data = data, slab = study)
  res <- rma(yi, vi, data = data, slab = study)
  data <- summary(data)
  
  write.csv(data, file = csv_path, row.names = FALSE)
  
  alim <- c(min(data$ci.lb), max(data$ci.ub))
  alim[1] <- ifelse(alim[1] > 10, floor(alim[1]/5)*5, floor(alim[1]/0.5)*0.5)
  alim[2] <- ifelse(alim[2] > 20, ceiling(alim[2]/5)*5, ceiling(alim[2]/0.5)*0.5)
  
  xlim <- c(alim[1]-1.65*diff(alim),alim[1]+1.65*diff(alim))
  
  ilab <- function(arg) {
    (3.3*diff(alim)*arg) + xlim[1]
  }
  ilab.xpos <- ilab(c(0.33,0.39,0.45))
  height = (res$k + 13)/4
  ks <- sum(data$graft_type == "S-QT")
  kb <- sum(data$graft_type == "B-QT")
  k <- ks + kb
  scale_efac <- function(k) {
    if (k < 7) {
      return(c(1.0, 0.8, 0.6))
    } else if (k <= 20) {
      return(c(0.8, 0.6, 0.4))
    } else if (k > 21) {
      return(c(0.3, 0.3, 0.2))
    } else {
      return(c(0.3, 0.3, 0.2))
    }}
  efac_value <- scale_efac(k)
  
  
  m.mean <- metamean(ni, mi, sdi, study, data, sm = "MRAW", subgroup = graft_type,
                     fixed = FALSE, random = TRUE, method.tau = "REML", tau.common = ifelse(k<10,TRUE,FALSE), 
                     hakn = TRUE, method.random.ci = "HK")
  
  range <- (alim[2] - alim[1]) * 1.65
  
  ks <- sum(data$graft_type == "S-QT")
  kb <- sum(data$graft_type == "B-QT")
  k <- ks + kb
  ylim <- c(-3,k+9)
  
  m.mean <- metamean(n = ni, mean = mi, sd = sdi, studlab = study, data = data,
                     sm = "MRAW", fixed = FALSE, random = TRUE, tau.common = FALSE,
                     method.tau = "REML", method.random.ci = "HK", subgroup = graft_type)
  summary(m.mean)
  
  res.sqt <- rma(yi, vi, data = data, subset = graft_type == "S-QT")
  res.bqt <- rma(yi, vi, data = data, subset = graft_type == "B-QT")
  reg <- rma(yi, vi, data = data, mods = ~ graft_type)
  # res.mv <- rma.mv(yi, vi, data = data, slab = study, mods = ~ graft_type, method = "REML")
  # pred.mv <- predict(res.mv, digits =2)
  # data$graft_type <- relevel(factor(data$graft_type), ref = "S-QT")
  
  # Generate and save forest plot
  
  height = (res$k + 13)/4
  svg(file = svg_path, width = 9, height = height)
  op <- par(xpd=TRUE)
  
  mlabfun <- function(text, x) {
    list(bquote(paste(.(text), 
                      italic("\u03c4"^2), " = ", .(fmtx(x$tau2, digits=2)) , ", ",
                      italic(I)^2, " = ", .(fmtx(x$I2, digits=1)), "%, ", 
                      italic(p),.(fmtp(x$QEp, digits=3, add0=TRUE, sep=TRUE, equal=TRUE))
    )))
  }
  
  with(
    res,
    forest(
      res,
      cex = 0.85,
      top = 2,
      alim = alim, 
      xlim = xlim,
      ylim = c(-3,k+9),
      ilab = cbind(
        ni,
        formatC(mi, format = "f", digits = 2),
        formatC(sdi, format = "f", digits = 2)
      ),
      ilab.xpos = ilab.xpos,
      ilab.pos = 2,
      rows = c(3:(kb + 2), (kb + 7):(k + 6)),
      refline = coef(res),
      mlab = mlabfun("RE Model for All Studies: ", res),
      plim = c(0.8, 1.2, 0.85),
      fonts = "Calibri Light",
      header = "Author(s) and Year",
      efac = efac_value,
      shade = "zebra",
      xlab = "",
      addpred=TRUE
    )
  )
  
  # Add additional column header labels
  text(ilab.xpos, k+9, c("N", "Mean", "SD"), pos=2, cex =0.85, font=2)
  
  # Add subgroup title labels
  text(xlim[1], c(k + 7.1, kb + 3.1), pos=4, c("S-QT","B-QT"), cex = 0.85, font =2)
  
  addpoly(res.sqt, 
          row=kb+5.5, 
          mlab=mlabfun("RE Model for Subgroup: ", res.sqt), cex=0.85, addpred=TRUE, efac=efac_value)
  
  addpoly(res.bqt, 
          row= 1.5, 
          mlab=mlabfun("RE Model for Subgroup: ", res.bqt), cex=0.85, addpred=TRUE, efac=efac_value)
  
  text(xlim[1], -2.2, pos=4, cex=0.85, bquote(paste("Test for Subgroup Differences: ",
                                                    italic(Q)[M], " = ", .(fmtx(reg$QM, digits=2)),
                                                    ", df = ", .(reg$p - 1), ", ",
                                                    italic(p),.(fmtp(reg$QMp, digits=3, add0=TRUE, sep=TRUE, equal=TRUE)))))
  
  par(op)
  dev.off()
}

# %% [markdown]
# ② Custom function for dichotomous data.

# %%
customfunction02 <- function(x) {
  # Define file paths
  data_path <- paste0("data/xlsx/dichotomous/",x,".xlsx")
  csv_path <- paste0("data/csv/dichotomous/",x,".csv")
  svg_path <- paste0("plots/forest/dichotomous/",x,".svg")
  
  data <- read_excel(data_path) %>%
    rename(ni = paste0(x, "_n"), xi = paste0(x, "_event")) %>% 
    select(study, graft_type, ni, xi)
  
  data <- escalc(measure = "PLO", ni = ni, xi = xi, data = data, slab = study)
  data <- summary(data,transf=transf.ilogit)
  # data.back <- summary(data, transf=transf.ilogit)
  # data$ilogit.yi <- data.back$yi
  # data$ilogit.ci.lb <- data.back$ci.lb
  # data$ilogit.ci.ub <- data.back$ci.ub
  write.csv(data, file = csv_path, row.names = FALSE)
  
  View(data)
  
  alim <- c(min(data$ci.lb), max(data$ci.ub))
  alim[1] <- ifelse(alim[1] > 10, floor(alim[1]/5)*5, floor(alim[1]/0.5)*0.5)
  alim[2] <- round(max(data$ci.ub[data$ci.ub != max(data$ci.ub)]), 2)
  #alim[2] <- ifelse(alim[2] > 20, ceiling(alim[2]/5)*5, ceiling(alim[2]/0.5)*0.5)
  xlim <- c(alim[1]-1.65*diff(alim),alim[1]+1.65*diff(alim))
  
  ilab <- function(arg) {
    (3.3*diff(alim)*arg) + xlim[1]
  }
  ilab.xpos <- ilab(c(0.39,0.45))
  
  
  ks <- sum(data$graft_type == "S-QT")
  kb <- sum(data$graft_type == "B-QT")
  k <- ks + kb
  y <- c(-3,k+9)
  
  
  
  m.prop <- metaprop(event = xi, 
                     n = ni, 
                     studlab = study, 
                     data = data, 
                     method = "GLMM", 
                     sm = "PLOGIT", 
                     fixed = FALSE, 
                     random = TRUE, 
                     method.random.ci = "HK", 
                     tau.common = TRUE)
  
  res.glmm <- rma.glmm(measure = "PLO", ni = ni, xi = xi, data = data, slab = study)
  pred <- predict(res.glmm, transf = transf.ilogit, digits = 2)
  
  # Generate and save forest plot
  scale_efac <- function(k) {
    if (k < 7) {
      return(c(1.0, 0.8, 0.6))
    } else if (k <= 15) {
      return(c(0.8, 0.6, 0.4))
    } else {
      return(c(0.4, 0.3, 0.2))
    }}
  efac_value <- scale_efac(k)
  
  height = (res.glmm$k + 13)/4
  svg(file = svg_path, width = 9, height = height)
  op <- par(xpd=TRUE)
  
  with(data, {
    forest(yi, ci.lb = ci.lb, ci.ub = ci.ub, slab = study,
           cex = 0.85, top = 2, alim = alim, at = seq(alim[1], alim[2], 0.1),
           xlim = xlim, ylim = c(-3,k+9),
           ilab = cbind(ni, xi), ilab.xpos = ilab.xpos,
           ilab.pos = 2, rows = c(3:(kb + 2), (kb + 7):(k + 6)),
           refline = pred$pred, mlab = "RE Model for All Studies: ",
           plim = c(0.9, 1.2, 0.85), fonts = "Calibri Light",
           header = FALSE,
           #header = "Author(s) and Year", 
           efac = efac_value, 
           shade = "zebra",
           xlab = "", digits = 3L
    )
  })
  
  
  # Add additional column header labels
  text(ilab.xpos, k+9, c("N", "Event"), pos = 2, cex = 0.85, font = 2)
  
  View(m.prop)
  View(res.glmm)
  
  # Add subgroup title labels
  text(xlim[1], c(k+7.1, kb+3.1), pos = 4, c("S-QT", "B-QT"), cex = 0.85, font = 2)
  
  # Add summary statistics, polygon, and pooled estimate for subgroup A
  m.prop.sqt <- update(m.prop, subset = graft_type == "S-QT")
  res.sqt <- update(res.glmm, subset = graft_type == "S-QT")
  pred.sqt <- predict(res.sqt, transf = transf.ilogit, digits = 2)
  
  text(xlim[1], kb + 5.5, pos = 4, cex = 0.85, bquote(paste(
    "RE Model for Subgroup: ", italic("\u03c4"^2), " = ", .(fmtx(m.prop.sqt$tau2, digits = 2)), ", ",
    italic(I)^2, " = ", .(fmtx(m.prop.sqt$I2 * 100, digits = 1)), "%, ", 
    italic(p), .(fmtp(m.prop.sqt$pval.Q[1], digits = 3, add0 = TRUE, sep = TRUE, equal = TRUE))
  )))
  addpoly(pred.sqt$pred, ci.lb = pred.sqt$ci.lb, ci.ub = pred.sqt$ci.ub, row = kb + 5.5, efac = 0.3)
  
  
  # Add summary statistics, polygon, and pooled estimate for subgroup B
  m.prop.bqt <- update(m.prop, subset = graft_type == "B-QT")
  res.bqt <- update(res.glmm, subset = graft_type == "B-QT")
  pred.bqt <- predict(res.bqt, transf = transf.ilogit, digits = 2)
  
  text(xlim[1], 1.5, pos = 4, cex = 0.85, bquote(paste(
    "RE Model for Subgroup: ", italic("\u03c4"^2), " = ", .(fmtx(m.prop.bqt$tau2, digits = 2)), ", ",
    italic(I)^2, " = ", .(fmtx(m.prop.bqt$I2 * 100, digits = 1)), "%, ", 
    italic(p), .(fmtp(m.prop.bqt$pval.Q[1], digits = 3, add0 = TRUE, sep = TRUE, equal = TRUE))
  )))
  addpoly(pred.bqt$pred, ci.lb = pred.bqt$ci.lb, ci.ub = pred.bqt$ci.ub, row = 1.5, efac = 0.3)
  
  abline(h = 0)
  
  # Add summary statistics, polygon, and pooled estimate for all studies`
  text(xlim[1], -1, pos = 4, cex = 0.85, bquote(paste(
    "RE Model for All Studies: ", italic("\u03c4"^2), " = ", .(fmtx(m.prop$tau2, digits = 2)), ", ",
    italic(I)^2, " = ", .(fmtx(m.prop$I2 * 100, digits = 1)), "%, ", 
    italic(p), .(fmtp(m.prop$pval.Q[1], digits = 3, add0 = TRUE, sep = TRUE, equal = TRUE))
  )))
  addpoly(pred$pred, ci.lb = pred$ci.lb, ci.ub = pred$ci.ub, row = -1, efac = 0.3)
  
  m.prop.subgroup <- update(m.prop, subgroup = graft_type)
  text(xlim[1], -2.2, pos = 4, cex = 0.85, bquote(paste(
    "Test for Subgroup Differences: ", italic(Q)[M], " = ", .(fmtx(m.prop.subgroup$Q.b.random, digits = 2)),
    ", df = ", .(m.prop.subgroup$df.Q.b.random), ", ", italic(p), .(fmtp(m.prop.subgroup$pval.Q.b.random, digits = 3, add0 = TRUE, sep = TRUE, equal = TRUE))
  )))
  
  par(op)
  dev.off()
}

# %% [markdown]
# ③ List the continuous outcomes and run the analysis and generate forest plots.

# %%
continuous <- c(
  "h_lsi_isokinetic_60",
  "h_lsi_isokinetic_180",
  "h_lsi_isometric",
  "ikdc_subjective",
  "instrumental_laxity",
  "koos_adl",
  "koos_pain",
  "koos_qol",
  "koos_sport",
  "koos_symptoms",
  "lysholm",
  "marx",
  "slht",
  "q_lsi_isokinetic_60",
  "q_lsi_isokinetic_180",
  "q_lsi_isometric",
  "tegner",
  "vas",
  "template"
)

lapply(continuous, customfunction01)

# %% [markdown]
# ④ List the dichotomous outcomes and run the analysis and generate forest plots.

# %%
dichotomous <- c(
  "arthrofibrosis",
  "donor_site_morbidity",
  "graft_rupture",
  "ikdc_objective",
  "lachman",
  "patellar_fracture_null",
  "patellar_fracture",
  "pivot_shift_0_1"
)

lapply(dichotomous, customfunction02)

# %% [markdown]
# ⑤ Create lattice summary plots.

# %%
