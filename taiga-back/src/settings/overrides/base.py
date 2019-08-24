"""
Base settings to build other settings files upon.
"""
from settings.common import *
from .kms import env

READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR.path('.env')))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = env('DJANGO_TIMEZONE', default='Australia/Sydney')
LANGUAGE_CODE = 'en-us'

PYTHON_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATE_FORMAT = 'd M Y'
DATETIME_FORMAT = 'd M Y H:i:s'
SHORT_DATE_FORMAT = DATE_FORMAT
SHORT_DATETIME_FORMAT = DATETIME_FORMAT


# STATIC
# ------------------------------------------------------------------------------
STATIC_URL = '/static/'

# MEDIA
# ------------------------------------------------------------------------------
MEDIA_URL = '/media/'

# SERVICES
# -----------------------------------------------------------------------------
SITES['api']['scheme'] = env('TAIGA_SITE_API_SCHEME', default='http')
SITES['api']['domain'] = env('TAIGA_SITE_API_FQDN', default='localhost:8000')

SITES['front']['scheme'] = env('TAIGA_SITE_FRONT_SCHEME', default='http')
SITES['front']['scheme'] = env('TAIGA_SITE_FRONT_FQDN', default='localhost:9001')

# WebHooks
# ----------------------------------------------------------------------------
WEBHOOKS_ENABLED = env.bool('TAIGA_WEBHOOKS_ENABLED', default=False)
WEBHOOKS_BLOCK_PRIVATE_ADDRESS = env.bool('TAIGA_WEBHOOKS_BLOCK_PRIVATE_ADDRESS', default=False)

# Events 
# ---------------------------------------------------------------------------
EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"

EVENTS_PUSH_BACKEND_OPTIONS = {} 
EVENTS_PUSH_BACKEND_OPTIONS['url'] = env.url('TAIGA_EVENTS_BACKEND_URL', default='')

# Auth
# ----------------------------------------------------------------------------
PUBLIC_REGISTER_ENABLED = env.bool('TAIGA_AUTH_SELF_REGISTER', default=False)

# LIMIT ALLOWED DOMAINS FOR REGISTER AND INVITE
# None or [] values in USER_EMAIL_ALLOWED_DOMAINS means allow any domain
USER_EMAIL_ALLOWED_DOMAINS = env('TAIGA_AUTH_ALLOWED_DOMAINS', default=None)

# GITHUB Auth SETTINGS
GITHUB_URL = "https://github.com/"
GITHUB_API_URL = "https://api.github.com/"
GITHUB_API_CLIENT_ID = env('TAIGA_AUTH_GITHUB_CLIENT_ID', default=None )
GITHUB_API_CLIENT_SECRET = env('TAIGA_AUTH_GITHUB_CLIENT_SECRET', default=None )

# Celery
# ----------------------------------------------------------------------------
CELERY_ENABLED = env.bool('CELERY_ENABLED', default=True )
CELERY_BROKER_URL = env('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = CELERY_BROKER_URL

if USE_TZ:
    # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-timezone
    CELERY_TIMEZONE = TIME_ZONE

# DATABASES
# ------------------------------------------------------------------------------
DATABASES["default"] = env.db('DATABASE_URL', default='')  # noqa F405


# EMAIL
# ----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = env( 'DJANGO_DEFAULT_FROM_EMAIL', default='Taiga<noreply@example.com>' )
# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env('DJANGO_EMAIL_SUBJECT_PREFIX', default='[Taiga]')

CHANGE_NOTIFICATIONS_MIN_INTERVAL = env.int('TAIGA_EMAIL_NOTIFICATIONS_WAIT_TIME', default=300) #seconds


# SITEMAP
# ----------------------------------------------------------------------------
# If is True /front/sitemap.xml show a valid sitemap of taiga-front client
FRONT_SITEMAP_ENABLED = env.bool('TAIGA_SITEMAP_ENABLED', default=False)
FRONT_SITEMAP_CACHE_TIMEOUT = 24*60*60  # In second

# STATS
# ----------------------------------------------------------------------------
STATS_ENABLED = env.bool('TAIGA_COLLECT_STATS', default=False)
FRONT_SITEMAP_CACHE_TIMEOUT = 60*60  # In second

# IMPORTERS
# ----------------------------------------------------------------------------

# Configuration for the GitHub importer
# Remember to enable it in the front client too.
IMPORTERS["github"] = {
    "active": env.bool('TAIGA_IMPORTER_GITHUB_ENABLED', default=False),
    "client_id": env('TAIGA_IMPORTER_GITHUB_CLIENT_ID', default=None),
    "client_secret": env('TAIGA_IMPORTER_GITHUB_CLIENT_SECRET', default=None)
}

# Configuration for the Trello importer
# Remember to enable it in the front client too.
IMPORTERS["trello"] = {
    "active": env.bool('TAIGA_IMPORTER_TRELLO_ENABLED', default=False),
    "api_key": env('TAIGA_IMPORTER_TRELLO_API_KEY', default=None),
    "secret_key": env('TAIGA_IMPORTER_TRELLO_SECRET_KEY', default=None)
}

# Configuration for the Jira importer
# Remember to enable it in the front client too.
IMPORTERS["jira"] = {
    "active": env.bool('TAIGA_IMPORTER_JIRA_ENABLED', default=False), # Enable or disable the importer
    "consumer_key": env('TAIGA_IMPORTER_JIRA_CONSUMER_KEY', default=None),
    "cert": env('TAIGA_IMPORTER_JIRA_CERT', default=None),
    "pub_cert": env('TAIGA_IMPORTER_JIRA_PUB_CERT', default=None)
}

# Configuration for the Asane importer
# Remember to enable it in the front client too.
#IMPORTERS["asana"] = {
#    "active": True, # Enable or disable the importer
#    "callback_url": "{}://{}/project/new/import/asana".format(SITES["front"]["scheme"],
#                                                              SITES["front"]["domain"]),
#    "app_id": "XXXXXX_get_a_valid_app_id_from_asana_XXXXXX",
#    "app_secret": "XXXXXX_get_a_valid_app_secret_from_asana_XXXXXX"
#}