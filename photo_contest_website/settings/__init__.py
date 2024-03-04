"""
Модуль содержит набор модулей с настройками
This is a django-split-settings main file.
To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""

from os import environ

import django_stubs_ext
from split_settings.tools import include, optional

django_stubs_ext.monkeypatch()

# Managing environment via `DJANGO_ENV` variable:
environ.setdefault("DJANGO_ENV", "development")
_ENV = environ["DJANGO_ENV"]

base_settings = [
    "components/django.py",  # standart django settigs
    "components/database.py",  # postgres
    "components/celery.py",  # celery
    "components/logger.py",  # user logging settings
    "components/restframework.py",  # django REST framework
    "components/swagger.py",  # documentation
    # Select the right env:
    "environments/{}.py".format(_ENV),
    # Optionally override some settings:
    optional("environments/local.py"),
]

include(*base_settings)
