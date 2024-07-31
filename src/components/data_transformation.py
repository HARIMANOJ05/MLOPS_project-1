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




@dataclass
class DataTransformationConfig:
    pass


   

class DataTransformation:
     
    def __init__(self):
        pass

    def initiate_data_ingestion():
        try:
            pass
        except Exception as e:
            raise customexception(e,sys)