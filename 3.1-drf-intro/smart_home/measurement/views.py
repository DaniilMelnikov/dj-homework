# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer
from django.shortcuts import get_object_or_404

class MultipleFieldLookupMixin:
    def get_object(self):
        queryset = self.get_queryset()           
        queryset = self.filter_queryset(queryset) 
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: 
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter) 
        self.check_object_permissions(self.request, obj)
        return obj

class SensorAdd(generics.CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class SensorUpdate_name(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_fields = 'name'

class SensorUpdate_description(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_fields = 'description'

class SensorUpdate(MultipleFieldLookupMixin, generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_fields = ['name', 'description']

class MeasurementAdd(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class SensorViewShort(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class SensorView(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer



