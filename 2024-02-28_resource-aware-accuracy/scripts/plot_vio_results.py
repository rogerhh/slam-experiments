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

    fig, ax = plt.subplots(1)

    ax.plot(xs[-1], ys[-1], 'go-', alpha=0.6, label="Optimal")
    ax.plot(orig_x, orig_y, 'mo-', alpha=0.6, label="Original")

    idx = 0
    ax.plot(xs[idx][0:19], ys[idx][0:19], 'bo-', alpha=0.6, label="VIO")

    ax.plot(xs[idx][18:21], ys[idx][18:21], 'ro-', alpha=1, label="Updated Subgraph")


    # handles, labels = ax.get_legend_handles_labels()
    # desired_order = [1, 0, 2]
    # reordered_handles = [handles[i] for i in desired_order]
    # reordered_labels = [labels[i] for i in desired_order]

    ax.legend(loc="best")


    # for i in range(len(xs)):
    #     x = xs[i]
    #     y = ys[i]
    #     theta = thetas[i]
    #     plt.plot(x, y, 'o-', alpha=0.5)
    plt.savefig("data/vio.png")
    plt.show()
        
