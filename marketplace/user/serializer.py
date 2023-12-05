from rest_framework import serializers
from .models import UserProfile, Address

class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer
    """
    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        """
        Create method for ProfileSerializer
        """
        return UserProfile.objects.create(user=self.context.get('user'), **validated_data)
    
    def validate(self, data):
        """
        Validate method for ProfileSerializer
        """
        user_profile = UserProfile.objects.filter(user=self.context.get('user')).exists()
        if user_profile and request.POST:
            raise serializers.ValidationError("Profile already exists.")
        return data

class ReadAddressSerializer(serializers.ModelSerializer):
    """
    Address serializer
    """
    class Meta:
        model = Address
        fields = '__all__'

class WriteAddressSerializer(serializers.ModelSerializer):
    """
    Address serializer
    """
    class Meta:
        model = Address
        fields = ['user', 'house_no', ]
    def update(self, validated_data):
        """
        Update method for AddressSerializer
        """
        return Address.objects.update(user=self.context.get('user'), **validated_data)