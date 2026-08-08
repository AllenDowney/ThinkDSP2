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


## Run notebook tests (skip chap01: audio play can hang headless CI)
tests:
	cd soln; pytest --nbmake --nbmake-timeout=180 \
		chap02.ipynb chap03.ipynb chap04.ipynb chap05.ipynb \
		chap06.ipynb chap07.ipynb chap08.ipynb chap09.ipynb \
		chap10.ipynb chap11.ipynb
