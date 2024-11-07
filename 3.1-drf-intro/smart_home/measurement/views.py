from rest_framework import status
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, ListCreateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorChangeSerializer


class SensorsListCreateView(ListCreateAPIView):
    """
    Добавляет новый датчик, получаем список датчиков
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(ListCreateAPIView):
    """
    Добавляет новое измерение, получаем список измерений
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorChangeView(UpdateAPIView):
    """
    Обновляем информацию по конкретному датчику
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorChangeSerializer


class SensorView(RetrieveAPIView):
    """
    Получаем информацию по конкретному датчику
    """
    queryset = Sensor.objects.all().prefetch_related('measurement')
    serializer_class = SensorDetailSerializer