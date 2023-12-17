#!/usr/bin/env python
"""
Module for the serializer class for the order app

Created_by:
    Samuel Ezeh
"""
from rest_framework import serializers
from .models import (
    Order,
    OrderItem
)
from rest_framework.relations import StringRelatedField
from django.db import transaction
from user.serializer import ReadAddressSerializer
from cart.models import Cart
from user.models import Address

class ReadOrderItemSerializer(serializers.ModelSerializer):
    """
    Order serializer
    """
    total_price = serializers.SerializerMethodField(
        method_name='get_total_price',
        read_only=True,
        required=False
    )

    def get_total_price(self, obj: OrderItem) -> float:
        """
        Get total price of order item
        """
        return obj.total_price()

    class Meta:
        model = OrderItem
        fields = ['id',
                  'product',
                  'quantity',
                  'total_price',
                  'price',
                  ]

class ReadOrderSserializer(serializers.ModelSerializer):
    """
    Order serializer
    
    Attributes:
        user (User): User who created the order
        ship_to (Address): Shipping address
        delivery_status (str): Delivery status
    """
    total_price = serializers.SerializerMethodField(
        method_name='get_total_price',
        required=False
    )
    class Meta:
        """
        Meta class for the serializer
        """
        models = Order
        fields = [
            'id',
            'user',
            'ship_to',
            'delivery_status',
            'cart',
            'created_at',
            'updated_at',
            'cart',
            'order_items',
            'total_price'
        ]
        cart = StringRelatedField()
        order_items = ReadOrderItemSerializer(many=True)
        ship_to = ReadAddressSerializer()
        user = StringRelatedField()

    def get_total_price(self, obj: Order) -> float:
        """
        Instance method that returns the total order price

        Parameters:
            obj(Order): instance of Order class

        Returns:
            float: The total price of the order
        """
        return obj.total_price
    
class WriteOrderSerializer(serializers.Serializer):
    """
    Order serializer
    
    Attributes:
        user (User): User who created the order
        ship_to (Address): Shipping address
        delivery_status (str): Delivery status
    """
    def validate(self, data):
        """
        Validate method for OrderSerializer
        """
        cart = cart.objects.filter(pk=data.get('cart'), user=self.context.get('user'))
        if not cart.exists():
            raise serializers.ValidationError("Cart is required.")

        if cart.first().items.count() < 1:
            raise serializers.ValidationError("Cart is empty.")

        return data
    
    def __init__(self, *args, **kwargs):
        """
        Constructor for OrderSerializer
        """
        super().__init__(*args, **kwargs)
        self.fields['ship_to'].queryset = Address.objects.filter(user=self.context.get('user'))
        self.fields['cart'].queryset = Cart.objects.filter(user=self.context.get('user'))

    def save(self, **kwargs):
        """
        Save method for OrderSerializer
        """
        user = self.context.get('user')
        cart_main = Cart.objects.filter(user=user)

        with transaction.atomic():
            order = Order.objects.create(
            user=user
            ship_to=self.validated_data.get('ship_to'),
            cart=self.validated_data.get('cart'),
            delivery_status=validated_data.get('delivery_status')
            )
            cart_items = CartItems.object.filter(user=self.context.get('user'),
                                                 pk=request.user.cart.id)
            order_items = [
                OrderItem(
                    order=order,
                    price=cart_item.product.price,
                    product=cart_item.product,
                    quantity=cart_item.quantity
                )
                for cart_item in cart_items
                ]
            
            for item in cart_items:
                product = Product.objects.get(pk=item.product.id)
                if product.quantity < item.quantity:
                    raise serializers.ValidationError(
                        {
                        'error': "your for this product {} order is more than\
                        the available quantity".format(product.name)
                        }
                        )
                product.quantity -= item.quantity
                product.save()
            OrderItem.objects.bulk_create(order_items)
            cart_main.delete()