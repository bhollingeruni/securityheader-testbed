"""
Django settings for testsuite project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*uj%vj%xueb2p#zmw_2w3m9)*3%jleweay87bhlhcr7*flnff4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'testsuite.test',
    'sub.testsuite.test'
]

CURRENT_ORIGIN = "http://testsuite.test:8000"
CURRENT_SCHEME = "http"
CURRENT_DOMAIN = "testsuite.test"
CURRENT_PORT = "8000"
CURRENT_SECURE_ORIGIN = "https://testsuite.test:9000"
CURRENT_SECURE_SCHEME = "https"
CURRENT_SECURE_DOMAIN = "testsuite.test"
CURRENT_SECURE_PORT = "9000"
SUBDOMAIN_ORIGIN = "http://sub.testsuite.test:8000"
SUBDOMAIN_SCHEME = "http"
SUBDOMAIN_DOMAIN = "sub.testsuite.test"
SUBDOMAIN_PORT = "8000"
EXTERNAL_ORIGIN = "http://sub.testsuite.test:8000"
EXTERNAL_SCHEME = "http"
EXTERNAL_DOMAIN = "sub.testsuite.test"
EXTERNAL_PORT = "8000"
EXTERNAL_SECURE_ORIGIN = "https://sub.testsuite.test:9000"
EXTERNAL_SECURE_SCHEME = "https"
EXTERNAL_SECURE_DOMAIN = "sub.testsuite.test"
EXTERNAL_SECURE_PORT = "9000"
EXTERNAL_SUBDOMAIN_ORIGIN = "http://sub.testsuite.test:8000"
EXTERNAL_SUBDOMAIN_SCHEME = "http"
EXTERNAL_SUBDOMAIN_DOMAIN = "sub.testsuite.test"
EXTERNAL_SUBDOMAIN_PORT = "8000"


# Application definition

INSTALLED_APPS = [
    'sslserver',
    'cookietest.apps.CookietestConfig',
    'browsertest.apps.BrowsertestConfig',
    'xframeoptionstest.apps.XframeoptionstestConfig',
    'xcontenttypeoptionstest.apps.XcontenttypeoptionstestConfig',
    'referrerpolicytest.apps.ReferrerpolicytestConfig',
    'contentsecuritypolicytest.apps.ContentsecuritypolicytestConfig',
    'corstest.apps.CorstestConfig',
    'hststest.apps.HststestConfig',
    'saveresult.apps.SaveresultConfig',
    'analyzeresult.apps.AnalyzeresultConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'testsuite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'testsuite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testsuite',
        'USER': 'bhollinger',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'results.log'),
        },
    },
    'loggers': {
        'testsuite': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
