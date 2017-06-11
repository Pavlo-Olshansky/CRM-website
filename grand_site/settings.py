"""
Django settings for grand_site project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable!!!" % var_name
        raise ImproperlyConfigured(error_msg)

# Get ENV VARIABLES key
ENV_ROLE = get_env_variable("ENV_ROLE")


#SECURITY WARNING: don't run with debug turned on in production!
if ENV_ROLE=='development':
    DEBUG = True
    SECRET_KEY = get_env_variable('SECRET_KEY')
else:
    from decouple import config
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG', default=False, cast=bool)


ALLOWED_HOSTS = ['my-grand-site-countinue.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'subscribers',
    'accounts',
    'contacts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'grand_site.urls'

if ENV_ROLE == 'development':
    grand_db_1_PASS = get_env_variable("grand_db_1_PASS")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'grand_db_1',
            'USER': 'postgres',
            'PASSWORD': grand_db_1_PASS,
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    from decouple import config
    import dj_database_url
    DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
        )
    }
    


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
	            'django.template.context_processors.debug',
	            'django.template.context_processors.request',
	            'django.contrib.auth.context_processors.auth',
	            'django.contrib.messages.context_processors.messages',

    			"django.template.context_processors.debug",
			    "django.template.context_processors.i18n",
			    "django.template.context_processors.media",
			    "django.template.context_processors.static",
			    "django.template.context_processors.tz",
            ],
        },
    },
]


WSGI_APPLICATION = 'grand_site.wsgi.application'

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Stripe Key Settings
STRIPE_SECRET_KEY = get_env_variable("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = get_env_variable("STRIPE_PUBLISHABLE_KEY")

# Current Subscription Price
SUBSCRIPTION_PRICE = 1000

LOGIN_REDIRECT_URL = '/account/list/'

