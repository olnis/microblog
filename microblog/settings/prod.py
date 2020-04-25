from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
<<<<<<< HEAD
=======
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'microblog',
        'USER': 'microblog',
        'PASSWORD': 'microblog',
>>>>>>> 8474b00060f05ed2dc47be83e7ea7a7468e2076b
    }
}
