from django.views.generic import TemplateView
from . import BLOGAPP_URLS_LABEL

# ルーティングでblog/blogpageが指定された場合
class BlogView(TemplateView):
    template_name = "%s/blog.html" % BLOGAPP_URLS_LABEL