from django.views.generic import TemplateView
from . import BLOGAPP_LABEL

class BlogView(TemplateView):
    template_name = "%s/blog.html" % BLOGAPP_LABEL
    print(template_name)