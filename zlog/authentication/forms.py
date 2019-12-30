from django.forms import ModelForm, fields
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'email'
        )