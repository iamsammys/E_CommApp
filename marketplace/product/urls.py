from django.urls import path, include
from rest_framework import routers
from .views import (
    ProductView,
    ProductCategoryView,
    ProductReviewView
)

router = routers.DefaultRouter()
router.register('product', ProductView, basename='product')
router.register('product-category', ProductCategoryView, basename='product-category')

urlpatterns = [
    path('', include(router.urls)),
    path('product/<str:product_id>/product-review/', ProductReviewView.as_view(
        {'get': 'list',
         'post': 'create',}),
         name='product-review'),
    path('product/<str:product_id>/product-review/<int:pk>/',
         ProductReviewView.as_view(
             {'get': 'retrieve',
              'put': 'update',
              'patch': 'partial_update',
              'delete': 'destroy'}),
              name='product-review-detail'),
]