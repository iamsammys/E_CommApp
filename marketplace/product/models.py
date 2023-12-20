from django.db import models
from shared.basemodel import BaseModel
from django.contrib.auth.models import User


class ProductCategory(BaseModel):
    """
    Product category models class
    """
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)
    
class Product(BaseModel):
    """
    Product models class

    Attributes:
        name: Product name
        description: Product description
        quantity: Product quantity
        price: Product price
        image: Product image
        category: Product category
    """
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return "{}".format(self.name)
    
class ProductReview(BaseModel):
    """
    Product review models class
    
    Attributes:
        product: Product
        user: User
        rating: Rating
        review: Review
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(default=0)
    review = models.TextField(blank=True, null=True, help_text="Enter your review about the product here")

    def __str__(self):
        return "{}".format(self.user.name)