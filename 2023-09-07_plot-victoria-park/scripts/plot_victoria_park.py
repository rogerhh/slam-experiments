import sys
from optparse import OptionParser
import csv
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--input_file", dest="input_file", 
                      default="", help="The filename that contains rank change output in csv format")

    (options, args) = parser.parse_args()

