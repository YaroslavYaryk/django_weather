from decouple import config
from django.views.generic.base import View
from django.shortcuts import redirect, render
from .services.generate_weather import get_weather_by_city, start_page_or_redirect
from django.contrib import  messages

# Create your views here.

class Home(View):
    template_name = "weather/home_page.html"

    def get(self, request):
        context = {"title": "Home Page", "api_key": config("API_Key")}

        # del request.session["city"]
        if start_page_or_redirect(request):
            return start_page_or_redirect(self.request)
        return render(request, template_name="weather/home_page.html", context=context)



def get_weather_from_search_bar(request):
    city = request.POST["search"]
    if not city:
        messages.add_message(request, 40, "empty input")
        return redirect("home")
    request.session["city"] = city
    return redirect("city_weather", city_name=city)


def get_weather_for_city(request, city_name):
    location = city_name
    try:
        days = get_weather_by_city(location)[0]
    except KeyError: #when city is not found
        messages.add_message(request, 40, "there is no this city")
        del request.session["city"]
        return redirect("home")
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
