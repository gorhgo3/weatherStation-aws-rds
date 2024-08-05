# weather/serializers.py

from rest_framework import serializers
from .models import WeatherRecord, HumidityRecord

class WeatherRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherRecord
        fields = '__all__'


class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = HumidityRecord
        fields = "__all__"