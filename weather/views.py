from decouple import config
from django.views.generic.base import TemplateView
from time import localtime, time
from django.shortcuts import redirect, render
import requests
from .services.generate_weather import get_weather_by_city


# Create your views here.

class Home(TemplateView):
    template_name = "weather/home_page.html"

    def get_context_data(self, **kwargs):
        context = {"title": "Home Page", "api_key": config("API_Key")}
        return context


def get_weather_from_search_bar(request):
    city = request.POST["search"]
    return redirect("city_weather", city_name=city)


def get_weather_for_city(request, city_name):
    location = city_name
    days = get_weather_by_city(location)[0]
    context = {
        "days": days,
        "title": location
    }

    return render(request, "weather/forecast.html", context=context)


def get_weather_for_city_specific_date(request, city_name, day):
    location = city_name
    weather = get_weather_by_city(location)[1].get(int(day))
    context = {
        "title": location,
        "weather": weather
    }

    return render(request, "weather/forecast_by_spec_day.html", context=context)
