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
    thetas = []

    for infile in infiles:
        with open(infile, "r") as fin:
            x, y, theta = read_2d_poses(fin)
            xs.append(x)
            ys.append(y)
            thetas.append(theta)

    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        theta = thetas[i]
        plt.plot(x, y, 'o-', alpha=0.5)
    plt.show()
        
