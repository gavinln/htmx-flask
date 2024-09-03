SCRIPT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

SHELL = /bin/bash

# highlight the Makefile targets
# @grep -E '^[a-zA-Z0-9_\-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: help
.DEFAULT_GOAL=help
help:  ## help for this Makefile
	@grep -E '^[a-zA-Z0-9_\-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: fix
fix:  ## run isort and ruff on python code
	ruff check --fix
	nixfmt flake.nix

.PHONY: edit
edit:
	poetry run nvim -S Session.vim

.PHONY: env-up
env-up:
	poetry install

.PHONY: env-rm
env-rm:
	poetry env remove $$(poetry env info -e)

.PHONY: run
run: env-up  ## run Flask app at http://127.0.0.1:5001/
	poetry run flask --app flaskr run -p 5001

.PHONY: debug
debug: env-up  ## debug Flask app at http://127.0.0.1:5001/
	poetry run flask --debug --app flaskr run -p 5001

.PHONY: djhtml
djhtml: env-up  ## format templates
	poetry run djhtml flaskr/templates/

.PHONY: clean
clean: env-rm  ## remove temporary files
	rm -f poetry.lock
	rm -rf dist/
	find . -name '.pytest_cache' -type d -exec rm -rf '{}' +
	find . -name '__pycache__' -type d -exec rm -rf '{}' +
	find . -name '.ruff_cache' -type d -exec rm -rf '{}' +
