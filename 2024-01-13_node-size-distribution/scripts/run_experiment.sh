#!/bin/bash

SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
EXPERIMENT_DIR=$SCRIPT_DIR/..
OUTPUT_DIR=$EXPERIMENT_DIR/output
PROCESSED_DIR=$EXPERIMENT_DIR/output/processed
DATA_DIR=$EXPERIMENT_DIR/data

BUILD_DIR=~/gtsam-gemmini-integrate/build

cd $BUILD_DIR

# make -j4 timing && ./timing/testGtsamIncremental -f w10000 --num_steps 10000 --node_dist_file "$OUTPUT_DIR/w10000_node_sizes.csv"

make -j4 timing && ./timing/testGtsamIncremental3D -f sphere2500 --node_dist_file "$OUTPUT_DIR/sphere2500_node_sizes.csv"
