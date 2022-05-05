from operator import is_
from django.urls import reverse_lazy
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

    # 取得データのハンドリング
    # def get_queryset(self):
    #     return Post.objects.order_by('-updated')

# ルーティングでblog/detailが指定された場合
class PostDetailView(DetailView):
    template_name = "%s/post_detail.html" % BLOGAPP_URLS_LABEL

    # models.pyで定義したmodelをセット
    model = Post

# ルーティングでblog/createが指定された場合
# post新規作成画面
class PostCreateView(CreateView):
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
class PostUpdateView(UpdateView):
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

    # ログインユーザを著者と設定
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # ログインユーザ以外は編集できないようにする
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# ルーティングでblog/deleteが指定された場合
# post編集画面
class PostDeleteView(DeleteView):
    template_name = "%s/post_confirm_delete.html" % BLOGAPP_URLS_LABEL

    # models.pyで定義したmodelをセット
    model = Post

    # 削除後に移動する先
    success_url = "/%s"  % BLOGAPP_URLS_LABEL
