#!/bin/bash

# Create necessary directories
mkdir -p uploads
export FLASK_APP=app.py

echo "Starting Gunicorn..."
exec gunicorn --config gunicorn_config.py app:app
