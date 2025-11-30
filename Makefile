# Makefile for easy development workflows.
# See development.md for docs.
# Note GitHub Actions call uv directly, not this Makefile.

.DEFAULT_GOAL := default

.PHONY: init default install lint test build clean 

default: install lint test 

.ONESHELL:
init:
	echo Changing module names to $(MODULE_NAME)
	find . -type f -print0 | xargs -0 sed -i 's/MY_MODULE/$(MODULE_NAME)/g'

install:
	uv sync --all-extras
	uv run maturin develop

lint:
	uv run ruff format
	uv run ruff check --fix

.ONESHELL:
test:
	. $(shell uv run devtools/find-python-activate.py)
	cargo test
	uv run pytest

build:
	uv build

clean:
	-rm -rf dist/
	-rm -rf *.egg-info/
	-rm -rf .pytest_cache/
	-rm -rf .mypy_cache/
	-rm -rf .venv/
	-rm -rf target/
	-rm -rf .ruff_cache/
	-find . -type d -name "__pycache__" -exec rm -rf {} +