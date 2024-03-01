"""
This file contains all the settings used in production.

This file is required and if development.py is present these
values are overridden.
"""

from photo_contest_website.settings.components import config
from .base import *


# Setting the production status:
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS')
