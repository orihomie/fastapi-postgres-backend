#! /usr/bin/env bash
set -e

python /app/app/worker_pre_start.py

rqworker -w app.worker.worker
