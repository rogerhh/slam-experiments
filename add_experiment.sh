#!/bin/bash

set -e

SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
EXPERIMENT_DIR=$SCRIPT_DIR/$1

echo "Making experiment directory: ${EXPERIMENT_DIR}"

mkdir -p "$EXPERIMENT_DIR"

cp -r $SCRIPT_DIR/template/* $EXPERIMENT_DIR

