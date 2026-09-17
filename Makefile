.DEFAULT_GOAL := help
.PHONY: help install hooks-install hooks-check generate generated-check format lint typecheck test build check check-all

help:
	@echo 'install | hooks-install | hooks-check | generate | generated-check | format | lint | typecheck | check | test | build | check-all'

install:
	uv sync --locked

hooks-install:
	uv run --locked pre-commit install

hooks-check:
	uv run --locked pre-commit run --all-files --show-diff-on-failure

generate:
	bash scripts/sync-contract.sh --check
	uv run --locked python codegen/generate.py

generated-check:
	bash scripts/sync-contract.sh --check
	uv run --locked python codegen/generate.py --check

format:
	git ls-files -z -- '*.md' ':!:contract/semantics/**' | xargs -0 uv run --locked mdformat --number
	uv run --locked ruff check --fix .
	uv run --locked ruff format .

lint:
	git ls-files -z -- '*.md' ':!:contract/semantics/**' | xargs -0 uv run --locked mdformat --check --number
	uv run --locked pre-commit validate-config
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

check-all: install hooks-check generated-check check test build
