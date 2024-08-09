# weather/views.py

from rest_framework import generics
from .models import WeatherRecord, HumidityRecord
from .serializers import WeatherRecordSerializer, HumiditySerializer
from rest_framework import generics, status
from rest_framework.response import Response


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


class WeatherStationApi(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
      reqData = request.data
      serializerErrors = []

      if 'humidity' in reqData:
          serializer = HumiditySerializer(data={'humidity':reqData['humidity']})
          if serializer.is_valid():
              serializer.save()
          else:
              serializerErrors.append(serializer.errors)

      """
      if 'temperature' in reqData:
          serializer = TemperatureSerializer(data={'temperature':reqData['temperature']})
          if serializer.is_valid():
              serializer.save()
          else:
              serializerErrors.append(serializer.errors)
      
      if 'lux' in reqData:
          serializer = LuxSerializer(data={'lux':reqData['lux']})
          if serializer.is_valid():
              serializer.save()
          else:
              serializerErrors.append(serializer.errors)
      """
      
      if len(serializerErrors) != 0:
        return Response(serializerErrors, status=status.HTTP_400_BAD_REQUEST)
      else:         
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
