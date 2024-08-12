import  os
import pandas  as pd
import sys 
import pickle
from src.exception.exception import customexception
from src.utils.utils import load_object
from src.logger.logging import logging
from sklearn.ensemble import RandomForestClassifier 




class Predictionpipeline:

    def __init__(self):
        print("prediction pipeline ... .. initiated")


    def predict(self,feature):
        try:
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model_path =os.path.join("artifacts","model.pkl")

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
           
            scaled_fea=preprocessor.transform(feature)
            print(type(scaled_fea))
            print(model)

            
            pred=model.predict(scaled_fea)

              


            return pred 
        
        
        
        except Exception as e:
            logging.info("exception occured in predict fun")

            raise customexception(e,sys)
        

class Customdata:
    def __init__(self,carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut=cut
        self.color=color
        self.clarity=clarity





    def get_data_as_dataframe(self):

        try:
            custom_prediction_data = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
                }
            
            df=pd.DataFrame(custom_prediction_data)

            logging.info("data gathered for prediction from user")
            return df
        except Exception as e:
            logging.info("error occured in prediction pipeline")

            raise customexception(e,sys)
        


