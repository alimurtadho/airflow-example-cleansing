from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hello world from first Airflow DAG!'

dag = DAG(  'dag_example', 
            description='Hello World DAG',
            schedule_interval='0 12 * * *',
            start_date=datetime(2021, 3, 20), catchup=False)

hello_operator = PythonOperator(task_id='example_dag', python_callable=print_hello, dag=dag)

hello_operator