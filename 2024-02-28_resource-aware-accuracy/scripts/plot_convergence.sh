#!/bin/bash

set -e

SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
EXPERIMENT_DIR=$SCRIPT_DIR/..
OUTPUT_DIR=$EXPERIMENT_DIR/output
DATA_DIR=$SCRIPT_DIR/data

python3 $SCRIPT_DIR/plot_convergence_rate.py --input_files "$OUTPUT_DIR/w10000_steps-3394_vio-1_relin-25.out $OUTPUT_DIR/w10000_steps-3394_vio-1_relin-50.out $OUTPUT_DIR/w10000_steps-3394_vio-1_relin-100.out $OUTPUT_DIR/w10000_steps-3394_vio-1_relin-2600.out"

# python3 $SCRIPT_DIR/plot_convergence_rate.py --input_files "$OUTPUT_DIR/sphere2500_steps-1000_vio-2_relin-25.out $OUTPUT_DIR/sphere2500_steps-1000_vio-2_relin-50.out $OUTPUT_DIR/sphere2500_steps-1000_vio-10_relin-100.out $OUTPUT_DIR/sphere2500_steps-1000_vio-2_relin-1000.out"

python3 $SCRIPT_DIR/plot_convergence_rate.py --input_files "$OUTPUT_DIR/parking-garage_steps-1654_vio-1_relin-10.out $OUTPUT_DIR/parking-garage_steps-1654_vio-1_relin-20.out $OUTPUT_DIR/parking-garage_steps-1654_vio-1_relin-30.out $OUTPUT_DIR/parking-garage_steps-1654_vio-1_relin-1600.out "
