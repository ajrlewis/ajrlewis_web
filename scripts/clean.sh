#! /usr/bin/env bash

rm -rf venv
rm -rf alembic
rm alembic.ini
find . -type d -name "__pycache__" -exec rm -rf {} +
