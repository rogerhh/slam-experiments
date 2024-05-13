import sys
from optparse import OptionParser
import random
from copy import deepcopy
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation
import numpy as np

def read_until(fin, pattern, keep=False):
    while True:
        pos = fin.tell()
        line = fin.readline()
        if not line:
            return False
        if pattern in line:
            if keep:
                fin.seek(pos)
                return True
            else:
                return True

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--infile", dest="input_file",
                      default="", help="The path of the measurements file")
    parser.add_option("--outfile", dest="output_file",
                      default="", help="The path of the output file")
    (options, args) = parser.parse_args()

    infile = options.input_file
    outfile = options.output_file

    with open(infile, "r") as fin:
        with open(outfile, "w") as fout:
            while read_until(fin, "BetweenFactor", keep=True):
                line = fin.readline()
                keys = [int(k) for k in line.split("(")[-1].strip(")\n ").split(",")]
                print(keys)

                read_until(fin, "measured:", keep=False)

                R = np.eye(3, 3)
                for i in range(3):
                    arr = fin.readline().strip("; \n").split(",")
                    for j in range(3):
                        R[i, j] = float(arr[j])

                read_until(fin, "t:", keep=True)

                t = np.zeros((3,))
                arr = fin.readline().split(":")[-1].strip("; \n").split()
                for i in range(3):
                    t[i] = float(arr[i])

                read_until(fin, "noise model", keep=True)

                vals = [float(x) for x in fin.readline().split("[")[-1].split("]")[0].split(";")]

                t_info = np.zeros((3, 3))
                t_info[0, 0] = vals[0]
                t_info[1, 1] = vals[1]
                t_info[2, 2] = vals[2]

                R_info = np.zeros((3, 3))
                R_info[0, 0] = vals[3]
                R_info[1, 1] = vals[4]
                R_info[2, 2] = vals[5]

                print(R, t)

                Rq = Rotation.from_matrix(R).as_quat()

                fout.write(f"EDGE_SE3:QUAT {keys[0]} {keys[1]} ")
                fout.write(f"{t[0]:.6f} {t[1]:.6f} {t[2]:.6f} ")
                fout.write(f"{Rq[0]:.6f} {Rq[1]:.6f} {Rq[2]:.6f} {Rq[3]:.6f} ")

                for i in range(3):
                    fout.write(f"{t_info[i, i]:.6f} ")
                    for j in range(6 - i - 1):
                        fout.write(f"{0:.6f} ")
                    fout.write(f"  ")

                for i in range(3):
                    fout.write(f"{R_info[i, i]:.6f} ")
                    for j in range(3 - i - 1):
                        fout.write(f"{0:.6f} ")
                    fout.write(f"  ")
                fout.write("\n")

