from rest_framework import serializers
from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    """
    Order serializer
    """
    class Meta:
        model = Order
        fields = '__all__'

    def validate(self, data):
        """
        Validate method for OrderSerializer                                                                                                                                 
        """
        user = data.get('user')

    def create(self, validated_data):
        """
        Create method for OrderSerializer
        """
        return Order.objects.create(user=context.get('user') **validated_data)