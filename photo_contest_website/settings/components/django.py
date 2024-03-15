import os
from pathlib import Path

from decouple import config

BASE_DIR = Path(__file__).resolve().parent

# CORE SETTINGS
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "api.apps.ApiConfig",
    "models_appl.apps.ModelsApplConfig",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "photo_contest_website.urls"

INTERNAL_IPS = ["127.0.0.1"]

WSGI_APPLICATION = "photo_contest_website.wsgi.application"

# MIDDLEWARE SETTINGS
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# TEMPLATES SETTINGS
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates", "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# I18N AND L10N SETTINGS
LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True

# STATIC FILES SETTINGS
STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# MEDIA FILES SETTINGS
MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR.parent.parent / "media"

# Environment
DJANGO_ENV = config("DJANGO_ENV", default="development")

# Перенаправдение пользователя на домашнюю страницу
# после успешного входа в систему
LOGIN_REDIRECT_URL = "profile"
LOGOUT_REDIRECT_URL = "profile"
