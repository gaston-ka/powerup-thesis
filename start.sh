#!/bin/bash

python manage.py makemigrations && python manage.py migrate && gunicorn  madinnah.wsgi:application --bind 0.0.0.0:8000
