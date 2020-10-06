from .base import *  # noqa


SECRET_KEY = 'fm6c6yzbfiii&w7j&9esgupyu469p-@uxc&f=1u3)rc#p8flj_'

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": base_dir_join("db.sqlite3")}
}

STATIC_ROOT = base_dir_join('staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = base_dir_join('mediafiles')
MEDIA_URL = '/media/'

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# Speed up password hashing
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# Celery
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True
