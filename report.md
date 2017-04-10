---
title:	ASTRO 250 HW3 Report — Kelvin-Helmholtz instability with Castro
author:	Kolen Cheung
date:	\today
abstract:	In this HW, different refinement parameters are used to investigate its effect on AMR on the study of Kelvin-Helmholtz instability through [Castro](https://github.com/BoxLib-Codes/Castro).
keywords:	ASTRO250, HW3, Kelvin-Helmholtz instability, Castro
lang:	en
papersize:	letter
fontsize:	12pt
documentclass:	memoir
classoption:	oneside, article
geometry:	inner=0.5in, outer=0.5in, top=0.5in, bottom=0.75in
fontfamily:	fourier
usepackage:	siunitx,cancel,physics,placeins
hypersetup:	bookmarksnumbered,pdfpagelabels,pagebackref,hypertexnames=false,linktocpage=true
colorlinks:	true
linkcolor:	blue
citecolor:	blue
urlcolor:	blue
toccolor:	blue
...

# Introduction

In the following, we will investigate using different parameters of AMR in Castro on different problems about Kelvin-Helmholtz instability. The problem statements are described in [Castro/Exec/hydro_tests/KH at 812930df5051d7f567b520b50945bd8eb5000d8b · BoxLib-Codes/Castro](https://github.com/BoxLib-Codes/Castro/tree/812930df5051d7f567b520b50945bd8eb5000d8b/Exec/hydro_tests/KH). And below we focuses on problem 3 and problem 5.

The code is organized in this way:

1. to run the code, it requires [Castro/Exec/hydro_tests/KH at 812930df5051d7f567b520b50945bd8eb5000d8b · BoxLib-Codes/Castro](https://github.com/BoxLib-Codes/Castro/tree/812930df5051d7f567b520b50945bd8eb5000d8b/Exec/hydro_tests/KH). Read [README.md](https://github.com/ickc/ASTRO250-hw3/blob/master/README.md) for usage.
2. different combinations of parameters are used, and plots are made for each run, which can be downloaded from [Releases · ickc/ASTRO250-hw3](https://github.com/ickc/ASTRO250-hw3/releases). They are put in `plots/*/`. The parameters can be read from within each plot directory, with files `input.2d` & `probin` for problem 3, or `input.2d.p5` & `probin.p5` for problem 5.

# Problem 3 — Linear Kelvin-Helmholtz Instability

The plot with no refinement level and `dengrad = 0.1; velgrad = 1.0` with $t = 2.0 \text{s}$ looks like this:

![Problem 3 — no refinement](plots/0-original/plt02530.png){width=50%}

With 2 more level of refinements, it then looks like this:

![problem 3 — 2 more level of refinements](plots/1-refine-2/plt02669.png){width=50%}

From here we see that with more refinement using AMR, more features can be seen from the "eyes" of the Kelvin-Helmholtz instability.

If we change `velgrad = 0.1`:

![problem 3 — `velgrad = 0.1`](plots/4-refine-2-velgrad-0.1/plt02669.png){width=50%}

You can see there are basically no difference. Hence the gradient is dominated by the density rather than velocity.

If we change `dengrad = 0.01`:

![Problem 3 — `dengrad = 0.01`](plots/5-refine-2-dengrad-0.01/plt02394.png){width=50%}

We see that it actually get worse. i.e. if the AMR refinement is trigger by a smaller gradient, the result does not necessarily gets better, because this smaller difference might not capture the boundary well enough to have any practical improvement by the AMR. Comparing the 2 plots, we see that indeed the refined mesh does not target the boundary as good as before.

So in the end, the plot with 2 extra level of AMR refinement and `dengrad = 0.1; velgrad = 1.0` looks best, and gives the most details.

# Problem 5 — Non-Linear Kelvin-Helmholtz Instability

Without any refinement, with `dengrad = 0.1; velgrad = 1.0` at $t = 2.7\text{s}$:

![Problem 5 — no refinement, at $t = 2.7\text{s}$](plots/6-p5-refine-0/plt04654.pdf){width=50%}

With 2 extra levels of refinement:

![Problem 5 — with 2 extra levels of refinement, at $t = 2.7\text{s}$](/Users/kolen/Dropbox/git/Cori/ASTRO250-hw3/plots/7-p5-refine-2/plt04659.pdf){width=50%}

We can see that in the case of non-linear Kelvin-Helmholtz instability, extra levels of refinement does pay off to show details otherwise hidden.

# Final Plots

Instead of plotting an image, I made videos at YouTube, one with the AMR grids annotated, one without. Click the image to redirect to YouTube:

[![at $t = 7.6 \text{s}$, with AMR grids annotated.](plots/9-p5-refine-2-9-16/plt13843.png)](https://youtu.be/1w6tcsmedWs)

[![at $t = 7.6 \text{s}$, without AMR grids annotated.](plots/10-p5-refine-2-9-16-no-grid/plt13843.png)](https://youtu.be/xweAiSQZ4aU)
