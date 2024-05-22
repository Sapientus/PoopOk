# stars/forms.py
from django import forms
from .models import Action

class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['target', 'action_type']
