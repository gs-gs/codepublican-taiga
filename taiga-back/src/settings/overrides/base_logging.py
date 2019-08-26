import logging

from .base import *  # noqa
from .base import env

from settings.common import LOGGING

SENTRY_DSN = env('SENTRY_DSN', default=None)
SENTRY_CLIENT = env('DJANGO_SENTRY_CLIENT', default='raven.contrib.django.raven_compat.DjangoClient')

if SENTRY_DSN:
    RAVEN_CONFIG = {
        'dsn': SENTRY_DSN,
        'release': env('SENTRY_RELEASE', default='unknown'),
        'environment': env('SENTRY_ENVIRONMENT', default='unkown'),
    }

LOGGING['handlers']['console']['level'] = 'INFO'
LOGGING['handlers']['sentry'] = { 
    'level' : 'WARNING',
    'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
}

LOGGING['loggers']["sentry"] = {
    'handlers': ['console'],
    'propagate': False,
    'level': 'WARNING',
}

LOGGING['loggers']['raven'] = {
    'level': 'DEBUG',
    'handlers': ['console'],
    'propagate': False,
}

LOGGING['loggers']['sentry.errors'] = {
    'level': 'DEBUG',
    'handlers': ['console'],
    'propagate': False,
}

# remove sentry for non-sentrified installations
if not SENTRY_DSN:
    del LOGGING['handlers']['sentry']
    for logger in LOGGING['loggers'].values():
        if 'sentry' in logger['handlers']:
            logger['handlers'].remove('sentry')
