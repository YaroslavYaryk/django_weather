from decouple import config
from time import localtime, time
import requests
import datetime
from calendar import monthrange
from django.shortcuts import redirect

today_day = localtime(time()).tm_mday
today_month = localtime(time()).tm_mon
today_year = localtime(time()).tm_year


def day_adding_according_to_data(day):
    if day < monthrange(today_year, today_month)[1]:
        return day
    return day % monthrange(today_year, today_month)[1]

def get_weather_by_city(location):
    weather_url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid="
    final_url = weather_url + config("API_Key")
    weather_data = requests.get(final_url).json()
    day1 = []
    day2 = []
    day3 = []
    day4 = []
    day5 = []
    day6 = []

    storage = {
        day_adding_according_to_data(today_day): day1,
        day_adding_according_to_data(today_day + 1): day2,
        day_adding_according_to_data(today_day + 2): day3,
        day_adding_according_to_data(today_day + 3): day4,
        day_adding_according_to_data(today_day + 4): day5,
        day_adding_according_to_data(today_day + 5): day6,
    }

    for elem in weather_data["list"]:
        date = localtime(elem["dt"])
        dictionary = {
            "year": date.tm_year,
            "month": datetime.date(date.tm_year, date.tm_mon, date.tm_mday).strftime('%B'),
            "day": date.tm_mday,
            "hour": date.tm_hour,
            "minute": date.tm_min
        }
        elem["date_time"] = dictionary
        elem["ico"] = elem["weather"][0]["icon"]
        storage[localtime(elem["dt"]).tm_mday].append(elem)
    days = [day1, day2, day3, day4, day5, day6]

    return days, storage


def start_page_or_redirect(request):
    if request.session.get("city"):
        return redirect("city_weather", request.session.get("city"))