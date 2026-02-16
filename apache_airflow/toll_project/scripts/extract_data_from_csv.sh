#!/usr/bin/env bash
set -euo pipefail

cut -d"," -f1,2,3,4 /opt/airflow/data/vehicle-data.csv > /opt/airflow/data/csv_data.csv