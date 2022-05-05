from django.apps import AppConfig
from . import ACCOUNTAPP_APPS_LABEL

class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '%s.account' % ACCOUNTAPP_APPS_LABEL
