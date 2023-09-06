#!/bin/bash

SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
EXPERIMENT_DIR=$SCRIPT_DIR/..
OUTPUT_DIR=$EXPERIMENT_DIR/output
PROCESSED_DIR=$EXPERIMENT_DIR/output/processed
DATA_DIR=$EXPERIMENT_DIR/data
SRC_DIR=~/igo-gtsam/python/gtsam/examples

cd $SRC_DIR

for l in {1..5}
do
  python3 IncrementalSystemSolver_onlyRelin.py -f w10000 --solver iterative --lc_steps_file ~/slam-experiments/2023-07-31_profile-rank-change/data/w10000_selected_steps.txt --lc_lookahead $l | tee $OUTPUT_DIR/w10000_lookahead-"$l".out
done
