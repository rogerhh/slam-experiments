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
    parser.add_option("--outfile", dest="outfile", 
                      default=None, help="output file path")

    (options, args) = parser.parse_args()

    infile = options.infile
    outfile = options.outfile

    with open(outfile, "w") as fout:
        with open(infile, "r") as fin:
            count = 0
            print(infile)
            while True:
                line = fin.readline()
                print("line = ", line)
                if not line:
                    break

                fout.write(f"VERTEX_SE3:QUAT {count} {line}")
                count += 1


