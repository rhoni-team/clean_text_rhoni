SHELL := /bin/bash

.PHONY: test
test:
	poetry run pytest ./tests

.PHONY: lint
lint:
	poetry run autopep8 --recursive ./src && \
	poetry run autopep8 --recursive ./tests && \
	poetry run pylint ./src ./tests || true
