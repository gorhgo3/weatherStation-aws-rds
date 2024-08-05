# weather/views.py

from rest_framework import generics
from .models import WeatherRecord, HumidityRecord
from .serializers import WeatherRecordSerializer, HumiditySerializer

class WeatherRecordListCreate(generics.ListCreateAPIView):
    queryset = WeatherRecord.objects.all()
    serializer_class = WeatherRecordSerializer

class WeatherRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeatherRecord.objects.all()
    serializer_class = WeatherRecordSerializer


class HumidityGeneric(generics.ListCreateAPIView):
    queryset = HumidityRecord.objects.all()
    serializer_class = HumiditySerializer


class HumidityDetail(generics.RetrieveAPIView):
    queryset = HumidityRecord.objects.all()
    serializer_class = HumiditySerializer
    lookup_field = 'pk'