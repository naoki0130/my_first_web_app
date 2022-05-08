import imp
from django.views.generic import TemplateView

from webapp.search_book.views import API_ID
from . import WEBAPP_LABEL
from config import settings
import requests
import json

API_ID = settings.WEATHER_API_KEY
SEARCH_URL = "https://api.openweathermap.org/data/2.5/weather?q=tokyo&units=metric&lang=ja&appid=" + API_ID

# 天気API
def getWeather():
    api = requests.get(SEARCH_URL).text
    result = json.loads(api)
    city_weather = {
        "city": result["name"],
        "temperature_now": result["main"]["temp"],
        "temperature_max": result["main"]["temp_max"],
        "temperature_min": result["main"]["temp_min"],
        "description": result["weather"][0]["description"],
        "icon": result["weather"][0]["icon"],
    }
    return city_weather

# ルーティングでindexが指定された場合
class IndexView(TemplateView):
    template_name = "%s/index.html" % WEBAPP_LABEL

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["user_name"] = self.request.user
        ctxt["weather_dic"] = getWeather()
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
