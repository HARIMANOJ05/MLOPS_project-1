import os
import sys
import pickle
import pandas as pd
import numpy as np 
import mlflow
from urllib.parse import urlparse

from src.utils.utils import load_object
from src.logger.logging import logging
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from src.exception.exception import customexception

class ModelEvaluation:
    def __init__(self):
        logging.info(" performing model evalaution ")


    
    def eval_metrics(self,actual,pred):

        r2=r2_score(actual,pred)
        mae=mean_absolute_error(actual,pred)
        rmse=np.sqrt(mean_squared_error(actual,pred))

        logging.info("eval metrics captured")

        return r2,mae,rmse
    
    def intiate_model_evaluation(self,train_arr,test_arr):
        try:
            X_test,y_test=(test_arr[ : , :-1],test_arr[:,-1])

            model_path=os.path.join("artifacts","model.pkl")
            
            model=load_object(model_path)

            logging.info("model evaluation initiated")
            
            tracking_uri_type_store=urlparse(mlflow.get_tracking_uri()).scheme

            print(tracking_uri_type_store)

            with mlflow.start_run():

                predictions=model.predict(X_test)

                (r2,mae,rmse)=self.eval_metrics(y_test,predictions)

                mlflow.log_param('r2',r2)
                mlflow.log_param('mae',mae)
                mlflow.log_param('rmse',rmse)

                logging.info("parms obtained by mlruns")
                
                if tracking_uri_type_store != "file":
                    
                    mlflow.sklearn.log_model(model,'model', registerd_model_name='ml_model')

                else:
                    mlflow.sklearn.log_model(model,'model')
                    


        except Exception as e:
            raise customexception(e,sys)
        logging.info("exception occured in model evaluation module")
    