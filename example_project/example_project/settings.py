# Django settings for example_project project.
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

SECRET_KEY = 'j$w14t$3(e7k*=c!ks!z&amp;w2s2af!xrku3%&amp;4!c@_5wwicjg&amp;c_c'

ROOT_URLCONF = 'django_autoconfig.autourlconf'

WSGI_APPLICATION = 'example_project.wsgi.application'

INSTALLED_APPS = (
    'tyler',
)

CELERY_ALWAYS_EAGER = True
import djcelery
djcelery.setup_loader()

from django_autoconfig.autoconfig import configure_settings
configure_settings(globals())

try:
    from local_settings import *
except ImportError:
    pass
