from django.db import models
from django.contrib.auth.models import User
from shared.basemodel import BaseModel


class UserProfile(BaseModel):
    """
    UserProfile model
    """
    user = model.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    phone = models.PhoneNumberField(blank=True)

    def __str__(self):
        """
        String representation of UserProfile model

        Returns:
            str: String representation of UserProfile model
        """
        return "[{}] {}.{}".format(self.__class__.__name__, self.user.username, self.id)

class Address(BaseModel):
    """
    Address model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house_no = models.CharField(max_length=255, blank=True null=True)
    street = models.CharField(max_length=255, blank=True null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    country = models.CountryField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        """
        String representation of Address model

        Returns:
            str: String representation of Address model
        """
        return "[{}] {}.{}".format(self.__class__.__name__, self.user.username, self.id)