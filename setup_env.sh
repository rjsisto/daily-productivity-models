#!/bin/bash

env_name=".venv"

python3 -m venv "$env_name"

source "$env_name/bin/activate"

pip install --upgrade pip
pip install -r packages/requirements.txt

deactivate 

echo "Python environment setup complete"