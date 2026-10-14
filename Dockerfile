FROM python:3.13-slim

ENV DJANGO_SETTINGS_MODULE=core.settings.prod
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

WORKDIR /home/app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

COPY . .

# Build-time placeholders only so settings import; real values come from the host at runtime.
RUN DJANGO_SECRET_KEY=build DB_NAME=x DB_USERNAME=x DB_PASSWORD=x DB_HOST=x \
    python manage.py collectstatic --noinput

# Hosts like Railway inject $PORT; locally it falls back to 8300.
CMD ["sh", "-c", "gunicorn core.wsgi:application --workers=2 --timeout=120 --bind=0.0.0.0:${PORT:-8300}"]
