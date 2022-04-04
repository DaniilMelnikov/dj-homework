from tkinter import CASCADE
from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название')
    description = models.CharField(max_length=200, verbose_name='Описание')

class Measurement(models.Model):
    id_sensor = models.ManyToManyField(Sensor, related_name='measurements')
    temperature = models.IntegerField()
    data = models.DateField(auto_now=True)