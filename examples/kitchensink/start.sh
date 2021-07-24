#!/bin/sh
set -eu
cd $(dirname $0)

docker-compose up -d

export PYTHONPATH="../../"

python ./app.py
