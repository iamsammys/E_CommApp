from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from shared.basemodel import BaseModel


class Cart(BaseModel):
    """
    Cart model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "[{}] {}.{}".format(self.__class__, self.user.name, self.id)
    
    def get_total_price(self) -> int:
        """
        Get total price of cart

        Returns:
            int: total price of cart
        """
        total_price = 0
        for cart_item in self.cart_items.all():
            total_price += (cart_item.product.price * cart_item.quantity)
        return total_price

class CartItem(BaseModel):
    """
    CartItem model
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        """
        Meta class
        """
        unique_together = ('cart', 'product')

    def __str__(self) -> str:
        """
        String representation of CartItem
        
        Returns:
            str: CartItem string representation
        """
        return "[{}] {}.{}".format(self.__class__.__name__, self.cart.id, self.product.id)
    
    def get_item_unit_price(self) -> int:
        """
        Get unit price of item

        Returns:
            int: unit price of item
        """
        return self.product.price
    
    def get_item_total_price(self) -> int:
        """
        Get total price of item

        Returns:
            int: total price of item
        """
        return self.product.price * self.quantity