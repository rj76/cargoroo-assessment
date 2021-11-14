from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-pk8c%a2c!e4ol07k14^3&iv6@hfmnjbin8e#5d8+yf+h%m4em3'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'cargoroo.pedroja.tech', '3.8.31.12']

INTERNAL_IPS = [
    '127.0.0.1',
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'rest_framework',
    'rest_framework_gis',
    'django_extensions',

    'api.apps.ApiConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'cargoroo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['{0}/cargoroo/templates'.format(BASE_DIR)],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cargoroo.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'cargoroo',
        'USER': 'cargoroo',
        'PASSWORD': 'cargoroo',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework_gis.schema.GeoFeatureAutoSchema',
}
