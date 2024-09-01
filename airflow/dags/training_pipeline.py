from __future__ import annotations
import pendulum
import json

from textwrap import dedent
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.pipeline.training_pipeline import Trainingpipeline

training_pipeline=Trainingpipeline()

with DAG (
    dag_id= "project_training_pipeline",
    default_args={"retries":2},
    description="training pipeline",
    schedule="@weekly",
    start_date=pendulum.datetime(2024,8,19,tz="UTC"),
    catchup=False,
    tags=["machine learning","classification","gemstone"],

) as dag:
    
    dag.doc_md=__doc__


    def data_ingestion(**Kwargs):
        ti=Kwargs["ti"]
        train_data_path,test_data_path=training_pipeline.start_data_ingestion()
        ti.xcom_push('data_ingestion_artifact',{'train_data_path':train_data_path,'test_data_path':test_data_path})
    

    def data_transformation(**Kwargs):
        ti=Kwargs['ti']
        data_ingestion_artifact= ti.xcom_pull(task_ids="data_ingestion",key="data_ingestion_artifact")
        train_arr, test_arr = training_pipeline.start_data_transformation(
        data_ingestion_artifact['train_data_path'], 
        data_ingestion_artifact['test_data_path'])
                                                    

        train_arr=train_arr.tolist()
        test_arr=test_arr.tolist()
        ti.xcom_push('data_transformation_artifact',{'train_arr':train_arr,"test_arr":test_arr})

    def model_trainig(**Kwargs):
        import numpy as np
        ti=Kwargs["ti"]
        
        data_transformation_artifact=ti.xcom_pull(task_ids="data_transformation",key="data_transformation_artifact")
        train_arr=np.array(data_transformation_artifact['train_arr'])
        test_arr=np.array(data_transformation_artifact['test_arr'])
        training_pipeline.start_model_training(train_arr,test_arr)

    def push_data_to_s3():
        import os
        bucket_name=os.getenv("BUCKET_NAME")
        artifact_folder='/app/artifacts'
        os.system(f"aws s3 sync {artifact_folder} s3:/{bucket_name}/artifact")


    data_ingestion_task=PythonOperator(
        task_id='data_ingestion',
        python_callable=data_ingestion
    )
    data_ingestion_task.doc_md=dedent(
        """\
        ### data_ingestion
        creates train and test file
        """
    )

    data_transformation_task=PythonOperator(
        task_id='data_transformation',
        python_callable=data_transformation
    )
    data_transformation_task.doc_md=dedent(
        """\
        ### data_transformation
        performs data trandformation
        """
    )


    model_trainer_task=PythonOperator(
        task_id='model_training',
        python_callable=model_trainig
    )
    model_trainer_task.doc_md=dedent(
        """\
        ### model training
        performs model training 
        """
    )


    push_data_model_task=PythonOperator(
        task_id='push_data_to_s3',
        python_callable=push_data_to_s3
    )
    

data_ingestion_task >> data_transformation_task >> model_trainer_task >> push_data_model_task



