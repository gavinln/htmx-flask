SCRIPT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

SHELL = /bin/bash

# highlight the Makefile targets
# @grep -E '^[a-zA-Z0-9_\-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: help
.DEFAULT_GOAL=help
help:  ## help for this Makefile
	@grep -E '^[a-zA-Z0-9_\-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: tmux
tmux:  ## run tmux
	tmuxp load .tmuxp.yaml

.PHONY: fix
fix:  ## run isort and ruff on python code
	ruff check --fix
	nixfmt flake.nix

.PHONY: env-up
env-up:
	poetry install

.PHONY: env-rm
env-rm:
	poetry env remove $$(poetry env info -e)

.PHONY: flaskr-run
flaskr-run: env-up  ## run Flask app at http://127.0.0.1:5000/hello
	poetry run flask --app flaskr run

.PHONY: flaskr-init-db
flaskr-init-db: env-up  ## initliaze databsae
	poetry run flask --app flaskr init-db

.PHONY: flaskr-help
flaskr-help: env-up  ## flaskr commands help
	poetry run flask --app flaskr --help

.PHONY: flaskr-routes
flaskr-routes: env-up  ## flaskr routes
	poetry run flask --app flaskr routes

.PHONY: clean
clean: env-rm  ## remove temporary files
	rm -f poetry.lock
	rm -rf dist/
	find . -name '.pytest_cache' -type d -exec rm -rf '{}' +
	find . -name '__pycache__' -type d -exec rm -rf '{}' +
	find . -name '.ruff_cache' -type d -exec rm -rf '{}' +
