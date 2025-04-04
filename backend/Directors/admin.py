from django.contrib import admin
from .models import Director

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'hire_date', 'department')
    search_fields = ('full_name', 'email', 'phone_number', 'department')
    actions = ['make_active', 'make_inactive']
    list_per_page = 20
    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = "Mark selected directors as active"
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = "Mark selected directors as inactive"
# Register your models here.
admin.site.register(Director, DirectorAdmin)