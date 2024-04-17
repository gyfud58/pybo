from .base import *

ALLOWED_HOSTS = ['3.34.191.141']
STATIC_ROOT  =  BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}