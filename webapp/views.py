import imp
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["user_name"] = "N.O"
        return ctxt


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_services"] = 123456789
        ctxt["skills"] = [
            "Python",
            "Java",
            "JavaSctipt",
            "SQL",
        ]
        return ctxt

class BlogView(TemplateView):
    template_name = "blog.html"
