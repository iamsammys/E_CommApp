from django.shortcuts import render
from rest_framework import viewsets
from .models import Profile
from .serializer import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    Profile viewset
    """
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """
        Get queryset for ProfileViewSet
        """
        return Profile.objects.filter(user=self.request.user)
    
    def get_serializer_context(self):
        """
        Get serializer context for ProfileViewSet
        """
        return {'user': self.request.user}