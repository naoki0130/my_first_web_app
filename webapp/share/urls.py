from django.urls import path
from .views import (
    ShareImageView,
    ShareImageUploadView,
    ShareMovieView,
    ShareMovieUploadView
)

# includeされたアプリ側の urls.py で指定するプロジェクトにおける名前空間:share
app_name = 'share'
urlpatterns = [
    path('image/', ShareImageView.as_view(), name='index_img'),
    path('upload_img/', ShareImageUploadView.as_view(), name='upload_img'),
    path('movie/', ShareMovieView.as_view(), name='index_mov'),
    path('upload_mov/', ShareMovieUploadView.as_view(), name='upload_mov'),
]