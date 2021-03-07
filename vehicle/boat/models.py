from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    hin = models.CharField(max_length=50)
    current_hours = models.IntegerField()
    service_interval = models.IntegerField()
    next_service = models.DateField()