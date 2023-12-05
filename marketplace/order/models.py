from django.db import models
from shared.basemodel import BaseModel
from django.contrib.auth.models import User


class Order(BaseModel):
    """
    Order model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "[{}].{}".format(self.__class__.__name__, self.id)
    
class OrderItem(BaseModel):
    """
    OrderItems model
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)

    def __str__(self) -> str:
        return "[{}] {}.{}".format(self.__class__.__name__, self.user.username, self.id)