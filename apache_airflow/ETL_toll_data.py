from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

#defining DAG arguments
default_args = {
    'owner': 'DE1',
    'start_date': days_ago(0),
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
    schedule_interval=timedelta(days=1),
)

# define the tasks
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xvzf /home/project/airflow/dags/finalassignment/tolldata.tgz',
    dag=dag,
)

extract_data_from_csv = BashOperator(
    task_id = 'extract_data_from_csv',
    bash_command = 'cut -d"," -f1,2,3,4 vehicle-data.csv > csv_data.csv',
    dag= dag,
)

extract_data_from_tsv = BashOperator(
    task_id = 'extract_data_from_tsv',
    bash_command = "cut -d $'\\t' -f4,5,6 tollplaza-data.tsv > tsv_data.csv",
    dag=dag,
)

extract_data_from_fixed_width = BashOperator(
    task_id = 'extract_data_from_fixed_width',
    bash_command = 'cut -d " " -f6,7 payment-data.txt > fixed_width_data.csv',
    dag=dag,
)

consolidate_data = BashOperator(
    task_id = 'consolidate_data',
    bash_command = 'paste -d"," csv_data.csv tsv_data.csv fixed_width_data.csv > extracted_data.csv',
    dag=dag,
)

transform_data = BashOperator(
    task_id = 'transform_data',
    bash_command = 'tr "[a-z]" "[A-Z]" < extracted_data.csv > transformed_data.csv ',
    dag=dag,
)

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data