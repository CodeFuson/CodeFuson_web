import os
from pathlib import Path

# Base directory of the project (i.e., where settings.py is located)
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY is used for cryptographic signing. Keep it secret in production.
SECRET_KEY = "django-insecure-y%yhg9a=7!5t3yb(a+@266bqe%+2@rf++f9e-o$pjt0dk&yv%%"

# DEBUG should be False in production.
DEBUG = True

# ALLOWED_HOSTS specifies which host/domain names are valid for your site.
ALLOWED_HOSTS = []  # Allow all hosts by default, modify as neededai_generator

# List of installed Django apps, including third-party apps like Django REST framework and CORS handling
INSTALLED_APPS = [
    "django.contrib.admin",  # Django admin
    "django.contrib.auth",  # Django authentication
    "django.contrib.contenttypes",  # Django content types
    "django.contrib.sessions",  # Session handling
    "django.contrib.messages",  # Django messages framework
    "django.contrib.staticfiles",  # Static files handling
    'rest_framework',  # Django REST framework for building APIs
    'corsheaders',  # CORS middleware for React frontend integration
    'ai_generator'
]

# Middleware is a list of middleware components to process requests and responses.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",  # Security middleware
    "django.contrib.sessions.middleware.SessionMiddleware",  # Session handling middleware
    "django.middleware.common.CommonMiddleware",  # Common middleware for handling things like headers
    "django.middleware.csrf.CsrfViewMiddleware",  # CSRF protection
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # Authentication middleware
    "django.contrib.messages.middleware.MessageMiddleware",  # Messaging middleware
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Clickjacking protection
    'corsheaders.middleware.CorsMiddleware',  # CORS middleware for React
]

# CORS settings to allow the frontend to communicate with the backend
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React development server URL (frontend)
    "http://yourfrontenddomain.com",  # Add your production frontend domain here
]

CORS_ORIGIN_ALLOW_ALL = True # Disable this for production for better security

# The root URL configuration for your Django app
ROOT_URLCONF = "core.urls"

# REST framework settings for versioning
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',  # API versioning strategy
    'DEFAULT_VERSION': 'v1',  # Default version for your API
}

# Template settings for Django, where we use the Django template engine to render views
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # Directory to search for HTML templates
        ],
        'APP_DIRS': True,  # Look for templates in app directories
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

# WSGI application setup for the Django server
WSGI_APPLICATION = "core.wsgi.application"

# Database settings (using PostgreSQL in this example, adjust as needed)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Database backend (PostgreSQL in this case)
        'NAME': 'codefuson_db',  # Name of your PostgreSQL database
        'USER': 'postgres',  # Database username
        'PASSWORD': 'postgres',  # Database password
        'HOST': 'localhost',  # Database host (use 'localhost' for local development)
        'PORT': '5432',  # PostgreSQL default port
    }
}

# Password validation settings for stronger passwords
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

# Localization settings
LANGUAGE_CODE = "en-us"  # Language used in your app
TIME_ZONE = "UTC"  # Time zone for your app
USE_I18N = True  # Enable internationalization
USE_TZ = True  # Enable timezone support

# Static files settings (CSS, JS, images, etc.)
STATIC_URL = "/static/"  # The URL where static files will be served from

# Add the path to the React build static files so that Django can serve them
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/build/static')
]

# Uncomment this line if you want to collect all static files into one directory (for production)
# STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type for models
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS configuration to ensure your frontend can make requests to your Django backend
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React frontend development server URL
    "http://localhost:8000",
]
