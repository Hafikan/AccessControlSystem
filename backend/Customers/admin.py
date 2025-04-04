from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'membership_type', 'member_since')
    search_fields = ('full_name', 'email', 'phone_number')
    list_filter = ('membership_type', )
    ordering = ('member_since',)
    
admin.site.register(Customer, CustomerAdmin)