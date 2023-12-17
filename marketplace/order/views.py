from django.shortcuts import render
from rest_framework import viewsets
from .models import Order, OrderItem
from .serializer import (
    ReadOrderSserializer, 
    ReadOrderItemSerializer
)

class OrderViewSet(viewsets.ModelViewSet):
    pass