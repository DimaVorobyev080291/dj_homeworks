from django.db import models

class Sensor(models.Model):
    """
    Создаем таблицу Sensor (Датчик)
    """
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.title


class Measurement(models.Model):
    """
    Создаем таблицу Measurement (Измерение)
    """
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement', verbose_name='id датчика')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата первого замера')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата повторного замера')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'