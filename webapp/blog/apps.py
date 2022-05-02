from django.apps import AppConfig
from . import BLOGAPP_APPS_LABEL

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '%s.blog' % BLOGAPP_APPS_LABEL
