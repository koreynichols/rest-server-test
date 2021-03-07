from rest_framework import viewsets
from .serializers import Boat_Serializer
from .models import Boat
# Create your views here.

class Boat_Viewset(viewsets.ModelViewSet):
    queryset = Boat.objects.all()
    serializer_class = Boat_Serializer