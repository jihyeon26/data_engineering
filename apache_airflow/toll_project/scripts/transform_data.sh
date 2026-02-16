#!/usr/bin/env bash
set -euo pipefail

tr "[a-z]" "[A-Z]" < /opt/airflow/data/extracted_data.csv > /opt/airflow/data/transformed_data.csv