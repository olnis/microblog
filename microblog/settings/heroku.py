from .common import *

import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {}
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
