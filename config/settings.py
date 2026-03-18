import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-r-ml_40k$rtu)3=$2^y$uo+tl^o5=84a*7#7oy#s@ax3dkpf5k",
)
DEBUG = os.getenv("DJANGO_DEBUG", "True").lower() == "true"
SOCIAL_LOGIN_ENABLED = (
    os.getenv(
        "DJANGO_ENABLE_SOCIAL_LOGIN",
        os.getenv("DJANGO_ENABLE_GOOGLE_LOGIN", "False"),
    ).lower()
    == "true"
)
ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv(
        "DJANGO_ALLOWED_HOSTS",
        "127.0.0.1,localhost,.pythonanywhere.com",
    ).split(",")
    if host.strip()
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "hangarin",
]

if SOCIAL_LOGIN_ENABLED:
    INSTALLED_APPS += [
        "django.contrib.sites",
        "allauth",
        "allauth.account",
        "allauth.socialaccount",
        "allauth.socialaccount.providers.google",
        "allauth.socialaccount.providers.github",
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

if SOCIAL_LOGIN_ENABLED:
    MIDDLEWARE.insert(-1, "allauth.account.middleware.AccountMiddleware")

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "hangarin" / "templates",
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

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

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Manila"

USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "hangarin" / "static",
]
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/login/"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

if SOCIAL_LOGIN_ENABLED:
    SITE_ID = int(os.getenv("DJANGO_SITE_ID", "1"))
    AUTHENTICATION_BACKENDS.append(
        "allauth.account.auth_backends.AuthenticationBackend"
    )
    ACCOUNT_EMAIL_VERIFICATION = "none"
    ACCOUNT_LOGIN_METHODS = {"email", "username"}
    SOCIALACCOUNT_PROVIDERS = {
        "google": {
            "SCOPE": [
                "profile",
                "email",
            ],
            "AUTH_PARAMS": {
                "access_type": "online",
            },
            "OAUTH_PKCE_ENABLED": True,
        },
        # Inference: requesting email scope helps ensure GitHub returns a usable email.
        "github": {
            "SCOPE": [
                "user:email",
            ],
        },
    }
