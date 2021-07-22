#!/bin/sh
set -eu
cd $(dirname $0)

pytest -s --cov=line_botkit --cov-report=html
