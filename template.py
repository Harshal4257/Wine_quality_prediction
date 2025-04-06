import os
from pathlib import Path

package_name = "winequalitypred"

list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_evaluation.py",
    f"src/{package_name}/components/model_trainer.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/training_pipeline.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/utils/__init__.py",
    "notebooks/research.ipynb",
    "notebooks/EDA.ipynb",
    "notebooks/model_training.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "setup.py",
    "init_setup.sh",
]

for files in list_of_files:
    files = Path(files)
    filedir,filename = os.path.split(files)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(files)) or (os.path.getsize(files) == 0):
        with open(files,"w")as f:
            pass
    else:
        print("File already exists")