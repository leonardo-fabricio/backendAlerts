from rest_framework import generics
from .serializer import * 
from rest_framework.response import Response


class AlertCreate(generics.CreateAPIView):
    serializer_class = AlertSerializer

class AlertList(generics.ListAPIView):
    serializer_class = AlertSerializer
    queryset= Alert.objects.all()