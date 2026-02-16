from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


#defining DAG arguments
default_args = {
    'owner': 'DE1',
    'start_date': datetime(2026, 2, 15),
    'email': ['your_email_here'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG
dag = DAG(
    dag_id = 'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule="@daily",
)

# define the tasks
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command="bash -c '/opt/airflow/scripts/unzip_data.sh'",
    dag=dag,
)

extract_data_from_csv = BashOperator(
    task_id = 'extract_data_from_csv',
    bash_command = "bash -c '/opt/airflow/scripts/extract_data_from_csv.sh'",
    dag= dag,
)

extract_data_from_tsv = BashOperator(
    task_id = 'extract_data_from_tsv',
    bash_command = "bash -c '/opt/airflow/scripts/extract_data_from_tsv.sh'",
    dag=dag,
)

extract_data_from_fixed_width = BashOperator(
    task_id = 'extract_data_from_fixed_width',
    bash_command = "bash -c '/opt/airflow/scripts/extract_data_from_fixed_width.sh'",
    dag=dag,
)

consolidate_data = BashOperator(
    task_id = 'consolidate_data',
    bash_command = "bash -c '/opt/airflow/scripts/consolidate_data.sh'",
    dag=dag,
)

transform_data = BashOperator(
    task_id = 'transform_data',
    bash_command = "bash -c '/opt/airflow/scripts/transform_data.sh'",
    dag=dag,
)

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data