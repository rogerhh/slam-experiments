import sys
from optparse import OptionParser
import csv
import numpy as np
import matplotlib.pyplot as plt
import re

def read_until(fin, match):
    while True:
        line = fin.readline()

        if not line:
            print(f"{match} not found in fin!")
            exit(1)

        if match in line:
            break

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--real_infile", dest="real_infile", 
                      default=None, help="The output from firesim")
    parser.add_option("--model_indir", dest="model_indir", 
                      default=None, help="The directory that contains the cycle predictions")

    (options, args) = parser.parse_args()

    real_infile = options.real_infile
    model_indir = options.model_indir

    real_step_dict = {}
    model_step_dict = {}

    with open(real_infile, "r") as fin:
        step = None
        node = None

        read_until(fin, "mt_model")

        while True:
            line = fin.readline()

            if not line:
                break

            arr = line.split()

            if "step = " in line:
                step = int(arr[2])
                real_step_dict[step] = {}

            if " time: " in line:
                node_index = arr.index("node")
                node = int(arr[node_index + 1])

                if node not in real_step_dict[step].keys():
                    real_step_dict[step][node] = {}

                time_index = arr.index("time:")
                key = arr[time_index - 1]
                time_str = re.sub(r'\D', '', arr[time_index + 1])
                cycles = int(time_str)

                real_step_dict[step][node][key] = cycles


    key_to_name_mapping = {"AtA": "AtA", "cholCost": "chol", "addCost": "merge", "backsolveCost": "backsolve"}

    for step in real_step_dict.keys():
        model_infile = f"{model_indir}/step-{900}-pred_cycles.out"

        model_step_dict[step] = {}

        with open(model_infile, "r") as fin:
            while True:
                line = fin.readline()

                if not line:
                    break

                if "node" in line:
                    arr = line.split()
                    node_index = arr.index("node")
                    node = int(arr[node_index + 1])

                    if node not in model_step_dict[step].keys():
                        model_step_dict[step][node] = {}

                    for i, a in enumerate(arr):
                        if arr[i][-1] == ":":
                            key = arr[i][:-1]
                            real_key = key_to_name_mapping[key]
                            cycles = int(arr[i + 1])
                            model_step_dict[step][node][real_key] = cycles


    t = {}
    y = {}
    y_model = {}
    for step in real_step_dict.keys():
        if step not in model_step_dict.keys():
            print(f"step {step} not in model_step_dict")
            exit(1)

        for node in real_step_dict[step].keys():
            for key in real_step_dict[step][node].keys():
                if key not in t.keys():
                    t[key] = []
                if key not in y.keys():
                    y[key] = []
                    y_model[key] = []

                t[key].append(len(t[key]))
                y[key].append(real_step_dict[step][node][key])

                if node not in model_step_dict[step].keys() or key not in model_step_dict[step][node].keys():
                    y_model[key].append(0)
                else:
                    y_model[key].append(model_step_dict[step][node][key])


    for key in t.keys():
        plt.plot(t[key], y[key], label=f"real_{key}")
        plt.plot(t[key], y_model[key], label=f"model_{key}")
        plt.legend()
        plt.show()



    







