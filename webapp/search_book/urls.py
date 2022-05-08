from django.urls import path
from webapp.search_book.views import IndexView, DetailView

# includeされたアプリ側の urls.py で指定するプロジェクトにおける名前空間:search_book
app_name = 'search_book'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<str:keyword>/<str:isbn>', DetailView.as_view(), name='detail'),
]
