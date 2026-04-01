from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Keep this secret in production!
SECRET_KEY = "django-insecure-^jd*!h9(rh6rfcu8&jrb+xuvj!65)a-8y5j(_jpbsiaa_!v0kz"

# DEBUG should be False in a real production environment
DEBUG = True

ALLOWED_HOSTS = []

# --- Application Definition ---
INSTALLED_APPS = [
    "daphne",                  # ASGI Server for handling WebSockets (Task 2)
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    "rest_framework",          # Framework for building Task 1, 3, and 4 APIs
    "blog",                    # App for Task 1 (Blog) and Task 2 (Chat)
    "channels",                # Required for Task 2: Real-time communication
    "shop",                    # App for Task 3 (E-commerce) and Task 4 (AI Engine)
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

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# Standard Sync server configuration
WSGI_APPLICATION = "core.wsgi.application"

# --- Task 2: Real-time Configuration ---
# ASGI is required for handling WebSockets in Task 2
ASGI_APPLICATION = "core.asgi.application"

# --- Database Configuration (Task 1 & 3) ---
# Using PostgreSQL for professional-grade data storage
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',       
        'USER': 'postgres',      
        'PASSWORD': 'Mali1234@#', 
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# --- Password Validation ---
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- Internationalization ---
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --- Static Files ---
STATIC_URL = "static/"

# --- Task 2: Channel Layers ---
# Using InMemory layer to handle communication between chat instances
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}