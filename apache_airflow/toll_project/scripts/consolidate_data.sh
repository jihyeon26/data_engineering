#!/usr/bin/env bash
set -euo pipefail

paste -d"," /opt/airflow/data/csv_data.csv /opt/airflow/data/tsv_data.csv /opt/airflow/data/fixed_width_data.csv > /opt/airflow/data/extracted_data.csv