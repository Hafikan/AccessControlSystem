from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from Directors.models import Director
from Customers.models import Customer

User = get_user_model()
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a profile for the user when a new user is created.
    """
    if created:
        if instance.role == 'Director':
            Director.objects.create(user=instance)
        elif instance.role == 'Customer':
            Customer.objects.create(user=instance,)