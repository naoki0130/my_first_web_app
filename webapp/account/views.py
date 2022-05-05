from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from . import ACCOUNTAPP_URLS_LABEL

# ルーティングでblog/indexが指定された場合
class AccountView(ListView):
    template_name = "%s/post_list.html" % ACCOUNTAPP_URLS_LABEL

