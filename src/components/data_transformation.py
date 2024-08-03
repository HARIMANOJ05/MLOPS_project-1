from src.logger.logging import logging
from src.exception.exception import customexception
import os 
import pandas as pd
import numpy as np 
import sys
from dataclasses import dataclass
from pathlib import Path

from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from src.utils.utils import save_object




@dataclass
class DataTransformationConfig:
    preprocessor_obj_filepath=os.path.join('artifacts','preprocessor.pkl')
                                           


   

class DataTransformation:
    def __init__(self):
        self.data_transformation_config= DataTransformationConfig()

    

    def get_data_transforamtion(self):
        try:

            logging.info("data transformation intiated")

            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
                
            
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
                
            logging.info('Pipeline Initiated')
                
            
            num_pipeline=Pipeline(
                    steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())

                    ]

                )
                
            
            cat_pipeline=Pipeline(
                    steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                    ('scaler',StandardScaler())
                    ]

                )
                
            preprocessor=ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_cols),
                ('cat_pipeline',cat_pipeline,categorical_cols)
                ])
                
            return preprocessor
        except Exception as e:
        
            logging.info("Exception occured in the initiate_datatransformation")
            raise customexception(e,sys)
            

    
    
    
       
    def initiate_data_transformation(self,train_path,test_path):
        try:

            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("read train and test data complete")
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head : \n{test_df.head().to_string()}')


            preprocessor_obj = self.get_data_transforamtion()


            target_column='price'
            drop_column=[target_column,'id']

            input_feature_train_df=train_df.drop(columns=drop_column,axis=1)
            target_feature_train_df=train_df['price']

            input_feature_test_df=train_df.drop(columns=drop_column,axis=1)
            target_feature_test_df=train_df['price']


            input_feature_train_df_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_df_arr=preprocessor_obj.transform(input_feature_test_df)

            logging.info("Applying preprocessing object on training and testing datasets.")
            
            train_arr = np.c_[input_feature_train_df_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_df_arr, np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_filepath,
                obj=preprocessor_obj
            )
            
            logging.info("preprocessing pickle file saved")
            
            return (
                train_arr,
                test_arr
            )


  
        except Exception as e:
            logging.info("exception occured  in data transformation file ")
            raise customexception(e,sys)