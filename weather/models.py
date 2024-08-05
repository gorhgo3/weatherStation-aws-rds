from django.db import models

class WeatherRecord(models.Model):
    recorded_at = models.DateTimeField(auto_now_add=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.recorded_at} - Temp: {self.temperature}°C, Humidity: {self.humidity}%"

class HumidityRecord(models.Model):
    recorded_at = models.DateTimeField(auto_now_add=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.recorded_at}, Humidity: {self.humidity}"