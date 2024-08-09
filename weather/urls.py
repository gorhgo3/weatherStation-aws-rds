# weather/urls.py

from django.urls import path
from .views import WeatherRecordListCreate, WeatherRecordDetail, HumidityGeneric, HumidityDetail, WeatherStationApi

urlpatterns = [
    path('api/add/weather/', WeatherStationApi.as_view(), name='humidity-list'),
    path('api/humidity/<int:pk>/', HumidityDetail.as_view()),
    path('api/humidity/', HumidityGeneric.as_view()),
]