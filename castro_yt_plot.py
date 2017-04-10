#!/usr/bin/env python2

import yt
import os

def yt_plt(pltPath):
    """Procedure to save the plots to pltPath.pdf
    """
    ds1= yt.load(pltPath)
    ds1.derived_field_list
    p1 = yt.ProjectionPlot(ds1, "z", "density")
    p1.annotate_grids()
    p1.save(pltPath + ".pdf")

if __name__ == "__main__":
    pltsPath = os.path.expanduser("~/NERSC/Castro/Exec/hydro_tests/KH/")
    # get all the directories with name starting as plt
    # these are the directories of each CASTRO plot output
    pltDir = [name for name in os.listdir(pltsPath)
        if (os.path.isdir(os.path.join(pltsPath, name)) and name[:3] == "plt")]
    for plt in pltDir:
        yt_plt(os.path.join(pltsPath, plt))
