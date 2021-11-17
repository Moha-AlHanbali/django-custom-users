from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'favorite_genre', 'favorite_band', 'favorite_song']
    fieldsets = UserAdmin.fieldsets + (
        ('personal_preferences', {'fields': ('favorite_genre', 'favorite_band', 'favorite_song')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)