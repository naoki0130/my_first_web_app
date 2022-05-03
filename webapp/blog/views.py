from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.blog.models import Post
from . import BLOGAPP_URLS_LABEL

# ルーティングでblog/indexが指定された場合
class BlogView(ListView):
    template_name = "%s/post_list.html" % BLOGAPP_URLS_LABEL

    # models.pyで定義したmodelをセット
    model = Post

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

# ルーティングでblog/updateが指定された場合
# post編集画面
class PostUpdateView(UpdateView):
    template_name = "%s/post_form.html" % BLOGAPP_URLS_LABEL

    # models.pyで定義したmodelをセット
    model = Post

    # 編集対象にするフィールド
    fields = ["title", "body", "category", "tags"]

# ルーティングでblog/deleteが指定された場合
# post編集画面
class PostDeleteView(DeleteView):
    template_name = "%s/post_confirm_delete.html" % BLOGAPP_URLS_LABEL

    # models.pyで定義したmodelをセット
    model = Post

    # 削除後に移動する先
    success_url = "/"
