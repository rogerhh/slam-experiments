import numpy as np
import scipy
from scipy.stats import special_ortho_group
import sys
from optparse import OptionParser

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--infile", dest="infile", 
                      default=None, help="Input log file")
    (options, args) = parser.parse_args()

    infile = options.infile

    with open(infile, "r") as fin:


