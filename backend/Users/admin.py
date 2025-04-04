# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import CustomUser
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'photo','first_name', 'last_name', 'email', 'is_active', 'role')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_active', 'role')
    ordering = ('username',)
    fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'email','photo')
        }),
        ('Permissions', {
            'fields': ('is_active', 'role')
        }),
    )
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)