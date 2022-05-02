from django.urls import path
from .views import BlogView

app_name = 'blog'
urlpatterns = [
    path('blogpage/', BlogView.as_view(), name='blogpage'),
]