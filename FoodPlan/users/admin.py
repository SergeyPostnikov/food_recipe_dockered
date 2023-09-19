from django.contrib import admin
from .models import SiteUser


@admin.register(SiteUser)
class UserAdmin(admin.ModelAdmin):
    exclude = (
        'last_login', 
        'groups', 
        'user_permissions',
        'date_joined',
        'first_name',
        'last_name',
        'email',
        'is_superuser',
        'is_active',
        'is_staff'
    )
