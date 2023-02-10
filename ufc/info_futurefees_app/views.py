from django.shortcuts import render
from .serializer import PastFeesSerializer, FutureFeesSerializer
from .models import *
from rest_framework import viewsets


class FutureFeesViewset(viewsets.ModelViewSet):
    queryset = FutureFees.objects.all()
    serializers_class = FutureFeesSerializer

class PastFeesViewset(viewsets.ModelViewSet):
    queryset = PastFees.objects.all()
    serializers_class = PastFeesSerializer





