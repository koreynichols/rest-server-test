from rest_framework import viewsets
from .serializers import Car_Serializer
from .models import Car
# Create your views here.

class Car_Viewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = Car_Serializer