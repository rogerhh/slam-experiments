import sys
from optparse import OptionParser
import csv
import numpy as np
import matplotlib.pyplot as plt
import re

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--infile", dest="infile", 
                      default=None, help="uartlog")
    parser.add_option("--outfig", dest="outfig", 
                      default=None, help="output figure path")
    parser.add_option("--is3D", dest="is3D", type="int",
                      default=1, help="output figure path")
    parser.add_option("--edge_rate", dest="edge_rate", type="float",
                      default=0.005, help="output figure path")

    (options, args) = parser.parse_args()

    infile = options.infile
    outfig = options.outfig
    is3D = options.is3D
    edge_rate = options.edge_rate

    xss = []
    yss = []
    zss = []

    poses = []

    edges = []

    with open(infile, "r") as fin:
        xs = []
        ys = []
        zs = []
        while True:
            line = fin.readline()

            print(line)

            if not line:
                break

            if "VERTEX" in line:
                arr = line.split()

                x, y, z = float(arr[2]), float(arr[3]), float(arr[4])

                poses.append([x, y, z])

                if len(xs) > 0:
                    prev_x, prev_y, prev_z = xs[-1], ys[-1], zs[-1]
                    if (x - prev_x) ** 2 + (y - prev_y) ** 2 + (z - prev_z) ** 2 > 100:
                        xss.append(xs)
                        yss.append(ys)
                        zss.append(zs)
                        xs = []
                        ys = []
                        zs = []
                else:
                    xs = []
                    ys = []
                    zs = []

                xs.append(x)
                ys.append(y)
                zs.append(z)

            if "EDGE" in line:
                arr = line.split()
                k1, k2 = int(arr[1]), int(arr[2])
                edges.append([k1, k2])

    xss.append(xs)
    yss.append(ys)
    zss.append(zs)
    

    fig = plt.figure()

    if is3D:
        ax = fig.add_subplot(111, projection="3d")
    else:
        ax = fig.add_subplot(111)

    for xs, ys, zs in zip(xss, yss, zss):

        width = 0.9
        alpha = 0.9
        if is3D:
            ax.plot(xs, ys, zs, "b-", linewidth=width, alpha=alpha)
        else:
            ax.plot(xs, ys, "b-", linewidth=width, alpha=alpha)

    w2 = 0.3
    alpha2 = 0.3
    for k1, k2 in edges:
        if np.random.uniform() >= edge_rate:
            continue

        p1 = poses[k1]
        p2 = poses[k2]
        ex = [p1[0], p2[0]]
        ey = [p1[1], p2[1]]
        ez = [p1[2], p2[2]]
        if is3D:
            ax.plot(ex, ey, ez, 'k-', linewidth=w2, alpha=alpha2)
        else:
            ax.plot(ex, ey, 'k-', linewidth=w2, alpha=alpha2)

    ax.set_xlabel("m")
    ax.set_ylabel("m")

    plt.savefig(outfig)


