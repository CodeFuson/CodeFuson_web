import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-y%yhg9a=7!5t3yb(a+@266bqe%+2@rf++f9e-o$pjt0dk&yv%%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []  # Allow all hosts by default, modify as needed

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',  # Django REST framework for building APIs
    'corsheaders',  # CORS middleware for React frontend integration
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',  # CORS middleware for React
    'django.middleware.common.CommonMiddleware',
]

# CORS (Cross-Origin Resource Sharing) settings to allow the frontend to communicate with the backend
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React development server
    "http://yourfrontenddomain.com",  # Production domain of your frontend app
]

CORS_ORIGIN_ALLOW_ALL = False  # Set to False in production for better security

ROOT_URLCONF = "CodeFuson.urls"

# REST Framework settings for versioning
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v1',  # Default version for your API
}

# Template settings to use Django's templating engine
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # Directory to search for HTML templates
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

WSGI_APPLICATION = "CodeFuson.wsgi.application"

# Database settings (using PostgreSQL in this example)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'codefusion_db',  # Name of your PostgreSQL database
        'USER': 'postgres',  # Database username
        'PASSWORD': 'postgres',  # Database password
        'HOST': 'localhost',  # Database host (usually localhost)
        'PORT': '5432',  # Default PostgreSQL port
    }
}

# Password validation settings to enforce stronger passwords
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

# Localization settings (language and timezone)
LANGUAGE_CODE = "en-us"  # Language for your application
TIME_ZONE = "UTC"  # Time zone for your application
USE_I18N = True
USE_TZ = True

# Static files settings (CSS, JS, images, etc.)
STATIC_URL = "/static/"  # URL where static files will be served from

# Add the React build static files path (if you want to serve React's build from Django)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/build/static'),  # React build statikus fájlok helye
]

# Uncomment this for production to collect all static files into one directory
# STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS configuration (this allows your frontend to make requests to your Django API)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React development server
]
CORS_ORIGIN_ALLOW_ALL = False  # For security, set to False in production
