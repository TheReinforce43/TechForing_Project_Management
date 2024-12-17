"""
Django settings for techforing_backend project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import environ
env = environ.Env()
environ.Env.read_env()
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS=[
    'User',
    'Comments',
    'Project',
    'Project_member',
    'Tasks'
]


CUSTOM_APPS=[
    'rest_framework',
     'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
]

INSTALLED_APPS = DEFAULT_APPS + CUSTOM_APPS + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "techforing_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "techforing_backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}



# AUTHENTICATION_BACKENDS = [
#     'User.backends.EmailBackend',  # Replace `your_app` with the app name
#     'django.contrib.auth.backends.ModelBackend',  # Keep the default backend
# ]



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# jwt authentication support section 



REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework.authentication.TokenAuthentication',
    # ],

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    
    # 'DEFAULT_PAGINATION_CLASS': 'Employee.pagination.DynamicPageSizePagination',
    # 'DEFAULT_PAGINATION_CLASS': 'Employee.pagination.DynamicPageSizePagination',
     # Default page size if not specified in the request
   
    'PAGE_SIZE': 10,  # Number of results per page
    # 'MAX_PAGE_SIZE': 1000,  # Maximum page size to limit abuse
    # "DATETIME_FORMAT": "%Y-%m-%d %I:%M %p",
}

# JWT settings configuration

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=80),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    'AUTH_HEADER_TYPES': ('Bearer',),  # Make sure you're using 'Bearer'
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    # 'TOKEN_USER_CLASS': 'User.Users',   # Ensure it uses your custom user model
}






# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Base url to serve media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = 'User.Users'
