import os
from pathlib import Path
import logging

# Configure logging to output the time and the message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "End-to-end-Vine-Quality-ML-Project"

# List of all files and directories to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

# Loop through the list to create the directories and files
for filepath in list_of_files:
    filepath = Path(filepath) # Automatically handles path slashes based on the OS
    filedir, filename = os.path.split(filepath) # Separates folder path from the file name

    # Create directory if it does not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create the file if it does not exist or if it is completely empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # Creates an empty file
            logging.info(f"Creating empty file: {filepath}")

    # If the file exists and has content, skip it
    else:
        logging.info(f"{filename} already exists")