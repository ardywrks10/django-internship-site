#!/bin/bash
set -e

echo ">> Running migrations..."
python manage.py migrate

echo ">> Creating superuser"
python manage.py createsuperuser --noinput || echo ">> Superuser already exists or could not be created. Skipping."

echo ">> Collecting static files..."
python manage.py collectstatic --noinput

echo ">> Starting server..."
python manage.py runserver 0.0.0.0:$PORT
