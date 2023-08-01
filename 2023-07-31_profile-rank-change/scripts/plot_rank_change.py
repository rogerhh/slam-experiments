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
                      default="", help="The filename for hte output graph")
    parser.add_option("--select_period", dest="select_period", 
                      default="200", help="The period at which to select 'loop closure steps'")

    (options, args) = parser.parse_args()

    filename = options.input_file
    var_width = int(options.var_width)
    out_figure = options.output_figure
    select_period = int(options.select_period)

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

    if out_figure != "":
        plt.savefig(out_figure + ".png")

    # Select the highest percentage depth every select_period steps
    max_steps = []
    max_depths = []
    max_is = []
    for start_i in range(0, len(output["Step"]), select_period):
        max_percentage_depth = 0
        max_step = 0
        max_i = 0
        max_depth = 0
        for i in range(start_i, min(start_i + select_period, len(output["Step"]))):
            depth = output["Depth"][i]
            step = output["Step"][i]
            percentage_depth = depth / step            
            if percentage_depth >= max_percentage_depth:
                max_percentage_depth = percentage_depth
                max_step = step
                max_i = i
                max_depth = depth
        max_steps.append(max_step)
        max_is.append(max_i)
        max_depths.append(max_depth)

    print(max_steps)
    print(max_depths)

    plt.plot(max_steps, max_depths, 'ro', markersize=10, mfc='none')
    if out_figure != "":
        plt.savefig(out_figure + "_selected.png")

            
