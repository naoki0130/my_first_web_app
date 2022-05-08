from django.apps import AppConfig
from . import SEARCH_BOOKAPP_APPS_LABEL

class SearchBookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '%s.search_book' % SEARCH_BOOKAPP_APPS_LABEL
