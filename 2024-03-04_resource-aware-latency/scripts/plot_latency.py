import sys
from optparse import OptionParser
import random
from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--input_files", "-f", dest="input_files",
                      default="", help="The path of all the files containing the poses to plot.")
    (options, args) = parser.parse_args()

    infiles = options.input_files.split()

    iters = []
    lats = []

    for infile in infiles:
        it = []
        lat = []
        with open(infile, "r") as fin:
            while True:
                line = fin.readline()

                if not line:
                    break

                if "update_time" in line:
                    arr = line.split()
                    it.append(int(arr[2].strip(", ")))
                    lat.append(int(arr[5]))

        iters.append(it)
        lats.append(lat)

    count = 0
    for l in lats[1]:
        if l > 34000:
            count += 1
    print("Deadline miss rate: ", count / len(lats[1]))

    count = 0
    for l in lats[3]:
        if l > 34000:
            count += 1
    print("Deadline miss rate: ", count / len(lats[3]))

    fig, ax = plt.subplots(1)
    ax.plot(iters[1], 1e-3 * np.array(lats[1]), 'ro-', linewidth=0.3, markersize=3, label="Full SLAM With Contention")
    ax.plot(iters[0], 1e-3 * np.array(lats[0]), 'bo-', linewidth=0.3, markersize=3, label="Full SLAM No Contention")
    ax.plot(iters[2], 1e-3 * np.array(lats[2]), 'mo-', linewidth=0.3, markersize=3, label="Resource Aware No Contention")
    ax.plot(iters[3], 1e-3 * np.array(lats[3]), 'go-', linewidth=0.3, markersize=3, label="Resource Aware With Contention")
    ax.plot([0, 3000], [34, 34], 'k-', label="Target Latency")

    plt.xlabel("Number of Poses")
    plt.ylabel("Latency (ms)")

    handles, labels = ax.get_legend_handles_labels()
    desired_order = [1, 0, 2, 3, 4]
    reordered_handles = [handles[i] for i in desired_order]
    reordered_labels = [labels[i] for i in desired_order]

    ax.legend(reordered_handles, reordered_labels)

    plt.savefig("data/latency-comparison.png")
    plt.show()

    fig, ax = plt.subplots(1)
    ax.plot(iters[1], 1e-3 * np.array(lats[1]), 'ro-', linewidth=0.3, markersize=3, label="Full SLAM With Contention")
    ax.plot(iters[0], 1e-3 * np.array(lats[0]), 'bo-', linewidth=0.3, markersize=3, label="Full SLAM No Contention")
    ax.plot([0, 3000], [34, 34], 'k-', label="Target Latency")

    plt.xlabel("Number of Poses")
    plt.ylabel("Latency (ms)")


    handles, labels = ax.get_legend_handles_labels()
    desired_order = [1, 0, 2]
    reordered_handles = [handles[i] for i in desired_order]
    reordered_labels = [labels[i] for i in desired_order]

    ax.legend(reordered_handles, reordered_labels)

    plt.savefig("data/latency-comparison-baseline.png")
    plt.show()

