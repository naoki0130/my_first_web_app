from django.urls import path
from .views import BlogView

# includeされたアプリ側の urls.py で指定するプロジェクトにおける名前空間:blog
app_name = 'blog'
urlpatterns = [
    path('blogpage/', BlogView.as_view(), name='blogpage'),
]