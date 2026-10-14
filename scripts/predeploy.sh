#!/bin/sh
# Runs at container start (scripts/start.sh), before gunicorn.
set -e

python manage.py migrate --noinput

# Content seeds are idempotent, but they overwrite admin edits to seeded
# concepts, so only run them when RUN_SEEDS=true.
if [ "$RUN_SEEDS" = "true" ]; then
  sh scripts/seed_all.sh
fi
