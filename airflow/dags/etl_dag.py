from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
dag = DAG('ecommerce_etl', start_date=datetime(2025,10,21), schedule_interval='@hourly')
# Tasks placeholder
