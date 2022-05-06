from django.views.generic import TemplateView
from . import WEBAPP_LABEL

# ルーティングでindexが指定された場合
class IndexView(TemplateView):
    template_name = "%s/index.html" % WEBAPP_LABEL

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["user_name"] = self.request.user
        return ctxt

# ルーティングでaboutが指定された場合
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
