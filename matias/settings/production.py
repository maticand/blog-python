from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['matiasblog.herokuapp.com', 'matiascandia.com.ar']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'daq6p699s0lcpn',
        'USER': 'gsmdwkaonaksvl',
        'PASSWORD': '1abbddea53bf1e9da0c3beb4062a4d4b883f65e910eb25a186c0650dca5a44c3',
        'HOST': 'ec2-174-129-218-200.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
