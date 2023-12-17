from django.urls import path, include
from rest_framework import routers
from .views import CartViewSet, CartItemViewSet

routers = routers.DefaultRouter()
routers.register('cart', CartViewSet, basename='cart')
routers.register('cart-item', CartItemViewSet, basename='cart-item')

urlpatterns = [
    path('', include(routers.urls))
]