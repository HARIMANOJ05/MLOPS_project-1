''' from asyncio import tasks
import json
from textwrap import dedent 
import pendulum
import os 
from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
    'batch_prediction',
    default_args={'retries':2},
    description='gemstone batch prediction pipeline ',
    schedule_interval='@weekly',
    start_date= pendulum.datetime(2024,1,9,tz='UTC'),
    catchup=False,
    tags=['daimond price prediction'],
)as dag:
    
    def download_files(**kwargs):
        bucket_name="gemstone_repo"
        input_dir="/app/input_files"
        #creating dir
        os.makedirs(input_dir,exist_ok=True)
        
    def batch_prediction(**kwargs):
        config = BatchPredictionConfig()
        sensor_batch_prediction =SensorBatchPrediction(batch_config=config)
        sensor_batch_prediction.start_prediction()

    def upload_files(**kwargs):
        #bucket_name= "gemstone-repo"

        download_input_files = PythonOperator(
            task_id='download_file',
            python_callable=download_files
        )

        generate_prediction_files = PythonOperator(
            task_id='preditction',
            python_callable=batch_prediction
        )

        upload_predicition_files = PythonOperator(
            task_id= "upload_prediction_files",
            python_callable=upload_files
        )
'''
