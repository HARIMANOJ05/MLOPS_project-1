from src.logger.logging import logging
from src.exception.exception import customexception
import os 
import pandas as pd
import numpy as np 
import sys
from dataclasses import dataclass
from pathlib import Path

from src.utils.utils import save_object,evaluate_model
from sklearn.linear_model import Lasso,LinearRegression,Ridge
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from xgboost import XGBRFRegressor
from sklearn.ensemble import RandomForestRegressor
from src.components.data_transformation import DataTransformationConfig


@dataclass
class ModeltrainerConfig:
    trainer_file_path=os.path.join("artifacts","model.pkl")


   

class Modeltrainer :
     
    def __init__(self):

        self.model_trainer_config=ModeltrainerConfig()

    def initiate_model_trainer(self,train_arr,test_arr):
        try:
            logging.info("train test data appended")
            X_train,y_train,X_test,y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1],

            )

            
            models={

            "lasso":Lasso(),
            "Ridge":Ridge(),
            "linear_regression":LinearRegression(),
            "xgboost":XGBRFRegressor(),
            "randomforest": RandomForestRegressor()
         }
            
            model_report:dict=evaluate_model( X_train,y_train,X_test,y_test,models)
            print(model_report)

            logging.info(f'Model Report : {model_report}')

            best_model_score=max(sorted(model_report.values()))
            
            best_model=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            print(f'high performing model is {best_model}, with r2 score of {best_model_score}')
            logging.info(f'Best Model Found , Model Name : {best_model} , R2 Score : {best_model_score}')



            save_object(
                
                file_path=self.model_trainer_config.trainer_file_path,
                obj=best_model)
            
            
   
            
        except Exception as e:
            raise customexception(e,sys)