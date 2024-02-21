"""
This is a django-split-settings main file.
To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""

from os import environ
from split_settings.tools import include, optional

ENV = environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'components/django.py',  # standart django settigs
    'components/database.py',  # postgres
    'components/celery.py',  # celery
    'components/logger.py',  # user logging settings
    'components/restframework.py',  # django REST framework
    'components/swagger.py'  # documentation

    # Select the right env:
    'environments/{0}.py'.format(ENV),
    # Optionally override some settings:
    optional('environments/local.py'),
]


# Include settings:
include(*base_settings)
