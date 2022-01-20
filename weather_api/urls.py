from django.urls import path
from .views import WeatherForCityAPIView, WeatherForCitySpecDayAPIView

urlpatterns = [
    path("city/<city>/", WeatherForCityAPIView.as_view(), name="city_weather"),
    path("city/<city>/<day>/", WeatherForCitySpecDayAPIView.as_view(), name="city_weather_spec_date"),
]