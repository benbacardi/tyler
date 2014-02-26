# Django settings for test_project project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

INTERNAL_IPS = ('127.0.0.1', '10.252.24.0/24',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'dbfile'),
    }
}

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'j$w14t$3(e7k*=c!ks!z&amp;w2s2af!xrku3%&amp;4!c@_5wwicjg&amp;c_c'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'test_project.urls'

WSGI_APPLICATION = 'test_project.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tyler',
)

try:
    from local_settings import *
except ImportError:
    pass
