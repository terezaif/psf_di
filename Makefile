
.PHONY: setup
setup:
	pyenv local 3.8.7
	python -m venv .venv
	.venv/bin/python -m pip install -r requirements_dev.txt