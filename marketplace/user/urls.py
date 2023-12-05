from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, AddressViewSet

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'address', AddressViewSet, basename='address')

urlpatterns = router.urls