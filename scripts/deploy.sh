#!/usr/bin/env bash
# Example deploy helper for the template. Customize per fork.
set -euo pipefail
docker compose build
docker compose up -d
docker compose exec backend pipenv run python manage.py migrate
docker compose exec backend pipenv run python manage.py seed_demo
echo "Deploy complete."
