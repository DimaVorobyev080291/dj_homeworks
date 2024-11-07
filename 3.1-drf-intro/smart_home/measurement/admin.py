from django.contrib import admin
from .models import Sensor, Measurement

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    """    
    Админка модели Sensor
    """
    list_display = ['id', 'title', 'description']

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    """    
    Админка модели Measurement
    """
    list_display = ['id', 'sensor', 'temperature', 'created_at', 'updated_at']