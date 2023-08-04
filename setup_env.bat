@echo off

set env_name=.venv

python -m venv %env_name%

%env_name%\Scripts\activate

pip install -r requirements.txt

deactivate

echo Python environment setup complete
