#! /usr/bin/env bash

echo ">>> rm -rf venv"
rm -rf venv
echo ">>> rm -rf migrations"
rm -rf migrations
echo '>>> find . -type d -name "__pycache__" -exec rm -rf {} +'
find . -type d -name "__pycache__" -exec rm -rf {} +
