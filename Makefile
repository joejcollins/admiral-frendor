# Consistent set of make tasks.
.DEFAULT_GOAL:=help  # because it's is a safe task.

ap-dummy: # run the dummy ansible playbook
	.venv/bin/ansible-playbook ./playbooks/dummy.yml

clean: # Remove the environment.
	rm -rf .venv
	rm -rf *.egg-info
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete
	rm -rf .collections

.PHONY: docs
docs: # Serve the documentation.
	.venv/bin/mkdocs serve

.PHONY: help
help: # Show help for each of the makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

lint:  # Lint the code with ruff.
	.venv/bin/ruff check ./src ./tests
	.venv/bin/yamllint --config-file .yamllint.yml ./playbooks
	.venv/bin/ansible-lint ./playbooks

lock:  # Update the lock file from pyproject.toml.
	uv lock

publish: # Publish the documentation.
	.venv/bin/mkdocs gh-deploy --force --verbose

report:  # Report the python version and pip list.
	.venv/bin/python --version
	uv pip list -v
	.venv/bin/ansible-galaxy collection list

test:  # Run tests.
	.venv/bin/pytest ./tests --verbose --color=yes --capture=no
	.venv/bin/pytest --cov=src

venv:  # Create the virtual environment.
	uv venv .venv --clear
	uv sync --frozen
	.venv/bin/ansible-galaxy collection install --collections-path ./.collections --requirements-file ./requirements.yml
	.venv/bin/ansible-galaxy role install --roles-path ./.roles --role-file ./requirements.yml
