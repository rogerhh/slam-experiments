import sys
from optparse import OptionParser
import random
from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np

def 

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--infile", dest="input_file",
                      default="", help="The path of the measurements file")
    parser.add_option("--outfile", dest="output file",
                      default="", help="The path of the output file")
    (options, args) = parser.parse_args()

    infile = options.input_file

    with open(infile, "r") as fin:


