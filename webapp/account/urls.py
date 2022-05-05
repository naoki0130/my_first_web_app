from django.urls import path
from .views import (
    AccountView, 
)

# includeされたアプリ側の urls.py で指定するプロジェクトにおける名前空間:blog
app_name = 'account'
urlpatterns = [
    path('', AccountView.as_view(), name='index'),
]