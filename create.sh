#!/bin/bash

# Define your project name and virtual environment name
PROJECT_NAME="familles"
VENV_NAME="venv"

# Create a virtual environment
python3 -m venv $VENV_NAME

# Activate the virtual environment
source $VENV_NAME/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Start Django development server
python manage.py runserver