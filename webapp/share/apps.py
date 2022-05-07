from django.apps import AppConfig
from . import SHAREAPP_APPS_LABEL


class ShareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '%s.share' % SHAREAPP_APPS_LABEL
