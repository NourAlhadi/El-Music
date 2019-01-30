from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import ElmusicUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = ElmusicUser
    list_display = ['username', 'email', 'is_superuser', 'is_staff']


admin.site.register(ElmusicUser, CustomUserAdmin)

