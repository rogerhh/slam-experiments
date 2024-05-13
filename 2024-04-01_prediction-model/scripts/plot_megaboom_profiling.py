import sys
from optparse import OptionParser
import csv
import numpy as np
import matplotlib.pyplot as plt

def read_until(fin, match, keep=False):
    while True:
        pos = fin.tell()
        line = fin.readline()
        if not line:
            print(f"{match} is not found")
            return False

        if match in line:
            if keep:
                fin.seek(pos)
            return True


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--infile", dest="infile", 
                      default="", help="The filename that contains the profiled cycle count")
    parser.add_option("--savedir", dest="savedir", 
                      default="", help="The directory to save plots to")
    parser.add_option("--plot", dest="plot", action="store_true",
                      default=False, help="Whether or not to plot figures.")
    parser.add_option("--save", dest="save", action="store_true",
                      default=False, help="Whether or not to save figures.")

    (options, args) = parser.parse_args()

    infile = options.infile

    cycles = []

    with open(infile, "r") as fin:
        read_until(fin, "===sphere===")

        while read_until(fin, "Reorder cycles", keep=True):
            cycles.append({})

            reorder_cycles = None
            symbolic_cycles = None
            relin_cycles = None
            ata_cycles = None
            fac_cycles = None
            merge_cycles = None
            chol_cycles = None
            backsolve_cycles = None

            while True:
                line = fin.readline()

                if line is None:
                    break

                arr = line.split()

                print(line)

                if "Reoder cycles:" in line:
                    reorder_cycles = float(arr[-1])
                elif "Symbolic cycles:" in line:
                    symbolic_cycles = float(arr[-1])
                elif "Restore cycles:" in line:
                    restore_cycles = float(arr[-1])
                elif "Relin cycles:" in line:
                    relin_cycles = float(arr[-1])
                elif "AtA cycles:" in line:
                    ata_cycles = float(arr[-1])
                elif "fac cycles:" in line:
                    fac_cycles = float(arr[-1])
                elif "merge cycles:" in line:
                    merge_cycles = float(arr[-1])
                elif "Cholesky cycles:" in line:
                    chol_cycles = float(arr[-1])
                elif "Backsolve cycles:" in line:
                    backsolve_cycles = float(arr[-1])
                elif "Total step cycles:" in line:
                    step_cycles = float(arr[-1])
                    break

            cycles[-1]["Reorder"] = reorder_cycles
            cycles[-1]["Symbolic"] = symbolic_cycles
            cycles[-1]["Restore"] = restore_cycles
            cycles[-1]["Relinearize"] = relin_cycles
            cycles[-1]["Hessian"] = ata_cycles
            cycles[-1]["Partial Factorization"] = fac_cycles
            cycles[-1]["Merge"] = merge_cycles
            cycles[-1]["Cholesky"] = chol_cycles
            cycles[-1]["Backsolve"] = backsolve_cycles
            cycles[-1]["Total"] = step_cycles

            reorder_cycles = None
            symbolic_cycles = None
            relin_cycles = None
            ata_cycles = None
            fac_cycles = None
            merge_cycles = None
            chol_cycles = None
            backsolve_cycles = None


    total = []
    sym = []
    chol = []
    backsolve = []

    for i, cycle in enumerate(cycles):
        total.append(cycle["Total"])
        sym.append(cycle["Symbolic"])
        chol.append(cycle["Cholesky"])
        backsolve.append(cycle["Backsolve"])

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    t = range(len(cycles))
    plt.plot(t, total, label="Total")
    plt.plot(t, sym, label="Symbolic")
    plt.plot(t, chol, label="Cholesky")
    plt.plot(t, backsolve, label="Backsolve")

    plt.legend()

    # ax.set_yscale("log")

    if options.save:
        outfile = f"{options.savedir}/overall.png"
        plt.savefig(outfile)

    if options.plot:
        plt.show()

    reorder = []
    relin = []
    restore = []
    hessian = []
    fac = []
    merge = []

    for i, cycle in enumerate(cycles):
        reorder.append(cycle["Reorder"])
        restore.append(cycle["Restore"])
        relin.append(cycle["Relinearize"])
        hessian.append(cycle["Hessian"])
        fac.append(cycle["Partial Factorization"])
        merge.append(cycle["Merge"])

    t = range(len(cycles))
    plt.plot(t, reorder, label="Reorder (Symbolic)")
    plt.plot(t, reorder, label="Restore (Cholesky)")
    plt.plot(t, relin, label="Relinearize (Cholesky)")
    plt.plot(t, hessian, label="Hessian (Cholesky)")
    plt.plot(t, fac, label="Partial Factorization (Cholesky)")
    plt.plot(t, merge, label="Backsolve (Cholesky)")

    plt.legend()

    if options.save:
        outfile = f"{options.savedir}/breakdown.png"
        plt.savefig(outfile)

    if options.plot:
        plt.show()




