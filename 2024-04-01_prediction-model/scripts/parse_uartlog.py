import numpy as np
import scipy
from scipy.stats import special_ortho_group
import sys
from optparse import OptionParser
import math
from copy import deepcopy

class NodeData:
    def __init__(self, fin, step):
        self.step = step

        line = fin.readline()
        arr = line.split()

        if "no cholesky" in line:
            self.width = int(arr[3])
            self.height = int(arr[5])

            line = fin.readline()
            arr = line.split()

        self.index = int(arr[1])
        self.total_cycles = int(arr[4])

        line = fin.readline()
        arr = line.split()
        self.init_cycles = int(arr[2])

        line = fin.readline()
        arr = line.split()
        self.AtA_cycles = int(arr[2])

        line = fin.readline()
        arr = line.split()
        self.chol_cycles = int(arr[2])

        line = fin.readline()
        arr = line.split()
        self.merge_cycles = int(arr[2])



def read_step(fin, step):
    while True:
        line = fin.readline()

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--infile", dest="infile",
                      default=None, help="Input file path")
    (options, args) = parser.parse_args()

    infile = options.infile

    step = -1
    with open(infile, "r") as fin:
        while True:
            line = fin.readline()
            arr = line.split()

            if not line:
                break

            if "step = " in line:
                step = int(arr[2])

            if "no cholesky" in line:




