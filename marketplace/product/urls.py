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
router.register('product-review', ProductReviewView, basename='product-review')

urlpatterns = [
    path('', include(router.urls)),
]