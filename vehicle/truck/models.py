from django.db import models

# Create your models here.
class Truck(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    seats = models.IntegerField()
    bed_length = models.IntegerField()
    color = models.CharField(max_length=50)
    vin = models.CharField(max_length=50)
    current_mileage = models.IntegerField()
    service_interval = models.IntegerField()
    next_service = models.DateField()