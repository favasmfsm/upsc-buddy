FROM python:3.13-slim AS builder

WORKDIR /home/app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pipenv

COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy --ignore-pipfile || pipenv install --skip-lock

FROM python:3.13-slim

ENV DJANGO_SETTINGS_MODULE=core.settings.prod
ENV PYTHONUNBUFFERED=1

WORKDIR /home/app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /root/.local/share/virtualenvs /root/.local/share/virtualenvs
COPY --from=builder /usr/local/bin/pipenv /usr/local/bin/pipenv
COPY --from=builder /usr/local/lib/python3.13 /usr/local/lib/python3.13

RUN pip install --no-cache-dir pipenv

COPY . .

CMD ["pipenv", "run", "gunicorn", "--workers=2", "--bind=0.0.0.0:8300", "core.wsgi:application"]
