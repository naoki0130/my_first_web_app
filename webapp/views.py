from django.views.generic import TemplateView
from . import WEBAPP_LABEL

class IndexView(TemplateView):
    template_name = "%s/index.html" % WEBAPP_LABEL

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["user_name"] = "N.O"
        return ctxt


class AboutView(TemplateView):
    template_name = "%s/about.html" % WEBAPP_LABEL

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
