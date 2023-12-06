from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from user.models import UserProfile, Address


@receiver(post_save, sender=User)
def create_user_profile_and_address(sender, instance, created, **kwargs):
    """
    Create user profile and address when user is created.
    """
    if created:
        UserProfile.objects.create(user=instance)
        Address.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile_and_address(sender, created, instance, **kwargs):
    """
    Save user profile and address when user is saved.
    """
    if created:
        instance.userprofile.save()
        instance.address.save()