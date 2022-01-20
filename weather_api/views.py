from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny
)
from weather.services.generate_weather import get_weather_by_city


class WeatherForCityAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, city):
        result = get_weather_by_city(city)[1]
        return Response(result)

class WeatherForCitySpecDayAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, city, day):
        result = get_weather_by_city(city)[1].get(int(day))
        return Response(result)

