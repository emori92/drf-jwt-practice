from .base import *


# secure
SECRET_KEY='###DRF-TUTORIAL-SECRETKEY'
DEBUG = True


# db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # transaction
        'ATOMIC_REQUESTS': True,
    }
}


# static
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
