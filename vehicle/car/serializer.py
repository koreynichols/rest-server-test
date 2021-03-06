from rest_framework import serializers
from .models import Car

class Car_Serializer(serializer.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'