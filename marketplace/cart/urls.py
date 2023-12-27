from django.urls import path, include
from rest_framework import routers
from .views import CartViewSet, CartItemViewSet

routers = routers.DefaultRouter()
routers.register('cart', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(routers.urls)),
    path('cart/<str:cart_id>/cart-item/', CartItemViewSet.as_view({'get': 'list',
                                                                   'post': 'create'}
                                                                   ), name='cart-item-list'),
    path('cart/<str:cart_id>/cart-item/<str:pk>/', CartItemViewSet.as_view({'get': 'retrieve',
                                                                            'put': 'update',
                                                                            'delete': 'destroy',
                                                                            'patch': 'partial-update'}),
                                                                            name='cart-item-detail'),
]