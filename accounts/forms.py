from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ElmusicUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = ElmusicUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = ElmusicUser
        fields = ('username', 'email')
