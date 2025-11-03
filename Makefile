PROJECT_NAME = ThinkDSP2
PYTHON_VERSION = 3.12
PYTHON_INTERPRETER = python



## Set up Python environment
create_environment:
	conda create -y --name $(PROJECT_NAME) python=$(PYTHON_VERSION)
	@echo ">>> conda env created. Activate with:\nconda activate $(PROJECT_NAME)"


## Install dependencies
requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt


tests:
	cd soln; pytest --nbmake chap*.ipynb
