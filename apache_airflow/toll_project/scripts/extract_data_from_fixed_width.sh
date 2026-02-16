#!/usr/bin/env bash
set -euo pipefail

awk '{print $(NF-1) "," $NF}' /opt/airflow/data/payment-data.txt > /opt/airflow/data/fixed_width_data.csv