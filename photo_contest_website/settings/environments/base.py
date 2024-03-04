# autoflake: skip_file
from typing import TYPE_CHECKING

from photo_contest_website.settings.components.database import DATABASES
from photo_contest_website.settings.components.django import (
    BASE_DIR,
    DEFAULT_AUTO_FIELD,
    DJANGO_ENV,
    INSTALLED_APPS,
    LANGUAGE_CODE,
    MEDIA_ROOT,
    MEDIA_URL,
    MIDDLEWARE,
    ROOT_URLCONF,
    SECRET_KEY,
    STATIC_ROOT,
    STATIC_URL,
    TEMPLATES,
    TIME_ZONE,
    USE_I18N,
    USE_TZ,
    WSGI_APPLICATION,
)
from photo_contest_website.settings.components.logger import AUTH_PASSWORD_VALIDATORS

if TYPE_CHECKING:
    from django.http import HttpRequest
