#! /usr/bin/env bash
set -e

python /app/app/worker_pre_start.py

rqworker --url $REDIS_URI
