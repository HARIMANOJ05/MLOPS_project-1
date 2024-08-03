from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import os 
import pandas as pd
import numpy as np 
import sys
import pickle
import mlflow
import mlflow.sklearn
from urllib.parse import urlparse
from src.utils.utils import load_object
from src.exception.exception import customexception
from dataclasses import dataclass
@dataclass
class ModelevaluationConfig:
    pass


   

class Modelevaluation:
     
    def __init__(self):
        pass

    def initiate_model_evaluation():
        try:
            pass
        except Exception as e:
            raise customexception(e,sys)