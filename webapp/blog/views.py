from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from webapp.blog.models import Post
from . import BLOGAPP_URLS_LABEL

# ルーティングでblog/indexが指定された場合
class BlogView(ListView):
    template_name = "%s/post_list.html" % BLOGAPP_URLS_LABEL

    # models.pyで定義したmodelをセット
    model = Post

    # 更新日時でソート
    ordering = ['-updated']

    # paginationの設定
    paginate_by = 4

    # ログインユーザの情報表示
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["login_user"] = self.request.user
        return ctxt

# ルーティングでblog/detailが指定された場合
class PostDetailView(DetailView):
    template_name = "%s/post_detail.html" % BLOGAPP_URLS_LABEL

    # models.pyで定義したmodelをセット
    model = Post

# ルーティングでblog/createが指定された場合
# post新規作成画面
class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "%s/post_form.html" % BLOGAPP_URLS_LABEL

    # models.pyで定義したmodelをセット
    model = Post

    # 編集対象にするフィールド
    fields = ["title", "body", "category", "tags"]

    # viewの判別用変数
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["view_type"] = "create"
        return ctxt

    # ログインユーザを著者と設定
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# ルーティングでblog/updateが指定された場合
# post編集画面
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "%s/post_form.html" % BLOGAPP_URLS_LABEL

    # models.pyで定義したmodelをセット
    model = Post

    # 編集対象にするフィールド
    fields = ["title", "body", "category", "tags"]

    # viewの判別用変数
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["view_type"] = "update"
        return ctxt

    # 著者以外は編集できないようにする
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    # 著者以外のユーザは削除NG, 確認画面へ遷移する
    def handle_no_permission(self):
        '''to:[login,Profile] will signup or create profiles'''
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return render(self.request, template_name="%s/post_auth_rejection.html" % BLOGAPP_URLS_LABEL)

# ルーティングでblog/deleteが指定された場合
# post編集画面
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "%s/post_confirm_delete.html" % BLOGAPP_URLS_LABEL

    # models.pyで定義したmodelをセット
    model = Post

    # 削除後に移動する先
    success_url = "/%s"  % BLOGAPP_URLS_LABEL

    # ログインユーザ以外は削除できないようにする
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    # 著者以外のユーザは削除NG, 確認画面へ遷移する
    def handle_no_permission(self):
        '''to:[login,Profile] will signup or create profiles'''
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return render(self.request, template_name="%s/post_auth_rejection.html" % BLOGAPP_URLS_LABEL)
