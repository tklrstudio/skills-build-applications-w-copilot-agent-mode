"""
Django settings for octofit_tracker project.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-placeholder-key-for-exercise'
DEBUG = True
ALLOWED_HOSTS = [
    '*',
    'localhost',
    '127.0.0.1',
    '.app.github.dev',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'djongo',
    'octofit_tracker',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'octofit_tracker.urls'

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
        }
    }
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'https://jasontklr-skills-build-applications-w-copilot-agent-mode-3000.app.github.dev',
]

CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = [
    'https://jasontklr-skills-build-applications-w-copilot-agent-mode-8000.app.github.dev',
]

STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
