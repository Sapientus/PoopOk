import re

from django import forms
from django.contrib.auth import get_user_model


class ValidationMixin:
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Ця електронна пошта вже використовується.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError("Тільки цифри.")
        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(phone_number):
            raise forms.ValidationError("Формат номера не коректний.")
        return phone_number
