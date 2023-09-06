
import sys
from optparse import OptionParser
import random
from copy import deepcopy

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--input_file", "-f", dest="input_file",
                      default="", help="The path of the file containing the output.")
    (options, args) = parser.parse_args()

    infile = options.input_file

    with open(infile, "r") as fin:
        while True:
            line = fin.readline()

            if not line:
                break

            arr = line.split()

            if "step = " in line:
                step = int(arr[-1])

            elif "Matrix size" in line:
                m_size = int(arr[-1].strip(")"))

            elif "Relin rank: " in line:
                relin_rank = int(arr[-1])

            elif "Observe rank: " in line:
                obs_rank = int(arr[-1])

            elif "before conditioning" in line:
                cond_before = float(arr[-1])

            elif "after conditioning" in line:
                cond_after = float(arr[-1])

            elif "cg_count" in line:
                cg_count = int(arr[-1])

                print(f"At step {step}, matrix size = {m_size}, relin rank = {relin_rank}, obs rank = {obs_rank}, cond_before = {cond_before}, cond_after = {cond_after}, cg_count = {cg_count} ")

