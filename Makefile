# Variables
PYTHON=./venv/bin/python
PIP=./venv/bin/pip
PYLINT=./venv/bin/pylint
PYTEST=./venv/bin/pytest

# Default target
.PHONY: all
all: lint test

# Set up virtual environment and install dependencies
.PHONY: setup
setup:
	python3 -m venv venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run the app
.PHONY: run
run:
	$(PYTHON) app.py

# Run tests using pytest
.PHONY: test
test:
	$(PYTEST) tests/

# Run linting using pylint
.PHONY: lint
lint:
	$(PYLINT) src/

# Clean cache and compiled files
.PHONY: clean
clean:
	rm -rf __pycache__ .pytest_cache .pylint.d *.pyc *.pyo

# Build Docker image
.PHONY: docker-build
docker-build:
	docker build -t churn-predictor .

# Run Docker container
.PHONY: docker-run
docker-run:
	docker run -d -p 8000:8000 churn-predictor
