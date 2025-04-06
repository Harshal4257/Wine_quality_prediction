echo [$(date)]: "Start"

echo [$(date)]: "Creating enviorment with python 3.9"

conda create --prefix ./env python=3.9 -y

echo [$(date)]: "Activating the enviorment"

source activate ./env

echo [$(date)]: "Installing the requirements"

pip install -r requirements.txt

echo [$(date)]: "End"