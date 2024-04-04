#!/bin/bash

set -e

SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
EXPERIMENT_DIR=$SCRIPT_DIR/..
OUTPUT_DIR=$EXPERIMENT_DIR/output
BUILD_DIR=$HOME/gtsam-gemmini-integrate/build

num_steps=100


dirname=incremental_w10000_steps-${num_steps}
mkdir -p ${OUTPUT_DIR}/${dirname}
echo ${OUTPUT_DIR}/${dirname}
$BUILD_DIR/timing/testGtsamIncremental-datasetgen -f w10000 --num_steps $num_steps --dataset_outdir "${OUTPUT_DIR}/${dirname}"

dirname=incremental_sphere2500_steps-${num_steps}
mkdir -p ${OUTPUT_DIR}/${dirname}
echo ${OUTPUT_DIR}/${dirname}
$BUILD_DIR/timing/testGtsamIncremental3D-datasetgen -f sphere2500 --num_steps $num_steps --dataset_outdir "${OUTPUT_DIR}/${dirname}"
