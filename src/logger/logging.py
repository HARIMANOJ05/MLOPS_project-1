import logging
import os 
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%d,%m,%y,%H')}.log"

log_path=os.path.join(os.getcwd(),"logs")

os.makedirs(log_path,exist_ok=True)

LOG_FILEPATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    filename=LOG_FILEPATH

)

