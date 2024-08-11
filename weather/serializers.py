# weather/serializers.py

from rest_framework import serializers
from .models import WeatherRecord, HumidityRecord, TemperatureModel

class WeatherRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherRecord
        fields = '__all__'


class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = HumidityRecord
        fields = ["humidity", "recorded_at"]


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TemperatureModel
        fields = ["temperature", "recorded_at"]


class WindSpeedSerializer(serializers.ModelField):
    class Meta: 
        # model = 
        fields = "__all__"


class LuxSerializer(serializers.ModelField):
    class Meta: 
        # model = 
        fields = "__all__"
