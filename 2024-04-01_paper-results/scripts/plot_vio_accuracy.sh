#!/bin/bash

set -e

SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
EXP_DIR=$SCRIPT_DIR/..
OUTPUT_DIR=$EXP_DIR/output
BUILD_DIR=$HOME/gtsam-gemmini-integrate/build

OUTDIR1=$OUTPUT_DIR/vio-traj

mkdir -p $OUTDIR1

$BUILD_DIR/timing/testGtsamIncremental-vio -f w10000 --num_steps 100 --outdir $OUTDIR1

