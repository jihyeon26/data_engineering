#!/usr/bin/env bash
set -euo pipefail

awk -F'\t' '{print $5 "," $6 "," $7}' /opt/airflow/data/tollplaza-data.tsv > /opt/airflow/data/tsv_data.csv