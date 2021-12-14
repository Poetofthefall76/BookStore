from django.contrib.auth import forms
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import models


class RegistrationForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]


class LoginForm(AuthenticationForm):
        fields = [
            "username",
            "password",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-input", "placeholder": "Username"}),
            "password": forms.PasswordInput(attrs={"class": "form-input", "placeholder": "Password"})
        }



