from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets



class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializers_class = ProductSerializer

class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializers_class = OrderSerializer
