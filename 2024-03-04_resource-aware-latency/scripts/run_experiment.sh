#!/bin/bash

set -e

SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
EXPERIMENT_DIR=$SCRIPT_DIR/..
OUTPUT_DIR=$EXPERIMENT_DIR/output
SRC_DIR=$HOME/igo-gtsam/build/

export MKL_NUM_THREADS=4

NUM_CONTENTION_ITER=130

# $SRC_DIR/timing/testGtsamIncremental -f w10000 --num_steps 3000 -e 0.1 | tee $OUTPUT_DIR/run.out.no_contention

$SRC_DIR/timing/testGtsamIncremental -f w10000 --num_steps 3000 -e 0.1 | tee $OUTPUT_DIR/run.out.contention & $SRC_DIR/timing/eigenBackground -n 2000 -i $NUM_CONTENTION_ITER

# time $SRC_DIR/timing/testGtsamIncremental-partial -f w10000 --num_steps 3000 -d 0 -e 0 -m 30 --vio_relin_keys 1 --max_relin_key 50 | tee $OUTPUT_DIR/run.out.partial.no_contention

# $SRC_DIR/timing/testGtsamIncremental-partial -f w10000 --num_steps 3000 --relin_thresh 0.1 -d 0 -e 0 -m 30 --vio_relin_keys 1 --max_relin_key 50 | tee $OUTPUT_DIR/run.out.partial.contention & $SRC_DIR/timing/eigenBackground -n 2000 -i $NUM_CONTENTION_ITER

