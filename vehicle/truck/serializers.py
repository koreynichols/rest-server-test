from rest_framework import serializers
from .models import Truck

class Truck_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'