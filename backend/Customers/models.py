from django.db import models
from Users.models import CustomUser

class Customer(models.Model):
    membership_type_choices = [
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('vip', 'VIP'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    member_since = models.DateField(null=True, blank=True)
    member_end = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    membership_type = models.CharField(max_length=10, choices=membership_type_choices, default='basic')

    def __str__(self):
        return f'{self.full_name} ({self.membership_type})'
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


# Create your models here.
