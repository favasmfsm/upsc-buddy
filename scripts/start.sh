#!/bin/sh
# Container entrypoint: prepare the database, then serve.
set -e

sh scripts/predeploy.sh
exec gunicorn core.wsgi:application --workers=2 --timeout=120 --bind="0.0.0.0:${PORT:-8300}"
