#!/bin/sh
set -eu
cd $(dirname $0)

export PYTHONPATH="../../"

python ./app.py
