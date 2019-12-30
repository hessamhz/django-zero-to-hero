from django.forms import ModelForm, fields
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.password_validation import validate_password


class UserRegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), validators=[validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput(), validators=[validate_password])

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'confirm_password',
            'email'
        )

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )