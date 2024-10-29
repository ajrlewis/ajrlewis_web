#! /usr/bin/env bash

source .env
source venv/bin/activate
fastapi dev wsgi.py
deactivate
