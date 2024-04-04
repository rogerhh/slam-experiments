#!/bin/bash

set -e

SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
DATA_DIR=$SCRIPT_DIR/../data
IGO_PYTHON_DIR=$HOME/igo/python

# python3 $IGO_PYTHON_DIR/main.py --params $SCRIPT_DIR/params.yml

python3 $IGO_PYTHON_DIR/main.py --params $SCRIPT_DIR/sphere_params.yml
# python3 $IGO_PYTHON_DIR/main.py --params $SCRIPT_DIR/sphere_params_pcg_selcholupdate2.yml

