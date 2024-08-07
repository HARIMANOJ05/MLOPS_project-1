import  os
import pandas as pd
import sys
from src.exception.exception import customexception
from src.utils.utils import load_object
from src.logger.logging import logging


class Predictionpipeline:

    def __init__(self):
        print("prediction pipeline ... .. initiated")


    def predict(self,feature):
        try:
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            scaled_features=preprocessor.transform(feature)
            pred=model.predict(scaled_features)

            return pred 
        
        
        
        except Exception as e:


            raise customexception
        

class customdata:
    def __init__(self):
        pass



    def get_data_as_dataframe():
        pass

