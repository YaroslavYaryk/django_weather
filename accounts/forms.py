from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class   RegisterUserForm(UserCreationForm):
    """ Registrating form class """

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"}))

    class Meta:
        model = User

        fields = ("username",
                  "email", "password1", "password2",)
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Username'}),
            "email": forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Email'}),
        }


class LoginUserForm(AuthenticationForm):
    """ Login form class """

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))

    class Meta:
        model = User

        fields = ("username", "password",)
