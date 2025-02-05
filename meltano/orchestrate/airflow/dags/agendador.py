from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(
    'rodar_jobs_meltano',
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2025, 2, 4),  
        'retries': 1,
    },
    catchup=False,
) as dag:
    task_pg_csv_local = BashOperator(
        task_id='pg_csv_local',
        bash_command='cd /home/thiago/code-challenge/meltano && meltano run pg_csv_local',
    )

    task_csv_csv_local = BashOperator(
        task_id='csv_csv_local',
        bash_command='cd /home/thiago/code-challenge/meltano && meltano run csv_csv_local',
    )

    task_csv_postgres_externo = BashOperator(
        task_id='csv_postgres_externo',
        bash_command='cd /home/thiago/code-challenge/meltano && meltano run csv_postgres_externo',
    )

    
    [task_pg_csv_local, task_csv_csv_local] >> task_csv_postgres_externo
