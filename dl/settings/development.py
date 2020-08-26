# Python imports
from os.path import join
import django_heroku

# project imports
from .common import *

# uncomment the following line to include i18n
# from .i18n import *


# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

# allow all hosts during development
ALLOWED_HOSTS = ['*']

# adjust the minimal login
LOGIN_URL = 'core_login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'core_login'


# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_ROOT, 'run', 'dev.sqlite3'),
    }
}


# #####   TEMP  CONFIGURATION ##################33
DATABASE_NAME = 'deeplibrary'
DATABASE_USER = 'deeplibrary'
DATABASE_PASSWORD = 'deep'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '27017'


# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

BASE_DIR = PROJECT_ROOT
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = "/static/"
django_heroku.settings(locals())