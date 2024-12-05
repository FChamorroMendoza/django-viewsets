"""
Django settings for marvel project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
# NOTE: Importamos os para indicar el directorio de templates y otras utilidades:
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$dpguq$#6!6dw($(qd6))7qcw%%#a=sc!-!7t!_av9%5*(q=uf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# Apps que se agregan automáticamente al crear un proyecto en Django.
BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Acá van las apps de 3ros que necesitamos agregar para que Django las encuentre.
THIRD_APPS = ['rest_framework', 'rest_framework.authtoken', 'drf_yasg']

# Acá van las apps que creamos nosotros.
LOCAL_APPS = ['e_commerce']

INSTALLED_APPS = BASE_APPS + THIRD_APPS + LOCAL_APPS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Local apps: Acá ponemos el nombre de las carpetas de nuestras aplicaciones
    'e_commerce',
    # Third party apps: acá vamos agregando las aplicaciones de terceros, extensiones de Django.
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',

    ),

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'marvel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # NOTE: Agregamos el directorio para los templates, necesario para Swagger
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        # 'DIRS': [],
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

WSGI_APPLICATION = 'marvel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if os.getenv("DB_ENGINE") == "POSTGRES":

    # NOTE: Reemplazamos la configuración inicial de base de datos para trabajar con Postgres:
    # Recordemos:
        #   POSTGRES_DB: marvel_db
        #   POSTGRES_USER: inove_user
        #   POSTGRES_PASSWORD: 123Marvel!

    DATABASES = {
        'default': {
            # 'ENGINE': 'django.db.backends.postgresql_psycopg2' --> En desuso.
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'marvel_db',        # POSTGRES_DB
            'USER' : 'inove_user',      # POSTGRES_USER
            'PASSWORD' : '123Marvel!',  # POSTGRES_PASSWORD
            'HOST':'db',                # Nombre del servicio
            'PORT': '5432'              # Número del puerto
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# NOTE: Para debug

# Color en los prints:
# Modo de uso: print(VERDE+"mi texto")

AMARILLO = "\033[;33m"
CIAN = "\033[;36m"
VERDE = "\033[;32m"

# NOTE: Para manejo de sesión.
LOGIN_URL = '/admin/login'

# API DOCS Settings:
# https://drf-yasg.readthedocs.io/en/stable/settings.html
LOGOUT_URL = '/admin/logout'

# Acá van todas las configuraciones para la UI de Swagger.
SWAGGER_SETTINGS = {
    'DEFAULT_MODEL_RENDERING': "example",
    # Seteo los tipos de Authenticaciones que puedo utilizar en
    # Swagger.
    # https://drf-yasg.readthedocs.io/en/stable/settings.html#security-definitions-settings
    'SECURITY_DEFINITIONS': {
        # HTTP Basic Authentication:
        'basic': {
            'description': "Basic Auth",
            'type': 'basic',
            'in': 'header'
        },
        # Token Authentication:
        'DRF Token': {
            'description': '**Ejemplo: Token ea0dfcbbdff1a55ae26a67cd71bcc6adffb1f200**',
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
         }
    },
    "USE_SESSION_AUTH": True,
    'LOGIN_URL': LOGIN_URL,
    'LOGOUT_URL': LOGOUT_URL
}

# Acá van todas las configuraciones para la UI de Redoc.
REDOC_SETTINGS = {
   'LAZY_RENDERING': False,
}