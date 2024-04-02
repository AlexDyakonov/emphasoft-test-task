import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

# Для хранения секретов предпочитаю использовать .env файл, поэтому дальше будет выглядеть так все
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DEBUG = os.getenv("DEBUG_MODE", "True") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split() or []

CSRF_TRUSTED_ORIGINS = []
if scrf_subdomain := os.getenv("SCRF_SUBDOMAIN"):
    CSRF_TRUSTED_ORIGINS += [f"http://{scrf_subdomain}", f"https://{scrf_subdomain}"]


# CORS_HEADERS
cors_allow_headers = os.getenv("CORS_ALLOW_HEADERS")
CORS_ALLOW_HEADERS = cors_allow_headers.split(",") if cors_allow_headers else ["*"]

CORS_ORIGIN_ALLOW_ALL = os.getenv("CORS_ORIGIN_ALLOW_ALL", "False") == "True"

CORS_ALLOW_CREDENTIALS = os.getenv("CORS_ALLOW_CREDENTIALS", "False") == "True"

# Application definition
# Стандартная админка не нравится, поэтому использую джаззмин.
# Хотя там есть проблема с выходом (на 5 версии джанго), когда отправляется гет запрос, а должен быть пост (templates/admin/base.html фиксит проблему)
# Для документации поставил сваггер и yasg который позволяет Docstring преобразовать в документацию апи
# Все приложения в отдельный каталог app. У каждого рпиложения в файле apps.py изменяю название модуля
INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # External
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_swagger",
    "drf_yasg",
    "django_filters",
    # Custom
    "apps.api",
    "apps.reservation",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

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

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# Тут настройка для удобной работы и с SQLITE и с PostgreSQL. Локально предпочитаю sqlite (если возможно)

DATABASES = (
    {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
    if os.getenv("SQLITE") == "True"
    else {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_DB"),
            "USER": os.getenv("POSTGRES_USER"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
            "HOST": os.getenv("POSTGRES_HOST"),
            "PORT": os.getenv("POSTGRES_PORT", 5432),
        }
    }
)


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static/staticfiles")]

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# DRF
# Тут я указал, что по дефолту все запросы должны быть авторизованы
# Поэтому гет пермишн меняю для тех эндпоинтов, где должны быть права просмотра всеми
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}


# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "debug.log",
            "formatter": "standard",
        },
    },
    "root": {
        "handlers": ["file"],
        "level": "DEBUG",
    },
}
