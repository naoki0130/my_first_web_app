from unicodedata import name
from django.urls import path, include
from webapp.views import *

app_name = 'webapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', include('webapp.blog.urls', namespace='blog'), name='blog'),
]
