import sys
from optparse import OptionParser
import random
from copy import deepcopy

from utils import *

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--input_files", "-f", dest="input_files",
                      default="", help="The path of all the files containing the poses to plot.")
    (options, args) = parser.parse_args()

    infiles = options.input_files.split()

    print(options.input_files)

    xs = []
    ys = []
    zs = []

    for infile in infiles:
        with open(infile, "r") as fin:
            x, y, z = read_3d_poses(fin)
            xs.append(x)
            ys.append(y)
            zs.append(z)

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    print(len(xs))
    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        z = zs[i]
        ax.plot(x, y, z , '-', alpha=0.5)
    plt.show()
        
