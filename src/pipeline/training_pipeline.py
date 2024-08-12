import os
import sys
from src.logger.logging import logging
from src.exception.exception import customexception
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_tainer import Modeltrainer
from src.components.model_evaluation import ModelEvaluation



obj=DataIngestion()

train_data_path,test_data_path=obj.initiate_data_ingestion()

data_transformation=DataTransformation()

train_arr,test_arr=data_transformation.initiate_data_transformation(train_data_path,test_data_path)


model_trainer_obj=Modeltrainer()
model_trainer_obj.initiate_model_trainer(train_arr,test_arr)

model_evaluation_obj=ModelEvaluation()
model_evaluation_obj.intiate_model_evaluation(train_arr,test_arr)
