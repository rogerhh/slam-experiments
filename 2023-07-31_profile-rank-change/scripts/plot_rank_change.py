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
    parser.add_option("--dataset_name", dest="dataset_name", 
                      default="", help="The name of the dataset used for output files")
    parser.add_option("--data_dir", dest="data_dir", 
                      default="", help="The directory to store the figures.")
    parser.add_option("--select_period", dest="select_period", 
                      default="200", help="The period at which to select 'loop closure steps'")
    parser.add_option("--plot", dest="plot", action="store_true",
                      default=False, help="Whether or not to plot figures.")
    parser.add_option("--save", dest="save", action="store_true",
                      default=False, help="Whether or not to save figures.")

    (options, args) = parser.parse_args()

    filename = options.input_file
    var_width = int(options.var_width)
    dataset_name = options.dataset_name
    data_dir = options.data_dir
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
    plt.plot(output["Step"], output["Total affected keys"], "r")
    plt.plot(output["Step"], output["Relinearize affected keys"], "g")
    plt.plot(output["Step"], output["New factors affected keys"], "y")
    plt.legend(["Step", "Total affected rank", "Relinearize rank", "New factors rank"])
    plt.title("Step vs Rank of Affected Matrix")

    out_figure = data_dir + "/" + dataset_name + "_step_vs_affected_rank.png"
    if options.plot:
        plt.show()
    if options.save:
        plt.savefig(out_figure)

    # Select the highest percentage depth every select_period steps
    max_steps = []
    max_affecteds = []
    max_is = []
    for start_i in range(0, len(output["Step"]), select_period):
        max_percentage_affected = 0
        max_step = 0
        max_i = 0
        max_affected = 0
        for i in range(start_i, min(start_i + select_period, len(output["Step"]))):
            affected = output["Total affected keys"][i]
            step = output["Step"][i]
            percentage_affected = affected / step            
            if percentage_affected >= max_percentage_affected:
                max_percentage_affected = percentage_affected
                max_step = step
                max_i = i
                max_affected = affected
        max_steps.append(max_step)
        max_is.append(max_i)
        max_affecteds.append(max_affected)

    print(max_steps)
    print(max_affecteds)

    plt.plot(max_steps, max_affecteds, 'ro', markersize=10, mfc='none')

    out_figure = data_dir + "/" + dataset_name + "_step_vs_affected_rank_selected.png"

    if options.plot:
        plt.show()
    if options.save:
        plt.savefig(out_figure)

    selected_filename = data_dir + "/" + dataset_name + "_selected_steps.txt"

    with open(selected_filename, "w") as fout:
        fout.write(dataset_name + " SELECTED LOOP CLOSURE STEPS:\n")
        fout.write(f"NUM_STEPS: {len(max_steps)}\n")
        for step in max_steps:
            fout.write(f"{step} ")

            
