#!/usr/bin/env python2

import argparse
import os
import yt

def yt_plt(pltPath, annotate, ext):
    """Procedure to save the plots to pltPath.pdf
    """
    ds1= yt.load(pltPath)
    ds1.derived_field_list
    p1 = yt.ProjectionPlot(ds1, "z", "density")
    if annotate:
        p1.annotate_grids()
    p1.save('.'.join((pltPath, ext)))

def main(args):
    pltsPath = args.d
    annotate = args.a
    ext = args.t

    pltsPath = os.path.expanduser(pltsPath)
    # get all the directories with name starting as plt
    # these are the directories of each CASTRO plot output
    pltDir = [name for name in os.listdir(pltsPath)
        if (os.path.isdir(os.path.join(pltsPath, name)) and name[:3] == "plt")]
    for plt in pltDir:
        yt_plt(os.path.join(pltsPath, plt), annotate, ext)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.set_defaults(func=main)
    # Args
    parser.add_argument('-d',
                        help='The input directory of the plots. Expects directories of name "plt..." within this directory.')
    parser.add_argument('-a',
                        action='store_true',
                        help='Annotate the grids.')
    parser.add_argument('-t',
                        help='The output file extension. e.g. pdf, png, etc.')
    args = parser.parse_args()
    args.func(args)
