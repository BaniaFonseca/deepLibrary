# Python imports
from os.path import join
# import django_heroku

# project imports
from .common import *

# uncomment the following line to include i18n
# from .i18n import *


# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

# allow all hosts during development
ALLOWED_HOSTS = ['*']

# adjust the minimal login
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'




# #####   TEMP  CONFIGURATION ##################33
DATABASE_NAME = 'deeplibrary'
DATABASE_USER = 'deeplibrary'
DATABASE_PASSWORD = 'deep'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '27017'

# ##### DATABASE CONFIGURATION ############################
DATABASES ={
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': DATABASE_USER,
        'NAME': DATABASE_NAME,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': '5432'
    }
}


# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# BASE_DIR = PROJECT_ROOT
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = "/static/"

# django_heroku.settings(locals())