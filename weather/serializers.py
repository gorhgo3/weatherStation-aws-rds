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
class TemperatureSerializer(serializers.ModelField):
    class Meta: 
        # model = 
        fields = "__all__"

class WindSpeedSerializer(serializers.ModelField):
    class Meta: 
        # model = 
        fields = "__all__"
        
class LuxSerializer(serializers.ModelField):
    class Meta: 
        # model = 
        fields = "__all__"
