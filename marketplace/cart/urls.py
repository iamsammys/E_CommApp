from django.urls import path, include
from rest_framework import routers
from .views import CartViewSet, CartItemViewSet

routers = routers.DefaultRouter()
routers.register('cart', CartViewSet)
routers.register('cart-item', CartItemViewSet)

urlpatterns = [
    path('', include(routers.urls))
]