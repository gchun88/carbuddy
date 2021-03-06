"""
Django settings for carbuddy project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+$nd2)gqgmwrp27t_zz_0bffp)^2n7@-tc@0@51+ec=cdco3yl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

#AUTH USER SETTINGS
AUTH_USER_MODEL = 'users.tblUser'

# Application definition

INSTALLED_APPS = [
    'headfoot',
    'listing',
    'userinput',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'phonenumber_field',
'allauth',  # <--
'allauth.account',  # <--
'allauth.socialaccount',  # <--
'allauth.socialaccount.providers.google',  # <--
'allauth.socialaccount.providers.facebook',  # <--
'django.contrib.sites',  # make sure sites is included
]

#google authentication???
AUTHENTICATION_BACKENDS = (
 'django.contrib.auth.backends.ModelBackend',
 'allauth.account.auth_backends.AuthenticationBackend',
 )
SITE_ID = 2
LOGIN_REDIRECT_URL = '/'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_FORMS = {'signup': 'users.forms.CustomUserCreationForm'}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'carbuddy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'carbuddy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
import os
STATIC_URL = '/static/'
#MEDIA_URL = '/images/'


# Deployment settings.py
#STATICFILES_DIRS - > this is a list of static folders' paths for different apps
STATICFILES_DIRS = [os.path.join(BASE_DIR, "listing/templates/listing/static"),os.path.join(BASE_DIR, "carbuddy/templates/carbuddy/static"),os.path.join(BASE_DIR, "headfoot/templates/headfoot/static"),os.path.join(BASE_DIR, "users/templates/users/static")]
#STATIC_ROOT is a path for one general static folder that migate everything into one
STATIC_ROOT = os.path.join(BASE_DIR, "static")
#MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

#Production settings.py
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#STATIC_PRODUCTION_DIR = os.path.abspath(os.path.join(
#os.path.dirname(__file__), '..', '..', 'static_production'))
#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(STATIC_PRODUCTION_DIR, "static")
#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(STATIC_PRODUCTION_DIR, "media")
#STATICFILES_DIRS = [#os.path.join(BASE_DIR, "static"),#]


# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'



