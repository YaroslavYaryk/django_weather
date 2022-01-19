from django.urls import path
from .views import Home, get_weather_for_city, get_weather_from_search_bar, get_weather_for_city_specific_date

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("city/<city_name>/", get_weather_for_city, name="city_weather"),
    path("city/<city_name>/<day>/", get_weather_for_city_specific_date, name="city_weather_spec_date"),
    path("get_city_search", get_weather_from_search_bar, name="get_city"),
]
