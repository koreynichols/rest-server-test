from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField()
    model = models.CharField()
    year = models.IntegerField()
    seats = models.IntegerField()
    color = models.CharField()
    vin = models.CharField()
    current_mileage = models.IntegerField()
    service_interval = models.IntegerField()
    next_service = models.DateField()