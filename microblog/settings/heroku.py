from .common import *

import dj_database_url


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['*']

MIDDLEWARE_CLASSES = (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES['default'] = dj_database_url.config(
    conn_max_age=600, ssl_require=True)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
