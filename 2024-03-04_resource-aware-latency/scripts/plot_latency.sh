#!/bin/bash

set -e

SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
EXPERIMENT_DIR=$SCRIPT_DIR/..
OUTPUT_DIR=$EXPERIMENT_DIR/output

python3 $SCRIPT_DIR/plot_latency.py --input_files "$OUTPUT_DIR/run.out.no_contention $OUTPUT_DIR/run.out.contention $OUTPUT_DIR/run.out.partial.no_contention $OUTPUT_DIR/run.out.partial.contention "
