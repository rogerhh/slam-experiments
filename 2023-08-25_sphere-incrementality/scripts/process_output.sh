#!/bin/bash

SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
EXPERIMENT_DIR=$SCRIPT_DIR/..
OUTPUT_DIR=$EXPERIMENT_DIR/output
PROCESSED_DIR=$EXPERIMENT_DIR/output/processed
DATA_DIR=$EXPERIMENT_DIR/data
SRC_DIR=~/igo-gtsam/python/gtsam/examples

python3 $SCRIPT_DIR/process_output.py -f $OUTPUT_DIR/w10000_extdiag_lookahead-1_withLinOps.out

