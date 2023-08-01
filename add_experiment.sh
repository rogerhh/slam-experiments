#!/bin/bash

set -e

SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
EXPERIMENT_DIR=$SCRIPT_DIR/$1

echo "Making experiment directory: ${EXPERIMENT_DIR}"

mkdir -p "$EXPERIMENT_DIR"

touch $EXPERIMENT_DIR/report.md
mkdir $EXPERIMENT_DIR/scripts
mkdir $EXPERIMENT_DIR/output
mkdir $EXPERIMENT_DIR/output/processed
mkdir $EXPERIMENT_DIR/data


