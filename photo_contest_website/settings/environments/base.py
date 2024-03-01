from typing import TYPE_CHECKING

from photo_contest_website.settings.components.django import (
    BASE_DIR,
    SECRET_KEY,
    INSTALLED_APPS,
    DEFAULT_AUTO_FIELD,
    ROOT_URLCONF,
    WSGI_APPLICATION,
    MIDDLEWARE,
    TEMPLATES,
    LANGUAGE_CODE,
    TIME_ZONE,
    USE_I18N,
    USE_TZ,
    STATIC_URL,
    STATIC_ROOT,
    MEDIA_URL,
    MEDIA_ROOT,
    DJANGO_ENV,
)

from photo_contest_website.settings.components.database import (
    DATABASES,
)

from photo_contest_website.settings.components.logger import (
    AUTH_PASSWORD_VALIDATORS,
)

if TYPE_CHECKING:
    from django.http import HttpRequest
