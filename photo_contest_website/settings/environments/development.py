from photo_contest_website.settings.components import config, Csv
from photo_contest_website.settings.environments.base import *


# Setting the development status:
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1,localhost", cast=Csv())
