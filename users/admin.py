from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    exclude = ('date_joined', 'username', )
    fieldsets = (
        ('Login info', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
            'phone_number',
        )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        ('Login info', {'fields': ('email', 'password1', 'password2')}),
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
            'phone_number'
        )})
    )
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(CustomUser, CustomUserAdmin)
