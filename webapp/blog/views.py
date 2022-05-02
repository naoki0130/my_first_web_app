from django.views.generic import TemplateView
from . import BLOGAPP_URLS_LABEL

class BlogView(TemplateView):
    template_name = "%s/blog.html" % BLOGAPP_URLS_LABEL
    print(template_name)