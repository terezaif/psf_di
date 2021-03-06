
.PHONY: setup
setup:
	pyenv local 3.8.5
	python -m venv .venv
	.venv/bin/python -m pip install -r requirements.txt