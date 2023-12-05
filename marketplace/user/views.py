from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile, Address
from .serializer import ProfileSerializer, WriteAddressSerializer, ReadAddressSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    Profile viewset
    """
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """
        Get queryset for ProfileViewSet
        """
        return UserProfile.objects.filter(user=self.request.user)
    
    def get_serializer_context(self):
        """
        Get serializer context for ProfileViewSet
        """
        return {'user': self.request.user}
    
class AddressViewSet(viewsets.ModelViewSet):
    """
    Address viewset
    """
    def get_queryset(self):
        """
        Get queryset for AddressViewSet
        """
        return Address.objects.filter(user=self.request.user)
    
    def get_serializer_context(self):
        """
        Get serializer context for AddressViewSet
        """
        return {'user': self.request.user}
    
    def get_serializer_class(self):
        """
        Get serializer class for AddressViewSet
        """
        if self.request.method == 'POST':
            return WriteAddressSerializer
        return ReadAddressSerializer