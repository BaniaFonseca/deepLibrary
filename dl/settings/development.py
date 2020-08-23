# Python imports
from os.path import join

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
        'ENGINE': 'djongo',
        'NAME': 'deeplibrary',
        'HOST': 'mongodb+srv://deeplibrary:deep@deeplibrary.9ud8i.gcp.mongodb.net/deeplibrary?retryWrites=true&w=majority',
        'USER': 'deeplibrary',
        'PASSWORD': 'deep',
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
