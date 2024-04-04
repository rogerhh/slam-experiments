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

    size = len(orig_x)
    plt.plot(xs[-1][:size], ys[-1][:size], 'go-', alpha=0.6, label="Optimal")
    plt.plot(orig_x, orig_y, 'mo-', alpha=0.6, label="Original")
    plt.legend(loc="best")
    plt.savefig("data/ra_low1.png")
    plt.show()

    idx = 0
    size = len(xs[idx])
    plt.plot(xs[-1][:size], ys[-1][:size], 'go-', alpha=0.6, label="Optimal")
    plt.plot(xs[idx], ys[idx], 'bo-', alpha=0.6, label="Resource Aware")
    plt.plot(xs[idx][16:19], ys[idx][16:19], 'ro-', alpha=1, label="Updated Subgraph")
    plt.legend(loc="center")
    plt.savefig("data/ra_low2.png")
    plt.show()

    idx = 1
    size = len(xs[idx])
    plt.plot(xs[-1][:size], ys[-1][:size], 'go-', alpha=0.6, label="Optimal")
    plt.plot(xs[idx], ys[idx], 'bo-', alpha=0.6, label="Resource Aware")
    plt.plot(xs[idx][13:16], ys[idx][13:16], 'ro-', alpha=1, label="Updated Subgraph")
    plt.legend(loc="center")
    plt.savefig("data/ra_low3.png")
    plt.show()

    idx = 2
    size = len(xs[idx])
    plt.plot(xs[-1][:size], ys[-1][:size], 'go-', alpha=0.6, label="Optimal")
    plt.plot(xs[idx], ys[idx], 'bo-', alpha=0.6, label="Resource Aware")
    plt.plot(xs[idx][10:13], ys[idx][10:13], 'ro-', alpha=1, label="Updated Subgraph")
    plt.legend(loc="center")
    plt.savefig("data/ra_low4.png")
    plt.show()

    # plt.plot(orig_x, orig_y, 'co-', alpha=0.4, label="Original")

    # plt.plot(xs[-1], ys[-1], 'bo-', alpha=0.4, label="Resource Aware")
    # plt.plot(xs[-1], ys[-1], 'go-', alpha=0.4, label="Optimal")



    # for i in range(len(xs)):
    #     x = xs[i]
    #     y = ys[i]
    #     theta = thetas[i]
    #     plt.plot(x, y, 'o-', alpha=0.5)
        
