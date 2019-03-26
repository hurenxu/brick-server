"""
Django settings for userservice project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

#TEMPLATE_DEBUG = False
TEMPLATE_DEBUG = True 

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jinja',
    'core',
    'brick',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

#MIDDLEWARE_CLASSES = (
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'core.middlewares.BuildingMiddleware',
]

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'brick',
        'USER': 'bricker',
        'PASSWORD': 'brick-demo',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND':'django_jinja.backend.Jinja2',
        'APP_DIRS': True,
        'OPTIONS': {
                'match_extension': '.jinja',
            }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        }
    }
]

TEMPLATE_DIRS = (
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.filesystem.load_template_source',
)

TEMPLATE_LOADERS = (
    'django_jinja.loaders.AppLoader',
    'django_jinja.loaders.FileSystemLoader',
)

DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja'
AUTH_PROFILE_MODULE = 'core.UserProfile'

BD_SETTINGS = {
    'operation_cold_down': 10, # people can re-do operation after 10 minutes
    'default_schedule': {
        'start': '08:00am',
        'end': '06:00pm',
    },
}

OAUTH_SINGLE_ACCESS_TOKEN = True
OAUTH_DELETE_EXPIRED = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s][%(asctime)s][%(module)s] %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
            #'filename': '%s/logs/%s' % (BASE_DIR, 'null_debug.log'),
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            #'class': 'logging.FileHandler',
            #'filename': '%s/logs/%s' % (BASE_DIR, 'console.log'),
            #'filename': '%s/logs/%s' % (BASE_DIR, 'stream_debug.log'),
            #'formatter': 'simple',
            'formatter': 'verbose',
            'stream': sys.stdout
        },
        'file.debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '%s/logs/%s' % (BASE_DIR, 'debug.log'),
            'formatter': 'verbose'
        },
        'file.info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '%s/logs/%s' % (BASE_DIR, 'info.log'),
            'formatter': 'verbose'
        },
        'file.error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '%s/logs/%s' % (BASE_DIR, 'errors.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'core': {
            'level': 'INFO',
            'handlers': ['file.info', 'file.error'],
        },
    }
}
