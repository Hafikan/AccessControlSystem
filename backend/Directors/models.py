from django.db import models
from Users.models import CustomUser

class Director(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    hire_date = models.DateField(null=False, blank=False)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.full_name} ({self.department})'
    
    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'
# Create your models here.
