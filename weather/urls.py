# weather/urls.py

from django.urls import path
from .views import WeatherRecordListCreate, WeatherRecordDetail, HumidityGeneric, HumidityDetail

urlpatterns = [
    path('api/weather/', WeatherRecordListCreate.as_view(), name='weather-list-create'),
    path('api/humidity/', HumidityGeneric.as_view(), name='humidity-list'),
    path('api/humidity/<int:pk>/', HumidityDetail.as_view(), name='humidity-list'),
    path('api/weather/<int:pk>/', WeatherRecordDetail.as_view(), name='weather-detail'),
]
