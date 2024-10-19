import re
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from django.contrib.auth import get_user_model

from users.mixins.model_mixins import ValidationMixin


class UserRegistrationForm(forms.ModelForm, ValidationMixin):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email', 'phone_number']

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError("Passwords don't match.")
    #     return cd['password2']
    #
    # def clean_phone_number(self):
    #     data = self.cleaned_data['phone_number']
    #     if not data.isdigit():
    #         raise forms.ValidationError("Тільки цифри")
    #     pattern = re.compile(r'^\d{10}$')
    #     if not pattern.match(data):
    #         raise forms.ValidationError("Формат номера не коректний")
    #
    #     return data


class ProfileForm(forms.ModelForm, ValidationMixin):
    class Meta:
        model = get_user_model()
        fields = [
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
            "phone_number",
        ]

    # def clean_email(self):
    #     data = self.cleaned_data['email']
    #     qs = get_user_model().objects.exclude(
    #         id=self.instance.id
    #     ).filter(
    #         email=data
    #     )
    #     if qs.exists():
    #         raise forms.ValidationError('Email already in use.')
    #     return data
