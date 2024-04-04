#!/bin/bash

set -e

SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
EXPERIMENT_DIR=$SCRIPT_DIR/..
OUTPUT_DIR=$EXPERIMENT_DIR/output
SRC_DIR=$HOME/igo-gtsam/build/timing

num_steps=1000

# for (( vio_relin_keys = 1; vio_relin_keys <= 1; vio_relin_keys += 5 )); do
#   for (( max_relin_keys = 25; max_relin_keys <= 300; max_relin_keys += 25 )); do
#     echo ${vio_relin_keys} ${max_relin_keys}
#     $SRC_DIR/testGtsamIncremental3D-partial -f sphere2500 --num_steps ${num_steps} -e 0.001 -d 0 -m 50 --vio_relin_keys ${vio_relin_keys} --max_relin_keys ${max_relin_keys} > ${OUTPUT_DIR}/sphere2500_steps-${num_steps}_vio-${vio_relin_keys}_relin-${max_relin_keys}.out
#   done
# done

num_steps=3394

for (( vio_relin_keys = 1; vio_relin_keys <= 5; vio_relin_keys += 4 )); do
  for (( max_relin_keys = 25; max_relin_keys <= 300; max_relin_keys += 25 )); do
    echo ${vio_relin_keys} ${max_relin_keys}
    $SRC_DIR/testGtsamIncremental-partial -f w10000 --num_steps ${num_steps} -e 0.001 -d 0 -m 50 --vio_relin_keys ${vio_relin_keys} --max_relin_keys ${max_relin_keys} > ${OUTPUT_DIR}/w10000_steps-${num_steps}_vio-${vio_relin_keys}_relin-${max_relin_keys}.out
  done
done

