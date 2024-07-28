echo [$(date)] : "start"

echo [$(date)] :"creating a virtual environment"



python -m venv mlopvenv


echo [$(date)] :"activating virtual environment"

mlopvenv\Scripts\activate



echo [$(date)] :" virtual environment created "

pip install -r requirements_dev.txt

echo [$(date)] :" end "
