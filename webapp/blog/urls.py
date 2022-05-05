from django.urls import path
from .views import (
    BlogView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView
)

# includeされたアプリ側の urls.py で指定するプロジェクトにおける名前空間:blog
app_name = 'blog'
urlpatterns = [
    path('', BlogView.as_view(), name='index'),
    path('detail/<pk>/', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('update/<pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<pk>', PostDeleteView.as_view(), name='delete'),
]