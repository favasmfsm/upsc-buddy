from .shared import *

SECRET_KEY = os.getenv("SECRET_KEY", "dev-insecure-change-me-please-use-32b+")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS", "localhost,127.0.0.1,.localhost,testserver"
).split(",")
X_FRAME_OPTIONS = "ALLOWALL"

# Prefer Postgres (Docker). Set USE_SQLITE=True for a quick local escape hatch.
USE_SQLITE = os.getenv("USE_SQLITE", "False") == "True"

if USE_SQLITE:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db" / "db.sqlite3",
        }
    }
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME", "upsc_buddy"),
            "USER": os.getenv("DB_USERNAME", "upsc_buddy"),
            "PASSWORD": os.getenv("DB_PASSWORD", "upsc_buddy"),
            "HOST": os.getenv("DB_HOST", "127.0.0.1"),
            "PORT": os.getenv("DB_PORT", "5432"),
        }
    }

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

SIMPLE_JWT = {
    **SIMPLE_JWT,
    "SIGNING_KEY": SECRET_KEY,
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
