import logging
from .base import env

SENTRY_DSN = env('SENTRY_DSN', default=None)
SENTRY_CLIENT = env('DJANGO_SENTRY_CLIENT', default='raven.contrib.django.raven_compat.DjangoClient')

if SENTRY_DSN:
    SENTRY_CELERY_LOGLEVEL = env.int('DJANGO_SENTRY_LOG_LEVEL', logging.INFO)
    RAVEN_CONFIG = {
        'dsn': SENTRY_DSN,
        'release': env('BUILD_REFERENCE', default='unknown'),
    }


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'sentry'],
            'level': 'DEBUG',
        },
        'elasticsearch': {
            'handlers': ['console', 'sentry'],
            'level': 'WARNING',
        },
        'sentry': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'WARNING',
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'faker': {  # boring stuff from the tests
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        'factory': {  # boring stuff from the tests
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            # boring to have it in sentry
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

# remove sentry for non-sentrified installations
if not SENTRY_DSN:
    del LOGGING['handlers']['sentry']
    for logger in LOGGING['loggers'].values():
        if 'sentry' in logger['handlers']:
            logger['handlers'].remove('sentry')
