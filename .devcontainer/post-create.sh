#!/bin/sh

# This script is run after the container is created.
make clean
make venv

# Install pre-commit hooks
.venv/bin/pre-commit install

# Ansible will ignore the ansible.cfg it if is in a world writeable directory.
chmod 700 ./
