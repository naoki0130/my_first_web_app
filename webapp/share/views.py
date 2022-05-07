from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
)
from webapp.share.forms import ImageUploadForm, VideoUploadForm
from webapp.share.models import ImageModel, VideoModel
from . import SHAREAPP_URLS_LABEL

# ルーティングでshare/index_imgが指定された場合
class ShareImageView(LoginRequiredMixin, ListView):
    template_name = "%s/index_img.html" % SHAREAPP_URLS_LABEL

    model = ImageModel

    # 投稿日時でソート
    ordering = ['-uploaded']

# ルーティングでshare/upload_imgが指定された場合
class ShareImageUploadView(LoginRequiredMixin, CreateView):
    template_name = "%s/upload_img.html" % SHAREAPP_URLS_LABEL

    form_class = ImageUploadForm

    # ログインユーザを投稿者と設定
    def form_valid(self, form):
        form.instance.uploaded_user = self.request.user
        return super().form_valid(form)

# ルーティングでshare/index_movが指定された場合
class ShareMovieView(LoginRequiredMixin, ListView):
    template_name = "%s/index_mov.html" % SHAREAPP_URLS_LABEL

    model = VideoModel

    # 投稿日時でソート
    ordering = ['-uploaded']

# ルーティングでshare/upload_movが指定された場合
class ShareMovieUploadView(LoginRequiredMixin, CreateView):
    template_name = "%s/upload_mov.html" % SHAREAPP_URLS_LABEL

    form_class = VideoUploadForm

    # ログインユーザを投稿者と設定
    def form_valid(self, form):
        form.instance.uploaded_user = self.request.user
        return super().form_valid(form)