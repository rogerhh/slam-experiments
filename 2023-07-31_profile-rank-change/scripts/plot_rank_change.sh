#!/bin/bash

set -e

SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
EXPERIMENT_DIR=$SCRIPT_DIR/..
OUTPUT_DIR=$EXPERIMENT_DIR/output
PROCESSED_DIR=$EXPERIMENT_DIR/output/processed
DATA_DIR=$EXPERIMENT_DIR/data

python3 $SCRIPT_DIR/plot_rank_change.py --input_file $OUTPUT_DIR/w10000_rank_change.out --var_width 3 --output_figure $DATA_DIR/w10000_step_vs_change_rank.png
