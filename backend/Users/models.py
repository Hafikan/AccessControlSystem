from django.db import models
from django.contrib.auth.models import AbstractUser

def user_phpoto_path(instance, filename):
    """
    Generate the file path for user profi   le picture upload.
    """
    return f'profile_pictures/{instance.username}/{filename}'

class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """
    # Add any additional fields you want to include in your custom user model
    # For example:
    # bio = models.TextField(blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    role_choices = [
        ('admin', 'Admin'),
        ('Customer', 'Customer'),
        ('Director', 'Director'),

    ]
    first_name = models.CharField(max_length=30, blank=True, null=False, default='')
    last_name = models.CharField(max_length=30, blank=True, null=False, default='')
    is_active = models.BooleanField(default=True)   
    role = models.CharField(max_length=10, choices=role_choices, default='Customer')
    username = models.CharField(max_length=10, unique=True, blank=False, null=False)
    photo = models.ImageField(upload_to=user_phpoto_path, blank=True, null=False, default='profile_pictures/default.png')

    def __str__(self):
        return f' {self.first_name}, {self.last_name}, {self.username} '