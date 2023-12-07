#!/usr/bin/env python
"""
Module to create model classes for the order app

Created_by:
    Samuel Ezeh
"""

from django.db import models
from user.models import Address
from shared.basemodel import BaseModel
from django.contrib.auth.models import User
from product.models import Product


DELIVERY_STATUS = (
    ('PENDING', 'Pending'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Failed')
)

class Order(BaseModel):
    """
    Order model

    Attributes:
        user (User): User who created the order
        ship_to (Address): Shipping address
        delivery_status (str): Delivery status
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ship_to = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='shipping_address')
    delivery_status = models.CharField(max_length=10, choices=DELIVERY_STATUS, default='PENDING')


    def __str__(self) -> str:
        """
        String representation of the object
        
        Returns:
            str: String representation of the object    
        """
        return "[{}].{}".format(self.__class__.__name__, self.id)
    
    def total_price(self) -> float:
        """
        Calculate total price of the order

        Return:
            float: Total price
        """
        result = 0.0
        for item in self.order_items.all():
            result += item.total_price()
        return 
    
class OrderItem(BaseModel):
    """
    OrderItems model

    Attributes:
        order (Order): Order to which the item belongs
        product (Product): Product ordered
        quantity (int): Quantity of the product ordered
        price (float): Price of the product
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orders')
    quantity = models.IntegerField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False, default=0.0)

    def __str__(self) -> str:
        """
        String representation of the object
        
        Returns:
            str: String representation of the object
        """
        return "[{}] {}.{}".format(self.__class__.__name__, self.user.username, self.id)
    
    def total_price(self) -> float:
        """
        Calculate total price of the order item
        
        Returns:
            float: Total price
        """
        return self.price * self.quantity