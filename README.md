# Usage

1. Put the content of this directory into [Castro/Exec/hydro_tests/KH at 812930df5051d7f567b520b50945bd8eb5000d8b · BoxLib-Codes/Castro](https://github.com/BoxLib-Codes/Castro/tree/812930df5051d7f567b520b50945bd8eb5000d8b/Exec/hydro_tests/KH)
2. adjust parameters in `input.2d` & `probin` for problem 3, or `input.2d.p5` & `probin.p5` for problem 5
3. On NERSC's Cori, run `sbatch job3.sh` for problem 3 or `sbatch job5.sh` for problem 5
4. run `make -f makefile -j 32` to make plots, which uses yt through the script in `castro_yt_plot.py`.
