from typing import TYPE_CHECKING

from photo_contest_website.settings.components.database import (
    DATABASES,
)
from photo_contest_website.settings.components.django import BASE_DIR
from photo_contest_website.settings.components.django import DEFAULT_AUTO_FIELD
from photo_contest_website.settings.components.django import DJANGO_ENV
from photo_contest_website.settings.components.django import INSTALLED_APPS
from photo_contest_website.settings.components.django import LANGUAGE_CODE
from photo_contest_website.settings.components.django import MEDIA_ROOT
from photo_contest_website.settings.components.django import MEDIA_URL
from photo_contest_website.settings.components.django import MIDDLEWARE
from photo_contest_website.settings.components.django import ROOT_URLCONF
from photo_contest_website.settings.components.django import SECRET_KEY
from photo_contest_website.settings.components.django import STATIC_ROOT
from photo_contest_website.settings.components.django import STATIC_URL
from photo_contest_website.settings.components.django import TEMPLATES
from photo_contest_website.settings.components.django import TIME_ZONE
from photo_contest_website.settings.components.django import USE_I18N
from photo_contest_website.settings.components.django import USE_TZ
from photo_contest_website.settings.components.django import WSGI_APPLICATION
from photo_contest_website.settings.components.logger import (
    AUTH_PASSWORD_VALIDATORS,
)

if TYPE_CHECKING:
    from django.http import HttpRequest
