# Wardrobe1/settings.py

from pathlib import Path
import os # <-- ДОБАВЛЕНО: для работы с переменными окружения
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv() 
# ==============================================================================
# ↓↓↓ ВАЖНЫЕ ИЗМЕНЕНИЯ ДЛЯ БЕЗОПАСНОСТИ И ХОСТИНГА ↓↓↓
# ==============================================================================

# Никогда не храните секретный ключ в коде. Мы будем хранить его на сервере.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-default-key-for-local-dev')

# DEBUG будет True только на вашем компьютере. На сервере он будет False.
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# На сервере здесь будет ваш домен, а '*' - для локальной разработки
ALLOWED_HOSTS = ['www.wardrobe-online.ru', 'localhost', '127.0.0.1']

# ==============================================================================
# ↑↑↑ ИЗМЕНЕНИЯ ЗДЕСЬ ЗАКОНЧИЛИСЬ ↑↑↑
# ==============================================================================


# --- ПРИЛОЖЕНИЯ ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'users.apps.UsersConfig',
    'clothes.apps.ClothesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # --- ДОБАВЛЕНО: Помощник для статических файлов ---
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # --- КОНЕЦ ИЗМЕНЕНИЙ ---
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Wardrobe1.urls'

# --- ШАБЛОНЫ ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'Wardrobe1.wsgi.application'

# --- БАЗА ДАННЫХ ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- ВАЛИДАТОРЫ ПАРОЛЕЙ ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- МОДЕЛЬ ПОЛЬЗОВАТЕЛЯ ---
AUTH_USER_MODEL = 'users.CustomUser'

# --- URL'ы АУТЕНТИФИКАЦИИ ---
LOGIN_REDIRECT_URL = 'clothes:item_list'
LOGOUT_REDIRECT_URL = 'clothes:home'
LOGIN_URL = 'login'

# --- ЯЗЫК И ВРЕМЯ ---
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- СТАТИЧЕСКИЕ И МЕДИА ФАЙЛЫ ---
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# --- ДОБАВЛЕНО: Настройка для whitenoise ---
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# --- КОНЕЦ ИЗМЕНЕНИЙ ---

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'