import sys
from optparse import OptionParser
import random
from copy import deepcopy

from utils import *

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--input_file", "-f", dest="input_file",
                      default="", help="The path of the file containing the poses to plot.")
    (options, args) = parser.parse_args()

    infile = options.input_file

    orig_x = []
    orig_y = []
    orig_theta = []

    xs = []
    ys = []
    thetas = []

    with open(infile, "r") as fin:
        orig_x, orig_y, orig_theta = read_2d_poses(fin)

        while True:
            x, y, theta = read_2d_poses(fin)
            if len(x) == 0:
                break
            xs.append(x)
            ys.append(y)
            thetas.append(theta)

    plt.plot(orig_x, orig_y, 'co-', alpha=0.4, label="Original")

    plt.plot(xs[-1], ys[-1], 'bo-', alpha=0.4, label="Loop Closure")
    plt.plot(xs[-1], ys[-1], 'go-', alpha=0.4, label="Optimal")

    plt.legend(loc="best")


    # for i in range(len(xs)):
    #     x = xs[i]
    #     y = ys[i]
    #     theta = thetas[i]
    #     plt.plot(x, y, 'o-', alpha=0.5)
    plt.savefig("data/lc.png")
    plt.show()
        
