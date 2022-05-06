from django.urls import path
from .views import (
    SignUpView, 
) 
from django.contrib.auth import views as auth_views
from . import ACCOUNTAPP_URLS_LABEL

# includeされたアプリ側の urls.py で指定するプロジェクトにおける名前空間:blog
app_name = 'account'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="%s/login.html" % ACCOUNTAPP_URLS_LABEL), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="%s/logout.html" % ACCOUNTAPP_URLS_LABEL), name='logout'),
]