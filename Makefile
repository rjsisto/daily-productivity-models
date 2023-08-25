VENV = .venv
PYTHON = $(VENV)/bin/python3 #this is only for unix
PIP = $(VENV)/bin/pip #this is only for unix
export DATA_FOLDER=src/data
export MODEL_FOLDER=src/models

#TODO add a command to download the data and the models using dvc

help:
	@awk 'BEGIN {FS = ":.*##"; printf "\033[35m\033[0m"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$1, 5) } ' $(MAKEFILE_LIST)

##@  Environment
env: ## Create the virtual environment
	@python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "Python environment setup complete"

clean: ## Removes the existing virtual environment
	rm -rf $(VENV)
	@echo "Python virtual environment removed"


env-win:
	@echo "make windows environment"


##@ Jupyter

jup: ##Launch the Jupyter Notebook
	$(VENV)/bin/jupyter-lab

jup-win: 
	@echo "jupyter for windows"

build_models: ##Builds all of the models from the Jupyter Notebooks (will take a while)
	$(PYTHON) notebooks/create_models.py


##@ Dashboard

dash: ##Launch the Dashboard
	$(PYTHON) data_app/model_page.py


##@ Download SRC Files

download_data: ##Download the data files
	$(VENV)/bin/dvc pull src/data

download_models: ##Download the models
	$(VENV)/bin/dvc pull src/models



build:
	@echo "Hello"

