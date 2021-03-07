from rest_framework import serializers
from .models import Boat

class Boat_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = '__all__'