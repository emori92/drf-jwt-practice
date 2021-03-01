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

LOGGING = {
    # 初期化
    'version': 1,
    'disable_existing_loggers': False,

    # logger
    'loggers': {

        # Django
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },

        # apps
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagete': False,
        },

        'accounts': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagete': False,
        },
    },

    # handler
    'handlers': {
        # condole
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'develop',
        },
    },

    # formatter
    'formatters': {
        # develop
        'develop': {
            'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d %(message)s'
        },
    },
}
