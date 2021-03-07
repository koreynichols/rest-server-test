from rest_framework import viewsets
from .serializers import Truck_Serializer
from .models import Truck
# Create your views here.

class Truck_Viewset(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = Truck_Serializer