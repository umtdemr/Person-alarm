from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'not-so-secret'  # generate your own secret key

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SITE_URL = 'http://127.0.0.1:8000'  # replace with url

T_TOKEN = ''  # telegram bot token
T_USER = ''  # telegram user id
