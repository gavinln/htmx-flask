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
edit:  ## edit with neovim and sessions
	poetry run nvim -S Session.vim

.PHONY: tailwind
tailwind:  ## tailwind watch
	tailwindcss -i tailwind_flaskr/static/css/input.css -o tailwind_flaskr/static/css/output.css -w -p

.PHONY: env-up
env-up:
	poetry install

.PHONY: env-rm
env-rm:
	poetry env remove $$(poetry env info -e)

.PHONY: run
run: env-up  ## run Flask app at http://127.0.0.1:5000/
	poetry run flask --app tailwind_flaskr run

.PHONY: serve
serve:  # serve application
	PYTHONPATH=$$SCRIPT_DIR poetry run waitress-serve --host 127.0.0.1 --call tailwind_flaskr:create_app

.PHONY: watch
watch:  # watch and serve application
	PYTHONPATH=$$SCRIPT_DIR watchexec -w . --poll 1s -r -- poetry run waitress-serve --host 127.0.0.1 --call tailwind_flaskr:create_app

.PHONY: clean
clean: env-rm  ## remove temporary files
	rm -f poetry.lock
	rm -rf dist/
	find . -name '.pytest_cache' -type d -exec rm -rf '{}' +
	find . -name '__pycache__' -type d -exec rm -rf '{}' +
	find . -name '.ruff_cache' -type d -exec rm -rf '{}' +
