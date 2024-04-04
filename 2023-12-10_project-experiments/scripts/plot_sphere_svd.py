import yaml
import sys
import os
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.realpath(__file__))
output_dir = script_dir + "/../output"

exp_names = ["identity", "ahat", "boundnorm", "extdiag", "selcholupdate2", "selcholupdate4"]

sphere_data = {}

for exp in exp_names:
    fname = output_dir + "/sphere_" + exp + ".yml"
    with open(fname, "r") as fin:
        sphere_data[exp] = yaml.full_load(fin)

    sigma = sphere_data[exp][592]["evals"]
    plt.plot(range(len(sigma)), sigma, label=exp)
    
plt.yscale("log")
plt.legend()
plt.show()



