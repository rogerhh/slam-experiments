import sys
from optparse import OptionParser
import csv
import numpy as np
import matplotlib.pyplot as plt
import re

def read_until(fin, match, keep=False, max_lines=-1):
    print(f"match = {match}")
    count = 0
    orig_pos = fin.tell()
    while True:
        pos = fin.tell()
        line = fin.readline()

        if not line:
            print(f"{match} not found in fin!")
            return False

        if match in line:
            print(f"{match} found in fin")
            print(line)
            if keep:
                fin.seek(pos)
            return True

        count += 1
        if count == max_lines:
            print(f"{match} not found in fin within {max_lines} lines!")
            fin.seek(orig_pos)
            return False

def read_data(fin, match):
    has_data = read_until(fin, match, keep=True, max_lines=10)
    if has_data:
        line = fin.readline()
        print(f"line = {line}")
        count = int(line.split("{")[0].split()[-2])
        avg = float(line.split("{")[-1].split()[0])
        return count, avg
    else:
        return 0, 0


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--infile", dest="infile", 
                      default=None, help="uartlog")
    parser.add_option("--outfig", dest="outfig", 
                      default=None, help="output figure path")

    (options, args) = parser.parse_args()

    infile = options.infile
    outfig = options.outfig

    plt.rcParams.update({'font.size': 35, 'axes.titlesize': "large", 'axes.labelsize': 'large'})
    plt.figure(figsize=(18, 7))

    frame_count = 0
    nonkey = {}
    key = {}
    back = {}
    pgo = {}

    pgo_acc = 0
    back_acc = 0
    key_acc = 0
    nonkey_acc = 0
    back_acc = 0

    last_nonkey_count = 0
    last_key_count = 0
    last_back_count = 0

    with open(infile, "r") as fin:
        while read_until(fin, "---"):

            pgo_count, pgo_avg = read_data(fin, "PGO Update")
            back_count, back_avg = read_data(fin, "VioBackend [ms]")
            nonkey_count, nonkey_avg = read_data(fin, "VioFrontend Frame")
            key_count, key_avg = read_data(fin, "VioFrontend Keyframe")
            frontend_count, frontend_avg = read_data(fin, "VioFrontend [ms]")

            if back_count != last_back_count:
                diff_count = back_count - last_back_count

                pgo_time = pgo_count * pgo_avg - pgo_acc
                pgo_acc = pgo_count * pgo_avg

                pgo[back_count] = pgo_time / diff_count

                back_time = back_count * back_avg - back_acc
                back_acc = back_count * back_avg

                back[back_count] = back_time / diff_count

                last_back_count = back_count

            if last_nonkey_count != nonkey_count:
                diff_count = nonkey_count - last_nonkey_count

                nonkey_time = nonkey_count * nonkey_avg - nonkey_acc
                nonkey_acc = nonkey_count * nonkey_avg

                nonkey[key_count] = nonkey_time / diff_count

                last_nonkey_count = nonkey_count


            if last_key_count != key_count:
                diff_count = key_count - last_key_count
                key_time = key_count * key_avg - key_acc
                key_acc = key_count * key_avg

                key[key_count] = key_time / diff_count

                last_key_count = key_count

            

    print(back)


    for d, label in zip([back, key, nonkey], ["Backend", "Frontend (Keyframe)", "Frontend (Non-Keyframe)"]):
        keys = sorted(d.keys())
        values = []
        for k in keys:
            values.append(d[k])
        plt.plot(keys, values, label=label, linewidth=4)

    plt.xlabel("Step")
    plt.ylabel("Latency (ms)")

    plt.legend()

    plt.savefig(outfig, bbox_inches="tight")

    exit(0)





    t = []
    PGO_count = 0
    PGO_acc = 0
    PGO = []
    frontend_count = 0
    frontend_acc = 0
    frontend = []
    backend_count = 0
    backend_acc = 0
    backend = []
    with open(infile, "r") as fin:
        while read_until(fin, "---"):
            t.append(len(t))

            has_pgo = read_until(fin, "PGO", keep=True, max_lines=10)

            if not has_pgo:
                PGO.append(0)
            else:
                line = fin.readline()

                count = int(line.split("{")[0].split()[-2])
                avg = float(line.split("{")[-1].split()[0])

                acc = count * avg
                countdiff = count - PGO_count
                accdiff = acc - PGO_acc

                PGO_time = 0 if countdiff == 0 else accdiff / countdiff
                
                PGO.append(accdiff)
                PGO_count = count
                PGO_acc = acc


            read_until(fin, "VioBackend [ms]", keep=True)
            line = fin.readline()

            count = int(line.split("{")[0].split()[-2])
            avg = float(line.split("{")[-1].split()[0])

            acc = count * avg
            countdiff = count - backend_count
            accdiff = acc - backend_acc

            backend_time = 0 if countdiff == 0 else accdiff / countdiff
            
            backend.append(accdiff)
            backend_count = count
            backend_acc = acc


            read_until(fin, "VioFrontend [ms]", keep=True)
            line = fin.readline()

            count = int(line.split("{")[0].split()[-2])
            avg = float(line.split("{")[-1].split()[0])

            acc = count * avg
            countdiff = count - frontend_count
            accdiff = acc - frontend_acc

            frontend_time = 0 if countdiff == 0 else accdiff / countdiff
            
            frontend.append(accdiff)
            frontend_count = count
            frontend_acc = acc

    plt.plot(t, frontend, label="Frontend time")
    plt.plot(t, backend, label="Backend time")
    plt.plot(t, PGO, label="Loop Closure time")

    plt.xlabel("Step")
    plt.ylabel("Latency (ms)")

    plt.legend()

    plt.savefig(outfig)
    

