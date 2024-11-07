from rest_framework import serializers
from measurement.models import Measurement, Sensor

class MeasurementSerializer(serializers.ModelSerializer):
    """
    Serializer таблице Measurement для представления MeasurementCreateView
    """
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at', 'updated_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    """
    Serializer таблице Sensor для представлений SensorsListCreateView, SensorView
    """
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'title', 'description', 'measurements']


class SensorChangeSerializer(serializers.ModelSerializer):
    """
    Serializer таблице Sensor для представления SensorChangeView
    """
    class Meta:
        model = Sensor
        fields = ['id', 'title', 'description']