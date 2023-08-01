import sys
from optparse import OptionParser
import csv
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--input_file", dest="input_file", 
                      default="", help="The filename that contains rank change output in csv format")
    parser.add_option("--var_width", dest="var_width", 
                      default="", help="The width of the variables (assuming same for all)")
    parser.add_option("--output_figure", dest="output_figure", 
                      default="", help="The width of the variables (assuming same for all)")

    (options, args) = parser.parse_args()

    filename = options.input_file
    var_width = int(options.var_width)
    out_figure = options.output_figure

    output = {}

    with open(filename, "r") as fin:
        # There must be an easier way to parse csvs
        reader = csv.reader(fin, delimiter=",")

        
        headers = next(reader)
        for i, header in enumerate(headers):
            headers[i] = header.strip()
            output[headers[i]] = []
        print(headers)

        for row in reader:

            for j, d in enumerate(row):
                output[headers[j]].append(int(d))

    
    figure = plt.figure()
    plt.plot(output["Step"], output["Step"], "b")
    plt.plot(output["Step"], output["Depth"], "r")
    plt.legend(["Step", "Loop Closure Size"])
    plt.title("Step vs Loop Closure Size")
    plt.savefig(out_figure)
