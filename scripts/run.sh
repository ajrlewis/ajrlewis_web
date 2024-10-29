#! /usr/bin/env bash

source .env
source venv/bin/activate
fastapi dev src/main.py
deactivate
