"""
This file contains all the settings that defines the development server.

SECURITY WARNING: don't run with debug turned on in production!
"""

from photo_contest_website.settings.components import config, Csv

from photo_contest_website.settings.components.django import (
    DATABASES,
    INSTALLED_APPS,
    MIDDLEWARE,
)

# Setting the development status:

DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Installed apps for development only:
INSTALLED_APPS += (

)

MIDDLEWARE += (

)

DATABASES['default']['CONN_MAX_AGE'] = 0
