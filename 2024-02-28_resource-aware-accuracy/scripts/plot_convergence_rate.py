import sys
from optparse import OptionParser
import random
from copy import deepcopy

from utils import *

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--input_files", "-f", dest="input_files",
                      default="", help="The path of the file containing the poses to plot.")
    (options, args) = parser.parse_args()

    infiles = options.input_files.split()

    max_plot_idx = 150

    fix, ax = plt.subplots(1)
    ax.ticklabel_format(axis="y", style="sci", scilimits=(0,0))

    for infile in infiles:
        iters = []
        chi2s = []
        max_relin_keys = None
        dataset_name = None
        with open(infile, "r") as fin:
            while True:
                line = fin.readline()
                if not line:
                    break

                if dataset_name is None and "Loading" in line:
                    dataset_name = line.split()[-1]

                if max_relin_keys is None and "max_relin_keys = " in line:
                    arr = line.split(",")
                    for item in arr:
                        if "max_relin_keys" in item:
                            max_relin_keys = int(item.strip().split()[-1])


                if "iter = " in line:
                    arr = line.split(",")
                    it = None
                    chi2 = None
                    for item in arr:
                        if "iter" in item:
                            it = float(item.strip().split()[-1])
                        if "Chi2" in item:
                            chi2 = float(item.strip().split()[-1])
                    iters.append(it)
                    chi2s.append(chi2)


        plt.plot(iters[:max_plot_idx], chi2s[:max_plot_idx], label=f"Num updated poses: {max_relin_keys}")

    plt.xlabel("Number of iterations")
    plt.ylabel("Chi2 error")

    plt.legend()
    plt.savefig(f"data/{dataset_name}_convergence_rate.png")
    plt.show()


    # plt.plot(orig_x, orig_y, 'co-', alpha=0.4, label="Original")

    # plt.plot(xs[-1], ys[-1], 'bo-', alpha=0.4, label="Resource Aware")
    # plt.plot(xs[-1], ys[-1], 'go-', alpha=0.4, label="Optimal")



    # for i in range(len(xs)):
    #     x = xs[i]
    #     y = ys[i]
    #     theta = thetas[i]
    #     plt.plot(x, y, 'o-', alpha=0.5)
        
