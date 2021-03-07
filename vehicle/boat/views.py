from rest_framework import viewsets
from .serializers import Boat_Serializer
from .models import Boat
from rest_framework.permissions import IsAuthenticated

class Boat_Viewset(viewsets.ModelViewSet):
    queryset = Boat.objects.all()
    serializer_class = Boat_Serializer
        permission_classes = (IsAuthenticated, )