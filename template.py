import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'Text_Summarizer'

list_files = [
    ".github/workflows/.gitkeep",
    f'src/{project_name}/__init__.py', #Acts like local package in order to import files from other folders or directories
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    "config/config.yml",
    "params.yml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for filepath in list_files:
    filepath = Path(filepath)
    filedir, filepath = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info("Creating directory:{filedir} for the file {filename}")
    
    if (not os.path.exists(filepath or(os.path.getsize(filepath) == 0))):
        with open(filepath, 'w') as f:
            pass
            logging.info("Creating empty file: {filepath}")

    else:
        logging.info("{filename} already exists")



