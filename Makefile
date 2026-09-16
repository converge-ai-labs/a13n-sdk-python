.DEFAULT_GOAL := help
.PHONY: help install generate generated-check format lint typecheck test build check check-all

help:
	@echo 'install | generate | generated-check | format | check | test | build | check-all'

install:
	uv sync --locked

generate:
	bash scripts/sync-contract.sh --check
	uv run --locked python codegen/generate.py

generated-check:
	bash scripts/sync-contract.sh --check
	uv run --locked python codegen/generate.py --check

format:
	uv run --locked ruff check --fix .
	uv run --locked ruff format .

lint:
	uv lock --check
	uv run --locked ruff check --no-fix .
	uv run --locked ruff format --check .

typecheck:
	uv run --locked pyright

test:
	uv run --locked python -m pytest

build:
	uv build --no-build-isolation

check: lint typecheck

check-all: install generated-check check test build
