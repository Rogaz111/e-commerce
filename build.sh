#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

echo "Changing Directory.."

cd app

echo  "Current Directory: app"

python manage.py collectstatic --no-input

python manage.py migrate