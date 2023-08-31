#!/bin/bash

SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
EXPERIMENT_DIR=$SCRIPT_DIR/..
OUTPUT_DIR=$EXPERIMENT_DIR/output
PROCESSED_DIR=$EXPERIMENT_DIR/output/processed
DATA_DIR=$EXPERIMENT_DIR/data
SRC_DIR=~/igo-gtsam/python/gtsam/examples

cd $SRC_DIR

pu_types=$1

echo $pu_types

for t in $pu_types
do
  for l in 1
  do
    python3 IncrementalSystemSolver3D.py -f sphere2500 --solver iterative --lc_steps_file ${DATA_DIR}/sphere_selected_steps.txt --preconditioner_type "$t" --lc_lookahead $l | tee $OUTPUT_DIR/sphere_bignoise_vertex3_"$t"_lookahead-"$l"_withLinOps.out
  done
done
