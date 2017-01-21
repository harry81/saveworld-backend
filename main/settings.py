"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import datetime
import raven
import urllib

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_xnb+ht0%h1mk188cuyn@7a6p63iki+7sbg(zn%1_@l00or%7o'

# SECURITY WARNING: don't run with debug turned on in production!
ISAWS = os.getenv('ISAWS', False)
DEBUG = False if ISAWS else True
SESSION_COOKIE_DOMAIN="localhost" if DEBUG else '.healworld.co.kr'

ADMINS = (
    ('pointer', 'chharry@gmail.com'),
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_comments',
    'django_extensions',
    'django.contrib.gis',

    #third party
    'rest_framework',
    'rest_framework_gis',
    'django_filters',
    'versatileimagefield',
    'storages',
    'corsheaders',
    'oauth2_provider',
    'social.apps.django_app.default',
    'rest_framework_social_oauth2',
    'fsm_admin',
    'raven.contrib.django.raven_compat',
    'djcelery',
    'constance',
    'constance.backends.database',
    'actstream',

    # private app
    'core',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'social.backends.kakao.KakaoOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.naver.NaverOAuth2',
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

EMAIL_USE_TLS = True
EMAIL_PORT = 587
SERVER_EMAIL = 'chharry@gmail.com'
EMAIL_SUBJECT_PREFIX = '[HEALWORLD]'

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

SMS_APPID = os.getenv('SMS_APPID')
SMS_APIKEY = os.getenv('SMS_APIKEY')

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id, name, email, age_range'
}

SESSION_COOKIE_AGE = 60 * 60 * 24 * 365
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/get_token/'
# SOCIAL_AUTH_LOGIN_ERROR_URL = '/get_token/'
SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_KAKAO_KEY = os.getenv('SOCIAL_AUTH_KAKAO_KEY')
SOCIAL_AUTH_KAKAO_SECRET = os.getenv('SOCIAL_AUTH_KAKAO_SECRET')
SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_NAVER_KEY = os.getenv('SOCIAL_AUTH_NAVER_KEY')
SOCIAL_AUTH_NAVER_SECRET = os.getenv('SOCIAL_AUTH_NAVER_SECRET')

# SOCIAL_AUTH_PIPELINE = (
#     'social.pipeline.social_auth.social_details',
#     'social.pipeline.social_auth.social_uid',
#     'social.pipeline.social_auth.auth_allowed',
#     'social.pipeline.social_auth.social_user',
#     'social.pipeline.social_auth.associate_user',
#     'social.pipeline.social_auth.load_extra_data',
#     'social.pipeline.user.user_details',
#     'core.pipeline.social_auth.update_extra',
# )

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('RDS_DB_NAME'),
        'USER': os.getenv('RDS_USERNAME'),
        'PASSWORD': os.getenv('RDS_PASSWORD'),
        'HOST': os.getenv('RDS_HOSTNAME'),
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1
AUTH_USER_MODEL = 'core.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT= os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# STORAGE
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'healworld-dev-seoul'
AWS_S3_HOST = 's3.ap-northeast-2.amazonaws.com'
AWS_QUERYSTRING_AUTH = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'healworld.co.kr.s3-website.ap-northeast-2.amazonaws.com',
    'www.healworld.co.kr.s3-website.ap-northeast-2.amazonaws.com',
    'healworld.co.kr',
    'www.healworld.co.kr',
    'localhost:8100',
    'healworld:8100',
    '127.0.0.1:8100'
)

ALLOWED_HOSTS = ['*']

REST_FRAMEWORK = {
     'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
}
FSM_ADMIN_FORCE_PERMIT = True

GCM_SERVER_KEY = os.getenv('GCM_SERVER_KEY')

RAVEN_CONFIG = {
    'dsn': "https://%s@sentry.io/127326" % os.getenv('RAVEN_DSN'),
}

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')

BROKER_URL = 'sqs://{0}:{1}@'.format(
    urllib.quote(AWS_ACCESS_KEY_ID, safe=''),
    urllib.quote(AWS_SECRET_ACCESS_KEY, safe='')
)

BROKER_TRANSPORT_OPTIONS = {
    'region': '.ap-northeast-2',
    'polling_interval': 3,
    'visibility_timeout': 3600,
}
CELERY_SEND_TASK_ERROR_EMAILS = True


BROKER_TRANSPORT = 'sqs'
BROKER_USER = AWS_ACCESS_KEY_ID
BROKER_PASSWORD = AWS_SECRET_ACCESS_KEY

CELERY_DEFAULT_QUEUE = 'celery-myapp-production'
CELERY_QUEUES = {
    CELERY_DEFAULT_QUEUE: {
        'exchange': CELERY_DEFAULT_QUEUE,
        'binding_key': CELERY_DEFAULT_QUEUE,
    }
}

try:
    from settings_local import *
except:
    pass

### ACTSTREAM
ACTSTREAM_SETTINGS = {
    'FETCH_RELATIONS': True,
    'USE_PREFETCH': True,
    'USE_JSONFIELD': True,
    'GFK_FETCH_DEPTH': 1,
}

### CELERY
import djcelery
djcelery.setup_loader()


### CONSTANCE
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_CONFIG = {
    'SEND_TEXT': (True, 'Send text message or not'),
    'SECONDS_TO_SEND_TEXT': (60, 'Seconds to send text message'),
    'NOTIFICATION_HOW_LONG': (60, 'When the user is notified')
}
