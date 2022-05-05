from unicodedata import name
from django.urls import path, include
from webapp.views import *

# includeされたアプリ側の urls.py で指定するプロジェクトにおける名前空間:webapp
app_name = 'webapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', include('webapp.blog.urls', namespace='blog'), name='blog'),
    path('account/', include('webapp.account.urls', namespace='account'), name='account'),
]
